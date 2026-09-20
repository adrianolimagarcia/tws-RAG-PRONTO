# Sessão 2026-09-19 (parte 2) — o scorer não é BM25, e o benchmark tem teto de 89,7%

> **Regra de evidência desta sessão:** todo número vem de execução registrada. Onde não
> medi, escrevo `NAO MEDIDO`. Não estimo.
>
> **Produção intocada:** `mcp_server/` não teve mudança de comportamento. Medido: a
> paridade produção × laboratório segue em `0/262` (Jaccard@15 = 0,1325), exatamente a
> linha de base que a sessão anterior registrou.

---

## 1. Resumo em uma frase

O scorer que este repositório chama de "BM25" não é BM25 — não usa IDF, não usa TF e
normaliza por um comprimento que não é o real. Consertar isso melhora muito o **primeiro
estágio** (recall@10 de 0,832 → 0,885 no `blind_v3`), mas o ganho **não sobrevive ao
segundo estágio**, porque os bônus do reranker são constantes calibradas para a escala
antiga. E o benchmark não pode passar de **89,7%**: 27 das 262 perguntas não têm resposta
no índice.

---

## 2. O que foi medido (e o que isso separa)

### 2.1 O gargalo é de RANKING, não de cobertura

Recall do documento relevante por posição no ranking bruto (`blind_v3_slices`, 262 q,
corpus 6732 docs):

| posição | @1 | @5 | @10 | @20 | @50 | @100 | @200 | pool |
|---|---|---|---|---|---|---|---|---|
| acertos | 165 | 206 | 218 | 222 | 224 | **231** | 239 | **245** |
| fração | 0,630 | 0,786 | 0,832 | 0,847 | 0,855 | **0,882** | 0,912 | **0,935** |

231 dos 262 documentos relevantes **já estão no top-100**, mas só 165 estão no top-1.
O problema não é "não achou" — é "achou e ordenou errado". Isso aponta para o scorer, não
para o corpus.

### 2.2 O scorer não é BM25 (três desvios medidos)

1. **`tokenize()` devolve `set`** — a frequência do termo é destruída. O loop soma uma
   constante por termo apenas *presente*: um termo que ocorre 20× pesa igual a um que
   ocorre 1×.
2. **Não existe IDF em lugar nenhum.** No corpus, 20 termos têm `df ≥ 50%`:
   `10.2.8` df=96,2%, `workload` 95,4%, `hcl` 95,1%, `automation` 94,9%, `escopo` 86,0%,
   `componente` 85,8% — todos vindos do `context_prefix` indexado nas 4315
   `message_catalog`. Sem IDF, citar "10.2.8" empurra ~6479 documentos para cima com o
   **mesmo peso** de um termo distintivo.
3. **`dl` é o tamanho do *set*** e `avg_dl=60` está hardcoded, enquanto o comprimento real
   médio é **118,4 palavras** (medido). A normalização por tamanho nunca é aplicada.

### 2.3 Ligar o BM25 real: ganho grande no 1º estágio

Ranking bruto (sem o 2º estágio), corpus 6732 docs:

| benchmark | métrica | controle | BM25 real | Δ |
|---|---|---|---|---|
| `golden_qa` (70) | Hit@1 | 0,629 | **0,729** | **+10,0pp** |
| | Hit@10 | 0,886 | **1,000** | +11,4pp |
| | MRR | 0,6979 | **0,8240** | +0,126 |
| `blind_v3` (262) | Hit@1 | 0,630 | **0,672** | +4,2pp |
| | Hit@10 | 0,824 | **0,870** | +4,6pp |
| | MRR | 0,6859 | **0,7396** | +0,054 |

Ganho em **todas** as posições medidas nos dois benchmarks. Atribuição por ablação
(`blind_v3`): só o comprimento real **piora** (@1 0,618); só IDF leva @10 a 0,874; TF+IDF+dl
juntos levam a 0,885. **É a combinação, não um componente isolado.**

### 2.4 Mas o ganho NÃO sobrevive ao 2º estágio

Aqui está o achado central. `second_stage_rerank` não só reordena: ele **soma constantes
fixas** (+8, +12, +15, +20, +32, +45, +55) ao score recebido e **corta o pool**. Essas
constantes foram calibradas por varredura contra o scorer antigo, cujo topo vale ~1–5.
Com BM25 real o topo vale ~10–40, e as mesmas constantes passam a pesar ~10× menos:

| configuração (`blind_v3`) | Hit@1 | Hit@10 | Hit@15 |
|---|---|---|---|
| V0 controle (scorer + reranker do repo) | 172 | 218 | 221 |
| BM25 real + reranker na escala antiga | 180 | 219 | 227 |
| BM25 real, **só o 1º estágio** (bônus desligados) | 176 | **229** | **232** |

O 1º estágio sozinho entrega @10 = 229. Com o 2º estágio na escala antiga, cai para 219:
o reranker **perde 10 documentos de profundidade**.

Mas cuidado com a leitura — ele não é puramente ruim. Olhando @1: 176 (só 1º estágio) →
**180** (com reranker). Ou seja, **o 2º estágio troca profundidade por top-1**: ganha 4 no
@1 e perde 10 no @10. Essa troca é o comportamento *desejado* de um reranker de precisão.
O problema é que, na escala antiga, ele faz essa troca usando bônus pequenos demais para a
nova unidade — e `scripts/ablate_second_stage.py` (default) confirma que com o scorer
antigo a troca valia +7 no @1. Com BM25 real vale +4. O reranker ficou **menos útil**, não
inútil.

A leitura correta da §2.4 é: **a escala do 2º estágio precisa ser recalibrada junto com o
1º**, e §2.5 mostra que nenhuma constante única recalibra os dois.

### 2.5 Tentei consertar a escala de três formas. As três falharam em transferir.

| tentativa | resultado |
|---|---|
| Normalizar pela média do pool (varredura k=0,5…20) | cada benchmark prefere um k diferente; nenhum k é estável |
| `RAG_RERANK_UNIT` (dividir o bônus) | mesma instabilidade, exposta como switch |
| Bônus **proporcionais** ao score do candidato (escala-livre por construção) | **muito pior**: −17,1pp @1 no `golden_qa`, −26,0pp no `holdout_100` |

A proporcional foi a hipótese mais promissora — é invariante a escala *por construção*, sem
número mágico. Foi medida e rejeitada. Não promovi.

**Conclusão da §2.5:** o defeito não é "o valor da constante". É que existe **uma** constante
fixa tentando servir corpora com distribuições de score diferentes. Este repositório já
havia chegado à mesma conclusão para o peso do RRF ("não existe peso único") e para a
partição por fonte. É a **terceira** vez que a mesma classe de defeito aparece — agora no
2º estágio do scorer, não na fusão.

---

## 3. Onde as regressões aparecem (12 benchmarks, avaliador real)

Rodando `data/eval/evaluate_rag_benchmark.py` como subprocesso, com e sem `RAG_BM25_REAL=1`:

| benchmark | V0 @1 | V1 @1 | Δ @1 | Δ @10 | teto |
|---|---|---|---|---|---|
| `golden_qa_benchmark` | 0,657 | 0,757 | **+10,0pp** | +5,7pp | 83% |
| `blind_v3_slices` | 0,656 | 0,687 | **+3,1pp** | +0,4pp | 90% |
| `holdout_100_unseen` | 0,900 | 0,890 | −1,0pp | +2,0pp | 100% |
| `blind_holdout_50_vault` | 0,980 | 0,980 | 0,0pp | 0,0pp | 100% |
| `fresh_blind_test_40` | 0,500 | 0,575 | **+7,5pp** | +5,0pp | 100% |
| `blind_holdout_qa_30` | 0,233 | 0,267 | **+3,3pp** | +6,7pp | 100% |
| `realistic_blind_holdout_30` | 0,967 | 0,900 | −6,7pp | +3,3pp | 100% |
| `holdout_40_test` | 0,750 | 0,675 | −7,5pp | 0,0pp | 95% |
| `golden_qa_virgin` | 0,333 | 0,292 | −4,2pp | −8,3pp | 100% |
| `pure_virgin_test_40` | 0,950 | 0,900 | −5,0pp | 0,0pp | 100% |
| `rest_api_benchmark_40` | 0,150 | 0,125 | −2,5pp | +5,0pp | 100% |
| `rest_api_benchmark_ops_40` | 0,000 | 0,000 | 0,0pp | 0,0pp | **0%** |

**5 ganham @1, 11 ganham ou empatam @10, 6 perdem @1.** Não é vitória limpa.

### 3.1 Por que isso não é o agregado que importa

Os arquivos de benchmark **não são independentes** — medido, não suposto:

| par | sobreposição exata de pergunta |
|---|---|
| `golden_qa` → `blind_v3` | **100% (70/70)** — é subconjunto |
| `pure_virgin_test_40` → `blind_v3` | **97,4%** |
| `blind_holdout_qa_30` → `blind_v3` | **75,0%** |
| `blind_holdout_50_vault` → `blind_v3` | 28,0% |
| `holdout_100` → `blind_v3` | 24,2% |

Somar os arquivos como conjuntos separados conta as mesmas perguntas várias vezes.
Deduplicado por texto de pergunta: **766 linhas → 552 perguntas distintas**.

Agregado deduplicado (IC95 bootstrap pareado, 6000 reamostragens):

| métrica | V0 | V1 | Δ | IC95 | veredito |
|---|---|---|---|---|---|
| Hit@1 | 0,654 | 0,658 | **+0,36pp** | [−1,81, +2,54] | não significativo |
| Hit@3 | 0,732 | 0,739 | +0,72pp | [−1,27, +2,90] | não significativo |
| Hit@5 | 0,755 | 0,768 | +1,27pp | [−0,54, +3,08] | não significativo |
| Hit@10 | 0,786 | 0,797 | +1,09pp | [−0,72, +2,90] | não significativo |

79 perguntas distintas melhoraram de posição, 52 pioraram.

**Veredito honesto: isso é um EMPATE no agregado.** Cada benchmark isolado é amostra
pequena (40–262 questões, mesmos pares de sobreposição) e nenhuma diferença de @1 é
significativa isoladamente, exceto as duas que já vinham significativas.

---

## 4. O teto do benchmark: 89,7%, não 100%

`blind_v3_slices`: **27/262 perguntas (10,3%)** não têm **nenhum** `relevant_claim_ids`
presente no corpus. Para essas não existe posição correta possível — nem no pool inteiro.

| fatia | n | pergunta sem resposta no índice |
|---|---|---|
| `A_com_ancora` | 107 | 10 (9,3%) |
| `B_sem_ancora` | 140 | 2 (1,4%) |
| `D_holdout_temporal` | 15 | **15 (100%)** |

A fatia `D` faz **0 acertos em qualquer posição, incluindo o pool inteiro**. Ela não mede
recuperação — mede a cobertura do corpus pelo benchmark. O avaliador reportava
`Hit@1 = 172/262 (65,6%)` sem mencionar que o **melhor valor possível** é 89,7%.

O avaliador agora reporta isso:

```
Perguntas SEM resposta no indice: 27/262 (10.3%)
TETO do benchmark (melhor Hit@1 possivel): 89.7%
Hit @ 1 entre as respondiveis: 172/235 (73.2%)
```

E o campo correspondente entra no `eval_summary.json`
(`perguntas_sem_resposta_no_indice`, `teto_do_benchmark`, `hit_rate_at_1_entre_respondiveis`).
Isto é **diagnóstico**, não métrica: não muda o veredito, impede que o teto fique implícito.

---

## 5. Achado colateral: `expand_query` é nociva hoje

`expand_query` (expansão por sinônimos) é **código morto** no avaliador — só
`scripts/debug_virgin.py` e `scripts/rank_virgin.py` a usam. Quem usa esses dois scripts
mede um recuperador muito pior que o avaliado:

| configuração (`blind_v3`) | Hit@1 |
|---|---|
| sem expansão (o que o avaliador faz) | 0,630 |
| **com** `expand_query` | **0,466** (−16,4pp) |

**Mecanismo:** sem IDF, injetar sinônimos de termos genéricos (`plano` → plan/symphony,
`mensagem` → message/msg/codigo) adiciona constantes a milhares de documentos e destrói o
sinal. A expansão só deve ser reconsiderada **depois** do IDF, nunca antes.

---

## 6. Estado atual

| | |
|---|---|
| HEAD | `3402d8a` + esta fatia |
| comportamento default | **inalterado** — controle reproduz `172/262`, MRR `0.7134` |
| prova da inalteração | `eval_summary.json` idêntico; **2.235.024 pares** (pergunta, doc) com score idêntico, 0 divergências |
| produção | **intocada** (paridade segue `0/262`) |
| gate | `INVALID` (inalterado) |
| switch novo | `RAG_BM25_REAL=1` (default OFF) |

### 6.1 Sobre o `README.md` principal

O `README.md` anuncia **93,49% Hit@1 em 1.952 perguntas**. **NAO MEDIDO** por mim — não
afirmo que está errado. Mas dois fatos medidos nesta sessão tornam o número suspeito de
precisar de qualificação:

1. benchmarks deste repo contêm **10,3% de perguntas sem resposta no índice** — um teto
   implícito de 89,7% no `blind_v3`, e o denominador do número de 1.952 não foi auditado;
2. os arquivos de benchmark **se sobrepõem até 100%** entre si — 766 linhas viram 552
   perguntas distintas; um número de "1.952 perguntas únicas" precisa passar pela mesma
   deduplicação antes de ser citado como 1.952 distintas.

---

## 7. Próximos passos

### Desbloqueado, e agora com alvo definido

1. **Calibrar o 2º estágio por benchmark, não globalmente.** Medido: nenhuma constante
   única transfere (§2.5, três tentativas). O caminho que ainda não foi testado é
   **aprender os pesos em um split e validar em outro** — e isso exige splits
   independentes, que hoje não existem (item 2).
2. **Corrigir a independência dos splits** (herdado da sessão anterior: 309 FAIL de split,
   446 FAIL de duplicata). Agora com número maior: `pure_virgin_test_40` é 97,4% o
   `blind_v3`; `golden_qa` é **100%** o `blind_v3`. Sem isso, nenhum veredito de
   "generalização" é possível, e o agregado da §3.1 não pode ser somado.
3. **Decidir sobre as 27 perguntas sem resposta.** Ou entram no corpus (se são conhecimento
   legítimo ausente), ou saem do benchmark (se não são respondíveis por projeto). Hoje elas
   penalizam todo recuperador igualmente e travam a leitura do `D_holdout_temporal`.

### Bloqueado por entrada humana

4. **Benchmark V4 (sealed holdout)** — inalterado. Perguntas novas não podem ser geradas do
   corpus: o vazamento medido prova que seriam tautológicas por construção.

### Bloqueado pelo gate

5. **Fatia do MCP** — fazer a produção usar `rag_core`. Só depois do gate, e só se o
   agregado deixar de empatar (§3.1).

---

## 8. Splits disjuntos por evidência — e o número honesto é 53,0%

### 8.1 O que faltava

O `decontaminated-manifest.json` admitia explicitamente o que **não** foi corrigido:

```json
"escopo_nao_corrigido": ["7-split (309 FAIL)", "8-duplicata (446 FAIL)"]
```

E os checks 7 e 8 do `audit_eval_leakage.py` só pegam "pergunta em dois arquivos".
Nenhum deles pega o vazamento mais grave: **a mesma evidência (claim) fundamentando uma
pergunta de treino e uma de teste.**

`scripts/build_honest_splits.py` ataca isso por união-find: duas perguntas entram no mesmo
cluster se compartilham qualquer claim, e o **cluster é indivisível**. Distribuição
determinística (tamanho, depois hash do conteúdo) — sem RNG, reproduzível por construção.
`scripts/gate_honest_splits.py` **re-verifica do zero** o que foi gravado, sem confiar no
builder.

### 8.2 O compromisso, medido (não escondido)

O harness emite **duas** variantes em vez de escolher uma:

| variante | pergunta | claim | runbook | maior cluster | representatividade |
|---|---|---|---|---|---|
| `honest_v1` (estrita) | 0 | **0** | **0** | **106** | ruim: um tema inteiro vai para o treino |
| `honest_v1_claim` | 0 | **0** | 4 | 20 | melhor |

A variante estrita é limpa mas concentra as 106 perguntas dos labs RHEL9/WSL num único
cluster indivisível, que vai **todo** para o treino — o teste fica sem esse tema. Nenhuma
das duas é "a certa"; o script mostra o número das duas.

### 8.3 O resultado inesperado: minha hipótese estava ERRADA

Eu esperava que o vazamento inflasse os números. **Não infla.** Isolando por contraste
(mesmo recuperador, perguntas de evidência vazada × evidência exclusiva):

| posição | vazada − exclusiva | IC95 | veredito |
|---|---|---|---|
| @1 | **−7,68pp** | [−18,47, +3,50] | não significativo |
| @10 | +3,77pp | [−6,33, +13,33] | não significativo |

Hipótese de inflação por vazamento **refutada**.

### 8.4 A causa real: seleção de pergunta

As 262 perguntas do `blind_v3_slices` são uma **fatia mais fácil** do pool:

| grupo | n | @1 | @10 | @15 | MRR |
|---|---|---|---|---|---|
| perguntas do `blind_v3` | 262 | **0,656** | 0,832 | 0,844 | 0,7134 |
| mesmas perguntas, fora do `blind_v3` | 161 | **0,323** | 0,460 | 0,478 | 0,3685 |

**+33,4pp @1 mais fáceis**, IC95 [+23,8, +42,8], **significativo em todas as posições**.

Este é o número que faltava no projeto: a inflação **não** vem de vazamento de evidência —
vem de o benchmark ser composto das perguntas fáceis. E note: uma fração dos arquivos
"sintéticos" (`golden_qa_virgin`, `pure_virgin`, `blind_holdout_qa_30`) pontua **0,23–0,33**
@1, muito abaixo do `blind_v3`. O projeto publicava o subconjunto favorável.

### 8.5 O número honesto

No pool **completo e deduplicado** (423 perguntas distintas):

| métrica | valor | teto |
|---|---|---|
| **Hit@1** | **224/423 = 53,0%** | 83,7% |
| Hit@10 | 292/423 = 69,0% | — |
| Hit@15 | 298/423 = 70,4% | — |
| MRR | 0,5821 | — |
| perguntas sem resposta no índice | 69/423 (16,3%) | — |
| Hit@1 entre as respondíveis | 224/354 = 63,3% | — |

Contra os **65,6%** publicados do `blind_v3`, a inflação por seleção é de **~12,6pp**.

### 8.6 O BM25 real sobrevive ao teste honesto? Não significativamente

| conjunto | Δ@1 | IC95 | Δ@15 | IC95 |
|---|---|---|---|---|
| `honest_v1` TESTE | −2,86pp | [−7,14, +1,43] | +4,29pp | [−0,71, +9,29] |
| `honest_v1` TREINO | +3,53pp | [0,00, +7,07] | **+3,53pp** | [+0,71, +6,71] |
| `honest_v1_claim` TESTE | −1,43pp | [−5,71, +2,14] | +2,14pp | [−2,14, +7,14] |

**O BM25 real ajuda a PROFUNDIDADE (@10/@15) mas não o top-1.** Exatamente o que o split
honesto existe para detectar — e o que o `blind_v3` sozinho escondia.

### 8.7 O que continua bloqueado

O **benchmark V4 (sealed holdout)** segue bloqueado por entrada humana. Não por falta de
método: por medição. Gerar perguntas do corpus produz perguntas tautológicas — e a §8.4
agora dá a magnitude desse problema (+33,4pp), que é maior do que se supunha.

---

## 9. Como reproduzir
P=/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO
cd $P

# CONTROLE -> 172/262, MRR 0.7134, teto 89.7%  (deve ser IDENTICO antes e depois desta fatia)
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  python3 data/eval/evaluate_rag_benchmark.py

# BM25 REAL -> 180/262, MRR 0.7424
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 RAG_BM25_REAL=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  python3 data/eval/evaluate_rag_benchmark.py

# idem no golden_qa -> 46/70 (0,657) vs 53/70 (0,757)
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 RAG_BM25_REAL=1 \
  python3 data/eval/evaluate_rag_benchmark.py

# paridade producao x laboratorio -> inalterada (0/262)
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  python3 scripts/measure_prod_eval_parity.py --top 15

# gate -> INVALID
python3 scripts/gate_rag_v4.py

# SPLITS HONESTOS: constroi as duas variantes e verifica do zero
python3 scripts/build_honest_splits.py --ambos
python3 scripts/gate_honest_splits.py --variant honest_v1

# O NUMERO HONESTO: pool completo deduplicado -> Hit@1 224/423 (53,0%), teto 83,7%
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/splits/honest_v1/test.jsonl \
  python3 data/eval/evaluate_rag_benchmark.py

# e com o scorer novo -> 58/140 (41,4%), @10 60,7%, @15 65,0%
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 RAG_BM25_REAL=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/splits/honest_v1/test.jsonl \
  python3 data/eval/evaluate_rag_benchmark.py
```

Os três switches são opt-in e default OFF: `RAG_BM25_REAL` (scorer),
`RAG_RERANK_UNIT` (escala do 2º estágio), e os já existentes de corpus.
