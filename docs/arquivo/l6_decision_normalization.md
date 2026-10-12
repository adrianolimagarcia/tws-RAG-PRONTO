# Level-6 — Decisão formal: normalização de termos técnicos (2026-08-28)

## Resultado

**NÃO integrado em produção.**

A normalização determinística (Layer 1) + índice de termos canônicos (Layer 2)
melhora o ranking **híbrido puro (pré-rerank)** em todos os golds, mas o
cross-encoder do Level-5 (produção) já resgata a robustez léxica que o Level-6
oferece, e pós-rerank o candidato empata ou perde marginalmente — falhando os
critérios de aceitação quando medidos com paridade de produção (pós-rerank).

## Evidência

### Gold parafraseado (5116 queries, bonus 2.0)

| Variante | Pré-rerank R@1 | Pós-rerank R@1 | Pré MRR | Pós MRR |
|----------|---------------:|---------------:|--------:|--------:|
| baseline | 63.00% | 64.29% | 0.7402 | 0.7469 |
| l1 | 63.02% | 64.27% | 0.7398 | 0.7467 |
| l12 | **65.66%** | 63.51% | **0.7602** | 0.7441 |
| Δ l12 vs baseline | **+2.66pp** | **-0.78pp** | **+0.0200** | **-0.0028** |

### Gold template (5116 queries, bonus 2.0)

| Variante | Pré-rerank R@1 | Pós-rerank R@1 | Pré MRR | Pós MRR |
|----------|---------------:|---------------:|--------:|--------:|
| baseline | 57.49% | 57.53% | 0.6888 | 0.6882 |
| l12 | **60.36%** | 56.63% | **0.7106** | 0.6848 |
| Δ l12 vs baseline | **+2.87pp** | **-0.90pp** | **+0.0218** | **-0.0034** |

### Gold perturbado (5116 queries, 754 corrompidas, bonus 2.0)

| Variante | Pré-rerank R@1 | Pós-rerank R@1 | Pré MRR | Pós MRR |
|----------|---------------:|---------------:|--------:|--------:|
| baseline | 60.46% | 62.57% | 0.7153 | 0.7317 |
| l12 | **63.37%** | 62.28% | **0.7376** | 0.7317 |
| Δ l12 vs baseline | **+2.91pp** | **-0.29pp** | **+0.0223** | 0.0000 |

### Por tipo de perturbação (R@1)

| Perturbação | Base pré | l12 pré | Δ pré | Base pós | l12 pós | Δ pós |
|-------------|---------:|--------:|------:|---------:|--------:|------:|
| none | 63.0% | 65.7% | +2.7pp | 62.2% | 61.9% | -0.3pp |
| case_scramble | 72.1% | 73.5% | +1.4pp | 87.8% | 88.1% | +0.3pp |
| code_truncation | 11.3% | 21.1% | **+9.8pp** | 54.4% | 53.9% | -0.5pp |
| hyphen_space_swap | 42.9% | 47.5% | +4.6pp | 46.2% | 45.8% | -0.4pp |
| camelcase_flatten | 38.9% | 22.2% | -16.7pp | 38.9% | 38.9% | 0.0pp |

## Interpretação

1. **O Level-6 funciona pré-rerank**: resgata códigos truncados (+9.8pp em
   `code_truncation`) e separadores multiword (+4.6pp em `hyphen_space_swap`),
   exatamente as falhas do tokenizador BM25 baseline.
2. **O reranker (Level-5) já cobre essa robustez**: em `code_truncation`, o
   baseline pula de 11.3% → 54.4% R@1 pós-rerank. O cross-encoder entende a
   query truncada semanticamente, tornando a normalização léxica redundante.
3. **Pós-rerank, o term index adiciona candidatos que o reranker rankeia pior**,
   resultando em ligeira perda de R@1 (parafraseado -0.78pp, perturbado
   -0.29pp) com ganho marginal de R@5 (+0.18pp, +0.26pp).
4. **`camelcase_flatten` regride -16.7pp pré-rerank** (n=18): o split de
   camelCase emite formas divididas que o índice não associa ao termo já
   dividido da query. Amostra pequena, mas indicativa de ruído do boost.

## Critérios de aceitação (paridade de produção, pós-rerank)

| Critério | Pré-rerank | Pós-rerank | Resultado |
|----------|-----------:|-----------:|-----------|
| Parafraseado R@1 ≥ +1pp ou MRR ≥ +0.01 | ✅ +2.66pp / +0.0200 | ❌ -0.78pp / -0.0028 | **falha** |
| Parafraseado R@5 sem regressão > 1pp | ✅ +0.90pp | ✅ +0.18pp | passa |
| Template R@1 ≥ +1pp ou MRR ≥ +0.01 | ✅ +2.87pp / +0.0218 | ❌ -0.90pp / -0.0034 | **falha** |
| Perturbado R@1 ≥ +2pp vs baseline | ✅ +2.91pp | ❌ -0.29pp | **falha** |

## Causa da falha registrada

Ganho pré-rerank anulado pelo reranker de produção; pós-rerank o candidato
regride R@1 nos três golds (parafraseado -0.78pp, template -0.90pp,
perturbado -0.29pp). Fuzzy matching dispara pouco (6 fuzzy / 48.536 exact no
parafraseado) e não é o fator decisivo; o fator é a neutralização do boost
pelo cross-encoder.

## Estado final

- Produção **inalterada**: `scripts/rag_retrieval_eval_hybrid.py` e
  `scripts/rag_retrieval_eval_on_gold.py` mantêm `hybrid_bm25_rrf_vector_topic_rerank`.
- Scripts experimentais preservados: `scripts/rag_term_normalize.py`,
  `scripts/build_perturbed_gold.py`.
- Benchmark preservado: `data/sft/eval_perturbed_paraphrased.jsonl`.
- Artefatos: `data/rag/l6_*.json`.
- Nenhum commit criado.

## Artefatos

| Artefato | Descrição |
|----------|-----------|
| `scripts/rag_term_normalize.py` | Script experimental (baseline/l1/l12, `--bonus`, `--rerank`) |
| `scripts/build_perturbed_gold.py` | Gerador de benchmark de perturbações |
| `data/sft/eval_perturbed_paraphrased.jsonl` | Gold perturbado (5116 queries, 754 corrompidas) |
| `data/rag/l6_exp_paraphrased.json` | Sweep bonus 0.5 pré-rerank |
| `data/rag/l6_exp_paraphrased_nobonus.json` | Sweep bonus 0.0 pré-rerank |
| `data/rag/l6_exp_para_bonus{10,15,20}.json` | Sweep bonus 1.0/1.5/2.0 pré-rerank |
| `data/rag/l6_exp_template_bonus20.json` | Template bonus 2.0 pré-rerank |
| `data/rag/l6_exp_perturbed.json` | Perturbado pré-rerank |
| `data/rag/l6_exp_para_bonus20_rerank.json` | Parafraseado pós-rerank |
| `data/rag/l6_exp_perturbed_rerank.json` | Perturbado pós-rerank |
| `data/rag/l6_exp_template_bonus20_rerank.json` | Template pós-rerank |
| `docs/l6_decision_normalization.md` | Este documento |
