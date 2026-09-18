#!/usr/bin/env python3
"""Mede a travessia CROSS-LINGUAL PT->EN do ramo denso (BGE-M3) no benchmark por operacao.

PERGUNTA QUE ESTE SCRIPT RESPONDE
---------------------------------
O benchmark por operacao mostrou que a recuperacao e' quase nula (BM25 1/40 @1). A
causa medida foi lexical: cobertura de tokens pergunta<->alvo com mediana 0,00 e
21/40 casos zerados, porque os registros derivados da spec sao INGLES e as perguntas
sao PT-BR. Resta saber se o problema e' do MODELO ou do DADO:
  - se o embedding do BGE-M3 (multilingue) aproxima pergunta PT de registro EN, o
    dado esta' ok e o que falta e' usar o ramo denso;
  - se nao aproxima, nenhum reranker resolve e o dado precisa de texto em PT.

CONFIGURACOES MEDIDAS (todas com o corpus CONGELADO)
  bm25         - esparso puro, a linha de base ja publicada
  dense_raw    - RAG_DENSE_ONLY=raw: o ranking do proprio BGE-M3, SEM segundo estagio.
                 E' o sinal cross-lingual cru, antes de qualquer reordenacao.
  dense_rerank - RAG_DENSE_ONLY=rerank: denso passando pelo mesmo second_stage_rerank
                 da producao (forma final).
  dense_off    - CONTROLE: fonte OFF. O alvo nao existe no corpus; tem de dar 0/40.

DISCIPLINA
  - Read-only: nao liga default nenhum, nao muta o lab, nao altera corpus.
  - `rank=None` e' estado PROPRIO (nunca convertido em zero): reportado como
    `nunca_recuperado` ao lado dos acertos.
  - `eval_summary.json` e' artefato gerado: salvo e RESTAURADO ao final.
  - Registra (HEAD, n_docs) de cada medicao para que o numero seja rastreavel.

USO
    python3 scripts/measure_crosslingual_dense.py --out /tmp/cross.json
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
SUM = os.path.join(REPO, "data", "eval", "eval_summary.json")
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_ops_40.jsonl")

# Corpus congelado em TODAS as medicoes: sem isso, cada evidencia gravada entra no
# corpus como lab_evidence e move as metricas (defeito ja medido e documentado).
BASE = {
    "RAG_MEASURE_EXCLUDE_EVIDENCE": "1",
    "RAG_INGEST_REST_API": "1",
    "RAG_REST_GRANULARITY": "operation",
    "RAG_BENCHMARK_FILE": BENCH,
    "PYTHONHASHSEED": "0",
}
V6 = "data/indexes/corpus_bge_m3_v6.pt"
V6META = "data/indexes/corpus_docs_meta_v6.json"
DENSE = {"RAG_DENSE_INDEX": V6, "RAG_DENSE_META": V6META}

CONFIGS: dict[str, dict] = {
    "bm25": {},
    "dense_raw": {**DENSE, "RAG_DENSE_ONLY": "raw"},
    "dense_rerank": {**DENSE, "RAG_DENSE_ONLY": "rerank"},
    "dense_off": {**DENSE, "RAG_DENSE_ONLY": "raw", "_fonte_off": "1"},
}


def head() -> str:
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip()


def roda(extra: dict) -> dict:
    env = dict(os.environ)
    env.update(BASE)
    fonte_off = extra.pop("_fonte_off", None)
    if fonte_off:
        env.pop("RAG_INGEST_REST_API", None)
        env.pop("RAG_REST_GRANULARITY", None)
    env.update(extra)

    r = subprocess.run([PY, "data/eval/evaluate_rag_benchmark.py"], cwd=REPO, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"erro": f"rc={r.returncode}", "stderr": r.stderr[-400:]}

    # n_docs = TAMANHO DO CORPUS, lido do proprio avaliador (nao confundir com o
    # numero de perguntas avaliadas). E' o que torna a medicao rastreavel.
    n_docs = None
    for linha in r.stdout.splitlines():
        if "Total de documentos" in linha:
            try:
                n_docs = int(linha.split(":")[-1].strip())
            except ValueError:
                pass
            break

    d = json.load(open(SUM, encoding="utf-8"))
    det = d.get("details", [])
    # rank=None e' estado PROPRIO, nao zero: separado dos acertos.
    nunca = sum(1 for x in det if x.get("rank") is None)
    ranks = [x["rank"] for x in det if x.get("rank") is not None]
    return {
        "n_docs": n_docs,
        "total": d.get("total"),
        "n_avaliadas": len(det),
        "hit1": d.get("hit_rate_at_1"),
        "hit3": d.get("hit_rate_at_3"),
        "hit5": d.get("hit_rate_at_5"),
        "hit10": d.get("hit_rate_at_10"),
        "mrr": d.get("mrr"),
        "nunca_recuperado": nunca,
        "acertos": len(ranks),
        "pior_rank": max(ranks) if ranks else None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="arquivo JSON de saida")
    ap.add_argument("--n-docs", default=None, help="n_docs esperado (valida o corpus)")
    args = ap.parse_args()

    if not os.path.exists(os.path.join(REPO, V6)):
        print(f"ERRO: {V6} nao existe - rode o build do indice v6 antes.", file=sys.stderr)
        return 2
    if not os.path.exists(BENCH):
        print(f"ERRO: {BENCH} nao existe.", file=sys.stderr)
        return 2

    # backup do artefato gerado; restaurado no finally
    bak = SUM + ".bak-measure"
    if os.path.exists(SUM):
        shutil.copy2(SUM, bak)

    h = head()
    res: dict = {"head": h, "benchmark": os.path.relpath(BENCH, REPO),
                 "indice_denso": V6, "corpus": "congelado (RAG_MEASURE_EXCLUDE_EVIDENCE=1)",
                 "configs": {}}
    try:
        for nome, extra in CONFIGS.items():
            print(f"  medindo {nome} ...", file=sys.stderr, flush=True)
            m = roda(dict(extra))
            m["head"] = h
            res["configs"][nome] = m
            print(f"    -> hit1={m.get('hit1')} hit10={m.get('hit10')} "
                  f"mrr={m.get('mrr')} nunca={m.get('nunca_recuperado')}", file=sys.stderr, flush=True)
    finally:
        if os.path.exists(bak):
            shutil.move(bak, SUM)

    # n_docs tem de ser o MESMO nas configuracoes com fonte ligada (mesmo corpus).
    ligadas = {n: c.get("n_docs") for n, c in res["configs"].items()
               if n != "dense_off" and "erro" not in c}
    res["n_docs_por_config"] = ligadas
    res["n_docs_consistente"] = len(set(ligadas.values())) <= 1

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)

    print(f"HEAD={h}")
    for n, c in res["configs"].items():
        if "erro" in c:
            print(f"  {n}: ERRO {c['erro']}")
        else:
            print(f"  {n}: hit1={c['hit1']} hit3={c['hit3']} hit5={c['hit5']} "
                  f"hit10={c['hit10']} mrr={c['mrr']} nunca={c['nunca_recuperado']}")
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
