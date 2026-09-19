#!/usr/bin/env python3
"""Roda um par A/B do evaluator e guarda os dois summaries lado a lado.

Motivo: `eval_summary.json` e' sobrescrito a cada rodada, entao a comparacao A/B
perde o braco A se os dois rodarem em sequencia sem copia. Este script roda os dois
bracos, copia cada summary e imprime o diff das metricas principais.

O gate (`scripts/gate_rag_v4.py --run-a --run-b`) consome os dois arquivos.

Uso:
  scripts/ab_experiment.py --benchmark data/eval/blind_v3_slices.jsonl \
      --a "" --b "RAG_DROP_SYNTHETIC=1" --rotulo-a baseline --rotulo-b sem-synthetic
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PY = sys.executable


def roda(benchmark: Path, env_extra: dict[str, str], destino: Path) -> dict:
    env = dict(os.environ)
    env.update({
        "PYTHONHASHSEED": "0",
        "RAG_MEASURE_EXCLUDE_EVIDENCE": "1",
        "RAG_INGEST_REST_API": "1",
        "RAG_BENCHMARK_FILE": str(benchmark),
    })
    # limpa as ablacoes antes de aplicar as do braco, para nao vazar config entre bracos
    for k in ("RAG_DROP_SYNTHETIC", "RAG_DROP_CTXPREFIX", "RAG_SCORER"):
        env.pop(k, None)
    env.update(env_extra)

    p = subprocess.run([PY, "data/eval/evaluate_rag_benchmark.py"],
                       cwd=str(REPO), env=env, capture_output=True, text=True)
    if p.returncode != 0:
        print(f"  ERRO na rodada: rc={p.returncode}")
        print((p.stderr or "")[-800:])
        raise SystemExit(1)

    origem = REPO / "data" / "eval" / "eval_summary.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(origem, destino)
    return json.loads(destino.read_text(encoding="utf-8"))


def resumo(d: dict) -> dict:
    return {
        "total": d.get("total"),
        "at_1": d.get("hit_rate_at_1"),
        "at_10": d.get("hit_rate_at_10"),
        "mrr": d.get("mrr"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--benchmark", default=str(REPO / "data" / "eval" / "blind_v3_slices.jsonl"))
    ap.add_argument("--a", default="", help="env do braco A, ex 'RAG_DROP_SYNTHETIC=1' (vazio = baseline)")
    ap.add_argument("--b", required=True, help="env do braco B")
    ap.add_argument("--rotulo-a", default="A")
    ap.add_argument("--rotulo-b", default="B")
    ap.add_argument("--saida", default="/tmp/ab")
    args = ap.parse_args()

    bench = Path(args.benchmark)
    if not bench.exists():
        print(f"benchmark nao existe: {bench}", file=sys.stderr)
        return 1
    saida = Path(args.saida)
    nome = bench.stem

    def parse(s: str) -> dict[str, str]:
        out = {}
        for par in [x for x in s.split(",") if x.strip()]:
            k, _, v = par.partition("=")
            out[k.strip()] = v.strip()
        return out

    print(f"benchmark: {bench.name}")
    print(f"  A ({args.rotulo_a}): {parse(args.a) or 'baseline (sem env extra)'}")
    print(f"  B ({args.rotulo_b}): {parse(args.b)}")
    print()

    print("  rodando A...")
    da = roda(bench, parse(args.a), saida / f"{nome}__A.json")
    print("  rodando B...")
    db = roda(bench, parse(args.b), saida / f"{nome}__B.json")

    ra, rb = resumo(da), resumo(db)
    print()
    print(f"=== {nome} ===")
    print(f"  {'metrica':<10} {args.rotulo_a:>14} {args.rotulo_b:>14}   delta")
    for k in ("total", "at_1", "at_10", "mrr"):
        va, vb = ra[k], rb[k]
        d = f"{vb - va:+.4f}" if isinstance(va, (int, float)) and isinstance(vb, (int, float)) else "-"
        print(f"  {k:<10} {str(va):>14} {str(vb):>14}   {d}")
    print()
    print(f"  summaries: {saida}/{nome}__A.json  e  __B.json")
    print(f"  proximo:  scripts/gate_rag_v4.py --run-a {saida}/{nome}__A.json "
          f"--run-b {saida}/{nome}__B.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
