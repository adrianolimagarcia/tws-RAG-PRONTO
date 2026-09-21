# AGENTS.md — tws-RAG

Memória do repositório. O que está aqui foi **medido**; o que não foi está marcado `UNKNOWN`.

## Comandos que importam

**Controle obrigatório** (tem de dar exatamente `230/423 @1, 287/423 @5, 301/423 @10, MRR 0,6016`;
rodar antes e depois de qualquer mudança de scorer, e reverter quem quebrar):

```bash
RAG_DENSE_MASK_TO_CORPUS=1 RAG_INGEST_REST_API=1 PYTHONHASHSEED=0 \
RAG_BENCHMARK_FILE=data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl \
python3 data/eval/evaluate_rag_benchmark.py
```

- O pool de 423 é a linha de base de todo o projeto. O original vivia em `/tmp` e foi
  perdido; `data/eval/reconstroi_pool423.py` o refaz a partir de `lex_summary.json`
  (md5 esperado: `119b61b596948e30cdf6b25655aa3268`).
- `data/eval/eval_summary.json` é **artefato de execução**: `git checkout --` nele antes de
  commitar. Duas corridas em paralelo se sobrescrevem — rode sequencialmente.
- Modelos de tradução vivem em `/tmp/ragexp/hfhome` com `HF_HUB_OFFLINE=1`.

## Armadilhas do repositório

- **`rag_core/lexical.py` não é BM25** apesar do nome: `tokenize()` devolve `set` (mata o TF),
  não há IDF, e `avg_dl=60` é hardcoded, embora o real medido seja 46,9.
- **A produção (`mcp_server/tws_expert_mcp.py`) usa BM25 DE VERDADE** (TF via `postings`,
  IDF de Robertson, `avgdl` derivado do corpus, `k1=1.5`). Lab e produção medem scorers
  **diferentes** — o harness subestima a produção (mesmas 24 perguntas EN: 2/24 vs 6/24 @1).
  Não comparar número de lab com número de produção sem dizer isso.
- Corpus do lab (`load_documents()`) tem **6913** docs; o do MCP, **7019**. Não são o mesmo índice.
- **O corpus da produção está DESATUALIZADO em relação às fontes de conhecimento.** Ele é
  gerado por `scripts/consolidate_corpus.py`, que **não inclui a fonte REST API** — então os
  alvos de 80 das 423 perguntas (`rest-*`, `ops-*`) não existem no índice de produção e
  pontuam 0 por construção. `RAG_INGEST_REST_API` só afeta `rag_core/corpus.py` (lab).
  Regenerar/promover o corpus é decisão explícita, não um efeito colateral de switch.
- `TWS_CORPUS_FILE` troca o corpus da produção **só para medição** (default inalterado).
  `data/eval/augmenta_corpus_rest.py` monta a variante aumentada; o lab continua com
  `RAG_BM25_REAL=1` como melhor config.

## Medir a produção (antes de concluir qualquer coisa sobre o sistema)

```bash
python3 data/eval/measure_producao_pool423.py
TWS_CORPUS_FILE=$PWD/data/export/tws_corpus_master_with_rest_both.jsonl \
  python3 data/eval/measure_producao_pool423.py
```

Medido em 2026-09-21 (ponte OFF, pool 423): produção **202 @1 / 256 @5 / MRR 0,5381**, alvo
ausente 82 (19,4%). Com a união REST: **211 @1 / 270 @5 / MRR 0,5665**, ausente 22 (5,2%),
ganha 9 / perde 0. O lab bate a produção (p=0,0060; deixa de ser significativo com o corpus
consertado). **Não** inferir a produção a partir das 24 perguntas EN — isso já deu errado.
- `compute_bm25` e o laço de float do legado são caminho congelado: fatorar a expressão muda
  o resultado no último bit e quebra o controle. Não "otimizar" sem controle bit-idêntico.
- Switch com valor inválido deve **falhar alto** (`SystemExit`), nunca silenciar — foi assim
  que um `RAG_REST_GRANULARITY` errado produziu um falso negativo que parecia resultado.
- `data/evidence/lab-validation-*.jsonl` entra no corpus (`LAB_FILES`); evidência em `.json`
  **não** entra. Salvar resultado de medição como `.jsonl` contamina a si mesmo.

## O que já foi testado e NÃO funciona (não repetir)

Medido em pool 423 / blind_v3 / golden_qa, todos pioram quando ligados:

- `RAG_AVG_DL=46.9` (valor real) em vez de 60: @1 −4/−3/−2. O 60 é calibração, não erro.
- `RAG_RERANK_ADAPT` (bônus do 2º estágio proporcionais à escala do pool): −2/0/0, e
  resultado idêntico para todo K de 1 a 20. A tese de "constante fixa é o defeito" foi
  medida e **não** se sustenta.
- `RAG_TYPE_PRIOR=flat` (iguala os multiplicadores de tipo): −5/−3/−2. O prior de tipo
  correlaciona com o erro (o alvo que perde é `message_catalog`/`rest_api_surface`), mas
  removê-lo piora.
- Escalas de `RAG_REST_GRANULARITY` inválidas (`0`, `1`) **abortam a corrida inteira** — se
  um loop de configurações não imprime nada, é provavelmente isso, não "0/40 de verdade".

## O que funciona

- `RAG_BM25_REAL=1` é o único ganho que transfere: @1 +5/+4/+3 e @5 +12/+4/+3 em 3/3
  benchmarks; combinado (n=493) @5 p=0,0201 significativo, @1 p=0,28 não significativo.
- Ponte EN→PT (`RAG_TRADUZ_EN`) só tem ganho medido no **catálogo de mensagens**; em 5
  domínios testados, 0 com ganho significativo e 2 com sinal negativo. Não vender como ganho geral.

## `UNKNOWN` (não afirmar sem medir)

- Efeito da **ponte EN→PT** na produção no pool de 423 (medido só com a ponte OFF).
- Efeito de **ranking** do conserto de corpus separado de cobertura (os +9 vêm de perguntas
  cujo alvo não estava no índice; itens `rest-*` que apontam para o mesmo id de família inflam).
- As **20 perguntas** que nem lab nem produção acham (o lab tem o doc para 2 delas).
