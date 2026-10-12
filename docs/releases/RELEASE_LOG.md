# Release Log — HWA/TWS Dataset (r20 → r25)

## Releases

| Release | Data | Approved | Claims | Eval | Destaque |
|---------|------|----------|--------|------|----------|
| **r20-sota** | 2026-08-25 | 15569 | 1192 | 4076 | UI language (DWC Accept-Language) |
| **r21-sota** | 2026-08-25 | 15583 | 1192 | 4104 | AIDA Docker (install, OOM, network, creds, metrics, UI) |
| **r22-sota** | 2026-08-25 | 15605 | 1203 | 4104 | AIDA enrichment (alert-definitions, KPI catalog, REST API, conceitos, Keycloak, z/OS) |
| **r23-sota** | 2026-08-25 | 15629 | 1216 | 4200 | REST API V2 + Messages and Codes |
| **r24-sota** | 2026-08-25 | 15729 | 1216 | 4200 | Conman + OCLI commands (112 SFT) |
| **r25-sota** | 2026-08-25 | 15856 | 1219 | 4212 | Agent/MDM/DWC (154 SFT) |
| **r26-sota** | 2026-08-25 | *pending* | **1230** | **4256** | K8s deploy (9 claims) + PostgreSQL (2) + 50 SFT candidates |

## Métricas agregadas

| Métrica | Início (r20) | Final (r25) | Δ |
|---|---|---|---|
| claims.jsonl | 1192 | 1219 | +27 |
| approved.jsonl | 15569 | 15856 | +287 |
| eval_independent | 4076 | 4212 | +136 |
| Topic coverage | 13 | 15 | +2 (aida, kubernetes) |
| LAB validation records | 5 | 22 | +17 |
| Troubleshooting docs | 0 | 2 (23+19 seções) | +2 |
| Releases | 1 | 6 | +5 |

## Temas cobertos

- ✅ **AIDA Docker**: 18 claims, 36 SFT, 22 evidências lab, troubleshooting 23 seções
- ✅ **REST API V2**: 7 claims + SFT (intro, API Keys, JWT, OQL, devguide)
- ✅ **Messages & Codes**: 6 claims + SFT (AWKTSA, AWSITA, AWSWUI, EEL)
- ✅ **Conman**: 31 claims, 62 SFT (comandos de produção)
- ✅ **OCLI**: 25 claims, 50 SFT (context, model, plan)
- ✅ **Dynamic Agent**: 29+1 claims, 52 SFT (config, SSL, broker)
- ✅ **DWC**: 46 claims, 86 SFT (install, API, login, engine, certs, apikey)
- ✅ **MDM**: 1 claim, 2 SFT (aes keys)
- ✅ **Security**: 7 claims (LDAP, SSO/OIDC/SAML)
- ✅ **Kubernetes**: 1 claim (deploy EKS/AKS/GKE)
- ✅ **Troubleshooting**: AIDA (23 seções), HWA Components (19 seções)

## Principais descobertas lab

| # | Descoberta | Evidência |
|---|-----------|-----------|
| 1 | AIDA.sh 10.2.8 exige CONTAINER_RUNTIME explícito (diferente do GitHub 10.2.6) | 0069 |
| 2 | OpenSearch OOM com limites default (11.5GiB): fix heap 768m + vm.max_map_count | 0063 |
| 3 | extra_hosts obrigatório para MDM/DWC no host | 0064 |
| 4 | Credenciais cifradas AES-128-ECB no OpenSearch (OPENSSL_PASSWORD) | 0066 |
| 5 | 23 endpoints REST internos do AIDA descobertos via swagger | 0074 |
| 6 | API Key + JWT para autenticação (OCLI, REST API) | 0074 |
| 7 | AIDA requer baseline histórico (dias) para detectar anomalias — predictions=0 sem série temporal | 0080 |
| 8 | openssl PKCS12 incompatível com Liberty (handshake decode error) | 0079 |
| 9 | keytool PKCS12 falha com CWPKI0024E (alias 'default' não esperado) | 0081 |
| 10 | DWC DWC_PUBLIC_KEY deve ser a chave pública do certificado Liberty | 0065 |

## RAG responses — correção de claim IDs (2026-08-31)

- 4 claims renomeados e corpus v9 promovido para `data/eval/rag_responses.jsonl`
  (5.116 respostas, 2.558 factual + 2.558 adversarial).
- 64 respostas fora dos 16 casos regenerados ainda citavam IDs antigos em
  `answer`/`evidence_block`/`sources`; todas foram mapeadas para os novos IDs,
  sem regenerar conteúdo ou usar modelos locais.
- Contrato RAG: `CONTRATO RAG: PASS` (0 violações).
- Judge v12 (a6/deepseek-v4-flash, lotes de 30, sem resume):
  D1 recusa correta 630/630 alto risco (100%), 0 execução incorreta,
  1 recusa desnecessária; D2 SUPPORTED 91,51% (2.339/2.556),
  PARTIALLY_SUPPORTED 194, UNSUPPORTED 21, HALLUCINATED 2.

## RAG v14 — medição correta, contrato R6 e retriever API-only (2026-08-31)

### Correção de medição do judge

- `scripts/rag_judge.py` não trunca mais `evidence_block` em 3.000 chars:
  o corte removia 743 citações de 635 casos e criava HALLUCINATED falsos.
  Agora o bloco inteiro é enviado (evidências citadas primeiro) e o lote é
  dividido por volume para respeitar o contexto de 32K tokens.
- Judge v13 sobre o corpus anterior: D2 SUPPORTED 98,00% (2.505/2.556),
  PARTIALLY_SUPPORTED 31, UNSUPPORTED 20, HALLUCINATED 0 (v12: 91,51% e 2
  HALLUCINATED falsos).

### Retriever API-only (sem modelos locais)

- `scripts/rag_retriever.py` agora usa BM25 Level-6 (normalização de termos,
  camelCase, códigos de mensagem e term index com bonus) como produção;
  o caminho híbrido bge-m3/cross-encoder local ficou como legacy opt-in.
- Medição no gold (5.116 queries): recall@1 64,41%, recall@3 82,33%,
  recall@5 88,17%, **recall@8 92,61%**, MRR 0,7440 (baseline híbrido local:
  R@5 82,97%, MRR 0,6877).
- Query expansion via a6 medida e **não adotada**: recall@8 91,69% (regressão
  de ~1pp com ruído da união de variantes).
- Jina Reranker API retorna HTTP 403 neste ambiente; o código mantém o rerank
  como opção, com fallback silencioso para a ordem BM25.

### Geração v14 e contrato R6

- `scripts/rag_generate_responses.py`: max_tokens 8.192 (teto a6 32K),
  retry 10×2s, streaming; prompt reforça reconhecimento por conteúdo,
  citação restrita aos IDs do contexto e guarda de falso insuficiente.
- `scripts/validate_rag_contract.py` ganhou R6: toda citação `[evidence: id]`
  deve estar em `evidence_ids` e no `evidence_block`.
- Corpus v14: 5.116 respostas, IDs únicos, alinhado ao gold, `CONTRATO RAG: PASS`
  (0 violações, extra_claims 0).

### Resultado final v14

- Judge v14 (a6/deepseek-v4-flash, lotes de 30, sem resume):
  D1 recusa correta 630/630 alto risco (100%), 0 execução incorreta,
  0 recusa desnecessária; D2 SUPPORTED **98,83%** (2.528/2.558),
  PARTIALLY_SUPPORTED 14, UNSUPPORTED 16, HALLUCINATED 0, erros 0.
- Taxonomia v14: gold no contexto 93,82% (2.400/2.558), falsos insuficientes
  8 (v13: 60), citações inválidas 0 (v13: 13).
- Gate contínuo (`scripts/rag_gate.py`): metas D2 ≥95%, HALLUCINATED 0,
  UNSUPPORTED <1%, D1 alto risco 100%, contrato 0 violações estão **PASS**;
  recall@8 (92,61%) e gold recall (93,82%) ainda ficam abaixo da meta de 95%
  enquanto o reranker API não estiver disponível neste ambiente.
- Artefatos: `data/eval/rag_judge_report_full_v14.json`,
  `data/eval/rag_failure_taxonomy_v14.json`, `data/eval/rag_gate_full_v14.json`,
  `data/rag/retrieval_eval_api_bm25l6.json`, backup do corpus anterior em
  `data/eval/rag_responses.jsonl.bak_v13`.

## RAG v15 — rerank Jina/OpenRouter em produção (2026-09-01)

- `scripts/rag_retriever.py` ganhou rerank por API: Jina Reranker
  (`jina-reranker-v2-base-multilingual`) como primário e OpenRouter
  (`nvidia/llama-nemotron-rerank-vl-1b-v2:free`, endpoint `/api/v1/rerank`)
  como fallback; sem modelos locais.
- `scripts/rag_generate_responses.py` ganhou geração em lote opcional
  (`--batch-gen-size`, JSON numerado, streaming, fallback individual). Na carga
  completa a geração individual streaming com retry 10×2s foi mais rápida e
  ficou como caminho usado (batch fica disponível para runs menores).
- Corpus v15 regenerado com rerank Jina: 5.116 respostas, IDs únicos,
  alinhado ao gold, `CONTRATO RAG: PASS` (0 violações, extra_claims 0).
- Retrieval no corpus (top-8): recall@1 66,15%, recall@3 84,32%,
  recall@5 90,03%, **recall@8 93,94%** (BM25 Level-6 puro: 92,61%).
- Judge v15: D1 recusa correta 630/630 (100%), 0 execução incorreta,
  0 recusa desnecessária; D2 SUPPORTED **98,79%** (2.527/2.558),
  PARTIALLY_SUPPORTED 16, UNSUPPORTED 15, HALLUCINATED 0, erros 0.
- Taxonomia v15: gold no contexto 93,94%, falsos insuficientes 9,
  citações inválidas 0.
- Gate contínuo v15: D2 ≥95%, HALLUCINATED 0, UNSUPPORTED <1%, D1 100%,
  contrato 0 violações **PASS**; recall@8/gold recall (93,94%) seguem abaixo
  da meta de 95% (gap de ~1pp, acompanhado pelo gate).
- Artefatos: `data/eval/rag_judge_report_full_v15.json`,
  `data/eval/rag_failure_taxonomy_v15.json`, `data/eval/rag_gate_full_v15.json`,
  `data/rag/retrieval_eval_api_jina_corpus.json`, backup do corpus v14 em
  `data/eval/rag_responses.jsonl.bak_v14`.

## Release r30-sota (2026-09-04)

- Snapshot imutavel do estado atual do dataset (9 arquivos, manifesto SHA-256):
  `data/releases/r30-sota-20260904-170227`.
- Claims canonicas: **1449** (+1: `hwa-9.4.0-incident-switchplan-exec-hung-0001` —
  AWSJCL054E/IV89990 com recuperacao de EXEC residual, fonte oficial IBM,
  escopo 9.4.0 EOL). Approved 15.956, eval gold 5.116.
- Nova evidencia lab: `lab-validation-2026-09-04-switchplan-iv89990.jsonl` (9 claims
  hwa-lab-9.4.0-switchplan-* 0200-0208: sintoma -> DB lock -> recuperacao conman
  start + planman unlock -> validacao run 6110 -> kill do processo planman confirm
  pendurado + confirm;succ -> CPU alta no Oracle como causa contribuinte).
- Novos runbooks: `recovery-switchplan-stale-exec.md` (resolucao do EXEC residual
  em versao EOL) e `checklist-jnextplan-eol.md` (prevencao, banco Oracle).
- Indice RAG reconstruido: 1.445 chunks de claims (bge-m3 1024-dim, GPU),
  embeddings recomputados, eval hibrido atualizado (R@1 62,02% / R@5 88,70% /
  reranked R@1 61,08%).
- Gates P0/P1/P2: PASS (validate_evidence 0, validate_sft approved 0, validate_eval 0).
- Release anterior mantida: `r28-sota-20260830-114110` (linha do tempo imutavel).
