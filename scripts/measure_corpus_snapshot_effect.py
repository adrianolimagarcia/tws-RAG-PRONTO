#!/usr/bin/env python3
"""Mede o efeito do SNAPSHOT DO CORPUS nas metricas do benchmark REST.

POR QUE ESTE SCRIPT EXISTE
--------------------------
O avaliador (data/eval/evaluate_rag_benchmark.py, linha 30) carrega TODO arquivo
`data/evidence/lab-validation-*.jsonl` para dentro do corpus como documento
`lab_evidence`. Consequencia: o corpus NAO e' congelado - ele cresce a cada evidencia
que o proprio agente registra, e as metricas andam junto (medido: 6874 -> 6903 docs
derrubou BM25 @1 de 5/40 para 4/40 e o hibrido de 8/40 para 6/40). Medicao que muda
porque o medidor escreveu no objeto medido nao e' medicao.

O QUE ESTE SCRIPT FAZ
---------------------
Congela o corpus por OVERLAY, sem tocar no avaliador padrao: monkeypatch de
`load_documents` que filtra os documentos `lab_evidence`. O arquivo do avaliador NAO e'
alterado, nenhum default muda, nenhuma fonte e' ligada ou desligada.

Como `RAG_HYBRID` e' lido no IMPORT do modulo, cada configuracao roda em processo
proprio - este script mede UMA configuracao por execucao e imprime o resultado.

rank=None
---------
`rank=None` significa "o alvo NUNCA foi recuperado" e e' um ESTADO PROPRIO, nao zero:
nao entra em nenhum hit@k e e' contado separadamente como `nunca_recuperado`. Tratar
None como 0 inflaria o hit@1 artificialmente.

VALIDACAO DE REPLICACAO
-----------------------
As metricas sao recalculadas a partir de `details[].rank` e CONFRONTADAS com os campos
`hit_rate_at_*` que o proprio avaliador devolveu. Se divergirem, o instrumento esta
errado e o script FALHA em vez de reportar.

USO
    RAG_INGEST_REST_API=1 python3 scripts/measure_corpus_snapshot_effect.py --corpus atual
    RAG_INGEST_REST_API=1 python3 scripts/measure_corpus_snapshot_effect.py --corpus congelado
    (para o hibrido, exportar RAG_HYBRID=1 RAG_DENSE_INDEX=... RAG_DENSE_META=...)
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AVALIADOR = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_40.jsonl")
RESUMO = os.path.join(REPO, "data", "eval", "eval_summary.json")


def head_atual() -> str:
    try:
        return subprocess.check_output(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                                       text=True).strip()
    except Exception:  # noqa: BLE001
        return "?"


def carregar_avaliador():
    spec = importlib.util.spec_from_file_location("ev", AVALIADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def hit_at(ranks: list[int | None], k: int) -> int:
    """Conta hits em @k. `None` (nunca recuperado) NAO conta - nao vira zero."""
    return sum(1 for r in ranks if r is not None and r <= k)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", choices=("atual", "congelado"), required=True,
                    help="'congelado' exclui os documentos lab_evidence por overlay")
    ap.add_argument("--out", default="",
                    help="arquivo para o JSON do resultado. OBRIGATORIO na pratica: "
                         "run_evaluation() imprime o relatorio dele em STDOUT, entao "
                         "despejar o JSON no stdout mistura as duas saidas.")
    args = ap.parse_args()

    if not os.environ.get("RAG_INGEST_REST_API"):
        print("ERRO: exporte RAG_INGEST_REST_API=1 (o benchmark REST exige a fonte ligada)")
        return 2

    os.environ.setdefault("RAG_BENCHMARK_FILE", BENCH)
    retriever = "hibrido" if os.environ.get("RAG_HYBRID") == "1" else "BM25"

    # --- preserva eval_summary.json: run_evaluation() o SOBRESCREVE a cada chamada ---
    backup = RESUMO + ".preservado"
    tinha = os.path.exists(RESUMO)
    if tinha:
        shutil.copy2(RESUMO, backup)

    try:
        ev = carregar_avaliador()
        orig = ev.load_documents

        if args.corpus == "congelado":
            def carregar():
                return [d for d in orig() if d.get("type") != "lab_evidence"]
        else:
            carregar = orig

        n_docs = len(carregar())
        ev.load_documents = carregar
        try:
            # run_evaluation() NAO retorna as metricas - ele so' GRAVA eval_summary.json
            # (verificado no codigo do avaliador). Ler o arquivo recem-gravado e' o unico
            # caminho; por isso o backup/restore acima.
            ev.run_evaluation()
            with open(RESUMO, encoding="utf-8") as f:
                m = json.load(f)
        finally:
            ev.load_documents = orig
    finally:
        # --- restaura o artefato preservado ---
        if tinha:
            shutil.move(backup, RESUMO)

    det = m.get("details") or []
    ranks = [d.get("rank") for d in det]
    total = len(ranks)

    # --- recalculado a partir dos ranks, com None tratado como estado proprio ---
    calc = {f"hit@{k}": hit_at(ranks, k) for k in (1, 3, 5, 10)}
    nunca = sum(1 for r in ranks if r is None)
    mrrs = [1.0 / r for r in ranks if r is not None and r > 0]
    mrr_calc = sum(mrrs) / total if total else 0.0

    # --- validacao de replicacao contra o que o AVALIADOR devolveu ---
    div = []
    for k in (1, 3, 5, 10):
        oficial = m.get(f"hit_rate_at_{k}")
        if oficial is None:
            continue
        esperado = calc[f"hit@{k}"] / total if total else 0.0
        if abs(float(oficial) - esperado) > 1e-9:
            div.append(f"hit@{k}: avaliador={float(oficial):.6f} recalculado={esperado:.6f}")
    if abs(float(m.get("mrr") or 0.0) - mrr_calc) > 1e-9:
        div.append(f"mrr: avaliador={float(m.get('mrr') or 0):.6f} recalculado={mrr_calc:.6f}")

    out = {
        "head": head_atual(),
        "corpus": args.corpus,
        "retriever": retriever,
        "n_docs": n_docs,
        "total": total,
        "hit@1": calc["hit@1"], "hit@3": calc["hit@3"],
        "hit@5": calc["hit@5"], "hit@10": calc["hit@10"],
        "mrr": round(mrr_calc, 6),
        "nunca_recuperado": nunca,
        "ranks": ranks,
        "replicacao_ok": not div,
        "divergencias": div,
    }
    texto = json.dumps(out, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(texto + "\n")
    # resumo humano vai para STDERR: o stdout ja' e' do avaliador
    print(f"[medidor] corpus={args.corpus} retriever={retriever} n_docs={n_docs} "
          f"hit@1={calc['hit@1']}/{total} hit@10={calc['hit@10']}/{total} "
          f"nunca_recuperado={nunca} replicacao_ok={not div}", file=sys.stderr)

    if div:
        print("\n*** REPLICACAO NAO FECHOU - instrumento divergente do avaliador ***",
              file=sys.stderr)
        for d in div:
            print(f"  {d}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
