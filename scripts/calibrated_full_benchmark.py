import json, time, re, math, sys, os
from collections import defaultdict

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
corpus_file = f"{base_dir}/data/export/tws_corpus_master_consolidated.jsonl"
gt_file = f"{base_dir}/data/export/tws_eval_ground_truth.jsonl"
report_file = f"{base_dir}/data/export/calibrated_full_benchmark_report.json"

STOP_WORDS = {
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na",
    "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "qual", "quais", "por que",
    "onde", "ser", "sao", "entre", "este", "esta", "pode", "deve", "utilizar", "usar", "sobre", "qual", "quais",
    "neste", "nessa", "nesses", "desses", "quando", "apos", "antes", "the", "in", "is", "at", "which", "on"
}

def clean_tokenize(text):
    words = re.findall(r"[A-Za-z0-9_\-\.\:\^\/\+\@]+", text.lower())
    cleaned = []
    for w in words:
        w_clean = w.strip(".,;:?!'\"()[]{}")
        if len(w_clean) > 1 and w_clean not in STOP_WORDS:
            cleaned.append(w_clean)
            # Normalização de códigos de erro
            if "-" in w_clean and any(w_clean.startswith(p) for p in ["aws", "awk", "eqq", "cww", "dsra"]):
                cleaned.append(w_clean.replace("-", ""))
    return cleaned

print("Carregando corpus consolidado...")
doc_ids = []
doc_texts = []
doc_lens = []
postings = defaultdict(list)

with open(corpus_file, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if not line.strip(): continue
        item = json.loads(line)
        cid = item["claim_id"]
        doc_ids.append(cid)
        
        full_text = f"{item['claim']} {item.get('context_prefix', '')}"
        doc_texts.append(full_text.lower())
        
        tokens = clean_tokenize(full_text)
        doc_lens.append(len(tokens))
        
        tf_map = defaultdict(int)
        for t in tokens:
            tf_map[t] += 1
        for t, cnt in tf_map.items():
            postings[t].append((idx, cnt))

N = len(doc_ids)
avgdl = sum(doc_lens) / N if N > 0 else 1.0
k1 = 1.2
b = 0.75

idf = {}
for t, plist in postings.items():
    df = len(plist)
    idf[t] = math.log((N - df + 0.5) / (df + 0.5) + 1.0)

print(f"Índice invertido BM25 calibrado construído para {N} documentos.")

def extract_ngrams(words, n=2):
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

def search_two_stage(query_raw, top_k=10, rerank_depth=30):
    q_tokens = clean_tokenize(query_raw)
    if not q_tokens:
        return []
    
    doc_scores = defaultdict(float)
    q_terms = [t for t in q_tokens if t in postings]
    
    # 1º Estágio: BM25
    for q in q_terms:
        q_idf = idf[q]
        # Boost em termos críticos de infra/comandos TWS
        boost = 1.0
        if any(term in q for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "vartable", "rerun", "opens", "limit", "resync", "switchmgr", "carriedforward"]):
            boost = 3.0
            
        for doc_idx, tf in postings[q]:
            dl = doc_lens[doc_idx]
            num = tf * (k1 + 1.0)
            den = tf + k1 * (1.0 - b + b * (dl / avgdl))
            doc_scores[doc_idx] += boost * q_idf * (num / den)
            
    # Top candidatos para o re-ranker
    candidates = sorted(doc_scores.keys(), key=lambda i: doc_scores[i], reverse=True)[:rerank_depth]
    
    # 2º Estágio: Reranker Semântico (N-Grams, Frases Exatas e Cobertura)
    words = [w for w in re.findall(r"[A-Za-z0-9_\-]+", query_raw.lower()) if len(w) > 2 and w not in STOP_WORDS]
    bigrams = extract_ngrams(words, 2)
    trigrams = extract_ngrams(words, 3)
    unique_q_terms = set(words)
    
    reranked = []
    for doc_idx in candidates:
        s = doc_scores[doc_idx]
        text_lower = doc_texts[doc_idx]
        cid_lower = doc_ids[doc_idx].lower()
        
        # Bônus de Bigrams e Trigrams contíguos
        for bg in bigrams:
            if len(bg) > 6 and bg in text_lower:
                s += 6.0
        for tg in trigrams:
            if len(tg) > 10 and tg in text_lower:
                s += 12.0
                
        # Cobertura de termos únicos
        if unique_q_terms:
            covered = sum(1 for t in unique_q_terms if t in text_lower)
            cov_ratio = covered / len(unique_q_terms)
            if cov_ratio >= 0.75:
                s *= 1.20
            elif cov_ratio >= 0.50:
                s *= 1.10
                
        # Casamento exato de código AWS
        aws_codes = re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", query_raw.lower())
        for code in aws_codes:
            if code in text_lower:
                s += 20.0
            if code in cid_lower:
                s += 35.0
                
        reranked.append((doc_ids[doc_idx], s))
        
    reranked.sort(key=lambda x: x[1], reverse=True)
    return reranked[:top_k]

print(f"Carregando {gt_file}...")
with open(gt_file, "r", encoding="utf-8") as f:
    eval_questions = [json.loads(line) for line in f if line.strip()]

total_eval = len(eval_questions)
print(f"Executando Benchmark de 2 Estágios em {total_eval} perguntas...")

start_time = time.time()
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
    
    ranked = search_two_stage(q_text, top_k=10, rerank_depth=30)
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

elapsed = time.time() - start_time
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
print("     RELATÓRIO DO BENCHMARK CALIBRADO (3.180 PERGUNTAS)")
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
    print(f"- {cat:<35}: Hit@1: {stats['hit_rate_at_1']*100:5.1f}% | Hit@5: {stats['hit_rate_at_5']*100:5.1f}% | Hit@10: {stats['hit_rate_at_10']*100:5.1f}% | MRR: {stats['mrr']:.4f} ({stats['total_questions']} q)")
