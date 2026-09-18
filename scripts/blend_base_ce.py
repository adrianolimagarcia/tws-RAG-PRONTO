#!/usr/bin/env python3
"""BLEND baseline x cross-encoder - elimina o roteador em vez de melhora-lo.

MOTIVO (medido, runbook 5ab): o CE LARGE ganha +13 na fatia B e perde -28 na A. Uma rota DURA
exige classificar cada pergunta e, com o classificador a 67,2%, o dano de mandar A para o CE
supera o ganho de mandar B -> o hibrido por proxy da' +1 no v3 e -13 nos externos.

O BLEND NAO DECIDE: soma os dois scores normalizados DENTRO do conjunto de candidatos e ordena.
Nao ha classificador, entao nao ha erro de classificacao a amplificar.

RISCO EXPLICITO (o que matou o re-ranker linear de 14.09): as duas escalas nao sao comparaveis
(score cru do BM25 de ordem 5-100 vs logit do CE). Por isso a normalizacao e' min-max DENTRO dos
candidatos de cada pergunta, e o controle e' duro:
   alpha=0  tem de reproduzir o baseline EXATAMENTE (183/262 no v3, 166/180 nos externos)
   alpha=1  tem de reproduzir o CE puro

Read-only. Inferencia apenas, sem treino. Caches e modelo ja' em disco.
"""
import importlib.util, json, os, re, sys, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"
HF_CACHE = os.path.join(NR, "hf_cache")
MODEL = os.environ.get("CE_MODEL", "BAAI/bge-reranker-large")
TOP_N = int(os.environ.get("CE_TOP_N", "20"))
TEXT_CAP = 400
ALPHAS = [round(x / 10, 1) for x in range(11)]

BENCHES = [
    ("blind_v3_slices", "v3"),
    ("holdout_100_unseen", "h100"),
    ("blind_holdout_50_vault", "h50"),
    ("realistic_blind_holdout_30", "r30"),
]


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def minmax(vals):
    if not vals:
        return []
    lo, hi = min(vals), max(vals)
    if hi - lo < 1e-12:
        return [0.5 for _ in vals]
    return [(v - lo) / (hi - lo) for v in vals]


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

    caches = {tag: json.load(open(os.path.join(NR, f"rerank_cache_{tag}.json"))) for tag, _ in BENCHES}

    from sentence_transformers import CrossEncoder
    import torch
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[blend] {MODEL} em {dev} | top_n={TOP_N} | n_docs={len(docs)}", flush=True)
    model = CrossEncoder(MODEL, max_length=512, cache_folder=HF_CACHE, device=dev)

    # ---- 1. pontua o CE e guarda os SCORES crus (nao so' a ordem) ----
    scored = {}
    for tag, _ in BENCHES:
        entries = caches[tag]
        pairs, meta = [], []
        for ei, e in enumerate(entries):
            for ci, c in enumerate(e["cands"][:TOP_N]):
                t = m.get(c["id"], "")
                if t:
                    pairs.append((e["question"], t[:TEXT_CAP]))
                    meta.append((ei, ci))
        t1 = time.time()
        raw = model.predict(pairs, batch_size=64, show_progress_bar=False)
        print(f"[blend] {tag}: {len(pairs)} pares em {time.time()-t1:.0f}s", flush=True)
        per = defaultdict(dict)
        for (ei, ci), s in zip(meta, raw):
            per[ei][ci] = float(s)
        scored[tag] = per

    # ---- 2. varredura de alpha ----
    def evaluate(alpha, tag):
        entries = caches[tag]
        per = scored[tag]
        h1 = 0
        for ei, e in enumerate(entries):
            cands = e["cands"][:TOP_N]
            bs = [c.get("score", 0.0) for c in cands]
            ce_map = per.get(ei, {})
            # candidato sem texto limpo nao foi pontuado -> recebe o MINIMO dos pontuados
            fallback = min(ce_map.values()) if ce_map else 0.0
            cs = [ce_map.get(ci, fallback) for ci in range(len(cands))]
            bn, cn = minmax(bs), minmax(cs)
            blended = [(1.0 - alpha) * bn[i] + alpha * cn[i] for i in range(len(cands))]
            order = sorted(range(len(cands)), key=lambda i: (-blended[i], str(cands[i]["id"])))
            top = cands[order[0]] if order else None
            if top is not None and rs._match(top, e):
                h1 += 1
        return h1

    res = {}
    for alpha in ALPHAS:
        row = {}
        for tag, short in BENCHES:
            row[short] = evaluate(alpha, tag)
        row["ext"] = row["h100"] + row["h50"] + row["r30"]
        res[alpha] = row
        print(f"  alpha={alpha:.1f}  v3 {row['v3']:3d}/262   h100 {row['h100']:3d}  h50 {row['h50']:2d}  "
              f"r30 {row['r30']:2d}   externos {row['ext']:3d}/180   ({time.time()-t0:.0f}s)", flush=True)

    # Referencia: o cache guarda os candidatos PRE-2o-estagio (cands ja' vem ordenado por score),
    # entao alpha=0 reproduz o 1o ESTAGIO, nao a producao. Medir os dois:
    pre = {}
    for tag, short in BENCHES:
        pre[short] = sum(1 for e in caches[tag] if e["cands"] and rs._match(e["cands"][0], e))
    pre["ext"] = pre["h100"] + pre["h50"] + pre["r30"]
    PROD = {"v3": 183, "h100": 89, "h50": 49, "r30": 28, "ext": 166}

    b = res[0.0]
    print(f"\n[blend] CONTROLE alpha=0 = 1o ESTAGIO: v3 {b['v3']}/262  externos {b['ext']}/180"
          f"  -> {'OK' if (b['v3'], b['ext']) == (pre['v3'], pre['ext']) else 'FALHOU'}")
    print(f"[blend] REFERENCIA pre-2a-etapa (medida no cache): v3 {pre['v3']}/262  externos {pre['ext']}/180")
    print(f"[blend] REFERENCIA producao (2a etapa ligada):     v3 {PROD['v3']}/262  externos {PROD['ext']}/180")
    print(f"[blend] CONTROLE alpha=1 = CE puro top-20: v3 {res[1.0]['v3']}/262 (esperado 173)")

    print("\n[blend] criterio: ganho sobre a PRODUCAO no v3 E externos nao-negativos vs producao:")
    best = None
    for alpha in ALPHAS:
        r = res[alpha]
        dv, de = r["v3"] - PROD["v3"], r["ext"] - PROD["ext"]
        mark = "  <== PASSA" if (dv > 0 and de >= 0) else ""
        print(f"  alpha={alpha:.1f}  v3 {r['v3']:3d} ({dv:+3d})   externos {r['ext']:3d} ({de:+3d}){mark}")
        if dv > 0 and de >= 0 and (best is None or dv > best[1]):
            best = (alpha, dv, de)
    if best is None:
        print("  -> NENHUM alpha passa")
    else:
        print(f"  -> melhor: alpha={best[0]:.1f}  (v3 {best[1]:+d}, externos {best[2]:+d})")

    json.dump({str(k): v for k, v in res.items()},
              open(os.path.join(REPO, "data", "eval", "blend_base_ce_sweep.json"), "w"))
    print(f"[blend] {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
