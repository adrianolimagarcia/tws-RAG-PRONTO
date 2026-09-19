#!/usr/bin/env python3
"""Descontamina benchmarks: remove perguntas que VAZAM para dentro do indice.

Por que existe
--------------
O P0-B mediu que remover `synthetic_questions` do indice custa recall legitimo
(-2,67pt @1 em `blind_v3`, que tem zero tautologias). Logo a correcao nao e' no
indice -- e' no benchmark. Este script aplica a regra:

    nenhuma pergunta de benchmark pode ser (quase) identica a uma
    synthetic_question da PROPRIA claim relevante.

Ele consome o relatorio do `audit_eval_leakage.py` (--json) e escreve copias
filtradas em `data/eval/decontaminated/`. NAO altera os originais.

Escopo explicito (o que este script NAO faz)
--------------------------------------------
- NAO remove `7-split` (mesma pergunta em varios arquivos) nem `8-duplicata`
  (near-duplicate ENTRE arquivos): sao outro defeito (splits nao independentes),
  com correcao propria. Sao reportados como pendencia, nao silenciados.
- NAO remove `5-codigo` / `6-copia-da-claim` / `9-template` / `10-relevancia-ampla`
  (todos WARN ou de outra natureza).

Fail-closed: arquivo que ficaria vazio aborta com exit 2, em vez de gerar um
benchmark de zero perguntas que passaria em qualquer gate por vacuidade.

Uso:
    python scripts/decontaminate_benchmarks.py --leak-json rel.json [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVAL_DIR = REPO / "data" / "eval"
OUT_DEFAULT = EVAL_DIR / "decontaminated"

# Checks cujos achados de nivel FAIL marcam a pergunta como contaminada:
# 1-exato = identica a uma synthetic_question; 2-ngrama / 3-jaccard = quase.
CHECKS_CONTAMINANTES = ("1-exato", "2-ngrama", "3-jaccard")


def carrega_contaminadas(leak: dict) -> tuple[dict[str, set[str]], dict[str, int]]:
    """(arquivo -> {qid contaminado}) e contagem por check."""
    por_arquivo: dict[str, set[str]] = defaultdict(set)
    por_check: dict[str, int] = defaultdict(int)
    for a in leak.get("achados", []):
        if a.get("check") not in CHECKS_CONTAMINANTES:
            continue
        if a.get("nivel") != "FAIL":
            continue
        arq, qid = a.get("arquivo"), a.get("qid")
        if not arq or not qid:
            # achado sem campo estruturado: nao silenciar, abortar.
            raise SystemExit(
                f"ERRO: achado {a.get('check')} sem arquivo/qid estruturado — "
                f"rode a versao do audit_eval_leakage.py que emite esses campos")
        por_arquivo[arq].add(str(qid).split(":")[-1])
        por_check[a["check"]] += 1
    return por_arquivo, dict(por_check)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--leak-json", required=True, help="relatorio do audit_eval_leakage.py")
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    ap.add_argument("--benchmarks", nargs="*", default=None)
    args = ap.parse_args()

    leak = json.loads(Path(args.leak_json).read_text(encoding="utf-8"))
    contam, por_check = carrega_contaminadas(leak)

    if args.benchmarks:
        paths = [Path(p) for p in args.benchmarks]
    else:
        paths = sorted(EVAL_DIR.glob("*.jsonl"))
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  checks contaminantes (nivel FAIL): {por_check or 'nenhum'}")
    print()
    print(f"  {'benchmark':46} {'antes':>6} {'remov':>6} {'depois':>7}")
    total_antes = total_remov = 0
    pendentes = []
    for p in paths:
        linhas = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
        ruins = contam.get(p.name, set())
        mantidas = [d for d in linhas if str(d.get("id")) not in ruins]
        removidas = len(linhas) - len(mantidas)
        total_antes += len(linhas)
        total_remov += removidas

        if not mantidas and linhas:
            print(f"  ERRO: {p.name} ficaria com 0 de {len(linhas)} perguntas — abortando",
                  file=sys.stderr)
            return 2

        destino = out_dir / p.name
        with destino.open("w", encoding="utf-8") as fh:
            for d in mantidas:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        marca = "  <- LIMPO" if removidas == 0 and linhas else ""
        print(f"  {p.name:46} {len(linhas):>6} {removidas:>6} {len(mantidas):>7}{marca}")

    print()
    print(f"  total: {total_antes} -> {total_antes - total_remov} perguntas "
          f"({total_remov} removidas)")
    print(f"  destino: {out_dir.relative_to(REPO)}")

    # Pendencias explicitas: nao silenciar o que NAO foi corrigido.
    for a in leak.get("achados", []):
        if a.get("check") in ("7-split", "8-duplicata") and a.get("nivel") == "FAIL":
            pendentes.append(a["check"])
    if pendentes:
        from collections import Counter
        c = Counter(pendentes)
        print()
        print("  PENDENTE (nao corrigido por este script, por escopo):")
        for k, v in sorted(c.items()):
            print(f"    {k}: {v} achados FAIL — splits nao independentes / near-duplicata entre arquivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
