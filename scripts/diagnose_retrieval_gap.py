#!/usr/bin/env python3
"""Diagnostica POR QUE o documento-alvo de um benchmark cai fundo no ranking.

Por que existe
--------------
O benchmark REST (`data/eval/rest_api_benchmark_40.jsonl`) deu 2,5% @1 com a fonte
ligada e 0,0% com ela desligada. O teste de vazamento passa, logo o benchmark e'
valido — mas o teto de 17,5% @10 ficou sem explicacao.

Uma primeira tentativa de explicar usou `compute_bm25` direto e produziu numeros
DIFERENTES do avaliador (0/40 @1 e 4/40 @10 contra 1/40 e 7/40), porque omitia a
diversificacao de fonte e o `second_stage_rerank`. As posicoes calculadas nao eram
as do avaliador e foram retiradas.

Este script evita esse erro de um jeito estrutural: ele NAO reimplementa o pipeline.
Ele carrega o avaliador real e INTERCEPTA `compute_bm25` por monkeypatch, de modo
que os scores capturados sao exatamente os que o avaliador usou, na mesma ordem de
chamada. Se o avaliador mudar, isto continua fiel.

Uso:
    RAG_INGEST_REST_API=1 PYTHONHASHSEED=0 python3 scripts/diagnose_retrieval_gap.py \
        --benchmark data/eval/rest_api_benchmark_40.jsonl
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import statistics
import sys

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_PY = os.path.join(REPO_DIR, "data", "eval", "evaluate_rag_benchmark.py")


def carregar_avaliador():
    spec = importlib.util.spec_from_file_location("ev_bench", EVAL_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--top", type=int, default=8)
    args = ap.parse_args()

    ev = carregar_avaliador()

    capturado: list[tuple] = []
    original = ev.compute_bm25

    def espiar(query_tokens, doc_tokens, query_raw, doc_text, doc=None, avg_dl=60):
        score = original(query_tokens, doc_tokens, query_raw, doc_text, doc, avg_dl)
        capturado.append((doc.get("id"), score, doc.get("type"), len(doc_tokens)))
        return score

    ev.compute_bm25 = espiar
    ev.run_evaluation()  # roda o pipeline REAL, com o benchmark de RAG_BENCHMARK_FILE

    bench = [json.loads(l) for l in open(args.benchmark)]
    docs = ev.load_documents()
    n = len(docs)
    if len(capturado) != n * len(bench):
        print(f"  AVISO: capturados {len(capturado)} scores, esperado {n * len(bench)}", file=sys.stderr)

    por_pergunta = [capturado[i * n:(i + 1) * n] for i in range(len(bench))]

    print()
    print("  === score do alvo vs o topo, por pergunta ===")
    for b, cap in list(zip(bench, por_pergunta))[: args.top]:
        alvo = b["relevant_claim_ids"][0]
        mapa = {i: (s, t, l) for i, s, t, l in cap}
        if alvo not in mapa:
            print(f"    {b['id']}  alvo AUSENTE do corpus")
            continue
        sa, ta, la = mapa[alvo]
        topo = sorted(cap, key=lambda x: -x[1])[:1][0]
        pos = sum(1 for x in cap if x[1] > sa) + 1
        print(f"    {b['id']} {b['family'][:20]:20s} alvo={sa:5.2f} ({ta},{la}tok) pos={pos:5d}"
              f" | top1={topo[1]:5.2f} ({topo[2]},{topo[3]}tok)")

    print()
    print("  === agregado ===")
    razoes = []
    for b, cap in zip(bench, por_pergunta):
        alvo = b["relevant_claim_ids"][0]
        mapa = {i: s for i, s, t, l in cap}
        if alvo not in mapa:
            continue
        razoes.append((mapa[alvo], max(s for _, s, _, _ in cap)))
    if razoes:
        print(f"    score do alvo   : mediana={statistics.median(a for a, _ in razoes):.2f}"
              f"  max={max(a for a, _ in razoes):.2f}")
        print(f"    score do top-1  : mediana={statistics.median(t for _, t in razoes):.2f}"
              f"  min={min(t for _, t in razoes):.2f}")
        print(f"    razao top1/alvo : mediana={statistics.median(t / max(0.01, a) for a, t in razoes):.1f}x")

    print()
    print("  === quem vence, por tipo de documento (top-1 de cada pergunta) ===")
    vencedores = {}
    for cap in por_pergunta:
        if not cap:
            continue
        topo = sorted(cap, key=lambda x: -x[1])[0]
        vencedores[topo[2]] = vencedores.get(topo[2], 0) + 1
    for tipo, qtd in sorted(vencedores.items(), key=lambda x: -x[1]):
        print(f"    {str(tipo):28s} {qtd}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
