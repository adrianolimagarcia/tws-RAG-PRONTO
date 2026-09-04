# PLAN — Release SOTA (P0–P6)

Ordem de execução priorizada por valor/urgência. Cada etapa tem arquivos,
alteração, testes, critério de conclusão e risco.

## Etapa 0 — Baseline de verdade
- [ ] Executar harness `all` + validadores para refrescar `ultra_sota_report.json`
      (estado atual é stale).
- [ ] Registrar contagens reais em `docs/PROGRESS.md`.
- Critério: relatório reflete 1.152 claims / 14.892 approved / 3.864 eval.
- Risco: baixo.

## Etapa 1 — P0: release imutável
- [ ] `scripts/release_snapshot.py` (novo): snapshot + manifesto SHA-256.
- [ ] `scripts/regression_gate.py` (novo): gate de regressão por dimensão.
- [ ] `config.yaml`: bloco `release`; `sft.approved_file` → snapshot.
- [ ] Gerar primeiro release; verificar AC-001/AC-002/AC-003.
- [ ] `validate_tokens.py` suportar `--dir` para snapshot (se necessário).
- Risco: médio (mudança de config); rollback trivial (indireção `latest.json`).

## Etapa 2 — P6: contradição + matriz + equilíbrio PT/EN
- [ ] `scripts/contradiction_gate.py` (novo): detecta pares conflitantes
      (ex.: PRIORITY em $JOBS); gera backlog de adjudicação.
- [ ] `scripts/support_matrix.py` (novo): matriz claim × versão × plataforma × status.
- [ ] `scripts/balance_holdout_language.py` (novo): relatório e rebalanceamento
      PT/EN por fonte (AC-010).
- [ ] Executar; registrar adjudicações pendentes (AC-006/AC-007).
- Risco: médio (falsos positivos de contradição); calibrar heurística.

## Etapa 3 — P1: blind eval set
- [ ] `scripts/build_blind_eval.py` (novo): seed de ≥300 casos, 9 famílias,
      4 métricas.
- [ ] `scripts/run_blind_eval.py` (novo): runner com heurísticas + triagem LLM.
- [ ] Gerar seed; validar schema (AC-004).
- Risco: médio (vazamento); reusa anti-vazamento do build_eval_gold.

## Etapa 4 — P2: RAG evidence-first
- [ ] `docs/RAG_EVIDENCE_CONTRACT.md` (novo): contrato consumível.
- [ ] `scripts/validate_rag_contract.py` (novo): valida respostas (AC-005).
- Risco: baixo (contrato + validador, sem mudança em dados).

## Etapa 5 — P3: expansão real
- [ ] `docs/LAB_SESSION_FORMAT.md` (novo): formato de lab session.
- [ ] Pesquisa oficial (Perplexity/verify-hwa-facts) para `dwc_api`/`incidents`
      e claims sensíveis; registrar candidatos em `data/incoming/`.
- [ ] Aplicar `--require-corroboration` em release com ações sensíveis.
- Risco: médio (depende de lab/perplexity); entregável é backlog + formato.

## Etapa 6 — P4: sintético comportamental
- [ ] Mapear cobertura sintética por claim (script de análise).
- [ ] Gerar 3–5 cenários comportamentais por claim de cobertura baixa.
- [ ] Gerar pares contrastivos.
- [ ] Validar (estrutura, termos frios, versão, risco, entailment).
- [ ] Ablação baseline vs +sintético no blind eval/holdout.
- Risco: alto (pode inflar sem ganho); gate de ablação decide promoção.

## Etapa 7 — P5: function calling
- [ ] `scripts/expand_function_calling.py` (novo): consome registry, gera
      positivos/negativos.
- [ ] Validar com `validate_function_calls.py`; medir 5 métricas.
- Risco: médio (depende do produto chamar tools — registry existe).

## Etapa 8 — Release final + documentação
- [ ] Reexecutar harness + todos os validadores.
- [ ] Gerar release final; atualizar README, PROGRESS, runbook.
- [ ] Registrar decisões/limitações em `docs/DECISIONS_SOTA_RELEASE.md`.
- Critério: todos os gates verdes; AC-001..AC-010 atendidos ou
  PARTIALLY_VERIFIED com justificativa.
