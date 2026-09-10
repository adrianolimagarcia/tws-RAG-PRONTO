# API REST V2 & INTEGRACAO

> Total de tópicos canônicos cobertos nesta seção: 113

---

### 1. com-sla-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Uma prática recomendada para recuperação de desastres é definir RTO (tempo alvo de recuperação) e RPO (perda de dados tolerável) para o ambiente HWA, usando como base as capacidades documentadas de backup/restauração (backup MDM com banco espelhado, cópia de arquivos de configuração e chaves AES TWA_DATA_DIR/ssl/aes). RTO/RPO são metas organizacionais, não valores prescritos pela HCL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada para recuperação de desastres é definir RTO (tempo alvo de recuperação) e RPO (perda de dados tolerável) para o ambiente HWA, usando como base as capacidades documentadas de backup/restauração (backup MDM com banco espelhado, cópia de arquivos de configuração e chaves AES TWA_DATA_DIR/ssl/aes)?*

---

### 2. hwa-10.1-real-oql-intro-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 introduziu o Orchestration Query Language (OQL) como sintaxe de consulta mais simples que permite ordenar resultados sem necessidade de explicitos parametros de ordenacao na URL; OQL usa sintaxe de pontos para ordenacao (ex.: sort=field asc). Nao existe OQL na REST API V1 da 9.5.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 introduziu o Orchestration Query Language (OQL) como sintaxe de consulta mais simples que permite ordenar resultados sem necessidade de explicitos parametros de ordenacao na URL; OQL usa sintaxe de pontos para ordenacao (ex?*

---

### 3. hwa-10.1-real-restv2-intro-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando; a V2 substitui/complementa a V1 presente em 9.5. Endpoints e autenticacao JWT da V2 sao distintos da V1.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando; a V2 substitui/complementa a V1 presente em 9.5. Endpoints e autenticacao JWT da V2 sao distintos da V1.?*

---

### 4. hwa-10.2.8-agent-auth-combinations-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed agents) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: REST API V2 (HTTPS Port 31116) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Na instalação de agentes HWA 10.2.8, apikey é mutuamente exclusivo com wauser, wapassword, sslkeysfolder e sslpassword e requer tdwbhostname e tdwbport; jwt true também requer autenticação via apikey ou wauser/wapassword e os parâmetros do broker.

**Plataforma / Validação:** Distributed agents

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 5. hwa-10.2.8-agent-ssl-folder-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed agents) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Na instalação de agentes HWA 10.2.8, sslkeysfolder deve apontar para uma pasta PEM contendo ca.crt, tls.key e tls.crt; additionalCAs pode conter CAs intermediárias ou confiáveis, e sslkeysfolder/sslpassword são mutuamente exclusivos com wauser, wapassword, apikey e jwt true.

**Plataforma / Validação:** Distributed agents

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na instalação de agentes HWA 10.2.8, sslkeysfolder deve apontar para uma pasta PEM contendo ca?*

---

### 6. hwa-10.2.8-aida-install-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: aida > installation [aida_install]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a instalacao do AI Data Advisor via Docker usa o script AIDA.sh (requer CONTAINER_RUNTIME=docker|podman) com os comandos: load (carrega as 9 imagens do pacote offline), build-start (builda es/keycloak e sobe todos os containers), first-start (configuracao guiada opcional), add-credentials/update-credentials/delete-credentials (gerencia credenciais do engine no OpenSearch), set-custom-port (padrao 9432), start/stop/restart/down/down-volumes. O docker-compose.yml define 11 servicos (config, keycloak, nginx, ui, exporter, ad, email, orchestrator, predictor, redis, es). O OpenSearch (2.19.6, construido via Dockerfile-es sobre ubi9) e o Keycloak (26.6.4, via Dockerfile-keycloak) NAO vem no tar de imagens: sao buildados com download da internet (artifacts.opensearch.org, quay.io).

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 7. hwa-10.2.8-aida-metrics-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: aida > metrics [aida_monitoring]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o fluxo de dados do AI Data Advisor e: (1) o aida-exporter autentica no servidor WA (credenciais do OpenSearch) e consulta os endpoints REST V2 de metricas (GET /metrics sem auth, GET /twsd/engine/historical_metric/metadata e /record, GET /twsd/engine/definition/{alert,kpi,aida_catalog} com auth basic); (2) processa KPI definitions e grava metricas no OpenSearch (indice metric-index-<data>, alert-definitions, kpis-definition); (3) o aida-orchestrator agenda predicoes (aida-predictor, modelo prophet/neural) e deteccao de alertas (aida-ad); (4) os alertas aparecem no Workload Dashboard do DWC e podem ser enviados por email (aida-email, SMTP configurado no common.env). Parametros chave: METRICS_FETCH_INTERVAL=240s (o /metrics expira apos ~10min sem poll), EXPORTER_EXECUTION_INTERVAL=86400s, PROPHET_ORCHESTRATOR={"schedule":1440,"schedule_alert":15} (min entre predicao e deteccao), DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180, RESOLVE_ALERTS_AFTER_DAYS=1.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 8. hwa-10.2.8-aida-rest-api-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: aida > api [aida_api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor expoe uma API REST interna (sob /api, documentada em /api/swagger com spec OpenAPI 3.0) com 23 endpoints em 6 grupos: KPIs (POST /kpi, POST /kpi/list, GET /kpi/category/list, PUT /kpi/updateAll), Alerts (POST /alert/definition/list, POST /alert/definition, PUT /alert/definition/update, PUT /alert/definition/updateAll, POST /alert/instance, POST /alert/instance/list, PUT /alert/instance/update), Metrics (POST /metric/instance/list), Special Days (POST /special-day/list, PUT /special-day/add, PUT /special-day/update, DELETE /special-day/delete, POST /special-day/holidays, GET /special-day/holidays/list), Actions (GET /actions/retrain, GET /actions/retrain/retrain-details, GET /actions/retrain/last-retrain) e JWT (POST /jwt, GET /jwt/create-session). A autenticacao usa Keycloak (realm aida, client publico 'nginx', usuarios default aidaadmin com role aida-admin e aidauser): o nginx valida o Bearer JWT via discovery/introspection contra o Keycloak; o token e obtido por password grant em https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token. Schemas: SpecialDay, KPI, AlertDefinition, AlertInstance, MetricInstance, MetricDefinition, MetricProperties, MetricPropertiesInstance.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para api no HWA?*

---

### 9. hwa-10.2.8-aida-zos-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: aida > platforms [aida_platforms]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, ha diferencas entre o AI Data Advisor em Distributed vs z/OS: (1) registro de engine - Distributed requer Engine host + Engine port (default 9443); z/OS requer DWC host + DWC port + Remote server name; (2) ambos suportam autenticacao por Credentials (usuario+senha) ou API Keys; (3) tanto HCL Workload Automation quanto HCL Workload Automation for Z expoem metricas e KPI definitions segundo o padrao OpenMetrics (com endpoints distintos: /metrics e /twsd/engine/historical_metric/* para Distributed, /twsz/v1/aida/* para z/OS conforme ENDPOINTS_Z_CONF do common.env); (4) o modelo de ML do predictor suporta neural para Distributed e apenas Prophet para AIDA em z/OS Linux; (5) sem Keycloak, a autenticacao usa as roles do Dynamic Workload Console em ambos; com Keycloak, aplica-se ao deployment Docker em ambos.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 10. hwa-10.2.8-apikey-api-key-auth-upgrade-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
Ao atualizar de v10.x.x ou v9.5.x para 10.2.x, é necessário habilitar a autenticação por API Key: exportar o certificado público do servidor do keystore TWSServerKeyFile.p12 e importá-lo no truststore TWSServerTrustFile.p12 com o alias mpjwtkey, além de ajustar a variável mp.jwt.trust.key no arquivo jwt_variables.xml.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Ao atualizar de v10.x?*

---

### 11. hwa-10.2.8-centralized-agent-update-behavior-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
During centralized agent update, currently running jobs continue execution, new jobs do not start, and the agent restarts upon completion.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: During centralized agent update, currently running jobs continue execution, new jobs do not start, and the agent restarts upon completion?*

---

### 12. hwa-10.2.8-dwc-api-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/model [rest/model]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para colocar uma job stream em modo draft via REST API V2 é necessário recuperar o ID e o payload atual da job stream com GET /twsd/api/v2/model/jobstream e enviar o payload atualizado com PUT /twsd/api/v2/model/jobstream/{jobStream_id}, incluindo o parâmetro 'draft' na lista options; a operação é mutating, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*

---

### 13. hwa-10.2.8-dwc-api-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/fence [rest/fence]]`

**Regra Canônica / Evidência:**
O endpoint POST /twsd/api/v2/plan/workstation/action/update-fence é documentado no HCL Workload Automation 10.2.8 para alterar o valor do fence de uma workstation no plano atual; jobs não são iniciados em uma workstation se suas prioridades forem menores ou iguais ao valor do fence, sendo uma operação mutating, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/workstation/action/update-fence no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/plan/workstation/action/update-fence é documentado no HCL Workload Automation 10.2.8 para alterar o valor do fence de uma workstation no plano atual; jobs não são iniciados em uma workstation se suas prioridades forem menores ou iguais ao valor do fence, sendo uma operação mutating, conforme documentação oficial?*

---

### 14. hwa-10.2.8-dwc-api-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job com dependência no plano atual via REST API V2 consiste em obter o ID do job sucessor com GET /twsd/api/v2/model/jobdefinition e os dados do job predecessor com GET /twsd/api/v2/plan/job e então adicionar a dependência com POST /twsd/api/v2/plan/job/{job_id}/action/add-dependencies (corpo com array dependencies contendo dependencyType e jobId do predecessor); operação mutating, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job com dependência no plano atual via REST API V2 consiste em obter o ID do job sucessor com GET /twsd/api/v2/model/jobdefinition e os dados do job predecessor com GET /twsd/api/v2/plan/job e então adicionar a dependência com POST /twsd/api/v2/plan/job/{job_id}/action/add-dependencies (corpo com array dependencies contendo dependencyType e jobId do predecessor); operação mutating, conforme documentação oficial?*

---

### 15. hwa-10.2.8-dwc-api-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream no plano via REST API V2 consiste em consultar GET /twsd/api/v2/plan/jobstream e inspecionar o array dependencies da resposta (que contém os IDs de todos os jobs e job streams predecessores) e então obter os detalhes de cada predecessor com GET /twsd/api/v2/plan/job/{job_id} e GET /twsd/api/v2/plan/jobstream/{jobstream_id}; operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream no plano via REST API V2 consiste em consultar GET /twsd/api/v2/plan/jobstream e inspecionar o array dependencies da resposta (que contém os IDs de todos os jobs e job streams predecessores) e então obter os detalhes de cada predecessor com GET /twsd/api/v2/plan/job/{job_id} e GET /twsd/api/v2/plan/jobstream/{jobstream_id}; operação de leitura, conforme documentação oficial?*

---

### 16. hwa-10.2.8-dwc-api-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os sucessores de uma job stream no plano via REST API V2 consiste em obter o ID da job stream com GET /twsd/api/v2/plan/jobstream e consultar GET /twsd/api/v2/plan/job e GET /twsd/api/v2/plan/jobstream com o filtro OQL 'dependencies.jobStreamId = <id da job stream>' para listar os jobs e job streams que dependem dela; operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os sucessores de uma job stream no plano via REST API V2 consiste em obter o ID da job stream com GET /twsd/api/v2/plan/jobstream e consultar GET /twsd/api/v2/plan/job e GET /twsd/api/v2/plan/jobstream com o filtro OQL 'dependencies?*

---

### 17. hwa-10.2.8-dwc-api-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para listar e gerenciar dependências de uma job stream no plano via REST API V2 utiliza GET /twsd/api/v2/plan/jobstream para obter o ID e o array dependencies da job stream e os endpoints PUT /twsd/api/v2/plan/jobstream/{jobStream_id}/action/release-all-dependencies (sem corpo de requisição), release-dependencies e remove-dependencies (corpo com array dependencies a liberar/remover); operações mutating, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?*

---

### 18. hwa-10.2.8-dwc-api-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/model [rest/model]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para recuperar os predecessores de uma job stream a partir da base de dados via REST API V2 consiste em consultar GET /twsd/api/v2/model/jobstream e inspecionar os arrays de dependências da definição (externalPredecessors, promptDependencies, fileDependencies, resourceDependencies) e então obter as definições completas de cada predecessor com GET /twsd/api/v2/model/jobdefinition/{job_abstract_id} e GET /twsd/api/v2/model/jobstream/{jobstream_abstract_id}; operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*

---

### 19. hwa-10.2.8-dwc-api-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/model [rest/model]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para criar uma nova job definition na base de dados via REST API V2 consiste em preparar um payload JSON com kind igual a 'JobDefinition' e o array def contendo folder, name, workstation, type e task (ex.: type UNIX com taskString, userName e isCommand), enviá-lo com POST /twsd/api/v2/model/jobdefinition e verificar a criação com GET /twsd/api/v2/model/jobdefinition; a resposta retorna o ID da nova definição.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para criar uma nova job definition na base de dados via REST API V2 consiste em preparar um payload JSON com kind igual a 'JobDefinition' e o array def contendo folder, name, workstation, type e task (ex?*

---

### 20. hwa-10.2.8-dwc-api-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: dwc_api > rest/model [rest/model]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para consultar uma job stream ou job definition via REST API V2 (GET /twsd/api/v2/model/jobstream e GET /twsd/api/v2/model/jobdefinition) existem dois métodos: model filters com sintaxe análoga à do composer (ex.: /@/@#/@/JS-API) e OQL com o preset 'Filter by exact name and matching folder', que gera a query name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC para filtrar pelo nome exato e pasta com ordenação decrescente.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar rest/model?*
- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*

---

### 21. hwa-10.2.8-dwc-api-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para submeter um job ad-hoc via REST API V2 usa o endpoint POST /twsd/api/v2/plan/job/submit-ad-hoc-job com corpo contendo task e workstationKey; o task pode ser simples (UNIX com taskString, isCommand e userName) ou executável (OTHER com taskString contendo XML JSDL jsdl:jobDefinition com jsdle:executable e jsdle:script), e a submissão é verificada com GET /twsd/api/v2/plan/job.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job/submit-ad-hoc-job no HWA?*
- *Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?*
- *Como submeter execuções pontuais via API REST V2 no HWA?*

---

### 22. hwa-10.2.8-dwc-api-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/model [rest/model]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a resposta do endpoint GET /twsd/api/v2/model/jobstream fornece o ID da job stream no cabeçalho da resposta (response header) e o payload JSON completo no corpo da resposta, itens necessários para as etapas seguintes do fluxo (ex.: atualização com PUT /twsd/api/v2/model/jobstream/{jobStream_id}).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a resposta do endpoint GET /twsd/api/v2/model/jobstream fornece o ID da job stream no cabeçalho da resposta (response header) e o payload JSON completo no corpo da resposta, itens necessários para as etapas seguintes do fluxo (ex?*

---

### 23. hwa-10.2.8-dwc-api-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest/plan [rest/plan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a resposta de GET /twsd/api/v2/plan/jobstream documenta o array dependencies com entradas tipadas pelo campo dependencyType, incluindo JOIN (com joinName, joinQuantity, members e criteria), EXTERNAL_JOBSTREAM (com jobStreamId e jobStreamName do predecessor), RESOURCE (com name, quantity e available) e PROMPT (com promptName, promptStatus e actions como REPLY_PROMPT); no plano, predecessores de tipo job aparecem como EXTERNAL_JOB com jobId e jobName.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?*

---

### 24. hwa-10.2.8-dwc-apikey-expiry-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > authentication [authentication]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as API Keys criadas no Dynamic Workload Console possuem expiracao padrao de 365 dias, configuravel pela propriedade com.ibm.tws.util.jwt.apikey.expiration.date. Apos gerada, a API Key e armazenada no arquivo config.yaml do usuario ($HOME/.OCLI/config.yaml no Linux).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as API Keys criadas no Dynamic Workload Console possuem expiracao padrao de 365 dias, configuravel pela propriedade com?*

---

### 25. hwa-10.2.8-dwc-apikey-oidc-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > authentication [authentication]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a geracao de API Keys requer um provedor de autenticacao/autorizacao que use o padrao aberto OpenID Connect. Na primeira conexao do Orchestration CLI, e necessario autenticar usando API Keys, que sao atualizadas automaticamente no arquivo config.yaml.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a geracao de API Keys requer um provedor de autenticacao/autorizacao que use o padrao aberto OpenID Connect?*

---

### 26. hwa-10.2.8-dwc-engine-connection-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a engine connection do Dynamic Workload Console pode ser criada via REST API interna do DWC (contexto /dwc/api, JAX-RS EngineApplication em /v1/): POST /dwc/api/v1/engine/create com JSON {name, type (TWS=distributed), hostname, port, remoteServerName, credentials {user, password}, showInDashboard, enableSSC, reporting} retorna 200 com 'created successfully'; a conexao e persistida em tdwc.tdwc_engineconnection (engine_id numerico gerado por identity), tdwc.tdwc_credential (senha criptografada) e tdwc.tdwc_preferenceable (preferencetype); a validacao de conectividade usa GET /dwc/api/v1/engine/{engine_id}/checkConnection (engine_id NUMERICO, nao o nome) que retorna {'successful': true} quando o engine responde na porta HTTPS.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /dwc/api no HWA?*

---

### 27. hwa-10.2.8-dwc-engine-connection-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 do engine (https://<host>:31116/twsd/) e servida pelo engineServer, que e o server Open Liberty do MDM instalado em ${HWA_INST_DIR}/usr/servers/engineServer, que no lab e /opt/hwa/usr/servers/engineServer (WLP_USER_DIR do MDM) iniciado por appservertools/startAppServer.sh como o usuario HWA; o Dynamic Workload Console valida a engine connection contra essa porta, portanto o engineServer precisa estar ativo (e o hostname do engine resolvido no /etc/hosts do host do DWC, ex.: localhost MDMHOST) para o checkConnection retornar sucesso.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para mdm no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 do engine (https://<host>:31116/twsd/) e servida pelo engineServer, que e o server Open Liberty do MDM instalado em ${HWA_INST_DIR}/usr/servers/engineServer, que no lab e /opt/hwa/usr/servers/engineServer (WLP_USER_DIR do MDM) iniciado por appservertools/startAppServer?*

---

### 28. hwa-10.2.8-dwc-engine-restart-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > engines [engines]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, operacoes de engine (start/stop/restart) podem ser executadas via REST API nos servicos de engines expostos em /twsd, complementando o appservman local.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para engines no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, operacoes de engine (start/stop/restart) podem ser executadas via REST API nos servicos de engines expostos em /twsd, complementando o appservman local?*

---

### 29. hwa-10.2.8-dwc-eventrule-rest-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > eventrules [eventrules]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as event rules podem ser administradas via REST API (servicos de event rules em /twsd), incluindo deployment e engine de regras, complementando o uso de sendevent e do Dynamic Workload Console.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para eventrules no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 30. hwa-10.2.8-dwc-restv2-filter-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 oferece filtragem aprimorada: e possivel usar planFilter (sintaxe similar ao conman) e/ou OQL, podendo combinar ambos usando planFilter para filtrar e OQL para ordenar, conforme a especificidade da consulta.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar restv2?*
- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*

---

### 31. hwa-10.2.8-dwc-restv2-https-tls-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o acesso a REST API e exclusivamente via HTTPS (porta 31116 por padrao), exigindo certificados TLS validos no master domain manager; o lab confirmou TLS 1.3 no endpoint /twsd.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o acesso a REST API e exclusivamente via HTTPS (porta 31116 por padrao), exigindo certificados TLS validos no master domain manager; o lab confirmou TLS 1.3 no endpoint /twsd?*

---

### 32. hwa-10.2.8-dwc-restv2-model-query-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 permite consultar job streams de modelo com filtros de modelo (ex.: /@/@#/@/JS-API) ou com OQL (ex.: name = 'JS-API' AND folder LIKE '/' ORDER BY name DESC), retornando os resultados no envelope padrao com count e results.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 permite consultar job streams de modelo com filtros de modelo (ex?*

---

### 33. hwa-10.2.8-dwc-restv2-multi-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 introduziu endpoints multi-item eficientes: cada acao pode ser executada por ID ou por filtro, permitindo operar sobre varios itens de uma vez.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 introduziu endpoints multi-item eficientes: cada acao pode ser executada por ID ou por filtro, permitindo operar sobre varios itens de uma vez?*

---

### 34. hwa-10.2.8-dwc-restv2-oql-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Object Query Language (OQL) e usado para monitorar o ambiente do production plan e se aplica a REST API V2 e ao Orchestration Monitor. Suporta keywords como AND, OR, IN, LIKE e ORDER BY, e os campos sao case-sensitive.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Object Query Language (OQL) e usado para monitorar o ambiente do production plan e se aplica a REST API V2 e ao Orchestration Monitor?*

---

### 35. hwa-10.2.8-dwc-restv2-payload-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 introduziu payloads melhorados para facilitar o consumo, com estrutura/hierarquia reformulada em relacao a V1.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 introduziu payloads melhorados para facilitar o consumo, com estrutura/hierarquia reformulada em relacao a V1.?*

---

### 36. hwa-10.2.8-dwc-restv2-recommended-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 e recomendada para qualquer integracao futura por ser mais facil de configurar, mais poderosa e flexivel que a V1. A API cobre administracao de engines, event rules, workload modelling, plans e security.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 37. hwa-10.2.8-dwc-restv2-services-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API (acessivel em /twsd) cobre servicos de administracao de engines, event rules, workload modelling, plans e security, permitindo operar o produto via UI e CLI de forma programatica.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 38. hwa-10.2.8-dwc-restv2-submit-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para submeter uma job stream via REST API V2 e necessario primeiro consultar o job stream de modelo com GET /twsd/api/v2/model/jobstream (usando model filters como /@/@#/@/JS-API ou OQL) e depois usar o id retornado no POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit. As respostas usam o envelope {"count":N,"results":[...]}.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para submeter uma job stream via REST API V2 e necessario primeiro consultar o job stream de modelo com GET /twsd/api/v2/model/jobstream (usando model filters como /@/@#/@/JS-API ou OQL) e depois usar o id retornado no POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit?*

---

### 39. hwa-10.2.8-dwc-restv2-swagger-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 expoe uma interface Swagger em https://MDM_IP_address:tdwbport/twsd/ com a opcao 'Try it out!', permitindo testar operacoes (List Operations) diretamente no navegador.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 expoe uma interface Swagger em https://MDM_IP_address:tdwbport/twsd/ com a opcao 'Try it out!', permitindo testar operacoes (List Operations) diretamente no navegador?*

---

### 40. hwa-10.2.8-dwc-restv2-url-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a REST API e acessada via HTTPS na URL https://hostname:port_number/twsd, sendo a porta padrao do master domain manager ou backup domain manager a 31116.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a REST API e acessada via HTTPS na URL https://hostname:port_number/twsd, sendo a porta padrao do master domain manager ou backup domain manager a 31116.?*

---

### 41. hwa-10.2.8-dwc-restv2-v1-diff-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > restv2 [restv2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 difere da V1 por oferecer filtragem aprimorada (planFilter/OQL), payloads melhorados para consumo e endpoints multi-item (operacao por ID ou por filtro), sendo recomendada para integracoes futuras.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para restv2 no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a REST API V2 difere da V1 por oferecer filtragem aprimorada (planFilter/OQL), payloads melhorados para consumo e endpoints multi-item (operacao por ID ou por filtro), sendo recomendada para integracoes futuras?*

---

### 42. hwa-10.2.8-dwc-trace-template-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, o template trace.xml para o DWC fica em configDropins/templates/trace.xml e pode ser personalizado com valores de trace.specification (por exemplo tws_all, tws_rest, tws_db) antes de copiar para overrides.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, o template trace?*

---

### 43. hwa-10.2.8-dynagent-resource-advisor-url-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: REST API V2 (HTTPS Port 31116) > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
A propriedade ResourceAdvisorUrl da seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 define a URL do master em ambiente distribuído ou do dynamic domain manager que hospeda o agent, no formato https://tdwb_server:tdwb_port/JobManagerRESTWeb/JobScheduler/resource, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade ResourceAdvisorUrl da seção [ResourceAdvisorAgent] do JobManager?*

---

### 44. hwa-10.2.8-dynamicagent-resource-advisor-url-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
O agente dinâmico conecta-se ao DWB via HTTPS ResourceAdvisorUrl no JobManager.ini seção [ResourceAdvisorAgent]; registra-se automaticamente na instalação ao MDM ou DDM; ResourceAdvisorUrl = https://<tdwb_server>:<tdwb_port>/JobManagerRESTWeb/JobScheduler/resource.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O agente dinâmico conecta-se ao DWB via HTTPS ResourceAdvisorUrl no JobManager?*

---

### 45. hwa-10.2.8-govern-object-versioning-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o recurso de versionamento de objetos mantém todas as versões anteriores de objetos de agendamento e de segurança, e no Dynamic Workload Console é possível ver o histórico, comparar versões e restaurar uma versão anterior; o recurso exige as opções globais dbAudit=1 e auditStore=db ou both.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o recurso de versionamento de objetos mantém todas as versões anteriores de objetos de agendamento e de segurança, e no Dynamic Workload Console é possível ver o histórico, comparar versões e restaurar uma versão anterior; o recurso exige as opções globais dbAudit=1 e auditStore=db ou both?*

---

### 46. hwa-10.2.8-gui-sap-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, é possível criar, pela Dynamic Workload Console (Workload Designer), uma definição de SAP job que referencia um InfoPackage ou Process Chain do SAP Business Warehouse; na página Task define-se o Subtype como BW Process Chain ou BW InfoPackage e clica-se em Save para salvar a definição no banco de dados; para InfoPackages o Start type deve ser 'Start later in background process' com Start time 'Immediate', e para process chains o modo deve ser 'Start Using Meta Chain or API'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é possível criar, pela Dynamic Workload Console (Workload Designer), uma definição de SAP job que referencia um InfoPackage ou Process Chain do SAP Business Warehouse; na página Task define-se o Subtype como BW Process Chain ou BW InfoPackage e clica-se em Save para salvar a definição no banco de dados; para InfoPackages o Start type deve ser 'Start later in background process' com Start time 'Immediate', e para process chains o modo deve ser 'Start Using Meta Chain or API'?*

---

### 47. hwa-10.2.8-incident-awktsa050e-restart-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: incidents > dynamic_agent [dynamic_agent]]`

**Regra Canônica / Evidência:**
Sintoma: apos submeter workload, a mensagem AWKTSA050E 'A problem with the JCL content, prevent Dynamic Workload Bridge from submitting the job' e escrita no messages.log do master domain manager. Causa: o erro indica que um restart do WebSphere Application Server Liberty Base e necessario. Resolucao: reiniciar o WebSphere Liberty e reenviar o workload. Fonte: HCL Troubleshooting Guide 10.2.8 (AWKTSA050E error issued during submission).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKTSA050E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKTSA050E no HWA?*
- *Qual endpoint REST API V2 é utilizado para dynamic_agent no HWA?*
- *O que causa e como solucionar o problema: apos submeter workload, a mensagem AWKTSA050E 'A problem with the JCL content, prevent Dynamic Workload Bridge from submitting the job' e escrita no messages?*

---

### 48. hwa-10.2.8-incident-critical-empty-hotlist-0141

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: incidents > critical-network [critical-network]]`

**Regra Canônica / Evidência:**
Sintoma: um job critical de alto risco tem uma hot list vazia. Causa: normalmente ocorre se um job critical ou predecessor critical foi projetado com um conflito que o fara sempre atrasar (ex.: start restriction apos o deadline do job critical); a hot list fica vazia se o job/job stream que causa o problema nao tem as dependencias follows resolvidas. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: um job critical de alto risco tem uma hot list vazia?*
- *O que causa e como solucionar o problema: um job critical de alto risco tem uma hot list vazia?*

---

### 49. hwa-10.2.8-incident-mrc019e-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: incidents > connection [connection]]`

**Regra Canônica / Evidência:**
Sintoma: AWSMRC019E (EOF/erro de comunicacao) ao conectar ocli ou REST. Causa: contextroot incorreto (ex.: /twsd sozinho em vez de /,/twsd/cli) ou autenticacao ausente. Resolucao: usar contextroot /,/twsd/cli no config.yaml do ocli e configurar a API Key (connection.jwt).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSMRC019E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSMRC019E no HWA?*
- *O que causa e como solucionar o problema: AWSMRC019E (EOF/erro de comunicacao) ao conectar ocli ou REST?*

---

### 50. hwa-10.2.8-incident-tokensrv-password-0095

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation. Causa: o usuario sob o qual esses servicos iniciam pode ter mudado a senha, ou o nome do servico nao corresponde ao esperado pelo HWA (impactado por mudanca na configuracao da workstation). Resolucao: seguir o procedimento do Administration Guide para o caso de senha alterada; temporariamente, iniciar o servico manualmente pelo Windows Services panel. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation?*
- *O que causa e como solucionar o problema: em Windows, o Tivoli Token Service e o HCL Workload Automation for user service (batchup) falham ao iniciar apos restart da workstation?*

---

### 51. hwa-10.2.8-k8s-deploy-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os pre-requisitos para deployment via helm chart em Kubernetes incluem: Helm 3.12 ou posterior, Kubernetes versao 1.29 ou posterior, kubectl, OpenSSL, Jetstack cert-manager, um ingress controller (para NGINX via helm, habilitar controller.extraArgs.enable-ssl-passthrough), Grafana e Prometheus para dashboards, API key do HCL Entitled Registry (hclcr.io) e, opcionalmente, o Gateway API para roteamento de trafego externo em vez de Ingress.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*

---

### 52. hwa-10.2.8-k8s-deploy-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as imagens de container do deployment Kubernetes sao servidas pelo HCL Entitled Registry hclcr.io/wa, com tags por versao: hcl-workload-automation-agent-dynamic, hcl-workload-automation-server e hcl-workload-automation-console na tag 10.2.8.00.20260727; o acesso as imagens requer um secret docker-registry no namespace criado com kubectl create secret docker-registry sa-<namespace> --docker-server=hclcr.io --docker-username=<user> --docker-password=<api_key>.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as imagens de container do deployment Kubernetes sao servidas pelo HCL Entitled Registry hclcr?*

---

### 53. hwa-10.2.8-k8s-deploy-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: REST API V2 (HTTPS Port 31116) > Tópico: kubernetes > agents [k8s_agent_gateway]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para dynamic agent em Kubernetes com remote gateway, os parametros adicionados a partir da versao 10.2 no deployment wa-agent sao agent.dynamic.gateway.hostname (IP/hostname do agente com local gateway), agent.dynamic.gateway.port (porta do agente com local gateway, default 31114) e agent.dynamic.gateway.jmFullyQualifiedHostname (hostname do novo agente); e necessario atualizar JobManagerGWURIs no arquivo JobManagerGW.ini do agente com local gateway para apontar para o nome do servico (ex.: https://wa-agent:31114/ita/JobManagerGW/JobManagerRESTWeb/JobScheduler/resource).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para agents?*

---

### 54. hwa-10.2.8-message-ita047i-0153

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
AWSITA047I: mensagem informativa do JobManager indicando inicio/parada de processo no dynamic agent. Observada no lab: apos ShutDownLwa e StartUpLwa, MDMDA retornou com o flag JobManager e o registro de recursos foi retomado, mas uma nova submissao ad hoc com alias unico permaneceu READY — o restart sozinho nao resolveu o dispatch; AWSITA047I 'Starting' e AWSITA111I 'The Resource Advisor Agent is stopped' foram registrados. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA047I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA047I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA111I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA111I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA047I no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSITA111I no HWA e qual ação é recomendada?*

---

### 55. hwa-10.2.8-resource-resource-units-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
Um recurso é uma restrição de agendamento física ou lógica (unidades de fita, conexões de banco de dados, slots de aplicação); é associado a uma workstation com unidades disponíveis; jobs solicitam unidades via dependência needs; as unidades permanecem reservadas enquanto o job é executado e são liberadas ao concluir.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Um recurso é uma restrição de agendamento física ou lógica (unidades de fita, conexões de banco de dados, slots de aplicação); é associado a uma workstation com unidades disponíveis; jobs solicitam unidades via dependência needs; as unidades permanecem reservadas enquanto o job é executado e são liberadas ao concluir?*

---

### 56. hwa-10.2.8-rest-api-v2-endpoint-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
REST API V2 is recommended for modern integrations; the documented REST endpoint is /twsd/ with default HTTPS port 31116 for MDM/BMDM. Context: Access the REST API using https://hostname:port_number/twsd where 31116 is the default HTTPS port.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para mdm no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: REST API V2 is recommended for modern integrations; the documented REST endpoint is /twsd/ with default HTTPS port 31116 for MDM/BMDM?*

---

### 57. hwa-10.2.8-rest-service-url-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Para MDM ou BMDM HWA Distributed 10.2.8, a URL documentada do serviço REST é https://hostname:port_number/twsd e a porta HTTPS padrão é 31116. Context: https://hostname:port_number/twsd ... The HTTPS port number of the master domain manager or backup domain manager. The default is 31116.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para mdm no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Para MDM ou BMDM HWA Distributed 10.2.8, a URL documentada do serviço REST é https://hostname:port_number/twsd e a porta HTTPS padrão é 31116. Context: https://hostname:port_number/twsd?*

---

### 58. hwa-10.2.8-rest-v2-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
A documentação HWA 10.2.8 recomenda REST API V2 para integrações futuras. Context: REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A documentação HWA 10.2.8 recomenda REST API V2 para integrações futuras?*

---

### 59. hwa-10.2.8-restapi-auth-apikey-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: rest_api > auth [rest_api_auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a autenticacao na REST API (incluindo REST API V2) pode ser feita por API Keys, permitindo autenticar uma linha de comando ou aplicacao de forma facil e rapida. As API Keys sao gerenciadas via OCLI (comando ocli apikey create/list/delete) e enviadas no header HTTP x-api-key. A API Key substitui a necessidade de usuario/senha em automacoes, oferecendo maior seguranca (rotacao de chaves, escopo por usuario).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para auth no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a autenticacao na REST API (incluindo REST API V2) pode ser feita por API Keys, permitindo autenticar uma linha de comando ou aplicacao de forma facil e rapida?*

---

### 60. hwa-10.2.8-restapi-auth-jwt-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: rest_api > auth [rest_api_auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a autenticacao de agentes pode ser aprimorada usando JSON Web Tokens (JWT). Os JWTs sao usados para autenticar agentes dinâmicos junto ao master domain manager, substituindo o certificado SSL tradicional. O JWT oferece um padrao moderno de autenticacao, permitindo maior seguranca e integracao com sistemas de identidade existentes. O JWT e configurado no arquivo jwtFed.xml do DWC/engine.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para auth no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a autenticacao de agentes pode ser aprimorada usando JSON Web Tokens (JWT)?*

---

### 61. hwa-10.2.8-restapi-devguide-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: rest_api > devguide [rest_api_v2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Developer's Guide (Driving HCL Workload Automation) documenta o uso da REST API para operacoes de workload. Exemplo: para submeter um job stream no plano atual, use GET /twsd/api/v2/model/jobstream com filtros de modelo ou OQL para encontrar o job stream pelo nome (ex.: JS-API), obtenha o ID do job stream na resposta, depois use POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit para submete-lo no plano. A resposta inclui count, results com kind, key, def (com id, folder, name, workstation, options, runCycles, matchingCriteria). O Developer's Guide completo esta em https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*

---

### 62. hwa-10.2.8-restapi-oql-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: rest_api > oql [rest_api_oql]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Orchestration Query Language (OQL) e uma linguagem de consulta para a REST API V2 que permite ordenar resultados de forma simples. O OQL pode ser usado sozinho ou combinado com planFilter (planFilter para filtragem, OQL para ordenacao). O OQL e mais simples que o planFilter e oferece uma sintaxe mais acessivel para consultas aos recursos de workload (job streams, jobs, planos).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para oql no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Orchestration Query Language (OQL) e uma linguagem de consulta para a REST API V2 que permite ordenar resultados de forma simples?*

---

### 63. hwa-10.2.8-restapi-v2-intro-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: rest_api > v2_overview [rest_api_v2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a REST API V2 foi introduzida para operar o produto tanto pela Interface de Usuario quanto pela Linha de Comando, acessivel via HTTPS ao master/backup domain manager (porta default 31116). Os novos recursos incluem: (1) filtragem aprimorada via planFilter (similar a sintaxe do conman) ou OQL (Orchestration Query Language, mais simples e com ordenacao), podendo usar ambos combinados (planFilter para filtragem, OQL para ordenacao); (2) payloads melhorados para consumo mais facil; (3) endpoints multi-item eficientes (cada acao pode ser executada por ID ou por filtro, permitindo operar em um item ou multiplos). A autenticacao pode ser feita por basic auth (usuario/senha), API Keys ou JSON Web Tokens (JWT).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar v2_overview?*
- *Qual endpoint REST API V2 é utilizado para v2_overview no HWA?*

---

### 64. hwa-10.2.8-restauth-api-keys-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
A versão 10.2.8 enfatiza o uso de API Keys para autenticação CLI/REST; a primeira conexão com o HCL Workload Automation via Orchestration CLI requer autenticação com API Keys.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A versão 10.2.8 enfatiza o uso de API Keys para autenticação CLI/REST; a primeira conexão com o HCL Workload Automation via Orchestration CLI requer autenticação com API Keys?*

---

### 65. hwa-10.2.8-restocli-abbreviated-forms-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Os comandos do Orchestration CLI no HCL Workload Automation 10.2.8 possuem formas abreviadas (podem ser usadas a abreviatura ou a forma por extenso) e as opções de comando não diferenciam maiúsculas de minúsculas, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Os comandos do Orchestration CLI no HCL Workload Automation 10.2.8 possuem formas abreviadas (podem ser usadas a abreviatura ou a forma por extenso) e as opções de comando não diferenciam maiúsculas de minúsculas, conforme documentação oficial?*

---

### 66. hwa-10.2.8-restocli-api-keys-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
A autenticação da linha de comando e de aplicações contra o HCL Workload Automation 10.2.8 é documentada pelo uso de API Keys (Personal e Service) geradas no Dynamic Workload Console e de JSON Web Token (parâmetro -jwt), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A autenticação da linha de comando e de aplicações contra o HCL Workload Automation 10.2.8 é documentada pelo uso de API Keys (Personal e Service) geradas no Dynamic Workload Console e de JSON Web Token (parâmetro -jwt), conforme documentação oficial?*

---

### 67. hwa-10.2.8-restocli-base-url-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
A base URL documentada da REST API V2 é https://hostname:port_number/twsd, onde hostname é o master domain manager (MDM) ou backup MDM e port_number é a porta HTTPS cujo padrão é 31116, no HCL Workload Automation 10.2.8 conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para mdm no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A base URL documentada da REST API V2 é https://hostname:port_number/twsd, onde hostname é o master domain manager (MDM) ou backup MDM e port_number é a porta HTTPS cujo padrão é 31116, no HCL Workload Automation 10.2.8 conforme documentação oficial?*

---

### 68. hwa-10.2.8-restocli-command-groups-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O Orchestration CLI do HCL Workload Automation 10.2.8 é organizado em três grupos de comandos principais (context, model e plan), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O Orchestration CLI do HCL Workload Automation 10.2.8 é organizado em três grupos de comandos principais (context, model e plan), conforme documentação oficial?*

---

### 69. hwa-10.2.8-restocli-comparison-operators-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
A sintaxe OQL do HCL Workload Automation 10.2.8 documenta as keywords AND, OR, IN, NOT IN, LIKE, NOT LIKE, ORDER BY (ASC/DESC), além dos operadores de comparação =, !=, <=, >=, <, > e de listas, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A sintaxe OQL do HCL Workload Automation 10.2.8 documenta as keywords AND, OR, IN, NOT IN, LIKE, NOT LIKE, ORDER BY (ASC/DESC), além dos operadores de comparação =, !=, <=, >=, <, > e de listas, conforme documentação oficial?*

---

### 70. hwa-10.2.8-restocli-context-commands-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Os comandos de contexto (context) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem list, new, remove, set e switch, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Os comandos de contexto (context) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem list, new, remove, set e switch, conforme documentação oficial?*

---

### 71. hwa-10.2.8-restocli-first-run-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Na primeira conexão do Orchestration CLI com o HCL Workload Automation 10.2.8, a autenticação é realizada usando API Keys, com um fluxo inicial que exibe um link web para gerar a API Key, que é automaticamente atualizada no arquivo config.yaml, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Na primeira conexão do Orchestration CLI com o HCL Workload Automation 10.2.8, a autenticação é realizada usando API Keys, com um fluxo inicial que exibe um link web para gerar a API Key, que é automaticamente atualizada no arquivo config?*

---

### 72. hwa-10.2.8-restocli-get-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint GET /twsd/api/v2/model/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar definições de job stream na base de dados (camada de modelo), podendo usar filtros de modelo ou OQL, sendo uma operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/model/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar definições de job stream na base de dados (camada de modelo), podendo usar filtros de modelo ou OQL, sendo uma operação de leitura, conforme documentação oficial?*

---

### 73. hwa-10.2.8-restocli-get-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint GET /twsd/api/v2/plan/job é documentado no HCL Workload Automation 10.2.8 para consultar jobs do plano atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/plan/job é documentado no HCL Workload Automation 10.2.8 para consultar jobs do plano atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial?*

---

### 74. hwa-10.2.8-restocli-get-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint GET /twsd/api/v2/plan/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar job streams no plano de produção atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/plan/jobstream é documentado no HCL Workload Automation 10.2.8 para consultar job streams no plano de produção atual (verificar submissões), sendo uma operação de leitura, conforme documentação oficial?*

---

### 75. hwa-10.2.8-restocli-get-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint GET /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para consultar/verificar definições de job na base de dados, sendo uma operação de leitura, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint GET /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para consultar/verificar definições de job na base de dados, sendo uma operação de leitura, conforme documentação oficial?*

---

### 76. hwa-10.2.8-restocli-model-commands-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Os comandos de modelo (model) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem add, delete, display, draft/undraft, extract, list, listfolder, lock, mkfolder, modify, new, nop/unnop, rename, renamefolder, replace, rmfolder e unlock, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Os comandos de modelo (model) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem add, delete, display, draft/undraft, extract, list, listfolder, lock, mkfolder, modify, new, nop/unnop, rename, renamefolder, replace, rmfolder e unlock, conforme documentação oficial?*

---

### 77. hwa-10.2.8-restocli-model-layer-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
A REST API V2 do HCL Workload Automation 10.2.8 organiza os endpoints em camada de modelo (definições na base de dados, prefixo /model/) e camada de plano (plano de produção atual, prefixo /plan/), conforme documentação oficial dos endpoints.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 organiza os endpoints em camada de modelo (definições na base de dados, prefixo /model/) e camada de plano (plano de produção atual, prefixo /plan/), conforme documentação oficial dos endpoints?*

---

### 78. hwa-10.2.8-restocli-multi-item-endpoints-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
A REST API V2 do HCL Workload Automation 10.2.8 introduz endpoints multi-item eficientes, nos quais cada ação pode ser executada por ID ou por filtro, permitindo operar um único item ou múltiplos itens, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 introduz endpoints multi-item eficientes, nos quais cada ação pode ser executada por ID ou por filtro, permitindo operar um único item ou múltiplos itens, conforme documentação oficial?*

---

### 79. hwa-10.2.8-restocli-ocli-wildcards-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O Orchestration CLI do HCL Workload Automation 10.2.8 suporta wildcards e delimitadores documentados, incluindo @ (padrão nulo ou um/múltiplos caracteres), ? (um único caractere), a sintaxe de pasta /@/ e delimitadores como +, ~, ;, , e =, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O Orchestration CLI do HCL Workload Automation 10.2.8 suporta wildcards e delimitadores documentados, incluindo @ (padrão nulo ou um/múltiplos caracteres), ? (um único caractere), a sintaxe de pasta /@/ e delimitadores como +, ~, ;, , e =, conforme documentação oficial?*

---

### 80. hwa-10.2.8-restocli-oql-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O Orchestration Query Language (OQL) é uma nova sintaxe que se aplica à REST API V2 e auxilia no monitoramento do ambiente de plano de produção do HCL Workload Automation 10.2.8, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O Orchestration Query Language (OQL) é uma nova sintaxe que se aplica à REST API V2 e auxilia no monitoramento do ambiente de plano de produção do HCL Workload Automation 10.2.8, conforme documentação oficial?*

---

### 81. hwa-10.2.8-restocli-pagination-envelope-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
The documented HCL Workload Automation 10.2.8 REST API V2 response envelope contains "count" and "results" fields, but no pagination parameters (limit, offset, page) are documented in the official REST API reference pages (awsddrestapi.html or the OpenAPI spec WA_API3_v2.json).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 82. hwa-10.2.8-restocli-path-param-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit é documentado no HCL Workload Automation 10.2.8 para submeter um job stream ao plano de produção atual, usando o ID do job stream de modelo, sendo uma operação mutating, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/jobstream/ no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/plan/jobstream/{model_jobstream_id}/submit é documentado no HCL Workload Automation 10.2.8 para submeter um job stream ao plano de produção atual, usando o ID do job stream de modelo, sendo uma operação mutating, conforme documentação oficial?*

---

### 83. hwa-10.2.8-restocli-plan-commands-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Os comandos de plano (plan) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem submit job, submit sched, submit docommand, rerun, cancel job, cancel sched, release job, release sched, showjobs, kill, hold/release e muitos outros, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Os comandos de plano (plan) do Orchestration CLI no HCL Workload Automation 10.2.8 incluem submit job, submit sched, submit docommand, rerun, cancel job, cancel sched, release job, release sched, showjobs, kill, hold/release e muitos outros, conforme documentação oficial?*

---

### 84. hwa-10.2.8-restocli-post-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint POST /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para criar uma definição de job (job definition) na base de dados, sendo uma operação mutating, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O endpoint POST /twsd/api/v2/model/jobdefinition é documentado no HCL Workload Automation 10.2.8 para criar uma definição de job (job definition) na base de dados, sendo uma operação mutating, conforme documentação oficial?*

---

### 85. hwa-10.2.8-restocli-post-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O endpoint POST /twsd/api/v2/plan/job/submit-ad-hoc-job é documentado no HCL Workload Automation 10.2.8 para submeter um job ad-hoc ao plano, sendo uma operação mutating, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job/submit-ad-hoc-job no HWA?*
- *Qual endpoint REST API V2 é documentado para submeter um job ad-hoc no plano?*

---

### 86. hwa-10.2.8-restocli-query-term-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Uma consulta OQL no HCL Workload Automation 10.2.8 começa com uma expressão composta por conditions chamadas queryTerms, onde cada queryTerm contém três elementos (field, comparison_operator, value) e os campos e valores são case-sensitive, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Uma consulta OQL no HCL Workload Automation 10.2.8 começa com uma expressão composta por conditions chamadas queryTerms, onde cada queryTerm contém três elementos (field, comparison_operator, value) e os campos e valores são case-sensitive, conforme documentação oficial?*

---

### 87. hwa-10.2.8-restocli-rest-api-v2-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
A REST API V2 é a nova versão das REST APIs do HCL Workload Automation 10.2.8, projetada para operar o produto tanto pela Interface de Usuário quanto pela Interface de Linha de Comando, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A REST API V2 é a nova versão das REST APIs do HCL Workload Automation 10.2.8, projetada para operar o produto tanto pela Interface de Usuário quanto pela Interface de Linha de Comando, conforme documentação oficial?*

---

### 88. hwa-10.2.8-restocli-version-command-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O comando version do Orchestration CLI no HCL Workload Automation 10.2.8 tem a sintaxe documentada ocli [context|model|plan|plugin] version|v e exibe a versão do Orchestration CLI instalada, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para ocli no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: O comando version do Orchestration CLI no HCL Workload Automation 10.2.8 tem a sintaxe documentada ocli [context|model|plan|plugin] version|v e exibe a versão do Orchestration CLI instalada, conforme documentação oficial?*

---

### 89. hwa-10.2.8-restore-backup-mdm-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
A página 'Backing up and restoring the database' (awsadbckupnrestore.html) da documentação do HCL Workload Automation 10.2.8 NÃO fornece um procedimento completo e passo a passo de restauração do banco de dados HWA a partir de um backup. A página documenta o backup dos arquivos de configuração (useropts, localopts, Security, Sfinal, globalopts, TWSConfig.properties, planos forecast/archived/trial), o uso de um backup master domain manager com banco de dados espelhado (mirror) para recuperação de desastres, e o backup de arquivos de log. Não há etapas explícitas de 'restore' do banco de dados; a manutenção geral do banco é remetida à documentação do fornecedor do RDBMS.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*

---

### 90. hwa-10.2.8-restore-resolved-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
RESOLUCAO de hwa-10.2.8-restore-0001 (contradicted): na documentacao 10.2.8, a pagina 'Backing up and restoring the database' NAO fornece etapas explicitas de restore de banco; o que ela documenta como recuperacao e: (1) backup dos arquivos de configuracao e planos, (2) uso de um backup master domain manager acessando banco espelhado para disaster recovery, e (3) restauracao dos arquivos de configuracao. A restauracao efetiva do banco e executada pelo DBA com a ferramenta do SGBD, fora do escopo da pagina.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: RESOLUCAO de hwa-10.2.8-restore-0001 (contradicted): na documentacao 10.2.8, a pagina 'Backing up and restoring the database' NAO fornece etapas explicitas de restore de banco; o que ela documenta como recuperacao e: (1) backup dos arquivos de configuracao e planos, (2) uso de um backup master domain manager acessando banco espelhado para disaster recovery, e (3) restauracao dos arquivos de configuracao?*

---

### 91. hwa-10.2.8-restsubmit-rest-api-v2-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
Endpoints da REST API v2: GET /twsd/api/v2/model/jobdefinition, GET /twsd/api/v2/model/jobstream, GET /twsd/api/v2/plan/job, GET /twsd/api/v2/plan/jobstream e POST /twsd/api/v2/plan/jobstream/{id}/submit.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/jobdefinition no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Endpoints da REST API v2: GET /twsd/api/v2/model/jobdefinition, GET /twsd/api/v2/model/jobstream, GET /twsd/api/v2/plan/job, GET /twsd/api/v2/plan/jobstream e POST /twsd/api/v2/plan/jobstream/{id}/submit?*

---

### 92. hwa-10.2.8-restv2-endpoints-0148

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest_api_v2 [rest_api_v2]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a REST API V2 esta disponivel em https://<host>:31116/twsd/api/v2/ com autenticacao Bearer (JWT de API key Personal). Endpoints GET read-only validados no lab: engine/info (licenseType/timezone), engine/users, engine/groups, model/jobdefinition (84), model/jobstream, model/workstation (5), model/domain (MASTERDM master), model/variabletable, model/folder, plan/job (236), plan/job/{id}, plan/job/count, plan/jobstream (201), plan/workstation, plan/prompt, plan/resource, objects-info. O context root e '/twsd/api/v2/' e o JWT do ocli (Personal) autoriza a REST API v2.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/ no HWA?*

---

### 93. hwa-10.2.8-restv2-oql-name-0149

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > oql [oql]]`

**Regra Canônica / Evidência:**
Na REST API V2 do HWA 10.2.8 (parametro 'oql' de GET /twsd/api/v2/plan/job), o filtro OQL usa o campo 'name' (ex.: oql=name = 'UPDATESTATS' retorna os jobs com esse nome). GAP doc x impl: a spec OpenAPI oficial exemplifica 'key.name = \'TEST_JOB\'', mas no lab 'oql=key.name = \'X\'' retorna 400 OQL_FILTER_SYNTAX_ERROR. A sintaxe aceita e 'name = \'X\'' (campo simples, sem prefixo key.).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8 (parametro 'oql' de GET /twsd/api/v2/plan/job), o filtro OQL usa o campo 'name' (ex?*

---

### 94. hwa-10.2.8-restv2-oql-sort-0150

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > oql [oql]]`

**Regra Canônica / Evidência:**
Na REST API V2 do HWA 10.2.8, o parametro 'oql' suporta ordenacao com dot notation: 'oql=ORDER BY key.name ASC' em GET /twsd/api/v2/plan/job retorna 200 com resultados ordenados (sem parametros de sort separados na URL). OQL com ORDER BY e o mecanismo de ordenacao da V2.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, o parametro 'oql' suporta ordenacao com dot notation: 'oql=ORDER BY key?*

---

### 95. hwa-10.2.8-restv2-pagination-0152

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > pagination [pagination]]`

**Regra Canônica / Evidência:**
Na REST API V2 do HWA 10.2.8, GET /twsd/api/v2/plan/job suporta paginacao explicita com 'limit' e 'offset' (ex.: limit=2 retorna 2 resultados e a resposta inclui 'next' com a URL completa para a proxima pagina: https://localhost:31116/twsd/api/v2/plan/job?limit=2&offset=2). O campo 'count' na resposta indica o total de itens (236).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, GET /twsd/api/v2/plan/job suporta paginacao explicita com 'limit' e 'offset' (ex?*

---

### 96. hwa-10.2.8-restv2-workspace-404-0153

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > model [model]]`

**Regra Canônica / Evidência:**
Na REST API V2 do HWA 10.2.8, o endpoint GET /twsd/api/v2/model/workspace aparece na spec OpenAPI oficial (WA_API3_v2.json) mas retorna HTTP 404 no lab — nao exposto/implementado neste ambiente. Diferente dos demais endpoints model/* (jobdefinition, workstation, domain, folder, calendar, variabletable) que respondem 200.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/model/workspace no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Na REST API V2 do HWA 10.2.8, o endpoint GET /twsd/api/v2/model/workspace aparece na spec OpenAPI oficial (WA_API3_v2.json) mas retorna HTTP 404 no lab — nao exposto/implementado neste ambiente?*

---

### 97. hwa-10.2.8-runbook-recommended-first-component-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, é uma boa prática iniciar o upgrade pelo Dynamic Workload Console (DWC) primeiro: ao atualizar o console para o novo nível de versão, ele pode ser usado para verificar se o ambiente está funcionando após atualizar os componentes restantes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é uma boa prática iniciar o upgrade pelo Dynamic Workload Console (DWC) primeiro: ao atualizar o console para o novo nível de versão, ele pode ser usado para verificar se o ambiente está funcionando após atualizar os componentes restantes?*

---

### 98. hwa-10.2.8-sec-api-key-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a API Key (token JWT) usada para autenticar o Orchestration CLI é armazenada no arquivo config.yaml, localizado em $HOME/.OCLI/config.yaml (Linux) ou %userprofile%\.OCLI\config.yaml (Windows), adicionando ou substituindo o valor da propriedade JWT.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a API Key (token JWT) usada para autenticar o Orchestration CLI é armazenada no arquivo config?*

---

### 99. hwa-10.2.8-sec-api-key-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, API Keys expiram por padrão após 365 dias; a duração e o intervalo de transição de status podem ser configurados com os parâmetros com.ibm.tws.dao.rdbms.apikey.expiring.timeout e com.ibm.tws.util.jwt.apikey.expiration.date no arquivo TWSConfig.properties, exigindo reinício do Liberty; API Keys já criadas não podem ser modificadas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, API Keys expiram por padrão após 365 dias; a duração e o intervalo de transição de status podem ser configurados com os parâmetros com?*

---

### 100. hwa-10.2.8-sec-manage-api-keys-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, ao criar uma API Key na Dynamic Workload Console (menu Manage API Keys, tipo Personal ou Service), o token é exibido uma única vez na caixa de diálogo e a documentação instrui a salvá-lo e armazená-lo em local seguro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, ao criar uma API Key na Dynamic Workload Console (menu Manage API Keys, tipo Personal ou Service), o token é exibido uma única vez na caixa de diálogo e a documentação instrui a salvá-lo e armazená-lo em local seguro?*

---

### 101. hwa-10.2.8-sec-open-id-connect-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, ao executar o Orchestration CLI pela primeira vez, um erro exibe um link web para criação da API Key; após autenticar no provedor OpenID Connect configurado, a API Key gerada é atualizada automaticamente no arquivo config.yaml.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, ao executar o Orchestration CLI pela primeira vez, um erro exibe um link web para criação da API Key; após autenticar no provedor OpenID Connect configurado, a API Key gerada é atualizada automaticamente no arquivo config?*

---

### 102. hwa-10.2.8-showjobs-agent-ready-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, um job que falha porque o agente não está disponível é reiniciado automaticamente, volta a READY e aguarda a reconexão do agente. Context: If a job fails because the agent is not available, the job is automatically restarted and set to the READY status, waiting for the agent to connect again.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, um job que falha porque o agente não está disponível é reiniciado automaticamente, volta a READY e aguarda a reconexão do agente?*

---

### 103. hwa-10.2.8-timezone-job-stream-level-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o fuso horário especificado no nível do job stream se aplica às definições de tempo dos run cycles e às restrições de tempo (definidas pelos keywords at, deadline, schedtime e until).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o fuso horário especificado no nível do job stream se aplica às definições de tempo dos run cycles e às restrições de tempo (definidas pelos keywords at, deadline, schedtime e until)?*

---

### 104. hwa-10.2.8-trouble-awsres003e-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; monitoring) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o Resource Advisor loga AWSRES003E quando nao recebe o heartbeat de uma workstation (em ambiente Linux a falha pode ocorrer por resolucao de host perdida em /etc/hosts); a causa e a workstation/alias de host nao resolvido ou indisponivel, e a recuperacao e restaurar a resolucao do hostname da workstation (ex.: readicionar o alias do MDMHOST em /etc/hosts) e verificar a conectividade de rede antes de reiniciar o monitoramento.

**Plataforma / Validação:** distributed; monitoring

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSRES003E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSRES003E no HWA?*

---

### 105. hwa-10.2.8-vm-9f-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A REST API V2 do HCL Workload Automation Distributed é servida no caminho https://hostname:port/twsd (porta padrão 31116), e não no caminho legado /JobManagerRESTWeb/, tanto na 10.2.0 quanto na 10.2.8. A REST API V2 foi introduzida na 10.1 Fix Pack 1.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para jobman no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation Distributed é servida no caminho https://hostname:port/twsd (porta padrão 31116), e não no caminho legado /JobManagerRESTWeb/, tanto na 10.2.0 quanto na 10.2.8. A REST API V2 foi introduzida na 10.1 Fix Pack 1.?*

---

### 106. hwa-9.5-real-twsd-31116-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 Fix Pack 7 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5 Fix Pack 7 Distributed (MDM ou BMDM), o servico REST usa o contexto HTTPS /twsd e a porta padrao 31116; tambem em 10.2.8 o porto padrao do REST permanece 31116, mas em 9.5 o contexto e /twsd na raiz do servidor (não e o caminho /twsd/api da V2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para /twsd/api no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5 Fix Pack 7 Distributed (MDM ou BMDM), o servico REST usa o contexto HTTPS /twsd e a porta padrao 31116; tambem em 10.2.8 o porto padrao do REST permanece 31116, mas em 9.5 o contexto e /twsd na raiz do servidor (não e o caminho /twsd/api da V2)?*

---

### 107. hwa-distributed-cancel-sched-pend-10.2.0-001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.0, `cancel sched`/`cs` requer acesso `cancel`; com `;pend`, antes do lançamento aguarda a resolução das dependências e, após o lançamento, cancela os jobs restantes; em ambos os casos os dependentes são liberados da dependência.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.0, `cancel sched`/`cs` requer acesso `cancel`; com `;pend`, antes do lançamento aguarda a resolução das dependências e, após o lançamento, cancela os jobs restantes; em ambos os casos os dependentes são liberados da dependência?*

---

### 108. hwa-distributed-rest-api-v2-base-url-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
A REST API V2 do HCL Workload Automation 10.2.8 é acessada pela URL base https://<hostname>:<port_number>/twsd, onde <hostname> é o master domain manager ou backup master domain manager e <port_number> é a porta HTTPS desses componentes, cujo padrão (default) é 31116.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 é acessada pela URL base https://<hostname>:<port_number>/twsd, onde <hostname> é o master domain manager ou backup master domain manager e <port_number> é a porta HTTPS desses componentes, cujo padrão (default) é 31116.?*

---

### 109. hwa-lab-10.2.8-rest-api-v2-inspection-and-operations-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: TWS REST API v2 / Open Liberty > Interface: HTTP/REST (Swagger UI em /twsd/) > Tópico: integration > rest_api [v2_endpoints]]`

**Regra Canônica / Evidência:**
A API REST oficial v2 do HWA 10.2.8 (exposta na porta 31116 via Liberty engineServer sob o prefixo /twsd/api/v2/) possui mais de 210 rotas documentadas em WA_API3_v2.json. O endpoint /twsd/api/v2/plan/job retorna os dados completos de execução em JSON estruturado, incluindo histórico de jobruns (regular vs recovery), códigos de retorno e o array de ações permitidas (RERUN_JOB, GET_JOB_LOG, HOLD_JOB).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Qual o prefixo base e porta padrão da API REST v2 do HCL Workload Automation 10.2.8?*
- *Como a API REST v2 do HWA representa o histórico de tentativas (rerun) de um job no plano?*
- *Quais são os principais metadados e ações operacionais retornados pela rota /twsd/api/v2/plan/job?*

---

### 110. hwa-lab-10.2.8-rest-v2-job-mutation-actions-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: TWS REST API v2 / Security Engine > Interface: HTTP PUT / CLI makesec > Tópico: integration > rest_mutations [rerun_hold_release]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, operações mutantes no plano via API REST v2 utilizam o método HTTP PUT nos endpoints /twsd/api/v2/plan/job/run/{run_id}/action/rerun (com payload JSON RerunDetailsV2) e /twsd/api/v2/plan/job/{job_id}/action/hold e release. A autorização exige que o usuário autenticado esteja explicitamente configurado com permissões de execução (ACCESS=RERUN,EXEC,SUBMIT) no arquivo de segurança Security compilado com makesec, caso contrário o servidor retorna HTTP 403 (AWSJDB817E).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Qual método HTTP e endpoint da API REST v2 do HWA são utilizados para solicitar o rerun de um job no plano?*
- *O que causa o erro HTTP 403 AWSJDB817E ao tentar executar ações mutantes no plano via REST API v2?*
- *Como autorizar um usuário de integração REST a executar ações no plano de produção do HWA?*

---

### 111. hwa-rest-twsd-31116-official-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Para HCL Workload Automation 9.5 Fix Pack 7 em ambiente Distributed com MDM ou BMDM, o serviço REST usa o contexto HTTPS /twsd e a porta padrão é 31116. Context: https://hostname:port_number/twsd ... The default is 31116.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para mdm no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Para HCL Workload Automation 9.5 Fix Pack 7 em ambiente Distributed com MDM ou BMDM, o serviço REST usa o contexto HTTPS /twsd e a porta padrão é 31116. Context: https://hostname:port_number/twsd?*

---

### 112. hwa-version-matrix-restv2-intro-10.1-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.1 Fix Pack 1, foi introduzida a REST API V2 para operar o produto tanto pela interface de usuario quanto pela linha de comando?*

---

### 113. hwa-version-matrix-restv2-recommended-10.2.8-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: REST API V2 (HTTPS Port 31116) > Tópico: dwc_api > rest [rest]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a documentacao recomenda explicitamente o uso da REST API V2 para integracoes futuras, por ser mais facil de configurar, mais poderosa e flexivel.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para rest no HWA?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a documentacao recomenda explicitamente o uso da REST API V2 para integracoes futuras, por ser mais facil de configurar, mais poderosa e flexivel?*

---
