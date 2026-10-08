#!/usr/bin/env python3
"""Compara off x fuse x gate no MESMO pool de 450, pelo PIOR conjunto (gate de promocao v4).

Uso: python3 data/eval/compara_gates.py /tmp/ragexp/verif /tmp/ragexp/verif_gate
"""
import glob
import json
import math
import os
import sys

ORDEM = ["off", "fuse", "gate_media", "gate_baixa"]
CONJS = ["geral_70", "mensagens", "virgem_expandido", "virgem+mensagens", "virgem_INGLES",
         "holdout_40", "holdout_qa_30", "realistico", "pure_virgin", "holdout_100"]


def carrega(dirs):
    dados = {}
    for d in dirs:
        for f in glob.glob(os.path.join(d, "*.json")):
            o = json.load(open(f))
            rot = o.get("rotulo") or o["modo"]
            dados.setdefault(rot, {})[o["conjunto"]] = {x["pos"]: x["rank"] for x in o["ranks"]}
    return dados


def hit(ranks, pos, k):
    r = ranks.get(pos)
    return r is not None and r <= k


def mcnemar(A, B, k, chaves):
    g = sum(1 for c, p in chaves if hit(B[c], p, k) and not hit(A[c], p, k))
    perde = sum(1 for c, p in chaves if hit(A[c], p, k) and not hit(B[c], p, k))
    n = g + perde
    if n == 0:
        return g, perde, 1.0
    pv = min(1.0, 2.0 * sum(math.comb(n, j) for j in range(0, min(g, perde) + 1)) / (2.0 ** n))
    return g, perde, pv


def main():
    dados = carrega(sys.argv[1:])
    base = dados["off"]
    print("=== RESULTADO POR CONJUNTO (Hit@1 e Hit@5) ===")
    print("%-18s %s" % ("conjunto", "".join("%14s" % r for r in ORDEM)))
    for c in CONJS:
        linha = []
        for r in ORDEM:
            if c not in dados.get(r, {}):
                linha.append("%14s" % "-")
                continue
            D = dados[r][c]
            h1 = sum(1 for p in D if hit(D, p, 1))
            h5 = sum(1 for p in D if hit(D, p, 5))
            linha.append("%14s" % ("%d/%d" % (h1, h5)))
        print("%-18s %s" % (c, "".join(linha)))

    chaves = [(c, p) for c in CONJS if c in base
              for p in base[c] if all(c in dados.get(r, {}) and p in dados[r][c] for r in ORDEM)]

    print()
    print("=== AGREGADO (n=%d) ===" % len(chaves))
    print("%-8s %8s %8s %8s %8s" % ("modo", "@1", "@5", "@10", "MRR"))
    for r in ORDEM:
        D = {c: dados[r][c] for c in base}
        h1 = sum(1 for c, p in chaves if hit(D[c], p, 1))
        h5 = sum(1 for c, p in chaves if hit(D[c], p, 5))
        h10 = sum(1 for c, p in chaves if hit(D[c], p, 10))
        mrr = sum(1.0 / D[c][p] for c, p in chaves if D[c].get(p) is not None) / len(chaves)
        print("%-8s %8d %8d %8d %8.4f" % (r, h1, h5, h10, mrr))

    print()
    print("=== McNemar vs off (ganha/perde) e por CONJUNTO (o criterio do repo e' o PIOR) ===")
    for r in ORDEM[1:]:
        print("  %s:" % r)
        for k in (1, 5):
            g, p, pv = mcnemar(base, dados[r], k, chaves)
            print("    @%-2d global ganha %3d / perde %3d  p=%.4f %s"
                  % (k, g, p, pv, "SIG" if pv < 0.05 else ""))
        piores = []
        for c in CONJS:
            if c not in base:
                continue
            ch = [(c, p) for p in base[c] if p in dados[r][c]]
            g, p, pv = mcnemar(base, dados[r], 1, ch)
            delta = g - p
            if pv < 0.05 or delta < 0:
                piores.append((c, delta, pv))
        if not piores:
            print("    @1 por conjunto: NENHUM conjunto regride (nem significativo nem nominal)")
        for c, d, pv in sorted(piores, key=lambda x: x[1]):
            print("    @1 %-18s delta %+3d %s" % (c, d, "p=%.4f" % pv if pv < 0.05 else ""))


if __name__ == "__main__":
    main()
