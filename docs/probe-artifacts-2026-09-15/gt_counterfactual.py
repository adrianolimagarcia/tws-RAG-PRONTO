#!/usr/bin/env python3
"""Read-only: replica o pipeline do avaliador do repo tws-RAG-PRONTO e mede
contrafactuais de GT (remocao de expectativas sobre-atribuidas) SEM tocar o repo.

Nao chama run_evaluation() (que grava eval_summary.json). So importa as funcoes.
Uso: PYTHONDONTWRITEBYTECODE=1 python3 gt_counterfactual.py
"""
import json, os, sys, importlib.util, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
EVAL = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")

spec = importlib.util.spec_from_file_location("evrag", EVAL)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

BENCH = os.path.join(REPO, "data", "eval", "golden_qa_benchmark.jsonl")
bench = [json.loads(l) for l in open(BENCH) if l.strip()]

t0 = time.time()
docs = m.load_documents()
print(f"n_docs={len(docs)} (load {time.time()-t0:.1f}s)", flush=True)
from collections import Counter
print("tipos:", Counter(d["type"] for d in docs).most_common(), flush=True)

AUTH = "hwa-lab-10.2.8-rest-api-v2-auth-0001"

# --- variantes de GT: qid -> set de claim_ids a REMOVER da expectativa ---
VARIANTS = {
    "baseline (GT atual)": {},
    "GTv2_doc (remove auth em 4: 0023,0026,0027,0029)": {
        "eval-0023": {AUTH}, "eval-0026": {AUTH}, "eval-0027": {AUTH}, "eval-0029": {AUTH}},
    "GTv2_medido (remove auth em 2: 0023,0029)": {
        "eval-0023": {AUTH}, "eval-0029": {AUTH}},
    "GTv2_max (remove auth em 5, inclui eval-0011)": {
        "eval-0011": {AUTH}, "eval-0023": {AUTH}, "eval-0026": {AUTH},
        "eval-0027": {AUTH}, "eval-0029": {AUTH}},
}

# --- pre-computa o ranking por pergunta UMA vez (o ranking nao depende do GT) ---
rankings = {}
for b in bench:
    qid, q_text = b["id"], b.get("question", "")
    q_tokens = m.tokenize(q_text)
    scored = []
    for doc in docs:
        s = m.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
        if s > 0:
            scored.append([s, doc])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    diversified, seen = [], defaultdict(int)
    for s, doc in scored:
        k = doc.get("runbook") or doc.get("type")
        c = seen[k]
        if doc.get("type") == "ragflow_runbook_chunk" and c >= 2:
            s *= 0.65
        seen[k] += 1
        diversified.append((s, doc))
    diversified.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    rankings[qid] = (m.second_stage_rerank(q_text, diversified, top_n=20), q_tokens, b)
    print(f"  ranqueado {qid} ({time.time()-t0:.0f}s)", flush=True)

json.dump({k: {"top": [d["id"] for d in v[0][:30]], "q": v[2].get("question")}
           for k, v in rankings.items()},
          open("/root/workspace/rankings_top30.json", "w"), ensure_ascii=False, indent=1)


def match_rank(d, expected_cids, expected_runbook, q_tokens):
    if d["id"] in expected_cids:
        return True
    if d["type"] == "aws_message":
        for e in expected_cids:
            if d.get("code", "").lower() in e.lower():
                return True
    if d["type"] in ("ragflow_runbook_chunk", "runbook_section") and expected_runbook \
            and d.get("runbook") == expected_runbook:
        oc = len(q_tokens.intersection(d["tokens"]))
        if oc >= 2 and (oc / max(1, len(q_tokens))) >= 0.25:
            return True
    return False


print("\n=== CONTRAFACTUAIS ===")
out = {}
for name, removals in VARIANTS.items():
    hits = {1: 0, 3: 0, 5: 0, 10: 0}
    rr = []
    per_q = {}
    for b in bench:
        qid = b["id"]
        retr, q_tokens, _ = rankings[qid]
        exp = set(b.get("relevant_claim_ids", [])) - removals.get(qid, set())
        rb = b.get("runbook_ref")
        rank = None
        why = None
        for i, d in enumerate(retr):
            if match_rank(d, exp, rb, q_tokens):
                rank = i + 1
                why = "claim" if d["id"] in exp else ("aws_code" if d["type"] == "aws_message" else "runbook_match3")
                break
        per_q[qid] = (rank, why, sorted(exp))
        if rank:
            rr.append(1.0 / rank)
            for k in hits:
                if rank <= k:
                    hits[k] += 1
        else:
            rr.append(0.0)
    n = len(bench)
    mrr = sum(rr) / n
    out[name] = dict(hits=hits, mrr=mrr, per_q=per_q)
    print(f"{name:52s} @1 {hits[1]:2d}/{n}  @3 {hits[3]:2d}  @5 {hits[5]:2d}  @10 {hits[10]:2d}  MRR {mrr:.4f}")

print("\n=== EFEITO POR PERGUNTA (rank antes -> depois) ===")
base = out["baseline (GT atual)"]["per_q"]
for name in VARIANTS:
    if name.startswith("baseline"):
        continue
    print(f"\n-- {name}")
    for qid in sorted(VARIANTS[name]):
        r0, w0, e0 = base[qid]
        r1, w1, e1 = out[name]["per_q"][qid]
        flag = "  <== MUDOU" if r0 != r1 else ""
        print(f"   {qid}: rank {r0} ({w0}) -> {r1} ({w1}) | exp {len(e0)}->{len(e1)} | via={w1}{flag}")

json.dump({k: {"hits": v["hits"], "mrr": v["mrr"],
               "per_q": {q: v["per_q"][q] for q in v["per_q"]}}
           for k, v in out.items()},
          open("/root/workspace/gt_counterfactual_results.json", "w"), ensure_ascii=False, indent=1)
print("\nwrote /root/workspace/gt_counterfactual_results.json")
