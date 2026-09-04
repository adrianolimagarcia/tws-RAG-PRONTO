---
title: Índice do conhecimento — HWA/TWS
type: index
tags:
  - vault
  - indice
  - moc
updated: 2026-08-24
---

# Índice do conhecimento — HWA/TWS

> [!info] Este repositório é um vault Obsidian
> A raiz do projeto é o vault. Nenhum arquivo é duplicado: o vault adiciona **navegação e notas de conhecimento** sobre os arquivos canônicos. Fontes de verdade: código em `scripts/`, documentação normativa em `README.md` + `docs/`, evidências em `data/evidence/`, manuais em `MANUAIS/`.
>
> **Para agentes:** leia este índice primeiro e depois os arquivos canônicos. O acesso primário é via **sistema de arquivos** (grep/read/glob) — funciona sempre, sem dependências. O `obsidian` CLI (no WSL) pode consultar o vault quando o Obsidian está aberto com o toggle "Command line interface" ativado (Settings > General > Advanced). O wrapper `~/.local/bin/obsidian-headless` + Xvfb permite usar o CLI sem janela gráfica. O pacote `ob` (obsidian-headless npm) é somente para Sync/Publish, não para busca/leitura do vault.

## Notas do vault

- [Mapa do domínio HWA/TWS](hwa-dominio.md)

## Documentação normativa (`docs/`)

- [PRD — Release SOTA](../PRD_SOTA_RELEASE.md)
- [SPEC — Release SOTA](../SPEC_SOTA_RELEASE.md)
- [PLAN — Release SOTA](../PLAN_SOTA_RELEASE.md)
- [DECISIONS — Release SOTA](../DECISIONS_SOTA_RELEASE.md)
- [Contrato RAG evidence-first](../RAG_EVIDENCE_CONTRACT.md)
- [Formato de lab sessions](../LAB_SESSION_FORMAT.md)
- [Guia de treino](../TRAINING_GUIDE.md)
- [Roadmap de qualidade do dataset](../dataset-quality-roadmap.md)
- [Progresso](../PROGRESS.md)
- [Synthetic teacher: PRD](../PRD_SYNTHETIC_TEACHER.md) · [SPEC](../SPEC_SYNTHETIC_TEACHER.md) · [EVALS](../EVALS_SYNTHETIC_TEACHER.md)
- [Execução r16](../r16-execution-plan.md) · [próximos passos r16](../r16-next-steps.md) · [auditoria r17 (EN)](../r17-en-audit.md)
- [Fix plugin opencode-antigravity-auth](../opencode-antigravity-plugin-fix.md)

## Runbooks (`data/runbooks/`)

- [HWA 10.2.8 — lab no WSL](../../data/runbooks/hwa-10.2.8-wsl-lab.md)
- [Failover MDM/FTA](../../data/runbooks/failover-mdm-fta.md)
- [Recuperação de JnextPlan](../../data/runbooks/recovery-jnextplan.md)
- [Upgrade de agente](../../data/runbooks/upgrade-agente.md)
- [Upgrade 9.5 → 10.2.3](../../data/runbooks/upgrade-9.5-para-10.2.3.md)
- [Validação e correção sfinal](../../data/runbooks/sfinal-validate-and-correct.md)

## Evidências (`data/evidence/`)

- [Registro de claims (canônico)](../../data/evidence/README.md)
- [Catálogo de comandos](../../data/evidence/command-catalog.md)
- [Matriz de pesquisa](../../data/evidence/research-matrix.md)
- [Política de validação de não-oficiais](../../data/evidence/unofficial-validation-policy.md)
- [Auditoria de materiais não-oficiais](../../data/evidence/unofficial-materials-audit.md)
- [Backlog multiversão](../../data/evidence/multiversion-research-backlog.md)
- [Política de segurança em automação](../../data/evidence/automation-safety-policy.md)
- [Resultados de pesquisa (rodada 2)](../../data/evidence/research-results-round-2.md)
- [Revisão de pontos em aberto](../../data/evidence/open-points-review.md)

## Manuais (`MANUAIS/`)

- [Acervo HWA/TWS (proveniência e versões)](../../MANUAIS/README.md)

## Fonte de dados do treino (`data/`)

- [Documentos-fonte em `data/raw/`](../../data/raw/) — REST API WA, conhecimento TWS, etc.
- [Corpus e splits na raiz de `data/`](../../data/) — `corpus.jsonl`, `train_full.jsonl`, `eval.jsonl`, `quarantine.jsonl`
