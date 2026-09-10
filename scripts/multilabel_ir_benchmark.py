import json, time, re, math, sys, os
from collections import defaultdict

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
corpus_file = f"{base_dir}/data/export/tws_corpus_master_consolidated.jsonl"
gt_file = f"{base_dir}/data/export/tws_eval_ground_truth.jsonl"
report_file = f"{base_dir}/data/export/multilabel_benchmark_report.json"

STOP_WORDS = {
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na",
    "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "qual", "quais", "por que",
    "onde", "ser", "sao", "entre", "este", "esta", "pode", "deve", "utilizar", "usar", "sobre", "qual", "quais",
    "neste", "nessa", "nesses", "desses", "quando", "apos", "antes", "the", "in", "is", "at", "which", "on"
}

SYNONYMS = {
    "sfinal": ["makeplan", "switchplan", "startappserver", "checksync", "createpostreports", "updatestats", "2359", "final", "d+1"],
    "planman": ["showinfo", "resync", "checksync", "resetplan", "symphony", "preproduction", "scratch"],
    "conman": ["batchman", "mailman", "jobman", "showcpus", "showjobs", "start", "stop", "link", "limit", "lc", "confirm", "status"],
    "composer": ["vartable", "runcycle", "schedule", "jsdl", "erule", "lock", "unlock", "pool", "cpuname", "broker"],
    "edwa": ["eventrule", "genericeventplugin", "twsobjectmonitor", "filemonitor", "sendevent", "event1", "jobstatuschanged", "msglog", "objectkey"],
    "rest": ["twsd", "31116", "submit-ad-hoc-job", "joblog", "rerun", "update-priority", "release", "hold", "openapi", "bearer", "apikey"],
    "boot": ["systemd", "tebctl", "tws-domain-start", "hosts", "pidfile", "postgresql", "restart"]
}

TERM_EXPAND = {
    "senha": ["password", "credential", "passwd", "senha", "credencial"],
    "password": ["password", "senha", "credential"],
    "credencial": ["credential", "password", "senha", "apikey"],
    "autenticacao": ["authentication", "auth", "login", "jwt", "bearer", "apikey"],
    "authentication": ["authentication", "auth", "login", "jwt", "bearer"],
    "jwt": ["jwt", "token", "apikey", "api key", "bearer"],
    "chave": ["key", "token", "chave"],
    "falha": ["error", "fail", "erro", "problema", "falha", "failure"],
    "error": ["error", "fail", "erro", "falha", "failure", "problema"],
    "erro": ["error", "erro", "fail", "falha"],
    "mensagem": ["message", "msg", "mensagem", "codigo", "code"],
    "procedimento": ["procedure", "command", "procedimento", "comando", "passo", "step"],
    "comando": ["command", "comando", "cli"],
    "bloqueio": ["lockout", "lock", "bloqueio", "retry", "bind", "ldap"],
    "critica": ["critical", "hot", "list", "wsa", "deadline", "hotlist"],
    "dependencia": ["dependency", "deps", "dependencia", "predecessor", "follows", "conddep"],
    "ad-hoc": ["ad-hoc", "adhoc", "submit", "pontual"],
    "limpeza": ["cleanup", "purge", "limpeza", "logcleanupfrequency"],
    "repeticao": ["repeat", "every", "periodic", "interval"],
    "consulta": ["query", "showinfo", "display", "show", "consulta"],
    "plano": ["plan", "symphony", "plano", "production plan"],
    "production plan": ["plan", "symphony", "plano de producao", "plano"],
    "agenda": ["schedule", "schedule", "job stream", "stream", "agendamento"],
    "backup": ["backup", "backup", "restore", "copia", "copia de seguranca"],
    "restore": ["restore", "restauracao", "recuperacao", "backup"],
    "restauracao": ["restore", "recuperacao", "backup"],
    "agente": ["agent", "agente", "fta", "dynamic agent", "workstation"],
    "workstation": ["workstation", "cpu", "ws", "maestro host", "node", "agente"],
    "pool": ["pool", "dynamic pool", "broker", "workstation pool"],
    "virada": ["rollover", "jnextplan", "sfinal", "makeplan", "switchplan", "virada", "final"],
    "failover": ["failover", "switchmgr", "switch", "backup", "fta", "alta disponibilidade", "ha"],
    "seguranca": ["security", "seguranca", "tls", "ssl", "certificado", "ldap", "sso"],
    "security": ["security", "seguranca", "tls", "ssl", "sso", "authorization"],
    "console": ["dwc", "console", "dynamic workload console", "ui", "web"],
    "variavel": ["variable", "vartable", "variavel", "substituicao", "caret", "circunflexo", "expand"],
    "recurso": ["resource", "recurso", "resource advisor", "needs"],
    "evento": ["event", "evento", "event rule", "edwa", "trigger", "dispara"],
    "regra": ["rule", "event rule", "regra", "erule"],
    "jnextplan": ["jnextplan", "makeplan", "virada", "rollover", "switchplan"],
    "diario": ["daily", "everyday", "diario", "23:59", "2359"],
    "processador": ["processador", "processor", "switcheventprocessor", "switchevtp", "event processor"],
    "alternar": ["alternar", "switch", "switchmgr", "switcheventprocessor", "switchevtp"]
}

def clean_tokenize(text):
    if not text:
        return []
    words = re.findall(r"[A-Za-z0-9_\-\.\:\^\/\+\@]+", text.lower())
    cleaned = []
    for w in words:
        w_clean = w.strip(".,;:?!'\"()[]{}")
        if len(w_clean) > 1 and w_clean not in STOP_WORDS:
            cleaned.append(w_clean)
            if "-" in w_clean and any(w_clean.startswith(p) for p in ["aws", "awk", "eqq", "cww", "dsra"]):
                cleaned.append(w_clean.replace("-", ""))
            if "awswui" in w_clean:
                cleaned.append(w_clean.replace("awswui", "awsui"))
            elif "awsui" in w_clean:
                cleaned.append(w_clean.replace("awsui", "awswui"))
            subwords = re.findall(r'[A-Za-z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|[0-9]+', w_clean)
            if len(subwords) > 1:
                for sw in subwords:
                    if len(sw) > 2 and sw not in STOP_WORDS:
                        cleaned.append(sw.lower())
    return cleaned

def expand_tokens(tokens):
    out = set(tokens)
    for t in list(tokens):
        tl = t.lower()
        for root, syns in SYNONYMS.items():
            if root in tl:
                out.update(syns)
        for term, syns in TERM_EXPAND.items():
            if term in tl or tl in term:
                out.update(syns)
    return list(out)

# 1. Carregar Corpus
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
        
        synth_q = " ".join(item.get("synthetic_questions", []))
        full_text = f"{item['claim']} {item.get('context_prefix', '')} {synth_q}"
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

# 2. Carregar e unificar ground-truth (Multi-label Relevance)
with open(gt_file, "r", encoding="utf-8") as f:
    raw_gts = [json.loads(line) for line in f if line.strip()]

q_map = {}
for g in raw_gts:
    q_txt = g["question"].strip()
    tgt = g["target_claim_id"]
    cat = g.get("category", "Geral")
    if q_txt not in q_map:
        q_map[q_txt] = {"question": q_txt, "targets": set(), "category": cat}
    q_map[q_txt]["targets"].add(tgt)

eval_items = list(q_map.values())
total_eval = len(eval_items)
print(f"Total de perguntas unificadas (sem viés de colisão): {total_eval}")

def extract_ngrams(words, n=2):
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

def search_sota(query_raw, top_k=10, rerank_depth=40):
    raw_tokens = clean_tokenize(query_raw)
    expanded = expand_tokens(raw_tokens)
    if not expanded:
        return []
    
    doc_scores = defaultdict(float)
    q_terms = [t for t in expanded if t in postings]
    
    for q in q_terms:
        q_idf = idf[q]
        boost = 1.0
        if any(term in q for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "vartable", "rerun", "opens", "limit", "resync", "switchmgr", "carriedforward"]):
            boost = 3.0
            
        for doc_idx, tf in postings[q]:
            dl = doc_lens[doc_idx]
            num = tf * (k1 + 1.0)
            den = tf + k1 * (1.0 - b + b * (dl / avgdl))
            doc_scores[doc_idx] += boost * q_idf * (num / den)
            
    candidates = sorted(doc_scores.keys(), key=lambda i: doc_scores[i], reverse=True)[:rerank_depth]
    
    words = [w for w in re.findall(r"[A-Za-z0-9_\-]+", query_raw.lower()) if len(w) > 2 and w not in STOP_WORDS]
    bigrams = extract_ngrams(words, 2)
    trigrams = extract_ngrams(words, 3)
    unique_q_terms = set(words)
    
    reranked = []
    for doc_idx in candidates:
        s = doc_scores[doc_idx]
        text_lower = doc_texts[doc_idx]
        cid_lower = doc_ids[doc_idx].lower()
        
        for bg in bigrams:
            if len(bg) > 6 and bg in text_lower: s += 8.0
        for tg in trigrams:
            if len(tg) > 10 and tg in text_lower: s += 15.0
                
        if unique_q_terms:
            covered = sum(1 for t in unique_q_terms if t in text_lower)
            cov_ratio = covered / len(unique_q_terms)
            if cov_ratio >= 0.75: s *= 1.25
            elif cov_ratio >= 0.50: s *= 1.12
                
        aws_codes = re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", query_raw.lower())
        for code in aws_codes:
            code_alt = code.replace("awswui", "awsui") if "awswui" in code else code.replace("awsui", "awswui")
            if code in text_lower or code_alt in text_lower: s += 25.0
            if code in cid_lower or code_alt in cid_lower: s += 45.0
                
        reranked.append((doc_ids[doc_idx], s))
        
    reranked.sort(key=lambda x: x[1], reverse=True)
    return reranked[:top_k]

# Executar avaliação cega multi-label
start_time = time.time()
hits_at_1 = 0
hits_at_3 = 0
hits_at_5 = 0
hits_at_10 = 0
reciprocal_ranks = []
category_stats = defaultdict(lambda: {"total": 0, "hits_1": 0, "hits_5": 0, "hits_10": 0, "mrr_sum": 0.0})

for item in eval_items:
    q_text = item["question"]
    target_ids = item["targets"]
    category = item.get("category", "Geral")
    
    ranked = search_sota(q_text, top_k=10, rerank_depth=40)
    ranked_ids = [r[0] for r in ranked]
    
    # Encontrar o melhor rank entre todos os targets válidos
    rank = None
    for idx, r_id in enumerate(ranked_ids):
        if r_id in target_ids:
            rank = idx + 1
            break
            
    if rank is not None:
        rr = 1.0 / rank
    else:
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
    "total_unique_questions": total_eval,
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

print("\n" + "="*65)
print("   RELATÓRIO DO BENCHMARK MULTI-LABEL CANÔNICO (1.952 PERGUNTAS ÚNICAS)")
print("="*65)
print(f"Total Avaliado:        {total_eval} perguntas únicas em {elapsed:.2f}s ({summary['queries_per_second']} qps)")
print(f"Hit Rate @ 1:          {hits_at_1}/{total_eval} ({summary['hit_rate_at_1']*100:.2f}%)")
print(f"Hit Rate @ 3:          {hits_at_3}/{total_eval} ({summary['hit_rate_at_3']*100:.2f}%)")
print(f"Hit Rate @ 5:          {hits_at_5}/{total_eval} ({summary['hit_rate_at_5']*100:.2f}%)")
print(f"Hit Rate @ 10:         {hits_at_10}/{total_eval} ({summary['hit_rate_at_10']*100:.2f}%)")
print(f"MRR Geral:             {summary['mean_reciprocal_rank_mrr']:.4f}")
print("="*65)
print("\nDesempenho por Categoria:")
for cat, stats in summary["category_breakdown"].items():
    print(f"- {cat:<35}: Hit@1: {stats['hit_rate_at_1']*100:5.1f}% | Hit@5: {stats['hit_rate_at_5']*100:5.1f}% | Hit@10: {stats['hit_rate_at_10']*100:5.1f}% | MRR: {stats['mrr']:.4f} ({stats['total_questions']} q)")
