# HCL Workload Automation 10.2.8 (Distributed) — SOTA RAG Dataset & Knowledge Base
> **Versão:** `v1.0.0-gold`  
> **Status:** Concluído, Validado em Lab Físico/Containerizado e Auditado por CI Gates.  
> **Plataforma Canônica:** RHEL 9 (UBI9), HWA 10.2.8.00, Liberty engineServer, PostgreSQL, FTA clássico e Dynamic Agent.

---

## Resumo Executivo da Linha de Base

Este repositório contém a mais abrangente base de conhecimento empírica, estruturada e canonizada sobre o **HCL Workload Automation (TWS/HWA) 10.2.8**. Construída com rigor de engenharia (HAOS SOTA), cada afirmação técnica foi validada contra o comportamento de runtime real de um cluster distribuído com 3 containers:
- **`tws-hwa`**: Master Domain Manager (MDM), Dynamic Workload Broker, Liberty engineServer, Open DWC.
- **`tws-bmdm`**: Backup Master Domain Manager (BMDM) com replicação ativa de Symphony e banco compartilhado.
- **`tws-agent`**: Agente híbrido isolado em rede contendo Fault-Tolerant Agent (`AGT1`) e Dynamic Agent (`TWS-AGENT_1`).

---

## Métricas & Resultados do Full Benchmark (3.180 Perguntas)

Avaliamos o corpus em escala total (3.180 perguntas de teste cego mapeadas contra 2.548 documentos únicos) utilizando o motor BM25 otimizado:

| Métrica | Resultado Geral |
| :--- | :--- |
| **Total de Perguntas Avaliadas** | **3.180 perguntas** |
| **Tempo de Execução** | **19.14 segundos** (166.1 consultas/segundo) |
| **Hit Rate @ 1** | **57.58%** (1.831 / 3.180) |
| **Hit Rate @ 5** | **67.36%** (2.142 / 3.180) |
| **Hit Rate @ 10** | **70.85%** (2.253 / 3.180) |
| **Mean Reciprocal Rank (MRR)** | **0.6181** |

### Destaques por Especialidade:
- **Troubleshooting & Mensagens de Erro (AWS***)**: **97.8% Hit@1 \| 98.7% Hit@5 \| MRR 0.9820**
- **Agendamento Avançado & Workflows (NEEDS, RECOVERY)**: **78.6% Hit@1 \| 91.0% Hit@5 \| MRR 0.8299**
- **Instalação & Manutenção**: **67.3% Hit@1 \| 82.2% Hit@5 \| MRR 0.7332**

---

## Estrutura de Artefatos para Consumo

### 1. Servidor MCP para Agentes de IA (Hermes, Claude Code, OpenCode)
Localizado em `mcp_server/tws_expert_mcp.py`. Permite consulta nativa stdio JSON-RPC:
```bash
# Execução direta:
python3 mcp_server/tws_expert_mcp.py

# Ferramentas expostas:
# - tws_expert_search(query, category, top_k)
# - tws_get_claim(claim_id)
# - tws_list_categories()
```

### 2. Formato LLM / NotebookLM / Perplexity Spaces / ChatGPT
Documentos limpos em Markdown de alta densidade sem chaves JSON em `data/export/llm_knowledge_bases/`:
- `tws_hwa_10.2.8_knowledge_book_complete.md` (1.83 MB — Livro completo consolidado para upload em NotebookLM)
- `01_alta_disponibilidade_failover.md`
- `02_arquitetura_topologia_mesh.md`
- `03_operacao_cli_conman_composer_planman.md`
- `04_agendamento_avancado_workflows.md`
- `05_api_rest_v2_integracao.md`
- `06_troubleshooting_mensagens_aws.md`
- `07_instalacao_manutencao.md`

### 3. Dados Mestres para Treinamento e RAG Corporativo
Em `data/export/`:
- `tws_corpus_master_consolidated.jsonl`: 2.548 claims únicas desduplicadas e indexadas.
- `tws_eval_ground_truth.jsonl`: 3.180 pares de pergunta-claim para avaliação contínua.
- `tws_taxonomy_audit_report.json`: Distribuição analítica por tema.

---

## Gerenciamento do Laboratório Local (CachyOS Host)

Para economizar recursos de hardware (RAM/CPU) quando o lab não estiver sob teste:
```bash
# Pausar lab (libera ~6-8 GB de memória RAM):
docker stop tws-hwa tws-bmdm tws-agent

# Retomar lab:
docker start tws-hwa tws-bmdm tws-agent

# Monitorar saúde:
docker exec tws-hwa su - wauser -c "conman 'sc @'"
```

---
*Compilado e homologado via HAOS SOTA Pipeline — 2026.*
