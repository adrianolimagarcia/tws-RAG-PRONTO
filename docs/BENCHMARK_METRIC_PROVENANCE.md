# Proveniência da métrica do benchmark RAG (TWS/HWA 10.2.8)

## Regra de citação (obrigatória)

A métrica deste harness é **DEPENDENTE DO CORPUS**. Todo número de benchmark deve ser
citado **com o estado do corpus**: `(<HEAD>, <n_docs>)`. Um número sem esses dois
atributos é **ambíguo** e não deve ser tratado como "o baseline".

## Baseline atual (canônico)

| atributo | valor |
|---|---|
| HEAD | `d942790` |
| documentos indexados | **6869** |
| benchmark 70 (Hit@1) | **53/70 (75,7%)** |
| benchmark 70 (Hit@10) | **68/70 (97,1%)** |
| benchmark 70 (MRR) | **0,8214** |
| virgem PT 24 (Hit@1) | 8/24 (33,3%) — MRR 0,5306 |
| virgem expandido 39 (Hit@1) | 17/39 (43,6%) — MRR 0,6012 |

Reprodução: `PYTHONHASHSEED=0 python3 data/eval/evaluate_rag_benchmark.py`
(saída byte-idêntica ao `data/eval/eval_summary.json`; `PYTHONHASHSEED=random` dá o
mesmo resultado — o harness é determinístico).

## Proveniência da queda 54/70 → 53/70 (não é bug nem não-determinismo)

`git log` de `data/eval/eval_summary.json`:

| commit | Hit@1 | n_docs | contexto |
|---|---|---|---|
| `547d53b` | **0,7714 (= 54/70)** | corpus menor | antes das evidências/runbooks de HA |
| `d742037` | **0,7571 (= 53/70)** | corpus maior | após a frente #1 (link-isolation) |

**Causa:** a pergunta `eval-0029` ("qual arquivo de log registra `CWWKF0011I` / engineServer
Liberty pronto") tinha o chunk correto `ragflow:hwa-10.2.8-wsl-lab.md:0160` em **rank 1**;
com o crescimento do corpus ele caiu **rank 1 → 3 → 4**, porque chunks de runbooks **novos**
passaram a ocupar o topo:
`hwa-10.2.8-autofailover-link-isolation-test.md:0001/0003` e depois
`hwa-10.2.8-edwa-eif-jobstatus-msglog-e2e.md:0001`.

⇒ É **crescimento de corpus competindo no rank 1**, comportamento esperado de retrieval —
**não** é regressão de harness, **não** é não-determinismo. (O projeto já corrigiu 3 causas de
não-determinismo: glob sem `sorted`, `sort` sem desempate, soma de floats sobre `set` — nenhuma
delas está reaberta.)

## Nota sobre o `FAMILY_BOOST`

O comentário do `FAMILY_BOOST` em `data/eval/evaluate_rag_benchmark.py` citava
"baseline 54/70 @1 e 68/70 @10 preservados" — **desatualizado** (era o corpus de `547d53b`).
Corrigido para citar o número **com** `(HEAD, n_docs)`.

## Consequência prática

- Ao adicionar/remover documentos do corpus, o baseline **pode mudar** — sempre re-medir e
  registrar `(HEAD, n_docs)` junto do número.
- Adicionar fontes **duplicadas** do catálogo já indexado não muda a métrica (delta zero
  medido em `hwa-lab-10.2.8-harness-ha-claims-index-coverage-negative-0001`).
- O gate de CI roda o benchmark; o `eval_summary.json` commitado deve refletir o HEAD.
