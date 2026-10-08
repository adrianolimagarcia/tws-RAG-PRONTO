#!/usr/bin/env python3
"""O denso funciona na fatia REST? Isola DENSO PURO x FUSAO x ESPARSO.

Motivo: a evidencia `varredura-do-peso-da-fusao...-o-braco-rest-ficou-invalido` registra denso
PURO a 32,5% @1 no rest_ops_40, mas a producao mediu 0-1/40 com fuse/gate. A hipotese e' que o
RRF DILUI o ramo denso (o esparso vota errado e o voto conta), nao que o denso falhe.

Uso: HF_HOME=... python3 data/eval/mede_roteador_rest.py
"""
import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))

import tws_expert_mcp as mcp  # noqa: E402

CONJUNTOS = [
    ("rest_api", "rest_api_benchmark_40.jsonl"),
    ("rest_api_ops", "rest_api_benchmark_ops_40.jsonl"),
    ("fresh_blind", "fresh_blind_test_40.jsonl"),
    ("vault", "blind_holdout_50_vault.jsonl"),
    ("holdout_100", "holdout_100_unseen.jsonl"),
    ("mensagens", "golden_qa_messages_benchmark.jsonl"),
    ("pure_virgin", "pure_virgin_test_40.jsonl"),
]


def rankeia(func, q, top_k=100):
    """Devolve {claim_id: rank} do modo dado, com a MESMA normalizacao de query do MCP."""
    try:
        res = func(q)
    except Exception:
        return {}
    out = {}
    for i, r in enumerate(res[:top_k], 1):
        cid = r["claim_id"] if isinstance(r, dict) else r[0]
        out.setdefault(cid, i)
    return out


def main():
    modos = {
        "esparso": lambda q: mcp.handle_tool_call(
            "tws_expert_search", {"query": q, "top_k": 100})["results"],
        "denso_puro": lambda q: [{"claim_id": c} for c, _ in
                                 mcp.tws_dense.busca(q, top_k=100)],
    }
    for rotulo, arq in CONJUNTOS:
        caminho = os.path.join(RAIZ, "data", "eval", arq)
        itens = [json.loads(l) for l in open(caminho, encoding="utf-8") if l.strip()]
        print("=== %s (%d)" % (rotulo, len(itens)))
        for nome, fn in modos.items():
            t0 = time.time()
            h = {1: 0, 5: 0, 10: 0}
            mrr = 0.0
            n = 0
            for o in itens:
                rel = o.get("relevant_claim_ids") or []
                if not rel:
                    continue
                n += 1
                R = rankeia(fn, o["question"])
                melhores = [R[r] for r in rel if r in R]
                if melhores:
                    m = min(melhores)
                    mrr += 1.0 / m
                    for k in h:
                        if m <= k:
                            h[k] += 1
            print("  %-11s n=%3d @1 %3d @5 %3d @10 %3d MRR %.4f (%.0fs)"
                  % (nome, n, h[1], h[5], h[10], mrr / n if n else 0, time.time() - t0))


if __name__ == "__main__":
    main()
