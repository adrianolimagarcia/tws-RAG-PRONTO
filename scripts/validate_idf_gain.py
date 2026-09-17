#!/usr/bin/env python3
"""Validacao honesta do ganho do IDF: bootstrap, McNemar e consistencia por fatia.

`idf` deu +6 no blind v3 (183 -> 189) e +1 nos 180 externos. Como o IDF NAO tem parametro livre,
nao ha ajuste a temer - mas +6/262 ~= 0,81 erro-padrao ainda esta dentro da faixa de ruido.

Este script:
  (1) grava o resultado POR PERGUNTA de base e idf (v3 e os 3 externos);
  (2) bootstrap pareado (10.000 reamostragens) no delta do v3 -> intervalo de confianca;
  (3) contagem de McNemar (ganhou/perdeu) e teste exato binomial;
  (4) consistencia por fatia (A/B/D).

READ-ONLY: usa as funcoes de producao para a base e uma copia com IDF para a variante.
"""
import sys, os, json, re, math, random, argparse, time
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

SETS = [
    ("v3", "data/eval/blind_v3_slices.jsonl"),
    ("h100", "data/eval/holdout_100_unseen.jsonl"),
    ("h50", "data/eval/blind_holdout_50_vault.jsonl"),
    ("r30", "data/eval/realistic_blind_holdout_30.jsonl"),
]
OUT = os.path.join(REPO, "data/eval/idf_validation_perquestion.json")

K1, B_, AVG_DL = 1.2, 0.75, 60
HWA_TERMS = ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer",
             "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens",
             "limit", "securityutility", "resync", "twsobjectmonitor", "switcheventprocessor",
             "switchevtp", "helm", "chart", "kubernetes", "tebctl", "cwwkf0011i", "enretain", "wapl",
             "mmrresolve", "symnew", "conddep", "wa_pull_info", "baserecprompt", "aida", "carryforward"]


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


def make_idf_scorer(df, N):
    def sc(qt, doc_tokens, qraw, dtext, doc=None):
        if not doc_tokens:
            return 0.0
        overlap = qt.intersection(doc_tokens)
        if not overlap:
            return 0.0
        score = 0.0
        dl = len(doc_tokens)
        dl_low = dtext.lower()
        for t in sorted(overlap):
            boost = 4.0 if any(x in t for x in HWA_TERMS) else 1.0
            tf = (K1 + 1) / (1.0 + K1 * (1.0 - B_ + B_ * (dl / AVG_DL)))
            d = df.get(t, 0)
            score += boost * tf * math.log((N - d + 0.5) / (d + 0.5) + 1.0)
        q_low = qraw.lower()
        if "processador de eventos" in q_low or "event processor" in q_low:
            if "switcheventprocessor" in dl_low or "switchevtp" in dl_low:
                score += 15.0
        for code in re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", qraw.lower()):
            if code in dl_low:
                score += 15.0
        if doc:
            if doc.get("type") == "message_catalog":
                m = re.search(r"aws([a-z]{3})", doc.get("id", "").lower())
                if m:
                    for fam in E.detect_families(qraw):
                        if fam.lower() == m.group(1):
                            score += E.FAMILY_BOOST
                            break
            dt = doc.get("type")
            if dt == "canonical_claim": score *= 1.25
            elif dt == "lab_evidence": score *= 1.20
            elif dt == "ragflow_runbook_chunk": score *= 1.15
            elif dt == "message_catalog": score *= 1.10
            for token in sorted(qt):
                if token.isalnum() and len(token) > 3 and token in (doc.get("id") or "").lower():
                    score += 4.0
            if doc.get("title") and qt.intersection(E.tokenize(doc["title"])):
                score *= 1.15
            if doc.get("runbook") and doc["runbook"].replace(".md", "").replace("-", "") in qraw.lower().replace("-", ""):
                score *= 1.1
            if dt == "ragflow_runbook_chunk":
                meta = doc.get("metadata", {})
                for cmd in meta.get("commands", []):
                    if cmd.lower() in qraw.lower(): score += 3.5
                for c in meta.get("aws_codes", []):
                    if c.lower() in qraw.lower(): score += 12.0
                if doc.get("path") and qt.intersection(E.tokenize(doc["path"])):
                    score *= 1.2
        return score
    return sc


def main():
    docs = E.load_documents()
    N = len(docs)
    df = Counter()
    for d in docs:
        for t in set(d["tokens"]):
            df[t] += 1
    idf_sc = make_idf_scorer(df, N)
    print(f"[v] n_docs={N}  vocab={len(df)}")

    rows = []
    t0 = time.time()
    for tag, path in SETS:
        bench = [json.loads(l) for l in open(os.path.join(REPO, path)) if l.strip()]
        for b in bench:
            q = b.get("question") or ""
            exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
            if not q:
                continue
            qt = E.tokenize(q)
            out = {}
            for name, sc in (("base", E.compute_bm25), ("idf", idf_sc)):
                scored = []
                for d in docs:
                    s = sc(qt, d["tokens"], q, d["text"], doc=d)
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
                pos = E.second_stage_rerank(q, div, top_n=20)
                out[name] = match_rank(pos, exp, rb, qt)
            rows.append({"set": tag, "slice": b.get("slice", tag),
                         "base": out["base"], "idf": out["idf"]})
        print(f"[v] {tag} ok ({time.time()-t0:.0f}s)", flush=True)

    json.dump(rows, open(OUT, "w"))

    def h1(rs, k):
        return sum(1 for r in rs if r[k] == 1)

    print("\n  POR CONJUNTO:")
    for tag in [t for t, _ in SETS]:
        rs = [r for r in rows if r["set"] == tag]
        print(f"    {tag:<6} n={len(rs):<4} base {h1(rs,'base'):>3} -> idf {h1(rs,'idf'):>3} "
              f"({h1(rs,'idf')-h1(rs,'base'):+d})")

    v3 = [r for r in rows if r["set"] == "v3"]
    ext = [r for r in rows if r["set"] != "v3"]
    print(f"\n  v3 : base {h1(v3,'base')} -> idf {h1(v3,'idf')} ({h1(v3,'idf')-h1(v3,'base'):+d})")
    print(f"  ext: base {h1(ext,'base')} -> idf {h1(ext,'idf')} ({h1(ext,'idf')-h1(ext,'base'):+d})")

    # --- McNemar ---
    g = sum(1 for r in v3 if r["base"] != 1 and r["idf"] == 1)
    l = sum(1 for r in v3 if r["base"] == 1 and r["idf"] != 1)
    print(f"\n  McNEMAR (v3): ganhou {g} | perdeu {l}")
    n = g + l
    if n:
        p = sum(math.comb(n, i) for i in range(g, n + 1)) / (2 ** n) * 2
        print(f"    teste binomial exato (2 lados, H0: p=0,5): p = {min(p,1.0):.4f}"
              f"  {'SIGNIFICATIVO' if p < 0.05 else 'NAO significativo'}")

    # --- bootstrap pareado no v3 ---
    random.seed(12345)
    deltas = []
    idx = list(range(len(v3)))
    for _ in range(10000):
        s = [v3[random.choice(idx)] for _ in idx]
        deltas.append(sum(1 for r in s if r["idf"] == 1) - sum(1 for r in s if r["base"] == 1))
    deltas.sort()
    lo, hi = deltas[int(0.025 * len(deltas))], deltas[int(0.975 * len(deltas))]
    print(f"\n  BOOTSTRAP PAREADO (v3, 10.000): delta medio {sum(deltas)/len(deltas):+.2f} "
          f"IC95% [{lo:+d}, {hi:+d}]")
    print(f"    {'IC NAO inclui 0 -> ganho consistente' if lo > 0 else 'IC INCLUI 0 -> nao conclusivo'}")

    # --- consistencia por fatia ---
    print("\n  POR FATIA (v3):")
    for sl in sorted({r["slice"] for r in v3}):
        rs = [r for r in v3 if r["slice"] == sl]
        print(f"    {sl:<22} base {h1(rs,'base'):>3}/{len(rs):<3} -> idf {h1(rs,'idf'):>3}/{len(rs):<3} "
              f"({h1(rs,'idf')-h1(rs,'base'):+d})")


if __name__ == "__main__":
    main()
