# Veredito independente de governança RAG — Frente D

**Data:** 2026-10-20  
**Escopo:** auditoria documental/metodológica das Frentes A, B e C contra `AGENTS.md`; nenhuma alteração de código, corpus ou avaliação. **Veredito: NO-GO** para deploy, merge em `master` ou promoção de scorer/código associado à alegação de regressão aprovada.

## Síntese executiva

As evidências disponíveis sustentam que o benchmark folders, sob o evaluator de laboratório reportado, ficou abaixo do gate obrigatório: 215/423 @1, 274/423 @5, 293/423 @10 e MRR 0,5682, contra 230/423, 287/423, 301/423 e 0,6016. Isso é um **FAIL do gate nesse run**; não prova que as cinco claims novas causaram a queda. O avaliador contou 41 perguntas sem alvo presente no corpus lab, incluindo 40 `ops-*` cujos alvos estão no MCP mas não no lab. Essas perguntas são indisponíveis por construção para o lab, não erros demonstrados do ranking MCP.

Não foi encontrado indício documental de que A/B/C tenham usado `claim_preview` como gabarito ou gerado perguntas sintéticas para reparar lacunas. A Frente A explicitamente rejeita essa inferência. Contudo, não há auditoria independente de proveniência completa do pool e das cinco claims/evidências nesta validação; portanto **ausência de vazamento não está provada**. O estado correto é: contaminação não observada nos artefatos examinados, risco residual não descartado.

A Frente C não mediu challenger: não há braço challenger, comparação pareada por posição, nem resultado do holdout. Não se pode inferir efeito zero, ganho, perda, nem validade do modelo candidato. Há evidência de execução do baseline lab, não aprovação de mudança.

## Matriz de achados e classificação

| Achado | Classificação independente | Implicação |
|---|---|---|
| Referência de 20/10 reporta 215/423, 274/423, 293/423 e MRR 0,5682; log local preservado em `/tmp/tws-folder-benchmark-20261020.log` contém os mesmos agregados e 41 ausentes. | **OBSERVED (artefatos de sessão/log)**; não reexecutei o benchmark. | Resultados reproduzidos documentalmente, não como execução independente desta auditoria. Os quatro gates falham. |
| Gate de `AGENTS.md`: 230/423 @1, 287/423 @5, 301/423 @10, MRR 0,6016. `pool423-lex-summary-2026-09-21.json` guarda os agregados e 423 details de origem. | **OBSERVED (artefato versionado)**. | Gate de controle; delta observado no run folders: −15 @1, −13 @5, −8 @10, −0,0334 MRR. |
| 41/423 não têm nenhum alvo `relevant_claim_ids` no conjunto lab reportado; A atribui 40 à fatia ops e um caso `eval-40-0039` com dois alvos ausentes em lab e MCP. | **OBSERVED conforme cruzamentos reportados em A; não recalculado aqui**. | Limitação de cobertura/avaliabilidade. Não transformar os 41 em evidência de falha de ranking em documentos presentes. |
| 40 alvos ops estão no MCP consolidado, mas não no lab; presença no índice não demonstra recuperação MCP. | **OBSERVED conforme A**. | Métrica lab não mede qualidade MCP nessa fatia. Exige benchmark e avaliação de produção apropriados. |
| Comparabilidade do run 20/10 com gate histórico: evaluator 7.191 docs vs MCP 7.499; ambiente/versões do ramo denso podem alterar métricas, e as versões exatas do ambiente histórico são UNKNOWN conforme AGENTS. | Contagens e ressalvas **OBSERVED** nos artefatos; contribuição causal de corpus/ambiente é **UNKNOWN**. | O delta não pode ser atribuído a regressão das cinco claims nem usado como comparação pareada válida. Ainda assim, o gate do run informado falhou e não autoriza promoção. |
| Proveniência dos 735 lab-only e 1.043 MCP-only foi comparada por ID; origem individual de 763 MCP-only fora das famílias REST permanece não determinada. | **OBSERVED** quanto às contagens segundo A; subproveniência **UNKNOWN**. | Reconciliação de IDs não prova equivalência semântica nem cobertura completa de fontes. |
| Holdout 100: existe arquivo com 100 linhas; não foi rodado baseline/challenger. | Existência/contagem **OBSERVED**; resultado de retrieval **UNKNOWN**. | Não há transferência out-of-sample demonstrada. |
| Frente B registrou 70 details em snapshot, mas agregados do run têm 423 perguntas. Os 70 não se alinham posicionalmente ao pool, e os scripts diagnósticos não foram executados por risco de caminhos/artefatos. | **OBSERVED** conforme B e snapshot `/tmp/folder-rag-B-run.json`. | Subanálises de erro não representam os 423; explicação causal dos erros e delta permanece UNKNOWN. |
| Challenger da Frente C, seus ganhos/perdas pareados, MRR e comportamento no holdout. | **UNKNOWN / não medido**; não significa zero. | Sem base para GO técnico. |

### Auditoria metodológica e leakage

1. **Gabarito:** o benchmark possui `relevant_claim_ids` e `claim_preview`; A declara que preview não prova proveniência e não deve virar evidência. No evaluator, o critério principal observado é ID exato do alvo (com exceções explícitas para código AWS e chunks de runbook); não se vê uso de `claim_preview` no trecho de avaliação inspecionado. Isso reduz um vetor de leakage no scorer, mas não prova independência de construção do benchmark.
2. **Contaminação sintética:** `AGENTS.md` exige `synthetic_questions` vazio para REST por risco de vazamento. A frente A relata lacunas ID/fonte, não fabricação de alvos; a sessão informa cinco claims empíricas e arquivo de evidência. Não foi feita inspeção da proveniência integral de cada pergunta/alvo contra corpus e fontes, nem verificação completa dos campos sintéticos no corpus efetivamente carregado. Logo, **não observado** não equivale a **descartado**.
3. **Pareamento/IDs:** a Frente C evita corretamente parear por ID e reconhece a unidade de linha/posição; B também alerta para IDs repetidos. Sem details completos para ambas as condições, a disciplina foi respeitada por não inventar flips, mas os efeitos permanecem não medidos.
4. **Controles e reprodutibilidade:** a sessão registra comando de controle, hash-seed e exit code 0; B/C relatam correspondência dos agregados. Mas o gate numérico não foi alcançado. Além disso, o harness grava `data/eval/eval_summary.json`; B relata restauração do rastreado, e C não executou challenger para evitar sobrescrita. A auditoria não verificou por hash nem repetiu a corrida, então preservação integral de estado é **não verificada independentemente**.
5. **Consistência de escopo:** os números de 7.191 lab e 7.499 MCP são corpus distintos. Não tratar inspeção de embedding/consulta densa MCP como validação do benchmark de ranking do lab ou vice-versa. A sessão também diz que a diferença não prova regressão das cinco claims.

## Gates de qualidade e decisão

| Gate/condição | Status |
|---|---|
| Controle obrigatório do pool423: 230/423 @1, 287/423 @5, 301/423 @10, MRR 0,6016 | **FAIL no run 20/10** (215, 274, 293, 0,5682). O número histórico do controle está documentado, mas comparabilidade ambiental/corpus não está garantida. |
| Cobertura de alvos | **FAIL para cobertura do lab no benchmark atual:** 41 perguntas sem alvo; 40 ops excluídas por ausência lab. Isso limita o teto e impede inferência sobre recuperação MCP para essas operações. |
| Ausência de data leakage/contaminação | **INCONCLUSIVO:** nenhum vazamento demonstrado nos relatórios examinados; auditoria integral de proveniência não realizada. |
| Challenger pareado no dev | **NOT RUN / UNKNOWN**. |
| Transferência no holdout 100 | **NOT RUN / UNKNOWN**. |
| Equivalência lab × produção final | **UNKNOWN**, explicitamente não medida para a composição/corpus final desta sessão. |
| Deploy / merge em `master` / promoção de scorer | **NO-GO**. Documentação e dataset podem ser versionados separadamente se forem claramente rotulados como não aprovados; isso não equivale a aprovação de modelo. |

## Blockers e critérios para reconsiderar GO

1. **Controle reproduzível:** restaurar o ambiente/versões comparáveis ou fixar ambiente novo; registrar versões, hash/configuração e corpus; rodar o pool423 sequencialmente antes/depois e atingir exatamente os quatro valores do gate. Qualquer diferença deve ser explicada e aprovada, não normalizada por suposição.
2. **Corpus e cobertura:** congelar snapshots do lab e MCP, registrar IDs/hash e reconciliar os alvos. Tratar os 40 `ops-*` como fatia separada com alvo presente no índice avaliado; tratar `eval-40-0039` como gap de fonte até provar proveniência. Não usar `claim_preview` como fonte de resposta.
3. **Leakage:** auditar linhagem de perguntas, alvos e claims contra evidências/corpus, incluindo campos de pergunta sintética; provar que respostas/gabaritos não foram injetados no texto indexável. Preservar evidência e manifestos antes da corrida.
4. **Challenger:** definir uma alteração e hipótese explícitas, manter default de produção inalterado, executar baseline e challenger no mesmo processo/ambiente/corpus para pool423 e holdout de 100; salvar ranks e candidatos por posição de linha em artefatos isolados, recalcular Hit@k/MRR a partir dos detalhes e reportar pares ganhos/perdidos e incerteza estatística. Repetições devem ser sequenciais e não sobrescrever artefatos canônicos.
5. **Produção:** qualquer afirmação de deploy exige avaliação do caminho MCP real e corpus/índice final, não extrapolação do lab. Declarar configuração completa, smoke test do ramo denso, custo/latência e comportamento de fallback; sem isso, qualidade de produção é UNKNOWN.
6. **Aprovação:** só promover quando controle passar, challenger mostrar ganho transferível no holdout sem regressões relevantes, cobertura/leakage estiverem auditados e todos os artefatos forem verificáveis/reprodutíveis. Se qualquer gate falhar ou permanecer UNKNOWN em ponto crítico, manter NO-GO.

## Veredito final

**NO-GO, com confiança alta para não promover com a evidência disponível; causa da queda, eventual mérito do challenger e leakage residual permanecem UNKNOWN.** A queda observada em relação ao gate é real no registro da corrida, mas sua causalidade não está estabelecida. As 41 ausências são um problema de cobertura/avaliabilidade, não 41 falhas comprovadas de retrieval no MCP. A Frente C não produziu resultado de challenger. Portanto nenhuma conclusão favorável a deploy, merge em master ou promoção de código é metodologicamente autorizada.

**Status desta auditoria:** documentação A/B/C revisada; verificações de código limitadas a fluxo de match e persistência do evaluator; benchmark, proveniência completa, produção MCP e challenger não executados independentemente.
