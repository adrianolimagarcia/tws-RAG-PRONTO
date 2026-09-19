# Runbook — medir a FUSÃO e o PESO da fusão (RAG)

Protocolo para medir qualquer mudança na fusão lexical×densa deste repo. Escrito porque
a fusão é o ponto onde este projeto **mais se enganou**: quatro trials semânticos
anteriores foram medidos contra baselines DIFERENTES do harness e produziram um "+9"
ilusório (Jina), e um benchmark fraco (40 perguntas com o código na própria pergunta)
fez o híbrido parecer melhor do que é.

## Regra zero

**Toda medição de fusão tem um CONTROLE OBRIGATÓRIO embutido: o baseline lexical do
harness tem de reproduzir, no blind v3 com o corpus congelado, exatamente:**

```
Total de documentos indexados no corpus RAG: 6732
Hit Rate @ 1:  172/262 (65.6%)
Hit Rate @ 10: 218/262 (83.2%)
Hit Rate @ 15: 221/262 (84.4%)
Recall @ 15:   0.7345
Mean Reciprocal Rank (MRR):    0.7134
```

Ambiente do controle (não omitir nenhuma variável):

```bash
export PYTHONHASHSEED=0
export RAG_MEASURE_EXCLUDE_EVIDENCE=1     # corpus congelado = 6732
export RAG_INGEST_REST_API=1              # granularidade FAMÍLIA = +24 docs
export RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl
python data/eval/evaluate_rag_benchmark.py
```

Se não reproduzir, a medição é **INVÁLIDA** e nada pode ser concluído. Não "ajuste" o
baseline para fechar o número — investigue por que divergiu.

Motivo: o único jeito de comparar duas configurações é as duas passarem pelo **mesmo**
recuperador e o **mesmo** reranker. Baseline diferente = delta inventado.

### O controle NÃO é o `w=0.0` da varredura

Os dois parecem o mesmo baseline lexical e **não são**:

| caminho | @1 | @10 | @15 |
|---|---|---|---|
| controle (BM25 puro, sem `RAG_HYBRID`, sem rerank) | 172/262 | **218/262** | 221/262 |
| `RAG_HYBRID=1 RAG_RRF_W=0.0 RAG_RERANK_TOP=15` | 172/262 | **217/262** | 220/262 |

`w=0.0` zera o peso denso mas ainda passa pelo caminho híbrido e pelo `second_stage_rerank`,
que reordena dentro do topo. O `@1` coincide; `@10` e `@15` **não**. Não use um no lugar do
outro ao declarar controle.

### Correção do MRR do controle (2026-09-19)

O controle foi re-baselinado antes com `MRR 0,7133` — **estava errado**. O valor do
evaluator é **0,7134**. O `0,7133` veio de `scripts/measure_fusion_v3.py`, que replica o
pipeline lexical por conta própria e concorda em `@1`/`@10` mas divergia em MRR na quarta
decimal. Erro de processo: a segunda fonte foi usada como confirmação sem ser confrontada
na métrica inteira. Verificado rodando o código do HEAD **sem** a refatoração do `rag_core`:
também dá `0,7134`. Se um dia `0,7133` for vinculante, falta identificar qual estado de
código/corpus o produziu — o HEAD não é esse estado.

### Por que o controle deixou de ser 183/262 (re-baselinado em 19/09)

O valor histórico `183/262` **é obsoleto** — ele não descreve o código atual, e sim o
estado de `ffc4a75` (16/09). Provado rodando o avaliador **daquele commit** num worktree
isolado (`git worktree add --detach /tmp/wt ffc4a75`), que devolveu exatamente
`corpus 6979 · @1 183/262 · @10 232/262 · MRR 0,7577`.

A divergência tem causa mecânica, não é ruído:

| estado | corpus | @1 | @10 | MRR |
|---|---|---|---|---|
| `ffc4a75` (16/09) — origem do 183 | 6979 | 183/262 | 232/262 | 0,7577 |
| hoje, congelado — **controle atual** | 6732 | 172/262 | 218/262 | 0,7133 |

1. **O corpus foi reconstruído** em `8331519` ("um id = um documento"): 99 colisões de id
   + 106 registros-lixo removidos. 6979 → 6732 são **247 documentos** que existiam na
   medição original e não existem mais.
2. **O caminho lexical mudou**: `tokenize()` foi introduzido e o lever de stopwords
   entrou em `b61bc1c`, ambos depois de `ffc4a75`.

Ou seja: o 183 mede um corpus que **não existe mais**. Manter esse número como controle
bloquearia toda medição futura legitimamente. O controle correto é o do corpus atual —
e a regra que importa é a de baixo: **todas as variantes têm de passar pelo mesmo
harness e pelo mesmo corpus dentro da mesma rodada.**

Confirmado por duas vias independentes na mesma rodada: `scripts/measure_fusion_v3.py`
(que tem guarda embutida e imprime `CONTROLE FALHOU` contra o 183) e invocação direta do
avaliador — ambos deram 172/262 com o corpus 6732.

## Corpus congelado (sem isso a medição se contamina)

O corpus de medição inclui os próprios arquivos de evidência (`lab_evidence`), então
**medir perturba o objeto medido**. Use sempre:

```
RAG_MEASURE_EXCLUDE_EVIDENCE=1     # corpus congelado = 6732 docs
```

Sem o switch: 6904 docs (e subindo a cada evidência gravada). Os números **mudam**
(5/40 → 4/40, 8/40 → 6/40 já aconteceu por isso).

## Conjuntos e para que serve cada um

| conjunto | perguntas | papel |
|---|---|---|
| `blind_v3_slices.jsonl` | 262 | **referência** da casa; fatias A/B/D; tem o controle 183/262 |
| `rest_ops_40` (benchmark por operação) | 40 | corpus REST isolado, ground truth mecânico |
| `holdout_100_unseen.jsonl` | 100 | validação **externa** |
| `blind_holdout_50_vault.jsonl` | 50 | validação **externa** |
| `realistic_blind_holdout_30.jsonl` | 30 | validação **externa** |

**Ajustar num conjunto, validar nos OUTROS.** É o que reprovou o challenger em 17/09
(+15 no v3, −6 nos externos). Vale também para o peso: um alfa ajustado que não
generaliza out-of-domain não é ganho, é overfitting.

## Estado conhecido (não redescobrir)

Medido em 17/09 (`ffc4a75`, `scripts/measure_fusion_v3.py`, blind v3, controle OK):

| variante | @1 | @3 | @5 | @10 | MRR |
|---|---|---|---|---|---|
| baseline lexical (harness) | 183/262 | 209 | 221 | 232 | 0,7576 |
| cobertura (união, ordem lexical) | 181 | 207 | 219 | 230 | 0,7510 |
| rrf `1/(60+r)` | **149** | 196 | 212 | 233 | 0,6771 |

Por fatia (@1): A com âncora 97 → **57**; B sem âncora 80 → **86**; D 6 → 6.
`recall@50` por ramo: lex 83,5% · denso 83,8% · união **93,8%**.

**Leitura:** o denso ACHA os documentos (união leva o recall@50 a 93,8%) mas o @1 **não**
melhora — o gargalo é **ordenação**, não geração de candidatos. E o dano é
**dependente de fatia**: destrói a fatia com âncora, ajuda a sem âncora.

Medido em 18/09 nos 3 held-outs externos: denso puro é pior em todos (@15 81/46/26 contra
97/50/30), e o oráculo **não tem o que colher** (`so_denso` = 0, 0, 0). `bm25_rerank` é
**idêntico** a `bm25` — o reranker não move nada ali; todo o dano é da **fusão**.

## RESPOSTA: não existe peso único (medido em 19/09)

Varredura completa de `RAG_RRF_W` em {0.0, 0.5, 1.0}, 5 conjuntos, controle OK. As curvas
são **monotônicas em direções opostas**:

| conjunto | w=0.0 | w=0.5 | w=1.0 |
|---|---|---|---|
| geral_blind_v3 | **0.6565** | 0.6336 | 0.5496 |
| holdout_100 | **0.9100** | 0.8400 | 0.7400 |
| blind_holdout_50 | **0.9600** | 0.9600 | 0.9200 |
| realistic_30 | **0.9333** | 0.9333 | 0.8000 |
| **rest_ops_40** | 0.0250 | 0.1500 | **0.2500** |

`peso_otimo_estavel_no_tune = False`. **Um índice único com um peso único está
estruturalmente errado para esta mistura de fontes**: qualquer valor é compromisso que
paga preço nos dois lados.

**Leitura por ramo:** no geral o denso gera candidatos úteis mas atrapalha a *ordenação*
no topo (recall@15 melhora com w=0.5 em dois conjuntos, mas o @1 só piora). No REST o
esparso não tem o que casar (cobertura lexical mediana 0,00) — é o denso que recupera.

### O REST não deve ser recuperado: é CLASSIFICAÇÃO

O espaço de resposta do REST é **fechado e enumerado** (276 operações, com método/path/
família). Isso não é busca, é escolha entre alternativas conhecidas. Medido no **mesmo**
benchmark e **mesmo** corpus:

| método | @1 |
|---|---|
| recuperação, melhor ramo (denso puro) | 0.2500 |
| **classificação, 276 classes** | **0.9250** (37/40) |
| classificação, sem as perguntas com vazamento (34/37) | 0.9189 |

**3,7×.** O vazamento de rótulo (3/40) **não** sustenta o número. `deepseek-v4-flash` via
a6api, 0 erros de API, 40 chamadas (piloto de 5 antes). Script: `scripts/classify_rest_ops_276.py`.

**Consequência arquitetural:** se o REST sai do índice e vira classificação, o problema da
fusão **desaparece** do lado REST em vez de ser calibrado.

### CUIDADO: `@1` e `recall@15` contam histórias opostas

A tabela acima é de `@1`. A **segunda métrica da mesma rodada diz o contrário**:

| conjunto | Δ`@1` (w=0.5 vs w=0.0) | Δ`recall@15` |
|---|---|---|
| geral_blind_v3 | −2,29pt | **+5,40pt** |
| holdout_100 | −7,00pt | **+1,50pt** |
| blind_holdout_50 | 0,00 | 0,00 (teto) |
| realistic_30 | 0,00 | −4,44pt |

O híbrido **perde `@1` em dois conjuntos e ganha `recall@15` em dois** — é uma **troca**, não
um vencedor. E a produção **entrega 15 documentos** (`top_n=15`, pool de 20 do RRF, em
`evaluate_pure_virgin_hybrid_cpu.py`), então `recall@15` é a métrica da janela que o consumidor
realmente recebe.

**Portanto NÃO desligar `RAG_HYBRID` por causa da tabela de `@1`.** Antes de mexer no default,
responder: o consumidor usa a **ordem** (`@1`) ou a **presença na janela** (`recall@15`)? Se as
duas divergem, não há recomendação — há decisão de produto pendente. O default `0.5` foi
escolhido por convenção ("peso igual por default", padrão da indústria), não por medição; agora
está medido, e o resultado é misto.

### Armadilha do índice denso (custou uma medição inteira)

O braço REST da varredura nasceu inválido por usar o índice **v5**, que tem os 24 registros
de FAMÍLIA e **zero** dos 276 de OPERAÇÃO. Com `RAG_DENSE_MASK_TO_CORPUS=1` o ramo denso
recupera só docs fora do corpus e é **zerado pela máscara** → `w=1.0` devolvia `0/40` em
tudo, que **parece** resultado.

| índice | granularidade | `w=1.0` no rest_ops_40 |
|---|---|---|
| v5 | operação | 0.0000 @1 (ramo denso inexistente) |
| v6 | operação | **0.2500 @1**, 0.7250 @10 |

Regra: **conferir `n_docs` do índice contra `n_docs` do corpus ANTES de concluir.** Se uma
variante que deveria usar o ramo denso dá exatamente `0.0000` em tudo — ou exatamente o
mesmo número do ramo esparso puro — suspeitar de índice incompleto antes de reportar.

## Como rodar a varredura do peso

```
RAG_RRF_W  em {0.0, 0.25, 0.5, 0.75, 1.0}    # peso do ramo DENSO; default 0.5 = igual
```

```
python scripts/sweep_fusion_weight.py --out /tmp/sweep.json
```

Detalhes que importam:

- **`RAG_RRF_W` só é lido com `RAG_HYBRID=1`.** Sem o híbrido não há fusão a ponderar.
- A implementação usa `2*w` / `2*(1-w)`, então **`w=0.5` reproduz exatamente** o RRF de
  produção. Verificado por igualdade de scores e ordem, não por inspeção.
- `w` fora de `[0,1]` **levanta erro** em vez de silenciar.
- **Rodar desacoplado do TTY** (`setsid nohup ... < /dev/null`). Em 18/09 a varredura
  morreu na 2ª de 25 execuções por `tcsetattr: ioctl inapropriado` e deixou o
  `eval_summary.json` sujo + backup órfão. O script grava a cada conjunto concluído,
  mas **confira e restaure** depois de qualquer kill:
  `git checkout HEAD -- data/eval/eval_summary.json && rm -f data/eval/eval_summary.json.bak-sweep`

## O que a literatura diz (e o que ela NÃO diz)

Consulta Perplexity de 18/09, registrada em
`data/evidence/lab-validation-2026-09-18-analise-baseada-em-fontes-sobre-fusao-rrf-...jsonl`.

- O defeito é **conhecido**: com `k=60` o amortecimento suaviza as diferenças de rank
  (rank 1 = 1/61, rank 10 = 1/70), então candidatos de meio de lista do ramo fraco
  **continuam influentes** e diluem o forte.
- **"A fusão aterrissa entre os ramos" NÃO é teorema.** RRF é agregação de ranks, não
  interpolação. Pode ficar acima dos dois, abaixo do melhor, ou abaixo dos dois.
- **Peso é o botão de confiança no ramo; `k` é o botão de sensibilidade ao topo.**
  Baixar `k` amplifica o topo de TODOS os ramos — inclusive o rank 1 ruim do fraco —
  então **não** resgata o ramo forte.
- **Chen et al. (2022)**: sem rótulos, RRF `k=60` é o padrão robusto.
  **Bruch/Gai/Ingber (TOIS 2023)**: ajustado, a combinação convexa normalizada ganha
  in-domain e out-of-domain, e o melhor `k` do RRF não transfere entre domínios.
  As duas são compatíveis — a conclusão depende de haver rótulos.
- **Normalização não é o ponto**: min-max e z-score são largamente intercambiáveis
  depois de reajustar o peso. O problema prático é **calibrar o peso**.
- Todos os grandes sistemas de produção usam **peso igual por default** e **expõem** o
  peso por ramo. O Qdrant recomenda manter `1.0/1.0` **sem conjunto de avaliação** —
  que é a disciplina de defaults OFF deste repo.

## Disciplina

- **Nenhum default ligado.** Todos os switches são opt-in e ficam OFF.
- **Produção intocada.** `scripts/evaluate_pure_virgin_hybrid_cpu.py` é caminho de
  produção (RRF → top-20 → rerank `top_n=15`, entrega 15 docs). Não alterar para medir.
- **Evidência sanitizada**: sem IP, host, UID ou caminho de usuário.
- **Publicar SEMPRE por `scripts/publish.sh`** (fail-closed, único ponto de varredura
  de segredo). Commit direto passa por cima e já aconteceu uma vez aqui.
