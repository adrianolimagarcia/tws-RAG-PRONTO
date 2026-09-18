#!/usr/bin/env python3
"""BLEND (corrigido): CE SOMADO ao 2o estagio, nao no lugar dele.

DEFEITO DO TESTE ANTERIOR (scripts/blend_base_ce.py): ele blendeou o CE com o score
PRE-2o-estagio, ou seja, SUBSTITUIU o 2o estagio. Medido: alpha=0 reproduziu 169/262 e
141/180 (o 1o estagio), nao a producao (183/166). Como o 2o estagio vale +14 no v3 e +25
nos externos, o teste comecava 25 pontos atras e nenhum alpha podia recuperar. O teste
anterior nao mediu 'blend', mediu 'CE no lugar do 2o estagio' - e isso ja' era sabido ruim.

DESENHO CORRETO: manter o 2o estagio e ADICIONAR o sinal do CE como termo extra.
  final = (1 - lam) * minmax(score_2a_etapa) + lam * minmax(score_CE)
CONTROLE DURO: lam=0 tem de reproduzir a PRODUCAO EXATAMENTE (183/262, 166/180).

Tambem salva os scores crus do CE em disco, para nao precisar re-inferir em rodadas futuras.

Read-only. Inferencia apenas, sem treino.
"""
import importlib.util, json, os, sys, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"
HF_CACHE = os.path.join(NR, "hf_cache")
CE_SCORES = os.path.join(NR, "ce_scores_top20.json")
MODEL = os.environ.get("CE_MODEL", "BAAI/bge-reranker-large")
TOP_N = int(os.environ.get("CE_TOP_N", "20"))
TEXT_CAP = 400
LAMBDAS = [round(x / 10, 1) for x in range(11)]
BENCHES = [
    ("blind_v3_slices", "v3", os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")),
    ("holdout_100_unseen", "h100", os.path.join(REPO, "data", "eval", "holdout_100_unseen.jsonl")),
    ("blind_holdout_50_vault", "h50", os.path.join(REPO, "data", "eval", "blind_holdout_50_vault.jsonl")),
    ("realistic_blind_holdout_30", "r30", os.path.join(REPO, "data", "eval", "realistic_blind_holdout_30.jsonl")),
]
PROD = {"v3": 183, "h100": 89, "h50": 49, "r30": 28, "ext": 166}


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def minmax(v):
    if not v:
        return []
    lo, hi = min(v), max(v)
    return [0.5] * len(v) if hi - lo < 1e-12 else [(x - lo) / (hi - lo) for x in v]


def main():
    t0 = time.time()
    rs = load_mod("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    ev = load_mod("ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    atrib = load_mod("atrib", os.path.join(REPO, "scripts", "attribute_ordering_flips.py"))
    docs = ev.load_documents()
    print(f"[b2] n_docs={len(docs)}", flush=True)

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

    # ---- 1. reconstroi o pipeline real e o score da 2a etapa por candidato ----
    built = {}
    for tag, short, path in BENCHES:
        rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
        ents = []
        for b in rows:
            q = b.get("question", "")
            qt = ev.tokenize(q)
            sc = []
            for d in docs:
                s = ev.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
                if s > 0:
                    sc.append([s, d])
            sc.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
            dv = []
            seen = defaultdict(int)
            for s, d in sc:
                k = d.get("runbook") or d.get("type")
                if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
                    s *= 0.65
                seen[k] += 1
                dv.append((s, d))
            dv.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
            top = []
            for s, d in dv[:TOP_N]:
                s2, _ = atrib.ss_parts(q, s, d)
                top.append({"id": d["id"], "doc": d, "s1": s, "s2": s2})
            ents.append({"q": q, "expected": set(b.get("relevant_claim_ids", [])),
                         "runbook": b.get("runbook_ref"), "q_tokens": qt, "cands": top})
        built[tag] = ents
        print(f"[b2] {tag}: pipeline reconstruido ({len(ents)} perguntas, {time.time()-t0:.0f}s)", flush=True)

    # ---- 2. CE sobre o top-20 (ou reusa os scores salvos) ----
    if os.path.exists(CE_SCORES):
        ce = json.load(open(CE_SCORES))
        print("[b2] scores do CE reusados de disco", flush=True)
    else:
        from sentence_transformers import CrossEncoder
        import torch
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        model = CrossEncoder(MODEL, max_length=512, cache_folder=HF_CACHE, device=dev)
        ce = {}
        for tag, short, _ in BENCHES:
            ents = built[tag]
            pairs, meta = [], []
            for ei, e in enumerate(ents):
                for ci, c in enumerate(e["cands"]):
                    t = m.get(c["id"], "")
                    if t:
                        pairs.append((e["q"], t[:TEXT_CAP]))
                        meta.append((ei, ci))
            t1 = time.time()
            raw = model.predict(pairs, batch_size=64, show_progress_bar=False)
            per = defaultdict(dict)
            for (ei, ci), s in zip(meta, raw):
                per[ei][ci] = float(s)
            ce[tag] = {str(k): v for k, v in per.items()}
            print(f"[b2] {tag}: {len(pairs)} pares em {time.time()-t1:.0f}s", flush=True)
        json.dump(ce, open(CE_SCORES, "w"))
        print(f"[b2] scores do CE salvos em {CE_SCORES}", flush=True)

    # ---- 3. varredura de lambda ----
    def at1(tag, lam):
        h = 0
        for ei, e in enumerate(built[tag]):
            cands = e["cands"]
            s2 = [c["s2"] for c in cands]
            per = {int(k): v for k, v in ce[tag].get(str(ei), {}).items()}
            fb = min(per.values()) if per else 0.0
            csc = [per.get(ci, fb) for ci in range(len(cands))]
            n2, nc = minmax(s2), minmax(csc)
            bl = [(1 - lam) * n2[i] + lam * nc[i] for i in range(len(cands))]
            order = sorted(range(len(cands)), key=lambda i: (-bl[i], str(cands[i]["id"])))
            if order:
                c = cands[order[0]]
                ent = {"expected": e["expected"], "runbook": e["runbook"], "q_tokens": e["q_tokens"]}
                cand = {"id": c["id"], "type": c["doc"].get("type"), "ov": len(set(e["q_tokens"]) & c["doc"]["tokens"])}
                if rs._match(cand, ent):
                    h += 1
        return h

    res = {}
    for lam in LAMBDAS:
        row = {short: at1(tag, lam) for tag, short, _ in BENCHES}
        row["ext"] = row["h100"] + row["h50"] + row["r30"]
        res[lam] = row
        print(f"  lam={lam:.1f}  v3 {row['v3']:3d}/262   externos {row['ext']:3d}/180   ({time.time()-t0:.0f}s)", flush=True)

    b = res[0.0]
    print(f"\n[b2] CONTROLE lam=0 == PRODUCAO: v3 {b['v3']}/262 (esperado 183), externos {b['ext']}/180 (esperado 166)"
          f"  -> {'OK' if (b['v3'], b['ext']) == (183, 166) else 'FALHOU'}")
    print("\n[b2] ganho sobre a PRODUCAO:")
    best = None
    for lam in LAMBDAS:
        r = res[lam]
        dv, de = r["v3"] - PROD["v3"], r["ext"] - PROD["ext"]
        mark = "  <== PASSA" if (dv > 0 and de >= 0) else ""
        print(f"  lam={lam:.1f}  v3 {r['v3']:3d} ({dv:+3d})   externos {r['ext']:3d} ({de:+3d}){mark}")
        if dv > 0 and de >= 0 and (best is None or dv > best[1]):
            best = (lam, dv, de)
    print(f"  -> {'melhor: lam=%.1f (v3 %+d, externos %+d)' % best if best else 'NENHUM lambda passa'}")
    json.dump({str(k): v for k, v in res.items()},
              open(os.path.join(REPO, "data", "eval", "blend_on_top_of_stage2_sweep.json"), "w"))
    print(f"[b2] {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
