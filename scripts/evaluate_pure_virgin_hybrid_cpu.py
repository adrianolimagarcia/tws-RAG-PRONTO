#!/usr/bin/env python3
"""Busca Híbrida 100% em CPU:
Combina os Embeddings Densos pré-computados (corpus_bge_m3_v3.pt, 13.7MB)
com o BM25 Léxico usando Reciprocal Rank Fusion (RRF) na CPU pura,
sem depender de GPU em runtime.

Atualizado 18.09.2026: o indice era `corpus_bge_m3.pt` (v1, 09/09, 2427 linhas)
e cobria apenas 2309 dos 6903 ids unicos do corpus (~33.5%) - dois tercos do
corpus nao tinham vetor denso. Repontado para `corpus_bge_m3_v3.pt`, reconstruido
sobre os 7020 documentos atuais (6903 ids unicos, 117 duplicados de id).
"""
import sys, os, time, json, re
import torch

sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")
import evaluate_rag_benchmark as lex_engine

CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
INDEX_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/indexes/corpus_bge_m3_v3.pt"
DOCS_META_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/indexes/corpus_docs_meta_v3.json"
TEST_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/pure_virgin_test_40.jsonl"
os.environ["HF_HOME"] = CACHE_DIR

def main():
    print("==================================================")
    print("  BUSCA HÍBRIDA (DENSE BGE-M3 + BM25) EM CPU PURA ")
    print("==================================================")
    # Forçar estritamente CPU
    device = torch.device("cpu")
    print(f"Executando no dispositivo: {device} (ZERO GPU)")

    t0 = time.time()
    # Carregar matriz pré-computada de 4.8 MB na memória RAM da CPU
    print(f"Carregando matriz de embeddings de {INDEX_FILE} na RAM...")
    corpus_embeddings = torch.load(INDEX_FILE, map_location=device, weights_only=False).float()  # [2427, 1024]
    with open(DOCS_META_FILE) as f:
        doc_ids = json.load(f)
    idx_to_id = {i: doc_id for i, doc_id in enumerate(doc_ids)}

    # Carregar documentos do corpus
    corpus = lex_engine.load_documents()
    corpus_map = {d["id"]: d for d in corpus}
    print(f"Total de documentos: {len(corpus)} (Matriz em RAM: {corpus_embeddings.element_size() * corpus_embeddings.nelement() / (1024**2):.2f} MB)")

    # Carregar tokenizer e modelo de embedding para queries na CPU
    print("Carregando tokenizer BGE-M3 na CPU...")
    from transformers import AutoTokenizer, AutoModel
    embed_tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    embed_mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR, use_safetensors=True).to(device)
    embed_mod.eval()
    print(f"Carregado em {time.time()-t0:.2f}s!")

    benchmark = [json.loads(l) for l in open(TEST_FILE) if l.strip()]
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

        # 1. Ramo Denso: Gerar embedding da query na CPU e multiplicar por cosseno
        with torch.no_grad():
            q_in = embed_tok([q_text], padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
            q_out = embed_mod(**q_in)
            q_emb = torch.nn.functional.normalize(q_out.last_hidden_state[:, 0, :], p=2, dim=1).float() # [1, 1024]
            # Multiplicação matricial instantânea na CPU (< 2ms)
            dense_scores = torch.mm(q_emb, corpus_embeddings.T).squeeze(0) # [2427]
            dense_top_indices = torch.topk(dense_scores, k=30).indices.tolist()

        dense_ranked_ids = [idx_to_id[i] for i in dense_top_indices]

        # 2. Ramo Esparso: BM25 com tokenização limpa e N-grams
        q_tokens = lex_engine.tokenize(q_text)
        sparse_candidates = []
        for doc in corpus:
            s = lex_engine.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
            if s > 0:
                sparse_candidates.append((s, doc["id"]))
        sparse_candidates.sort(key=lambda x: x[0], reverse=True)
        sparse_ranked_ids = [c[1] for c in sparse_candidates[:30]]

        # 3. Fusão RRF (Reciprocal Rank Fusion k=60)
        rrf_scores = {}
        for r, did in enumerate(dense_ranked_ids, 1):
            rrf_scores[did] = rrf_scores.get(did, 0.0) + 1.0 / (60.0 + r)
        for r, did in enumerate(sparse_ranked_ids, 1):
            rrf_scores[did] = rrf_scores.get(did, 0.0) + 1.0 / (60.0 + r)

        fused_sorted_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)[:20]
        top_candidates = [(rrf_scores[did], corpus_map[did]) for did in fused_sorted_ids if did in corpus_map]

        # 4. Segundo Estágio de Re-ranking de N-Grams e Cobertura
        reranked_docs = lex_engine.second_stage_rerank(q_text, top_candidates, top_n=15)

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
    print("   RESULTADO DO TESTE VIRGEM EM CPU COM BUSCA HÍBRIDA")
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
