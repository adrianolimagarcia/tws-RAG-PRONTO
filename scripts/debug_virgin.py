#!/usr/bin/env python3
"""Debug: para uma pergunta virgem, mostra o que o harness realmente recupera (top-5)."""
import json, os, sys

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "data", "eval"))

import importlib.util
spec = importlib.util.spec_from_file_location(
    "rag_eval", os.path.join(BASE, "data", "eval", "evaluate_rag_benchmark.py"))
rag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag)

docs = rag.load_documents()
print("docs carregados:", len(docs))
ids = {d["id"] for d in docs}
print("hwa-msgcat-awsdah002e esta no indice?", "hwa-msgcat-awsdah002e" in ids)
print("hwa-msgcat-awsbhu159e esta no indice?", "hwa-msgcat-awsbhu159e" in ids)
print("total de docs message_catalog:", sum(1 for d in docs if d.get("type") == "message_catalog"))

bench = [json.loads(l) for l in open(f"{BASE}/data/eval/golden_qa_virgin_benchmark.jsonl") if l.strip()]

for b in bench[:3]:
    q = b["question"]
    want = b["relevant_claim_ids"]
    qtok = rag.expand_query(q)
    scored = []
    for d in docs:
        s = rag.compute_bm25(qtok, d["tokens"], q, d["text"], doc=d)
        if s > 0:
            scored.append([s, d])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    top = rag.second_stage_rerank(q, scored, top_n=20)[:5]
    print("\n" + "=" * 70)
    print("PERGUNTA:", q[:95])
    print("ESPERADO:", want)
    for i, d in enumerate(top, 1):
        mark = "  <<< HIT" if d["id"] in want else ""
        print(f"  {i}. [{d['id']}] {d['text'][:110]}{mark}")
