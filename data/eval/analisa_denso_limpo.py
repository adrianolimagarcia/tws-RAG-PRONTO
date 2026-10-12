#!/usr/bin/env python3
"""Compara modos densos do MCP no pool 423, reportando TAMBEM o subconjunto LIMPO.

Por que o subconjunto limpo importa: o pool e' HETEROGENEO em vazamento. Medido pelo criterio
que o proprio repo usa (maior n-grama contiguo pergunta<->alvo <= 4), a fatia `vault` tem
mediana 15 (pergunta praticamente literal) e `v3`/`eval` chegam a 15, enquanto `ops` e `rest`
sao limpas por construcao (mediana 0,0). Um ganho medido no pool inteiro pode ser so' o denso
espelhando texto que o BM25 precisa casar literalmente.

Uso: python3 data/eval/analisa_denso_limpo.py
"""
import json
import math
import os
import re
import statistics as st

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS = os.path.join(RAIZ, "data/export/tws_corpus_master_consolidated.jsonl")
POOL = os.environ.get("RAG_POOL", "/tmp/ragexp/pool_recon.jsonl")
MODOS = os.environ.get("RAG_MODOS_DIR", "/tmp/ragexp/denso_modos")


def ngramas(texto, n):
    w = re.findall(r"\w+", texto.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def maior_ngrama(pergunta, alvos):
    """Maior n contiguo compartilhado entre a pergunta e QUALQUER documento-alvo."""
    for n in range(2, 16):
        if not any(ngramas(pergunta, n) & ngramas(t, n) for t in alvos):
            return n - 1
    return 15


def alturas(m):
    """{linha: rank} a partir do arquivo de uma corrida. Preserva None (alvo ausente)."""
    dados = json.load(open(os.path.join(MODOS, "modo_%s.json" % m), encoding="utf-8"))
    # Indexar pela LINHA: o pool tem 423 linhas e 413 ids (10 rotulos blind-XXXX repetidos
    # entre perguntas DISTINTAS). Por id, 10 linhas seriam colapsadas.
    return {d["linha"]: d["rank"] for d in dados["ranks"]}


def acerta(ranks, linha, k):
    r = ranks.get(linha)
    return r is not None and r <= k


def mcnemar(A, B, sel, rot):
    def wins(k):
        g = sum(1 for i in sel if acerta(B, i, k) and not acerta(A, i, k))
        p = sum(1 for i in sel if acerta(A, i, k) and not acerta(B, i, k))
        n = g + p
        if n == 0:
            return g, p, 1.0
        pv = min(1.0, 2.0 * sum(math.comb(n, j) for j in range(0, min(g, p) + 1))
                 / (2.0 ** n))
        return g, p, pv
    partes = []
    for k in (1, 5, 10):
        g, p, pv = wins(k)
        partes.append("@%d +%d/-%d p=%.4f%s" % (k, g, p, pv, "*" if pv < 0.05 else ""))
    mrr_a = sum(1.0 / A[i] for i in sel if A.get(i) is not None) / len(sel)
    mrr_b = sum(1.0 / B[i] for i in sel if B.get(i) is not None) / len(sel)
    print("  %-24s %s | MRR %+.4f" % (rot, " | ".join(partes), mrr_b - mrr_a))


def main():
    corpus = {}
    for linha in open(CORPUS, encoding="utf-8"):
        if linha.strip():
            o = json.loads(linha)
            corpus[o["claim_id"]] = " ".join(
                [o.get("claim", ""), o.get("context_prefix", "")]
                + list(o.get("synthetic_questions") or []))
    pool = [json.loads(l) for l in open(POOL, encoding="utf-8") if l.strip()]

    vaz = {}
    for i, o in enumerate(pool):
        alvos = [corpus[c] for c in (o.get("relevant_claim_ids") or []) if c in corpus]
        vaz[i] = maior_ngrama(o["question"], alvos) if alvos else 0

    print("=== vazamento do pool (maior n-grama pergunta<->alvo; repo usa <=4 como limpo) ===")
    limpos = [i for i in range(len(pool)) if vaz[i] <= 4]
    print("  limpo: %d de %d | mediana geral %.1f | max %d"
          % (len(limpos), len(pool), st.median(vaz.values()), max(vaz.values())))
    porfat = {}
    for i, o in enumerate(pool):
        porfat.setdefault(str(o["id"]).split("-")[0], []).append(vaz[i])
    for k in sorted(porfat):
        print("     %-8s n=%3d mediana %5.1f max %2d"
              % (k, len(porfat[k]), st.median(porfat[k]), max(porfat[k])))

    off, fuse, route = alturas("off"), alturas("fuse"), alturas("route")
    todos = list(range(len(pool)))
    restops = [i for i, o in enumerate(pool)
               if str(o["id"]).split("-")[0] in ("rest", "ops")]

    for nome, sel in (("POOL INTEIRO", todos),
                      ("LIMPO (n-grama<=4)", limpos),
                      ("rest+ops (limpo)", restops)):
        print("\n=== %s  (n=%d) ===" % (nome, len(sel)))
        for modo, R in (("fuse", fuse), ("route", route)):
            mcnemar(off, R, sel, "off -> %s" % modo)

    print("\n=== por fatia, off -> fuse (@1 / @5) ===")
    grupos = {}
    for i, o in enumerate(pool):
        grupos.setdefault(str(o["id"]).split("-")[0], []).append(i)
    print("  %-8s %14s %14s" % ("fatia", "off", "fuse"))
    for k in sorted(grupos):
        s = grupos[k]
        a1 = sum(1 for i in s if acerta(off, i, 1))
        a5 = sum(1 for i in s if acerta(off, i, 5))
        b1 = sum(1 for i in s if acerta(fuse, i, 1))
        b5 = sum(1 for i in s if acerta(fuse, i, 5))
        print("  %-8s %4d/%2d %4d/%2d   %4d/%2d %4d/%2d"
              % (k, a1, len(s), a5, len(s), b1, len(s), b5, len(s)))


if __name__ == "__main__":
    main()
