# TWS/HWA Knowledge — RAG Pronto

Base de conhecimento canonico e curado de **HCL Workload Automation / IBM Workload Scheduler**
(9.x e 10.x), pronta para consumo em RAG. Sem artefatos pesados de treinamento — so o
conhecimento em forma legivel (JSONL atomico + markdown).

## Origem / Proveniencia

Gerado a partir do repositorio de dataset
[`adrianolimagarcia/hwa-tws-dataset`](https://github.com/adrianolimagarcia/hwa-tws-dataset)
(privado), no estado do release imutavel **r30-sota-20260904-170227** (claims 1449,
gates P0/P1/P2 PASS). Para atualizar este repositorio, re-exporte do dataset — nunca edite
as claims aqui sem propagar de volta.

## Estrutura

| Caminho | Conteudo |
|---|---|
| `data/evidence/claims.jsonl` | **1449 claims canonicas** (1 por linha): fato atomico + metadata (topic, subtopic, version_scope, platform_scope, evidence_tier, risk, operation_mode, source_url oficial, supporting_quote) |
| `data/evidence/lab-validation-*.jsonl` | Evidencias de laboratorio/producao (incidentes reais: mdmhost-dns, switchplan/IV89990, ...) |
| `data/evidence/claim_terms.tsv` | Indice de termos canonicos / skip-list de claim_ids |
| `data/evidence/automation-action-registry.json` | Registry de acoes de automacao (schema de seguranca) |
| `data/runbooks/` | Procedimentos operacionais (JnextPlan/SwitchPlan, 9.4 EOL, failover MDM/FTA, upgrades, DNS) |
| `docs/` | Contrato evidence-first (R1-R5), decisoes SOTA, troubleshooting, guias |

## Como usar em RAG

1. **Ingestao**: leia `data/evidence/claims.jsonl` linha a linha — cada linha e um chunk
   atomico auto-contido (nao precisa chunking).
2. **Filtro duro antes da busca**: use `version_scope` e `platform_scope` da pergunta
   contra os mesmos campos da claim (exatidao de versao > tudo).
3. **Ranking**: por topic/subject, depois evidence_tier (official_primary >
   official_corroborated > community), depois similaridade.
4. **Seguranca**: o campo `risk` viaja com a claim (`read_only`, `mutating`, `destructive`,
   `credential_sensitive`). Acoes `mutating`/`destructive` **nunca** devem ser executadas sem
   citacao completa da fonte e validacao humana.
5. **Contrato**: toda resposta factual deve seguir `docs/RAG_EVIDENCE_CONTRACT.md` (R1-R5).

## Estatisticas (release r30-sota)

- Claims: **1449** (verified 1392 / community_practice 14 / version_dependent 39 / outros 4)
- Evidencias lab: 100+ arquivos `lab-validation-*`
- Runbooks: 10+ procedimentos · Docs: 29 artefatos (contrato, decisoes, troubleshooting)
- Escopo de versoes: 8.3 → 10.2.8 (HCL/IBM), com enfase em Distributed + casos reais
  (9.4.0.6 EOL, Oracle)

## Seguranca

Sem segredos, sem dados pessoais, sem artefatos brutos. Fontes oficiais HCL/IBM citadas
por claim (`source_url`). Varredura de segredos executada antes da publicacao.
