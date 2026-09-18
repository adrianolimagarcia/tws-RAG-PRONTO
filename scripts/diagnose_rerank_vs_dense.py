#!/usr/bin/env python3
"""Diagnostica POR QUE o segundo estagio piora candidatos densos.

HIPOTESE A TESTAR (mecanismo, nao ajuste)
-----------------------------------------
`second_stage_rerank` soma bonus de n-grama de +8/+12/+15/+20 ao score recebido e
processa SOMENTE candidates[:top_n]. Os scores que ele recebe do ramo denso sao
~1.0 com passos de 1e-6 (ou ~0,016 no RRF). Se os bonus sao ordens de grandeza
maiores que a diferenca entre candidatos, eles NAO desempatam - eles APAGAM a ordem
de entrada e impoem a propria. O reranker estaria calibrado para scores de BM25
(dezenas), nao para cosseno nem RRF.

O QUE ESTE SCRIPT MEDE (por pergunta, sem agregar nada)
  1. rank DENSO do alvo (a ordem do BGE-M3)
  2. rank do alvo APOS o segundo estagio, sobre os mesmos candidatos
  3. se o alvo estava no pool (top_n) ou foi cortado antes de ser pontuado
  4. a escala: o intervalo dos scores de entrada contra a magnitude dos bonus

Assim a perda de @1 (32,5% -> 22,5%) fica atribuida a um mecanismo, nao a uma
impressao: ou o alvo e' CORTADO (pool pequeno), ou e' REBAIXADO (bonus dominam).

USO
    python3 scripts/diagnose_rerank_vs_dense.py [--top-n 20] [--pool 30]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import statistics
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ambiente ANTES de importar o avaliador: os switches sao lidos no topo do modulo.
os.environ.setdefault("RAG_MEASURE_EXCLUDE_EVIDENCE", "1")
os.environ.setdefault("RAG_INGEST_REST_API", "1")
os.environ.setdefault("RAG_REST_GRANULARITY", "operation")
os.environ.setdefault("RAG_DENSE_INDEX", "data/indexes/corpus_bge_m3_v6.pt")
os.environ.setdefault("RAG_DENSE_META", "data/indexes/corpus_docs_meta_v6.json")
os.environ.setdefault("RAG_BENCHMARK_FILE", "data/eval/rest_api_benchmark_ops_40.jsonl")


def carrega_modulo():
    caminho = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")
    spec = importlib.util.spec_from_file_location("ev", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top-n", type=int, default=20, help="quanto o segundo estagio processa")
    ap.add_argument("--pool", type=int, default=30, help="candidatos densos oferecidos")
    args = ap.parse_args()

    ev = carrega_modulo()
    docs = ev.load_documents()
    por_id = {d["id"]: d for d in docs}
    bench = [json.loads(l) for l in open(os.path.join(REPO, ev.BENCHMARK_FILE), encoding="utf-8")]

    # pool grande para saber se o alvo existiria se o pool fosse maior
    POOL_DIAG = max(args.pool, 300)

    linhas = []
    cand: list = []  # ultimo pool denso montado; usado no bloco de escala abaixo
    for item in bench:
        q = item["question"]
        alvo = item["relevant_claim_ids"][0]
        dids = ev._dense_top30(q, POOL_DIAG)

        rank_denso = None
        for i, did in enumerate(dids, 1):
            if did == alvo:
                rank_denso = i
                break

        cand = [(1.0 - r * 1e-6, por_id[did]) for r, did in enumerate(dids[: args.pool]) if did in por_id]
        rr = ev.second_stage_rerank(q, cand, top_n=args.top_n)
        rank_rr = None
        for i, d in enumerate(rr, 1):
            if d["id"] == alvo:
                rank_rr = i
                break

        no_pool = rank_denso is not None and rank_denso <= args.pool
        linhas.append({
            "id": item["id"],
            "rank_denso": rank_denso,
            "rank_rerank": rank_rr,
            "no_pool": no_pool,
            "cortado_pelo_pool": rank_denso is not None and rank_denso > args.pool,
        })

    n = len(linhas)
    print(f"perguntas: {n}   pool={args.pool}   segundo_estagio_processa={args.top_n}")
    print()

    # --- distribuicao dos ranks densos ---
    rd = [l["rank_denso"] for l in linhas if l["rank_denso"] is not None]
    print(f"alvo presente no pool de {POOL_DIAG}: {len(rd)}/{n}")
    if rd:
        print(f"  rank denso do alvo: min={min(rd)} mediana={statistics.median(rd)} max={max(rd)}")
        print(f"  denso rank<=10: {sum(1 for x in rd if x <= 10)}/{n}")
    print()

    # --- o que o segundo estagio fez com quem ele viu ---
    viu = [l for l in linhas if l["no_pool"]]
    manteve = [l for l in viu if l["rank_rerank"] is not None]
    rebaixou = [l for l in manteve if l["rank_rerank"] > l["rank_denso"]]
    subiu = [l for l in manteve if l["rank_rerank"] < l["rank_denso"]]
    perdeu = [l for l in viu if l["rank_rerank"] is None]

    print(f"alvos que o segundo estagio VIU (dentro do pool): {len(viu)}/{n}")
    print(f"  manteve o alvo na saida : {len(manteve)}")
    print(f"  REBAIXOU (rank piorou)  : {len(rebaixou)}")
    print(f"  subiu                   : {len(subiu)}")
    print(f"  DESCARTOU (saiu da saida de {args.top_n}): {len(perdeu)}")
    print()

    # --- o teste da hipotese: a escala ---
    print("ESCALA DOS SCORES DE ENTRADA vs BONUS DO RERANKER")
    print("  bonus possiveis: +8.0 e +12.0 (bigramas), +15.0 e +20.0 (trigramas)")
    if len(cand) >= 2:
        s = [x[0] for x in cand]
        print(f"  score de entrada: min={min(s):.9f} max={max(s):.9f} amplitude={max(s)-min(s):.9f}")
        print(f"  amplitude da entrada / menor bonus (+8): {(max(s)-min(s))/8.0:.3e}")
    # quanto o rerank moveu, em posicoes
    if manteve:
        deltas = [l["rank_rerank"] - l["rank_denso"] for l in manteve]
        print(f"  deslocamento do alvo (posicoes): min={min(deltas)} mediana={statistics.median(deltas)} max={max(deltas)}")
    print()

    # --- veredito mecanico ---
    if perdeu and not rebaixou:
        v = "CORTE: o alvo estava no pool mas saiu da saida do segundo estagio."
    elif rebaixou and not perdeu:
        v = "REBAIXAMENTO: o segundo estagio reordenou o alvo para pior (bonus sobre a ordem de entrada)."
    elif rebaixou and perdeu:
        v = "AMBOS: ha rebaixamento e ha corte."
    else:
        v = "SEM DANO: o segundo estagio nao piorou nenhum alvo que viu."
    print(f"VEREDITO: {v}")

    out = {"top_n": args.top_n, "pool": args.pool, "n": n, "linhas": linhas,
           "rebaixou": len(rebaixou), "perdeu": len(perdeu), "subiu": len(subiu),
           "veredito": v}
    print(json.dumps({k: out[k] for k in ("top_n", "pool", "n", "rebaixou", "perdeu", "subiu")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
