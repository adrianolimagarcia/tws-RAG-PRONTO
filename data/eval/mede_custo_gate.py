#!/usr/bin/env python3
"""Taxa de disparo do gate e latencia por modo, no pool 423 (pelo caminho real).

Uso: HF_HOME=... RAG_DENSE_MODE=gate python3 data/eval/mede_custo_gate.py
"""
import json
import os
import re
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))


def main():
    import tws_expert_mcp as mcp
    pool = os.environ.get("RAG_POOL", "/tmp/ragexp/pool_recon.jsonl")
    itens = [json.loads(l) for l in open(pool, encoding="utf-8") if l.strip()]
    disparos = 0
    t0 = time.time()
    for o in itens:
        base = mcp.search_bm25(re.findall(r"\w+", o["question"].lower()), top_k=5)
        if mcp._deve_fundir(base):
            disparos += 1
        mcp.handle_tool_call("tws_expert_search", {"query": o["question"], "top_k": 10000})
    dt = time.time() - t0
    print("%s: dispara em %d/%d (%.1f%%) | %.1f ms/pergunta"
          % (mcp.DENSE_MODE, disparos, len(itens), 100 * disparos / len(itens), 1000 * dt / len(itens)))


if __name__ == "__main__":
    main()
