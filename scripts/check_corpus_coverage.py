#!/usr/bin/env python3
"""Medidor de cobertura ITEM-A-ITEM do corpus RAG contra a FONTE DE VERDADE.

Por que existe
--------------
O `coverage_backlog.json` do dataset declarava `missing: 0` em todos os topicos
usando `minimum_verified_claims: 40` por topico — um LIMIAR DE VOLUME. Com esse
criterio, um topico passa com 59 claims enquanto 152 de 212 endpoints da API
documentada ficam fora do corpus. Limiar de volume nao mede cobertura funcional.

Este script mede contra a fonte, contando item a item, e separa DUAS coberturas
que vinham sendo confundidas:

  EXTRACAO  — todo item da fonte tem registro derivado? (independe do switch)
  INGESTAO  — o registro derivado esta' no corpus AGORA? (depende do switch)

Um item pode ter extracao 100% e ingestao 0% (e' o caso das man pages com
RAG_INGEST_DERIVED OFF). Reportar so' um dos dois esconde a lacuna real.

Uso:
  python3 scripts/check_corpus_coverage.py --source rest
  python3 scripts/check_corpus_coverage.py --source manpages
  python3 scripts/check_corpus_coverage.py --all
  python3 scripts/check_corpus_coverage.py --all --json saida.json
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SPEC = os.environ.get("REST_API_SPEC", "/root/workspace/tws-docs-raw/WA_API3_v2.json")
REST_DERIVED = os.path.join(REPO, "data", "knowledge", "rest-api-derived.jsonl")
MAN_DERIVED = os.path.join(REPO, "data", "knowledge", "man-pages-derived.jsonl")
MAN_CONTAINER = os.environ.get("MANPAGES_CONTAINER", "tws-hwa")
MAN_DIRS = ["/opt/hwa/TWS/man/composer/cat1", "/opt/hwa/TWS/man/conman/cat1"]


def carregar_loader():
    """Importa o loader do corpus sem executar a avaliacao."""
    p = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")
    sys.path.insert(0, os.path.dirname(p))
    spec = importlib.util.spec_from_file_location("ev_cov", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def corpus_atual() -> tuple[list[dict], str]:
    """Corpus como o loader o entrega AGORA (respeita os switches do ambiente)."""
    ev = carregar_loader()
    docs = ev.load_documents()
    sw = []
    for v in ("RAG_INGEST_DERIVED", "RAG_INGEST_REST_API"):
        sw.append(f"{v}={'1' if os.environ.get(v) == '1' else '0'}")
    return docs, " ".join(sw)


# --------------------------------------------------------------------------
# Fonte 1: REST API (spec OpenAPI)
# --------------------------------------------------------------------------
def medir_rest(docs: list[dict]) -> dict:
    if not os.path.exists(SPEC):
        return {"erro": f"spec nao encontrada: {SPEC}"}
    with open(SPEC, encoding="utf-8") as fh:
        spec = json.load(fh)
    paths = list((spec.get("paths") or {}).keys())

    # registros derivados que existem (extracao) e que estao no corpus (ingestao)
    derivados = []
    if os.path.exists(REST_DERIVED):
        derivados = [json.loads(l) for l in open(REST_DERIVED, encoding="utf-8") if l.strip()]
    ids_derivados = {r["claim_id"] for r in derivados}
    ids_no_corpus = {d["id"] for d in docs if d["id"] in ids_derivados}

    # cobertura por endpoint: o path (ou o par de segmentos significativos) aparece
    # no texto do corpus? Regra explicita e reproduzivel.
    #
    # ARMADILHA MEDIDA: se contarmos o corpus INTEIRO, a propria derivacao nossa
    # (`rest_api_surface`) contem os paths e o numero vai a 100% assim que o switch
    # liga — a metrica passaria a medir a nossa parafrase, nao a cobertura da FONTE.
    # Por isso reportamos as duas leituras e a distincao e' explicita:
    #   fonte_original  -> so' os documentos que NAO sao derivados nossos
    #   corpus_completo -> tudo (inclui a nossa derivacao)
    TIPOS_DERIVADOS = {"rest_api_surface", "man_page_syntax", "derived_knowledge"}
    texto_orig = " \n ".join(
        (d.get("text") or "") for d in docs if d.get("type") not in TIPOS_DERIVADOS
    )
    texto = " \n ".join((d.get("text") or "") for d in docs)

    def _cobertos(blob: str) -> list[str]:
        out = []
        for p in paths:
            seg = [s for s in p.split("/") if s and not s.startswith("{")]
            chave = "/".join(seg[-2:]) if len(seg) >= 2 else (seg[-1] if seg else "")
            if p in blob or (chave and chave in blob):
                out.append(p)
        return out

    cobertos_orig = _cobertos(texto_orig)
    cobertos = _cobertos(texto)
    ausentes = [p for p in paths if p not in set(cobertos_orig)]

    fam = collections.Counter()
    for p in ausentes:
        partes = p.split("/")
        fam[partes[4] if len(partes) > 4 else "?"] += 1

    return {
        "fonte": "REST API (spec OpenAPI)",
        "itens_na_fonte": len(paths),
        "extracao": {
            "registros_derivados": len(derivados),
            "ids_distintos": len(ids_derivados),
            "operacoes_cobertas": sum(r.get("n_operations", 0) for r in derivados),
        },
        "ingestao": {
            "no_corpus": len(ids_no_corpus),
            "fora_do_corpus": len(ids_derivados - ids_no_corpus),
        },
        "endpoints": {
            "cobertos_fonte_original": len(cobertos_orig),
            "pct_fonte_original": round(100 * len(cobertos_orig) / max(1, len(paths)), 1),
            "cobertos_corpus_completo": len(cobertos),
            "pct_corpus_completo": round(100 * len(cobertos) / max(1, len(paths)), 1),
            "ausentes": len(ausentes),
        },
        "ausentes_por_familia": dict(fam.most_common()),
    }


# --------------------------------------------------------------------------
# Fonte 2: man pages do produto
# --------------------------------------------------------------------------
def _man_pages_no_container() -> list[tuple[str, str]]:
    script = (
        "for d in " + " ".join(MAN_DIRS) + "; do for f in $d/*.1; do echo \"$f\"; done; done"
    )
    proc = subprocess.run(
        ["docker", "exec", MAN_CONTAINER, "bash", "-lc", script],
        capture_output=True, text=True, timeout=120,
    )
    if proc.returncode != 0:
        return []
    out = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line.endswith(".1"):
            continue
        tool = "composer" if "/composer/" in line else "conman"
        out.append((tool, os.path.basename(line)[:-2]))
    return out


def medir_manpages(docs: list[dict]) -> dict:
    paginas = _man_pages_no_container()
    if not paginas:
        return {"erro": "nao consegui listar as man pages do container"}
    derivados = []
    if os.path.exists(MAN_DERIVED):
        derivados = [json.loads(l) for l in open(MAN_DERIVED, encoding="utf-8") if l.strip()]
    por_chave = {(r.get("tool"), r.get("command")): r for r in derivados}
    ids_derivados = {r["claim_id"] for r in derivados}
    ids_no_corpus = {d["id"] for d in docs if d["id"] in ids_derivados}

    sem_registro = [f"{t}/{c}" for t, c in paginas if (t, c) not in por_chave]

    return {
        "fonte": "man pages do produto",
        "itens_na_fonte": len(paginas),
        "extracao": {
            "registros_derivados": len(derivados),
            "paginas_com_registro": len(paginas) - len(sem_registro),
            "sem_registro": sem_registro,
        },
        "ingestao": {
            "no_corpus": len(ids_no_corpus),
            "fora_do_corpus": len(ids_derivados - ids_no_corpus),
        },
    }


def imprimir(r: dict) -> None:
    print(f"  === {r.get('fonte')} ===")
    if "erro" in r:
        print(f"    ERRO: {r['erro']}")
        return
    n = r["itens_na_fonte"]
    e, i = r["extracao"], r["ingestao"]
    print(f"    itens na fonte            : {n}")
    print(f"    EXTRACAO  com registro    : {e.get('paginas_com_registro', e.get('registros_derivados'))}/{n}")
    print(f"    INGESTAO  no corpus       : {i['no_corpus']}  fora: {i['fora_do_corpus']}")
    if "endpoints" in r:
        ep = r["endpoints"]
        print(f"    ENDPOINTS fonte original  : {ep['cobertos_fonte_original']}/{n} ({ep['pct_fonte_original']}%)  ausentes: {ep['ausentes']}")
        print(f"    ENDPOINTS corpus completo : {ep['cobertos_corpus_completo']}/{n} ({ep['pct_corpus_completo']}%)  <- inclui a NOSSA derivacao")
        if r["ausentes_por_familia"]:
            print(f"    ausentes por familia      : {r['ausentes_por_familia']}")
    if e.get("sem_registro"):
        print(f"    sem registro derivado     : {len(e['sem_registro'])} -> {e['sem_registro'][:8]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["rest", "manpages"])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", help="grava o resultado em JSON")
    args = ap.parse_args()

    docs, switches = corpus_atual()
    print(f"  corpus: {len(docs)} docs   switches: {switches}")
    print()

    resultados = []
    if args.all or args.source == "rest":
        resultados.append(medir_rest(docs))
    if args.all or args.source == "manpages":
        resultados.append(medir_manpages(docs))

    for r in resultados:
        imprimir(r)
        print()

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"corpus_docs": len(docs), "switches": switches,
                       "fontes": resultados}, fh, ensure_ascii=False, indent=2)
        print(f"  gravado: {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
