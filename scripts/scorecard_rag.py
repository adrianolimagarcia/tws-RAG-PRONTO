#!/usr/bin/env python3
"""Scorecard consolidado do RAG: um numero por conjunto, sem escolher a dedo.

POR QUE EXISTE
  As medicoes estao espalhadas em evidencias de varias datas e corpora, e cada uma
  responde a uma pergunta diferente. Sem uma tabela unica, "qual o score do RAG?" nao
  tem resposta - e o risco e' citar o numero que favorece.

CONFIGURACOES
  producao   : replica do pipeline em uso (RRF denso+esparso -> top-20 -> rerank top_n=15)
  lexical_re : lexical -> rerank top_n=15, SEM fusao (a variante que as medicoes
               apontaram como melhor no corpus geral)
  lexical    : lexical puro, sem rerank (referencia do que a 2a etapa acrescenta)
  denso      : ramo denso puro (so' onde o corpus justifica; carrega o modelo)

Tudo com RAG_MEASURE_EXCLUDE_EVIDENCE=1 (corpus congelado) e, quando ha denso,
RAG_DENSE_MASK_TO_CORPUS=1 para os dois ramos verem o MESMO conjunto.

USO
    python3 scripts/scorecard_rag.py --out /tmp/scorecard.json
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

BASE = {"RAG_MEASURE_EXCLUDE_EVIDENCE": "1", "PYTHONHASHSEED": "0",
        "RAG_DENSE_MASK_TO_CORPUS": "1",
        "RAG_DENSE_INDEX": "data/indexes/corpus_bge_m3_v5.pt",
        "RAG_DENSE_META": "data/indexes/corpus_docs_meta_v5.json"}

CONFIGS = {
    "lexical": {},
    "lexical_re": {"RAG_RERANK_TOP": "15"},
    "producao": {"RAG_HYBRID": "1", "RAG_RERANK_TOP": "15"},
    "denso": {"RAG_DENSE_ONLY": "raw", "RAG_DENSE_TOP": "30"},
}

# (nome, caminho, precisa_denso, fonte_rest)
CONJUNTOS = [
    ("blind_v3_slices", "data/eval/blind_v3_slices.jsonl", True, False),
    ("golden_qa_70", "data/eval/golden_qa_benchmark.jsonl", True, False),
    ("holdout_100_unseen", "data/eval/holdout_100_unseen.jsonl", True, False),
    ("blind_holdout_50", "data/eval/blind_holdout_50_vault.jsonl", True, False),
    ("realistic_30", "data/eval/realistic_blind_holdout_30.jsonl", True, False),
    ("rest_ops_40", "data/eval/rest_api_benchmark_ops_40.jsonl", True, True),
]


def head() -> str:
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip()


def roda(bench: str, extra: dict, rest: bool) -> dict:
    env = dict(os.environ)
    env.update(BASE)
    env["RAG_BENCHMARK_FILE"] = bench
    if rest:
        env["RAG_INGEST_REST_API"] = "1"
        env["RAG_REST_GRANULARITY"] = "operation"
    env.update(extra)
    r = subprocess.run([PY, "data/eval/evaluate_rag_benchmark.py"], cwd=REPO, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"erro": f"rc={r.returncode}", "stderr": r.stderr[-200:]}
    n_docs = None
    for linha in r.stdout.splitlines():
        if "Total de documentos" in linha:
            n_docs = int(linha.split(":")[-1].strip())
            break
    d = json.load(open(SUM, encoding="utf-8"))
    return {"n_docs": n_docs, "total": d.get("total"),
            "hit1": d.get("hit_rate_at_1"), "hit3": d.get("hit_rate_at_3"),
            "hit5": d.get("hit_rate_at_5"), "hit10": d.get("hit_rate_at_10"),
            "hit15": d.get("hit_rate_at_15"), "recall15": d.get("recall_at_15"),
            "mrr": d.get("mrr")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--conjuntos", default="", help="lista separada por virgula; vazio = todos")
    args = ap.parse_args()

    sel = set(args.conjuntos.split(",")) if args.conjuntos else None
    bak = SUM + ".bak-scorecard"
    if os.path.exists(SUM):
        shutil.copy2(SUM, bak)
    h = head()
    res = {"head": h, "corpus": "congelado (RAG_MEASURE_EXCLUDE_EVIDENCE=1)", "conjuntos": {}}
    try:
        for nome, caminho, _precisa, rest in CONJUNTOS:
            if sel and nome not in sel:
                continue
            if not os.path.exists(os.path.join(REPO, caminho)):
                print(f"  AVISO: {caminho} nao existe, pulando", file=sys.stderr)
                continue
            res["conjuntos"][nome] = {"arquivo": caminho, "configs": {}}
            for nome_c, extra in CONFIGS.items():
                print(f"  {nome} / {nome_c} ...", file=sys.stderr, flush=True)
                res["conjuntos"][nome]["configs"][nome_c] = roda(caminho, dict(extra), rest)
    finally:
        if os.path.exists(bak):
            shutil.move(bak, SUM)

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2, default=str)

    print(f"HEAD={h}   corpus={res['corpus']}")
    print()
    print(f"{'conjunto':<22} {'cfg':<12} {'n':>5} {'n_docs':>7} {'@1':>7} {'@5':>7} {'@10':>7} {'@15':>7} {'rec15':>7} {'MRR':>8}")
    for nome, bloco in res["conjuntos"].items():
        for nome_c, m in bloco["configs"].items():
            if "erro" in m:
                print(f"{nome:<22} {nome_c:<12} ERRO {m['erro']}")
                continue
            print(f"{nome:<22} {nome_c:<12} {str(m['total']):>5} {str(m['n_docs']):>7} "
                  f"{m['hit1']:>7.3f} {m['hit5']:>7.3f} {m['hit10']:>7.3f} {m['hit15']:>7.3f} "
                  f"{m['recall15']:>7.3f} {m['mrr']:>8.4f}")
        print()
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
