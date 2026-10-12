#!/usr/bin/env python3
"""Gera corpus enriquecido de forma transparente e compatível com o MCP e auditor.

Mescla os claims do corpus master com os metadados gerados em data/export/enriched_claims_store.jsonl:
- Preserva todos os campos existentes.
- Adiciona as novas perguntas sintéticas no array `synthetic_questions`.
- Adiciona keywords/sinônimos em `context_prefix` ou novo campo semântico.
"""
import argparse
import json
import os
import sys

CORPUS_IN = "data/export/tws_corpus_master_consolidated.jsonl"
STORE_PATH = "data/export/enriched_claims_store.jsonl"
CORPUS_OUT = "data/export/tws_corpus_enriched.jsonl"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", default=STORE_PATH)
    parser.add_argument("--out", default=CORPUS_OUT)
    args = parser.parse_args()

    store = {}
    if os.path.exists(args.store):
        for line in open(args.store, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                store[d["claim_id"]] = d

    print(f"Lidos {len(store)} claims enriquecidos de {args.store}")

    modificados = 0
    total = 0
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f_out:
        for line in open(CORPUS_IN, encoding="utf-8"):
            if not line.strip():
                continue
            item = json.loads(line)
            cid = item["claim_id"]
            total += 1
            if cid in store:
                enr = store[cid]
                novas_p = enr.get("perguntas", [])
                novas_kw = enr.get("keywords", [])
                
                # Atualiza synthetic_questions
                sq = item.get("synthetic_questions") or []
                sq_set = set(sq)
                for p in novas_p:
                    if p not in sq_set:
                        sq.append(p)
                        sq_set.add(p)
                item["synthetic_questions"] = sq

                # Adiciona keywords ao context_prefix
                if novas_kw:
                    kw_str = " Termos correlatos: " + ", ".join(novas_kw) + "."
                    cp = item.get("context_prefix") or ""
                    if "Termos correlatos:" not in cp:
                        item["context_prefix"] = (cp + kw_str).strip()

                modificados += 1

            f_out.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Novo corpus gerado em {args.out}: {total} claims ({modificados} enriquecidos)")

if __name__ == "__main__":
    main()
