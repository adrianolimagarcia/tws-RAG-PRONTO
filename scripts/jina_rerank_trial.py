#!/usr/bin/env python3
"""TRIAL read-only: re-ranqueia o top-N do pipeline lexical com o Jina reranker (API).

NAO altera o avaliador, o corpus, o boost nem o rerank do harness. A chave e lida de
/root/.haos/secrets/jina_api_key.txt (nunca do repo, nunca impressa, nunca em log).
Aborta sozinho se o gasto acumulado passar de JINA_BUDGET tokens (default 600k).

Replica as 3 regras de match do avaliador (claim id exato; codigo de mensagem em
aws_message; chunk de runbook com o mesmo runbook_ref e overlap >= 2 tokens e >= 25%).

Uso:
  python3 scripts/jina_rerank_trial.py --slice D
  python3 scripts/jina_rerank_trial.py --slice q70 --limit 25
  python3 scripts/jina_rerank_trial.py --slice A --limit 25 --topn 20
"""
import argparse
import importlib.util
import json
import os
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET = os.environ.get("JINA_SECRET", "/root/.haos/secrets/jina_api_key.txt")
API = "https://api.jina.ai/v1/rerank"
BUDGET = int(os.environ.get("JINA_BUDGET", "600000"))
TEXT_CAP = int(os.environ.get("JINA_TEXT_CAP", "800"))


def api_key():
    with open(SECRET, encoding="utf-8") as fh:
        return fh.read().strip()


def jina_rerank(query, documents, model, tentativas=5):
    """Chama o rerank com retry/backoff: a API responde 429 (rate limit) apos ~20
    chamadas seguidas. Sem isto o trial morre no meio (aconteceu)."""
    body = json.dumps({"model": model, "query": query, "documents": documents}).encode()
    for i in range(tentativas):
        req = urllib.request.Request(
            API, data=body,
            headers={"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and i < tentativas - 1:
                espera = 3 * (2 ** i)   # 3s, 6s, 12s, 24s
                print(f"  (HTTP {exc.code}) aguardando {espera}s...", flush=True)
                time.sleep(espera)
                continue
            raise
        finally:
            time.sleep(0.7)   # espacamento entre chamadas


def load_eval():
    spec = importlib.util.spec_from_file_location(
        "ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m


def harness_top(m, q_text, docs, topn):
    """Os candidatos EXATAMENTE como o harness os ordena: BM25 -> MMR (penaliza o 3o+
    chunk do mesmo runbook) -> second_stage_rerank. E este o baseline real (53/70)."""
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
    ret = m.second_stage_rerank(q_text, div, top_n=topn)
    return list(ret)[:topn]


def lexical_top(m, q_text, docs, topn):
    """Ranking lexical puro (BM25) — e dele que saem os candidatos para o Jina."""
    qt = m.tokenize(q_text)
    scored = []
    for d in docs:
        s = m.compute_bm25(qt, d["tokens"], q_text, d["text"], doc=d)
        if s > 0:
            scored.append((s, d))
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [d for _, d in scored[:topn]]


def rank_of(m, ordered_docs, q_text, expected_cids, expected_runbook):
    """Mesmas 3 regras de match do avaliador, para comparacao justa."""
    qt = m.tokenize(q_text)
    for idx, d in enumerate(ordered_docs):
        if d["id"] in expected_cids:
            return idx + 1
        if d.get("type") == "aws_message":
            for ecid in expected_cids:
                if d.get("code", "").lower() in ecid.lower():
                    return idx + 1
        if (d.get("type") in ("ragflow_runbook_chunk", "runbook_section")
                and expected_runbook and d.get("runbook") == expected_runbook):
            ov = len(qt.intersection(d["tokens"]))
            if ov >= 2 and (ov / max(1, len(qt))) >= 0.25:
                return idx + 1
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slice", default="D", choices=["A", "B", "D", "q70"])
    ap.add_argument("--limit", type=int, default=0, help="0 = todas")
    ap.add_argument("--topn", type=int, default=20)
    ap.add_argument("--model", default="jina-reranker-v3")
    ap.add_argument("--candidates", default="harness", choices=["bm25", "harness"],
                    help="de onde saem os candidatos: 'harness' = o pipeline real (53/70)")
    args = ap.parse_args()

    m = load_eval()
    docs = m.load_documents()

    if args.slice == "q70":
        summ = json.load(open(os.path.join(REPO, "data", "eval", "eval_summary.json"), encoding="utf-8"))
        bench = [{"id": d["id"], "question": d["question"],
                  "relevant_claim_ids": d.get("expected_claims") or [],
                  "runbook_ref": d.get("expected_runbook")} for d in summ["details"]]
    else:
        path = os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")
        bench = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
        # o nome da fatia no arquivo e o nome longo (A_com_ancora, B_sem_ancora, D_holdout_temporal)
        slice_map = {"A": "A_com_ancora", "B": "B_sem_ancora", "D": "D_holdout_temporal"}
        alvo = slice_map.get(args.slice, args.slice)
        bench = [x for x in bench if x.get("slice") == alvo]

    if args.limit:
        bench = bench[:args.limit]

    print(f"slice={args.slice} perguntas={len(bench)} topn={args.topn} modelo={args.model}")
    print(f"budget={BUDGET} tokens  (cap de texto/doc={TEXT_CAP} chars)")
    spent = 0
    base_hits = {"1": 0, "10": 0}
    jina_hits = {"1": 0, "10": 0}
    rows = []
    for b in bench:
        q = b.get("question", "")
        exp = set(b.get("relevant_claim_ids") or [])
        rb = b.get("runbook_ref")
        cands = (harness_top if args.candidates == "harness" else lexical_top)(m, q, docs, args.topn)
        if not cands:
            continue
        # baseline = ordem lexical (o top-N; o rank conta dentro dele)
        r_base = rank_of(m, cands, q, exp, rb)
        texts = [(d.get("text") or "")[:TEXT_CAP] for d in cands]
        try:
            res = jina_rerank(q, texts, args.model)
        except Exception as exc:  # rede/credencial/limite
            print(f"  ERRO na API: {str(exc)[:150]}")
            print(f"  gasto ate agora: {spent} tokens")
            return 1
        spent += int((res.get("usage") or {}).get("total_tokens", 0))
        if spent > BUDGET:
            print(f"  ABORTADO por orcamento: {spent} > {BUDGET} tokens")
            return 1
        # A API devolve os resultados JA ordenados por relevancia; o campo `index`
        # aponta para a posicao ORIGINAL. Reordenar por `index` DESFAZ o rerank
        # (foi um bug real: dava 0 flips e ordem identica a lexical).
        order = [cands[r["index"]] for r in res.get("results", [])]
        r_jina = rank_of(m, order, q, exp, rb)
        if r_base == 1:
            base_hits["1"] += 1
        if r_base and r_base <= 10:
            base_hits["10"] += 1
        if r_jina == 1:
            jina_hits["1"] += 1
        if r_jina and r_jina <= 10:
            jina_hits["10"] += 1
        rows.append((b["id"], r_base, r_jina))
        if len(rows) % 10 == 0:
            print(f"  ... {len(rows)}/{len(bench)}  tokens={spent}")

    n = len(rows)
    print()
    print(f"  n={n}   tokens gastos={spent}")
    print(f"  baseline lexical : @1 {base_hits['1']}/{n}   @10 {base_hits['10']}/{n}")
    print(f"  Jina {args.model.split('/')[-1]:<26}: @1 {jina_hits['1']}/{n}   @10 {jina_hits['10']}/{n}")
    melhor = sum(1 for _, a, b in rows if a and b and b < a)
    pior = sum(1 for _, a, b in rows if a and b and b > a)
    print(f"  flips: melhorou={melhor}  piorou={pior}")
    print("  detalhe (id, lexical, jina):")
    for i, a, b in rows:
        mark = "  <== ganhou" if (a and b and b < a) else ("  <== perdeu" if (a and b and b > a) else "")
        print(f"    {i:12s} {str(a):>5} {str(b):>5}{mark}")
    # Persistir SEMPRE: o resumo ja se perdeu uma vez por causa de um `tail` no shell.
    outp = os.path.join(REPO, "docs", "probe-artifacts-2026-09-15",
                        f"jina_{args.slice}_{args.candidates}.json")
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    with open(outp, "w", encoding="utf-8") as fh:
        json.dump({"slice": args.slice, "model": args.model, "topn": args.topn,
                   "n": n, "tokens": spent, "baseline": base_hits, "jina": jina_hits,
                   "flips": {"melhorou": melhor, "piorou": pior}, "rows": rows},
                  fh, ensure_ascii=False, indent=1)
    print(f"  resultados gravados: {outp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
