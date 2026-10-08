#!/usr/bin/env python3
"""Estatistica final da fusao densa na producao, ponte ON (o default do sistema).

Uso: python3 data/eval/final_fusao.py <off.json> <fuse.json>
"""
import json
import math
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS = os.path.join(RAIZ, "data/export/tws_corpus_master_consolidated.jsonl")
POOL = os.environ.get("RAG_POOL", "/tmp/ragexp/pool_recon.jsonl")


def ler(p):
    return {d["linha"]: d["rank"] for d in json.load(open(p))["ranks"]}


def acerta(D, i, k):
    r = D.get(i)
    return r is not None and r <= k


def mcnemar(A, B, sel, rot):
    partes = []
    for k in (1, 3, 5, 10):
        g = sum(1 for i in sel if acerta(B, i, k) and not acerta(A, i, k))
        p = sum(1 for i in sel if acerta(A, i, k) and not acerta(B, i, k))
        n = g + p
        pv = 1.0 if n == 0 else min(
            1.0, 2.0 * sum(math.comb(n, j) for j in range(0, min(g, p) + 1)) / (2.0 ** n))
        partes.append("@%d +%d/-%d p=%.4f%s" % (k, g, p, pv, "*" if pv < 0.05 else ""))
    ma = sum(1.0 / A[i] for i in sel if A.get(i) is not None) / len(sel)
    mb = sum(1.0 / B[i] for i in sel if B.get(i) is not None) / len(sel)
    print("  %-22s %s | MRR %+.4f" % (rot, " | ".join(partes), mb - ma))


def main():
    A = ler(sys.argv[1])
    B = ler(sys.argv[2])
    todos = sorted(set(A) & set(B))

    print("=== a troca que a producao vera (mesma ponte nos dois lados) ===")
    for nome, D in (("off", A), ("fuse", B)):
        print("  %-5s @1 %3d | @3 %3d | @5 %3d | @10 %3d"
              % (nome, *[sum(1 for i in todos if acerta(D, i, k)) for k in (1, 3, 5, 10)]))
    mcnemar(A, B, todos, "todos (n=%d)" % len(todos))

    # subconjunto limpo: criterio do repo (maior n-grama contiguo pergunta<->alvo <= 4)
    corpus = {}
    for linha in open(CORPUS, encoding="utf-8"):
        if linha.strip():
            o = json.loads(linha)
            corpus[o["claim_id"]] = " ".join(
                [o.get("claim", ""), o.get("context_prefix", "")]
                + list(o.get("synthetic_questions") or []))
    pool = [json.loads(l) for l in open(POOL, encoding="utf-8") if l.strip()]

    def ngr(s, n):
        w = re.findall(r"\w+", s.lower())
        return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

    limpos = []
    for i in todos:
        if i >= len(pool):
            continue
        alvos = [corpus[c] for c in (pool[i].get("relevant_claim_ids") or []) if c in corpus]
        mx = 0
        if alvos:
            for n in range(2, 16):
                if any(ngr(pool[i]["question"], n) & ngr(t, n) for t in alvos):
                    mx = n
                else:
                    break
        if mx <= 4:
            limpos.append(i)
    mcnemar(A, B, limpos, "limpo (n=%d)" % len(limpos))

    restops = [i for i in todos
               if i < len(pool) and str(pool[i]["id"]).split("-")[0] in ("rest", "ops")]
    mcnemar(A, B, restops, "rest+ops (n=%d)" % len(restops))


if __name__ == "__main__":
    main()
