# AGENDAMENTO AVANCADO & WORKFLOWS

> Total de tópicos canônicos cobertos nesta seção: 78

---

### 1. com-sla-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
Uma prática organizacional recomendada é definir classes de SLA por criticidade de job (crítico, padrão, batch) e medir o atraso com as métricas que o produto já coleta (ex.: Late_start_runs e Late_end_runs na view JOB_STATISTICS_V, e o monitoramento de jobs críticos via approachingLateOffset/deadlineOffset). O SLA em si é uma decisão da organização, não um padrão prescrito pela HCL.

**Plataforma / Validação:** Distributed

---

### 2. hwa-10.2.0-every-jobstream-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.0, a palavra-chave EVERY inicia repetidamente um job stream ou job em uma taxa especificada.

**Plataforma / Validação:** Distributed

---

### 3. hwa-10.2.8-awsjpl526w-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation Distributed 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > dependency [dependency]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation (10.1.0/10.2.0, Platform Independent; comportamento aplicavel ao planner distribuido), AWSJPL526W e uma mensagem de WARNING do MakePlan: "An external dependency in job stream js=WS#JSXXXX, or a job belonging to it, cannot be resolved because the matching criteria could not be satisfied." A causa e uma dependencia externa (por exemplo um job/job stream apos a keyword FOLLOWS) que nao esta agendado(a) para rodar no dia em que o plano e estendido; o planner simplesmente ignora esse job/job stream. A mensagem nao indica, por si so, um erro — e preciso verificar as dependencias (FOLLOWS, dia de execucao, criterios de condicao).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL526W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL526W no HWA?*

---

### 4. hwa-10.2.8-cal-graphical-designer-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, um calendário pode ser criado no Graphical Designer pela aba Assets, clicando no ícone de adição (+), selecionando Calendar no menu suspenso, informando o nome e selecionando as datas desejadas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um calendário pode ser criado no Graphical Designer pela aba Assets, clicando no ícone de adição (+), selecionando Calendar no menu suspenso, informando o nome e selecionando as datas desejadas?*

---

### 5. hwa-10.2.8-capacity-symphony-file-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
A documentação do HCL Workload Automation 10.2.8 documenta um algoritmo para estimar o tamanho do arquivo Symphony: por instância de Job Scheduler 512 bytes, por instância de job 512 bytes, por string docommand >40 bytes o tamanho da string, por prompt ad hoc 512, por dependência de arquivo 512, por recovery prompt 512 e por recovery job 512; e para dados do banco, por workstation 512, por resource 512, por usuário 256, por prompt 512 e por calendar 512 (se ignoreCalendars off).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 6. hwa-10.2.8-dbviews-audit-0172

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
A view AUDIT_STORE_RECORDS_V do banco do HCL Workload Automation exibe informacoes sobre os registros de auditoria armazenados no banco, e CALENDARS_V exibe informacoes sobre calendarios. Usadas para consultas de auditoria e referencia de calendarios de scheduling. Fonte: IBM Workload Scheduler Database Views.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco AUDIT_STORE_RECORDS_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional AUDIT_STORE_RECORDS_V no banco de dados do HWA?*

---

### 7. hwa-10.2.8-dbviews-catalog-0167

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
O banco de dados do HCL Workload Automation (DB2, Oracle ou MSSQL) expoe views de leitura para consultas e reports (schema MASTER ou equivalente). Catalogo das views mais usadas: JOB_HISTORY_V (historico de jobs), JOB_STATISTICS_V (informacoes sobre jobs), JOB_DEPS_V (jobs/job streams que dependem de um job), JOB_STREAM_DEPS_V (jobs/job streams que dependem de um job stream), PLAN_JOBS_V (jobs no plano), PLAN_JOB_STREAMS_V (job streams no plano), CALENDARS_V (calendarios), LOG_MESSAGES_V (mensagens logadas pelas acoes), EVENT_RULES_V (event rules), EVENT_CONDITIONS_V (eventos associados a cada event rule), EVENT_RULE_ACTIONS_V (acoes associadas a cada event rule), EVENT_RULE_INSTANCES_V (historico de event rules executadas), ACTION_RUNS_V (acoes executadas por event rule), AUDIT_STORE_RECORDS_V (registros de auditoria), FILE_REFS_V (jobs/job streams dependentes de um arquivo), INTERNETWORK_DEPS_V (dependencias internetwork), PLAN_DOMAINS_V (dominios no plano), PLAN_FILES_V (arquivos no plano), PLAN_PROMPTS_V (prompts no plano), PLAN_RESOURCES_V (recursos no plano). As views PLAN_* refletem o plano corrente; as demais, o banco de definicoes e historico. Fonte: IBM Workload Scheduler Database Views (guia de views, aplicavel ao HWA 10.2).

**Plataforma / Validação:** Distributed

---

### 8. hwa-10.2.8-dynagent-backup-resource-advisor-urls-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
A propriedade BackupResourceAdvisorUrls da seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 define a lista de URLs retornadas pelo master em ambiente distribuído ou pelo dynamic domain manager, que o agent usa para se conectar ao master/DDM, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade BackupResourceAdvisorUrls da seção [ResourceAdvisorAgent] do JobManager?*

---

### 9. hwa-10.2.8-dynagent-concurrency-broker-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
There is no component named "concurrency broker" documented in HCL Workload Automation 10.2.8; the broker is composed of the Resource Advisor and Job Dispatcher.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*
- *Qual a regra documentada no HWA Distributed sobre: There is no component named "concurrency broker" documented in HCL Workload Automation 10.2.8; the broker is composed of the Resource Advisor and Job Dispatcher?*

---

### 10. hwa-10.2.8-dynagent-job-dispatcher-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
O JobDispatcherConfig.properties do Dynamic Workload Broker no HCL Workload Automation 10.2.8 documenta o parâmetro FailQInterval, que especifica os segundos para tentar novamente a operação após falhas como notificação de cliente, requisições de Allocation/Reallocate/Cancel Allocation ao Resource Advisor e falhas de banco por conectividade, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*

---

### 11. hwa-10.2.8-dynagent-job-manager-ini-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
As seções documentadas do arquivo JobManager.ini do dynamic agent no HCL Workload Automation 10.2.8 são [ITA], [JobManager.Logging.cclog], [Launchers], [NativeJobLauncher], [JavaJobLauncher], [ResourceAdvisorAgent], [SystemScanner], [Env] e [EventDrivenWorkload], conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*
- *Qual a regra documentada no HWA Distributed sobre: As seções documentadas do arquivo JobManager?*

---

### 12. hwa-10.2.8-dynagent-resource-advisor-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
A seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 configura o agente do Resource Advisor, que escaneia intermitentemente os recursos da máquina (CPU, sistema operacional, file systems e redes) e envia atualizações de status ao master em ambiente distribuído ou ao dynamic domain manager, com as propriedades documentadas ResourceAdvisorUrl, BackupResourceAdvisorUrls, FullyQualifiedHostname, CPUScannerPeriodSeconds, ScannerPeriodSeconds e NotifyToResourceAdvisorPeriodSeconds, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A seção [ResourceAdvisorAgent] do JobManager?*

---

### 13. hwa-10.2.8-dynagent-resource-advisor-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
O Dynamic Workload Broker no HCL Workload Automation 10.2.8 é composto pelos componentes Resource Advisor e Job Dispatcher, cujos parâmetros de configuração são definidos nos arquivos ResourceAdvisorConfig.properties e JobDispatcherConfig.properties, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*

---

### 14. hwa-10.2.8-dynagent-resource-advisor-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
O dynamic agent no HCL Workload Automation 10.2.8 é criado e registrado automaticamente no banco de dados quando o agent é instalado, sendo hospedado pela workstation broker, registrado como 'agent' e aparecendo como atualizado pelo Resource Advisor Agent no Dynamic Workload Console, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*
- *Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?*

---

### 15. hwa-10.2.8-dynagent-resource-advisor-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
O Resource Advisor no Dynamic Workload Broker do HCL Workload Automation 10.2.8 aloca recursos a cada job em intervalos de tempo definidos pelo parâmetro TimeSlotLength (padrão 15 segundos) e, se um job não encontra recurso, espera o intervalo CheckInterval (padrão 60 segundos) antes de tentar novamente, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para resource?*
- *Qual a regra documentada no HWA Distributed sobre: O Resource Advisor no Dynamic Workload Broker do HCL Workload Automation 10.2.8 aloca recursos a cada job em intervalos de tempo definidos pelo parâmetro TimeSlotLength (padrão 15 segundos) e, se um job não encontra recurso, espera o intervalo CheckInterval (padrão 60 segundos) antes de tentar novamente, conforme documentação oficial?*

---

### 16. hwa-10.2.8-dynagent-retry-de-conexo-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
There is no documented connection retry property in JobManager.ini [ResourceAdvisorAgent] section, and no [ServiceLocator] section with provider URL is documented in HCL Workload Automation 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: There is no documented connection retry property in JobManager?*

---

### 17. hwa-10.2.8-dynamic-pool-job-promotion-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para garantir que um trabalho crítico obtenha os recursos necessários em um dynamic pool, são especificadas as variáveis tws.job.promoted (valores YES/NO, indicando se o trabalho é promovido) e tws.job.resourcesForPromoted (definida na definição do dynamic pool, com valores 1 se o trabalho é promovido ou 10 se não é), de modo que um trabalho promovido pode ser executado em um número maior de agentes dinâmicos do pool, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 18. hwa-10.2.8-event-actions-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
As ações no HCL Workload Automation 10.2.8 são classificadas em ações operacionais (que alteram o status de objetos de agendamento, como submeter jobs ou job streams e responder a prompts) e ações de notificação (como enviar email), conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 19. hwa-10.2.8-event-batch-jobs-and-job-streams-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
As principais tarefas da automação orientada a eventos no HCL Workload Automation 10.2.8 incluem acionar a execução de jobs e job streams batch com base em eventos em tempo real, responder a prompts, notificar usuários em condições anômalas e invocar um produto externo, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 20. hwa-10.2.8-event-orchestration-monitor-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
O Orchestration Monitor no HCL Workload Automation 10.2.8 é uma seção do Dynamic Workload Console que funciona como um hub de controle que supervisiona todo o workload associado a um engine específico, permitindo monitorar workstation, job stream, job, resource, prompt e file, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 21. hwa-10.2.8-event-orchestration-monitor-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
The Orchestration Monitor in HCL Workload Automation 10.2.8 Distributed monitors workstations, job streams, jobs, resources, prompts and files; event rules are not documented as monitored items in the Orchestration Monitor overview. Event rule instances are instead monitored in the event processing server logs and database (log.llrc_log_records).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 22. hwa-10.2.8-event-submit-job-stream-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
As ações do provider TWSAction no HCL Workload Automation 10.2.8 são SubmitJobStream, SubmitJob, SubmitAdHocJob e ReplyPrompt, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 23. hwa-10.2.8-event-twsobjects-monitor-events-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
Os eventos do provider TWSObjectsMonitor no HCL Workload Automation 10.2.8 incluem Job Status Changed, Job Submitted, Job Late, Job Stream Completed, Job Stream Late, Workstation Status Changed e Prompt Status Changed, entre outros, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 24. hwa-10.2.8-globalopts-encfresourcequantity-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enCFResourceQuantity (alias rq) define como as quantidades de recursos são contabilizadas nas decisões de carry-forward; neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enCFResourceQuantity (alias rq) define como as quantidades de recursos são contabilizadas nas decisões de carry-forward; neste ambiente está YES?*

---

### 25. hwa-10.2.8-globalopts-enexpandedresources-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enExpandedResources (alias er) habilita recursos expandidos (acima do limite padrão de 64 recursos por workstation); neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enExpandedResources (alias er) habilita recursos expandidos (acima do limite padrão de 64 recursos por workstation); neste ambiente está YES?*

---

### 26. hwa-10.2.8-globalopts-enstartcondsucccrondeadline-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enStartCondSuccOnDeadline (alias od) faz com que uma start condition seja marcada como SUCC quando atinge seu deadline; neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enStartCondSuccOnDeadline (alias od) faz com que uma start condition seja marcada como SUCC quando atinge seu deadline; neste ambiente está YES?*

---

### 27. hwa-10.2.8-globalopts-extrecprompt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global extRecPrompt (alias xp) tem valor '1000' neste ambiente. extRecPrompt | xp Additional prompts after abend. Specify an additional number of prompts for the value defined in baseRecPropmt . This applies when a job is rerun after abending and the limit specified in baseRecPropmt has been reached. Th

**Plataforma / Validação:** Distributed

---

### 28. hwa-10.2.8-globalopts-riskconfidence-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global riskConfidence (alias rc) tem valor '50' neste ambiente. riskConfidence | rc Critical Jobs Risk Confidence Specifies when a critical job must be set as High Risk , comparing the confidence factor of completing before deadline and the percentage specified in this parameter. If the probability of c

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global riskConfidence (alias rc) tem valor '50' neste ambiente?*

---

### 29. hwa-10.2.8-globalopts-startconditiondeadlineoffset-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global startConditionDeadlineOffset (alias cd) tem valor '2400' neste ambiente. startConditionDeadlineOffset | cd Start condition deadline offset. The default offset set for the start condition deadline in 24 hour format: "hhmm" (0001-9959). Specify the time range during which the start condition is active. The default

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global startConditionDeadlineOffset (alias cd) tem valor '2400' neste ambiente?*
- *Qual o propósito e valor padrão da opção global startConditionDeadlineOffset no optman do HWA?*

---

### 30. hwa-10.2.8-gui-designer-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Graphical Designer é aberto em Design > Graphical Designer e possui uma palette com duas abas: Blocks (job streams, jobs, wait jobs e join conditions) e Assets (Calendar, Credentials, Domain, Folder, Job definition, Job stream, Prompt, Resource, Run cycle group, Variable table, Workstation e Workstation class); os itens são salvos no banco de dados ao selecionar Deploy, e o workspace pode ser exportado/importado como JSON e salvo como imagem PNG.

**Plataforma / Validação:** Distributed

---

### 31. hwa-10.2.8-gui-jobstream-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para adicionar um job a um job stream pela Dynamic Workload Console, navega-se em Design > Workload Designer, seleciona-se o engine, escolhe-se o card Job stream, clica-se em Edit no job stream desejado e trabalha-se na view Details ou na view Graphical; na view Details clica-se no sinal de + junto de Jobs e busca-se a definição de job para clicar em Add; na view Graphical clica-se com o botão direito e seleciona-se Add Jobs ou usa-se o campo Search; em ambos é possível marcar o job como Critical.

**Plataforma / Validação:** Distributed

---

### 32. hwa-10.2.8-gui-jobstream-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, é possível criar uma definição de job stream pelo Graphical Designer, adicionar um run cycle e adicionar jobs (arrastando definições da aba Assets) ao job stream; a página oficial 'Managing job stream definitions' documenta esse procedimento.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é possível criar uma definição de job stream pelo Graphical Designer, adicionar um run cycle e adicionar jobs (arrastando definições da aba Assets) ao job stream; a página oficial 'Managing job stream definitions' documenta esse procedimento?*

---

### 33. hwa-10.2.8-gui-sap-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: scheduling > dependency [dependency]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, define-se um evento de background do SAP como dependência internetwork pela Dynamic Workload Console abrindo o Workload Designer (Design > Workload Designer), selecionando o job stream e clicando em Edit, depois em Add Dependency e selecionando Internetwork; nos campos Network Agent informa-se o agente conectado ao sistema SAP e em Dependency informam-se os parâmetros do evento SAP (por exemplo -evtid ... -evtpar ...), clicando em Save para salvar o job stream.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, define-se um evento de background do SAP como dependência internetwork pela Dynamic Workload Console abrindo o Workload Designer (Design > Workload Designer), selecionando o job stream e clicando em Edit, depois em Add Dependency e selecionando Internetwork; nos campos Network Agent informa-se o agente conectado ao sistema SAP e em Dependency informam-se os parâmetros do evento SAP (por exemplo -evtid?*

---

### 34. hwa-10.2.8-incident-bia015i-dst-0085

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > scheduling [scheduling]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBIA015I 'Schedule <workstation>#<schedule> added' — o horario do schedule aparece incorreto (o mesmo pode acontecer com a keyword deadline). Causa: funcoes de data/hora da C-Runtime Library falham ao calcular o horario correto durante a primeira semana do horario de verao (daylight savings time). Resolucao: para o argumento de tempo das keywords at, until ou deadline, especificar um valor diferente do horario de inicio do periodo de producao definido no arquivo de opcoes globais — os valores devem diferir por mais ou menos uma hora. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA015I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA015I no HWA?*
- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *O que causa e como solucionar o problema: AWSBIA015I 'Schedule <workstation>#<schedule> added' — o horario do schedule aparece incorreto (o mesmo pode acontecer com a keyword deadline)?*

---

### 35. hwa-10.2.8-incident-prompt-number-0094

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > prompt [prompt]]`

**Regra Canônica / Evidência:**
Sintoma: ao submeter um job ou Job Scheduler dependente de um prompt ad-hoc, o conman nao consegue submeter por causa do prompt number. Causa: no master domain manager, prompts sao criados no plano com um prompt number unico mantido em arquivo; o JnextPlan inicia o prompt number em 1 e incrementa a cada prompt; ao submeter com prompt ad-hoc em outro agent durante a vigencia do plano, o numero pode conflitar. Resolucao: modificar o ultimo prompt number garantindo que o digito menos significativo esteja na posicao 21 (ex.: '98' → '2098' substituindo dois espacos por '20'); salvar e reexecutar o submit. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar prompt?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: ao submeter um job ou Job Scheduler dependente de um prompt ad-hoc, o conman nao consegue submeter por causa do prompt number?*

---

### 36. hwa-10.2.8-incident-rerun-recovery-cross-domain-0116

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > recovery [recovery]]`

**Regra Canônica / Evidência:**
Sintoma: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta. Causa: o recovery job foi especificado para rodar em uma workstation e dominio diferentes do job original; o job original nao consegue detectar o estado do recovery job, portanto nao determina se ele terminou ou em que estado. Resolucao: para o job especifico ainda em 'running', resolver o estado manualmente; para novos jobs, configurar o recovery job na mesma workstation/dominio. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta?*
- *O que causa e como solucionar o problema: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta?*

---

### 37. hwa-10.2.8-monitor-calendars-v-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > calendar [calendar]]`

**Regra Canônica / Evidência:**
A view CALENDARS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre calendários de agendamento, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A view CALENDARS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre calendários de agendamento, conforme documentação oficial?*

---

### 38. hwa-10.2.8-monitor-dashboard-widgets-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
Os widgets documentados do Workload Dashboard no HCL Workload Automation 10.2.8 incluem Engines, Available workstations, Unavailable workstations, Pending Prompts, Critical job status, Job status, Jobs in late, Jobs in error, Min duration, Max duration e Resources, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 39. hwa-10.2.8-monitor-plan-jobs-v-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
A view PLAN_JOBS_V no HCL Workload Automation 10.2.8 é documentada com colunas-chave de consulta do plano como Job_id, Job_name, Job_stream_name, Scheduled_time, Status, Return_code, Priority e Deadline, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 40. hwa-10.2.8-monitor-plan-resources-v-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
A view PLAN_RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os recursos (resources) presentes no plano, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco PLAN_RESOURCES_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional PLAN_RESOURCES_V no banco de dados do HWA?*

---

### 41. hwa-10.2.8-monitor-prompts-v-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
A view PROMPTS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre prompts, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 42. hwa-10.2.8-monitor-resources-v-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
A view RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre recursos (resources) definidos, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A view RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre recursos (resources) definidos, conforme documentação oficial?*

---

### 43. hwa-10.2.8-perf-every-minimal-0166

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), a opcao 'EVERY' cria nova instancia de job stream ou job no plano; em job-level ela causa multiplos 'sbj' internos ao mesmo job stream instance que podem afetar a performance das atualizacoes do plano. Importante verificar se EVERY e usado com valores minimos (poucos minutos) para evitar aumentar o numero de jobs num job stream (algumas centenas de jobs podem impactar performance). Metodologias: mover EVERY para job stream level se possivel; dividir o job stream em multiplos com 'AT xx till xx' (time partitioning). Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.4).

**Plataforma / Validação:** Distributed

---

### 44. hwa-10.2.8-prompt-globalnamed-prompt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
Uma prompt é uma pergunta operacional textual; um job/job stream com prompt não conclui o processamento de dependências até que o usuário designado forneça resposta; reply responde prompts; prompts predefinidas (globais, no banco, reutilizáveis) vs ad hoc (locais ao job).

**Plataforma / Validação:** Distributed

---

### 45. hwa-10.2.8-resource-resource-syntax-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
Sintaxe de recurso: $resource workstation#resourcename units "description"; o nome do recurso pode ter até 8 caracteres alfanuméricos incluindo - e _, iniciando com letra; a quantidade normalmente varia de 0 a 1024.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintaxe de recurso: $resource workstation#resourcename units "description"; o nome do recurso pode ter até 8 caracteres alfanuméricos incluindo - e _, iniciando com letra; a quantidade normalmente varia de 0 a 1024.?*

---

### 46. hwa-10.2.8-runbook-database-view-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: incidents > recovery [recovery]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V também registra a opção de recuperação (Recovery_option) de cada job com valores possíveis C (Continue), R (Rerun) e S (Stop), além de Recovery_repeat_interval e Recovery_repeat_occurrences.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?*

---

### 47. hwa-10.2.8-runbook-recovery-option-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > runbook [recovery_continue]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção de recuperação 'continue' é uma opção de recuperação definida na definição do job (job definition): se o job termina de forma anormal, o produto continua com o próximo job (do job stream), não sendo um parâmetro do comando rerun.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção de recuperação 'continue' é uma opção de recuperação definida na definição do job (job definition): se o job termina de forma anormal, o produto continua com o próximo job (do job stream), não sendo um parâmetro do comando rerun?*

---

### 48. hwa-10.2.8-runbook-recovery-option-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção de recuperação 'rerun' (na definição do job) faz com que, se o job terminar de forma anormal, o job seja rerun, podendo ser combinada com 'repeatevery hhmm for number attempts' e 'rerun after prompt' para controlar a sequência de rerun.

**Plataforma / Validação:** Distributed

---

### 49. hwa-10.2.8-runbook-rerun-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, quando o rerun usa a opção ;from, as opções de recuperação (recovery options) são parcialmente herdadas da definição original e parcialmente obtidas do job 'from': a opção de recuperação 'stop' e 'continue' são recuperadas do job 'from' (NÃO herdadas do job original), enquanto 'rerun', 'repeatevery', 'for', 'after' e 'abendprompt' são herdadas do job original.

**Plataforma / Validação:** Distributed

---

### 50. hwa-10.2.8-runcycle-graphical-designer-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > runcycle [runcycle]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation, desde a versão 10.2.4, os run cycle groups podem ser criados e atribuídos como Triggers a job streams diretamente no Graphical Designer, funcionando como objetos de agendamento reutilizáveis.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation, desde a versão 10.2.4, os run cycle groups podem ser criados e atribuídos como Triggers a job streams diretamente no Graphical Designer, funcionando como objetos de agendamento reutilizáveis?*

---

### 51. hwa-10.2.8-sec-variable-table-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > vartable [vartable]]`

**Regra Canônica / Evidência:**
A segurança de variable tables no HCL Workload Automation 10.2.8 é controlada no security file por meio da keyword vartable (ex.: vartable name=@ access=add,delete,display,modify,list,use,unlock), e a permissão é concedida no nível da tabela, não no nível de cada variável individual.

**Plataforma / Validação:** Distributed

---

### 52. hwa-10.2.8-showprompts-states-0038

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > prompt [prompt]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, showprompts/sp usa ASKED para prompt emitido sem resposta e INACT para prompt ainda não emitido. Context: ASKED The prompt was issued, but no reply was given. INACT The prompt has not been issued.

**Plataforma / Validação:** Distributed

---

### 53. hwa-10.2.8-showresources-available-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > resource [resource]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, no formato standard de showresources, Available é o número de unidades de recurso não alocadas. Context: Available — The number of resource units that have not been allocated.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, no formato standard de showresources, Available é o número de unidades de recurso não alocadas?*

---

### 54. hwa-10.2.8-tune-bm-check-deadline-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
A opção bm check deadline no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar se um job perdeu seu deadline, com padrão documentado de zero (desabilitada); deadlines de jobs críticos são avaliados automaticamente, independentemente desta opção.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm check deadline no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar se um job perdeu seu deadline, com padrão documentado de zero (desabilitada); deadlines de jobs críticos são avaliados automaticamente, independentemente desta opção?*

---

### 55. hwa-10.2.8-tune-bm-late-every-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
A opção bm late every no localopts do HCL Workload Automation 10.2.8 especifica, em minutos, o máximo de tempo que pode decorrer antes que o HCL Workload Automation pule um job every que não iniciou em sua hora esperada; aplica-se apenas a jobs definidos com every junto com a dependência de horário at.

**Plataforma / Validação:** Distributed

---

### 56. hwa-10.2.8-variable-plan-generation-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > vartable [variable_resolution]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a ordem de resolução de variáveis na geração do plano é: run cycle, job stream, workstation e tabela padrão (apenas para ^variablename^); na submissão de um job stream, a ordem é: especificada na submissão, job stream, workstation e tabela padrão (apenas para ^variablename^).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a ordem de resolução de variáveis na geração do plano é: run cycle, job stream, workstation e tabela padrão (apenas para ^variablename^); na submissão de um job stream, a ordem é: especificada na submissão, job stream, workstation e tabela padrão (apenas para ^variablename^)?*

---

### 57. hwa-10.2.8-vm-9f-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
A palavra-chave CRITICAL (job mission-critical) e a opção global enWorkloadServiceAssurance (alias wa) existem e são idênticas no HCL Workload Automation Distributed 10.2.0 e 10.2.8. enWorkloadServiceAssurance tem valor padrão YES em ambas; jobs critical exigem deadline.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A palavra-chave CRITICAL (job mission-critical) e a opção global enWorkloadServiceAssurance (alias wa) existem e são idênticas no HCL Workload Automation Distributed 10.2.0 e 10.2.8. enWorkloadServiceAssurance tem valor padrão YES em ambas; jobs critical exigem deadline?*
- *Qual o propósito e valor padrão da opção global enWorkloadServiceAssurance no optman do HWA?*

---

### 58. hwa-10.2.8-vm-9f-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > runcycle [runcycle]]`

**Regra Canônica / Evidência:**
A palavra-chave runcyclegroup (sem $) com vartable e on runcycle <name> "FREQ=..." ... end, com nome de até 8 caracteres, é suportada na definição de job stream do HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica.

**Plataforma / Validação:** Distributed

---

### 59. hwa-10.2.8-vm-9f-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
A definição de recuperação de job RECOVERY RERUN [same_workstation] [repeatevery hhmm] [for number attempts] é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica. A palavra-chave onlate aceita apenas a ação kill em ambas as versões.

**Plataforma / Validação:** Distributed

---

### 60. hwa-10.2.8-wsa-confidence-factor-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para cada trabalho crítico é fornecido um Confidence Factor percentual que indica a confiança de que o trabalho crítico cumprirá seu deadline; quando o trabalho termina, o fator é sobrescrito para 0% se o deadline estimado foi excedido e para 100% se não foi, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para cada trabalho crítico é fornecido um Confidence Factor percentual que indica a confiança de que o trabalho crítico cumprirá seu deadline; quando o trabalho termina, o fator é sobrescrito para 0% se o deadline estimado foi excedido e para 100% se não foi, conforme documentação oficial?*

---

### 61. hwa-10.2.8-wsa-critical-network-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, definir um trabalho crítico e seu deadline dispara o cálculo dos horários de início de todos os trabalhos que são predecessores do trabalho crítico, sendo o conjunto de predecessores denominado critical network (rede crítica), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, definir um trabalho crítico e seu deadline dispara o cálculo dos horários de início de todos os trabalhos que são predecessores do trabalho crítico, sendo o conjunto de predecessores denominado critical network (rede crítica), conforme documentação oficial?*

---

### 62. hwa-10.2.8-wsa-critical-path-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o critical path é a cadeia de dependências, que leva ao trabalho crítico, mais em risco de causar a perda do deadline em um dado momento; é construído retrocedendo a partir do trabalho crítico, selecionando o predecessor com o maior horário de término estimado, e é recalculado automaticamente se o horário de término real diferir substancialmente do estimado, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o critical path é a cadeia de dependências, que leva ao trabalho crítico, mais em risco de causar a perda do deadline em um dado momento; é construído retrocedendo a partir do trabalho crítico, selecionando o predecessor com o maior horário de término estimado, e é recalculado automaticamente se o horário de término real diferir substancialmente do estimado, conforme documentação oficial?*

---

### 63. hwa-10.2.8-wsa-critical-start-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o critical start time aplica-se apenas a sistemas distribuídos e representa o último horário em que o trabalho pode iniciar sem fazer o trabalho crítico perder o deadline, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o critical start time aplica-se apenas a sistemas distribuídos e representa o último horário em que o trabalho pode iniciar sem fazer o trabalho crítico perder o deadline, conforme documentação oficial?*

---

### 64. hwa-10.2.8-wsa-critical-start-time-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Time Planner calcula o critical start time (horário de início crítico), que é o último horário em que o trabalho pode iniciar para cumprir seu deadline, e, retrocedendo a partir dele, calcula o último horário em que cada predecessor da rede crítica pode iniciar, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Time Planner calcula o critical start time (horário de início crítico), que é o último horário em que o trabalho pode iniciar para cumprir seu deadline, e, retrocedendo a partir dele, calcula o último horário em que cada predecessor da rede crítica pode iniciar, conforme documentação oficial?*

---

### 65. hwa-10.2.8-wsa-deadline-offset-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global deadlineOffset (abreviação do) fornece um deslocamento usado para calcular o critical start time quando o deadline está ausente tanto para o trabalho crítico quanto para seu job stream, assumindo como deadline do trabalho crítico o fim do plano mais esse deslocamento (expresso em minutos); o padrão é 2 minutos, e quando o plano é estendido os horários de início desses trabalhos críticos são automaticamente alterados para coincidir com o novo horário de término do plano, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global deadlineOffset (abreviação do) fornece um deslocamento usado para calcular o critical start time quando o deadline está ausente tanto para o trabalho crítico quanto para seu job stream, assumindo como deadline do trabalho crítico o fim do plano mais esse deslocamento (expresso em minutos); o padrão é 2 minutos, e quando o plano é estendido os horários de início desses trabalhos críticos são automaticamente alterados para coincidir com o novo horário de término do plano, conforme documentação oficial?*
- *Qual o propósito e valor padrão da opção global deadlineOffset no optman do HWA?*

---

### 66. hwa-10.2.8-wsa-designer-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, um trabalho pode ser marcado como crítico usando as funções do Workload Designer no Dynamic Workload Console ao adicioná-lo a um job stream, podendo o deadline ser definido no nível do trabalho ou do job stream, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um trabalho pode ser marcado como crítico usando as funções do Workload Designer no Dynamic Workload Console ao adicioná-lo a um job stream, podendo o deadline ser definido no nível do trabalho ou do job stream, conforme documentação oficial?*

---

### 67. hwa-10.2.8-wsa-high-risk-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, um status de risco pode ser definido para o trabalho crítico: high risk quando os tempos calculados mostram que o trabalho crítico terminará após seu deadline, e potential risk quando trabalhos predecessores críticos foram adicionados à hot list, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um status de risco pode ser definido para o trabalho crítico: high risk quando os tempos calculados mostram que o trabalho crítico terminará após seu deadline, e potential risk quando trabalhos predecessores críticos foram adicionados à hot list, conforme documentação oficial?*

---

### 68. hwa-10.2.8-wsa-hot-list-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, trabalhos da rede crítica que tenham impacto real ou potencial no cumprimento do deadline do trabalho crítico são adicionados a uma hot list associada ao trabalho crítico; apenas os trabalhos que iniciam a rede crítica atual (sem predecessor) podem ser incluídos na hot list, por razões como erro, duração excedendo o longDurationThreshold, ou trabalho ainda não iniciado com o critical start time quase atingido, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, trabalhos da rede crítica que tenham impacto real ou potencial no cumprimento do deadline do trabalho crítico são adicionados a uma hot list associada ao trabalho crítico; apenas os trabalhos que iniciam a rede crítica atual (sem predecessor) podem ser incluídos na hot list, por razões como erro, duração excedendo o longDurationThreshold, ou trabalho ainda não iniciado com o critical start time quase atingido, conforme documentação oficial?*

---

### 69. hwa-10.2.8-wsa-plan-monitor-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Plan Monitor verifica constantemente a rede crítica para assegurar o cumprimento do deadline; quando ocorrem mudanças que afetam os tempos (adição/remoção de trabalhos ou dependências follows), ele solicita ao Time Planner o recálculo dos horários críticos, e, quando um trabalho da rede é concluído, os tempos dos trabalhos seguintes são recalculados considerando a duração real, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Plan Monitor verifica constantemente a rede crítica para assegurar o cumprimento do deadline; quando ocorrem mudanças que afetam os tempos (adição/remoção de trabalhos ou dependências follows), ele solicita ao Time Planner o recálculo dos horários críticos, e, quando um trabalho da rede é concluído, os tempos dos trabalhos seguintes são recalculados considerando a duração real, conforme documentação oficial?*

---

### 70. hwa-9.5-real-enlegacyid-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: scheduling > jobstream [jobstream]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5 (IBM Workload Scheduler), a opcao global enLegacyId (legacy job stream identifier mode, usada em TWS 8.x) NAO e mais suportada: a partir da 9.5 ela foi removida, o identificador de job stream (jobstream_id) passa a ser gerado conforme descrito no comando showjobs, e job streams com carry forward passam a manter seus nomes e identificadores originais (reportando entre chaves {} a data do carry forward). Comportamento real e distinto da 8.x; generalizar o modo legado da 8.x para 9.5 produz resposta errada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5 (IBM Workload Scheduler), a opcao global enLegacyId (legacy job stream identifier mode, usada em TWS 8.x) NAO e mais suportada: a partir da 9.5 ela foi removida, o identificador de job stream (jobstream_id) passa a ser gerado conforme descrito no comando showjobs, e job streams com carry forward passam a manter seus nomes e identificadores originais (reportando entre chaves {} a data do carry forward)?*

---

### 71. hwa-9.5-real-wsa-basico-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > deadline [deadline]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5, o Workload Service Assurance (WSA) existe e e controlado pela opcao global enWorkloadServiceAssurance (wa, padrao yes) e gerencia o processamento privilegiado de jobs criticos (mission-critical) e seus predecessores, com offsets globais como approachingLateOffset, deadlineOffset e promotionOffset. Em 9.5 o WSA e a forma classica/basica de garantir jobs criticos; a taxonomia expandida e integracao com dynamic agents e um comportamento posterior (10.1+).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para deadline?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5, o Workload Service Assurance (WSA) existe e e controlado pela opcao global enWorkloadServiceAssurance (wa, padrao yes) e gerencia o processamento privilegiado de jobs criticos (mission-critical) e seus predecessores, com offsets globais como approachingLateOffset, deadlineOffset e promotionOffset?*

---

### 72. hwa-lab-10.2.8-cross-workstation-dependency-fta-dyn-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent & Dynamic Agent > Interface: CLI composer / conman > Tópico: scheduling > dependencies [cross_workstation]]`

**Regra Canônica / Evidência:**
No HWA 10.2.8, uma dependência cruzada entre tecnologias heterogêneas (um job em Dynamic Agent com FOLLOWS apontando para um job em Fault-Tolerant Agent) é mantida de forma íntegra pelo Batchman: o job do Dynamic Agent permanece retido em HOLD até a conclusão com SUCC do job no FTA, liberando imediatamente o despacho via Broker.

**Plataforma / Validação:** Distributed; Linux x86_64; containers tws-hwa e tws-agent; HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *É possível configurar uma dependência FOLLOWS entre um job rodando em Dynamic Agent e um job em FTA?*
- *Como o Batchman resolve dependências cruzadas entre agentes dinâmicos e agentes tolerantes a falhas?*

---

### 73. hwa-lab-10.2.8-dynamic-pool-load-balancing-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman / composer > Tópico: scheduling > load_balancing [dynamic_pool]]`

**Regra Canônica / Evidência:**
Um Dynamic Workload Broker Pool (TYPE POOL) contendo múltiplos agentes dinâmicos membros (ex: MDMDA local e TWS-AGENT_1 remoto) distribui automaticamente as instâncias de jobs concorrentes entre os membros saudáveis, registrando na saída do conman showjobs o agente executor entre chaves (ex: {MDMDA}, {TWS-AGENT_1}).

**Plataforma / Validação:** Distributed; Linux x86_64; containers tws-hwa e tws-agent; HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como o Dynamic Workload Console e o conman indicam qual agente de um pool executou determinado job?*
- *Como configurar balanceamento de carga de jobs entre múltiplos agentes dinâmicos em um dynamic pool?*

---

### 74. hwa-lab-10.2.8-interactive-prompts-and-conman-reply-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Human Approval (PROMPT) > Interface: CLI composer / conman showprompts / reply > Tópico: scheduling > governance [prompt_workflow]]`

**Regra Canônica / Evidência:**
No HWA 10.2.8, prompts de interação humana ($PROMPT) possuem limite estrito de 8 caracteres no nome e, quando vinculados a um job, retêm o job em HOLD com anotação do prompt ID (ex: #505(PRM_LAB)) e o job stream em estado STUCK. A lista de pendências é visualizada via 'conman showprompts' (estado ASKED) e liberada imediatamente pelo operador com o comando 'conman reply <id>;yes', promovendo o job para execução e conclusão com SUCC.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como funciona a dependência de aprovação humana por PROMPT no HWA e qual o tamanho máximo do seu nome?*
- *Qual comando conman exibe os prompts pendentes aguardando resposta do operador?*
- *Como o operador responde e libera um prompt no conman?*

---

### 75. hwa-lab-10.2.8-message-ita034i-0152

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: scheduling > every [every]]`

**Regra Canônica / Evidência:**
AWSITA034I: mensagem informativa do JobManager relacionada a execucao de jobs com EVERY no dynamic agent. Observada no lab: uma submissao ad hoc da stream CPLXJOB2M com job-level EVERY 0002 executou a primeira instancia de CPLX_EVERY as 14:59 e a segunda as 15:01; ambas completaram SUCC com return code 0. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA034I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA034I no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para every?*

---

### 76. hwa-lab-10.2.8-scheduling-needs-resource-naming-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Composer / Workload Planning Engine > Interface: CLI composer > Tópico: scheduling > resources [needs_limit]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o utilitário composer impõe um limite estrito de no máximo 8 caracteres para o nome de um recurso lógico ($RESOURCE), rejeitando nomes maiores com o erro AWSJOM012E. Recursos definidos com até 8 caracteres são consumidos com sucesso pela cláusula NEEDS dentro do Job Stream.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Qual é o tamanho máximo permitido para o nome de um recurso lógico no HWA composer?*
- *O que causa o erro AWSJOM012E ao criar um objeto $RESOURCE no composer?*
- *Como configurar uma dependência de recurso lógico compartilhado usando a cláusula NEEDS?*

---

### 77. hwa-lab-10.2.8-scheduling-recovery-rerun-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Batchman / Job Recovery > Interface: CLI composer / conman > Tópico: scheduling > recovery [rerun_action]]`

**Regra Canônica / Evidência:**
Ao configurar a instrução RECOVERY RERUN na definição de um job no HWA 10.2.8, quando a execução primária falha com return code diferente de zero (ABEND), o Batchman dispara automaticamente e de forma instantânea uma nova tentativa (>>rerun as) que, ao concluir com código 0, promove o job para SUCC.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como funciona a recuperação automática de jobs com a diretiva RECOVERY RERUN no HWA?*
- *O que indica a anotação '>>rerun as' na saída do comando conman showjobs?*
- *Um job que falha na primeira tentativa pode se recuperar automaticamente sem intervenção manual do operador?*

---

### 78. hwa-lab-10.2.8-vartable-resolution-and-missing-vars-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Variable Table (VARTABLE) > Interface: CLI composer / conman stdlist > Tópico: scheduling > vartable [dynamic_resolution]]`

**Regra Canônica / Evidência:**
No HWA 10.2.8, variáveis definidas em uma VARTABLE e referenciadas no JCL com circunflexos (^VAR^) são resolvidas e interpoladas dinamicamente pelo Batchman no momento do despacho para o Jobman. Se uma variável referenciada não existir na tabela associada nem na tabela default (MAIN_TABLE), o HWA não interrompe o parsing nem cancela a submissão, repassando a string literal original com circunflexos (^VAR_NAME^) para a execução do script.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como funciona a interpolação de variáveis de uma VARTABLE no JCL de um job do HWA?*
- *O que acontece em tempo de execução quando um job referencia uma variável inexistente em sua VARTABLE?*
- *Qual é o comportamento do Batchman ao despachar um job com sintaxe ^VAR^ para o Jobman?*

---
