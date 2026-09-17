#!/usr/bin/env python3
"""Reconstroi o indice denso do corpus ATUAL com BAAI/bge-m3 (dense, CLS normalizado).

Por que existe: o indice em `data/indexes/corpus_bge_m3.pt` e de 2026-09-09 e tem 2427
entradas, enquanto o corpus de hoje tem ~6969 docs. A cobertura medida era A 105/139,
B 149/188 e D 0/16 (100% fora) — ou seja, medir fusao lexical x densa com ele devolvia
nulo ARTEFATUAL, nao do metodo.

RECEITA (replicada EXATAMENTE do `build_dense_index.py` original, para os scores serem
comparaveis com o caminho de query em `evaluate_pure_virgin_hybrid_cpu.py`):
    texto : d["text"][:500], "\n" -> " ", strip
    tok   : padding=True, truncation=True, max_length=128
    vetor : last_hidden_state[:, 0, :]  (CLS) + normalize L2
    dtype : float16 na GPU
    batch : 64

SAIDA: escreve em arquivos NOVOS (_v2) por padrao. Nao sobrescreve o indice em uso.
"""
import sys, os, time, json, argparse

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
os.environ.setdefault("HF_HOME", CACHE_DIR)

sys.path.insert(0, os.path.join(REPO, "data", "eval"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-index", default=os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"))
    ap.add_argument("--out-meta", default=os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json"))
    ap.add_argument("--batch-size", type=int, default=64)
    ap.add_argument("--max-chars", type=int, default=500)
    ap.add_argument("--max-length", type=int, default=128)
    args = ap.parse_args()

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"[idx] dispositivo: {device}")
    if device.startswith("cuda"):
        print(f"[idx] gpu: {torch.cuda.get_device_name(0)}")

    t0 = time.time()
    from transformers import AutoModel, AutoTokenizer
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=CACHE_DIR)
    model = AutoModel.from_pretrained(
        "BAAI/bge-m3", cache_dir=CACHE_DIR,
        torch_dtype=torch.float16, use_safetensors=True,
    ).to(device)
    model.eval()
    print(f"[idx] modelo carregado em {time.time()-t0:.1f}s")

    import evaluate_rag_benchmark as lex_engine
    corpus = lex_engine.load_documents()
    print(f"[idx] corpus: {len(corpus)} docs")

    doc_ids, doc_texts = [], []
    for d in corpus:
        doc_ids.append(d["id"])
        doc_texts.append(d["text"][: args.max_chars].replace("\n", " ").strip())

    dups = len(doc_ids) - len(set(doc_ids))
    print(f"[idx] ids unicos: {len(set(doc_ids))} (duplicados: {dups})")

    t1 = time.time()
    chunks = []
    with torch.no_grad():
        for i in range(0, len(doc_texts), args.batch_size):
            batch = doc_texts[i : i + args.batch_size]
            inputs = tok(batch, padding=True, truncation=True,
                         max_length=args.max_length, return_tensors="pt").to(device)
            out = model(**inputs)
            cls = out.last_hidden_state[:, 0, :]
            chunks.append(torch.nn.functional.normalize(cls, p=2, dim=1).cpu())
            done = min(i + args.batch_size, len(doc_texts))
            if (i // args.batch_size) % 10 == 0 or done == len(doc_texts):
                el = time.time() - t1
                print(f"[idx] {done}/{len(doc_texts)}  ({el:.1f}s, {done/max(el,1e-9):.1f} doc/s)", flush=True)

    emb = torch.cat(chunks, dim=0)
    print(f"[idx] matriz: {tuple(emb.shape)} dtype={emb.dtype} "
          f"({emb.element_size()*emb.nelement()/(1024**2):.2f} MB) em {time.time()-t1:.1f}s")

    os.makedirs(os.path.dirname(args.out_index), exist_ok=True)
    torch.save(emb.cpu(), args.out_index)
    with open(args.out_meta, "w") as f:
        json.dump(doc_ids, f)
    print(f"[idx] gravado: {args.out_index}")
    print(f"[idx] gravado: {args.out_meta}")
    print(f"[idx] TOTAL {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
