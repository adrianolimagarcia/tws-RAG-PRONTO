#!/usr/bin/env python3
"""measure_dense_fusion_gain.py — mede a fusao densa pelo HARNESS REAL e testa significancia.

POR QUE ISTO SUBSTITUI a medicao anterior (`measure_confidence_gated_fusion.py`, removida)
--------------------------------------------------------------------------------------
A primeira tentativa reimplementava o topo do pipeline (BM25 + margem) num script proprio
e comparava com o harness "por fora". Isso deu dois numeros INCOMPATIVEIS para o mesmo
conjunto e o MESMO caminho lexical:
    harness          : 192/423
    reimplementacao  : 220/423
E a reimplementacao nao tinha o 2o estagio de ID (+45/+55 para codigo de erro), que e' o
que resolve os casos de mensagem. Toda conclusao tirada dessa base estava errada, incluindo
a manchete "+30 @1". Este script mede SO' pelo harness, que reproduz o baseline gravado
(Hit@5 287, MRR 0,6016) bit a bit.

O QUE ELE MEDE
--------------
Para cada conjunto, roda o harness DUAS vezes (lexical puro e RAG_HYBRID=1) e compara
PERGUNTA A PERGUNTA, nao so' o total: o total esconde que a fusao pode ganhar 9 e perder 1
(ganho real) ou ganhar 15 e perder 44 (regressao real). Aplica McNemar EXATO nas
discordancias - sem isso, "+2 em 24 perguntas" nao e' prova de nada.

USO
    python3 data/eval/measure_dense_fusion_gain.py [conjunto.jsonl ...]
Requer HF_HOME apontando para um cache com BGE-M3 e o indice denso v6 presente.
"""
import os
import re
import sys
import json
import math
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HARNESS = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")
PY = os.environ.get("RAG_PY", sys.executable)
TMP = os.environ.get("RAG_FUSION_TMP", "/tmp/ragexp")


def latencia_extra_ms(caminho, n_amostras=8):
    """Custo do ramo denso por consulta: carrega o modelo uma vez e cronometra.

    O modelo e' carregado FORA da medicao; so' o encode da query + o produto contra a
    matriz entra na conta. E' esse delta que a producao pagaria por consulta.
    """
    import time
    sys.path.insert(0, os.path.join(REPO, "data", "eval"))
    sys.path.insert(0, REPO)
    os.environ["RAG_DENSE_MASK_TO_CORPUS"] = "1"
    import evaluate_rag_benchmark as eng

    eng._dense_init()
    qs = []
    for l in open(caminho, encoding="utf-8"):
        if l.strip():
            o = json.loads(l)
            if o.get("question"):
                qs.append(o["question"])
        if len(qs) >= n_amostras:
            break
    if not qs:
        return None
    eng._dense_top30(qs[0], 30)  # aquecimento (aloca matriz, cache de tokenizacao)
    t0 = time.perf_counter()
    for q in qs:
        eng._dense_top30(q, 30)
    return 1000.0 * (time.perf_counter() - t0) / len(qs)


def roda(caminho, modo, rotulo):
    """Roda o harness em 'lex' (puro) ou 'hyb' (RAG_HYBRID=1) e devolve os detalhes."""
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    env["RAG_INGEST_REST_API"] = "1"
    env["RAG_BENCHMARK_FILE"] = caminho
    if modo == "hyb":
        env["RAG_HYBRID"] = "1"
        env["RAG_RRF_W"] = os.environ.get("RAG_RRF_W", "0.75")
        env["RAG_DENSE_MASK_TO_CORPUS"] = "1"
        env["HF_HOME"] = os.environ.get("HF_HOME", "/tmp/ragexp/hfhome")
        env["HF_HUB_OFFLINE"] = "1"
        env["TRANSFORMERS_OFFLINE"] = "1"
    log = os.path.join(TMP, "fus_%s_%s.log" % (rotulo.replace("/", "_"), modo))
    with open(log, "w") as fh:
        subprocess.run([PY, HARNESS], env=env, stdout=fh, stderr=subprocess.STDOUT)
    d = json.load(open(os.path.join(REPO, "data/eval/eval_summary.json")))
    return {x["id"]: x for x in d["details"]}


def mcnemar_exato(lex, fus):
    """Teste de McNemar EXATO (binomial bilateral) sobre as discordancias de Hit@1."""
    so_lex = so_fus = 0
    for i in set(lex) & set(fus):
        a = lex[i].get("rank") == 1
        b = fus[i].get("rank") == 1
        if a and not b:
            so_lex += 1
        elif b and not a:
            so_fus += 1
    n = so_lex + so_fus
    if n == 0:
        return so_lex, so_fus, 1.0
    k = min(so_lex, so_fus)
    p = 2.0 * sum(math.comb(n, j) for j in range(k + 1)) / (2.0 ** n)
    return so_lex, so_fus, min(1.0, p)


def por_faixa(lex, fus):
    out = []
    for f in ("alta", "media", "baixa"):
        ids = [i for i in lex if i in fus and lex[i].get("confianca") == f]
        if not ids:
            continue
        a = sum(1 for i in ids if lex[i].get("rank") == 1)
        b = sum(1 for i in ids if fus[i].get("rank") == 1)
        out.append((f, len(ids), a, b))
    return out


CONJUNTOS = [
    ("data/eval/decontaminated/golden_qa_virgin_benchmark.jsonl",
     "golden_qa_virgin (pergunta humana PT)"),
    ("data/eval/decontaminated/golden_qa_virgin_en_benchmark.jsonl",
     "golden_qa_virgin EN (pergunta humana em ingles)"),
    ("data/eval/decontaminated/golden_qa_messages_benchmark.jsonl",
     "golden_qa_messages (pergunta humana, codigo de erro)"),
    ("data/eval/decontaminated/pure_virgin_test_40.jsonl", "pure_virgin_test_40"),
    ("data/eval/decontaminated/blind_holdout_qa_30.jsonl", "blind_holdout_qa_30"),
    ("data/eval/decontaminated/blind_v3_slices.jsonl", "blind_v3_slices (controle sintetico)"),
    (os.environ.get("RAG_FUSION_POOL", "/tmp/ragexp/attrib3/pool.jsonl"),
     "POOL 423 (benchmark de producao)"),
]


def main():
    apenas = sys.argv[1:]
    os.makedirs(TMP, exist_ok=True)
    print("=" * 96)
    print("FUSAO DENSA MEDIDA PELO HARNESS REAL (nao por reimplementacao)")
    print("=" * 96)
    print("%-46s %10s %10s %7s %9s" % ("conjunto", "lexical", "fusao", "delta", "McNemar p"))
    print("-" * 96)
    for rel, rot in CONJUNTOS:
        caminho = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
        if apenas and not any(a in caminho for a in apenas):
            continue
        if not os.path.exists(caminho):
            print("%-46s (ausente)" % rot[:46])
            continue
        lex = roda(caminho, "lex", rot)
        fus = roda(caminho, "hyb", rot)
        l1 = sum(1 for x in lex.values() if x.get("rank") == 1)
        f1 = sum(1 for x in fus.values() if x.get("rank") == 1)
        n = len(lex)
        so_lex, so_fus, p = mcnemar_exato(lex, fus)
        marca = ""
        if p < 0.05:
            marca = " REGRIDE" if so_fus < so_lex else " GANHA"
        print("%-46s %5d/%d %5d/%d %+7d %9.4f%s"
              % (rot[:46], l1, n, f1, n, f1 - l1, p, marca))
        print("      ganha %d, perde %d" % (so_fus, so_lex))
        for f, nf, a, b in por_faixa(lex, fus):
            print("      faixa %-6s n=%3d lexical %3d (%3.0f%%) fusao %3d (%3.0f%%) delta %+d"
                  % (f, nf, a, 100 * a / nf, b, 100 * b / nf, b - a))
    print()
    print("NOTA: 'lexical' e' o caminho esparso do harness COM o 2o estagio de ID (+45/+55),")
    print("nao BM25 puro. Toda comparacao de fusao tem de ser contra ele, porque e' o que a")
    print("producao executa hoje.")


if __name__ == "__main__":
    main()
