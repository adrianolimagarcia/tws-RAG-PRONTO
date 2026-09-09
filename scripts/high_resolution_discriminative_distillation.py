#!/usr/bin/env python3
"""Destilação Discriminativa de Alta Resolução (Doc2Query-- High-Res).
Gera perguntas sintéticas específicas baseadas em palavras-chave discriminativas únicas
(opções optman, subcomandos, keywords de JSDL/composer, parâmetros de config e sintomas),
valida na GPU com BAAI/bge-reranker-large e regrava no dataset de claims.
"""
import sys, os, time, json, re
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
CLAIMS_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/evidence/claims.jsonl"
MODEL_NAME = "BAAI/bge-reranker-large"
os.environ["HF_HOME"] = CACHE_DIR

def extract_discriminative_questions(claim_obj):
    text = claim_obj.get("claim", "")
    topic = claim_obj.get("topic", "")
    subtopic = claim_obj.get("subtopic", "")
    cid = claim_obj.get("claim_id", "")
    term_dict = claim_obj.get("normalized_terminology") or {}
    lower = text.lower()
    questions = []

    # 1. Opções Globais do Optman (ex: riskConfidence, logmanMinMaxPolicy, smtpServerName)
    opt_matches = re.findall(r"opção global\s+([A-Za-z0-9_]+)", text)
    if not opt_matches:
        opt_matches = re.findall(r"\b([A-Za-z0-9_]+)\s+\(alias\s+[a-z]{1,4}\)", text)
    for opt in set(opt_matches):
        if len(opt) > 3 and opt not in ["HCL", "Workload", "Automation", "Distributed"]:
            questions.append(f"Qual o propósito e valor padrão da opção global {opt} no optman do HWA?")
            questions.append(f"Como configurar a opção global {opt} no Master Domain Manager?")

    # 2. Keywords de definição (onlate, until, deadline, draft, vartable, runcyclegroup)
    for kw in ["onlate", "draft", "vartable", "runcyclegroup", "recovery", "follows", "needs", "opens", "prompt"]:
        if f"'{kw}'" in lower or f"\"{kw}\"" in lower or f"palavra-chave {kw}" in lower or f"keyword {kw}" in lower:
            questions.append(f"Qual a finalidade e como utilizar a keyword '{kw}' em definições de jobs no composer?")

    # 3. Subcomandos específicos do Conman e Composer
    for cmd in ["fence", "delete", "showcpus", "showschedules", "getmon", "switcheventprocessor", "switchmgr", "limit", "link", "unlink", "start", "stop"]:
        if f"comando conman '{cmd}'" in lower or f"conman {cmd}" in lower or f"conman '{cmd}'" in lower:
            questions.append(f"Como utilizar o comando conman '{cmd}' para gerenciar workstations e execução no HWA?")
        if f"comando composer '{cmd}'" in lower or f"composer {cmd}" in lower:
            questions.append(f"Qual o comportamento do comando composer '{cmd}' ao manipular objetos no banco?")

    # 4. Parâmetros de infraestrutura e variáveis de ambiente (evtsize, JobManager.ini, ResourceAdvisorUrl)
    for param in ["evtsize", "resourceadvisorurl", "eventprocessorhostname", "mdmhost", "ita_cfg", "tws_env.sh"]:
        if param in lower:
            questions.append(f"Como o parâmetro ou arquivo '{param}' é configurado na infraestrutura de agentes HWA?")

    # 5. Sintomas de incidentes operacionais específicos
    symptom_match = re.search(r"Sintoma:\s*([^.\n]+)", text)
    if symptom_match:
        symptom_text = symptom_match.group(1).strip()
        if len(symptom_text) > 15:
            questions.append(f"O que causa e como solucionar o problema: {symptom_text}?")

    # 6. Códigos de Erro (AWS, AWK, EQQ, CWW, DSRA)
    codes = re.findall(r"\b([A-Z]{3,6}[-_]?[0-9]{3,5}[A-Z]?)\b", text + " " + cid)
    for c in set(codes):
        clean_c = c.replace("-", "").replace("_", "").upper()
        if len(clean_c) >= 6 and any(clean_c.startswith(p) for p in ["AWS", "AWK", "EQQ", "CWW", "DSRA"]):
            questions.append(f"Qual é o significado da mensagem de erro {clean_c} no HWA e qual ação é recomendada?")

    # 7. Views do banco relacional (ex: JOB_DEPS_V)
    views = re.findall(r"\b([A-Z]{3,10}_[A-Z0-9_]{2,15}_V)\b", text)
    for v in set(views):
        questions.append(f"Qual é a estrutura e utilidade da view relacional {v} no banco de dados do HWA?")

    return list(set(questions))[:4]

def main():
    print("==================================================")
    print("  DESTILAÇÃO DISCRIMINATIVA DE ALTA RESOLUÇÃO     ")
    print("==================================================")
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Dispositivo: {device} ({torch.cuda.get_device_name(0)})")

    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, cache_dir=CACHE_DIR, torch_dtype=torch.float16, use_safetensors=True
    ).to(device)
    model.eval()
    print(f"Modelo carregado na GPU em {time.time()-t0:.2f}s!")

    claims = [json.loads(l) for l in open(CLAIMS_FILE) if l.strip()]
    candidate_pairs = []
    pair_metadata = []

    for c_idx, c in enumerate(claims):
        existing_q = set(c.get("synthetic_questions", []))
        high_res_q = extract_discriminative_questions(c)
        for q in high_res_q:
            if q not in existing_q:
                candidate_pairs.append([q, c["claim"][:600]])
                pair_metadata.append((c_idx, q))

    print(f"Total de perguntas discriminativas de alta resolução geradas: {len(candidate_pairs)}")
    if not candidate_pairs:
        print("Nenhuma pergunta nova para validar.")
        return

    # Validar na GPU em batches
    batch_size = 32
    scores = []
    t_start = time.time()
    with torch.no_grad():
        for i in range(0, len(candidate_pairs), batch_size):
            batch = candidate_pairs[i:i+batch_size]
            inputs = tokenizer(batch, padding=True, truncation=True, max_length=256, return_tensors="pt").to(device)
            batch_scores = model(**inputs, return_dict=True).logits.view(-1).float().cpu().tolist()
            scores.extend(batch_scores)
            if (i // batch_size) % 10 == 0:
                print(f"  Validado {min(i+batch_size, len(candidate_pairs))}/{len(candidate_pairs)} pares ({time.time()-t_start:.1f}s)...")

    # Filtrar com logit >= 1.0 (alta fidelidade)
    approved = 0
    for (c_idx, q), score in zip(pair_metadata, scores):
        if score >= 1.0:
            c = claims[c_idx]
            if "synthetic_questions" not in c:
                c["synthetic_questions"] = []
            if q not in c["synthetic_questions"]:
                c["synthetic_questions"].append(q)
                approved += 1

    print(f"\nValidação concluída: {approved}/{len(candidate_pairs)} perguntas aprovadas pela GPU ({approved/len(candidate_pairs)*100:.1f}%)!")

    # Gravar claims atualizadas
    with open(CLAIMS_FILE, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    total_with_q = sum(1 for c in claims if c.get("synthetic_questions"))
    total_q_count = sum(len(c.get("synthetic_questions", [])) for c in claims)
    print(f"Dataset de claims regravado com sucesso!")
    print(f"Total de claims com perguntas: {total_with_q}/{len(claims)} ({total_with_q/len(claims)*100:.1f}%)")
    print(f"Total de perguntas sintéticas discriminativas no dataset: {total_q_count}")

if __name__ == "__main__":
    main()
