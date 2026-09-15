#!/usr/bin/env python3
"""EXPERIMENTO CONTROLADO (read-only no repo): um modelo semantico DIFERENTE do
cross-encoder refutado — bi-encoder denso multilingue (intfloat/multilingual-e5-small,
via ONNX/Xenova; sem torch) — sobre o MESMO top-50 do cache do sandbox, e tambem sobre
o benchmark de 70 perguntas.

Variaveis controladas:
  - mesmo cache/top-50 (v3) e mesmo match do sandbox (_match);
  - texto LIMPO (export primeiro, sem synthetic_questions) para nao vazar a pergunta;
  - cap de texto: 400 chars (identico ao trial do cross-encoder) vs SEM cap (texto integral).
Mede: @1/@3/@5/@10/MRR por fatia (v3) e no 70q; e o hibrido (ancoradas = baseline).

Nao escreve nada no repo. Saidas em /root/workspace/.
"""
import json, os, re, sys, time, unicodedata
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
E5 = "/root/workspace/e5"
CACHE = "/tmp/ha_fm/rerank_cache.json"
BENCH70 = os.path.join(REPO, "data", "eval", "golden_qa_benchmark.jsonl")

CAP = None if (len(sys.argv) > 1 and sys.argv[1] == "full") else 400
print(f"=== CAP = {CAP} ===", flush=True)

# ---------- 1. modelo ----------
tok = Tokenizer.from_file(os.path.join(E5, "tokenizer.json"))
tok.enable_truncation(max_length=512)
tok.enable_padding(pad_id=1, pad_token="<pad>")
sess = ort.InferenceSession(os.path.join(E5, "onnx", "model.onnx"),
                            providers=["CPUExecutionProvider"])
so = ort.SessionOptions()
sess.set_providers(["CPUExecutionProvider"])
IN = [i.name for i in sess.get_inputs()]
print("inputs ONNX:", IN, flush=True)


def embed(texts, prefix, batch=24):
    out = []
    t0 = time.time()
    for i in range(0, len(texts), batch):
        chunk = [prefix + t for t in texts[i:i + batch]]
        enc = tok.encode_batch(chunk)
        ids = np.array([e.ids for e in enc], dtype=np.int64)
        am = np.array([e.attention_mask for e in enc], dtype=np.int64)
        feed = {"input_ids": ids, "attention_mask": am}
        if "token_type_ids" in IN:
            feed["token_type_ids"] = np.zeros_like(ids)
        h = sess.run(None, feed)[0]                     # (b, seq, dim)
        m = am[..., None].astype(np.float32)
        v = (h * m).sum(1) / np.clip(m.sum(1), 1e-9, None)   # mean pooling
        v = v / np.clip(np.linalg.norm(v, axis=1, keepdims=True), 1e-9, None)
        out.append(v.astype(np.float32))
        if i % (batch * 20) == 0:
            print(f"   embed {i}/{len(texts)} ({time.time()-t0:.0f}s)", flush=True)
    return np.vstack(out)


# ---------- 2. mapa de texto limpo (mesma logica do trial do CE) ----------
def clean_map():
    m = {}
    with open(os.path.join(REPO, "data", "export", "tws_corpus_master_consolidated.jsonl"),
              encoding="utf-8") as fh:
        for ln in fh:
            if ln.strip():
                d = json.loads(ln)
                m[d["claim_id"]] = d.get("claim", "")   # SEM synthetic_questions (sem vazamento)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    ev = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev)
    for d in ev.load_documents():
        if d["id"] not in m:
            m[d["id"]] = d["text"]
    return m, ev


textmap, ev = clean_map()
print(f"textmap: {len(textmap)} ids", flush=True)

# ---------- 3. cache v3 + cache 70q ----------
cache = json.load(open(CACHE))
from collections import defaultdict


def build70():
    import importlib.util
    spec = importlib.util.spec_from_file_location("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
    docs = ev.load_documents()
    bench = [json.loads(l) for l in open(BENCH70) if l.strip()]
    out = []
    for b in bench:
        q = b.get("question", "")
        div, qt = rs.pipeline(ev, docs, q)
        base = ev.second_stage_rerank(q, div, top_n=20)
        exp = set(b.get("relevant_claim_ids", []))
        out.append({"id": b["id"], "slice": "q70", "question": q,
                    "expected": list(exp), "runbook": b.get("runbook_ref"),
                    "q_tokens": sorted(qt), "rank_baseline": rs.rank_of(base, exp, b.get("runbook_ref"), qt),
                    "base_order50": [d["id"] for d in base[:50]],
                    "cands": [{"id": d["id"], "type": d.get("type"), "score": s,
                               "ov": len(set(qt) & d["tokens"])} for s, d in div[:50]]})
        print("  70q cache", b["id"], flush=True)
    return rs, out


import importlib.util
spec = importlib.util.spec_from_file_location("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
_rs_unused, c70 = build70()
print(f"cache 70q: {len(c70)} perguntas", flush=True)

ALL = cache + c70

# ---------- 4. textos unicos a embeddar ----------
doc_ids = set()
for e in ALL:
    for c in e["cands"]:
        doc_ids.add(c["id"])
doc_ids = sorted(doc_ids)
texts = []
for cid in doc_ids:
    t = textmap.get(cid, "")
    if CAP:
        t = t[:CAP]
    texts.append(t if t.strip() else "vazio")
print(f"docs unicos a embeddar: {len(texts)}", flush=True)

D = embed(texts, "passage: ")
print(f"embeddings docs: {D.shape} em {time.time():.0f}", flush=True)
Q = embed([e["question"] for e in ALL], "query: ")
idx = {cid: i for i, cid in enumerate(doc_ids)}


def metrics(entries, scorer, label):
    by = defaultdict(list)
    for k, e in enumerate(entries):
        cands = e["cands"]
        order = scorer(k, e)
        rank = None
        for i, c in enumerate(order):
            if rs._match(c, e):
                rank = i + 1
                break
        by[e["slice"]].append(rank)
    line = [f"{label}"]
    for sl in ("A_com_ancora", "B_sem_ancora", "D_holdout_temporal", "q70"):
        rs_ = by.get(sl)
        if not rs_:
            continue
        n = len(rs_)
        h = {k: sum(1 for r in rs_ if r and r <= k) for k in (1, 3, 5, 10)}
        mrr = sum(1 / r for r in rs_ if r) / n
        line.append(f"{sl[:16]:17s} n={n:3d} @1 {100*h[1]/n:5.1f} @3 {100*h[3]/n:5.1f} "
                    f"@5 {100*h[5]/n:5.1f} @10 {100*h[10]/n:5.1f} MRR {mrr:.4f}")
    print("\n".join(line), flush=True)
    return by


def dense(k, e):
    qv = Q[k]
    sims = [(float(np.dot(qv, D[idx[c["id"]]])), c) for c in e["cands"]]
    sims.sort(key=lambda x: (-x[0], str(x[1]["id"])))
    return [c for _, c in sims]


def baseline(k, e):
    return e["cands"]


ANCHOR = re.compile(r"aws[a-z]{3}[0-9]{3}[iew]|composer |conman |planman |optman |cww|/twsd/", re.I)


def hybrid(k, e):
    """Ancoradas (codigo/comando na pergunta) ficam no baseline; o resto vai ao denso."""
    return baseline(k, e) if ANCHOR.search(e["question"]) else dense(k, e)


def probe(k, e):   # sanity check do pipeline denso: so a 1a pergunta
    return dense(k, e)


print("\n=== SANITY: top-3 denso da 1a pergunta v3 vs baseline ===")
e0 = ALL[0]
print("Q:", e0["question"][:100])
print("baseline:", [c["id"][:50] for c in e0["cands"][:3]])
print("denso   :", [(c["id"][:50], round(float(np.dot(Q[0], D[idx[c['id']]])), 3)) for c in dense(0, e0)[:3]])
print("esperado:", e0["expected"])

print("\n=== RESULTADOS ===")
metrics(ALL, baseline, "BASELINE (1o estagio, top-50)  ")
metrics(ALL, dense,    f"DENSO e5-small cap={CAP}       ")
metrics(ALL, hybrid,   f"HIBRIDO e5 cap={CAP} (anc=base)")

# quantas perguntas o denso melhora/piora vs baseline (por fatia) — o numero que decide
print("\n=== FLIPS por fatia (denso vs baseline, @1) ===")
b_by = {}
for k, e in enumerate(ALL):
    order = baseline(k, e)
    r = next((i + 1 for i, c in enumerate(order) if rs._match(c, e)), None)
    b_by[k] = r
d_by = {}
for k, e in enumerate(ALL):
    order = dense(k, e)
    r = next((i + 1 for i, c in enumerate(order) if rs._match(c, e)), None)
    d_by[k] = r
for sl in ("A_com_ancora", "B_sem_ancora", "D_holdout_temporal", "q70"):
    ks = [k for k, e in enumerate(ALL) if e["slice"] == sl]
    if not ks:
        continue
    up = [k for k in ks if (d_by[k] == 1) and (b_by[k] != 1)]
    dn = [k for k in ks if (b_by[k] == 1) and (d_by[k] != 1)]
    print(f"  {sl:22s} n={len(ks):3d}  @1 base={sum(1 for k in ks if b_by[k]==1):3d} "
          f"denso={sum(1 for k in ks if d_by[k]==1):3d}  ganhou={len(up)} perdeu={len(dn)}")
    if sl in ("D_holdout_temporal", "q70"):
        for k in up:
            print(f"      + {ALL[k]['id']} base_rank={b_by[k]} -> 1")
        for k in dn:
            print(f"      - {ALL[k]['id']} base_rank=1 -> {d_by[k]}")
json.dump({"cap": CAP,
           "baseline": {ALL[k]["id"]: b_by[k] for k in b_by},
           "denso": {ALL[k]["id"]: d_by[k] for k in d_by}},
          open(f"/root/workspace/dense_trial_cap{CAP}.json", "w"), ensure_ascii=False, indent=1)
print("wrote", f"/root/workspace/dense_trial_cap{CAP}.json")

