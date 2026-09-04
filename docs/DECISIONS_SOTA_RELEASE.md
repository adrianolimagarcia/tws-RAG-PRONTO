# DECISIONS — Release SOTA (P0–P6)

Data: 2026-08-23
Release final: `data/releases/r17-sota-20260823-124416/`

## P0 — Release imutável

- **Decisão**: R17 (estado canônico atual) é o baseline; primeiro release imutável
  `r17-sota-20260823-114436` com manifesto SHA-256.
- **Artefatos**: `scripts/release_snapshot.py`, `scripts/regression_gate.py`,
  `data/releases/<id>/snapshot_manifest.json`, `data/releases/latest.json`.
- **Config**: `sft.approved_file` aponta para o snapshot imutável; `release.id`
  registra o release ativo. Treino nunca lê `data/sft/approved.jsonl` mutável.
- **Gate**: `regression_gate.py` falha se destructive cai >0% ou outras
  dimensões caem >5% (default). Re-hash do release confere (AC-001 PASS).
- **Limitação**: releases intermediários aninhados (`r17-sota-20260823-102815-*`)
  foram gerados durante iteração do script e permanecem por imutabilidade;
  não são apontados por `latest.json`.

## P1 — Blind eval set

- **Decisão**: `data/eval/blind_eval_seed.jsonl` com 320 casos, 9 famílias,
  4 métricas. Runner `run_blind_eval.py` com heurísticas determinísticas;
  juiz LLM é triagem opcional (nunca veredito final).
- **Limitação**: respostas reais dependem do pipeline RAG/modelo; o runner
  foi testado com respostas sintéticas. Revisão humana obrigatória antes de
  usar como gate.

## P2 — RAG evidence-first

- **Decisão**: contrato em `docs/RAG_EVIDENCE_CONTRACT.md`; validador
  `validate_rag_contract.py` com regras R1–R5.
- **Validação**: 5 respostas de teste → violações R1/R2/R4/R5 detectadas
  corretamente; exit 1 quando viola, 0 quando limpo.

## P3 — Expansão real

- **Decisão**: formato de lab session em `docs/LAB_SESSION_FORMAT.md`;
  fontes oficiais registradas em `data/incoming/official_sources_*.jsonl`
  (REST API v2, Troubleshooting Guide 10.2.8, Release Notes, System
  Requirements). Extração/verificação pendente de lab/perplexity.
- **Regra**: claims sensíveis novas exigem 2 evidências independentes OU
  1 oficial + 1 lab (`validate_evidence.py --require-corroboration`).

## P4 — Sintético comportamental

- **Decisão**: `generate_behavioral_scenarios.py` (determinístico, deriva do
  claim, sem fatos novos) → 904 candidatos PT + 904 EN validados para 181
  claims de cobertura baixa (<3 SFT). Cenários mapeados para o contrato
  `synthetic_scenarios.json` (technical, troubleshooting, risk_confirmation,
  edge_case, version_platform, false_premise, comparison, clarification).
- **Ablação**: `ablation_report.py` → baseline 14.892 + 904 candidatos,
  0 overlap record_ids, 0 vazamento no test, 167 claims elevadas a 3+.
  **Decisão pendente**: promover apenas após treino + holdout cego, se
  melhorar factual_correctness sem piorar abstention_correct.
- **Correções aplicadas**: falso positivo IP em `validate_synthetic_sft.py`
  (versão `10.2.8.00` não é IP) e política de risco por cenário.

## P5 — Function calling

- **Decisão**: `expand_function_calling.py` consome o registry → 39 candidatos
  PT + 39 EN validados (16 positivos habilitados + 23 recusas de desabilitadas).
- **Validador**: `validate_function_calls.py` ganhou `--file`.
- **Limitação**: o contrato atual (`validate_function_calls.py`) só aceita
  recusas para ações `enabled=false`; recusas por origem/versão inválida em
  ações habilitadas não são representáveis no schema atual (documentado;
  evolução futura do refusal_schema).

## P6 — Idioma e contradição

- **Decisão**: `contradiction_gate.py` → 16 pares pendentes de adjudicação
  (incluindo o par crítico `composer-keyword-order-0115` vs
  `composer-priority-in-jobs-0124` — PRIORITY em $JOBS).
- **Decisão**: `support_matrix.py` → matriz 1152 claims × versão × plataforma ×
  status.
- **Decisão**: `balance_holdout_language.py` → relatório mostra holdout já
  balanceado (train/val/test ≈ 49/51 PT/EN por fonte hcl_help/ibm/other);
  rebalanceamento automático não necessário (AC-010 via relatório).

### Adjudicação dos 16 pares (2026-08-23)

- **Artefato**: `data/evidence/contradiction_adjudications.jsonl` (17 registros;
  16 pares, o par 0115/0124 tem 2 registros: `claim_b_wins` + `needs_revision`).
- **Veredito majoritário**: 15/16 pares = `both_scope` (falsos positivos do
  detector de polaridade/prescrição — vocabulário comum, sem contradição real).
- **Par real**: `0115` vs `0124` → **`0124 wins`** (evidência de laboratório
  10.2.8.00 confirma que PRIORITY NÃO é válido em $JOBS) e **`0115 needs_revision`**.
- **Correção aplicada**: claim 0115 reescrito para não implicar PRIORITY como
  keyword $JOBS válida (ordem canônica escopada às keywords válidas; PRIORITY
  apenas em $SCHEDULES, sbj, chgjob — ver 0124).
- **Gate corrigido**: `contradiction_gate.py` agora filtra pares adjudicados do
  backlog persistido antes de compor `combined`; `--require-adjudication` passa
  com 0 pendentes após adjudicação.

### Quarentena PRIORITY em $JOBS (2026-08-23)

- **Artefato**: `data/sft/quarantine_priority_in_jobs.jsonl` (4 registros).
- **Critério**: SFT ligados ao claim 0115 (2) + SFT cuja resposta ensina
  PRIORITY como keyword $JOBS válida sem negação (2).
- **Impacto**: `approved.jsonl` 14.892 → 14.888; splits regenerados
  (train 10.886 / val 2.658 / test 1.344); validadores PASS.

### Contrato de function calling evoluído (2026-08-23)

- **refusal_schema** (`automation-action-registry.json`): adicionados
  `origin_not_allowed`, `version_not_supported`, `missing_required_parameter`,
  `invalid_parameter`.
- **`validate_function_calls.py`**: recusas contextuais agora são aceitas mesmo
  em ações habilitadas (`not is_contextual and requested["enabled"]`).
- **`expand_function_calling.py`**: gera 4 tipos de recusa contextual para ações
  habilitadas → 82 candidatos (16 positivos + 66 recusas) por idioma; validação PASS.

## Perguntas em aberto

- Q2: Tolerância do gate de regressão (default 0% destructive / 5% outros) —
  ainda em aberto, usar default.
- Q1 (adjudicação dos 16 pares) e Q3 (refusal_schema contextual) foram
  **resolvidas** em 2026-08-23.

---

# Decisões hwa-dataset-quality-gates (D1-D6)

Fase 5 do plano `hwa-dataset-quality-gates` (2026-08-23). Gate único encadeado:
`scripts/validate_all.py` (F5) executa os 8 validadores do pipeline em ordem via
subprocess, sem alterar comportamento dos validadores nem os dados.

- **D1 — Ordem F1→F2→F3→F5→F4**: execução encadeada das frentes na ordem
  F1 (verificação de claims sensíveis) → F2 (promoção validada) → F3
  (corroboração/validação estrutural) → F5 (gate único `validate_all.py`) →
  F4 por último (agente Perplexity + KB + correção dos 3 pontos MCP).
- **D2 — Promoção por validação estrutural + ablação PENDENTE**: promoção de
  SFT ao `approved.jsonl` ocorre por validação estrutural (gates PASS); a
  ablação/treino QLoRA permanece **PENDENTE** — sem treino QLoRA nesta rodada
  (decisão do usuário; nenhum treino executado).
- **D3 — FC promovidos só com claim_ids mapeados**: exemplos de function
  calling só são promovidos com `claim_ids` mapeados (fonte primária: mapping
  em `approved.jsonl`; fallback menor claim_id por comprimento), pois
  `validate_sft.py` exige `claim_ids` não vazio.
- **D4 — Quarentena z/OS = referência, fora do pipeline**: claims z/OS em
  quarentena são material de referência, fora do dataset Distributed; não
  entram em `approved.jsonl` nem nos splits.
- **D5 — Sem 2ª evidência nem lab → lab_required (nunca inferir)**: claim sem
  corroborating_sources nem lab_validation permanece com exigência de
  validação lab (`lab_required`); o pipeline nunca infere evidência.
- **D6 — F4 corrige/documenta só os 3 pontos MCP Perplexity**: 403 fallback,
  timeout não-real (`timedOut=false`), diferenças Windows vs Linux — escopo
  fechado; sem expansão para outros pontos MCP.
- **D7 — Promocao P4/P5 = experimental ate ablacao empirica (sem treino QLoRA,
  decisao 2026-08-23)**: a promocao dos 679 candidatos (602 comportamentais +
  77 FC) foi aprovada por **VALIDACAO ESTRUTURAL** (gates) e NAO por evidencia
  empirica de melhoria do modelo; a ablacao real (modelo com vs sem candidatos
  P4/P5) NAO foi executada — sem treino QLoRA (decisao do usuario 2026-08-23).
  Ate haver ablacao empirica, os registros promovidos de
  `behavioral_scenarios_*` e `function_calling_expansion_*` sao considerados
  **EXPERIMENTAIS** e nao devem basear decisoes de qualidade do modelo; o gate 5
  (`validate_rag_contract`) permanece SKIP ate existir corpus de respostas RAG
  (depende de treino/inferencia).
