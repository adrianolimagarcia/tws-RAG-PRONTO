#!/usr/bin/env python3
"""Compara os modos densos do MCP de producao no pool de 423, ponte OFF.

Roda o caminho REAL de producao (mcp_server.handle_tool_call) em tres configuracoes e
reporta metrica geral, por fatia e o teste pareado (McNemar exato) contra o modo off.

    off    : BM25 puro (comportamento de sempre)
    fuse   : RRF k=60 denso+esparso, identico ao laboratorio
    route  : denso vira o recuperador quando a consulta parece de superficie de API

O pareado e' indexado pela POSICAO DA LINHA: o pool tem 423 linhas mas 413 ids (10 rotulos
blind-XXXX sao reusados por perguntas distintas). Indexar por id colapsaria 10 linhas.

Uso: python3 data/eval/measure_denso_mcp.py
"""
import json
import math
import os
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
POOL = os.environ.get("RAG_POOL", "/tmp/ragexp/pool_recon.jsonl")
SAIDA = "/tmp/ragexp/denso_modos"
PY = os.environ.get("RAG_PY", sys.executable)

ROTEADOR = '''# quantas perguntas do pool o detector de fatia aciona
import json, re, sys
sys.path.insert(0, "mcp_server")
import tws_expert_mcp as m
itens = [json.loads(l) for l in open("%s", encoding="utf-8") if l.strip()]
n = sum(1 for o in itens if m._e_fatia_api(o["question"]))
por_fatia = {}
for i, o in enumerate(itens):
    g = str(o["id"]).split("-")[0]
    d = por_fatia.setdefault(g, [0, 0]); d[1] += 1
    if m._e_fatia_api(o["question"]): d[0] += 1
print(json.dumps({"total": n, "n": len(itens), "por_fatia": por_fatia}))
''' % POOL


def roda(modo):
    os.makedirs(SAIDA, exist_ok=True)
    env = dict(os.environ)
    env["RAG_DENSE_MODE"] = modo
    env["RAG_TRADUZ_EN"] = "0"
    env["RAG_OUT"] = os.path.join(SAIDA, "modo_%s.json" % modo)
    t0 = time.time()
    r = subprocess.run([PY, "data/eval/measure_producao_pool423.py"],
                       env=env, capture_output=True, text=True)
    if r.returncode != 0:
        print("  [%s] FALHOU:\n%s" % (modo, (r.stderr or r.stdout)[-1500:]))
        return None
    linhas = [l for l in r.stdout.splitlines() if "Hit@" in l or "MRR" in l]
    print("  [%s] %s  (%.0fs)" % (modo, " | ".join(x.strip() for x in linhas), time.time() - t0))
    return json.load(open(env["RAG_OUT"]))["ranks"]


def metricas(ranks):
    by = {d["linha"]: d for d in ranks}
    n = len(by)
    def hit(k):
        return sum(1 for d in by.values() if d["rank"] is not None and d["rank"] <= k)
    mrr = sum(1.0 / d["rank"] for d in by.values() if d["rank"] is not None) / n
    return by, hit, mrr, n


def mcnemar(A, B, k):
    """McNemar exato bicaudal. A = base, B = novo."""
    ids = sorted(set(A) & set(B))
    def h(d, kk):
        return d["rank"] is not None and d["rank"] <= kk
    g = sum(1 for i in ids if h(B[i], k) and not h(A[i], k))
    p = sum(1 for i in ids if h(A[i], k) and not h(B[i], k))
    n = g + p
    if n == 0:
        return g, p, 1.0
    pv = min(1.0, 2.0 * sum(math.comb(n, j) for j in range(0, min(g, p) + 1)) / (2.0 ** n))
    return g, p, pv


def main():
    if not os.path.exists(POOL):
        raise SystemExit("pool nao encontrado: %s" % POOL)

    print("=== quantas perguntas o detector de fatia aciona ===")
    r = subprocess.run([PY, "-c", ROTEADOR], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        info = json.loads(r.stdout.strip().splitlines()[-1])
        print("  %d de %d perguntas (%.1f%%)" % (info["total"], info["n"],
                                                 100.0 * info["total"] / info["n"]))
        for g, (d, t) in sorted(info["por_fatia"].items()):
            print("     %-7s %2d/%2d" % (g, d, t))
    else:
        print("  (nao foi possivel medir o roteador)")

    print("\n=== medindo os tres modos ===")
    res = {}
    for modo in ("off", "fuse", "route", "fuse_route"):
        res[modo] = roda(modo)
    if not res.get("off"):
        raise SystemExit("o modo off falhou; sem base de comparacao")

    base, hb, mb, n = metricas(res["off"])
    print("\n=== resultado (pool de %d linhas) ===" % n)
    print("  %-8s %7s %7s %9s" % ("modo", "@1", "@5", "MRR"))
    for modo in ("off", "fuse", "route", "fuse_route"):
        if not res[modo]:
            continue
        by, h, m, _ = metricas(res[modo])
        print("  %-8s %3d (%4.1f%%) %3d  %.4f" % (modo, h(1), 100.0 * h(1) / n, h(5), m))

    print("\n=== pareado contra off (McNemar exato) ===")
    for modo in ("fuse", "route", "fuse_route"):
        if not res[modo]:
            continue
        novo, _, _, _ = metricas(res[modo])
        print("  off -> %s" % modo)
        for k in (1, 5, 10):
            g, p, pv = mcnemar(base, novo, k)
            print("     @%-2d ganha %3d / perde %3d  p=%.4f%s"
                  % (k, g, p, pv, "  SIGNIFICATIVO" if pv < 0.05 else ""))

    print("\n=== por fatia (@1 / @5), off -> route ===")
    if res["route"]:
        novo, hr, _, _ = metricas(res["route"])
        grupos = {}
        for i, d in base.items():
            grupos.setdefault(str(d["id"]).split("-")[0], []).append(i)
        print("  %-8s %14s %14s" % ("fatia", "off", "route"))
        for g in sorted(grupos):
            sel = grupos[g]
            a1 = sum(1 for i in sel if base[i]["rank"] is not None and base[i]["rank"] <= 1)
            a5 = sum(1 for i in sel if base[i]["rank"] is not None and base[i]["rank"] <= 5)
            b1 = sum(1 for i in sel if novo[i]["rank"] is not None and novo[i]["rank"] <= 1)
            b5 = sum(1 for i in sel if novo[i]["rank"] is not None and novo[i]["rank"] <= 5)
            print("  %-8s %5d/%2d @1 %5d/%2d @5   %5d/%2d @1 %5d/%2d @5"
                  % (g, a1, len(sel), a5, len(sel), b1, len(sel), b5, len(sel)))


if __name__ == "__main__":
    main()
