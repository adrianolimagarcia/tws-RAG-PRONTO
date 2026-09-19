# Relatório — Medição honesta do RAG (2026-09-19)

**Escopo:** fatiar o `RUNBOOK_RAG_SCORE_ULTRA_SOTA` e executar a prioridade imediata
declarada (P0-A + instrumentos de medição) sem tocar produção.

**Regra de evidência:** todo número abaixo vem de execução registrada em
`data/evidence/` ou `data/eval/results/`. Onde a amostra é pequena, está dito. Onde
não foi medido, está dito `UNKNOWN` — não estimado.

**Produção intocada:** `mcp_server/` sem mudança de comportamento em nenhum commit
desta série.

---

## 1. Entregas

| # | entrega | artefato | commit |
|---|---|---|---|
| 1 | `rag_core/` — scorer extraído do evaluator, importável | `rag_core/{config,corpus,lexical}.py` | `7f225b6` |
| 2 | Auditor de vazamento de benchmark, fail-closed | `scripts/audit_eval_leakage.py` | `7f225b6` |
| 3 | Medidor de paridade produção × laboratório | `scripts/measure_prod_eval_parity.py` | `6bcbadf` |
| 4 | Resultados de benchmark em caminho durável | `data/eval/results/` | `8d13821` |
| 5 | Gate de promoção (§17) — 11 critérios | `scripts/gate_rag_v4.py` | `aa1b386` |
| 6 | A/B `synthetic_questions` no índice | `scripts/ab_experiment.py` | `91de162` |
| 7 | Descontaminação de benchmarks + manifesto | `scripts/decontaminate_benchmarks.py` | `ae103c4` |

Correções incidentais no caminho: defeito de isenção no `publish.sh` (a isenção
documentada nunca ativava — o `awk` casava a linha inteira e o marcador tinha texto
depois dele) e padrão IPv4 largo demais, que barrava a versão do produto HCL.

---

## 2. O controle (linha de base)

`blind_v3_slices.jsonl`, corpus congelado de **6732** documentos.

| métrica | valor |
|---|---|
| Hit@1 | **172/262** = 0,6565 |
| Hit@10 | **218/262** = 0,8321 |
| Hit@15 | **221/262** = 0,8435 |
| MRR | **0,7134** |

**Reproduzido 5×**, incluindo depois da refatoração `rag_core` e depois da
descontaminação (o `blind_v3` descontaminado é idêntico ao original — 262 perguntas,
dicts iguais). Correção registrada: o valor anterior de MRR 0,7133 vinha do
`measure_fusion_v3.py`, que concorda em @1/@10 e divergia na 4ª decimal.

A refatoração `rag_core` foi provada behavior-preserving por **três vias
independentes**: o controle reproduz, **168.300 pares** (pergunta, doc) com igualdade
exata de float e 0 divergências, e `eval_summary.json` byte-idêntico (mesmo sha256).

---

## 3. Achado principal — o benchmark vaza para dentro do índice

O auditor (19 benchmarks, 979 perguntas, 16244 synthetic_questions, 7019 claims)
devolveu **FAIL**: 1037 achados FAIL, 668 WARN.

| check | n |
|---|---|
| `1-exato` — pergunta **idêntica** a uma synthetic_question indexada | **158** |
| `3-jaccard` / `2-ngrama` — quase idêntica | 92 / 17 |
| `7-split` — mesma pergunta em vários arquivos | **309** |
| `8-duplicata` — near-duplicate **entre** arquivos | **748** |
| `5-codigo` / `6-copia-da-claim` / `9-template` | 202 / 98 / 81 |

**O evaluator indexa `synthetic_questions`** — nas duas versões do código
(pré e pós-refatoração). Isso corrige uma afirmação minha anterior: eu havia dito
"o lab está limpo" com base num grep rodado em `evaluate_rag_benchmark.py` **depois**
da refatoração, quando a montagem do texto já tinha migrado para `rag_core/corpus.py`.
Procurei no arquivo errado e chamei a ausência de resultado. Os números de
`holdout_100` (0,9100), `blind_holdout_50` (0,9600), `fresh_blind_test_40` (0,9333)
e `realistic_30` estavam **inflados** e foram retirados como evidência de qualidade.

**Os splits não são independentes:** os 3 "held-outs externos" compartilham 20–28% das
perguntas e 29–57% das claims com o `blind_v3`; `pure_virgin_test_40` é 97,4% o
`blind_v3` renomeado. Sobreviveram limpos: `blind_v3` e `rest_api_benchmark_ops_40`.

---

## 4. Produção e laboratório não são o mesmo recuperador

`scripts/measure_prod_eval_parity.py` usa os **dois recuperadores reais** (importa o
módulo do MCP, não reimplementa). Linha de base, 262 consultas:

| métrica | valor |
|---|---|
| Jaccard@15 | média **0,1325** · mediana 0,0714 · min 0 · max 0,6667 |
| overlap@1 (mesmo 1º doc) | **0,4351** |
| tau (ordem relativa) | **0,3953** |
| paridade exata | **0/262** |

Cinco divergências estruturais: corpus (7019 × 6732), texto indexado, tokenização
(`\w+` cru × normalizada+stopwords+sinônimos), scoring (BM25 real com IDF × sem IDF e
sem TF) e ausência de rerank no MCP. IDs compartilhados: 6194.

**Escopo:** o lado laboratório mede o **estágio BM25 puro**. MMR/source-diversity e o
reranker vêm depois desse ponto — o número mede a divergência do recuperador, não do
pipeline inteiro.

---

## 5. P0-B — vazamento e ganho são o mesmo campo

A/B medido (`baseline` × `RAG_DROP_SYNTHETIC=1`), dois benchmarks, para o teste ser
falseável:

| benchmark | MRR A → B | Δ MRR (IC95) | @1 A → B |
|---|---|---|---|
| `blind_v3` — **0** tautologias, n=262 | 0,7134 → 0,6951 | −0,0183 [−0,0349, −0,0043] | 0,6565 → 0,6298 |
| `holdout_100` — **72%** tautológico, n=100 | 0,9286 → 0,8595 | −0,0692 [−0,1148, −0,031] | 0,90 → 0,81 |

Razão contaminado/limpo: **3,78×** em MRR, **3,37×** em @1 — o excedente é a tautologia.

**Minha previsão estava parcialmente errada.** Previ "efeito ~nulo no limpo". Há custo
real de −2,67pt @1 **sem vazamento algum**, com IC95 que não cruza zero. As
`synthetic_questions` funcionam **também como expansão de vocabulário** do documento.

**Conclusão:** remover `synthetic_questions` do índice está **rejeitado** como correção
(custa recall legítimo). O defeito está na **construção do benchmark**: o problema não é
a claim ter synthetic_questions indexadas, é a **pergunta do benchmark ser uma delas**.

Veredito do gate: `INCONCLUSIVE` nos dois — correto. O IC do MRR exclui zero (a perda é
real) mas o McNemar binário não é significativo (0 ganhos contra 2 e 3 perdas).

---

## 6. Descontaminação

Aplicada a regra do §5: nenhuma pergunta pode ser (quase) idêntica a uma
synthetic_question da própria claim relevante.

| benchmark | antes | removidas | depois |
|---|---|---|---|
| `blind_v3_slices` | 262 | **0** | 262 |
| `holdout_100_unseen` | 100 | **73** | 27 |
| `fresh_blind_test_40` | 40 | **32** | 8 |
| `blind_holdout_50_vault` | 50 | **35** | 15 |
| `realistic_blind_holdout_30` | 30 | 18 | 12 |
| `golden_qa_*` + `rest_api_*` (8 arquivos) | — | **0** | — |
| **total** | **979** | **182** | **797** |

**Resultado no `holdout_100`:**

| | n | @1 | @10 | MRR |
|---|---|---|---|---|
| original (contaminado) | 100 | 0,9000 | 0,9700 | 0,9286 |
| descontaminado | 27 | **0,7778** | 0,9630 | 0,8459 |
| delta | | **−12,22pt** | −0,70pt | −0,0827 |

**Ressalva:** n=27 dá IC largo. 0,7778 é o único número limpo deste benchmark, não uma
medida de alta confiança.

Os arquivos filtrados **não são versionados** (derivados e regeneráveis; re-introduzem
conteúdo já existente no repo). O que entra é o manifesto de procedência
(`data/eval/decontaminated-manifest.json`), com qid + check por remoção e sem texto de
pergunta.

---

## 7. Gate de promoção (§17)

11 critérios; veredito = **pior** critério, nunca média; `UNKNOWN` não promove.
Veredito atual: **INVALID**.

| critério | estado |
|---|---|
| controle reproduz exatamente | **PASS** |
| leakage scan | **FAIL** (as 158 tautologias) |
| paridade produção/eval | **FAIL** (0/262) |
| manifest corpus/índice · recall@15 global e macro · hard negatives · latência · sealed holdout | `UNKNOWN` |

Dois defeitos do próprio gate, encontrados e corrigidos durante o A/B: o controle era
lido de `--summary` (sobrescrito a cada rodada) em vez do braço A; e o controle do
`blind_v3` (n=262) era exigido em A/B de outro benchmark, tornando todo A/B fora do
`blind_v3` `INVALID` por construção.

---

## 8. Pendências

1. **`7-split` (309) e `8-duplicata` (446) FAIL** — splits não independentes e
   near-duplicata entre arquivos. É o defeito que explica o `pure_virgin_test_40` ser
   97,4% o `blind_v3`. Correção própria (deduplicação entre benchmarks), não feita.
2. **Benchmark V4 (sealed holdout)** — bloqueado por entrada humana. Perguntas novas
   **não podem** ser geradas do corpus: o próprio vazamento medido prova que seriam
   tautológicas por construção. Exige perguntas de fora, escritas ou validadas pelo
   dono. O invólucro (split selado, procedência, gate) é construível sem isso.
3. **Fatia do MCP** — fazer a produção usar `rag_core`. Mudança de produção, bloqueada
   pelo gate enquanto ele diz `INVALID`.
4. **P0-B/P0-C de otimização** — o "BM25" sem IDF e o reranker de escalas misturadas.
   Ganhos medíveis dentro do laboratório.

---

## 9. Reprodução

```bash
PY=<venv>/bin/python

# controle
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  $PY data/eval/evaluate_rag_benchmark.py          # 172/218/221, MRR 0,7134

# vazamento
$PY scripts/audit_eval_leakage.py --json /tmp/leak.json     # exit 1 = FAIL

# paridade produção x laboratório (mesmo env do controle, senão compara outra coisa)
env PYTHONHASHSEED=0 RAG_MEASURE_EXCLUDE_EVIDENCE=1 RAG_INGEST_REST_API=1 \
    RAG_BENCHMARK_FILE=$PWD/data/eval/blind_v3_slices.jsonl \
  $PY scripts/measure_prod_eval_parity.py --top 15

# descontaminação (precisa do relatório acima)
$PY scripts/decontaminate_benchmarks.py --leak-json /tmp/leak.json

# gate
$PY scripts/gate_rag_v4.py
```

Todos os scripts são offline, stdlib + deps do repo, sem path absoluto no código.
