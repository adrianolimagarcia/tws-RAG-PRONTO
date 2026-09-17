#!/usr/bin/env python3
"""Alvo cirurgico da ordenacao: quem perde/ganha o rank-1 e o que ocupa o topo nos quase-acertos.

Duas perguntas, ambas caras para o desenho do re-ranker:

(1) FLIPS de rank-1 causados pelo `second_stage_rerank`:
      1 -> 1     manteve
      1 -> >1    PERDEU o rank-1   (regressao pura: alvo de conserto)
      >1 -> 1    GANHOU o rank-1   (o que ele faz de bom)
      >1 -> >1   nao mexeu no topo
(2) Nos quase-acertos (doc certo em rank 2-10 no pos), QUE TIPO de documento esta em rank 1,
    e qual o gap de score. Se houver um padrao (ex.: chunk de runbook batendo claim),
    o conserto e' um BOOST dirigido - sem modelo nenhum.
"""
import sys, os, json, time
from collections import defaultdict, Counter

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
    flips = defaultdict(Counter)
    top1_type = Counter()
    gap = []
    perdeu_exemplos = []
    t0 = time.time()

    for b in bench:
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
        pos = E.second_stage_rerank(q, div, top_n=20)
        rp, rq = match_rank(pre, exp, rb, qt), match_rank(pos, exp, rb, qt)

        if rp == 1 and rq == 1: flips[sl]["1->1 manteve"] += 1
        elif rp == 1 and rq != 1: flips[sl]["1->>1 PERDEU"] += 1
        elif rp != 1 and rq == 1: flips[sl][">1->1 GANHOU"] += 1
        else: flips[sl][">1->>1 neutro"] += 1

        if rp == 1 and rq != 1 and len(perdeu_exemplos) < 6:
            perdeu_exemplos.append((sl, q[:58], pos[0].get("type"), (pos[0].get("id") or "")[:44]))

        # quase-acerto: certo em rank 2-10 no pos -> quem esta em rank 1?
        if rq is not None and 2 <= rq <= 10 and pos:
            top1_type[pos[0].get("type")] += 1
            s1 = next((s for s, d in div if d["id"] == pos[0]["id"]), 0.0)
            gap.append((s1, rq))

    print("\n" + "=" * 80)
    print("  (1) FLIPS DE RANK-1 causados pelo second_stage_rerank")
    print("  " + "-" * 76)
    cols = ["1->1 manteve", "1->>1 PERDEU", ">1->1 GANHOU", ">1->>1 neutro"]
    print(f"  {'fatia':<22} " + " ".join(f"{c:>14}" for c in cols))
    T = Counter()
    for sl in sorted(flips):
        for c in cols: T[c] += flips[sl][c]
        print(f"  {sl:<22} " + " ".join(f"{flips[sl][c]:>14}" for c in cols))
    print(f"  {'TOTAL':<22} " + " ".join(f"{T[c]:>14}" for c in cols))

    print("\n" + "=" * 80)
    print("  (2) NOS QUASE-ACERTOS (certo em rank 2-10): que TIPO ocupa o rank 1?")
    print("  " + "-" * 76)
    tot = sum(top1_type.values())
    for k, v in top1_type.most_common():
        print(f"    {k:<28} {v:>4}  ({100*v/max(1,tot):>5.1f}%)")
    print(f"    {'TOTAL':<28} {tot:>4}")

    if gap:
        r2 = [g for g, r in gap if r == 2]
        print(f"\n    distribuicao do rank do doc certo: " +
              " ".join(f"r{r}={sum(1 for _,x in gap if x==r)}" for r in range(2, 11)))

    print("\n  EXEMPLOS de rank-1 PERDIDO (o que subiu no lugar):")
    for sl, q, ty, cid in perdeu_exemplos:
        print(f"    [{sl[:12]:<12}] {q}")
        print(f"        quem ficou em 1o: {ty} {cid}")

    print("\n" + "=" * 80)
    print(f"  ALVO: consertar {T['1->>1 PERDEU']} regressoes de rank-1 sem perder "
          f"{T['>1->1 GANHOU']} ganhos")
    print("=" * 80)
    print(f"  ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
