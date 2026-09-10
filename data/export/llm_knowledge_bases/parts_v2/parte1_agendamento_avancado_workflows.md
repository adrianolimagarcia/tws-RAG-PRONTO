# PARTE1 AGENDAMENTO AVANCADO WORKFLOWS

## I. Agendamento Avancado & Workflows

> 74 registros.

---

### 1. `hwa-10.2.0-every-jobstream-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.0, a palavra-chave EVERY inicia repetidamente um job stream ou job em uma taxa especificada.

> **ATENCAO / RESSALVAS DE USO:** A sintaxe permite EVERY em run cycle de job stream com EVERYENDTIME e em job statement. Esta evidência não estabelece comportamento específico de 10.2.6 ou 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | keyword=EVERY, objects=['job stream', 'job'], effect=repeated launch at specified rate |
| Produto | HCL Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Job stream definition |
| Citacao de suporte | every — Launches a job stream or a job repeatedly at a specified rate. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | jobstream |
| Modo de operacao | read |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | other |
| Familia | every-jobstream |


---

### 2. `hwa-10.2.8-awsjpl526w-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `dependency`

**Afirmacao / Conteudo:**

Em HCL Workload Automation (10.1.0/10.2.0, Platform Independent; comportamento aplicavel ao planner distribuido), AWSJPL526W e uma mensagem de WARNING do MakePlan: "An external dependency in job stream js=WS#JSXXXX, or a job belonging to it, cannot be resolved because the matching criteria could not be satisfied." A causa e uma dependencia externa (por exemplo um job/job stream apos a keyword FOLLOWS) que nao esta agendado(a) para rodar no dia em que o plano e estendido; o planner simplesmente ignora esse job/job stream. A mensagem nao indica, por si so, um erro — e preciso verificar as dependencias (FOLLOWS, dia de execucao, criterios de condicao).

> **ATENCAO / RESSALVAS DE USO:** Fonte IBM Support oficial localizada (pesquisa Perplexity 2026-08-19). O catalogo AWSJPL nao e publicado como pagina web individual na 10.2.8, mas o Troubleshooting Guide 10.2.8 (awstrmst.pdf) cobre mensagens AWSJPL/MakePlan. Mantem-se escopo generico (10.1.0/10.2.0) ja que a pagina IBM cobre essas versoes. Pesquisa Perplexity Direct (2026-08-23): AWSJPL526W e warning de dependencia externa nao resolvida no MakePlan; nao indica falha por si so — o planner ignora dependencias nao agendadas para o dia; verificar criterios de FOLLOWS e agendamento do job dependente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSJPL526W, component=planner/MakePlan, status=unconfirmed |
| Produto | HCL Workload Automation Distributed |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://www.ibm.com/support/pages/node/7248487 |
| Titulo da fonte | AWSJPL526W in MAKEPLAN - IBM Support (IBM Workload Automation 10.1.0;10.2.0, Platform Independent) |
| Citacao de suporte | AWSJPL526W An external dependency in job stream "js=WS#JSXXXX", or a job belonging to it, cannot be resolved because the matching criteria could not be satisfied. AWSJPL526W is warning message and it does not always mean a problem. AWSJPL526W can happen when an external dependency cannot be resolved. For example, the job/job stream after the FOLLOWS keyword is not scheduled to run on the day for the plan to be extended, in that case the planner will just ignore that job/job stream. |
| Coletado em | 2026-08-19 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | dependency |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | message |
| Ferramenta | planner |
| Codigo da mensagem | AWSJPL526W |
| Componente | planner/MakePlan |
| Familia | awsjpl526w-0001 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL526W no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL526W no HWA?


---

### 3. `hwa-10.2.8-cal-graphical-designer-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, um calendário pode ser criado no Graphical Designer pela aba Assets, clicando no ícone de adição (+), selecionando Calendar no menu suspenso, informando o nome e selecionando as datas desejadas.

> **ATENCAO / RESSALVAS DE USO:** Procedimento de criação de calendário via Dynamic Workload Console (DWC). O exemplo usa a data 26 de novembro de 2024. A página awsrgcalendef.html documenta a definição equivalente via composer ($calendar).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | calendar=calendário, Graphical Designer=Designer Gráfico, Assets tab=aba Assets, add + icon=ícone de adição (+), Calendar=Calendar (item de menu), Date selection=seleção de datas |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/calendar_dwc.html |
| Titulo da fonte | Managing calendar definitions |
| Citacao de suporte | From the Graphical Designer, select the Assets tab and click on the add + icon. From the drop-down menu, select Calendar. In Name, type the name Campaign_celebration. In Date selection, select the day 26th of November. Click Add. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | calendar |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | gui |
| Familia | cal-graphical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um calendário pode ser criado no Graphical Designer pela aba Assets, clicando no ícone de adição (+), selecionando Calendar no menu suspenso, informando o nome e selecionando as datas desejadas?


---

### 4. `hwa-10.2.8-cal-job-stream-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `calendar`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, um calendário criado pode ser adicionado a um job stream arrastando-o da aba Assets para o workspace do job stream no Graphical Designer e, em seguida, implantando (Deploy) o workspace.

> **ATENCAO / RESSALVAS DE USO:** O calendário é associado ao job stream como exceção (run calendar) para que o job stream execute em um dia não coberto pelo run cycle. A implantação (Deploy) é necessária para gravar a alteração no banco de dados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | job stream=job stream, Assets tab=aba Assets, drag=arrastar, workspace=workspace, Deploy=implantar |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/calendar_dwc.html |
| Titulo da fonte | Managing calendar definitions |
| Citacao de suporte | Expand the Calendar menu, and then drag the Campaign_celebration calendar into the wf_newsletter_1 job stream in the workspace. Deploy the workspace. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | calendar_definition |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | gui |
| verbs | deploy |
| Familia | cal-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um calendário criado pode ser adicionado a um job stream arrastando-o da aba Assets para o workspace do job stream no Graphical Designer e, em seguida, implantando (Deploy) o workspace?


---

### 5. `hwa-10.2.8-capacity-symphony-file-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

A documentação do HCL Workload Automation 10.2.8 documenta um algoritmo para estimar o tamanho do arquivo Symphony: por instância de Job Scheduler 512 bytes, por instância de job 512 bytes, por string docommand >40 bytes o tamanho da string, por prompt ad hoc 512, por dependência de arquivo 512, por recovery prompt 512 e por recovery job 512; e para dados do banco, por workstation 512, por resource 512, por usuário 256, por prompt 512 e por calendar 512 (se ignoreCalendars off).

> **ATENCAO / RESSALVAS DE USO:** Algoritmo oficial de estimativa de crescimento do arquivo Symphony.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Symphony file=arquivo Symphony, Job Scheduler instance=instância de Job Scheduler |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadavoidfullfilesys.html |
| Titulo da fonte | Avoiding full file systems |
| Citacao de suporte | Per job instance: 512... Per workstation: 512... multiply them by the indicated size in bytes, and sum them to find the approximate Symphony file size. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | capacity-symphony |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 6. `hwa-10.2.8-dbviews-audit-0172`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

A view AUDIT_STORE_RECORDS_V do banco do HCL Workload Automation exibe informacoes sobre os registros de auditoria armazenados no banco, e CALENDARS_V exibe informacoes sobre calendarios. Usadas para consultas de auditoria e referencia de calendarios de scheduling. Fonte: IBM Workload Scheduler Database Views.

> **ATENCAO / RESSALVAS DE USO:** Extraido do awsdvmst.pdf.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | IBM Workload Scheduler Database Views - Audit and calendars |
| Citacao de suporte | AUDIT_STORE_RECORDS_V displays information about the auditing records stored in the database. CALENDARS_V displays information about calendars. |
| Coletado em | 2026-08-23 |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; referencia. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=dbviews |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | dbviews-audit |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco AUDIT_STORE_RECORDS_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional AUDIT_STORE_RECORDS_V no banco de dados do HWA?


---

### 7. `hwa-10.2.8-dbviews-catalog-0167`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

O banco de dados do HCL Workload Automation (DB2, Oracle ou MSSQL) expoe views de leitura para consultas e reports (schema MASTER ou equivalente). Catalogo das views mais usadas: JOB_HISTORY_V (historico de jobs), JOB_STATISTICS_V (informacoes sobre jobs), JOB_DEPS_V (jobs/job streams que dependem de um job), JOB_STREAM_DEPS_V (jobs/job streams que dependem de um job stream), PLAN_JOBS_V (jobs no plano), PLAN_JOB_STREAMS_V (job streams no plano), CALENDARS_V (calendarios), LOG_MESSAGES_V (mensagens logadas pelas acoes), EVENT_RULES_V (event rules), EVENT_CONDITIONS_V (eventos associados a cada event rule), EVENT_RULE_ACTIONS_V (acoes associadas a cada event rule), EVENT_RULE_INSTANCES_V (historico de event rules executadas), ACTION_RUNS_V (acoes executadas por event rule), AUDIT_STORE_RECORDS_V (registros de auditoria), FILE_REFS_V (jobs/job streams dependentes de um arquivo), INTERNETWORK_DEPS_V (dependencias internetwork), PLAN_DOMAINS_V (dominios no plano), PLAN_FILES_V (arquivos no plano), PLAN_PROMPTS_V (prompts no plano), PLAN_RESOURCES_V (recursos no plano). As views PLAN_* refletem o plano corrente; as demais, o banco de definicoes e historico. Fonte: IBM Workload Scheduler Database Views (guia de views, aplicavel ao HWA 10.2).

> **ATENCAO / RESSALVAS DE USO:** Consolidado do awsdvmst.pdf (Database Views, 94 paginas). Views de reporting para queries SQL.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | IBM Workload Scheduler Database Views - catalogo de views |
| Citacao de suporte | JOB_HISTORY_V displays information about job history. JOB_DEPS_V displays information about jobs and job streams that depend on a job. PLAN_JOBS_V displays information about jobs in the plan. |
| Coletado em | 2026-08-23 |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; referencia. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=dbviews |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | scheduler |
| verbs | plan |
| Familia | dbviews-catalog |


---

### 8. `hwa-10.2.8-dbviews-deps-0171`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

As views de dependencia do banco do HCL Workload Automation: JOB_DEPS_V (jobs/job streams que dependem de um job), JOB_STREAM_DEPS_V (jobs/job streams que dependem de um job stream), FILE_REFS_V (jobs/job streams que dependem de um arquivo), INTERNETWORK_DEPS_V (jobs/job streams que dependem de uma dependencia internetwork) e JOB_DEFINITION_REFS_V (job streams em que um job aparece). Usadas para consultar a teia de dependencias de um objeto (quem depende de quem). Fonte: IBM Workload Scheduler Database Views.

> **ATENCAO / RESSALVAS DE USO:** Extraido do awsdvmst.pdf.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | IBM Workload Scheduler Database Views - Dependency views |
| Citacao de suporte | JOB_DEPS_V displays information about jobs and job streams that depend on a job. JOB_STREAM_DEPS_V displays information about jobs and job streams that depend on a job stream. |
| Coletado em | 2026-08-23 |
| Capacidade | db_views_dependencies |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; referencia. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=dbviews |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | dbviews-deps |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_STREAM_DEPS_V no HCL Workload Automation?
- Qual é o propósito da view de banco JOB_DEPS_V no HCL Workload Automation?
- Como consultar dependências e definições utilizando a view JOB_DEPS_V no banco de dados?


---

### 9. `hwa-10.2.8-dynagent-resource-advisor-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

O dynamic agent no HCL Workload Automation 10.2.8 é criado e registrado automaticamente no banco de dados quando o agent é instalado, sendo hospedado pela workstation broker, registrado como 'agent' e aparecendo como atualizado pelo Resource Advisor Agent no Dynamic Workload Console, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: fluxo de registro automático do dynamic agent e definição automática de workstation.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic agent=workstation dinâmica que gerencia vários tipos de job, Resource Advisor Agent=componente que atualiza o dynamic agent no console, registro automático=criação e registro no banco durante a instalação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | This workstation is automatically created and registered in the HCL Workload Automation database when you install the agent. The agent is hosted by the workload broker workstation. Because the installation and registration processes are performed automatically, when you view the agent in the Dynamic Workload Console, it results as updated by the Resource Advisor Agent. This workstation is registered in the HCL Workload Automation database as agent. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-resource |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para resource?
- Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?


---

### 10. `hwa-10.2.8-dynamic-pool-job-promotion-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para garantir que um trabalho crítico obtenha os recursos necessários em um dynamic pool, são especificadas as variáveis tws.job.promoted (valores YES/NO, indicando se o trabalho é promovido) e tws.job.resourcesForPromoted (definida na definição do dynamic pool, com valores 1 se o trabalho é promovido ou 10 se não é), de modo que um trabalho promovido pode ser executado em um número maior de agentes dinâmicos do pool, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a promoção de trabalhos críticos em dynamic pools via variáveis tws.job.*.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic pool=dynamic pool, tws.job.promoted=tws.job.promoted, tws.job.resourcesForPromoted=tws.job.resourcesForPromoted |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobprom.html |
| Titulo da fonte | Promoting jobs scheduled on dynamic pools |
| Citacao de suporte | A promoted job can run on a larger number of dynamic agents in the dynamic pool than a non-promoted job... tws.job.resourcesForPromoted... Values can be 1 if the job is promoted or 10 if the job is not promoted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | dynamic-pool |


---

### 11. `hwa-10.2.8-event-actions-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

As ações no HCL Workload Automation 10.2.8 são classificadas em ações operacionais (que alteram o status de objetos de agendamento, como submeter jobs ou job streams e responder a prompts) e ações de notificação (como enviar email), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Operational versus notification action classification.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Operational actions=ações operacionais, Notification actions=ações de notificação, notification email=email de notificação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | Operational actions ... cause the change in the status of scheduling objects ... submitting a job, job stream, or command, or replying to a prompt. Notification actions ... sending an email, logging the event in an internal auditing database, or running a non-HCL Workload Automation command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | event-actions |


---

### 12. `hwa-10.2.8-event-batch-jobs-and-job-streams-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

As principais tarefas da automação orientada a eventos no HCL Workload Automation 10.2.8 incluem acionar a execução de jobs e job streams batch com base em eventos em tempo real, responder a prompts, notificar usuários em condições anômalas e invocar um produto externo, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Main tasks of event-driven workload automation.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | batch jobs and job streams=jobs e job streams batch, prompt=prompt, external product=produto externo |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | Trigger the execution of batch jobs and job streams based on the reception or combination of real time events. Reply to prompts. Notify users when anomalous conditions occur... Invoke an external product when a particular event condition occurs. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-batch |


---

### 13. `hwa-10.2.8-event-orchestration-monitor-0031`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

O Orchestration Monitor no HCL Workload Automation 10.2.8 é uma seção do Dynamic Workload Console que funciona como um hub de controle que supervisiona todo o workload associado a um engine específico, permitindo monitorar workstation, job stream, job, resource, prompt e file, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented role of the Orchestration Monitor as a monitoring control hub.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Orchestration Monitor=Orchestration Monitor, control hub=hub de controle |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/monitoringnew_overview.html |
| Titulo da fonte | Orchestration Monitor overview |
| Citacao de suporte | The Orchestration Monitor is a Dynamic Workload Console section that functions like a control hub that oversees all of your workload associated with a specific engine. From there, you can monitor: Workstation, Job stream, Job, Resource, Prompt, File |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-orchestration |


---

### 14. `hwa-10.2.8-event-orchestration-monitor-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

The Orchestration Monitor in HCL Workload Automation 10.2.8 Distributed monitors workstations, job streams, jobs, resources, prompts and files; event rules are not documented as monitored items in the Orchestration Monitor overview. Event rule instances are instead monitored in the event processing server logs and database (log.llrc_log_records).

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausência de event rules como item monitorado pelo Orchestration Monitor.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Orchestration Monitor=Orchestration Monitor, event rules=regras de evento |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/monitoringnew_overview.html |
| Titulo da fonte | Orchestration Monitor overview - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The monitored items listed are: Workstation, Job stream, Job, Resource, Prompt, File. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-orchestration |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 15. `hwa-10.2.8-event-submit-job-stream-0021`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

As ações do provider TWSAction no HCL Workload Automation 10.2.8 são SubmitJobStream, SubmitJob, SubmitAdHocJob e ReplyPrompt, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented TWSAction action types; these actions submit workloads or reply to prompts.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SubmitJobStream=ação SubmitJobStream, SubmitJob=ação SubmitJob, SubmitAdHocJob=ação SubmitAdHocJob, ReplyPrompt=ação ReplyPrompt |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsaction.html |
| Titulo da fonte | TWSAction actions |
| Citacao de suporte | TWSAction actions are: SubmitJobStream, SubmitJob, SubmitAdHocJob, ReplyPrompt |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
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
| verbs | submit |
| Familia | event-submit |


---

### 16. `hwa-10.2.8-event-twsobjects-monitor-events-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

Os eventos do provider TWSObjectsMonitor no HCL Workload Automation 10.2.8 incluem Job Status Changed, Job Submitted, Job Late, Job Stream Completed, Job Stream Late, Workstation Status Changed e Prompt Status Changed, entre outros, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Full documented list of TWSObjectsMonitor events.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TWSObjectsMonitor events=eventos TWSObjectsMonitor, Job Status Changed=Job Status Changed, Workstation Status Changed=Workstation Status Changed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsobjectsmonitor.html |
| Titulo da fonte | TWSObjectsMonitor events |
| Citacao de suporte | TWSObjectsMonitor events are: Job Status Changed, Job Until, Job Submitted, Job Cancelled, Job Restarted, Job Late, Job Promoted, Job Risk Level Changed, Job Exceeded Maximum Duration, Job Did not Reach Minimum Duration, Job Stream Status Changed, Job Stream Completed, Job Stream Until, Job Stream Submitted, Job Stream Cancelled, Job Stream Late, Workstation Status Changed, Application Server Status Changed, Child Workstation Link Changed, Parent Workstation Link Changed, Prompt Status Changed, ProductAlert |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | event-twsobjects |


---

### 17. `hwa-10.2.8-govern-job-stream-name-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o nome de um job stream deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 16 caracteres.

> **ATENCAO / RESSALVAS DE USO:** Hard product constraint (16-char limit) documented for the schedule keyword.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | job_stream_name=must start with a letter; alphanumeric, dash, underscore; max 16 characters |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgchdcajab.html |
| Titulo da fonte | schedule - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The name must start with a letter, and can contain alphanumeric characters, dashes, and underscores. It can contain up to 16 characters. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | naming_jobstream |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de um job stream deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 16 caracteres?


---

### 18. `hwa-10.2.8-gui-conddep-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `gui`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, uma condição de join agrega múltiplas dependências de diferentes predecessores em uma única dependência e libera o job sucessor quando o número mínimo configurado de dependências é satisfeito; se nenhum número mínimo for especificado, todas as dependências predecessoras devem ser satisfeitas.

> **ATENCAO / RESSALVAS DE USO:** O comportamento padrão 'todas as dependências' é corroborado pelo designer_overview: 'If you do not specify a value, all predecessor dependencies must be satisfied.'

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcondepsjoin_intro.html |
| Titulo da fonte | Joining or combining conditional dependencies |
| Citacao de suporte | You can add multiple dependencies from different predecessors to a single join dependency. You then specify how many of those dependencies must be met for HCL Workload Automation to consider the join satisfied. When the conditions satisfy the join, the successor job runs. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | gui_join_dependency |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=gui |
| Tipo | other |
| Ferramenta | gui |
| Familia | gui-conddep |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, uma condição de join agrega múltiplas dependências de diferentes predecessores em uma única dependência e libera o job sucessor quando o número mínimo configurado de dependências é satisfeito; se nenhum número mínimo for especificado, todas as dependências predecessoras devem ser satisfeitas?


---

### 19. `hwa-10.2.8-gui-designer-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Graphical Designer é aberto em Design > Graphical Designer e possui uma palette com duas abas: Blocks (job streams, jobs, wait jobs e join conditions) e Assets (Calendar, Credentials, Domain, Folder, Job definition, Job stream, Prompt, Resource, Run cycle group, Variable table, Workstation e Workstation class); os itens são salvos no banco de dados ao selecionar Deploy, e o workspace pode ser exportado/importado como JSON e salvo como imagem PNG.

> **ATENCAO / RESSALVAS DE USO:** A lista completa de itens das abas foi confirmada na página 'Using the palette' (palette.html); designer_overview confirma abertura, Deploy e formatos JSON/PNG.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/designer_overview.html |
| Titulo da fonte | Graphical Designer overview |
| Citacao de suporte | To open the Graphical Designer from the Dynamic Workload Console, open the Design menu and click Graphical Designer... the palette is divided in two tabs, Blocks and Assets... The items you defined in a workspace can be saved to the database by selecting Deploy... You can export workspaces as JSON files or upload previously exported workspaces... You can also save the workspace visuals as Portable Network Graphics (PNG) files. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=deploy |
| Tipo | command |
| Ferramenta | gui |
| verbs | deploy; run |
| Familia | gui-designer |


---

### 20. `hwa-10.2.8-gui-jobstream-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para adicionar um job a um job stream pela Dynamic Workload Console, navega-se em Design > Workload Designer, seleciona-se o engine, escolhe-se o card Job stream, clica-se em Edit no job stream desejado e trabalha-se na view Details ou na view Graphical; na view Details clica-se no sinal de + junto de Jobs e busca-se a definição de job para clicar em Add; na view Graphical clica-se com o botão direito e seleciona-se Add Jobs ou usa-se o campo Search; em ambos é possível marcar o job como Critical.

> **ATENCAO / RESSALVAS DE USO:** A descrição de busca/Add de job por definição e a flag Critical aplicam-se a distributed systems; em z/OS adiciona-se novo job selecionando o tipo.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/AddingAJobToAJobStream.html |
| Titulo da fonte | Adding a job to a job stream |
| Citacao de suporte | Click the plus button near to Jobs, and depending on your environment: On distributed systems Search for the job definition to be added and click Add... For example, you can set a job as Critical... Right-click inside the graphical view and select Add Jobs or search for the required job by using the displayed Search field. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
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
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Terminologia normalizada | command=add |
| Tipo | command |
| Ferramenta | gui |
| verbs | add |
| Familia | gui-jobstream |


---

### 21. `hwa-10.2.8-gui-jobstream-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, é possível criar uma definição de job stream pelo Graphical Designer, adicionar um run cycle e adicionar jobs (arrastando definições da aba Assets) ao job stream; a página oficial 'Managing job stream definitions' documenta esse procedimento.

> **ATENCAO / RESSALVAS DE USO:** A página existe em v1028 sob General_Help; confirma criação de job stream, run cycle e adição de jobs pelo Graphical Designer.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/Creating_js_t.html |
| Titulo da fonte | Managing job stream definitions |
| Citacao de suporte | You can create a job stream, add a run cycle, and add jobs from the Graphical Designer... From the Assets tab, drag the following jobs and drop them into the PAYROLL_PROC_26 job stream. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
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
| Terminologia normalizada | topic=gui |
| Tipo | other |
| Ferramenta | gui |
| verbs | run |
| Familia | gui-jobstream |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é possível criar uma definição de job stream pelo Graphical Designer, adicionar um run cycle e adicionar jobs (arrastando definições da aba Assets) ao job stream; a página oficial 'Managing job stream definitions' documenta esse procedimento?


---

### 22. `hwa-10.2.8-gui-sap-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `dependency`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, define-se um evento de background do SAP como dependência internetwork pela Dynamic Workload Console abrindo o Workload Designer (Design > Workload Designer), selecionando o job stream e clicando em Edit, depois em Add Dependency e selecionando Internetwork; nos campos Network Agent informa-se o agente conectado ao sistema SAP e em Dependency informam-se os parâmetros do evento SAP (por exemplo -evtid ... -evtpar ...), clicando em Save para salvar o job stream.

> **ATENCAO / RESSALVAS DE USO:** URL oficial correta em v1028 é /apps/src_usr/awsaujscewrkevts.html; a URL informada /distr/src_ref/awsaujscewrkevts.html retorna 404. Os parâmetros exatos do SAP ficam na seção 'Parameters to define an SAP internetwork dependency' referenciada pela página.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/apps/src_usr/awsaujscewrkevts.html |
| Titulo da fonte | Defining internetwork dependencies based on SAP background events with the Dynamic Workload Console |
| Citacao de suporte | In the job stream subrow, click Add Dependency and select Internetwork... In the Network Agent field, enter the name of the agent workstation connected to the SAP background processing system where the event runs... Click Save to save the changes to the job stream. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | dependency |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=add |
| Tipo | command |
| Ferramenta | gui |
| verbs | add |
| Familia | gui-sap |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, define-se um evento de background do SAP como dependência internetwork pela Dynamic Workload Console abrindo o Workload Designer (Design > Workload Designer), selecionando o job stream e clicando em Edit, depois em Add Dependency e selecionando Internetwork; nos campos Network Agent informa-se o agente conectado ao sistema SAP e em Dependency informam-se os parâmetros do evento SAP (por exemplo -evtid?


---

### 23. `hwa-10.2.8-incident-bia015i-dst-0085`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `scheduling`

**Afirmacao / Conteudo:**

Sintoma: AWSBIA015I 'Schedule <workstation>#<schedule> added' — o horario do schedule aparece incorreto (o mesmo pode acontecer com a keyword deadline). Causa: funcoes de data/hora da C-Runtime Library falham ao calcular o horario correto durante a primeira semana do horario de verao (daylight savings time). Resolucao: para o argumento de tempo das keywords at, until ou deadline, especificar um valor diferente do horario de inicio do periodo de producao definido no arquivo de opcoes globais — os valores devem diferir por mais ou menos uma hora. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - daylight savings time |
| Citacao de suporte | The problem is related to the C-Runtime Library date and time functions that fail to calculate the correct time during the first week of daylight savings time. |
| Coletado em | 2026-08-23 |
| Capacidade | scheduling |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSBIA015I |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSBIA015I |
| Familia | incident-bia015i |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIA015I no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA015I no HWA?
- Qual o comportamento das opções until e deadline na submissão de jobs no conman?
- O que causa e como solucionar o problema: AWSBIA015I 'Schedule <workstation>#<schedule> added' — o horario do schedule aparece incorreto (o mesmo pode acontecer com a keyword deadline)?


---

### 24. `hwa-10.2.8-incident-job-ready-not-start-0134`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `jobs`

**Afirmacao / Conteudo:**

Sintoma: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia. Causa (mais comuns): (1) o limite da workstation esta zerado; (2) a workstation esta parada; (3) a workstation onde o job deveria rodar nao esta linkada; (4) o numero de jobs rodando na workstation e maior que o limite configurado. Resolucao: verificar cada uma dessas causas na workstation alvo. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Correlaciona com lab (limit, link, fenced).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - job ready not start |
| Citacao de suporte | The workstation limit is set to zero. The workstation is stopped. The workstation on which the job should run is not linked. The number of jobs running on the workstation is greater than the limit set on the workstation. |
| Coletado em | 2026-08-23 |
| Capacidade | jobs |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| verbs | start |
| Familia | incident-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia?
- O que causa e como solucionar o problema: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia?


---

### 25. `hwa-10.2.8-incident-max-40-deps-0118`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dependencies`

**Afirmacao / Conteudo:**

Sintoma: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta. Causa: a instancia de Job Scheduler ja tem o numero maximo (40) de dependencias definidas; normalmente um erro alertaria sobre o limite, mas a mensagem pode nao ser exibida se houver atraso na propagacao das atualizacoes do Symphony pela rede ou se a atualizacao coincidiu com atualizacoes de outros usuarios. Resolucao: reduzir o numero de dependencias para abaixo de 40. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - max 40 dependencies |
| Citacao de suporte | This occurs when a Job Scheduler instance already has the maximum number (40) of dependencies defined. |
| Coletado em | 2026-08-23 |
| Capacidade | dependencies |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | incident-max |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: Sintoma: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta?
- O que causa e como solucionar o problema: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta?


---

### 26. `hwa-10.2.8-incident-prompt-number-0094`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `prompt`

**Afirmacao / Conteudo:**

Sintoma: ao submeter um job ou Job Scheduler dependente de um prompt ad-hoc, o conman nao consegue submeter por causa do prompt number. Causa: no master domain manager, prompts sao criados no plano com um prompt number unico mantido em arquivo; o JnextPlan inicia o prompt number em 1 e incrementa a cada prompt; ao submeter com prompt ad-hoc em outro agent durante a vigencia do plano, o numero pode conflitar. Resolucao: modificar o ultimo prompt number garantindo que o digito menos significativo esteja na posicao 21 (ex.: '98' → '2098' substituindo dois espacos por '20'); salvar e reexecutar o submit. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - duplicate ad-hoc prompt number |
| Citacao de suporte | When modifying the last prompt number, remember that the least significant digit must always be in character position 21. |
| Coletado em | 2026-08-23 |
| Capacidade | prompt |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (edicao de prompt number); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter a edicao do arquivo. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| Familia | incident-prompt |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar prompt?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: ao submeter um job ou Job Scheduler dependente de um prompt ad-hoc, o conman nao consegue submeter por causa do prompt number?


---

### 27. `hwa-10.2.8-incident-rerun-recovery-cross-domain-0116`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `recovery`

**Afirmacao / Conteudo:**

Sintoma: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta. Causa: o recovery job foi especificado para rodar em uma workstation e dominio diferentes do job original; o job original nao consegue detectar o estado do recovery job, portanto nao determina se ele terminou ou em que estado. Resolucao: para o job especifico ainda em 'running', resolver o estado manualmente; para novos jobs, configurar o recovery job na mesma workstation/dominio. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - rerun recovery cross domain |
| Citacao de suporte | This problem would occur if the recovery job was specified to run on a different workstation and domain from the original job. The original job is then unable to detect the state of the recovery job |
| Coletado em | 2026-08-23 |
| Capacidade | recovery |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=rerun |
| Status de revisao | verified |
| Tipo | command |
| verbs | rerun |
| Familia | incident-rerun |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta?
- O que causa e como solucionar o problema: um job com recovery job usando o metodo 'rerun' — o job original falha, mas quando o recovery job roda, o job original permanece em 'running' e nao volta?


---

### 28. `hwa-10.2.8-monitor-calendars-v-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

A view CALENDARS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre calendários de agendamento, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Calendar_identifier, Calendar_name, Calendar_description, Calendar_dates, Calendar_folder_id, Calendar_folder_name.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=CALENDARS_V, termo_pt_br=visão CALENDARS_V (calendários) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvcalendars.html |
| Titulo da fonte | CALENDARS_V |
| Citacao de suporte | The CALENDARS_V view displays information about calendars. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-calendars |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A view CALENDARS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre calendários de agendamento, conforme documentação oficial?


---

### 29. `hwa-10.2.8-monitor-dashboard-widgets-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

Os widgets documentados do Workload Dashboard no HCL Workload Automation 10.2.8 incluem Engines, Available workstations, Unavailable workstations, Pending Prompts, Critical job status, Job status, Jobs in late, Jobs in error, Min duration, Max duration e Resources, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Cada widget é documentado com drill-down para as views de monitoramento (Monitor Workstations, Monitor Prompts, Monitor Jobs, Monitor Resources).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=widgets do Workload Dashboard, termo_pt_br=widgets do Workload Dashboard |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/dashboardtask.html |
| Titulo da fonte | Workload Dashboard |
| Citacao de suporte | Available workstations - This widget shows the number of available workstations for the selected engine. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | monitor-dashboard |


---

### 30. `hwa-10.2.8-monitor-plan-jobs-v-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

A view PLAN_JOBS_V no HCL Workload Automation 10.2.8 é documentada com colunas-chave de consulta do plano como Job_id, Job_name, Job_stream_name, Scheduled_time, Status, Return_code, Priority e Deadline, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Status documentado com valores C/H/W/B/R/S/O/E/U/X (Canceled/Held/Waiting/Blocked/Ready/Running/Successful/Error/Undecided/Suppressed).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PLAN_JOBS_V, termo_pt_br=colunas de consulta do plano em PLAN_JOBS_V |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvplanjobs.html |
| Titulo da fonte | PLAN_JOBS_V |
| Citacao de suporte | Status - The job status. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan; status |
| Familia | monitor-plan |


---

### 31. `hwa-10.2.8-monitor-plan-resources-v-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

A view PLAN_RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os recursos (resources) presentes no plano, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Resource_id, Resource_name, Resource_number, Status (Available/Not_available/Undecided), Available, Not_used, In_use.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PLAN_RESOURCES_V, termo_pt_br=visão PLAN_RESOURCES_V (recursos no plano) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvplanReource.html |
| Titulo da fonte | PLAN_RESOURCES_V |
| Citacao de suporte | The PLAN_RESOURCES_V view displays information about resources in the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | monitor-plan |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco PLAN_RESOURCES_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional PLAN_RESOURCES_V no banco de dados do HWA?


---

### 32. `hwa-10.2.8-monitor-prompts-v-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

A view PROMPTS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre prompts, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Prompt_identifier, Prompt_name, Prompt_value, Prompt_fol_id, Prompt_fol_name, Prompt_Symphony_id.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PROMPTS_V, termo_pt_br=visão PROMPTS_V (prompts) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvprompts.html |
| Titulo da fonte | PROMPTS_V |
| Citacao de suporte | The PROMPTS_V view displays information about prompts. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-prompts |


---

### 33. `hwa-10.2.8-monitor-resources-v-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

A view RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre recursos (resources) definidos, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Workstation_identifier, Resource_name, Resource_identifier, Resource_description, Resource_units, Resource_fol_name.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=RESOURCES_V, termo_pt_br=visão RESOURCES_V (recursos) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvresources.html |
| Titulo da fonte | RESOURCES_V |
| Citacao de suporte | The RESOURCES_V view displays information about resources. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-resources |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A view RESOURCES_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre recursos (resources) definidos, conforme documentação oficial?


---

### 34. `hwa-10.2.8-perf-every-minimal-0166`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), a opcao 'EVERY' cria nova instancia de job stream ou job no plano; em job-level ela causa multiplos 'sbj' internos ao mesmo job stream instance que podem afetar a performance das atualizacoes do plano. Importante verificar se EVERY e usado com valores minimos (poucos minutos) para evitar aumentar o numero de jobs num job stream (algumas centenas de jobs podem impactar performance). Metodologias: mover EVERY para job stream level se possivel; dividir o job stream em multiplos com 'AT xx till xx' (time partitioning). Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.4).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 19-20). Correlaciona com hwa-lab-10.2.8-every-stream-job-execution-0037 (EVERY 0002 validado no lab).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - EVERY option |
| Citacao de suporte | the latter causes multiple internal sbj to the same job stream instance that could affect performances especially in the plan updates... Move EVERY option at job stream level if possible. Split the Job stream in multiple job stream with AT xx till xx (time partitioning) |
| Coletado em | 2026-08-23 |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; recomendacao. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=perf |
| Status de revisao | verified |
| Tipo | other |
| Familia | perf-every |


---

### 35. `hwa-10.2.8-prompt-globalnamed-prompt-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

Uma prompt é uma pergunta operacional textual; um job/job stream com prompt não conclui o processamento de dependências até que o usuário designado forneça resposta; reply responde prompts; prompts predefinidas (globais, no banco, reutilizáveis) vs ad hoc (locais ao job).

> **ATENCAO / RESSALVAS DE USO:** A página usa os termos 'global or named prompts' e 'local or unnamed prompts' (não 'predefined'/'ad hoc'). O comando reply existe na lista de comandos Orchestration CLI. Prompts globais são resetadas a cada execução do JnextPlan.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | prompt=mensagem textual exibida ao operador que interrompe o processamento, global/named prompt=prompt definida no banco como objeto de agendamento, reutilizável, local/unnamed prompt=prompt definida dentro do job/job stream, não reutilizável, reply=resposta à prompt (manual ou por ação de event rule) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgpromptdef.html |
| Titulo da fonte | Prompt definition |
| Citacao de suporte | A prompt identifies a textual message that is displayed to the operator and halts processing of the job or job stream until an affirmative answer is replied ... A global prompt is defined in the database as a scheduling object, it is identified by a unique name and it can be used by any job or job stream. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | prompt-globalnamed |


---

### 36. `hwa-10.2.8-resource-resource-syntax-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

Sintaxe de recurso: $resource workstation#resourcename units "description"; o nome do recurso pode ter até 8 caracteres alfanuméricos incluindo - e _, iniciando com letra; a quantidade normalmente varia de 0 a 1024.

> **ATENCAO / RESSALVAS DE USO:** Sintaxe completa: $resource [folder/]workstation#[folder/]resourcename units ["description"]. Descrição até 120 caracteres alfanuméricos entre aspas duplas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | $resource=comando de definição de recurso, workstation#resourcename=workstation e nome do recurso, units=número de unidades disponíveis (0 a 1024), description=descrição opcional entre aspas duplas (até 120 caracteres) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgresdef.html |
| Titulo da fonte | Resource definition |
| Citacao de suporte | The resource name can contain up to eight alphanumeric characters, including dashes (-) and underscores (_), and must start with a letter. ... units Specifies the number of available resource units. Values can be 0 through 1024. |
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

- Qual a regra documentada no HWA Distributed sobre: Sintaxe de recurso: $resource workstation#resourcename units "description"; o nome do recurso pode ter até 8 caracteres alfanuméricos incluindo - e _, iniciando com letra; a quantidade normalmente varia de 0 a 1024.?


---

### 37. `hwa-10.2.8-runbook-cancel-sched-0012`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando cancel sched (cs) cancela um job stream: se cancelado antes de iniciar, o job stream não executa; se cancelado após iniciar, os jobs já iniciados completam e os demais jobs do job stream são cancelados.

> **ATENCAO / RESSALVAS DE USO:** Cancelling a job stream is destructive; documented behavior.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=cancel sched, abbreviation=cs, effect=cancels a job stream |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_cancel_sched.html |
| Titulo da fonte | cancel sched |
| Citacao de suporte | If you cancel a job stream before it starts, the job stream does not run. When you cancel a job stream after it starts, the jobs in the job stream that are started will complete. The remaining jobs from the job stream are cancelled. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | cancel_jobstream |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | cancel |
| object_hint | sched |
| Familia | runbook-cancel |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel sched (cs) cancela um job stream: se cancelado antes de iniciar, o job stream não executa; se cancelado após iniciar, os jobs já iniciados completam e os demais jobs do job stream são cancelados?


---

### 38. `hwa-10.2.8-runbook-database-view-0034`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `recovery`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V também registra a opção de recuperação (Recovery_option) de cada job com valores possíveis C (Continue), R (Rerun) e S (Stop), além de Recovery_repeat_interval e Recovery_repeat_occurrences.

> **ATENCAO / RESSALVAS DE USO:** Read-only DB view; corroborates recovery option values (C/R/S) with the recovery definition topic.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | database_view=JOB_STATISTICS_V, columns=['Recovery_option', 'Recovery_repeat_interval', 'Recovery_repeat_occurrences'], recovery_values={'C': 'Continue', 'R': 'Rerun', 'S': 'Stop'} |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobstatistics.html |
| Titulo da fonte | JOB_STATISTICS_V |
| Citacao de suporte | Recovery_option The recovery options for the job. Possible values are: C Continue, R Rerun, S Stop |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | recovery |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | rerun; stop |
| Familia | runbook-database |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?


---

### 39. `hwa-10.2.8-runbook-recovery-option-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção de recuperação 'continue' é uma opção de recuperação definida na definição do job (job definition): se o job termina de forma anormal, o produto continua com o próximo job (do job stream), não sendo um parâmetro do comando rerun.

> **ATENCAO / RESSALVAS DE USO:** Clarifies that 'continue' is a recovery option in the job definition, not a rerun command option. Official docs do not document a rerun ;continue parameter.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recovery_option=continue, context=job definition recovery |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningjobrecovery.html |
| Titulo da fonte | Defining job rerun and recovery actions |
| Citacao de suporte | continue If the job ends abnormally, continue with the next job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | recovery_continue |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | rerun |
| Familia | runbook-recovery |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção de recuperação 'continue' é uma opção de recuperação definida na definição do job (job definition): se o job termina de forma anormal, o produto continua com o próximo job (do job stream), não sendo um parâmetro do comando rerun?


---

### 40. `hwa-10.2.8-runbook-recovery-option-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção de recuperação 'rerun' (na definição do job) faz com que, se o job terminar de forma anormal, o job seja rerun, podendo ser combinada com 'repeatevery hhmm for number attempts' e 'rerun after prompt' para controlar a sequência de rerun.

> **ATENCAO / RESSALVAS DE USO:** Documents the job-definition rerun recovery sequence and that successful rerun releases dependencies.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recovery_option=rerun, options=['repeatevery', 'for', 'rerun after prompt'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningjobrecovery.html |
| Titulo da fonte | Defining job rerun and recovery actions |
| Citacao de suporte | rerun If the job ends abnormally, rerun the job. ... repeatevery hhmm for number attempts You can specify how often you want HCL Workload Automation to rerun the failed job and the maximum number of rerun attempts to be performed. If any rerun in the sequence completes successfully, the remaining rerun sequence is ignored and any job dependencies are released. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | rerun |
| Familia | runbook-recovery |


---

### 41. `hwa-10.2.8-runbook-release-job-0008`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando release job remove a dependência somente para o job em progresso; quando o mesmo job é rerun, a dependência persiste, e para removê-la permanentemente do job stream é preciso usar o comando deldep job.

> **ATENCAO / RESSALVAS DE USO:** Important nuance: release only affects the current instance; deldep is needed for permanent removal.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=release job, effect=removes dependency only for current instance, related=deldep job |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_release_job.html |
| Titulo da fonte | release job |
| Citacao de suporte | When you use the command, the dependency is removed only for the job that are in progress. When you rerun the same job, the dependency persist. To remove the dependency permanently from a job stream, refer to deldep job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | release_dependency |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | deldep; release; remove; rerun |
| object_hint | job |
| Familia | runbook-release |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando release job remove a dependência somente para o job em progresso; quando o mesmo job é rerun, a dependência persiste, e para removê-la permanentemente do job stream é preciso usar o comando deldep job?


---

### 42. `hwa-10.2.8-runbook-rerun-0004`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, quando o rerun usa a opção ;from, as opções de recuperação (recovery options) são parcialmente herdadas da definição original e parcialmente obtidas do job 'from': a opção de recuperação 'stop' e 'continue' são recuperadas do job 'from' (NÃO herdadas do job original), enquanto 'rerun', 'repeatevery', 'for', 'after' e 'abendprompt' são herdadas do job original.

> **ATENCAO / RESSALVAS DE USO:** Documents exactly which recovery options come from the from-job vs the original job when rerun ;from is used.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rerun, option=from, recovery_options=['stop', 'continue', 'rerun', 'repeatevery', 'for', 'after', 'abendprompt'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgrerun.html |
| Titulo da fonte | rerun (conman) |
| Citacao de suporte | Recovery options retrieval criteria ... stop: Retrieved from from job Yes ... continue: Retrieved from from job Yes ... rerun: Inherited from original job Yes |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | every |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | rerun; stop |
| Familia | runbook-rerun |


---

### 43. `hwa-10.2.8-runcycle-graphical-designer-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `runcycle`

**Afirmacao / Conteudo:**

No HCL Workload Automation, desde a versão 10.2.4, os run cycle groups podem ser criados e atribuídos como Triggers a job streams diretamente no Graphical Designer, funcionando como objetos de agendamento reutilizáveis.

> **ATENCAO / RESSALVAS DE USO:** Página listada sob 'HCL Workload Automation version 10.2.4 enhancements', confirmando a introdução do recurso na 10.2.4. A página confirma criação e atribuição como Triggers no Graphical Designer; o aspecto de 'subsets' (subconjuntos de run cycles) não é explicitamente mencionado nesta página, apenas a reutilização do grupo, por isso a confiança é média para o termo 'subsets'.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | run cycle group=grupo de run cycles, Triggers=gatilhos, Graphical Designer=Designer Gráfico, job stream=job stream, reusable scheduling object=objeto de agendamento reutilizável |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1rcgtriggers.html |
| Titulo da fonte | Run cycle groups available as triggers in the Graphical Designer |
| Citacao de suporte | You can now create and assign run cycle groups as Triggers to job streams directly in the Graphical Designer to design a precise, time-driven automation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | runcycle |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | gui |
| verbs | run |
| Familia | runcycle-graphical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation, desde a versão 10.2.4, os run cycle groups podem ser criados e atribuídos como Triggers a job streams diretamente no Graphical Designer, funcionando como objetos de agendamento reutilizáveis?


---

### 44. `hwa-10.2.8-sec-variable-table-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `vartable`

**Afirmacao / Conteudo:**

A segurança de variable tables no HCL Workload Automation 10.2.8 é controlada no security file por meio da keyword vartable (ex.: vartable name=@ access=add,delete,display,modify,list,use,unlock), e a permissão é concedida no nível da tabela, não no nível de cada variável individual.

> **ATENCAO / RESSALVAS DE USO:** Documentado: o administrador pode usar a keyword $default para aplicar permissões na tabela padrão independentemente do nome.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | variable_table=tabela de variáveis, vartable=keyword de segurança para tabelas de variáveis, security_file=arquivo de segurança, access=permissão de acesso |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtsecurity.html |
| Titulo da fonte | Variable table security |
| Citacao de suporte | vartable name=@ access=add,delete,display,modify,list,use,unlock |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | vartable |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | add; delete; display; list; modify |
| Familia | sec-variable |


---

### 45. `hwa-10.2.8-showprompts-states-0038`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `prompt`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, showprompts/sp usa ASKED para prompt emitido sem resposta e INACT para prompt ainda não emitido. Context: ASKED The prompt was issued, but no reply was given. INACT The prompt has not been issued.

> **ATENCAO / RESSALVAS DE USO:** The doc lists four prompt states (YES, NO, ASKED, INACT); the claim covers only ASKED and INACT, which are supported verbatim and not contradicted. Read-only diagnostic command.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowprompts.html |
| Titulo da fonte | showprompts |
| Citacao de suporte | ASKED The prompt was issued, but no reply was given. INACT The prompt has not been issued. |
| Coletado em | 2026-08-18 |
| Capacidade | prompt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showprompts |
| Status de revisao | verified |
| Tipo | other |
| Familia | showprompts-states |


---

### 46. `hwa-10.2.8-showresources-available-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

Em HWA 10.2.8, no formato standard de showresources, Available é o número de unidades de recurso não alocadas. Context: Available — The number of resource units that have not been allocated.

> **ATENCAO / RESSALVAS DE USO:** The 'Standard format' page is a sub-topic of showresources in v1028 and defines the standard-format fields (CPU, Resource, Total, Available, Qty, Used By). Read-only diagnostic command.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstdformat7.html |
| Titulo da fonte | Standard format |
| Citacao de suporte | Available The number of resource units that have not been allocated. |
| Coletado em | 2026-08-18 |
| Capacidade | resource |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showresources |
| Status de revisao | verified |
| Tipo | other |
| Familia | showresources-available |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, no formato standard de showresources, Available é o número de unidades de recurso não alocadas?


---

### 47. `hwa-10.2.8-tune-bm-check-deadline-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

A opção bm check deadline no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar se um job perdeu seu deadline, com padrão documentado de zero (desabilitada); deadlines de jobs críticos são avaliados automaticamente, independentemente desta opção.

> **ATENCAO / RESSALVAS DE USO:** Recomenda-se definir no master domain manager para obter informação atualizada de todo o ambiente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm check deadline=bm check deadline, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm check deadline = seconds - ... To disable the option and not check deadlines, enter a value of zero, the default value. Deadlines for critical jobs are evaluated automatically, independently of the bm check deadline option. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm check deadline no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar se um job perdeu seu deadline, com padrão documentado de zero (desabilitada); deadlines de jobs críticos são avaliados automaticamente, independentemente desta opção?


---

### 48. `hwa-10.2.8-tune-bm-late-every-0026`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

A opção bm late every no localopts do HCL Workload Automation 10.2.8 especifica, em minutos, o máximo de tempo que pode decorrer antes que o HCL Workload Automation pule um job every que não iniciou em sua hora esperada; aplica-se apenas a jobs definidos com every junto com a dependência de horário at.

> **ATENCAO / RESSALVAS DE USO:** A referência oficial de detalhes de localopts não documenta um valor padrão quantitativo para bm late every.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm late every=bm late every, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm late every = minutes - When an every job does not start at its expected start time, bm late every specifies the maximum number of minutes that elapse before HCL Workload Automation skips the job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |


---

### 49. `hwa-10.2.8-variable-plan-generation-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `vartable`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a ordem de resolução de variáveis na geração do plano é: run cycle, job stream, workstation e tabela padrão (apenas para ^variablename^); na submissão de um job stream, a ordem é: especificada na submissão, job stream, workstation e tabela padrão (apenas para ^variablename^).

> **ATENCAO / RESSALVAS DE USO:** Na geração do plano, a ordem dentro do run cycle é: run cycle no job stream, depois run cycle em um run cycle group e, por fim, a tabela definida no nível do run cycle group. Na submissão de job stream, a ordem é: especificada durante a submissão, job stream, workstation e tabela padrão. Variáveis ${variablename} não são resolvidas na tabela padrão.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | variable resolution=resolução de variáveis, plan generation=geração do plano, run cycle=run cycle, job stream=job stream, workstation=workstation, default variable table=tabela de variáveis padrão, submit operation=operação de submissão |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtresolution.html |
| Titulo da fonte | Variable resolution |
| Citacao de suporte | When you generate a plan, HCL Workload Automation analyzes the variable tables in the order shown below for variable resolution: In the run cycle. ... In the job stream. In the workstation. ... In the default variable table, but only when the variables are specified in the ^variablename^ format in the job definition. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | variable_resolution |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan; run |
| Familia | variable-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a ordem de resolução de variáveis na geração do plano é: run cycle, job stream, workstation e tabela padrão (apenas para ^variablename^); na submissão de um job stream, a ordem é: especificada na submissão, job stream, workstation e tabela padrão (apenas para ^variablename^)?


---

### 50. `hwa-10.2.8-vm-9f-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `syntax`

**Afirmacao / Conteudo:**

A dependência condicional IF (follows <ws>#<stream>.<job> if <condition>) é suportada na definição de job stream do HCL Workload Automation Distributed na 10.2.0 e 10.2.8. A documentação oficial 10.2.8 lista como condições de status para jobs: FAIL, ABEND, SUCC e SUPPR; o status EXEC não consta da lista oficial de condições de dependência.

> **ATENCAO / RESSALVAS DE USO:** EXEC como condicao de status NAO e documentado nas listas oficiais de condicoes (FAIL/ABEND/SUCC/SUPPR para jobs; SUCC/SUPPR/ABEND para job streams). QUALIFICACAO (m1): a documentacao oficial 10.2.8 usa a condicao EXEC em exemplos de JOIN para job streams externos (conditional dependency para detectar que um stream externo entrou em execucao), mas EXEC nao aparece nas tabelas de condicoes de status validas para condicoes IF. Portanto, EXEC e aceito na gramatica JOIN em contexto de stream externo, porem nao deve ser generalizado como condicao de status de job. Status do claim: verified para FAIL/ABEND/SUCC/SUPPR; a validade de EXEC em JOIN e version_dependent.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | if=condição de dependência condicional, follows=dependência de precedência, status_conditions=FAIL, ABEND, SUCC, SUPPR (jobs); SUCC, SUPPR, ABEND (job streams), EXEC=usado em exemplos de JOIN p/ streams externos; NAO e condicao de status documentada |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcondlogic.html |
| Titulo da fonte | Conditional logic (HCL Workload Automation 10.2.8) |
| Citacao de suporte | follows <ws>#<stream>.<job> if <condition> |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | conditional_dependency |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | vm-9f |


---

### 51. `hwa-10.2.8-vm-9f-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

A palavra-chave CRITICAL (job mission-critical) e a opção global enWorkloadServiceAssurance (alias wa) existem e são idênticas no HCL Workload Automation Distributed 10.2.0 e 10.2.8. enWorkloadServiceAssurance tem valor padrão YES em ambas; jobs critical exigem deadline.

> **ATENCAO / RESSALVAS DE USO:** CRITICAL e WSA idênticos em 10.2.0 e 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | critical=palavra-chave de job mission-critical, enWorkloadServiceAssurance=opção global de workload service assurance, wa=alias, default=YES |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance (10.2.8) |
| Citacao de suporte | enWorkloadServiceAssurance | wa ... The default value is YES. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | vm-9f |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A palavra-chave CRITICAL (job mission-critical) e a opção global enWorkloadServiceAssurance (alias wa) existem e são idênticas no HCL Workload Automation Distributed 10.2.0 e 10.2.8. enWorkloadServiceAssurance tem valor padrão YES em ambas; jobs critical exigem deadline?
- Qual o propósito e valor padrão da opção global enWorkloadServiceAssurance no optman do HWA?


---

### 52. `hwa-10.2.8-vm-9f-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `runcycle`

**Afirmacao / Conteudo:**

A palavra-chave runcyclegroup (sem $) com vartable e on runcycle <name> "FREQ=..." ... end, com nome de até 8 caracteres, é suportada na definição de job stream do HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica.

> **ATENCAO / RESSALVAS DE USO:** runcyclegroup idêntico em 10.2.0 e 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | runcyclegroup=palavra-chave de grupo de run cycles, vartable=tabela de variáveis associada, on runcycle=definição de run cycle com FREQ, name_length=máximo 8 caracteres |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgruncycgrpdef.html |
| Titulo da fonte | Run cycle group definition (10.2.8) |
| Citacao de suporte | runcyclegroup <name> ... on runcycle <name> "FREQ=..." ... end |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | runcycle |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | vm-9f |


---

### 53. `hwa-10.2.8-vm-9f-0006`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

A definição de recuperação de job RECOVERY RERUN [same_workstation] [repeatevery hhmm] [for number attempts] é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica. A palavra-chave onlate aceita apenas a ação kill em ambas as versões.

> **ATENCAO / RESSALVAS DE USO:** Validado no lab container 10.2.8: RECOVERY RERUN inline testado e documentado na evidência recovery-rerun-container-0001.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recovery=definição de ação de recuperação de job, rerun=opção de reexecução automática, same_workstation=reexecutar na mesma workstation, repeatevery=intervalo entre reexecuções, for=número máximo de tentativas, onlate=ação ao expirar o deadline; aceita apenas kill |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningjobrecovery.html |
| Titulo da fonte | Defining job rerun and recovery actions (10.2.8) |
| Citacao de suporte | recovery rerun [same_workstation] [repeatevery hhmm] [for number attempts] |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | lab_validated |
| Classificacao de risco | read_only |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | kill; rerun |
| Familia | vm-9f |


---

### 54. `hwa-10.2.8-wsa-confidence-factor-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para cada trabalho crítico é fornecido um Confidence Factor percentual que indica a confiança de que o trabalho crítico cumprirá seu deadline; quando o trabalho termina, o fator é sobrescrito para 0% se o deadline estimado foi excedido e para 100% se não foi, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o Confidence Factor e seu comportamento ao final do trabalho.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Confidence Factor=fator de confiança |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningcriticaljobs.html |
| Titulo da fonte | Planning critical jobs |
| Citacao de suporte | When a job finishes running, the confidence factor is overwritten and set to 0% when the estimate deadline was exceeded and is set to 100% when the deadline was not exceeded. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-confidence |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para cada trabalho crítico é fornecido um Confidence Factor percentual que indica a confiança de que o trabalho crítico cumprirá seu deadline; quando o trabalho termina, o fator é sobrescrito para 0% se o deadline estimado foi excedido e para 100% se não foi, conforme documentação oficial?


---

### 55. `hwa-10.2.8-wsa-critical-network-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, definir um trabalho crítico e seu deadline dispara o cálculo dos horários de início de todos os trabalhos que são predecessores do trabalho crítico, sendo o conjunto de predecessores denominado critical network (rede crítica), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o conceito de rede crítica formada pelos predecessores.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | critical network=rede crítica |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Using workload service assurance |
| Citacao de suporte | The set of predecessors of a critical job make up its critical network. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, definir um trabalho crítico e seu deadline dispara o cálculo dos horários de início de todos os trabalhos que são predecessores do trabalho crítico, sendo o conjunto de predecessores denominado critical network (rede crítica), conforme documentação oficial?


---

### 56. `hwa-10.2.8-wsa-critical-path-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o critical path é a cadeia de dependências, que leva ao trabalho crítico, mais em risco de causar a perda do deadline em um dado momento; é construído retrocedendo a partir do trabalho crítico, selecionando o predecessor com o maior horário de término estimado, e é recalculado automaticamente se o horário de término real diferir substancialmente do estimado, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a identificação e o recálculo dinâmico do caminho crítico (critical path).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | critical path=caminho crítico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | The critical path is the chain of dependencies, leading to the critical job, that is most at risk of causing the deadline to be missed at any given time... Working back from the critical job, the path is constructed by selecting the predecessor with the latest estimated end time. If the actual end time differs substantially from the estimated end time, the critical path is automatically recalculated. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o critical path é a cadeia de dependências, que leva ao trabalho crítico, mais em risco de causar a perda do deadline em um dado momento; é construído retrocedendo a partir do trabalho crítico, selecionando o predecessor com o maior horário de término estimado, e é recalculado automaticamente se o horário de término real diferir substancialmente do estimado, conforme documentação oficial?


---

### 57. `hwa-10.2.8-wsa-critical-start-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o critical start time aplica-se apenas a sistemas distribuídos e representa o último horário em que o trabalho pode iniciar sem fazer o trabalho crítico perder o deadline, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirma que o critical start é conceito de plataforma distribuída.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | critical start=horário de início crítico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningcriticaljobs.html |
| Titulo da fonte | Planning critical jobs |
| Citacao de suporte | Critical start. It applies to distributed systems only and represents the latest time at which the job can start without causing the critical job to miss its deadline. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | wsa-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o critical start time aplica-se apenas a sistemas distribuídos e representa o último horário em que o trabalho pode iniciar sem fazer o trabalho crítico perder o deadline, conforme documentação oficial?


---

### 58. `hwa-10.2.8-wsa-critical-start-time-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Time Planner calcula o critical start time (horário de início crítico), que é o último horário em que o trabalho pode iniciar para cumprir seu deadline, e, retrocedendo a partir dele, calcula o último horário em que cada predecessor da rede crítica pode iniciar, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o cálculo retroativo dos horários de início crítico na rede.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | critical start time=horário de início crítico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Using workload service assurance |
| Citacao de suporte | Time Planner calculates its critical start time, which is the latest starting time for the job to keep up with its deadline. Moving backwards from the critical start time it calculates the latest time at which each predecessor within the critical network can start. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| verbs | start |
| Familia | wsa-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Time Planner calcula o critical start time (horário de início crítico), que é o último horário em que o trabalho pode iniciar para cumprir seu deadline, e, retrocedendo a partir dele, calcula o último horário em que cada predecessor da rede crítica pode iniciar, conforme documentação oficial?


---

### 59. `hwa-10.2.8-wsa-deadline-offset-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção global deadlineOffset (abreviação do) fornece um deslocamento usado para calcular o critical start time quando o deadline está ausente tanto para o trabalho crítico quanto para seu job stream, assumindo como deadline do trabalho crítico o fim do plano mais esse deslocamento (expresso em minutos); o padrão é 2 minutos, e quando o plano é estendido os horários de início desses trabalhos críticos são automaticamente alterados para coincidir com o novo horário de término do plano, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o fallback de deadline (fim do plano + offset) e a mudança automática quando o plano é estendido.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | deadlineOffset=deadlineOffset (do) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | The deadlineOffset option provides an offset used to calculate the critical start time in case the deadline is missing for both a critical job and its job stream. The plan end plus this offset is assumed as the critical job's deadline. The offset is expressed in minutes. The default is 2 minutes. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | wsa-deadline |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global deadlineOffset (abreviação do) fornece um deslocamento usado para calcular o critical start time quando o deadline está ausente tanto para o trabalho crítico quanto para seu job stream, assumindo como deadline do trabalho crítico o fim do plano mais esse deslocamento (expresso em minutos); o padrão é 2 minutos, e quando o plano é estendido os horários de início desses trabalhos críticos são automaticamente alterados para coincidir com o novo horário de término do plano, conforme documentação oficial?
- Qual o propósito e valor padrão da opção global deadlineOffset no optman do HWA?


---

### 60. `hwa-10.2.8-wsa-designer-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, um trabalho pode ser marcado como crítico usando as funções do Workload Designer no Dynamic Workload Console ao adicioná-lo a um job stream, podendo o deadline ser definido no nível do trabalho ou do job stream, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta como identificar um trabalho crítico e definir deadline no DWC.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Workload Designer=Workload Designer, deadline=deadline |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningcriticaljobs.html |
| Titulo da fonte | Planning critical jobs |
| Citacao de suporte | you can flag it as critical when you add it to a job stream using the Workload Designer functions on the Dynamic Workload Console. You can define the deadline either at job or job stream level. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-designer |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um trabalho pode ser marcado como crítico usando as funções do Workload Designer no Dynamic Workload Console ao adicioná-lo a um job stream, podendo o deadline ser definido no nível do trabalho ou do job stream, conforme documentação oficial?


---

### 61. `hwa-10.2.8-wsa-high-risk-0026`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, um status de risco pode ser definido para o trabalho crítico: high risk quando os tempos calculados mostram que o trabalho crítico terminará após seu deadline, e potential risk quando trabalhos predecessores críticos foram adicionados à hot list, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta os estados de risco alto e potencial do trabalho crítico.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | high risk=risco alto, potential risk=risco potencial |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | High risk: Calculated timings show that the critical job will finish after its deadline. Potential risk: Critical predecessor jobs have been added to the hot list. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list; status |
| Familia | wsa-high |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um status de risco pode ser definido para o trabalho crítico: high risk quando os tempos calculados mostram que o trabalho crítico terminará após seu deadline, e potential risk quando trabalhos predecessores críticos foram adicionados à hot list, conforme documentação oficial?


---

### 62. `hwa-10.2.8-wsa-hot-list-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, trabalhos da rede crítica que tenham impacto real ou potencial no cumprimento do deadline do trabalho crítico são adicionados a uma hot list associada ao trabalho crítico; apenas os trabalhos que iniciam a rede crítica atual (sem predecessor) podem ser incluídos na hot list, por razões como erro, duração excedendo o longDurationThreshold, ou trabalho ainda não iniciado com o critical start time quase atingido, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta os critérios de inclusão na hot list e a restrição a trabalhos iniciais da rede.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | hot list=hot list, critical network=rede crítica |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | The hot list includes any critical network jobs that have a real or potential impact on the timely completion of the critical job... Note that only the jobs beginning the current critical network, for which there is no predecessor, can be included in the hot list. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | wsa-hot |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, trabalhos da rede crítica que tenham impacto real ou potencial no cumprimento do deadline do trabalho crítico são adicionados a uma hot list associada ao trabalho crítico; apenas os trabalhos que iniciam a rede crítica atual (sem predecessor) podem ser incluídos na hot list, por razões como erro, duração excedendo o longDurationThreshold, ou trabalho ainda não iniciado com o critical start time quase atingido, conforme documentação oficial?


---

### 63. `hwa-10.2.8-wsa-plan-monitor-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Plan Monitor verifica constantemente a rede crítica para assegurar o cumprimento do deadline; quando ocorrem mudanças que afetam os tempos (adição/remoção de trabalhos ou dependências follows), ele solicita ao Time Planner o recálculo dos horários críticos, e, quando um trabalho da rede é concluído, os tempos dos trabalhos seguintes são recalculados considerando a duração real, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o monitoramento contínuo e recálculo dinâmico de tempos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Plan Monitor=Plan Monitor, Time Planner=Time Planner |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Using workload service assurance |
| Citacao de suporte | Plan Monitor constantly checks the critical network to ensure that the deadline of the critical job can be met. When changes that have an impact on timings are made to the critical network... Plan Monitor requests Time Planner to recalculate the critical start times. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| verbs | plan |
| Familia | wsa-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Plan Monitor verifica constantemente a rede crítica para assegurar o cumprimento do deadline; quando ocorrem mudanças que afetam os tempos (adição/remoção de trabalhos ou dependências follows), ele solicita ao Time Planner o recálculo dos horários críticos, e, quando um trabalho da rede é concluído, os tempos dos trabalhos seguintes são recalculados considerando a duração real, conforme documentação oficial?


---

### 64. `hwa-9.5-real-enlegacyid-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `jobstream`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5 (IBM Workload Scheduler), a opcao global enLegacyId (legacy job stream identifier mode, usada em TWS 8.x) NAO e mais suportada: a partir da 9.5 ela foi removida, o identificador de job stream (jobstream_id) passa a ser gerado conforme descrito no comando showjobs, e job streams com carry forward passam a manter seus nomes e identificadores originais (reportando entre chaves {} a data do carry forward). Comportamento real e distinto da 8.x; generalizar o modo legado da 8.x para 9.5 produz resposta errada.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (global options 9.5). Contraste de versao: enLegacyId existia em TWS 8.x e foi removido a partir da 9.5; nao usar como comportamento de 9.5/10.2.8.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | HCL Workload Automation 9.5 global options (awsadgloboptdescr) |
| Citacao de suporte | enLegacyId Starting from version 9.5, this option is no longer supported. As a result, the job stream identifier jobstream_id is generated as described in showjobs. Carried forward job streams now keep their original names and identifiers, and they report between braces {} the date when they were carried forward. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | enLegacyId=opcao global de identificador legado de job stream (removida a partir de 9.5), jobstream_id=identificador do job stream gerado como descrito em showjobs, carry forward=manutencao de job streams entre periodos de plano |
| Capacidade | jobstream |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| verbs | showjobs |
| Familia | real-enlegacyid |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5 (IBM Workload Scheduler), a opcao global enLegacyId (legacy job stream identifier mode, usada em TWS 8.x) NAO e mais suportada: a partir da 9.5 ela foi removida, o identificador de job stream (jobstream_id) passa a ser gerado conforme descrito no comando showjobs, e job streams com carry forward passam a manter seus nomes e identificadores originais (reportando entre chaves {} a data do carry forward)?


---

### 65. `hwa-lab-10.2.8-calendar-freedays-0057`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `calendar`

**Afirmacao / Conteudo:**

In the HWA laboratory, a calendar object was created with $calendar NAME followed by free dates in mm/dd/yy. The calendar name is limited to 8 characters in the root folder. A job stream referencing FREEDAYS LABCAL before ON RUNCYCLE validated and was added.

> **ATENCAO / RESSALVAS DE USO:** FREEDAYS keyword must appear before ON RUNCYCLE. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer add and list calendar

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Calendar and freedays |
| Citacao de suporte | $calendar LABCAL; 12/25/26 01/01/26; FREEDAYS LABCAL validated. Name max 8 in root. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | calendar |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=calendar |
| Status de revisao | verified |


---

### 66. `hwa-lab-10.2.8-deadline-onlate-0056`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job defined with DEADLINE 0001 ONLATE KILL ran past its deadline; the stream became SUCC but the job DLJOB was suppressed and shown as HOLD with [Suppressed]; [Late] <00:01, demonstrating the deadline/onlate action.

> **ATENCAO / RESSALVAS DE USO:** ONLATE STOP is not a valid action; KILL was accepted. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sj DEAD_TEST

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Deadline and onlate behavior |
| Citacao de suporte | DLJOB HOLD [Until] [Suppressed]; [Late] <00:01. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | deadline |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['kill'], result=DLJOB HOLD [Until] [Suppressed]; [Late] <00:01. | ONLATE STOP is not a valid action; KILL was accepted., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-deadline.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=deadline |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, a job defined with DEADLINE 0001 ONLATE KILL ran past its deadline; the stream became SUCC but the job DLJOB was suppressed and shown as HOLD with [Suppressed]; [Late] <00:01, demonstrating the deadline/onlate action?


---

### 67. `hwa-lab-10.2.8-every-stream-job-execution-0037`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

In the HWA laboratory, an ad hoc submission of the stream CPLXJOB2M containing a job-level EVERY 0002 executed the first CPLX_EVERY instance at 14:59 and a second every run at 15:01; both completed SUCC with return code 0.

> **ATENCAO / RESSALVAS DE USO:** This record specifically validates job-level EVERY. The stream-level EVERY tests separately produced repeated planned instances. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman showjobs and JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Job-level EVERY execution |
| Citacao de suporte | CPLX_EVERY SUCC 14:59; every run CPLX_EVERY SUCC 15:01; JobManager AWSITA031I/AWSITA034I for both job IDs. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=every |
| Status de revisao | verified |


---

### 68. `hwa-lab-10.2.8-interactive-prompts-and-conman-reply-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HWA 10.2.8, prompts de interação humana ($PROMPT) possuem limite estrito de 8 caracteres no nome e, quando vinculados a um job, retêm o job em HOLD com anotação do prompt ID (ex: #505(PRM_LAB)) e o job stream em estado STUCK. A lista de pendências é visualizada via 'conman showprompts' (estado ASKED) e liberada imediatamente pelo operador com o comando 'conman reply <id>;yes', promovendo o job para execução e conclusão com SUCC.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:43:40-03:00 |

**Procedimento executado:** Criado objeto $PROMPT PRM_LAB (AWSJCL003I). Submetido schedule MDM#JS_PROMPT_RUN com JOB_PROMPTED condicionado ao prompt. Stream entrou em STUCK e job em HOLD #505. Comando showprompts exibiu 'ASKED 505(PRM_LAB)'. Executado 'reply 505;yes;noask', liberando o job para SUCC rc0 e promovendo o stream para SUCC.

**Saida real observada:** Ciclo completo de governança e aprovação por prompt comprovado: STUCK -> ASKED -> reply -> SUCC.

**Perguntas relacionadas:**

- Como funciona a dependência de aprovação humana por PROMPT no HWA e qual o tamanho máximo do seu nome?
- Qual comando conman exibe os prompts pendentes aguardando resposta do operador?
- Como o operador responde e libera um prompt no conman?


---

### 69. `hwa-lab-10.2.8-onoverlap-0062`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `jobstream`

**Afirmacao / Conteudo:**

In the HWA laboratory, job streams with ONOVERLAP PARALLEL and ONOVERLAP DONOTSTART both validated and their jobs completed SUCC.

> **ATENCAO / RESSALVAS DE USO:** Parallel allows overlapping runs; donotstart prevents a new run until the previous completes. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer add and conman sj

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Onoverlap handling |
| Citacao de suporte | OOVPAR_TEST and OOVDN_TEST SUCC. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | onoverlap |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=jobstream |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, job streams with ONOVERLAP PARALLEL and ONOVERLAP DONOTSTART both validated and their jobs completed SUCC?


---

### 70. `hwa-lab-10.2.8-recovery-stop-continue-rerun-0038`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `recovery`

**Afirmacao / Conteudo:**

In the HWA laboratory, RECOVTEST demonstrated recovery behavior: FAIL_STOP ended ABEND with return code 7; FAIL_CONT ended ABEND but used RECOVERY CONTINUE; FAIL_RERUN first ended ABEND and then reran after one minute, completing SUCC with return code 0 on the first retry.

> **ATENCAO / RESSALVAS DE USO:** The stream overall was ABEND because it contained the STOP failure. The rerun script was stateful and succeeded on its retry. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman showjobs and JobManager_message.log [P19 ADU 2026-08-20: risk corrigido de destructive para mutating; claim observacional de laboratorio, sem acao destrutiva]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Recovery STOP CONTINUE RERUN execution |
| Citacao de suporte | FAIL_STOP ABEND ... 7; FAIL_CONT ABEND ... 7; FAIL_RERUN ABEND ... 7; rerun 1 of 2 FAIL_RERUN SUCC ... 0. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | recovery |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rerun'], result=FAIL_STOP ABEND ... 7; FAIL_CONT ABEND ... 7; FAIL_RERUN ABEND ... 7; rerun 1 of 2 FAIL_RERUN SUCC ... 0. | The stream overall was ABEND because it contained the STOP failure. The rerun script was stateful and succeeded on its retry., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-recovery-execution.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=recovery |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, RECOVTEST demonstrated recovery behavior: FAIL_STOP ended ABEND with return code 7; FAIL_CONT ended ABEND but used RECOVERY CONTINUE; FAIL_RERUN first ended ABEND and then reran after one minute, completing SUCC with return code 0 on the first retry?


---

### 71. `hwa-lab-10.2.8-scheduling-needs-resource-naming-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o utilitário composer impõe um limite estrito de no máximo 8 caracteres para o nome de um recurso lógico ($RESOURCE), rejeitando nomes maiores com o erro AWSJOM012E. Recursos definidos com até 8 caracteres são consumidos com sucesso pela cláusula NEEDS dentro do Job Stream.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:32:00-03:00 |

**Procedimento executado:** Tentado adicionar recurso com nome DB_SEMAPHORE (AWSJOM012E The value specified for field 'resource name' exceeds the maximum length, which is 8). Corrigido para DB_SEM 2 no composer e submetido com cláusula NEEDS 2 DB_SEM no JOB_NEEDS_A e NEEDS 1 DB_SEM no JOB_NEEDS_B.

**Saida real observada:** Composer aceitou o recurso DB_SEM (AWSJCL003I) e o Batchman serializou a execução garantindo a disponibilidade das 2 unidades compartilhadas com SUCC.

**Perguntas relacionadas:**

- Qual é o tamanho máximo permitido para o nome de um recurso lógico no HWA composer?
- O que causa o erro AWSJOM012E ao criar um objeto $RESOURCE no composer?
- Como configurar uma dependência de recurso lógico compartilhado usando a cláusula NEEDS?


---

### 72. `hwa-lab-10.2.8-scheduling-recovery-rerun-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Ao configurar a instrução RECOVERY RERUN na definição de um job no HWA 10.2.8, quando a execução primária falha com return code diferente de zero (ABEND), o Batchman dispara automaticamente e de forma instantânea uma nova tentativa (>>rerun as) que, ao concluir com código 0, promove o job para SUCC.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:32:45-03:00 |

**Procedimento executado:** Definido JOB_AUTO_RECOVERY com RECOVERY RERUN. Na 1ª tentativa o script gerou exit 1 (#J568544 ABEND). O Batchman disparou automaticamente o rerun como #J568723 com exit 0 (SUCC), registrado no Symphony e na API REST v2.

**Saida real observada:** Saída do conman sj: JOB_AUTO_RECOVERY ABEND 10 ReturnCode 1 >>rerun as JOB_AUTO_RECOVERY SUCC 10 ReturnCode 0.

**Perguntas relacionadas:**

- Como funciona a recuperação automática de jobs com a diretiva RECOVERY RERUN no HWA?
- O que indica a anotação '>>rerun as' na saída do comando conman showjobs?
- Um job que falha na primeira tentativa pode se recuperar automaticamente sem intervenção manual do operador?


---

### 73. `hwa-lab-10.2.8-variable-table-native-0046`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `vartable`

**Afirmacao / Conteudo:**

In the HWA laboratory, variable table LABTAB was created with vartable/members/end syntax and variable VARMARK=LAB_VALUE_OK. A native UNIX docommand job using ${VARMARK} produced no substitution (VALUE_IS_), while the same job using ^VARMARK^ produced VALUE_IS_LAB_VALUE_OK.

> **ATENCAO / RESSALVAS DE USO:** The variable table must be assigned at job-stream level with VARTABLE before ON RUNCYCLE. Native job types use the caret syntax for variables; ${var} is for dynamic-agent integration jobs. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local Composer/conman execution plus https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtabledefn.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Variable table and native job substitution |
| Citacao de suporte | JCLFILE echo VALUE_IS_LAB_VALUE_OK; output VALUE_IS_LAB_VALUE_OK. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | vartable |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=vartable |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, variable table LABTAB was created with vartable/members/end syntax and variable VARMARK=LAB_VALUE_OK?


---

### 74. `hwa-lab-10.2.8-vartable-resolution-and-missing-vars-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HWA 10.2.8, variáveis definidas em uma VARTABLE e referenciadas no JCL com circunflexos (^VAR^) são resolvidas e interpoladas dinamicamente pelo Batchman no momento do despacho para o Jobman. Se uma variável referenciada não existir na tabela associada nem na tabela default (MAIN_TABLE), o HWA não interrompe o parsing nem cancela a submissão, repassando a string literal original com circunflexos (^VAR_NAME^) para a execução do script.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8 |
| Observado em | 2026-09-09T22:42:45-03:00 |

**Procedimento executado:** Criado schedule MDM#JS_VAR_RUN associado a VARTABLE LAB_VAR_TBL contendo LAB_MSG e LAB_PORT. Submetido no plano com conman sbs: JOB_VARTABLE_OK resolveu os valores 'MSG_VAL_CONTAINER_RHEL9' e '9090' no stdlist; JOB_VAR_MISSING manteve '^VAR_QUE_NAO_EXISTE^' literal no stdlist.

**Saida real observada:** Stdlist comprovou substituição perfeita de variáveis existentes e preservação literal sem falha de parsing para variáveis ausentes.

**Perguntas relacionadas:**

- Como funciona a interpolação de variáveis de uma VARTABLE no JCL de um job do HWA?
- O que acontece em tempo de execução quando um job referencia uma variável inexistente em sua VARTABLE?
- Qual é o comportamento do Batchman ao despachar um job com sintaxe ^VAR^ para o Jobman?


---
