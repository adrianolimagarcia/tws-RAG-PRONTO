# PRD — Expansão Sintética com Professor-Crítico (HWA SFT)

Status: **APROVADO para Fases 0–6** · Data: 2026-08-21

## Problema
O dataset SFT HWA já tem cobertura factual ampla (13.067 registros aprovados,
3.072 casos de avaliação), mas pode melhorar robustez diante de perguntas
reais: formulações informais, dúvidas de iniciantes, ambiguidades de
versão/plataforma, solicitações inseguras e cenários de troubleshooting.

## Objetivo
Criar um pipeline versionado de geração sintética supervisionada que produza
exemplos diversos e auditáveis, revisados por um professor-crítico e
promovidos somente quando passarem validações determinísticas e auditoria.

## Usuários/consumidores
- Modelo HWA treinado com QLoRA (Qwen2.5-1.5B-Instruct).
- Operadores e administradores HWA/TWS.
- Equipe responsável por evidência, avaliação e segurança do dataset.

## Escopo (Fases 0–6)
- Variantes adicionais de perguntas/respostas ancoradas em claims verified.
- Perfis: technical, beginner, cli_operation, troubleshooting,
  version_platform, false_premise, risk_confirmation, unknown_evidence.
- Ciclo professor → crítico (approve/revise/reject) → gates → revisão humana.
- Metadados de proveniência (synthetic_generation).
- Splits sem vazamento e manifestos baseline × tratamento.

## Fora do escopo (Fases 7–8)
- Treino QLoRA real (exige nova autorização).
- Escala para todos os claims restantes.
- Multi-turn (exige evolução de schema e treino).
- Alteração do tokenizer.
- Distilação por logits de modelo fechado.
- Provedores de modelo (local/external) — exigem autorização explícita.

## Requisitos funcionais
- REQ-SYN-001: simulação de perguntas por cenários.
- REQ-SYN-002: retenção factual (claim_id, versão, plataforma, termos frios).
- REQ-SYN-003: professor e crítico logicamente separados; crítico não promove.
- REQ-SYN-004: segurança (risco, recusa, sem segredos).
- REQ-SYN-005: promoção controlada (isolada em candidates/; não toca approved).
- REQ-SYN-006: avaliação comparativa baseline × tratamento.

## Critérios de aceitação (Fases 0–6)
- 100% dos registros passam schema, segurança, dedup e termos frios.
- 100% possuem claim verificado e metadados coerentes.
- 0 destrutivos/sensíveis promovidos sem revisão humana.
- Nenhum claim_family_id em mais de um split.
- Pipeline reproduzível por seed (42).

## Dependências
- data/evidence/claims.jsonl (verified, não hwa-lab-*).
- scripts/check_natural_batch.py (funções cold_terms/risk policy).
- data/sft/synthetic_scenarios.json (contrato).

## Riscos
- Viés do professor → crítico independente + gates + revisão humana.
- Vazamento de proveniência → splits por família.
- Custo de GPU → apenas na Fase 7 sob autorização.
