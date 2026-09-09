#!/usr/bin/env python3
"""Avaliação do Benchmark Holdout Expandido (100 Perguntas Inéditas)
com o Two-Stage Pipeline definitivo em CPU Pura:
Estágio 1: BM25 + Anthropic Contextual Retrieval Prefix + Ontologia Bilíngue
Estágio 2: Micro-Reranker Neural BAAI/bge-reranker-base Quantizado em INT8 (CPU)
"""
import sys, os, time, json, re
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")
import evaluate_rag_benchmark as lex_engine

CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
BENCHMARK_100 = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/holdout_100_unseen.jsonl"
MODEL_NAME = "BAAI/bge-reranker-base"
os.environ["HF_HOME"] = CACHE_DIR

def main():
    print("==================================================")
    print("  TWO-STAGE PRODUCTION PIPELINE (100 Qs EM CPU)   ")
    print("==================================================")
    device = torch.device("cpu")
    print(f"Executando no dispositivo: {device} (ZERO GPU)")

    t0 = time.time()
    print("Carregando e quantizando BAAI/bge-reranker-base em INT8...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR).to(device)
    model.eval()
    quantized_reranker = torch.quantization.quantize_dynamic(
        model, {torch.nn.Linear}, dtype=torch.qint8
    )
    print(f"Re-ranker neural INT8 pronto na CPU em {time.time()-t0:.2f}s!")

    print("Indexando corpus com Contextual Prefix...")
    docs = lex_engine.load_documents()
    print(f"Total de documentos indexados: {len(docs)}")

    benchmark = [json.loads(l) for l in open(BENCHMARK_100) if l.strip()]
    hit_1 = 0
    hit_3 = 0
    hit_5 = 0
    hit_10 = 0
    reciprocal_ranks = []
    results_detail = []

    t_eval_start = time.time()
    for idx, item in enumerate(benchmark, 1):
        q_id = item["id"]
        q_text = item["question"]
        expected_cids = set(item.get("relevant_claim_ids", []))
        runbook_target = item.get("runbook_ref")

        # 1. Primeiro Estágio: BM25 com Contextual Prefix
        q_tokens = lex_engine.tokenize(q_text)
        scored = []
        for doc in docs:
            score = lex_engine.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)

        top_candidates = [s[1] for s in scored[:10]]
        if not top_candidates:
            reciprocal_ranks.append(0.0)
            continue

        # 2. Segundo Estágio: Ensemble Lexical-Neural Reranker na CPU
        pairs = [[q_text, d["text"][:450]] for d in top_candidates]
        with torch.no_grad():
            inputs = tokenizer(pairs, padding=True, truncation=True, max_length=192, return_tensors="pt").to(device)
            neural_scores = quantized_reranker(**inputs, return_dict=True).logits.view(-1).float().tolist()

        # Combinar score léxico original (bm25 + ngrams) com score neural
        combined_scores = []
        for (bm_score, d), n_score in zip(scored[:10], neural_scores):
            # Normalizar para escalas compatíveis
            final_s = bm_score + (n_score * 4.0)
            combined_scores.append((final_s, d))

        reranked_docs = [doc for _, doc in sorted(combined_scores, key=lambda x: x[0], reverse=True)]

        # Avaliar match
        rank = None
        for r_idx, doc in enumerate(reranked_docs, 1):
            is_match = False
            if doc["id"] in expected_cids:
                is_match = True
            elif doc["type"] == "aws_message":
                m_code = doc.get("msg_code")
                for ecid in expected_cids:
                    if m_code and m_code in ecid:
                        is_match = True; break
            elif runbook_target and doc.get("runbook") == runbook_target:
                is_match = True
            elif doc.get("type") == "runbook_chunk":
                for ecid in expected_cids:
                    codes = re.findall(r"\b([A-Z]{3,6}[0-9]{3,5}[A-Z]?)\b", ecid)
                    if codes and any(c.lower() in doc["text"].lower() for c in codes):
                        is_match = True; break

            if is_match:
                rank = r_idx
                break

        if rank is not None:
            if rank == 1: hit_1 += 1
            if rank <= 3: hit_3 += 1
            if rank <= 5: hit_5 += 1
            if rank <= 10: hit_10 += 1
            reciprocal_ranks.append(1.0 / rank)
        else:
            reciprocal_ranks.append(0.0)

        results_detail.append({
            "id": q_id,
            "rank": rank,
            "top_1": reranked_docs[0]["id"] if reranked_docs else None,
            "target": list(expected_cids)
        })

    total = len(benchmark)
    mrr = sum(reciprocal_ranks) / total if total else 0.0
    total_time = time.time() - t_eval_start

    print("==================================================")
    print("   RESULTADO DAS 100 PERGUNTAS (TWO-STAGE CPU)    ")
    print("==================================================")
    print(f"Total de Perguntas Avaliadas: {total}")
    print(f"Tempo total de avaliação: {total_time:.2f}s ({total_time/total*1000:.1f}ms por query na CPU)")
    print(f"Hit Rate @ 1:  {hit_1}/{total} ({hit_1/total*100:.1f}%)")
    print(f"Hit Rate @ 3:  {hit_3}/{total} ({hit_3/total*100:.1f}%)")
    print(f"Hit Rate @ 5:  {hit_5}/{total} ({hit_5/total*100:.1f}%)")
    print(f"Hit Rate @ 10: {hit_10}/{total} ({hit_10/total*100:.1f}%)")
    print(f"Mean Reciprocal Rank (MRR):    {mrr:.4f}")
    print("==================================================")

if __name__ == "__main__":
    main()
