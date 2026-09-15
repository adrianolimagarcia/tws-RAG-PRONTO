#!/usr/bin/env python3
"""Read-only: teto REAL de re-ranking no benchmark de 70 perguntas.
Para cada pergunta: rank do 1o doc que casa (regra do harness), rank do doc esperado
por id exato, e tamanho do pool (score>0). Responde: um re-ranker PERFEITO sobre o
top-K quantas perguntas poderia recuperar? Nao altera nada.
"""
import json, os, importlib.util, time
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
spec = importlib.util.spec_from_file_location(
    "evrag", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

bench = [json.loads(l) for l in open(os.path.join(REPO, "data", "eval", "golden_qa_benchmark.jsonl")) if l.strip()]
docs = m.load_documents()

def match(d, exp, rb, qt):
    if d["id"] in exp: return "claim"
    if d["type"] == "aws_message":
        for e in exp:
            if d.get("code", "").lower() in e.lower(): return "aws_code"
    if d["type"] in ("ragflow_runbook_chunk", "runbook_section") and rb and d.get("runbook") == rb:
        oc = len(qt.intersection(d["tokens"]))
        if oc >= 2 and (oc / max(1, len(qt))) >= 0.25: return "runbook_match3"
    return None

rows = []
for b in bench:
    q, qt = b.get("question", ""), m.tokenize(b.get("question", ""))
    exp, rb = set(b.get("relevant_claim_ids", [])), b.get("runbook_ref")
    scored = []
    for d in docs:
        s = m.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
        if s > 0: scored.append([s, d])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    div, seen = [], defaultdict(int)
    for s, d in scored:
        k = d.get("runbook") or d.get("type")
        if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2: s *= 0.65
        seen[k] += 1
        div.append((s, d))
    div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    ret = m.second_stage_rerank(q, div, top_n=20)
    r_harness, via = None, None
    for i, d in enumerate(ret):
        v = match(d, exp, rb, qt)
        if v: r_harness, via = i + 1, v; break
    # rank do doc ESPERADO por id exato (1o deles) na ordem final
    r_exp = None
    for i, d in enumerate(ret):
        if d["id"] in exp: r_exp = i + 1; break
    # rank do 1o match na ordem do 1o estagio (sem 2a etapa)
    r_stage1 = None
    for i, (s, d) in enumerate(div):
        if match(d, exp, rb, qt): r_stage1 = i + 1; break
    rows.append(dict(qid=b["id"], pool=len(scored), r_harness=r_harness, via=via,
                     r_exp_id=r_exp, r_stage1=r_stage1, n_exp=len(exp), rb=rb,
                     exp_rank1=min([i + 1 for i, d in enumerate(ret) if d["id"] in exp] or [None]) if exp else None))
    print(f"{b['id']} pool={len(scored):5d} harness_rank={r_harness} via={via} exp_id_rank={r_exp} stage1_rank={r_stage1}", flush=True)

json.dump(rows, open("/root/workspace/ceiling70.json", "w"), ensure_ascii=False, indent=1)

misses = [r for r in rows if r["r_harness"] != 1]
print(f"\n=== misses: {len(misses)} ===")
for K in (10, 20, 50, 100):
    rec = [r for r in misses if r["r_harness"] and r["r_harness"] <= K]
    print(f"  misses com 1o match dentro do top-{K} (re-ranker poderia fixar): {len(rec)} -> @1 max = {53+len(rec)}/70")
# esperado presente no pool
print("\nesperado presente no POOL (score>0), por id exato:")
absent = []
for r in rows:
    if r["r_exp_id"] is None and r["r_harness"] != 1:
        absent.append(r["qid"])
print("  misses sem NENHUM doc esperado na ordem final:", absent)
inpool = 0
for b, r in zip(bench, rows):
    if any(d["id"] in set(b.get("relevant_claim_ids", [])) for d in docs): inpool += 1
print(f"  perguntas cujo doc esperado EXISTE no corpus: {inpool}/70")
