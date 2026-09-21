# Registro da sessão — 2026-09-21

Continuação da sessão de 2026-09-20. Duas frentes pedidas: **generalização da ponte EN→PT**
e **a ordem (o gargalo do top-1)**. Todo número abaixo veio de execução registrada; o que
não foi medido está marcado como `UNKNOWN`.

Controle reproduzido antes e depois de cada mudança, em todas as seções:
**230 @1 / 287 @5 / MRR 0,6016** no pool de 423.

> Ressalva sobre o nome: o projeto já tem um `README.md`, então este registro tem nome
> próprio para não sobrescrevê-lo.

---

## 1. O controle foi RECONSTRUÍDO (o pool de 423 tinha desaparecido)

O pool de 423 perguntas usado em toda a medição anterior vivia em `/tmp/ragexp/attrib3/pool.jsonl`
e foi **perdido** (diretório volátil). Ele é reconstruível: `lex_summary.json` guarda `id` e
`question` de cada uma das 423 entradas, e **todos os 423 ids existem nos benchmarks do repo**.

- `data/eval/reconstroi_pool423.py` refaz o pool casando `(id, question)` contra as fontes.
- `data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl` — 423 linhas,
  md5 `119b61b596948e30cdf6b25655aa3268`.
- O summary de origem (`lex_summary.json`) existia **só em `/tmp`** — a mesma armadilha que
  perdeu o pool. Foi copiado para `data/evidence/pool423-lex-summary-2026-09-21.json`, e o
  script usa esse arquivo por padrão. Reconstruir agora não depende de `/tmp`.
- **Teste de verdade:** rodar o harness nesse arquivo devolve
  `230/423 @1, 287/423 @5, 301/423 @10, MRR 0,6016` — idêntico ao registrado. Se não
  devolvesse, a reconstrução estaria errada e não serviria.

Isso resolve a dependência de `/tmp` para o conjunto principal de medição.

---

## 2. Trilha A — a ponte EN→PT **não generaliza** (medido)

O ganho registrado (+29pp @1) estava medido em **24 perguntas de um domínio só** (catálogo
de mensagens). Para testar generalização, gerei perguntas EN de outros domínios traduzindo
os benchmarks PT existentes (`opus-mt-ROMANCE-en`), **preservando o gabarito**: só o campo
`question` muda, com `assert` de que `relevant_claim_ids` e `expected_answer` são idênticos
ao original.

Cada domínio foi medido nos três cenários, no harness, com o mesmo gabarito:

| domínio | n | PT | EN (sem ponte) | EN→PT (com ponte) | ganha/perde @1 | p |
|---|---|---|---|---|---|---|
| catálogo de mensagens (controle) | 24 | 8 | 2 | 7 | — | 0,125 |
| API REST | 40 | 4 | 3 | 4 | 3/2 | 1,000 |
| planejamento de modelo | 70 | 53 | 38 | **35** | 10/13 | 0,678 |
| instalação/upgrade | 39 | 28 | 16 | 23 | 11/4 | 0,119 |
| mensagens (pure_virgin) | 39 | 36 | 24 | **23** | 3/4 | 1,000 |

**Veredito: 0 de 5 domínios com ganho significativo; 2 de 5 com sinal negativo.**
A recuperação do PT fica entre 64% e 100%, mas nenhuma diferença passa de ruído. O melhor
sinal (+7 em instalação/upgrade) tem p=0,119 — **não conclusivo, não é ganho**.

O que isso significa na prática: a ponte continua **correta e útil** para o domínio onde foi
medida (catálogo de mensagens, onde `EN 2 → 7`), mas ela **não deve ser vendida como ganho
geral**. Não há evidência de que ela ajude fora do catálogo.

---

## 3. Trilha B — as três hipóteses de boost foram FALSIFICADAS

A análise de erro mostrou o mecanismo: nas **84 perguntas com alvo em rank 2–15**, o
documento que fica em #1 é `canonical_claim` em 49 casos, enquanto o alvo que perde é
`message_catalog` (24) ou `rest_api_surface` (11). Ou seja, **o ranking ordena por
autoridade/tipo, não por relevância** — a ordem dos multiplicadores do 1º estágio
(`canonical 1.25 > lab 1.20 > ragflow 1.15 > msgcat 1.10`) aponta na mesma direção do erro.

Também testei e **descartei** a hipótese de tamanho: o vencedor é maior que o alvo em 43
casos e menor em 40 — não explica nada.

Testei cada alavanca de forma isolada. Todas **pioram**:

| hipótese | pool 423 @1 | blind_v3 @1 | golden_qa @1 | veredito |
|---|---|---|---|---|
| `RAG_AVG_DL=46.9` (avg_dl **real** medido) vs 60 hardcoded | −4 | −3 | −2 | **falsificada** |
| `RAG_AVG_DL=40` | −7 (p=0,039) | −6 | −5 | piora |
| `RAG_RERANK_ADAPT` (bônus escalado pela escala do pool), todo K | −2 | 0 | 0 | **falsificada** |
| `RAG_TYPE_PRIOR=flat` (iguala os multiplicadores) | −5 | −3 | −2 | **falsificada** |

Detalhe que importa: o `avg_dl` **real medido é 46,9** (|set(tokens)| sobre 7019 docs),
contra 60 hardcoded. Mesmo assim, corrigir para o valor "certo" **piora de forma consistente
nos três benchmarks**. Isso mostra que o 60 não é um erro de digitação: é um parâmetro de
calibração embutido do scorer legado, e "consertar a teoria" quebra o resultado.

Da mesma forma, os bônus adaptativos dão **resultado idêntico em todos os K de 1 a 20**
(escala real do pool medida: 3,8–9,2; top-1: 5,1–12,5) e sempre ligeiramente pior. A
hipótese de que a escala das constantes fixas era o defeito não se sustenta.

### Correção de uma conclusão anterior (retratação)

A sessão de 2026-09-20 deixou pendente: *"13/14 falhas no top-10 mas rank 2–9 → é a escala
dos bônus do 2º estágio"*. **Isso foi testado agora e está errado.** Corrigir a escala
**piora**. A conclusão anterior não sobrevive à medição; retiro a atribuição.

---

## 4. O achado que reformula o problema: **lab e produção medem scorers diferentes**

O `rag_core/lexical.py` (usado pelo harness e por toda a medição anterior) é documentado no
próprio código como **não sendo BM25**: `tokenize()` devolve `set()`, o que **destrói a
frequência do termo (TF)**; **não há IDF**; e `avg_dl=60` está hardcoded.

Mas o **buscador de produção** (`mcp_server/tws_expert_mcp.py`, `search_bm25`) **já é BM25
de verdade**: conta TF por `postings[t].append((idx, count))`, calcula IDF de Robertson
(`log((N - df + 0.5)/(df + 0.5) + 1)`), deriva `avgdl` do corpus, usa `k1=1.5`.

Ou seja: **o laboratório estava medindo um scorer que a produção não usa.** Medi os dois, mais
o BM25 real ligado no harness, nas **mesmas 24 perguntas EN**:

| caminho | @1 | @5 |
|---|---|---|
| harness legado (sem TF, sem IDF) | 2/24 (8,3%) | 3/24 (12,5%) |
| harness com `RAG_BM25_REAL=1` | 4/24 (16,7%) | 9/24 (37,5%) |
| **MCP de produção** (BM25 real) | **6/24 (25,0%)** | **12/24 (50,0%)** |

ATENÇÃO ao ler: **os `6/24 @1` e `12/24 @5` são a MESMA corrida** (a do MCP, com a ponte
DESLIGADA). Não são "@1 sem ponte, @5 com ponte" nem dois experimentos. E este `6/24` é
justamente o ponto de partida da ponte: com a ponte ligada o MCP vai a **13/24 @1 e
17/24 @5** (medido e registrado na sessão 2026-09-20).

prova que os três indexam o mesmo gabarito: 24/24 ids-alvo presentes nos dois índices.

### Ligar o BM25 real no harness: o único ganho que transfere

| benchmark | @1 antes → depois | @5 antes → depois |
|---|---|---|
| pool 423 | 230 → **235** (+5) | 287 → **299** (+12) |
| blind_v3 (262) | 182 → **186** (+4) | 221 → **225** (+4) |
| golden_qa (70) | 53 → **56** (+3) | 64 → **67** (+3) |

**Direção positiva em 3 de 3 benchmarks, em @1 e em @5.** Combinado (pool 423 + golden_qa,
sem dupla contagem, n=493):

- **@5: 351 → 366, ganha 26 / perde 11, p=0,0201 → SIGNIFICATIVO**
- @1: 283 → 291, ganha 25 / perde 17, p=0,280 → não significativo

Leitura honesta: há **ganho significativo de recall no top-5** e um ganho de @1 que é
positivo e consistente mas ainda **não passa de ruído estatístico** com este n. Não é para
declarar vitória no top-1; é para declarar que a similaridade base importa mais que os boosts.

Importante: **isso não autoriza mudar produção.** A produção já usa BM25 real; o switch só
reduz a distância entre o que medimos e o que serve.

---

## 5. O que fica (tudo opt-in, default = comportamento inalterado)

Três switches de MEDIÇÃO, todos validados: valor inválido **falha alto** em vez de silenciar
(lição do `RAG_REST_GRANULARITY`, onde um valor errado produziu falso negativo).

| switch | onde | default | efeito |
|---|---|---|---|
| `RAG_AVG_DL=<float>` | `rag_core/config.py` | 60 | muda o `avg_dl` do 1º estágio; `0` desliga a normalização |
| `RAG_TYPE_PRIOR=flat` | `rag_core/config.py` + `lexical.py` | `on` | iguala os multiplicadores de tipo em 1,0 |
| `RAG_RERANK_ADAPT=<float>` | `data/eval/evaluate_rag_benchmark.py` | 0 (off) | bônus do 2º estágio proporcionais à escala do pool |

Com os defaults, o controle segue **bit-idêntico**: 230/287/0,6016, verificado depois de
todas as edições. Nenhuma mudança de produção (`mcp_server/`) foi feita nesta sessão.

Instrumentos persistidos no repo (antes viviam só em `/tmp`):

- `data/eval/reconstroi_pool423.py` — reconstrói o pool a partir de `lex_summary.json`
- `data/eval/measure_escala_e_bm25_real.py` — matriz BM25 real × escala adaptativa
- `data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl` — o pool de 423
- `data/evidence/lab-validation-2026-09-21-*.json` — os resultados brutos de cada medição
  (`.json`, não `.jsonl`, de propósito: não entram no corpus)

---

## 5b. A PRODUÇÃO foi medida no pool de 423 (a lacuna mais importante fechou)

Não existia instrumento que dirigisse o buscador real (`mcp_server.search_bm25`). Criei
`data/eval/measure_producao_pool423.py`. **Validação**: nas 24 perguntas EN ele reproduz
exatamente o registrado (6/24 @1, 12/24 @5).

| sistema | @1 | @3 | @5 | @10 | MRR | alvo ausente |
|---|---|---|---|---|---|---|
| lab (controle, corpus do lab) | 230 (54,4%) | — | 287 (67,8%) | 301 | 0,6016 | 47 (11,1%) |
| **produção** (corpus de 14/09, 7019 docs) | **202 (47,8%)** | 240 | **256 (60,5%)** | 281 | 0,5381 | **82 (19,4%)** |
| **produção final** (corpus corrigido, 7381) | **209 (49,4%)** | 250 | **265 (62,6%)** | 293 | 0,5588 | **22 (5,2%)** |
| produção final, com a ponte EN→PT | 215 (50,8%) | 257 | 271 (64,1%) | 299 | 0,5738 | 22 (5,2%) |

Pareado: **lab bate a produção antiga por 38 a 67 (p=0,0060)**. A produção era pior que o
laboratório — **não** melhor, ao contrário do que as 24 perguntas EN sugeriam. Minha
inferência anterior (n=24) está **corrigida**: n=24 não generalizou para n=423.

## 5c. A maior alavanca era COBERTURA — e ela foi corrigida

**O corpus que a produção consome não tinha a fonte REST API.** Causa, por medida:

- os alvos das 40 perguntas `rest-*` e das 40 `ops-*` existem em
  `data/knowledge/rest-api-derived(+-ops).jsonl` e **não** existiam no corpus de produção;
- o corpus foi commitado em **14/09 18:16**; a fonte REST entrou em **18/09 11:59**
  (`1de2308`) — **4 dias depois**. O switch `RAG_INGEST_REST_API` só existe em
  `rag_core/corpus.py`, o carregador do **laboratório**;
- **80 das 423 perguntas (18,9%) pontuavam 0 por construção** — o alvo não estava no índice.
  Não era falha de recuperação.

**Correção aplicada** em `scripts/consolidate_corpus.py` (o corretor de corpus), agora
ingerindo as **duas** granularidades REST: 24 famílias + 276 operações, ids **disjuntos**
(verificado), com `synthetic_questions` vazio de propósito — o MCP indexa esse campo, e
pergunta no índice seria vazamento de gabarito. Também corrigi um `base_dir` **hardcoded**
(o script só rodava na máquina do autor) e adicionei verificação de que a regeneração é
**puramente aditiva**: 359 novos, **0 alterados, 0 removidos**.

**Varredura de vazamento**: **0 das 423** perguntas aparece literalmente no texto indexado, em
todas as variantes testadas — inclusive com os 59 registros de evidência que a regeneração
também capturou.

Efeito medido (pareado, por linha):

| passo | @1 | @5 | @10 | MRR |
|---|---|---|---|---|
| só famílias REST (7102) | ganha 7 / perde 1, p=0,07 | **ganha 10 / perde 1, p=0,0117** | **+14/−0, p=0,0001** | +0,0200 |
| + operações (7381) | +1 / −0, p=1,0 | +2 / −2, p=1,0 | — | +0,0007 |

Resultado final: **@1 202 → 209, @5 256 → 265, alvo ausente 82 → 22 (5,2%)**.

## 5d. Mas cobertura resolvida ≠ recuperação resolvida — e o motivo é cross-lingual

O passo das 276 **operações** reduz os alvos ausentes de 43 para 22 e **não move métrica**
(@1 +1, @5 +2/−2, p=1,0). Não é inutilidade: dos **21 alvos** que a operação tornou
*presentes*, **apenas 1 entra no top-5** — os outros caem nos ranks **18, 89, 202, 900, 1237,
7065**. A fatia `ops-*` está em **0/40 @1 e 0/40 @5**.

**Causa, medida antes no próprio repo** (`lab-validation-2026-09-18-benchmark-por-operacao…`):
os registros de operação são **texto da spec OpenAPI em inglês** e as perguntas são PT-BR.
Sobreposição de tokens pergunta↔alvo: **mediana 0,00**, com **21 dos 40 casos zerados**. Sem
termo compartilhado, o BM25 não tem sinal — por construção, não por ajuste de peso.

E o registro irmão (`…busca-densa-bge-m3-cross-lingual…`) já havia medido, **no mesmo corpus e
nas mesmas 40 perguntas**: BM25 **1/40 @1**; ramo **denso puro (BGE-M3) 13/40 @1 (32,5%)**,
29/40 @10, MRR 0,4649. O pior rank do denso é **11**; o único acerto do BM25 caiu no rank
**1447**. Conclusão literal daquele registro: a travessia PT→EN *"o ramo denso faz, e o ramo
denso simplesmente não estava sendo usado"*.

**Verificado agora**: o MCP de produção é **BM25 puro — zero menções a embedding/BGE/denso**.
Ou seja, o achado de 18/09 nunca chegou à produção.

**Mas eu não vou vender essa alavanca como ganho, porque há uma tensão não resolvida no
repo**: o veredito de 20/09 (`…dense-fusion-pooled-verdict`) mediu a **fusão** densa em 296
perguntas e ela **piora de forma significativa** (lexical 202/296 contra fusão 181/296,
p=0,0111), com direção incoerente entre conjuntos. Então: o denso resolve a fatia
cross-lingual **e** a fusão densa global perde. O desenho que **nunca foi testado** é denso
com **roteamento por fatia** em vez de fusão global — e o denso **nunca foi ligado na
produção** para medir no pool de 423. Isso é `UNKNOWN`, não promessa.

## 5e. A ponte EN→PT no pool inteiro: direção positiva, não significativa

Medida na produção, no pool de 423, com o corpus corrigido:

- ponte OFF: @1 209 (49,4%), @5 265, MRR 0,5588 — **27 ms/pergunta**
- ponte ON: @1 215 (50,8%), @5 271, MRR 0,5738 — **156 ms/pergunta**

Pareado por linha: @1 **ganha 8 / perde 2 (p=0,1094)**; @5 **ganha 7 / perde 1 (p=0,0703)**;
MRR **+0,0151**. **Positivo em @1, @3, @5, @10 e MRR ao mesmo tempo** — mais coerente que
qualquer alavanca já falsificada — mas **dentro do ruído** em n=423, e **6× mais lenta**.
O pool é majoritariamente PT-BR, onde a ponte nem dispara; o efeito deveria ser maior numa
fatia EN, que este pool não tem.

## 6. UNKNOWN (não medido — não inventar)

- **Denso com roteamento por fatia (rest/ops) na produção, no pool 423.** A alavanca com maior
  teto conhecido (13/40 @1 contra 1/40 do esparso na fatia), mas o denso **nunca** foi ligado na
  produção e a fusão global já foi falsificada. Não afirmar ganho sem medir.
- **Taxa de disparo da ponte e o efeito na fatia EN** do pool (que não existe neste pool).
- **Efeito de ranking puro do conserto de corpus**, separado da cobertura.
- **As 20 perguntas que nem lab nem produção acham** (o lab tem o doc para 2 delas).
- **Se o lab ainda bate a produção corrigida**: o pareado lab × produção +REST deu 44/64
  (p=0,0670), contra 38/67 (p=0,0060) antes — deixou de ser significativo, mas ninguém mediu
  lab × produção **final** (7381) ainda.
