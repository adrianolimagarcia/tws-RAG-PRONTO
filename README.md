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

## Métricas & Resultados do Benchmark Canônico Multi-Label (1.952 Perguntas Únicas)

Avaliamos o corpus em escala total (1.952 perguntas cegas únicas sem viés de colisão, cobrindo as 2.548 claims canônicas) utilizando o pipeline de Information Retrieval de dois estágios (BM25 Calibrado + Reranker de N-Grams e Cobertura Semântica):

| Métrica | Resultado Geral |
| :--- | :--- |
| **Total de Perguntas Únicas Avaliadas** | **1.952 perguntas** |
| **Tempo de Execução** | **7.75 segundos** (251.8 consultas/segundo) |
| **Hit Rate @ 1** | **93.49%** (1.825 / 1.952) |
| **Hit Rate @ 3** | **95.65%** (1.867 / 1.952) |
| **Hit Rate @ 5** | **96.47%** (1.883 / 1.952) |
| **Hit Rate @ 10** | **97.44%** (1.902 / 1.952) |
| **Mean Reciprocal Rank (MRR)** | **0.9480** |

### Destaques por Especialidade:
- **Alta Disponibilidade & Failover**: **100.0% Hit@1 \| 100.0% Hit@5 \| MRR 1.0000** (15 q)
- **Troubleshooting & Mensagens de Erro (AWS***)**: **99.9% Hit@1 \| 99.9% Hit@5 \| MRR 0.9985** (664 q)
- **Agendamento Avançado & Workflows (NEEDS, RECOVERY)**: **96.0% Hit@1 \| 97.3% Hit@5 \| MRR 0.9640** (74 q)
- **Instalação & Manutenção**: **90.7% Hit@1 \| 96.0% Hit@5 \| MRR 0.9356** (75 q)
- **Operação CLI (conman/composer/planman)**: **88.8% Hit@1 \| 92.9% Hit@5 \| MRR 0.9056** (392 q)
- **API REST v2 & Integração**: **83.3% Hit@1 \| 92.7% Hit@5 \| MRR 0.8641** (150 q)

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
Documentos Markdown de alta densidade em `data/export/llm_knowledge_bases/`.

**Versão v2 — completa (recomendada):**
- `tws_hwa_10.2.8_knowledge_book_v2_complete.md` — **5,3 MB / ~809 mil palavras**: livro único com todos os campos, ressalvas de uso, níveis de evidência e os 14 runbooks operacionais integrados. Para ChatGPT/Claude Projects.
- `parts_v2/` — **24 arquivos temáticos**, todos abaixo do limite de 500k palavras por fonte do NotebookLM (use estes para o NotebookLM).
- `README_CONSUMO.md` — guia de qual artefato usar em cada ferramenta e a regra anti-contaminação (fato oficial x prática de comunidade).
- `BOOK_V2_MANIFEST.json` — manifesto com contagem por categoria, runbooks e tamanhos.

**Versão v1 — digest de claims (mantida para compatibilidade):**
- `tws_hwa_10.2.8_knowledge_book_complete.md` — 1,9 MB, apenas 5 campos por registro e sem runbooks.
- `01_alta_disponibilidade_failover.md` … `08_procedimentos_e_referencias_adicionais.md`

### 3. Dados Mestres para Treinamento e RAG Corporativo
Em `data/export/`:
- `tws_corpus_master_consolidated.jsonl`: 2.548 claims únicas desduplicadas e indexadas.
- `tws_eval_ground_truth_multilabel.jsonl`: 1.952 perguntas canônicas com listas de relevância multi-label.
- `multilabel_benchmark_report.json`: Relatório analítico completo do benchmark.
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
