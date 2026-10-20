# Benchmark de regressão — folders — 2026-10-20

## Execução
```sh
RAG_DENSE_MASK_TO_CORPUS=1 RAG_INGEST_REST_API=1 PYTHONHASHSEED=0 \
RAG_BENCHMARK_FILE=data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl \
python3 data/eval/evaluate_rag_benchmark.py
```
Exit code: 0; 423 perguntas; corpus do harness reportado: **7.191 documentos**. Este corpus do harness é distinto do corpus MCP de produção, que tem **7.499** documentos e índice denso correspondente. Portanto este resultado **não prova regressão das cinco novas claims** por comparação pareada.

| Métrica | Observado | Gate em AGENTS.md | Resultado |
|---|---:|---:|---|
| Hit@1 | 215/423 | 230/423 | FAIL |
| Hit@5 | 274/423 | 287/423 | FAIL |
| Hit@10 | 293/423 | 301/423 | FAIL |
| MRR | 0.5682 | 0.6016 | FAIL |
| Hit@3 | 258/423 | não indicado | informativo |
| Sem resposta no índice | 41/423 | não indicado | informativo |

## Evidência independente de índice MCP
- Corpus MCP consolidado: **7.499 claims**.
- Embeddings `mcp_bge_m3.pt`: **7.499 × 1.024**, ordem de metadados idêntica ao corpus e valores finitos.
- Consulta densa “Como listar job streams no folder QA usando conman” retornou `lab-20261020-folders-stream-success` em top-1 (score 0.7137) e `lab-20261020-folders-list-context` em top-2 (0.6469).
- Cinco novas claims empíricas vêm da validação de `composer`, `conman` e logs TWS; evidência em `data/evidence/lab-validation-2026-10-20-folders-execution.jsonl`.

## Decisão
**NO-GO para promover como regressão aprovada.** Branch de documentação/dataset pode ser versionada isoladamente; não realizar deploy, merge em master ou anunciar que o gate 423 passou. Reproduzir baseline no mesmo ambiente, confrontar variações do scorer/corpus e corrigir discrepâncias antes de promoção.

Saída completa desta execução: `/tmp/tws-folder-benchmark-20261020.log` (log local, efêmero).
