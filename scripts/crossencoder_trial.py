#!/usr/bin/env python3
"""TRIAL LIMITADO: cross-encoder multilíngue sobre o top-50 do cache do sandbox.
NAO altera o avaliador nem o baseline. Usa venv isolado (/tmp/ha_fm/rerank-venv).
Tune em A, validacao em B/D. Uso: <venv>/bin/python scripts/crossencoder_trial.py [--limit N] [--out path]
Metricas: Hit@1/@3/@5/@10, MRR, throughput (pairs/s), tempo total, modelo, pico de RAM.
Entrada de texto limpa (claim cru, sem synthetic_questions) para nao vazar a pergunta.
"""
import importlib.util, json, os, resource, sys, time
from collections import defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE = os.environ.get("RERANK_CACHE", "/tmp/ha_fm/rerank_cache.json")
MODEL = os.environ.get("CE_MODEL", "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")
TOP_N = int(os.environ.get("CE_TOP_N", "50"))
TEXT_CAP = 400


def load_sandbox():
    spec = importlib.util.spec_from_file_location("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    if spec is None or spec.loader is None:
        raise RuntimeError("sem sandbox")
    rs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs)
    return rs


def clean_text_map():
    corp = {}
    for ln in open(os.path.join(REPO, "data", "export", "tws_corpus_master_consolidated.jsonl"), encoding="utf-8"):
        ln = ln.strip()
        if ln:
            d = json.loads(ln)
            corp[d["claim_id"]] = d.get("claim", "")
    # docs do avaliador (para chunks/msgcat/aws/optman, que nao estao no export)
    evspec = importlib.util.spec_from_file_location("ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    if evspec is None or evspec.loader is None:
        raise RuntimeError("sem avaliador")
    ev = importlib.util.module_from_spec(evspec)
    evspec.loader.exec_module(ev)
    m = dict(corp)
    for d in ev.load_documents():
        if d["id"] not in m:
            m[d["id"]] = d["text"]
    return m


def toks(s):
    import re, unicodedata
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", s)


def leak_check(cache, m):
    """A pergunta casa com o texto limpo de algum doc? (0 = sem vazamento)."""
    idx = {cid: set(toks(t)) for cid, t in m.items() if t}
    emb = 0
    for e in cache:
        qt = set(toks(e["question"]))
        if not qt:
            continue
        for s in idx.values():
            if not s:
                continue
            if min(len(qt & s) / len(qt), len(qt & s) / len(s)) >= 0.7:
                emb += 1
                break
    return emb


def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    out_path = None
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    only_slices = None
    if "--slices" in sys.argv:
        only_slices = sys.argv[sys.argv.index("--slices") + 1].split(",")

    rs = load_sandbox()
    m = clean_text_map()
    cache = json.load(open(CACHE))
    if only_slices:
        cache = [e for e in cache if e["slice"] in only_slices]
    if limit:
        cache = cache[:limit]
    emb = leak_check(cache, m)
    print(f"modelo={MODEL} | perguntas={len(cache)} | top_n={TOP_N} | vazamento(>=0.7)={emb}/{len(cache)}")

    from sentence_transformers import CrossEncoder
    model = CrossEncoder(MODEL, max_length=512)

    # monta pares (pergunta, texto_limpo)
    pairs = []
    for e in cache:
        for c in e["cands"][:TOP_N]:
            t = m.get(c["id"], "")
            if t:
                pairs.append((e, c, t[:TEXT_CAP]))
    t0 = time.time()
    scores = model.predict([(e["question"], t) for e, c, t in pairs],
                           batch_size=64, show_progress_bar=False)
    dt = time.time() - t0
    # agrupa por pergunta
    by_entry = defaultdict(list)
    for (e, c, _), s in zip(pairs, scores):
        by_entry[id(e)].append((s, c))
    # rank
    by_slice = defaultdict(list)
    for e in cache:
        sc = by_entry[id(e)]
        sc.sort(key=lambda x: (-float(x[0]), str(x[1]["id"])))
        order = [c for _, c in sc]
        rank = None
        for i, c in enumerate(order):
            if rs._match(c, e):
                rank = i + 1
                break
        by_slice[e["slice"]].append((e, rank))
    # metricas
    lines = [f"throughput: {len(pairs):d} pares em {dt:.1f}s = {len(pairs)/max(dt,1e-6):.1f} pares/s"]
    lines.append(f"pico RAM (maxrss): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.0f} MiB")
    hdr = f"{'fatia':22s} n @1   @3   @5   @10   MRR"
    print("=== RESULTADO CROSS-ENCODER (top-50) ===")
    print(hdr)
    for sl in ("A_com_ancora", "B_sem_ancora", "D_holdout_temporal"):
        ents = by_slice.get(sl, [])
        n = len(ents)
        h = {1: 0, 3: 0, 5: 0, 10: 0}
        mrr = 0.0
        for _, r in ents:
            if r:
                mrr += 1.0 / r
                for k in h:
                    if r <= k:
                        h[k] += 1
        lines.append(f"{sl:22s} {n:3d} {100*h[1]/max(n,1):5.1f} {100*h[3]/max(n,1):5.1f} "
                     f"{100*h[5]/max(n,1):5.1f} {100*h[10]/max(n,1):5.1f} {mrr/max(n,1):.4f}")
        print(lines[-1])
    # guarda
    if out_path:
        json.dump(lines, open(out_path, "w"), ensure_ascii=False)
        print(f"salvo -> {out_path}")


if __name__ == "__main__":
    main()
