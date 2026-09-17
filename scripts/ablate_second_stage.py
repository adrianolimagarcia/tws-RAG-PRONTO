#!/usr/bin/env python3
"""Ablacao do re-ranker que JA EXISTE (second_stage_rerank), nas fatias reais.

Pergunta: o `second_stage_rerank` (n-gram contiguity + cobertura semantica) melhora ou
PIORA a ordenacao? Ele esta no caminho de producao e nunca foi ablatado nas 262.

Compara tres ordenacoes, todas com o MESMO pool (lexical puro, sem denso, para isolar):
  pre    : diversificacao, sem second_stage          (top-20)
  pos    : diversificacao + second_stage_rerank      (top-20)  <- baseline de producao
  pre10  : diversificacao, sem second_stage, top-10  (controle de tamanho)

Se `pre` > `pos`, o re-ranker existente esta DESTRUINDO ordem e o conserto e' codigo.
"""
import sys, os, json, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402


def match_rank(ranked, exp, exp_rb, qt):
    for i, d in enumerate(ranked):
        if d["id"] in exp:
            return i + 1
        if d["type"] == "aws_message":
            if any(d.get("code", "").lower() in c.lower() for c in exp):
                return i + 1
        elif d["type"] in ("ragflow_runbook_chunk", "runbook_section") and exp_rb \
                and d.get("runbook") == exp_rb:
            ov = len(qt.intersection(d["tokens"]))
            if ov >= 2 and (ov / max(1, len(qt))) >= 0.25:
                return i + 1
    return None


def main():
    docs = E.load_documents()
    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    print(f"[abl] corpus {len(docs)} | perguntas {len(bench)}")

    variants = ("pre", "pos", "pre_top10")
    res = {v: defaultdict(lambda: {"h1": 0, "h3": 0, "h10": 0, "rr": [], "n": 0}) for v in variants}
    trocas = defaultdict(lambda: {"ganhou": 0, "perdeu": 0, "igual": 0})
    t0 = time.time()

    for i, b in enumerate(bench, 1):
        q = b["question"]; exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
        sl = b["slice"]; qt = E.tokenize(q)

        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        div = []
        seen = defaultdict(int)
        for s, d in scored:
            k = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
                s *= 0.65
            seen[k] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        pre = [d for _, d in div][:20]
        pre10 = [d for _, d in div][:10]
        pos = E.second_stage_rerank(q, div, top_n=20)

        r = {}
        for v, ranked in (("pre", pre), ("pos", pos), ("pre_top10", pre10)):
            rr = match_rank(ranked, exp, rb, qt)
            r[v] = rr
            s = res[v][sl]; s["n"] += 1
            if rr is not None:
                s["rr"].append(1.0 / rr)
                if rr <= 1: s["h1"] += 1
                if rr <= 3: s["h3"] += 1
                if rr <= 10: s["h10"] += 1
            else:
                s["rr"].append(0.0)

        # quem o second_stage moveu?
        a, c = r["pre"], r["pos"]
        if a == c:
            trocas[sl]["igual"] += 1
        elif (c is not None) and (a is None or c < a):
            trocas[sl]["ganhou"] += 1
        else:
            trocas[sl]["perdeu"] += 1

        if i % 60 == 0:
            print(f"[abl] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    def agg(v):
        h1 = h3 = h10 = n = 0; rr = 0.0
        for sl, s in res[v].items():
            h1 += s["h1"]; h3 += s["h3"]; h10 += s["h10"]; n += s["n"]; rr += sum(s["rr"])
        return h1, h3, h10, n, (rr / n if n else 0.0)

    print("\n" + "=" * 78)
    print(f"  {'variante':<12} {'@1':>9} {'@3':>9} {'@10':>9} {'MRR':>9}")
    print("  " + "-" * 74)
    for v in variants:
        h1, h3, h10, n, mrr = agg(v)
        print(f"  {v:<12} {h1:>4}/{n:<4} {h3:>4}/{n:<4} {h10:>4}/{n:<4} {mrr:>9.4f}")

    print("\n  POR FATIA (@1):")
    for sl in sorted({r["slice"] for r in bench}):
        cells = []
        for v in variants:
            s = res[v][sl]
            cells.append(f"{s['h1']:>3}/{s['n']:<3} {100.0*s['h1']/max(1,s['n']):>5.1f}%")
        print(f"    {sl:<22} " + " | ".join(cells))

    print("\n  O QUE O second_stage_rerank FEZ (pre -> pos):")
    for sl in sorted(trocas):
        t = trocas[sl]
        print(f"    {sl:<22} ganhou {t['ganhou']:>3} | perdeu {t['perdeu']:>3} | igual {t['igual']:>3}")

    print("\n" + "=" * 78)
    h1p, _, _, _, _ = agg("pre")
    h1q, _, _, _, _ = agg("pos")
    if h1p > h1q:
        print(f"[abl] O second_stage_rerank PIORA o @1: {h1q} com ele vs {h1p} sem ele "
              f"(delta {h1q-h1p}). O re-ranker existente esta destruindo ordem.")
    elif h1p < h1q:
        print(f"[abl] O second_stage_rerank AJUDA o @1: {h1q} com ele vs {h1p} sem ele "
              f"(delta +{h1q-h1p}). O ganho esta em outro lugar.")
    else:
        print(f"[abl] second_stage_rerank e NEUTRO no @1 ({h1q} nos dois).")
    print("=" * 78)


if __name__ == "__main__":
    main()
