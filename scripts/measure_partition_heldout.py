#!/usr/bin/env python3
"""Mede a PARTICAO por fonte/origem nos conjuntos externos held-out.

PERGUNTA
--------
O corpus de operacoes REST mostrou que denso puro bate o pipeline atual (32,5% vs
22,5% @1). No corpus geral a evidencia de 17/09 diz o contrario (o reranker e' ganho
liquido de +14). Se o sinal depende do conjunto, a saida NAO e' escolher um pipeline
global - e' PARTICIONAR. Este script mede se a particao e' sustentavel nos held-outs.

DESENHO
  atual       : pipeline de PRODUCAO replicado - RRF (denso+esparso) -> top-20 ->
                second_stage_rerank top_n=15 (evaluate_pure_virgin_hybrid_cpu.py:98-102)
  denso_puro  : ramo denso sozinho, sem fusao e sem segundo estagio
  bm25        : lexical puro, referencia
  Tudo com RAG_DENSE_MASK_TO_CORPUS=1: o ramo denso so' pode devolver documento que
  esteja no corpus carregado, senao ele enxerga um conjunto diferente do lexical e a
  comparacao deixa de ser sobre os MESMOS documentos.

O QUE DECIDE
  1. Agregado por held-out: a partição so' se paga se o ganho num grupo nao custar no outro.
  2. Por topico: o sinal se separa por um atributo, ou e' ruido dentro de cada grupo?
  3. ORACULO (melhor dos dois por pergunta): o teto que uma particao PERFEITA atingiria.
  4. PROXY DETERMINISTICO: um atributo DISPONIVEL EM PRODUCAO (codigo de mensagem ou
     nome de comando na pergunta) reproduz a separacao do oraculo? O topico/subtopico do
     benchmark NAO serve: e' rotulo de anotacao, nao existe no pedido real - foi
     exatamente por isso que a rota de 17/09 foi declarada nao-implantavel.

USO
    python3 scripts/measure_partition_heldout.py --out /tmp/particao.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import statistics
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
SUM = os.path.join(REPO, "data", "eval", "eval_summary.json")
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"

HELDOUTS = {
    "holdout_100_unseen": os.path.join(NR, "rerank_cache_holdout_100_unseen.json.bench.jsonl"),
    "blind_holdout_50_vault": os.path.join(NR, "rerank_cache_blind_holdout_50_vault.json.bench.jsonl"),
    "realistic_blind_holdout_30": os.path.join(NR, "rerank_cache_realistic_blind_holdout_30.json.bench.jsonl"),
}

BASE = {"RAG_MEASURE_EXCLUDE_EVIDENCE": "1", "PYTHONHASHSEED": "0",
        "RAG_DENSE_MASK_TO_CORPUS": "1",
        "RAG_DENSE_INDEX": "data/indexes/corpus_bge_m3_v5.pt",
        "RAG_DENSE_META": "data/indexes/corpus_docs_meta_v5.json"}

CONFIGS = {
    "bm25": {},
    # replica da PRODUCAO: RRF -> top-20 -> rerank top_n=15
    "atual": {"RAG_HYBRID": "1", "RAG_RERANK_TOP": "15"},
    "denso_puro": {"RAG_DENSE_ONLY": "raw", "RAG_DENSE_TOP": "30"},
    "denso_puro_60": {"RAG_DENSE_ONLY": "raw", "RAG_DENSE_TOP": "60"},
}

# PROXY DETERMINISTICO, disponivel no pedido real (nao usa rotulo do benchmark):
# a pergunta cita um codigo de mensagem (ex.: AWSUI3069E) ou um comando do produto.
RX_MENSAGEM = re.compile(r"\b[A-Z]{2,}[A-Z0-9]{0,6}\d{3,4}[A-Z]?\b")
RX_COMANDO = re.compile(r"\b(conman|composer|jnextplan|switchplan|makeplan|optman|mgr|batchman|"
                        r"planman|sbs|sj|ss|sc|stat|extract|display|ocli|symphony)\b", re.I)


def head() -> str:
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip()


def roda(bench: str, extra: dict) -> dict:
    env = dict(os.environ)
    env.update(BASE)
    env["RAG_BENCHMARK_FILE"] = bench
    env.update(extra)
    r = subprocess.run([PY, "data/eval/evaluate_rag_benchmark.py"], cwd=REPO, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"erro": f"rc={r.returncode}", "stderr": r.stderr[-300:]}
    n_docs = None
    for linha in r.stdout.splitlines():
        if "Total de documentos" in linha:
            n_docs = int(linha.split(":")[-1].strip())
            break
    d = json.load(open(SUM, encoding="utf-8"))
    return {"n_docs": n_docs, "total": d.get("total"),
            "hit1": d.get("hit_rate_at_1"), "hit3": d.get("hit_rate_at_3"),
            "hit5": d.get("hit_rate_at_5"), "hit10": d.get("hit_rate_at_10"),
            "hit15": d.get("hit_rate_at_15"), "recall15": d.get("recall_at_15"),
            "mrr": d.get("mrr"), "details": d.get("details", [])}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    bak = SUM + ".bak-particao"
    if os.path.exists(SUM):
        shutil.copy2(SUM, bak)
    h = head()
    res: dict = {"head": h, "heldouts": {}, "proxy": {
        "regex_mensagem": RX_MENSAGEM.pattern, "regex_comando": RX_COMANDO.pattern}}
    try:
        for nome_h, caminho in HELDOUTS.items():
            bench = [json.loads(l) for l in open(caminho, encoding="utf-8")]
            res["heldouts"][nome_h] = {"n": len(bench), "configs": {}}
            for nome_c, extra in CONFIGS.items():
                print(f"  {nome_h} / {nome_c} ...", file=sys.stderr, flush=True)
                res["heldouts"][nome_h]["configs"][nome_c] = roda(caminho, dict(extra))
    finally:
        if os.path.exists(bak):
            shutil.move(bak, SUM)

    # ---- analise: oraculo + proxy ----
    for nome_h, bloco in res["heldouts"].items():
        bench = [json.loads(l) for l in open(HELDOUTS[nome_h], encoding="utf-8")]
        meta = {b["id"]: b for b in bench}
        a = bloco["configs"].get("atual", {}).get("details", [])
        p = bloco["configs"].get("denso_puro", {}).get("details", [])
        if not a or not p:
            continue
        ra = {d["id"]: d.get("rank") for d in a}
        rp = {d["id"]: d.get("rank") for d in p}

        def acerta(r):
            return r is not None and r <= 15

        so_atual = [q for q in ra if acerta(ra[q]) and not acerta(rp.get(q))]
        so_denso = [q for q in ra if acerta(rp.get(q)) and not acerta(ra[q])]
        ambos = [q for q in ra if acerta(ra[q]) and acerta(rp.get(q))]
        nenhum = [q for q in ra if not acerta(ra[q]) and not acerta(rp.get(q))]

        # oraculo: escolher o melhor por pergunta
        oraculo = len(ambos) + len(so_atual) + len(so_denso)
        bloco["analise"] = {
            "hit15_atual": len(ambos) + len(so_atual),
            "hit15_denso": len(ambos) + len(so_denso),
            "ambos": len(ambos), "so_atual": len(so_atual),
            "so_denso": len(so_denso), "nenhum": len(nenhum),
            "oraculo_hit15": oraculo,
        }

        # proxy deterministico
        def tem_proxy(qid):
            q = meta.get(qid, {}).get("question", "")
            return bool(RX_MENSAGEM.search(q) or RX_COMANDO.search(q))

        com = [q for q in ra if tem_proxy(q)]
        sem = [q for q in ra if not tem_proxy(q)]
        bloco["analise"]["proxy"] = {
            "n_com_atributo": len(com), "n_sem_atributo": len(sem),
            "hit15_atual_com": sum(1 for q in com if acerta(ra[q])),
            "hit15_denso_com": sum(1 for q in com if acerta(rp.get(q))),
            "hit15_atual_sem": sum(1 for q in sem if acerta(ra[q])),
            "hit15_denso_sem": sum(1 for q in sem if acerta(rp.get(q))),
        }

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2, default=str)

    print(f"HEAD={h}")
    print(f"{'held-out':<28} {'cfg':<14} {'n_docs':>7} {'@1':>7} {'@10':>7} {'@15':>7} {'rec15':>7} {'MRR':>8}")
    for nome_h, bloco in res["heldouts"].items():
        for nome_c, m in bloco["configs"].items():
            if "erro" in m:
                print(f"{nome_h:<28} {nome_c:<14} ERRO {m['erro']}")
                continue
            print(f"{nome_h:<28} {nome_c:<14} {str(m['n_docs']):>7} {m['hit1']:>7.3f} "
                  f"{m['hit10']:>7.3f} {m['hit15']:>7.3f} {m['recall15']:>7.3f} {m['mrr']:>8.4f}")
        an = bloco.get("analise")
        if an:
            print(f"   -> @15: atual {an['hit15_atual']} | denso {an['hit15_denso']} | "
                  f"oraculo {an['oraculo_hit15']} (so_atual {an['so_atual']}, so_denso {an['so_denso']}, "
                  f"ambos {an['ambos']}, nenhum {an['nenhum']})")
            pr = an["proxy"]
            print(f"   -> proxy: com_atributo n={pr['n_com_atributo']} (atual {pr['hit15_atual_com']} "
                  f"vs denso {pr['hit15_denso_com']}) | sem n={pr['n_sem_atributo']} "
                  f"(atual {pr['hit15_atual_sem']} vs denso {pr['hit15_denso_sem']})")
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
