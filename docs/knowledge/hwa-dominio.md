---
title: Mapa do domínio HWA/TWS
type: knowledge
tags:
  - hwa
  - iws
  - tws
  - dominio
status: maintained
updated: 2026-08-24
---

# Mapa do domínio HWA/TWS

> [!note] Natureza desta nota
> Nota de **navegação**: descreve a estrutura do domínio e aponta onde cada assunto é tratado. **Não é fonte de fatos** — para afirmações verificadas, consulte `data/evidence/claims.jsonl` ([registro de claims](../../data/evidence/README.md)).

## O que é

**HCL Workload Automation (HWA)** é o produto de automação de cargas de trabalho, anteriormente **IBM Workload Scheduler (IWS)** e **Tivoli Workload Scheduler (TWS)**. A linhagem e as versões estão documentadas no [acervo de manuais](../../MANUAIS/README.md).

## Linha de versões presente no acervo

| Versão | Produto | Onde |
| --- | --- | --- |
| 8.5.1.1 | TWS (IBM) | `MANUAIS/PDF-IBM-TWS-8.5.1/` |
| 9.5 | IWS/HWA (IBM/HCL) | `MANUAIS/PDF-IBM-IWS-9.5/`, `MANUAIS/HCL-HWA-9.5-FP7/` |
| 10.2 | HWA | `MANUAIS/PDF-IBM-HWA-10.2/` |
| 10.2.2 | HWA | `MANUAIS/HCL-HWA-10.2.2/`, `MANUAIS/PDF-IBM-HWA-10.2/` |
| 10.2.8 | HWA (HCL) | `MANUAIS/PDF-HCL-HWA-10.2.8/`, runbook [HWA 10.2.8 — lab WSL](../../data/runbooks/hwa-10.2.8-wsl-lab.md) |

## Componentes e interfaces

- **CLI de agendamento** — linguagem e utilitários nos manuais de referência (ex.: PDF `awsrgmst-*`); ver [catálogo de comandos](../../data/evidence/command-catalog.md).
- **REST API (WA API)** — fonte local: [WA_API3_v2_REST_API.md](../../data/raw/WA_API3_v2_REST_API.md).
- **Dynamic Workload Console (DWC)** — GUI; manuais `tswebmst-*`.
- **Planejamento (JnextPlan)** — runbook [recuperação de JnextPlan](../../data/runbooks/recovery-jnextplan.md).
- **Agentes e failover (FTA/MDM)** — runbook [failover MDM/FTA](../../data/runbooks/failover-mdm-fta.md).
- **Códigos de mensagem** — famílias `AWS*`, `EQQ*`, `EEL*`; consultar o manual de mensagens da versão (ex.: `awsmsmst-10.2.2.pdf`). Não generalizar entre versões.

## Pipelines do projeto

- Corpus causal + RAG: [README](../../README.md) e [roadmap de qualidade](../dataset-quality-roadmap.md).
- Release SOTA (P0–P6): [PLAN](../PLAN_SOTA_RELEASE.md) · [SPEC](../SPEC_SOTA_RELEASE.md) · [DECISIONS](../DECISIONS_SOTA_RELEASE.md).

## Regras de domínio

- **Não misturar versões**: comportamento de uma versão não comprova outra ([backlog multiversão](../../data/evidence/multiversion-research-backlog.md)).
- **Somente evidência verificada** sustenta SFT ([registro de claims](../../data/evidence/README.md)); materiais não-oficiais passam por [política própria](../../data/evidence/unofficial-validation-policy.md).
- **Segurança**: nunca executar comandos gerados pelo modelo sem validação ([política de automação](../../data/evidence/automation-safety-policy.md)).
