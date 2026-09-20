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


def carrega_pool(usar_split_honesto=True):
    """Pool de perguntas distintas.

    Default: o split honesto (disjunto por evidencia) - e' a estimativa nao inflada.
    Com `--pool-completo`: o pool decontaminado inteiro, que tem ~3x mais perguntas e
    da' um limiar mais estavel, ao custo de incluir perguntas que ja' foram vistas.
    Os dois numeros divergem; reporte qual foi usado.
    """
    if usar_split_honesto and POOL.exists():
        caminhos = [POOL]
        fonte = str(POOL.relative_to(REPO))
    else:
        dec = REPO / "data" / "eval" / "decontaminated"
        caminhos = sorted(p for p in dec.glob("*.jsonl") if "negatives" not in p.name)
        fonte = "decontaminated/*"
    pool = {}
    for p in caminhos:
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            q = r.get("question", "").strip().lower()
            if q and q not in pool:
                pool[q] = r
    return list(pool.values()), fonte


def calibra_rag_core(bench):
    """Mesmo sinal do MCP: MARGEM (top1 - top2), para os dois serem comparaveis."""
    from rag_core.corpus import load_documents
    from rag_core.lexical import tokenize, compute_bm25, prepare_corpus
    docs = load_documents()
    prepare_corpus(docs)
    ids = {d["id"] for d in docs}
    scores, rotulo = [], []
    for b in bench:
        q = b.get("question", "")
        qt = tokenize(q)
        pontuados = []
        for d in docs:
            s = compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                pontuados.append(s)
        pontuados.sort(reverse=True)
        s1 = pontuados[0] if pontuados else 0.0
        s2 = pontuados[1] if len(pontuados) > 1 else 0.0
        scores.append(s1 - s2)
        rotulo.append(bool(set(b.get("relevant_claim_ids", []) or []) & ids))
    return docs, scores, rotulo, "margem (top1-top2)"


def calibra_mcp(bench):
    """Corpus de PRODUCAO: o mesmo que o mcp_server indexa.

    Usa a MARGEM (top1 - top2) como sinal, nao o score absoluto: a margem separa
    "top-1 e' a claim certa" com AUC 0,850 contra 0,669 do score absoluto.
    """
    sys.path.insert(0, str(REPO / "mcp_server"))
    import tws_expert_mcp as mcp
    import re
    scores, rotulo = [], []
    for b in bench:
        q = b.get("question", "")
        toks = re.findall(r"\w+", q.lower())
        try:
            # top_k=2 basta para a margem; mais que isso so' custa tempo
            res = mcp.search_bm25(toks, top_k=2)
            s1 = res[0]["score"] if res else 0.0
            s2 = res[1]["score"] if len(res) > 1 else 0.0
        except Exception:
            s1, s2 = 0.0, 0.0
        scores.append((s1 - s2) / s1 if s1 > 0 else 0.0)
        # ROTULO = a decisao real: "o top-1 e' a evidencia esperada?". Usar "a evidencia
        # existe no corpus" como rotulo da um alvo mais fraco (AUC ~0,75 em vez de ~0,85),
        # porque o sistema ainda pode errar qual documento entrega - e e' esse erro que
        # chega ao usuario como alucinacao.
        rel = set(b.get("relevant_claim_ids", []) or [])
        top1 = res[0]["claim_id"] if res else None
        rotulo.append(bool(top1 and top1 in rel))
    return mcp.docs, scores, rotulo, "margem normalizada (1 - top2/top1)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mcp", action="store_true", help="calibra o scorer de PRODUCAO")
    ap.add_argument("--pool-completo", action="store_true",
                    help="usa o pool decontaminado inteiro (~423 perguntas) em vez do "
                         "split honesto (140). Limiar mais estavel, porem inclui "
                         "perguntas ja' vistas - reporte junto com o numero.")
    ap.add_argument("--aplicar", type=float, metavar="LIMIAR",
                    help="grava o limiar em data/eval/abstention.json para o MCP usar "
                         "sem precisar de variavel de ambiente")
    args = ap.parse_args()
    bench, fonte = carrega_pool(usar_split_honesto=not args.pool_completo)
    print(f"perguntas: {len(bench)}  (fonte: {fonte})")

    if args.mcp:
        docs, scores, rotulo, sinal = calibra_mcp(bench)
        nome = "mcp_server.search_bm25 (PRODUCAO)"
    else:
        docs, scores, rotulo, sinal = calibra_rag_core(bench)
        nome = "rag_core.compute_bm25 (BENCHMARK)"
    print(f"sinal: {sinal}")

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
