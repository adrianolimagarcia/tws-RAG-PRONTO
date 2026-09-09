#!/usr/bin/env python3
"""Destilação abrangente das 536 claims restantes na GPU GTX 1050 Ti.
Gera perguntas sintéticas específicas por domínio (DB Views, Scheduling, Observability,
Security, Agents) e valida com BAAI/bge-reranker-large antes de injetar no dataset estático.
"""
import sys, os, time, json, re
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
CLAIMS_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/evidence/claims.jsonl"
MODEL_NAME = "BAAI/bge-reranker-large"
os.environ["HF_HOME"] = CACHE_DIR

def infer_domain_questions(claim_obj):
    text = claim_obj.get("claim", "")
    topic = claim_obj.get("topic", "")
    subtopic = claim_obj.get("subtopic", "")
    lower = text.lower()
    questions = []

    # 1. Views do Banco Relacional e Dicionário de Dados
    views = re.findall(r"\b([A-Z]{3,10}_[A-Z0-9_]{2,15}_V)\b", text)
    if views or "view" in lower or "database" in lower or "tabela" in lower:
        for v in set(views):
            questions.append(f"Qual é o propósito da view de banco {v} no HCL Workload Automation?")
            questions.append(f"Como consultar dependências e definições utilizando a view {v} no banco de dados?")
        if not views and "dependen" in lower and "banco" in lower:
            questions.append("Quais são as principais views relacionais para auditar dependências no banco do HWA?")

    # 2. Scheduling, RunCycles, Prompts e Dependências
    if "runcycle" in lower or "every" in lower or "prompt" in lower:
        questions.append(f"Como configurar e qual o comportamento de {subtopic or 'regras de agendamento'} no HWA?")
    if "conddep" in lower or "dependência condicional" in lower:
        questions.append("Como definir dependências condicionais entre jobs no HWA?")

    # 3. Observabilidade, AIDA, KPIs e Logs
    if "aida" in lower or "ai data advisor" in lower:
        questions.append("Como o AIDA atua na detecção de anomalias e predição de problemas no HWA?")
        questions.append("Como configurar e monitorar KPIs de execução preditiva com AIDA?")
    if "prometheus" in lower or "grafana" in lower or "métrica" in lower:
        questions.append("Como exportar métricas operacionais do HWA para ferramentas de monitoramento como Prometheus?")

    # 4. Segurança, Permissões, Usuários e Auditoria
    if "security" in lower or "auditing" in lower or "permissão" in lower or "permissões" in lower:
        questions.append(f"Quais são as diretrizes de segurança e governança para {subtopic or 'acesso a objetos'} no HWA?")
        questions.append("Como configurar auditoria e rastreabilidade de mudanças no Dynamic Workload Console?")

    # 5. Agentes, Dynamic Pool e Topologia
    if "fault-tolerant" in lower or "fta" in lower:
        questions.append("Qual a arquitetura e comportamento de agentes tolerantes a falhas (FTA) no HWA?")
    if "pool" in lower or "dynamic pool" in lower:
        questions.append("Como o HWA balanceia e despacha jobs dinamicamente em pools de agentes?")

    # 6. SLA, Automação de Mudanças e Melhores Práticas
    if "sla" in lower or "service level" in lower:
        questions.append("Como o HWA Distributed monitora SLAs de execução e caminhos críticos de jobs?")
    if "draft" in lower and "job stream" in lower:
        questions.append("Como a palavra-chave draft impede que um job stream entre no plano de produção?")

    # Fallback contextual
    if not questions:
        sentences = re.split(r'(?<!\d)\.(?!\d)', text)
        first_clause = sentences[0].strip() if sentences else text[:80]
        if len(first_clause) > 20:
            questions.append(f"Qual a regra documentada no HWA Distributed sobre: {first_clause}?")

    return list(set(questions))[:3]

def main():
    print("==================================================")
    print("  DESTILAÇÃO ABRANGENTE DAS CLAIMS RESTANTES      ")
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
        existing_q = c.get("synthetic_questions", [])
        if len(existing_q) < 2:  # Claims sem perguntas ou com pouca cobertura
            generated_qs = infer_domain_questions(c)
            for q in generated_qs:
                if q not in existing_q:
                    candidate_pairs.append([q, c["claim"][:600]])
                    pair_metadata.append((c_idx, q))

    print(f"Total de novas perguntas candidatas para validação na GPU: {len(candidate_pairs)}")
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

    # Filtrar com logit >= 0.5 (alta coerência)
    approved = 0
    for (c_idx, q), score in zip(pair_metadata, scores):
        if score >= 0.5:
            c = claims[c_idx]
            if "synthetic_questions" not in c:
                c["synthetic_questions"] = []
            if q not in c["synthetic_questions"]:
                c["synthetic_questions"].append(q)
                approved += 1

    print(f"\nValidação concluída: {approved}/{len(candidate_pairs)} perguntas aprovadas pela GPU ({approved/len(candidate_pairs)*100:.1f}%)!")

    # Gravar claims
    with open(CLAIMS_FILE, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    total_with_q = sum(1 for c in claims if c.get("synthetic_questions"))
    total_q_count = sum(len(c.get("synthetic_questions", [])) for c in claims)
    print(f"Dataset de claims regravado com sucesso!")
    print(f"Cobertura total de claims com perguntas: {total_with_q}/{len(claims)} ({total_with_q/len(claims)*100:.1f}%)")
    print(f"Total de perguntas sintéticas consolidadas no dataset: {total_q_count}")

if __name__ == "__main__":
    main()
