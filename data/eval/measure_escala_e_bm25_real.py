"""BM25 REAL x escala adaptativa do 2o estagio.

POR QUE ESTA COMBINACAO: as tres hipoteses de boost foram falsificadas por medicao
(avg_dl real: -4/-3/-2; bonus adaptativo sozinho: -2/0/0; prior de tipo flat: -5/-3/-2).
O que sobra e' a SIMILARIDADE BASE, e o repo ja' mediu que ali ha' ganho: ligar
RAG_BM25_REAL=1 faz o @10 do 1o estagio ir de 0,832 para 0,885 em blind_v3, MAS o
resultado final fica em 0,844 - porque as constantes fixas do 2o estagio (+8..+55) pesam
~10x menos quando o score de topo passa de ~1-5 para ~10-40 ("o ganho do 1o estagio fica
MASCARADO pelo 2o").

Ou seja: o defeito de escala que o repo descreve e' exatamente o que `RAG_RERANK_ADAPT`
existe para corrigir, agora acoplado ao 1o estagio que tem similaridade de verdade.

Matriz: RAG_BM25_REAL {0,1} x RAG_RERANK_ADAPT {off, K}. Transferencia cobrada em 2+
benchmarks; sem p<0,05 nao conta como ganho.
"""
import json
import math
import os
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HARNESS = os.path.join(REPO, "data/eval/evaluate_rag_benchmark.py")
PY = "/tmp/ragexp/venv/bin/python"
TMP = os.environ.get("RAG_OUT", "/tmp/ragexp/combo")
os.makedirs(TMP, exist_ok=True)

BENCHS = [
    ("pool423", os.path.join(REPO, "data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl")),
    ("blind_v3", os.path.join(REPO, "data/eval/decontaminated/blind_v3_slices.jsonl")),
    ("golden_qa", os.path.join(REPO, "data/eval/decontaminated/golden_qa_benchmark.jsonl")),
]
KS = [None, 1.0, 2.0, 4.0, 8.0]


def roda(bench, real, k, rot):
    env = dict(os.environ)
    env.update(PYTHONHASHSEED="0", RAG_INGEST_REST_API="1", RAG_DENSE_MASK_TO_CORPUS="1",
               RAG_BENCHMARK_FILE=bench)
    if real:
        env["RAG_BM25_REAL"] = "1"
    else:
        env.pop("RAG_BM25_REAL", None)
    if k is not None:
        env["RAG_RERANK_ADAPT"] = str(k)
    else:
        env.pop("RAG_RERANK_ADAPT", None)
    rot2 = "%s_r%d_a%s" % (rot, real, k)
    with open(os.path.join(TMP, rot2 + ".log"), "w") as fh:
        subprocess.run([PY, HARNESS], env=env, stdout=fh, stderr=subprocess.STDOUT)
    res = os.path.join(TMP, rot2 + ".json")
    subprocess.run(["cp", os.path.join(REPO, "data/eval/eval_summary.json"), res])
    d = json.load(open(res))
    return [x.get("rank") for x in d["details"]]


def mcnemar(a, b):
    ganha = sum(1 for x, y in zip(a, b) if y == 1 and x != 1)
    perde = sum(1 for x, y in zip(a, b) if x == 1 and y != 1)
    n = ganha + perde
    if n == 0:
        return 0, 0, 1.0
    p = 2.0 * sum(math.comb(n, k) for k in range(0, min(ganha, perde) + 1)) / (2.0 ** n)
    return perde, ganha, min(1.0, p)


def a1(rs):
    return sum(1 for r in rs if r == 1)


def a5(rs):
    return sum(1 for r in rs if r is not None and r <= 5)


def main():
    out = {}
    for nome, bench in BENCHS:
        if not os.path.exists(bench):
            print("!! faltando %s" % bench)
            continue
        print("\n=== %s ===" % nome)
        base = roda(bench, 0, None, nome)   # controle do repo
        n = len(base)
        print("  CONTROLE (legado, sem adapt)     @1 %3d/%d (%5.1f%%)  @5 %3d"
              % (a1(base), n, 100 * a1(base) / n, a5(base)))
        out[nome] = {}
        for real in (0, 1):
            for k in KS:
                if real == 0 and k is None:
                    continue
                r = roda(bench, real, k, nome)
                perde, ganha, p = mcnemar(base, r)
                marca = "SIG" if p < 0.05 else ""
                tag = "REAL" if real else "leg "
                print("  %s adapt=%-5s @1 %3d/%d (%5.1f%%) @5 %3d  delta@1 %+3d  ganha %2d perde %2d p=%.4f %s"
                      % (tag, k, a1(r), n, 100 * a1(r) / n, a5(r), a1(r) - a1(base),
                         ganha, perde, p, marca))
                out[nome]["r%d_a%s" % (real, k)] = {"a1": a1(r), "a5": a5(r), "n": n,
                                                    "ganha": ganha, "perde": perde, "p": p}
    json.dump(out, open("/tmp/ragexp/combo_resultado.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
