import json, time, re, sys, os, math
from collections import defaultdict

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
corpus_file = f"{base_dir}/data/export/tws_corpus_master_consolidated.jsonl"
gt_file = f"{base_dir}/data/export/tws_eval_ground_truth.jsonl"
report_file = f"{base_dir}/data/export/full_benchmark_report.json"

print("Carregando corpus consolidado...")
doc_ids = []
doc_lens = []
postings = defaultdict(list) # term -> list of (doc_idx, tf)

start_build = time.time()
with open(corpus_file, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if not line.strip(): continue
        item = json.loads(line)
        cid = item["claim_id"]
        doc_ids.append(cid)
        
        text = f"{item['claim']} {item.get('context_prefix', '')} {' '.join(item.get('synthetic_questions', []))}"
        tokens = re.findall(r"\w+", text.lower())
        doc_lens.append(len(tokens))
        
        tf_map = defaultdict(int)
        for t in tokens:
            tf_map[t] += 1
            
        for t, count in tf_map.items():
            postings[t].append((idx, count))

N = len(doc_ids)
avgdl = sum(doc_lens) / N if N > 0 else 0.0
k1 = 1.5
b = 0.75

# Pré-calcular IDF
idf = {}
for term, p_list in postings.items():
    df = len(p_list)
    idf[term] = math.log((N - df + 0.5) / (df + 0.5) + 1.0)

print(f"Índice invertido construído em {time.time()-start_build:.2f}s para {N} documentos.")

def search_bm25(query_tokens, top_k=10):
    doc_scores = defaultdict(float)
    q_terms = [t for t in query_tokens if t in postings]
    if not q_terms:
        return []
        
    for q in q_terms:
        q_idf = idf[q]
        for doc_idx, tf in postings[q]:
            dl = doc_lens[doc_idx]
            num = tf * (k1 + 1.0)
            den = tf + k1 * (1.0 - b + b * (dl / avgdl))
            doc_scores[doc_idx] += q_idf * (num / den)
            
    # Obter top_k
    top_indices = sorted(doc_scores.keys(), key=lambda i: doc_scores[i], reverse=True)[:top_k]
    return [(doc_ids[i], doc_scores[i]) for i in top_indices]

print(f"Carregando {gt_file}...")
with open(gt_file, "r", encoding="utf-8") as f:
    eval_questions = [json.loads(line) for line in f if line.strip()]

total_eval = len(eval_questions)
print(f"Executando Full Benchmark em {total_eval} perguntas...")

start_eval = time.time()
hits_at_1 = 0
hits_at_3 = 0
hits_at_5 = 0
hits_at_10 = 0
reciprocal_ranks = []
category_stats = defaultdict(lambda: {"total": 0, "hits_1": 0, "hits_5": 0, "hits_10": 0, "mrr_sum": 0.0})

for q_item in eval_questions:
    q_text = q_item["question"]
    target_id = q_item["target_claim_id"]
    category = q_item.get("category", "Geral")
    q_tokens = re.findall(r"\w+", q_text.lower())
    
    ranked = search_bm25(q_tokens, top_k=10)
    ranked_ids = [r[0] for r in ranked]
    
    if target_id in ranked_ids:
        rank = ranked_ids.index(target_id) + 1
        rr = 1.0 / rank
    else:
        rank = None
        rr = 0.0
        
    reciprocal_ranks.append(rr)
    category_stats[category]["total"] += 1
    category_stats[category]["mrr_sum"] += rr
    
    if rank == 1:
        hits_at_1 += 1
        category_stats[category]["hits_1"] += 1
    if rank is not None and rank <= 3:
        hits_at_3 += 1
    if rank is not None and rank <= 5:
        hits_at_5 += 1
        category_stats[category]["hits_5"] += 1
    if rank is not None and rank <= 10:
        hits_at_10 += 1
        category_stats[category]["hits_10"] += 1

elapsed = time.time() - start_eval
mrr = sum(reciprocal_ranks) / total_eval if total_eval > 0 else 0

summary = {
    "total_questions_evaluated": total_eval,
    "elapsed_seconds": round(elapsed, 2),
    "queries_per_second": round(total_eval / elapsed, 1) if elapsed > 0 else 0,
    "hit_rate_at_1": round(hits_at_1 / total_eval, 4),
    "hit_rate_at_3": round(hits_at_3 / total_eval, 4),
    "hit_rate_at_5": round(hits_at_5 / total_eval, 4),
    "hit_rate_at_10": round(hits_at_10 / total_eval, 4),
    "mean_reciprocal_rank_mrr": round(mrr, 4),
    "category_breakdown": {}
}

for cat, s in category_stats.items():
    tot = s["total"]
    summary["category_breakdown"][cat] = {
        "total_questions": tot,
        "hit_rate_at_1": round(s["hits_1"] / tot, 4) if tot > 0 else 0,
        "hit_rate_at_5": round(s["hits_5"] / tot, 4) if tot > 0 else 0,
        "hit_rate_at_10": round(s["hits_10"] / tot, 4) if tot > 0 else 0,
        "mrr": round(s["mrr_sum"] / tot, 4) if tot > 0 else 0
    }

with open(report_file, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("\n" + "="*60)
print("       RELATÓRIO DO FULL BENCHMARK (3.180 PERGUNTAS)")
print("="*60)
print(f"Total Avaliado:        {total_eval} perguntas em {elapsed:.2f}s ({summary['queries_per_second']} qps)")
print(f"Hit Rate @ 1:          {hits_at_1}/{total_eval} ({summary['hit_rate_at_1']*100:.2f}%)")
print(f"Hit Rate @ 3:          {hits_at_3}/{total_eval} ({summary['hit_rate_at_3']*100:.2f}%)")
print(f"Hit Rate @ 5:          {hits_at_5}/{total_eval} ({summary['hit_rate_at_5']*100:.2f}%)")
print(f"Hit Rate @ 10:         {hits_at_10}/{total_eval} ({summary['hit_rate_at_10']*100:.2f}%)")
print(f"MRR Geral:             {summary['mean_reciprocal_rank_mrr']:.4f}")
print("="*60)
print("\nDesempenho por Categoria:")
for cat, stats in summary["category_breakdown"].items():
    print(f"- {cat:<35}: Hit@1: {stats['hit_rate_at_1']*100:5.1f}% | Hit@5: {stats['hit_rate_at_5']*100:5.1f}% | MRR: {stats['mrr']:.4f} ({stats['total_questions']} q)")
print(f"\nRelatório completo gravado em {report_file}")
