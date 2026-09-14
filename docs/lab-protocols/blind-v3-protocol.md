# Protocolo do conjunto cego v3 — fatias por propriedade

**Artefato:** `data/eval/blind_v3_slices.jsonl` (262 perguntas scorable) + `data/eval/blind_v3_negatives.jsonl` (5 negativos).
**Construtor:** `scripts/build_blind_v3.py` (reprodutível; `--dry-run` mostra as contagens sem gravar).
**Fora do corpus indexado:** este protocolo vive em `docs/lab-protocols/` e não entra no glob de `data/evidence/`.

## Por que existe

O `@1` do mesmo retriever varia de **23,3% a 100%** conforme o conjunto. A causa dominante **não** é o conhecimento do sistema: é o **estilo/proveniência da pergunta**. Um número único de hit é, portanto, ininterpretável. O v3 quebra o conjunto por **propriedade da pergunta**, e cada fatia tem um teto próprio.

## Regras de honestidade (aplicadas pelo construtor)

1. **Sem vazamento:** nenhuma pergunta que case com **uma** `synthetic_question` do corpus (cobertura mútua ≥ 0,70) entra nas fatias A/B/D. 159 perguntas foram descartadas por isso.
2. **Ground truth fechado por construção:** toda pergunta aponta para `relevant_claim_ids` existentes no corpus (verificado: 0 órfãs).
3. **Fatia D gerada por humano, não pelo corpus:** as 15 perguntas do holdout temporal foram escritas à mão sobre as claims mais novas, **sem** reutilizar as `synthetic_questions` delas e **sem** copiar os tokens distintivos da resposta.
4. **Negativos verificados:** cada termo-alvo da fatia C teve seus tokens **distintivos** conferidos como ausentes do corpus (0 ocorrências).
5. **Métrica congelada:** cada rodada cita `(HEAD, n_docs)` e o `eval_summary.json` commitado é restaurado byte a byte após rodadas de diagnóstico.

## As quatro fatias

| fatia | definição | n | teto medido (@1) |
|---|---|---|---|
| **A — com âncora** | a pergunta carrega código de mensagem (`AWS*####`) ou termo exato em caixa alta | 107 | **86,0%** |
| **B — sem âncora** | paráfrase sem código/termo exato | 140 | **55,0%** |
| **C — negativos** | a resposta **não existe** no corpus; o correto é abster | 5 | métrica de abstenção (não implementada — limite declarado) |
| **D — holdout temporal** | pergunta escrita sobre claims novas (`source_file` ≥ 2026-09-13) | 15 | **40,0%** |

Baseline completo (corpus 6894 docs, HEAD `0f308b9`, `RAG_DROP_*` desligado):

| fatia | @1 | @5 | @10 | MRR |
|---|---|---|---|---|
| A | 86,0% | 91,6% | 92,5% | 0,8840 |
| B | 55,0% | 77,9% | 83,6% | 0,6422 |
| D | 40,0% | 46,7% | 53,3% | 0,4400 |

## Leitura

- **A âncora é o fator dominante:** 86% com âncora contra 55% sem. A pergunta que traz o código/termo exato é quase resolvida por casamento lexical; a paráfrase cai 31 pontos.
- **O conhecimento mais novo é o pior recuperado (D = 40%).** O holdout temporal é o teste mais duro e o mais relevante: é o que mede se o sistema aprende com o que o laboratório acabou de produzir.
- **A fatia B é onde mora o ganho real de engenharia** (77,9% @5 → 55% @1: há 33 pontos de ordenação a recuperar sem tocar em recall).

## Ablações de medição (interruptores no avaliador, default OFF)

| ablação | efeito medido |
|---|---|
| `RAG_DROP_SYNTHETIC=1` (remove a pergunta embutida do índice) | `holdout100` 89%→80%; `holdout50` 98%→92%; `messages` 100%→100%; conjunto ativo 53→54 |
| `RAG_DROP_CTXPREFIX=1` (remove o `context_prefix` repetido) | **nenhum** efeito (ativo 75,7%→75,7%; holdout100 89%→89%) |
| A1+A2 combinados | ativo 54/70 (77,1%), holdout100 82% |

**Conclusão corrigida:** o vazamento da pergunta embutida é real e vale **6–9 pontos** nos conjuntos derivados de claim — mas **não** explica o spread inteiro (o `messages` fica em 100% sem ele, e `pure_virgin` fica em 95% com 2,5% de embutimento). O que domina o número é o **estilo da pergunta**.

## Como usar (regra de ouro)

1. **Nunca tune e meça no mesmo conjunto.** Tune em A; valide em B/D.
2. **Reporte por fatia.** Um número agregado esconde 31 pontos de diferença.
3. **Toda melhoria tem de aparecer em B e/ou D** — ganho só em A é ganho lexical, não de recuperação.
4. **A fatia C exige métrica de abstenção** (hoje inexistente): declarar como limite em vez de inferir.

---

## Adendo — ataque às fatias B/D: teto medido e resultado negativo do re-rank lexical

**Correção de baseline:** as fatias passaram a carregar `runbook_ref` (o v3 não o trazia, o que desligava o match por chunk de runbook do avaliador e deixava o v3 mais estrito que o real). Baseline corrigido: **A 90,7% · B 57,1% · D 40,0% @1**.

**Sandbox:** `scripts/rerank_sandbox.py` replica o pipeline (bm25 → sort → diversidade → 2ª etapa) **sem alterar o avaliador**. A replicação foi validada: baseline replicado **183/262 (69,8%)** idêntico ao avaliador, e **232/232** ranks do matcher do sandbox coincidem com os do avaliador (0 divergências).

**Resultado 1 — o re-rank existente é um lever só-de-âncora:**

| estágio | A | B | D |
|---|---|---|---|
| 1º estágio (sem re-rank) | 78,5% | 57,1% | 40,0% |
| após a 2ª etapa do avaliador | **90,7%** (+12,2) | 57,1% (**0,0**) | 40,0% (**0,0**) |

**Resultado 2 — re-ranker linear sobre o top-50 é pior que o baseline** (features normalizadas em [0,1] não são comparáveis entre si nem com o boost aditivo sobre o score cru do BM25): paridade 76,6% (A) / 52,1% (B); especificidade 61,7% / 38,6%; esp+paridade 73,8% / 50,0%.

**Resultado 3 — o boost de especificidade não transfere.** Preservando a ordem baseline e somando o sinal de especificidade em unidades de posição, a **ascensão coordenada na fatia A (tune) não encontrou nenhum peso** — o melhor em A é o próprio baseline. Efeito isolado (peso 2): `f_rarecov` B 57,9% (**+0,8** = 1 pergunta em 140); `f_minidf` B 56,4%; `f_type` B 55,7%; `f_contig` B 57,1%; `f_entity` A 89,7%. **Nenhum ganho transfere de A para B/D.**

**Resultado 4 — o teto, que é o achado que importa:**

| fatia | recall@50 | @1 hoje | **folga** |
|---|---|---|---|
| A | 97,2% | 90,7% | +6,5 pts |
| B | 87,1% | 57,1% | **+30,0 pts** |
| D | 73,3% | 40,0% | **+33,3 pts** |

O doc correto **já está no pool de 50** em 87,1% (B) e 73,3% (D). Logo o gargalo de B/D é **ordenação semântica**, não recall — e o sinal necessário não é lexical.

**Conclusão do adendo:** B/D **não** são atacáveis por re-ranking lexical. Exigem sinal semântico (embedding/cross-encoder), ausente no ambiente (sem `sentence_transformers`; cache HF só com whisper; ADR-002 descartou o `bge-reranker` por exigir `torch`+`transformers` ~2 GB). O próximo passo é **decisão de infra**, não mais tuning.
