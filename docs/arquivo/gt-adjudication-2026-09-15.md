# Material de adjudicação de GT — benchmark de 70 perguntas

> Gerado read-only por `scripts/probe_lab_evidence_pool.py` + `eval_summary.json`.
> **Nada aqui foi alterado**: é insumo para decisão do dono. `docs/` não entra no corpus do RAG.

## 1. Expectativa SOBRE-ATRIBUÍDA (mesmo claim em perguntas tematicamente alheias)

O claim `hwa-lab-10.2.8-rest-api-v2-auth-0001` é esperado em **5** perguntas; só a primeira é sobre autenticação.

| pergunta | rank | tema do esperado | bate com a pergunta? |
|---|---|---|---|
| eval-0011 | 3 | auth da API v2 | sim |
| eval-0023 | 3 | auth da API v2 | **não** |
| eval-0026 | 6 | auth da API v2 | **não** |
| eval-0027 | 3 | auth da API v2 | **não** |
| eval-0029 | 4 | auth da API v2 | **não** |

## 2. As 17 perguntas fora do @1 — esperado × top-1

| pergunta | rank | esperado (1º) | top-1 entregue |
|---|---|---|---|
| eval-0010 | 3 | `hwa-10.2.8-backup-backup-master-data-0001` | `hwa-master-domain-manager-registered-master-00` |
| eval-0011 | 3 | `hwa-lab-10.2.8-rest-api-v2-auth-0001` | `hwa-lab-10.2.8-single-user-wauser-unification-` |
| eval-0015 | 18 | `hwa-lab-10.2.8-single-user-wauser-unification-` | `ragflow:hwa-10.2.8-mdm-engine-failure-backup-b` |
| eval-0021 | 62 | `hwa-lab-10.2.8-planman-resync-hot-recovery-000` | `hwa-10.2.3-symphony-database-replication-0044` |
| eval-0023 | 3 | `hwa-lab-10.2.8-rest-api-v2-auth-0001` | `hwa-msgcat-awsbeh029e` |
| eval-0024 | 4 | `hwa-lab-10.2.8-dynamic-pool-workstation-e2e-00` | `hwa-10.2-distributed-conman-showjobs-0001` |
| eval-0026 | 6 | `hwa-10.2.8-dwc-install-0024` | `hwa-install-liberty-1028-procedure-0009` |
| eval-0027 | 3 | `hwa-lab-10.2.8-rest-api-v2-auth-0001` | `hwa-10.2.8-dwc-restv2-submit-0011` |
| eval-0029 | 4 | `hwa-lab-10.2.8-rest-api-v2-auth-0001` | `ragflow:hwa-10.2.8-edwa-eif-jobstatus-msglog-e` |
| eval-0039 | 7 | `hwa-10.2.8-conman-switcheventprocessor-0010` | `hwa-10.2.8-backup-backup-master-data-0001` |
| eval-0040 | 5 | `hwa-10.2.8-incident-switchmgr-thiscpu-0067` | `hwa-10.2.8-incident-symphony-master-0060` |
| eval-0041 | 3 | `hwa-10.2.8-distributed-cli-api-key-jwt-0001` | `hwa-version-matrix-composer-conman-9.5-0008` |
| eval-0042 | 2 | `hwa-10.2.8-sec-api-key-0017` | `hwa-10.2.8-vm-orchestration-cli-0014` |
| eval-0061 | 3 | `hwa-10.2.8-backup-backup-master-data-0001` | `hwa-themaster-domain-manager-0001` |
| eval-0062 | 6 | `hwa-lab-10.2.8-bmdm-container-install-0001` | `hwa-10.2.8-capacity-symphony-file-0017` |
| eval-0065 | 2 | `hwa-10.2.8-composer-new-0001` | `hwa-10.2.8-composer-add-0001` |
| eval-0069 | 4 | `hwa-10.2.8-showjobs-wildcard-ws-filter-0111` | `hwa-10.2-distributed-conman-showjobs-0001` |

## 3. O que a medição de pool mostrou (fatia D)

- 49 dos 50 documentos esperados **estão no pool** (score BM25 > 0); só 1 tem score 0.
- Portanto o gargalo da fatia D é **ordenação sob competição**, não cobertura de tokens.
- Quem ganha é sistematicamente o documento **genérico-autoritativo** do produto:
  - `v3-D-0002` (rank 214): topo = 5 mensagens `hwa-msgcat-awsbia*` (o catálogo, 62% do corpus)
  - `v3-D-0003` (rank 405): topo = 5 claims `hwa-10.2.8-composer-*`
  - `v3-D-0001` (rank 355): topo = 5 claims `backup-*`
- Mesmo padrão estrutural já visto nas man pages (−1 @1) e na adjudicação dos misses.

## 4. Decisões que dependem do dono

1. **GT v2**: corrigir a sobre-atribuição acima (isso **baixa** o número medido — é o número honesto).
2. **Pesos por tipo** (`canonical_claim` 1.25 × `lab_evidence` 1.20): mexer aqui é decisão de métrica.
3. **Texto da `lab_evidence`**: nomear os objetos do produto (comandos, códigos, arquivos) que a evidência já descreve — sem citar a pergunta, que seria tuning.
