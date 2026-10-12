#!/usr/bin/env python3
"""gate_honest_splits.py — re-verifica os splits de forma INDEPENDENTE e quantifica
quanto o arranjo ANTIGO estava vazado.

Nao confia no `build_honest_splits.py`: le os arquivos gravados e recomputa as
interseccoes do zero. Um gate que so' acredita em quem gerou o artefato nao e' um gate.

Duas perguntas:
  A. Os splits gravados sao realmente disjuntos em pergunta e claim?   (fail-closed)
  B. QUANTO o conjunto antigo estava vazado?                           (magnitude)

A resposta de B e' o numero que faltava no projeto: que fracao das perguntas de teste do
arranjo antigo tinha a mesma EVIDENCIA de alguma pergunta de treino. Sem esse numero, o
"agregado" antigo nao era interpretavel.

Uso: python3 scripts/gate_honest_splits.py [--variant honest_v1]
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "scripts"))

from build_honest_splits import norm  # noqa: E402


def le(p: Path):
    out = []
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def claims(rows):
    s = set()
    for r in rows:
        s |= set(r.get("relevant_claim_ids", []) or [])
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="honest_v1")
    args = ap.parse_args()

    base = REPO / "data" / "eval" / "splits" / args.variant
    treino = le(base / "train.jsonl")
    teste = le(base / "test.jsonl")
    if not treino or not teste:
        print(f"ERRO: splits nao encontrados em {base}")
        return 2

    qtr = {norm(r["question"]) for r in treino}
    qte = {norm(r["question"]) for r in teste}
    ctr, cte = claims(treino), claims(teste)
    rtr = {r.get("runbook_ref") for r in treino if r.get("runbook_ref")}
    rte = {r.get("runbook_ref") for r in teste if r.get("runbook_ref")}

    viol = []
    print("=== A. DISJUNCAO RE-VERIFICADA (independente do builder) ===")
    print(f"  variante: {args.variant}")
    print(f"  treino {len(treino)} perguntas | teste {len(teste)} perguntas")
    print(f"  pergunta: INTERSECCAO {len(qtr & qte)}")
    print(f"  claim:    INTERSECCAO {len(ctr & cte)}")
    print(f"  runbook:  INTERSECCAO {len(rtr & rte)}")
    if qtr & qte:
        viol.append(f"pergunta repetida treino/teste: {len(qtr & qte)}")
    if ctr & cte:
        viol.append(f"claim compartilhada treino/teste: {len(ctr & cte)}")

    # --- B. quanto o arranjo ANTIGO estava vazado -------------------------
    # O arranjo antigo era: "cada arquivo e' um conjunto de teste". A "referencia" era o
    # proprio conjunto acumulado. A pergunta honesta e': para cada pergunta de um arquivo,
    # alguma pergunta de QUALQUER OUTRO arquivo compartilha a evidencia? Se sim, o par
    # treino/teste implicito esta' vazado.
    print()
    print("=== B. QUANTO O ARRANJO ANTIGO ESTAVA VAZADO ===")
    from build_honest_splits import IN_DIR
    por_arq = collections.defaultdict(list)
    for name in sorted(p for p in __import__("os").listdir(IN_DIR) if p.endswith(".jsonl")):
        if "negatives" in name:
            continue
        por_arq[name] = le(IN_DIR / name)

    # dedup global por texto, mantendo a primeira ocorrencia (mesma regra do builder)
    visto = {}
    for name in sorted(por_arq):
        for r in por_arq[name]:
            q = norm(r.get("question", ""))
            if q and q not in visto:
                visto[q] = (name, r)
    print(f"  perguntas distintas no total: {len(visto)}")

    # para cada pergunta, a evidencia dela aparece em pergunta de OUTRO arquivo?
    claim_to_files = collections.defaultdict(set)
    for q, (name, r) in visto.items():
        for cid in r.get("relevant_claim_ids", []) or []:
            claim_to_files[cid].add(name)

    vazadas = 0
    for q, (name, r) in visto.items():
        cs = set(r.get("relevant_claim_ids", []) or [])
        for cid in cs:
            if claim_to_files[cid] - {name}:
                vazadas += 1
                break
    pct = 100.0 * vazadas / max(1, len(visto))
    print(f"  perguntas cuja EVIDENCIA tambem aparece em outro arquivo: {vazadas}/{len(visto)} ({pct:.1f}%)")
    print(f"  -> no arranjo antigo, {pct:.1f}% das perguntas 'de teste' tinham evidencia "
          f"compartilhada com outra particao.")
    print(f"  -> nos splits novos, essa fracao e' {100.0 * len(ctr & cte) / max(1, len(ctr | cte)):.1f}% "
          f"(por construcao, 0 em numero absoluto: {len(ctr & cte)}).")

    print()
    print("  VEREDITO:", "PASS" if not viol else "FAIL")
    for v in viol:
        print("    [FAIL] " + v)
    if not viol:
        print("    [PASS] splits disjuntos em pergunta e claim, verificado do zero")
    return 0 if not viol else 1


if __name__ == "__main__":
    sys.exit(main())
