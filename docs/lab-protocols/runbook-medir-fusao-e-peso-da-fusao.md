# Runbook — medir a FUSÃO e o PESO da fusão (RAG)

Protocolo para medir qualquer mudança na fusão lexical×densa deste repo. Escrito porque
a fusão é o ponto onde este projeto **mais se enganou**: quatro trials semânticos
anteriores foram medidos contra baselines DIFERENTES do harness e produziram um "+9"
ilusório (Jina), e um benchmark fraco (40 perguntas com o código na própria pergunta)
fez o híbrido parecer melhor do que é.

## Regra zero

**Toda medição de fusão tem um CONTROLE OBRIGATÓRIO embutido: o baseline lexical do
harness tem de reproduzir `@1 172/262` no blind v3** (corpus congelado = 6732 docs,
`@10 218/262`, `MRR 0,7133`).

Se não reproduzir, a medição é **INVÁLIDA** e nada pode ser concluído. Não "ajuste" o
baseline para fechar o número — investigue por que divergiu.

Motivo: o único jeito de comparar duas configurações é as duas passarem pelo **mesmo**
recuperador e o **mesmo** reranker. Baseline diferente = delta inventado.

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
