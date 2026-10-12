# README da sessão — ponte EN→PT e o inventário do que NÃO funciona (2026-09-20)

> **Este arquivo não substitui o `README.md` do projeto.** É o registro da sessão de
> 2026-09-20, que atacou a consulta em inglês e testou cinco alavancas de ganho geral.
> O `README.md` continua sendo a apresentação do dataset e do pipeline.
>
> **Regra de evidência usada aqui:** todo número vem de execução registrada em
> `data/evidence/`. O que não foi medido está escrito `UNKNOWN` — não estimado.
>
> **Mudança de produção desta sessão:** `mcp_server/` — a única alteração de
> comportamento entregue. Tudo o mais é medição. A árvore foi restaurada
> (`eval_summary.json`, `rag_core/lexical.py`, `evaluate_rag_benchmark.py`) a cada
> experimento que piorou.

---

## 1. O que foi feito

Sete commits, cada um com evidência própria:

| # | entrega | artefato | commit |
|---|---|---|---|
| 1 | Fusão densa guiada por confiança — **medida e não ligada** | `data/eval/measure_dense_fusion_gain.py` | `a7ab1d4` |
| 2 | **Retratação**: a manchete "+30 @1" era erro de medição | evidência corrigida | `4c01638` |
| 3 | Veredito da fusão em pool de 296 perguntas limpas — **regride** | `data/eval/measure_dense_fusion_pooled.py` | `539ef5d` |
| 4 | Restaura o `eval_summary.json` (artefato de run) | — | `9b536db` |
| 5 | Conjunto sintético de 27 perguntas virgens, com asserção anti-vazamento | `scripts/generate_synthetic_virgin_v2.py` | `253d568` |
| 6 | Cinco alavancas simples de ganho geral — **nenhuma passa de ruído** | evidência | `9bd84c1` |
| 7 | **Ponte EN→PT por tradução da consulta** — o ganho da sessão | `mcp_server/tws_traduz.py` | `3ffc21b` |

---

## 2. O que deu certo

### 2.1 A consulta em inglês era a lacuna real — e está fechada

As **mesmas perguntas**, em dois idiomas, no buscador do próprio MCP (7.019 claims):

| cenário | @1 | @5 | MRR |
|---|---|---|---|
| inglês, sem ponte | 6/24 = **25,0%** | 12/24 = **50,0%** | 0,342 |
| inglês, **com a ponte** | 13/24 = **54,2%** | 17/24 = **70,8%** | 0,595 |
| português nativo | 13/24 = 54,2% | 17/24 = 70,8% | 0,601 |

O inglês deixa de ser a lacuna: **passa a acertar igual ao português**. E o português
**não regride** (13 @1 / 17 @5, idêntico antes e depois) — o requisito duro.

Pelo harness de 423, com tradução humana: @1 `2→10` (McNemar `p=0,0215`, ganha 9 / perde 1)
e @5 `3→20` (`p=0,0001`, ganha 18 / perde 1).

### 2.2 Não é preciso LLM grande — e a medição mostrou por quê

Um MarianMT dedicado (`Helsinki-NLP/opus-mt-tc-big-en-pt`, **938 MB, CPU, offline**) fez
13/24 @1 — **empata com a tradução humana** (13/24). A latência é 1,5–1,8 s por consulta
em inglês e **16 ms em português** (a consulta PT não passa pelo tradutor).

O modelo multilíngue maior foi testado e **rejeitado**: misturava espanhol e francês
("El producto cessó", "processeur", "n'a pu").

### 2.3 O controle continua sólido

| métrica | valor |
|---|---|
| Hit@1 (pool produção, n=423) | **230** = 54,4% |
| Hit@3 | 272 = 64,3% |
| Hit@5 | **287** = 67,8% |
| Hit@10 | 301 = 71,2% |
| Hit@15 | 311 = 73,5% |
| MRR | **0,6016** |
| teto do benchmark | 90,3% (41 das 423 sem resposta no índice) |

Reproduzido após cada experimento. `md5` do corpus antes e depois de tudo:
`4e43f65b3ab7` — intacto.

### 2.4 Onde o sistema acerta, por forma da pergunta

| forma da pergunta | @1 | @5 |
|---|---|---|
| cita o código da mensagem | 34/34 = 100% | 100% |
| pure_virgin (n=39) | 36 = 92% | 39 = 100% |
| bem-formada, outros domínios | 74–76% | 91–95% |
| **só o sintoma, em português** | 13/24 = 54% | 17/24 = 71% |
| **só o sintoma, em inglês** | **13/24 = 54%** (era 25%) | **71%** (era 50%) |

Por faixa de confiança do MCP (n=423): alta `113/135 = 84%`, média `65/129 = 50%`,
baixa `52/159 = 33%`.

---

## 3. O que deu errado

### 3.1 Eu otimizei um número agregado e dei voltas por isso

O Hit@1 do pool é dominado por perguntas **onde o sistema já funciona**. Toda alavanca
parecia "não dar ganho" justamente porque o gargalo está em outro lugar: o esparso já tem
o documento certo no top-15 em **73,5%** dos casos, e acerta @1 em 54,4%. **Falta ordem,
não recall.** Só ao decompor por forma da pergunta isso ficou visível.

### 3.2 Cinco alavancas de ganho geral — nenhuma passou

| alavanca | resultado | veredito |
|---|---|---|
| janela do reranker (`RAG_RERANK_TOP` 0→200) | 214 → **230** → 219 | o default 20 **já é o ótimo** |
| desligar o reranker | 214 vs 230 | ele **ajuda** (+16) |
| denso reordenando o pool esparso (`rescore` K=20/50/100) | 220 / 203 / 196 | piora |
| conserto do tokenizador de acento | 224 (legado) / 223 (BM25 real) | piora |
| BM25 real (`RAG_BM25_REAL=1`) | 235 vs 230, **p=0,50**, +13% de tempo | **ruído** |

Meu palpite inicial de que "o reranker é o gargalo" estava **errado** — medido, ele ajuda.

### 3.3 Achei um bug real, mas ele não paga

O tokenizador **exclui letras acentuadas**: `estação` virava `"esta"+"o"`, **`não` e
`licença` eram descartadas inteiras**, `binário` virava `"bin"+"rio"`. Consertei com dobra
de acento por NFD (preservando o comprimento, porque o BM25 casa subsequência por
posição). Medido: **224 vs 230 — piora** nos dois scorers. O scorer foi calibrado junto com
o defeito (`AVG_DL=60` fixo, sem IDF real).

**Revertido.** Consertar tokenizador **e** scorer juntos exigiria recalibrar e revalidar a
suíte toda, sem garantia de ganho líquido. Fica registrado como defeito conhecido, com o
efeito medido.

### 3.4 A expansão pelo glossário curado piorou

Antes de recorrer à tradução, testei o barato: expandir a consulta pelos tópicos de
`hwa_bilingual_terms.json`. Só 7 das 24 perguntas casaram algum tópico, e o resultado foi
`@1 1/24` e `@5 2/24` — **piora**. Termo de tópico amplo é ruído de IDF.

Contexto que explica: o mapa `TERM_EXPAND` cobre **3 de 166** palavras inglesas das
perguntas; o glossário tem 104 termos, de jargão de tópico, não da linguagem de sintoma.

### 3.5 O "melhor dos dois por score" perdia acertos

A primeira integração no MCP comparava o score BM25 da consulta original com o da
traduzida e ficava com o maior. Medido: **11 acertos contra 13** — score BM25 de duas
consultas diferentes **não é comparável** (depende da IDF dos termos que cada uma contém),
e o score alto da consulta original ganhava com a resposta errada no topo. Corrigido: se a
consulta não é portuguesa, é a tradução que vai à busca.

### 3.6 Errei o protocolo de teste duas vezes (e o erro era meu, não do servidor)

Rodei o servidor MCP por stdio e vi `results: []`, concluindo que a ponte não funcionava.
Duas vezes o defeito era do meu payload: usei `"args"` onde o protocolo é `"arguments"`, e
li `result.results` quando a resposta vem em `result.content[0].text`. O servidor estava
certo; eu é que estava testando errado. Depurar o caminho direto (`handle_tool_call`)
separou as duas coisas.

---

## 4. Estado atual

### Instrumentos

| instrumento | onde | para que |
|---|---|---|
| harness de 423 | `data/eval/evaluate_rag_benchmark.py` | controle de produção |
| medidor da ponte | `data/eval/measure_ponte_en_pt.py` | EN × traduzida × latência, no caminho do MCP |
| gerador de perguntas virgens | `scripts/generate_synthetic_virgin_v2.py` | 27 perguntas, asserção anti-vazamento |
| medidores de fusão densa | `data/eval/measure_dense_fusion_{gain,pooled}.py` | o que foi medido e não ligado |

### Evidência desta sessão (`data/evidence/`)

- `lab-validation-2026-09-20-ponte-en-pt-por-traducao.jsonl` — **o ganho da sessão**
- `lab-validation-2026-09-20-simple-levers-exhausted.jsonl` — as cinco alavancas que falharam
- `lab-validation-2026-09-20-question-shape-determines-dense-fusion.jsonl` — a fusão densa
- `lab-validation-2026-09-20-dense-fusion-{measured-harness,pooled-verdict}.jsonl`

### Solução implementada (`mcp_server/`)

`tws_traduz.py` (novo) + integração na busca de `tws_expert_mcp.py`:

- **detecção de idioma barata** — consulta portuguesa não passa pelo tradutor (16 ms);
- se a consulta não é portuguesa, **é ela que vai à busca, traduzida**;
- **import preguiçoso** de `torch`/`transformers` e **degradação graciosa** — sem o modelo,
  o MCP funciona exatamente como antes;
- `RAG_TRADUZ_EN=0` desliga; `RAG_TRADUZ_MODELO` troca o modelo.

Dependência (opcional): `pip install transformers torch sentencepiece sacremoses`; o modelo
(938 MB) é baixado uma vez e fica em cache — depois, `HF_HUB_OFFLINE=1`.

---

## 5. Próximos passos

### Desbloqueados (não dependem de você)

1. **Generalizar a ponte**: medir perguntas EN de **outros domínios** (runbooks, API REST).
   Hoje o ganho está medido em 24 perguntas de um tipo só — catálogo de mensagens.
2. **Atacar a ordem**: o gargalo restante é ordenação (o alvo está no top-5 em 71–100% dos
   casos). O reranker já está no ótimo; a fusão densa é condicional à forma da pergunta.
3. **Fusão densa condicionada** — medida (+16, n=90, `p=0,0025`), **não implementada**. Exige
   detectar a forma da pergunta antes de consultar.

### Bloqueados por entrada humana

4. **Reconciliar a documentação**: este README e o `README-SESSAO-2026-09-19.md` convivem
   com o `README.md`; decidir se viram seção dele.
5. **Decidir sobre o `mcp_server/tws_traduz.py`**: hoje a ponte liga por padrão e imprime
   `1,5–1,8 s` de latência em consulta inglesa. Em ambiente interativo isso pode ser
   aceitável; em lote, não.

### Bloqueado pelo gate

6. A regra de promoção do projeto continua valendo: a ponte entra na produção **medida e
   reversível**, não por conveniência.

---

## 6. Como reproduzir

```bash
cd /run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO

# controle: o baseline de produção (esperado 230 @1, 287 @5, MRR 0,6016)
RAG_DENSE_MASK_TO_CORPUS=1 RAG_INGEST_REST_API=1 PYTHONHASHSEED=0 \
  python3 data/eval/evaluate_rag_benchmark.py

# a ponte EN->PT no caminho do MCP (com latência)
python3 data/eval/measure_ponte_en_pt.py
RAG_TRADUZ_EN=0 python3 data/eval/measure_ponte_en_pt.py   # controle SEM a ponte

# a ponte com tradução automática (exige transformers/torch/sentencepiece/sacremoses)
python3 data/eval/measure_ponte_en_pt.py --mt

# o servidor MCP de ponta a ponta (protocolo: "arguments"; resposta em content[0].text)
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"tws_expert_search","arguments":{"query":"The console could not find the job stream in the Symphony file.","top_k":3}}}' \
 | python3 mcp_server/tws_expert_mcp.py
```

---

## 7. Ressalvas

- **Divergência encontrada no artefato de run**: o bloco `confianca` de
  `eval_summary.json` traz `top1_correto_faixa_{alta,media,baixa}` = 115/60/39, que somam
  **214** — e não batem com o próprio `hit_rate_at_1` = **230**. Agrupando o campo
  `confianca` dos `details` da mesma corrida, os números somam 230 e batem com o Hit@1:
  alta 113/135 (83,7%), média 65/129 (50,4%), baixa 52/159 (32,7%). **Os números das faixas
  citados nesta sessão vêm dos `details`**, que são autoconsistentes; o bloco agregado é que
  não reconcilia. Fica registrado como defeito do resumo, não corrigido aqui.
- Os percentuais de faixa do docstring do MCP (alta 84,0%, média 29,5%, baixa 20,5%, base
  47,8%) vêm de uma medição **de laboratório**, com outro scorer e outra base — não são os
  mesmos números da tabela acima e não devem ser somados a eles.
- **`UNKNOWN`**: o ganho da ponte em perguntas inglesas de runbooks e API REST não foi
  medido. O que está medido são 24 perguntas do catálogo de mensagens.
- **`UNKNOWN`**: latência e custo da fusão densa em produção (o modelo BGE-M3 tem 2,27 GB).
- O conserto do tokenizador de acento **piora** o resultado isoladamente — não é um
  "quick win" pendente, é um defeito entrelaçado com a calibração do scorer.
- `data/eval/eval_summary.json` é artefato de execução, não de código: toda corrida o
  sobrescreve, e ele é restaurado ao baseline antes de cada commit.
