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
- **O corpus da produção, até 2026-09-21, não tinha a fonte REST API.** Causa: o corpus era de
  14/09 e a fonte entrou no repo em 18/09 (`1de2308`); `RAG_INGEST_REST_API` só existe em
  `rag_core/corpus.py`, o carregador do **lab**. Resultado medido: 80 das 423 perguntas
  (`rest-*`, `ops-*`) tinham alvo ausente e pontuavam 0 **por construção**.
- `scripts/consolidate_corpus.py` agora ingere as **duas** granularidades REST (24 famílias +
  276 operações, ids disjuntos) com `synthetic_questions` **vazio** — o MCP indexa esse campo,
  e pergunta no índice é vazamento de gabarito. Ele também captura tudo que há em
  `data/evidence/*.jsonl`: regenerar depois de gravar evidência muda o corpus. Por isso há
  `SKIP_REST_API=1` (só a fonte REST) e a evidência é gravada em `.jsonl`, não `.json`.
- `TWS_CORPUS_FILE` troca o corpus da produção **só para medição** (default inalterado).

## Medir a produção (antes de concluir qualquer coisa sobre o sistema)

```bash
python3 data/eval/measure_producao_pool423.py                      # default = produção
HF_HOME=/tmp/hf python3 data/eval/measure_producao_pool423.py       # ponte EN->PT ligada
```

Medido em 2026-09-21 (pool 423, corpus corrigido de 7381 docs):
- produção, ponte OFF: **@1 209 (49,4%) | @3 250 | @5 265 (62,6%) | @10 293 | MRR 0,5588**,
  alvo ausente 22 (5,2%), **27 ms/pergunta**;
- com a ponte ON: **@1 215 (50,8%) | @5 271 | MRR 0,5738**, mas **156 ms/pergunta**. Pareado
  @1 +8/−2 p=0,11 (positivo, **não** significativo).
- Antes do conserto de corpus era @1 202 (47,8%) / @5 256 / MRR 0,5381 / **82 ausentes**.
- O lab bate a produção por 38/67 (p=0,0060) no corpus antigo. **Não** inferir a produção a
  partir das 24 perguntas EN — isso já deu errado uma vez (n=24 não generaliza).
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
- **Nunca indexar resultado de medição por `id` de pergunta.** O pool tem **423 linhas mas 413
  ids**: 10 rótulos `blind-XXXX` são reusados por perguntas **distintas** (6 com alvos
  diferentes). Um dicionário por id colapsa 10 linhas e qualquer contagem por subconjunto sai
  errada. Indexar pela **posição da linha**.
- A fatia `ops-*` está em **0/40 @1 e 0/40 @5** com BM25, mesmo com os alvos presentes no
  índice: dos 21 alvos que a fonte de operações tornou presentes, só 1 chega ao top-5 (os
  outros caem em ranks 18, 89, 202, 900, 1237, 7065). Causa medida: os registros de operação
  são **texto de spec OpenAPI em inglês** e as perguntas são PT-BR; mediana de sobreposição de
  tokens **0,00**, com 21/40 casos zerados. Não é ajuste de peso — é falta de sinal.
- **A produção é BM25 puro: não há ramo denso** em `mcp_server/tws_expert_mcp.py`. O repo já
  mediu (18/09) que o denso (BGE-M3) faz **13/40 @1** nessa fatia contra **1/40** do BM25 — mas
  o veredito de 20/09 diz que a **fusão** densa **piora** no conjunto grande (202×181 em 296,
  p=0,0111). Denso com **roteamento por fatia** nunca foi testado nem ligado na produção: é
  `UNKNOWN`, não um ganho disponível.

## O que funciona

- `RAG_BM25_REAL=1` é o único ganho que transfere: @1 +5/+4/+3 e @5 +12/+4/+3 em 3/3
  benchmarks; combinado (n=493) @5 p=0,0201 significativo, @1 p=0,28 não significativo.
- Ponte EN→PT (`RAG_TRADUZ_EN`) só tem ganho medido no **catálogo de mensagens**; em 5
  domínios testados, 0 com ganho significativo e 2 com sinal negativo. Não vender como ganho geral.

## `UNKNOWN` (não afirmar sem medir)

- **Denso com roteamento por fatia** (rest/ops) na produção, no pool 423. Maior teto conhecido,
  nunca medido no caminho real.
- **Lab × produção final (7381)**: o pareado contra o corpus +REST deu 44/64 (p=0,0670), contra
  38/67 (p=0,0060) antes — mas ninguém mediu lab × produção **final**.
- **Taxa de disparo da ponte** e o efeito numa fatia EN (este pool é majoritariamente PT-BR).
- As **20 perguntas** que nem lab nem produção acham (o lab tem o doc para 2 delas).
