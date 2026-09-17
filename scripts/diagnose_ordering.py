#!/usr/bin/env python3
"""Anatomia da falha de ORDENACAO nas fatias reais (blind v3, 262 perguntas).

O que mede, e por que decide o desenho do re-ranker:

(a) EM QUE RANK perdemos o documento certo. Se o doc certo esta em rank 2-3, um ajuste leve
    resolve; se esta em 21-50, precisa de re-rank forte; se nao esta no pool, o problema e outro.
(b) O SCORE DO TOP-1 LEXICAL separa a fatia A (com ancora) da B/D (sem ancora)? Se separar,
    existe um GATE barato: confiar no lexical quando o top-1 e forte, re-ranquear quando e fraco.
    Foi exatamente o que faltou nos 4 trials anteriores - todos re-ranquearam TUDO e destruiram A.

Sem GPU para o lexical; usa o denso so para montar o pool da uniao.
"""
import sys, os, json, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

TOPN = 50


def rank_of(ranked, expected, exp_rb, qt):
    for i, d in enumerate(ranked):
        if d["id"] in expected:
            return i + 1
        if d["type"] == "aws_message":
            if any(d.get("code", "").lower() in c.lower() for c in expected):
                return i + 1
        elif d["type"] in ("ragflow_runbook_chunk", "runbook_section") and exp_rb \
                and d.get("runbook") == exp_rb:
            ov = len(qt.intersection(d["tokens"]))
            if ov >= 2 and (ov / max(1, len(qt))) >= 0.25:
                return i + 1
    return None


def main():
    emb = torch.load(os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"),
                     map_location="cpu", weights_only=False).float()
    ids = json.load(open(os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json")))
    docs = E.load_documents()
    by_id = {d["id"]: d for d in docs}

    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).eval()

    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    buckets = ["rank 1", "rank 2-3", "rank 4-10", "rank 11-20", "rank 21-50", "fora do pool"]
    dist = defaultdict(lambda: defaultdict(int))
    topscore = defaultdict(list)
    lexonly_score = defaultdict(list)
    t0 = time.time()

    for i, b in enumerate(bench, 1):
        q = b["question"]; exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
        sl = b["slice"]; qt = E.tokenize(q)

        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append((s, d))
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        if not scored:
            continue
        topscore[sl].append(scored[0][0])

        # pool da uniao (lexical topN + denso topN), ordenado pelo LEXICAL
        with torch.no_grad():
            ti = tok([q], padding=True, truncation=True, max_length=128, return_tensors="pt")
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
            sc = torch.mm(qe, emb.T).squeeze(0)
            dt = torch.topk(sc, k=TOPN).indices.tolist()
        pool_ids = []
        seen = set()
        for _, d in scored[:TOPN]:
            if d["id"] not in seen:
                seen.add(d["id"]); pool_ids.append(d["id"])
        for j in dt:
            cid = ids[j]
            if cid not in seen:
                seen.add(cid); pool_ids.append(cid)

        pool = []
        for cid in pool_ids:
            d = by_id.get(cid)
            if not d:
                continue
            pool.append((E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d), d))
        pool.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        r = rank_of([d for _, d in pool], exp, rb, qt)
        if r is None:
            dist[sl]["fora do pool"] += 1
        elif r == 1:
            dist[sl]["rank 1"] += 1
        elif r <= 3:
            dist[sl]["rank 2-3"] += 1
        elif r <= 10:
            dist[sl]["rank 4-10"] += 1
        elif r <= 20:
            dist[sl]["rank 11-20"] += 1
        else:
            dist[sl]["rank 21-50"] += 1

        # score do top-1 lexical, por resultado
        key = "acertou@1" if r == 1 else "errou@1"
        lexonly_score[(sl, key)].append(scored[0][0])

        if i % 60 == 0:
            print(f"[ana] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    print("\n" + "=" * 84)
    print("  (a) ONDE ESTA O DOCUMENTO CERTO, com o pool da uniao ordenado pelo lexical")
    print("  " + "-" * 80)
    print(f"  {'fatia':<22} " + " ".join(f"{b:>12}" for b in buckets))
    for sl in sorted(dist):
        tot = sum(dist[sl].values())
        cells = [f"{dist[sl][b]:>3} {100*dist[sl][b]/max(1,tot):>5.1f}%" for b in buckets]
        print(f"  {sl:<22} " + " ".join(f"{c:>12}" for c in cells))

    print("\n" + "=" * 84)
    print("  (b) O SCORE DO TOP-1 LEXICAL separa acerto de erro? (candidato a GATE)")
    print("  " + "-" * 80)
    print(f"  {'fatia / resultado':<34} {'n':>4} {'mediana':>9} {'media':>9} {'min':>9} {'max':>9}")
    for k in sorted(lexonly_score):
        v = sorted(lexonly_score[k])
        if not v:
            continue
        med = v[len(v) // 2]
        print(f"  {k[0]+' / '+k[1]:<34} {len(v):>4} {med:>9.2f} {sum(v)/len(v):>9.2f} {v[0]:>9.2f} {v[-1]:>9.2f}")

    print("\n" + "=" * 84)
    print("  (c) A vs B/D no score do top-1 (o gate tem de separar ISSO)")
    print("  " + "-" * 80)
    for sl in sorted(topscore):
        v = sorted(topscore[sl])
        med = v[len(v) // 2]
        print(f"  {sl:<34} n={len(v):>4} mediana={med:>9.2f} media={sum(v)/len(v):>9.2f}")
    a = sorted(topscore.get("A_com_ancora", []))
    bd = sorted(topscore.get("B_sem_ancora", []) + topscore.get("D_holdout_temporal", []))
    if a and bd:
        print(f"\n  mediana A = {a[len(a)//2]:.2f}   mediana B+D = {bd[len(bd)//2]:.2f}")
        print(f"  minimo A  = {a[0]:.2f}   maximo B+D = {bd[-1]:.2f}")


if __name__ == "__main__":
    main()
