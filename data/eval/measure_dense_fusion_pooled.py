"""RESPOSTA COM DADOS EXISTENTES: agrupa os conjuntos LIMPOS e testa no conjunto todo.

Por que agrupar: n=24 deu p=0,022 (ganho) e n=39 deu p=0,27 (nao conclusivo) para o MESMO
efeito. O tamanho do conjunto domina o veredito. Agrupar os conjuntos de pergunta humana
que ja' existem no repo da' n suficiente SEM gerar pergunta nova e sem risco de vies de
geracao - e' a medida mais honesta disponivel hoje.

Regra de inclusao (pre-registrada): mediana do maior n-grama contiguo pergunta<->claim do
gabarito <= 4 (pergunta que CITA termo, nao copia frase). Conjuntos mais vazados ficam fora
e sao reportados. Cada conjunto e' medido pelo harness (lexical e RAG_HYBRID=1) e as
perguntas sao agrupadas por id; o teste e' McNemar exato no pool.

ATENCAO a uma armadilha do log: o harness grava `data/eval/eval_summary.json` a cada run.
Duas corridas em paralelo sobrescrevem uma a outra e os numeros saem trocados. Aqui as
corridas sao SEQUENCIAIS e o resumo e' copiado imediatamente apos cada uma.
"""
import os
import re
import sys
import json
import math
import subprocess

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
HARNESS = os.path.join(REPO, "data/eval/evaluate_rag_benchmark.py")
PY = os.environ.get("RAG_PY", "/tmp/ragexp/venv/bin/python")
TMP = "/tmp/ragexp/pooled"
os.makedirs(TMP, exist_ok=True)

CONJUNTO_MASTER = os.path.join(REPO, "data/export/tws_corpus_master_consolidated.jsonl")
txt_claim = {}
for line in open(CONJUNTO_MASTER, encoding="utf-8"):
    if line.strip():
        o = json.loads(line)
        txt_claim[o["claim_id"]] = f"{o['claim']} {o.get('context_prefix','')}"


def palavras(s):
    return re.findall(r"\w+", s.lower())


def ngrama(pergunta, claim, teto=40):
    p, c = palavras(pergunta), palavras(claim)
    if not p or not c:
        return 0
    for n in range(2, min(teto, len(p)) + 1):
        conj = {tuple(p[i:i + n]) for i in range(len(p) - n + 1)}
        if not any(tuple(c[i:i + n]) in conj for i in range(len(c) - n + 1)):
            return n - 1
    return min(teto, len(p))


def mediana_ngrama(caminho):
    ns = []
    for l in open(caminho, encoding="utf-8"):
        if not l.strip():
            continue
        o = json.loads(l)
        cl = " ".join(txt_claim.get(c, "") for c in (o.get("relevant_claim_ids") or []))
        if (o.get("question") and cl.strip()):
            ns.append(ngrama(o["question"], cl))
    ns.sort()
    return (ns[len(ns) // 2] if ns else 0), len(ns)


def roda(caminho, modo, rot):
    env = dict(os.environ)
    env.update(PYTHONHASHSEED="0", RAG_INGEST_REST_API="1", RAG_BENCHMARK_FILE=caminho)
    if modo == "hyb":
        env.update(RAG_HYBRID="1", RAG_RRF_W=os.environ.get("RAG_RRF_W", "0.75"),
                   RAG_DENSE_MASK_TO_CORPUS="1", HF_HOME="/tmp/ragexp/hfhome",
                   HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    with open(os.path.join(TMP, "%s_%s.log" % (rot, modo)), "w") as fh:
        subprocess.run([PY, HARNESS], env=env, stdout=fh, stderr=subprocess.STDOUT)
    res = os.path.join(TMP, "%s_%s.json" % (rot, modo))
    subprocess.run(["cp", os.path.join(REPO, "data/eval/eval_summary.json"), res])
    d = json.load(open(res))
    return {x["id"]: x.get("rank") for x in d["details"]}


CANDIDATOS = [
    ("golden_qa_benchmark.jsonl", "geral (70)"),
    ("golden_qa_messages_benchmark.jsonl", "mensagens (34)"),
    ("golden_qa_virgin_expanded.jsonl", "virgem+mensagens (39)"),
    ("golden_qa_virgin_en_benchmark.jsonl", "virgem INGLES (24)"),
    ("holdout_40_test.jsonl", "holdout_40 (39)"),
    ("blind_holdout_qa_30.jsonl", "holdout_qa_30 (24)"),
    ("realistic_blind_holdout_30.jsonl", "realistico (12)"),
    ("pure_virgin_test_40.jsonl", "pure_virgin (39)"),
    ("holdout_100_unseen.jsonl", "holdout_100 (27)"),
]

print("=" * 92)
print("FILTRO PRE-REGISTRADO: so' entram conjuntos com mediana de n-grama <= 4")
print("=" * 92)
incluidos, fora = [], []
for arq, rot in CANDIDATOS:
    p = os.path.join(REPO, "data/eval/decontaminated", arq)
    if not os.path.exists(p):
        continue
    med, n = mediana_ngrama(p)
    status = "INCLUI" if med <= 4 else "FORA (vazado)"
    print("  %-34s mediana n-grama=%2d  n=%3d   %s" % (rot, med, n, status))
    (incluidos if med <= 4 else fora).append((p, rot))

print()
print("=" * 92)
print("MEDINDO (sequencial, um harness por vez)")
print("=" * 92)
pool_lex, pool_fus = {}, {}
por_conj = {}
for p, rot in incluidos:
    lex = roda(p, "lex", rot.replace(" ", "_").replace("(", "").replace(")", ""))
    fus = roda(p, "hyb", rot.replace(" ", "_").replace("(", "").replace(")", ""))
    l1 = sum(1 for v in lex.values() if v == 1)
    f1 = sum(1 for v in fus.values() if v == 1)
    por_conj[rot] = (l1, f1, len(lex))
    print("  %-34s lexical %3d/%d  fusao %3d/%d  delta %+d"
          % (rot, l1, len(lex), f1, len(lex), f1 - l1))
    pool_lex.update(lex)
    pool_fus.update(fus)


def mcnemar(a, b):
    perde = ganha = 0
    for i in set(a) & set(b):
        ca, cb = a[i] == 1, b[i] == 1
        if cb and not ca:
            ganha += 1
        elif ca and not cb:
            perde += 1
    n = ganha + perde
    if n == 0:
        return perde, ganha, 1.0
    p = 2.0 * sum(math.comb(n, k) for k in range(0, min(ganha, perde) + 1)) / (2.0 ** n)
    return perde, ganha, min(1.0, p)


perde, ganha, p = mcnemar(pool_lex, pool_fus)
n = len(set(pool_lex) & set(pool_fus))
l1 = sum(1 for i in set(pool_lex) & set(pool_fus) if pool_lex[i] == 1)
f1 = sum(1 for i in set(pool_lex) & set(pool_fus) if pool_fus[i] == 1)
print()
print("=" * 92)
print("POOL DE PERGUNTAS LIMPAS: n=%d" % n)
print("  lexical %d/%d (%.1f%%)   fusao %d/%d (%.1f%%)   delta %+d"
      % (l1, n, 100 * l1 / n, f1, n, 100 * f1 / n, f1 - l1))
print("  ganha %d | perde %d | McNemar exato p=%.4f  %s"
      % (ganha, perde, p, "SIGNIFICATIVO" if p < 0.05 else "NAO conclusivo"))
print()
print("POR CONJUNTO (direcao tem de ser coerente para o pool fazer sentido):")
for rot, (a, b, m) in por_conj.items():
    print("   %-34s %+d" % (rot, b - a))
json.dump({"pool_lex": pool_lex, "pool_fus": pool_fus, "por_conjunto": por_conj},
          open("/tmp/ragexp/pooled_resultado.json", "w"))
