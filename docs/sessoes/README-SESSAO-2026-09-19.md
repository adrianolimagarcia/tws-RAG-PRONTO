# README da sessão — medição honesta do RAG (2026-09-19)

> **Este arquivo não substitui o `README.md` do projeto.** É o registro da sessão de
> 2026-09-19, que auditou a *medição* do RAG. O `README.md` continua sendo a
> apresentação do dataset e do pipeline.
>
> **Regra de evidência usada aqui:** todo número vem de execução registrada em
> `data/evidence/` ou `data/eval/results/`. Amostra pequena está marcada. O que não foi
> medido está escrito `UNKNOWN` — não estimado.
>
> **Produção intocada:** `mcp_server/` não teve mudança de comportamento nesta sessão.

---

## 1. O que foi feito

Sete commits, cada um com evidência própria:

| # | entrega | artefato | commit |
|---|---|---|---|
| 1 | `rag_core/` — scorer extraído do evaluator, importável | `rag_core/{config,corpus,lexical}.py` | `7f225b6` |
| 2 | Auditor de vazamento de benchmark, fail-closed | `scripts/audit_eval_leakage.py` | `7f225b6` |
| 3 | Medidor de paridade produção × laboratório | `scripts/measure_prod_eval_parity.py` | `6bcbadf` |
| 4 | Resultados de benchmark em caminho durável | `data/eval/results/` | `8d13821` |
| 5 | Gate de promoção (§17), 11 critérios | `scripts/gate_rag_v4.py` | `aa1b386` |
| 6 | A/B `synthetic_questions` no índice | `scripts/ab_experiment.py` | `91de162` |
| 7 | Descontaminação de benchmarks + manifesto | `scripts/decontaminate_benchmarks.py` | `ae103c4` |
| — | Relatório técnico consolidado | `docs/lab-protocols/relatorio-2026-09-19-medicao-honesta-do-rag.md` | `9cf0aa2` |

---

## 2. O que deu certo

### 2.1 O controle é sólido

`blind_v3_slices.jsonl`, corpus congelado de 6732 documentos:

| métrica | valor |
|---|---|
| Hit@1 | **172/262** = 0,6565 |
| Hit@10 | **218/262** = 0,8321 |
| Hit@15 | **221/262** = 0,8435 |
| MRR | **0,7134** |

Reproduzido **5×**, inclusive depois da refatoração `rag_core` e depois da
descontaminação. A refatoração foi provada behavior-preserving por **três vias
independentes**: o controle reproduz, **168.300 pares** (pergunta, doc) com igualdade
exata de float e 0 divergências, e `eval_summary.json` byte-idêntico (mesmo sha256).

### 2.2 Os instrumentos de medição funcionam

- **Auditor de vazamento** — 19 benchmarks, 979 perguntas, 16244 synthetic_questions,
  7019 claims. Fail-closed (exit 1 em FAIL), offline, stdlib, zero path absoluto.
- **Medidor de paridade** — usa os dois recuperadores **reais** (importa o módulo do
  MCP, não reimplementa).
- **Gate de promoção** — 11 critérios; veredito = **pior** critério, nunca média;
  `UNKNOWN` não promove. Testado de ponta a ponta: devolve `INVALID` hoje, que é o
  resultado correto.

### 2.3 O defeito principal foi encontrado e quantificado

**O benchmark vaza para dentro do índice.** 158 perguntas são idênticas a uma
`synthetic_question` da própria claim relevante, e o evaluator **indexa**
`synthetic_questions`. Para essas perguntas, a resposta está literalmente dentro do
documento.

Isso foi medido, não inferido — e a correção foi aplicada:

| benchmark | antes | removidas | depois |
|---|---|---|---|
| `blind_v3_slices` | 262 | **0** | 262 |
| `holdout_100_unseen` | 100 | **73** | 27 |
| `fresh_blind_test_40` | 40 | **32** | 8 |
| `blind_holdout_50_vault` | 50 | **35** | 15 |
| **total (19 arquivos)** | **979** | **182** | **797** |

### 2.4 E a correção óbvia estava errada

A tentação era remover `synthetic_questions` do índice. Medido: **custaria recall
legítimo**.

| benchmark | MRR baseline → sem synth_q | Δ MRR (IC95) |
|---|---|---|
| `blind_v3` — **0** tautologias | 0,7134 → 0,6951 | −0,0183 [−0,0349, −0,0043] |
| `holdout_100` — 72% tautológico | 0,9286 → 0,8595 | −0,0692 [−0,1148, −0,031] |

As `synthetic_questions` são **também expansão de vocabulário** do documento. A
correção certa é no **benchmark** (a pergunta não pode ser uma delas), não no índice.

---

## 3. O que deu errado

### 3.1 Eu afirmei que o lab estava limpo, e não estava

Declarei como fato medido que "o evaluator não indexa `synthetic_questions`". O grep
rodou em `evaluate_rag_benchmark.py` **depois** da refatoração, quando a montagem do
texto já tinha migrado para `rag_core/corpus.py`. Procurei no arquivo errado e chamei a
ausência de resultado. **O evaluator indexa, nas duas versões.**

Consequência: os números `holdout_100` (0,9100), `blind_holdout_50` (0,9600),
`fresh_blind_test_40` (0,9333) e `realistic_30` estavam **inflados** e foram retirados
como evidência de qualidade. Corrigido em `88b3c31`.

### 3.2 Minha previsão no A/B estava parcialmente errada

Previ "efeito ~nulo no benchmark limpo". Há custo real de −2,67pt @1 **sem vazamento
algum**, com IC95 que não cruza zero. O experimento foi desenhado para ser falseável e
me falsificou — que é o comportamento desejado.

### 3.3 Erros de medição que produziriam "0% de paridade" falso

Dois bugs meus no medidor de paridade: lia `mcp.documents` (o módulo usa `mcp.docs`) e
montava o texto do doc com `d.get('claim')` (o schema é `id/text/tokens/type`). O
segundo zerava os 6732 doc_tokens e **todo score dava 0** — o script imprimia
"Jaccard 0,0000" como se fosse resultado. O sinal que me salvou: um zero *total* entre
dois recuperadores lexicais sobre corpora 88% sobrepostos é implausível. O script hoje
**aborta (exit 2)** em corpus vazio, ranking vazio ou corpora sem id em comum.

### 3.4 Dois defeitos no próprio gate

1. Em modo A/B o controle era lido de `--summary` (`eval_summary.json`, sobrescrito a
   cada rodada) em vez do braço A.
2. O controle do `blind_v3` (n=262) era exigido em A/B de **outro** benchmark, tornando
   todo A/B fora do `blind_v3` `INVALID` por construção.

### 3.5 O scanner de publicação tinha defeitos reais

- **A isenção nunca ativava.** O `awk` casava `^\+# publish-patterns:start$`, mas o
  marcador tinha texto depois dele. O bloco de padrões era varrido junto com o resto,
  ao contrário do que o comentário prometia.
- **Padrão IPv4 largo demais** — barrava a versão do produto HCL (`10.2.8.00`), o que
  bloquearia toda publicação futura que citasse a versão.

### 3.6 O relatório em prosa não é entrega

Por várias rodadas eu reportei no chat sem produzir **artefato**. Só quando questionado
o documento foi escrito. Relatório que existe apenas na conversa não é auditável.

---

## 4. Estado atual

| | |
|---|---|
| HEAD | `9cf0aa2` == origin, árvore limpa |
| corpus | 6732 documentos (verificado após cada operação) |
| produção | **intocada** |
| gate | **`INVALID`** — leakage `FAIL`, paridade `FAIL` |

**Atenção ao `README.md` principal:** ele anuncia **93,49% Hit@1 em 1.952 perguntas**.
Essa medição é de outro conjunto, e eu **não** a auditei — então não afirmo que está
errada. Mas o defeito de construção que medi (pergunta idêntica a uma
`synthetic_question` indexada) é sistêmico nos benchmarks deste repo, e o número
merece passar pelo scanner antes de ser usado como referência:

```bash
$PY scripts/audit_eval_leakage.py --benchmarks <arquivo-do-benchmark-de-1952>.jsonl
```

---

## 5. Próximos passos

### Desbloqueados (não dependem de você)

1. **`7-split` (309 FAIL) e `8-duplicata` (446 FAIL)** — splits não independentes e
   near-duplicata **entre** arquivos. É o defeito que explica o `pure_virgin_test_40`
   ser 97,4% o `blind_v3` renomeado. Correção própria (deduplicação entre benchmarks),
   não feita. **É o próximo passo de maior valor** — corrige a independência dos
   splits, que hoje invalida qualquer alegação de validação externa.
2. **P0-C** — o "BM25" do harness não é BM25 completo: `tokenize()` devolve `set` (perde
   TF), `compute_bm25` não usa IDF, `avg_dl=60` hardcoded. Ganho medível dentro do
   laboratório, sem tocar produção.
3. **Auditar o benchmark de 1.952 perguntas** do README principal com o scanner.

### Bloqueados por entrada humana

4. **Benchmark V4 (sealed holdout)** — perguntas novas **não podem** ser geradas do
   corpus: o próprio vazamento medido prova que seriam tautológicas por construção.
   Exige perguntas de fora, escritas ou validadas por você. O invólucro (split selado,
   procedência auditável, gate consumindo) é construível sem isso.

### Bloqueado pelo gate

5. **Fatia do MCP** — fazer a produção usar `rag_core` e parar de indexar
   `synthetic_questions`. É mudança de produção, e o gate diz `INVALID`. Alvo
   mensurável: `Jaccard@15 = 1,0` e `262/262` de paridade.

---

## 6. Como reproduzir

```bash
P=/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO
PY=<venv>/bin/python
cd $P

# controle -> 172/262, 218/262, 221/262, MRR 0,7134
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  $PY data/eval/evaluate_rag_benchmark.py

# vazamento -> exit 1 = FAIL
$PY scripts/audit_eval_leakage.py --json /tmp/leak.json

# paridade produção x laboratório -> 0/262
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  $PY scripts/measure_prod_eval_parity.py --top 15

# descontaminação (precisa do relatório acima) -> 979 -> 797
$PY scripts/decontaminate_benchmarks.py --leak-json /tmp/leak.json

# gate -> INVALID
$PY scripts/gate_rag_v4.py
```

Todos os scripts são offline, sem path absoluto no código. Os benchmarks descontaminados
**não são versionados** (são derivados e regeneráveis); o que entra é o manifesto de
procedência em `data/eval/decontaminated-manifest.json`.
