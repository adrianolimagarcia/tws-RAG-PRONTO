# Release Report — r25-sota (2026-08-25)

**Snapshot:** `data/releases/r25-sota-20260825-173038/`
**Release anterior:** `r24-sota-20260825-161729` (baseline)
**Manifesto:** `snapshot_manifest.json` (15 artefatos, SHA-256 por arquivo)

---

## 1. Escopo da rodada

Rodada **hwa-agent-mdm-dwc-2026-08-25**: geração de SFT candidates a partir de
77 claims verificadas de Dynamic Agent, MDM e DWC.

- **154 candidatos gerados** (77 PT + 77 EN), 77 claims
- Temas: dynagent (29+1), DWC (46), MDM (1)
- Auditoria independente: APROVADO COM RESSALVAS na 1ª rodada (8 PT com resposta
  EN + 6 Context markers) → corrigido → 2 deltas → **FINAL: APPROVED**
- 154 promovidos − 27 duplicados de rodadas anteriores (dynagent já tinha SFT) =
  **+127 líquido**

## 2. Métricas

### SFT (approved.jsonl)
| Métrica | r24 | r25 | Δ |
|---|---|---|---|
| aprovados | 15729 | 15856 | +127 líquido |

- Idiomas: pt / en balanceados (163+163 = 326 candidates totais)
- Novos tópicos cobertos: dynamic agent (config, localopts, SSL, broker), DWC
  (install, API, login, engine connection, certs), MDM (aes keys)

### Splits: train=11573 / validation=2841 / test=1469
### Eval: 4212 casos (2106 PT / 2106 EN)
### Gates: 8/8 PASS · Regression r24→r25: PASS

## 3. Notas técnicas

- Duplicatas: 27 respostas colidiam com SFT dynagent de rodadas anteriores
  (mesmo claim text) → removidos os novos, mantidos os antigos (primeira ocorrência).
- Laço: promote → validate FAIL (duplicatas) → dedup → validate_all PASS →
  snapshot r25.