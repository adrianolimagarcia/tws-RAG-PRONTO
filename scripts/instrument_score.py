#!/usr/bin/env python3
"""Instrumenta compute_bm25 para UM par (query, doc), imprimindo cada componente do score.
Permite diff entre seeds e isola exatamente qual parcela e nao-deterministica.
"""
import json, os, re, sys
from collections import defaultdict

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, BASE)

import importlib.util
spec = importlib.util.spec_from_file_location(
    "rag_eval", os.path.join(BASE, "data", "eval", "evaluate_rag_benchmark.py"))
rag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag)

qid = sys.argv[1] if len(sys.argv) > 1 else "eval-0039"
target = sys.argv[2] if len(sys.argv) > 2 else "ragflow:hwa-10.2.8-wsl-lab.md:0151"

bench = [json.loads(l) for l in open(f"{BASE}/data/eval/golden_qa_benchmark.jsonl") if l.strip()]
b = next(x for x in bench if x.get("id") == qid)
q_text = b["question"]
docs = rag.load_documents()
doc = next(d for d in docs if d["id"] == target)

qtok = rag.tokenize(q_text)
dtok = doc["tokens"]
overlap = qtok.intersection(dtok)
k1, bb, avg_dl = 1.2, 0.75, 60
dl = len(dtok)
base = 0.0
for t in sorted(overlap):
    boost = 4.0 if any(term in t for term in ["sfinal","jnextplan","resetplan","makeplan","switchplan","checksync","composer","conman","planman","joblog","vartable","rerun","generic","event1","sbs","opens","limit","securityutility","resync","twsobjectmonitor","switcheventprocessor","switchevtp","helm","chart","kubernetes","tebctl","cwwkf0011i","enretain","wapl","mmrresolve","symnew","conddep","wa_pull_info","baserecprompt","aida","carryforward"]) else 1.0
    base += boost * ((k1 + 1) / (1.0 + k1 * (1.0 - bb + bb * (dl / avg_dl))))

print("## COMPONENTES")
print("overlap_n\t", len(overlap))
print("base\t", repr(base))
print("dl\t", dl)
print("type\t", doc.get("type"))
print("path\t", doc.get("path"))
print("title\t", doc.get("title"))
meta = doc.get("metadata", {})
print("meta.commands_type\t", type(meta.get("commands")).__name__)
print("meta.commands\t", repr(meta.get("commands"))[:300])
print("meta.aws_codes_type\t", type(meta.get("aws_codes")).__name__)
print("meta.aws_codes\t", repr(meta.get("aws_codes"))[:300])
print("doc_text_len\t", len(doc.get("text") or ""))
print("doc_text_md5\t", __import__("hashlib").md5((doc.get("text") or "").encode()).hexdigest())
print("final\t", repr(rag.compute_bm25(qtok, dtok, q_text, doc["text"], doc=doc)))
