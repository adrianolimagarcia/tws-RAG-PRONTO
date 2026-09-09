#!/usr/bin/env python3
"""Destilação de Perguntas Sintéticas e Entidades Operacionais para o Dataset de Claims.
Absorve a capacidade do HyDE Reverso permanentemente nos dados para que motores BM25/FTS leves
alcancem alto Hit Rate sem precisar de inferência neural em runtime.
"""
import json, os, re

BASE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CLAIMS_FILE = os.path.join(BASE_DIR, "data/evidence/claims.jsonl")

def generate_questions_for_claim(claim_obj):
    text = claim_obj.get("claim", "")
    topic = claim_obj.get("topic", "")
    subtopic = claim_obj.get("subtopic", "")
    cid = claim_obj.get("claim_id", "")
    lower = text.lower()

    questions = []

    # 1. Códigos de Erro (AWS, AWK, EQQ, CWW, etc.)
    codes = re.findall(r"\b([A-Z]{3,6}[0-9]{3,5}[A-Z]?)\b", text)
    for c in set(codes):
        if len(c) >= 6:
            questions.append(f"Qual é o significado da mensagem de erro {c} no HWA?")
            questions.append(f"Como solucionar ou diagnosticar o erro {c} no HWA?")

    # 2. Utilitários e Comandos CLI
    cmds = []
    for tool in ["conman", "composer", "optman", "planman", "wappman", "twsinst", "serverinst", "wa_pull_info", "switchmgr", "switcheventprocessor"]:
        if tool in lower:
            cmds.append(tool)
    for cmd in set(cmds):
        questions.append(f"Como utilizar o utilitário {cmd} no HCL Workload Automation?")
        if subtopic and subtopic != topic:
            questions.append(f"Qual o comando no {cmd} para {subtopic}?")

    # 3. REST API V2 / Endpoints
    endpoints = re.findall(r"(/[a-zA-Z0-9_\-/]+(?:api|v2|twsd)[a-zA-Z0-9_\-/]*)", text)
    if "rest api" in lower or endpoints:
        questions.append(f"Qual o endpoint e método REST API V2 documentado para {subtopic or topic} no HWA?")

    # 4. Arquitetura e Componentes Essenciais
    if "symphony" in lower:
        questions.append("Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?")
    if "dynamic agent" in lower or "dynamic workload broker" in lower:
        questions.append(f"Como configurar ou solucionar problemas no dynamic agent ou broker para {subtopic}?")
    if "jnextplan" in lower or "resetplan" in lower:
        questions.append("Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?")
    if "sfinal" in lower or "esteira" in lower or "virada" in lower:
        questions.append("Como funciona a esteira FINAL de produção e o fluxo de virada diária?")

    # Limitar a no máximo 4 perguntas de maior sinal sem duplicatas
    unique_q = []
    for q in questions:
        if q not in unique_q:
            unique_q.append(q)
            if len(unique_q) >= 4:
                break
    return unique_q

def main():
    print("Iniciando destilação de perguntas sintéticas nas claims...")
    if not os.path.exists(CLAIMS_FILE):
        print(f"Erro: {CLAIMS_FILE} não encontrado.")
        return

    with open(CLAIMS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    enriched_lines = []
    total_questions = 0
    claims_with_q = 0

    for line in lines:
        if not line.strip():
            continue
        c = json.loads(line)
        sq = generate_questions_for_claim(c)
        c["synthetic_questions"] = sq
        if sq:
            claims_with_q += 1
            total_questions += len(sq)
        enriched_lines.append(json.dumps(c, ensure_ascii=False) + "\n")

    with open(CLAIMS_FILE, "w", encoding="utf-8") as f:
        f.writelines(enriched_lines)

    print(f"Concluído com sucesso!")
    print(f"Total de claims processadas: {len(enriched_lines)}")
    print(f"Claims enriquecidas com perguntas sintéticas: {claims_with_q}/{len(enriched_lines)} ({claims_with_q/len(enriched_lines)*100:.1f}%)")
    print(f"Total de perguntas sintéticas absorvidas no dataset: {total_questions}")

if __name__ == "__main__":
    main()
