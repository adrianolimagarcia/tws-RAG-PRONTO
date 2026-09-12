#!/usr/bin/env python3
"""Dump dos scores dos candidatos de uma pergunta especifica, para diff entre seeds.

Uso: PYTHONHASHSEED=<n> python3 scripts/debug_q.py eval-0039
Imprime (posicao, id, score_repr) do estagio BM25 e do pos-rerank.
"""
import json, os, sys
from collections import defaultdict

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, BASE)

import importlib.util
spec = importlib.util.spec_from_file_location(
    "rag_eval", os.path.join(BASE, "data", "eval", "evaluate_rag_benchmark.py"))
rag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag)

qid = sys.argv[1] if len(sys.argv) > 1 else "eval-0039"
bench = [json.loads(l) for l in open(f"{BASE}/data/eval/golden_qa_benchmark.jsonl") if l.strip()]
b = next(x for x in bench if x.get("id") == qid)
q_text = b["question"]
print(f"# {qid}: {q_text[:110]}")
print(f"# esperado: {b.get('relevant_claim_ids')}")

docs = rag.load_documents()
qtok = rag.tokenize(q_text)
scored = []
for doc in docs:
    s = rag.compute_bm25(qtok, doc["tokens"], q_text, doc["text"], doc=doc)
    if s > 0:
        scored.append([s, doc])
scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
print("\n## BM25 top-8")
for i, (s, d) in enumerate(scored[:8], 1):
    print(f"{i}\t{repr(s)}\t{d['id']}")

diversified, seen = [], defaultdict(int)
for s, doc in scored:
    k = doc.get("runbook") or doc.get("type")
    if doc.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
        s *= 0.65
    seen[k] += 1
    diversified.append((s, doc))
diversified.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
final = rag.second_stage_rerank(q_text, diversified, top_n=20)
print("\n## pos-rerank top-12")
for i, d in enumerate(final[:12], 1):
    print(f"{i}\t{d['id']}")
