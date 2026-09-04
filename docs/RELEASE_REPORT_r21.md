# Release Report — r21-sota (2026-08-25)

**Snapshot:** `data/releases/r21-sota-20260825-140052/`
**Release anterior:** `r20-sota-20260825-105238` (baseline de regressão)
**Manifesto:** `snapshot_manifest.json` (15 artefatos congelados, SHA-256 por arquivo)

---

## 1. Escopo da rodada

Rodada **hwa-aida-1028-docker-2026-08-25**: instalação, configuração e validação
em laboratório do **AI Data Advisor (AIDA)** 10.2.8 via Docker, a partir do pacote
`HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz` (1.8 GB, sha256 `facc5bf6…`).

- 7 claims novas verificadas (lab + fonte oficial AIDA User's Guide 10.2.8):
  `hwa-10.2.8-aida-{intro-0001, install-0002, es-oom-0003, network-host-0004,
  credentials-0005, metrics-0006, ui-0007}`
- 9 evidências lab: `data/evidence/lab-validation-2026-08-25-aida-docker.jsonl`
  (0061–0069: tar/extract, docker load, OOM fix, extra_hosts, common.env,
  credentials, metrics flow, UI health, AIDA.sh CONTAINER_RUNTIME)
- 14 candidatos SFT promovidos (7 PT / 7 EN) após auditoria independente.
- Runbook P33 + `docs/TROUBLESHOOTING_AIDA_DOCKER.md`.

## 2. Métricas

### Claims
| Métrica | r20 | r21 | Δ |
|---|---|---|---|
| claims.jsonl | 1185 | 1192 | +7 |
| verified | 1119 | 1126 | +7 |
| topic novo `aida` | 0 | 7 | +7 |

### SFT (approved.jsonl)
| Métrica | r20 | r21 | Δ |
|---|---|---|---|
| aprovados | 15569 | 15583 | +14 |
| topic `aida` | 0 | 14 | +14 |

- Idiomas: pt=7640 / en=7943 (balanço 49,0%/51,0%).
- Riscos: read_only=10773, mutating=2857, destructive=981, credential_sensitive=972.

### Splits (leakage-safe por famílias conectadas)
| Split | r20 | r21 |
|---|---|---|
| train | 11356 | 11366 |
| validation | 2788 | 2790 |
| test | 1425 | 1427 |

### Eval independente (gold factual PT/EN)
| Métrica | r20 | r21 | Δ |
|---|---|---|---|
| casos | 4076 | 4104 | +28 |
| pt / en | 2038/2038 | 2052/2052 | — |

### Gates (validate_all.py, 8 gates)
| Gate | Resultado |
|---|---|
| validate_evidence (--require-corroboration) | PASS (1192) |
| validate_sft (approved, --require-risk-coverage) | PASS (15583) |
| split_sft | PASS (11366/2790/1427) |
| validate_eval | PASS (4104) |
| validate_rag_contract | SKIP (sem corpus RAG) |
| validate_function_calls | PASS |
| contradiction_gate | PASS (1174 elegíveis, 0 pendentes) |
| regression_gate (r20→r21) | PASS (sem queda >5%; destructive 0%) |

Integridade: 12 artefatos monitorados, nenhum alterado durante os gates.

## 3. Auditoria independente (segregação de deveres)

- **Auditor:** `hwa-dataset-auditor`.
- **Pacote congelado:** `data/sft/candidates_aida_2026_08_25_frozen.jsonl`
  (sha256 `a5f5ec5f…c76c`), 14 records.
- **1ª rodada:** APROVADO COM RESSALVAS — C1 (MEDIUM): `CONTAINER_RUNTIME`
  obrigatório não verificável contra o GitHub público (que é 10.2.6, não 10.2.8);
  C2 (MEDIUM): versões OpenSearch/Keycloak do 10.2.8 (2.19.6/26.6.4) diferem do
  README público (2.3.0/24.0.0 p/ 10.2.6).
- **Correção (builder):** evidência lab 0069 (AIDA.sh 10.2.8 real exige
  CONTAINER_RUNTIME — prova direta do script, linhas 40-51) + notas nas claims
  install-0002/intro-0001 documentando a divergência de versões.
- **Re-auditoria (delta):** FINAL **APPROVED** — caveats resolvidos, hash do
  pacote inalterado, nenhum record modificado.
- **Gate extra:** 4 claims sensíveis (mutating/credential_sensitive) receberam os
  campos obrigatórios `preconditions`/`impact`/`reversibility`/`stop_criterion`
  (exigência do `validate_evidence --require-corroboration`).

## 4. Rejeitadas e pendências

- **Claims rejeitadas:** nenhuma (7/7 aprovadas).
- **Candidatos SFT rejeitados:** nenhum (14/14 aprovados).
- **Caveats residuais:** nenhum bloqueante. Notas LOW já incorporadas.

## 5. Riscos residuais

1. **Gate RAG (5) SKIP** — sem corpus de respostas; ablação pendente até treino
   QLoRA (inalterado).
2. **Recursos de produção vs lab**: o AIDA oficial pede 32Gi RAM (request 8Gi);
   o lab validou com valores reduzidos (es heap 768m, limits 3G). As claims/SFT
   apresentam a adaptação lab explicitamente ("low-RAM machine", "host-only lab").
3. **GitHub público (10.2.6) diverge do pacote 10.2.8** (AIDA.sh sem auto-deteção
   de runtime; OpenSearch 2.19.6/Keycloak 26.6.4 vs 2.3.0/24.0.0) — documentado
   nas claims; referir sempre ao pacote 10.2.8.
4. **OpenSearch cluster yellow** (1 nó) — esperado em lab single-node.
5. **Certificado self-signed / EXTERNAL_HOSTNAME** — UI do AIDA acessível apenas
   via host exato configurado (HTTPS 9432); DWC segue com exceção manual.

## 6. Consumo do treino

`config.yaml` atualizado por `release_snapshot.py`:
- `release.id: r21-sota-20260825-140052`
- `sft.approved_file: data/releases/r21-sota-20260825-140052/approved.jsonl`

O treino consumirá exclusivamente o snapshot imutável (P0); nenhum treinamento
foi iniciado nesta rodada.
