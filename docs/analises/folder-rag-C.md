# Frente C — protótipo challenger de rerank/roteamento

**Status: inconclusivo / parcialmente executado.** O objetivo era medir ablação pareada por consulta em dev e holdout, sem alterar defaults. Não publico métricas pareadas porque o avaliador só persiste `rank_raw` e `rank` agregados num artefato compartilhado, sem saída configurável preservando as 423 linhas; além disso, a execução sobrescreve `data/eval/eval_summary.json`. Relatar flips comparando runs independentes sem exportação pareada seria especulativo.

## Escopo e hipótese

A hipótese challenger mais simples seria um roteamento opt-in para estratégia densa ou refinamento de rerank, com default inalterado. Não foi introduzido código de produção nem nova flag: sem harness que mantenha saída por posição da pergunta para ambos os braços, não é possível avaliar ganho/perda por pergunta, sobretudo porque IDs repetem em benchmarks (regra em `AGENTS.md`). A restrição de não usar fusão densa global por default permanece.

## Baseline observada (dev)

Executei o controle de laboratório de `AGENTS.md`, com `PYTHONHASHSEED=0`, `RAG_DENSE_MASK_TO_CORPUS=1`, `RAG_INGEST_REST_API=1` e pool de 423. O avaliador reportou corpus de **7.191 docs**, 423 perguntas, **215/423 @1**, **258/423 @3**, **274/423 @5**, **293/423 @10**, MRR **0,5682378282**, e 41 perguntas sem resposta no índice. Reproduz a Frente B, não o gate de referência (230/423, 287/423 @5, MRR 0,6016); diferença ambiental/corpus não foi isolada.

**Não é baseline da produção.** É o harness lexical de laboratório; `AGENTS.md` documenta diferenças entre lab e MCP e proíbe inferir produção a partir desse número.

## Holdout e flips

`data/eval/holdout_100_unseen.jsonl` contém 100 linhas. Não executei baseline/challenger nela pois o harness grava `eval_summary.json`, e não mantém details integrais pareados por linha. Tampouco usei `id` para parear: IDs não são chave segura; a unidade deve ser posição.

| Conjunto | N | Ganhos @1 | Perdas @1 | Delta líquido @1 | Delta @5 | Delta MRR |
|---|---:|---:|---:|---:|---:|---:|
| Dev pool423 | 423 | não medido | não medido | não medido | não medido | não medido |
| Holdout 100 unseen | 100 | não medido | não medido | não medido | não medido | não medido |

Não existe resultado challenger; ausência de medição não é zero.

## Limitações e próximo passo seguro

1. Criar harness experimental isolado que receba benchmark e saída, execute braços sequencialmente no mesmo processo/ambiente, grave ranks por **posição**, valide agregados e preserve/restaure `eval_summary.json`.
2. Rodar ambos conjuntos com scorer, corpus, ambiente e `PYTHONHASHSEED` fixos; computar transições @1/@5 e delta de MRR por posição.
3. Só então testar hipótese challenger explícita, com flag opt-in e default seguro. Não promover sem transferência em holdout e controle de `AGENTS.md`.

## Evidência consultada

- `AGENTS.md`: invariantes, comparabilidade lab/produção, controle obrigatório e pareamento por posição.
- `docs/analises/folder-rag-A.md`: lab 7.191 vs MCP 7.499 e gaps de cobertura.
- `docs/analises/folder-rag-B.md`: baseline observada e limites do artefato.
- `data/eval/evaluate_rag_benchmark.py`: evaluator escreve `eval_summary.json`; seu fluxo não oferece caminho de saída configurável.
- `data/eval/holdout_100_unseen.jsonl`: 100 entradas.

**Conclusão:** nenhuma estratégia foi medida pareadamente ou promovida. Baseline dev reproduzida; holdout e flips **UNVERIFIED**. Nenhuma alteração de scorer/default foi feita.
