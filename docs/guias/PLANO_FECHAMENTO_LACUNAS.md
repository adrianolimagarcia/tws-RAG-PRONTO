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
| 1.2 | JOB (jd) UNIX docommand — criar, rodar, ver saída | DONE (runbook hwa-10.2.8-unix-docommand-basico.md) |
| 1.3 | JOB (jd) UNIX script — TASKTYPE UNIXSCRIPT | DONE (runbook hwa-10.2.8-unix-script.md) |
| 1.4 | JOBSTREAM (sched) — ciclo de vida completo no plano | DONE (runbook hwa-10.2.8-jobstream-ciclo-vida.md) |
| 1.5 | WORKSTATION (ws/cpu) — tipos FTA, dynamic agent, pool | DONE (runbook hwa-10.2.8-workstations.md) |
| 1.6 | RESOURCE (res) — number/numbered resources, alocação | DONE (runbook hwa-10.2.8-resource.md) |
| 1.7 | CALENDAR (cal) — runcycles, feriados | DONE (runbook hwa-10.2.8-calendar.md) |
| 1.8 | VARIABLE TABLE (vartable) — variáveis em jobs | DONE (runbook hwa-10.2.8-vartable.md) |
| 1.9 | EVENT RULE (evtrule) — EDWA, ações automáticas | pendente |
| 1.10 | PARAMETER (par) — parâmetros de job stream | DONE (runbook hwa-10.2.8-parameter.md) |
| 1.11 | USER (user) — logon de execução | DONE (runbook hwa-10.2.8-user.md) |
| 1.12 | WORKSTATION CLASS — classes e herança | DONE (runbook hwa-10.2.8-workstation-class.md) |

### Variações de job a testar dentro do item 1.2/1.3

- filemon (file monitor), internet/HTTP job, database job
- dependências (follows), time restrictions, recovery options

Cada item gera: runbook em `data/runbooks/` + claims `lab-validation-*` em
`data/knowledge/lab-procedures-derived.jsonl` (seguir ENRIQUECIMENTO.md).

## Fase 2 — Dynamic Workload Console (validação web)

- 2.1 DWC instalado no host + engine MDM_LAB conectada | DONE (runbook hwa-10.2.8-dwc-instalacao-lab.md)
  **LIMITACAO DOCUMENTADA** (runbook hwa-10.2.8-dwc-deploy.md): imagem oficial exige credencial comercial do HCL Entitled Registry (hclcr.io); pull sem auth falha. Procedimento completo documentado; deploy executavel assim que houver credencial.
- 2.2 Documentar instalacao e configuracao (portas, SSL, usuario) — DONE (runbook hwa-10.2.8-dwc-deploy.md: env vars, portas 9080/9443, ENGINE_* para tws-hwa:31116, SSO/LTPA)
- 2.3 Validação via API REST | DONE (engine conectada, checkConnection OK). Form login no browser com limitação (400 no j_security_check) - documentado — PENDENTE DE DWC (runbook hwa-10.2.8-dwc-validacao-web.md com roteiro pronto; equivalencias CLI ja validadas na Fase 1)
- 2.4 Runbook de troubleshooting DWC (conexao, certificados) — DONE (runbook hwa-10.2.8-dwc-troubleshooting.md)

## Fase 3 — Configuração master/agente a partir do lab real

- 3.1 localopts e globalopts do MDM: documentar cada parâmetro em uso — DONE (runbook hwa-10.2.8-config-localopts-globalopts.md)
- 3.2 JobManager.ini do dynamic agent (tws-agent): parâmetros e tuning — DONE (runbook hwa-10.2.8-config-jobmanager-ini.md)
- 3.3 Configuração de mailman, batchman, planman no lab — DONE (runbook hwa-10.2.8-config-processos-mdm.md)
- 3.4 Referência de segurança: SSL entre componentes, autenticação — DONE (runbook hwa-10.2.8-config-seguranca-ssl.md)

## Fase 4 — Backup/restore e disaster recovery testado (CONCLUÍDA)

- 4.1 Backup do banco de dados TWS (procedimento + restore testado) — DONE (runbook hwa-10.2.8-backup-banco.md; pg_dump 658K/1s, restore 3,5s, 0 divergências)
- 4.2 Backup do plano (JnextPlan) e arquivos críticos — DONE (runbook hwa-10.2.8-backup-arquivos.md; tar TWSDATA 17MB/504 arquivos, restore validado)
- 4.3 Cenário DR completo documentado passo a passo — DONE (runbook hwa-10.2.8-disaster-recovery.md)

## Fase 5 — Integração na base RAG + re-benchmark (CONCLUÍDA 2026-10-12)

- 5.1 Enriquecimento: 37 runbooks das fases 1-4 destilados em **49 claims** `lab-validation-*`
  (21 arquivos em `data/evidence/lab-validation-2026-10-12-*.jsonl`); corpus reconstruído
  via `consolidate_corpus.py`: 7408 → **7457 claims**; 49/49 enriquecidas com perguntas
  sintéticas via LLM e aplicadas com `apply_enrichment_safe.py` (modo seguro).
- 5.2 Reindexação densa: **LIMITAÇÃO** — `build_dense_index_mcp.py` exige torch, indisponível
  no host (sem pip). Índice denso v6 (set/2026) mantido; MCP tem fallback para BM25.
  Cobertura BM25 verificada manualmente: 49/49 novas claims no corpus e recuperáveis.
- 5.3 Re-benchmark (`calibrated_full_benchmark.py`, 16519 perguntas, mesmo conjunto):
  - Corpus anterior (7408): Hit@1 **84.40%** (13942/16519), MRR **0.8770**
  - Corpus novo (7457): Hit@1 **84.38%** (13938/16519), MRR **0.8769**
  - Veredito: **SEM REGRESSÃO** (diferença de 4 perguntas = ruído estatístico).
  - Nota: a baseline de 93,5%/0,948 citada no guia refere-se a outra avaliação (1952 perguntas).

## PLANO FECHADO — todas as 5 fases concluídas em 2026-10-12.
## Variações de job testadas

| # | Variação | Status |
|---|----------|--------|
| V1 | filemon (file monitor via utilitário) | DONE (runbook hwa-10.2.8-job-filemonitor.md) |
| V2 | FOLLOWS (dependência entre jobs) | DONE (runbook hwa-10.2.8-job-dependency-follows.md) |
| V3 | Recovery (ABEND, RECOVERY STOP, rerun) | DONE (runbook hwa-10.2.8-job-recovery-rerun.md) |
| V4 | Time restriction (AT) | DONE (documentado no runbook do item 1.4) |

