#!/usr/bin/env python3
"""Harness de Avaliacao Automatica do RAG TWS/HWA com Indexacao Hibrida.
Consome o golden_qa_benchmark.jsonl (35 perguntas) e indexa:
- 1.449 claims canonicas (claims.jsonl)
- Todas as evidencias de laboratorio (lab-validation-*.jsonl)
- Runbooks fatiados por secoes funcionais (data/runbooks/*.md)

Mede:
- Hit Rate @ 1, @ 3, @ 5
- Mean Reciprocal Rank (MRR)
- Cobertura de runbooks
"""
import glob, json, math, os, re, sys
from collections import defaultdict

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BENCHMARK_FILE = os.path.join(REPO_DIR, "data", "eval", "golden_qa_benchmark.jsonl")
CLAIMS_FILE = os.path.join(REPO_DIR, "data", "evidence", "claims.jsonl")
LAB_FILES = glob.glob(os.path.join(REPO_DIR, "data", "evidence", "lab-validation-*.jsonl"))
RUNBOOKS_DIR = os.path.join(REPO_DIR, "data", "runbooks")

# Mapa de expansao de sinonimos semanticos de termos operacionais do HWA
SYNONYMS = {
    "sfinal": ["makeplan", "switchplan", "startappserver", "checksyc", "createpostreports", "updatestats", "2359", "final"],
    "planman": ["showinfo", "resync", "checksyc", "resetplan", "symphony", "preproduction"],
    "conman": ["batchman", "mailman", "jobman", "showcpus", "showjobs", "start", "stop", "link", "limit", "lc"],
    "composer": ["vartable", "runcyle", "schedule", "jsdl", "erule", "lock", "unlock", "pool"],
    "edwa": ["eventrule", "genericeventplugin", "twsobjectmonitor", "filemonitor", "sendevent", "event1", "jobstatuschanged"],
    "rest": ["twsd", "31116", "submit-ad-hoc-job", "joblog", "rerun", "update-priority", "release", "hold"]
}

def tokenize(text):
    if not text:
        return set()
    words = re.findall(r"[A-Za-z0-9_\-\.\:\^]+", text.lower())
    stop = {"de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "qual", "quais", "por que", "onde", "como"}
    tokens = {w for w in words if len(w) > 2 and w not in stop}
    
    # Adicionar expansao de sinonimos
    expanded = set(tokens)
    for t in tokens:
        for root, syns in SYNONYMS.items():
            if root in t:
                expanded.update(syns)
    return expanded

def load_documents():
    docs = []
    # 1. Claims canonicas
    if os.path.exists(CLAIMS_FILE):
        for line in open(CLAIMS_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('claim', '')} {c.get('notes', '')} {c.get('topic', '')} {c.get('subtopic', '')}"
                docs.append({
                    "id": cid,
                    "type": "canonical_claim",
                    "text": text,
                    "tokens": tokenize(text)
                })

    # 2. Lab validation claims
    for lf in LAB_FILES:
        for line in open(lf):
            if line.strip():
                try:
                    c = json.loads(line)
                    cid = c.get("claim_id", "")
                    if cid:
                        text = f"{c.get('claim', '')} {c.get('result', '')} {c.get('observations', '')} {c.get('sanitized_output', '')}"
                        docs.append({
                            "id": cid,
                            "type": "lab_evidence",
                            "text": text,
                            "tokens": tokenize(text)
                        })
                except Exception:
                    pass

    # 3. Seções estruturadas dos Runbooks Markdown
    for rbf in glob.glob(os.path.join(RUNBOOKS_DIR, "*.md")):
        fname = os.path.basename(rbf)
        try:
            content = open(rbf, encoding="utf-8", errors="ignore").read()
            sections = re.split(r"\n##+\s+", content)
            for s_idx, sec in enumerate(sections):
                if not sec.strip(): continue
                lines = sec.strip().splitlines()
                title = lines[0] if lines else f"section_{s_idx}"
                sec_id = f"runbook:{fname}:{s_idx}"
                tokens = tokenize(sec)
                docs.append({
                    "id": sec_id,
                    "type": "runbook_section",
                    "runbook": fname,
                    "title": title,
                    "text": sec,
                    "tokens": tokens
                })
        except Exception:
            pass

    return docs

def compute_bm25(query_tokens, doc_tokens, avg_dl=50):
    if not doc_tokens:
        return 0.0
    k1 = 1.2
    b = 0.75
    overlap = query_tokens.intersection(doc_tokens)
    if not overlap:
        return 0.0
    score = 0.0
    dl = len(doc_tokens)
    for t in overlap:
        boost = 1.0
        # Boost de termos técnicos específicos de HWA
        if any(term in t for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens", "limit", "securityutility", "resync", "twsobjectmonitor"]):
            boost = 3.0
        score += boost * ((k1 + 1) / (1.0 + k1 * (1.0 - b + b * (dl / avg_dl))))
    return score

def run_evaluation():
    if not os.path.exists(BENCHMARK_FILE):
        print(f"Erro: {BENCHMARK_FILE} nao encontrado.")
        return

    benchmark = [json.loads(line) for line in open(BENCHMARK_FILE)]
    docs = load_documents()
    print(f"Documentos indexados para retrieval: {len(docs)}")

    top_k_hits = {1: 0, 3: 0, 5: 0, 10: 0}
    reciprocal_ranks = []
    results = []

    for b in benchmark:
        qid = b.get("id")
        q_text = b.get("question", "")
        expected_cids = set(b.get("relevant_claim_ids", []))
        expected_runbook = b.get("runbook_ref")
        q_tokens = tokenize(q_text)

        scored = []
        for doc in docs:
            score = compute_bm25(q_tokens, doc["tokens"])
            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        retrieved_docs = [s[1] for s in scored]

        # Avaliar match por claim ou por runbook
        rank = None
        for idx, d in enumerate(retrieved_docs):
            is_match = False
            # Match 1: claim id exato
            if d["id"] in expected_cids:
                is_match = True
            # Match 2: se for runbook esperado
            elif d["type"] == "runbook_section" and expected_runbook and d.get("runbook") == expected_runbook:
                # Se a pergunta tem sobreposição de termos técnicos na seção
                if len(q_tokens.intersection(d["tokens"])) >= 3:
                    is_match = True

            if is_match:
                rank = idx + 1
                break

        if rank is not None:
            reciprocal_ranks.append(1.0 / rank)
            if rank <= 1: top_k_hits[1] += 1
            if rank <= 3: top_k_hits[3] += 1
            if rank <= 5: top_k_hits[5] += 1
            if rank <= 10: top_k_hits[10] += 1
        else:
            reciprocal_ranks.append(0.0)

        results.append({
            "id": qid,
            "domain": b.get("domain"),
            "question": q_text,
            "rank": rank,
            "expected_claims": list(expected_cids),
            "expected_runbook": expected_runbook,
            "top_3_retrieved": [d["id"] for d in retrieved_docs[:3]]
        })

    total = len(benchmark)
    mrr = sum(reciprocal_ranks) / total if total else 0.0

    print("==================================================")
    print("      RELATÓRIO DE AVALIAÇÃO DO RAG BENCHMARK     ")
    print("==================================================")
    print(f"Total de Perguntas Avaliadas: {total}")
    print(f"Hit Rate @ 1:  {top_k_hits[1]}/{total} ({top_k_hits[1]/total*100:.1f}%)")
    print(f"Hit Rate @ 3:  {top_k_hits[3]}/{total} ({top_k_hits[3]/total*100:.1f}%)")
    print(f"Hit Rate @ 5:  {top_k_hits[5]}/{total} ({top_k_hits[5]/total*100:.1f}%)")
    print(f"Hit Rate @ 10: {top_k_hits[10]}/{total} ({top_k_hits[10]/total*100:.1f}%)")
    print(f"Mean Reciprocal Rank (MRR):    {mrr:.4f}")
    print("==================================================")

    out_file = os.path.join(REPO_DIR, "data", "eval", "eval_summary.json")
    with open(out_file, "w") as f:
        json.dump({
            "total": total,
            "hit_rate_at_1": top_k_hits[1] / total,
            "hit_rate_at_3": top_k_hits[3] / total,
            "hit_rate_at_5": top_k_hits[5] / total,
            "hit_rate_at_10": top_k_hits[10] / total,
            "mrr": mrr,
            "details": results
        }, f, indent=2, ensure_ascii=False)
    print(f"Sumário de avaliação gravado em {out_file}")

if __name__ == "__main__":
    run_evaluation()
