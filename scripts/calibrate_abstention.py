#!/usr/bin/env python3
"""calibrate_abstention.py — acha o limiar de abstencao a partir dos DADOS, por scorer.

POR QUE POR SCORER: existem DOIS scorers no repo e a escala deles nao e' a mesma.
- `rag_core.lexical.compute_bm25` (benchmark) — score de topo tipico 3..85.
- `mcp_server.search_bm25` (producao) — BM25 com k1=1.5, b=0.75 sobre o corpus
  consolidado, escala diferente.
Um limiar calibrado num NAO vale no outro. Este script mede cada um no seu proprio
corpus e imprime o limiar daquele scorer.

O QUE ELE MEDE: para cada pergunta do benchmark, o "score do top-1" e se a evidencia
esperada esta' no corpus. Perguntas cuja evidencia NAO esta' no corpus sao o alvo
perfeito de abstencao: nenhum recuperador pode acerta-las, entao responder e' alucinar
por construcao.

Metricas por limiar:
  respostas boas perdidas  (custo de abster cedo demais)
  alucinacoes evitadas     (beneficio de abster)  -> fracao das nao-respondiveis

Uso:
  python3 scripts/calibrate_abstention.py                 # scorer rag_core
  python3 scripts/calibrate_abstention.py --mcp           # scorer de producao
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
os.chdir(REPO)

POOL = REPO / "data" / "eval" / "splits" / "honest_v1" / "test.jsonl"


def carrega_pool():
    """Pool de perguntas distintas, do split honesto se existir; senao do decontaminado."""
    caminhos = [POOL]
    if not POOL.exists():
        dec = REPO / "data" / "eval" / "decontaminated"
        caminhos = sorted(p for p in dec.glob("*.jsonl") if "negatives" not in p.name)
    pool = {}
    for p in caminhos:
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            q = r.get("question", "").strip().lower()
            if q and q not in pool:
                pool[q] = r
    return list(pool.values()), (caminhos[0].relative_to(REPO) if len(caminhos) == 1 else "decontaminated/*")


def calibra_rag_core(bench):
    from rag_core.corpus import load_documents
    from rag_core.lexical import tokenize, compute_bm25, prepare_corpus
    docs = load_documents()
    prepare_corpus(docs)
    ids = {d["id"] for d in docs}
    scores, rotulo = [], []
    for b in bench:
        q = b.get("question", "")
        qt = tokenize(q)
        best = 0.0
        for d in docs:
            s = compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > best:
                best = s
        scores.append(best)
        rotulo.append(bool(set(b.get("relevant_claim_ids", []) or []) & ids))
    return docs, scores, rotulo


def calibra_mcp(bench):
    """Corpus de PRODUCAO: o mesmo que o mcp_server indexa."""
    sys.path.insert(0, str(REPO / "mcp_server"))
    import tws_expert_mcp as mcp
    scores, rotulo = [], []
    for b in bench:
        q = b.get("question", "")
        toks = __import__("re").findall(r"\w+", q.lower())
        # top-1 mesmo com top_k alto, para nao depender do top_k default
        top = None
        try:
            res = mcp.search_bm25(toks, top_k=1)
            top = res[0]["score"] if res else 0.0
        except Exception:
            top = 0.0
        scores.append(top)
        rotulo.append(bool(set(b.get("relevant_claim_ids", []) or []) & set(mcp.doc_ids)))
    return mcp.docs, scores, rotulo


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mcp", action="store_true", help="calibra o scorer de PRODUCAO")
    args = ap.parse_args()
    bench, fonte = carrega_pool()
    print(f"perguntas: {len(bench)}  (fonte: {fonte})")

    if args.mcp:
        docs, scores, rotulo = calibra_mcp(bench)
        nome = "mcp_server.search_bm25 (PRODUCAO)"
    else:
        docs, scores, rotulo = calibra_rag_core(bench)
        nome = "rag_core.compute_bm25 (BENCHMARK)"

    resp = [s for s, ok in zip(scores, rotulo) if ok]
    nao = [s for s, ok in zip(scores, rotulo) if not ok]
    print(f"corpus: {len(docs)} docs | scorer: {nome}")
    print(f"respondiveis {len(resp)} | nao-respondiveis {len(nao)}")
    if not resp or not nao:
        print("ERRO: faltam grupos para calibrar.")
        return 1

    w = sum(1 for x in resp for y in nao if x > y) + 0.5 * sum(1 for x in resp for y in nao if x == y)
    print(f"AUC (separabilidade) = {w / (len(resp) * len(nao)):.3f}   (0.5 = inutil)")

    print()
    print("  %9s %8s %8s %10s %10s" % ("limiar", "abstem", "boa", "boas perd", "aluc evit"))
    cands = sorted(set(scores))
    passo = max(1, len(cands) // 25)
    for t in cands[::passo]:
        ab = sum(1 for s in scores if s < t)
        perd = sum(1 for s in resp if s < t)
        ev = sum(1 for s in nao if s < t)
        print("  %9.3f %8d %8d %10d %10d" % (t, ab, len(resp) - perd, perd, ev))

    print()
    print("COMO USAR: escolha o limiar pelo custo que voce aceita. Exemplo: o limiar")
    print("imediatamente abaixo da mediana das nao-respondiveis evita ~metade das")
    print("alucinacoes estruturais. NAO reutilize este numero noutro scorer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
