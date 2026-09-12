#!/usr/bin/env python3
"""Diagnostico: imprime (id_pergunta, rank) para o benchmark, para diff entre seeds.

Uso: PYTHONHASHSEED=<n> python3 scripts/diff_seed.py [arquivo_benchmark]
Comparar as saidas de dois seeds diferentes revela QUAL pergunta flipa,
permitindo isolar o ponto de nao-determinismo restante.
"""
import json, os, sys

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, BASE)

import importlib.util
spec = importlib.util.spec_from_file_location(
    "rag_eval", os.path.join(BASE, "data", "eval", "evaluate_rag_benchmark.py"))
rag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag)

bench_file = sys.argv[1] if len(sys.argv) > 1 else f"{BASE}/data/eval/golden_qa_benchmark.jsonl"
docs = rag.load_documents()
bench = [json.loads(l) for l in open(bench_file) if l.strip()]

for b in bench:
    q_text = b.get("question", "")
    expected = set(b.get("relevant_claim_ids", []))
    q_tokens = rag.tokenize(q_text)
    scored = []
    for doc in docs:
        s = rag.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
        if s > 0:
            scored.append([s, doc])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    from collections import defaultdict
    diversified, seen = [], defaultdict(int)
    for s, doc in scored:
        k = doc.get("runbook") or doc.get("type")
        if doc.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
            s *= 0.65
        seen[k] += 1
        diversified.append((s, doc))
    diversified.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    final = rag.second_stage_rerank(q_text, diversified, top_n=20)
    rank = next((i for i, d in enumerate(final, 1) if d["id"] in expected), 0)
    print(f"{b.get('id')}\t{rank}")
