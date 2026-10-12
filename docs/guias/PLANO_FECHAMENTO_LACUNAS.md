# Plano de Fechamento de Lacunas — TWS

Criado em 2026-10-12. Objetivo: tornar o material sobre HCL Workload Automation 10.2.8
completo e validado em lab, cobrindo as 4 lacunas identificadas na avaliação.

## Fase 1 — Catálogo de job types testado no lab (EM ANDAMENTO)

Testar cada tipo de job no lab (tws-hwa/tws-bmdm/tws-agent) e documentar com
evidência real: definição, execução, saída e troubleshooting.

| # | Job type | Status |
|---|----------|--------|
| 1.1 | PROMPT (job com aprovação de operador) | ✅ documentado (runbook hwa-10.2.8-prompt-job-lifecycle.md) |
| 1.2 | UNIX docommand básico | pendente |
| 1.3 | UNIX script (TASKTYPE UNIXSCRIPT) | pendente |
| 1.4 | Variable table (vartable) | pendente |
| 1.5 | File monitor (filemon) | pendente |
| 1.6 | Internet / HTTP job | pendente |
| 1.7 | Database job | pendente |
| 1.8 | Dependências entre jobs (follows) | pendente |
| 1.9 | Time restrictions | pendente |
| 1.10 | Recovery options (rerun/stop/continue) | pendente |

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
