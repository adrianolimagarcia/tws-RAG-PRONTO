# Diagnóstico de ranking Hit@1 — pool423 (Frente B)

**Escopo:** avaliação do *lab evaluator* `data/eval/evaluate_rag_benchmark.py`, não do MCP de produção. Execução informada no worktree isolado com Python 3.11.16, sem mudanças em código de produção.

```sh
RAG_DENSE_MASK_TO_CORPUS=1 RAG_INGEST_REST_API=1 PYTHONHASHSEED=0 \
RAG_BENCHMARK_FILE=data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl \
python3 data/eval/evaluate_rag_benchmark.py
```

## Resultado e replicação

| Métrica | Execução observada | `benchmark-folders-20261020.md` | Gate em `AGENTS.md` |
|---|---:|---:|---:|
| Corpus do harness | 7.191 docs | 7.191 | — |
| Perguntas | 423 | 423 | 423 |
| Hit@1 | 215 (50,8%) | 215 | 230 |
| Hit@3 | 258 (61,0%) | 258 | — |
| Hit@5 | 274 (64,8%) | 274 | 287 |
| Hit@10 | 293 (69,3%) | 293 | 301 |
| MRR | 0,5682378282 (0,5682) | 0,5682 | 0,6016 |
| Sem resposta no índice | 41 (9,7%) | 41 | — |

Reproduziu a referência da sessão folders, não o gate de `AGENTS.md`: −15 Hit@1 (−3,55 pp), −13 Hit@5, −8 Hit@10 e −0,03336 MRR contra o gate. A causa histórica do delta não foi isolada. Ambiente/versões do ramo denso podem mover métricas; a referência folders também distingue 7.191 docs do harness e 7.499 no corpus/índice MCP. Não atribuir causalidade às cinco claims sem comparação pareada sob corpus e pipeline constantes. **Resultado do avaliador de laboratório, não da produção.**

O evaluator escreveu `data/eval/eval_summary.json`, copiado para `/tmp/folder-rag-B-run.json`; restaurei o arquivo rastreado com `git checkout -- data/eval/eval_summary.json`. Pré-run restaurado: 70 details, MRR 0,8182. A saída corrente tinha agregados para 423, mas apenas 70 objetos em `details`; logo não existe decomposição íntegra por pergunta nesta execução.

## Classificação disponível — parcial, não representativa

Os 70 details `eval-*` não correspondem por posição às 423 linhas do pool (perguntas/ids diferentes). Somam 53 hits @1 e 17 erros:

| Rank do alvo | N |
|---|---:|
| 1 | 53 |
| 2–5 | 11 |
| 6–10 | 4 |
| >10 | 2 |

Entre os erros parciais, há dois em cada domínio `seguranca_rest`, `topologia_ha`, `seguranca` e `instalacao`; demais domínios têm um erro. Exemplos incluem REST/segurança, conman/composer e topologia, mas sua proporção entre os 208 erros completos é desconhecida.

| Confiança | N total (70) | Hit@1 | Erro |
|---|---:|---:|---:|
| alta | 16 | 14 | 2 |
| média | 24 | 16 | 8 |
| baixa | 30 | 23 | 7 |
| **Total** | **70** | **53** | **17** |

Não medidos: EN vs PT-BR, taxas completas por domínio/tipo (AWS messages, optman, composer/conman, REST ops, folders) e códigos TWS. O schema não contém idioma. Não cruzar por `id`: `AGENTS.md` alerta que 10 IDs blind são reutilizados; usar posição de linha.

## Rank flips e ordenação

Inspecionei os instrumentos. `diagnose_rank1_flips.py` e `attribute_ordering_flips.py` apontam para o checkout principal por caminho hard-coded; o segundo também grava `data/eval/ordering_attribution.json`. Não os executei para não cruzar isolamento nem sobrescrever artefato. `diagnose_retrieval_gap.py` importa evaluator local, mas chama `run_evaluation()` (sobrescreve `eval_summary.json`) e foi concebido para benchmark de alvo único; precisa de adaptação/saída isolada antes de uso aqui.

Evidência histórica de **outro conjunto**, `blind_v3` (262 consultas): `ordering_attribution.json` registra 7.006 docs, 183/262 @1 em ambas trilhas, max diferença de score 2,84e−14; 49 alvos em ranks 2–10, sendo 19 rebaixados pelo segundo estágio e 30 erros do scorer base. A evidência `lab-validation-2026-09-17-ordering-attribution-and-entity-boost-fix-rejected.jsonl` atribui o maior delta favorecedor do documento errado a `ss_entidade_id` em 16/19 rebaixamentos; bigrama em 2 e `ss_par_cli` em 1. Em 14/19, o errado recebeu boost de entidade sem boost no correto. Mecanismo plausível medido naquele benchmark, **não** causa comprovada dos erros deste run.

**Observado:** 41 ausentes (teto teórico 90,3% @1); agregados replicam referência de 20/10. **Não observado:** rank pré/pós-reranker por linha deste pool, margens por domínio, flips, distribuição dos 208 erros e causa do delta contra o gate. Causa-raiz do delta 230→215 não estabelecida; corpus distinto e sensibilidade ambiental são fatores de comparabilidade conhecidos, mas contribuição específica desconhecida.

## Próximos passos por bloqueio

- **Desbloqueado:** adaptar scripts para resolver repo via `__file__`/argumento e aceitar output temporário; preservar details por linha e validar Hit@k/MRR recomputados contra agregados.
- **Exige entrada humana:** recuperar ambiente/versões e artefatos da execução 230/423 para comparação pareada intra-ambiente.
- **Bloqueado por evidência ausente:** afirmar causa do delta ou taxas completas por domínio, idioma e código antes de produzir details de 423 linhas e scores pré/pós reranker.

**Status:** agregado TESTADO; classificação parcial REVIEWED; flips e atribuição integral deste pool UNVERIFIED.
