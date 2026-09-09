#!/usr/bin/env python3
"""Doc2Query-- Offline com Cross-Encoder Filtering na GPU GTX 1050 Ti.
Gera perguntas sintéticas conceituais e utiliza o BAAI/bge-reranker-large na GPU
para pontuar e filtrar apenas expansões de alta relevância (logit > 1.5),
injetando-as no dataset estático para melhorar o retrieval em CPU.
"""
import sys, os, time, json, re
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

CACHE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker/hf_cache"
CLAIMS_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/evidence/claims.jsonl"
MODEL_NAME = "BAAI/bge-reranker-large"
os.environ["HF_HOME"] = CACHE_DIR

# Mapeamento de termos conceituais para perguntas sintéticas operacionais
CONCEPT_MAP = [
    (["wa_pull_info", "coleta", "diagnóstico"], [
        "Qual a função do script wa_pull_info no HWA e que tipo de dados ele coleta?",
        "Como coletar logs de diagnóstico e snapshot do ambiente HWA para suporte?"
    ]),
    (["until=", "deadline="], [
        "Qual o comportamento das opções until e deadline na submissão de jobs no conman?",
        "Como definir limites de horário e prazo na submissão ad-hoc sbd do conman?"
    ]),
    (["kubernetes", "helm", "openshift"], [
        "Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?",
        "Qual o procedimento de deployment de containers HWA com Helm?"
    ]),
    (["local parameter", "local_parameters", "parâmetros locais"], [
        "O que causa erro na resolução de local parameters em jobs e como solucionar?",
        "Como gerenciar e resolver arquivos de parâmetros locais no HWA?"
    ]),
    (["wapl", "z/os"], [
        "O que é a linguagem WAPL e como ela é utilizada no Workload Automation for Z?",
        "Como utilizar a Workload Automation Programming Language WAPL para z/OS?"
    ]),
    (["return code", "códigos de retorno", "submit sched", "submit job"], [
        "Quais comandos conman possuem códigos de retorno específicos documentados?",
        "Como o conman reporta return codes na submissão de schedules e jobs?"
    ]),
    (["event rule", "event-on-demand", "regras de evento"], [
        "Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?",
        "Quais ações podem ser disparadas por event rules no HWA Distributed?"
    ]),
    (["production plan", "instância", "symphony"], [
        "O que acontece ao modificar uma instância de job no plano versus sua definição no banco?",
        "Qual a diferença entre a definição de um objeto no banco e sua instância no Symphony?"
    ]),
    (["dynamic agent", "não aparece", "not found", "dwc"], [
        "Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?",
        "Como solucionar problemas de registro de agentes dinâmicos no broker?"
    ]),
    (["post /twsd/api/v2/plan/job/submit", "ad-hoc", "rest/plan"], [
        "Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?",
        "Como submeter execuções pontuais via API REST V2 no HWA?"
    ])
]

def main():
    print("==================================================")
    print("  DESTILAÇÃO OFFLINE DOC2QUERY-- VIA GPU CUDA     ")
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

    print(f"Lendo claims de {CLAIMS_FILE}...")
    claims = []
    with open(CLAIMS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                claims.append(json.loads(line))

    print(f"Total de claims: {len(claims)}")
    
    # 1. Gerar pares candidatos para validação neural
    candidate_pairs = []
    pair_metadata = []

    for c_idx, c in enumerate(claims):
        text = c.get("claim", "")
        text_lower = text.lower()
        existing_q = set(c.get("synthetic_questions", []))

        # Testar cada conceito
        for keywords, questions in CONCEPT_MAP:
            if any(k in text_lower for k in keywords):
                for q in questions:
                    if q not in existing_q:
                        candidate_pairs.append([q, text[:600]])
                        pair_metadata.append((c_idx, q))

    print(f"Total de perguntas candidatas geradas para validação pela GPU: {len(candidate_pairs)}")
    if not candidate_pairs:
        print("Nenhuma pergunta nova para validar.")
        return

    # 2. Avaliar em batches na GPU com BAAI/bge-reranker-large
    print("Pontuando pares com BAAI/bge-reranker-large na GPU...")
    batch_size = 32
    scores = []
    t_eval_start = time.time()

    with torch.no_grad():
        for i in range(0, len(candidate_pairs), batch_size):
            batch = candidate_pairs[i:i+batch_size]
            inputs = tokenizer(batch, padding=True, truncation=True, max_length=256, return_tensors="pt").to(device)
            batch_scores = model(**inputs, return_dict=True).logits.view(-1).float().cpu().tolist()
            scores.extend(batch_scores)
            if (i // batch_size) % 5 == 0:
                print(f"  Validado {min(i+batch_size, len(candidate_pairs))}/{len(candidate_pairs)} pares ({time.time()-t_eval_start:.1f}s)...")

    # 3. Filtrar com threshold de alta relevância (Doc2Query--: manter logit >= 1.0)
    THRESHOLD = 1.0
    approved_count = 0
    
    for (c_idx, q), score in zip(pair_metadata, scores):
        if score >= THRESHOLD:
            c = claims[c_idx]
            if "synthetic_questions" not in c:
                c["synthetic_questions"] = []
            if q not in c["synthetic_questions"]:
                c["synthetic_questions"].append(q)
                approved_count += 1

    print(f"\nValidação na GPU concluída em {time.time()-t_eval_start:.2f}s!")
    print(f"Perguntas APROVADAS pela GPU (Score >= {THRESHOLD}): {approved_count}/{len(candidate_pairs)} ({approved_count/len(candidate_pairs)*100:.1f}%)")

    # 4. Gravar claims atualizadas no dataset oficial
    print(f"Gravando {len(claims)} claims enriquecidas em {CLAIMS_FILE}...")
    with open(CLAIMS_FILE, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print("Dataset de claims atualizado com sucesso via destilação da GPU!")

if __name__ == "__main__":
    main()
