# SPEC — Release SOTA (P0–P6)

Especificação técnica dos componentes novos. Convenções: Python 3.10+,
stdlib-first (sem dependências novas), UTF-8, JSONL. Toda escrita atômica
(arquivo `.next` + `replace`).

## P0 — Release imutável

### `scripts/release_snapshot.py`

Fluxo:
1. Ler `config.yaml` → `release.id` (ex.: `r17-sota`), `release.generator`
   (ex.: `release_snapshot.py@<commit>`), `release.source_root`.
2. Criar `data/releases/<release.id>-<YYYYmmdd-HHMMSS>/`.
3. Copiar artefatos canônicos (lista em `RELEASE_FILES`):
   - `data/evidence/claims.jsonl`
   - `data/evidence/automation-action-registry.json`
   - `data/sft/approved.jsonl`, `candidates.jsonl`,
     `community_practice_approved.jsonl`, `function_calling_candidates.jsonl`
   - `data/sft/eval_independent.jsonl`
   - `data/sft/train.jsonl`, `validation.jsonl`, `test.jsonl`
   - `data/sft/split_manifest.json`
   - `data/train_full.jsonl` (corpus causal elegível)
   - `data/quality_report.json`
   - `data/ultra_sota_report.json`, `data/coverage_backlog.json`
4. Calcular SHA-256 de cada arquivo copiado (sobre o cópia, garantindo
   imutabilidade local).
5. Registrar contagens (linhas não vazias) de cada JSONL.
6. Re-executar gates rápidos e registrar exit codes:
   - `validate_evidence.py`, `validate_sft.py --file <snapshot>/approved.jsonl
     --status approved --require-risk-coverage`, `validate_eval.py` (sobre o
     snapshot), `validate_tokens.py --dir <snapshot>` (se suportado), compile.
7. Escrever `snapshot_manifest.json` com:
   ```json
   {
     "release_id": "r17-sota-20260823-...",
     "created_at": "...",
     "generator": "...",
     "files": {"name": {"sha256": "...", "lines": N, "bytes": N}},
     "gates": {"validate_evidence": 0, ...},
     "sources": ["HCL 10.2.8 docs", "lab WSL 10.2.8", ...],
     "distribution_summary": {"by_language": {...}, "by_risk": {...}, ...}
   }
   ```
8. Gravar `data/releases/latest.json` → aponta para o release id (indireção
   usada pelo config e pelo regression gate).
9. Imprimir resumo.

Invariantes:
- Nada no diretório do release é sobrescrito depois de criado (uma segunda
  execução com mesmo id falha se o diretório existe e `--force` ausente).
- O manifesto registra hashes dos arquivos **dentro** do release, não dos
  arquivos-fonte (que podem mudar depois).

### `scripts/regression_gate.py`

Compara o release atual com um release baseline (`--baseline <dir>` ou
`data/releases/latest.json`). Para cada dimensão (`language`, `version_scope`,
`risk`, `topic`, `source_url` família via `source_domain`), computa contagens
no approved do baseline vs atual e falha se:
- `risk == destructive`: qualquer queda > 0%.
- outras dimensões: queda > tolerância (default 5%, `--tolerance`).
Também compara eval count e divergência de claims.

Saída: tabela + exit 0/1. Uso: `python scripts/regression_gate.py --baseline <dir>`.

### Config

`config.yaml` ganha bloco:
```yaml
release:
  id: "r17-sota"
  approved_file: "data/releases/latest/approved.jsonl"   # via indireção
```
E `sft.approved_file` passa a apontar para `data/releases/<id>/approved.jsonl`
gerado no snapshot. O README documenta que o treino usa snapshot imutável.

## P6 — Contradição e matriz

### `scripts/contradiction_gate.py`

1. Carregar `claims.jsonl`.
2. Agrupar por `(normalized_command, version_scope)` onde `normalized_command`
   é extraído do claim_id ou do texto (ex.: `composer`, `conman sj`,
   `PRIORITY`, `jnextplan`).
3. Para cada par no mesmo grupo com status `verified`/`version_dependent`/
   `observed_in_lab`, rodar heurística de conflito:
   - escopo oposto (ex.: "não é válido" vs "é válido") via presença de
     negações (`não`, `not`, `inválido`, `rejeit`, `não suporta`).
   - versão divergente com escopo idêntico (ex.: um diz 10.2.8, outro 9.5).
   - risco divergente (read_only vs destructive) para o mesmo comando.
4. Escrever `data/evidence/contradiction_backlog.jsonl` com pares, motivo e
   status `pending_adjudication`.
5. Exit 0 se backlog vazio ou `--allow-pending`; exit 1 se novos pares
   pendentes sem adjudicação (`--require-adjudication`).

A adjudicação é manual: arquivo `data/evidence/contradiction_adjudications.jsonl`
com campos `pair_id`, `verdict` (`claim_a_wins`|`claim_b_wins`|`both_scope`|
`needs_revision`), `rationale`, `adjudicated_by`, `adjudicated_at`.

### `scripts/support_matrix.py`

Gera `data/evidence/support_matrix.json`:
```json
{"claims": [{"claim_id": ..., "version": ..., "platform": ..., "status": ...,
             "evidence_tier": ..., "risk": ..., "topic": ..., "has_lab": bool}],
 "grouped": {"<version>": {"<platform>": {"<status>": N}}}}
```

### Reequilíbrio PT/EN (P6)

`scripts/balance_holdout_language.py` (ou extensão do split):
- Relatório: contagem de approved por `(language, source_family)`.
- Holdout `test.jsonl` rebalanceado para PT/EN ≈ 50/50 por família de fonte,
  mantendo família connected (não separar paráfrases do mesmo claim).
- Só rebalanceia se não quebrar o gate anti-vazamento (reusa lógica do
  `split_sft.py`).

## P1 — Blind eval set

### `scripts/build_blind_eval.py`

Gera `data/eval/blind_eval_seed.jsonl` a partir de claims + eval gold:
- 9 famílias (tag `family`):
  1. `no_evidence` — pergunta sem evidência no corpus.
  2. `false_premise` — premissa falsa embutida.
  3. `wrong_version` — pede versão errada.
  4. `wrong_platform` — plataforma errada (z/OS vs Distributed).
  5. `lookalike_command` — comando parecido mas inexistente.
  6. `conflicting_sources` — fontes conflitantes (usa claims contraditórias).
  7. `empty_retrieval` — recuperação vazia.
  8. `obsolete_doc` — documento obsoleto.
  9. `mutating_destructive` — pedido mutante/destrutivo.
- Cada caso: `case_id`, `family`, `prompt`, `expected_behavior`
  (resposta correta OU recusa), `ground_truth_fact` (se aplicável),
  `evidence_ids_expected` (IDs que a resposta deve citar), `source_family`,
  `language`, `risk`.
- Separado por fonte e por família de prompt (nunca vazar claim usado no
  treino para o caso — usa apenas subjects, como `build_eval_gold`).
- 4 métricas por caso (definidas no schema):
  `metrics: ["factual_correctness", "evidence_fidelity", "citation_correct",
             "abstention_correct"]`.

### `scripts/run_blind_eval.py` (juiz LLM como triagem)

- Executa o pipeline RAG/modelo nos casos; coleta resposta + `evidence_ids`.
- Para cada métrica, pontuação 0/1 por heurística determinística (presença de
  IDs, recusa bem formada, paridade de fato via n-gramas).
- Juiz LLM opcional (Perplexity/API) apenas como **triagem**: gera sugestões;
  o veredito final é sempre por revisão humana no arquivo
  `data/eval/blind_eval_judgments.jsonl`.
- Relatório: `data/eval/blind_eval_report.json` com 4 métricas separadas.

## P2 — RAG evidence-first

### Contrato (documento + validador `scripts/validate_rag_contract.py`)

Regras por resposta:
1. Resposta factual (não-recusa) DEVE conter `evidence_ids` (lista de
   `claim_id`/`source_url`) OU marcador `[evidence: ...]`.
2. Se a recuperação não atingir limiar de (versão, plataforma) para a pergunta,
   a resposta DEVE ser de insuficiência:
   `"não há suporte suficiente no corpus disponível"` + pedido do dado ausente
   ou encaminhamento para fonte oficial.
3. Fontes `version_dependent`, `observed_in_lab`, `community` devem ser
   sinalizadas com rótulo explícito.
4. Para risco alto (mutating/destructive/credential_sensitive), resposta deve
   incluir URL/título/versão da evidência.
- Validador aceita corpus de respostas (JSONL) e reporta violações por regra.
- `docs/RAG_EVIDENCE_CONTRACT.md` descreve o contrato consumível pelo RAG.

## P3 — Expansão real

- Formato lab session em `docs/LAB_SESSION_FORMAT.md`: comando, pré-condições,
  saída sanitizada, versão, SO/plataforma, resultado, evidência (arquivo
  `lab-validation-*.jsonl`), risco, reversibilidade.
- Prioridade: mutações/destrutivas, incidentes, troubleshooting; depois
  DWC/REST, OCLI, bancos, HA, upgrades.
- Claims sensíveis novos: exigir 2 evidências independentes OU 1 oficial + 1
  execução de laboratório (`validate_evidence.py --require-corroboration`).
- Pesquisa oficial via `verify-hwa-facts`/Perplexity para preencher backlog
  `dwc_api` e `incidents` do harness.

## P4 — Sintético comportamental

- Reutilizar `teacher_provider_v2.py` + `generate_synthetic_expansion.py`.
- Alvo: claims verified com <3 candidatos sintéticos (cobertura baixa).
- Por claim: 3–5 cenários das famílias: diagnóstico, comparação, pré-condição,
  ambiguidade, versão/plataforma.
- Pares contrastivos: pergunta correta × 1 alteração errada (versão, flag,
  origem, privilégio, comando).
- Validação: `validate_synthetic_sft.py` (estrutura, termos frios, versão,
  risco, entailment via `entailment_audit.py`).
- Ablação: splits baseline vs +sintético, avaliar no blind eval e no
  `eval_independent`; só promover se melhorar sem piorar falsas recusas.
  Relatório `data/sft/experiments/ablation_<ts>.json`.

## P5 — Function calling

- Fonte de verdade: `data/evidence/automation-action-registry.json`.
- Gerar casos positivos (ação válida → schema JSON) e negativos (payload
  inválido, ação desabilitada, origem inválida, versão incompatível, parâmetro
  ausente, pedido destrutivo → recusa/confirmação).
- Medir separadamente: schema validity, ação correta, parâmetro correto,
  confirmação, recusa.
- Mutações: modelo planeja e solicita confirmação; execução fora do modelo
  (validada pelo registry). Isso é contrato, não dataset apenas.
- `scripts/expand_function_calling.py` consome registry e gera candidatos.

## Compatibilidade e rollback

- Nenhum script novo altera arquivos-fonte (apenas lê ou escreve em
  `data/releases`, `data/eval`, `data/evidence/*_backlog|*_adjudications`).
- Rollback: release anterior permanece; `data/releases/latest.json` aponta de
  volta. Nenhuma exclusão.
- Gates não mudam comportamento dos validadores existentes (apenas adicionam).
