#!/usr/bin/env python3
"""Aplica enriquecimento offline de forma cirúrgica e segura.

Políticas de preservação:
1. Injeta APENAS perguntas sintéticas (perguntas geradas).
2. NÃO injeta keywords genéricas como texto livre, pois poluem o IDF do BM25 (ex: 'monitoramento', 'conman', 'HWA').
3. Limita a 2 perguntas sintéticas por claim enriquecido.
4. Preserva exatamente o claim, category, context_prefix e demais metadados.
"""
import argparse
import json
import os
import re
import sys

CORPUS_ORIGINAL = "data/export/tws_corpus_master_consolidated.jsonl"
STORE_PATH = "data/export/enriched_claims_store.jsonl"
CORPUS_OUT = "data/export/tws_corpus_enriched_safe.jsonl"

def main():
    if not os.path.exists(STORE_PATH):
        raise SystemExit(f"Store não encontrada: {STORE_PATH}")

    store = {}
    for line in open(STORE_PATH, encoding="utf-8"):
        if not line.strip():
            continue
        d = json.loads(line)
        store[d["claim_id"]] = d

    print(f"Lidos {len(store)} claims enriquecidos da store.")

    bench_toks = []
    bench_file = "data/eval/clean_holdout_v4_sealed.jsonl"
    if os.path.exists(bench_file):
        for line in open(bench_file, encoding="utf-8"):
            if not line.strip(): continue
            d = json.loads(line)
            # extrai tokens significativos da pergunta do benchmark
            toks = set(re.findall(r"\w+", d["question"].lower()))
            bench_toks.append(toks)

    total_injetados = 0
    total_filtrados = 0
    with open(CORPUS_OUT, "w", encoding="utf-8") as fout:
        for line in open(CORPUS_ORIGINAL, encoding="utf-8"):
            if not line.strip():
                continue
            item = json.loads(line)
            cid = item["claim_id"]

            if cid in store:
                enr = store[cid]
                # Pega apenas perguntas sintéticas (máximo 2)
                novas_perguntas = enr.get("perguntas", [])[:2]
                
                # synthetic_questions existentes
                existentes = list(item.get("synthetic_questions") or [])
                existentes_set = set(existentes)

                adicionadas = []
                for q in novas_perguntas:
                    q_limpa = q.strip()
                    if not q_limpa or q_limpa in existentes_set:
                        continue
                    
                    # Verificação rigorosa anti-vazamento (Jaccard < 0.50 com o benchmark)
                    q_toks = set(re.findall(r"\w+", q_limpa.lower()))
                    max_j = 0.0
                    for b_toks in bench_toks:
                        inter = len(q_toks & b_toks)
                        union = len(q_toks | b_toks)
                        j = inter / union if union > 0 else 0.0
                        if j > max_j:
                            max_j = j
                    
                    if max_j < 0.50:
                        adicionadas.append(q_limpa)
                        existentes_set.add(q_limpa)
                    else:
                        total_filtrados += 1

                if adicionadas:
                    item["synthetic_questions"] = existentes + adicionadas
                    total_injetados += 1

            fout.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Novo corpus seguro gerado em {CORPUS_OUT}: {total_injetados} claims enriquecidos ({total_filtrados} perguntas filtradas por salvaguarda).")

if __name__ == "__main__":
    main()
