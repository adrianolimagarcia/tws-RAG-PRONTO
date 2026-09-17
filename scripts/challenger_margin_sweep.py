#!/usr/bin/env python3
"""Testa o DESENHO DESAFIANTE com varredura de margem, sem modelo novo.

Diagnostico medido: 58 perguntas tem o doc certo em rank 2-10; em 59% delas o rank-1 e' outro
claim quase-duplicado; e re-ranquear TUDO destroi a fatia A (todos os 4 trials anteriores).

Desenho: o rank-1 de PRODUCAO (pos second_stage) so cai se um candidato de rank 2-K o superar
POR MARGEM, segundo o score DENSO (que ja existe, indice v2).

    desafiante = argmax denso entre ranks 2..K
    se denso(desafiante) - denso(rank1) > margem:  promove o desafiante a rank 1

Varre-se a margem de -0.05 a 0.30. O ponto que importa: existe margem com ganho LIQUIDO?
Reporta por fatia, para ver o trade-off A (proteger) x B (atacar) explicitamente.
"""
import sys, os, json, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

K = 20
MARGINS = [-0.05, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.15, 0.20, 0.30]


def load_bench(path):
    return [json.loads(l) for l in open(path) if l.strip()]


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
    emb = torch.load(os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"),
                     map_location="cpu", weights_only=False).float()
    ids = json.load(open(os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json")))
    id2row = {}
    for r, cid in enumerate(ids):
        id2row.setdefault(cid, r)
    docs = E.load_documents()
    by_id = {d["id"]: d for d in docs}

    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).eval()

    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    res = {m: defaultdict(lambda: {"h1": 0, "n": 0}) for m in MARGINS}
    prom = {m: 0 for m in MARGINS}
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
        pos = E.second_stage_rerank(q, div, top_n=K)

        with torch.no_grad():
            ti = tok([q], padding=True, truncation=True, max_length=128, return_tensors="pt")
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
        # denso de cada candidato do top-K
        dsc = []
        for d in pos:
            r = id2row.get(d["id"])
            dsc.append(float(torch.mm(qe, emb[r].unsqueeze(1)).squeeze()) if r is not None else -9.0)

        for m in MARGINS:
            ranked = list(pos)
            if len(ranked) > 1 and dsc:
                tail = max(range(1, len(dsc)), key=lambda j: dsc[j])
                if dsc[tail] - dsc[0] > m:
                    ranked = [ranked[tail]] + [x for j, x in enumerate(ranked) if j != tail]
                    prom[m] += 1
            rr = match_rank(ranked, exp, rb, qt)
            s = res[m][sl]; s["n"] += 1
            if rr == 1:
                s["h1"] += 1

        if i % 60 == 0:
            print(f"[chg] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    slices = sorted({r["slice"] for r in bench})
    print("\n" + "=" * 92)
    print(f"  {'margem':>7} {'promov':>7} {'@1 total':>12} " +
          " ".join(f"{s[:14]:>15}" for s in slices))
    print("  " + "-" * 88)
    base = None
    for m in MARGINS:
        h1 = sum(res[m][s]["h1"] for s in slices)
        n = sum(res[m][s]["n"] for s in slices)
        if m == 0.0:
            pass
        cells = " ".join(f"{res[m][s]['h1']:>4}/{res[m][s]['n']:<4} {100*res[m][s]['h1']/max(1,res[m][s]['n']):>5.1f}%"
                         for s in slices)
        print(f"  {m:>7.2f} {prom[m]:>7} {h1:>5}/{n:<4} {100*h1/max(1,n):>5.1f}% {cells}")

    print("\n  (referencia: baseline de producao = 183/262 = 69,8%; teto oracle dos quase-acertos = 232/262 = 88,5%)")
    print("=" * 92)


if __name__ == "__main__":
    main()
