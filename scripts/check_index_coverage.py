#!/usr/bin/env python3
"""Mede a COBERTURA de um indice denso contra os ids esperados das fatias do blind v3.

Cobertura = fracao dos `relevant_claim_ids` das perguntas que EXISTEM no indice.
Se um id esperado nao esta no indice, o ramo denso simplesmente nao pode recupera-lo —
e qualquer medicao de fusao (lexical U denso) devolve um nulo ARTEFATUAL do indice,
nao do metodo. Foi exatamente o que aconteceu com o indice de 2026-09-09 (D: 0/16).

Uso:
    python scripts/check_index_coverage.py --index <arquivo.pt> --meta <meta.json>
"""
import os, json, argparse

import torch

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
SLICES = os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default=os.path.join(REPO, "data/indexes/corpus_bge_m3_v2.pt"))
    ap.add_argument("--meta", default=os.path.join(REPO, "data/indexes/corpus_docs_meta_v2.json"))
    args = ap.parse_args()

    emb = torch.load(args.index, map_location="cpu", weights_only=False)
    ids = json.load(open(args.meta))
    print(f"[cov] indice : {args.index}")
    print(f"[cov] matriz : {tuple(emb.shape)} dtype={emb.dtype}")
    print(f"[cov] ids    : {len(ids)} (unicos {len(set(ids))})")
    idx_ids = set(ids)

    rows = [json.loads(l) for l in open(SLICES) if l.strip()]
    print(f"[cov] perguntas: {len(rows)}")
    print()
    print(f"  {'fatia':<22} {'perg':>5} {'ids_esp':>8} {'no_indice':>10} {'FORA':>6} {'cobertura':>10}")
    print(f"  {'-'*22} {'-'*5} {'-'*8} {'-'*10} {'-'*6} {'-'*10}")

    tot_exp = tot_in = 0
    for sl in sorted({r["slice"] for r in rows}):
        sub = [r for r in rows if r["slice"] == sl]
        exp = set()
        for r in sub:
            exp |= set(r.get("relevant_claim_ids", []))
        inside = exp & idx_ids
        fora = exp - idx_ids
        pct = (100.0 * len(inside) / len(exp)) if exp else 0.0
        tot_exp += len(exp); tot_in += len(inside)
        print(f"  {sl:<22} {len(sub):>5} {len(exp):>8} {len(inside):>10} {len(fora):>6} {pct:>9.1f}%")
    pct = (100.0 * tot_in / tot_exp) if tot_exp else 0.0
    print(f"  {'TOTAL':<22} {len(rows):>5} {tot_exp:>8} {tot_in:>10} {tot_exp-tot_in:>6} {pct:>9.1f}%")

    # Veredito de utilidade
    print()
    if tot_exp and tot_in / tot_exp >= 0.99:
        print("[cov] VEREDITO: indice COMPLETO para estas fatias — fusao pode ser medida.")
    else:
        print(f"[cov] VEREDITO: indice INCOMPLETO ({tot_exp-tot_in} ids fora) — "
              f"fusao mediria artefato nas fatias afetadas.")


if __name__ == "__main__":
    main()
