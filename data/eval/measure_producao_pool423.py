#!/usr/bin/env python3
"""Mede a PRODUCAO (mcp_server/tws_expert_mcp.py) no pool de 423.

POR QUE ISSO EXISTIA FALTANDO: todo numero de metrica do projeto vinha do harness
(`data/eval/evaluate_rag_benchmark.py`), que usa o scorer de `rag_core/lexical.py` - um
scorer que NAO e' o da producao. O MCP tem BM25 proprio (TF por `postings`, IDF de
Robertson, avgdl derivado do corpus, k1=1.5) e mais um prior de tipo/codigo no 2o estagio.
Medir o lab e reportar como se fosse o sistema era o defeito de metodo.

O que este script mede: exatamente o caminho que o usuario recebe, via
`handle_tool_call("tws_expert_search")`, no pool de 423 perguntas.

Metricas: Hit@1, Hit@3, Hit@5, Hit@10 e MRR sobre `relevant_claim_ids` do gabarito.

Uso:
    python3 data/eval/measure_producao_pool423.py
    RAG_TRADUZ_EN=0 python3 data/eval/measure_producao_pool423.py   # sem a ponte
"""
import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))

POOL = os.path.join(RAIZ, "data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl")
# top_k alto de proposito: aqui nao queremos o top-5 que o usuario ve, queremos a POSICAO
# do alvo no ranking completo (senao Hit@10 e MRR ficam truncados e o numero mente).
TOP_K = 10000


def main():
    import tws_expert_mcp as mcp

    if not os.path.exists(POOL):
        raise SystemExit("pool nao encontrado: %s\nRode data/eval/reconstroi_pool423.py" % POOL)

    itens = [json.loads(l) for l in open(POOL, encoding="utf-8") if l.strip()]
    ranks, t0 = [], time.time()

    # ATENCAO: `ranks` e' indexado pela POSICAO da linha, nunca pelo `id`. Medido: o pool tem
    # 423 linhas mas apenas 413 ids unicos - 10 rotulos `blind-XXXX` sao reusados por perguntas
    # DISTINTAS (6 delas com alvos diferentes). Um dicionario por id colapsa essas 10 linhas e
    # a contagem por subconjunto fica 413 em vez de 423.
    for pos_linha, o in enumerate(itens):
        esperados = set(o.get("relevant_claim_ids") or [])
        if not esperados:
            continue
        res = mcp.handle_tool_call("tws_expert_search",
                                   {"query": o["question"], "top_k": TOP_K})
        achados = [x["claim_id"] for x in res.get("results", [])]
        pos = next((i + 1 for i, c in enumerate(achados) if c in esperados), None)
        ranks.append((pos_linha, o["id"], pos))

    n = len(ranks)
    dur = time.time() - t0

    def hit(k):
        return sum(1 for _i, _d, p in ranks if p is not None and p <= k)

    mrr = sum(1.0 / p for _i, _d, p in ranks if p is not None) / n
    n_ids = len({d for _i, d, _p in ranks})

    ponte = "OFF" if os.environ.get("RAG_TRADUZ_EN") == "0" else "ON"
    print("=" * 76)
    print("PRODUCAO (mcp_server/tws_expert_mcp.py) no pool de %d perguntas" % n)
    print("ponte EN->PT: %s | corpus: %d claims | %.1f ms/pergunta"
          % (ponte, len(mcp.docs), 1000 * dur / n))
    print("=" * 76)
    for k in (1, 3, 5, 10):
        print("  Hit@%-3d %4d/%d (%5.1f%%)" % (k, hit(k), n, 100 * hit(k) / n))
    print("  MRR    %.4f" % mrr)
    if n_ids != n:
        print("  NOTA: %d linhas mas %d ids unicos (o pool reusa rotulos) - nao indexar por id"
              % (n, n_ids))

    print("\n  distribuicao de rank do alvo (1..10 e ausente):")
    for k in range(1, 11):
        q = sum(1 for _i, _d, p in ranks if p == k)
        if q:
            print("     rank %2d: %3d" % (k, q))
    aus = sum(1 for _i, _d, p in ranks if p is None)
    print("     ausente: %3d (%.1f%%)" % (aus, 100 * aus / n))

    # comparacao com o harness, no MESMO conjunto
    res_arq = os.path.join(RAIZ, "data/eval/eval_summary.json")
    if os.path.exists(res_arq):
        try:
            d = json.load(open(res_arq))
            if len(d.get("details", [])) == n:
                h1 = sum(1 for x in d["details"] if x.get("rank") == 1)
                h5 = sum(1 for x in d["details"]
                         if x.get("rank") is not None and x["rank"] <= 5)
                print("\n  (referencia) harness no mesmo conjunto: @1 %d (%.1f%%)  @5 %d (%.1f%%)"
                      % (h1, 100 * h1 / n, h5, 100 * h5 / n))
        except Exception:
            pass

    saida = {
        "conjunto": POOL, "n": n, "ponte_en_pt": ponte, "top_k": TOP_K,
        "ms_por_pergunta": round(1000 * dur / n, 2),
        "hit@1": hit(1), "hit@3": hit(3), "hit@5": hit(5), "hit@10": hit(10),
        "mrr": round(mrr, 4),
        "ausente": sum(1 for _i, _d, p in ranks if p is None),
        "ranks": [{"linha": i, "id": d, "rank": p} for i, d, p in ranks],
    }
    destino = os.environ.get("RAG_OUT", "/tmp/ragexp/producao_pool423.json")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as fh:
        json.dump(saida, fh, ensure_ascii=False, indent=1)
    print("\n  gravado em %s" % destino)


if __name__ == "__main__":
    main()
