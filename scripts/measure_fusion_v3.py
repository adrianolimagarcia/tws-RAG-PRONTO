#!/usr/bin/env python3
"""Mede se o ramo DENSO ajuda, nas fatias reais do blind v3 (262 perguntas).

Por que existe: o RRF do repo (`evaluate_pure_virgin_hybrid_cpu.py`) so foi medido no
benchmark mais fraco da casa (40 perguntas, Hit@1 100%, com 10/40 trazendo o codigo na
propria pergunta). E os 4 trials semanticos anteriores foram medidos contra baselines
DIFERENTES do harness — o que produziu "+9" ilusorio no Jina.

CONTROLE EMBUTIDO: o baseline aqui e o pipeline LEXICAL EXATO do harness
(`compute_bm25` -> diversificacao de fonte -> `second_stage_rerank`), replicado verbatim.
Ele TEM de reproduzir `@1 183/262 (A 97/107 B 80/140 D 6/15)`. Se nao reproduzir, a
medicao e invalida e o script aborta.

VARIANTES:
  baseline : pipeline lexical do harness (o que existe hoje)
  cobertura: candidatos = lexical_topN U denso_topN, ORDENADOS pelo lexical.
             O denso so traz candidato que nao entraria — nao reordena nada.
  rrf      : fusao por rank (1/(60+r)) sobre as duas listas, ordenacao final pelo RRF.
             Aqui o denso PARTICIPA da ordem.

USO:
    python scripts/measure_fusion_v3.py --index data/indexes/corpus_bge_m3_v2.pt \
        --meta data/indexes/corpus_docs_meta_v2.json
"""
import sys, os, json, argparse, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))

import evaluate_rag_benchmark as E  # noqa: E402

BENCH = os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")
RRF_K = 60
TOPN = 50


def lexical_rank(q_text, q_tokens, docs):
    """Pipeline lexical do harness, replicado verbatim (ver evaluate_rag_benchmark.run_evaluation)."""
    scored = []
    for doc in docs:
        s = E.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
        if s > 0:
            scored.append([s, doc])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

    diversified = []
    seen = defaultdict(int)
    for s, doc in scored:
        key = doc.get("runbook") or doc.get("type")
        if doc.get("type") == "ragflow_runbook_chunk" and seen[key] >= 2:
            s *= 0.65
        seen[key] += 1
        diversified.append((s, doc))
    diversified.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return diversified


def is_match(d, expected_cids, expected_runbook, q_tokens):
    """Funcao de match do harness, replicada verbatim."""
    if d["id"] in expected_cids:
        return True
    if d["type"] == "aws_message":
        for ecid in expected_cids:
            if d.get("code", "").lower() in ecid.lower():
                return True
        return False
    if d["type"] in ("ragflow_runbook_chunk", "runbook_section") and expected_runbook \
            and d.get("runbook") == expected_runbook:
        ov = len(q_tokens.intersection(d["tokens"]))
        if ov >= 2 and (ov / max(1, len(q_tokens))) >= 0.25:
            return True
    return False


def score_ranking(ranked_docs, expected_cids, expected_runbook, q_tokens):
    for i, d in enumerate(ranked_docs):
        if is_match(d, expected_cids, expected_runbook, q_tokens):
            return i + 1
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default=os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"))
    ap.add_argument("--meta", default=os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json"))
    ap.add_argument("--topn", type=int, default=TOPN)
    ap.add_argument("--dense-k", type=int, default=TOPN)
    ap.add_argument("--final", type=int, default=20)
    ap.add_argument("--device", default="cpu")
    args = ap.parse_args()

    dev = torch.device(args.device)
    print(f"[fus] indice: {args.index}")
    emb = torch.load(args.index, map_location=dev, weights_only=False).float()
    ids = json.load(open(args.meta))
    print(f"[fus] matriz: {tuple(emb.shape)}  ids: {len(ids)}")

    docs = E.load_documents()
    docs_by_id = {d["id"]: d for d in docs}
    print(f"[fus] corpus: {len(docs)}")

    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).to(dev).eval()
    print(f"[fus] bge-m3 carregado em {args.device}")

    bench = [json.loads(l) for l in open(BENCH) if l.strip()]
    print(f"[fus] perguntas: {len(bench)}\n")

    res = {v: defaultdict(lambda: {"h1": 0, "h3": 0, "h5": 0, "h10": 0, "rr": [], "n": 0})
           for v in ("baseline", "cobertura", "rrf")}

    t0 = time.time()
    for i, b in enumerate(bench, 1):
        q_text = b.get("question", "")
        exp = set(b.get("relevant_claim_ids", []))
        exp_rb = b.get("runbook_ref")
        qt = E.tokenize(q_text)
        sl = b["slice"]

        # --- ramo lexical (identico ao harness) ---
        div = lexical_rank(q_text, qt, docs)
        lex_docs = [d for _, d in div]
        lex_ids = [d["id"] for d in lex_docs]
        base_top = E.second_stage_rerank(q_text, div[:200], top_n=args.final)

        # --- ramo denso ---
        with torch.no_grad():
            ti = tok([q_text], padding=True, truncation=True, max_length=128,
                     return_tensors="pt").to(dev)
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
            sc = torch.mm(qe, emb.T).squeeze(0)
            dtop = torch.topk(sc, k=min(args.dense_k, sc.shape[0])).indices.tolist()
        dense_ids = [ids[j] for j in dtop]

        # --- cobertura: uniao de candidatos, ordenacao LEXICAL ---
        cand_ids = []
        seen = set()
        for cid in lex_ids[: args.topn] + dense_ids:
            if cid not in seen and cid in docs_by_id:
                seen.add(cid); cand_ids.append(cid)
        cand = []
        for cid in cand_ids:
            d = docs_by_id[cid]
            s = E.compute_bm25(qt, d["tokens"], q_text, d["text"], doc=d)
            cand.append([s, d])
        cand.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        div2 = []
        seen2 = defaultdict(int)
        for s, d in cand:
            k = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen2[k] >= 2:
                s *= 0.65
            seen2[k] += 1
            div2.append((s, d))
        div2.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        cob_top = E.second_stage_rerank(q_text, div2, top_n=args.final)

        # --- rrf: fusao por rank, ordenacao final pelo RRF ---
        rrf = defaultdict(float)
        for r, cid in enumerate(lex_ids[: args.topn]):
            rrf[cid] += 1.0 / (RRF_K + r + 1)
        for r, cid in enumerate(dense_ids):
            rrf[cid] += 1.0 / (RRF_K + r + 1)
        fused = sorted(rrf.items(), key=lambda x: (-x[1], str(x[0])))[: args.final]
        rrf_top = [docs_by_id[c] for c, _ in fused if c in docs_by_id]

        for v, ranked in (("baseline", base_top), ("cobertura", cob_top), ("rrf", rrf_top)):
            r = score_ranking(ranked, exp, exp_rb, qt)
            s = res[v][sl]; s["n"] += 1
            if r is not None:
                s["rr"].append(1.0 / r)
                if r <= 1: s["h1"] += 1
                if r <= 3: s["h3"] += 1
                if r <= 5: s["h5"] += 1
                if r <= 10: s["h10"] += 1
            else:
                s["rr"].append(0.0)
        if i % 40 == 0:
            print(f"[fus] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    # --- relatorio ---
    def agg(v):
        h1 = h3 = h5 = h10 = n = 0; rr = 0.0
        for sl, s in res[v].items():
            h1 += s["h1"]; h3 += s["h3"]; h5 += s["h5"]; h10 += s["h10"]; n += s["n"]
            rr += sum(s["rr"])
        return h1, h3, h5, h10, n, (rr / n if n else 0.0)

    print("\n" + "=" * 76)
    print(f"  {'variante':<12} {'@1':>7} {'@3':>7} {'@5':>7} {'@10':>7} {'MRR':>8}")
    print("  " + "-" * 72)
    for v in ("baseline", "cobertura", "rrf"):
        h1, h3, h5, h10, n, mrr = agg(v)
        print(f"  {v:<12} {h1:>3}/{n:<3} {h3:>3}/{n:<3} {h5:>3}/{n:<3} {h10:>3}/{n:<3} {mrr:>8.4f}")

    print("\n  POR FATIA (@1):")
    slices = sorted({r["slice"] for r in bench})
    print(f"  {'fatia':<22} " + " ".join(f"{v:>14}" for v in ("baseline", "cobertura", "rrf")))
    for sl in slices:
        cells = []
        for v in ("baseline", "cobertura", "rrf"):
            s = res[v][sl]
            cells.append(f"{s['h1']:>3}/{s['n']:<3} {100.0*s['h1']/max(1,s['n']):>5.1f}%")
        print(f"  {sl:<22} " + " ".join(f"{c:>14}" for c in cells))

    # --- controle obrigatorio ---
    h1b, _, _, _, nb, _ = agg("baseline")
    print("\n" + "=" * 76)
    if h1b == 183 and nb == 262:
        print(f"[fus] CONTROLE OK: baseline @1 {h1b}/{nb} == 183/262 documentado.")
    else:
        print(f"[fus] CONTROLE FALHOU: baseline @1 {h1b}/{nb}, esperado 183/262 —")
        print("[fus] a medicao NAO e valida (o baseline nao reproduz o harness).")
    print("=" * 76)


if __name__ == "__main__":
    main()
