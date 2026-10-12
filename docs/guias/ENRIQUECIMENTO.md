# Guia de Enriquecimento da Base de Conhecimento

Como adicionar manuais, interações documentadas e evidências de lab à base,
do jeito certo — sem quebrar o corpus nem os índices.

## Princípios

1. **Nunca edite `data/export/tws_corpus_master_consolidated.jsonl` diretamente.**
   Claims novas entram como `lab-validation-*` (lab) ou com `source_url` (oficial).
2. **Toda claim precisa de evidência.** Sem evidência de lab ou fonte oficial,
   a claim não entra (ver `docs/specs/RAG_EVIDENCE_CONTRACT.md`).
3. **Enriquecimento é seguro por padrão:** `apply_enrichment_safe.py` não injeta
   keywords genéricas (poluem o IDF do BM25) e limita a 2 perguntas sintéticas
   por claim.

## Passo a passo

### 1. Documente o material novo

- **Manual / procedimento:** crie um arquivo em `data/knowledge/` seguindo o
  formato jsonl existente (veja `man-pages-derived.jsonl` como exemplo).
- **Interação / troubleshooting:** documente em `data/runbooks/` como runbook.
- **Evidência de lab:** registre em `data/evidence/` e referencie na claim.

### 2. Valide o enriquecimento (modo seguro)

```bash
cd /run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO
python3 scripts/apply_enrichment_safe.py --help   # ver opções
python3 scripts/apply_enrichment_safe.py          # gera data/export/tws_corpus_enriched_safe.jsonl
```

Para lotes maiores (com LLM):

```bash
python3 scripts/batch_enrich_corpus.py --workers 6 --limit 50
```

### 3. Reindexe

```bash
python3 scripts/build_dense_index_mcp.py
python3 scripts/check_index_coverage.py   # confere cobertura do índice
```

### 4. Meça o ganho

```bash
python3 scripts/calibrated_full_benchmark.py
```

Compare Hit@1 / MRR com a linha de base (93,5% / 0,948). Se regrediu,
descarte o lote e investigue.

## Lacunas prioritárias (medidas em 2026-09-11)

Ver `docs/guias/PLANO_ENRIQUECIMENTO_DATASET.md`. Resumo:

| # | Ação | Cobertura atual |
|---|---|---|
| P1 | Catálogo de mensagens de erro | 22,3% (maior lacuna) |
| P2 | Classificação taxonômica ("Outros" 63%) | em andamento |
| P3 | Matriz de versões (9.5/10.1/10.2.x) | quase só 10.2.8 |
| P4 | Incidentes de lab (HA/failover/recovery) | 13 claims |
| P5 | Camada de configuração | lab + docs |
