# Release Report — r22-sota (2026-08-25)

**Snapshot:** `data/releases/r22-sota-20260825-143234/`
**Release anterior:** `r21-sota-20260825-140052` (baseline de regressão)
**Manifesto:** `snapshot_manifest.json` (15 artefatos, SHA-256 por arquivo)

---

## 1. Escopo da rodada

Rodada **hwa-aida-1028-enrichment-f4-2026-08-25**: enriquecimento do material
AIDA (AI Data Advisor) 10.2.8 com 4 fases:

- **F1**: Mineração lab — schemas reais do OpenSearch (12 alert-definitions, 6 kpis-definition, metric-index, 95 special-days), API REST interna (23 endpoints com swagger + Keycloak auth)
- **F2**: Documentação oficial — 18 páginas do AIDA User's Guide 10.2.8 (conceitos, KPIs, alertas, retrain, special days, Keycloak, email, z/OS)
- **F3**: Validação lab — ciclo de alertas (15min), retrain (24h), email via Redis, widget DWC (bloqueado Kaspersky)
- **F4**: 22 candidatos SFT promovidos (11 PT / 11 EN) após auditoria independente APROVADO

## 2. Métricas

### Claims
| Métrica | r21 | r22 | Δ |
|---|---|---|---|
| claims.jsonl | 1192 | 1203 | +11 |
| verified | 1126 | 1137 | +11 |
| topic `aida` | 7 | 18 | +11 |

### SFT (approved.jsonl)
| Métrica | r21 | r22 | Δ |
|---|---|---|---|
| aprovados | 15583 | 15605 | +22 |
| topic `aida` | 14 | 36 | +22 |

- Idiomas: pt=7651 / en=7954
- Riscos: read_only=10795, mutating=2857, destructive=981, credential_sensitive=972

### Splits: train=11376 / validation=2796 / test=1433
### Eval: 4148 casos (2074 PT / 2074 EN)

### Gates: 8/8 PASS (RAG SKIP opcional)

## 3. Evidências

- 18 evidências lab (0061-0078) em `lab-validation-2026-08-25-aida-docker.jsonl`
- Runbook P33 + P33b + troubleshooting 8-12 em docs/