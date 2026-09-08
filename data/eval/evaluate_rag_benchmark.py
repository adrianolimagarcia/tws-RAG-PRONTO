#!/usr/bin/env python3
"""Harness de Avaliacao Automatica do RAG TWS/HWA.
Consome o golden_qa_benchmark.jsonl e mede:
- Hit Rate @ 1, 3, 5
- Mean Reciprocal Rank (MRR)
- Cobertura de runbooks
"""
import glob, json, math, os, re, sys
from collections import defaultdict

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BENCHMARK_FILE = os.path.join(REPO_DIR, "data", "eval", "golden_qa_benchmark.jsonl")
CLAIMS_FILE = os.path.join(REPO_DIR, "data", "evidence", "claims.jsonl")
LAB_FILES = glob.glob(os.path.join(REPO_DIR, "data", "evidence", "lab-validation-*.jsonl"))
RUNBOOKS_DIR = os.path.join(REPO_DIR, "data", "runbooks")

def tokenize(text):
    if not text:
        return set()
    words = re.findall(r"[A-Za-z0-9_\-\.\:\^]+", text.lower())
    stop = {"de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "a", "an", "the", "in", "on", "at", "to", "for", "of", "and", "or", "is", "was", "with"}
    return {w for w in words if len(w) > 2 and w not in stop}

def load_documents():
    docs = []
    # 1. Claims canonicas
    if os.path.exists(CLAIMS_FILE):
        for line in open(CLAIMS_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('claim', '')} {c.get('notes', '')} {c.get('topic', '')} {c.get('subtopic', '')}"
                docs.append({
                    "id": cid,
                    "type": "canonical_claim",
                    "text": text,
                    "tokens": tokenize(text),
                    "obj": c
                })
    # 2. Lab validation claims
    for lf in LAB_FILES:
        for line in open(lf):
            if line.strip():
                try:
                    c = json.loads(line)
                    cid = c.get("claim_id", "")
                    if cid:
                        text = f"{c.get('claim', '')} {c.get('result', '')} {c.get('observations', '')} {c.get('sanitized_output', '')}"
                        docs.append({
                            "id": cid,
                            "type": "lab_evidence",
                            "text": text,
                            "tokens": tokenize(text),
                            "obj": c
                        })
                except Exception:
                    pass
    return docs

def compute_bm25_lite(query_tokens, doc_tokens, avg_dl=40):
    if not doc_tokens:
        return 0.0
    k1 = 1.2
    b = 0.75
    overlap = query_tokens.intersection(doc_tokens)
    score = 0.0
    dl = len(doc_tokens)
    for t in overlap:
        # Boost de termos técnicos específicos de HWA
        boost = 1.0
        if any(term in t for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens", "limit", "securityutility"]):
            boost = 2.5
        score += boost * ((k1 + 1) / (1.0 + k1 * (1.0 - b + b * (dl / avg_dl))))
    return score

def run_evaluation():
    if not os.path.exists(BENCHMARK_FILE):
        print(f"Erro: {BENCHMARK_FILE} nao encontrado.")
        return

    benchmark = [json.loads(line) for line in open(BENCHMARK_FILE)]
    docs = load_documents()
    print(f"Documentos indexados para retrieval: {len(docs)}")

    top_k_hits = {1: 0, 3: 0, 5: 0}
    reciprocal_ranks = []
    results = []

    for b in benchmark:
        qid = b.get("id")
        q_text = b.get("question", "")
        expected_ids = set(b.get("relevant_claim_ids", []))
        q_tokens = tokenize(q_text)

        scored = []
        for doc in docs:
            score = compute_bm25_lite(q_tokens, doc["tokens"])
            if score > 0:
                scored.append((score, doc["id"]))

        scored.sort(key=lambda x: x[0], reverse=True)
        retrieved_ids = [s[1] for s in scored]

        # Calcular rank do primeiro acerto
        rank = None
        for idx, did in enumerate(retrieved_ids):
            if did in expected_ids:
                rank = idx + 1
                break

        if rank is not None:
            reciprocal_ranks.append(1.0 / rank)
            if rank <= 1: top_k_hits[1] += 1
            if rank <= 3: top_k_hits[3] += 1
            if rank <= 5: top_k_hits[5] += 1
        else:
            reciprocal_ranks.append(0.0)

        results.append({
            "id": qid,
            "domain": b.get("domain"),
            "question": q_text,
            "rank": rank,
            "expected": list(expected_ids),
            "top_3_retrieved": retrieved_ids[:3]
        })

    total = len(benchmark)
    mrr = sum(reciprocal_ranks) / total if total else 0.0

    print("==================================================")
    print("      RELATÓRIO DE AVALIAÇÃO DO RAG BENCHMARK     ")
    print("==================================================")
    print(f"Total de Perguntas Avaliadas: {total}")
    print(f"Hit Rate @ 1: {top_k_hits[1]}/{total} ({top_k_hits[1]/total*100:.1f}%)")
    print(f"Hit Rate @ 3: {top_k_hits[3]}/{total} ({top_k_hits[3]/total*100:.1f}%)")
    print(f"Hit Rate @ 5: {top_k_hits[5]}/{total} ({top_k_hits[5]/total*100:.1f}%)")
    print(f"Mean Reciprocal Rank (MRR):   {mrr:.4f}")
    print("==================================================")

    # Gravar sumario
    out_file = os.path.join(REPO_DIR, "data", "eval", "eval_summary.json")
    with open(out_file, "w") as f:
        json.dump({
            "total": total,
            "hit_rate_at_1": top_k_hits[1] / total,
            "hit_rate_at_3": top_k_hits[3] / total,
            "hit_rate_at_5": top_k_hits[5] / total,
            "mrr": mrr,
            "details": results
        }, f, indent=2, ensure_ascii=False)
    print(f"Sumário de avaliação gravado em {out_file}")

if __name__ == "__main__":
    run_evaluation()
