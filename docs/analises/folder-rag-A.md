# Auditoria de reconciliação do corpus — Frente A

**Data:** 2026-10-20. Análise somente leitura. Não foram modificados benchmark, código ou resultados de avaliação; não foi executado benchmark nem usado gabarito sintético.

## Resultado quantitativo

Comparando `load_documents()` com `RAG_INGEST_REST_API=1` contra o `claim_id` de cada linha do consolidado MCP:

| Grupo | IDs |
|---|---:|
| Lab | 7.191 |
| MCP | 7.499 |
| Em ambos | 6.456 |
| Apenas lab | 735 |
| Apenas MCP | 1.043 |
| União | 8.234 |

Ambos os conjuntos são únicos. A diferença líquida é **308** (7.499−7.191), mas há **1.778 divergências de pertencimento** (735 + 1.043). A identidade é comparada por ID exato, não por conteúdo ou semântica.

## Proveniência das diferenças

- **735 lab-only:** todos os IDs têm prefixo `ragflow:`. O carregador percorre `RUNBOOKS_DIR/*.md` e emite chunks com `parse_markdown_ragflow()`. Não há IDs MCP com esse namespace correspondente no consolidado examinado. São chunks de runbook locais, granularidade distinta de claims MCP.
- **1.043 MCP-only:** 276 IDs `hwa-10.2.8-rest-op-*`; 9 IDs `hwa-10.2.8-rest-*` (não operação); 758 outros `hwa-*`; 5 `tws-*`. O consolidado tem essas linhas, mas elas não aparecem no conjunto carregado pelo lab. A correspondência por prefixo não identifica com segurança o arquivo-fonte dos 763 não operação; a origem individual depende de cruzar as entradas e regras de `scripts/consolidate_corpus.py`, e permanece **não determinada** aqui. Não atribuo fonte por suposição.

A opção REST do carregador não deve ser confundida com igualdade de corpora: mesmo ativada, ela não produziu esses IDs de operação no resultado do lab.

## Alvos ausentes no benchmark (41 perguntas)

O cruzamento do `relevant_claim_ids` do pool423 confirmou 41 perguntas sem qualquer alvo no lab (42 IDs-alvo, pois uma pergunta tem dois):

- **40 perguntas `ops-0001`–`ops-0040`:** um alvo REST por pergunta. Todos os 40 IDs exatos não estão no lab e estão no MCP. São lacunas de cobertura entre os conjuntos, não mismatch de grafia. São 40 de 276 operações MCP-only. Presença no MCP não demonstra que o retriever MCP os recupera.
- **`eval-40-0039`:** os alvos `hwa-lab-10.2.8-opens-file-trigger-syntax-0001` e `hwa-lab-10.2.8-opens-hostname-resolution-0001` não aparecem nem no lab nem no MCP. Isso é gap de fonte/coleção nos artefatos examinados, não mismatch identificado. A origem documental precisa de rastreamento adicional; `claim_preview` do benchmark não é prova de proveniência e não deve ser convertido em evidência/gabarito.

IDs completos dos 40 `ops-*` estão nos arquivos de pool e export, todos sob prefixo `hwa-10.2.8-rest-op-`; o sufixo distingue os alvos conforme o endpoint indicado pela linha do benchmark. Contagem e presença foram conferidas em todos os 40 casos individualmente.

## Interpretação, limites e cautelas

1. Não chamar 308 de “os documentos divergentes”: é só o saldo. O conjunto de IDs divergentes contém 735 lab-only e 1.043 MCP-only.
2. A ausência das 40 operações no índice lab explica indisponibilidade do alvo por construção na medição da sessão. Não é evidência sobre qualidade do ranking no índice MCP.
3. Para os dois alvos de `eval-40-0039`, investigar fontes canônicas, evidências válidas, documentação autoritativa e histórico de renomeação, sem sintetizar resposta.
4. A auditoria não compara texto, aliases ou versões, e não executa scorer. Atribuição por arquivo dos 763 IDs MCP-only fora das duas famílias REST não foi comprovada.

## Evidências consultadas

- `docs/sessoes/benchmark-folders-20261020.md`: 7.191 reportados e 41/423 sem alvo no índice lab.
- `rag_core/corpus.py`: fontes e switches usados por `load_documents()`.
- `data/export/tws_corpus_master_consolidated.jsonl`: 7.499 linhas/IDs.
- `data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl`: 423 linhas e alvos.

**Conclusão:** reconciliação por IDs concluída. Subproveniência dos 763 IDs MCP-only fora das famílias REST e origem dos dois alvos de `eval-40-0039` seguem não determinadas. Nenhuma alteração de código/dataset nem execução do benchmark.
