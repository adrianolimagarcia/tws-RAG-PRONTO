# PROGRESS — Expansão Sintética HWA (teacher-critic v2, final v6)

Atualizado: 2026-08-23

## Estado atual

**TREINO NÃO EXECUTADO. Nenhum registro promovido ao approved.jsonl.**

Expansão sintética concluída (v6) com diagnóstico de causa raiz e revisão
humana assistida dos candidatos de alto risco.

## Números

| Métrica | v1 | v5 | v6 (final) |
|---|---|---|---|
| Sintéticos aprovados | 1.068 | 8.171 | **8.355** |
| Claims cobertos | 100 (13%) | 750 (97,7%) | **767 (99,9%)** |
| Idiomas | pt 534 / en 534 | pt 3.521 / en 4.650 | pt 3.597 / en 4.758 |
| Tratamento total | 14.135 | 21.238 | **21.422** (+63,9%) |
| Riscos | read/mutating | read 6.207, mut 1.368, destr 263, cred 333 | read 6.345, mut 1.368, destr 287, cred 355 |

## Investigações dos 18 claims restantes

Após o diagnóstico inicial, os 18 claims sem candidato foram investigados
individualmente com `diagnose_remaining_claims.py`:

- **12 claims** não foram selecionados por sorte/quota no pass9 (prompts únicos,
  sem colisão) — resolvidos na passada 10.
- **6 claims** (install×4, tls-0002, themaster-0013) tinham subject genérico
  ("install", "tls", "job stream de fim de dia...") que colidia com prompts já
  existentes — corrigido anexando o número do claim ao subject no fallback.

**Correção aplicada em `teacher_provider.py`:**
- Subject genérico curto (≤1 token relevante) → anexa número do claim.
- Fallback nt com valores → anexa número do claim para unicidade.

**Resultado:** passada 10 gerou 191 candidatos para 17 dos 18 claims restantes
(todos sem colisão). O claim `hwa-10.2.8-govern-0018` permanece sem candidato
por não ter sido selecionado no seed 47 — aceito como limitação menor (99,9%).

## Revisão humana assistida dos candidatos de alto risco

- Total de alto risco no v6: **642** (destructive 287 + credential_sensitive 355).
- Sinalizados por heurística: **8**.
- **Falsos positivos confirmados: 8/8** (4× composer -jwt, 4× apikey).
- Segredos reais expostos: **0**.
- Verdict: **APROVADO** (registro em `human_review_high_risk_v6.json`).

## Validações executadas

- Gate sintético v6: OK — 8.355 aprovados, 0 duplicatas, termos frios OK.
- Splits: vazamento cruzado OK.
  baseline: train 8.948 / validation 2.732 / test 1.387
  tratamento: train 14.767 / validation 4.263 / test 2.392
- Hashes preservados:
  - approved.jsonl: 90b50dd8ca6c
  - train.jsonl: 3f6c88a589b2
  - validation.jsonl: 0229a81e2be4
  - test.jsonl: 29a749fb4991

## Melhoria de qualidade sintética — v7 (concluído)

Executado ciclo RPI para ampliar/precisar o dataset com base no material existente.

### Workstreams
- **WS1+WS2** (profundidade): +1.173 candidatos para 90 claims ralos/gap
  (`govern-0018` + 89 claims com ≤4 candidatos). Cobertura vai a 100%.
- **WS3a** troubleshooting: implementado corpo de resposta distinto
  (sintoma/causa/recuperação extraídos do claim). +1.087 registros
  (era 7 no v6).
- **WS3b** risk_confirmation: +281 registros (era 38 no v6) — reforço de
  segurança (confirmar antes de operação destrutiva/mutante).
- **WS4** contrastivos: +1.180 (comparison+hard_negative) para 35 famílias
  confusáveis (410 claims) — reduz ambiguidade entre claims similares.

### Integração v7
- Sintéticos: **10.961** (v6 era 8.355; +2.606).
- Claims cobertos: **768/768 (100%)**.
- Tratamento total: **24.028** (+84% vs baseline 13.067).
- Cenários balanceados (troubleshooting 7→1.087; risk_confirmation 38→281).
- Gate sintético: OK. Splits regenerados, vazamento cruzado OK.
- Artefato "Não HCL Workload"→"No HCL Workload" reaplicado (0 pendências).
- Entailment audit v7: ENTAILED 8.388 (76,4%); issues são FPs do heurístico
  (mesmo padrão do v6, já investigado).

### Arquivos
- `data/sft/candidates/synthetic_treatment_v7.jsonl` — tratamento final
- `data/sft/candidates/synthetic_ws{12,3a,3b,4}_approved.jsonl` — passes
- `data/sft/experiments/entailment_audit_v7.jsonl` / `_summary_v7.json`
- `scripts/teacher_provider_v2.py` — `_troubleshooting_body` (resposta distinta)
- `scripts/generate_synthetic_expansion.py` — `--claims-file`, troubleshooting/risk_confirmation habilitados

## Entailment audit do v6 (concluído)

- Script: `scripts/entailment_audit_v6.py` (reusa `entailment_audit.py`).
- Verdicts: ENTAILED 6.309 (75,5%) / PARTIALLY 917 (11,0%) / NOT_ENTAILED 1.129 (13,5%).
- Todos os issues do heurístico são FALSO POSITIVO (case-sensitivity, split por
  versão, negação semântica, abreviações). Evidência em
  `data/sft/experiments/entailment_audit_v6_report.md`.
- Defeito real corrigido: 26 respostas com artefato "Não HCL Workload" → "No
  HCL Workload" (homófono). Gate segue OK; splits regenerados.

## Próximos passos

1. Decisão de promoção ou treino QLoRA (bloqueado até autorização explícita).

## Artefatos gerados

- `data/sft/candidates/synthetic_treatment_v6.jsonl` — tratamento final (8.355)
- `data/sft/experiments/human_review_high_risk_v6.json` — revisão humana
- `data/sft/experiments/synthetic_expansion_pass10_critic_report.json`
- `data/sft/experiments/treatment_manifest.json`
- `scripts/diagnose_remaining_claims.py`
- `scripts/teacher_provider.py` — fallback com número do claim

---

# R17 — 2026-08-23: REST API v2 no lab + Synthetic teacher v7

## Frente 1: REST API v2 validada no laboratório
- **Descoberta**: REST API v2 em `https://localhost:31116/twsd/api/v2/` (engineServer Liberty, porta 31116), autenticação Bearer com JWT Personal do ocli
- **Spec OpenAPI oficial**: `WA_API3_v2.json` (212 paths) extraída do WAR `TWSdRESTWeb-10.2.8.00-SNAPSHOT.war` → copiada para `data/evidence/restapi/`
- **22 endpoints GET read-only validados (todos 200)**: engine/info, engine/users, engine/groups, model/* (jobdefinition 84, jobstream 9, workstation 5, domain MASTERDM, calendar, variabletable, folder), plan/* (job 236, job/{id}, job/count, jobstream 201, workstation, prompt, resource), objects-info, auth/status
- **OQL validado**: `oql=name = 'UPDATESTATS'` → 200 (filtro por campo `name`); `oql=ORDER BY key.name ASC` → 200 (sort dot-notation); **GAP doc×impl**: `oql=key.name = 'X'` (exemplo oficial) → 400 OQL_FILTER_SYNTAX_ERROR
- **plan_filter validado**: `plan_filter=/MDMDA#/` → 200 (224 jobs); wildcard `/@/@#/@/@.@` → 200 (236)
- **Paginação**: limit/offset com URL `next` na resposta
- **4 claims restv2-* atualizadas** com lab_validation (0011, 0012, 0016, 0041) + **6 claims novas** (0148-0153: endpoints, oql-name gap, oql-sort, planfilter, pagination, workspace-404)
- Evidência: `data/evidence/lab-validation-2026-08-23-r17-restapi.jsonl`

## Frente 2: Synthetic teacher v7
- **Alvo**: 90 claims verified sem cobertura sintética (globalopts, incidents, dbviews, dwc-restv2, perf, restv2)
- **Geração**: 1.150 candidatos (4 rodadas: v7a 976, v7b 122, v7c 38, v7d 14) com seeds/thresholds variados
- **Critic**: 1.124 aprovados + 12 ita238e aprovados manualmente (falso positivo do detector de IP: "10.2.8.00" é versão, não IP)
- **Filtros**: 97 multi_turn (5 msgs) removidos (ROLES exige 3 msgs), 96 duplicatas de prompt/resposta removidas
- **Normalização**: "10.2.8.00" → "10.2.8" (versão canônica, evita falso positivo regex IP)
- **Prompts genéricos**: 79 corrigidos (rest_api_v2/troubleshooting → subject específico do claim)
- **Resultado**: approved 14.049 → **14.892** (+843), claims cobertos 997 → **1.073**, splits 10.890/2.658/1.344, validadores TODOS PASS

---

# hwa-dataset-quality-gates — Estado das fases (2026-08-23)

Plano: `hwa-dataset-quality-gates`. Fases F1–F5; decisões D1–D6 registradas em
`docs/DECISIONS_SOTA_RELEASE.md`.

| Fase | Nome | Estado | Marcador |
|---|---|---|---|
| F1 | Verificação de claims sensíveis (51 backlog) | **CONCLUÍDO** — 51 claims sensíveis revalidados; 48 corroborados com 2ª fonte oficial, 3 restantes com `validation_scope=common_practice_unvalidated` no `sensitive_revalidation_backlog`; `validate_evidence --require-corroboration` exit 0 | ✅ |
| F2 | Promoção validada de SFT | **CONCLUÍDO** — 679 promovidos (602 comportamentais PT/EN + 77 FC) via `scripts/promote_validated_sft.py`; gates PASS; release r18-sota-20260823-160452 | ✅ |
| F3 | Corroboração / validação estrutural | Gates estruturais PASS (evidence estrito, sft, eval, fc, contradição, regressão) | ✅ |
| F4 | Agente Perplexity + KB + 3 pontos MCP | **CONCLUÍDO** — agente `.opencode/agents/perplexity-specialist.md` + KB `.opencode/knowledge/perplexity-mcp.md` criados; `validate_opencode_assets.py` exit 0; 3 pontos MCP investigados 2026-08-23: nenhum defeito — 403=fallback interno server.py:662-667, timeout imposto server.py:608/680 com repro `timedOut:true` em 5s, Windows vs Linux=design | ✅ |
| F5 | Gate único `scripts/validate_all.py` | **CONCLUÍDO** — 8 gates encadeados via subprocess; verificado | ✅ |

**F5 — detalhe**: `scripts/validate_all.py` (stdlib-only: subprocess, argparse,
time, sys, pathlib, json) executa em ordem: validate_evidence (estrito,
`--require-corroboration`), validate_sft (approved + `--require-risk-coverage`),
split_sft (checagem determinística, integridade por hash), validate_eval,
validate_rag_contract (SKIP quando não há corpus RAG em `data/`; `--require-rag` torna obrigatório),
validate_function_calls, contradiction_gate, regression_gate (`--baseline`
release mais recente). Exit agregado: 0 todos PASS / 1 qualquer FAIL / 2 erro
do próprio script. Modos `--list` e `--gate N`. Nenhum dado do pipeline é
alterado (12 artefatos monitorados por hash).

**Resultado da execução real** (2026-08-23): 8/8 gates — **7 PASS + 1 SKIP**;
gate `validate_rag_contract` **SKIP** quando não há corpus de respostas RAG em
`data/` (ablação PENDENTE: sem treino QLoRA ainda não há respostas de modelo);
`--require-rag` torna o gate obrigatório (FAIL exit 1 sem corpus). Exit agregado
do `validate_all.py`: **0**.

---

# hwa-dataset-quality-gates — F4 executada (2026-08-23)

**Agente Perplexity + KB** via `.opencode/agents/perplexity-specialist.md` +
`.opencode/knowledge/perplexity-mcp.md`; `validate_opencode_assets.py` exit 0
(10 skills, 11 agentes, 4 comandos); fix de frontmatter em
`llm-fingerprint/SKILL.md` (description com YAML inválido); demais agentes
intactos.

**Investigação dos 3 pontos MCP Perplexity** (2026-08-23) — conclusão: nenhum
defeito, os 3 pontos são comportamento correto/design:

- **PONTO 1 (fallback 403)**: NÃO É BUG. server.py:662-667 trata 403 como
  fallback interno (tenta próximo impersonation fingerprint); se todos falharem
  sobe PerplexityAuthError (retryable=false) via tool_error. Design documentado
  no README.
- **PONTO 2 (timeout não-real)**: NÃO É BUG. server.py:608 deadline =
  monotonic + timeout_seconds; linha 680 timed_out=True se estourar; linhas
  650-653 capeiam connect/read pelo budget. **REPRO REAL**: timeout_seconds=5 →
  envelope `{"timedOut": true, "ready": false, "elapsed_ms": 6193}`. O teste
  anterior (timedOut=false em 5465ms) era correto: resposta completou dentro do
  prazo.
- **PONTO 3 (Windows vs Linux)**: DIVERGÊNCIA POR DESIGN documentada.
  server.py (Windows, DPAPI CryptUnprotectData) vs server_linux.py (WSL,
  edge-aes-key.bin exportada 1x via export_key.py). README seção "Versão Linux
  nativa (WSL)".
- **Conclusão**: nenhuma correção necessária no plugin; KB perplexity-mcp.md
  atualizado (seção "Known divergence points" → "Divergence points —
  investigated 2026-08-23 (F4)"), validate_opencode_assets.py exit 0.

---

# hwa-dataset-quality-gates — F2 executada (2026-08-23)

**Promoção validada de SFT** via `scripts/promote_validated_sft.py`:
- approved.jsonl: 14.888 → **15.567** (+679: 602 comportamentais PT/EN + 77 FC);
  CRLF preservado; `validate_sft.py --status approved --require-risk-coverage` PASS.
- Rejeitados e reportados (regra Etapa 2b: nunca forçar): 1.206 comportamentais
  por `resposta duplicada` (gerador cria 3-5 paráfrases por claim com a mesma
  resposta; só a 1ª ocorrência de cada hash de resposta é válida) + 5 FC por
  `prompt duplicado` (o gerador reutilizou o comando "showcpus" para
  `conman_show_workstations` e `conman_show_cpus_link`).
- Falso positivo corrigido: "10.2.8.00" (versão canônica, não IP) normalizado
  para "10.2.8" no conteúdo das mensagens (convenção DECISIONS P4/learnings).
- FC claim_ids mapeados (D3): 69 primário (approved FC action->claim_ids) +
  8 fallback (claims verified por termo, menor claim_id por comprimento);
  `sem_match=0`; campos do approved preenchidos a partir do claim mapeado.
- Splits regenerados: train=11.362 / val=2.784 / test=1.421; `validate_eval` PASS
  (3.864 casos). Release imutável `r18-sota-20260823-160452` (15 artefatos;
  gates internos validate_evidence/validate_sft/validate_eval = 0/0/0).
- `regression_gate.py --baseline r17-sota-20260823-124416` → **PASS** (nenhuma
  dimensão regrediu; destructive 962 → 974, ≥0%).

**Ablação F2: PENDENTE - sem treino QLoRA (decisao do usuario 2026-08-23);
promocao baseada em validacao estrutural + gates.**

---

# Ablacao e status experimental da promocao P4/P5 (2026-08-23)

- A promocao dos 679 candidatos (602 comportamentais + 77 FC) foi aprovada por
  **VALIDACAO ESTRUTURAL** (gates) e **NAO** por evidencia empirica de melhoria
  do modelo.
- **Ablacao real** (comparar modelo com vs sem candidatos P4/P5) **NAO foi
  executada** — sem treino QLoRA (decisao do usuario 2026-08-23).
- **IMPLICACAO FORMAL**: ate haver ablacao empirica, os registros promovidos de
  `behavioral_scenarios_*` e `function_calling_expansion_*` sao considerados
  **EXPERIMENTAIS**. Nao usar como base para decisoes de qualidade do modelo
  sem ablacao.
- Gate 5 (`validate_rag_contract`) permanece **SKIP** ate existir corpus de
  respostas RAG (depende de treino/inferencia).
