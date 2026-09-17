#!/usr/bin/env python3
"""Validacao CRUZADA do re-ranker desafiante DENTRO do regime dificil (blind v3, 262).

Por que existe: a varredura achou +15 escolhendo a margem nas MESMAS 262 perguntas (ajuste no
teste). Os conjuntos held-out do repo (89-98% de baseline) sao faceis demais para testar esta
hipotese: nao tem headroom, e o desafiante so pode atrapalhar la (-6 medido em 180 perguntas).

O teste correto e' k-fold: escolher a margem em k-1 folds e medir no fold que sobrou. O numero
que sai e' o ganho ESPERADO em perguntas que nao participaram da escolha da margem.

Fase 1: computa, por pergunta, acerto@1 do baseline e do desafiante em cada margem -> JSON.
Fase 2: k-fold sobre essa matriz (barato, sem GPU).
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
MARGINS = [-0.05, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.15, 0.20, 0.30]
OUT = os.path.join(REPO, "data/eval/challenger_cv_perquestion.json")


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


def compute():
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

    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    rows = []
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
            kk = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[kk] >= 2:
                s *= 0.65
            seen[kk] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        pos = E.second_stage_rerank(q, div, top_n=K)

        with torch.no_grad():
            ti = tok([q], padding=True, truncation=True, max_length=128, return_tensors="pt")
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
        dsc = []
        for d in pos:
            r = id2row.get(d["id"])
            dsc.append(float(torch.mm(qe, emb[r].unsqueeze(1)).squeeze()) if r is not None else -9.0)

        base = match_rank(pos, exp, rb, qt)
        per = {}
        for m in MARGINS:
            ranked = list(pos)
            if len(ranked) > 1 and dsc:
                tail = max(range(1, len(dsc)), key=lambda j: dsc[j])
                if dsc[tail] - dsc[0] > m:
                    ranked = [ranked[tail]] + [x for j, x in enumerate(ranked) if j != tail]
            per[f"{m}"] = match_rank(ranked, exp, rb, qt)
        rows.append({"slice": sl, "baseline": base, "per_margin": per})
        if i % 60 == 0:
            print(f"[cv] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    json.dump({"margins": MARGINS, "rows": rows}, open(OUT, "w"))
    print(f"[cv] gravado {OUT}  ({len(rows)} perguntas)")


def crossval(folds=5):
    d = json.load(open(OUT))
    margins = [str(m) for m in d["margins"]]
    rows = d["rows"]
    n = len(rows)
    base1 = sum(1 for r in rows if r["baseline"] == 1)

    print(f"\n  baseline @1 = {base1}/{n} ({100*base1/n:.1f}%)")
    print(f"\n  {'margem':>7} {'@1 (in-sample)':>16} {'@1 (held-out CV)':>18}")
    print("  " + "-" * 46)
    # in-sample (o numero enganoso)
    for m in margins:
        h = sum(1 for r in rows if r["per_margin"][m] == 1)
        print(f"  {float(m):>7.2f} {h:>7}/{n:<4}{100*h/n:>5.1f}%", end="")
        # held-out: escolhe a melhor margem nos outros folds
        tot = 0
        for f in range(folds):
            test = [i for i in range(n) if i % folds == f]
            train = [i for i in range(n) if i % folds != f]
            best, bh = None, -1
            for mm in margins:
                hh = sum(1 for i in train if rows[i]["per_margin"][mm] == 1)
                if hh > bh:
                    bh, best = hh, mm
            tot += sum(1 for i in test if rows[i]["per_margin"][best] == 1)
        print(f" {tot:>9}/{n:<4}{100*tot/n:>5.1f}%   (margem escolhida fora do fold)")
    print("\n  Se o held-out CV ficar ABAIXO do baseline, o ganho in-sample era sobreajuste.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["compute", "cv", "both"], default="both")
    ap.add_argument("--folds", type=int, default=5)
    a = ap.parse_args()
    if a.phase in ("compute", "both"):
        compute()
    if a.phase in ("cv", "both"):
        crossval(a.folds)
