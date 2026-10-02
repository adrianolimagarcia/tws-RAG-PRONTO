#!/usr/bin/env python3
"""Experimento e Harness Comparativo de Re-ranking no Holdout Limpo V4 e Pool 423.

Avalia:
  1. Baseline de Producao (sem neural reranker)
  2. BGE-Reranker-Base (top-10, top-15, top-20)
  3. BGE-Reranker-Large (top-10, top-15, top-20)
  4. Gated Challenger (re-ranker so' atua quando a margem do 1o estagio < limiar)
  5. RRF / Blend (fusao de ranking 1o estagio + reranker)

Uso:
  /run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/.venv/bin/python scripts/experiment_reranker.py --bench data/eval/clean_holdout_v4_sealed.jsonl
"""
import argparse
import json
import math
import os
import sys
import time
from typing import List, Dict, Any, Tuple

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_DIR, "mcp_server"))

import tws_expert_mcp as mcp

HF_CACHE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"

_MODELS = {}

def get_reranker(model_name: str, device: str = "cpu"):
    if (model_name, device) in _MODELS:
        return _MODELS[(model_name, device)]
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_name, cache_dir=HF_CACHE, local_files_only=True)
    mod = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=HF_CACHE, local_files_only=True)
    dev = torch.device(device)
    mod.to(dev)
    mod.eval()
    _MODELS[(model_name, device)] = (tok, mod, dev)
    return tok, mod, dev

def score_pairs_batch(tok, mod, dev, pairs: List[Tuple[str, str]], batch_size: int = 16) -> List[float]:
    import torch
    scores = []
    for i in range(0, len(pairs), batch_size):
        batch = pairs[i:i+batch_size]
        inputs = tok(batch, padding=True, truncation=True, max_length=256, return_tensors="pt")
        inputs = {k: v.to(dev) for k, v in inputs.items()}
        with torch.no_grad():
            logits = mod(**inputs).logits.squeeze(-1)
            if logits.ndim == 0:
                logits = logits.unsqueeze(0)
            scores.extend(logits.cpu().tolist())
    return scores

def eval_ranking(ranks: List[Tuple[int, Any, int | None]]):
    n = len(ranks)
    if n == 0:
        return {}
    def hit(k):
        return sum(1 for _, _, p in ranks if p is not None and p <= k)
    mrr = sum(1.0 / p for _, _, p in ranks if p is not None) / n
    return {
        "n": n,
        "hit1": hit(1),
        "hit1_pct": round(100.0 * hit(1) / n, 2),
        "hit3": hit(3),
        "hit3_pct": round(100.0 * hit(3) / n, 2),
        "hit5": hit(5),
        "hit5_pct": round(100.0 * hit(5) / n, 2),
        "hit10": hit(10),
        "hit10_pct": round(100.0 * hit(10) / n, 2),
        "mrr": round(mrr, 4)
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bench", default="data/eval/clean_holdout_v4_sealed.jsonl")
    parser.add_argument("--device", default="cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") != "" else "cpu")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    # Checa cuda
    import torch
    if args.device == "cuda" and not torch.cuda.is_available():
        args.device = "cpu"

    print(f"Carregando benchmark: {args.bench} (device: {args.device})")
    items = [json.loads(line) for line in open(args.bench, encoding="utf-8") if line.strip()]
    if args.limit > 0:
        items = items[:args.limit]

    # Obter primeiros estagios (top-50 para permitir re-ranking ate top-20)
    print("Recuperando candidatos do primeiro estagio (MCP tws_expert_search)...")
    q_data = []
    t0 = time.time()
    for idx, item in enumerate(items):
        esperados = set(item.get("relevant_claim_ids") or [])
        if not esperados:
            continue
        res = mcp.handle_tool_call("tws_expert_search", {"query": item["question"], "top_k": 50})
        results = res.get("results", [])
        conf = res.get("confianca", "baixa")
        margin = res.get("margin", 0.0)
        q_data.append({
            "idx": idx,
            "id": item.get("id"),
            "question": item["question"],
            "esperados": esperados,
            "results": results,
            "confianca": conf,
            "margin": margin
        })
    print(f"Recuperacao concluida em {time.time()-t0:.2f}s ({len(q_data)} perguntas)")

    # 1. BASELINE
    base_ranks = []
    for q in q_data:
        achados = [x["claim_id"] for x in q["results"]]
        pos = next((i + 1 for i, c in enumerate(achados) if c in q["esperados"]), None)
        base_ranks.append((q["idx"], q["id"], pos))
    res_base = eval_ranking(base_ranks)
    print("\n" + "="*60)
    print("1. BASELINE DE PRODUCAO (sem reranker):")
    print(f"   Hit@1: {res_base['hit1']}/{res_base['n']} ({res_base['hit1_pct']}%) | "
          f"Hit@3: {res_base['hit3']} ({res_base['hit3_pct']}%) | "
          f"Hit@5: {res_base['hit5']} ({res_base['hit5_pct']}%) | "
          f"Hit@10: {res_base['hit10']} ({res_base['hit10_pct']}%) | MRR: {res_base['mrr']}")

    # 2. EXPERIMENTAR BGE-RERANKER-BASE E LARGE
    for m_name in ["BAAI/bge-reranker-base", "BAAI/bge-reranker-large"]:
        print("\n" + "="*60)
        print(f"Carregando {m_name}...")
        tok, mod, dev = get_reranker(m_name, device=args.device)

        for top_n in [10, 15, 20]:
            t_start = time.time()
            # Avalia puro
            puro_ranks = []
            # Avalia blend RRF
            rrf_ranks = []
            # Avalia gate (so mexe se confianca != alta)
            gate_ranks = []

            for q in q_data:
                cand = q["results"][:top_n]
                restante = q["results"][top_n:]
                pairs = [(q["question"], c["claim"]) for c in cand]
                scores = score_pairs_batch(tok, mod, dev, pairs)

                # Reordena por score cross-encoder
                cand_scored = list(zip(cand, scores))
                cand_reordered = [c for c, s in sorted(cand_scored, key=lambda x: x[1], reverse=True)]
                final_achados_puro = [x["claim_id"] for x in (cand_reordered + restante)]
                pos_puro = next((i + 1 for i, c in enumerate(final_achados_puro) if c in q["esperados"]), None)
                puro_ranks.append((q["idx"], q["id"], pos_puro))

                # Gated: se confianca == 'alta' (margem >= 0.177), mantem original; senao usa reranked
                if q["confianca"] == "alta":
                    final_achados_gate = [x["claim_id"] for x in q["results"]]
                else:
                    final_achados_gate = final_achados_puro
                pos_gate = next((i + 1 for i, c in enumerate(final_achados_gate) if c in q["esperados"]), None)
                gate_ranks.append((q["idx"], q["id"], pos_gate))

                # Blend RRF: rrf = 1 / (60 + rank_mcp) + 1 / (60 + rank_ce)
                ce_order = {c["claim_id"]: rank for rank, (c, s) in enumerate(sorted(cand_scored, key=lambda x: x[1], reverse=True))}
                blend_scored = []
                for rank_mcp, c in enumerate(cand):
                    cid = c["claim_id"]
                    r_ce = ce_order[cid]
                    rrf_score = 1.0 / (60.0 + rank_mcp) + 1.0 / (60.0 + r_ce)
                    blend_scored.append((c, rrf_score))
                blend_reordered = [c for c, s in sorted(blend_scored, key=lambda x: x[1], reverse=True)]
                final_achados_blend = [x["claim_id"] for x in (blend_reordered + restante)]
                pos_blend = next((i + 1 for i, c in enumerate(final_achados_blend) if c in q["esperados"]), None)
                rrf_ranks.append((q["idx"], q["id"], pos_blend))

            dur = time.time() - t_start
            rp = eval_ranking(puro_ranks)
            rg = eval_ranking(gate_ranks)
            rb = eval_ranking(rrf_ranks)
            print(f"\n[{m_name.split('/')[-1]} | top-{top_n} | {dur*1000/len(q_data):.1f} ms/q]")
            print(f"  * PURO : Hit@1: {rp['hit1']}/{rp['n']} ({rp['hit1_pct']}%) | "
                  f"Hit@3: {rp['hit3']} ({rp['hit3_pct']}%) | "
                  f"Hit@5: {rp['hit5']} ({rp['hit5_pct']}%) | MRR: {rp['mrr']}")
            print(f"  * GATE : Hit@1: {rg['hit1']}/{rg['n']} ({rg['hit1_pct']}%) | "
                  f"Hit@3: {rg['hit3']} ({rg['hit3_pct']}%) | "
                  f"Hit@5: {rg['hit5']} ({rg['hit5_pct']}%) | MRR: {rg['mrr']}")
            print(f"  * RRF  : Hit@1: {rb['hit1']}/{rb['n']} ({rb['hit1_pct']}%) | "
                  f"Hit@3: {rb['hit3']} ({rb['hit3_pct']}%) | "
                  f"Hit@5: {rb['hit5']} ({rb['hit5_pct']}%) | MRR: {rb['mrr']}")

if __name__ == "__main__":
    main()
