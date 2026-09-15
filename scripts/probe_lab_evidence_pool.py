#!/usr/bin/env python3
"""READ-ONLY: por que uma evidencia de lab ENTRA ou fica FORA do pool de recuperacao.

'Pool' = documentos com score BM25 > 0. O avaliador descarta score 0 ANTES de ranquear
(`if score > 0` em run_evaluation), entao score 0 e literalmente 'nao existe' para o retrieval.

Para as fatias que falham (D_holdout_temporal e as perguntas do 70 fora do @1), mede:
  - o score BM25 do documento esperado e o rank final que ele alcanca;
  - o tamanho do documento (o BM25 normaliza por comprimento);
  - quais tokens da pergunta NAO existem no documento (o que o deixaria de fora).

Nao altera corpus, boost nem rerank. Uso: python3 scripts/probe_lab_evidence_pool.py
"""
import importlib.util
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_eval():
    spec = importlib.util.spec_from_file_location(
        "ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m


def main():
    m = load_eval()
    docs = m.load_documents()
    by_id = {d["id"]: d for d in docs}
    types = {}
    for d in docs:
        types[d["id"]] = d.get("type")
    print(f"corpus: {len(docs)} docs")

    def full_rank(q_text, expected_ids):
        """Replica o pipeline de run_evaluation (BM25 -> MMR -> second stage) e devolve
        (rank do esperado, top-5 com tipo). Mede ORDENACAO, nao so presenca."""
        from collections import defaultdict
        qt = m.tokenize(q_text)
        scored = []
        for d in docs:
            s = m.compute_bm25(qt, d["tokens"], q_text, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        seen = defaultdict(int)
        div = []
        for s, d in scored:
            k = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
                s *= 0.65
            seen[k] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        ret = m.second_stage_rerank(q_text, div, top_n=20)
        rank = None
        for i, d in enumerate(ret):
            if d["id"] in expected_ids:
                rank = i + 1
                break
        top5 = [(d["id"][:44], d.get("type")) for d in ret[:5]]
        return rank, top5

    def probe(qid, question, expected, rank):
        qt = m.tokenize(question)
        print(f"\n{qid}  rank={rank}")
        print(f"  Q: {question[:88]}")
        for e in expected:
            d = by_id.get(e)
            if d is None:
                print(f"  ESPERADO AUSENTE DO CORPUS: {e}")
                continue
            s = m.compute_bm25(qt, d["tokens"], question, d["text"], doc=d)
            missing = [t for t in qt if t not in d["tokens"]]
            verdict = "FORA DO POOL (score 0)" if s <= 0 else "no pool"
            print(f"  {e[:58]:58s} tipo={str(types.get(e)):22s} score={s:7.1f} "
                  f"len={len(d['tokens']):5d} {verdict}")
            if missing:
                print(f"      tokens da pergunta ausentes no doc ({len(missing)}): "
                      f"{', '.join(missing[:10])}")

    # 1) fatia D do benchmark cego (a mais fraca)
    bpath = os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")
    if os.path.exists(bpath):
        bench = [json.loads(l) for l in open(bpath, encoding="utf-8") if l.strip()]
        D = [x for x in bench if x.get("slice") == "D_holdout_temporal"]
        print(f"\n=== FATIA D (holdout temporal): {len(D)} perguntas ===")
        for x in D:
            r, top5 = full_rank(x.get("question", ""), set(x.get("relevant_claim_ids") or []))
            probe(x["id"], x.get("question", ""), x.get("relevant_claim_ids") or [], r)
            print(f"      top-5: {top5}")
    else:
        print("blind_v3_slices.jsonl ausente")

    # 2) as perguntas do benchmark de 70 que nao acertam @1
    spath = os.path.join(REPO, "data", "eval", "eval_summary.json")
    if os.path.exists(spath):
        summ = json.load(open(spath, encoding="utf-8"))
        det = [d for d in summ.get("details", []) if not (d.get("rank") and d["rank"] == 1)]
        print(f"\n=== 70 PERGUNTAS fora do @1: {len(det)} ===")
        for d in det:
            probe(d["id"], d.get("question", ""), d.get("expected_claims") or [], d.get("rank"))
    else:
        print("eval_summary.json ausente")


if __name__ == "__main__":
    sys.exit(main())
