#!/usr/bin/env python3
"""Quantifica em que posicao a mensagem CORRETA cai, para perguntas virgens."""
import json, os, sys

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, BASE)

import importlib.util
spec = importlib.util.spec_from_file_location(
    "rag_eval", os.path.join(BASE, "data", "eval", "evaluate_rag_benchmark.py"))
rag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag)

docs = rag.load_documents()

for bench_file, label in [("golden_qa_virgin_benchmark.jsonl", "PT"),
                          ("golden_qa_virgin_en_benchmark.jsonl", "EN")]:
    bench = [json.loads(l) for l in open(f"{BASE}/data/eval/{bench_file}") if l.strip()]
    ranks = []
    for b in bench:
        q, want = b["question"], set(b["relevant_claim_ids"])
        qtok = rag.expand_query(q)
        scored = []
        for d in docs:
            s = rag.compute_bm25(qtok, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        final = rag.second_stage_rerank(q, scored, top_n=20)
        rank = next((i for i, d in enumerate(final, 1) if d["id"] in want), None)
        ranks.append(rank)
    found = [r for r in ranks if r]
    print(f"\n=== VIRGEM {label}: {len(bench)} perguntas ===")
    print(f"  encontradas no top-10: {sum(1 for r in found if r<=10)}/{len(bench)}")
    print(f"  encontradas em alguma posicao: {len(found)}/{len(bench)}")
    if found:
        print(f"  melhor posicao: {min(found)} | mediana: {sorted(found)[len(found)//2]} | pior: {max(found)}")
    print(f"  posicoes: {sorted(found)[:15]}")
