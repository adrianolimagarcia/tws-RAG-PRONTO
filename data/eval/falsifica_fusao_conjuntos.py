#!/usr/bin/env python3
"""Falsificacao multi-conjunto: a fusao densa ajuda ou regride, POR CONJUNTO.

O veredito de 2026-09-20 (data/evidence/lab-validation-...-dense-fusion-pooled-verdict.jsonl)
mediu a fusao no LABORATORIO (corpus de 6908 docs, ANTES da fonte REST) e deu NEGATIVO no
agregado: lexical 202/296 x fusao 181/296, McNemar p=0,0111. Mas o mesmo registro mostra que o
efeito e' ESPECIFICO por conjunto: ganha em virgem-ingles (2 -> 8) e perde em mensagens (34 -> 24)
e pure_virgin (36 -> 27).

Este script roda os MESMOS conjuntos pelo caminho REAL de producao (handle_tool_call), no corpus
atual de 7381 docs (que ja' inclui a fonte REST, ausente quando o veredito foi medido), nos modos
`off` e `fuse`. Reproduz o veredito, ou mostra que ele caducou.

Uso:
  HF_HOME=/tmp/ragexp/hfhome python3 data/eval/falsifica_fusao_conjuntos.py off  /tmp/ragexp/verif
  HF_HOME=/tmp/ragexp/hfhome python3 data/eval/falsifica_fusao_conjuntos.py fuse /tmp/ragexp/verif
"""
import json
import os
import re
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))

CONJUNTOS = [
    ("geral_70", "golden_qa_benchmark.jsonl"),
    ("mensagens", "golden_qa_messages_benchmark.jsonl"),
    ("virgem_expandido", "golden_qa_virgin_expanded.jsonl"),
    ("virgem+mensagens", "golden_qa_virgin_messages_expanded.jsonl"),
    ("virgem_INGLES", "golden_qa_virgin_en_benchmark.jsonl"),
    ("holdout_40", "holdout_40_test.jsonl"),
    ("holdout_qa_30", "blind_holdout_qa_30.jsonl"),
    ("realistico", "realistic_blind_holdout_30.jsonl"),
    ("pure_virgin", "pure_virgin_test_40.jsonl"),
    ("holdout_100", "holdout_100_unseen.jsonl"),
]
TOP_K = 10000


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "off"
    destino = sys.argv[2] if len(sys.argv) > 2 else "/tmp/ragexp/verif"
    os.environ["RAG_DENSE_MODE"] = modo
    os.makedirs(destino, exist_ok=True)

    import tws_expert_mcp as mcp
    print("modo=%s | corpus=%d docs | denso disponivel=%s"
          % (modo, len(mcp.docs), mcp.tws_dense.disponivel() if mcp.tws_dense else None))
    assert mcp.DENSE_MODE == modo, "modo nao aplicado: %s" % mcp.DENSE_MODE

    for nome, arquivo in CONJUNTOS:
        caminho = os.path.join(RAIZ, "data/eval", arquivo)
        itens = [json.loads(l) for l in open(caminho, encoding="utf-8") if l.strip()]
        t0 = time.time()
        ranks = []
        for pos, o in enumerate(itens):
            esperados = set(o.get("relevant_claim_ids") or [])
            if not esperados:
                continue
            res = mcp.handle_tool_call("tws_expert_search",
                                       {"query": o["question"], "top_k": TOP_K})
            achados = [x["claim_id"] for x in res.get("results", [])]
            p = next((i + 1 for i, c in enumerate(achados) if c in esperados), None)
            ranks.append((pos, o["id"], p, o["question"]))
        h = lambda k: sum(1 for _p, _d, r, _q in ranks if r is not None and r <= k)
        n = len(ranks)
        saida = {"conjunto": nome, "arquivo": arquivo, "modo": modo, "n": n,
                 "hit1": h(1), "hit5": h(5), "hit10": h(10),
                 "mrr": sum(1.0 / r for _p, _d, r, _q in ranks if r is not None) / n,
                 "ranks": [{"pos": p, "id": d, "rank": r} for p, d, r, _q in ranks],
                 "segundos": round(time.time() - t0, 1)}
        with open(os.path.join(destino, "%s_%s.json" % (nome, modo)), "w",
                  encoding="utf-8") as fh:
            json.dump(saida, fh, ensure_ascii=False, indent=1)
        print("  %-18s n=%3d @1 %3d @5 %3d @10 %3d MRR %.4f (%.0fs)"
              % (nome, n, h(1), h(5), h(10), saida["mrr"], saida["segundos"]), flush=True)


if __name__ == "__main__":
    main()
