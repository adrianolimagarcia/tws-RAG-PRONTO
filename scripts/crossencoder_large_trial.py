#!/usr/bin/env python3
"""FASE 2 - cross-encoder LARGE (bge-reranker-large) na GPU, rota HIBRIDA.

O que muda em relacao ao trial de 14.09 (registrado em
data/evidence/lab-validation-2026-09-14-rag-crossencoder-trial-limited-negative.jsonl):
  - o modelo de la era MEDIO (cross-encoder/mmarco-mMiniLMv2-L12-H384-v1, 471 MB) em CPU;
  - aqui e' BAAI/bge-reranker-large (2,2 GB, JA em disco) na GTX 1050 Ti.
  - mede tambem os 180 externos, nao so' as fatias do v3.

ROTA HIBRIDA (protege A, que e' onde o 2o estagio atual ganha +12,2):
  pergunta COM ancora (codigo/entidade/CLI) -> ordem do BASELINE
  pergunta SEM ancora                        -> ordem do CROSS-ENCODER

Read-only: nao altera o avaliador, o corpus nem o lab. Inferencia apenas - sem treino.
"""
import importlib.util, json, os, re, resource, sys, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"
HF_CACHE = os.path.join(NR, "hf_cache")
MODEL = os.environ.get("CE_MODEL", "BAAI/bge-reranker-large")
TOP_N = int(os.environ.get("CE_TOP_N", "50"))
TEXT_CAP = 400

BENCHES = [
    ("blind_v3_slices", os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")),
    ("holdout_100_unseen", os.path.join(REPO, "data", "eval", "holdout_100_unseen.jsonl")),
    ("blind_holdout_50_vault", os.path.join(REPO, "data", "eval", "blind_holdout_50_vault.jsonl")),
    ("realistic_blind_holdout_30", os.path.join(REPO, "data", "eval", "realistic_blind_holdout_30.jsonl")),
]

# Proxy de "tem ancora" derivado SO' do texto da pergunta (sem rotulo de avaliacao).
ANCHOR_RE = re.compile(
    r"aws[a-z]{3}[0-9]{3}[iew]|"
    r"\b(sfinal|jnextplan|resetplan|makeplan|switchplan|checksync|composer|conman|planman|optman|"
    r"joblog|vartable|rerun|securityutility|resync|twsobjectmonitor|switcheventprocessor|switchevtp|"
    r"tebctl|wapl|mmrresolve|symnew|conddep|aida|carryforward|enretain|kubernetes|helm)\b",
    re.I)


def load_sandbox():
    spec = importlib.util.spec_from_file_location("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    if spec is None or spec.loader is None:
        raise RuntimeError("sem sandbox")
    rs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs)
    return rs


def load_ev():
    spec = importlib.util.spec_from_file_location("ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    if spec is None or spec.loader is None:
        raise RuntimeError("sem avaliador")
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)
    return ev


def clean_text_map(ev):
    """Texto LIMPO por doc: claim cru do export (sem synthetic_questions) para nao vazar a pergunta."""
    corp = {}
    p = os.path.join(REPO, "data", "export", "tws_corpus_master_consolidated.jsonl")
    if os.path.exists(p):
        for ln in open(p, encoding="utf-8"):
            ln = ln.strip()
            if ln:
                d = json.loads(ln)
                corp[d["claim_id"]] = d.get("claim", "")
    m = dict(corp)
    for d in ev.load_documents():
        if d["id"] not in m:
            m[d["id"]] = d["text"]
    return m


def toks(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", s)


def leak_check(entries, m):
    idx = {cid: set(toks(t)) for cid, t in m.items() if t}
    emb = 0
    for e in entries:
        qt = set(toks(e["question"]))
        if not qt:
            continue
        for s in idx.values():
            if s and min(len(qt & s) / len(qt), len(qt & s) / len(s)) >= 0.7:
                emb += 1
                break
    return emb


def build_cache(rs, ev, docs, bench_path, tag, out):
    rows = [json.loads(l) for l in open(bench_path, encoding="utf-8") if l.strip()]
    for r in rows:
        r.setdefault("slice", tag)
    tmp = out + ".bench.jsonl"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    rs.build(ev, docs, tmp, out)
    return json.load(open(out))


def metrics(entries, rank_fn):
    n = len(entries)
    h = {1: 0, 3: 0, 5: 0, 10: 0}
    mrr = 0.0
    for e in entries:
        r = rank_fn(e)
        if r:
            mrr += 1.0 / r
            for k in h:
                if r <= k:
                    h[k] += 1
    return {"n": n, "at1": h[1], "at3": h[3], "at5": h[5], "at10": h[10], "mrr": mrr / max(n, 1)}


def main():
    t0 = time.time()
    rs = load_sandbox()
    ev = load_ev()
    docs = ev.load_documents()
    m = clean_text_map(ev)
    print(f"[ce] n_docs={len(docs)}  ({time.time()-t0:.0f}s)", flush=True)

    # ---- 1. caches top-50 por benchmark ----
    caches = {}
    for tag, path in BENCHES:
        out = os.path.join(NR, f"rerank_cache_{tag}.json")
        if os.path.exists(out):
            caches[tag] = json.load(open(out))
            print(f"[ce] cache {tag}: reusado ({len(caches[tag])} perguntas)", flush=True)
        else:
            caches[tag] = build_cache(rs, ev, docs, path, tag, out)
            print(f"[ce] cache {tag}: construido ({len(caches[tag])} perguntas, {time.time()-t0:.0f}s)", flush=True)

    # valida a replicacao do baseline dentro do cache do v3
    v3 = caches["blind_v3_slices"]
    b1 = sum(1 for e in v3 if e.get("rank_baseline") == 1)
    print(f"[ce] CONTROLE: baseline @1 no cache v3 = {b1}/{len(v3)}  (esperado 183)", flush=True)

    # valida o proxy de ancora contra o campo has_anchor do v3
    rows_v3 = [json.loads(l) for l in open(os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl"), encoding="utf-8") if l.strip()]
    by_q = {r.get("question"): r for r in rows_v3}
    agree = tot = 0
    for e in v3:
        r = by_q.get(e["question"])
        if r is None or r.get("has_anchor") is None:
            continue
        tot += 1
        if bool(ANCHOR_RE.search(e["question"])) == bool(r["has_anchor"]):
            agree += 1
    print(f"[ce] proxy de ancora vs campo has_anchor: {agree}/{tot} concordam"
          f"  ({100*agree/max(tot,1):.1f}%)", flush=True)

    # ---- 2. cross-encoder na GPU ----
    from sentence_transformers import CrossEncoder
    dev = "cuda"
    try:
        import torch
        if not torch.cuda.is_available():
            dev = "cpu"
    except Exception:
        dev = "cpu"
    print(f"[ce] carregando {MODEL} em {dev} ...", flush=True)
    t1 = time.time()
    model = CrossEncoder(MODEL, max_length=512, cache_folder=HF_CACHE, device=dev)
    print(f"[ce] modelo carregado em {time.time()-t1:.1f}s", flush=True)

    results = {}
    for tag, _ in BENCHES:
        entries = caches[tag]
        emb = leak_check(entries, m)
        pairs, meta = [], []
        for e in entries:
            for c in e["cands"][:TOP_N]:
                t = m.get(c["id"], "")
                if t:
                    pairs.append((e["question"], t[:TEXT_CAP]))
                    meta.append((e, c))
        t2 = time.time()
        scores = model.predict(pairs, batch_size=64, show_progress_bar=False)
        dt = time.time() - t2
        by_e = defaultdict(list)
        for (e, c), s in zip(meta, scores):
            by_e[id(e)].append((float(s), c))
        for e in entries:
            sc = by_e.get(id(e), [])
            sc.sort(key=lambda x: (-x[0], str(x[1]["id"])))
            e["_ce_order"] = [c for _, c in sc]

        def ce_rank(e):
            for i, c in enumerate(e["_ce_order"]):
                if rs._match(c, e):
                    return i + 1
            return None

        def base_rank(e):
            return e.get("rank_baseline")

        def hyb_rank(e):
            if ANCHOR_RE.search(e["question"]):
                return e.get("rank_baseline")
            return ce_rank(e)

        results[tag] = {
            "n": len(entries), "vazamento": emb, "pares": len(pairs), "seg": round(dt, 1),
            "throughput": round(len(pairs) / max(dt, 1e-6), 1),
            "baseline": metrics(entries, base_rank),
            "ce_puro": metrics(entries, ce_rank),
            "hibrido": metrics(entries, hyb_rank),
        }
        r = results[tag]
        print(f"\n[{tag}] n={r['n']} pares={r['pares']} {r['throughput']} p/s vazamento={emb}")
        for k in ("baseline", "ce_puro", "hibrido"):
            mm = r[k]
            print(f"   {k:10s} @1 {mm['at1']:4d}/{mm['n']} ({100*mm['at1']/mm['n']:5.1f}%)"
                  f"  @3 {100*mm['at3']/mm['n']:5.1f}%  @10 {100*mm['at10']/mm['n']:5.1f}%  MRR {mm['mrr']:.4f}")

    # ---- 3. por fatia (v3) ----
    print("\n=== v3 POR FATIA ===")
    for sl in ("A_com_ancora", "B_sem_ancora", "D_holdout_temporal"):
        ents = [e for e in caches["blind_v3_slices"] if e.get("slice") == sl]
        if not ents:
            continue
        def mk(fn):
            return metrics(ents, fn)
        def ce_rank2(e):
            for i, c in enumerate(e.get("_ce_order", [])):
                if rs._match(c, e):
                    return i + 1
            return None
        bl = mk(lambda e: e.get("rank_baseline"))
        ce = mk(ce_rank2)
        hy = mk(lambda e: e.get("rank_baseline") if ANCHOR_RE.search(e["question"]) else ce_rank2(e))
        print(f"  {sl:22s} n={len(ents):3d}  baseline {bl['at1']:3d} ({100*bl['at1']/len(ents):5.1f}%)"
              f"  CE {ce['at1']:3d} ({100*ce['at1']/len(ents):5.1f}%)"
              f"  hibrido {hy['at1']:3d} ({100*hy['at1']/len(ents):5.1f}%)")

    out = os.path.join(REPO, "data", "eval", "crossencoder_large_trial.json")
    json.dump({"model": MODEL, "device": dev, "n_docs": len(docs), "top_n": TOP_N,
               "ram_mib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
               "resultados": results}, open(out, "w"), ensure_ascii=False)
    print(f"\n[ce] gravado {out}  ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
