# Plano de Fechamento de Lacunas — TWS

Criado em 2026-10-12. Objetivo: tornar o material sobre HCL Workload Automation 10.2.8
completo e validado em lab, cobrindo as 4 lacunas identificadas na avaliação.

## Fase 1 — Catálogo de OBJETOS TWS testado no lab, um a um (EM ANDAMENTO)

Cobrir todos os tipos de objeto do banco de dados TWS (composer), testando cada um
no lab (tws-hwa/tws-bmdm/tws-agent): criar, executar/consultar, documentar com
evidência real e troubleshooting.

### Objetos de definição (composer)

| # | Objeto | Status |
|---|--------|--------|
| 1.1 | PROMPT (prom) — ciclo de vida, STUCK, limpeza | ✅ documentado (runbook hwa-10.2.8-prompt-job-lifecycle.md) |
| 1.2 | JOB (jd) UNIX docommand — criar, rodar, ver saída | pendente |
| 1.3 | JOB (jd) UNIX script — TASKTYPE UNIXSCRIPT | pendente |
| 1.4 | JOBSTREAM (sched) — ciclo de vida completo no plano | pendente |
| 1.5 | WORKSTATION (ws/cpu) — tipos FTA, dynamic agent, pool | pendente |
| 1.6 | RESOURCE (res) — number/numbered resources, alocação | pendente |
| 1.7 | CALENDAR (cal) — runcycles, feriados | pendente |
| 1.8 | VARIABLE TABLE (vartable) — variáveis em jobs | pendente |
| 1.9 | EVENT RULE (evtrule) — EDWA, ações automáticas | pendente |
| 1.10 | PARAMETER (par) — parâmetros de job stream | pendente |
| 1.11 | USER (user) — logon de execução | pendente |
| 1.12 | WORKSTATION CLASS — classes e herança | pendente |

### Variações de job a testar dentro do item 1.2/1.3

- filemon (file monitor), internet/HTTP job, database job
- dependências (follows), time restrictions, recovery options

Cada item gera: runbook em `data/runbooks/` + claims `lab-validation-*` em
`data/knowledge/lab-procedures-derived.jsonl` (seguir ENRIQUECIMENTO.md).

## Fase 2 — Dynamic Workload Console (validação web)

- 2.1 Subir container DWC no lab e conectar ao MDM
- 2.2 Documentar instalação e configuração (portas, SSL, usuário)
- 2.3 Validar via browser: monitorar plano, submeter job ad-hoc, responder prompt
- 2.4 Runbook de troubleshooting DWC (conexão, certificados)

## Fase 3 — Configuração master/agente a partir do lab real

- 3.1 localopts e globalopts do MDM: documentar cada parâmetro em uso
- 3.2 JobManager.ini do dynamic agent (tws-agent): parâmetros e tuning
- 3.3 Configuração de mailman, batchman, planman no lab
- 3.4 Referência de segurança: SSL entre componentes, autenticação

## Fase 4 — Backup/restore e disaster recovery testado

- 4.1 Backup do banco de dados TWS (procedimento + restore testado)
- 4.2 Backup do plano (JnextPlan) e recovery
- 4.3 Cenário DR completo documentado passo a passo

## Fase 5 — Integração na base RAG + re-benchmark

- 5.1 Aplicar enriquecimento (apply_enrichment_safe.py)
- 5.2 Reindexar (build_dense_index_mcp.py)
- 5.3 Re-benchmark (calibrated_full_benchmark.py) vs baseline 93,5% / 0,948
