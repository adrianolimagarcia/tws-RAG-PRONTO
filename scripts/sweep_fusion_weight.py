#!/usr/bin/env python3
"""Varredura do PESO DA FUSAO (RAG_RRF_W) em corpora de forca oposta.

PERGUNTA
--------
Foi medido que a fusao RRF de peso igual aterrissa ENTRE os dois ramos e perde o
melhor, nos dois sentidos: no corpus de operacoes REST o fraco e' o esparso (2,5% @1)
e a fusao derruba o denso de 32,5% para 15%; no corpus geral o fraco e' o denso
(63-74% @1) e a fusao derruba o lexical de 90-98% para 84-96%. Ponderar a fusao
resolve? Depende de o peso otimo ser ESTAVEL entre conjuntos.

Este script NAO escolhe um peso bom. Ele mede a CURVA e responde:
  - o argmax do peso e' o mesmo no corpus REST e no corpus geral?
  - se nao for, nenhum peso global serve - a fusao ponderada herda o defeito da
    particao, e o registro tem de dizer isso.

PROTOCOLO (o mesmo que reprovou o challenger de 17/09)
  TUNE   em blind_v3_slices (geral) e rest_ops_40 (REST)
  VALIDA nos held-outs externos que NAO entraram no tune (100/50/30)

DISCIPLINA
  Corpus congelado; RAG_DENSE_MASK_TO_CORPUS=1 (os dois ramos veem o MESMO conjunto);
  eval_summary.json salvo e restaurado; nada de default alterado.

USO
    python3 scripts/sweep_fusion_weight.py --out /tmp/sweep.json
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
SUM = os.path.join(REPO, "data", "eval", "eval_summary.json")

BASE = {"RAG_MEASURE_EXCLUDE_EVIDENCE": "1", "PYTHONHASHSEED": "0",
        "RAG_DENSE_MASK_TO_CORPUS": "1",
        "RAG_DENSE_INDEX": "data/indexes/corpus_bge_m3_v5.pt",
        "RAG_DENSE_META": "data/indexes/corpus_docs_meta_v5.json",
        "RAG_HYBRID": "1", "RAG_RERANK_TOP": "15"}

TUNE = {
    "geral_blind_v3": ("data/eval/blind_v3_slices.jsonl", False),
    "rest_ops_40": ("data/eval/rest_api_benchmark_ops_40.jsonl", True),
}
VALIDA = {
    "holdout_100_unseen": ("data/eval/holdout_100_unseen.jsonl", False),
    "blind_holdout_50": ("data/eval/blind_holdout_50_vault.jsonl", False),
    "realistic_30": ("data/eval/realistic_blind_holdout_30.jsonl", False),
}

# GRADE GROSSEIRA DE PROPOSITO: 3 pontos que DECIDEM a pergunta (esparso puro / peso
# igual / denso puro). Nao resolve curva nao-monotona; resolve "o argmax do corpus REST
# e' o mesmo do corpus geral?". Se a forma exigir, refina-se DEPOIS - 5 pesos x 5
# conjuntos nao cabem em blocos de execucao controlada neste host.
PESOS = [0.0, 0.5, 1.0]


def head() -> str:
    return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip()


def roda(bench: str, rest: bool, w: float) -> dict:
    env = dict(os.environ)
    env.update(BASE)
    env["RAG_BENCHMARK_FILE"] = bench
    env["RAG_RRF_W"] = str(w)
    if rest:
        # Benchmark por operacao: granularidade OPERACAO (276 registros) -> corpus 6984.
        env["RAG_INGEST_REST_API"] = "1"
        env["RAG_REST_GRANULARITY"] = "operation"
    else:
        # Conjuntos gerais: a fonte REST entra na granularidade FAMILIA (24 registros),
        # que e' o que compoe o corpus congelado do runbook (6708 + 24 = 6732). Sem isto
        # a varredura media 6708 - um corpus DIFERENTE do que produziu o controle.
        env["RAG_INGEST_REST_API"] = "1"
    r = subprocess.run([PY, "data/eval/evaluate_rag_benchmark.py"], cwd=REPO, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"erro": f"rc={r.returncode}", "stderr": r.stderr[-200:]}
    n_docs = None
    for linha in r.stdout.splitlines():
        if "Total de documentos" in linha:
            n_docs = int(linha.split(":")[-1].strip())
            break
    d = json.load(open(SUM, encoding="utf-8"))
    return {"n_docs": n_docs, "total": d.get("total"), "hit1": d.get("hit_rate_at_1"),
            "hit5": d.get("hit_rate_at_5"), "hit10": d.get("hit_rate_at_10"),
            "hit15": d.get("hit_rate_at_15"), "recall15": d.get("recall_at_15"),
            "mrr": d.get("mrr")}


def salva(res: dict, caminho: str) -> None:
    """Grava a cada conjunto concluido: um kill nao pode perder a varredura inteira."""
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2, default=str)


def carrega(out: str) -> dict:
    """Retoma: um kill nao pode custar o trabalho ja' feito."""
    if os.path.exists(out):
        try:
            with open(out, encoding="utf-8") as fh:
                d = json.load(fh)
            if isinstance(d, dict) and "conjuntos" in d:
                return d
        except (OSError, ValueError):
            pass
    return {}


def bloco(conjuntos: dict, res: dict, out: str) -> None:
    for nome, (caminho, rest) in conjuntos.items():
        feito = res["conjuntos"].setdefault(nome, {"arquivo": caminho, "pesos": {}})
        for w in PESOS:
            # ja' medido e sem erro? nao repete (retomada apos interrupcao)
            ant = feito["pesos"].get(str(w))
            if ant and "erro" not in ant:
                print(f"  {nome} / w={w} ... JA' FEITO, pulando", file=sys.stderr, flush=True)
                continue
            print(f"  {nome} / w={w} ...", file=sys.stderr, flush=True)
            feito["pesos"][str(w)] = roda(caminho, rest, w)
            salva(res, out)  # persistido a CADA peso, nao so' a cada conjunto


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    bak = SUM + ".bak-sweep"
    if os.path.exists(SUM):
        shutil.copy2(SUM, bak)
    h = head()
    antigo = carrega(args.out)
    res: dict = {"head": h, "pesos_varridos": PESOS,
                 "corpus": "congelado; RAG_DENSE_MASK_TO_CORPUS=1",
                 "pipeline": "RRF(denso,esparso; w no denso) -> top-20 -> rerank top_n=15",
                 "conjuntos": antigo.get("conjuntos", {})}
    res["retomado_de"] = antigo.get("head") if antigo else None
    res["interrupcoes"] = antigo.get("interrupcoes", 0)
    try:
        bloco(TUNE, res, args.out)
        bloco(VALIDA, res, args.out)
    finally:
        if os.path.exists(bak):
            shutil.move(bak, SUM)

    # argmax por conjunto (por @1 e por recall@15) e estabilidade entre corpora
    res["argmax"] = {}
    for nome, b in res["conjuntos"].items():
        vals = {w: m for w, m in b["pesos"].items() if "erro" not in m}
        if not vals:
            continue
        m1 = max(vals.items(), key=lambda kv: (kv[1]["hit1"], kv[1]["mrr"]))
        m15 = max(vals.items(), key=lambda kv: (kv[1]["recall15"], kv[1]["hit1"]))
        res["argmax"][nome] = {"w_por_hit1": m1[0], "hit1": m1[1]["hit1"],
                               "w_por_recall15": m15[0], "recall15": m15[1]["recall15"]}

    tune_w1 = {res["argmax"][k]["w_por_hit1"] for k in TUNE if k in res["argmax"]}
    res["peso_otimo_estavel_no_tune"] = len(tune_w1) <= 1

    # CONTROLE OBRIGATORIO (regra zero do runbook). O baseline lexical do harness tem de
    # reproduzir 172/262 @1 no blind v3 com o corpus congelado = 6732 docs. O w=0.0 zera o
    # peso do ramo denso, entao ELE E' o baseline lexical - o controle fica embutido na
    # propria varredura. Sem isto, comparar pesos entre si ainda valeria, mas nada poderia
    # ser comparado com o historico do repo.
    CTRL_ESPERADO = 172 / 262
    ctrl = res["conjuntos"].get("geral_blind_v3", {}).get("pesos", {}).get("0.0", {})
    res["controle"] = {
        "regra": "baseline lexical (w=0.0) no blind v3, corpus congelado",
        "esperado_hit1": CTRL_ESPERADO, "obtido_hit1": ctrl.get("hit1"),
        "n_docs": ctrl.get("n_docs"),
        "ok": (ctrl.get("hit1") is not None and ctrl.get("n_docs") == 6732
               and abs(ctrl["hit1"] - CTRL_ESPERADO) < 1e-9)}

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2, default=str)

    print(f"HEAD={h}   {res['corpus']}")
    print(f"{'conjunto':<22} {'w':>5} {'n_docs':>7} {'@1':>7} {'@10':>7} {'@15':>7} {'rec15':>7} {'MRR':>8}")
    for nome, b in res["conjuntos"].items():
        for w, m in b["pesos"].items():
            if "erro" in m:
                print(f"{nome:<22} {w:>5} ERRO {m['erro']}")
                continue
            print(f"{nome:<22} {w:>5} {str(m['n_docs']):>7} {m['hit1']:>7.3f} {m['hit10']:>7.3f} "
                  f"{m['hit15']:>7.3f} {m['recall15']:>7.3f} {m['mrr']:>8.4f}")
        print()
    print("ARGMAX por conjunto:")
    for nome, a in res["argmax"].items():
        print(f"  {nome:<22} w(@1)={a['w_por_hit1']} hit1={a['hit1']:.3f} | "
              f"w(recall15)={a['w_por_recall15']} rec15={a['recall15']:.3f}")
    print(f"PESO OTIMO ESTAVEL no tune: {res['peso_otimo_estavel_no_tune']}")
    c = res["controle"]
    estado = "OK" if c["ok"] else "FALHOU"
    print(f"CONTROLE {estado}: baseline lexical @1 obtido={c['obtido_hit1']} "
          f"esperado={c['esperado_hit1']:.6f} n_docs={c['n_docs']} (esperado 6732)")
    if not c["ok"]:
        print("  -> medicao INVALIDA pela regra zero do runbook; nao concluir nada.")
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
