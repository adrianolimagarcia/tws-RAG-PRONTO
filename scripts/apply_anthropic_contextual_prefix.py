#!/usr/bin/env python3
"""Aplica o padrão Anthropic Contextual Retrieval nas claims do HWA:
Prefixa em cada documento um bloco conciso de 40-70 tokens contextualizando:
[Contexto: Produto > Versão > Componente > Interface/Ferramenta > Modo de Operação]
Isso elimina o 'Context Collapse' e permite que o primeiro estágio (BM25/Dense)
discrimine o escopo com precisão máxima sem perder a especificidade do fato.
"""
import json, os, re

BASE_DIR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CLAIMS_FILE = os.path.join(BASE_DIR, "data/evidence/claims.jsonl")

def build_context_prefix(claim_obj):
    product = claim_obj.get("product", "HCL Workload Automation")
    version = claim_obj.get("version_scope") or claim_obj.get("version") or "10.2.8"
    platform = claim_obj.get("platform_scope") or claim_obj.get("platform") or "Distributed"
    topic = claim_obj.get("topic", "geral")
    subtopic = claim_obj.get("subtopic", "")
    capability = claim_obj.get("capability", "")
    term_dict = claim_obj.get("normalized_terminology") or {}
    
    # Identificar componente primário
    component = "Master Domain Manager (MDM)"
    lower_text = (claim_obj.get("claim", "") + " " + claim_obj.get("claim_id", "")).lower()
    if "dwc" in lower_text or "console" in lower_text:
        component = "Dynamic Workload Console (DWC)"
    elif "dynamic agent" in lower_text or "dynagent" in lower_text or "broker" in lower_text:
        component = "Dynamic Workload Broker / Dynamic Agent"
    elif "fta" in lower_text or "fault-tolerant" in lower_text:
        component = "Fault-Tolerant Agent (FTA)"
    elif "bmdm" in lower_text or "backup master" in lower_text:
        component = "Backup Master Domain Manager (BMDM)"
    elif "aida" in lower_text or "ai data advisor" in lower_text:
        component = "AI Data Advisor (AIDA)"
    elif "database" in lower_text or "postgresql" in lower_text or "dbviews" in lower_text or "view" in lower_text:
        component = "Relational Database (PostgreSQL / DB2 / Oracle)"
    elif "z/os" in lower_text or "zos" in lower_text or "ispf" in lower_text:
        component = "Workload Automation for Z (z/OS Engine)"

    # Identificar interface de operação
    interface = "Geral"
    if "conman" in lower_text:
        interface = "CLI conman (Monitoramento e Plano)"
    elif "composer" in lower_text:
        interface = "CLI composer (Definições de Banco e Modelagem)"
    elif "optman" in lower_text or "globalopts" in lower_text:
        interface = "CLI optman (Opções Globais do Master)"
    elif "planman" in lower_text or "symphony" in lower_text or "jnextplan" in lower_text or "resetplan" in lower_text:
        interface = "CLI planman / Scripts de Plano (Symphony)"
    elif "rest" in lower_text or "api" in lower_text:
        interface = "REST API V2 (HTTPS Port 31116)"
    elif "twsinst" in lower_text or "serverinst" in lower_text or "install" in lower_text:
        interface = "Instalação / Utilitários de Setup"

    sub_info = f" > {subtopic}" if subtopic and subtopic != topic else ""
    cap_info = f" [{capability}]" if capability else ""
    prefix = f"[Escopo: {product} {version} ({platform}) > Componente: {component} > Interface: {interface} > Tópico: {topic}{sub_info}{cap_info}]"
    return prefix

def main():
    print(f"Lendo claims de {CLAIMS_FILE}...")
    if not os.path.exists(CLAIMS_FILE):
        print("Erro: Arquivo de claims não encontrado.")
        return

    with open(CLAIMS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    applied_count = 0

    for line in lines:
        if not line.strip():
            continue
        c = json.loads(line)
        prefix = build_context_prefix(c)
        c["context_prefix"] = prefix
        applied_count += 1
        updated_lines.append(json.dumps(c, ensure_ascii=False) + "\n")

    with open(CLAIMS_FILE, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print(f"Contextual Retrieval Prefix aplicado com sucesso em {applied_count} claims!")
    print(f"Exemplo de prefixo gerado:\n  {json.loads(updated_lines[0])['context_prefix']}")

if __name__ == "__main__":
    main()
