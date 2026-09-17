#!/usr/bin/env python3
"""VALIDACAO HELD-OUT do re-ranker desafiante, com a margem FIXADA DE ANTEMAO.

Por que existe: a varredura (`challenger_margin_sweep.py`) achou o melhor @1 na margem 0,10
OLHANDO as 262 perguntas do blind v3. Isso e' ajuste no conjunto de teste. Um ganho assim NAO
pode ser reportado como resultado antes de ser medido em perguntas que nao participaram da
escolha da margem.

Aqui a margem vem da CLI (default 0,10 = centro do plato 0,08-0,12) e o benchmark e' outro.
Reporta baseline vs desafiante e o detalhe dos flips de rank-1.

Uso:
    python scripts/validate_challenger_holdout.py --bench data/eval/holdout_100_unseen.jsonl
"""
import sys, os, json, argparse, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

K = 20


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True)
    ap.add_argument("--margin", type=float, default=0.10)
    ap.add_argument("--k", type=int, default=K)
    args = ap.parse_args()

    bench = [json.loads(l) for l in open(args.bench) if l.strip()]
    print(f"[val] benchmark: {os.path.basename(args.bench)}  n={len(bench)}  margem FIXA={args.margin}")
    if not bench:
        return
    print(f"[val] campos: {sorted(bench[0].keys())}")

    emb = torch.load(os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"),
                     map_location="cpu", weights_only=False).float()
    ids = json.load(open(os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json")))
    id2row = {}
    for r, cid in enumerate(ids):
        id2row.setdefault(cid, r)

    docs = E.load_documents()
    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).eval()

    res = {"baseline": {"h1": 0, "h3": 0, "h10": 0, "rr": 0.0, "n": 0},
           "desafiante": {"h1": 0, "h3": 0, "h10": 0, "rr": 0.0, "n": 0}}
    flips = defaultdict(int)
    t0 = time.time()

    for i, b in enumerate(bench, 1):
        q = b.get("question") or b.get("q") or ""
        exp = set(b.get("relevant_claim_ids", []))
        rb = b.get("runbook_ref")
        if not q:
            continue
        qt = E.tokenize(q)

        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        div = []
        seen = defaultdict(int)
        for s, d in scored:
            kk = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[kk] >= 2:
                s *= 0.65
            seen[kk] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        pos = E.second_stage_rerank(q, div, top_n=args.k)

        with torch.no_grad():
            ti = tok([q], padding=True, truncation=True, max_length=128, return_tensors="pt")
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
        dsc = []
        for d in pos:
            r = id2row.get(d["id"])
            dsc.append(float(torch.mm(qe, emb[r].unsqueeze(1)).squeeze()) if r is not None else -9.0)

        ranked = list(pos)
        if len(ranked) > 1 and dsc:
            tail = max(range(1, len(dsc)), key=lambda j: dsc[j])
            if dsc[tail] - dsc[0] > args.margin:
                ranked = [ranked[tail]] + [x for j, x in enumerate(ranked) if j != tail]

        for v, rk in (("baseline", pos), ("desafiante", ranked)):
            rr = match_rank(rk, exp, rb, qt)
            s = res[v]; s["n"] += 1
            if rr is not None:
                s["rr"] += 1.0 / rr
                if rr <= 1: s["h1"] += 1
                if rr <= 3: s["h3"] += 1
                if rr <= 10: s["h10"] += 1

        a = match_rank(pos, exp, rb, qt)
        c = match_rank(ranked, exp, rb, qt)
        if a == c:
            flips["igual"] += 1
        elif c is not None and (a is None or c < a):
            flips["ganhou"] += 1
        else:
            flips["perdeu"] += 1

        if i % 40 == 0:
            print(f"[val] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    print("\n" + "=" * 72)
    print(f"  {'variante':<14} {'@1':>10} {'@3':>10} {'@10':>10} {'MRR':>9}")
    print("  " + "-" * 68)
    for v in ("baseline", "desafiante"):
        s = res[v]
        n = max(1, s["n"])
        print(f"  {v:<14} {s['h1']:>4}/{s['n']:<4} {s['h3']:>4}/{s['n']:<4} "
              f"{s['h10']:>4}/{s['n']:<4} {s['rr']/n:>9.4f}")
    d1 = res["desafiante"]["h1"] - res["baseline"]["h1"]
    print(f"\n  DELTA @1 = {d1:+d}   (ganhou {flips['ganhou']} | perdeu {flips['perdeu']} | igual {flips['igual']})")
    print("=" * 72)


if __name__ == "__main__":
    main()
