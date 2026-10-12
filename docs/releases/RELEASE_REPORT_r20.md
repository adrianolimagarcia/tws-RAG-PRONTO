# Release Report — r20-sota (2026-08-25)

**Snapshot:** `data/releases/r20-sota-20260825-105238/`
**Release anterior:** `r19-sota-20260823-171000` (baseline de regressão)
**Manifesto:** `snapshot_manifest.json` (15 artefatos congelados, SHA-256 por arquivo)

---

## 1. Escopo da rodada

Rodada **hwa-dwc-1028-ui-language-2026-08-25**: idioma da interface do
Dynamic Workload Console 10.2.8 (Accept-Language do navegador) e idioma das
default tasks (primeiro login do usuário).

- 2 claims novas verificadas (lab + fonte oficial):
  - `hwa-10.2.8-dwc-ui-language-0001` — UI segue o Accept-Language do navegador;
    sem seletor no login; sem propriedade de idioma no `TdwcGlobalSettings.xml`.
  - `hwa-10.2.8-dwc-default-tasks-language-0002` — default tasks criadas no
    idioma do 1º login e não traduzidas depois; solução oficial = novo usuário
    com 1º login no idioma desejado; `precannedTaskCreation` lida só no 1º login.
- Evidência lab: `data/evidence/lab-validation-2026-08-25-dwc-ui-language.jsonl`
  (2 records: 0057 curl Accept-Language pt-BR vs en-US; 0058 doc oficial).
- 4 candidatos SFT promovidos (2 PT / 2 EN), após auditoria independente.

## 2. Métricas

### Claims
| Métrica | r19 | r20 | Δ |
|---|---|---|---|
| claims.jsonl | 1167 | 1185 | +18 |
| observed_in_lab | — | 9 | — |
| verified | — | 1119 | — |
| version_dependent | — | 39 | — |

### SFT (approved.jsonl)
| Métrica | r19 | r20 | Δ |
|---|---|---|---|
| aprovados | 15567 | 15569 | +2 líquido* |
| candidatos | — | 17 | — |

\* +12 (rodada install DWC) −14 (obsoletos removidos) +4 (UI language) = +2 líquido.

- Idiomas: pt=7633 / en=7936 (balanço 49,0%/51,0%).
- Riscos: read_only=10767, mutating=2851, destructive=981, credential_sensitive=970.
- Topics novos: `dwc_ui` (4), `dwc_api` 650→654, `topology_ha` 1089→1091.

### Splits (leakage-safe por famílias conectadas)
| Split | r19 | r20 |
|---|---|---|
| train | 11352 | 11356 |
| validation | 2788 | 2788 |
| test | 1425 | 1425 |

### Eval independente (gold factual PT/EN)
| Métrica | r19 | r20 | Δ |
|---|---|---|---|
| casos | 4004 | 4076 | +72 |
| pt / en | — | 2038 / 2038 | — |

### Gates (validate_all.py, 8 gates)
| Gate | Resultado |
|---|---|
| validate_evidence (--require-corroboration) | PASS (1185) |
| validate_sft (approved, --require-risk-coverage) | PASS (15569) |
| split_sft | PASS (11356/2788/1425) |
| validate_eval | PASS (4076) |
| validate_rag_contract | SKIP (sem corpus RAG; ablação pendente) |
| validate_function_calls | PASS |
| contradiction_gate | PASS (1167 elegíveis, 0 pendentes) |
| regression_gate (r19→r20) | PASS (sem queda >5%; destructive 0%) |

Integridade: 12 artefatos monitorados, nenhum alterado durante os gates.

## 3. Auditoria independente (segregação de deveres)

- **Auditor:** `hwa-dataset-auditor` (independência; o builder não aprova os
  próprios exemplos).
- **Pacote congelado:** `data/sft/candidates_uilang_2026_08_25_frozen.jsonl`
  (sha256 `d1c7310e…990da`).
- **1ª rodada:** APPROVED WITH CAVEATS — 2 MEDIUM: opção "(2) operational
  alternative" (Manage Tasks rename/recreate/delete) não acarretada pela claim
  0002 e descrevia mutação sob `risk=read_only`.
- **Correção (builder):** remoção da opção mutante, renumeração,
  "WebSphere Liberty Base administrator", termo oficial "graphical view limits".
- **Re-auditoria (delta):** FINAL **APPROVED** — todos os caveats resolvidos;
  sem novos problemas; PT/EN fiéis.

## 4. Rejeitadas e pendências

- **Claims rejeitadas nesta rodada:** nenhuma (as 2 novas claims passaram na
  verificação lab + fonte oficial).
- **Candidatos SFT rejeitados:** nenhum — 4/4 aprovados após correção de escopo.
- **Caveats residuais do auditor (LOW/NOTE, não bloqueantes):**
  - `WSL2` como descritor de proveniência lab (aceitável; consta no
    `lab_validation` da claim).
  - Termo "WebSphere Liberty Base" é abreviação do oficial
    "WebSphere Application Server Liberty Base administrator" (fidelidade ok).

## 5. Riscos residuais

1. **Gate RAG (5) SKIP** — sem corpus de respostas (`data/eval/rag_responses.jsonl`);
   ablação PENDENTE até existir treino QLoRA. Não é regressão; é cobertura
   incompleta do pipeline.
2. **Descoberta lab (Opção A):** criação de default tasks **não** observada via
   login HTTP puro para `wauser_en` (tdwc_querytask: wauser=21, wauser_en=0);
   indica que a criação é disparada pela UI/JS (SPA). Não contradiz a claim 0002
   (que descreve o 1º login com navegador), mas merece evidência lab adicional
   com navegador real antes de generalizar.
3. **FFDCs no dwcServer** (`NoClassDefFoundError` de SmallRye JWT/Micrometer/
   MongoDB) — features não usadas no lab; inofensivos, servidor saudável.
4. **Certificado self-signed** do lab (CN=HWA-LAB) — esperado; navegador exige
   exceção manual; não afeta o dataset.
5. **Corpus causal:** `quality_report.json` mantém `verdict: APROVADO COM
   RESSALVAS` (par contencioso >1%) — inalterado pela rodada SFT.

## 6. Consumo do treino

`config.yaml` atualizado por `release_snapshot.py`:
- `release.id: r20-sota-20260825-105238`
- `sft.approved_file: data/releases/r20-sota-20260825-105238/approved.jsonl`

O treino consumirá exclusivamente o snapshot imutável (P0); nenhum treinamento
foi iniciado nesta rodada (não autorizado).
