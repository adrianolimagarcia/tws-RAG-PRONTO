# Avaliação do Experimento Sintético (Teacher-Critic)

Status: **AUDITORIA INDEPENDENTE CONCLUÍDA; TREINO NÃO EXECUTADO** — o
tratamento está pronto para experimento controlado, mas ainda não foi promovido
ao dataset aprovado.

## Objetivo

Medir, com evidência, se o dataset sintético gerado pelo pipeline
teacher-critic melhora o modelo QLoRA sem degradar segurança ou aderência
factual.

## Hipótese

O tratamento (baseline + candidatos sintéticos aprovados) melhora:
1. robustez a formulações variadas (beginner, cli_operation, false_premise);
2. qualificação de escopo de versão/plataforma (version_platform);
3. recusa/confirmação para ações de risco (risk_confirmation);
4. resposta de evidência insuficiente (unknown_evidence).

Sem degradar:
- exatidão factual (eval factual existente);
- política de segurança (destructive/credential_sensitive).

## Protocolo

### 1. Preparação (feita nas Fases 0–6)

- Baseline: `data/sft/approved.jsonl` (13.067 registros).
- Tratamento final: baseline + 1.068 candidatos sintéticos aprovados pelo crítico.
- Auditoria linguística: 1.068/1.068 registros verificados; 0 suspeitas finais.
- Tradução: 535 registros processados externamente e 9 correções técnicas locais.
- Splits sem vazamento: `data/sft/experiments/baseline_splits/` e
  `data/sft/experiments/treatment_splits/` (famílias inteiras no mesmo corte).
- Manifests: `pipeline_baseline_manifest.json`, `baseline_manifest.json`,
  `treatment_manifest.json`.
- Auditoria final: `data/sft/experiments/synthetic_teacher_language_audit_final.json`.
- Resultado independente: aceitável para experimento controlado, com ressalvas
  de qualidade do corpus geral e sem prontidão para produção.

### 2. Treino (Fase 7 — bloqueado até nova autorização)

- Mesmos hiperparâmetros para ambos: `config.yaml` sft.
- Modelo base: `Qwen/Qwen2.5-1.5B-Instruct`.
- Dois runs isolados: `output/sft-baseline` e `output/sft-treatment`.
- Executar primeiro `python scripts/train_sft.py --dry-run`.

### 3. Avaliação (pós-treino)

| Critério | Fonte | Decisão de aceite |
|---|---|---|
| Factualidade | `eval_independent.jsonl` (3.072 casos) | tratamento >= baseline |
| Adversarial/segurança | casos adversarial do eval | sem regressão |
| Termos frios | gate sintético + auditoria | 100% |
| Escopo versão/plataforma | auditoria de metadados | sem regressão |
| Segurança (destructive/credential) | política de risco | sem regressão |
| Inadequação em novos prompts | avaliação manual cega | tratamento <= baseline |

### 4. Go / No-Go

Promover os sintéticos ao `approved.jsonl` apenas se TODOS os critérios de
aceite acima forem atendidos, seguindo o padrão atômico de integração
(`integrate_natural_golden.py`).

## Artefatos

- `data/sft/experiments/pipeline_baseline_manifest.json` — hashes/counts base.
- `data/sft/experiments/baseline_manifest.json` — splits baseline.
- `data/sft/experiments/treatment_manifest.json` — splits tratamento.
- `data/sft/experiments/synthetic_teacher_critic_report.json` — decisões do crítico.
- `data/sft/experiments/synthetic_teacher_human_review.json` — plano de revisão humana.
- `data/sft/experiments/synthetic_teacher_post_review_report.json` — decisões da
  revisão assistida e impacto no tratamento.
- `data/sft/candidates/synthetic_teacher_critic.jsonl` — candidatos aprovados.
- `data/sft/candidates/synthetic_teacher_treatment.jsonl` — candidatos após a
  exclusão temporária dos 44 itens que exigem regeneração.
- `data/sft/candidates/synthetic_teacher_language_final2.jsonl` — tratamento
  linguístico final validado.

## Riscos e mitigação

- Melhoria aparente por vazamento: mitiga por splits por família + prompts
  inéditos + revisão manual cega.
- Viés do professor: crítico + gates + revisão humana obrigatória para
  destructive/credential_sensitive e amostras para mutating/read_only.
- Custo de GPU: runs isolados, piloto pequeno, dry-run antes.
