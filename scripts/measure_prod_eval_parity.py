#!/usr/bin/env python3
"""Mede a divergencia de retrieval entre PRODUCAO (MCP) e LABORATORIO (evaluator).

P0-A do RUNBOOK RAG V4. O gate final e':

    mesma query + mesma config + mesmo corpus manifest
      => mesmos IDs e mesma ordem no MCP e no evaluator

Este script mede o ESTADO ATUAL, que ainda nao satisfaz o gate: o MCP e o evaluator
carregam corpora diferentes e indexam texto diferente (o MCP inclui
`synthetic_questions`; o evaluator nao). O objetivo aqui e' QUANTIFICAR a divergencia,
nao declara-la consertada.

Metricas por consulta:
  - Jaccard@15: sobreposicao dos conjuntos top-15
  - overlap@1: o primeiro documento coincide?
  - Kendall tau aproximado nos itens em comum (ordem relativa)
Agregado: media, mediana, quantis, e quantas consultas tem paridade exata.

Deterministico, offline. Nao altera nenhum dado.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "mcp_server"))


def carrega_consultas(caminho: Path, limite: int | None) -> list[tuple[str, str]]:
    out = []
    for line in caminho.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        q = d.get("question") or d.get("query") or ""
        if q:
            out.append((str(d.get("id") or f"q{len(out)}"), q))
        if limite and len(out) >= limite:
            break
    return out


def ranking_evaluator(consultas: list[tuple[str, str]], top: int) -> dict[str, list[str]]:
    """Ranking do estagio BM25 do laboratorio, replicando `run_evaluation` linha a linha.

    Escopo: e' o estagio LEXICAL PURO. O evaluator aplica MMR/source-diversity e o
    `second_stage_rerank` DEPOIS deste ponto. Comparar aqui mede a divergencia do
    recuperador, nao do pipeline inteiro - o rotulo importa.

    Espelha exatamente (evaluate_rag_benchmark.py ~linhas 281-289):
        q_tokens = tokenize(q_text)                      # sem expand_query
        score = compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
        if score > 0: ...
        sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))   # desempate deterministico
    """
    from rag_core import corpus as corpus_mod
    from rag_core import lexical as lex

    docs = corpus_mod.load_documents()
    # ATENCAO ao schema: o doc do evaluator tem ['id', 'text', 'tokens', 'type'].
    # NAO existe campo 'claim' - usa-lo devolve vazio e zera todos os scores.
    dtokens = {str(d.get("id", "")): d.get("tokens") or set() for d in docs}

    out: dict[str, list[str]] = {}
    for qid, q in consultas:
        qt = lex.tokenize(q)
        scored = []
        for d in docs:
            cid = str(d.get("id", ""))
            s = lex.compute_bm25(qt, dtokens[cid], q, d.get("text") or "", doc=d)
            if s > 0:
                scored.append((s, cid))
        scored.sort(key=lambda x: (-x[0], x[1]))
        out[qid] = [cid for _, cid in scored[:top]]
    return out


def ranking_mcp(consultas: list[tuple[str, str]], top: int) -> dict[str, list[str]]:
    """Ranking da producao, pelo proprio modulo do MCP (importado, nao reimplementado)."""
    import re as _re

    import tws_expert_mcp as mcp

    out: dict[str, list[str]] = {}
    for qid, q in consultas:
        # tokenizador do proprio MCP: re.findall(r"\w+", text.lower())
        tokens = _re.findall(r"\w+", q.lower())
        res = mcp.search_bm25(tokens, top_k=top)
        ids = []
        for r in res or []:
            if isinstance(r, dict):
                ids.append(str(r.get("claim_id") or r.get("id") or ""))
            elif isinstance(r, (list, tuple)) and r:
                ids.append(str(r[0]))
        out[qid] = [i for i in ids if i]
    return out


def jaccard(a: list[str], b: list[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def tau_aprox(a: list[str], b: list[str]) -> float | None:
    """Kendall tau sobre os itens presentes nos dois rankings."""
    comuns = [x for x in a if x in set(b)]
    if len(comuns) < 2:
        return None
    pos_a = {x: i for i, x in enumerate(a)}
    pos_b = {x: i for i, x in enumerate(b)}
    conc = disc = 0
    for i in range(len(comuns)):
        for j in range(i + 1, len(comuns)):
            da = pos_a[comuns[i]] - pos_a[comuns[j]]
            db = pos_b[comuns[i]] - pos_b[comuns[j]]
            if da * db > 0:
                conc += 1
            elif da * db < 0:
                disc += 1
    tot = conc + disc
    return (conc - disc) / tot if tot else None


docs_by_id: dict[str, dict] = {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--benchmark", default=str(REPO / "data" / "eval" / "blind_v3_slices.jsonl"))
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--limite", type=int, default=None)
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    consultas = carrega_consultas(Path(args.benchmark), args.limite)
    if not consultas:
        print("erro: nenhuma consulta carregada", file=sys.stderr)
        return 1
    print(f"consultas: {len(consultas)}  benchmark: {Path(args.benchmark).name}  top={args.top}")

    global docs_by_id
    from rag_core import corpus as corpus_mod
    docs = corpus_mod.load_documents()
    for d in docs:
        docs_by_id[str(d.get("id") or d.get("claim_id") or "")] = d
    print(f"corpus do evaluator: {len(docs)} docs")

    import tws_expert_mcp as mcp
    n_mcp = len(getattr(mcp, "docs", []) or [])
    print(f"corpus do MCP: {n_mcp} docs (carregado de {getattr(mcp, 'CORPUS_FILE', '?')})")

    print("rodando evaluator...")
    re_ = ranking_evaluator(consultas, args.top)
    print("rodando MCP...")
    rm = ranking_mcp(consultas, args.top)

    # GUARDA DE ZERO SILENCIOSO: corpus vazio ou ranking vazio nao e' resultado.
    # Um medidor que le o atributo errado produz "0% de paridade" indistinguivel de
    # divergencia real. Abortar e' a unica resposta honesta.
    vazios = []
    if not docs:
        vazios.append("corpus do evaluator vazio")
    if n_mcp == 0:
        vazios.append("corpus do MCP vazio (atributo errado? o modulo usa `docs`)")
    n_sem_ranking = sum(1 for v in rm.values() if not v)
    if n_sem_ranking == len(consultas):
        vazios.append("MCP nao devolveu nenhum resultado para nenhuma consulta")
    n_sem_ranking_ev = sum(1 for v in re_.values() if not v)
    if n_sem_ranking_ev == len(consultas):
        vazios.append("evaluator nao devolveu nenhum resultado para nenhuma consulta "
                      "(schema do doc errado? as chaves sao id/text/tokens/type, NAO 'claim')")

    # GUARDA DE ESPACO DE ID: se os dois corpora nao compartilham NENHUM id, o Jaccard
    # 0,0000 e' artefato de comparacao, nao divergencia de retrieval.
    ids_ev = {str(d.get("id", "")) for d in docs}
    ids_mcp = {str(i) for i in getattr(mcp, "doc_ids", [])}
    if ids_ev and ids_mcp and not (ids_ev & ids_mcp):
        vazios.append("os corpora NAO compartilham nenhum id - comparacao impossivel")

    if vazios:
        print()
        print("  ABORTADO — medicao invalida (zero silencioso):")
        for v in vazios:
            print(f"    - {v}")
        print("  Nao reporte isto como '0% de paridade': e' falha do medidor, nao resultado.")
        return 2

    linhas = []
    for qid, _ in consultas:
        a, b = re_.get(qid, []), rm.get(qid, [])
        linhas.append({
            "qid": qid,
            "jaccard15": jaccard(a, b),
            "overlap1": 1.0 if (a and b and a[0] == b[0]) else 0.0,
            "tau": tau_aprox(a, b),
            "n_eval": len(a), "n_mcp": len(b),
            "top1_eval": a[0] if a else None, "top1_mcp": b[0] if b else None,
        })

    js = [x["jaccard15"] for x in linhas]
    ov = [x["overlap1"] for x in linhas]
    taus = [x["tau"] for x in linhas if x["tau"] is not None]
    exatos = sum(1 for x in linhas if x["jaccard15"] == 1.0 and x["overlap1"] == 1.0)

    res = {
        "benchmark": Path(args.benchmark).name,
        "top": args.top,
        "n_consultas": len(linhas),
        "n_docs_evaluator": len(docs),
        "n_docs_mcp": n_mcp,
        "jaccard15": {"media": statistics.mean(js) if js else None,
                      "mediana": statistics.median(js) if js else None,
                      "min": min(js) if js else None, "max": max(js) if js else None},
        "overlap_at_1": statistics.mean(ov) if ov else None,
        "tau_medio": statistics.mean(taus) if taus else None,
        "consultas_com_paridade_exata": exatos,
        "por_consulta": linhas,
    }

    print()
    print("=== PARIDADE PRODUCAO x LABORATORIO ===")
    print(f"  corpus: evaluator={res['n_docs_evaluator']}  MCP={res['n_docs_mcp']}  "
          f"{'IGUAIS' if res['n_docs_evaluator'] == res['n_docs_mcp'] else 'DIFERENTES'}")
    print(f"  Jaccard@{args.top}: media={res['jaccard15']['media']:.4f} "
          f"mediana={res['jaccard15']['mediana']:.4f} "
          f"min={res['jaccard15']['min']:.4f} max={res['jaccard15']['max']:.4f}")
    print(f"  overlap@1 (mesmo 1o doc): {res['overlap_at_1']:.4f}")
    print(f"  tau medio (ordem relativa): {res['tau_medio']}")
    print(f"  consultas com paridade EXATA (Jaccard=1 e mesmo top1): "
          f"{exatos}/{len(linhas)}")
    print()
    veredito = "PASS" if (res["n_docs_evaluator"] == res["n_docs_mcp"] and exatos == len(linhas)) else "FAIL"
    print(f"  GATE (mesmo corpus + ranking identico): {veredito}")
    if veredito == "FAIL":
        print("  -> esperado: a fatia do MCP ainda nao foi feita. Este numero e' a linha de base")
        print("     que a mudanca tem de levar a paridade.")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nrelatorio: {args.json_out}")
    return 0 if veredito == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
