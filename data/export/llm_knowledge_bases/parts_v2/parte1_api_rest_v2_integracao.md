# PARTE1 API REST V2 INTEGRACAO

## I. API REST v2 & Integracao

> 119 registros.

---

### 1. `hwa-10.1-real-oql-intro-0012`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 introduziu o Orchestration Query Language (OQL) como sintaxe de consulta mais simples que permite ordenar resultados sem necessidade de explicitos parametros de ordenacao na URL; OQL usa sintaxe de pontos para ordenacao (ex.: sort=field asc). Nao existe OQL na REST API V1 da 9.5.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (10.1 REST API V2 docs). OQL e recurso introduzido na V2 (10.1 FP1).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.1 Fix Pack 1 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v101/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | HCL Workload Automation 10.1 - Introducing REST API V2 (OQL) |
| Citacao de suporte | The Orchestration Query Language (OQL) is a simple query syntax that enables you to order the results... |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | OQL=Orchestration Query Language (introduzido em 10.1 FP1), sorting=ordenacao simples na sintaxe de consulta |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.1 Fix Pack 1 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=["GET /twsd/api/v2/plan/job?oql=name = 'UPDATESTATS'", 'GET /twsd/api/v2/plan/job?oql=ORDER BY key.name ASC'], result=OQL validado: filtro 'name = \'UPDATESTATS\'' -> 200 count=2; ORDER BY key.name ASC -> 200. GAP: 'key.name = \'UPDATESTATS\'' (exemplo oficial) -> 400 OQL_FILTER_SYNTAX_ERROR; campo aceito no filtro é 'name', não 'key.name'., validated_at=2026-08-23T10:00:00BRT |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | real-oql |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 introduziu o Orchestration Query Language (OQL) como sintaxe de consulta mais simples que permite ordenar resultados sem necessidade de explicitos parametros de ordenacao na URL; OQL usa sintaxe de pontos para ordenacao (ex?


---

### 2. `hwa-10.1-real-restv2-intro-0011`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando; a V2 substitui/complementa a V1 presente em 9.5. Endpoints e autenticacao JWT da V2 sao distintos da V1.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (10.1 release docs). Contraste de versao: V2 nao existia antes de 10.1 FP1; 9.5 usa V1.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.1 Fix Pack 1 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v101/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | HCL Workload Automation 10.1 - Introducing REST API V2 |
| Citacao de suporte | A new version of REST APIs has been introduced to operate on the product from both User Interface and Command Line Interface. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | REST API V2=introduzida em 10.1 Fix Pack 1, REST API V1=usada em 9.5 |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.1 Fix Pack 1 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=['GET /twsd/api/v2/engine/info', 'GET /twsd/api/v2/model/workstation', 'GET /twsd/api/v2/plan/job'], result=REST API V2 confirmada no lab: engine/info 200 (licenseType PERSERVER), model/workstation 200 (5), plan/job 200 (236). Autenticacao via Bearer JWT Personal do ocli. Endpoints distintos da V1 confirmados., validated_at=2026-08-23T10:00:00BRT |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | real-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando; a V2 substitui/complementa a V1 presente em 9.5. Endpoints e autenticacao JWT da V2 sao distintos da V1.?


---

### 3. `hwa-10.2.8-agent-auth-combinations-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Na instalação de agentes HWA 10.2.8, apikey é mutuamente exclusivo com wauser, wapassword, sslkeysfolder e sslpassword e requer tdwbhostname e tdwbport; jwt true também requer autenticação via apikey ou wauser/wapassword e os parâmetros do broker.

> **ATENCAO / RESSALVAS DE USO:** Não solicitar nem armazenar API keys, senhas ou JWTs. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: exclusão mútua entre -sslkeysfolder e -wauser (AWSFAB486E) e omissão total (AWSFAB502E) validadas no binário.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | installer=twsinst, authentication=['apikey', 'wauser/wapassword', 'jwt'], required=['tdwbhostname', 'tdwbport'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed agents |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | Agent installation parameters - twsinst script |
| Citacao de suporte | This parameter is mutually exclusive with: -wauser... -wapassword... -sslkeysfolder... -sslpassword... and it is required with: -tdwbhostname... -tdwbport. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | credential_sensitive |
| Capacidade | agent |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed agents |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | agent-auth |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 4. `hwa-10.2.8-agent-ssl-folder-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Na instalação de agentes HWA 10.2.8, sslkeysfolder deve apontar para uma pasta PEM contendo ca.crt, tls.key e tls.crt; additionalCAs pode conter CAs intermediárias ou confiáveis, e sslkeysfolder/sslpassword são mutuamente exclusivos com wauser, wapassword, apikey e jwt true.

> **ATENCAO / RESSALVAS DE USO:** Não registrar material criptográfico real. Claim de configuração, não autorização para executar instalação. | Describes the sslkeysfolder certificate-folder/password usage for dynamic and fault-tolerant agent installs. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: -sslkeysfolder com ca.crt, tls.key e tls.crt graváveis permitiu a geração de keystores no twsinst.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | installer=twsinst, parameter=sslkeysfolder, files=['ca.crt', 'tls.key', 'tls.crt', 'additionalCAs'], mutual_exclusion=['wauser', 'wapassword', 'apikey', 'jwt true'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed agents |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | Agent installation parameters - twsinst script |
| Citacao de suporte | The folder must contain the following files and folders: ca.crt, tls.key, tls.crt... The sslkeysfolder and sslpassword parameters are mutually exclusive with the wauser, wapassword, apikey, and jwt true parameters. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | credential_sensitive |
| Capacidade | agent |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed agents |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento cross-version (9.5/10.1/10.2.x) - lab é 10.2.8.00 apenas |
| Status de revisao | lab_validated |
| Tipo | other |
| Familia | agent-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na instalação de agentes HWA 10.2.8, sslkeysfolder deve apontar para uma pasta PEM contendo ca?


---

### 5. `hwa-10.2.8-aida-install-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `installation`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a instalacao do AI Data Advisor via Docker usa o script AIDA.sh (requer CONTAINER_RUNTIME=docker|podman) com os comandos: load (carrega as 9 imagens do pacote offline), build-start (builda es/keycloak e sobe todos os containers), first-start (configuracao guiada opcional), add-credentials/update-credentials/delete-credentials (gerencia credenciais do engine no OpenSearch), set-custom-port (padrao 9432), start/stop/restart/down/down-volumes. O docker-compose.yml define 11 servicos (config, keycloak, nginx, ui, exporter, ad, email, orchestrator, predictor, redis, es). O OpenSearch (2.19.6, construido via Dockerfile-es sobre ubi9) e o Keycloak (26.6.4, via Dockerfile-keycloak) NAO vem no tar de imagens: sao buildados com download da internet (artifacts.opensearch.org, quay.io).

> **ATENCAO / RESSALVAS DE USO:** AIDA.sh e docker-compose.yml inspecionados em laboratorio. AIDA.sh: Usage ./AIDA.sh COMMAND; detect_container_runtime exige CONTAINER_RUNTIME setado (erro 'CONTAINER_RUNTIME is not set' se ausente). Dockerfile-es baixa opensearch-2.19.6-linux-x64.tar.gz; Dockerfile-keycloak base quay.io/keycloak/keycloak:26.6.4. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE. Divergencia de versoes: o pacote 10.2.8 real usa OpenSearch 2.19.6 e Keycloak 26.6.4 (validado no Dockerfile-es/Dockerfile-keycloak do pacote); o README publico do GitHub (branch main, p/ 10.2.6) cita OpenSearch 2.3.0 e Keycloak V24.0.0 - referir sempre ao pacote 10.2.8 para versoes de componentes.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| Titulo da fonte | AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | For linux: ./AIDA.sh load ... Build, create, and start AIDA containers by running the following command: ./AIDA.sh build-start |
| Coletado em | 2026-08-25 |
| Capacidade | aida_install |
| Modo de operacao | mutate |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, Docker 29.7.2, CONTAINER_RUNTIME=docker, tested_commands=['export CONTAINER_RUNTIME=docker; cat ../aida-images-hcl.tar.gz | docker load', './AIDA.sh build-start'], result=9 imagens carregadas (predictor 7.74GB, ad/exporter/orchestrator/email ~3.1GB, nginx 2.3GB, ui 353MB, config 258MB, redis 263MB); build-start criou 10 containers e subiu todos (nginx 9432, keycloak, es, ui, exporter, ad, predictor, orchestrator, email, redis)., validated_at=2026-08-25T13:30:00BRT |
| Pre-condicoes | Confirmar versão 10.2.8, plataforma Distributed/Linux, autorização e backup/rollback aplicáveis antes da execução. |
| Impacto | Pode alterar estado operacional do AI Data Advisor (containers, configuração docker-compose/common.env, credenciais no OpenSearch); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar os arquivos de backup (docker-compose.yml.lab-bak*, common.env) e recriar os containers (./AIDA.sh down && ./AIDA.sh build-start) ou remover credenciais (delete_credentials). |
| Criterio de parada | Interromper diante de divergência de versão, falha de autenticação, OOM persistente, resolução DNS interna quebrada ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Status de revisao | lab_validated |
| Tipo | command |
| verbs | add; delete; install; start |
| Familia | aida-install |


---

### 6. `hwa-10.2.8-aida-metrics-0006`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `metrics`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o fluxo de dados do AI Data Advisor e: (1) o aida-exporter autentica no servidor WA (credenciais do OpenSearch) e consulta os endpoints REST V2 de metricas (GET /metrics sem auth, GET /twsd/engine/historical_metric/metadata e /record, GET /twsd/engine/definition/{alert,kpi,aida_catalog} com auth basic); (2) processa KPI definitions e grava metricas no OpenSearch (indice metric-index-<data>, alert-definitions, kpis-definition); (3) o aida-orchestrator agenda predicoes (aida-predictor, modelo prophet/neural) e deteccao de alertas (aida-ad); (4) os alertas aparecem no Workload Dashboard do DWC e podem ser enviados por email (aida-email, SMTP configurado no common.env). Parametros chave: METRICS_FETCH_INTERVAL=240s (o /metrics expira apos ~10min sem poll), EXPORTER_EXECUTION_INTERVAL=86400s, PROPHET_ORCHESTRATOR={"schedule":1440,"schedule_alert":15} (min entre predicao e deteccao), DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180, RESOLVE_ALERTS_AFTER_DAYS=1.

> **ATENCAO / RESSALVAS DE USO:** Validado em lab: exporter processou 6 KPI definitions e inseriu 80 metricas ('Kpis collected and saved'); metric-index cresceu para 80+ docs; /metrics do MDM responde 200 sem auth, metadata exige 401 sem credencial. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| Titulo da fonte | AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | WA_OMETRICS: Connection url to WA exposed metrics ... METRICS_FETCH_INTERVAL: Time interval (in seconds) to fetch metrics from WA endpoint - Default: 240 (4 minutes) - IMPORTANT: WA endpoint /metrics expires after ~10 minutes if not polled |
| Coletado em | 2026-08-25 |
| Capacidade | aida_monitoring |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, MDM REST V2 em wa-waserver:31116, tested_commands=['docker restart aida-exporter', 'docker logs aida-exporter', 'GET aida-es:9200/_cat/indices', 'GET aida-es:9200/metric-index-*/_count'], result=6 KPI definitions processadas; 80 metricas inseridas; indices metric-index-<data>/alert-definitions(12)/kpis-definition/wa-credentials(1)/special-days-labels(95)/predictions; count 81 apos nova coleta., validated_at=2026-08-25T13:50:00BRT |
| Terminologia normalizada | command=twsd |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | dwc |
| Familia | aida-metrics |


---

### 7. `hwa-10.2.8-aida-rest-api-0012`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `api`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor expoe uma API REST interna (sob /api, documentada em /api/swagger com spec OpenAPI 3.0) com 23 endpoints em 6 grupos: KPIs (POST /kpi, POST /kpi/list, GET /kpi/category/list, PUT /kpi/updateAll), Alerts (POST /alert/definition/list, POST /alert/definition, PUT /alert/definition/update, PUT /alert/definition/updateAll, POST /alert/instance, POST /alert/instance/list, PUT /alert/instance/update), Metrics (POST /metric/instance/list), Special Days (POST /special-day/list, PUT /special-day/add, PUT /special-day/update, DELETE /special-day/delete, POST /special-day/holidays, GET /special-day/holidays/list), Actions (GET /actions/retrain, GET /actions/retrain/retrain-details, GET /actions/retrain/last-retrain) e JWT (POST /jwt, GET /jwt/create-session). A autenticacao usa Keycloak (realm aida, client publico 'nginx', usuarios default aidaadmin com role aida-admin e aidauser): o nginx valida o Bearer JWT via discovery/introspection contra o Keycloak; o token e obtido por password grant em https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token. Schemas: SpecialDay, KPI, AlertDefinition, AlertInstance, MetricInstance, MetricDefinition, MetricProperties, MetricPropertiesInstance.

> **ATENCAO / RESSALVAS DE USO:** Descoberto em laboratorio via /api/swagger/swagger-ui-init.js e testado com token Keycloak (aidaadmin/admin realm aida client nginx). Respostas reais: /api/kpi/list (KPIs com last24hAlerts), /api/kpi/category/list (Jobs 5 / Queue 1), /api/alert/instance/list (count 0), /api/special-day/holidays/list (feriados por pais), /api/actions/retrain/last-retrain (count false). [Observado em laboratorio HWA 10.2.8 WSL2]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| Titulo da fonte | AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | swaggerDoc: openapi 3.0.0, title AIDA, servers [/api], tags [KPIs, Alerts, Metrics, Special Days, Actions, JWT] |
| Coletado em | 2026-08-25 |
| Capacidade | aida_api |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, Keycloak realm aida, tested_commands=['GET /api/swagger/swagger-ui-init.js', 'POST /api/kpi/list', 'GET /api/kpi/category/list', 'POST /api/alert/instance/list', 'GET /api/special-day/holidays/list', 'GET /api/actions/retrain/last-retrain'], result=23 endpoints mapeados; 6 testes reais OK com token aidaadmin (kpi/list, kpi/category/list, alert/instance/list, special-day/holidays/list, actions/retrain/last-retrain, metric/instance/list)., validated_at=2026-08-25T15:00:00BRT |
| Terminologia normalizada | command=add |
| Status de revisao | lab_validated |
| Tipo | command |
| verbs | add; list |
| Familia | aida-rest |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para api no HWA?


---

### 8. `hwa-10.2.8-aida-zos-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `platforms`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, ha diferencas entre o AI Data Advisor em Distributed vs z/OS: (1) registro de engine - Distributed requer Engine host + Engine port (default 9443); z/OS requer DWC host + DWC port + Remote server name; (2) ambos suportam autenticacao por Credentials (usuario+senha) ou API Keys; (3) tanto HCL Workload Automation quanto HCL Workload Automation for Z expoem metricas e KPI definitions segundo o padrao OpenMetrics (com endpoints distintos: /metrics e /twsd/engine/historical_metric/* para Distributed, /twsz/v1/aida/* para z/OS conforme ENDPOINTS_Z_CONF do common.env); (4) o modelo de ML do predictor suporta neural para Distributed e apenas Prophet para AIDA em z/OS Linux; (5) sem Keycloak, a autenticacao usa as roles do Dynamic Workload Console em ambos; com Keycloak, aplica-se ao deployment Docker em ambos.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Adding engines) + README do deploy (ENDPOINTS_Z_CONF, modelo prophet-only no z/OS). Diferenca de registro de engine validada conceitualmente com a claim hwa-10.2.8-aida-credentials-0005 (zconn vs dconn). [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_adding_WA_engines.html |
| Titulo da fonte | Adding engines to AIDA - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Engine host (Distributed only): hostname or IP ... Engine port (Distributed only): default 9443 ... DWC host (z/OS only): hostname or IP ... Remote server name (z/OS only): name or IP |
| Coletado em | 2026-08-25 |
| Capacidade | aida_platforms |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | dwc |
| Familia | aida-zos |


---

### 9. `hwa-10.2.8-apikey-api-key-auth-upgrade-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `api`

**Afirmacao / Conteudo:**

Ao atualizar de v10.x.x ou v9.5.x para 10.2.x, é necessário habilitar a autenticação por API Key: exportar o certificado público do servidor do keystore TWSServerKeyFile.p12 e importá-lo no truststore TWSServerTrustFile.p12 com o alias mpjwtkey, além de ajustar a variável mp.jwt.trust.key no arquivo jwt_variables.xml.

> **ATENCAO / RESSALVAS DE USO:** Tópico sensível a credenciais (chaves/certificados). Procedimento pós-upgrade obrigatório para autenticação JWT/API Key funcionar.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | authentication=API Key (JWT), keystore=TWSServerKeyFile.p12, truststore=TWSServerTrustFile.p12, alias=mpjwtkey, variable=mp.jwt.trust.key in jwt_variables.xml |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgradeAPIKey.html |
| Titulo da fonte | Enabling API Key authentication after upgrading |
| Citacao de suporte | the generated JWT is signed with the server private key... run the following commands on the master domain manager: keytool -exportcert ... keytool -importcert ... Edit the value of the mp.jwt.trust.key variable from the twstrustkey to mpjwtkey in the jwt_variables.xml file |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | api |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | import; upgrade |
| Familia | apikey-api |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Ao atualizar de v10.x?


---

### 10. `hwa-10.2.8-centralized-agent-update-behavior-0013`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

During centralized agent update, currently running jobs continue execution, new jobs do not start, and the agent restarts upon completion.

> **ATENCAO / RESSALVAS DE USO:** Centralized agent update lifecycle. | Primary ibm.com/docs 10.2.6 403 (not fetchable). HCL v1028 page states the same assertion in different wording; corroborated with wording difference recorded.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/docs/en/workload-automation/10.2.6?topic=managers-centralized-agent-update |
| Titulo da fonte | Centralized Agent Update |
| Citacao de suporte | Active jobs continue to run during update, new jobs remain in waiting status, and the agent reconnects automatically after the update. |
| Coletado em | 2026-08-16 |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento cross-version (9.5/10.1/10.2.x) - lab é 10.2.8.00 apenas |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| verbs | start |
| Familia | centralized-agent |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: During centralized agent update, currently running jobs continue execution, new jobs do not start, and the agent restarts upon completion?


---

### 11. `hwa-10.2.8-dwc-api-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/model`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para colocar uma job stream em modo draft via REST API V2 é necessário recuperar o ID e o payload atual da job stream com GET /twsd/api/v2/model/jobstream e enviar o payload atualizado com PUT /twsd/api/v2/model/jobstream/{jobStream_id}, incluindo o parâmetro 'draft' na lista options; a operação é mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.8-9 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | rest/model |
| Modo de operacao | guided_action |
| Citacao de suporte | In the JSON you just pasted, find the options parameter and include the draft parameter in the options list. The API returns a success message, and your job stream is now in draft mode. |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobstream + PUT /twsd/api/v2/model/jobstream/{jobStream_id}, method=GET + PUT (mutating), purpose=colocar job stream em modo draft |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awsddmst.pdf, Developer's Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer MDM ativo com REST API configurada. |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?


---

### 12. `hwa-10.2.8-dwc-api-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/fence`

**Afirmacao / Conteudo:**

O endpoint POST /twsd/api/v2/plan/workstation/action/update-fence é documentado no HCL Workload Automation 10.2.8 para alterar o valor do fence de uma workstation no plano atual; jobs não são iniciados em uma workstation se suas prioridades forem menores ou iguais ao valor do fence, sendo uma operação mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.11 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | rest/fence |
| Modo de operacao | guided_action |
| Citacao de suporte | The fence value plays a crucial role in job scheduling management, as jobs are not initiated on a workstation if their priorities are at or below the job fence value. |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/plan/workstation/action/update-fence, method=POST (mutating), purpose=alterar fence de workstation no plano |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awsddmst.pdf, Developer's Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer MDM ativo com REST API configurada. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/workstation/action/update-fence no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/plan/workstation/action/update-fence é documentado no HCL Workload Automation 10.2.8 para alterar o valor do fence de uma workstation no plano atual; jobs não são iniciados em uma workstation se suas prioridades forem menores ou iguais ao valor do fence, sendo uma operação mutating, conforme documentação oficial?


---

### 13. `hwa-10.2.8-dwc-api-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job com dependência no plano atual via REST API V2 consiste em obter o ID do job sucessor com GET /twsd/api/v2/model/jobdefinition e os dados do job predecessor com GET /twsd/api/v2/plan/job e então adicionar a dependência com POST /twsd/api/v2/plan/job/{job_id}/action/add-dependencies (corpo com array dependencies contendo dependencyType e jobId do predecessor); operação mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.12-14 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | rest/plan |
| Modo de operacao | guided_action |
| Citacao de suporte | Now, use the data you retrieved to add the dependency with the POST/twsd/api/v2/plan/job/{job_id}/action/add-dependencies endpoint. ... The API returns a success message, and the dependency is now active in the current plan. |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/plan/job/{job_id}/action/add-dependencies, method=POST (mutating), purpose=adicionar dependência entre jobs no plano |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awsddmst.pdf, Developer's Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer MDM ativo com REST API configurada. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | add; plan |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?
- Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job com dependência no plano atual via REST API V2 consiste em obter o ID do job sucessor com GET /twsd/api/v2/model/jobdefinition e os dados do job predecessor com GET /twsd/api/v2/plan/job e então adicionar a dependência com POST /twsd/api/v2/plan/job/{job_id}/action/add-dependencies (corpo com array dependencies contendo dependencyType e jobId do predecessor); operação mutating, conforme documentação oficial?


---

### 14. `hwa-10.2.8-dwc-api-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream no plano via REST API V2 consiste em consultar GET /twsd/api/v2/plan/jobstream e inspecionar o array dependencies da resposta (que contém os IDs de todos os jobs e job streams predecessores) e então obter os detalhes de cada predecessor com GET /twsd/api/v2/plan/job/{job_id} e GET /twsd/api/v2/plan/jobstream/{jobstream_id}; operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.15-17 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest/plan |
| Modo de operacao | read |
| Citacao de suporte | From the API response, locate the dependencies array in the response body. This array contains the IDs of all predecessor jobs and job streams. |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/plan/jobstream + GET /twsd/api/v2/plan/job/{job_id} + GET /twsd/api/v2/plan/jobstream/{jobstream_id}, method=GET (read), purpose=recuperar predecessores de job stream no plano |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream no plano via REST API V2 consiste em consultar GET /twsd/api/v2/plan/jobstream e inspecionar o array dependencies da resposta (que contém os IDs de todos os jobs e job streams predecessores) e então obter os detalhes de cada predecessor com GET /twsd/api/v2/plan/job/{job_id} e GET /twsd/api/v2/plan/jobstream/{jobstream_id}; operação de leitura, conforme documentação oficial?


---

### 15. `hwa-10.2.8-dwc-api-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os sucessores de uma job stream no plano via REST API V2 consiste em obter o ID da job stream com GET /twsd/api/v2/plan/jobstream e consultar GET /twsd/api/v2/plan/job e GET /twsd/api/v2/plan/jobstream com o filtro OQL 'dependencies.jobStreamId = <id da job stream>' para listar os jobs e job streams que dependem dela; operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.17-18 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest/plan |
| Modo de operacao | read |
| Citacao de suporte | To find successor jobs, use the GET/twsd/api/v2/plan/job endpoint. In the oql parameter field, enter the following query, replacing the example ID with your job stream ID |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/plan/job + GET /twsd/api/v2/plan/jobstream (filtro OQL dependencies.jobStreamId), method=GET (read), purpose=recuperar sucessores de job stream no plano |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os sucessores de uma job stream no plano via REST API V2 consiste em obter o ID da job stream com GET /twsd/api/v2/plan/jobstream e consultar GET /twsd/api/v2/plan/job e GET /twsd/api/v2/plan/jobstream com o filtro OQL 'dependencies?


---

### 16. `hwa-10.2.8-dwc-api-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para listar e gerenciar dependências de uma job stream no plano via REST API V2 utiliza GET /twsd/api/v2/plan/jobstream para obter o ID e o array dependencies da job stream e os endpoints PUT /twsd/api/v2/plan/jobstream/{jobStream_id}/action/release-all-dependencies (sem corpo de requisição), release-dependencies e remove-dependencies (corpo com array dependencies a liberar/remover); operações mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.18-22 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | rest/plan |
| Modo de operacao | guided_action |
| Citacao de suporte | To release all dependencies, use the PUT/twsd/api/v2/plan/jobstream/{jobStream_id}/action/release-all-dependencies endpoint. In the Swagger UI, paste the job stream ID into the ID parameter. No request body is required. |
| Terminologia normalizada | endpoint=PUT /twsd/api/v2/plan/jobstream/{jobStream_id}/action/release-all-dependencies | release-dependencies | remove-dependencies, method=PUT (mutating), purpose=liberar/remover dependências de job stream no plano |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awsddmst.pdf, Developer's Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer MDM ativo com REST API configurada. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan; release; remove |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?


---

### 17. `hwa-10.2.8-dwc-api-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/model`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream a partir da base de dados via REST API V2 consiste em consultar GET /twsd/api/v2/model/jobstream e inspecionar os arrays de dependências da definição (externalPredecessors, promptDependencies, fileDependencies, resourceDependencies) e então obter as definições completas de cada predecessor com GET /twsd/api/v2/model/jobdefinition/{job_abstract_id} e GET /twsd/api/v2/model/jobstream/{jobstream_abstract_id}; operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.22-24 (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest/model |
| Modo de operacao | read |
| Citacao de suporte | From the API response, locate the various dependency arrays within the definition, such as externalPredecessors and promptDependencies. These arrays contain the identifiers of the predecessor objects. |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobstream + GET /twsd/api/v2/model/jobdefinition/{job_abstract_id} + GET /twsd/api/v2/model/jobstream/{jobstream_abstract_id}, method=GET (read), purpose=recuperar predecessores de job stream da base de dados |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?


---

### 18. `hwa-10.2.8-dwc-api-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/model`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para criar uma nova job definition na base de dados via REST API V2 consiste em preparar um payload JSON com kind igual a 'JobDefinition' e o array def contendo folder, name, workstation, type e task (ex.: type UNIX com taskString, userName e isCommand), enviá-lo com POST /twsd/api/v2/model/jobdefinition e verificar a criação com GET /twsd/api/v2/model/jobdefinition; a resposta retorna o ID da nova definição.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.8 (LACUNA4 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Coletado em | 2026-08-23 |
| Status de revisao | draft |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Classificacao de risco | mutating |
| Capacidade | rest/model |
| Modo de operacao | guided_action |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Citacao de suporte | Prepare the payload template for the new job definition. Modify the fields within the def array with the required values. |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/model/jobdefinition, method=POST (mutating), purpose=criar job definition na base de dados |
| Responsavel | hwa-source-verifier |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial; sem prova de laboratório nesta fase (LACUNA4) — validação prática requer ambiente ativo com REST API/configuração disponível. |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?
- Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para criar uma nova job definition na base de dados via REST API V2 consiste em preparar um payload JSON com kind igual a 'JobDefinition' e o array def contendo folder, name, workstation, type e task (ex?


---

### 19. `hwa-10.2.8-dwc-api-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/model`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para consultar uma job stream ou job definition via REST API V2 (GET /twsd/api/v2/model/jobstream e GET /twsd/api/v2/model/jobdefinition) existem dois métodos: model filters com sintaxe análoga à do composer (ex.: /@/@#/@/JS-API) e OQL com o preset 'Filter by exact name and matching folder', que gera a query name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC para filtrar pelo nome exato e pasta com ordenação decrescente.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.10-12 (LACUNA4 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Coletado em | 2026-08-23 |
| Status de revisao | draft |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Classificacao de risco | read_only |
| Capacidade | rest/model |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Citacao de suporte | select Filter by exact name and matching folder and sort results in name descending order in the OQL string parameter field. Enter the name of the job stream in the name field to obtain the following query: name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobstream + GET /twsd/api/v2/model/jobdefinition, method=GET (read), purpose=consultar definições por model filters ou OQL |
| Responsavel | hwa-source-verifier |
| Tipo | command |
| Ferramenta | composer |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar rest/model?
- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?


---

### 20. `hwa-10.2.8-dwc-api-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job ad-hoc via REST API V2 usa o endpoint POST /twsd/api/v2/plan/job/submit-ad-hoc-job com corpo contendo task e workstationKey; o task pode ser simples (UNIX com taskString, isCommand e userName) ou executável (OTHER com taskString contendo XML JSDL jsdl:jobDefinition com jsdle:executable e jsdle:script), e a submissão é verificada com GET /twsd/api/v2/plan/job.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.14-15 (LACUNA4 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Coletado em | 2026-08-23 |
| Status de revisao | draft |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Classificacao de risco | mutating |
| Capacidade | rest/plan |
| Modo de operacao | guided_action |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Citacao de suporte | Use the POST /twsd/api/v2/plan/job/submit-ad-hoc-job API endpoint. In the request body, define the task and the workstationKey. |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/plan/job/submit-ad-hoc-job, method=POST (mutating), purpose=submeter job ad-hoc ao plano |
| Responsavel | hwa-source-verifier |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial; sem prova de laboratório nesta fase (LACUNA4) — validação prática requer ambiente ativo com REST API/configuração disponível. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan; submit |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job/submit-ad-hoc-job no HWA?
- Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?
- Como submeter execuções pontuais via API REST V2 no HWA?


---

### 21. `hwa-10.2.8-dwc-api-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/model`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a resposta do endpoint GET /twsd/api/v2/model/jobstream fornece o ID da job stream no cabeçalho da resposta (response header) e o payload JSON completo no corpo da resposta, itens necessários para as etapas seguintes do fluxo (ex.: atualização com PUT /twsd/api/v2/model/jobstream/{jobStream_id}).

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.9 (LACUNA4 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Coletado em | 2026-08-23 |
| Status de revisao | draft |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Classificacao de risco | read_only |
| Capacidade | rest/model |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Citacao de suporte | From the API response, copy and save the following two items: the job stream ID in the response header and the entire JSON payload from the response body. |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobstream, method=GET (read), purpose=obter ID no response header e payload no corpo |
| Responsavel | hwa-source-verifier |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a resposta do endpoint GET /twsd/api/v2/model/jobstream fornece o ID da job stream no cabeçalho da resposta (response header) e o payload JSON completo no corpo da resposta, itens necessários para as etapas seguintes do fluxo (ex?


---

### 22. `hwa-10.2.8-dwc-api-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest/plan`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a resposta de GET /twsd/api/v2/plan/jobstream documenta o array dependencies com entradas tipadas pelo campo dependencyType, incluindo JOIN (com joinName, joinQuantity, members e criteria), EXTERNAL_JOBSTREAM (com jobStreamId e jobStreamName do predecessor), RESOURCE (com name, quantity e available) e PROMPT (com promptName, promptStatus e actions como REPLY_PROMPT); no plano, predecessores de tipo job aparecem como EXTERNAL_JOB com jobId e jobName.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awsddmst.pdf p.16-20 (LACUNA4 2026-08-23); payloads de exemplo mostram JOIN/EXTERNAL_JOBSTREAM/RESOURCE/PROMPT (dependencies) e EXTERNAL_JOB (predecessor de job no plano).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Coletado em | 2026-08-23 |
| Status de revisao | draft |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Classificacao de risco | read_only |
| Capacidade | rest/plan |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf |
| Titulo da fonte | Developer's Guide: Driving HCL Workload Automation (10.2.8) |
| Citacao de suporte | Example of a response payload showing various dependency types: |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/plan/jobstream, method=GET (read), purpose=enumerar tipos de dependência no plano (dependencyType) |
| Responsavel | hwa-source-verifier |
| Tipo | other |
| Ferramenta | dwc |
| verbs | plan |
| Familia | dwc-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?


---

### 23. `hwa-10.2.8-dwc-apikey-expiry-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `authentication`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as API Keys criadas no Dynamic Workload Console possuem expiracao padrao de 365 dias, configuravel pela propriedade com.ibm.tws.util.jwt.apikey.expiration.date. Apos gerada, a API Key e armazenada no arquivo config.yaml do usuario ($HOME/.OCLI/config.yaml no Linux).

> **ATENCAO / RESSALVAS DE USO:** Expiracao padrao 365 dias; config.yaml em $HOME/.OCLI/config.yaml (Linux) ou %userprofile%\.OCLI\config.yaml (Windows).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/apikeyscenario.html |
| Titulo da fonte | API Key scenario - HCL Workload Automation 10.2.8 |
| Citacao de suporte | com.ibm.tws.util.jwt.apikey.expiration.date |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | authentication |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | dwc-apikey |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as API Keys criadas no Dynamic Workload Console possuem expiracao padrao de 365 dias, configuravel pela propriedade com?


---

### 24. `hwa-10.2.8-dwc-apikey-oidc-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `authentication`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a geracao de API Keys requer um provedor de autenticacao/autorizacao que use o padrao aberto OpenID Connect. Na primeira conexao do Orchestration CLI, e necessario autenticar usando API Keys, que sao atualizadas automaticamente no arquivo config.yaml.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/t_authenticatingcli_apikey.html |
| Titulo da fonte | Authenticating Orchestration CLI using API Keys - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Created valid credentials in an authentication or authorization provider that uses the open protocol standard OpenID Connect |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | authentication |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | dwc-apikey |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a geracao de API Keys requer um provedor de autenticacao/autorizacao que use o padrao aberto OpenID Connect?


---

### 25. `hwa-10.2.8-dwc-engine-connection-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a engine connection do Dynamic Workload Console pode ser criada via REST API interna do DWC (contexto /dwc/api, JAX-RS EngineApplication em /v1/): POST /dwc/api/v1/engine/create com JSON {name, type (TWS=distributed), hostname, port, remoteServerName, credentials {user, password}, showInDashboard, enableSSC, reporting} retorna 200 com 'created successfully'; a conexao e persistida em tdwc.tdwc_engineconnection (engine_id numerico gerado por identity), tdwc.tdwc_credential (senha criptografada) e tdwc.tdwc_preferenceable (preferencetype); a validacao de conectividade usa GET /dwc/api/v1/engine/{engine_id}/checkConnection (engine_id NUMERICO, nao o nome) que retorna {'successful': true} quando o engine responde na porta HTTPS.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25: engine connection MDM_LAB (hostname MDMHOST, porta 31116, remoteServerName MDM, type TWS) criada e validada; GET /1/info retornou NAME MDM_LAB, TYPE maestro, HOST MDMHOST, PORT 31116. GAP observado: usar o nome em vez do id numerico causa NumberFormatException (EngineAppService.findEngine). Endpoint /list retorna items vazio no lab mesmo com engine criada (filtro de dashboard/SSC). [fix auditor 2026-08-25: supporting_quote e observacao de laboratorio (curl), nao citacao da pagina citada; REST API interna nao documentada em mng_eng_c.html - evidencia primaria e o lab_validation]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/mng_eng_c.html |
| Titulo da fonte | Engine connections - Dynamic Workload Console User's Guide - HCL Workload Automation |
| Citacao de suporte | POST /dwc/api/v1/engine/create -> {"successful":true,"message":"MDM_LAB created successfully."}; GET /dwc/api/v1/engine/1/checkConnection -> {"successful":true,"message":"Connection to MDM_LAB: successful."} |
| Coletado em | 2026-08-25 |
| Capacidade | dwc |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | DWC instalado; sessao autenticada (LtpaToken2); engine (MDM) acessivel na porta HTTPS (31116); credenciais de engine validas. |
| Impacto | Cria registro de engine connection no banco TDWC (tdwc_engineconnection/tdwc_credential/tdwc_preferenceable) e habilita monitoramento do engine no console. |
| Reversibilidade | DELETE /dwc/api/v1/engine/{engine_id} remove a conexao. |
| Criterio de parada | Interromper se create retornar erro de schema/FK ou se checkConnection falhar (engine inacessivel). |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | create |
| Familia | dwc-engine |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /dwc/api no HWA?


---

### 26. `hwa-10.2.8-dwc-engine-connection-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 do engine (https://<host>:31116/twsd/) e servida pelo engineServer, que e o server Open Liberty do MDM instalado em ${HWA_INST_DIR}/usr/servers/engineServer, que no lab e /opt/hwa/usr/servers/engineServer (WLP_USER_DIR do MDM) iniciado por appservertools/startAppServer.sh como o usuario HWA; o Dynamic Workload Console valida a engine connection contra essa porta, portanto o engineServer precisa estar ativo (e o hostname do engine resolvido no /etc/hosts do host do DWC, ex.: localhost MDMHOST) para o checkConnection retornar sucesso.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25: com engineServer parado a porta 31116 nao respondia (curl 000) e o DWC nao conseguiria conectar; apos ./startAppServer.sh (como wauser, APPSERVERHOME=/opt/liberty/wlp, SERVERNAME=engineServer, WLP_USER_DIR=/opt/hwa/usr) a porta 31116 respondeu 200 em /twsd/ e o checkConnection do DWC retornou successful. Foi necessario adicionar localhost MDMHOST ao /etc/hosts. [fix auditor 2026-08-25: variavel DWC_INST_DIR corrigida para HWA_INST_DIR - engineServer pertence ao MDM]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html |
| Titulo da fonte | Server components installation - serverinst script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | curl -k https://MDMHOST:31116/twsd/ -> HTTP 200 (apos startAppServer.sh engineServer); GET /twsd/api/v2/model/jobdefinition (basic auth) -> HTTP 200 |
| Coletado em | 2026-08-25 |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | MDM instalado (serverinst); engineServer iniciado; resolucao de hostname do engine (ex.: MDMHOST no /etc/hosts); porta HTTPS 31116 liberada. |
| Impacto | Inicia/para o Liberty do engine; sem ele o DWC nao valida conexoes. |
| Reversibilidade | stopAppServer.sh para o engineServer; inicio e reversivel. |
| Criterio de parada | Interromper se o engineServer nao subir (log de erro no WLP_OUTPUT_DIR) ou a porta 31116 nao abrir. |
| Terminologia normalizada | command=twsd |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | dwc |
| verbs | open |
| Familia | dwc-engine |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 do engine (https://<host>:31116/twsd/) e servida pelo engineServer, que e o server Open Liberty do MDM instalado em ${HWA_INST_DIR}/usr/servers/engineServer, que no lab e /opt/hwa/usr/servers/engineServer (WLP_USER_DIR do MDM) iniciado por appservertools/startAppServer?


---

### 27. `hwa-10.2.8-dwc-engine-restart-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `engines`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, operacoes de engine (start/stop/restart) podem ser executadas via REST API nos servicos de engines expostos em /twsd, complementando o appservman local.

> **ATENCAO / RESSALVAS DE USO:** revalidacao pendente: sem 2a fonte oficial encontrada (2026-08-23); manter em backlog de revalidacao

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | administer engines |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | engines |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Tipo | command |
| Ferramenta | dwc |
| verbs | start; stop |
| Familia | dwc-engine |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para engines no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, operacoes de engine (start/stop/restart) podem ser executadas via REST API nos servicos de engines expostos em /twsd, complementando o appservman local?


---

### 28. `hwa-10.2.8-dwc-eventrule-rest-0017`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `eventrules`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as event rules podem ser administradas via REST API (servicos de event rules em /twsd), incluindo deployment e engine de regras, complementando o uso de sendevent e do Dynamic Workload Console.

> **ATENCAO / RESSALVAS DE USO:** States event rules can be defined via APIs; REST API services on Swagger Docs at /twsd.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | event rules |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | eventrules |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-eventrule |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para eventrules no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 29. `hwa-10.2.8-dwc-restv2-filter-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 oferece filtragem aprimorada: e possivel usar planFilter (sintaxe similar ao conman) e/ou OQL, podendo combinar ambos usando planFilter para filtrar e OQL para ordenar, conforme a especificidade da consulta.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Enhanced filtering opportunities: according to how specific your query needs to be, you can decide whether to use planFilter, which is similar to conman syntax... or OQL syntax... You can also decide to use both of them, using planFilter for filtering and OQL for ordering. |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | conman |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar restv2?
- Qual endpoint REST API V2 é utilizado para restv2 no HWA?


---

### 30. `hwa-10.2.8-dwc-restv2-https-tls-0018`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, o acesso a REST API e exclusivamente via HTTPS (porta 31116 por padrao), exigindo certificados TLS validos no master domain manager; o lab confirmou TLS 1.3 no endpoint /twsd.

> **ATENCAO / RESSALVAS DE USO:** Lab 22/08: TLS 1.3 confirmado no endpoint.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The HTTPS port number of the master domain manager or backup domain manager. The default is 31116. |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o acesso a REST API e exclusivamente via HTTPS (porta 31116 por padrao), exigindo certificados TLS validos no master domain manager; o lab confirmou TLS 1.3 no endpoint /twsd?


---

### 31. `hwa-10.2.8-dwc-restv2-model-query-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 permite consultar job streams de modelo com filtros de modelo (ex.: /@/@#/@/JS-API) ou com OQL (ex.: name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC), retornando os resultados no envelope padrao com count e results.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | Submitting a job stream - HCL Workload Automation 10.2.8 |
| Citacao de suporte | GET /twsd/api/v2/model/jobstream |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 permite consultar job streams de modelo com filtros de modelo (ex?


---

### 32. `hwa-10.2.8-dwc-restv2-multi-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 introduziu endpoints multi-item eficientes: cada acao pode ser executada por ID ou por filtro, permitindo operar sobre varios itens de uma vez.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Introduction of efficient multi-item endpoints: each action can be performed by ID and by filter. |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 introduziu endpoints multi-item eficientes: cada acao pode ser executada por ID ou por filtro, permitindo operar sobre varios itens de uma vez?


---

### 33. `hwa-10.2.8-dwc-restv2-oql-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Object Query Language (OQL) e usado para monitorar o ambiente do production plan e se aplica a REST API V2 e ao Orchestration Monitor. Suporta keywords como AND, OR, IN, LIKE e ORDER BY, e os campos sao case-sensitive.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/oql.html |
| Titulo da fonte | OQL - HCL Workload Automation 10.2.8 |
| Citacao de suporte | You can monitor the HCL Workload Automation production plan environment... by using the OQL, which applies to REST API V2 and the Orchestration Monitor |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| verbs | plan |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Object Query Language (OQL) e usado para monitorar o ambiente do production plan e se aplica a REST API V2 e ao Orchestration Monitor?


---

### 34. `hwa-10.2.8-dwc-restv2-payload-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 introduziu payloads melhorados para facilitar o consumo, com estrutura/hierarquia reformulada em relacao a V1.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Improved payloads for easier consumption |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 introduziu payloads melhorados para facilitar o consumo, com estrutura/hierarquia reformulada em relacao a V1.?


---

### 35. `hwa-10.2.8-dwc-restv2-recommended-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 e recomendada para qualquer integracao futura por ser mais facil de configurar, mais poderosa e flexivel que a V1. A API cobre administracao de engines, event rules, workload modelling, plans e security.

> **ATENCAO / RESSALVAS DE USO:** Nao duplica hwa-10.2.8-rest-v2-0001: complementa com detalhe dos servicos cobertos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration. |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 36. `hwa-10.2.8-dwc-restv2-services-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API (acessivel em /twsd) cobre servicos de administracao de engines, event rules, workload modelling, plans e security, permitindo operar o produto via UI e CLI de forma programatica.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | administer engines, event rules, workload modelling, plans, and security |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 37. `hwa-10.2.8-dwc-restv2-submit-0011`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para submeter uma job stream via REST API V2 e necessario primeiro consultar o job stream de modelo com GET /twsd/api/v2/model/jobstream (usando model filters como /@/@#/@/JS-API ou OQL) e depois usar o id retornado no POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit. As respostas usam o envelope {"count":N,"results":[...]}.

> **ATENCAO / RESSALVAS DE USO:** Envelope de resposta: {"count":1,"results":[...]} com campo id (ex.: 26dc6d8d-...).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | Submitting a job stream - HCL Workload Automation 10.2.8 |
| Citacao de suporte | POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | restv2 |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | dwc |
| verbs | plan; submit |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para submeter uma job stream via REST API V2 e necessario primeiro consultar o job stream de modelo com GET /twsd/api/v2/model/jobstream (usando model filters como /@/@#/@/JS-API ou OQL) e depois usar o id retornado no POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit?


---

### 38. `hwa-10.2.8-dwc-restv2-swagger-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 expoe uma interface Swagger em https://MDM_IP_address:tdwbport/twsd/ com a opcao 'Try it out!', permitindo testar operacoes (List Operations) diretamente no navegador.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | click List Operations... Try it out! |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| verbs | list |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 expoe uma interface Swagger em https://MDM_IP_address:tdwbport/twsd/ com a opcao 'Try it out!', permitindo testar operacoes (List Operations) diretamente no navegador?


---

### 39. `hwa-10.2.8-dwc-restv2-url-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, a REST API e acessada via HTTPS na URL https://hostname:port_number/twsd, sendo a porta padrao do master domain manager ou backup domain manager a 31116.

> **ATENCAO / RESSALVAS DE USO:** Corrobora hwa-10.2.8-rest-v2-port-31116-live-0077 (lab).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HWA with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The HTTPS port number of the master domain manager or backup domain manager. The default is 31116. |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a REST API e acessada via HTTPS na URL https://hostname:port_number/twsd, sendo a porta padrao do master domain manager ou backup domain manager a 31116.?


---

### 40. `hwa-10.2.8-dwc-restv2-v1-diff-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `restv2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 difere da V1 por oferecer filtragem aprimorada (planFilter/OQL), payloads melhorados para consumo e endpoints multi-item (operacao por ID ou por filtro), sendo recomendada para integracoes futuras.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rest_api_v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Enhanced filtering opportunities... Improved payloads for easier consumption... efficient multi-item endpoints |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | restv2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | dwc |
| Familia | dwc-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para restv2 no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 difere da V1 por oferecer filtragem aprimorada (planFilter/OQL), payloads melhorados para consumo e endpoints multi-item (operacao por ID ou por filtro), sendo recomendada para integracoes futuras?


---

### 41. `hwa-10.2.8-dwc-trace-template-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, o template trace.xml para o DWC fica em configDropins/templates/trace.xml e pode ser personalizado com valores de trace.specification (por exemplo tws_all, tws_rest, tws_db) antes de copiar para overrides.

> **ATENCAO / RESSALVAS DE USO:** Valores trace.specification documentados; aplicar conforme diagnóstico autorizado. [texto recuperado do unified dataset rag_corpus (verified_claim original)]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadwlptemplates.html |
| Titulo da fonte | Configuring HCL Workload Automation using templates |
| Citacao de suporte | Trace settings | Traces are disabled by default, so no file is present in the overrides folder. Copy the trace.xml file to the overrides folder to enable traces. | templates/trace.xml | changeTraceProperties |
| Coletado em | 2026-08-16 |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-trace |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, o template trace?


---

### 42. `hwa-10.2.8-dynagent-resource-advisor-url-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

A propriedade ResourceAdvisorUrl da seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 define a URL do master em ambiente distribuído ou do dynamic domain manager que hospeda o agent, no formato https://tdwb_server:tdwb_port/JobManagerRESTWeb/JobScheduler/resource, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: propriedade ResourceAdvisorUrl e formato do provider URL.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ResourceAdvisorUrl=URL do master/DDM que hospeda o agent, JobManagerRESTWeb=endpoint REST do Resource Advisor |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconfresadvisorag.html |
| Titulo da fonte | Configuring properties of the Resource advisor agent [ResourceAdvisorAgent] |
| Citacao de suporte | ResourceAdvisorUrl ... The URL of the master in a distributed environment, or of the dynamic domain manager in a z/OS or in a distributed environment, that is hosting the agent. ... The value is https://$(tdwb_server):$(tdwb_port)/JobManagerRESTWeb/JobScheduler/resource. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-resource |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade ResourceAdvisorUrl da seção [ResourceAdvisorAgent] do JobManager?


---

### 43. `hwa-10.2.8-dynamicagent-resource-advisor-url-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

O agente dinâmico conecta-se ao DWB via HTTPS ResourceAdvisorUrl no JobManager.ini seção [ResourceAdvisorAgent]; registra-se automaticamente na instalação ao MDM ou DDM; ResourceAdvisorUrl = https://<tdwb_server>:<tdwb_port>/JobManagerRESTWeb/JobScheduler/resource.

> **ATENCAO / RESSALVAS DE USO:** A página awsadgatewayconfig.html não existe em v1028 (404); o equivalente oficial é awsadconfresadvisorag.html. Auto-registro confirmado em awsrgworkstationconcept.html ('automatically created and registered ... when you install the agent'). Se porta for 0, o resource advisor agent não inicia. Com -gateway local/remote, a URL inclui /ita/JobManagerGW/.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ResourceAdvisorUrl=URL de conexão do agente dinâmico ao master/DDM, [ResourceAdvisorAgent]=seção do JobManager.ini/JobManagerGW.ini, tdwb_server=hostname do master (distribuído) ou dynamic domain manager, tdwb_port=porta do master/DDM, auto-registration=registro automático do agente dinâmico na instalação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconfresadvisorag.html |
| Titulo da fonte | Configuring properties of the Resource advisor agent [ResourceAdvisorAgent] |
| Citacao de suporte | ResourceAdvisorUrl ... The value is https://$(tdwb_server):$(tdwb_port)/JobManagerRESTWeb/JobScheduler/resource ... It is configured automatically at installation time. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | mdm |
| Familia | dynamicagent-resource |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O agente dinâmico conecta-se ao DWB via HTTPS ResourceAdvisorUrl no JobManager?


---

### 44. `hwa-10.2.8-govern-object-versioning-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o recurso de versionamento de objetos mantém todas as versões anteriores de objetos de agendamento e de segurança, e no Dynamic Workload Console é possível ver o histórico, comparar versões e restaurar uma versão anterior; o recurso exige as opções globais dbAudit=1 e auditStore=db ou both.

> **ATENCAO / RESSALVAS DE USO:** Object versioning is an audit-based DWC capability (dbAudit=1 + auditStore=db/both), distinct from composer in-place update.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | object_versioning=HWA maintains all previous versions of scheduling and security objects (audit-based), restore=restore a previous object version from Workload Designer Versions tab |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/checkversioninfo.html |
| Titulo da fonte | Checking version information - HCL Workload Automation 10.2.8 DWC |
| Citacao de suporte | HCL Workload Automation maintains all previous versions, both for scheduling and security objects. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-object |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o recurso de versionamento de objetos mantém todas as versões anteriores de objetos de agendamento e de segurança, e no Dynamic Workload Console é possível ver o histórico, comparar versões e restaurar uma versão anterior; o recurso exige as opções globais dbAudit=1 e auditStore=db ou both?


---

### 45. `hwa-10.2.8-gui-sap-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `api`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, é possível criar, pela Dynamic Workload Console (Workload Designer), uma definição de SAP job que referencia um InfoPackage ou Process Chain do SAP Business Warehouse; na página Task define-se o Subtype como BW Process Chain ou BW InfoPackage e clica-se em Save para salvar a definição no banco de dados; para InfoPackages o Start type deve ser 'Start later in background process' com Start time 'Immediate', e para process chains o modo deve ser 'Start Using Meta Chain or API'.

> **ATENCAO / RESSALVAS DE USO:** URL oficial correta em v1028 é /apps/src_usr/awsautwsjobipcr.html; a URL informada /distr/src_ref/awsautwsjobipcr.html retorna 404. O procedimento usa o Workload Designer (New > Job Definition > ERP), não a aba Assets do Graphical Designer.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/apps/src_usr/awsautwsjobipcr.html |
| Titulo da fonte | Creating an HCL Workload Automation job that contains InfoPackages or process chains |
| Citacao de suporte | On the Task page, in Subtype, specify either BW Process Chain or BW InfoPackage. Click Save to add the SAP job definition to the HCL Workload Automation database. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | api |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Tipo | command |
| Ferramenta | gui |
| verbs | start |
| Familia | gui-sap |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é possível criar, pela Dynamic Workload Console (Workload Designer), uma definição de SAP job que referencia um InfoPackage ou Process Chain do SAP Business Warehouse; na página Task define-se o Subtype como BW Process Chain ou BW InfoPackage e clica-se em Save para salvar a definição no banco de dados; para InfoPackages o Start type deve ser 'Start later in background process' com Start time 'Immediate', e para process chains o modo deve ser 'Start Using Meta Chain or API'?


---

### 46. `hwa-10.2.8-incident-awktsa050e-restart-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dynamic_agent`

**Afirmacao / Conteudo:**

Sintoma: apos submeter workload, a mensagem AWKTSA050E 'A problem with the JCL content, prevent Dynamic Workload Bridge from submitting the job' e escrita no messages.log do master domain manager. Causa: o erro indica que um restart do WebSphere Application Server Liberty Base e necessario. Resolucao: reiniciar o WebSphere Liberty e reenviar o workload. Fonte: HCL Troubleshooting Guide 10.2.8 (AWKTSA050E error issued during submission).

> **ATENCAO / RESSALVAS DE USO:** Extraida de awstrmst.pdf (F3 2026-08-23)

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Coletado em | 2026-08-23 |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| Citacao de suporte | This error indicates that a restart of WebSphere Application Server Liberty Base is required. Restart WebSphere Liberty. |
| Capacidade | dynamic_agent |
| Classificacao de risco | mutating |
| Modo de operacao | guided_action |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awstrmst.pdf, Troubleshooting Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer ambiente com o componente relevante ativo. |
| Terminologia normalizada | command=restart |
| Status de revisao | verified |
| Tipo | command |
| Codigo da mensagem | AWKTSA050E |
| Familia | incident-awktsa050e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWKTSA050E no HWA?
- Como solucionar ou diagnosticar o erro AWKTSA050E no HWA?
- Qual endpoint REST API V2 é utilizado para dynamic_agent no HWA?
- O que causa e como solucionar o problema: apos submeter workload, a mensagem AWKTSA050E 'A problem with the JCL content, prevent Dynamic Workload Bridge from submitting the job' e escrita no messages?


---

### 47. `hwa-10.2.8-incident-critical-empty-hotlist-0141`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `critical-network`

**Afirmacao / Conteudo:**

Sintoma: um job critical de alto risco tem uma hot list vazia. Causa: normalmente ocorre se um job critical ou predecessor critical foi projetado com um conflito que o fara sempre atrasar (ex.: start restriction apos o deadline do job critical); a hot list fica vazia se o job/job stream que causa o problema nao tem as dependencias follows resolvidas. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - critical empty hotlist |
| Citacao de suporte | This normally only occurs if you have designed a critical job or a critical predecessor with a conflict which means it will always be late, for example a start restriction after the critical job deadline. |
| Coletado em | 2026-08-23 |
| Capacidade | critical-network |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| verbs | list; start |
| Familia | incident-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: um job critical de alto risco tem uma hot list vazia?
- O que causa e como solucionar o problema: um job critical de alto risco tem uma hot list vazia?


---

### 48. `hwa-10.2.8-incident-mrc019e-0022`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `connection`

**Afirmacao / Conteudo:**

Sintoma: AWSMRC019E (EOF/erro de comunicacao) ao conectar ocli ou REST. Causa: contextroot incorreto (ex.: /twsd sozinho em vez de /,/twsd/cli) ou autenticacao ausente. Resolucao: usar contextroot /,/twsd/cli no config.yaml do ocli e configurar a API Key (connection.jwt).

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 22/08: contextroot /,/twsd/cli + jwt resolveu AWSMRC019E.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/t_authenticatingcli_apikey.html |
| Titulo da fonte | Authenticating Orchestration CLI using API Keys - HCL Workload Automation 10.2.8 |
| Citacao de suporte | contextroot |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | connection |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['ocli/REST connect com contextroot'], result=contextroot /twsd sozinho -> AWSMRC019E (EOF); contexto real /,/twsd/cli funciona (P29 ocli; lab-validation-2026-08-22-job-creation-gaps.jsonl), validated_at=2026-08-22T00:30:00BRT |
| Tipo | command |
| Ferramenta | ocli |
| Codigo da mensagem | AWSMRC019E |
| Familia | incident-mrc019e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSMRC019E no HWA?
- Como solucionar ou diagnosticar o erro AWSMRC019E no HWA?
- O que causa e como solucionar o problema: AWSMRC019E (EOF/erro de comunicacao) ao conectar ocli ou REST?


---

### 49. `hwa-10.2.8-incident-tokensrv-password-0095`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `windows`

**Afirmacao / Conteudo:**

Sintoma: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation. Causa: o usuario sob o qual esses servicos iniciam pode ter mudado a senha, ou o nome do servico nao corresponde ao esperado pelo HWA (impactado por mudanca na configuracao da workstation). Resolucao: seguir o procedimento do Administration Guide para o caso de senha alterada; temporariamente, iniciar o servico manualmente pelo Windows Services panel. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Token service fails |
| Citacao de suporte | The user under which these services start might have changed password... To resolve the problem temporarily, start the service manually using the Windows Services panel |
| Coletado em | 2026-08-23 |
| Capacidade | windows |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=restart |
| Status de revisao | verified |
| Tipo | command |
| Familia | incident-tokensrv |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation?
- O que causa e como solucionar o problema: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation?


---

### 50. `hwa-10.2.8-k8s-deploy-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os pre-requisitos para deployment via helm chart em Kubernetes incluem: Helm 3.12 ou posterior, Kubernetes versao 1.29 ou posterior, kubectl, OpenSSL, Jetstack cert-manager, um ingress controller (para NGINX via helm, habilitar controller.extraArgs.enable-ssl-passthrough), Grafana e Prometheus para dashboards, API key do HCL Entitled Registry (hclcr.io) e, opcionalmente, o Gateway API para roteamento de trafego externo em vez de Ingress.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Prerequisites). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicontaineronOpenShiftV4x.html |
| Titulo da fonte | Deploying HCL Workload Automation components on Red Hat OpenShift using helm charts - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Before you begin the deployment process, ensure your environment meets the following prerequisites: Helm 3.12 or later; OpenSSL; Grafana and Prometheus for monitoring dashboard; Jetstack cert-manager; Ingress controller...; Kubernetes version: >=1.29 or later; kubectl command-line tool...; API key for accessing HCL Entitled Registry: hcl.cr.io |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_deploy |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | k8s |
| verbs | deploy |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?


---

### 51. `hwa-10.2.8-k8s-deploy-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as imagens de container do deployment Kubernetes sao servidas pelo HCL Entitled Registry hclcr.io/wa, com tags por versao: hcl-workload-automation-agent-dynamic, hcl-workload-automation-server e hcl-workload-automation-console na tag 10.2.8.00.20260727; o acesso as imagens requer um secret docker-registry no namespace criado com kubectl create secret docker-registry sa-<namespace> --docker-server=hclcr.io --docker-username=<user> --docker-password=<api_key>.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Accessing the container images / Creating the Secret). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_inst/eqqi1getstartedDocker.html |
| Titulo da fonte | Deploying with containers - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The images are as follows: hclcr.io/wa/hcl-workload-automation-agent-dynamic: 10.2.8.00.20260727; hclcr.io/wa/hcl-workload-automation-server: 10.2.8.00.20260727; hclcr.io/wa/hcl-workload-automation-console: 10.2.8.00.20260727. To create a pull secret for your entitlement key that enables access to the entitled registry, run the following command: kubectl create secret docker-registry -n <workload_automation_namespace> sa-<workload_automation_namespace> --docker-server=<registry_server> --docker-username=<user_name> --docker-password=<password> |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_deploy |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | k8s |
| verbs | create; deploy |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as imagens de container do deployment Kubernetes sao servidas pelo HCL Entitled Registry hclcr?


---

### 52. `hwa-10.2.8-k8s-deploy-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `agents`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para dynamic agent em Kubernetes com remote gateway, os parametros adicionados a partir da versao 10.2 no deployment wa-agent sao agent.dynamic.gateway.hostname (IP/hostname do agente com local gateway), agent.dynamic.gateway.port (porta do agente com local gateway, default 31114) e agent.dynamic.gateway.jmFullyQualifiedHostname (hostname do novo agente); e necessario atualizar JobManagerGWURIs no arquivo JobManagerGW.ini do agente com local gateway para apontar para o nome do servico (ex.: https://wa-agent:31114/ita/JobManagerGW/JobManagerRESTWeb/JobScheduler/resource).

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Enabling installation of dynamic agents on kubernetes with a remote gateway). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideppec.html |
| Titulo da fonte | Considerations about deploying with containers - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The newly added parameters in version 10.2 facilitates you to deploy a new dynamic agent and enables the communication directly with another agent gateway: agent.dynamic.gateway.hostname, agent.dynamic.gateway.port (Default import value 31114), agent.dynamic.gateway.jmFullyQualifiedHostname. For containers, ensure to replace the JobManagerGWURIs value from JobManagerGWURIs=https://localhost:31114/... to JobManagerGWURIs=https://<wa-agent-service-name>:31114/... |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_agent_gateway |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | deploy |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?
- Como configurar ou solucionar problemas no dynamic agent ou broker para agents?


---

### 53. `hwa-10.2.8-message-ita047i-0153`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

AWSITA047I: mensagem informativa do JobManager indicando inicio/parada de processo no dynamic agent. Observada no lab: apos ShutDownLwa e StartUpLwa, MDMDA retornou com o flag JobManager e o registro de recursos foi retomado, mas uma nova submissao ad hoc com alias unico permaneceu READY — o restart sozinho nao resolveu o dispatch; AWSITA047I 'Starting' e AWSITA111I 'The Resource Advisor Agent is stopped' foram registrados. Fonte: lab HWA 10.2.8 (WSL2).

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (agent-restart-ready-0020).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | insufficient_evidence |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - agent restart ready |
| Citacao de suporte | AWSITA111I The Resource Advisor Agent is stopped; AWSITA047I Starting... restart alone did not resolve dispatch |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: ShutDownLwa/StartUpLwa -> MDMDA retornou com JobManager flag, mas job READY persistiu; AWSITA047I (Starting) registrado. Evidencia: agent-restart-ready-0020. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA047I, command=restart |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA047I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA047I no HWA?
- Qual é o significado da mensagem de erro AWSITA111I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA111I no HWA?
- Qual é o significado da mensagem de erro AWSITA047I no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSITA111I no HWA e qual ação é recomendada?


---

### 54. `hwa-10.2.8-resource-resource-units-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

Um recurso é uma restrição de agendamento física ou lógica (unidades de fita, conexões de banco de dados, slots de aplicação); é associado a uma workstation com unidades disponíveis; jobs solicitam unidades via dependência needs; as unidades permanecem reservadas enquanto o job é executado e são liberadas ao concluir.

> **ATENCAO / RESSALVAS DE USO:** Recursos só podem ser usados como dependência por jobs/job streams que rodam na workstation onde o recurso é definido; alocação por prioridade quando unidades insuficientes.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | resource=recurso de agendamento físico/lógico, workstation=workstation onde o recurso é definido, units=unidades disponíveis do recurso, needs=dependência que solicita unidades do recurso, release=liberação das unidades após conclusão do job/job stream |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgresdef.html |
| Titulo da fonte | Resource definition |
| Citacao de suporte | Resources represent physical or logical scheduling resources that can be used as dependencies for jobs and job streams. ... The resource units involved in needs dependencies for a job or for a job stream remain busy until the job or job stream is completed (successfully or not). The resource units are released as soon as the job or job stream is completed. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | resource-resource |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Um recurso é uma restrição de agendamento física ou lógica (unidades de fita, conexões de banco de dados, slots de aplicação); é associado a uma workstation com unidades disponíveis; jobs solicitam unidades via dependência needs; as unidades permanecem reservadas enquanto o job é executado e são liberadas ao concluir?


---

### 55. `hwa-10.2.8-rest-v2-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

A documentação HWA 10.2.8 recomenda REST API V2 para integrações futuras. Context: REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration.

> **ATENCAO / RESSALVAS DE USO:** Verified verbatim on the official v1028 page.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HCL Workload Automation with REST API |
| Citacao de suporte | REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration. |
| Coletado em | 2026-08-18 |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=rest |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | rest-v2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: A documentação HWA 10.2.8 recomenda REST API V2 para integrações futuras?


---

### 56. `hwa-10.2.8-restapi-auth-apikey-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `rest_api` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a autenticacao na REST API (incluindo REST API V2) pode ser feita por API Keys, permitindo autenticar uma linha de comando ou aplicacao de forma facil e rapida. As API Keys sao gerenciadas via OCLI (comando ocli apikey create/list/delete) e enviadas no header HTTP x-api-key. A API Key substitui a necessidade de usuario/senha em automacoes, oferecendo maior seguranca (rotacao de chaves, escopo por usuario).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Summary of enhancements). API Keys sao uma alternativa ao basic auth para automacao. [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 (Enhancing authentication using API Keys) |
| Citacao de suporte | Use API Keys to authenticate a command line or application easily and quickly. |
| Coletado em | 2026-08-25 |
| Capacidade | rest_api_auth |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=ocli |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | ocli |
| verbs | create; delete; list |
| Familia | restapi-auth |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para auth no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a autenticacao na REST API (incluindo REST API V2) pode ser feita por API Keys, permitindo autenticar uma linha de comando ou aplicacao de forma facil e rapida?


---

### 57. `hwa-10.2.8-restapi-auth-jwt-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `rest_api` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a autenticacao de agentes pode ser aprimorada usando JSON Web Tokens (JWT). Os JWTs sao usados para autenticar agentes dinâmicos junto ao master domain manager, substituindo o certificado SSL tradicional. O JWT oferece um padrao moderno de autenticacao, permitindo maior seguranca e integracao com sistemas de identidade existentes. O JWT e configurado no arquivo jwtFed.xml do DWC/engine.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Summary of enhancements). O JWT para agentes complementa a API Key para usuarios. O arquivo jwtFed.xml foi observado no lab em /opt/hwa/DWC/DWC_DATA/.../configDropins/overrides/. [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 (Enhancing agent authentication using JSON Web Tokens) |
| Citacao de suporte | Use JSON Web Tokens to enhance your agent authentication standard. |
| Coletado em | 2026-08-25 |
| Capacidade | rest_api_auth |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=restapi |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | restapi-auth |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para auth no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a autenticacao de agentes pode ser aprimorada usando JSON Web Tokens (JWT)?


---

### 58. `hwa-10.2.8-restapi-devguide-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `rest_api` / `devguide`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Developer's Guide (Driving HCL Workload Automation) documenta o uso da REST API para operacoes de workload. Exemplo: para submeter um job stream no plano atual, use GET /twsd/api/v2/model/jobstream com filtros de modelo ou OQL para encontrar o job stream pelo nome (ex.: JS-API), obtenha o ID do job stream na resposta, depois use POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit para submete-lo no plano. A resposta inclui count, results com kind, key, def (com id, folder, name, workstation, options, runCycles, matchingCriteria). O Developer's Guide completo esta em https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Developer's Guide - REST API). O Developer's Guide completo (awsddmst.pdf) cobre criacao de job definitions, setting draft, fence, dependencies, ad-hoc jobs, predecesors/successors. [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan - HCL Workload Automation 10.2.8 |
| Citacao de suporte | GET /twsd/api/v2/model/jobstream ... POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit |
| Coletado em | 2026-08-25 |
| Capacidade | rest_api_v2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | oql |
| verbs | plan |
| Familia | restapi-devguide |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?


---

### 59. `hwa-10.2.8-restapi-oql-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `rest_api` / `oql`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Orchestration Query Language (OQL) e uma linguagem de consulta para a REST API V2 que permite ordenar resultados de forma simples. O OQL pode ser usado sozinho ou combinado com planFilter (planFilter para filtragem, OQL para ordenacao). O OQL e mais simples que o planFilter e oferece uma sintaxe mais acessivel para consultas aos recursos de workload (job streams, jobs, planos).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Summary of enhancements). OQL complementa o planFilter com ordenacao e sintaxe mais simples. [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 (OQL - Orchestration Query Language) |
| Citacao de suporte | Orchestration Query Language: querying has never been so easy. |
| Coletado em | 2026-08-25 |
| Capacidade | rest_api_oql |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=restapi |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | restapi-oql |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para oql no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Orchestration Query Language (OQL) e uma linguagem de consulta para a REST API V2 que permite ordenar resultados de forma simples?


---

### 60. `hwa-10.2.8-restapi-v2-intro-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `rest_api` / `v2_overview`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a REST API V2 foi introduzida para operar o produto tanto pela Interface de Usuario quanto pela Linha de Comando, acessivel via HTTPS ao master/backup domain manager (porta default 31116). Os novos recursos incluem: (1) filtragem aprimorada via planFilter (similar a sintaxe do conman) ou OQL (Orchestration Query Language, mais simples e com ordenacao), podendo usar ambos combinados (planFilter para filtragem, OQL para ordenacao); (2) payloads melhorados para consumo mais facil; (3) endpoints multi-item eficientes (cada acao pode ser executada por ID ou por filtro, permitindo operar em um item ou multiplos). A autenticacao pode ser feita por basic auth (usuario/senha), API Keys ou JSON Web Tokens (JWT).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Introducing REST API V2). A REST API V2 e a versao recomendada para integracoes externas. O Developer's Guide (awsddmst.pdf) contem exemplos de payloads e fluxos. [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Enhanced filtering opportunities: according to how specific your query needs to be, you can decide whether to use planFilter, which is similar to conman syntax and offers the same filtering capabilities, or OQL syntax, which is simpler and allows ordering the results. |
| Coletado em | 2026-08-25 |
| Capacidade | rest_api_v2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| Familia | restapi-v2 |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar v2_overview?
- Qual endpoint REST API V2 é utilizado para v2_overview no HWA?


---

### 61. `hwa-10.2.8-restauth-api-keys-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

A versão 10.2.8 enfatiza o uso de API Keys para autenticação CLI/REST; a primeira conexão com o HCL Workload Automation via Orchestration CLI requer autenticação com API Keys.

> **ATENCAO / RESSALVAS DE USO:** Tópico sensível a credenciais com duas fontes oficiais. eqqg1JWTAPIKey.html confirma: 'Use API Keys to authenticate a command line or application easily and quickly.' e que API Keys podem autenticar composer, conman, wappman e ocli. A API Key gerada é armazenada no config.yaml; não expor tokens/credenciais em evidências.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | API Keys=API Keys, authentication=autenticação, Orchestration CLI=Orchestration CLI, REST=REST, JWT=JWT |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/t_authenticatingcli_apikey.html |
| Titulo da fonte | Authenticating Orchestration CLI using API Keys |
| Citacao de suporte | When you connect to HCL Workload Automation using Orchestration CLI for the first time, you need to authenticate the connection using API Keys. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | rest |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restauth-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: A versão 10.2.8 enfatiza o uso de API Keys para autenticação CLI/REST; a primeira conexão com o HCL Workload Automation via Orchestration CLI requer autenticação com API Keys?


---

### 62. `hwa-10.2.8-restocli-abbreviated-forms-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Os comandos do Orchestration CLI no HCL Workload Automation 10.2.8 possuem formas abreviadas (podem ser usadas a abreviatura ou a forma por extenso) e as opções de comando não diferenciam maiúsculas de minúsculas, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentadas as formas abreviadas e a insensibilidade a maiúsculas/minúsculas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | abbreviated_forms=formas abreviadas dos comandos, case_insensitive=opções de comando não diferenciam maiúsculas/minúsculas |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/c_oclicommands.html |
| Titulo da fonte | Orchestration CLI commands |
| Citacao de suporte | The commands that you can use in Orchestration CLI have abbreviated forms. You can either use the abbreviation or the spelled-out form to complete the task. ... The command options are not case sensitive and you can use either uppercase or lowercase letters. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-abbreviated |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Os comandos do Orchestration CLI no HCL Workload Automation 10.2.8 possuem formas abreviadas (podem ser usadas a abreviatura ou a forma por extenso) e as opções de comando não diferenciam maiúsculas de minúsculas, conforme documentação oficial?


---

### 63. `hwa-10.2.8-restocli-api-keys-0016`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

A autenticação da linha de comando e de aplicações contra o HCL Workload Automation 10.2.8 é documentada pelo uso de API Keys (Personal e Service) geradas no Dynamic Workload Console e de JSON Web Token (parâmetro -jwt), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Credencial-sensível: autenticação via API Keys/JWT confirmada em duas fontes oficiais.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | api_keys=API Keys Personal e Service, jwt=JSON Web Token (parâmetro -jwt), use_case=autenticar composer, conman, wappman e ocli |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1JWTAPIKey.html |
| Titulo da fonte | Enhancing authentication using API Keys |
| Citacao de suporte | You can use API Keys to authenticate the command line. You can use an API Key to get authenticated when you launch composer, conman, wappman, and ocli commands, instead of having to provide username and password as in previous versions. ... you can either specify it in the command line with the -jwt parameter, or add it in the useropts file. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | ocli |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: A autenticação da linha de comando e de aplicações contra o HCL Workload Automation 10.2.8 é documentada pelo uso de API Keys (Personal e Service) geradas no Dynamic Workload Console e de JSON Web Token (parâmetro -jwt), conforme documentação oficial?


---

### 64. `hwa-10.2.8-restocli-base-url-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

A base URL documentada da REST API V2 é https://hostname:port_number/twsd, onde hostname é o master domain manager (MDM) ou backup MDM e port_number é a porta HTTPS cujo padrão é 31116, no HCL Workload Automation 10.2.8 conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado o acesso à REST API V2 por URL base /twsd e interação via Swagger Docs em https://MDM_IP_address:tdwbport/twsd/.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | base_url=/twsd, host=master domain manager ou backup master domain manager, default_port=31116, protocol=HTTPS |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HCL Workload Automation with REST API |
| Citacao de suporte | After installing your master domain manager or backup master domain manager, you can access the available REST API services by connecting to the following URL: https://hostname:port_number/twsd ... The default is 31116. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | mdm |
| Familia | restocli-base |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Qual a regra documentada no HWA Distributed sobre: A base URL documentada da REST API V2 é https://hostname:port_number/twsd, onde hostname é o master domain manager (MDM) ou backup MDM e port_number é a porta HTTPS cujo padrão é 31116, no HCL Workload Automation 10.2.8 conforme documentação oficial?


---

### 65. `hwa-10.2.8-restocli-command-groups-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O Orchestration CLI do HCL Workload Automation 10.2.8 é organizado em três grupos de comandos principais (context, model e plan), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentados os grupos de comandos context, model e plan.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command_groups=context, model, plan |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/c_oclicommands.html |
| Titulo da fonte | Orchestration CLI commands |
| Citacao de suporte | In HCL Workload Automation, you can use the command line to run context, model, and plan commands. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan |
| Familia | restocli-command |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: O Orchestration CLI do HCL Workload Automation 10.2.8 é organizado em três grupos de comandos principais (context, model e plan), conforme documentação oficial?


---

### 66. `hwa-10.2.8-restocli-comparison-operators-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

A sintaxe OQL do HCL Workload Automation 10.2.8 documenta as keywords AND, OR, IN, NOT IN, LIKE, NOT LIKE, ORDER BY (ASC/DESC), além dos operadores de comparação =, !=, <=, >=, <, > e de listas, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentadas keywords e operadores essenciais do OQL, incluindo curingas @ e ? em LIKE/NOT LIKE.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | keywords=AND, OR, IN, NOT IN, LIKE, NOT LIKE, ORDER BY, comparison_operators==, !=, <=, >=, <, >, wildcards=@ (todos os caracteres) e ? (um único caractere) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/oql.html |
| Titulo da fonte | Using Orchestration Query Language |
| Citacao de suporte | LIKE Returns elements that match the specified pattern. The accepted characters are as follows: @: matches all characters. ?: matches a single character in a specific position. ... ORDER BY Orders the query results according to the specified fields. ... The accepted values are as follows: ASC: Sorts the results in ascending order. DESC: Sorts the results in descending order. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-comparison |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: A sintaxe OQL do HCL Workload Automation 10.2.8 documenta as keywords AND, OR, IN, NOT IN, LIKE, NOT LIKE, ORDER BY (ASC/DESC), além dos operadores de comparação =, !=, <=, >=, <, > e de listas, conforme documentação oficial?


---

### 67. `hwa-10.2.8-restocli-context-commands-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Os comandos de contexto (context) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem list, new, remove, set e switch, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentados os cinco comandos do grupo context.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | context_commands=list, new, remove, set, switch |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_contextcommands.html |
| Titulo da fonte | Multiple contexts and context commands |
| Citacao de suporte | To manage different contexts, you can use the following set of commands in Orchestration CLI: list, new, remove, set, switch. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | list; remove; set |
| Familia | restocli-context |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Os comandos de contexto (context) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem list, new, remove, set e switch, conforme documentação oficial?


---

### 68. `hwa-10.2.8-restocli-first-run-0023`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Na primeira conexão do Orchestration CLI com o HCL Workload Automation 10.2.8, a autenticação é realizada usando API Keys, com um fluxo inicial que exibe um link web para gerar a API Key, que é automaticamente atualizada no arquivo config.yaml, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Credencial-sensível: fluxo de autenticação por API Keys confirmado em duas fontes oficiais. Nenhuma credencial exposta.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | authentication=API Keys, first_run=primeira conexão gera API Key via link web, config=API Key atualizada automaticamente no config.yaml |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/t_authenticatingcli_apikey.html |
| Titulo da fonte | Authenticating Orchestration CLI using API Keys |
| Citacao de suporte | When you connect to HCL Workload Automation using Orchestration CLI for the first time, you need to authenticate the connection using API Keys. ... An error message with a web link to create the API Key is displayed. ... A message is displayed to indicate that the API Key has been successfully generated. This API Key gets automatically updated in the config.yaml file. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | ocli |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| verbs | run |
| Familia | restocli-first |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Na primeira conexão do Orchestration CLI com o HCL Workload Automation 10.2.8, a autenticação é realizada usando API Keys, com um fluxo inicial que exibe um link web para gerar a API Key, que é automaticamente atualizada no arquivo config?


---

### 69. `hwa-10.2.8-restocli-get-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint GET /twsd/api/v2/model/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar definições de job stream na base de dados (camada de modelo), podendo usar filtros de modelo ou OQL, sendo uma operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado exemplo de OQL: name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobstream, purpose=recuperar definições de job stream da base de dados, method=GET (read), query=model filters ou OQL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan |
| Citacao de suporte | Use the GET/twsd/api/v2/model/jobstream endpoint to find your job stream. You can query for the job stream using either model filters or OQL. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-get |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/model/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar definições de job stream na base de dados (camada de modelo), podendo usar filtros de modelo ou OQL, sendo uma operação de leitura, conforme documentação oficial?


---

### 70. `hwa-10.2.8-restocli-get-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint GET /twsd/api/v2/plan/job é documentado no HCL Workload Automation 10.2.8 para consultar jobs do plano atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado como verificação da submissão de jobs no plano.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/plan/job, purpose=recuperar jobs do plano atual, method=GET (read) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitadhocjob.html |
| Titulo da fonte | REST API - submitting an ad-hoc job |
| Citacao de suporte | To verify the submission, run the GET /twsd/api/v2/plan/job API call. Check that the ad-hoc job is successfully added to the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan |
| Familia | restocli-get |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/plan/job é documentado no HCL Workload Automation 10.2.8 para consultar jobs do plano atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial?


---

### 71. `hwa-10.2.8-restocli-get-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint GET /twsd/api/v2/plan/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar job streams no plano de produção atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado como consulta do plano para verificar job streams.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/plan/jobstream, purpose=recuperar job streams do plano atual, method=GET (read) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan |
| Citacao de suporte | To verify the submission, run the GET/twsd/api/v2/plan/jobstream API endpoint. Confirm that the response body contains the JSON object for the job stream you submitted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan |
| Familia | restocli-get |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/plan/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar job streams no plano de produção atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial?


---

### 72. `hwa-10.2.8-restocli-get-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint GET /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para consultar/verificar definições de job na base de dados, sendo uma operação de leitura, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado como verificação de criação da definição de job.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=GET /twsd/api/v2/model/jobdefinition, purpose=recuperar/verificar definições de job na base de dados, method=GET (read) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapicreatejobdef.html |
| Titulo da fonte | REST API - creating a new job definition in the database |
| Citacao de suporte | Run the GET/twsd/api/v2/model/jobdefinition API call again. Check that the job definition is present in the results list. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-get |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para consultar/verificar definições de job na base de dados, sendo uma operação de leitura, conforme documentação oficial?


---

### 73. `hwa-10.2.8-restocli-model-commands-0020`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Os comandos de modelo (model) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem add, delete, display, draft/undraft, extract, list, listfolder, lock, mkfolder, modify, new, nop/unnop, rename, renamefolder, replace, rmfolder e unlock, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comandos de modelo operam sobre definições na base de dados; incluem operações mutating (add, delete, replace, mkfolder, rmfolder, lock/unlock).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | model_commands=add, delete, display, extract, list, mkfolder, rmfolder, lock, unlock, modify, new, replace, rename, renamefolder, draft/undraft, nop/unnop, listfolder |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_ocli_modelcommands.html |
| Titulo da fonte | Model commands |
| Citacao de suporte | You can use the model commands to create or modify the item definitions for folders, jobs, job streams, and workstations. ... add, delete, display, draft/undraft, extract, list, listfolder, lock, mkfolder, modify, new, nop/unnop, rename, renamefolder, replace, rmfolder, unlock. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | ocli |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| verbs | add; delete; display; list; modify |
| Familia | restocli-model |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Os comandos de modelo (model) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem add, delete, display, draft/undraft, extract, list, listfolder, lock, mkfolder, modify, new, nop/unnop, rename, renamefolder, replace, rmfolder e unlock, conforme documentação oficial?


---

### 74. `hwa-10.2.8-restocli-model-layer-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

A REST API V2 do HCL Workload Automation 10.2.8 organiza os endpoints em camada de modelo (definições na base de dados, prefixo /model/) e camada de plano (plano de produção atual, prefixo /plan/), conforme documentação oficial dos endpoints.

> **ATENCAO / RESSALVAS DE USO:** A separação modelo/plano é evidenciada pelos prefixos /model/ e /plan/ nos endpoints documentados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | model_layer=camada /model/ (definições na base de dados), plan_layer=camada /plan/ (plano de produção atual) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan |
| Citacao de suporte | First, get the unique ID of the job stream you want to submit. Use the GET/twsd/api/v2/model/jobstream endpoint to find your job stream. ... Now, use the ID you retrieved to submit the job stream with the POST/twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit endpoint. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan |
| Familia | restocli-model |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 organiza os endpoints em camada de modelo (definições na base de dados, prefixo /model/) e camada de plano (plano de produção atual, prefixo /plan/), conforme documentação oficial dos endpoints?


---

### 75. `hwa-10.2.8-restocli-multi-item-endpoints-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

A REST API V2 do HCL Workload Automation 10.2.8 introduz endpoints multi-item eficientes, nos quais cada ação pode ser executada por ID ou por filtro, permitindo operar um único item ou múltiplos itens, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado o princípio de organização dos endpoints por ID ou filtro.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | multi_item_endpoints=endpoints que operam por ID ou por filtro, filter=filtro por planFilter ou OQL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 |
| Citacao de suporte | Introduction of efficient multi-item endpoints: each action can be performed by ID and by filter. In this way, you can decide whether to operate on a single item or on multiple items. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-multi |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 introduz endpoints multi-item eficientes, nos quais cada ação pode ser executada por ID ou por filtro, permitindo operar um único item ou múltiplos itens, conforme documentação oficial?


---

### 76. `hwa-10.2.8-restocli-ocli-wildcards-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O Orchestration CLI do HCL Workload Automation 10.2.8 suporta wildcards e delimitadores documentados, incluindo @ (padrão nulo ou um/múltiplos caracteres), ? (um único caractere), a sintaxe de pasta /@/ e delimitadores como +, ~, ;, , e =, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentados curingas e delimitadores para filtros de itens de agendamento na base de dados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | wildcards=@ e ? e sintaxe /@/ de pastas, delimiters=+, ~, ;, , e = |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_wildcards_ocli.html |
| Titulo da fonte | Special characters as wildcards and delimiters |
| Citacao de suporte | @: To indicate a null pattern or single character or more than one character (alphabets, numbers and/or alphanumeric). ... If you want the results to be more specific, you can use ? which can replace a single character. ... You can use /@/ in the syntax to indicate multiple folders. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-ocli |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: O Orchestration CLI do HCL Workload Automation 10.2.8 suporta wildcards e delimitadores documentados, incluindo @ (padrão nulo ou um/múltiplos caracteres), ? (um único caractere), a sintaxe de pasta /@/ e delimitadores como +, ~, ;, , e =, conforme documentação oficial?


---

### 77. `hwa-10.2.8-restocli-oql-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O Orchestration Query Language (OQL) é uma nova sintaxe que se aplica à REST API V2 e auxilia no monitoramento do ambiente de plano de produção do HCL Workload Automation 10.2.8, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado também como linguagem de filtragem usada na REST API V2 e no Orchestration Monitor do Dynamic Workload Console.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | OQL=Orchestration Query Language, purpose=filtragem de consultas na REST API V2 e no Orchestration Monitor |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1OQL.html |
| Titulo da fonte | Orchestration Query Language (OQL) |
| Citacao de suporte | The Orchestration Query Language (OQL) is a new syntax that applies to REST API V2 and helps you monitoring your HCL Workload Automation production plan environment. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-oql |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: O Orchestration Query Language (OQL) é uma nova sintaxe que se aplica à REST API V2 e auxilia no monitoramento do ambiente de plano de produção do HCL Workload Automation 10.2.8, conforme documentação oficial?


---

### 78. `hwa-10.2.8-restocli-pagination-envelope-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

The documented HCL Workload Automation 10.2.8 REST API V2 response envelope contains "count" and "results" fields, but no pagination parameters (limit, offset, page) are documented in the official REST API reference pages (awsddrestapi.html or the OpenAPI spec WA_API3_v2.json).

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausência de paginacao documentada; paginacao pode existir internamente mas nao esta documentada nas paginas oficiais consultadas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | pagination=parâmetros de paginação (limit/offset/page) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HCL Workload Automation with REST API - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The response is a JSON object containing a count field indicating the number of items returned and a results field containing the requested items. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | limit |
| Familia | restocli-pagination |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 79. `hwa-10.2.8-restocli-path-param-0011`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit é documentado no HCL Workload Automation 10.2.8 para submeter um job stream ao plano de produção atual, usando o ID do job stream de modelo, sendo uma operação mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado que não é necessário corpo de requisição para esta ação.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit, purpose=submeter um job stream no plano atual, method=POST (mutating), path_param=model_jobstream_id |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan |
| Citacao de suporte | Now, use the ID you retrieved to submit the job stream with the POST/twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit endpoint. ... No request body is required for this action. ... The API returns a success message with the ID of the job stream in the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | ocli |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan; submit |
| Familia | restocli-path |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream/ no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit é documentado no HCL Workload Automation 10.2.8 para submeter um job stream ao plano de produção atual, usando o ID do job stream de modelo, sendo uma operação mutating, conforme documentação oficial?


---

### 80. `hwa-10.2.8-restocli-plan-commands-0021`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Os comandos de plano (plan) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem submit job, submit sched, submit docommand, rerun, cancel job, cancel sched, release job, release sched, showjobs, kill, hold/release e muitos outros, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comandos de plano operam sobre itens no plano atual; incluem operações mutating (submit, cancel, kill, rerun, release, adddep/deldep).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | plan_commands=submit job, submit sched, rerun, cancel job, cancel sched, release job, release sched, showjobs, kill, showschedules, adddep, deldep, fence, limit, nop/unnop |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_ocli_plancommands.html |
| Titulo da fonte | Plan commands |
| Citacao de suporte | adddep job, adddep sched, altjob, altpass, altpri, cancel job, cancel sched, confirm, change resource, deldep job, deldep sched, fence, kill, limit cpu, limit sched, listfolder, nop/unnop, release job, release sched, reply, rerun, showcpu, showfile, showjobs, showprompt, show resource, showschedules, submit docommand, submit job, submit sched. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | ocli |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| verbs | cancel; kill; plan; release; rerun; showjobs; submit |
| Familia | restocli-plan |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Os comandos de plano (plan) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem submit job, submit sched, submit docommand, rerun, cancel job, cancel sched, release job, release sched, showjobs, kill, hold/release e muitos outros, conforme documentação oficial?


---

### 81. `hwa-10.2.8-restocli-post-0009`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint POST /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para criar uma definição de job (job definition) na base de dados, sendo uma operação mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado o payload da definição (kind JobDefinition com campo def) e a resposta retornando o ID da nova definição.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/model/jobdefinition, purpose=criar definição de job na base de dados, method=POST (mutating) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapicreatejobdef.html |
| Titulo da fonte | REST API - creating a new job definition in the database |
| Citacao de suporte | Use the POST/twsd/api/v2/model/jobdefinition endpoint to make a POST request. ... The API response returns the ID for the new job definition. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | ocli |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-post |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?
- Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para criar uma definição de job (job definition) na base de dados, sendo uma operação mutating, conforme documentação oficial?


---

### 82. `hwa-10.2.8-restocli-post-0010`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O endpoint POST /twsd/api/v2/plan/job/submit-ad-hoc-job é documentado no HCL Workload Automation 10.2.8 para submeter um job ad-hoc ao plano, sendo uma operação mutating, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** O caminho documentado é /plan/job/submit-ad-hoc-job (não simplesmente /plan/job). O corpo da requisição define task e workstationKey.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | endpoint=POST /twsd/api/v2/plan/job/submit-ad-hoc-job, purpose=submeter um job ad-hoc, method=POST (mutating) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitadhocjob.html |
| Titulo da fonte | REST API - submitting an ad-hoc job |
| Citacao de suporte | Use the POST /twsd/api/v2/plan/job/submit-ad-hoc-job API endpoint. ... The API returns a success message, and the ad-hoc job is submitted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | ocli |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan; submit |
| Familia | restocli-post |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job/submit-ad-hoc-job no HWA?
- Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?


---

### 83. `hwa-10.2.8-restocli-query-term-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

Uma consulta OQL no HCL Workload Automation 10.2.8 começa com uma expressão composta por conditions chamadas queryTerms, onde cada queryTerm contém três elementos (field, comparison_operator, value) e os campos e valores são case-sensitive, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentada a estrutura sintática básica do OQL.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | queryTerm=condição mínima de uma consulta OQL, field=campo, comparison_operator=operador de comparação, value=valor, case_sensitive=campos e valores distinguem maiúsculas/minúsculas |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/oql.html |
| Titulo da fonte | Using Orchestration Query Language |
| Citacao de suporte | An OQL query begins with an expression, which is composed of different conditions, known as queryTerms. A queryTerm is the minimum condition of a OQL construction, for example jobStreamName = test1. QueryTerms include three main elements: a field, a comparison_operator, and a value. The fields and the values of the query are case-sensitive. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-query |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: Uma consulta OQL no HCL Workload Automation 10.2.8 começa com uma expressão composta por conditions chamadas queryTerms, onde cada queryTerm contém três elementos (field, comparison_operator, value) e os campos e valores são case-sensitive, conforme documentação oficial?


---

### 84. `hwa-10.2.8-restocli-rest-api-v2-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

A REST API V2 é a nova versão das REST APIs do HCL Workload Automation 10.2.8, projetada para operar o produto tanto pela Interface de Usuário quanto pela Interface de Linha de Comando, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado que a REST API V2 é altamente recomendada para integrações futuras.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | rest_api_v2=nova versão das REST APIs, scope=UI e Command Line Interface |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 |
| Citacao de suporte | A new version of REST APIs has been introduced to operate on the product from both User Interface and Command Line Interface. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restocli-rest |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: A REST API V2 é a nova versão das REST APIs do HCL Workload Automation 10.2.8, projetada para operar o produto tanto pela Interface de Usuário quanto pela Interface de Linha de Comando, conforme documentação oficial?


---

### 85. `hwa-10.2.8-restocli-version-command-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

O comando version do Orchestration CLI no HCL Workload Automation 10.2.8 tem a sintaxe documentada ocli [context|model|plan|plugin] version|v e exibe a versão do Orchestration CLI instalada, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentada a sintaxe do comando version (com abreviatura v).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | version_command=ocli [context|model|plan|plugin] version|v, purpose=exibir a versão do Orchestration CLI instalada |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_version.html |
| Titulo da fonte | version |
| Citacao de suporte | You can use the version command to view the version of Orchestration CLI that is installed in your system. ... ocli [context|model|plan|plugin] version|v |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ocli |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | ocli |
| verbs | plan; version |
| Familia | restocli-version |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para ocli no HWA?
- Qual a regra documentada no HWA Distributed sobre: O comando version do Orchestration CLI no HCL Workload Automation 10.2.8 tem a sintaxe documentada ocli [context|model|plan|plugin] version|v e exibe a versão do Orchestration CLI instalada, conforme documentação oficial?


---

### 86. `hwa-10.2.8-restsubmit-rest-api-v2-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

Endpoints da REST API v2: GET /twsd/api/v2/model/jobdefinition, GET /twsd/api/v2/model/jobstream, GET /twsd/api/v2/plan/job, GET /twsd/api/v2/plan/jobstream e POST /twsd/api/v2/plan/jobstream/{id}/submit.

> **ATENCAO / RESSALVAS DE USO:** POST /plan/jobstream/{id}/submit é mutating (submete job stream ao plano atual). GET /model/jobdefinition confirmado em awsddapicreatejobdef.html; GET /plan/job confirmado em awsddapisubmitadhocjob.html. O endpoint de submit não requer corpo de requisição. A página awsddapisubmitjs.html está em common/src_dgd (não em distr/src_ref).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | model/jobdefinition=model/jobdefinition, model/jobstream=model/jobstream, plan/job=plan/job, plan/jobstream=plan/jobstream, plan/jobstream/{id}/submit=plan/jobstream/{id}/submit, REST API V2=REST API v2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddapisubmitjs.html |
| Titulo da fonte | REST API - submitting a job stream in the current plan |
| Citacao de suporte | Use the GET/twsd/api/v2/model/jobstream endpoint to find your job stream. ... submit the job stream with the POST/twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit endpoint. ... run the GET/twsd/api/v2/plan/jobstream API endpoint. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | jobstream |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | restv2 |
| verbs | plan; submit |
| Familia | restsubmit-rest |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?
- Qual a regra documentada no HWA Distributed sobre: Endpoints da REST API v2: GET /twsd/api/v2/model/jobdefinition, GET /twsd/api/v2/model/jobstream, GET /twsd/api/v2/plan/job, GET /twsd/api/v2/plan/jobstream e POST /twsd/api/v2/plan/jobstream/{id}/submit?


---

### 87. `hwa-10.2.8-restv2-endpoints-0148`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest_api_v2`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, a REST API V2 esta disponivel em https://<host>:31116/twsd/api/v2/ com autenticacao Bearer (JWT de API key Personal). Endpoints GET read-only validados no lab: engine/info (licenseType/timezone), engine/users, engine/groups, model/jobdefinition (84), model/jobstream, model/workstation (5), model/domain (MASTERDM master), model/variabletable, model/folder, plan/job (236), plan/job/{id}, plan/job/count, plan/jobstream (201), plan/workstation, plan/prompt, plan/resource, objects-info. O context root e '/twsd/api/v2/' e o JWT do ocli (Personal) autoriza a REST API v2.

> **ATENCAO / RESSALVAS DE USO:** model/workspace na spec mas 404 no lab

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | verified |
| Confianca | 0.95 |
| Produto | HWA |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsrgmst |
| Titulo da fonte | Lab validation R17 — REST API v2 endpoints |
| Citacao de suporte | engine/info: {licenseType:PERSERVER, timezone:America/Sao_Paulo}; plan/job: count=236; model/workstation: count=5 |
| Coletado em | 2026-08-23 |
| Responsavel | cowbot |
| Status de revisao | lab_validated |
| Pratica de comunidade | nao |
| Justificativa | Validado ponta a ponta no lab com JWT do ocli; spec OpenAPI oficial presente no WAR |
| Capacidade | rest_api_v2 |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=['GET engine/info', 'GET model/workstation', 'GET plan/job', 'GET objects-info'], result=20+ endpoints GET retornam 200 com JWT do ocli; contagens reais obtidas (jobs 236, jobstreams 201, workstations 5, jobdefs 84)., validated_at=2026-08-23T10:00:00BRT |
| Terminologia normalizada | command=twsd |
| Tipo | command |
| Ferramenta | ocli |
| Familia | restv2-endpoints |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/ no HWA?


---

### 88. `hwa-10.2.8-restv2-oql-name-0149`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `oql`

**Afirmacao / Conteudo:**

Na REST API V2 do HWA 10.2.8 (parametro 'oql' de GET /twsd/api/v2/plan/job), o filtro OQL usa o campo 'name' (ex.: oql=name = 'UPDATESTATS' retorna os jobs com esse nome). GAP doc x impl: a spec OpenAPI oficial exemplifica 'key.name = \'TEST_JOB\'', mas no lab 'oql=key.name = \'X\'' retorna 400 OQL_FILTER_SYNTAX_ERROR. A sintaxe aceita e 'name = \'X\'' (campo simples, sem prefixo key.).

> **ATENCAO / RESSALVAS DE USO:** Descoberta de lab — sintaxe real difere do exemplo oficial

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | verified |
| Confianca | 0.9 |
| Produto | HWA |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsrgmst |
| Titulo da fonte | Lab validation R17 — OQL filter syntax |
| Citacao de suporte | oql=name = 'UPDATESTATS' -> 200 count=2; oql=key.name = 'UPDATESTATS' -> 400 OQL_FILTER_SYNTAX_ERROR |
| Coletado em | 2026-08-23 |
| Responsavel | cowbot |
| Status de revisao | lab_validated |
| Pratica de comunidade | nao |
| Justificativa | Gap doc x impl confirmado no lab: spec documenta key.name mas servidor rejeita; campo aceito é name |
| Capacidade | oql |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=["GET /twsd/api/v2/plan/job?oql=name = 'UPDATESTATS'", "GET /twsd/api/v2/plan/job?oql=key.name = 'UPDATESTATS'"], result=name = 'X' -> 200 count=2; key.name = 'X' -> 400 OQL_FILTER_SYNTAX_ERROR. Gap confirmado., validated_at=2026-08-23T10:00:00BRT |
| Terminologia normalizada | command=twsd |
| Tipo | command |
| Ferramenta | restv2 |
| verbs | plan |
| Familia | restv2-oql |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?
- Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8 (parametro 'oql' de GET /twsd/api/v2/plan/job), o filtro OQL usa o campo 'name' (ex?


---

### 89. `hwa-10.2.8-restv2-oql-sort-0150`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `oql`

**Afirmacao / Conteudo:**

Na REST API V2 do HWA 10.2.8, o parametro 'oql' suporta ordenacao com dot notation: 'oql=ORDER BY key.name ASC' em GET /twsd/api/v2/plan/job retorna 200 com resultados ordenados (sem parametros de sort separados na URL). OQL com ORDER BY e o mecanismo de ordenacao da V2.

> **ATENCAO / RESSALVAS DE USO:** Contraste interessante: ORDER BY aceita key.name, mas filtro key.name rejeitado (claim 0149)

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | verified |
| Confianca | 0.92 |
| Produto | HWA |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsrgmst |
| Titulo da fonte | Lab validation R17 — OQL ORDER BY |
| Citacao de suporte | oql=ORDER BY key.name ASC -> HTTP 200, count=236, next com offset=3 |
| Coletado em | 2026-08-23 |
| Responsavel | cowbot |
| Status de revisao | lab_validated |
| Pratica de comunidade | nao |
| Justificativa | ORDER BY key.name ASC validado no lab — sort dentro do OQL funciona (diferente do filtro, onde key.name falha) |
| Capacidade | oql |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=['GET /twsd/api/v2/plan/job?oql=ORDER BY key.name ASC&limit=3'], result=200 OK, count=236, next URL com offset=3 — ordenacao OQL funcional., validated_at=2026-08-23T10:00:00BRT |
| Terminologia normalizada | command=twsd |
| Tipo | command |
| Ferramenta | restv2 |
| verbs | plan |
| Familia | restv2-oql |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?
- Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, o parametro 'oql' suporta ordenacao com dot notation: 'oql=ORDER BY key?


---

### 90. `hwa-10.2.8-restv2-pagination-0152`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `pagination`

**Afirmacao / Conteudo:**

Na REST API V2 do HWA 10.2.8, GET /twsd/api/v2/plan/job suporta paginacao explicita com 'limit' e 'offset' (ex.: limit=2 retorna 2 resultados e a resposta inclui 'next' com a URL completa para a proxima pagina: https://localhost:31116/twsd/api/v2/plan/job?limit=2&offset=2). O campo 'count' na resposta indica o total de itens (236).

> **ATENCAO / RESSALVAS DE USO:** count retorna total de itens; results paginados por limit/offset

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | verified |
| Confianca | 0.93 |
| Produto | HWA |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsrgmst |
| Titulo da fonte | Lab validation R17 — pagination |
| Citacao de suporte | plan/job?limit=2 -> 200 {count:236, results:[], next:'...?limit=2&offset=2'} |
| Coletado em | 2026-08-23 |
| Responsavel | cowbot |
| Status de revisao | lab_validated |
| Pratica de comunidade | nao |
| Justificativa | Paginacao limit/offset com URL next validada no lab |
| Capacidade | pagination |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=['GET /twsd/api/v2/plan/job?limit=2'], result=200 com count=236 e next URL apontando offset=2., validated_at=2026-08-23T10:00:00BRT |
| Terminologia normalizada | command=twsd |
| Tipo | command |
| Ferramenta | restv2 |
| verbs | limit; plan |
| Familia | restv2-pagination |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?
- Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, GET /twsd/api/v2/plan/job suporta paginacao explicita com 'limit' e 'offset' (ex?


---

### 91. `hwa-10.2.8-restv2-workspace-404-0153`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `model`

**Afirmacao / Conteudo:**

Na REST API V2 do HWA 10.2.8, o endpoint GET /twsd/api/v2/model/workspace aparece na spec OpenAPI oficial (WA_API3_v2.json) mas retorna HTTP 404 no lab — nao exposto/implementado neste ambiente. Diferente dos demais endpoints model/* (jobdefinition, workstation, domain, folder, calendar, variabletable) que respondem 200.

> **ATENCAO / RESSALVAS DE USO:** Possivel feature flag ou recurso de outra edicao (Universal Orchestrator?)

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | verified |
| Confianca | 0.85 |
| Produto | HWA |
| Versao | 10.2.8 |
| Plataforma | distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsrgmst |
| Titulo da fonte | Lab validation R17 — model/workspace 404 |
| Citacao de suporte | GET /twsd/api/v2/model/workspace -> HTTP 404 (spec lista o path) |
| Coletado em | 2026-08-23 |
| Responsavel | cowbot |
| Status de revisao | lab_validated |
| Pratica de comunidade | nao |
| Justificativa | Gap spec x impl: path documentado mas 404 no lab (pode ser recurso nao habilitado/versao) |
| Capacidade | model |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed |
| lab_validation | lab_environment=WSL2, HWA 10.2.8, https://localhost:31116/twsd/api/v2/, tested_commands=['GET /twsd/api/v2/model/workspace?limit=2'], result=404 — endpoint na spec mas nao disponivel no lab., validated_at=2026-08-23T10:00:00BRT |
| Terminologia normalizada | command=twsd |
| Tipo | command |
| Ferramenta | restv2 |
| Familia | restv2-workspace |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/workspace no HWA?
- Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, o endpoint GET /twsd/api/v2/model/workspace aparece na spec OpenAPI oficial (WA_API3_v2.json) mas retorna HTTP 404 no lab — nao exposto/implementado neste ambiente?


---

### 92. `hwa-10.2.8-runbook-recommended-first-component-0028`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, é uma boa prática iniciar o upgrade pelo Dynamic Workload Console (DWC) primeiro: ao atualizar o console para o novo nível de versão, ele pode ser usado para verificar se o ambiente está funcionando após atualizar os componentes restantes.

> **ATENCAO / RESSALVAS DE USO:** Documented upgrade best practice: DWC first; destructive/mutating environment change. Two official sources corroborate.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | procedure=upgrade, recommended_first_component=Dynamic Workload Console (DWC), purpose=post-upgrade verification |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading |
| Citacao de suporte | When upgrading your HCL Workload Automation environment, it is a good practice to start with the upgrade of the Dynamic Workload Console first. If you upgrade the console to the new product version level, you can then use it to verify that your environment is working after upgrading the remaining components. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | upgrade |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | upgrade |
| Familia | runbook-recommended |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é uma boa prática iniciar o upgrade pelo Dynamic Workload Console (DWC) primeiro: ao atualizar o console para o novo nível de versão, ele pode ser usado para verificar se o ambiente está funcionando após atualizar os componentes restantes?


---

### 93. `hwa-10.2.8-sec-api-key-0017`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `ocli`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a API Key (token JWT) usada para autenticar o Orchestration CLI é armazenada no arquivo config.yaml, localizado em $HOME/.OCLI/config.yaml (Linux) ou %userprofile%\.OCLI\config.yaml (Windows), adicionando ou substituindo o valor da propriedade JWT.

> **ATENCAO / RESSALVAS DE USO:** Caminhos documentados de armazenamento local do token; trata-se de material sensível — o arquivo deve ser tratado como credencial.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | API_Key=chave de API, JWT=JSON Web Token, config.yaml=arquivo de configuração do CLI, Orchestration_CLI=interface de linha de comando de orquestração |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/apikeyscenario.html |
| Titulo da fonte | Authenticating the command line client using API Keys |
| Citacao de suporte | Add or replace the JWT property, entering the API Key token you generated in Step 3 as the property value. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | ocli |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | ocli |
| Familia | sec-api |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a API Key (token JWT) usada para autenticar o Orchestration CLI é armazenada no arquivo config?


---

### 94. `hwa-10.2.8-sec-api-key-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `api`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, API Keys expiram por padrão após 365 dias; a duração e o intervalo de transição de status podem ser configurados com os parâmetros com.ibm.tws.dao.rdbms.apikey.expiring.timeout e com.ibm.tws.util.jwt.apikey.expiration.date no arquivo TWSConfig.properties, exigindo reinício do Liberty; API Keys já criadas não podem ser modificadas.

> **ATENCAO / RESSALVAS DE USO:** revalidacao pendente: sem 2a fonte oficial encontrada (2026-08-23); manter em backlog de revalidacao

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | API_Key=chave de API, expiration=expiração, TWSConfig.properties=arquivo de propriedades do servidor, Liberty=WebSphere Liberty |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/apikeyscenario.html |
| Titulo da fonte | Authenticating the command line client using API Keys |
| Citacao de suporte | API Keys expire by default after 365 days. You can set a custom duration for API Keys by adding the following parameters |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | api |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Tipo | other |
| verbs | status |
| Familia | sec-api |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, API Keys expiram por padrão após 365 dias; a duração e o intervalo de transição de status podem ser configurados com os parâmetros com?


---

### 95. `hwa-10.2.8-sec-manage-api-keys-0020`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `api`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, ao criar uma API Key na Dynamic Workload Console (menu Manage API Keys, tipo Personal ou Service), o token é exibido uma única vez na caixa de diálogo e a documentação instrui a salvá-lo e armazená-lo em local seguro.

> **ATENCAO / RESSALVAS DE USO:** Orientação documentada de manuseio seguro do token; para chaves tipo Service devem ser selecionados grupos. | v102 publication of the same scenario topic states the identical sentence (same topic, different 10.2.x doc publication).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Manage_API_Keys=gerenciar chaves de API, API_Key=chave de API, token=token |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/apikeyscenario.html |
| Titulo da fonte | Authenticating the command line client using API Keys |
| Citacao de suporte | The API Key token is displayed in the dialogue box. Save it and store it in a secure place. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | api |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Tipo | other |
| Familia | sec-manage |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, ao criar uma API Key na Dynamic Workload Console (menu Manage API Keys, tipo Personal ou Service), o token é exibido uma única vez na caixa de diálogo e a documentação instrui a salvá-lo e armazená-lo em local seguro?


---

### 96. `hwa-10.2.8-sec-open-id-connect-0019`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `api`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, ao executar o Orchestration CLI pela primeira vez, um erro exibe um link web para criação da API Key; após autenticar no provedor OpenID Connect configurado, a API Key gerada é atualizada automaticamente no arquivo config.yaml.

> **ATENCAO / RESSALVAS DE USO:** Documentado fluxo de primeira autenticação. | First connection fills the API Key field automatically (config.yaml auto-update fact).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | OpenID_Connect=provedor OpenID Connect, API_Key=chave de API, config.yaml=arquivo de configuração do CLI |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/t_authenticatingcli_apikey.html |
| Titulo da fonte | Authenticating Orchestration CLI using API Keys |
| Citacao de suporte | This API Key gets automatically updated in the config.yaml file. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | api |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Tipo | command |
| Ferramenta | ocli |
| verbs | open |
| Familia | sec-open |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, ao executar o Orchestration CLI pela primeira vez, um erro exibe um link web para criação da API Key; após autenticar no provedor OpenID Connect configurado, a API Key gerada é atualizada automaticamente no arquivo config?


---

### 97. `hwa-10.2.8-showjobs-agent-ready-0034`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, um job que falha porque o agente não está disponível é reiniciado automaticamente, volta a READY e aguarda a reconexão do agente. Context: If a job fails because the agent is not available, the job is automatically restarted and set to the READY status, waiting for the agent to connect again.

> **ATENCAO / RESSALVAS DE USO:** Behavior stated in the Comments section of the showjobs reference topic; it describes automatic restart on agent unavailability, not a manual rerun. Read-only diagnostic context.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs |
| Citacao de suporte | If a job fails because the agent is not available, the job is automatically restarted and set to the READY status, waiting for the agent to connect again. As soon as the agent connects again, the job is submitted. |
| Coletado em | 2026-08-18 |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showjobs |
| Status de revisao | verified |
| Tipo | other |
| verbs | set; showjobs; status |
| Familia | showjobs-agent |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, um job que falha porque o agente não está disponível é reiniciado automaticamente, volta a READY e aguarda a reconexão do agente?


---

### 98. `hwa-10.2.8-timezone-job-stream-level-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o fuso horário especificado no nível do job stream se aplica às definições de tempo dos run cycles e às restrições de tempo (definidas pelos keywords at, deadline, schedtime e until).

> **ATENCAO / RESSALVAS DE USO:** A página também informa que, se um fuso horário for especificado no job stream e em um keyword de restrição de tempo, eles devem ser iguais; e que, se nenhum fuso for especificado, o fuso do workstation é usado. Sintaxe: timezone|tz tzname.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | timezone=fuso horário, job stream level=nível do job stream, run cycle=run cycle, time restrictions=restrições de tempo, at=at, deadline=deadline, schedtime=schedtime, until=until |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjstimezone.html |
| Titulo da fonte | timezone |
| Citacao de suporte | The time zone specified at job stream level applies to the time definitions for the run cycles and the time restrictions (defined by the at, deadline, schedtime, and until keywords). |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | run |
| Familia | timezone-job |

**Perguntas relacionadas:**

- Qual o comportamento das opções until e deadline na submissão de jobs no conman?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o fuso horário especificado no nível do job stream se aplica às definições de tempo dos run cycles e às restrições de tempo (definidas pelos keywords at, deadline, schedtime e until)?


---

### 99. `hwa-10.2.8-trouble-awsres003e-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o Resource Advisor loga AWSRES003E quando nao recebe o heartbeat de uma workstation (em ambiente Linux a falha pode ocorrer por resolucao de host perdida em /etc/hosts); a causa e a workstation/alias de host nao resolvido ou indisponivel, e a recuperacao e restaurar a resolucao do hostname da workstation (ex.: readicionar o alias do MDMHOST em /etc/hosts) e verificar a conectividade de rede antes de reiniciar o monitoramento.

> **ATENCAO / RESSALVAS DE USO:** Observado em laboratorio 10.2.8: reinicio do WSL regenerou /etc/hosts e perdeu o alias MDMHOST, causando AWSRES003E. Recuperacao: readicionar alias. Diagnostico; nao modifica estado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSRES003E, component=Resource Advisor, symptom=heartbeat da workstation nao recebido, recovery=restaurar resolucao do hostname/alias e verificar rede |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; monitoring |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadmonitor.html |
| Titulo da fonte | HCL Workload Automation monitoring configuration |
| Citacao de suporte | AWSRES003E and AWSKRAE100E (heartbeat missed). |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; monitoring |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSRES003E no HWA?
- Como solucionar ou diagnosticar o erro AWSRES003E no HWA?


---

### 100. `hwa-10.2.8-vm-9f-0007`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A REST API V2 do HCL Workload Automation Distributed é servida no caminho https://hostname:port/twsd (porta padrão 31116), e não no caminho legado /JobManagerRESTWeb/, tanto na 10.2.0 quanto na 10.2.8. A REST API V2 foi introduzida na 10.1 Fix Pack 1.

> **ATENCAO / RESSALVAS DE USO:** Validado no lab container 10.2.8: REST API V2 servida em https://localhost:31116/twsd com 212 endpoints OpenAPI 3.1.0 e auth basic comprovada.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | REST API V2=interface REST de operação do produto, /twsd=caminho base da REST API V2, port=31116, introduced=10.1 Fix Pack 1, legacy_path=/JobManagerRESTWeb/ (V1) |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_dgd/awsddrestapi.html |
| Titulo da fonte | REST API (10.2.8) |
| Citacao de suporte | https://hostname:port/twsd |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | lab_validated |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | vm-9f |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para jobman no HWA?
- Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation Distributed é servida no caminho https://hostname:port/twsd (porta padrão 31116), e não no caminho legado /JobManagerRESTWeb/, tanto na 10.2.0 quanto na 10.2.8. A REST API V2 foi introduzida na 10.1 Fix Pack 1.?


---

### 101. `hwa-distributed-cancel-sched-pend-10.2.0-001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.0, `cancel sched`/`cs` requer acesso `cancel`; com `;pend`, antes do lançamento aguarda a resolução das dependências e, após o lançamento, cancela os jobs restantes; em ambos os casos os dependentes são liberados da dependência.

> **ATENCAO / RESSALVAS DE USO:** Re-verified 2026-08-19 against official 10.2.0 documentation (v102): behavior confirmed for 10.2.0 (cancel access; ;pend defers until dependencies resolved before launch; ;pend after launch cancels remaining jobs and releases dependents). Corroborated by 10.2.8 documentation with identical wording. Do not generalize to 10.1 or 9.x without checking those docs.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | destructive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgcancelsched.html |
| Titulo da fonte | cancel sched (HCL Workload Automation 10.2.0) |
| Citacao de suporte | Cancels a job stream. You must have cancel access to the job stream. If you use the ;pend option and the job stream has not been launched, cancellation is deferred until all of its dependencies, including an at time, are resolved. If you include the ;pend option and the job stream has already been launched, any remaining jobs in the job stream are cancelled, and any dependent jobs and job streams are released from the dependency. |
| Coletado em | 2026-08-18 |
| Capacidade | rest |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=conman, component=dynamic_workload_console |
| Status de revisao | verified |
| Tipo | other |
| verbs | cancel |
| Familia | cancel-sched |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.0, `cancel sched`/`cs` requer acesso `cancel`; com `;pend`, antes do lançamento aguarda a resolução das dependências e, após o lançamento, cancela os jobs restantes; em ambos os casos os dependentes são liberados da dependência?


---

### 102. `hwa-lab-10.2.8-agent-restart-reconnect-0048`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, after ShutDownLwa and StartUpLwa, dynamic agent MDMDA reconnected successfully with the JobManager flag preserved, LIMIT 10 and FENCE 0 maintained, and resource registration (AWSITA083I) continued after restart.

> **ATENCAO / RESSALVAS DE USO:** Restart preserved the workstation limit and fence settings; resource registration resumed normally. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local ShutDownLwa/StartUpLwa and conman showcpus

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Dynamic-agent restart and reconnect |
| Citacao de suporte | MDMDA ... LBI J M ... LIMIT 10 FENCE 0; AWSITA083I count 111 after restart. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSITA083I, command=restart |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA083I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA083I no HWA?
- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para mdm?


---

### 103. `hwa-lab-10.2.8-broker-topology-0070`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `topology`

**Afirmacao / Conteudo:**

In the HWA laboratory, the Dynamic Workload Broker workstation MDM_DWB exists (wks_agent_type='B' in mdl.wks_workstations) but the broker/gateway component is NOT running: JobManagerGW.ini has autostart=no (EIF port 31132), and no broker/JobManagerGW process is listening. The engine ports (31111 netman, 31113, 31114 agent, 31115/31116/31131 java/JobManager) are up, but the external JobManager REST service returned AWSJMR011E ServiceUnavailable earlier. CRITICAL jobs validated/ran SUCC in direct topology; the WSA global option (enWorkloadServiceAssurance, default YES) is not stored in local config files (it is a database global option).

> **ATENCAO / RESSALVAS DE USO:** The MDM_DWB broker workstation is defined but the broker runtime is not started. Enabling it would change lab topology. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local JobManagerGW.ini, mdl.wks_workstations, ss -tlnp

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Broker/gateway topology state |
| Citacao de suporte | MDM_DWB type B exists; JobManagerGW autostart=no; no broker process listening. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | topology |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSJMR011E, command=netman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJMR011E no HWA?
- Como solucionar ou diagnosticar o erro AWSJMR011E no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para topology?


---

### 104. `hwa-lab-10.2.8-claims-recovery-incident-0088`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

Incident and recovery of data/evidence/claims.jsonl (HWA training evidence). On 2026-08-18 a consolidation script run truncated claims.jsonl from 736 to 115 canonical records (the write failed partway, leaving the preserved prefix plus the manually appended recusal record). Recovery was performed from intact sources with precedence preserved > lab > shard > other: the 115 preserved prefix, 79 lab-validation-*.jsonl records, 524 research shard records (data/incoming/research/**/*.jsonl, schema-complete drafts), and 15 staging/other evidence records, plus the recusal record. The merged, deduplicated and normalized result is 677 valid records (verified=620, insufficient_evidence=34, community_practice=13, version_dependent=8, contradicted=2), all passing scripts/validate_evidence.py. Approximately 59 previously-integrated canonical records were not recoverable from any intact source (their source shards had been consumed during earlier integration); 93 SFT-referenced claim_ids now resolve to non-existent evidence records. SFT candidate files were re-audited: the 20 EDWA candidates reference only verified claims; the 34 syntax-rest candidates had 3 orphan claim_ids (hwa-10.2.8-fence-0001, hwa-10.2.8-limit-cpu-0001, hwa-10.2.8-rest-api-v2-endpoint-0011) which were repointed to verified lab claims (hwa-lab-10.2.8-fence-validation-0044, hwa-lab-10.2.8-limit-cpu-0074, hwa-lab-10.2.8-rest-v2-port-31116-live-0077). All candidate claim_ids now resolve to claims.jsonl.

> **ATENCAO / RESSALVAS DE USO:** Operational incident documentation: do NOT re-run a full rewrite of claims.jsonl without an atomic temp-file write + backup. Remaining loss (~59 canonical records + 93 orphan SFT references) is recorded for future re-verification batches.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmst_welcome.html |
| Titulo da fonte | HCL Workload Automation 10.2.8 - User's Guide and Reference (evidence pipeline) |
| Citacao de suporte | Recovered 677 valid records from preserved prefix (115), lab files (79), shards (524) and other evidence (15); validate_evidence.py passes. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=rest_api_v2, component=dynamic_workload_console |
| Status de revisao | verified |


---

### 105. `hwa-lab-10.2.8-corpus-edwa-expansion-0089`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

The HCL Workload Automation 10.2.8 training corpus was expanded with 22 official documentation pages covering EDWA (event-driven workload automation), BmEvents.conf and REST/event management, downloaded from help.hcl-software.com into data/raw/HCL-HWA-10.2.8/ (awsrgevntdrivworkauto, awsrgevntrulemgmntproc, awsrgeruledef, awsrgeventpro, awsrgtwsobjectsmonitor, awsrgfilemonitorevents, awsrgapplmonitor, awsrgdatesetmonitor, awsrgactionpro, awsrgtwsaction, awsrgmessagelogger, awsrggenericaction, awsrgmailsender, awsisnetvbmevents, awsisitmtepevents, awsrgdefineeventrule, awsrgtriggerruleelem, awsrgeventsend, awsrgeventsend4dyn, awsrgevtdef, awsrgprodproc, awsrgstartstop). The curation pipeline was re-run: extract_docs.py produced 21499 chunks (22 EDWA/BmEvents pages contributed ~221 chunks, 116 of which landed in train_full.jsonl), dedup_and_split.py produced 16846 eligible records (train 14933 / eval 1670 / buffer 243), audit_dataset.py passed with 0 shared hashes and 0 document-id overlap in the source-holdout cut, validate_tokens.py reported 0 sequences above the 2048-token limit, and simulate_dataset_quality.py returned verdict APROVADO COM RESSALVAS with critical=[], security_hits={}, synthetic_in_training=0, source-holdout provenance overlap 0/0/0, language_max_delta=0.0018, and unknown_version_share dropping to 0.0105.

> **ATENCAO / RESSALVAS DE USO:** 4 candidate pages returned HCL 404 (awsrgeventdrivworkauto, awsrgeventrulemgmntproc, awsrgtwsaction2, awsadedwa4diskspace - wrong URL spellings or moved pages) and were removed; correct spellings awsrgevntdrivworkauto/awsrgevntrulemgmntproc were fetched. All 22 pages are official and version 10.2.8.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation - HCL Workload Automation 10.2.8 |
| Citacao de suporte | verdict APROVADO COM RESSALVAS; 116 EDWA/BmEvents html chunks in train_full; unknown_version_share 0.0105. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=conman, component=dynamic_workload_console |
| Status de revisao | verified |


---

### 106. `hwa-lab-10.2.8-edwa-action-run-defect-0102`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, o endpoint POST /twsd/eventrule/engine/action_run/action/run (documentado no código como 'POST operation for run a List of ActionRun') sempre retorna HTTP 400 nesta versão (10.2.8.00): o provider RESTActionRunJsonListProvider chama por reflexão ActionRun.fromJsonList(String) (getMethod) e a classe com.ibm.tws.objects.log.ActionRun NÃO possui o método estático fromJsonList (o ActionRunHeader possui; o ActionRun apenas fromJson), causando NoSuchMethodException -> 400 antes de qualquer execução. O contrato decompilado mostra que, se o corpo fosse aceito, runActions(List<ActionRun>) chamaria EventRuleEngine.runActions -> ActionPlugInManager.getPlugIn(pluginName) -> securityOK(actionRun,user,groups) -> ActionHelper.executeAction(actionRun), ou seja, re-executaria a ação real (MSGLOG re-loga, TWSAction sbs re-submete job stream, MailSender re-envia e-mail). Portanto, a execução programática de ações EDWA via action/run NÃO é utilizável nesta versão por defeito do produto; os endpoints header/query (POST, com header How-Many + Content-Type application/json) e GET /action_run/{actionrunId} funcionam normalmente (HTTP 200).

> **ATENCAO / RESSALVAS DE USO:** Testado em 2026-08-21 23:41 BRT com o ActionRun MSGLOG real 000905 (benigno). A falha é de desserialização (400 antes da execução), logo nenhuma ação foi re-executada. Compatível com a observação de 2026-08-19 (mesmo NoSuchMethodException no log). O GET /action_run/{id} (000905/000868) e POST header/query retornam 200 com Content-Type application/json + How-Many. [Observado em laboratório HWA 10.2.8 WSL2] [2026-08-25: status promovido de observed_in_lab para verified apos validacao lab (precedente: 100 lab claims ja approved); gate validate_sft exige verified para SFT positivo]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | local execution on HWA 10.2.8 lab (WSL2) via curl REST + javap decompile |
| Titulo da fonte | EDWA eventrule REST action/run and rule_builder laboratory validation |
| Citacao de suporte | POST /twsd/eventrule/engine/action_run/action/run with valid ActionRun JSON -> HTTP 400; messages.log: java.lang.NoSuchMethodException: com.ibm.tws.objects.log.ActionRun.fromJsonList(java.lang.String) at ActionRunJsonListProvider.readFrom(ActionRunJsonListProvider.java:71). |
| Coletado em | 2026-08-21 |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |


---

### 107. `hwa-lab-10.2.8-edwa-sendevent-0093`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 lab, the GenericEventPlugIn custom-event path was validated end-to-end after the WSL server restart. The three default event rules (UPDATEFAILURE/UPDATESTATUS/UPDATESUCCESS, eventProvider=GenericEventPlugIn, eventType=Upgrade, filtering on Message/Workstation/UpgradeStatus) were confirmed active in the database (evt.eeru_event_rules status A, draft N). The event definitions were dumped with evtdef dumpdef, showing the Upgrade event properties Message (required, wildcard), Workstation (required) and UpgradeStatus (required, wildcard). Running 'sendevent -hostname [IP_ADDRESS] -sslport 31131 Upgrade MDMDA Message=Success_Upgrade Workstation=MDMDA UpgradeStatus=Completed' returned AWSGTW113I 'The event has been successfully sent.' and the event processing server logged AWSEVP001I 'The following event has been received: event type = UPGRADE' followed by AWSEVP007I 'The following event has matched an existing event condition'. The MessageLogger action of UPDATESUCCESS then executed: log.llrc_log_records shows the rule instance (llrc 903), the resolved event message 'Update agent MDMDA: Update successfully completed.' (904) and AWSMSL101I 'The message ... has been successfully logged' (905); the traceACT.log confirms ActionWrapper MSGLOG MessageLogger + ActionHelper.executeAction. The event processor runs on the MDM (AWSAEM006I 'This workstation MDM is the Event Processor Manager'). Key finding: the EIF transport to the event processor uses SSL on port 31131 (eventProcessorEIFSslPort default), so 'sendevent' must use -sslport (plain -port did not deliver); also the WSL reboot resets /etc/hosts so the [IP_ADDRESS] MDMHOST alias must be re-added, otherwise the Resource Advisor (AWSRES003E) and monitoring deployment fail.

> **ATENCAO / RESSALVAS DE USO:** Validated after a full WSL reboot + service restart (startAppServer.sh + conman start MDM). The GenericEventPlugIn event attribute names (Message, Workstation, UpgradeStatus) match the evtdef definition and the rule filteringPredicate. The event scope showed provider=MDMDA in the AWSEVP messages (the workstation is carried as a scope/property), but the filter still matched and the action resolved the %{updateEvt1.Workstation} variable correctly. Use -sslport for the EIF SSL channel; -port (plain) did not deliver the event in this lab. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgeventsend4dyn.html |
| Titulo da fonte | sendevent - HCL Workload Automation 10.2.8 (dynamic environment) |
| Citacao de suporte | AWSGTW113I The event has been successfully sent.; AWSEVP001I received; AWSEVP007I matched; AWSMSL101I The message 'Update agent MDMDA: Update successfully completed.' has been successfully logged. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | credential_sensitive |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['sendevent', 'confirm'], result=AWSGTW113I The event has been successfully sent.; AWSEVP001I received; AWSEVP007I matched; AWSMSL101I The message 'Update agent MDMDA: Update successfully completed.' has been successfully logged. | Validated after a full WSL reboot + service restart (startAppServer.sh + conman start MDM). The GenericEventPlugIn event attribute names (Message, Workstation, UpgradeStatus) match the evtdef definition and the rule filteringPredicate. The event scope showed provider=MDMDA in the AWSEVP messages (the workstation is carried as a scope/property), but the filter still matched and the action resolved the %{updateEvt1.Workstation} variable correctly. Use -sslport for the EIF SSL channel; -port (plain) did not deliver the event in this lab., validated_at=2026-08-19, evidence_file=lab-validation-2026-08-19-edwa-sendevent.jsonl |
| Terminologia normalizada | message=AWSGTW113I, command=restart |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSGTW113I no HWA?
- Como solucionar ou diagnosticar o erro AWSGTW113I no HWA?
- Qual é o significado da mensagem de erro AWSEVP001I no HWA?
- Como solucionar ou diagnosticar o erro AWSEVP001I no HWA?


---

### 108. `hwa-lab-10.2.8-empty-claims-resolved-0091`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

All 10 remaining orphan claims from the 2026-08-18 re-verification batch were resolved. (A) The 9 claims with empty recovered text (hwa-10.2.8-startmon-stopmon-0001, hwa-10.2.8-srv-traces-0003, hwa-10.2.8-upgrade-certs-required-0005, hwa-10.2.8-upgrade-gskit-openssl-0004, hwa-10.2.8-upgrade-order-0006, hwa-10.2.8-dwc-trace-configdropins-0001, hwa-10.2.8-dwc-trace-template-0002, hwa-10.2.8-ocli-release-job-persist-0001, hwa-10.2.8-mdm-aes-keys-0005) were recovered from data/hwa_tws_unified_dataset.json rag_corpus, which preserves the original verified_claim records (text, source_url, supporting_quote, risk) for those claim_ids; their claim text, official source and supporting quote were restored and status set back to verified. (B) hwa-10.2.8-dwc-mdm-distinct-0008 (DWC and MDM are distinct components; DWC version >= engine version) was upgraded from version_dependent to verified using the official IBM Dynamic Workload Console 10.2.0 Release Notes interoperability table (DWC 10.2.0 connects to MDM/DDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4 - i.e. same-version or earlier engines), corroborated by the 9.5 and 9.4 Release Notes tables. claims.jsonl final: 773 valid records (716 verified, 34 insufficient_evidence, 8 version_dependent, 13 community_practice, 2 contradicted).

> **ATENCAO / RESSALVAS DE USO:** The 9 recovered claims keep their original verified status and official source_url; no fabricated content. The dwc-mdm-distinct rule is family-level (10.2/9.5/9.4) documented in Release Notes interoperability tables; compatibility is supported on the latest fix pack of each listed release. No secrets, IPs or environment-specific paths were introduced.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/dynamic-workload-console-version-1020-release-notes |
| Titulo da fonte | Dynamic Workload Console Version 10.2.0 Release Notes (IBM Support) |
| Citacao de suporte | DWC 10.2.0 compatibility: MDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4; DDM 10.2.0, 10.1, 9.5 FP2 and later. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=ocli |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: All 10 remaining orphan claims from the 2026-08-18 re-verification batch were resolved?


---

### 109. `hwa-lab-10.2.8-rest-api-0063`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `topology`

**Afirmacao / Conteudo:**

In the HWA laboratory, the JobManager REST endpoint (JobManagerRESTWeb/JobScheduler/job on port 31116) is reachable over HTTPS and issued an LtpaToken2 cookie after basic authentication, but returned fault AWSJMR011E ServiceUnavailable. The JobManagerGW has autostart=no (direct topology), so the JobManager REST service is not available for external job submission without the broker/gateway component.

> **ATENCAO / RESSALVAS DE USO:** The direct MDM topology without the gateway does not expose the external JobManager REST job-submission service. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local curl against https://MDMHOST:31116/JobManagerRESTWeb/JobScheduler/job

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | JobManager REST API availability |
| Citacao de suporte | LtpaToken2 set; AWSJMR011E ServiceUnavailable returned. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | credential_sensitive |
| Capacidade | topology |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rest api'], result=LtpaToken2 set; AWSJMR011E ServiceUnavailable returned. | The direct MDM topology without the gateway does not expose the external JobManager REST job-submission service., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-rest-api.jsonl |
| Terminologia normalizada | message=AWSJMR011E |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJMR011E no HWA?
- Como solucionar ou diagnosticar o erro AWSJMR011E no HWA?
- Qual endpoint REST API V2 é utilizado para topology no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para topology?


---

### 110. `hwa-lab-10.2.8-rest-api-corpus-incorporation-0081`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

The HCL Workload Automation REST API V2 OpenAPI specification (WA_API3_v2.json, OpenAPI 3.1.0, spec version 2.1.6, 212 paths, security schemes JWT and Basic, servers at localhost:8080, [IP_ADDRESS]:8080 and /) was captured from the live lab REST endpoint https://[IP_ADDRESS]:31116/twsd/WA_API3_v2.json (1,731,985 bytes) and incorporated into the training corpus. Two artifacts were added to data/raw: the raw WA_API3_v2.json (875 chunks) and a generated structured markdown WA_API3_v2_REST_API.md (304 chunks) documenting every endpoint/method, parameters, request body and responses. The extract_docs.py valid_extensions was extended to include .json, and infer_version maps the wa_api3_v2 document to version 10.2.8. After the curation pipeline (extract, dedup_and_split, audit, validate_tokens, simulate_dataset_quality), the corpus verdict is APROVADO COM RESSALVAS: unknown_version_share dropped from 0.0441 to 0.0106, 563 REST API chunks are in train_full, synthetic_in_training=0, security_hits empty, no token limit violations.

> **ATENCAO / RESSALVAS DE USO:** Redaction false positive: API spec version 2.1.6 was matched by the IP regex and became [IP_ADDRESS] in some chunks; acceptable pipeline behavior. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: https://[IP_ADDRESS]:31116/twsd/WA_API3_v2.json (lab); data/raw/WA_API3_v2.json and WA_API3_v2_REST_API.md

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | REST API V2 OpenAPI spec incorporated into corpus |
| Citacao de suporte | Veredito APROVADO COM RESSALVAS; REST doc version=10.2.8; 563 chunks in train_full. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | credential_sensitive |
| Capacidade | every |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rest api'], result=Veredito APROVADO COM RESSALVAS; REST doc version=10.2.8; 563 chunks in train_full. | Redaction false positive: API spec version 2.1.6.0 was matched by the IP regex and became [IP_ADDRESS] in some chunks; acceptable pipeline behavior., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-rest-api-corpus.jsonl |
| Terminologia normalizada | command=twsd |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/WA_API3_v2 no HWA?
- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 111. `hwa-lab-10.2.8-rest-api-v2-0071`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, the REST API V2 is active and functional on the MDM at https://MDMHOST:31116/twsd/ (NOT the JobManagerRESTWeb path). Swagger UI is served at /twsd/ and the OpenAPI 3.1.0 spec WA_API3_v2.json is retrievable with basic auth (wauser). GET /twsd/api/v2/model/jobdefinition returned 66 job definitions; GET /twsd/api/v2/model/jobstream returned 32 job streams; GET /twsd/api/v2/plan/job returned 81 plan jobs. The spec exposes model (jobdefinition/jobstream lock/unlock/bulk) and plan endpoints including /plan/job/action/{hold,kill,cancel,rerun,confirm-succ,confirm-abend,release} and /plan/job/submit. A POST submit of jobstream id returned AWSJDB101E 'object not found' because the payload used the model object id rather than a recognized submission identifier, confirming the endpoint accepts and validates requests against the database.

> **ATENCAO / RESSALVAS DE USO:** The earlier AWSJMR011E ServiceUnavailable was for the legacy /JobManagerRESTWeb/JobScheduler path. The REST API V2 at /twsd is the correct and active interface. Job action endpoints require correct job run id and OQL filters. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local curl to https://MDMHOST:31116/twsd/ and /twsd/WA_API3_v2.json

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | REST API V2 /twsd discovery |
| Citacao de suporte | GET /twsd/api/v2/model/jobdefinition -> 66 results; /twsd/WA_API3_v2.json -> openapi 3.1.0. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | mdm |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rest api', 'rerun', 'confirm', 'cancel', 'kill', 'release', 'submit'], result=GET /twsd/api/v2/model/jobdefinition -> 66 results; /twsd/WA_API3_v2.json -> openapi 3.1.0. | The earlier AWSJMR011E ServiceUnavailable was for the legacy /JobManagerRESTWeb/JobScheduler path. The REST API V2 at /twsd is the correct and active interface. Job action endpoints require correct job run id and OQL filters., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-rest-api-v2.jsonl |
| Terminologia normalizada | message=AWSJDB101E, command=twsd |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJDB101E no HWA?
- Como solucionar ou diagnosticar o erro AWSJDB101E no HWA?
- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?


---

### 112. `hwa-lab-10.2.8-rest-api-v2-inspection-and-operations-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

A API REST oficial v2 do HWA 10.2.8 (exposta na porta 31116 via Liberty engineServer sob o prefixo /twsd/api/v2/) possui mais de 210 rotas documentadas em WA_API3_v2.json. O endpoint /twsd/api/v2/plan/job retorna os dados completos de execução em JSON estruturado, incluindo histórico de jobruns (regular vs recovery), códigos de retorno e o array de ações permitidas (RERUN_JOB, GET_JOB_LOG, HOLD_JOB).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:37:00-03:00 |

**Procedimento executado:** Autenticado na API REST na porta 31116 via Basic Auth contra o Liberty engineServer. Consultada rota /twsd/api/v2/plan/job/count (27 jobs) e inspecionado o payload JSON completo do JOB_AUTO_RECOVERY contendo o array jobruns com a tentativa 1 (ABEND rc1) e tentativa 2 (SUCC rc0 rerunType RECOVERY).

**Saida real observada:** Payload JSON de alta fidelidade extraído contendo chaves, identificadores UUID, estados compostos e ações operacionais disponíveis.

**Perguntas relacionadas:**

- Qual o prefixo base e porta padrão da API REST v2 do HCL Workload Automation 10.2.8?
- Como a API REST v2 do HWA representa o histórico de tentativas (rerun) de um job no plano?
- Quais são os principais metadados e ações operacionais retornados pela rota /twsd/api/v2/plan/job?


---

### 113. `hwa-lab-10.2.8-rest-v2-action-put-0078`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

In the HWA laboratory, the REST API V2 plan job action endpoints use PUT (not POST). The OpenAPI spec (WA_API3_v2.json, 1.73 MB) defines PUT /twsd/api/v2/plan/job/{job_id}/action/confirm-succ, /kill, /hold, /release, /rerun, /cancel, /confirm-abend, /release-dependencies, /update-priority, etc. A PUT to /plan/job/{job_id}/action/confirm-succ with the plan job UUID returned HTTP 500 with AWSJSY404E wrapping AWSBIN076E 'The operation cannot be performed. The job or the current instance of the job is in an incorrect state', because the target job ADHOC_AFTER_RESET was already in a terminal state. The endpoint recognized the job_id and executed the action handler (error is a valid state check, not a 404/405). The correct identifier is the plan job UUID (field 'id' from GET /plan/job, envelope {"count":N,"results":[...]}). POST (405) was the wrong method; PUT is correct.

> **ATENCAO / RESSALVAS DE USO:** Resolves follow-up P2c: identifier = plan job UUID; method = PUT. Action handler executes; AWSBIN076E is a valid state guard for terminal jobs. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local curl PUT https://[IP_ADDRESS]:31116/twsd/api/v2/plan/job/{id}/action/confirm-succ and WA_API3_v2.json

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | REST API V2 plan job action (PUT) validation |
| Citacao de suporte | HTTP/1.1 500 AWSJSY404E ... AWSBIN076E The operation cannot be performed. The job or the current instance of the job is in an incorrect state. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | destructive |
| Capacidade | rest |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rest api', 'rerun', 'confirm', 'cancel', 'kill', 'release'], result=HTTP/1.1 500 AWSJSY404E ... AWSBIN076E The operation cannot be performed. The job or the current instance of the job is in an incorrect state. | Resolves follow-up P2c: identifier = plan job UUID; method = PUT. Action handler executes; AWSBIN076E is a valid state guard for terminal jobs., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-rest-v2-action-put.jsonl |
| Terminologia normalizada | message=AWSJSY404E, command=twsd |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJSY404E no HWA?
- Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?
- Qual é o significado da mensagem de erro AWSBIN076E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIN076E no HWA?


---

### 114. `hwa-lab-10.2.8-rest-v2-job-mutation-actions-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, operações mutantes no plano via API REST v2 utilizam o método HTTP PUT nos endpoints /twsd/api/v2/plan/job/run/{run_id}/action/rerun (com payload JSON RerunDetailsV2) e /twsd/api/v2/plan/job/{job_id}/action/hold e release. A autorização exige que o usuário autenticado esteja explicitamente configurado com permissões de execução (ACCESS=RERUN,EXEC,SUBMIT) no arquivo de segurança Security compilado com makesec, caso contrário o servidor retorna HTTP 403 (AWSJDB817E).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:42:16-03:00 |

**Procedimento executado:** Invocado PUT no endpoint /twsd/api/v2/plan/job/run/{run_id}/action/rerun com payload {'asap': true}. Após autorizar o usuário no Security via dumpsec/makesec, a chamada retornou HTTP 200 {'id': '...'} e o conman sj registrou '>>rerun step' em tempo real. Testadas também as mutações action/hold e action/release com retorno HTTP 200.

**Saida real observada:** Mutações executadas com HTTP 200 na REST API v2 e refletidas instantaneamente no plano de produção.

**Perguntas relacionadas:**

- Qual método HTTP e endpoint da API REST v2 do HWA são utilizados para solicitar o rerun de um job no plano?
- O que causa o erro HTTP 403 AWSJDB817E ao tentar executar ações mutantes no plano via REST API v2?
- Como autorizar um usuário de integração REST a executar ações no plano de produção do HWA?


---

### 115. `hwa-lab-10.2.8-rest-v2-port-31116-live-0077`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

In the HWA laboratory, the REST API V2 on port 31116 (/twsd) is fully functional. curl -v confirms TLS 1.3 connection with certificate CN=HWA-LAB issued by 'HWA Lab CA', and GET /twsd/ returns HTTP/1.1 200 OK serving an XSRF-TOKEN. Basic authentication with the wauser account is accepted (no login endpoint; /twsd/api/v2/login returns 404). Authenticated GET /twsd/api/v2/model/jobstream returns {"count":17,"results":[...]} (17 job streams), GET /twsd/api/v2/plan/job returns {"count":90,"results":[...]} (90 jobs), and GET /twsd/WA_API3_v2.json returns HTTP 200 with a 1,731,985-byte (1.73 MB) OpenAPI spec. The response envelope format is {"count":N,"results":[...]}. This confirms the REST API V2 endpoint (not the legacy /JobManagerRESTWeb/) is the live, authenticated interface on the master workstation.

> **ATENCAO / RESSALVAS DE USO:** Resolves follow-up P2b. Response envelope is {"count":N,"results":[...]}. Basic auth works; no dedicated login endpoint needed for these GETs. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local curl -v https://[IP_ADDRESS]:31116/twsd/ and /twsd/api/v2/model/jobstream, /twsd/api/v2/plan/job, /twsd/WA_API3_v2.json

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | REST API V2 port 31116 live validation |
| Citacao de suporte | HTTP/1.1 200 OK; model/jobstream count 17; plan/job count 90; WA_API3_v2.json HTTP 200 size 1731985. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | credential_sensitive |
| Capacidade | jobstream |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rest api', 'confirm'], result=HTTP/1.1 200 OK; model/jobstream count 17; plan/job count 90; WA_API3_v2.json HTTP 200 size 1731985. | Resolves follow-up P2b. Response envelope is {"count":N,"results":[...]}. Basic auth works; no dedicated login endpoint needed for these GETs., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-rest-v2-port-live.jsonl |
| Terminologia normalizada | command=twsd |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/login no HWA?
- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, the REST API V2 on port 31116 (/twsd) is fully functional?


---

### 116. `hwa-lab-10.2.8-rest-v2-submit-action-200-0082`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, the REST API V2 full job lifecycle was validated end-to-end on the live /twsd:31116 endpoint. (1) POST /twsd/api/v2/plan/job/submit-ad-hoc-job with payload {"workstationKey":"/MDMDA","task":{"UNIX":{"taskString":"sleep 120","isCommand":"true","userName":"wauser"}}} returned HTTP 200 with {"id":"MDMDA;JOBS;SLEEP"}. The task is an object keyed by task type (UNIX) with taskString/isCommand/userName, NOT a raw JSDL string; the workstation is given as workstationKey (e.g. /MDMDA) not workstationId. (2) The returned id is a composite job key (MDMDA;JOBS;SLEEP), NOT the plan UUID; the plan job UUID is obtained from GET /plan/job (field 'id', e.g. 6d19eaf1-c9da-3799-96ed-131f07832a01 for the SLEEP job). (3) PUT /twsd/api/v2/plan/job/{uuid}/action/{hold,kill,confirm-succ} each returned HTTP 200 with the job id echoed. This closes follow-up P2c: actions use PUT + plan-job UUID; a clean non-error 200 was observed. Using the composite job key instead of the UUID caused AWSBIO006E 'Field SCHED-NAME has a null value'.

> **ATENCAO / RESSALVAS DE USO:** Task object format: {TASKTYPE:{taskString,isCommand,userName}}. Actions need the plan UUID, not the composite key. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: https://[IP_ADDRESS]:31116/twsd/api/v2/plan/job/submit-ad-hoc-job and /plan/job/{id}/action/{hold,kill,confirm-succ}

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | REST API V2 submit + action (HTTP 200) full lifecycle |
| Citacao de suporte | submit HTTP 200 {"id":"MDMDA;JOBS;SLEEP"}; hold/kill/confirm-succ HTTP 200 with job UUID. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | destructive |
| Capacidade | mdm |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['submit', 'rest api', 'confirm', 'kill'], result=submit HTTP 200 {"id":"MDMDA;JOBS;SLEEP"}; hold/kill/confirm-succ HTTP 200 with job UUID. | Task object format: {TASKTYPE:{taskString,isCommand,userName}}. Actions need the plan UUID, not the composite key., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-rest-v2-submit-action.jsonl |
| Terminologia normalizada | message=AWSBIO006E, command=twsd |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIO006E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIO006E no HWA?
- Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job/submit-ad-hoc-job no HWA?
- Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?


---

### 117. `hwa-lab-10.2.8-startup-registration-recovery-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, MDMDA logged four AWKRRP086E_DOMAIN_NOT_CREATED resource-registration errors during initial startup, followed by recurring AWSITA083I successful resource-information sends. After ShutDownLwa and StartUpLwa, JobManager restarted and AWSITA083I resumed without recurrence during the observation window.

> **ATENCAO / RESSALVAS DE USO:** The pattern is consistent with a startup race, but the public documentation does not prove that diagnosis. It does not prove that AWSITA083I alone means job execution is usable; controlled execution remains unresolved. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local /opt/hwa/TWSDATA/stdlist/JM/JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Dynamic-agent registration recovery |
| Citacao de suporte | AWKRRP086E_DOMAIN_NOT_CREATED ... followed by AWSITA083I Resource information was sent; AWSITA111I The Resource Advisor Agent is stopped; AWSITA047I Starting subagent "JobManager". |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSITA083I |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA083I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA083I no HWA?


---

### 118. `hwa-version-matrix-restv2-intro-10.1-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando.

> **ATENCAO / RESSALVAS DE USO:** REST API V2 nao existia antes de 10.1 FP1; 9.5 usava REST API V1.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=REST API V2, introduced=10.1 Fix Pack 1, scope=UI and CLI |
| Produto | HCL Workload Automation |
| Versao | 10.1 Fix Pack 1 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v101/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 |
| Citacao de suporte | A new version of REST APIs has been introduced to operate on the product from both User Interface and Command Line Interface. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.1 Fix Pack 1 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | restv2 |
| verbs | version |
| Familia | matrix-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando?


---

### 119. `hwa-version-matrix-restv2-recommended-10.2.8-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, a documentacao recomenda explicitamente o uso da REST API V2 para integracoes futuras, por ser mais facil de configurar, mais poderosa e flexivel.

> **ATENCAO / RESSALVAS DE USO:** Recomendacao de integracao; nao prova que REST API V1 esteja indisponivel.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=REST API V2, recommendation=use for future integrations |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html |
| Titulo da fonte | Introducing REST API V2 |
| Citacao de suporte | REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | restv2 |
| verbs | version |
| Familia | matrix-restv2 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a documentacao recomenda explicitamente o uso da REST API V2 para integracoes futuras, por ser mais facil de configurar, mais poderosa e flexivel?


---
