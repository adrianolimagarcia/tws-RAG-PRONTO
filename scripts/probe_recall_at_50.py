#!/usr/bin/env python3
"""Explica POR QUE a fusao nao ajuda: recall@50 de cada ramo, separado, por fatia.

Se o ramo denso tem recall@50 alto e a fusao mesmo assim nao melhora, o gargalo e a
ORDENACAO (o scorer lexical nao premia o doc certo nem com ele no pool).
Se o ramo denso tem recall@50 baixo, o embedding simplesmente nao acha o documento.
"""
import sys, os, json, time
from collections import defaultdict

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

K = 50


def main():
    dev = torch.device("cpu")
    emb = torch.load(os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"),
                     map_location=dev, weights_only=False).float()
    ids = json.load(open(os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json")))
    docs = E.load_documents()
    print(f"[rec] corpus {len(docs)} | indice {tuple(emb.shape)}")

    from transformers import AutoTokenizer, AutoModel
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR,
                                    use_safetensors=True).to(dev).eval()

    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    agg = defaultdict(lambda: {"lex": 0, "den": 0, "uni": 0, "exp": 0, "q": 0})
    t0 = time.time()

    for i, b in enumerate(bench, 1):
        q_text = b["question"]; exp = set(b.get("relevant_claim_ids", [])); sl = b["slice"]
        qt = E.tokenize(q_text)

        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q_text, d["text"], doc=d)
            if s > 0:
                scored.append((s, d))
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        lex50 = {d["id"] for _, d in scored[:K]}

        with torch.no_grad():
            ti = tok([q_text], padding=True, truncation=True, max_length=128, return_tensors="pt").to(dev)
            o = mod(**ti)
            qe = torch.nn.functional.normalize(o.last_hidden_state[:, 0, :], p=2, dim=1).float()
            sc = torch.mm(qe, emb.T).squeeze(0)
            dt = torch.topk(sc, k=K).indices.tolist()
        den50 = {ids[j] for j in dt}

        a = agg[sl]; a["q"] += 1; a["exp"] += len(exp)
        a["lex"] += len(exp & lex50)
        a["den"] += len(exp & den50)
        a["uni"] += len(exp & (lex50 | den50))
        if i % 60 == 0:
            print(f"[rec] {i}/{len(bench)} ({time.time()-t0:.0f}s)", flush=True)

    print(f"\n  {'fatia':<22} {'perg':>5} {'ids':>5} | {'lex@50':>12} {'denso@50':>12} {'uniao@50':>12}")
    print("  " + "-" * 76)
    T = {"lex": 0, "den": 0, "uni": 0, "exp": 0, "q": 0}
    for sl in sorted(agg):
        a = agg[sl]
        for k in T: T[k] += a[k]
        print(f"  {sl:<22} {a['q']:>5} {a['exp']:>5} | "
              f"{a['lex']:>5}/{a['exp']:<3}{100*a['lex']/a['exp']:>5.1f}% "
              f"{a['den']:>5}/{a['exp']:<3}{100*a['den']/a['exp']:>5.1f}% "
              f"{a['uni']:>5}/{a['exp']:<3}{100*a['uni']/a['exp']:>5.1f}%")
    print(f"  {'TOTAL':<22} {T['q']:>5} {T['exp']:>5} | "
          f"{T['lex']:>5}/{T['exp']:<3}{100*T['lex']/T['exp']:>5.1f}% "
          f"{T['den']:>5}/{T['exp']:<3}{100*T['den']/T['exp']:>5.1f}% "
          f"{T['uni']:>5}/{T['exp']:<3}{100*T['uni']/T['exp']:>5.1f}%")


if __name__ == "__main__":
    main()
