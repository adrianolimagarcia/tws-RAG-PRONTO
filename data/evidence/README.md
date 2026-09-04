# Evidence Registry

## Registries

- `claims.jsonl` — canonical, product-only evidence. Each line is one atomic,
  version-scoped claim with an official URL, short supporting quotation,
  retrieval date, verdict and confidence. This file feeds RAG, SFT and factual
  evaluation only. Do not add process or lab metadata here.
- `lab-claims.jsonl` — process claims (prefix `hwa-lab-*`): they describe the
  verification activity itself (which claims were resolved/reclassified in a
  lab round), not product facts. Kept for audit trail; excluded from RAG, SFT
  and factual evaluation. Migrated by `scripts/migrate_lab_claims.py`.

## Rules

Only `verified` and explicitly scoped `version_dependent` claims may support SFT
candidates. Local documents and AI-generated text are not independent evidence.

`scripts/validate_evidence.py` enforces the canonical schema on `claims.jsonl`
and rejects non-official sources, duplicated ids and sensitive content.
