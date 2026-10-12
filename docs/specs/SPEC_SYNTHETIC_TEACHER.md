# Spec — Pipeline de Expansão Sintética com Professor-Crítico

Status: **IMPLEMENTADO (Fases 0–6) + EXPANSÃO v2** · Pipeline version: teacher-critic-v1 + v2-expansion

## Arquitetura

```text
claims verified (claims.jsonl)
      │
      ▼
[generate_synthetic_teacher_candidates.py]  ── TeacherProvider (offline)
      │  saída: candidates/synthetic_teacher_pilot.jsonl  (review_status=candidate)
      ▼
[generate_synthetic_expansion.py]  ── TeacherProviderV2 (offline-v2)
      │  cobre claims restantes com novos cenários (clarification, comparison,
      │  hard_negative, edge_case, multi_turn) + gate Jaccard < 0.85
      │  saída: candidates/synthetic_expansion.jsonl
      ▼
[validate_synthetic_sft.py]  ── contrato + schema (--allow-pending)
      ▼
[critic_synthetic_candidates.py]  ── approve/revise/reject + razões
      │  saída: candidates/synthetic_teacher_critic.jsonl
      ▼
[check_synthetic_teacher_batch.py]  ── gates determinísticos (termos frios,
      │                                risco, sensibilidade, dedup, cobertura)
      ▼
[plan_synthetic_human_review.py]  ── revisão humana: destructive/credential 100%,
      │                              mutating 25%, read_only 5%
      ▼
[build_synthetic_experiment_splits.py]  ── splits sem vazamento (baseline e
                                           tratamento) + manifestos
      ▼
(Fase 7) train_sft.py --dry-run → treino → eval — BLOQUEADO até autorização
```

## Componentes

| Script | Fase | Papel |
|---|---|---|
| `build_synthetic_baseline_manifest.py` | 0 | Hashes/counts de claims, approved, eval, splits |
| `generate_synthetic_teacher_candidates.py` | 2 | Seleção determinística + geração por cenário |
| `teacher_provider.py` | 2 | Interface provider + `OfflineTeacherProvider` + `subject_for_claim` |
| `teacher_provider_v2.py` | 2 | Provider estendido (offline-v2): cenários novos + corpo bilíngue |
| `generate_synthetic_expansion.py` | 2 | Expansão: claims restantes + novos cenários + gate Jaccard < 0.85 |
| `validate_synthetic_sft.py` | 1 | Schema, contrato de cenário, synthetic_generation |
| `critic_synthetic_candidates.py` | 3 | Decisões approve/revise/reject com razões |
| `check_synthetic_teacher_batch.py` | 4 | Gate determinístico do subconjunto aprovado |
| `plan_synthetic_human_review.py` | 5 | Plano de revisão humana por risco |
| `build_synthetic_experiment_splits.py` | 6 | Splits baseline/tratamento sem vazamento |
| `test_synthetic_teacher.py` | 4 | 13 testes unitários/estruturais |

## Contrato de dados

Cada candidato (compatível com schema SFT existente, + campos opcionais):

```json
{
  "messages": [{"role": "system"}, {"role": "user"}, {"role": "assistant"}],
  "claim_ids": ["hwa-..."],
  "product": "HCL Workload Automation",
  "version": "10.2.8",
  "platform": "Distributed",
  "language": "pt",
  "risk": "read_only",
  "review_status": "candidate",
  "record_id": "sft-...",
  "claim_family_id": "claim-...",
  "paraphrase_family_id": "claim-...-syn-<scenario>-<lang>",
  "teacher_style": "synthetic",
  "synthetic_generation": {
    "pipeline_version": "teacher-critic-v1",
    "scenario_type": "technical",
    "template_version": "1.0",
    "teacher_model_alias": "offline",
    "critic_decision": "approve",
    "critic_reasons": [],
    "critic_model_alias": "critic-v1"
  }
}
```

## Cenários

Definidos em `data/sft/synthetic_scenarios.json` com `allowed_risks` por
cenário. Restrições de elegibilidade:
- `troubleshooting`: claim deve ter código de erro/mensagem ou termo "erro".
- `unknown_evidence`: claim com knowledge_status=insufficient ou notes
  contendo "insufficient".
- `risk_confirmation`: apenas riscos mutating/destructive.
- Novos cenários da expansão v2: `clarification`, `comparison`,
  `hard_negative`, `edge_case` (3 mensagens) e `multi_turn` (5 mensagens:
  system/user/assistant/user/assistant). O crítico e o gate aceitam o formato
  multi_turn e verificam termos frios em todos os turnos do assistente.

## Segurança e autorização

- Nenhum comando real, credencial, IP ou produção.
- destructive/credential_sensitive: revisão humana 100% (obrigatória).
- mutating: amostra 25%; read_only: amostra 5%.
- Provedores de modelo (local/external) e treino (Fase 7): exigem nova
  autorização explícita.

## Observabilidade

- Manifestos em `data/sft/experiments/` com hashes, contagens, decisões,
  amostras de revisão e verificação de vazamento.
- `pipeline_baseline_manifest.json` preserva o estado pré-experimento.

## Compatibilidade e rollback

- Não altera `approved.jsonl`, `train/validation/test.jsonl`, nem `claims.jsonl`.
- Candidatos ficam isolados em `data/sft/candidates/`.
- Rollback = remover artefatos de `candidates/` e `experiments/`; approved
  intocado.
