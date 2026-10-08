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

---

# Adendo (commit e93e2cd): o denso foi implementado na produção — e a fusão foi FALSIFICADA

O ramo denso não existia em `mcp_server/tws_expert_mcp.py`. Ele agora existe, **opt-in**
(`RAG_DENSE_MODE=fuse`), com `mcp_server/tws_dense.py`, `scripts/build_dense_index_mcp.py` e o
índice `data/indexes/mcp_bge_m3.pt` (7381 × 1024, derivado e no `.gitignore`).

## O que a medição mostrou (duas medições, mesmo caminho real `handle_tool_call`)

**Medição 1 — pool 423.** A fusão *parece* ganhar, e de forma robusta:

| modo | @1 | @5 | @10 | MRR |
|---|---|---|---|---|
| off (BM25 + ponte) | 215 | 271 | 299 | 0,5738 |
| fuse (RRF + denso) | **225** | **308** | **349** | **0,6243** |

@1 ganha 37 / perde 27, p=0,26; **@3 283 vs 257, @5 308 vs 271, @10 349 vs 299 (todos
p<0,0001)**. E sobrevive à descontaminação: no subconjunto sem vazamento (n-grama pergunta↔alvo
≤ 4, n=328) o MRR ganha **+0,0605**. A fatia `ops` sai de 1/40 para 10/40 @5; `rest` de 8 para 21.

**Medição 2 — os 10 conjuntos independentes do repo (n=450).** A fusão **REGRIDE**:

| conjunto | off @1 | fuse @1 | delta |
|---|---|---|---|
| mensagens | 50 | 31 | **−19** |
| holdout_100 | 79 | 69 | **−10** |
| holdout_qa_30 | 8 | 6 | −2 |
| holdout_40 / realistico / pure_virgin | 22/22/26 | 21/21/25 | −1 cada |
| geral_70 | 47 | 49 | +2 |
| virgem+mensagens | 17 | 20 | +3 |
| virgem_INGLES | 14 | 17 | +3 |
| virgem_expandido | 24 | 30 | +6 |
| **AGREGADO** | **309** | **289** | **−20 (McNemar p=0,0308 contra a fusão)** |

## Por que o pool 423 enganou

Composição. O pool 423 é **54% `blind_v3`** (227 linhas), onde a fusão quase não move o ranking
(158→155 @1), mais a fatia sintética `rest/ops`, onde ela ganha muito. Um pool dominado por um
benchmark que **não se move**, somado a uma fatia onde a fusão ganha, produz um ganho agregado
que **não existe** nos conjuntos medidos independentemente. É literalmente o *"o pior critério é
a média"* que o gate de promoção v4 deste repo existe para barrar.

O resultado de 20/09 (laboratório, corpus pré-REST, 202×181, p=0,0111) **não caducou**: a fonte
REST não o reverteu. Meu experimento o reproduz, no corpus atual e pelo caminho real.

## Decisão

**Default permanece `off`** (BM25 + ponte). Verificado: reproduz 215/257/271/299, MRR 0,5738,
ausente 22 — idêntico ao registrado. A fusão fica **opt-in**. Onde ela ganha de forma
consistente em **duas medições independentes**: benchmark virgem de **mensagem em inglês**
(@1 +3, @5 +4) e `virgem_expandido` (@1 +6) — o caso em que a pergunta descreve um sintoma sem
citar código nem texto, e o lexical tem pouco o que casar.

**Roteamento por fatia também foi rejeitado**: @1 214 / @5 282 (pior que a fusão global) e piora
fatias não roteadas (`virgin` @1 14→7).

## Dois defeitos de contrato corrigidos no processo

1. A **confiança** estava a ser calculada sobre o score RRF. As faixas de `_params_confianca()`
   foram calibradas no score BM25 (AUC 0,850) — rotular "alta" a partir de outra escala seria
   afirmação não calibrada. Agora a margem vem do **ramo esparso**.
2. O top-1 da fusão volta a trazer `margin` (1º menos 2º, em unidades RRF), como o BM25 já fazia.

## Erros meus nesta sessão (registrados para não se repetirem)

- Atribuí `ausente 22→35` à truncagem do ramo esparso; era **ponte OFF vs ON** comparadas sem controle.
- Removi a truncagem em `RRF_K=30` convencido de que "fundir deve somar, nunca remover" — derrubou
  o @5 de 306 para 274, porque o BM25 devolvia até 10.000 candidatos e a cauda longa reordenava o topo.
- Calculei estatística com uma closure que capturava a variável errada (`+328/−0` em todos os cortes).
- **O mais grave**: quase commitei a fusão como default reportando só o pool 423 e o subconjunto
  limpo — os dois a favoreciam. O teste multi-conjunto só foi rodado porque o repo já tinha um
  veredito NEGATIVO registrado que eu tive de reconciliar. **Medir onde é fácil não é medir.**

---

## Addendo 2 (19/09): o gate por confiança — a alavanca que regredia passa a ganhar

A fusão densa reprovou **duas vezes** (lab 20/09: 202x181, p=0,0111; produção 19/09: 309x289,
p=0,0308). Mas o efeito era **específico**, não nulo: ganhava onde o léxico não tem termo
literal e perdia onde o BM25 já acerta (`mensagens` 50→31 @1).

**Antes de varrer limiar, testei se havia sinal separável** — porque varrer limiar sobre o
mesmo conjunto que revelou a hipótese é treinar e testar no mesmo dado. Havia, e **invertido**:
a margem do BM25 separa o ganho da fusão com **AUC 0,111** (o score absoluto, 0,515, é inútil).
Das perguntas que a fusão **ganha**, 48,3% são confiança baixa e só 13,8% alta; das que
**perde**, 73,5% são alta. A leitura mecânica: a fusão ajuda exatamente quando o léxico não tem
sinal. (A margem se mostrou a melhor de três features — `n_tok` 0,777, útil, mas a margem venceu.)

O gate então é trivial: **fundir só quando a margem do BM25 for fraca**. Nenhum limiar novo para
o denso — reusa as faixas de `_params_confianca()`, já calibradas no BM25 (AUC 0,850).

### O teste que importa: transferência

O desenho do gate saiu de 10 conjuntos/450 perguntas. Validar nele seria circular, então separei
**6 conjuntos/447 perguntas que nunca entraram no oráculo nem na escolha do limiar**:

| | @1 | @5 | @10 | MRR |
|---|---|---|---|---|
| `off` | 247 | 296 | 322 | 0,6097 |
| **`gate/baixa`** | **256** | **318** | **339** | **0,6355** |
| `fuse` | 239 | 325 | 369 | 0,6232 |

`gate/baixa` vs `off`: @1 **+11/−2** (p=0,0225), @5 **+24/−2** (p<0,0001), @10 +22/−5 (p=0,0015).
**Nenhum dos 6 conjuntos regride** — 4 não perdem *nenhuma* pergunta a mais. E a fusão **pura**
desaba no holdout (`fresh_blind` 22→12, `vault` 44→41): é o dano que o gate evita. Sem o
`blind_v3` (58% do holdout, o mesmo que dominou o pool 423): @5 **+14/−0**.

No desenho, `baixa` venceu `media` por **não regredir em nenhum conjunto** (media regride em
`holdout_100` e `realistico`) — e foi *essa* a razão da escolha, feita só ali.

### Cobertura não pode ser descartada

Ligar a fusão levantou `ausente` de 22 para **30**: com os ramos em profundidade 30, alvo no
BM25 rank 31+ sumia. Corrigido anexando a **cauda esparsa depois da cabeça fundida** — o RRF
continua somando só `esparsos[:RRF_K]`, a cauda **não participa da soma**, então não reordena
(este é exatamente o erro do addendo 1, em que a cauda longa dentro do RRF derrubou o @5).
Resultado: `ausente` 22→**16** e MRR 0,5738→0,6046 no pool 423; @1/@5/@10 **idênticos** antes
e depois do append.

### Bugs de contrato que o caminho revelou (todos corrigidos)

1. `_carrega()` usava `if _CACHE:`; a guarda nova escreve no mesmo dict, e o cache passava a ser
   devolvido **sem modelo** (`KeyError: 'tok'`).
2. **429 do HuggingFace propagava e derrubava a busca inteira** por causa de um ramo opcional.
   Agora carrega `local_files_only` e `busca()` **nunca levanta**: avisa uma vez e cai no BM25.
3. O caminho de degradação ignorava o `top_k` (`top_k=3` devolvia 30).
4. `disponivel()` só olhava se os arquivos existem: corpus reconstruído (7019→7381) com `.pt`
   velho faria a fusão operar sobre ranking **parcial em silêncio**. Adicionada `alinhado()`.

Default promovido para `gate/baixa` (verificado sem nenhuma env var, nos dois perfis: reproduz
exatamente). `off` e `fuse` seguem disponíveis. Controle do `AGENTS.md` intacto: 230/287/301,
MRR 0,6016. Custo: dispara em **27%** das consultas, **+54 ms** só nelas.

---

## Addendo 3 (19/09): o roteador de fatia REST — o ponto cego que o lexical não alcança

O `AGENTS.md` deixara explícito: *"Um roteador que ligue `fuse` puro só em `rest/ops` não foi
medido NO CAMINHO DA PRODUÇÃO."* Medi.

**O sintoma.** Sob o gate, `rest_api_ops` ficava em **0/40 @1**. A tentação era registrar "o
denso não ajuda aqui". Antes disso, olhei o registro antigo: havia denso **puro** a 32,5% no
mesmo conjunto, com o braço invalidado. Medi os três caminhos no mesmo harness:

| conjunto | esparso @1 | **denso puro @1** | fundido @1 |
|---|---|---|---|
| `rest_api` (40) | 7 | **18** | 8 |
| `rest_api_ops` (40) | 0 | **8** | 0 |
| `mensagens` (50) | 50 | 9 | 50 |

**Não é que o denso falhe — é que a fusão o dilui.** O RRF soma o voto lexical errado ao
vetorial. O fato que explica os dois lados da tabela: nesta fatia a sobreposição de vocabulário
com o corpus é ~0 (mediana 0,00), então o lexical não tem o que casar e erra — e o embedding
carrega a semântica. Denso e lexical vencem em fatias **disjuntas**. A correção é **roteamento**,
não troca de ramo.

**O detector é um sinal legítimo, não gabarito.** As perguntas REST dizem "api" porque *são*
sobre a API. Separação medida: dispara em **42,5%** das REST (34/80) contra **6,3%** das não-REST
do holdout (23/367) — ~7x mais denso no alvo. Robustez: dos 17 termos candidatos, **só `api`
aparece** nas perguntas REST; a lista completa e a lista mínima dão números **idênticos**. E a
regra descoberta no `rest_api` **transfere** para `rest_api_ops` (conjunto independente) sem
ajuste: 0→1 @1, 5→11 @5.

**Efeito.** Holdout (n=447, o mesmo do gate): **@1 258→262, @5 318→330, @10 339→350**. Pool 423:
**@1 221→223, @3 268→281, @5 291→303, @10 314→325, MRR 0,5970→0,6119**.

**A perda de colateral é ilusória, e provei.** As 5 perguntas "não-REST" que perdem são *todas
REST genuínas* — o detector acertou; o denso é que não é uniformemente melhor. Testei a hipótese
de guardar a rota pelo gate do BM25 ("rotear só se o esparso também estiver fraco"): **zera o
colateral, mas corta o ganho pela metade** (`rest_api` 15→9, `ops` 1→0), e o colateral que ela
elimina **não é significativo** (p=0,22/0,13/0,13). O mecanismo condena a guarda: a margem do
BM25 foi calibrada no corpus **geral** e **não calibra nesta fatia** — aqui o lexical pontua alto
e erra. Fica opt-in (`RAG_REST_GUARD=1`), desligada.

### O achado mais importante desta sessão: o ambiente muda o número

O venv de medição estava em `/tmp` e foi **apagado** no meio do trabalho. Reconstruí (torch 2.14,
transformers 5.17). Então o baseline de produção não reproduziu: deu **221/268/291/314, MRR
0,5970** em vez dos 225/270/293/317 registrados. Antes de suspeitar do meu código, rodei o commit
anterior **intacto** no ambiente novo: deu **exatamente 221/268/291/314**. Não era o código — era
o venv. O controle LAB (lexical, sem torch) reproduz **bit-a-bit** (230/287/301, MRR 0,6016), o
que isola a causa nos embeddings do BGE-M3.

Consequência registrada: **comparação de produção só vale intra-ambiente**. Gravei
`requirements-medicao.txt` para fechar essa lacuna. Permaneceram `UNKNOWN` as versões exatas do
venv original (nunca foram registradas) — os números absolutos de produção desta sessão não são
comparáveis aos de sessões anteriores; o que vale é o pareado (off × on), que é intra-run.
