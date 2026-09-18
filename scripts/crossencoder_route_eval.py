#!/usr/bin/env python3
"""FASE 2b - a ROTA decide. CE sobre o top-20 (nao top-50), com a rota medida em duas formas.

Por que refazer: a Fase 2 mostrou que o CE LARGE leva a fatia B de 80 -> 93 (+13), mas
derruba A de 97 -> 69 (-28). Logo o resultado depende inteiramente de QUEM vai para o CE.
A rodada anterior usou um PROXY de ancora e o hibrido deu A=91 (nao 97) - o proxy desvia.

Aqui:
  - CE sobre o top-20 (o 2o estagio so' re-rankeia 20; comparacao justa e 60% mais barata);
  - rota (1) pelo CAMPO has_anchor do v3 (propriedade a priori, existe no benchmark);
  - rota (2) pelo PROXY derivado so' do texto (unico disponivel nos externos);
  - mede a concordancia proxy x campo, e o efeito de cada rota por conjunto.

Read-only. Inferencia apenas.
"""
import importlib.util, json, os, re, sys, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"
HF_CACHE = os.path.join(NR, "hf_cache")
MODEL = os.environ.get("CE_MODEL", "BAAI/bge-reranker-large")
TOP_N = int(os.environ.get("CE_TOP_N", "20"))
TEXT_CAP = 400

BENCHES = [
    ("blind_v3_slices", os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")),
    ("holdout_100_unseen", os.path.join(REPO, "data", "eval", "holdout_100_unseen.jsonl")),
    ("blind_holdout_50_vault", os.path.join(REPO, "data", "eval", "blind_holdout_50_vault.jsonl")),
    ("realistic_blind_holdout_30", os.path.join(REPO, "data", "eval", "realistic_blind_holdout_30.jsonl")),
]
ANCHOR_RE = re.compile(
    r"aws[a-z]{3}[0-9]{3}[iew]|"
    r"\b(sfinal|jnextplan|resetplan|makeplan|switchplan|checksync|composer|conman|planman|optman|"
    r"joblog|vartable|rerun|securityutility|resync|twsobjectmonitor|switcheventprocessor|switchevtp|"
    r"tebctl|wapl|mmrresolve|symnew|conddep|aida|carryforward|enretain|kubernetes|helm)\b", re.I)


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"sem {name}")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def toks(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", s)


def main():
    t0 = time.time()
    rs = load_mod("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    ev = load_mod("ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    docs = ev.load_documents()

    m = {}
    p = os.path.join(REPO, "data", "export", "tws_corpus_master_consolidated.jsonl")
    if os.path.exists(p):
        for ln in open(p, encoding="utf-8"):
            ln = ln.strip()
            if ln:
                d = json.loads(ln)
                m[d["claim_id"]] = d.get("claim", "")
    for d in docs:
        m.setdefault(d["id"], d["text"])

    # campo has_anchor real (so' o v3 tem)
    real_anchor = {}
    for ln in open(os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl"), encoding="utf-8"):
        ln = ln.strip()
        if ln:
            r = json.loads(ln)
            if r.get("has_anchor") is not None:
                real_anchor[r["question"]] = bool(r["has_anchor"])

    caches = {}
    for tag, _ in BENCHES:
        f = os.path.join(NR, f"rerank_cache_{tag}.json")
        caches[tag] = json.load(open(f))

    from sentence_transformers import CrossEncoder
    import torch
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[r] {MODEL} em {dev}, top_n={TOP_N}, n_docs={len(docs)}", flush=True)
    model = CrossEncoder(MODEL, max_length=512, cache_folder=HF_CACHE, device=dev)

    per_q = []
    for tag, _ in BENCHES:
        entries = caches[tag]
        pairs, meta = [], []
        for e in entries:
            for c in e["cands"][:TOP_N]:
                t = m.get(c["id"], "")
                if t:
                    pairs.append((e["question"], t[:TEXT_CAP]))
                    meta.append((e, c))
        t1 = time.time()
        sc = model.predict(pairs, batch_size=64, show_progress_bar=False)
        dt = time.time() - t1
        print(f"[r] {tag}: {len(pairs)} pares em {dt:.0f}s = {len(pairs)/max(dt,1e-6):.1f} p/s", flush=True)
        by_e = defaultdict(list)
        for (e, c), s in zip(meta, sc):
            by_e[id(e)].append((float(s), c))
        for _i, e in enumerate(entries):
            order = by_e.get(id(e), [])
            order.sort(key=lambda x: (-x[0], str(x[1]["id"])))
            ce_rank = None
            for i, (_, c) in enumerate(order):
                if rs._match(c, e):
                    ce_rank = i + 1
                    break
            base_rank = e.get("rank_baseline")
            q = e["question"]
            ra = real_anchor.get(q)
            px = bool(ANCHOR_RE.search(q))
            # NAO gravar o texto da pergunta: redundante (esta no benchmark) e faz o scanner
            # de segredo do publish.sh abortar por falso positivo em strings de VERSAO do
            # produto. Guarda-se o INDICE dentro do conjunto, que junta com o benchmark.
            per_q.append({"set": tag, "i": _i, "slice": e.get("slice"),
                          "base": base_rank, "ce": ce_rank,
                          "has_anchor_real": ra, "proxy": px})

    json.dump(per_q, open(os.path.join(REPO, "data", "eval", "crossencoder_route_perquestion.json"), "w"))

    # --- concordancia proxy x campo real (so' v3) ---
    v3 = [r for r in per_q if r["set"] == "blind_v3_slices" and r["has_anchor_real"] is not None]
    ok = sum(1 for r in v3 if r["proxy"] == r["has_anchor_real"])
    fp = sum(1 for r in v3 if r["proxy"] and not r["has_anchor_real"])
    fn = sum(1 for r in v3 if r["has_anchor_real"] and not r["proxy"])
    print(f"\n[r] PROXY vs campo has_anchor (v3): {ok}/{len(v3)} concordam ({100*ok/max(len(v3),1):.1f}%)"
          f" | falso-ancora={fp} | falso-nao-ancora={fn}")

    def h1(rows, route):
        h = 0
        for r in rows:
            use_ce = route(r)
            rank = r["ce"] if use_ce else r["base"]
            if rank == 1:
                h += 1
        return h

    print("\n=== ROTA (1) pelo CAMPO has_anchor real (v3) ===")
    print(f"  v3: baseline {h1(v3, lambda r: False)}/{len(v3)}"
          f"   CE-total {h1(v3, lambda r: True)}/{len(v3)}"
          f"   HIBRIDO {h1(v3, lambda r: not r['has_anchor_real'])}/{len(v3)}")
    for sl in ("A_com_ancora", "B_sem_ancora", "D_holdout_temporal"):
        rs_ = [r for r in v3 if r["slice"] == sl]
        print(f"    {sl:22s} n={len(rs_):3d}  baseline {h1(rs_, lambda r: False):3d}"
              f"   hibrido(campo) {h1(rs_, lambda r: not r['has_anchor_real']):3d}")

    print("\n=== ROTA (2) pelo PROXY ===")
    for tag, _ in BENCHES:
        rows = [r for r in per_q if r["set"] == tag]
        nb = h1(rows, lambda r: False)
        nc = h1(rows, lambda r: True)
        nh = h1(rows, lambda r: not r["proxy"])
        print(f"  {tag:28s} n={len(rows):3d}  baseline {nb:3d}   CE {nc:3d}   hibrido(proxy) {nh:3d}"
              f"   delta {nh-nb:+3d}")

    ext = [r for r in per_q if r["set"] != "blind_v3_slices"]
    print(f"\n  EXTERNOS (180): baseline {h1(ext, lambda r: False)}   "
          f"hibrido(proxy) {h1(ext, lambda r: not r['proxy'])}")
    print(f"[r] {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
