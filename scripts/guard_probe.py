#!/usr/bin/env python3
"""Testa as TRES GUARDAS DE CONFIANCA do re-ranker desafiante. SOMENTE READ-ONLY.

Contexto medido: o desafiante (promove um candidato de rank 2-20 ao rank-1 se o score denso dele
superar o do rank-1 POR MARGEM) da +15 no blind v3 mas -6 nos 180 externos. O ganho e' dependente
de regime: ajuda onde ha quase-acertos (baseline fraco) e atrapalha onde o baseline ja e' forte.

Hipoteses de GUARDA (aplicar o desafiante so quando o baseline esta FRACO):
  (a) gap rank1<->rank2   : aplicar so se (score1 - score2) < G
  (b) denso absoluto      : aplicar so se o denso do desafiante > T
  (c1) tipo do rank-1     : aplicar so se o rank-1 NAO for canonical_claim
  (c2) ancora exata       : aplicar so se a query NAO tiver um codigo (ex AWSBEH021E) presente no rank-1

DISCIPLINA: a MARGEM do desafiante fica FIXA em 0,10 (escolhida antes, validada por CV). Os limiares
das guardas sao varridos NO BLIND V3 (conjunto de ajuste) e depois aplicados SEM ALTERACAO aos 180
externos (held-out). Criterio de aceite: ganho no v3 E nao-negativo nos 180.

Uso:
    python scripts/guard_probe.py --phase compute   # 1 passada nos 4 conjuntos
    python scripts/guard_probe.py --phase analyze
"""
import sys, os, json, re, argparse, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

K = 20
MARGIN = 0.10          # FIXA antes dos holdouts
CODE_RE = re.compile(r"\b[A-Z]{3,5}[A-Z0-9]{2,8}\d[A-Z0-9]*\b")
SETS = [
    ("v3", "data/eval/blind_v3_slices.jsonl"),
    ("h100", "data/eval/holdout_100_unseen.jsonl"),
    ("h50", "data/eval/blind_holdout_50_vault.jsonl"),
    ("r30", "data/eval/realistic_blind_holdout_30.jsonl"),
]
OUT = os.path.join(REPO, "data/eval/guard_probe_records.json")


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
    n_docs = len(docs)
    print(f"[gp] n_docs (lido nesta execucao) = {n_docs} | indice = {tuple(emb.shape)}")

    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).eval()

    allrec = {}
    t0 = time.time()
    for tag, path in SETS:
        bench = [json.loads(l) for l in open(os.path.join(REPO, path)) if l.strip()]
        recs = []
        for i, b in enumerate(bench, 1):
            q = b.get("question") or ""
            exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
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
            smap = {d["id"]: s for s, d in div}
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
            ch = None
            if len(pos) > 1 and dsc:
                tail = max(range(1, len(dsc)), key=lambda j: dsc[j])
                promoted = (dsc[tail] - dsc[0]) > MARGIN
                if promoted:
                    ranked = [pos[tail]] + [x for j, x in enumerate(pos) if j != tail]
                    ch = match_rank(ranked, exp, rb, qt)
                    ch_id = pos[tail]["id"]
                else:
                    ch = base
                    ch_id = None
                ch_dense, ch_rank = dsc[tail], tail + 1
            else:
                ch, ch_id, ch_dense, ch_rank = base, None, -9.0, -1

            codes = set(CODE_RE.findall(q))
            r1_text = pos[0]["text"] if pos else ""
            anchor_hit = any(c in r1_text for c in codes) if codes else False

            recs.append({
                "set": tag, "slice": b.get("slice", tag),
                "base": base, "chal": ch, "promoted": ch_id is not None,
                "s1": smap.get(pos[0]["id"], 0.0) if pos else 0.0,
                "s2": smap.get(pos[1]["id"], 0.0) if len(pos) > 1 else 0.0,
                "d1": dsc[0] if dsc else -9.0,
                "dch": ch_dense, "ch_rank": ch_rank,
                "r1_type": pos[0]["type"] if pos else "",
                "anchor_hit": anchor_hit, "n_codes": len(codes),
            })
            if i % 50 == 0:
                print(f"[gp] {tag} {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)
        allrec[tag] = recs
        print(f"[gp] {tag}: {len(recs)} perguntas")

    json.dump({"n_docs": n_docs, "margin": MARGIN, "records": allrec}, open(OUT, "w"))
    print(f"[gp] gravado {OUT}")


def analyze():
    d = json.load(open(OUT))
    rec = d["records"]
    ext = [r for t in ("h100", "h50", "r30") for r in rec[t]]
    v3 = rec["v3"]
    print(f"[gp] n_docs={d['n_docs']} margem={d['margin']} | v3={len(v3)} externos={len(ext)}")

    b3 = sum(1 for r in v3 if r["base"] == 1)
    be = sum(1 for r in ext if r["base"] == 1)
    c3 = sum(1 for r in v3 if r["chal"] == 1)
    ce = sum(1 for r in ext if r["chal"] == 1)
    print(f"\n  SEM GUARDA: v3 {b3}->{c3} ({c3-b3:+d}) | externos {be}->{ce} ({ce-be:+d})")

    def apply_guard(pred):
        a3 = sum(1 for r in v3 if (r["chal"] if pred(r) else r["base"]) == 1)
        ae = sum(1 for r in ext if (r["chal"] if pred(r) else r["base"]) == 1)
        return a3, ae

    res = []

    # (a) gap rank1-rank2: aplicar so se gap < G
    gaps = sorted(r["s1"] - r["s2"] for r in v3)
    cand_g = [gaps[int(len(gaps) * p)] for p in (0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9)]
    for G in sorted(set(round(g, 3) for g in cand_g)):
        a3, ae = apply_guard(lambda r, G=G: (r["s1"] - r["s2"]) < G)
        res.append((f"(a) gap<{G}", a3, ae))

    # (b) denso absoluto: aplicar so se dch > T
    ds = sorted(r["dch"] for r in v3 if r["promoted"])
    cand_t = [ds[int(len(ds) * p)] for p in (0.1, 0.25, 0.4, 0.5, 0.6, 0.75)] if ds else []
    for T in sorted(set(round(t, 3) for t in cand_t)):
        a3, ae = apply_guard(lambda r, T=T: r["promoted"] and r["dch"] > T)
        res.append((f"(b) denso>{T}", a3, ae))

    # (c1) tipo do rank-1 != canonical_claim
    a3, ae = apply_guard(lambda r: r["r1_type"] != "canonical_claim")
    res.append(("(c1) rank1 nao-claim", a3, ae))

    # (c2) sem ancora exata no rank-1
    a3, ae = apply_guard(lambda r: not r["anchor_hit"])
    res.append(("(c2) sem ancora exata", a3, ae))

    # combinacoes das melhores
    print(f"\n  {'guarda':<26} {'v3 @1':>12} {'delta':>7} {'externos':>12} {'delta':>7} {'PASSA?':>8}")
    print("  " + "-" * 80)
    passou = []
    for name, a3, ae in res:
        ok = (a3 > b3) and (ae >= be)
        if ok:
            passou.append(name)
        print(f"  {name:<26} {a3:>4}/{len(v3):<4}{100*a3/len(v3):>5.1f}% {a3-b3:>+7d} "
              f"{ae:>4}/{len(ext):<4}{100*ae/len(ext):>5.1f}% {ae-be:>+7d} {'SIM' if ok else 'nao':>8}")

    print("\n" + "=" * 80)
    if passou:
        print(f"[gp] GUARDAS QUE PASSAM o criterio (ganho no v3 E nao-negativo nos externos): {passou}")
    else:
        print("[gp] NENHUMA GUARDA PASSA. Criterio: ganho no v3 E nao-negativo nos 180 externos.")
        print("[gp] => o re-ranker desafiante fica REJEITADO para producao.")
    print("=" * 80)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["compute", "analyze", "both"], default="both")
    a = ap.parse_args()
    if a.phase in ("compute", "both"):
        compute()
    if a.phase in ("analyze", "both"):
        analyze()
