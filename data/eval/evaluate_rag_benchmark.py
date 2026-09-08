#!/usr/bin/env python3
"""Harness de Avaliacao Automatica do RAG TWS/HWA com Indexacao Hibrida Enriquecida.
Indexa:
- 1.449 claims canonicas (claims.jsonl)
- 335 mensagens canonicas AWS* (aws_messages_dictionary.jsonl)
- 92 opcoes globais do optman (optman_global_options_catalog.jsonl)
- Todas as evidencias de laboratorio (lab-validation-*.jsonl)
- Runbooks estruturados por secoes funcionais com boost ponderado

Mede:
- Hit Rate @ 1, @ 3, @ 5, @ 10
- Mean Reciprocal Rank (MRR)
"""
import glob, json, math, os, re, sys
from collections import defaultdict

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BENCHMARK_FILE = os.path.join(REPO_DIR, "data", "eval", "golden_qa_benchmark.jsonl")
CLAIMS_FILE = os.path.join(REPO_DIR, "data", "evidence", "claims.jsonl")
AWS_MSGS_FILE = os.path.join(REPO_DIR, "data", "evidence", "aws_messages_dictionary.jsonl")
OPTMAN_FILE = os.path.join(REPO_DIR, "data", "evidence", "optman_global_options_catalog.jsonl")
LAB_FILES = glob.glob(os.path.join(REPO_DIR, "data", "evidence", "lab-validation-*.jsonl"))
RUNBOOKS_DIR = os.path.join(REPO_DIR, "data", "runbooks")

SYNONYMS = {
    "sfinal": ["makeplan", "switchplan", "startappserver", "checksync", "createpostreports", "updatestats", "2359", "final", "d+1"],
    "planman": ["showinfo", "resync", "checksync", "resetplan", "symphony", "preproduction", "scratch"],
    "conman": ["batchman", "mailman", "jobman", "showcpus", "showjobs", "start", "stop", "link", "limit", "lc", "confirm", "status"],
    "composer": ["vartable", "runcycle", "schedule", "jsdl", "erule", "lock", "unlock", "pool", "cpuname", "broker"],
    "edwa": ["eventrule", "genericeventplugin", "twsobjectmonitor", "filemonitor", "sendevent", "event1", "jobstatuschanged", "msglog", "objectkey"],
    "rest": ["twsd", "31116", "submit-ad-hoc-job", "joblog", "rerun", "update-priority", "release", "hold", "openapi", "bearer", "apikey"],
    "boot": ["systemd", "tebctl", "tws-domain-start", "hosts", "pidfile", "postgresql", "restart"]
}

def tokenize(text):
    if not text:
        return set()
    words = re.findall(r"[A-Za-z0-9_\-\.\:\^\/\+]+", text.lower())
    stop = {"de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "qual", "quais", "por que", "onde"}
    tokens = {w for w in words if len(w) > 2 and w not in stop}
    
    expanded = set(tokens)
    for t in list(tokens):
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
                docs.append({"id": cid, "type": "canonical_claim", "text": text, "tokens": tokenize(text)})

    # 2. Dicionario de Mensagens AWS*
    if os.path.exists(AWS_MSGS_FILE):
        for line in open(AWS_MSGS_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('code', '')} {c.get('component', '')} {c.get('message', '')} {c.get('claim', '')}"
                docs.append({"id": cid, "type": "aws_message", "code": c.get("code"), "text": text, "tokens": tokenize(text)})

    # 3. Catalogo Optman
    if os.path.exists(OPTMAN_FILE):
        for line in open(OPTMAN_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('name', '')} {c.get('alias', '')} {c.get('value', '')} {c.get('claim', '')}"
                docs.append({"id": cid, "type": "optman_option", "text": text, "tokens": tokenize(text)})

    # 4. Lab validation claims
    for lf in LAB_FILES:
        for line in open(lf):
            if line.strip():
                try:
                    c = json.loads(line)
                    cid = c.get("claim_id", "")
                    if cid:
                        text = f"{c.get('claim', '')} {c.get('result', '')} {c.get('observations', '')} {c.get('sanitized_output', '')}"
                        docs.append({"id": cid, "type": "lab_evidence", "text": text, "tokens": tokenize(text)})
                except Exception:
                    pass

    # 5. Seções Estruturadas dos Runbooks Markdown
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
                docs.append({
                    "id": sec_id,
                    "type": "runbook_section",
                    "runbook": fname,
                    "title": title,
                    "text": sec,
                    "tokens": tokenize(sec)
                })
        except Exception:
            pass

    return docs

def compute_bm25(query_tokens, doc_tokens, query_raw, doc_text, avg_dl=60):
    if not doc_tokens:
        return 0.0
    k1 = 1.2
    b = 0.75
    overlap = query_tokens.intersection(doc_tokens)
    if not overlap:
        return 0.0
    score = 0.0
    dl = len(doc_tokens)
    
    # 1. Base BM25 com boost em termos HWA
    for t in overlap:
        boost = 1.0
        if any(term in t for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens", "limit", "securityutility", "resync", "twsobjectmonitor"]):
            boost = 3.5
        score += boost * ((k1 + 1) / (1.0 + k1 * (1.0 - b + b * (dl / avg_dl))))

    # 2. Boost em codigos de erro exatos (ex: AWSJDB802E, AWSVAL006E, AWSBEH021E)
    codes_in_query = re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", query_raw.lower())
    doc_lower = doc_text.lower()
    for code in codes_in_query:
        if code in doc_lower:
            score += 15.0  # boost forte para match de código de erro

    return score

def run_evaluation():
    if not os.path.exists(BENCHMARK_FILE):
        print(f"Erro: {BENCHMARK_FILE} nao encontrado.")
        return

    benchmark = [json.loads(line) for line in open(BENCHMARK_FILE)]
    docs = load_documents()
    print(f"Total de documentos indexados no corpus RAG: {len(docs)}")

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
            score = compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"])
            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        retrieved_docs = [s[1] for s in scored]

        rank = None
        for idx, d in enumerate(retrieved_docs):
            is_match = False
            # Match 1: claim id exato
            if d["id"] in expected_cids:
                is_match = True
            # Match 2: match por codigo de mensagem se houver
            elif d["type"] == "aws_message":
                for ecid in expected_cids:
                    if d.get("code", "").lower() in ecid.lower():
                        is_match = True
            # Match 3: match por runbook section com overlap substantivo
            elif d["type"] == "runbook_section" and expected_runbook and d.get("runbook") == expected_runbook:
                if len(q_tokens.intersection(d["tokens"])) >= 4:
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
