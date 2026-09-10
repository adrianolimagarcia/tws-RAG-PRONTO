# OUTROS

> Total de tópicos canônicos cobertos nesta seção: 1608

---

### 1. com-change-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
Uma prática recomendada para mudanças em produção é exigir justificativa usando a capacidade opcional de auditoria do Dynamic Workload Console (Administration > Security > Auditing Preferences), que força cada usuário a fornecer um motivo para alterar um objeto, e usar a trilha de auditoria (usuário, data/hora, motivo) para revisão pós-mudança. A política de exigir justificativa é opcional e configurável; a HCL não a torna obrigatória por padrão.

**Plataforma / Validação:** Distributed

---

### 2. com-config-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Uma prática recomendada de configuração avançada para isolamento multi-tenancy é usar folders/pastas e security domains distintos por unidade de negócio ou aplicação, combinando a estrutura de pastas do composer com o modelo de segurança baseado em papéis (ACLs, security roles e security domains) para isolar o acesso de cada tenant aos seus objetos de agendamento. O produto fornece os mecanismos (folders, role-based security), mas o desenho de isolamento por tenant é decisão organizacional, não prescrita pela HCL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 3. hwa-10.1-real-ocli-intro-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1 Fix Pack 1, o Orchestration CLI (OCLI) foi introduzido como interface de linha de comando para executar jobs e job streams no plano e interagir com o servidor; em 10.1/10.2.0 o OCLI suporta apenas comandos do plano (adddep, altjob, cancel, confirm, deldep, kill, limit sched, listfolder, release, rerun, showcpu, showjobs, showschedules, submit docommand/job/sched); comandos model nao existem nessas versoes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 Fix Pack 1, o Orchestration CLI (OCLI) foi introduzido como interface de linha de comando para executar jobs e job streams no plano e interagir com o servidor; em 10.1/10.2.0 o OCLI suporta apenas comandos do plano (adddep, altjob, cancel, confirm, deldep, kill, limit sched, listfolder, release, rerun, showcpu, showjobs, showschedules, submit docommand/job/sched); comandos model nao existem nessas versoes?*

---

### 4. hwa-10.1-real-ocli-plan-only-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1; 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1 e 10.2.0, o Orchestration CLI suportava apenas comandos plan; a familia de comandos model (list, delete, etc.) foi adicionada em versoes posteriores (10.2.2+). Qualquer exemplo de funcao de chamada que use ocli model para 10.1/10.2.0 e invalido.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.1 e 10.2.0, o Orchestration CLI suportava apenas comandos plan; a familia de comandos model (list, delete, etc?*

---

### 5. hwa-10.2-composer-command-inventory-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O índice oficial HCL 10.2.0 enumera os comandos Composer, que administram objetos de scheduling no banco de dados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 6. hwa-10.2-composer-xagent-host-check-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.0, a definição Composer de um Extended Agent usa type x-agent e host para identificar a workstation HWA física hospedeira; uma workstation física pode hospedar múltiplos X-Agents.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 7. hwa-10.2-distributed-awsjdb801e-troubleshooting-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, a mensagem AWSJDB801E indica um erro interno genérico de acesso ao banco; suas causas conhecidas incluem memória insuficiente do lock list do DB2 (DSRA0010E, SQL State 57011, Error -912), log de transações cheio, storage insuficiente no application heap, falha de autenticação de conexão e, em Oracle, ORA-01000 (máximo de cursores abertos).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB801E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB801E no HWA?*
- *Qual é o significado da mensagem de erro DSRA0010E no HWA?*
- *Como solucionar ou diagnosticar o erro DSRA0010E no HWA?*
- *Qual é o significado da mensagem de erro AWSJDB801E no HWA e qual ação é recomendada?*

---

### 8. hwa-10.2-distributed-composer-delete-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O comando composer delete remove do banco as definições dos objetos selecionados.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 9. hwa-10.2-distributed-composer-query-output-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No composer, display apresenta a definição inteira, list apresenta nomes e atributos resumidos, e print equivale a display com ;offline.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 10. hwa-10.2-distributed-composer-validate-syntax-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O comando composer validate filename;syntax verifica erros de sintaxe nas definições do arquivo sem aplicá-las ao banco.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 11. hwa-10.2-perfreport-cpu-utilization-101-compare-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No relatorio de performance oficial do HCL Workload Automation 10.2, com ~43.000 job streams no plano, a utilizacao media de CPU na carga maxima (~5.000 jobs/min) mostrou aumento de 15%-20% em comparacao com a versao 10.1, tanto no MDM quanto no servidor de banco; os valores sao especificos do ambiente de teste e nao devem ser tratados como requisito universal.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No relatorio de performance oficial do HCL Workload Automation 10.2, com ~43.000 job streams no plano, a utilizacao media de CPU na carga maxima (~5.000 jobs/min) mostrou aumento de 15%-20% em comparacao com a versao 10.1, tanto no MDM quanto no servidor de banco; os valores sao especificos do ambiente de teste e nao devem ser tratados como requisito universal?*

---

### 12. hwa-10.2-perfreport-plan-replication-threads-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mirrorbox [mirrorbox]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2, o recurso de replicacao de plano (mirroring) foi melhorado com paralelismo e caching; por padrao sao 6 threads com 6 filas mirrorbox_.msg; sob taxas altas (milhares de atualizacoes de status por minuto) ou latencia de rede entre o master domain manager e o banco, pode ser necessario ajustar a configuracao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, o recurso de replicacao de plano (mirroring) foi melhorado com paralelismo e caching; por padrao sao 6 threads com 6 filas mirrorbox_?*

---

### 13. hwa-10.2-perfreport-sub-processors-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 FP0 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
O relatório de performance 10.2 recomenda ajustes documentados, como subProcessors=10, cachesize=70000, filecachesize=40000 e cachemaxage=21600000 em TWSConfig.properties para replicação de plano, e descreve configs de datasource e heap do DWC/MDM.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O relatório de performance 10.2 recomenda ajustes documentados, como subProcessors=10, cachesize=70000, filecachesize=40000 e cachemaxage=21600000 em TWSConfig?*

---

### 14. hwa-10.2-showcpus-standard-xagent-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.0, a saída standard de showcpus/sc identifica X-AGENT como tipo de workstation no campo NODE; HOST não é coluna desse formato.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.0, a saída standard de showcpus/sc identifica X-AGENT como tipo de workstation no campo NODE; HOST não é coluna desse formato?*

---

### 15. hwa-10.2-showcpus-xagent-host-preflight-0030

**Escopo & Contexto:** `[Escopo: IBM Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em IBM Workload Automation Distributed 10.2.0, sc @!@;link é documentado para mostrar links de todas as workstations e, para Extended Agents, o campo HOST identifica a workstation hospedeira; a saída padrão deve ser correlacionada para identificar linhas X-AGENT.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em IBM Workload Automation Distributed 10.2.0, sc @!@;link é documentado para mostrar links de todas as workstations e, para Extended Agents, o campo HOST identifica a workstation hospedeira; a saída padrão deve ser correlacionada para identificar linhas X-AGENT?*

---

### 16. hwa-10.2.3-dwc-derby-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation / Dynamic Workload Console 10.2.3 (distributed; UNIX e Windows) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.3, o Apache Derby não é mais suportado para o Dynamic Workload Console.

**Plataforma / Validação:** distributed; UNIX e Windows

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.3, o Apache Derby não é mais suportado para o Dynamic Workload Console?*

---

### 17. hwa-10.2.4-composer-lock-contention-0040

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.4 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.4, tentar bloquear no Composer um objeto já bloqueado por outro usuário retorna erro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 18. hwa-10.2.4-showcpus-link-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.4 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.4, showcpus ou sc suporta o formato ;link para exibir informações sobre workstations e links.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, showcpus ou sc suporta o formato ;link para exibir informações sobre workstations e links?*

---

### 19. hwa-10.2.4-showjobs-hold-deps-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.4 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.4, sj @#@.@+state=hold;deps é documentado para exibir jobs no estado HOLD no formato de dependências.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, sj @#@?*

---

### 20. hwa-10.2.4-showjobs-props-unsatisfied-dependencies-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.4 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.4, showjobs ou sj com ;props exibe a propriedade runtime Not Satisfied Dependencies da instância de job selecionada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, showjobs ou sj com ;props exibe a propriedade runtime Not Satisfied Dependencies da instância de job selecionada?*

---

### 21. hwa-10.2.5-distributed-user-object-credential-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.5 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > credential [credential]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.5, o User Object Credential Management permite atualizar de forma centralizada e segura as senhas armazenadas nos user objects, aplicando a mudança de forma consistente no banco e nas instâncias do plano em uma única ação.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.5, o User Object Credential Management permite atualizar de forma centralizada e segura as senhas armazenadas nos user objects, aplicando a mudança de forma consistente no banco e nas instâncias do plano em uma única ação?*

---

### 22. hwa-10.2.8-AWKZSJ-001E-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; z/OS shadow job validation) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: messages > awkzsj [messages_awkzsj]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWKZSJ001E indica que o valor atribuído ao application name não é coerente com a definição XML de um z/OS shadow job; a causa documentada é um valor incorreto de application name, cujo valor correto é zShadowJob, e a recuperação é especificar zShadowJob e tentar novamente.

**Plataforma / Validação:** distributed; z/OS shadow job validation

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKZSJ001E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKZSJ001E no HWA?*
- *Qual é o significado da mensagem de erro AWKZSJ001E no HWA e qual ação é recomendada?*

---

### 23. hwa-10.2.8-AWKZSJ-002E-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; z/OS shadow job validation) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: messages > awkzsj [messages_awkzsj]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWKZSJ002E indica que a definição de namespace XML é desconhecida; a causa documentada é que a definição de namespace XML deve corresponder ao application name, e a recuperação é verificar se a definição de namespace está correta e tentar novamente.

**Plataforma / Validação:** distributed; z/OS shadow job validation

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKZSJ002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKZSJ002E no HWA?*
- *Qual é o significado da mensagem de erro AWKZSJ002E no HWA e qual ação é recomendada?*

---

### 24. hwa-10.2.8-EEL-HT15E-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; agent for z/OS) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem EELHT15E indica que o HTTP client do agente para z/OS falhou ao processar uma requisição para um destino; a causa documentada é um erro de comunicação HTTP com o Dynamic Workload Console, possivelmente por o destino estar indisponível, e a recuperação é verificar o estado da instância do Dynamic Workload Console e, se indisponível, executar startAppServer quando o WebSphere Application Server Liberty Base estiver em execução no master ou domain manager.

**Plataforma / Validação:** distributed; agent for z/OS

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELHT15E indica que o HTTP client do agente para z/OS falhou ao processar uma requisição para um destino; a causa documentada é um erro de comunicação HTTP com o Dynamic Workload Console, possivelmente por o destino estar indisponível, e a recuperação é verificar o estado da instância do Dynamic Workload Console e, se indisponível, executar startAppServer quando o WebSphere Application Server Liberty Base estiver em execução no master ou domain manager?*

---

### 25. hwa-10.2.8-EEL-IT01E-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; agent for z/OS) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem EELIT01E indica que o parâmetro TDWBHOSTNAME (hostname do Dynamic Workload Console) está ausente e é obrigatório; a causa documentada é que o agente para z/OS não pode iniciar porque o hostname do Dynamic Workload Console não foi fornecido, e a recuperação é fornecer o parâmetro de inicialização TDWBHOSTNAME e reiniciar o agente.

**Plataforma / Validação:** distributed; agent for z/OS

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELIT01E indica que o parâmetro TDWBHOSTNAME (hostname do Dynamic Workload Console) está ausente e é obrigatório; a causa documentada é que o agente para z/OS não pode iniciar porque o hostname do Dynamic Workload Console não foi fornecido, e a recuperação é fornecer o parâmetro de inicialização TDWBHOSTNAME e reiniciar o agente?*

---

### 26. hwa-10.2.8-EEL-SU09W-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; agent for z/OS) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem EELSU09W (warning) indica que um job não pôde ser liberado de hold e as tentativas repetidas falharam; a causa documentada é que o submit task não conseguiu comunicar com JES ao tentar liberar o job de hold, e a recuperação é determinar o status atual do job, liberá-lo manualmente se necessário e revisar o system log em busca de mensagens JES anteriores.

**Plataforma / Validação:** distributed; agent for z/OS

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELSU09W (warning) indica que um job não pôde ser liberado de hold e as tentativas repetidas falharam; a causa documentada é que o submit task não conseguiu comunicar com JES ao tentar liberar o job de hold, e a recuperação é determinar o status atual do job, liberá-lo manualmente se necessário e revisar o system log em busca de mensagens JES anteriores?*

---

### 27. hwa-10.2.8-aida-alert-definitions-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > alerts [aida_alerts]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor define alertas de anomalia por KPI com schema: definitionID (ex.: CONTINUOUS_JOBWKS), name, kpi (metric_name, ex.: application_wa_JobsByWorkstation_jobs), trigger {type: continuous|total, value: 10, timeFrame: 60, description}, periodicity ('1 hour'), isActive ('true'), alert-definition (CONTINUOUS|TOTAL). O trigger type 'continuous' detecta N anomalias CONSECUTIVAS dentro do periodo (ex.: 'Over 10 Consecutive Anomalies within 1 hour'); o 'total' detecta N anomalias TOTAIS no periodo ('Over 10 Anomalies within 1 hour'). O pacote instala 12 alert-definitions default (uma continuous + uma total para cada um de 6 KPIs): JOBWKS (jobs por workstation), JOBFOLDER (jobs por folder), JOBSTATUS (jobs por status), JOBTOTAL (total jobs), MESSAGE (message files fill percentile), INCOMPLETEPREDECESSOR_CRITICAL (WA critical job incomplete predecessor). As definicoes ficam no indice OpenSearch alert-definitions.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 28. hwa-10.2.8-aida-alerts-default-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > alerts [aida_alerts]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as alert definitions do AI Data Advisor ficam em um arquivo JSON dentro do HCL Workload Automation, recuperadas pelo AIDA Exporter e armazenadas no OpenSearch (indice alert-definitions); nao podem ser alteradas por usuarios. O pacote instala 12 definicoes default: para cada KPI de tendencia (jobs por folder/workstation/status/total, msgFileFill), uma definicao tipo continuous (10 anomalias CONSECUTIVAS em 60 min) e uma tipo total (10 anomalias TOTAIS em 60 min); para job history, continuous e total com value 2 e timeFrame 2880 min (2 dias); mais 2 para critical job incomplete predecessor (CONTINUOUS_INCOMPLETEPREDECESSOR_CRITICAL e TOTAL_INCOMPLETEPREDECESSOR_CRITICAL). Os usuarios podem pausar/resumir alertas (efeito imediato) e ativar/desativar a geracao, incluindo a opcao global Deactivate All Alerts. A sensibilidade pode ser ajustada via parametros ANOMALY_USE_TOLERANCE (default false), ANOMALY_FIXED_TOLERANCE (0.5), ANOMALY_PERCENTAGE_TOLERANCE (0.01), ALERT_ANOMALOUS_POINTS_REQUIRED e ALERT_ANOMALY_RANGE_MINUTES no common.env.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 29. hwa-10.2.8-aida-concepts-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > concepts [aida_concepts]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor (AIDA) define: KPI (indicador monitorado continuamente, ex.: numero de jobs concluidos no plano atual), Anomaly Source KPI (KPI cuja tendencia anomala disparou alerta), Correlated KPI (KPIs correlacionados adicionaveis a analise), Data Point (observacao singular de um KPI), Anomaly (ponto de dados fora da faixa esperada definida estatisticamente com base no historico), Alert (sequencia de anomalias de um KPI, ex.: 10 pontos consecutivos fora da faixa em 1 hora), Alert Instance (ocorrencia unica de um alerta, registrada no OpenSearch), Alert Severity (media dos desvios percentuais das anomalias que geraram o alerta; High > 30%, Medium 20-30%, Low < 20%), Anomaly Bounds (limites superior/inferior da faixa esperada), Alert Trigger (condicoes que definem um alerta; tipo continuous = pontos anomolos CONSECUTIVOS, total = pontos anomolos TOTAIS acima ou abaixo), Anomaly % (percentual de pontos fora da faixa no intervalo; <6 Low, 6-10 Medium, >10 High), Timerange (frequencia de checagem de anomalias, definida por PROPHET_ORCHESTRATOR schedule_alert do common.env) e Special Days (dias com sazonalidade - feriados, ferias - incluidos no modelo de predicao com tolerancia maior para evitar falsos positivos).

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 30. hwa-10.2.8-aida-credentials-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > credentials [aida_credentials]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as credenciais de conexao do AI Data Advisor ao servidor Workload Automation sao armazenadas CIFRADAS no OpenSearch (indice wa-credentials, doc id <host:port>), com a senha cifrada via openssl enc -AES-128-ECB -base64 -salt -pbkdf2 usando a chave derivada de OPENSSL_PASSWORD (definido no common.env). O fluxo interativo ./AIDA.sh add-credentials (ou config.sh add_credentials) coleta host (host:port), username, password, tipo de engine (y=distributed, n=zOS com engineName) e valida contra https://<host>/twsd/engine/info (distributed) ou /twsz/v1/<engineName>/engine/info (zOS). Para automacao sem TTY, chamar add_credentials <host> <user> <encrypted_password> direto no container aida-config (o dispatch final do config.sh so repassa 2 args: $1 $2).

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 31. hwa-10.2.8-aida-keycloak-email-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: aida > security [aida_security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a seguranca de acesso ao AI Data Advisor usa Keycloak (deployment Docker): realm chamado 'aida', com usuarios default aidaadmin (senha admin, role aida-admin - permite login direto na UI do AIDA, trabalhar com todos os KPIs, gerenciar special days, customizar tuning e pausar alertas) e admin (senha admin, role keycloak-admin - acesso ao admin console do Keycloak para definir usuarios/passwords). O Keycloak admin console fica em https://<ip>:<porta>/keycloak/auth/admin. Se o Keycloak nao for usado, a autenticacao usa as roles do Dynamic Workload Console. A notificacao por email de alertas requer configuracao SMTP no common.env: SMTP_SERVER (hostname FQDN do SMTP), SMTP_PORT (porta TLS, ex.: 587), SENDER_MAILID (conta de email remetente), SENDER_MAILPWD (senha), RECIPIENT_MAILIDS (lista separada por virgula) e HOST_IP (IP:porta do AIDA). Alertas tambem aparecem no Anomaly Widget do Workload Dashboard e podem disparar event rules no HCL Workload Automation para abrir tickets.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 32. hwa-10.2.8-aida-kpi-catalog-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > kpis [aida_kpis]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor define KPIs (Key Performance Indicators) com schema: name, metric_name (ex.: application_wa_JobsInPlanCount_job_total), frequency (240 segundos = METRICS_FETCH_INTERVAL), category (Jobs|Queue), subcategory (Trend|Trend_by_wks), type (total quando sem keyprop), keyprop (jobstatus quando quebra por status de job), keyPropValues ([SUCCESSFUL, UNDECIDED, WAITING, ERROR, BLOCKED, SUPPRESS, READY, HELD, RUNNING, CANCELED]), labels ([workstation] quando por workstation), workstation (ex.: /MDMDA), metric_description, esQuery (agregacao OpenSearch: match metricname + term properties.parsedTag + match properties.jobstatus + term properties.workstation), alert-definition (definicoes de alerta vinculadas, ex.: [TOTAL_JOBTOTAL]), isActive. O doc id e '<name><metric_name><tag>'. O exporter baixa os KPIs do MDM (GET /twsd/engine/definition/kpi) e os armazena no indice kpis-definition.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 33. hwa-10.2.8-aida-kpi-types-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > kpis [aida_kpis]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor monitora KPIs definidos em um arquivo JSON dentro do HCL Workload Automation (nao modificaveis por usuarios do AIDA), expostos segundo o padrao OpenMetrics. Os KPIs sao: (1) Number of jobs in plan by folder (by status), metric application_wa_JobsByFolder_jobs, divisao por job status (10), frequencia 240s; (2) Number of jobs in plan by workstation (by status), application_wa_JobsByWorkstation_jobs, frequencia 240s; (3) Number of jobs in plan by status, application_wa_JobsInPlanCount_job, frequencia 240s; (4) Number of total jobs in plan, application_wa_JobsInPlanCount_job_total, frequencia 240s; (5) Job history (start time & duration), metric job_history, divisao start time/duration, frequencia 86400s (diaria); (6) Available space for WA message files, application_wa_msgFileFill_percent, divisao por 12 queues, frequencia 240s. Os 10 job status sao: WAITING, READY, RUNNING, SUCCESSFUL, ERROR, CANCELED, HELD, UNDECIDED, BLOCKED, SUPPRESS. As 12 queues incluem Appserverbox.msg, Courier.msg, mirrorbox.msg, Mailbox.msg, Monbox.msgn, Moncmd.msg, auditbox.msg, clbox.msg, planbox.msg, Intercom.msg, pobox messages, server.ms.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 34. hwa-10.2.8-aida-metric-format-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > metrics [aida_monitoring]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor armazena as metricas coletadas do Workload Automation no indice OpenSearch metric-index-<data> (ex.: metric-index-08-25-2026) com schema: metricname (ex.: application_wa_JobsInPlanCount_job_total), category (Jobs), subcategory (Trend), value (numero), @timestamp (epoch millis), properties (jobstatus quando quebra por status, mp_scope: application, parsedTag: wawaserver31116), tag (wa-waserver:31116), parsedTag (tag sem caracteres especiais), uuid, e keyprop (jobstatus) quando a metrica quebra por status. Exemplo real: {"metricname":"application_wa_JobsInPlanCount_job","keyprop":"jobstatus","properties":{"jobstatus":"SUCCESSFUL","mp_scope":"application","parsedTag":"wawaserver31116"},"value":26,"tag":"wa-waserver:31116"}. O aida-predictor e o aida-ad consomem essas series temporais.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 35. hwa-10.2.8-aida-network-host-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: aida > networking [aida_troubleshoot]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, quando o Dynamic Workload Console/MDM engine rodam no HOST (fora do docker) e o AI Data Advisor roda em containers, os servicos AIDA precisam resolver o hostname do servidor WA (ex.: wa-waserver) via rede docker; em lab com host-only, e necessario adicionar extra_hosts no docker-compose.yml (ex.: 'wa-waserver:host-gateway', 'MDMHOST:host-gateway', 'host.docker.internal:host-gateway') para os containers alcancarem o gateway do host (<gateway>). Sem isso, o aida-exporter falha com NameResolutionError ('Failed to resolve wa-waserver').

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 36. hwa-10.2.8-aida-retrain-specialdays-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > prediction [aida_predict]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor executa um retrain automatico de todos os KPIs a cada 24 horas (iniciado no start do container Orchestrator); durante o retrain a area de predicao nao fica visivel. Os Special Days (feriados por pais ou datas customizadas, com propriedades name/date/repeat/end repeat/description/status Active|Draft e opcoes de repeticao daily/weekly/monthly/yearly) sao incluidos no modelo de predicao com nivel de tolerancia MAIOR que dias normais, para evitar alertas falsos positivos em datas sazonais (feriados, ferias, ciclos de negocio). O tuning de predicao por KPI permite ajustar a sensibilidade de deteccao de anomalias (mais sensibilidade = mais anomalias detectadas); o Global tuning sobrescreve todos os KPIs e as mudancas sao aplicadas apos o proximo retrain. O timerange (frequencia de checagem de anomalias) e definido pelo parametro PROPHET_ORCHESTRATOR schedule_alert do common.env (default 15 minutos).

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 37. hwa-10.2.8-aida-special-days-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > prediction [aida_predict]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor usa o indice OpenSearch special-days-labels (95 docs) com feriados por estado/regiao para modelar sazonalidade no predictor: schema state (ex.: AO, AR, AW) e names (lista de nomes de feriados no idioma local, ex.: 'Ano novo', 'Carnaval', 'Dia Internacional da Mulher' para AO; 'Ano Nuevo [New Year's Day]' para AR). Esses feriados alimentam o modelo de predicao (prophet/neural) para ajustar as bandas de confianca em datas especiais.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 38. hwa-10.2.8-aida-ui-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: aida > ui [aida_ui]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a interface do AI Data Advisor (UI web) e acessivel em https://<aida-ip>:9432/ (porta default configurável via AIDA.sh set-custom-port) e responde HTTP 200 com uma SPA React (title 'AI Data Advisor (AIDA)'); o endpoint /healthz responde 200. O nginx do AIDA valida o header Host contra EXTERNAL_HOSTNAME (parametro do common.env, obrigatorio para evitar HTTP Host Header attacks): acessar via hostname/porta diferente (ex.: localhost vs <host>) retorna HTTP 405 'Host not matching'. Com Keycloak configurado, a UI e acessivel diretamente (https://aida-ip:9432/); sem Keycloak, o AIDA e acessado pelo widget de alerta no Workload Dashboard do DWC.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 39. hwa-10.2.8-capacity-bm-look-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A página de performance do HCL Workload Automation 10.2.8 documenta que os períodos de varredura do batchman (bm look), jobman (jm read, jm look) e mailman (mm read) no arquivo localopts afetam a performance: tempos menores geram varreduras mais frequentes usando mais CPU, enquanto tempos maiores fazem os jobs demorarem mais; recomenda testar em ambiente de teste antes de aplicar em produção e alterar um parâmetro por vez.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A página de performance do HCL Workload Automation 10.2.8 documenta que os períodos de varredura do batchman (bm look), jobman (jm read, jm look) e mailman (mm read) no arquivo localopts afetam a performance: tempos menores geram varreduras mais frequentes usando mais CPU, enquanto tempos maiores fazem os jobs demorarem mais; recomenda testar em ambiente de teste antes de aplicar em produção e alterar um parâmetro por vez?*

---

### 40. hwa-10.2.8-capacity-jm-job-table-size-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção localopts 'jm job table size' no HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão de 1024 entradas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção localopts 'jm job table size' no HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão de 1024 entradas?*

---

### 41. hwa-10.2.8-capacity-localopts-job-processing-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > optman [optman]]`

**Regra Canônica / Evidência:**
A página de performance do HCL Workload Automation 10.2.8 documenta que o processamento e monitoramento de jobs em uma workstation é controlado principalmente por parâmetros no arquivo localopts e pelas opções globais gerenciadas por optman, e recomenda contatar o suporte HCL Software para orientação de tuning nesses parâmetros em caso de problemas de performance.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar optman?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 42. hwa-10.2.8-capacity-log-cleanup-frequency-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
A opção global logCleanupFrequency (lc) no HCL Workload Automation 10.2.8 define com que frequência a limpeza automática de instâncias de log (event rule e audit management) é executada, com valores válidos de 0 a 60 minutos e padrão 5 minutos; valor 0 desativa a limpeza automática.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: A opção global logCleanupFrequency (lc) no HCL Workload Automation 10.2.8 define com que frequência a limpeza automática de instâncias de log (event rule e audit management) é executada, com valores válidos de 0 a 60 minutos e padrão 5 minutos; valor 0 desativa a limpeza automática?*
- *Qual o propósito e valor padrão da opção global logCleanupFrequency no optman do HWA?*

---

### 43. hwa-10.2.8-capacity-log-history-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
A opção global logHistory (lh) no HCL Workload Automation 10.2.8, usada na gestão de event rules, especifica o número de dias em que dados de regra, ação e mensagem são salvos, com padrão 10 dias e descarte FIFO (first-in first-out).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: A opção global logHistory (lh) no HCL Workload Automation 10.2.8, usada na gestão de event rules, especifica o número de dias em que dados de regra, ação e mensagem são salvos, com padrão 10 dias e descarte FIFO (first-in first-out)?*
- *Qual o propósito e valor padrão da opção global logHistory no optman do HWA?*

---

### 44. hwa-10.2.8-capacity-mm-cache-size-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção localopts 'mm cache size' no HCL Workload Automation 10.2.8 especifica o tamanho do cache de leitura do Mailman para mensagens de entrada, com valor máximo (padrão) de 512 mensagens, usado juntamente com a opção mm cache mailbox.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção localopts 'mm cache size' no HCL Workload Automation 10.2.8 especifica o tamanho do cache de leitura do Mailman para mensagens de entrada, com valor máximo (padrão) de 512 mensagens, usado juntamente com a opção mm cache mailbox?*

---

### 45. hwa-10.2.8-capacity-stats-history-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
A opção global statsHistory (sh) no HCL Workload Automation 10.2.8 especifica por quantos dias as estatísticas de jobs são mantidas, com padrão 400 dias e descarte FIFO; a documentação afirma que isso não afeta os arquivos stdlist de jobs, que devem ser removidos com o comando rmstdlist.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção global statsHistory (sh) no HCL Workload Automation 10.2.8 especifica por quantos dias as estatísticas de jobs são mantidas, com padrão 400 dias e descarte FIFO; a documentação afirma que isso não afeta os arquivos stdlist de jobs, que devem ser removidos com o comando rmstdlist?*

---

### 46. hwa-10.2.8-capacity-stdlist-retention-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 a retenção dos arquivos stdlist (standard list) de jobs não é controlada por uma opção global de dias, mas pelo comando rmstdlist; a documentação global options afirma que os arquivos stdlist devem ser removidos com o comando rmstdlist.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 a retenção dos arquivos stdlist (standard list) de jobs não é controlada por uma opção global de dias, mas pelo comando rmstdlist; a documentação global options afirma que os arquivos stdlist devem ser removidos com o comando rmstdlist?*

---

### 47. hwa-10.2.8-certman-generate-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando 'certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>]' gera um novo Certificate Authority (CA) e certificados TLS; keypasswd (minimo 6 caracteres) e outpath sao obrigatorios; o comando modifica permissoes apenas para novos arquivos criados no outpath; para definir wauser/wagroup o usuario que executa deve ter permissao de alterar owner e group.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, o comando 'certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>]' gera um novo Certificate Authority (CA) e certificados TLS; keypasswd (minimo 6 caracteres) e outpath sao obrigatorios; o comando modifica permissoes apenas para novos arquivos criados no outpath; para definir wauser/wagroup o usuario que executa deve ter permissao de alterar owner e group?*

---

### 48. hwa-10.2.8-certman-location-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a ferramenta Certman fica em TWS_INST_DIR/TWS/bin e suporta as acoes generate (novo CA), generate a partir de CA existente, extract de certificados de um keystore/truststore existente no master domain manager, verify da validade dos certificados, import de certificados do master domain manager para o Dynamic Workload Console e remove de um alias do keystore/truststore; Certman nao e suportado em sistemas operacionais IBM i; a versao pode ser verificada com 'certman version'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a ferramenta Certman fica em TWS_INST_DIR/TWS/bin e suporta as acoes generate (novo CA), generate a partir de CA existente, extract de certificados de um keystore/truststore existente no master domain manager, verify da validade dos certificados, import de certificados do master domain manager para o Dynamic Workload Console e remove de um alias do keystore/truststore; Certman nao e suportado em sistemas operacionais IBM i; a versao pode ser verificada com 'certman version'?*

---

### 49. hwa-10.2.8-certman-output-files-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, 'certman generate' produz na pasta outpath os arquivos ca.crt (Root CA), ca.key (chave privada da CA), tls.crt (certificado assinado e validado pela CA), tls.key (chave privada do certificado tls) e tls.sth (stash file do certificado contendo a senha codificada em Base64); a documentacao recomenda salvar ca.key para poder gerar ou substituir certificados no futuro e adicionar a CA ao SO e ao browser para confianca.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, 'certman generate' produz na pasta outpath os arquivos ca?*

---

### 50. hwa-10.2.8-certman-version-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a versao da ferramenta Certman pode ser verificada executando o comando 'certman version'; qualquer comando Certman tambem informa a localizacao dos arquivos de log.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a versao da ferramenta Certman pode ser verificada executando o comando 'certman version'; qualquer comando Certman tambem informa a localizacao dos arquivos de log?*

---

### 51. hwa-10.2.8-cli-jwt-mutex-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > jwt [jwt]]`

**Regra Canônica / Evidência:**
In HWA CLI connection parameters, JWT token authentication is mutually exclusive with username and password.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: In HWA CLI connection parameters, JWT token authentication is mutually exclusive with username and password?*

---

### 52. hwa-10.2.8-composer-add-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer add (short form a) adiciona uma definicao de objeto de agendamento ao banco a partir de um arquivo de texto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 53. hwa-10.2.8-composer-add-file-format-0135

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer add exige arquivo de definicao no formato $JOBS (com /WS#/JOB, DOCOMMAND, STREAMLOGON, TASKTYPE, RECOVERY), e NAO aceita a sintaxe schedlang antiga 'job WS#JOB' (que falha silenciosamente sem criar o objeto).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 54. hwa-10.2.8-composer-commands-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer gerencia definicoes de objetos de agendamento no banco e seus comandos podem ser abreviados ate tantos caracteres iniciais quanto necessarios para diferencia-los, alem de formas curtas dedicadas; os comandos incluem add (a), create/extract (cr/ext), delete (de), display (di, alias print p), edit (ed), list (l), listfolder (lf), lock (lo), mkfolder (mf), modify (m), new, rename (rn), renamefolder (rnf), replace (rep), rmfolder (rf), unlock (un), update (up), validate (val), version (v), authenticate (au), chfolder (cf), continue (co), redo (red), exit (e), help (h) e system command.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 55. hwa-10.2.8-composer-critical-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o keyword composer para marcar um job como critico e' a palavra 'critical', que e' um keyword de job statement dentro da definicao de job stream (.def): deve ser colocada na secao do job individual (apos o nome do job e suas dependencias/atributos), e NAO como atributo de job stream e NAO na linha $jobs da definicao de job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 56. hwa-10.2.8-composer-critical-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, jobs criticos incluidos no plano por run cycle DEVEM ter deadline especificado em nivel de job, job stream ou run cycle; jobs criticos submetidos sob demanda podem nao ter deadline, usando-se entao a opcao global deadlineOffset. O processamento da rede critica (critical start time, promocao, hot list) requer o Workload Service Assurance habilitado (opcao global enWorkloadServiceAssurance, abreviacao wa, default YES) e autorizacao DISPLAY/MODIFY/LIST no arquivo de seguranca.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 57. hwa-10.2.8-composer-delete-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer delete (short form de) remove definicoes de objetos de agendamento do banco; requer acesso delete aos objetos (ou permissao modify no arquivo de tipo de objeto com attribute name=security para objetos de seguranca); aceita wildcards, exige confirmacao por objeto a menos que ;noask seja usado, e ;force remove a definicao de workstation/workstation class do banco; o objeto nao pode estar bloqueado por outro usuario.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 58. hwa-10.2.8-composer-delete-noask-0137

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer delete pede confirmacao interativa ('Are you sure... enter y for yes') e SEM resposta NAO deleta (AWSBIA290I deleted 0). Para automacao nao-interativa, e necessario usar o sufixo ;noask (ex.: delete jd=...;noask), que deleta imediatamente (AWSJCL003I).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL003I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL003I no HWA?*
- *Qual é o significado da mensagem de erro AWSBIA290I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?*

---

### 59. hwa-10.2.8-composer-every-position-0120

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o keyword EVERY na definicao de job stream deve ser posicionado DENTRO dos parenteses do ON RUNCYCLE, nao fora. Exemplo correto: ON RUNCYCLE RC1 FREQ=DAILY; (AT 0700 EVERY 02:00). EVERY fora dos parenteses e rejeitado ou ignorado pelo parser.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 60. hwa-10.2.8-composer-extract-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer extract (short form ext, sinonimo create/cr) extrai uma definicao de objeto do banco e a escreve em um arquivo de texto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 61. hwa-10.2.8-composer-if-conddep-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a dependencia condicional em um job stream composer .def usa a sintaxe 'follows <predecessor> if <condition> [| <condition>...]', onde a condicao pode ser um status de job (SUCC, FAIL, ABEND, SUPPR) ou um nome de condicao definido via outputcond/succoutputcond na definicao do job predecessor; 'if' so e valido anexado a um follows (nao standalone), e multiplas condicoes sao separadas por pipe (|) de um unico tipo.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 62. hwa-10.2.8-composer-invocation-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o composer pode ser executado em modo batch ou interativo; a sintaxe de invocacao e 'composer [custom_parameters] [-file customPropertiesFile][connection_parameters] ["command[&[command]][...]"]'; aceita -cf (working directory), -file (custom properties file com HOST/PORT/PROTOCOL/PASSWORD/USERNAME etc.), e connection_parameters -host, -port, -protocol, -proxy, -proxyport, -jwt, -username, -password, -timeout, -defaultws; -jwt e mutuamente exclusivo com -username/-password.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 63. hwa-10.2.8-composer-join-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a sintaxe composer para join condition em um job stream .def e um bloco 'join <join_name> <number|numconditions|ALL> of description "..." ... endjoin' colocado dentro de um job statement (ou no nivel do job stream), contendo linhas 'follows <predecessor> if <condition>' dentro do bloco; o nome do join tem maximo 16 caracteres; number/0/ALL define quantas dependencias devem ser satisfeitas; maximo de 4 instancias de join por objeto com numero ilimitado de condicionais por join; em um job podem ser definidas dependencias padrao e condicionais internas e externas, em um job stream apenas internas; dependencias internetwork nao sao suportadas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 64. hwa-10.2.8-composer-js-name-limit-0114

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o nome de um job stream (SCHEDULE keyword) tem limite maximo de 16 bytes. Nomes descritivos longos sao rejeitados pelo composer validate/add com erro AWSBHW007E.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHW007E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHW007E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 65. hwa-10.2.8-composer-keyword-order-0115

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a ordem das keywords na definicao de job e obrigatoria. Para keywords validas em $JOBS, TASK ou DOCOMMAND deve vir primeiro, depois RECOVERY, e END por ultimo. IMPORTANTE: PRIORITY NAO e uma keyword valida em definicoes $JOBS (composer add/validate); seu uso causa AWSJOM915E unexpected token PRIORITY independentemente da posicao (ver claim hwa-10.2.8-composer-priority-in-jobs-0124). A ordem RECOVERY->PRIORITY->END so e relevante em contextos onde PRIORITY e valido (job stream $SCHEDULES, submissao sbj, chgjob).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM915E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 66. hwa-10.2.8-composer-list-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer list sem argumento lista ou imprime todas as definições do tipo de objeto especificado: calendars/cal, eventrule/erule/er, prompts/prom, parms (variáveis globais da tabela padrão), vartable/vt, resources/res, runcyclegroup/rcg, wat, workstation/ws, domain/dom, workstationclass/wscl, jobs/jd, sched/js, users, acl, sdom, srol — sempre com a redação 'If no argument follows, lists or prints all ... definitions'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 67. hwa-10.2.8-composer-list-print-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer list (l) mostra os nomes dos objetos com seus atributos em tela, enquanto o comando print envia essa lista para o dispositivo ou arquivo especificado na variável local MAESTROLP (que por padrão é '| lp -tCONLIST', redirecionável com > arquivo, >> arquivo, | comando ou || comando); list ;offline equivale a print; a variável MAESTROLP deve estar exportada no ambiente antes de executar print.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 68. hwa-10.2.8-composer-lock-unlock-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer lock (short form lo) bloqueia o acesso a objetos do banco e composer unlock (short form un) libera o bloqueio de objetos definidos no banco.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 69. hwa-10.2.8-composer-lock-unlock-0138

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, composer lock (lo) bloqueia um objeto do banco contra alteracoes de outros usuarios (aparece 'Locked By' no list), e composer unlock (ul) libera (AWSBIA308I). O lock e por usuario/sessao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA308I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA308I no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 70. hwa-10.2.8-composer-modify-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer modify (short form m) modifica ou adiciona objetos de agendamento no banco; ao modificar, extrai apenas os objetos que podem ser bloqueados pelo usuario atual; requer acesso add para adicionar novo objeto e acesso modify se o objeto ja existir; para modificar objetos de seguranca exige permissao modify no arquivo de tipo de objeto com attribute name=security.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 71. hwa-10.2.8-composer-new-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer new adiciona uma definição de objeto de agendamento no banco e abre um template predefinido que ajuda a editar a definição, gravando-a no banco ao salvar; os templates ficam na subpasta templates do diretório de instalação e podem ser customizados; exige acesso add ao adicionar um novo objeto (ou modify se o objeto já existir), e definições de event rule são abertas com um editor XML; tipos suportados incluem calendar, domain, eventrule, folder, job, jobstream, parameter, prompt, resource, runcyclegroup, user, vartable, wat, workstation, workstationclass, accesscontrollist, securitydomain, securityrole.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 72. hwa-10.2.8-composer-new-interactive-0122

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer new tipo e estritamente interativo e NAO aceita argumento de nome junto. composer new folder MEUPASTA falha com AWSBIA003E. Para criar objetos sem interacao use composer add com arquivo de definicao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA003E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA003E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 73. hwa-10.2.8-composer-onlate-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a keyword 'onlate' na definição de job dentro de job stream define a ação quando o deadline do job expira. A única ação suportada é 'kill': se o job estiver rodando quando o deadline expira, ele é morto e termina em estado ABEND; jobs dependentes não são liberados, exceto dependência condicional em ABEND. As ações CONTINUE, SUPPR, RERUN e STOP NÃO são valores válidos de onlate.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função da keyword onlate e da ação kill na definição de jobs no composer do HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 74. hwa-10.2.8-composer-onoverlap-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a keyword 'onoverlap' na definição de job stream aceita os valores parallel, enqueue e donotstart. parallel (default) inicia a próxima instância mesmo que a anterior não tenha terminado; enqueue não inicia até a anterior completar (implementado como follows interno que conta no limite de 40 dependências, permitindo no máximo 39 manuais); donotstart não inicia a próxima instância se ela não puder começar dentro de 4 minutos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 75. hwa-10.2.8-composer-opens-workstation-0125

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao definir uma file dependency OPENS em job stream via composer, o filename DEVE ser qualificado com a workstation (ex.: OPENS MDMDA#arquivo). Se usado apenas OPENS "arquivo" sem prefixo de workstation, o composer rejeita com AWSJOM115E 'The required workstation or workstation class has not been supplied for the file dependency'. A documentacao oficial mostra [[folder/]workstation#] como opcional, mas na pratica (validado em laboratorio) o prefixo e exigido para file dependencies em alguns contextos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM115E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM115E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar mdm?*

---

### 76. hwa-10.2.8-composer-outputcond-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a definicao de output condition e feita na definicao de JOB (nao no job stream) com os keywords composer 'succoutputcond <Condition_Name> "Condition_Value"' (condicao que qualifica o job como SUCC, ex. succoutputcond UPDATE_OK "(RC <= 3)") e 'outputcond <Condition_Name> "Condition_Value"' (condicao que determina qual sucessor roda, ex. outputcond STATUS_ERR1 "RC=1"); o valor da condicao usa expressoes de return code (RC operador valor) ou expressoes booleanas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 77. hwa-10.2.8-composer-presentation-order-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Composer validates scheduling objects in presentation order; referenced objects must be defined before objects referencing them.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 78. hwa-10.2.8-composer-priority-in-jobs-0124

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o keyword PRIORITY NAO e valido em definicoes de job no formato $JOBS (composer add/validate). O uso de PRIORITY em $JOBS causa erro AWSJOM915E unexpected token PRIORITY independentemente da posicao (antes ou depois de RECOVERY STOP). PRIORITY funciona APENAS em: (1) definicoes de $SCHEDULES (job stream level e job level), (2) submissao ad-hoc sbd/sbj com ;priority=n, e (3) comando chgjob. A documentacao oficial HCL adverte que keywords incorretas em $JOBS causam truncamento silencioso da definicao no banco de dados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM915E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 79. hwa-10.2.8-composer-prompt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, definições de prompt (marcador $prompt) têm nome de até 8 caracteres alfanuméricos incluindo traços e sublinhados, começando por letra, e texto de até 200 caracteres; se o texto começa com dois-pontos (:), o prompt é exibido sem exigir resposta para continuar; se começa com exclamação (!), é exibido mas não é registrado no log; parâmetros no texto do prompt devem ser delimitados por acentos circunflexos (^var^).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 80. hwa-10.2.8-composer-prompt-db-object-0127

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, referenciar PROMPT em uma job stream exige que o objeto prompt exista previamente no banco. Se nao existir, o composer rejeita com AWSJDB311E 'The prompt prom=X referenced by object ... does not exist'. A definicao do objeto prompt usa a sintaxe $PROMPT seguido do nome e do texto entre aspas: $PROMPT PROMPT1 "texto?" (sem keyword DESCRIPTION). O dataset nao ensina essa sintaxe de definicao de prompt.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB311E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB311E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 81. hwa-10.2.8-composer-prompt-name-limit-0126

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o nome de um objeto PROMPT (prom=) tem limite de 8 bytes. Nomes maiores causam AWSJOM012E 'The value X specified for field prompt dependency name exceeds the maximum length, which is 8'. A documentacao oficial usa exemplos curtos (ex.: PRMT3) mas nao explicita o limite de 8 caracteres para nomes de prompt.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM012E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM012E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 82. hwa-10.2.8-composer-recovery-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a keyword composer 'recovery' na definição de job aceita as opções stop, continue e rerun (default stop, sem recovery job e sem prompt). A sintaxe é: recovery {stop [after ...] [abendprompt "text"] | continue [after ...] [abendprompt "text"] | rerun [same_workstation] [[repeatevery hhmm] [for number attempts]] [after ...] [abendprompt "text"]}. Não existe a forma 'recovery rerun <n>'; o número de tentativas é especificado com 'rerun ... for <number> attempts' (default 1, máximo 10.000) e o intervalo com 'repeatevery hhmm' (default 0, máximo 99h59m).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 83. hwa-10.2.8-composer-rename-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer rename (abreviação rn) usa a sintaxe rename <tipo>=<identificador_antigo> <novo_identificador> [;preview], onde a keyword de tipo (cal=, parm=/vb=, vt=, prom=, res=, rcg=, jd=, js=, er=, ws=, wscl=, dom=, wat=, fol=, user= etc.) é declarada APENAS no identificador antigo e o novo identificador NÃO leva prefixo de tipo; a opção ;preview revisa o resultado sem realizar a operação e sem executar validação (por exemplo, não verifica a existência das pastas-alvo nem o uso de palavras reservadas em nomes de job/job stream).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 84. hwa-10.2.8-composer-rename-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer rename exige que o novo nome não identifique um objeto já definido no banco e que o objeto a renomear esteja desbloqueado ou bloqueado pelo usuário que emite o comando; a autorização para rename exige acesso de delete sobre o nome antigo e de add sobre o novo nome (objetos de segurança exigem modify no arquivo com name=security), e renomear domain managers não é suportado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 85. hwa-10.2.8-composer-rename-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer rename pode mover um objeto para um caminho de pasta cujos nomes derivam de strings contidas no nome do objeto (tokens), e a pasta-alvo deve já existir; wildcards são suportados apenas para nomes de job/job stream (ex.: rename js @#ROME_MILAN_@ @#/ROME/MILAN/@).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 86. hwa-10.2.8-composer-rename-positional-0136

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer rename usa sintaxe POSICIONAL 'rename <objeto_antigo> <objeto_novo>' (ex.: rename jd=MDMDA#JOB1 MDMDA#JOB2). A forma com keyword newname= (ex.: rename jd=...;newname=...) e rejeitada com AWSBIA349E.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA349E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA349E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 87. hwa-10.2.8-composer-replace-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer replace (short form rep) substitui objetos de agendamento no banco, normalmente a partir de um arquivo de texto editado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 88. hwa-10.2.8-composer-runcycle-weekly-every-0133

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, run cycles complexos sao validados e adicionados com sucesso pelo composer: (1) ON RUNCYCLE RC1 "FREQ=WEEKLY;BYDAY=TH" (AT 0700) e (2) ON RUNCYCLE RC1 "FREQ=DAILY;" (AT 0600 EVERY 0002 EVERYENDTIME 1200). Ambos validam com AWSJCL003I e sao persistidos no banco. O dataset ensina esses padroes corretamente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL003I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL003I no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 89. hwa-10.2.8-composer-runcyclegroup-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a keyword de definicao de um run cycle group em arquivo .def e 'runcyclegroup' (sem prefixo $); o prefixo '$RCG runcyclegroupname' e usado apenas para REFERENCIAR um run cycle group dentro de um job stream (clausula on/except), nunca para defini-lo. Usar '$runcyclegroup' como keyword de definicao causa erro de sintaxe (AWSBCZ021E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBCZ021E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCZ021E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual a finalidade e como utilizar a keyword 'runcyclegroup' em definições de jobs no composer?*

---

### 90. hwa-10.2.8-composer-runcyclegroup-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, a definicao de run cycle group em arquivo .def exige as clausulas 'runcyclegroup <nome>', 'vartable [folder/]tablename' (obrigatoria, nao opcional) e 'end' para fechar o bloco; deve conter ao menos um run cycle inclusivo sob a keyword 'on'. As opcoes disponiveis sao description, vartable, freedays, on/except, runcycle, validfrom/validto, date/day/calendar/request/icalendar, fdignore/fdnext/fdprev, subset, at/schedtime, until/jsuntil, onuntil, every/everyendtime, deadline, timezone/tz. As clausulas DEFINITIONNAME, FREQUENCY, EXTEND, OVERRIDE e APPEND NAO existem na definicao oficial de run cycle group em 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*

---

### 91. hwa-10.2.8-composer-runcyclegroup-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o nome de um run cycle group pode conter ate 8 caracteres alfanumericos, incluindo hifens (-) e underscores (_), e deve comecar com letra; a description pode ter ate 120 caracteres alfanumericos entre aspas duplas e nao pode conter aspas duplas internas, dois-pontos, ponto-e-virgula ou ampersand; o nome da vartable comeca com letra, aceita alfanumericos/hifens/underscores e ate 80 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 92. hwa-10.2.8-composer-runcyclegroup-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation, a mensagem AWSBCZ021E significa 'A definition keyword was expected at this point' (uma keyword de definicao era esperada neste ponto), indicando que o composer encontrou um token invalido onde esperava uma keyword de definicao de objeto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBCZ021E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCZ021E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual é o significado da mensagem de erro AWSBCZ021E no HWA e qual ação é recomendada?*

---

### 93. hwa-10.2.8-composer-stream-keyword-order-0129

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a ordem das keywords dentro de um job statement em job stream e obrigatoria. A ordem canonica documentada e: follows -> needs -> opens -> priority -> prompt -> nop (no nivel stream: follows -> needs -> opens -> priority -> prompt -> onoverlap). Colocar keywords fora de ordem (ex.: PROMPT apos uma sequencia de outros modificadores e depois iniciar outro job na linha seguinte) pode causar AWSJOM915E unexpected token no proximo job. Combinado com o aviso oficial de que keywords mal posicionadas truncam a definicao no banco, a ordem importa.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM915E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 94. hwa-10.2.8-composer-task-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o composer cria job definitions baseadas em JSDL usando o argumento 'task' na sintaxe $jobs [[folder/]workstation#][folder/]jobname task <job_definition_xml_jsdl> [description ...] [tasktype ...] [recovery ...]; o argumento task recebe a sintaxe XML JSDL (namespaces jsdl/jsdle), e nao JSON/YAML, com tamanho maximo de 4095 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 95. hwa-10.2.8-composer-task-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, embedded jobs (jobs embutidos dentro do job stream, definidos via schedlang com a keyword BUILTIN e TASK em formato JSON, ou via YAML kind: JobStream) NAO sao suportados pelos comandos composer, dataextract e dataimport; embedded jobs so' podem ser criados/gerenciados pelo Dynamic Workload Console / Graphical Designer.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 96. hwa-10.2.8-composer-update-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer update (short form up) modifica os atributos de tipos especificos de objetos de agendamento no banco sem usar modify ou replace, sem abrir editor de texto; requer acesso modify e display; sintaxe '{update | up} {cpu | workstation | workstationclass}; filter ...; set ignore=on|off [;noask]'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 97. hwa-10.2.8-composer-update-js-syntax-0139

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando composer update NAO aceita arquivo de job definition ($JOBS) diretamente — com arquivo retorna AWSBHW008E (espera job stream name) e com jd= retorna AWSBIA094E (espera keyword CPU/WORKSTATION). update e destinado a workstations/job streams, nao a job definitions via arquivo.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA094E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA094E no HWA?*
- *Qual é o significado da mensagem de erro AWSBHW008E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHW008E no HWA?*

---

### 98. hwa-10.2.8-composer-user-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, definições de usuário têm a sintaxe username [workstation#][domain\]username[@internet_domain] password "password" end; usuários usados como valor de streamlogon para definições de job no Windows DEVEM ter definição de usuário (não é exigido para jobs em outros sistemas operacionais); o campo username/domain-user/UPN pode ter até 47 caracteres e a senha até 31 caracteres (deve estar entre aspas; senha nula = "").

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 99. hwa-10.2.8-composer-validate-interdependent-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando composer 'validate' valida definicoes de objetos sem adiciona-las ao banco de dados; por isso, se um arquivo contiver objetos com dependencias entre si (ex.: job_tom com dependencia follows em job_harry), o validate reporta erro de dependencia mesmo com sintaxe correta, pois nao adiciona nenhuma definicao ao banco. Nao ha workaround com validate: deve-se garantir que nao haja interdependencias entre objetos no mesmo arquivo. Nos comandos add, new, create ou modify, o erro de interdependencia nao ocorre se o objeto referenciado for definido antes do dependente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como o composer valida definições de jobs com dependências interdependentes mútuas no banco?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 100. hwa-10.2.8-composer-validate-no-persist-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
The composer validate command checks syntax without persisting definitions into the database and can report errors on interdependent definitions. Context: Validation checks syntax only and does not add definitions to the database.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 101. hwa-10.2.8-composer-vartable-exists-0128

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, referenciar VARTABLE no cabecalho de uma job stream exige que a variable table exista previamente no banco. Se nao existir, o composer rejeita com AWSJDB322E 'The variable table vt=X referenced by object ... does not exist'. A definicao usa $VARTABLE com a sintaxe: vartable [folder/]table_name [description "desc"] members variablename "value" end. O dataset mostra VARTABLE em exemplos de streams mas nao explica que e um objeto separado pre-existente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB322E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB322E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 102. hwa-10.2.8-composer-vartable-position-0116

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a keyword VARTABLE na definicao de job stream deve ser declarada ANTES de ON RUNCYCLE. Se VARTABLE aparecer depois de ON RUNCYCLE, o composer rejeita com AWSJOM915E unexpected token VARTABLE.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM915E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 103. hwa-10.2.8-composerjwt-token-source-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O comando composer do HCL Workload Automation 10.2.8 aceita o parâmetro -jwt para autenticação por JSON Web Token entre o master domain manager e os agentes; o token é recuperado do Dynamic Workload Console e o parâmetro -jwt é mutuamente exclusivo com os parâmetros -username e -password.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 104. hwa-10.2.8-dbviews-events-0170

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
As views de evento do banco do HCL Workload Automation: EVENT_RULES_V (event rules definidas), EVENT_CONDITIONS_V (eventos associados a cada event rule), EVENT_RULE_ACTIONS_V (acoes associadas a cada event rule), EVENT_RULE_INSTANCES_V (historico de event rules executadas), ACTION_RUNS_V (acoes executadas por cada event rule), ACTION_PARAMETERS_V (parametros associados as acoes executadas) e LOG_MESSAGES_V (mensagens logadas pelas acoes). Usadas para auditoria e diagnostico de event-driven workload automation (EDWA). Fonte: IBM Workload Scheduler Database Views.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual é o propósito da view de banco EVENT_RULE_INSTANCES_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional EVENT_RULE_INSTANCES_V no banco de dados do HWA?*

---

### 105. hwa-10.2.8-dwc-default-tasks-language-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_ui > language [dwc_ui_language]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as default tasks (predefined tasks) do Dynamic Workload Console sao criadas no idioma configurado no navegador no PRIMEIRO login do usuario e NAO sao traduzidas quando o idioma do navegador muda depois; para ter as default tasks em outro idioma, o administrador Liberty deve criar um novo usuario do DWC e faze-lo fazer o primeiro login com o navegador configurado nesse idioma. A propriedade precannedTaskCreation do TdwcGlobalSettings.xml (valores all|none|distributed|zos) controla se/quais tasks pre-definidas sao criadas e e lida apenas no primeiro login do usuario.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as default tasks (predefined tasks) do Dynamic Workload Console sao criadas no idioma configurado no navegador no PRIMEIRO login do usuario e NAO sao traduzidas quando o idioma do navegador muda depois; para ter as default tasks em outro idioma, o administrador Liberty deve criar um novo usuario do DWC e faze-lo fazer o primeiro login com o navegador configurado nesse idioma?*

---

### 106. hwa-10.2.8-dwc-derby-unsupported-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
Apache Derby database is unsupported for Dynamic Workload Console starting from HWA version 10.2.3. Context: Apache Derby is no longer supported as a database for Dynamic Workload Console starting from Version 10.2.3.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Apache Derby database is unsupported for Dynamic Workload Console starting from HWA version 10.2.3. Context: Apache Derby is no longer supported as a database for Dynamic Workload Console starting from Version 10.2.3.?*

---

### 107. hwa-10.2.8-dwc-login-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o login no Dynamic Workload Console usa o form login padrao do Liberty (POST /console/j_security_check com j_username/j_password): em caso de sucesso retorna 302 para /console/ e emite cookie LtpaToken2 (SSO); o registro de usuarios e o basicRegistry com realm TWSRealm, usuario principal definido por user.twsuser.id/user.twsuser.password (wauser_variables.xml) e grupo de administradores definido por admin.group.name (default Admins) no authentication_config.xml; apos o login o dashboard e servido em /console/dashboard/index.jsp.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 108. hwa-10.2.8-dwc-mdm-distinct-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Dynamic Workload Console (DWC) and the MDM engine are distinct architectural components; the DWC is an independent web application and the DWC version must be equal to or higher than the version of any engine it connects to. Official Release Notes compatibility tables list the engine versions each DWC release can connect to (e.g. DWC 10.2.0 connects to MDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4), i.e. same-version or earlier engines.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Dynamic Workload Console (DWC) and the MDM engine are distinct architectural components; the DWC is an independent web application and the DWC version must be equal to or higher than the version of any engine it connects to?*

---

### 109. hwa-10.2.8-dwc-sso-basic-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_ui > authentication [dwc_authentication]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Dynamic Workload Console (DWC) usa autenticacao baseada em LTPA (Lightweight Third Party Authentication) sobre o Liberty WebSphere. O login e feito via POST /console/j_security_check com j_username e j_password; o servidor retorna HTTP 302 com cookie LtpaToken2. O DWC suporta autenticacao por basicRegistry (usuarios definidos em authentication_config.xml) ou federated repositories (LDAP). O arquivo de configuracao de usuarios fica em DWC_DATA/usr/servers/dwcServer/configDropins/overrides/authentication_config.xml. O grupo administrador e definido pela propriedade admin.group.name (default: Admins) e o usuario instalador pertence a este grupo.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 110. hwa-10.2.8-dwc-trace-configdropins-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, os traces do Dynamic Workload Console são ativados editando o template trace.xml e copiando-o de configDropins/templates para configDropins/overrides; as alterações são efetivas imediatamente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, os traces do Dynamic Workload Console são ativados editando o template trace?*

---

### 111. hwa-10.2.8-dwc-ui-language-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_ui > language [dwc_ui_language]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o idioma da interface do Dynamic Workload Console segue o idioma configurado no navegador do usuario (header HTTP Accept-Language): nao existe seletor de idioma na pagina de login nem propriedade de idioma no TdwcGlobalSettings.xml; para mudar a interface de portugues para ingles basta configurar o navegador para ingles e refazer o login. O kit instala 14 locales em Console.war/locale/ (en, pt-br, es, fr, de, it, ja, ko, zh-CN, zh-TW, ru, hi, kn, ta).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o idioma da interface do Dynamic Workload Console segue o idioma configurado no navegador do usuario (header HTTP Accept-Language): nao existe seletor de idioma na pagina de login nem propriedade de idioma no TdwcGlobalSettings?*

---

### 112. hwa-10.2.8-enigma-r3batch-sap-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
Do not paste or request real passwords. In HCL Workload Automation Distributed 10.2.8, the r3batch access method connects the product to SAP R/3 systems, and SAP user passwords can be encrypted with the enigma utility (in TWA_home/methods) before being written into r3batch.opts files, producing {aes}... values. Perform this in the approved environment, never here in the conversation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Do not paste or request real passwords?*

---

### 113. hwa-10.2.8-event-designer-0036

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
The menu paths Design > Orchestrate and Administration > Manage event rules are not documented in HCL Workload Automation 10.2.8. The documented DWC locations for working with event rules are the Workload Designer and the Monitor Event Rules task.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: The menu paths Design > Orchestrate and Administration > Manage event rules are not documented in HCL Workload Automation 10.2.8. The documented DWC locations for working with event rules are the Workload Designer and the Monitor Event Rules task?*

---

### 114. hwa-10.2.8-event-domain-manager-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O event processing server no HCL Workload Automation 10.2.8 normalmente está localizado no master domain manager e recebe todos os eventos dos agents e os processa, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 normalmente está localizado no master domain manager e recebe todos os eventos dos agents e os processa, conforme documentação oficial?*

---

### 115. hwa-10.2.8-event-editing-event-rules-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser editadas na tarefa Editing event rules, sob Designing your workload, e após a edição a regra pode ser monitorada pela tarefa Monitor Event Rules, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser editadas na tarefa Editing event rules, sob Designing your workload, e após a edição a regra pode ser monitorada pela tarefa Monitor Event Rules, conforme documentação oficial?*

---

### 116. hwa-10.2.8-event-event-rule-instance-status-0038

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o administrador ou operador revisa o status das instâncias de event rules e das ações executadas no banco de dados e nos logs, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o administrador ou operador revisa o status das instâncias de event rules e das ações executadas no banco de dados e nos logs, conforme documentação oficial?*

---

### 117. hwa-10.2.8-event-external-events-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, eventos externos, como mensagens escritas em arquivos de log, eventos enviados por aplicações de terceiros e arquivos criados, atualizados ou excluídos, podem ser usados para acionar regras, inclusive em nós que não executam o HCL Workload Automation via comando sendevent, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, eventos externos, como mensagens escritas em arquivos de log, eventos enviados por aplicações de terceiros e arquivos criados, atualizados ou excluídos, podem ser usados para acionar regras, inclusive em nós que não executam o HCL Workload Automation via comando sendevent, conforme documentação oficial?*

---

### 118. hwa-10.2.8-event-file-monitor-events-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Os eventos do provider FileMonitor no HCL Workload Automation 10.2.8 são FileCreated, FileDeleted, ModificationCompleted e LogMessageWritten, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os eventos do provider FileMonitor no HCL Workload Automation 10.2.8 são FileCreated, FileDeleted, ModificationCompleted e LogMessageWritten, conforme documentação oficial?*

---

### 119. hwa-10.2.8-event-generic-action-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Os action providers documentados no HCL Workload Automation 10.2.8 são GenericAction, MailSender, MessageLogger, TWSAction, TWSForZosAction e ServiceNow, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os action providers documentados no HCL Workload Automation 10.2.8 são GenericAction, MailSender, MessageLogger, TWSAction, TWSForZosAction e ServiceNow, conforme documentação oficial?*

---

### 120. hwa-10.2.8-event-generic-event-plug-in-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, eventos customizados são definidos com o event provider GenericEventPlugIn e podem ser enviados ao event processing server com o comando sendevent para acionar regras a partir de qualquer agent ou workstation que execute o client de linha de comando remota, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, eventos customizados são definidos com o event provider GenericEventPlugIn e podem ser enviados ao event processing server com o comando sendevent para acionar regras a partir de qualquer agent ou workstation que execute o client de linha de comando remota, conforme documentação oficial?*

---

### 121. hwa-10.2.8-event-internal-events-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Os eventos detectáveis no HCL Workload Automation 10.2.8 são divididos em eventos internos (envolvendo status de objetos como jobs, job streams e workstations) e eventos externos (mensagens em arquivos de log, eventos de aplicações de terceiros e criação, atualização ou exclusão de arquivos), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os eventos detectáveis no HCL Workload Automation 10.2.8 são divididos em eventos internos (envolvendo status de objetos como jobs, job streams e workstations) e eventos externos (mensagens em arquivos de log, eventos de aplicações de terceiros e criação, atualização ou exclusão de arquivos), conforme documentação oficial?*

---

### 122. hwa-10.2.8-event-monitor-event-rules-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser monitoradas pela tarefa Monitor Event Rules, criada em Monitoring and Reporting > All Configured Tasks > New, sob Event Monitoring Task, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser monitoradas pela tarefa Monitor Event Rules, criada em Monitoring and Reporting > All Configured Tasks > New, sob Event Monitoring Task, conforme documentação oficial?*

---

### 123. hwa-10.2.8-event-object-related-events-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, os eventos são divididos nas categorias relacionados a objetos do HCL Workload Automation, monitoramento de arquivos, monitoramento de aplicações, eventos SAP, monitoramento de data sets e eventos genéricos, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, os eventos são divididos nas categorias relacionados a objetos do HCL Workload Automation, monitoramento de arquivos, monitoramento de aplicações, eventos SAP, monitoramento de data sets e eventos genéricos, conforme documentação oficial?*

---

### 124. hwa-10.2.8-event-rule-builder-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o rule builder varre periodicamente (por padrão a cada cinco minutos ou conforme o valor da opção global deploymentFrequency) o banco de dados em busca de regras não-draft e constrói arquivos de configuração de regras para implantação, e as novas configurações de monitoramento são baixadas para os agents, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o rule builder varre periodicamente (por padrão a cada cinco minutos ou conforme o valor da opção global deploymentFrequency) o banco de dados em busca de regras não-draft e constrói arquivos de configuração de regras para implantação, e as novas configurações de monitoramento são baixadas para os agents, conforme documentação oficial?*

---

### 125. hwa-10.2.8-event-twsobjects-monitor-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
Os event providers documentados no HCL Workload Automation 10.2.8 são TWSObjectsMonitor, FileMonitor, TWSApplicationMonitor e DatasetMonitor, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os event providers documentados no HCL Workload Automation 10.2.8 são TWSObjectsMonitor, FileMonitor, TWSApplicationMonitor e DatasetMonitor, conforme documentação oficial?*

---

### 126. hwa-10.2.8-evtsize-evtsize-message-size-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > evtsize [evtsize]]`

**Regra Canônica / Evidência:**
Não execute sem aprovação. No HCL Workload Automation Distributed 10.2.8, evtsize define o tamanho de arquivos de mensagens como Mailbox.msg e é usado para aumentar o arquivo após 'End of file on events file.'; requer usuário maestro/root ou Administrator e o engine deve estar parado. Confirme a janela e o procedimento aprovado.

**Plataforma / Validação:** Distributed

---

### 127. hwa-10.2.8-globalopts-baserecprompt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global baseRecPrompt (alias bp) tem valor '1000' neste ambiente. baseRecPrompt | bp Maximum prompts after abend. Specify the maximum number of prompts that can be displayed to the operator after a job abends. The default value is 1000 . Run JnextPlan to make this change effective. bindUser | bu User for 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual o propósito e valor padrão da opção global baseRecPrompt no optman do HWA?*

---

### 128. hwa-10.2.8-globalopts-binduser-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security [security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global bindUser (alias bu) tem valor 'wauser' neste ambiente. bindUser | bu User for binding to remote jobs from shadow job. Specify the user ID that is used to bind a shadow job to a remote job during the security check for "cross dependencies". This user must be given at least the following authoriz

**Plataforma / Validação:** Distributed

---

### 129. hwa-10.2.8-globalopts-enlistsecchk-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security [security]]`

**Regra Canônica / Evidência:**
A opção global enListSecChk (sc) do HCL Workload Automation 10.2.8 habilita a verificação de segurança de listas (list security check), controlando se as listas de acesso são verificadas durante as operações de agendamento.

**Plataforma / Validação:** Distributed

---

### 130. hwa-10.2.8-globalopts-enlogonbatch-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enLogonBatch (alias lb) tem valor 'NO' neste ambiente. enLogonBatch | lb Automatically grant logon as batch. This is for Windows ® jobs only. If set to yes , the logon users for Windows ® jobs are automatically granted the right to Logon as batch job . If set to no , or omitted, the right must 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enLogonBatch (alias lb) tem valor 'NO' neste ambiente?*

---

### 131. hwa-10.2.8-globalopts-enpreventstart-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enPreventStart (alias ps) impede o início de um job ou job stream sob certas condições definidas por política, atuando como guarda; neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enPreventStart (alias ps) impede o início de um job ou job stream sob certas condições definidas por política, atuando como guarda; neste ambiente está YES?*

---

### 132. hwa-10.2.8-globalopts-ensecfileextendedfields-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security [security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enSecFileExtendedFields (alias sl) tem valor 'NO' neste ambiente. Habilita campos estendidos no security file (valores longos de atributos para objetos de scheduling). Neste ambiente é NO (desligado).

**Plataforma / Validação:** Distributed

---

### 133. hwa-10.2.8-globalopts-ensslfullconnection-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > ssl [ssl]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enSSLFullConnection (alias sf) tem valor 'NO' neste ambiente. enSSLFullConnection | sf Enable the SSL full connection. Specify that HCL Workload Automation uses a higher level of SSL connection than the standard level. For full details see Configuring full SSL security . Valid values are yes to enable

**Plataforma / Validação:** Distributed

---

### 134. hwa-10.2.8-globalopts-enstrencrypt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > ssl [ssl]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enStrEncrypt (alias se) tem valor 'NO' neste ambiente. enStrEncrypt | se Enable strong password encryption. Enable or disable strong encryption. Enable strong encryption by setting this option to yes . See Configuring the SSL connection protocol for the network . The default value is no . Run J

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enStrEncrypt (alias se) tem valor 'NO' neste ambiente?*
- *Qual o propósito e valor padrão da opção global enStrEncrypt no optman do HWA?*
- *Como configurar a opção global enStrEncrypt no Master Domain Manager?*

---

### 135. hwa-10.2.8-globalopts-filestartconditionjobname-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global fileStartConditionJobName (alias fc) tem valor 'FILE_STARTCOND' neste ambiente. fileStartConditionJobName | fc Name of the job in charge of running the file monitoring task . Applicable only if you select file as the start condition type. Specify the name of the job which is automatically added to the plan to run the f

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global fileStartConditionJobName (alias fc) tem valor 'FILE_STARTCOND' neste ambiente?*
- *Como configurar a opção global fileStartConditionJobName no Master Domain Manager?*

---

### 136. hwa-10.2.8-globalopts-licenseproxypassword-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global licenseProxyPassword (alias pw) tem valor '****' neste ambiente. licenseProxyPassword | pw License Proxy Password The password of the proxy server which HCL Workload Automation is expected to contact. This option is required if you are using a proxy server protected by a user name and password. The defau

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global licenseProxyPassword (alias pw) tem valor '****' neste ambiente?*

---

### 137. hwa-10.2.8-globalopts-licenserefreshtoken-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global licenseRefreshToken tem valor 'License Refresh Token is absent' neste ambiente. Token de refresh para renovação automática da licença junto ao license server; presente quando licenseType usa OAuth/refresh. Neste ambiente está vazio.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global licenseRefreshToken tem valor 'License Refresh Token is absent' neste ambiente?*
- *Qual o propósito e valor padrão da opção global licenseRefreshToken no optman do HWA?*

---

### 138. hwa-10.2.8-globalopts-logmanminmaxpolicy-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global logmanMinMaxPolicy (alias lm) tem valor 'BOTH' neste ambiente. logmanMinMaxPolicy | lm Logman minimum and maximum run times policy. Specify how the minimum and maximum job run times are logged and reported by logman . Possible values are: elapsedtime The minimum and maximum elapsed runtimes are logged 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global logmanMinMaxPolicy (alias lm) tem valor 'BOTH' neste ambiente?*

---

### 139. hwa-10.2.8-globalopts-logmansmoothpolicy-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global logmanSmoothPolicy (alias lt) tem valor '-1' neste ambiente. logmanSmoothPolicy | lt Logman normal run time calculation policy. Set the weighting factor that favors the most recent job run when calculating the normal (average) run time for a job. This is expressed as a percentage. For example, specif

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global logmanSmoothPolicy (alias lt) tem valor '-1' neste ambiente?*

---

### 140. hwa-10.2.8-globalopts-resubmitjobname-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global resubmitJobName (alias rj) tem valor 'MASTERAGENTS#RESTART_STARTCOND' neste ambiente. resubmitJobName | rj Name of the job in charge of resubmitting the job stream. Specify the name of the Job Stream Submission job which is automatically added to the plan to resubmit a new instance of the job stream where the start condition

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global resubmitJobName (alias rj) tem valor 'MASTERAGENTS#RESTART_STARTCOND' neste ambiente?*
- *Como configurar a opção global resubmitJobName no Master Domain Manager?*

---

### 141. hwa-10.2.8-globalopts-sccdurl-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global sccdUrl tem valor 'http://localhost:8080/maximo/oslc/os/oslcincident' neste ambiente. URL do SCCM (System Center Configuration Manager) para integração de deploy de agentes/estações; usado pelo TWS para registro de workstations. Neste ambiente está vazio (sem SCCM).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global sccdUrl tem valor 'http://localhost:8080/maximo/oslc/os/oslcincident' neste ambiente?*

---

### 142. hwa-10.2.8-globalopts-sccduserpassword-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global sccdUserPassword tem valor '****' neste ambiente. Senha para autenticação na integração SCCM (armazenada criptografada). Neste ambiente está vazio.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global sccdUserPassword tem valor '****' neste ambiente?*

---

### 143. hwa-10.2.8-globalopts-servicenowurl-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: dwc_api > api [api]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global servicenowUrl (alias nu) tem valor 'http://localhost:8080/api/now/table/incident' neste ambiente. servicenowUrl | nu ServiceNow URL. Used in event rule management. If you use rules that implement an action that opens an incident in ServiceNow (or any other application that can open an incident in the ServiceNow format), specify the Serv

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global servicenowUrl (alias nu) tem valor 'http://localhost:8080/api/now/table/incident' neste ambiente?*

---

### 144. hwa-10.2.8-globalopts-servicenowuserpassword-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global servicenowUserPassword (alias np) tem valor '****' neste ambiente. Senha do usuário ServiceNow usada por regras de evento que abrem incidentes no ServiceNow (armazenada criptografada). Neste ambiente está vazio.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global servicenowUserPassword (alias np) tem valor '****' neste ambiente?*

---

### 145. hwa-10.2.8-globalopts-smtpuseauthentication-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseAuthentication (alias ua) tem valor 'NO' neste ambiente. smtpUseAuthentication | ua Mail plug-in uses SMTP authentication. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify if the SMTP connection needs to be authenticated. Valu

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseAuthentication (alias ua) tem valor 'NO' neste ambiente?*

---

### 146. hwa-10.2.8-globalopts-smtpuserpassword-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpUserPassword (alias up) tem valor '****' neste ambiente. smtpUserPassword | up SMTP server user password. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify the SMTP server user password. The password is stored in an encrypted f

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpUserPassword (alias up) tem valor '****' neste ambiente?*

---

### 147. hwa-10.2.8-globalopts-smtpusessl-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > ssl [ssl]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseSSL (alias us) tem valor 'NO' neste ambiente. smtpUseSSL | us Mail plug-in uses SSL. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify if the SMTP connection is to be authenticated via SSL. Values are yes or no . The

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseSSL (alias us) tem valor 'NO' neste ambiente?*

---

### 148. hwa-10.2.8-globalopts-smtpusetls-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > tls [tls]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseTLS (alias tl) tem valor 'NO' neste ambiente. smtpUseTLS | tl Mail plug-in uses TLS protocol. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify if the SMTP connection is to be authenticated via the Transport Layer Se

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpUseTLS (alias tl) tem valor 'NO' neste ambiente?*

---

### 149. hwa-10.2.8-globalopts-zosuserpassword-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI optman (Opções Globais do Master) > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global zOSUserPassword (alias zw) tem valor '****' neste ambiente. zOSUserPassword | zw HCL Workload Automation for Z connector user password . Used in event rule management. If you deploy rules implementing an action that submits job streams to the HCL Workload Automation for Z controller, specify the HCL

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global zOSUserPassword (alias zw) tem valor '****' neste ambiente?*

---

### 150. hwa-10.2.8-govern-composer-lock-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a seção lock do composer bloqueia o acesso às definições de objetos de agendamento no banco de dados para evitar que definições sejam sobrescritas por usuários acessando o mesmo objeto concorrentemente; enquanto um usuário mantém o objeto bloqueado, os demais usuários têm somente acesso de leitura até o objeto ser liberado ou explicitamente desbloqueado pelo administrador.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 151. hwa-10.2.8-govern-composer-replace-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O comando composer replace do HCL Workload Automation 10.2.8 substitui a definição existente de um objeto de agendamento no banco de dados no local, sobrescrevendo-a em vez de criar uma nova versão; não existe comando 'replace de mesmo nome cria nova versão' documentado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 152. hwa-10.2.8-govern-composer-unlock-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando composer unlock libera os bloqueios de acesso de objetos de agendamento no banco de dados; a opção ;forced permite que o usuário que bloqueou o objeto o desbloqueie independentemente da sessão, e o superuser pode desbloquear objetos independentemente de usuário e sessão.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 153. hwa-10.2.8-govern-composer-version-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 o comando composer version apenas exibe o banner da versão do programa composer (versão do software); ele não gerencia nem lista versões de definições de objetos no banco de dados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 154. hwa-10.2.8-govern-composer-write-to-db-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a forma documentada de gravar definições de objetos de agendamento no banco de dados via composer é pelos comandos add e replace (o replace substitui definições existentes); não há um comando composer 'deploy' ou 'upload' para definições de jobs/job streams.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 155. hwa-10.2.8-govern-pt-br-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não contém uma página ou tarefa denominada 'Manage change' nem 'Manage change > Monitor' com ação 'Deploy pending changes' no Dynamic Workload Console; as funções de mudança são documentadas como 'Keeping track of changes' (auditoria de justificativa/relatórios, verificação de versões e versionamento), sem tal tarefa ou ação.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não contém uma página ou tarefa denominada 'Manage change' nem 'Manage change > Monitor' com ação 'Deploy pending changes' no Dynamic Workload Console; as funções de mudança são documentadas como 'Keeping track of changes' (auditoria de justificativa/relatórios, verificação de versões e versionamento), sem tal tarefa ou ação?*

---

### 156. hwa-10.2.8-govern-streamlogon-user-name-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o nome de usuário de streamlogon de um job pode conter até 47 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de usuário de streamlogon de um job pode conter até 47 caracteres?*

---

### 157. hwa-10.2.8-ha-switchmgr-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
In HWA Distributed 10.2.8, switchmgr supports MDM-to-BMDM, domain-manager-to-backup-domain-manager, and DDM-to-BDDM switching.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar mdm?*

---

### 158. hwa-10.2.8-incident-aix-timezone-smit-0123

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > timezone [timezone]]`

**Regra Canônica / Evidência:**
Sintoma: inconsistencia de horario em jobs no AIX master domain manager (ex.: schedtime ou start time incorretos). Causa: setting incorreto do time zone no AIX. Resolucao: no AIX master domain manager: (1) iniciar smit; (2) selecionar System Environments > Change/Show Date, Time, and Time Zone > Change Time Zone Using User Entered Values; (3) setar o time zone relevante. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: inconsistencia de horario em jobs no AIX master domain manager (ex?*
- *O que causa e como solucionar o problema: inconsistencia de horario em jobs no AIX master domain manager (ex?*

---

### 159. hwa-10.2.8-incident-alias-archive-search-0120

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > alias [alias]]`

**Regra Canônica / Evidência:**
Sintoma: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece. Causa: jobs e job streams em status final sao armazenados no archive com seus nomes originais, nao seus aliases — qualquer busca/report de jobs completos deve ignorar os aliases. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece?*
- *O que causa e como solucionar o problema: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece?*

---

### 160. hwa-10.2.8-incident-auth-config-xml-0147

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando. Causa: divergencia entre os arquivos authentication_config.xml no DWC e no master domain manager. Resolucao: localizar e comparar os arquivos authentication_config.xml em ambos: no master domain manager (UNIX: TWA_DATA_DIR/usr/servers/engineServer/configDropins/overrides; Windows: TWA_home\usr\servers\engineServer\configDropins\overrides) e no DWC (UNIX: DWC_DATA_dir/usr/servers/dwcServer/configDropins/overrides; Windows: DWC_home\usr\servers\dwcServer\configDropins\overrides) e alinha-los. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando?*
- *O que causa e como solucionar o problema: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando?*

---

### 161. hwa-10.2.8-incident-awsjcl-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Na documentação distribuída oficial do HCL Workload Automation 10.2.8, a página 'HCL Workload Automation messages' do guia Messages and Codes (common/src_ms/awsmspart1TWS.html) documenta apenas quatro conjuntos de mensagens: AWKZSJ (z/OS shadow job validation), AWSWUI (Dynamic Workload Console), AWSZAP (action plug-in para z/OS) e EEL (agente HCL Workload Automation para z/OS). Os conjuntos de mensagens do motor, como AWSJCL (linha de comando), AWSBDW (jobman), AWSBHT (batchman) e AWSJIM (instalação do servidor), não estão documentados nessa página da versão 10.2.8 distribuída; eles estão disponíveis apenas em versões anteriores, como o guia 9.5 (AWSJCL, AWSBDW, AWSBHT, AWSJPL) e o manual IBM 9.4/9.5 (AWSJIM, capítulo 177).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL0006 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL0006 no HWA?*

---

### 162. hwa-10.2.8-incident-bcz021e-0042

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBCZ021E 'A definition keyword was expected at this point' ao validar/importar um arquivo de definicao com composer. Causa: o arquivo contem um token que nao e uma keyword de definicao valida naquela posicao (ex.: um nome de objeto solto sem a keyword SCHEDULE/KEYWORD que o precede, ou uma keyword colocada fora do contexto correto). Resolucao: verificar a linha apontada pelo erro e garantir que cada definicao comece com a keyword correta (ex.: SCHEDULE para job stream, KEYWORD para keyword definition) e que keywords de dependencia (FOLLOWS, OPENS, PROMPT) estejam dentro do contexto valido de um job. Validado no lab 10.2.8.00: arquivo com token solto 'R11BAD' + END -> AWSBCZ021E + AWSBIA296I Total objects successfully validated: 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA296I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA296I no HWA?*
- *Qual é o significado da mensagem de erro AWSBCZ021E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCZ021E no HWA?*
- *O que causa e como solucionar o problema: AWSBCZ021E 'A definition keyword was expected at this point' ao validar/importar um arquivo de definicao com composer?*

---

### 163. hwa-10.2.8-incident-beh023e-0069

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > appserver [appserver]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBEH023E 'Unable to establish communication with the server' durante MakePlan. Causa: o application server esta parado e o MakePlan nao consegue continuar. Resolucao: iniciar o WebSphere Application Server Liberty Base e verificar os logs do Liberty para identificar por que parou. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSBEH023E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBEH023E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBEH023E no HWA?*
- *O que causa e como solucionar o problema: AWSBEH023E 'Unable to establish communication with the server' durante MakePlan?*

---

### 164. hwa-10.2.8-incident-bhu025e-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU025E ao usar into=JOBS#<jobstream_id>. Causa: o job stream ID nao e aceito na sintaxe into= com separador #; a forma correta para qualificar por ID usa separador ';' (jobstream_id;schedid) ou horario entre parenteses. Resolucao: usar into=STREAM(hhmm) ou into=jobstream_id;schedid.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU025E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU025E no HWA?*
- *O que causa e como solucionar o problema: AWSBHU025E ao usar into=JOBS#<jobstream_id>?*

---

### 165. hwa-10.2.8-incident-bhu152e-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU152E 'There is more than one job stream instance with the given name' ao submeter job ad hoc com into=. Causa: a job stream alvo tem multiplas instancias no plano (ex.: dias diferentes ou instancias ABEND antigas). Resolucao: qualificar a instancia com into=STREAM(hhmm) ou into=STREAM(hhmm mm/dd).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU152E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU152E no HWA?*
- *O que causa e como solucionar o problema: AWSBHU152E 'There is more than one job stream instance with the given name' ao submeter job ad hoc com into=?*

---

### 166. hwa-10.2.8-incident-big-joblog-mdm-stop-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > application_server [application_server]]`

**Regra Canônica / Evidência:**
Sintoma: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente. Causa: problema conhecido que afeta OpenJDK v8, relacionado a uma questao temporaria do filesystem /tmp. Resolucao: o WebSphere Application Server Liberty Base reinicia automaticamente apos um curto periodo; se a questao temporaria do /tmp for resolvida, a operacao pode ser realizada novamente. Fonte: HCL Troubleshooting Guide 10.2.8 (Master Domain Manager may stop when trying to retrieve a big job log).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente?*
- *O que causa e como solucionar o problema: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente?*

---

### 167. hwa-10.2.8-incident-browser-close-thread-0130

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar. Causa: comportamento normal de aplicacoes WEB — quando o browser do cliente e fechado, nenhuma notificacao e entregue ao servidor segundo o protocolo HTTP; por isso a ultima thread disparada continua processando mesmo apos o fechamento. Resolucao: nao precisa de acao — apenas aguardar. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar?*
- *O que causa e como solucionar o problema: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar?*

---

### 168. hwa-10.2.8-incident-carrystates-0098

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: incidents > planner [planner]]`

**Regra Canônica / Evidência:**
Sintoma: ha um mismatch entre as instancias de Job Scheduler no Symphony file e o preproduction plan — instancias que deveriam ter sido removidas aparecem. Causa: job streams sao automaticamente deletados do preproduction plan quando completos; porem, se a opcao global carryStates (via optman) esta setada, job streams com jobs em status SUCC sao carregados para o novo Symphony quando o plano e estendido, mas deletados do preproduction plan — criando o mismatch. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar planner?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: ha um mismatch entre as instancias de Job Scheduler no Symphony file e o preproduction plan — instancias que deveriam ter sido removidas aparecem?*

---

### 169. hwa-10.2.8-incident-cluster-exe-0124

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: problema com Failover Clustering em Windows Server 2012. Causa: deprecacao da ferramenta cluster.exe command-line para Failover Clustering em Windows Server 2012. Resolucao: reinstalar a feature deprecated Failover Clustering cluster.exe. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: problema com Failover Clustering em Windows Server 2012. Causa: deprecacao da ferramenta cluster?*
- *O que causa e como solucionar o problema: problema com Failover Clustering em Windows Server 2012?*

---

### 170. hwa-10.2.8-incident-composer-dependency-order-0083

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > composer [composer]]`

**Regra Canônica / Evidência:**
Sintoma: ao usar composer para adicionar/modificar um conjunto de definicoes de objetos onde um objeto depende de outro no mesmo lote, o composer da erro de dependencia. Causa: o composer valida os objetos na ordem em que sao apresentados no comando/arquivo de definicao — se o primeiro objeto tem uma dependencia follows no segundo, a validacao falha porque o segundo ainda nao foi adicionado. Resolucao: ordenar as definicoes para que objetos dependidos venham primeiro, ou adicionar em lotes separados. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa e como solucionar o problema: ao usar composer para adicionar/modificar um conjunto de definicoes de objetos onde um objeto depende de outro no mesmo lote, o composer da erro de dependencia?*

---

### 171. hwa-10.2.8-incident-cpu-atsign-0084

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > composer [composer]]`

**Regra Canônica / Evidência:**
Sintoma: o comando display cpu=@ nao funciona em UNIX — nada acontece ao digitar display cpu=@ no prompt do composer. Causa: a tecla @ (atsign) esta configurada como caractere kill do terminal. Resolucao: usar stty -a para verificar o setting da tecla @; se estiver como kill, usar stty kill ^U para mudar para control/U (ou outro). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa e como solucionar o problema: o comando display cpu=@ nao funciona em UNIX — nada acontece ao digitar display cpu=@ no prompt do composer?*

---

### 172. hwa-10.2.8-incident-critical-late-0140

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > critical-network [critical-network]]`

**Regra Canônica / Evidência:**
Sintoma: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores. Resolucao: usando a tarefa successful predecessors, comparar o planned start, actual start e critical start de todos os predecessores do job atrasado; verificar se algum tem valores de tempo muito proximos ou planned start posterior ao critical start. Se for o caso: considerar mudar... Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores?*
- *O que causa e como solucionar o problema: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores?*

---

### 173. hwa-10.2.8-incident-db2-deadlock-timeout-0104

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: 'The current transaction has been rolled back because of a deadlock or timeout. Reason code 68' ao acessar um objeto. Causa: o objeto esta locked por outro usuario, ou por voce em outra sessao, mas o lock nao foi detectado pela aplicacao — a aplicacao espera ate ser interrompida pelo timeout do DB2. Resolucao: aumentar o timeout do DB2 (ou do Liberty) ou resolver o lock concorrente. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: 'The current transaction has been rolled back because of a deadlock or timeout?*
- *O que causa e como solucionar o problema: 'The current transaction has been rolled back because of a deadlock or timeout?*

---

### 174. hwa-10.2.8-incident-dwc-role-task-0129

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'. Causa: o usuario nao tem o role necessario para rodar a tarefa — para rodar uma tarefa e preciso um role que permita acessar os paineis do DWC relevantes ao tipo de tarefa. Resolucao: configurar os roles adequados para o usuario (ver Administration Guide, secao de roles do DWC). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'?*
- *O que causa e como solucionar o problema: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'?*

---

### 175. hwa-10.2.8-incident-dynagent-job-error-0082

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > dynamic-agent [dynamic-agent]]`

**Regra Canônica / Evidência:**
Sintoma: do Dynamic Workload Console, um dynamic agent aparece mas o status do job submetido fica continuamente em 'error'. Causa: o hostname local do master domain manager nao e conhecido na rede do agent (outro dominio DNS). Resolucao: editar o arquivo JobDispatcherConfig.properties e ajustar o parametro JDURL=https://<localhostname>. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?*
- *Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?*
- *O que causa e como solucionar o problema: do Dynamic Workload Console, um dynamic agent aparece mas o status do job submetido fica continuamente em 'error'?*

---

### 176. hwa-10.2.8-incident-dynagent-no-resources-0081

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > dynamic-agent [dynamic-agent]]`

**Regra Canônica / Evidência:**
Sintoma: do Dynamic Workload Console, um dynamic agent aparece, mas o job submetido aparece como 'No resources available'. Causa: o hostname local de um dynamic workload broker server registrado no agent nao e conhecido na rede do master domain manager (outro dominio DNS). Resolucao: editar o arquivo JobManager.ini e ajustar o parametro FullyQualifiedHostname = <servername>. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?*
- *Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?*
- *Como solucionar problemas de registro de agentes dinâmicos no broker?*
- *O que causa e como solucionar o problema: do Dynamic Workload Console, um dynamic agent aparece, mas o job submetido aparece como 'No resources available'?*

---

### 177. hwa-10.2.8-incident-dynagent-not-found-0080

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > dynamic-agent [dynamic-agent]]`

**Regra Canônica / Evidência:**
Sintoma: um dynamic agent instalado corretamente nao aparece no Dynamic Workload Console. Causa: o hostname do dynamic workload broker (tdwbhostname) ou a porta do broker, ou ambos, registrados no agent, nao sao conhecidos na rede do master domain manager porque o host do broker esta em outro dominio DNS. Resolucao: editar o arquivo JobManager.ini e corrigir os parametros de hostname/porta do broker. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?*
- *Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?*
- *Como solucionar problemas de registro de agentes dinâmicos no broker?*
- *O que causa e como solucionar o problema: um dynamic agent instalado corretamente nao aparece no Dynamic Workload Console?*

---

### 178. hwa-10.2.8-incident-event-lost-queue-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > events [events]]`

**Regra Canônica / Evidência:**
Sintoma: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue. Causa: a event queue e circular — eventos sao adicionados no fim e removidos do inicio; quando nao ha espaco para escrever no fim, o evento e escrito no inicio, sobrescrevendo o evento mais antigo. Resolucao: o evento sobrescrito nao pode ser recuperado; aumentar o tamanho da queue para evitar recorrencia (ver 'Managing the event queue' no Administration Guide). Fonte: HCL Troubleshooting Guide 10.2.8 (An event is lost).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue?*
- *O que causa e como solucionar o problema: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue?*

---

### 179. hwa-10.2.8-incident-external-lock-timeout-0109

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto. Causa: o objeto esta locked de fora do HCL Workload Automation — por exemplo, pelo database administrator ou por uma funcao automatica do banco — e a aplicacao espera ate ser interrompida pelo timeout do application server. Resolucao: identificar e liberar o lock externo, ou ajustar os timeouts. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto?*
- *O que causa e como solucionar o problema: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto?*

---

### 180. hwa-10.2.8-incident-graphical-designer-java-0132

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: ao trabalhar com um job no Graphical Designer, recebe um erro (ex.: AWSITA122E ou AWKRAA209E - The job with advanced options with ID application_type was not found). Causa: um erro inesperado ocorreu ao executar um metodo Java; ou o job com advanced options nao pode ser encontrado. Resolucao: (1) checar o JobManager_message.log; (2) checar o log mais recente em /opt/ibm/TWA/TWS/JavaExt/eclipse/configuration/*.log; (3) se o job plug-in nao for encontrado: garantir que o job plug-in esta em /opt/IBM/TWA/TWS/JavaExt/eclipse/plugins e listado no config.ini. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA122E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA122E no HWA?*
- *Qual é o significado da mensagem de erro AWKRAA209E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKRAA209E no HWA?*
- *O que causa e como solucionar o problema: ao trabalhar com um job no Graphical Designer, recebe um erro (ex?*

---

### 181. hwa-10.2.8-incident-hadr-db2-console-0131

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado. Causa: quando o no primario do DB2 para, cada request do DWC espera por um switch manual para o no standby. Resolucao: verificar que o no primario esta ativo e rodando. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado?*
- *O que causa e como solucionar o problema: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado?*

---

### 182. hwa-10.2.8-incident-hold-at-past-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > hold [hold]]`

**Regra Canônica / Evidência:**
Sintoma: job submetido com at=HHMM fica HOLD e so executa no dia seguinte. Causa: o horario especificado ja passou no plano corrente; o job e agendado para a proxima ocorrencia valida (possivelmente no dia seguinte). Resolucao: verificar o horizonte do plano e usar at= com data explicita ou into=STREAM(hhmm) para controlar a instancia.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: job submetido com at=HHMM fica HOLD e so executa no dia seguinte?*
- *O que causa e como solucionar o problema: job submetido com at=HHMM fica HOLD e so executa no dia seguinte?*

---

### 183. hwa-10.2.8-incident-hold-deps-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > hold [hold]]`

**Regra Canônica / Evidência:**
Sintoma: job permanece em HOLD sem executar. Causa: dependencias nao satisfeitas (follows, needs, opens, prompt) ou horario agendado ainda nao alcancado (at= no futuro). Resolucao: verificar as dependencias com sj / showjobs (coluna de dependencias), liberar com rj (release job) quando apropriado, ou aguardar o horario.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: job permanece em HOLD sem executar?*

---

### 184. hwa-10.2.8-incident-impersonate-right-0096

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows. Causa: a conta de usuario usada para rodar a linha de comando do HWA nao tem o direito de usuario 'Impersonate a client after authentication' (setting de seguranca de um subconjunto de versoes Windows); o upgrade nao concede esse direito a usuarios existentes. Resolucao: conceder o direito de usuario 'Impersonate a client after authentication' a conta. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows?*
- *O que causa e como solucionar o problema: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows?*

---

### 185. hwa-10.2.8-incident-import-dwc-privileges-0133

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr.log. Causa: o usuario do banco com autoridade administrativa especificado para importar os settings nao tem os privilegios necessarios para drop das tabelas existentes do DWC criadas com DWC V8.6.0.0. Resolucao: fornecer ao usuario especificado o privilegio CONTROL sobre as tabelas (ou o privilegio equivalente) antes do import. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr?*
- *O que causa e como solucionar o problema: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr?*

---

### 186. hwa-10.2.8-incident-informix-composer-deadlock-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > composer [composer]]`

**Regra Canônica / Evidência:**
Sintoma: deadlock de banco ao usar comandos composer com banco Informix — duas transacoes concorrentes nao progridem porque cada uma espera o lock que a outra detem. Resolucao: (1) parar o WebSphere Application Server Liberty Base; (2) editar o arquivo TWSConfig.properties (Windows: <TWA_home>\usr\servers\engineServer\resources\properties; UNIX: <TWA_DATA_DIR>/usr/servers/engineServer/resources/properties) e adicionar a propriedade com.ibm.tws.dao.rdbms.ids.lockTimeout=0; (3) iniciar o WebSphere Application Server Liberty Base. Fonte: HCL Troubleshooting Guide 10.2.8 (Solving deadlocks when using composer with an Informix database).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *O que causa e como solucionar o problema: deadlock de banco ao usar comandos composer com banco Informix — duas transacoes concorrentes nao progridem porque cada uma espera o lock que a outra detem?*

---

### 187. hwa-10.2.8-incident-ita105e-0070

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > agent [agent]]`

**Regra Canônica / Evidência:**
Sintoma: AWSITA105E 'Unable to notify scan results to the server because of a resources scanner error' ao realizar resources scan. Causa: o produto nao consegue executar o resources scan corretamente porque o hostname da maquina nao e reconhecido. Resolucao: em UNIX, verificar que o hostname esta listado no /etc/hosts e que ping hostname funciona; em Windows, verificar que ping hostname funciona. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSITA105E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA105E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA105E no HWA?*
- *O que causa e como solucionar o problema: AWSITA105E 'Unable to notify scan results to the server because of a resources scanner error' ao realizar resources scan?*

---

### 188. hwa-10.2.8-incident-ita238e-0045

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: AWSITA238E 'The user is not authorized to access the server' ao executar composer -jwt <token>, frequentemente envolvida por AWSITA400E 'The submitted command cannot be performed' e precedida de AWSBIA389E (workstation default invalida). Causa: o token JWT nao autoriza a operacao no servidor — token com escopo errado (ex.: JWT Personal criado para o ocli usado no composer), token expirado, ou token invalido/forjado. Resolucao: (1) verificar que o token e do tipo/escopo correto para a ferramenta (ocli vs composer vs REST); (2) gerar um novo API key no Dynamic Workload Console (Manage API Keys -> Personal/Service) com as permissoes necessarias; (3) validar a expiracao do JWT (claim exp no payload); (4) usar a autenticacao de SO (wauser) se aplicavel. Validado no lab 10.2.8.00: JWT do ocli no composer -> AWSITA400E->AWSITA238E; token invalido -> mesmo erro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA389E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA389E no HWA?*
- *Qual é o significado da mensagem de erro AWSITA238E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA238E no HWA?*
- *O que causa e como solucionar o problema: AWSITA238E 'The user is not authorized to access the server' ao executar composer -jwt <token>, frequentemente envolvida por AWSITA400E 'The submitted command cannot be performed' e precedida de AWSBIA389E (workstation default invalida)?*

---

### 189. hwa-10.2.8-incident-jar-corrupt-deploy-0099

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > deploy [deploy]]`

**Regra Canônica / Evidência:**
Sintoma: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy. Causa: o arquivo .jar identificado na mensagem esta corrompido. Resolucao: verificar e corrigir o formato do arquivo antes de tentar o deploy novamente. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy?*
- *O que causa e como solucionar o problema: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy?*

---

### 190. hwa-10.2.8-incident-jcl015w-0037

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCL015W 'The object ... already exists' ao tentar composer add/replace de um objeto que ja existe, com 0 objetos atualizados (AWSBIA090I errors 1, warnings 0 / AWSBIA288I Total objects updated: 0). Causa: tentativa de criar/sobrescrever um objeto existente sem a semantica correta (add de objeto duplicado, ou replace bloqueado por lock de outra sessao). Resolucao: para atualizar um objeto existente usar o modo replace/update adequado do composer; se houver lock de outra sessao (cross-session), aguardar unlock. O lab confirmou: replace cross-session bloqueado por lock -> AWSJCL015W 'The object js=MDMDA#EVTJS_LK1 already exists' + AWSBIA090I errors 1, warnings 0 + AWSBIA288I Total objects updated: 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA288I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA288I no HWA?*
- *Qual é o significado da mensagem de erro AWSBIA090I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA090I no HWA?*
- *O que causa e como solucionar o problema: AWSJCL015W 'The object?*

---

### 191. hwa-10.2.8-incident-jcl521e-0043

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCL521E 'The password specified for the Windows user does not comply with password security policy requirements' ao definir um usuario Windows com composer add/new. Causa: a senha fornecida nao atende a politica de seguranca de senhas do dominio/sistema, ou foi usada a palavra reservada '**********' (dez asteriscos) como senha. Resolucao: fornecer uma senha valida que cumpra a politica de seguranca e evitar usar a sequencia de dez asteriscos como senha. Pesquisa Perplexity (2026-08-23) confirma que a mensagem esta relacionada a politica de senha e que a correcao e informar uma senha em conformidade.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL521E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL521E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar security?*
- *O que causa e como solucionar o problema: AWSJCL521E 'The password specified for the Windows user does not comply with password security policy requirements' ao definir um usuario Windows com composer add/new?*

---

### 192. hwa-10.2.8-incident-jco032e-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > workstation [workstation]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCO032E ao usar ocli/composer com workstation inexistente (ex.: TEST_AGENT). Causa: a workstation referenciada nao esta definida no banco. Resolucao: listar as workstations reais (sc @;info ou ocli) e usar um nome valido (ex.: MDM, MDMDA).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO032E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO032E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar workstation?*
- *O que causa e como solucionar o problema: AWSJCO032E ao usar ocli/composer com workstation inexistente (ex?*

---

### 193. hwa-10.2.8-incident-jco084e-0058

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > updatestats [updatestats]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' ao executar UpdateStats em um plano grande. Causa: quando o UpdateStats roda por mais de duas horas (job run time excede 2h), o job falha com AWSJCO084E — o tempo excessivo faz a autenticacao expirar/ficar invalida. Resolucao: reduzir o tempo de execucao do UpdateStats (ex.: reduzir o volume de jobs no plano, otimizar a janela) ou investigar por que demora mais de 2h; a mensagem e enganosa (parece erro de autorizacao mas e timeout de execucao). Fonte: HCL Troubleshooting Guide 10.2.8 (UpdateStats fails if job run time exceeds two hours).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO084E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?*
- *O que causa e como solucionar o problema: AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' ao executar UpdateStats em um plano grande?*

---

### 194. hwa-10.2.8-incident-jco084e-timeout-config-0101

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > updatestats [updatestats]]`

**Regra Canônica / Evidência:**
Sintoma: UpdateStats em plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' porque o job run time excedeu duas horas. Causa: o default timeout das credenciais de usuario do WebSphere Application Server e 2 horas. Resolucao: aumentar o timeout para dar mais tempo ao UpdateStats: (1) navegar ate <TWA_home>/usr/servers/... (caminho do Liberty); (2) ajustar o timeout das credenciais. Fonte: HCL Troubleshooting Guide 10.2.8 (UpdateStats fails if it runs more than two hours).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO084E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?*
- *O que causa e como solucionar o problema: UpdateStats em plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' porque o job run time excedeu duas horas?*

---

### 195. hwa-10.2.8-incident-jco135w-0052

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > jobman [jobman]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCO135W (warning) do job manager relacionado a agendamento/dependencias, frequentemente ligado a problemas de storage/mailbox ou disponibilidade do job manager. Causa: warning do jobman quando um valor padrao e aplicado ao processamento de jobs criticos porque o produto perdeu a conexao com o banco, ou problemas de startup/disponibilidade do job manager. Resolucao: (1) verificar o log do job manager para o subcomponente e RC exatos; (2) checar mensagens anteriores que precedem o warning; (3) verificar conectividade de banco e espaco de storage/mailbox; (4) reiniciar o job manager se necessario. Pesquisa Perplexity (2026-08-23).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO135W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO135W no HWA?*
- *O que causa e como solucionar o problema: AWSJCO135W (warning) do job manager relacionado a agendamento/dependencias, frequentemente ligado a problemas de storage/mailbox ou disponibilidade do job manager?*

---

### 196. hwa-10.2.8-incident-jco136e-0071

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCO136E 'No more than 5 users are allowed to perform this operation at the same time' ao usar o Plan View conectado ao engine. Causa: o numero maximo de usuarios que podem usar o Plan View conectado ao mesmo engine e cinco. Resolucao: se necessario, modificar o limite editando a propriedade com.ibm.tws.conn.plan.view.maxusers no arquivo TWSConfig.properties. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSJCO136E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO136E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO136E no HWA?*
- *O que causa e como solucionar o problema: AWSJCO136E 'No more than 5 users are allowed to perform this operation at the same time' ao usar o Plan View conectado ao engine?*

---

### 197. hwa-10.2.8-incident-jcs037e-0072

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > agent [agent]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCS037E 'The value of the string <folder_name>/MASTERAGENTS in property RJ is not correct. The value must be alphanumeric' ao iniciar um agent. Causa: o arquivo pools.properties nao foi atualizado automaticamente. Resolucao: (1) parar o agent com ShutDownLwa; (2) navegar ate <TWS_home>/ITA/cpa/config (Windows) ou TWA_DATA_DIR/ITA/cpa/config (UNIX); (3) editar pools.properties e atualizar o nome da workstation MASTERAGENTS; (4) iniciar o agent com StartUpLwa. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSJCS037E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCS037E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCS037E no HWA?*
- *O que causa e como solucionar o problema: AWSJCS037E 'The value of the string <folder_name>/MASTERAGENTS in property RJ is not correct?*

---

### 198. hwa-10.2.8-incident-job-ready-not-start-0134

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > jobs [jobs]]`

**Regra Canônica / Evidência:**
Sintoma: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia. Causa (mais comuns): (1) o limite da workstation esta zerado; (2) a workstation esta parada; (3) a workstation onde o job deveria rodar nao esta linkada; (4) o numero de jobs rodando na workstation e maior que o limite configurado. Resolucao: verificar cada uma dessas causas na workstation alvo. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia?*
- *O que causa e como solucionar o problema: ao monitorar um job, ele parece pronto para rodar (todas as dependencias satisfeitas) mas nao inicia?*

---

### 199. hwa-10.2.8-incident-jom179e-0047

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > workstation [workstation]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJOM179E 'An error occurred deleting definition of the workstation. The workload broker server is currently unreachable' ao excluir uma workstation via Composer ou Dynamic Workload Console. Causa: remocao de um dynamic domain manager sem o procedimento de uninstall adequado, deixando o broker server inacessivel. Resolucao: (1) garantir que o dynamic domain manager foi totalmente removido (uninstall completo); (2) excluir as workstations restantes a partir do master domain manager; (3) verificar a conectividade do workload broker server. Pesquisa Perplexity (2026-08-23) confirma a causa e resolucao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM179E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM179E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar workstation?*
- *Qual é o significado da mensagem de erro AWSJOM179E no HWA e qual ação é recomendada?*
- *O que causa e como solucionar o problema: AWSJOM179E 'An error occurred deleting definition of the workstation?*

---

### 200. hwa-10.2.8-incident-jom915e-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJOM915E ao validar definicoes de job com keywords fora da ordem canonica (ex.: RECOVERY depois de PRIORITY, ou VARTABLE depois de ON RUNCYCLE). Causa: a ordem de keywords no job statement e obrigatoria. Resolucao: seguir a ordem follows → needs → opens → priority → prompt → nop (e VARTABLE antes de ON RUNCYCLE).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM915E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?*
- *O que causa e como solucionar o problema: AWSJOM915E ao validar definicoes de job com keywords fora da ordem canonica (ex?*

---

### 201. hwa-10.2.8-incident-keystore-reload-0108

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: Exception = java.io.IOException: Keystore was tampered with, or password was incorrect ao usar SSL/certificados. Causa: o certificado nao foi recarregado ou regenerado apos qualquer mudanca na senha do keystore no servidor ou connector. Resolucao: recarregar ou regenerar o certificado e reiniciar o application server; para regenerar, usar comando openssl genrsa. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: Exception = java?*

---

### 202. hwa-10.2.8-incident-ldap-multihomed-0136

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: conta LDAP bloqueada apos UMA tentativa de autenticacao errada. Causa: quando um unico hostname LDAP e mapeado para multiplos enderecos IP na configuracao de rede, se uma senha invalida e digitada no login, o WebSphere faz tantas tentativas de login quanto o numero de IPs associados + 1; se o numero resultante excede o maximo de falhas de login permitido pela politica de seguranca LDAP/AD local, a conta e bloqueada. Resolucao: alinhar o DNS (um IP por hostname) ou ajustar a politica de bloqueio. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: conta LDAP bloqueada apos UMA tentativa de autenticacao errada?*
- *O que causa e como solucionar o problema: conta LDAP bloqueada apos UMA tentativa de autenticacao errada?*

---

### 203. hwa-10.2.8-incident-liberty-cpu-tuning-0137

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > performance [performance]]`

**Regra Canônica / Evidência:**
Sintoma: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts). Resolucao: para reduzir o uso de CPU para ~1 segundo de CPU por hora e reduzir os EXCP counts por um fator de 10: (1) editar <USERDIR>/servers/dwcServer/server.xml adicionando <config updateTrigger=disabled/> apos a string de comentario; (2) substituir todas as strings scaninterval=5s por scaninterval=... (intervalo maior). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts)?*
- *O que causa e como solucionar o problema: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts)?*

---

### 204. hwa-10.2.8-incident-local-params-files-0122

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > parameters [parameters]]`

**Regra Canônica / Evidência:**
Sintoma: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente. Causa: um ou ambos os arquivos onde os parametros sao armazenados foram deletados ou renomeados. Resolucao: verificar que os arquivos parameters e parameters.KEY existem em TWA_home/TWS — sao necessarios para resolver local parameters e nao devem ser deletados/renomeados. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente?*
- *O que causa e como solucionar o problema: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente?*

---

### 205. hwa-10.2.8-incident-msl018e-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSMSL018E 'dependency does not exist' ao usar ocli plan release job sem o separador '=' na sintaxe. Causa: o comando ocli plan release exige job=<nome> com '='; sem o '=' o parser interpreta o argumento como outra coisa e reporta dependencia inexistente. Resolucao: usar a sintaxe completa 'ocli plan release job=WS#STREAM.JOB' (com '='). O lab confirmou: ocli plan release job=MDMDA#JOBS.R8REL2 -> Command forwarded for MDMDA#JOBS[(0300 23/08/26),...].R8REL2; job SUCC RC 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSMSL018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSMSL018E no HWA?*
- *O que causa e como solucionar o problema: AWSMSL018E 'dependency does not exist' ao usar ocli plan release job sem o separador '=' na sintaxe?*

---

### 206. hwa-10.2.8-incident-msp104e-0053

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > mail [mail]]`

**Regra Canônica / Evidência:**
Sintoma: AWSMSP104E ao enviar alertas de email/eventos — problema com mail sender name ou configuracao SMTP. Causa: o dominio do servidor SMTP nao esta definido na opcao mailSenderName, ou SMTP mal configurado. Resolucao: (1) definir um sender valido com dominio (ex.: tws@seudominio.com) na opcao mailSenderName usando o comando de gerenciamento apropriado; (2) reiniciar o servico de mail; (3) verificar conectividade SMTP. Pesquisa Perplexity (2026-08-23) confirma. Complementa hwa-10.2.8-trouble-awsmsp104e-0007.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSMSP104E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSMSP104E no HWA?*
- *O que causa e como solucionar o problema: AWSMSP104E ao enviar alertas de email/eventos — problema com mail sender name ou configuracao SMTP?*

---

### 207. hwa-10.2.8-incident-mssql-cascade-30-0107

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro. Causa: deletar com opcao cascade uma linha que contem mais de 30 referencias nao e suportado em MSSQL. Resolucao: evitar cascade com mais de 30 referencias no MSSQL; dividir a operacao. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro?*
- *O que causa e como solucionar o problema: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro?*

---

### 208. hwa-10.2.8-incident-null-password-cli-0111

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: ao lanca r programas CLI (como composer) e tentar rodar um comando, o erro 'user is not authorized to access server' e dado. Causa: o usuario que executa o comando tem senha nula (null password) — composer e muitos outros programas CLI do HWA nao podem rodar com senha nula. Resolucao: alterar a senha do usuario e tentar novamente. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar security?*
- *O que causa e como solucionar o problema: ao lanca r programas CLI (como composer) e tentar rodar um comando, o erro 'user is not authorized to access server' e dado?*

---

### 209. hwa-10.2.8-incident-oracle-permission-0105

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX. Causa: o usuario de administracao do Oracle nao tem permissao de leitura em todo o caminho do diretorio de instalacao do HWA. Resolucao: conceder permissao de leitura ao usuario do Oracle para cada diretorio do caminho (ex.: /opt, /myProducts e /TWS). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX?*
- *O que causa e como solucionar o problema: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX?*

---

### 210. hwa-10.2.8-incident-oracle-reports-privileges-0139

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > reports [reports]]`

**Regra Canônica / Evidência:**
Sintoma: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console. Causa: o usuario do banco especificado nas propriedades da engine connection nao tem os privilegios para rodar reports. Resolucao (somente Oracle): como administrador do Oracle: (1) atribuir ao usuario do banco o System privilege CREATE TABLE; (2) rodar o script (Windows: TWA_home\TWS\dbtools\oracle\script\d...). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console?*
- *O que causa e como solucionar o problema: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console?*

---

### 211. hwa-10.2.8-incident-rce012e-0078

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > remote-command [remote-command]]`

**Regra Canônica / Evidência:**
Sintoma: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao. Causa: (1) o host name especificado para o computador onde a instancia do remote command roda nao existe; (2) o numero da porta esta incorreto (diferente do configurado para o protocolo); (3) o tipo de protocolo especificado nao consegue estabelecer conexao porque o computador remoto nao aceita aquele protocolo. Resolucao: validar hostname, porta e protocolo. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao?*
- *O que causa e como solucionar o problema: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao?*

---

### 212. hwa-10.2.8-incident-remote-registry-0126

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > remote-command [remote-command]]`

**Regra Canônica / Evidência:**
Sintoma: remote command job entra em ABEND com AWKRCE012E 'Could not establish a connection'. Causa: um servico Windows necessario pode estar parado — iniciar o servico Remote Registry no sistema remoto. Nota: um Remote Command job que roda em workstation Windows configurada com samba protocol version 2 ou 3, sem servidor SSH ativo, falha. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKRCE012E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKRCE012E no HWA?*
- *O que causa e como solucionar o problema: remote command job entra em ABEND com AWKRCE012E 'Could not establish a connection'?*

---

### 213. hwa-10.2.8-incident-rmstdlist-aix-126-0113

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
Sintoma: o comando rmstdlist falha em AIX com exit code 126. Causa: pode haver muitos arquivos de log no diretorio stdlist. Resolucao: em AIX, remover regularmente os standard list files a cada 10-20 dias (ver User's Guide and Reference). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: o comando rmstdlist falha em AIX com exit code 126. Causa: pode haver muitos arquivos de log no diretorio stdlist?*
- *O que causa e como solucionar o problema: o comando rmstdlist falha em AIX com exit code 126?*

---

### 214. hwa-10.2.8-incident-rmstdlist-mtime-0112

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
Sintoma: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas. Causa: em UNIX, o comando usa a opcao -mtime do find, que e interpretada de forma diferente nas varias plataformas UNIX. Resolucao: considerar a interpretacao do -mtime na plataforma (ex.: rmstdlist -p 6 da os mesmos resultados que...). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas?*
- *O que causa e como solucionar o problema: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas?*

---

### 215. hwa-10.2.8-incident-root-ownership-0115

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > permissions [permissions]]`

**Regra Canônica / Evidência:**
Sintoma: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos. Causa: diretorios ou arquivos com ownership root nao foram recriados durante a fase de inicializacao. Resolucao: em UNIX, criar o diretorio/arquivo deletado com twsuser e group ownership, ou modificar o ownership do que foi criado com root; em Windows, procedimento equivalente. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos?*
- *O que causa e como solucionar o problema: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos?*

---

### 216. hwa-10.2.8-incident-schedlog-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > observability [observability]]`

**Regra Canônica / Evidência:**
Sintoma: diagnosticar por que um job falhou ou nao iniciou. Resolucao: o schedlog (log do scheduler) registra as atividades de cada workstation; consultar o schedlog no diretorio de logs da workstation (TWS_home/stdlist e schedlog) para rastrear a causa raiz.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: diagnosticar por que um job falhou ou nao iniciou?*
- *O que causa e como solucionar o problema: diagnosticar por que um job falhou ou nao iniciou?*

---

### 217. hwa-10.2.8-incident-session-invalid-0135

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: 'Session has become invalid' ao usar a interface do Dynamic Workload Console. Causa: a sessao de trabalho fechou — por logoff manual, timeout do HTTP session ou timeout da sessao LTPA (Lightweight Third Party Authentication), ou outro usuario invalidou a sessao logando com o mesmo User ID. Resolucao: verificar qual razao ocorreu, resolver o problema e logar novamente; se timeout, customizar os settings de timeout. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: 'Session has become invalid' ao usar a interface do Dynamic Workload Console?*
- *O que causa e como solucionar o problema: 'Session has become invalid' ao usar a interface do Dynamic Workload Console?*

---

### 218. hwa-10.2.8-incident-table-locked-db-gui-0110

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento. Causa: um usuario travou a tabela usando a linha de comando ou GUI do banco. DB2: apenas abrir a GUI do DB2 ja e suficiente para travar as tabelas, negando acesso a todos os processos do HWA. Oracle: abrir a linha de comando do Oracle sem auto-commit, ou a GUI, trava todas as tabelas. Resolucao: fechar a GUI/linha de comando do banco que esta segurando os locks. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento?*
- *O que causa e como solucionar o problema: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento?*

---

### 219. hwa-10.2.8-incident-tcl-hang-0093

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: em Windows, CreatePostReports.cmd, Makeplan.cmd, Updatestats.cmd ou rep8.cmd travam (hang) e os jobs nao completam. Causa: o interpretador Tool Command Language (TCL) trava sem retornar resposta ao chamador. Resolucao: esses jobs usam por default o interpretador TCL mas podem ser configurados para nao usa-lo — configurar para nao usar TCL evita o travamento. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: em Windows, CreatePostReports?*
- *O que causa e como solucionar o problema: em Windows, CreatePostReports?*

---

### 220. hwa-10.2.8-incident-terminal-services-interactive-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: ao rodar um job interativo remotamente em um fault-tolerant agent Windows via Terminal Services (Dynamic Workload Console ou linha de comando), a janela do programa de aplicacao nao abre na tela do Terminal Services, embora o programa esteja rodando no FTA. Causa: limitacao do Terminal Services, sem workaround conhecido. Resolucao: jobs interativos devem ser executados por um usuario logado no proprio fault-tolerant agent; nao podem ser executados remotamente via Terminal Services. Jobs que nao requerem interacao do usuario nao sao afetados. Fonte: HCL Troubleshooting Guide 10.2.8 (Interactive jobs are not interactive using Terminal Services).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: ao rodar um job interativo remotamente em um fault-tolerant agent Windows via Terminal Services (Dynamic Workload Console ou linha de comando), a janela do programa de aplicacao nao abre na tela do Terminal Services, embora o programa esteja rodando no FTA?*

---

### 221. hwa-10.2.8-incident-time-misaligned-0103

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > timezone [timezone]]`

**Regra Canônica / Evidência:**
Sintoma: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo. Causa: o tempo configurado nas workstations onde o master e o engine estao instalados nao esta alinhado. Resolucao (workaround): alinhar o tempo de todas as workstations da rede IBM Workload Scheduler, mesmo que estejam em timezones diferentes. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo?*
- *O que causa e como solucionar o problema: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo?*

---

### 222. hwa-10.2.8-incident-timezone-feature-0119

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > timezone [timezone]]`

**Regra Canônica / Evidência:**
Sintoma: o status relacionado a tempo de um job (ex.: 'Late') nao e reportado corretamente nas workstations porque a feature de time zone nao esta habilitada. Resolucao: habilitar a feature de time zone (ver User's Guide and Reference; ver Administration Guide para habilitar nas opcoes globais). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: o status relacionado a tempo de um job (ex?*
- *O que causa e como solucionar o problema: o status relacionado a tempo de um job (ex?*

---

### 223. hwa-10.2.8-incident-ulimit-concurrent-jobs-0127

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > performance [performance]]`

**Regra Canônica / Evidência:**
Sintoma: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes. Causa: memoria insuficiente e limite de processos por usuario para rodar os jobs concorrentemente. Resolucao: verificar e ajustar os ulimit settings (data, stack, etc.) — a submissao de um numero significativo de jobs Java requer grande quantidade de memoria; aumentar os valores de ulimit. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes?*
- *O que causa e como solucionar o problema: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes?*

---

### 224. hwa-10.2.8-incident-wui0331e-sql-0138

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: incidents > reports [reports]]`

**Regra Canônica / Evidência:**
Sintoma: AWSWUI0331E 'The SQL query could not be validated' ao rodar um report no Dynamic Workload Console. Causa: erro de sintaxe no statement da query (ex.: 'sele' no lugar de 'select'). Resolucao: verificar se a query SQL esta correta e, opcionalmente, tentar rodar a mesma query a partir da linha de comando do DB2 para validar. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSWUI0331E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSWUI0331E no HWA?*
- *Qual a ação recomendada para a mensagem AWSUI0331E no DWC?*
- *O que causa e como solucionar o problema: AWSWUI0331E 'The SQL query could not be validated' ao rodar um report no Dynamic Workload Console?*

---

### 225. hwa-10.2.8-k8s-deploy-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os componentes podem ser implantados em Kubernetes/OpenShift usando helm charts: ha guias oficiais para Red Hat OpenShift, Azure AKS, Google GKE e AWS EKS. O deployment containerizado usa imagens do registry (hclcr.io) e o helm chart define os valores (values.yaml) para os componentes (MDM, DWC, agentes, AIDA).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*

---

### 226. hwa-10.2.8-k8s-deploy-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o helm chart oficial de deployment em Kubernetes instala por padrao um unico servidor (master domain manager), um Dynamic Workload Console e um dynamic agent; para alta disponibilidade, a configuracao minima e composta por 2 Dynamic Workload Consoles e 2 servidores (master domain managers), e os componentes podem ser adicionados em multiplos namespaces e failure zones dentro de um mesmo cluster.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para deployment?*

---

### 227. hwa-10.2.8-k8s-deploy-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes suporta plataformas amd64 nas seguintes infraestruturas: Amazon EKS, Azure AKS, Google GKE e Red Hat OpenShift (OCP); o suporte a OpenShift foi formalmente testado com OpenShift 4.14 no HCL Workload Automation 10.2.7, e para Server e Console deve-se alterar os parametros waserver.server.exposeServiceType e waconsole.console.exposeServiceType de LoadBalancer para Routes.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes suporta plataformas amd64 nas seguintes infraestruturas: Amazon EKS, Azure AKS, Google GKE e Red Hat OpenShift (OCP); o suporte a OpenShift foi formalmente testado com OpenShift 4.14 no HCL Workload Automation 10.2.7, e para Server e Console deve-se alterar os parametros waserver?*

---

### 228. hwa-10.2.8-k8s-deploy-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > deployment [k8s_deploy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os recursos minimos documentados para deployment em Kubernetes sao: Server com limite de CPU 4 e memoria 16Gi (request CPU 1, memoria 4Gi, storage 10Gi), Console com limite CPU 4 e memoria 16Gi (request CPU 1, memoria 4Gi, storage 10Gi), e Dynamic Agent com request CPU 200m, memoria 200Mi e storage 2Gi; storage persistent via PVC criados pelo helm chart (um PVC por instancia de componente: data-wa-waserver-waserver0, data-wa-waconsole-waconsole0, data-wa-waagent-waagent0).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para deployment?*

---

### 229. hwa-10.2.8-k8s-deploy-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: kubernetes > security [k8s_secrets]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os secrets de senha em deployment Kubernetes sao armazenados em um objeto Secret do Kubernetes (wa-pwd-secret, tipo Opaque) com os campos WA_PASSWORD, DB_ADMIN_PASSWORD e DB_PASSWORD codificados em base64 no arquivo mysecret.yaml; opcionalmente o secret <release_name>-ssl-secret com SSL_PASSWORD pode forçar a senha do keystore, e a partir da versao 10.2, se as senhas do keystore secret e do secret opcional nao coincidirem, os keystores sao removidos e recriados com a senha definida, permitindo rotacao da senha do keystore.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os secrets de senha em deployment Kubernetes sao armazenados em um objeto Secret do Kubernetes (wa-pwd-secret, tipo Opaque) com os campos WA_PASSWORD, DB_ADMIN_PASSWORD e DB_PASSWORD codificados em base64 no arquivo mysecret?*

---

### 230. hwa-10.2.8-k8s-deploy-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > security [k8s_security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes criptografa dados em transito com TLS 1.2, dados em repouso com criptografia passiva de disco, secrets em Kubernetes Secrets aprovados, e logs livres de informacoes sensiveis; o chart instala os objetos wa-pwd-secret, certificados secret (wa-waserver/wa-waagent), network policies (mdm-network-policy, dwc-network-policy, da-network-policy) e services (wa-waserver-h, wa-waconsole-h, wa-waagent-h) por componente.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes criptografa dados em transito com TLS 1.2, dados em repouso com criptografia passiva de disco, secrets em Kubernetes Secrets aprovados, e logs livres de informacoes sensiveis; o chart instala os objetos wa-pwd-secret, certificados secret (wa-waserver/wa-waagent), network policies (mdm-network-policy, dwc-network-policy, da-network-policy) e services (wa-waserver-h, wa-waconsole-h, wa-waagent-h) por componente?*

---

### 231. hwa-10.2.8-k8s-deploy-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: kubernetes > deployment [k8s_storage]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o armazenamento persistente em deployment Kubernetes usa PVCs com access mode ReadWriteOnce; os tipos de disco suportados por provedor incluem AWS EBS GP2/IO1 SSD (EKS), Azure File/Azure Disk SSD com volumeBindingMode WaitForFirstConsumer (AKS), e GCP Standard/Balanced/SSD Persistent Disks (GKE); para o banco MSSQL em nuvem (Azure SQL ou Google Cloud SQL for SQL Server), define-se type=MSSQL no values.yaml do server e console.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o armazenamento persistente em deployment Kubernetes usa PVCs com access mode ReadWriteOnce; os tipos de disco suportados por provedor incluem AWS EBS GP2/IO1 SSD (EKS), Azure File/Azure Disk SSD com volumeBindingMode WaitForFirstConsumer (AKS), e GCP Standard/Balanced/SSD Persistent Disks (GKE); para o banco MSSQL em nuvem (Azure SQL ou Google Cloud SQL for SQL Server), define-se type=MSSQL no values?*

---

### 232. hwa-10.2.8-message-bdd003e-0041

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSBDD003E foi observada no lab durante a configuracao e validacao do arquivo BmEvents.conf (TWA_DATA_DIR=/opt/hwa/TWSDATA/BmEvents.conf) para reporte de eventos de agendamento. Parametros validados: OPTIONS=MASTER, LOGGING=ALL, SYMEVNTS=YES, CHSCHED=HIGH e lista EVENT=51 101 102... que sobrescreve completamente o default. A mensagem esta associada ao processamento de eventos do BmEvents durante o ciclo de deploy da configuracao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBDD003E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBDD003E no HWA?*
- *Qual é o significado da mensagem de erro AWSBDD003E no HWA e qual ação é recomendada?*

---

### 233. hwa-10.2.8-message-catalog-sets-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, o catalogo oficial de Messages and Codes em common/src_ms/awsmspart1TWS.html lista apenas quatro conjuntos de mensagens para HWA Distributed: AWKZSJ, AWSWUI, AWSZAP e EEL. As familias AWSBJV, AWSJCL, AWSJOL, AWSJSC, AWSFSE, AWSBMA e AWSIHS nao possuem pagina oficial de mensagens no catalogo 10.2.8; os codigos AWSJPL/AWSJCL relevantes para troubleshooting aparecem nas paginas de troubleshooting (awstrmakeplan, awstrswitchplan), e AWSJCL/AWSJOM existem em versoes mais antigas (ex.: v95).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, o catalogo oficial de Messages and Codes em common/src_ms/awsmspart1TWS?*

---

### 234. hwa-10.2.8-message-jcl050i-0039

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > optman [optman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJCL050I 'Command "chg" completed successfully' e a confirmacao informativa emitida pelo optman quando uma opcao global e alterada com sucesso (ex.: optman chg sh=401). Apos o comando, optman ls confirma o novo valor. Validado no lab: optman chg sh=401 -> AWSJCL050I; statsHistory passou de 400 para 401; optman chg sh=400 restaurou (AWSJCL050I novamente).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL050I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL050I no HWA?*
- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar optman?*

---

### 235. hwa-10.2.8-message-jdb402e-0040

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJDB402E e uma mensagem observada no lab durante operacoes de cleanup/delecao de objetos via REST API V2 ou composer (ex.: remocao de job streams orfaos de teste). Contexto lab: durante a limpeza dos 14 job streams de teste MDMDA + 3 MDMXA, cada composer delete retornou AWSBIA290I 'Total objects deleted: 1'; AWSJDB402E apareceu associada a operacoes de banco durante o cleanup, indicando tentativa de acesso/remocao de registro de objeto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB402E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB402E no HWA?*
- *Qual é o significado da mensagem de erro AWSBIA290I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?*
- *Qual é o significado da mensagem de erro AWSBIA290I no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSJDB402E no HWA e qual ação é recomendada?*

---

### 236. hwa-10.2.8-messages-awsui0002e-0001

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0002E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a user name that contains only supported characters. Wizard installation Re-enter the user name ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 237. hwa-10.2.8-messages-awsui0004e-0002

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0004E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a password that contains only supported characters. Wizard installation Re-enter the password ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 238. hwa-10.2.8-messages-awsui0005e-0003

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0005E indica um problema no Dynamic Workload Console: The confirm password must be the same as the password. O sistema The graphical wizard installation, stops with an error message. A acao documentada e: Re-enter the password and confirm password ensuring they are the same, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 239. hwa-10.2.8-messages-awsui0007e-0004

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0007E indica um problema no Dynamic Workload Console: A value must be entered in the password field. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid password, and launch a new installation. Wizard installation Enter a valid password, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 240. hwa-10.2.8-messages-awsui0009e-0005

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0009E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying an installation path that contains only supported characters. Wizard installation Re-enter the installation path ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 241. hwa-10.2.8-messages-awsui0011e-0006

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0011E indica um problema no Dynamic Workload Console: The specified INSTALL_METHOD is not valid. O sistema The installation exits with an error. A acao documentada e: Edit the response file specifying a supported installation method..

**Plataforma / Validação:** Distributed

---

### 242. hwa-10.2.8-messages-awsui0014e-0007

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0014E indica um problema no Dynamic Workload Console: The value entered as TCP/IP port is not valid. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid TCP/IP port number, and launch a new installation. Wizard installation Re-enter a valid TCP/IP port number, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 243. hwa-10.2.8-messages-awsui0016e-0008

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0016E indica um problema no Dynamic Workload Console: The value entered for TCP/IP port has already been assigned to the other ports indicated in the message text. O sistema The installation stops with an error message. A acao documentada e: Re-enter a new TCP/IP port number, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 244. hwa-10.2.8-messages-awsui0018e-0009

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0018E indica um problema no Dynamic Workload Console: Administrator's privileges are required to run the installation. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: Login as an Administrator and launch a new installation..

**Plataforma / Validação:** Distributed

---

### 245. hwa-10.2.8-messages-awsui0020e-0010

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0020E indica um problema no Dynamic Workload Console: A value must be entered in the service ID field. O sistema The installation stops with an error message. A acao documentada e: Enter a valid service ID, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 246. hwa-10.2.8-messages-awsui0023e-0011

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0023E indica um problema no Dynamic Workload Console: The values entered as credentials for IBM Integrated Portal are incorrect. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying valid credentials, and start a new installation. Wizard installation Enter the credentials again, ensuring that they are valid, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 247. hwa-10.2.8-messages-awsui0025e-0012

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0025E indica um problema no Dynamic Workload Console: This installation mode is not supported. O sistema Installation does not start. A acao documentada e: Launch a new installation using one of the supported methods: either the graphical wizard or the silent installation..

**Plataforma / Validação:** Distributed

---

### 248. hwa-10.2.8-messages-awsui0026e-0013

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0026E indica um problema no Dynamic Workload Console: The uninstallation completed but not all the files have been removed. You can find the error messages in the log file, before current error. O sistema The system uninstalls the application but leaves some files to be removed manually. A acao documentada e: Check the errors that caused the uninstallation failure in the log file. Optionally, remove the unnecessary files that have not been uninstalled properly..

**Plataforma / Validação:** Distributed

---

### 249. hwa-10.2.8-messages-awsui0028e-0014

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0028E indica um problema no Dynamic Workload Console: The installation of the product requires security to be enabled on the selected instance of IBM Integrated Portal. O sistema The installation exits with an error message. A acao documentada e: Enable security on the selected instance of IBM Integrated Portal or select a different instance of IBM Integrated Portal that has security enabled..

**Plataforma / Validação:** Distributed

---

### 250. hwa-10.2.8-messages-awsui0030w-0015

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0030W indica um problema no Dynamic Workload Console: The availability of the specified TCP/IP port could not be verified. O sistema Installation continues without checking port availability. A acao documentada e: Proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 251. hwa-10.2.8-messages-awsui0031e-0016

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0031E indica um problema no Dynamic Workload Console: A location must be specified for the WebSphere Update Installer. O sistema The installation stops with an error message. A acao documentada e: Enter a valid location, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 252. hwa-10.2.8-messages-awsui0033w-0017

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0033W indica um problema no Dynamic Workload Console: It was not possible to verify if IBM Integrated Portal is correctly installed. O sistema Installation continues. A acao documentada e: Check that IBM Integrated Portal is installed correctly, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 253. hwa-10.2.8-messages-awsui0034e-0018

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0034E indica um problema no Dynamic Workload Console: The IBM Integrated Portal profile that does not exist. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a directory where the IBM Integrated Portal was installed, and start the installation again. Wizard installation Specify a directory where the IBM Integrated Portal was installed and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 254. hwa-10.2.8-messages-awsui0036e-0019

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0036E indica um problema no Dynamic Workload Console: The IBM Integrated Portal cell does not exist. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a different directory, and start the installation again. Wizard installation Specify a directory that contains an instance of IBM Integrated Portal, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 255. hwa-10.2.8-messages-awsui0038e-0020

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0038E indica um problema no Dynamic Workload Console: The specified directory does not contain any WebSphere Update Installer. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid directory, and launch a new installation. Wizard installation Specify a valid directory, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 256. hwa-10.2.8-messages-awsui0043e-0021

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0043E indica um problema no Dynamic Workload Console: It is not possible to install more than one instance of Dynamic Workload Console on the same system. O sistema Installation fails. A acao documentada e: Uninstall the existing Dynamic Workload Console or install the new Dynamic Workload Console on a different system..

**Plataforma / Validação:** Distributed

---

### 257. hwa-10.2.8-messages-awsui0045e-0022

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0045E indica um problema no Dynamic Workload Console: It is not possible to install the Dynamic Workload Console Fix Pack 2 more than once on the same system. O sistema The installation fails. A acao documentada e: Uninstall the existing Dynamic Workload Console or install the Dynamic Workload Console Fix Pack 2 on a different system..

**Plataforma / Validação:** Distributed

---

### 258. hwa-10.2.8-messages-awsui0046e-0023

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0046E indica um problema no Dynamic Workload Console: A Windows Service ID was specified that already exists in the registry. O sistema The graphical wizard installation stops with an error message. A acao documentada e: Specify a valid Windows Service ID, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 259. hwa-10.2.8-messages-awsui0048e-0024

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0048E indica um problema no Dynamic Workload Console: The Windows Service ID specified for the WAS_SERVICE_NAME variable in the response file already exists in the registry. O sistema The silent installation fails with an error. A acao documentada e: Specify a valid Windows Service ID in the response file, and launch a new installation..

**Plataforma / Validação:** Distributed

---

### 260. hwa-10.2.8-messages-awsui0051e-0025

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0051E indica um problema no Dynamic Workload Console: See message. O sistema The silent installation fails. A acao documentada e: Check the indicated log file for details of why the installation failed..

**Plataforma / Validação:** Distributed

---

### 261. hwa-10.2.8-messages-awsui0052e-0026

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0052E indica um problema no Dynamic Workload Console: See message. O sistema The silent uninstallation fails. A acao documentada e: Check the indicated log file for details of why the uninstallation failed..

**Plataforma / Validação:** Distributed

---

### 262. hwa-10.2.8-messages-awsui0064e-0027

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0064E indica um problema no Dynamic Workload Console: See message. O sistema See message. A acao documentada e: See the trace file to check the cause of the error. Fix the problem and rerun the installation..

**Plataforma / Validação:** Distributed

---

### 263. hwa-10.2.8-messages-awsui0070w-0028

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0070W indica um problema no Dynamic Workload Console: You have selected to upgrade Dynamic Workload Console, but the instance of Dynamic Workload Console found on the system cannot be upgraded. O sistema If you are running the interactive wizard, the wizard stops. If you are running the silent installation, the installation fails. A acao documentada e: Proceed as follows:.

**Plataforma / Validação:** Distributed

---

### 264. hwa-10.2.8-messages-awsui0073e-0029

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0073E indica um problema no Dynamic Workload Console: See message. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: Install a fresh instance of the Dynamic Workload Console..

**Plataforma / Validação:** Distributed

---

### 265. hwa-10.2.8-messages-awsui0076w-0030

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0076W indica um problema no Dynamic Workload Console: See message. O sistema The installation proceeds. A acao documentada e: You can continue with the installation, but verify that the backup directory specified exists and that it has sufficient space to continue with the installation..

**Plataforma / Validação:** Distributed

---

### 266. hwa-10.2.8-messages-awsui0077e-0031

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0077E indica um problema no Dynamic Workload Console: See message. O sistema The installation fails. A acao documentada e: Free the required space on the specified backup directory, or specify a directory that has sufficient space..

**Plataforma / Validação:** Distributed

---

### 267. hwa-10.2.8-messages-awsui0079e-0032

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0079E indica um problema no Dynamic Workload Console: A more recent version of the Dynamic Workload Console fix pack is installed on the workstation. It is no longer possible to perform the rollbackoperation with the Fix Pack 2. O sistema Installation stops. A acao documentada e: Click Cancel to exit from the installation wizard. Proceed with the installation of a more recent fix pack.

**Plataforma / Validação:** Distributed

---

### 268. hwa-10.2.8-messages-awsui0083e-0033

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0083E indica um problema no Dynamic Workload Console: The specified directory does not contain any instance of IBM Integrated Portal. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a different directory, and start the installation again. Wizard installation Specify a directory that contains an instance of IBM Integrated Portal, and proceed with the installation..

**Plataforma / Validação:** Distributed

---

### 269. hwa-10.2.8-messages-awsui0085e-0034

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0085E indica um problema no Dynamic Workload Console: See message. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: Use a supported LDAP server type or install a fresh instance of the Dynamic Workload Console..

**Plataforma / Validação:** Distributed

---

### 270. hwa-10.2.8-messages-awsui0087e-0035

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0087E indica um problema no Dynamic Workload Console: See message text. O sistema The installation cannot proceed. A acao documentada e: Your system must satisfy the Dynamic Workload Console fix pack installation prerequisites otherwise your fix pack installation does not start. For more details about the fix pack installation prerequisites, see the Dynamic Workload Console fix pack readme. See the Dynamic Workload Console fix pack prerequisites and modify your system settings, if it is possible, or change the machine with another one that satisfies the prerequisites. Restart the installation..

**Plataforma / Validação:** Distributed

---

### 271. hwa-10.2.8-messages-awsui0101e-0036

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0101E indica um problema no Dynamic Workload Console: The plan view could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 272. hwa-10.2.8-messages-awsui0102e-0037

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0102E indica um problema no Dynamic Workload Console: The resource list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 273. hwa-10.2.8-messages-awsui0104e-0038

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0104E indica um problema no Dynamic Workload Console: The workstation list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 274. hwa-10.2.8-messages-awsui0106e-0039

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0106E indica um problema no Dynamic Workload Console: The job stream could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 275. hwa-10.2.8-messages-awsui0107e-0040

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0107E indica um problema no Dynamic Workload Console: The Job Stream Editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 276. hwa-10.2.8-messages-awsui0109e-0041

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0109E indica um problema no Dynamic Workload Console: The Resource Editor could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 277. hwa-10.2.8-messages-awsui0111e-0042

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0111E indica um problema no Dynamic Workload Console: The job stream could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 278. hwa-10.2.8-messages-awsui0112e-0043

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0112E indica um problema no Dynamic Workload Console: The resource availability definition could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 279. hwa-10.2.8-messages-awsui0114e-0044

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0114E indica um problema no Dynamic Workload Console: The job stream could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 280. hwa-10.2.8-messages-awsui0116e-0045

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0116E indica um problema no Dynamic Workload Console: The resource could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 281. hwa-10.2.8-messages-awsui0117e-0046

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0117E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Select a dependency on a job in another job stream. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 282. hwa-10.2.8-messages-awsui0118e-0047

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0118E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Complete all the fields in the panel before pressing OK..

**Plataforma / Validação:** Distributed

---

### 283. hwa-10.2.8-messages-awsui0120e-0048

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0120E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Specify different filter criteria and run the list again..

**Plataforma / Validação:** Distributed

---

### 284. hwa-10.2.8-messages-awsui0121e-0049

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0121E indica um problema no Dynamic Workload Console: In job A you have defined a dependency on job B, but job B is dependent, directly or indirectly, on job A. O sistema The requested action was not completed successfully. A acao documentada e: Define a valid dependency that does not create a circular dependency. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 285. hwa-10.2.8-messages-awsui0124e-0050

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0124E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply the correct name for the job stream instance. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 286. hwa-10.2.8-messages-awsui0125e-0051

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0125E indica um problema no Dynamic Workload Console: The workstation could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 287. hwa-10.2.8-messages-awsui0127e-0052

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0127E indica um problema no Dynamic Workload Console: There was a class cast exception due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 288. hwa-10.2.8-messages-awsui0128e-0053

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0128E indica um problema no Dynamic Workload Console: There is a problem with the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 289. hwa-10.2.8-messages-awsui0130e-0054

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0130E indica um problema no Dynamic Workload Console: The job dependency could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 290. hwa-10.2.8-messages-awsui0132e-0055

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0132E indica um problema no Dynamic Workload Console: The job could not be changed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 291. hwa-10.2.8-messages-awsui0133e-0056

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0133E indica um problema no Dynamic Workload Console: The job could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 292. hwa-10.2.8-messages-awsui0135e-0057

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0135E indica um problema no Dynamic Workload Console: The instance could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 293. hwa-10.2.8-messages-awsui0137e-0058

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0137E indica um problema no Dynamic Workload Console: The instance could not be released due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 294. hwa-10.2.8-messages-awsui0138e-0059

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0138E indica um problema no Dynamic Workload Console: The object could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 295. hwa-10.2.8-messages-awsui0140e-0060

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0140E indica um problema no Dynamic Workload Console: The status in the database could not be modified due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 296. hwa-10.2.8-messages-awsui0142e-0061

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0142E indica um problema no Dynamic Workload Console: The job dependency could not be removed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 297. hwa-10.2.8-messages-awsui0143e-0062

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0143E indica um problema no Dynamic Workload Console: The dependency could not be removed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 298. hwa-10.2.8-messages-awsui0145e-0063

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0145E indica um problema no Dynamic Workload Console: The action could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 299. hwa-10.2.8-messages-awsui0150e-0064

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0150E indica um problema no Dynamic Workload Console: The action could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 300. hwa-10.2.8-messages-awsui0155e-0065

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0155E indica um problema no Dynamic Workload Console: The workstation editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 301. hwa-10.2.8-messages-awsui0157e-0066

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0157E indica um problema no Dynamic Workload Console: The workstation could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 302. hwa-10.2.8-messages-awsui0158e-0067

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0158E indica um problema no Dynamic Workload Console: The selected workstations could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 303. hwa-10.2.8-messages-awsui0160e-0068

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0160E indica um problema no Dynamic Workload Console: Another run cycle could not be created due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 304. hwa-10.2.8-messages-awsui0162e-0069

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0162E indica um problema no Dynamic Workload Console: The operation could not be interrupted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 305. hwa-10.2.8-messages-awsui0163e-0070

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0163E indica um problema no Dynamic Workload Console: The resource could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 306. hwa-10.2.8-messages-awsui0165e-0071

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0165E indica um problema no Dynamic Workload Console: The resource header could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 307. hwa-10.2.8-messages-awsui0167e-0072

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0167E indica um problema no Dynamic Workload Console: The resource dependency could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 308. hwa-10.2.8-messages-awsui0168e-0073

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0168E indica um problema no Dynamic Workload Console: The scheduling specifications could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 309. hwa-10.2.8-messages-awsui0173e-0074

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0173E indica um problema no Dynamic Workload Console: See message. O sistema Processing continues but the object is displayed in read-only mode. A acao documentada e: Try to update the object later, after it has been released..

**Plataforma / Validação:** Distributed

---

### 310. hwa-10.2.8-messages-awsui0174e-0075

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0174E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Check whether a connector is installed on the server. If a connector is not installed, install an instance. Planning and Installation.

**Plataforma / Validação:** Distributed

---

### 311. hwa-10.2.8-messages-awsui0176e-0076

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0176E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Remove the external job that has no link or link it with another job. Retry the save of the job stream..

**Plataforma / Validação:** Distributed

---

### 312. hwa-10.2.8-messages-awsui0177e-0077

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0177E indica um problema no Dynamic Workload Console: An attempt was made to add a dependency from a different job scheduling engine. A job stream cannot have external dependencies from other job scheduling engines. O sistema The requested action was not completed successfully. A acao documentada e: Add the dependency into a job stream on the same engine. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 313. hwa-10.2.8-messages-awsui0180e-0078

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0180E indica um problema no Dynamic Workload Console: The selected engine is not available due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 314. hwa-10.2.8-messages-awsui0181e-0079

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0181E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: The selected view probably has a pending dialog. Close the dialog before attaching the view..

**Plataforma / Validação:** Distributed

---

### 315. hwa-10.2.8-messages-awsui0183e-0080

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0183E indica um problema no Dynamic Workload Console: The job output could not be loaded because it uses an unsupported encoding. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 316. hwa-10.2.8-messages-awsui0185e-0081

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0185E indica um problema no Dynamic Workload Console: The plan view could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 317. hwa-10.2.8-messages-awsui0188e-0082

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0188E indica um problema no Dynamic Workload Console: The job could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 318. hwa-10.2.8-messages-awsui0193e-0083

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0193E indica um problema no Dynamic Workload Console: Two lists cannot be created with the same name in the same path. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new list name. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 319. hwa-10.2.8-messages-awsui0196e-0084

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0196E indica um problema no Dynamic Workload Console: Two lists cannot be created with the same name in the same path. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new list name..

**Plataforma / Validação:** Distributed

---

### 320. hwa-10.2.8-messages-awsui0197w-0085

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0197W indica um problema no Dynamic Workload Console: The number format is not correct. The value remains unchanged. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new number in the correct format. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 321. hwa-10.2.8-messages-awsui0199e-0086

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0199E indica um problema no Dynamic Workload Console: The workstation definition could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 322. hwa-10.2.8-messages-awsui0201e-0087

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0201E indica um problema no Dynamic Workload Console: The job stream list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 323. hwa-10.2.8-messages-awsui0206e-0088

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0206E indica um problema no Dynamic Workload Console: The resource could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 324. hwa-10.2.8-messages-awsui0208e-0089

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0208E indica um problema no Dynamic Workload Console: The resource instance could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 325. hwa-10.2.8-messages-awsui0209e-0090

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0209E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Specify a fully qualified class name..

**Plataforma / Validação:** Distributed

---

### 326. hwa-10.2.8-messages-awsui0211e-0091

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0211E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a deadline that is later than the start time. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 327. hwa-10.2.8-messages-awsui0225e-0092

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0225E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Select another instance on which to perform the operation, or another operation to perform on the selected instance..

**Plataforma / Validação:** Distributed

---

### 328. hwa-10.2.8-messages-awsui0226e-0093

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0226E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Check that you have identified the required calendar correctly. Specify another calendar or create the required calendar..

**Plataforma / Validação:** Distributed

---

### 329. hwa-10.2.8-messages-awsui0236e-0094

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0236E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a value with a number of characters that is less than or equal to the allowed maximum length. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 330. hwa-10.2.8-messages-awsui0237e-0095

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0237E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a value with a number of characters that is greater than the minimum length. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 331. hwa-10.2.8-messages-awsui0238e-0096

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0238E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid IP address (in the format [IP_ADDRESS]) or a valid node name (in the format: <server>.<domain>). Retry the operation..

**Plataforma / Validação:** Distributed

---

### 332. hwa-10.2.8-messages-awsui0240e-0097

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0240E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 333. hwa-10.2.8-messages-awsui0242e-0098

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0242E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 334. hwa-10.2.8-messages-awsui0243e-0099

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0243E indica um problema no Dynamic Workload Console: The Job Stream Editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 335. hwa-10.2.8-messages-awsui0246e-0100

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0246E indica um problema no Dynamic Workload Console: The resources necessary to show the localized version were not found. O sistema Processing continues but the dialogs are shown without messages. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 336. hwa-10.2.8-messages-awsui0247e-0101

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0247E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a numeric string. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 337. hwa-10.2.8-messages-awsui0248e-0102

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0248E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a value within the accepted range. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 338. hwa-10.2.8-messages-awsui0254e-0103

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0254E indica um problema no Dynamic Workload Console: The resource name is a mandatory field. O sistema The requested action was not completed successfully. A acao documentada e: Supply a name for the resource. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 339. hwa-10.2.8-messages-awsui0259e-0104

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0259E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply the time in the correct format. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 340. hwa-10.2.8-messages-awsui0260e-0105

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0260E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 341. hwa-10.2.8-messages-awsui0261e-0106

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0261E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Retry the operation..

**Plataforma / Validação:** Distributed

---

### 342. hwa-10.2.8-messages-awsui0264e-0107

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0264E indica um problema no Dynamic Workload Console: The Workstation name is a mandatory field. O sistema The requested action was not completed successfully. A acao documentada e: Supply a Workstation name. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 343. hwa-10.2.8-messages-awsui0266e-0108

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0266E indica um problema no Dynamic Workload Console: The blank character is not a valid character. O sistema The requested action was not completed successfully. A acao documentada e: Supply the string again without using the blank character. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 344. hwa-10.2.8-messages-awsui0267e-0109

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0267E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Ensure that all rule details are correct. Supply an inclusive shift origin value in the periods selected. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 345. hwa-10.2.8-messages-awsui0269e-0110

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0269E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Set the Duration of the job instance to a value other than zero. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 346. hwa-10.2.8-messages-awsui0277e-0111

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0277E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Set filter values for both the Date and the Time fields, or do not set values for either. Retry the query..

**Plataforma / Validação:** Distributed

---

### 347. hwa-10.2.8-messages-awsui0278e-0112

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0278E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Set filter values for both the Date and the Time fields, or do not set values for either. Retry the query..

**Plataforma / Validação:** Distributed

---

### 348. hwa-10.2.8-messages-awsui0281e-0113

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0281E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Check the host name and make sure the computer where the host is running is active and accessible in the network (try pinging the host using the host name you supplied). Retry the operation..

**Plataforma / Validação:** Distributed

---

### 349. hwa-10.2.8-messages-awsui0283e-0114

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0283E indica um problema no Dynamic Workload Console: The object could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 350. hwa-10.2.8-messages-awsui0286e-0115

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0286E indica um problema no Dynamic Workload Console: Two run cycles with the same name cannot exist for the same job stream. O sistema The requested action was not completed successfully. A acao documentada e: Supply a different name for the new run cycle. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 351. hwa-10.2.8-messages-awsui0291e-0116

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0291E indica um problema no Dynamic Workload Console: The job stream could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 352. hwa-10.2.8-messages-awsui0292e-0117

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0292E indica um problema no Dynamic Workload Console: System action: O sistema Operator response: A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

---

### 353. hwa-10.2.8-messages-awsui0295e-0118

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0295E indica um problema no Dynamic Workload Console: You have defined a dependency so that job A depends on job B, but jobs A and B are the same. O sistema The requested action was not completed successfully. A acao documentada e: Change the dependency to a job other than itself. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 354. hwa-10.2.8-messages-awsui0296e-0119

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0296E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Ensure that the object of an external dependency exists before setting the dependency. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 355. hwa-10.2.8-messages-awsui0297e-0120

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0297E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply the job name of an existing job definition..

**Plataforma / Validação:** Distributed

---

### 356. hwa-10.2.8-messages-awsui0299e-0121

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0299E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Check the reason given in the system_error_message. Resolve the problem. If you cannot determine the problem from the error message, check that there is sufficient space to write the file, and that the user using the console has permission to write in the indicated directory. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 357. hwa-10.2.8-messages-awsui0300e-0122

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0300E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: If the file exists but with a different name, rename it to the expected name. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 358. hwa-10.2.8-messages-awsui0303e-0123

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0303E indica um problema no Dynamic Workload Console: A dependency between job streams must be unique. O sistema The requested action was not completed successfully. A acao documentada e: Modify one or both dependencies to make them unique. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 359. hwa-10.2.8-messages-awsui0304e-0124

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0304E indica um problema no Dynamic Workload Console: Run cycle names in job streams must be unique. O sistema The requested action was not completed successfully. A acao documentada e: Modify one or both run cycles to make their names unique. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 360. hwa-10.2.8-messages-awsui0305e-0125

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0305E indica um problema no Dynamic Workload Console: The remote server is not reachable. O sistema The requested action was not completed successfully. A acao documentada e: Check the validity of the user name and password. Check if the connection with the remote server is available. Check if the remote server is started. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 361. hwa-10.2.8-messages-awsui0307e-0126

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0307E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a name that conforms to the indicated naming rules..

**Plataforma / Validação:** Distributed

---

### 362. hwa-10.2.8-messages-awsui0311e-0127

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0311E indica um problema no Dynamic Workload Console: The job output could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 363. hwa-10.2.8-messages-awsui0313e-0128

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0313E indica um problema no Dynamic Workload Console: To rerun a job you have to specify either both the job definition and workstation, or neither of them (in this case, the original job definition and workstation will be used). O sistema The requested action was not completed successfully. A acao documentada e: Specify the workstation or clear the job definition field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 364. hwa-10.2.8-messages-awsui0314e-0129

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0314E indica um problema no Dynamic Workload Console: To rerun a job you have to specify either both the job definition and workstation, or neither of them (in this case, the original job definition and workstation will be used). O sistema The requested action was not completed successfully. A acao documentada e: Specify the job definition or clear the workstation field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 365. hwa-10.2.8-messages-awsui0316e-0130

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0316E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid value using only the permitted characters. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 366. hwa-10.2.8-messages-awsui0317e-0131

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0317E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid value using only the permitted characters. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 367. hwa-10.2.8-messages-awsui0318e-0132

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0318E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid value for this mandatory field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 368. hwa-10.2.8-messages-awsui0324e-0133

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0324E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Fill at least one of the fields indicated in the error message. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 369. hwa-10.2.8-messages-awsui0325e-0134

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0325E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully.c A acao documentada e: Supply a valid value for the mandatory field(s). Retry the operation..

**Plataforma / Validação:** Distributed

---

### 370. hwa-10.2.8-messages-awsui0326e-0135

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0326E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Check and correct the object name or specify another object. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 371. hwa-10.2.8-messages-awsui0327e-0136

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0327E indica um problema no Dynamic Workload Console: A string containing less than the indicated minimum characters has been entered. O sistema The requested action was not completed successfully. A acao documentada e: Enter a valid value of more than the indicated minimum characters. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 372. hwa-10.2.8-messages-awsui0330e-0137

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0330E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid value for this mandatory field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 373. hwa-10.2.8-messages-awsui0331e-0138

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0331E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 374. hwa-10.2.8-messages-awsui0333e-0139

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0333E indica um problema no Dynamic Workload Console: For the requested operation at least one Status value must be supplied. O sistema The requested action was not completed successfully. A acao documentada e: Supply at least one Status value. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 375. hwa-10.2.8-messages-awsui0335e-0140

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0335E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply the Query SQL statement field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 376. hwa-10.2.8-messages-awsui0336e-0141

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0336E indica um problema no Dynamic Workload Console: The connection to the database could not be established because the database is not active or the connection parameters set in the engine connection are not correct. O sistema The requested action was not completed successfully. A acao documentada e: Verify that the database is up and running and the connection parameters set in the engine connection are correct. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 377. hwa-10.2.8-messages-awsui0337e-0142

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0337E indica um problema no Dynamic Workload Console: The query does not return any results because the From time is later than the To time. O sistema The requested action was not completed successfully. A acao documentada e: Supply an earlier From time, or a later To time. Retry the query..

**Plataforma / Validação:** Distributed

---

### 378. hwa-10.2.8-messages-awsui0339e-0143

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0339E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Review the items in the list and reduce the number of them until it is not more than the indicated maximum. Retry the query..

**Plataforma / Validação:** Distributed

---

### 379. hwa-10.2.8-messages-awsui0340e-0144

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0340E indica um problema no Dynamic Workload Console: The query does not return any results because the Specific Dates list is empty. O sistema The requested action was not completed successfully. A acao documentada e: Add at least one date to the Specific Dates list. Retry the query..

**Plataforma / Validação:** Distributed

---

### 380. hwa-10.2.8-messages-awsui0341e-0145

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0341E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid value using only the permitted characters. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 381. hwa-10.2.8-messages-awsui0342e-0146

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0342E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Select one or more dates from the Specific Dates list to delete. Click Delete again..

**Plataforma / Validação:** Distributed

---

### 382. hwa-10.2.8-messages-awsui0344e-0147

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0344E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Choose an engine in the“”Enter Task Information“” panel..

**Plataforma / Validação:** Distributed

---

### 383. hwa-10.2.8-messages-awsui0346e-0148

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0346E indica um problema no Dynamic Workload Console: The database might not be available or the parameters specified for the database configuration are not correct. O sistema The requested action was not completed successfully. A acao documentada e: Check the database credentials, if the problem persists, contact the IBM Workload Scheduler administrator..

**Plataforma / Validação:** Distributed

---

### 384. hwa-10.2.8-messages-awsui0358e-0149

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0358E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a valid output limit value. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 385. hwa-10.2.8-messages-awsui0359w-0150

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0359W indica um problema no Dynamic Workload Console: The list of available actions and event types in the event rule task that you are editing depends on the engine specified. The engine has been modified and the new engine supports a different set of actions and event types. O sistema The engine has been changed as requested and the list of selected actions and event types has been reset. A acao documentada e: Edit your event rule definition specifying a new list of actions and event types. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 386. hwa-10.2.8-messages-awsui0361e-0151

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0361E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Change the input value to a positive value, greater than the indicated minimum..

**Plataforma / Validação:** Distributed

---

### 387. hwa-10.2.8-messages-awsui0370e-0152

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0370E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Choose an engine in the“”Enter Task Information“” panel..

**Plataforma / Validação:** Distributed

---

### 388. hwa-10.2.8-messages-awsui0371w-0153

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0371W indica um problema no Dynamic Workload Console: You have tried to modify the status of the event rules to be “”draft“”, but they are already in “”draft“” status. O sistema The requested action was not completed successfully. A acao documentada e: None.

**Plataforma / Validação:** Distributed

---

### 389. hwa-10.2.8-messages-awsui0372w-0154

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0372W indica um problema no Dynamic Workload Console: You have tried to modify the status of the event rules to be “”complete“”, but they are already in “”complete“” status. O sistema The requested action was not completed successfully. A acao documentada e: None.

**Plataforma / Validação:** Distributed

---

### 390. hwa-10.2.8-messages-awsui0376e-0155

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0376E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Correct the value for the number of days and retry the operation..

**Plataforma / Validação:** Distributed

---

### 391. hwa-10.2.8-messages-awsui0407e-0156

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0407E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you have sufficient permission and that the object was not deleted..

**Plataforma / Validação:** Distributed

---

### 392. hwa-10.2.8-messages-awsui0410e-0157

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0410E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: See message text.

**Plataforma / Validação:** Distributed

---

### 393. hwa-10.2.8-messages-awsui0500e-0158

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0500E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Choose a scheduler engine that is a supported version, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 394. hwa-10.2.8-messages-awsui0501e-0159

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0501E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a To priority greater than the From priority and retry the operation..

**Plataforma / Validação:** Distributed

---

### 395. hwa-10.2.8-messages-awsui0503e-0160

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0503E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid job definition name and all the other mandatory fields in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 396. hwa-10.2.8-messages-awsui0504e-0161

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0504E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Reduce the number of scheduled dependencies to less than the maximum and retry the operation..

**Plataforma / Validação:** Distributed

---

### 397. hwa-10.2.8-messages-awsui0506e-0162

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0506E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Determine why you are trying to define the same dependency twice. If you accidentally tried to create the same dependency twice, take to further action. Otherwise, modify a dependency in the job stream and retry the operation..

**Plataforma / Validação:** Distributed

---

### 398. hwa-10.2.8-messages-awsui0507e-0163

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0507E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Delete the dependency and retry the operation..

**Plataforma / Validação:** Distributed

---

### 399. hwa-10.2.8-messages-awsui0508e-0164

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0508E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Delete the dependency and retry the operation..

**Plataforma / Validação:** Distributed

---

### 400. hwa-10.2.8-messages-awsui0510e-0165

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0510E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Delete one of the resource dependencies at job level or job stream level and retry the operation..

**Plataforma / Validação:** Distributed

---

### 401. hwa-10.2.8-messages-awsui0511e-0166

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0511E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid job stream workstation name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 402. hwa-10.2.8-messages-awsui0512e-0167

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0512E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid workstation name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 403. hwa-10.2.8-messages-awsui0514e-0168

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0514E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid command and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 404. hwa-10.2.8-messages-awsui0515e-0169

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0515E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Enclose the parameter name between caret (^) characters and retry the operation..

**Plataforma / Validação:** Distributed

---

### 405. hwa-10.2.8-messages-awsui0516e-0170

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0516E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid job file and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 406. hwa-10.2.8-messages-awsui0517e-0171

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0517E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid login and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 407. hwa-10.2.8-messages-awsui0519e-0172

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0519E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid workstation class or use a wildcard and retry the operation..

**Plataforma / Validação:** Distributed

---

### 408. hwa-10.2.8-messages-awsui0520e-0173

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0520E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid parameter name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 409. hwa-10.2.8-messages-awsui0521e-0174

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0521E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid prompt name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 410. hwa-10.2.8-messages-awsui0523e-0175

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0523E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid domain name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 411. hwa-10.2.8-messages-awsui0524e-0176

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0524E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid calendar name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 412. hwa-10.2.8-messages-awsui0525e-0177

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0525E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply at least one day for the calendar and retry the operation..

**Plataforma / Validação:** Distributed

---

### 413. hwa-10.2.8-messages-awsui0526e-0178

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0526E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply the R/3 job information and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 414. hwa-10.2.8-messages-awsui0527e-0179

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0527E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select a job stream in the list and retry the operation..

**Plataforma / Validação:** Distributed

---

### 415. hwa-10.2.8-messages-awsui0529e-0180

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0529E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select a new SAP Job on the task panel, or change the workstation to the workstation the SAP job is defined on and retry the operation..

**Plataforma / Validação:** Distributed

---

### 416. hwa-10.2.8-messages-awsui0530e-0181

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0530E indica um problema no Dynamic Workload Console: It is not possible to establish a connection with the R/3 system. O sistema The requested operation is not completed successfully. A acao documentada e: Wait for the R/3 system to become available and try again..

**Plataforma / Validação:** Distributed

---

### 417. hwa-10.2.8-messages-awsui0532e-0182

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0532E indica um problema no Dynamic Workload Console: The job definition could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 418. hwa-10.2.8-messages-awsui0533e-0183

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0533E indica um problema no Dynamic Workload Console: The job definition list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 419. hwa-10.2.8-messages-awsui0535e-0184

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0535E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Edit the properties for this job and select a new task type and workstation and retry the operation..

**Plataforma / Validação:** Distributed

---

### 420. hwa-10.2.8-messages-awsui0536e-0185

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0536E indica um problema no Dynamic Workload Console: The job definitions could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 421. hwa-10.2.8-messages-awsui0538w-0186

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0538W indica um problema no Dynamic Workload Console: The workstation class could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 422. hwa-10.2.8-messages-awsui0540e-0187

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0540E indica um problema no Dynamic Workload Console: The workstation class could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 423. hwa-10.2.8-messages-awsui0541e-0188

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0541E indica um problema no Dynamic Workload Console: The workstation class could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 424. hwa-10.2.8-messages-awsui0543e-0189

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0543E indica um problema no Dynamic Workload Console: The user could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 425. hwa-10.2.8-messages-awsui0544e-0190

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0544E indica um problema no Dynamic Workload Console: The selected user list could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 426. hwa-10.2.8-messages-awsui0546e-0191

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0546E indica um problema no Dynamic Workload Console: The user could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 427. hwa-10.2.8-messages-awsui0548e-0192

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0548E indica um problema no Dynamic Workload Console: The parameters could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 428. hwa-10.2.8-messages-awsui0549w-0193

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0549W indica um problema no Dynamic Workload Console: The parameter could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 429. hwa-10.2.8-messages-awsui0551e-0194

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0551E indica um problema no Dynamic Workload Console: The parameter could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 430. hwa-10.2.8-messages-awsui0553e-0195

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0553E indica um problema no Dynamic Workload Console: The prompts could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 431. hwa-10.2.8-messages-awsui0554w-0196

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0554W indica um problema no Dynamic Workload Console: The prompt could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 432. hwa-10.2.8-messages-awsui0556e-0197

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0556E indica um problema no Dynamic Workload Console: The prompt could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 433. hwa-10.2.8-messages-awsui0557e-0198

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0557E indica um problema no Dynamic Workload Console: The prompt could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 434. hwa-10.2.8-messages-awsui0559w-0199

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0559W indica um problema no Dynamic Workload Console: The calendar could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 435. hwa-10.2.8-messages-awsui0561e-0200

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0561E indica um problema no Dynamic Workload Console: The calendar could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 436. hwa-10.2.8-messages-awsui0562e-0201

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0562E indica um problema no Dynamic Workload Console: The calendar could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 437. hwa-10.2.8-messages-awsui0564w-0202

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0564W indica um problema no Dynamic Workload Console: The domain could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 438. hwa-10.2.8-messages-awsui0565e-0203

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0565E indica um problema no Dynamic Workload Console: The multiple domains could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 439. hwa-10.2.8-messages-awsui0567e-0204

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0567E indica um problema no Dynamic Workload Console: The domain could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 440. hwa-10.2.8-messages-awsui0569e-0205

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0569E indica um problema no Dynamic Workload Console: The selected multiple prompts could not be replied to due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 441. hwa-10.2.8-messages-awsui0570e-0206

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0570E indica um problema no Dynamic Workload Console: The link action for selected domain could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 442. hwa-10.2.8-messages-awsui0572e-0207

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0572E indica um problema no Dynamic Workload Console: The unlink action for the selected domain could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 443. hwa-10.2.8-messages-awsui0574e-0208

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0574E indica um problema no Dynamic Workload Console: Some of the start actions were not completed for the domain due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 444. hwa-10.2.8-messages-awsui0575e-0209

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0575E indica um problema no Dynamic Workload Console: The start action for the selected domains cannot be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 445. hwa-10.2.8-messages-awsui0577e-0210

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0577E indica um problema no Dynamic Workload Console: The stop action for the selected domains could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 446. hwa-10.2.8-messages-awsui0579e-0211

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0579E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select another calendar and retry the operation. If the problem persists, contact Software Support for assistance..

**Plataforma / Validação:** Distributed

---

### 447. hwa-10.2.8-messages-awsui0580e-0212

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0580E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that all the calendars have a name defined and retry the operation..

**Plataforma / Validação:** Distributed

---

### 448. hwa-10.2.8-messages-awsui0581e-0213

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0581E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply at least one day for the calendar and retry the operation..

**Plataforma / Validação:** Distributed

---

### 449. hwa-10.2.8-messages-awsui0583e-0214

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0583E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply the password and confirmation password again, making sure they are identical and retry the operation..

**Plataforma / Validação:** Distributed

---

### 450. hwa-10.2.8-messages-awsui0584e-0215

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0584E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a password with a number of characters that is less than or equal to the maximum length and retry the operation..

**Plataforma / Validação:** Distributed

---

### 451. hwa-10.2.8-messages-awsui0585e-0216

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0585E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Retry the operation. If the problem persists, contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 452. hwa-10.2.8-messages-awsui0586e-0217

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0586E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid Workstation Name and all the other mandatory fields present in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 453. hwa-10.2.8-messages-awsui0589e-0218

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0589E indica um problema no Dynamic Workload Console: A workstation class might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new name. O sistema If OK is clicked the workstation class is renamed. Otherwise the rename action is ignored. A acao documentada e: Click OK to rename the workstation class or click Cancel to cancel the rename action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 454. hwa-10.2.8-messages-awsui0592e-0219

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0592E indica um problema no Dynamic Workload Console: The prompt might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new name. O sistema If OK is clicked the prompt is renamed. Otherwise the rename action is ignored. A acao documentada e: Click OK to rename the prompt or click Cancel to cancel the rename action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 455. hwa-10.2.8-messages-awsui0596e-0220

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0596E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Retry the operation. If the problem persists, contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 456. hwa-10.2.8-messages-awsui0598w-0221

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0598W indica um problema no Dynamic Workload Console: An error has occurred. See the error.log file for details. O sistema Processing continues. A acao documentada e: See the error.log file for details. If you can resolve the problem, do so. Retry the operation. If you cannot resolve the problem, or the problem persists, contact Software Support for assistance..

**Plataforma / Validação:** Distributed

---

### 457. hwa-10.2.8-messages-awsui0605e-0222

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0605E indica um problema no Dynamic Workload Console: This job might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new workstation data. O sistema If OK is clicked the workstation is modified. Otherwise the request is ignored. A acao documentada e: Click OK to modify the workstation, or click Cancel to cancel the modify request and retry the operation..

**Plataforma / Validação:** Distributed

---

### 458. hwa-10.2.8-messages-awsui0606w-0223

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0606W indica um problema no Dynamic Workload Console: This resource might be a dependency for a job scheduling object. If so, the dependency is also updated with the new workstation data. O sistema If OK is clicked the workstation is modified. Otherwise the request is ignored. A acao documentada e: Click OK to modify the workstation, or click Cancel to cancel the modify request and retry the operation..

**Plataforma / Validação:** Distributed

---

### 459. hwa-10.2.8-messages-awsui0608e-0224

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0608E indica um problema no Dynamic Workload Console: This job might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new job name. O sistema If OK is clicked the job is renamed. Otherwise the rename request is ignored. A acao documentada e: Click OK to rename the job, or click Cancel to cancel the rename request and retry the operation..

**Plataforma / Validação:** Distributed

---

### 460. hwa-10.2.8-messages-awsui0610e-0225

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0610E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply the user login in the following format: [<user>].[<account>]<,group>, where each section can have a maximum of eight characters, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 461. hwa-10.2.8-messages-awsui0611e-0226

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0611E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid Details field and all the other mandatory fields presents in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 462. hwa-10.2.8-messages-awsui0612e-0227

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0612E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid Time restriction and all the other mandatory fields presents in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 463. hwa-10.2.8-messages-awsui0614e-0228

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0614E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a start year that precedes the end year and retry the operation..

**Plataforma / Validação:** Distributed

---

### 464. hwa-10.2.8-messages-awsui0615e-0229

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0615E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a start month that precedes the end month and retry the operation..

**Plataforma / Validação:** Distributed

---

### 465. hwa-10.2.8-messages-awsui0616w-0230

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0616W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid Job name and all the other mandatory fields in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 466. hwa-10.2.8-messages-awsui0617e-0231

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0617E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid Network agent and all the other mandatory fields in the panel and retry the operation..

**Plataforma / Validação:** Distributed

---

### 467. hwa-10.2.8-messages-awsui0619e-0232

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0619E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that if the dependency field begins with a quote character it also ends with one, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 468. hwa-10.2.8-messages-awsui0620e-0233

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0620E indica um problema no Dynamic Workload Console: The dependency field can be enclosed in quote characters, but there can only be two - at the beginning and the end. At least one more has been found. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that if the dependency field begins with a quote character it also ends with one, with no other quote characters in the field, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 469. hwa-10.2.8-messages-awsui0621e-0234

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0621E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Correct the workstation name in the dependency field and retry the operation..

**Plataforma / Validação:** Distributed

---

### 470. hwa-10.2.8-messages-awsui0623e-0235

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0623E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Correct the job name in the dependency field and retry the operation..

**Plataforma / Validação:** Distributed

---

### 471. hwa-10.2.8-messages-awsui0624e-0236

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0624E indica um problema no Dynamic Workload Console: The successor for the job stream could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 472. hwa-10.2.8-messages-awsui0626e-0237

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0626E indica um problema no Dynamic Workload Console: The job or job stream could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 473. hwa-10.2.8-messages-awsui0627e-0238

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0627E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid time zone for the master domain manager and retry the operation..

**Plataforma / Validação:** Distributed

---

### 474. hwa-10.2.8-messages-awsui0630e-0239

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0630E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid workstation, job name, or both, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 475. hwa-10.2.8-messages-awsui0631e-0240

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0631E indica um problema no Dynamic Workload Console: The SAP job definition could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 476. hwa-10.2.8-messages-awsui0633e-0241

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0633E indica um problema no Dynamic Workload Console: The SAP job definition could not be renamed. O sistema The requested action is not completed successfully. A acao documentada e: Click Save and Close to rename the job. Otherwise, enter the original job name and click Modify and Close to modify the job and retry the operation..

**Plataforma / Validação:** Distributed

---

### 477. hwa-10.2.8-messages-awsui0635e-0242

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0635E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Contact Software Support for assistance..

**Plataforma / Validação:** Distributed

---

### 478. hwa-10.2.8-messages-awsui0636w-0243

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0636W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: The deadline must be greater than the start time, or one of the two must be set as blank. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 479. hwa-10.2.8-messages-awsui0638e-0244

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0638E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Try closing other applications to free up memory. Retry the operation. If the problem persists you might need to reboot the workstation where you are running the console..

**Plataforma / Validação:** Distributed

---

### 480. hwa-10.2.8-messages-awsui0639e-0245

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0639E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify another calendar and retry the operation..

**Plataforma / Validação:** Distributed

---

### 481. hwa-10.2.8-messages-awsui0640w-0246

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0640W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Click OK to continue, or click Cancel to specify a new domain and retry the operation..

**Plataforma / Validação:** Distributed

---

### 482. hwa-10.2.8-messages-awsui0641e-0247

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0641E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid workstation and retry the operation..

**Plataforma / Validação:** Distributed

---

### 483. hwa-10.2.8-messages-awsui0644e-0248

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0644E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a recovery option job name that is different from the job being defined and retry the operation..

**Plataforma / Validação:** Distributed

---

### 484. hwa-10.2.8-messages-awsui0645e-0249

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0645E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Change the resolution criteria for the dependencies of the job stream jobs and retry the operation..

**Plataforma / Validação:** Distributed

---

### 485. hwa-10.2.8-messages-awsui0646e-0250

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0646E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Change the resolution criteria for the dependencies of the job stream and retry the operation..

**Plataforma / Validação:** Distributed

---

### 486. hwa-10.2.8-messages-awsui0649e-0251

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0649E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Choose a resource that exists and retry the operation..

**Plataforma / Validação:** Distributed

---

### 487. hwa-10.2.8-messages-awsui0654e-0252

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0654E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Remove the job stream instance dependency on itself or on its jobs and retry the operation..

**Plataforma / Validação:** Distributed

---

### 488. hwa-10.2.8-messages-awsui0655e-0253

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0655E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Remove the job instance dependency on itself or on its job stream instance and retry the operation..

**Plataforma / Validação:** Distributed

---

### 489. hwa-10.2.8-messages-awsui0698w-0254

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0698W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply an earlier start time and retry the operation..

**Plataforma / Validação:** Distributed

---

### 490. hwa-10.2.8-messages-awsui0699w-0255

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0699W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply an earlier start time and retry the operation..

**Plataforma / Validação:** Distributed

---

### 491. hwa-10.2.8-messages-awsui0700w-0256

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0700W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a correct return code expression and retry the operation..

**Plataforma / Validação:** Distributed

---

### 492. hwa-10.2.8-messages-awsui0702w-0257

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0702W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a correct return code expression and retry the operation..

**Plataforma / Validação:** Distributed

---

### 493. hwa-10.2.8-messages-awsui0703w-0258

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0703W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a correct return code expression using only boolean operators and retry the operation..

**Plataforma / Validação:** Distributed

---

### 494. hwa-10.2.8-messages-awsui0705w-0259

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0705W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select an alternate plan before performing the restore operation and retry the operation..

**Plataforma / Validação:** Distributed

---

### 495. hwa-10.2.8-messages-awsui0707e-0260

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0707E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select a resource that is defined for the same workstation as the job and retry the operation..

**Plataforma / Validação:** Distributed

---

### 496. hwa-10.2.8-messages-awsui0708e-0261

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0708E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Remove some of the entries in the STDLIST file and retry the operation..

**Plataforma / Validação:** Distributed

---

### 497. hwa-10.2.8-messages-awsui0710w-0262

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0710W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Restore the plan and then change the user password..

**Plataforma / Validação:** Distributed

---

### 498. hwa-10.2.8-messages-awsui0714w-0263

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0714W indica um problema no Dynamic Workload Console: See message. O sistema Processing continues. A acao documentada e: Make sure that all the specified dependencies are correctly defined before the job stream is run..

**Plataforma / Validação:** Distributed

---

### 499. hwa-10.2.8-messages-awsui0720e-0264

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0720E indica um problema no Dynamic Workload Console: A dependency was specified on a resource that does not exist, or the rights of the specifying user are not sufficient to use the resource. The resource might have been removed from the database after the dependency was added. O sistema The requested operation is not completed successfully. A acao documentada e: Remove the resource dependency. Create the resource and recreate the dependency and retry the operation..

**Plataforma / Validação:** Distributed

---

### 500. hwa-10.2.8-messages-awsui0722e-0265

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0722E indica um problema no Dynamic Workload Console: A negative or null number of units for the resource was specified. O sistema The requested operation is not completed successfully. A acao documentada e: Modify the number of units for the specified resource to a positive value less than or equal to the number of units available and retry the operation..

**Plataforma / Validação:** Distributed

---

### 501. hwa-10.2.8-messages-awsui0723w-0266

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0723W indica um problema no Dynamic Workload Console: See message. O sistema Processing continues. A acao documentada e: Select a recognized time zone value, or leave the field blank and retry the operation..

**Plataforma / Validação:** Distributed

---

### 502. hwa-10.2.8-messages-awsui0724w-0267

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0724W indica um problema no Dynamic Workload Console: See message. O sistema Processing continues. A acao documentada e: Select a recognized time zone value and retry the operation..

**Plataforma / Validação:** Distributed

---

### 503. hwa-10.2.8-messages-awsui0726e-0268

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0726E indica um problema no Dynamic Workload Console: The query does not return any results because the date filter is not set correctly. O sistema The requested operation is not completed successfully. A acao documentada e: Set values for both Date and Time fields, or do not set values for either Date or Time fields and retry the query..

**Plataforma / Validação:** Distributed

---

### 504. hwa-10.2.8-messages-awsui0727e-0269

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0727E indica um problema no Dynamic Workload Console: The query does not return any results because the date filter is not set correctly. O sistema The requested operation is not completed successfully. A acao documentada e: Set values both for Time and Date fields, or do not set values for either Date or Time fields and retry the query..

**Plataforma / Validação:** Distributed

---

### 505. hwa-10.2.8-messages-awsui0729e-0270

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0729E indica um problema no Dynamic Workload Console: It is not possible to unlock the object. Some problem has been encountered during this operation. O sistema The requested operation is not completed successfully. A acao documentada e: Refer to the reason indicated in the message to resolve the issue and retry the operation..

**Plataforma / Validação:** Distributed

---

### 506. hwa-10.2.8-messages-awsui0730w-0271

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0730W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Change one or both of the limits to give a valid interval and retry the operation..

**Plataforma / Validação:** Distributed

---

### 507. hwa-10.2.8-messages-awsui0731e-0272

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0731E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Change one or both of the limits to give a valid interval and retry the operation..

**Plataforma / Validação:** Distributed

---

### 508. hwa-10.2.8-messages-awsui0733e-0273

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0733E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a valid name for the Run cycle and retry the operation..

**Plataforma / Validação:** Distributed

---

### 509. hwa-10.2.8-messages-awsui0734e-0274

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0734E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a name for the Run cycle and retry the operation..

**Plataforma / Validação:** Distributed

---

### 510. hwa-10.2.8-messages-awsui0735e-0275

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0735E indica um problema no Dynamic Workload Console: If a job stream is defined in a workstation class, then all of its jobs must be defined either on a workstation, or in the same workstation class. O sistema The requested operation is not completed successfully. A acao documentada e: Set the workstation of this job stream to the original value and retry the operation..

**Plataforma / Validação:** Distributed

---

### 511. hwa-10.2.8-messages-awsui0737e-0276

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0737E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select one or more days in the list in order to specify the Run cycle frequency and retry the operation..

**Plataforma / Validação:** Distributed

---

### 512. hwa-10.2.8-messages-awsui0739e-0277

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0739E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Enter an End date that is later than the Start date or leave the End date blank. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 513. hwa-10.2.8-messages-awsui0741e-0278

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0741E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid number of days in the Offset field and retry the operation..

**Plataforma / Validação:** Distributed

---

### 514. hwa-10.2.8-messages-awsui0742e-0279

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0742E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select another workstation that has Other as its operating system and retry the operation..

**Plataforma / Validação:** Distributed

---

### 515. hwa-10.2.8-messages-awsui0744e-0280

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0744E indica um problema no Dynamic Workload Console: The job could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 516. hwa-10.2.8-messages-awsui0746e-0281

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0746E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid value in the Raise event field and retry the operation..

**Plataforma / Validação:** Distributed

---

### 517. hwa-10.2.8-messages-awsui0747e-0282

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0747E indica um problema no Dynamic Workload Console: There is a problem with Table criteria due to an error in the IBM Workload Scheduler for Applications. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text represents an error code reported by IBM Workload Scheduler for Applications. Resolve the error and retry the operation. IBM Workload Scheduler for Applications User's Guide for information about the error message..

**Plataforma / Validação:** Distributed

---

### 518. hwa-10.2.8-messages-awsui0748e-0283

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0748E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Choose another action, or upgrade to a supported level of XBP and retry the operation..

**Plataforma / Validação:** Distributed

---

### 519. hwa-10.2.8-messages-awsui0751e-0284

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0751E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Fix the problem indicated in the error message and retry the operation..

**Plataforma / Validação:** Distributed

---

### 520. hwa-10.2.8-messages-awsui0753w-0285

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0753W indica um problema no Dynamic Workload Console: The selected job definition is used by one or more job streams. Verify that these job streams are defined on the same workstation class O sistema If OK is clicked, the job definition is saved. If cancel is clicked the save action is ignored. A acao documentada e: Click OK to submit or click Cancel to cancel the submit action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 521. hwa-10.2.8-messages-awsui0762e-0286

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0762E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Change the name of the task. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 522. hwa-10.2.8-messages-awsui0766e-0287

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0766E indica um problema no Dynamic Workload Console: The network might be down or the connection credentials might not be correct. O sistema The requested operation is not completed successfully. A acao documentada e: Check the engine properties and the credentials specified. Correct any problem you find and retry the operation..

**Plataforma / Validação:** Distributed

---

### 523. hwa-10.2.8-messages-awsui0769e-0288

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0769E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: You can share your own tasks only. Create another task or duplicate the previous task and share it..

**Plataforma / Validação:** Distributed

---

### 524. hwa-10.2.8-messages-awsui0770e-0289

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0770E indica um problema no Dynamic Workload Console: See message. O sistema The duplicate operation was not performed. No task was created. A acao documentada e: An internal problem prevents the task from being duplicated. Create the new task manually..

**Plataforma / Validação:** Distributed

---

### 525. hwa-10.2.8-messages-awsui0772e-0290

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0772E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a different task name and retry the operation..

**Plataforma / Validação:** Distributed

---

### 526. hwa-10.2.8-messages-awsui0773e-0291

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0773E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid value using only the permitted characters and retry the operation..

**Plataforma / Validação:** Distributed

---

### 527. hwa-10.2.8-messages-awsui0774e-0292

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0774E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a To priority greater than the From priority and retry the operation..

**Plataforma / Validação:** Distributed

---

### 528. hwa-10.2.8-messages-awsui0779e-0293

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0779E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Check that the engine is available (try pinging it). Check the engine connection credentials. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 529. hwa-10.2.8-messages-awsui0780e-0294

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0780E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Check with the IBM Workload Scheduler administrator that the engine is running. When the problem is fixed retry the operation..

**Plataforma / Validação:** Distributed

---

### 530. hwa-10.2.8-messages-awsui0782e-0295

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0782E indica um problema no Dynamic Workload Console: The selected engine has been shared by another user. O sistema The engine was not modified. A acao documentada e: Create another engine and share it..

**Plataforma / Validação:** Distributed

---

### 531. hwa-10.2.8-messages-awsui0783e-0296

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0783E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify another engine..

**Plataforma / Validação:** Distributed

---

### 532. hwa-10.2.8-messages-awsui0785e-0297

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0785E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure only one item is selected in the list or table and retry the operation..

**Plataforma / Validação:** Distributed

---

### 533. hwa-10.2.8-messages-awsui0786e-0298

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0786E indica um problema no Dynamic Workload Console: You tried to perform an action on multiple items, but some or all of the selected items do not support the specified action. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that all the selected items are compatible with the specified action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 534. hwa-10.2.8-messages-awsui0788e-0299

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0788E indica um problema no Dynamic Workload Console: You tried to perform an action on multiple items, but some of them do not support that action. O sistema The requested operation is not completed successfully. A acao documentada e: Deselect the items not compatible with the action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 535. hwa-10.2.8-messages-awsui0791e-0300

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0791E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Use the error message to determine what the problem is. Fix the problem and retry the operation..

**Plataforma / Validação:** Distributed

---

### 536. hwa-10.2.8-messages-awsui0792e-0301

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0792E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Request the owner of the items to share or unshare them..

**Plataforma / Validação:** Distributed

---

### 537. hwa-10.2.8-messages-awsui0794e-0302

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0794E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Ask the IBM Workload Scheduler administrator to grant the user the appropriate permissions to perform the required action on the selected plan object. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 538. hwa-10.2.8-messages-awsui0795e-0303

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0795E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Ensure that the IBM Workload Scheduler engine is available in the network (try pinging it) and is up and running. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 539. hwa-10.2.8-messages-awsui0797e-0304

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0797E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully for the items not owned by the user. A acao documentada e: Ask the owner of the items to share or unshare them and retry the operation..

**Plataforma / Validação:** Distributed

---

### 540. hwa-10.2.8-messages-awsui0798e-0305

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0798E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select another engine, and retry the action..

**Plataforma / Validação:** Distributed

---

### 541. hwa-10.2.8-messages-awsui0801e-0306

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0801E indica um problema no Dynamic Workload Console: You attempted to test the database connection or to run a report task to an engine that does not support the reporting. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports reporting..

**Plataforma / Validação:** Distributed

---

### 542. hwa-10.2.8-messages-awsui0803w-0307

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0803W indica um problema no Dynamic Workload Console: You have tested the connection to the indicated engine. The engine connection is working correctly but the database could not be accessed. O sistema The requested operation is not completed successfully. A acao documentada e: Ask the IBM Workload Scheduler administrator to resolve the problem with the access to the database for the indicated engine. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 543. hwa-10.2.8-messages-awsui0804e-0308

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0804E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully on the indicated items. A acao documentada e: Make sure only one item is selected in the list or table and retry the operation..

**Plataforma / Validação:** Distributed

---

### 544. hwa-10.2.8-messages-awsui0808e-0309

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0808E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Set the current plan to be the default plan. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 545. hwa-10.2.8-messages-awsui0809e-0310

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0809E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Complete the Engine Connection properties panel with the Database User ID and Password. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 546. hwa-10.2.8-messages-awsui0810e-0311

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0810E indica um problema no Dynamic Workload Console: The selected item has been shared by another user. O sistema The requested operation is not completed successfully. A acao documentada e: Choose an object you own to delete..

**Plataforma / Validação:** Distributed

---

### 547. hwa-10.2.8-messages-awsui0818e-0312

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0818E indica um problema no Dynamic Workload Console: You have tried to change a workstation to become the master domain manager. As there can only be one master domain manager at any given time, the program must first change the definition of the existing master domain manager to remove the manager attribute. However it could not find the existing master domain manager definition. Perhaps someone else has performed the same action at the same time. O sistema The requested operation is not completed successfully. A acao documentada e: Check the workstation definitions for the master domain and determine which workstation is the manager. Determine why the problem occurred and whether you still need to change the workstation to become the master domain manager. If so, retry the operation..

**Plataforma / Validação:** Distributed

---

### 548. hwa-10.2.8-messages-awsui0819w-0313

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0819W indica um problema no Dynamic Workload Console: You have tried to set this workstation as the master domain manager, but it already is. O sistema The requested operation is not completed successfully. A acao documentada e: None..

**Plataforma / Validação:** Distributed

---

### 549. hwa-10.2.8-messages-awsui0822e-0314

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0822E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Remove the non-valid characters from the value. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 550. hwa-10.2.8-messages-awsui0823e-0315

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0823E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Remove non-alphanumeric characters and spaces. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 551. hwa-10.2.8-messages-awsui0824e-0316

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0824E indica um problema no Dynamic Workload Console: See message. O sistema The SAP task is not submitted. A acao documentada e: Verify the task information is correct. If a command string was supplied, verify also that it is correct. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 552. hwa-10.2.8-messages-awsui0826w-0317

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0826W indica um problema no Dynamic Workload Console: See message. O sistema The plan is not created. A acao documentada e: Create an engine connection. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 553. hwa-10.2.8-messages-awsui0829w-0318

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0829W indica um problema no Dynamic Workload Console: You have tried to start the event processor but it is already up and running. O sistema Nothing. The system continues. A acao documentada e: None..

**Plataforma / Validação:** Distributed

---

### 554. hwa-10.2.8-messages-awsui0830w-0319

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0830W indica um problema no Dynamic Workload Console: You have tried to stop the event processor but it is already stopped. O sistema Nothing. The system continues. A acao documentada e: None..

**Plataforma / Validação:** Distributed

---

### 555. hwa-10.2.8-messages-awsui0831e-0320

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0831E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Verify that the plan name is correct in the report task. Correct the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 556. hwa-10.2.8-messages-awsui0833e-0321

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0833E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Use the information in the quoted error message to diagnose and correct the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 557. hwa-10.2.8-messages-awsui0834e-0322

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0834E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select a single job stream instance by specifying either the job stream ID or the scheduled start time. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 558. hwa-10.2.8-messages-awsui0836e-0323

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0836E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid value in the Name field and all other mandatory fields and retry the operation..

**Plataforma / Validação:** Distributed

---

### 559. hwa-10.2.8-messages-awsui0837e-0324

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0837E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a valid value within the indicated range. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 560. hwa-10.2.8-messages-awsui0838e-0325

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0838E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Supply a value for either the Target server or the Server group, but not both. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 561. hwa-10.2.8-messages-awsui0843e-0326

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0843E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler without specifying any action in the URL. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying an action..

**Plataforma / Validação:** Distributed

---

### 562. hwa-10.2.8-messages-awsui0844e-0327

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0844E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with invalid parameters. O sistema The IBM Workload Scheduler has not been not launched. A acao documentada e: Check the documentation to ensure that you have correctly typed the parameters..

**Plataforma / Validação:** Distributed

---

### 563. hwa-10.2.8-messages-awsui0846e-0328

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0846E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with an invalid status value. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying a valid status..

**Plataforma / Validação:** Distributed

---

### 564. hwa-10.2.8-messages-awsui0847e-0329

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0847E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with an invalid column parameter. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying a valid value for the column parameter, valid values are “”min“” or “”all“”..

**Plataforma / Validação:** Distributed

---

### 565. hwa-10.2.8-messages-awsui0875e-0330

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0875E indica um problema no Dynamic Workload Console: You have tried to launch an operation not applicable on the selected tasks. O sistema The operation has not been launched. A acao documentada e: Launch the operation on a valid task..

**Plataforma / Validação:** Distributed

---

### 566. hwa-10.2.8-messages-awsui0877e-0331

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0877E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the Workload Service Assurance feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports Workload Service Assurance..

**Plataforma / Validação:** Distributed

---

### 567. hwa-10.2.8-messages-awsui0883e-0332

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0883E indica um problema no Dynamic Workload Console: See message. O sistema The same data that was available before the refresh request is displayed. A acao documentada e: Refer to the mentioned error message to diagnose and correct the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 568. hwa-10.2.8-messages-awsui0886e-0333

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0886E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Verify that there are plans in the specified time range. Correct the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 569. hwa-10.2.8-messages-awsui0888w-0334

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0888W indica um problema no Dynamic Workload Console: Variable Tables are supported from version 8.5. If you selected an engine of an older version, the specified variable table value is ignored. O sistema Processing continues, ignoring the “”variable table“” field. A acao documentada e: No action is required. To avoid this warning message in the future, do not specify a value in the “”variable table“” field for engine versions prior to version 8.5..

**Plataforma / Validação:** Distributed

---

### 570. hwa-10.2.8-messages-awsui0893e-0335

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0893E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Contact Software Support for assistance..

**Plataforma / Validação:** Distributed

---

### 571. hwa-10.2.8-messages-awsui0894e-0336

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0894E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Contact Software Support for assistance..

**Plataforma / Validação:** Distributed

---

### 572. hwa-10.2.8-messages-awsui0898e-0337

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0898E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a valid regular expression. Check on the documentation for the supported regular expressions..

**Plataforma / Validação:** Distributed

---

### 573. hwa-10.2.8-messages-awsui0899e-0338

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0899E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a valid interval..

**Plataforma / Validação:** Distributed

---

### 574. hwa-10.2.8-messages-awsui0900e-0339

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0900E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a valid interval..

**Plataforma / Validação:** Distributed

---

### 575. hwa-10.2.8-messages-awsui0901e-0340

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0901E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Use the information in the quoted error message to diagnose and correct the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 576. hwa-10.2.8-messages-awsui0903w-0341

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0903W indica um problema no Dynamic Workload Console: See text. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that status of the selected workstation is compatible with the specified action and retry the operation..

**Plataforma / Validação:** Distributed

---

### 577. hwa-10.2.8-messages-awsui0904w-0342

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0904W indica um problema no Dynamic Workload Console: The workstation type “”Workload Broker“” is supported startingfrom version 8.5. If you selected an engine with a previous version, the operation is interrupted. O sistema Processing is interrupted. A acao documentada e: Specify a different workstation type if the selected engine version is prior to version 8.5..

**Plataforma / Validação:** Distributed

---

### 578. hwa-10.2.8-messages-awsui0906w-0343

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0906W indica um problema no Dynamic Workload Console: For security and auditability reasons, when an engine connection is shared to other users, the associated engine credentials are not shared. This message is presented when the default settings are overridden, for you to confirm the choice. O sistema If operator answers “”Yes“” the engine credentials will be shared along with the other engine properties. A acao documentada e: Answer “”Yes“” to allow sharing of engine credentials, or “”No“” to go back. This choice can be changed at any time by editing the engine properties..

**Plataforma / Validação:** Distributed

---

### 579. hwa-10.2.8-messages-awsui0907e-0344

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0907E indica um problema no Dynamic Workload Console: You attempted to run an operation using an old version of the connector for z/OS that does not support the Conditional logic feature. O sistema The requested operation is not completed successfully. A acao documentada e: You should upgrade your connector for z/OS to have all the new features available..

**Plataforma / Validação:** Distributed

---

### 580. hwa-10.2.8-messages-awsui0913w-0345

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0913W indica um problema no Dynamic Workload Console: User name and password are required to perform this operation. O sistema The requested operation is not completed successfully. A acao documentada e: Specify valid user and password values..

**Plataforma / Validação:** Distributed

---

### 581. hwa-10.2.8-messages-awsui0914e-0346

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0914E indica um problema no Dynamic Workload Console: You attempted run a plan view on an engine that does not support it. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports plan view..

**Plataforma / Validação:** Distributed

---

### 582. hwa-10.2.8-messages-awsui0916e-0347

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0916E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the Virtual workstation creation feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports Virtual workstation creation..

**Plataforma / Validação:** Distributed

---

### 583. hwa-10.2.8-messages-awsui0917e-0348

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0917E indica um problema no Dynamic Workload Console: You attempted to run an operation using an old version of the connector for z/OS that does not support the Virtual workstation creation feature. O sistema The requested operation is not completed successfully. A acao documentada e: You should upgrade your connector for z/OS to have all the new features available..

**Plataforma / Validação:** Distributed

---

### 584. hwa-10.2.8-messages-awsui0918e-0349

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0918E indica um problema no Dynamic Workload Console: The task you tried to run does not exit or has been deleted. O sistema The requested operation is not completed successfully. A acao documentada e: Replace this bookmark with a valid one that links an existing task..

**Plataforma / Validação:** Distributed

---

### 585. hwa-10.2.8-messages-awsui0920e-0350

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0920E indica um problema no Dynamic Workload Console: The specified object documentation url is invalid. O sistema The requested operation is not completed successfully. A acao documentada e: Change the documentation url and specify a valid url in the TdwcGlobalSettings.xml file..

**Plataforma / Validação:** Distributed

---

### 586. hwa-10.2.8-messages-awsui0921e-0351

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0921E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you have sufficient permission and that the object was not deleted..

**Plataforma / Validação:** Distributed

---

### 587. hwa-10.2.8-messages-awsui0922e-0352

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0922E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you selected only one “”Monitor task on Multiple Engines“” task before runniong View as Report action..

**Plataforma / Validação:** Distributed

---

### 588. hwa-10.2.8-messages-awsui0923e-0353

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0923E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: The file you are trying to upload it is not valid. Check file type and file size..

**Plataforma / Validação:** Distributed

---

### 589. hwa-10.2.8-messages-awsui0928e-0354

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0928E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Database was not successfully initialized. Be sure database is reachable, and user has enough permission to drop and create tables..

**Plataforma / Validação:** Distributed

---

### 590. hwa-10.2.8-messages-awsui0930e-0355

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0930E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: It was not possible to connect to database. Check database connection parameters, if correct, check if the RDBMS is reachable from the system in which the TDWC is installed..

**Plataforma / Validação:** Distributed

---

### 591. hwa-10.2.8-messages-awsui0937e-0356

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0937E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: It was not possible to use the database. The database must be initialized from the Manage settings portlet either by an import with recreate option, or in Configure settings repository section..

**Plataforma / Validação:** Distributed

---

### 592. hwa-10.2.8-messages-awsui0939e-0357

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0939E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Select less items from the list or table and retry the operation..

**Plataforma / Validação:** Distributed

---

### 593. hwa-10.2.8-messages-awsui0940e-0358

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0940E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Choose another action, or upgrade to a supported level of XBP and retry the operation..

**Plataforma / Validação:** Distributed

---

### 594. hwa-10.2.8-messages-awsui0943e-0359

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0943E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the User Fields feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports User Fields..

**Plataforma / Validação:** Distributed

---

### 595. hwa-10.2.8-messages-awsui0945e-0360

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0945E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Database was not successfully updated. Be sure database is reachable, and user has enough permission to create tables..

**Plataforma / Validação:** Distributed

---

### 596. hwa-10.2.8-messages-awsui0947e-0361

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0947E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Define at least one step inside the R3 Standard Job you want to create..

**Plataforma / Validação:** Distributed

---

### 597. hwa-10.2.8-messages-awsui0958e-0362

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0958E indica um problema no Dynamic Workload Console: The selected prompt could not be replied to due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 598. hwa-10.2.8-messages-awsui0959w-0363

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0959W indica um problema no Dynamic Workload Console: One or more filters are not supported with the current IBM Workload Scheduler engine version. The unsupported filters has been ignored. O sistema The query has been completed, but a specified filter has been ignored. A acao documentada e: Remove the indicated filter from the task..

**Plataforma / Validação:** Distributed

---

### 599. hwa-10.2.8-messages-awsui0975e-0364

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0975E indica um problema no Dynamic Workload Console: System action: O sistema Operator response: A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

---

### 600. hwa-10.2.8-messages-awsui2000e-0365

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2000E indica um problema no Dynamic Workload Console: There is a connection problem with the database. Possible errors are: • The database is down • The database password provided when the engine was created is wrong or has been changed. O sistema The requested operation is not completed successfully. A acao documentada e: Check the error log and trace files for the possible cause of the problem. Check that the database is up and that the connection credentials are correct. Correct the problem and retry the operation..

**Plataforma / Validação:** Distributed

---

### 601. hwa-10.2.8-messages-awsui2006e-0366

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2006E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Use the listed errors to determine what problems have occurred, fix them, and retry the operation..

**Plataforma / Validação:** Distributed

---

### 602. hwa-10.2.8-messages-awsui2007e-0367

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2007E indica um problema no Dynamic Workload Console: The report could not be produced due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

---

### 603. hwa-10.2.8-messages-awsui2009e-0368

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2009E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Check the error log and trace files for the possible cause of the problem. Correct the problem and retry the operation..

**Plataforma / Validação:** Distributed

---

### 604. hwa-10.2.8-messages-awsui2010w-0369

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2010W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed successfully. A acao documentada e: Specify a different filter to reduce the number of items returned by the query..

**Plataforma / Validação:** Distributed

---

### 605. hwa-10.2.8-messages-awsui3052e-0370

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3052E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a value between 30 and 7200, inclusive..

**Plataforma / Validação:** Distributed

---

### 606. hwa-10.2.8-messages-awsui3053e-0371

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3053E indica um problema no Dynamic Workload Console: The problem can be due to possible communication problems with IBM Workload Scheduler engine or with SAP. Alternatively, the Dynamic Workload Console may not be able to process the output supplied by R3Batch process because not available or corrupted. See message. O sistema No information about the selected process chain is retrieved. The requested action was not completed successfully. A acao documentada e: Ensure there is no connection problem with the engine and with SAP. Ensure SAP system is up and running. Check the trace.log file for more details about the error..

**Plataforma / Validação:** Distributed

---

### 607. hwa-10.2.8-messages-awsui3055e-0372

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3055E indica um problema no Dynamic Workload Console: The objectType cannot be created or update or delete or read in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 608. hwa-10.2.8-messages-awsui3057e-0373

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3057E indica um problema no Dynamic Workload Console: An Access Method and a Host must be specified for the Extended Agent. O sistema The workstation is not created. A acao documentada e: Specify an Access Method and an Host workstation name for the Extended Agent..

**Plataforma / Validação:** Distributed

---

### 609. hwa-10.2.8-messages-awsui3058e-0374

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3058E indica um problema no Dynamic Workload Console: A Domain must be specified for the workstation. O sistema The workstation is not created. A acao documentada e: Specify a Domain for the workstation..

**Plataforma / Validação:** Distributed

---

### 610. hwa-10.2.8-messages-awsui3059e-0375

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3059E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a name that conforms to the indicated naming rules..

**Plataforma / Validação:** Distributed

---

### 611. hwa-10.2.8-messages-awsui3069e-0376

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3069E indica um problema no Dynamic Workload Console: The workstation has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 612. hwa-10.2.8-messages-awsui3070e-0377

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3070E indica um problema no Dynamic Workload Console: The domain has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 613. hwa-10.2.8-messages-awsui3071e-0378

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3071E indica um problema no Dynamic Workload Console: The workstation has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 614. hwa-10.2.8-messages-awsui3074e-0379

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3074E indica um problema no Dynamic Workload Console: The workstation cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 615. hwa-10.2.8-messages-awsui3075e-0380

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3075E indica um problema no Dynamic Workload Console: The domain cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 616. hwa-10.2.8-messages-awsui3077e-0381

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3077E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply the correct name for the variable table. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 617. hwa-10.2.8-messages-awsui3086e-0382

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3086E indica um problema no Dynamic Workload Console: The job stream has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 618. hwa-10.2.8-messages-awsui3088e-0383

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3088E indica um problema no Dynamic Workload Console: The job stream cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 619. hwa-10.2.8-messages-awsui3089e-0384

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3089E indica um problema no Dynamic Workload Console: The job definition has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 620. hwa-10.2.8-messages-awsui3090e-0385

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3090E indica um problema no Dynamic Workload Console: The job definition has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 621. hwa-10.2.8-messages-awsui3092e-0386

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3092E indica um problema no Dynamic Workload Console: The master domain cannot be retrieved. O sistema The requested action was not completed successfully. A acao documentada e: Verify that the engine connection is working and that the operator is authorized to retrieve this information. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 622. hwa-10.2.8-messages-awsui3093e-0387

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3093E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a combined length less or equal the maximum allowed length..

**Plataforma / Validação:** Distributed

---

### 623. hwa-10.2.8-messages-awsui3094e-0388

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3094E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

---

### 624. hwa-10.2.8-messages-awsui3098e-0389

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3098E indica um problema no Dynamic Workload Console: You are saving a condition without defining any condition dependencies O sistema The requested action was not completed successfully. A acao documentada e: Add a condition dependency or press Cancel.

**Plataforma / Validação:** Distributed

---

### 625. hwa-10.2.8-messages-awsui3100e-0390

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3100E indica um problema no Dynamic Workload Console: The first value in the range must be lower than the second value. O sistema The requested action was not completed successfully. A acao documentada e: Specify a correct range or press Cancel..

**Plataforma / Validação:** Distributed

---

### 626. hwa-10.2.8-messages-awsui3101e-0391

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3101E indica um problema no Dynamic Workload Console: You cannot specify the “”Not equal to“” operator with an intermediate status, such as “”Started“”. O sistema The requested action was not completed successfully. A acao documentada e: Change either the operator or status values to form a valid combination..

**Plataforma / Validação:** Distributed

---

### 627. hwa-10.2.8-messages-awsui3105e-0392

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3105E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Specify an end time that is later than the start time. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 628. hwa-10.2.8-messages-awsui3106e-0393

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3106E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Enter a valid value: for distributed engines: alphanumeric; for z/OS engine: numeric (0-255); for mixed engines: the field must be left blank ..

**Plataforma / Validação:** Distributed

---

### 629. hwa-10.2.8-messages-awsui3107e-0394

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3107E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: To define a valid task at least one engine must be selected..

**Plataforma / Validação:** Distributed

---

### 630. hwa-10.2.8-messages-awsui3110e-0395

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3110E indica um problema no Dynamic Workload Console: Kill and Job Log actions are not permitted on a Shadow Job O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

---

### 631. hwa-10.2.8-messages-awsui3111e-0396

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3111E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Enter the name of the dynamic pool meeting the resource requirements associated to this workstation..

**Plataforma / Validação:** Distributed

---

### 632. hwa-10.2.8-messages-awsui3112e-0397

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3112E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Enter the name of the pool of dynamic agents associated to this workstation..

**Plataforma / Validação:** Distributed

---

### 633. hwa-10.2.8-messages-awsui3117e-0398

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3117E indica um problema no Dynamic Workload Console: The engine connection version does not support this object type. O sistema The requested action was not completed successfully. A acao documentada e: Use a later version engine connection that supports the object type.

**Plataforma / Validação:** Distributed

---

### 634. hwa-10.2.8-messages-awsui3121e-0399

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3121E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: See message..

**Plataforma / Validação:** Distributed

---

### 635. hwa-10.2.8-messages-awsui3122e-0400

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3122E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Supply a value within the accepted range. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 636. hwa-10.2.8-messages-awsui3124e-0401

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3124E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: Enter an integer..

**Plataforma / Validação:** Distributed

---

### 637. hwa-10.2.8-messages-awsui3126w-0402

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3126W indica um problema no Dynamic Workload Console: Multiple engine tasks can be run against Current plan only O sistema None A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

---

### 638. hwa-10.2.8-messages-awsui3130e-0403

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3130E indica um problema no Dynamic Workload Console: The update can be performed on a predefined number of workstations at a time. O sistema The operation is not performed. A acao documentada e: To update more workstations, browse to the TdwcGlobalSettings.xml file and specify the number of workstations in the updateWorkstationMaxNumber property..

**Plataforma / Validação:** Distributed

---

### 639. hwa-10.2.8-messages-awsui3131e-0404

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3131E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: See message..

**Plataforma / Validação:** Distributed

---

### 640. hwa-10.2.8-messages-awsui3133e-0405

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3133E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: See message..

**Plataforma / Validação:** Distributed

---

### 641. hwa-10.2.8-messages-awsui3134e-0406

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3134E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: See message..

**Plataforma / Validação:** Distributed

---

### 642. hwa-10.2.8-messages-awsui3135e-0407

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3135E indica um problema no Dynamic Workload Console: See message. O sistema The requested action was not completed successfully. A acao documentada e: See message..

**Plataforma / Validação:** Distributed

---

### 643. hwa-10.2.8-messages-awsui4100e-0408

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4100E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 644. hwa-10.2.8-messages-awsui4104e-0409

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4104E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 645. hwa-10.2.8-messages-awsui4105e-0410

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4105E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 646. hwa-10.2.8-messages-awsui4106e-0411

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4106E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 647. hwa-10.2.8-messages-awsui4107e-0412

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4107E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 648. hwa-10.2.8-messages-awsui4109e-0413

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4109E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 649. hwa-10.2.8-messages-awsui4110e-0414

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4110E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 650. hwa-10.2.8-messages-awsui4111e-0415

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4111E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 651. hwa-10.2.8-messages-awsui4112e-0416

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4112E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 652. hwa-10.2.8-messages-awsui4113e-0417

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4113E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 653. hwa-10.2.8-messages-awsui4114e-0418

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4114E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 654. hwa-10.2.8-messages-awsui4116e-0419

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4116E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 655. hwa-10.2.8-messages-awsui4117e-0420

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4117E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 656. hwa-10.2.8-messages-awsui4118e-0421

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4118E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 657. hwa-10.2.8-messages-awsui4119e-0422

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4119E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 658. hwa-10.2.8-messages-awsui4120e-0423

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4120E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 659. hwa-10.2.8-messages-awsui4121e-0424

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4121E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 660. hwa-10.2.8-messages-awsui4123e-0425

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4123E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 661. hwa-10.2.8-messages-awsui4124e-0426

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4124E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 662. hwa-10.2.8-messages-awsui4125e-0427

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4125E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 663. hwa-10.2.8-messages-awsui4126e-0428

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4126E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 664. hwa-10.2.8-messages-awsui4127e-0429

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4127E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 665. hwa-10.2.8-messages-awsui4128e-0430

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4128E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 666. hwa-10.2.8-messages-awsui4130e-0431

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4130E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 667. hwa-10.2.8-messages-awsui4131e-0432

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4131E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 668. hwa-10.2.8-messages-awsui4132e-0433

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4132E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 669. hwa-10.2.8-messages-awsui4133e-0434

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4133E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 670. hwa-10.2.8-messages-awsui4134e-0435

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4134E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 671. hwa-10.2.8-messages-awsui4136e-0436

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4136E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 672. hwa-10.2.8-messages-awsui4164e-0437

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4164E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 673. hwa-10.2.8-messages-awsui4173e-0438

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI4173E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 674. hwa-10.2.8-messages-awsui5002e-0439

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5002E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a valid value..

**Plataforma / Validação:** Distributed

---

### 675. hwa-10.2.8-messages-awsui5003e-0440

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5003E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter all the required values..

**Plataforma / Validação:** Distributed

---

### 676. hwa-10.2.8-messages-awsui5004e-0441

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5004E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a longer value..

**Plataforma / Validação:** Distributed

---

### 677. hwa-10.2.8-messages-awsui5006e-0442

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5006E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a value between 0 and 100..

**Plataforma / Validação:** Distributed

---

### 678. hwa-10.2.8-messages-awsui5007e-0443

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5007E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 679. hwa-10.2.8-messages-awsui5008e-0444

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5008E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 680. hwa-10.2.8-messages-awsui5009e-0445

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5009E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Provide a new value, ensuring it is supported..

**Plataforma / Validação:** Distributed

---

### 681. hwa-10.2.8-messages-awsui5010e-0446

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5010E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 682. hwa-10.2.8-messages-awsui5011e-0447

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5011E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 683. hwa-10.2.8-messages-awsui5013e-0448

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5013E indica um problema no Dynamic Workload Console: Unable to calculate the available correlation properties on the current events. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 684. hwa-10.2.8-messages-awsui5014e-0449

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5014E indica um problema no Dynamic Workload Console: Unable to execute an Heart Beat to keep the session up. O sistema The session is not kept up A acao documentada e: Close current session and start a new one.

**Plataforma / Validação:** Distributed

---

### 685. hwa-10.2.8-messages-awsui5015e-0450

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5015E indica um problema no Dynamic Workload Console: The Rule Editor cannot be opened. O sistema none A acao documentada e: Ensure that the connection to the server is working properly..

**Plataforma / Validação:** Distributed

---

### 686. hwa-10.2.8-messages-awsui5016e-0451

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5016E indica um problema no Dynamic Workload Console: The Rule Editor cannot be closed. O sistema none A acao documentada e: Ensure that the connection to the server is working properly..

**Plataforma / Validação:** Distributed

---

### 687. hwa-10.2.8-messages-awsui5018e-0452

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5018E indica um problema no Dynamic Workload Console: This message is displayed when a not specific internal error occurs. O sistema No change happens in the event rule. A acao documentada e: Close Rule Editor panel, reopen it and try to process the rule again..

**Plataforma / Validação:** Distributed

---

### 688. hwa-10.2.8-messages-awsui5019e-0453

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5019E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while adding an action to the action area. O sistema The action is not added or stored in the event rule. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 689. hwa-10.2.8-messages-awsui5020e-0454

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5020E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while removing an action from the action's area. O sistema The action is not removed from the event rule. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 690. hwa-10.2.8-messages-awsui5021e-0455

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5021E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while adding an event to the event's area. O sistema The event is not added or stored in the event rule. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 691. hwa-10.2.8-messages-awsui5023e-0456

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5023E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while ordering an event in sequence with others. O sistema The event has not been moved. A acao documentada e: Specify a different event sequence..

**Plataforma / Validação:** Distributed

---

### 692. hwa-10.2.8-messages-awsui5024e-0457

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5024E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while changing the event type (filter, set, sequence). O sistema The event type is not changed A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 693. hwa-10.2.8-messages-awsui5025e-0458

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5025E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Type a different name using only supported characters..

**Plataforma / Validação:** Distributed

---

### 694. hwa-10.2.8-messages-awsui5027e-0459

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5027E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide a shorter name..

**Plataforma / Validação:** Distributed

---

### 695. hwa-10.2.8-messages-awsui5028e-0460

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5028E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide a rule name..

**Plataforma / Validação:** Distributed

---

### 696. hwa-10.2.8-messages-awsui5029e-0461

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5029E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema The event rule cannot be saved. A acao documentada e: Provide date and time values..

**Plataforma / Validação:** Distributed

---

### 697. hwa-10.2.8-messages-awsui5030e-0462

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5030E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema The event rule cannot be saved. A acao documentada e: Provide a valid date value..

**Plataforma / Validação:** Distributed

---

### 698. hwa-10.2.8-messages-awsui5031e-0463

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5031E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide date and time values..

**Plataforma / Validação:** Distributed

---

### 699. hwa-10.2.8-messages-awsui5032e-0464

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5032E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide a shorter description..

**Plataforma / Validação:** Distributed

---

### 700. hwa-10.2.8-messages-awsui5033e-0465

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5033E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide a valid validity period..

**Plataforma / Validação:** Distributed

---

### 701. hwa-10.2.8-messages-awsui5035e-0466

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5035E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Make a selection..

**Plataforma / Validação:** Distributed

---

### 702. hwa-10.2.8-messages-awsui5036e-0467

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5036E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Select a value or more..

**Plataforma / Validação:** Distributed

---

### 703. hwa-10.2.8-messages-awsui5037e-0468

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5037E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved. A acao documentada e: Provide a valid time value..

**Plataforma / Validação:** Distributed

---

### 704. hwa-10.2.8-messages-awsui5038e-0469

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5038E indica um problema no Dynamic Workload Console: There is an error in some field of the Rule Editor. The event rule cannot be saved. O sistema The event rule cannot be saved and the button SAVE is disabled. A acao documentada e: Fix the errors and proceed..

**Plataforma / Validação:** Distributed

---

### 705. hwa-10.2.8-messages-awsui5039w-0470

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5039W indica um problema no Dynamic Workload Console: See message text. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 706. hwa-10.2.8-messages-awsui5041e-0471

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5041E indica um problema no Dynamic Workload Console: See message text. O sistema The search has failed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 707. hwa-10.2.8-messages-awsui5043e-0472

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5043E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved and the button SAVE is disabled. A acao documentada e: Specify a rule name and save the rule again..

**Plataforma / Validação:** Distributed

---

### 708. hwa-10.2.8-messages-awsui5044e-0473

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5044E indica um problema no Dynamic Workload Console: See message text. O sistema The event rule cannot be saved and the button SAVE is disabled. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 709. hwa-10.2.8-messages-awsui5045e-0474

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5045E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 710. hwa-10.2.8-messages-awsui5046w-0475

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5046W indica um problema no Dynamic Workload Console: See message text. O sistema none A acao documentada e: Specify an engine connection..

**Plataforma / Validação:** Distributed

---

### 711. hwa-10.2.8-messages-awsui5047e-0476

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5047E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 712. hwa-10.2.8-messages-awsui5049e-0477

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5049E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 713. hwa-10.2.8-messages-awsui5051e-0478

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5051E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 714. hwa-10.2.8-messages-awsui5052e-0479

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5052E indica um problema no Dynamic Workload Console: See message text. O sistema none A acao documentada e: Specify the correct credentials to access the IBM Workload Scheduler engine..

**Plataforma / Validação:** Distributed

---

### 715. hwa-10.2.8-messages-awsui5053e-0480

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5053E indica um problema no Dynamic Workload Console: See message text. O sistema The operation is not performed. A acao documentada e: If you have modified the plug-in, check that you have saved it with the correct name and path. Correct any error you find and repeat the operation..

**Plataforma / Validação:** Distributed

---

### 716. hwa-10.2.8-messages-awsui5055e-0481

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5055E indica um problema no Dynamic Workload Console: See message text. O sistema Unable to open the Event Rule Editor. A acao documentada e: If you have modified the plug-in, check that you have saved it with the correct name and path. Correct any error you find and repeat the operation..

**Plataforma / Validação:** Distributed

---

### 717. hwa-10.2.8-messages-awsui5056e-0482

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5056E indica um problema no Dynamic Workload Console: See message text. O sistema Unable to open the Event Rule Editor. A acao documentada e: If you have modified the plug-in, check that you have saved it with the correct name and path. Correct any error you find and repeat the operation..

**Plataforma / Validação:** Distributed

---

### 718. hwa-10.2.8-messages-awsui6000e-0483

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6000E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 719. hwa-10.2.8-messages-awsui6002e-0484

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6002E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Provide the user ID and password in the engine configuration and try again..

**Plataforma / Validação:** Distributed

---

### 720. hwa-10.2.8-messages-awsui6003e-0485

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6003E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Check the user ID and password in the engine configuration, correct the error, and try again..

**Plataforma / Validação:** Distributed

---

### 721. hwa-10.2.8-messages-awsui6004e-0486

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6004E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify another authorized user or ask the IBM Workload Scheduler administrator to grant the user specified in the engine configuration the rights to perform the selected operation..

**Plataforma / Validação:** Distributed

---

### 722. hwa-10.2.8-messages-awsui6006w-0487

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6006W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 723. hwa-10.2.8-messages-awsui6007e-0488

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6007E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 724. hwa-10.2.8-messages-awsui6008e-0489

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6008E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: You have not enough permission to execute the operation. Contact the administrator..

**Plataforma / Validação:** Distributed

---

### 725. hwa-10.2.8-messages-awsui6010e-0490

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6010E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: The runcycle has no calendar. Specify a calendar name to resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 726. hwa-10.2.8-messages-awsui6011e-0491

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6011E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: The default calendar specified on the jobstream has not found. Change the calendar name to resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 727. hwa-10.2.8-messages-awsui6012e-0492

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6012E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Error during lookup of workstation. Specify another workstation to resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 728. hwa-10.2.8-messages-awsui6013e-0493

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6013E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify a workstation name to resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 729. hwa-10.2.8-messages-awsui6015w-0494

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6015W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 730. hwa-10.2.8-messages-awsui6016w-0495

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6016W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 731. hwa-10.2.8-messages-awsui6017w-0496

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6017W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 732. hwa-10.2.8-messages-awsui6019e-0497

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6019E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Add at least a job to selected Jobstream or define it as a “”group“”. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 733. hwa-10.2.8-messages-awsui6020e-0498

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6020E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Remove all the jobs from the selected Jobstream or uncheck “”Group“” field. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 734. hwa-10.2.8-messages-awsui6021e-0499

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6021E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Ensure to not specify days over the schedule cycle length;.

**Plataforma / Validação:** Distributed

---

### 735. hwa-10.2.8-messages-awsui6022e-0500

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6022E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Ensure to not specify days over the schedule cycle length;.

**Plataforma / Validação:** Distributed

---

### 736. hwa-10.2.8-messages-awsui6023e-0501

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6023E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Ensure to not specify days over the schedule cycle length;.

**Plataforma / Validação:** Distributed

---

### 737. hwa-10.2.8-messages-awsui6025e-0502

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6025E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Ensure to not specify days over the schedule cycle length;.

**Plataforma / Validação:** Distributed

---

### 738. hwa-10.2.8-messages-awsui6026e-0503

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6026E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 739. hwa-10.2.8-messages-awsui6027w-0504

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6027W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Delete the object that was created, because it cannot be used. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 740. hwa-10.2.8-messages-awsui6029w-0505

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6029W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify an existing job stream in the condition. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 741. hwa-10.2.8-messages-awsui6030e-0506

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6030E indica um problema no Dynamic Workload Console: It was not possible to find the plugin with specified identifier. It may has been uninstalled from the engine. O sistema The requested operation is not completed. A acao documentada e: Check the plugin installation..

**Plataforma / Validação:** Distributed

---

### 742. hwa-10.2.8-messages-awsui6031w-0507

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6031W indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 743. hwa-10.2.8-messages-awsui6032e-0508

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6032E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Correct the runcycle and Retry the operation..

**Plataforma / Validação:** Distributed

---

### 744. hwa-10.2.8-messages-awsui6035e-0509

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6035E indica um problema no Dynamic Workload Console: See message. O sistema The requested operation is not completed. A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

---

### 745. hwa-10.2.8-messages-awsui6102e-0510

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6102E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Connect to a different scheduler engine..

**Plataforma / Validação:** Distributed

---

### 746. hwa-10.2.8-messages-awsui6103e-0511

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6103E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Connect to a different scheduler engine..

**Plataforma / Validação:** Distributed

---

### 747. hwa-10.2.8-messages-awsui6104w-0512

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6104W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Provide the user ID and password..

**Plataforma / Validação:** Distributed

---

### 748. hwa-10.2.8-messages-awsui6105e-0513

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6105E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Provide the user ID and password..

**Plataforma / Validação:** Distributed

---

### 749. hwa-10.2.8-messages-awsui6107e-0514

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6107E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Enter the passwords again. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 750. hwa-10.2.8-messages-awsui6113w-0515

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6113W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 751. hwa-10.2.8-messages-awsui6114e-0516

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6114E indica um problema no Dynamic Workload Console: The total number of characters in one or more of the specified fields exceeds the maximum supported limit. O sistema The requested operation is not performed. A acao documentada e: Reduce the number of characters in the specified fields. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 752. hwa-10.2.8-messages-awsui6116w-0517

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6116W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Specify a time in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 753. hwa-10.2.8-messages-awsui6120w-0518

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6120W indica um problema no Dynamic Workload Console: See message text. The objects you are trying to delete might be locked by another user or you might not have the required rights. O sistema The delete operation is performed only on the objects that can be deleted. The remaining objects remain unchanged. A acao documentada e: Correct the errors that prevent the object deletion. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 754. hwa-10.2.8-messages-awsui6124w-0519

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6124W indica um problema no Dynamic Workload Console: See message text. The objects you are trying to unlock might be locked by another user or you might not have the required rights. O sistema The unlock operation is performed only on the objects that can be unlocked. The remaining objects remain unchanged. A acao documentada e: Correct the errors that prevent the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 755. hwa-10.2.8-messages-awsui6126e-0520

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6126E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one date for the calendar. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 756. hwa-10.2.8-messages-awsui6131e-0521

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6131E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one week day. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 757. hwa-10.2.8-messages-awsui6132e-0522

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6132E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one week day. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 758. hwa-10.2.8-messages-awsui6133e-0523

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6133E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one week date. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 759. hwa-10.2.8-messages-awsui6137w-0524

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6137W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Resolve the compatibility issue, if possible, or select compatible objects. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 760. hwa-10.2.8-messages-awsui6138w-0525

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6138W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 761. hwa-10.2.8-messages-awsui6139e-0526

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6139E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Resolve the error condition. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 762. hwa-10.2.8-messages-awsui6146e-0527

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6146E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Specify a date in the correct time interval. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 763. hwa-10.2.8-messages-awsui6147e-0528

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6147E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one offset for the runcycle. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 764. hwa-10.2.8-messages-awsui6148e-0529

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6148E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one day and one type of day for the runcycle. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 765. hwa-10.2.8-messages-awsui6149e-0530

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6149E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one cycle specification for the runcycle. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 766. hwa-10.2.8-messages-awsui6154e-0531

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6154E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one type of day for the runcycle. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 767. hwa-10.2.8-messages-awsui6155e-0532

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6155E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one day, one type of day and one cycle specification. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 768. hwa-10.2.8-messages-awsui6156e-0533

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6156E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one type of day and one cycle specification. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 769. hwa-10.2.8-messages-awsui6161w-0534

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6161W indica um problema no Dynamic Workload Console: See message text. The objects you are trying to lock might be locked by another user or you might not have the required rights. O sistema The lock operation is performed only on the objects that can be locked. The remaining objects remain unchanged. A acao documentada e: Correct the errors that prevent the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 770. hwa-10.2.8-messages-awsui6164e-0535

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6164E indica um problema no Dynamic Workload Console: See message text. The specified days are invalid for the weekly cycle length (5). O sistema The Run Cycle can be evaluated only with days valid for the selected cycle. A acao documentada e: Correct the errors that prevent the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 771. hwa-10.2.8-messages-awsui6165e-0536

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6165E indica um problema no Dynamic Workload Console: See message text. The specified days are invalid for the monthly cycle length (31). O sistema The Run Cycle can be evaluated only with days valid for the selected cycle. A acao documentada e: Correct the errors that prevent the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 772. hwa-10.2.8-messages-awsui6167e-0537

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6167E indica um problema no Dynamic Workload Console: See message text. The specified days and the weekdays: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday are invalid for the specified cycle length. O sistema The Run Cycle can be evaluated only with days and weekdays valid for the selected cycle. A acao documentada e: Correct the errors that prevent the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 773. hwa-10.2.8-messages-awsui6168e-0538

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6168E indica um problema no Dynamic Workload Console: See message text.There is no destination object where to perform the operation. O sistema There is no destination object where to perform the operation. A acao documentada e: Create the destination object before to perform the action. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 774. hwa-10.2.8-messages-awsui6169e-0539

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6169E indica um problema no Dynamic Workload Console: See message text. O sistema There is no object where to perform the operation. A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 775. hwa-10.2.8-messages-awsui6171w-0540

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6171W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 776. hwa-10.2.8-messages-awsui6172w-0541

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6172W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 777. hwa-10.2.8-messages-awsui6173w-0542

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6173W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 778. hwa-10.2.8-messages-awsui6175w-0543

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6175W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 779. hwa-10.2.8-messages-awsui6176w-0544

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6176W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 780. hwa-10.2.8-messages-awsui6177w-0545

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6177W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select a Job Stream to print. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 781. hwa-10.2.8-messages-awsui6178w-0546

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6178W indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Use the information in the error_message to diagnose and resolve the problem. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 782. hwa-10.2.8-messages-awsui6180e-0547

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6180E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Change or remove one of the selected weekdays. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 783. hwa-10.2.8-messages-awsui6181e-0548

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6181E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Fill in all the required fields. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 784. hwa-10.2.8-messages-awsui6182w-0549

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6182W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 785. hwa-10.2.8-messages-awsui6183e-0550

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6183E indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Specify the Job stream name and the job number and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 786. hwa-10.2.8-messages-awsui6184e-0551

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6184E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: See message text..

**Plataforma / Validação:** Distributed

---

### 787. hwa-10.2.8-messages-awsui6186w-0552

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6186W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Save the job stream and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 788. hwa-10.2.8-messages-awsui6187w-0553

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6187W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Save the job stream and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 789. hwa-10.2.8-messages-awsui6188w-0554

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6188W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Save the R3 Standard Job and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 790. hwa-10.2.8-messages-awsui6194w-0555

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6194W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 791. hwa-10.2.8-messages-awsui6195w-0556

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6195W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 792. hwa-10.2.8-messages-awsui6196w-0557

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6196W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 793. hwa-10.2.8-messages-awsui6198w-0558

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6198W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 794. hwa-10.2.8-messages-awsui6202w-0559

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6202W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 795. hwa-10.2.8-messages-awsui6203e-0560

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6203E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Connect to a different scheduler engine..

**Plataforma / Validação:** Distributed

---

### 796. hwa-10.2.8-messages-awsui6204w-0561

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6204W indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 797. hwa-10.2.8-messages-awsui6205e-0562

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6205E indica um problema no Dynamic Workload Console: See message text. O sistema No action performed A acao documentada e: Correct the error and retry the operation. Retry the operation..

**Plataforma / Validação:** Distributed

---

### 798. hwa-10.2.8-messages-awsui6206e-0563

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6206E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Select at least one checkbox.

**Plataforma / Validação:** Distributed

---

### 799. hwa-10.2.8-messages-awsui6210e-0564

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6210E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Connect to a different scheduler engine..

**Plataforma / Validação:** Distributed

---

### 800. hwa-10.2.8-messages-awsui6211e-0565

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6211E indica um problema no Dynamic Workload Console: See message text. O sistema The requested operation is not performed. A acao documentada e: Connect to a different scheduler engine..

**Plataforma / Validação:** Distributed

---

### 801. hwa-10.2.8-messages-eel-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: messages > eel [messages_zos]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o conjunto de mensagens EEL cobre erros e avisos emitidos pelo HCL Workload Automation agent for z/OS. Essas mensagens sao especificas para ambientes z/OS e coverem problemas de conexao, processamento e recursos do agente para mainframe. O Message Help em https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmsghelp.html fornece Explanation, System action e Operator response para cada codigo EEL.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o conjunto de mensagens EEL cobre erros e avisos emitidos pelo HCL Workload Automation agent for z/OS?*

---

### 802. hwa-10.2.8-messages-format-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > format [messages_help]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as mensagens de erro e aviso seguem um formato padrao com: Message Number (codigo alfanumerico unico, ex.: AWKTSA050E, AWSITA104E), Message Text (descricao do erro), Explanation (explicacao adicional da causa), System action (descricao do que o sistema faz como resultado), Operator response (acao que o operador deve tomar) e See also (referencia a publicacoes relacionadas). Os conjuntos de mensagens (message sets) sao organizados por componente: AWKTSA (dynamic agent), AWKZSJ (z/OS shadow job validation), AWSWUI (Dynamic Workload Console), AWSZAP (Action plug-in for z/OS) e EEL (HCL Workload Automation agent for z/OS). O Message Help online esta em https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmsghelp.html e o guia completo Messages and Codes em PDF.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKTSA050E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKTSA050E no HWA?*
- *Qual é o significado da mensagem de erro AWSITA104E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA104E no HWA?*

---

### 803. hwa-10.2.8-monitor-db-views-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
As views de banco de dados no HCL Workload Automation 10.2.8 são documentadas como conjunto de views predefinidas para extrair informações do banco de dados e definir relatórios com ferramentas como Crystal Reports ou Brio, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: As views de banco de dados no HCL Workload Automation 10.2.8 são documentadas como conjunto de views predefinidas para extrair informações do banco de dados e definir relatórios com ferramentas como Crystal Reports ou Brio, conforme documentação oficial?*

---

### 804. hwa-10.2.8-monitor-dwc-reporting-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A seção Reporting do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentada para recuperar dados do banco de dados de workload e visualizar, imprimir e salvar resultados, usando relatórios predefinidos ou relatórios personalizados (BIRT), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A seção Reporting do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentada para recuperar dados do banco de dados de workload e visualizar, imprimir e salvar resultados, usando relatórios predefinidos ou relatórios personalizados (BIRT), conforme documentação oficial?*

---

### 805. hwa-10.2.8-monitor-job-history-v-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view JOB_HISTORY_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre o histórico de execução de jobs, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_HISTORY_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional JOB_HISTORY_V no banco de dados do HWA?*

---

### 806. hwa-10.2.8-monitor-job-statistics-v-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view JOB_STATISTICS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações de estatísticas sobre jobs, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?*

---

### 807. hwa-10.2.8-monitor-job-statistics-v-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view JOB_STATISTICS_V no HCL Workload Automation 10.2.8 é documentada com colunas de estatísticas de jobs como Successful_runs, Abended_runs, Late_start_runs, Late_end_runs, Total_reruns, Average_elapsed_time, Total_elapsed_time e Total_cpu_time, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 808. hwa-10.2.8-monitor-plan-job-streams-v-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view PLAN_JOB_STREAMS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os job streams presentes no plano, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco PLAN_JOB_STREAMS_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional PLAN_JOB_STREAMS_V no banco de dados do HWA?*

---

### 809. hwa-10.2.8-monitor-plan-jobs-v-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view PLAN_JOBS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os jobs presentes no plano corrente, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco PLAN_JOBS_V no HCL Workload Automation?*

---

### 810. hwa-10.2.8-monitor-plan-workstations-v-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
A view PLAN_WORKSTATIONS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre as workstations presentes no plano, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco PLAN_WORKSTATIONS_V no HCL Workload Automation?*

---

### 811. hwa-10.2.8-monitor-predefined-reports-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
Os relatórios predefinidos do Dynamic Workload Console no HCL Workload Automation 10.2.8 incluem os tipos Job Run Statistics, Job Run History, Workstation Workload Summary, Workstation Workload Runtimes, Plan Reports e Custom SQL Reports, gerados em Monitoring and Reporting, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os relatórios predefinidos do Dynamic Workload Console no HCL Workload Automation 10.2.8 incluem os tipos Job Run Statistics, Job Run History, Workstation Workload Summary, Workstation Workload Runtimes, Plan Reports e Custom SQL Reports, gerados em Monitoring and Reporting, conforme documentação oficial?*

---

### 812. hwa-10.2.8-monitor-rep-commands-list-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
Os comandos de relatório documentados no HCL Workload Automation 10.2.8 são rep1, rep2, rep3, rep4a, rep4b, rep7, rep8, rep11, reptr e xref, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os comandos de relatório documentados no HCL Workload Automation 10.2.8 são rep1, rep2, rep3, rep4a, rep4b, rep7, rep8, rep11, reptr e xref, conforme documentação oficial?*

---

### 813. hwa-10.2.8-monitor-rep7-report-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
O comando de relatório rep7 no HCL Workload Automation 10.2.8 é documentado como 'Report 07 - Job History Listing', permitindo gerar um relatório de histórico de jobs, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O comando de relatório rep7 no HCL Workload Automation 10.2.8 é documentado como 'Report 07 - Job History Listing', permitindo gerar um relatório de histórico de jobs, conforme documentação oficial?*

---

### 814. hwa-10.2.8-monitor-wappman-import-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
O utilitário wappman no HCL Workload Automation 10.2.8 é documentado para importar, substituir, excluir, exportar, exibir e listar workload applications, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wappman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wappman para gerenciar monitor?*

---

### 815. hwa-10.2.8-monitor-workload-dashboard-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
O Workload Dashboard do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentado como um recurso de monitoramento que permite monitorar o progresso do plano, aberto em Boards > Workload Dashboard, com widgets predefinidos, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O Workload Dashboard do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentado como um recurso de monitoramento que permite monitorar o progresso do plano, aberto em Boards > Workload Dashboard, com widgets predefinidos, conforme documentação oficial?*

---

### 816. hwa-10.2.8-msg-awsbab001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBAB001I (BAB) indica: "maestro.cat C @(#) 1.19 03/04/09 12:36:24 tws_main/src/catalog/maestro.xml, maestro_l10n_src, tws_dev @(#) AWSBAB002I @(#) Copyright IBM Corp. 1991, 2016. Copyright HCL Technologies Ltd. 2016. This is a dummy label. It must be the last label in every".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 817. hwa-10.2.8-msg-awsbak001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBAK001I (BAK) indica: "EDITOR.PUB.SYS BASICENTRY Maestro                                                     !                                                              Page# :FILE EDTTEXT=!# :RUN EDITOR.PUB.SYS,BASICENTRY#                  %       7   ¦       8   ·  ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 818. hwa-10.2.8-msg-awsbat001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBAT001I (BAT) indica: "The event counter is successfully initializing: !1 AWSBAT002I The event counter is successfully initializing, workstation counter on the hard drive has been updated : !1 AWSBAT003E The event counter failed to initialize for the following reason: "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 819. hwa-10.2.8-msg-awsbcs040w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS040W (BCS) indica: "Workstation "!1" was not found in the Symphony file on node "!2". AWSBCS041W Domain "!1" was not found in the Symphony file on node "!2". AWSBCS042W Node "!1" is not running. AWSBCS043W Nodes "!1" and "!2" are not linked. AWSBCS044I Nodes "!1" and "!".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 820. hwa-10.2.8-msg-awsbcs052i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS052I (BCS) indica: "Check that the HOSTNAME for the definition of workstation "!1" is correct.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 821. hwa-10.2.8-msg-awsbcs053i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS053I (BCS) indica: "Check that the machine for workstation "!1" is up and running.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 822. hwa-10.2.8-msg-awsbcs054i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS054I (BCS) indica: "Check that all nodes between "!1" and "!2"are correctly linked.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 823. hwa-10.2.8-msg-awsbcs055i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS055I (BCS) indica: "Verify that "Check Health Status" is supported on the HCL Workload Automation level of node "!1". AWSBCS060I If you cannot resolve the problem, search the HCL Support database for a solution at https://www.hcltech.com/products-and-platforms/support. ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 824. hwa-10.2.8-msg-awsbcs062i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS062I (BCS) indica: "Check the SSL configuration of node "!1". AWSBCS063I Check the SSL configuration of nodes "!1" and "!2". AWSBCS071I Verify that node "!1" is linked; if it is not, run Check Health Status on that node first. AWSBCS072I Run a link command on node "!1" ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 825. hwa-10.2.8-msg-awsbcs073i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS073I (BCS) indica: "Run a start command on node "!1" from conman or the TDWC; then, run a link command on node "!1".".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 826. hwa-10.2.8-msg-awsbcs074i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS074I (BCS) indica: "Run a stop command on node "!1" from conman or the TDWC; then, run Check Health Status again on node "!1".".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 827. hwa-10.2.8-msg-awsbcs075i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS075I (BCS) indica: "Use the evtsize utility to increase the maximum size of message files. AWSBCS076I If a workstation is planned to be offline for a long period, consider setting it to IGNORE to avoid that the pobox message file reaches its maximum size. AWSBCS077I Del".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 828. hwa-10.2.8-msg-awsbcs078e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCS078E (BCS) indica: "An internal error has occurred. The program is unable to initialize the OpenSSL libraries. Potential causes might be problems with the installation or configuration of the libraries, or you might have enabled FIPS, which is not currently supported. O".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 829. hwa-10.2.8-msg-awsbct002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT002E (BCT) indica: "A jcl file is required. AWSBCT003E The jcl file path must be no more than !1 characters AWSBCT004E The -u option is available only for root users. AWSBCT005W The jcl is submitted as root, you must use -u <user>. AWSBCT006E No password entry for the u".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 830. hwa-10.2.8-msg-awsbct021e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT021E (BCT) indica: "Could not assign a schedule name, use -s option. AWSBCT022E Could not assign a job name, use -j option. AWSBCT023E Must assign date/time in the format YYMMDDHHmm. AWSBCT024E Date/time must have 10 digits in the format YYMMDDHHmm. AWSBCT025E Priority ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 831. hwa-10.2.8-msg-awsbct031e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT031E (BCT) indica: "You must start Netman manually on this system. AWSBCT032I You are not authorized to start any product. AWSBCT033E An error occurred starting the local system, Type: !1, Error: !2 AWSBCT034E An error occurred starting the NS/DS system: !1, Error: !2 A".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 832. hwa-10.2.8-msg-awsbct071w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT071W (BCT) indica: "Netman is already down. AWSBCT072E Stopping local Netman, Error: !1 AWSBCT073W No Netman. AWSBCT074W Netman is already down. Usage: release [ -V | -U ]".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 833. hwa-10.2.8-msg-awsbct081e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT081E (BCT) indica: "Environment variable !1 was not found, not a HCL Workload Automation job. AWSBCT091E chmod error on !1, Error: !2 AWSBCT092E chown error on !1, Error: !2 Enter commands (!1)# AWSBCT094E No commands entered, the job has not been submitted. Usage: maes".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 834. hwa-10.2.8-msg-awsbct104i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT104I (BCT) indica: "Option !1 requires an argument. AWSBCT105E Unrecognized option !1. Running dbexpand converts all the existing databases".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 835. hwa-10.2.8-msg-awsbct107e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT107E (BCT) indica: "Databases not converted. Exiting. AWSBCT108E The globalopts file does not exist. AWSBCT109E The globalopts file needs read and write permission. Check the permissions. The backup is done in !1 by default.# AWSBCT111W !1 is identical to !2. AWSBCT112E".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 836. hwa-10.2.8-msg-awsbct134i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT134I (BCT) indica: " AWSBCT135I  AWSBCT136I  AWSBCT137I  AWSBCT138I -b Dir Use this directory to backup the database files.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 837. hwa-10.2.8-msg-awsbct139i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT139I (BCT) indica: " AWSBCT140I  AWSBCT141I  AWSBCT142I  AWSBCT200E You must enter the user manually. AWSBCT201E Incorrect option. AWSBCT202E The path is limited to !1 characters. AWSBCT203E The filename is the only argument available. Usage: delete { -V | -U | <file se".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 838. hwa-10.2.8-msg-awsbct706i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT706I (BCT) indica: "The -u and -d options cannot both be supplied. AWSBCT707I The -u option requires a username AWSBCT708E Incorrect username. AWSBCT709E Unknown argument %c AWSBCT710W The -u and -d options cannot both be supplied. AWSBCT711E No files specified. AWSBCT7".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 839. hwa-10.2.8-msg-awsbct727e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT727E (BCT) indica: "Unable to change owner for file %s (error %d) AWSBCT728E Unable to open file %s (error %d) AWSBCT729E Unable to reset restore privilege (error %d) AWSBCT751E Exception Message: !1 AWSBCT752I Done Setting attribute 'TWSHomeDir' as !1. AWSBCT753I Engin".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 840. hwa-10.2.8-msg-awsbct864i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCT864I (BCT) indica: " AWSBCT865E Error opening SC Manager. error = %d. AWSBCT866E -s option requires a service name. AWSBCT867E -u option requires a user name. AWSBCT868E -D option requires a dependency spec. AWSBCT869E -d option requires a display name. AWSBCT870E -l op".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 841. hwa-10.2.8-msg-awsbcu001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCU001E (BCU) indica: "Opening !1, error: !2 AWSBCU002E Locking !1, error: !2 AWSBCU003E Unable to allocate comarea !1 AWSBCU004E Could not set file options on !1, error !2 AWSBCU005E Closing !1, error: !2 AWSBCU006E Purging !1, error: !2 AWSBCU007E An error has occurred i".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 842. hwa-10.2.8-msg-awsbcv001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCV001E (BCV) indica: "Batchman has failed with an internal error, producing the following status code: !1. AWSBCV002E Error building !1, Error !2 AWSBCV003E Mailman was unable to start one of the internal components (!1) of batchman. The system error message is "!2" AWSBC".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 843. hwa-10.2.8-msg-awsbcv012e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCV012E (BCV) indica: "Mailman cannot read a message in a message file. The following gives more details of the error: "!1". AWSBCV017I The total cpu time used by MAILMAN was !1 seconds AWSBCV018I !1/Operator command: !2 AWSBCV021I Server !1 is available. AWSBCV024W Mailma".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 844. hwa-10.2.8-msg-awsbcv108i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCV108I (BCV) indica: "Started batchman, pin !1 AWSBCV109I Started jobman, pin !1 AWSBCV116I Switching managers in domain !1 from workstation "!2" to workstation "!3". AWSBCV121E Mailman cannot link to the following workstation: !1, which is a domain manager but is running".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 845. hwa-10.2.8-msg-awsbcv124e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCV124E (BCV) indica: "Mailman is unable to connect to workstation !1 using SSL due to an inconsistency in the HCL Workload Automation network configuration. AWSBCV130I Mailman has started the first phase of the replay protocol with the following workstation: !1. The remot".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 846. hwa-10.2.8-msg-awsbcw001w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCW001W (BCW) indica: "Warning illegal option(s): !1 AWSBCW003E Writer cannot connect to the remote mailman. The following gives more details of the error: "!1". AWSBCW004E Error non numeric sockfd: !1 !1 !1 !1 AWSBCW008E The following error has occurred while installing t".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 847. hwa-10.2.8-msg-awsbcw002w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCW002W (BCW) indica: "Writer cannot find a valid "wr read" value in the localopts file. The value found is as follows: !1. The default value is used. AWSBCW025E Writer is started by netman with an incorrect number of arguments. AWSBCW028I Started by !1/!2 from !3; worksta".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 848. hwa-10.2.8-msg-awsbcw035i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCW035I (BCW) indica: "Netman has told writer to quit, total cpu !1 AWSBCW037E Writer cannot initialize this workstation because mailman is still active. AWSBCW038E Writer needs the exclusive access to the Symphony and Sinfonia files in order to initialize the workstation.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 849. hwa-10.2.8-msg-awsbcx001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCX001E (BCX) indica: "An internal error has occurred. Monman cannot read a message in a message file. The following gives more details of the error: "!1". AWSBCX002E An internal error has occurred. Monman could not set the termination signal handling routines. The followi".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 850. hwa-10.2.8-msg-awsbcx006i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCX006I (BCX) indica: "Monman (pid=!1 pgid=!2) was started by netman (pid=!3 pgid=!4).               O  7Ý  7e  5C  "   ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 851. hwa-10.2.8-msg-awsbcy001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCY001E (BCY) indica: "Could not allocate dbaccs comarea. AWSBCY002E Invalid comarea passed to dbaccs routines. AWSBCY003E Attempt to write to unopened file. AWSBCY004E Database not available or access not initialized. AWSBCY005W File newer than dbaccs. AWSBCY006I End of c".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 852. hwa-10.2.8-msg-awsbcz001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBCZ001E (BCZ) indica: "An error while opening !1: !2 AWSBCZ002I The object ID is too long. AWSBCZ003E The object ID must start with an alphabetic character. AWSBCZ004E The object ID contains at least one character that is not valid. Valid characters are 0-9, a-z, dashes an".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 853. hwa-10.2.8-msg-awsbda001w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDA001W (BDA) indica: "A host has been specified for the master domain manager, and has been ignored. AWSBDA002W The domain manager "!1" is not defined as a fault-tolerant agent. AWSBDA003W The domain manager "!1" does not have "fullstatus" set to "on". AWSBDA004W The doma".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 854. hwa-10.2.8-msg-awsbdb001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDB001E (BDB) indica: "Error opening connection to conman, Error !1 AWSBDB002E Error unable to create stdlist AWSBDB006E Error in ntoh (Symphony rec): !1 AWSBDB007E Error sending scribner_response rec: !1 AWSBDB008E Error receiving scribner_response rec: !1 AWSBDB009E Erro".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 855. hwa-10.2.8-msg-awsbdb004w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDB004W (BDB) indica: "The timeout value "!1" is not valid. The default value has been used. AWSBDB005E There is a syntax error. Too few parameters have been supplied. AWSBDB010I Started by !1/!2 from !3 Workstation platform: !4 This is a dummy label. It must be the last l".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 856. hwa-10.2.8-msg-awsbdc001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDC001E (BDC) indica: "Error in !1, calling !2, for !3, error: !4 AWSBDC002E Error allocating space in !1, error: !2 AWSBDC003E Unknown parent for !1, id=!2 AWSBDC004E Unknown node for !1, ID=!2 AWSBDC005E Unknown network for !1, ID=!2 AWSBDC006E Unknown workstation for !1".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 857. hwa-10.2.8-msg-awsbdc101w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDC101W (BDC) indica: "Openview is not running on this system: !1 AWSBDC102E HCL Workload Automation is not correctly installed on this system: "!1". AWSBDC103E Initialization failed. AWSBDC104E No object for !1. AWSBDC105E Non-valid state packet received: !1 AWSBDC106E No".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 858. hwa-10.2.8-msg-awsbdc205e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDC205E (BDC) indica: "Initialization failed. AWSBDC206E Error opening !1, error: !2 AWSBDC207E Error returned from select operation: !1 AWSBDC208E Error opening snmp connection to !1: !2 AWSBDC209E Error in !1, invalid packet: !2 AWSBDC210E Error in sigact: !1 AWSBDC211E ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 859. hwa-10.2.8-msg-awsbdc305e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDC305E (BDC) indica: "Initialization failed. AWSBDC306E Error opening !1, error: !2 AWSBDC307E Error returned from select operation: !1 AWSBDC308W Process does not have a pid: !1 AWSBDC309E Process has a non-valid pid: !1 AWSBDC310E Error writing "!2" to !1: !3 AWSBDC311E".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 860. hwa-10.2.8-msg-awsbdc500e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDC500E (BDC) indica: "not string AWSBDC501E bad length AWSBDC502E not print %x AWSBDC503E need error message for work != node                  6          i                    ·          à         ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 861. hwa-10.2.8-msg-awsbdd001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDD001E (BDD) indica: "BmEvents error allocating space for !1: !2 AWSBDD002E BmEvents option !1 is not supported. AWSBDD003E BmEvents error opening !1: !2 AWSBDD004E BmEvents error writing !1: !2 AWSBDD101I BmEvents will write to !1 type !2 This is a dummy label. It must b".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 862. hwa-10.2.8-msg-awsbde004e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDE004E (BDE) indica: "A non-valid value for the timeout "!1" has been supplied. AWSBDE005E The "chkstat" command has not been supplied with the correct number of parameters. AWSBDE006E Unable to send a response record. The error is: !1. AWSBDE007E Unable to receive a requ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 863. hwa-10.2.8-msg-awsbdf001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDF001E (BDF) indica: "Unable to open a connection to the chkstat service: !1 AWSBDF002E Unable to start the chkstat service: !1 AWSBDF003E Error: !1 AWSBDF004E Cannot get a reply from the chkstat service: !1 AWSBDF005E Cannot send a request to the chkstat service: !1 AWSB".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 864. hwa-10.2.8-msg-awsbdg001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDG001E (BDG) indica: "Downloader cannot connect to the remote client. The socket descriptor passed to downloader by netman is not valid. The following gives more details of the error: !1. AWSBDG002E Downloader is unable to create the stdlist file. Usage: downloader [ -V |".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 865. hwa-10.2.8-msg-awsbdh001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDH001E (BDH) indica: "The action code !1 specified in the !2 native method is invalid AWSBDH002E The object type !1 specified in the !2 native method is invalid This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or Message endi".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 866. hwa-10.2.8-msg-awsbdj001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDJ001I (BDJ) indica: "O processo do monitor do servidor de aplicativos "appservman" foi iniciado. Ele inicia o servidor de aplicativos, se for parte da instalaÃ§Ã£o do agente, e monitora seu status. Se o servidor de aplicativos parar, o "appservman" inicializarÃ¡, de acor".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 867. hwa-10.2.8-msg-awsbdj018e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDJ018E (BDJ) indica: "An internal error has occurred. The program is unable to initialize the OpenSSL libraries. Potential causes might be problems with the installation or configuration of the libraries, or you might have enabled FIPS, which is not currently supported. T".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 868. hwa-10.2.8-msg-awsbdw001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDW001E (BDW) indica: "Jobman cannot set the process group id to the group id of the logon user. The operating system error is: "!1". AWSBDW003E Jobman cannot change the current working directory to the home directory of the logon user. The operating system error is: !1. A".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 869. hwa-10.2.8-msg-awsbdw002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDW002E (BDW) indica: "The user ID used to launch this job is not valid. The operating system error is: !1. AWSBDW005E Error "!2" occurred while trying to open JCL file "!1". AWSBDW009E The following operating system error occurred retrieving the password structure for eit".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 870. hwa-10.2.8-msg-awsbdw051i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDW051I (BDW) indica: "Jobman received a quit message. AWSBDW052I Jobman received a stop signal. AWSBDW056I Jobman is terminating. Workstation usage is: !1# AWSBDW057E The job "!1" was not launched for this reason: !2 Starting# AWSBDW065I The following output was received ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 871. hwa-10.2.8-msg-awsbdw070e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDW070E (BDW) indica: "Jobman cannot start. It has tried to become a daemon, giving the following internal error: "%li" and system error: "%s". AWSBDW071E The following script or command name: "%s" has exceeded the maximum number of characters allowed: %d. AWSBDW072E Jobma".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 872. hwa-10.2.8-msg-awsbdy101e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDY101E (BDY) indica: "Bad Mailbox record found. AWSBDY102E An internal error has occurred. The program cannot access the mailbox or ftbox common area in memory. The pointer to the mailbox common area is NULL or the area is not initialized. AWSBDY103I Received command MY:U".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 873. hwa-10.2.8-msg-awsbdz001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDZ001E (BDZ) indica: "Record out of range. Enter next record or Next, Prev, Back, Forward, Up (parent)# Other commands: List, Exit, Radix, Output, Modify# Hex is preceded by $. Octal is preceded by %# AWSBDZ005E The input was not valid. AWSBDZ006E No lists are possible fo".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 874. hwa-10.2.8-msg-awsbdz057e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBDZ057E (BDZ) indica: "No holders could be found. AWSBDZ058E No dependencies could be found. AWSBDZ059E No rerun jobs could be found. AWSBDZ060E No folders could be found. This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or Me".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 875. hwa-10.2.8-msg-awsbea001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEA001E (BEA) indica: "Unable to open the mozart database. AWSBEA002E Unable to read from the mozart database. AWSBEA003E An error occurred while initializing the SORT routine. AWSBEA004E An error occurred in the SORTINPUT. AWSBEA005E An error occurred in the SORTOUTPUT. T".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 876. hwa-10.2.8-msg-awsbec110e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC110E (BEC) indica: "Cannot open file "!1". AWSBEC111E An error occurred while writing file "!1". AWSBEC112E An error occurred while reading file "!1". %-60.60s %-63.63s Page %4d".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 877. hwa-10.2.8-msg-awsbec806i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC806I (BEC) indica: " Usage: report2 [-V | -U] [-i input] [-o output] 	-V    Version information# 	-U    Usage information# 	-i    Use this to supply the name of an input file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 878. hwa-10.2.8-msg-awsbec813i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC813I (BEC) indica: " Usage: report3 [-V | -U] [-i input] [-o output] 	-V    Version information# 	-U    Usage information# 	-i    Use this to supply the name of an input file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 879. hwa-10.2.8-msg-awsbec820i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC820I (BEC) indica: " AWSBEC821E The following database open error occurred:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 880. hwa-10.2.8-msg-awsbec828i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC828I (BEC) indica: " Usage: report4b [-V | -U] [-i input] [-o output] 	-V    Version information# 	-U    Usage information# 	-i    Use this to supply the name of an input file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 881. hwa-10.2.8-msg-awsbec835i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC835I (BEC) indica: " Usage: report7 [-V | -U] [-s sched] [-f date -t date]".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 882. hwa-10.2.8-msg-awsbec845i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC845I (BEC) indica: " Usage: report8 [-V | -U] [-p]".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 883. hwa-10.2.8-msg-awsbec857i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC857I (BEC) indica: " Usage: report11 [-V | -U] [-i input] [-o output] 	-V    Version information# 	-U    Usage information# 	-i    Use this to supply the name of an input file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 884. hwa-10.2.8-msg-awsbec864i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC864I (BEC) indica: " Usage: caxtract [-V | -U] [-o output] 	-V    Version information# 	-U    Usage information# 	-o    Use this to supply the name of an output file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 885. hwa-10.2.8-msg-awsbec869i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC869I (BEC) indica: " AWSBEC870E The following database open error occurred:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 886. hwa-10.2.8-msg-awsbec885i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC885I (BEC) indica: "-i Use this to supply the name of an input file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 887. hwa-10.2.8-msg-awsbec886i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC886I (BEC) indica: "-o Use this to supply the name of an output file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 888. hwa-10.2.8-msg-awsbec887i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC887I (BEC) indica: "Cannot open file '%s' Usage: paxtract [-V | -U] [-a] [-o output] 	-V    Version information# 	-U    Usage information# 	-o    Use this to supply the name of an output file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 889. hwa-10.2.8-msg-awsbec892i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC892I (BEC) indica: " Usage: prxtract [-V | -U] [-o output] 	-V    Version information# 	-U    Usage information# 	-o    Use this to supply the name of an output file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 890. hwa-10.2.8-msg-awsbec897i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC897I (BEC) indica: " Usage: rextract [-V | -U] [-o output] 	-V    Version information# 	-U    Usage information# 	-o    Use this to supply the name of an output file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 891. hwa-10.2.8-msg-awsbec902i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEC902I (BEC) indica: " AWSBEC903I Cannot open file '%s'                                      Ì          å          þ                	  0       ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 892. hwa-10.2.8-msg-awsbee001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEE001E (BEE) indica: "Parameter !1 does not exist. AWSBEE002E The following parameter name is not valid: !1. AWSBEE003E You cannot use the following parameter: !1. Usage: parms [<parm-name> | -c <parm-name> <parm-content> | -d <parm-name> | -e <file-name> | -r <file-name>".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 893. hwa-10.2.8-msg-awsbef001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEF001E (BEF) indica: "Missing last archive run date. AWSBEF002E Archiver could not create a directory with the following path: !1. AWSBEF003I The Symphony file !1 from schedlog was archived. AWSBEF004E An error occurred while opening the Symphony file from schedlog !1. AW".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 894. hwa-10.2.8-msg-awsbeg201e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEG201E (BEG) indica: "O seguinte diretÃ³rio nÃ£o pÃ´de ser criado: !2. O seguinte erro foi retornado do sistema operacional: !1 AWSBEG202E NÃ£o foi possÃ­vel definir os direitos de acesso para o seguinte diretÃ³rio: !2. O seguinte erro foi retornado do sistema operacional".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 895. hwa-10.2.8-msg-awsbeh001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEH001E (BEH) indica: "The connection configuration file "!1" containing the connection properties cannot be found. AWSBEH002E The target host computer is not defined in the connection configuration file or the supplied command parameters. AWSBEH003E The protocol is not de".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 896. hwa-10.2.8-msg-awsbeh122i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEH122I (BEH) indica: "The upload of the generic event provider XML has completed successfully. AWSBEH123I The download of the generic event provider XML has completed successfully. Usage: planman [-u | -v] planman [connectionParameters]".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 897. hwa-10.2.8-msg-awsbeh144w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEH144W (BEH) indica: "Unable to execute the Resync command because the Symphony file is not found. AWSBEH145W Unable to execute the Checksync command because the Symphony file is not found. This is a dummy label. It must be the last label in every subcomponent. It ensures".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 898. hwa-10.2.8-msg-awsbei001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEI001E (BEI) indica: "User "!1" does not exist. AWSBEI002E The file "!1" is empty, or an error occurred during the conversion of the contents of the file to UNICODE. No user has been added to or updated in the local database. AWSBEI003W An internal error has occurred. Can".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 899. hwa-10.2.8-msg-awsbei007e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEI007E (BEI) indica: "You are not authorized to run this command. User !1 found. AWSBEI009E An error has occurred. The user "!1" has not been updated or added. AWSBEI010E Cannot open the file "!1". Operating system error: "!2". AWSBEI011E The Unicode (UTF-8) name of the w".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 900. hwa-10.2.8-msg-awsbej002i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBEJ002I (BEJ) indica: "No error was found in the Symphony file. AWSBEJ010E Error: Job stream record (#!1) has incorrect dependencies. AWSBEJ011E Error: Job record (#!1) has incorrect dependencies. AWSBEJ012E Error while reading record (#!1): !2 AWSBEJ014E Error: The job st".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 901. hwa-10.2.8-msg-awsbhs001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHS001E (BHS) indica: "Error: Unable to open connection to MVS gateway: !1 AWSBHS002E Error: Unable to start the MVS gateway: !1 AWSBHS003E Error: !1 AWSBHS004E Error: Cannot get reply from the MVS gateway: !1 AWSBHS005E Error: Cannot send request to MVS gateway: !1 AWSBHS".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 902. hwa-10.2.8-msg-awsbht001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHT001E (BHT) indica: "The job "!1" in file "!2" has failed with the error: !3 AWSBHT002W Job logs on differently than documentation indicates. AWSBHT015W Batchman cannot release a job stream from its dependencies because the job stream is not in the "holding" state that i".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 903. hwa-10.2.8-msg-awsbht003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHT003E (BHT) indica: "Batchman is unable to allocate memory for its internal record table during initialization. AWSBHT004E Batchman has read a record in the message file which has the following destination workstation (!1) that cannot be found. The message originated at ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 904. hwa-10.2.8-msg-awsbht201i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHT201I (BHT) indica: "Job stream !1 UNTIL time !2 has occurred. The UNTIL user option is !3 AWSBHT202I Job !1 UNTIL time !2 has occurred. The UNTIL user option is !3 AWSBHT203I Job !1 Maximum Duration time !2 has exceeded. The MaxDur user option is !3 AWSBHT204I Job !1 Mi".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 905. hwa-10.2.8-msg-awsbht230w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHT230W (BHT) indica: "Warning: Dependency !1 not found in Symphony;ignored. AWSBHT231W A duplicated job termination (JT) record has been received for the following job: !1. AWSBHT233W An incorrect dependency has been detected for the following jobstream: !1.Priority will ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 906. hwa-10.2.8-msg-awsbhu001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHU001E (BHU) indica: "Conman encountered an error when attempting to open the Symphony file: the file does not exist or conman could not find it. The following gives more details of the error: !1. AWSBHU002E Conman encountered an error when attempting to open either the M".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 907. hwa-10.2.8-msg-awsbhu021e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHU021E (BHU) indica: "The agent on workstation: !1 cannot be started because it has not got the latest Symphony file version. AWSBHU022E The time value specified as an argument is incorrect. It must be numeric, between 0000 and 2359. AWSBHU023E You have issued an "opens" ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 908. hwa-10.2.8-msg-awsbhu126e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHU126E (BHU) indica: "A time zone has been specified in a time dependency, but time zone use has not been enabled for workstation: !1 AWSBHU127W Submitted !1 to batchman as !2# but workstation !3 not present in the Symphony file. AWSBHU128W Dependency !1 might not be pres".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 909. hwa-10.2.8-msg-awsbhu606e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHU606E (BHU) indica: "An error occurred while saving the user options file:"!1" AWSBHU607E The value specified for the "-protocol" connection parameter is not valid. It must be "http" or "https". Do you want save the user name and password in your "useropts" file (enter "".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 910. hwa-10.2.8-msg-awsbhu617i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHU617I (BHU) indica: "The "bulk_discovery" command was forwarded to batchman. AWSBHU618E The "bulk_discovery" was not performed because no configuration file was found. AWSBHU619E The following error occurred obtaining the monitoring configuration file for workstation "!1".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 911. hwa-10.2.8-msg-awsbhv001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHV001E (BHV) indica: "An unspecified error was encountered building the following message file !1 AWSBHV002E Unexpected error creating new SYMPHONY AWSBHV003E Unable to open CROSSREF help file AWSBHV004E An internal error has occurred. Stageman has found an incorrect reco".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 912. hwa-10.2.8-msg-awsbhv065e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHV065E (BHV) indica: "In the options for stageman there is an option that has a required argument, but that argument has not been supplied. The option in question is as follows: "!1". AWSBHV066E The following argument: "!1" is not valid for the "!2" option; perhaps it has".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 913. hwa-10.2.8-msg-awsbhw001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHW001E (BHW) indica: "A job name, file name or keyword is missing in the submitted command. AWSBHW002E The submitted command appears to contain extra or duplicated characters. AWSBHW003E There is a syntax error in the name. It must be between 1 and 16 bytes. AWSBHW004E Th".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 914. hwa-10.2.8-msg-awsbhx011w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHX011W (BHX) indica: "The job has negative elapsed time. Check the time parameters. 	Workstation : %-s# 	Job Stream  : %-s# 	Job         : %-s# 	Elapse time : %ld# 	Cpu time    : %ld# 	Start time  : %d# 	Start date  : %ld# 	Sched date  : %ld# 	Record Num  : %d# AWSBHX021E".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 915. hwa-10.2.8-msg-awsbhx027w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHX027W (BHX) indica: "The value specified for the "-timeout" connection parameter is not valid. It must be the number of seconds that the command line client is to wait for a connection before timing out. AWSBHX028I Updating statistics. Percentage complete: !1%. AWSBHX029".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 916. hwa-10.2.8-msg-awsbhz001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBHZ001E (BHZ) indica: "Schedulr cannot be run on this workstation, because the settings in the global options or the localopts file indicate that this workstation is not the master domain manager. AWSBHZ002E There is not enough memory available to run schedulr. AWSBHZ003W ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 917. hwa-10.2.8-msg-awsbia002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA002E (BIA) indica: "The identifier "!1" is required at this point,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 918. hwa-10.2.8-msg-awsbia003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA003E (BIA) indica: "A parameter or identifier has been supplied where it is".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 919. hwa-10.2.8-msg-awsbia004e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA004E (BIA) indica: "The delimiter "!1" is required at this point,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 920. hwa-10.2.8-msg-awsbia005e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA005E (BIA) indica: "Expected a !1 here. AWSBIA006E Error on database access. AWSBIA007E Security error. AWSBIA008E The supplied job stream !1#!2 could not be found. AWSBIA009E Error opening database. AWSBIA010E Autodoc not allowed for this job. AWSBIA011I !1: Old value ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 921. hwa-10.2.8-msg-awsbia018e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA018E (BIA) indica: "Job "!1" is already present in the job stream. AWSBIA019E For job stream !1#!2: errors !3, warnings !4. AWSBIA020E Mastsked not updated. AWSBIA021E Job "!1" does not exist in job stream".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 922. hwa-10.2.8-msg-awsbia022e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA022E (BIA) indica: "A file system error "!2"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 923. hwa-10.2.8-msg-awsbia023e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA023E (BIA) indica: "Job !1#!2 not found in job master. AWSBIA024E Job master changed while trying to update job !1#!2. Update aborted. Continue (enter "y" for yes, "n" for no)? # Command : %s # Workstation ID    Job stream         Creator                      Last Updat".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 924. hwa-10.2.8-msg-awsbia031e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA031E (BIA) indica: "An error has occurred writing the redirected output file "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 925. hwa-10.2.8-msg-awsbia032e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA032E (BIA) indica: "Error reading schedule. Errors occurred in the definition. Do you want to re-edit (enter "y" for yes, "n" for no)? # AWSBIA034E No job streams found in !1#!2 AWSBIA035I Found !1 job streams in !2#!3 AWSBIA036I Schedule !1#!2 has been deleted. AWSBIA0".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 926. hwa-10.2.8-msg-awsbia056i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA056I (BIA) indica: "Workstation !1 has been deleted. AWSBIA057E No resources were found. AWSBIA058I Found !1 resource(s). AWSBIA059I There is/are !1 Resource(s) in the database. AWSBIA060E Error modifying resources. Command : %s # Prompt    Description # --------  -----".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 927. hwa-10.2.8-msg-awsbia098e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA098E (BIA) indica: "A file system error "!2"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 928. hwa-10.2.8-msg-awsbia100e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA100E (BIA) indica: "CPU !1 does not exist in cpudata: !2 AWSBIA101E Only SCHEDULE or CPU can be specified here. Replace (enter "y" for yes, "n" for no)?# Okay to delete CPU definition !1? [N/Y]# Okay to delete Schedule definition !1#!2? [N/Y]# AWSBIA105E A file system e".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 929. hwa-10.2.8-msg-awsbia201e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA201E (BIA) indica: "You are not authorized to access job !1#!2. AWSBIA202I Found !1 jobs for !2#!3 AWSBIA203E No qualifying jobs were found in !1. AWSBIA204W For !1, errors !2, warnings !3. Command : %s # Workstation ID   Job                                      Logon  ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 930. hwa-10.2.8-msg-awsbia389e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIA389E (BIA) indica: "Composer was not able to obtain a valid default workstation from the value "!1". The error is: "!2". AWSBIA390E The specified cpu id could not be found. AWSBIA391E The required workstation name is missing. AWSBIA392E The specified workstation could n".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 931. hwa-10.2.8-msg-awsbib001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB001E (BIB) indica: "There is a syntax error. The time specified in the "at", "until", or "deadline" time definitions must be between 0000 and 2359 (hhmm). AWSBIB002E There is a syntax error. The job "limit" must be between 0 and 1024. AWSBIB003W The "resource number" mu".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 932. hwa-10.2.8-msg-awsbib039e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB039E (BIB) indica: "There is a syntax error. A numeric value (for example,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 933. hwa-10.2.8-msg-awsbib040e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB040E (BIB) indica: "There is a syntax error. An object identifier (for example,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 934. hwa-10.2.8-msg-awsbib041e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB041E (BIB) indica: "There is a syntax error. A date-related keyword has been supplied (for example, "deadline") but it is not followed by a date or day specification, or a calendar or iCalendar name. AWSBIB042E There is a syntax error. A "day", "weekday", or "workday" k".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 935. hwa-10.2.8-msg-awsbib044e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB044E (BIB) indica: "There is a syntax error. A time-related keyword (for example, "every") has been supplied, but its value is either missing or is not a valid time specification. AWSBIB045E There is a syntax error. An "opens" keyword has been supplied, but its value is".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 936. hwa-10.2.8-msg-awsbib201e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB201E (BIB) indica: "There is a syntax error. An object identifier (for example,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 937. hwa-10.2.8-msg-awsbib202e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB202E (BIB) indica: "There is a syntax error. An object identifier (for example,".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 938. hwa-10.2.8-msg-awsbib206e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIB206E (BIB) indica: "There is a syntax error. More than one parameter was specified. %.33s(%d) %.80s# AWSBIB208E There is a syntax error. The number of job stream dependencies exceeds the maximum number allowed. AWSBIB209E There is a syntax error. The number of job depen".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 939. hwa-10.2.8-msg-awsbic001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIC001E (BIC) indica: "An error occurred opening the database: !1 AWSBIC002E An error occurred opening the file "!1" for reading AWSBIC003E An error was returned from the parser. AWSBIC004E "!1" line !2, error looking for "!3#!4" job in database: !5 AWSBIC005E "!1" line !2".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 940. hwa-10.2.8-msg-awsbid001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBID001E (BID) indica: "Compiler cannot find the "thiscpu" option in the local options file (localopts). AWSBID002E Compiler cannot find the "master" option in either the localopts file or the global options. AWSBID003E Compiler cannot be run on this workstation, because th".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 941. hwa-10.2.8-msg-awsbie013e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIE013E (BIE) indica: "Error: input file "!1" and output file "!2" are identical This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or Message ending in a <br/> tag is not the last item in the subcomponent.                  C ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 942. hwa-10.2.8-msg-awsbif002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIF002E (BIF) indica: "Couldn't malloc program globals. AWSBIF003E Couldn't open output, error is: !1 AWSBIF004E Error writing output, error is: !1 User defined text# AWSBIF006E Error reading mastsked is: !1 AWSBIF007E Error finding next job stream is: !1 This is a dummy l".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 943. hwa-10.2.8-msg-awsbih104i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIH104I (BIH) indica: "-m The argument given is the month in mmyy format".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 944. hwa-10.2.8-msg-awsbih105i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIH105I (BIH) indica: "-o The argument given is the name of an output".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 945. hwa-10.2.8-msg-awsbii001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBII001E (BII) indica: "Unable to write token control structure. AWSBII002E No tokens in list. AWSBII003E Non-valid token "!1" in list (!2). AWSBII004E No read access to parameter in "!1". AWSBII005E Undefined parameter "!1" in string "!2"; not replaced. AWSBII006E Paramete".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 946. hwa-10.2.8-msg-awsbij001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIJ001E (BIJ) indica: "An internal error has occurred. Jobmon is unable to create a socket for communication with jobman. The error occurred in the following source code file: !1 at line: !2. The error message and error number are as follows: !3 : !4. AWSBIJ002E Unable to ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 947. hwa-10.2.8-msg-awsbij149e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIJ149E (BIJ) indica: "An internal error has occurred. Jobmon was unable to retrieve the security information for the HCL Workload Automation user object. The error occurred in the following source code file: !1 at line: !2. The error message and error number are as follow".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 948. hwa-10.2.8-msg-awsbik001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIK001E (BIK) indica: "Error creating socket !1:!2 error = !3. : !4. AWSBIK002E Unable to get host name !1:!2 error = !3. : !4. AWSBIK003E Unable to get host entries by name !1:!2 error = !3. : !4. AWSBIK004E Error binding socket to address !1:!2 error = !3. : !4. AWSBIK00".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 949. hwa-10.2.8-msg-awsbim001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIM001E (BIM) indica: "The workstation type does not match the workstation type in the database. AWSBIM002E The workstation "!1" is not a valid host. AWSBIM003E The domain name must be specified for this workstation definition. AWSBIM004E An extended agent "!1" cannot host".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 950. hwa-10.2.8-msg-awsbin001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIN001E (BIN) indica: "The workstation: "!1" has not been initialized yet. AWSBIN002E The workstation "!1" is already active. AWSBIN003E The workstation "!1" identified as the target for a switch manager operation is not a fault-tolerant agent. AWSBIN004E The domain manage".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 951. hwa-10.2.8-msg-awsbio001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIO001E (BIO) indica: "The supplied parameter "!1" is not valid. AWSBIO002E The supplied parameter "!1" does not have a valid length. AWSBIO003E The supplied parameter "!1" already exists. AWSBIO004E The supplied parameter "!2!1" has a non-alphabetic first character. AWSBI".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 952. hwa-10.2.8-msg-awsbip001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIP001E (BIP) indica: "A general failure occurred in file: !1 at line: !2. AWSBIP002E The object of type !1 is represented by a non-valid ID or handle in method !2 AWSBIP003E Either the object does not exist or its properties cannot be displayed with this Dynamic Workload ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 953. hwa-10.2.8-msg-awsbir001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIR001E (BIR) indica: "<unknown symphony record> Locale LANG set to the following: "!1"# AWSBIR100E option requires an argument -- %c AWSBIR101E illegal option -- %c AWSBIR102E Cannot open file '%s' This is a dummy label. It must be the last label in every subcomponent. It".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 954. hwa-10.2.8-msg-awsbis003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS003E (BIS) indica: "The following HCL Workload Automation configuration file does not exist: %s. AWSBIS004I Installed %s AWSBIS005I Saving %s as %s AWSBIS006I Attempting to remove %s AWSBIS007I The %s command installed as hard link AWSBIS008I The %s command installed as".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 955. hwa-10.2.8-msg-awsbis022i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS022I (BIS) indica: "HCL Workload Automation has been successfully installed. AWSBIS023E Unable to install %s properly. AWSBIS024E Customize has been launched with the '"-m <module_name>" option incorrectly specified more than once. AWSBIS025E Customize has been issued w".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 956. hwa-10.2.8-msg-awsbis065w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS065W (BIS) indica: "You are trying to install HCL Workload Automation in the following location: "%s" under the following group: "%s". However, there is already an instance installed in that location and group. AWSBIS066E HCL Workload Automation is already installed in ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 957. hwa-10.2.8-msg-awsbis067e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS067E (BIS) indica: "There is more than one entry for Netman in the same group. AWSBIS068W Netman is already installed in this group %s at location %s. AWSBIS069I Netman location for installation or update: %s AWSBIS070E The netman directory was not found.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 958. hwa-10.2.8-msg-awsbis071e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS071E (BIS) indica: "Netman customize failed during execution.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 959. hwa-10.2.8-msg-awsbis072e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS072E (BIS) indica: "An error occurred while creating or updating the components file. AWSBIS073I Replaced the calendars successfully. You might have calendars defined in your database.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 960. hwa-10.2.8-msg-awsbis115i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS115I (BIS) indica: "[-m <module-name>] -- <module-name> to be used to install module Usage: at [[-q<queue>] | [-s<job _stream>]] <time_specification> AWSBIS502E "at": You are not authorized to use the "at" command. This is a dummy label. It must be the last label in eve".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 961. hwa-10.2.8-msg-awsbis206e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS206E (BIS) indica: "Type %s calendars require a HOLIDAYS calendar to be predefined. AWSBIS207E Type %s calendars require a -s parameter. AWSBIS208E Your HCL Workload Automation license has expired. Valid options are: # 	-c <name>	Make a calendar with the given <name>. #".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 962. hwa-10.2.8-msg-awsbis235e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS235E (BIS) indica: "Day %s is not in range 1-31. AWSBIS236E Argument %s must be greater than zero. AWSBIS237E Argument %s is not in range 1-3. AWSBIS238E Incorrect option %s. AWSBIS239E One or more errors occurred. Calendars database not modified. See below. AWSBIS240E ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 963. hwa-10.2.8-msg-awsbis273e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS273E (BIS) indica: "More than one calendar option has been specified.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 964. hwa-10.2.8-msg-awsbis274e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS274E (BIS) indica: "Environment variable TEMP is not set.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 965. hwa-10.2.8-msg-awsbis275e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS275E (BIS) indica: "No argument was supplied with -freedays. Specify a valid calendar name. AWSBIS276E Cannot understand the NLS/Unknown format. Exiting. AWSBIS277E The non-working days (freedays) calendar %s is not found in the Symphony file.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 966. hwa-10.2.8-msg-awsbis278e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS278E (BIS) indica: "There is a syntax error in the command.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 967. hwa-10.2.8-msg-awsbis279e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS279E (BIS) indica: "Cannot determine the remote shell program. AWSBIS280E Cannot connect to %s. AWSBIS281E There is a syntax error in the command.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 968. hwa-10.2.8-msg-awsbis283e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS283E (BIS) indica: "Cannot determine the remote shell program. Cannot connect to %s".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 969. hwa-10.2.8-msg-awsbis285i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS285I (BIS) indica: " AWSBIS286E There is a syntax error in the command.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 970. hwa-10.2.8-msg-awsbis287e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS287E (BIS) indica: "Cannot connect to %s AWSBIS288E There is a syntax error in the command.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 971. hwa-10.2.8-msg-awsbis290e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS290E (BIS) indica: "No files were found in the file set. AWSBIS291E Jobstdl failed running: %s. AWSBIS292I Setting POSIX to true. AWSBIS293I Setting DATE to %s. AWSBIS294I Setting NAME to %s. AWSBIS295I Setting WHICH to %s. AWSBIS296I Setting SELECT to first. AWSBIS297I".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 972. hwa-10.2.8-msg-awsbis304i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS304I (BIS) indica: "File Status :%s: ==== AWSBIS305I ==== Exit Status :%s: ==== Usage: reptr [-V|-v|-U|-u] [-{pre|post}] [-{summary|detail}] <symfile> Usage: rep11 [-V|-v|-U|-u] | [-s job_stream] ... [-c workstation ...] ... [-m month ...] ... [-o out_file|-p pipe_comma".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 973. hwa-10.2.8-msg-awsbis335e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS335E (BIS) indica: "JnextPlan failed while running: %s. AWSBIS357I If you run the JnextPlan -for 0000 command while the enCarryForward option is not set to ALL, some job streams might not be carried forward. Type "y" for yes, "n" for no. AWSBIS358E JnextPlan was cancele".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 974. hwa-10.2.8-msg-awsbis338e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS338E (BIS) indica: "If you cannot resolve the problem, search the HCL Support database for a solution at https://www.hcltech.com/products-and-platforms/support. AWSBIS339E File %s does not exist. AWSBIS340E There is a syntax error in the command.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 975. hwa-10.2.8-msg-awsbis345e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS345E (BIS) indica: "An internal error has occurred. ResetPlan failed while running: %s. AWSBIS346W No Symphony file was found. Usage: MakePlan [-V| -U".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 976. hwa-10.2.8-msg-awsbis348e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIS348E (BIS) indica: "An internal error has occurred. MakePlan failed while running: %s. AWSBIS349E An internal error has occurred. SwitchPlan failed while running: %s. AWSBIS350W The application server is not running. AWSBIS351I The script "CheckPrerequisites" is startin".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 977. hwa-10.2.8-msg-awsbit006i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIT006I (BIT) indica: "Operations Center Threshold Monitor Condition		window. Usage: %s [-uname <name>] -master <nodename> [-operator <user>] [-password <user's password>] AWSBIT502E You must be root to install HCL Workload Automation OpC integration. AWSBIT503I Unknown pa".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 978. hwa-10.2.8-msg-awsbit508e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIT508E (BIT) indica: "Operations center not present on this system. AWSBIT509W Installing only event recognition. AWSBIT510W If not already done, this script should be run on the OpC".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 979. hwa-10.2.8-msg-awsbit511i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIT511I (BIT) indica: "Select the OpC version installed on your machine:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 980. hwa-10.2.8-msg-awsbit512i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIT512I (BIT) indica: "Enter choice [1-2]: \c AWSBIT513E Incorrect choice %s AWSBIT514E OpC 1.x is not supported on HP-UX 10.x AWSBIT515E Cannot determine the operating system version.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 981. hwa-10.2.8-msg-awsbiu001w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU001W (BIU) indica: "Magent already running. Usage: %s [-uname <name>] [-noinst] {[-ovwdir <dir>] | -manager <host>} AWSBIU502E You must be root to customize TWS AWSBIU503E Cannot reach node manager = %s. This must be a valid host name".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 982. hwa-10.2.8-msg-awsbiu101i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU101I (BIU) indica: "removing executing demons if any AWSBIU102E You must be root to decustomize TWS. AWSBIU103E Cannot determine OS version. Unable to define OpenView".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 983. hwa-10.2.8-msg-awsbiu105e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU105E (BIU) indica: "Error: Action is only valid for TWS events AWSBIU106E Error: Action not defined for TWS trap %s              õ   #      ö   k      ÷         ø  *      ù  ³      ú  Û      û  ø      ü  :      ý  \      þ        ÿ  ²         Ù  ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 984. hwa-10.2.8-msg-awsbiu504e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU504E (BIU) indica: "openview does not exist on this system.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 985. hwa-10.2.8-msg-awsbiu505i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU505I (BIU) indica: "modifying files for %s in %s AWSBIU506E %s already exists AWSBIU507I Copying the appropriate application registration file. AWSBIU508I Copying sample filters AWSBIU509I Copying the field registration AWSBIU510I Compiling the field registration AWSBIU".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 986. hwa-10.2.8-msg-awsbiu517i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU517I (BIU) indica: "Adding OVW path to TWS .profile AWSBIU518I /tmp/.profile contains the new version of %s .profile AWSBIU519I %s .profile has replaced the old file.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 987. hwa-10.2.8-msg-awsbiu520i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU520I (BIU) indica: "Adding traps to trapd.conf AWSBIU521I /tmp/trapd.conf contains the new version of %s/trapd.conf".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 988. hwa-10.2.8-msg-awsbiu522w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU522W (BIU) indica: "%s/trapd.conf has replaced the old file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 989. hwa-10.2.8-msg-awsbiu523i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU523I (BIU) indica: "changing ownership and permissions on programs AWSBIU524I IMPORTANT AWSBIU525W Be sure to add an appropriate entry to each workstation's rhost This could be '"<manager> <user>"' if a user other than tws will be # running the management station.  Or '".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 990. hwa-10.2.8-msg-awsbiu534w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU534W (BIU) indica: "/etc/snmpd.peers has been replaced the old file is /etc/snmpd.peers.old AWSBIU535E /tmp/snmpd.conf contains the new version of /etc/snmpd.conf".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 991. hwa-10.2.8-msg-awsbiu536w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU536W (BIU) indica: "/etc/snmpd.conf has been replaced the old file is /etc/snmpd.conf.old AWSBIU537I Recompile the defs for this machine AWSBIU538E /tmp/mib.defs contains the new version of /etc/mib.defs".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 992. hwa-10.2.8-msg-awsbiu539w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU539W (BIU) indica: "/etc/mib.defs has been replaced the old file is /etc/mib.defs.old AWSBIU540W After you have installed the changes to the system files you".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 993. hwa-10.2.8-msg-awsbiu541i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU541I (BIU) indica: "Refreshing snmpd AWSBIU542I Setting up the agent files AWSBIU543I Copying the configuration files. AWSBIU544W /tmp/StartUp contains the new version of %s/StartUp".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 994. hwa-10.2.8-msg-awsbiu545w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU545W (BIU) indica: "%s/StartUp has been replaced AWSBIU546W You should now restart Netview/Openview and TWS AWSBIU547I Select the OV version installed on your machine:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 995. hwa-10.2.8-msg-awsbiu548i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU548I (BIU) indica: "Enter choice [1-2]: \c AWSBIU549E Invalid choice %s. AWSBIU550E ERROR: OpenView 3.3 is not supported on HP-UX 10.x AWSBIU551E -client option can only be specified on AIX AWSBIU552E The trap definition file <maehome>/OV/mae.traps.hp must be loaded".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 996. hwa-10.2.8-msg-awsbiu553e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU553E (BIU) indica: "The trap definition file <maehome>/OV/mae.traps.aix must be loaded".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 997. hwa-10.2.8-msg-awsbiu554e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU554E (BIU) indica: "The file %s is missing. This file is needed to configure the".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 998. hwa-10.2.8-msg-awsbiu555i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIU555I (BIU) indica: "Linking to mdemon and muser OV 3.3 static executables AWSBIU556I Linking to mdemon and muser OV 4.x dynamic executables AWSBIU557E Cannot determine OS version. Unable to define OpenView".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 999. hwa-10.2.8-msg-awsbiv001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIV001E (BIV) indica: "Command too long. AWSBIV002E Remote aborted connection without initiating protocol: %d. AWSBIV003E Remote aborted connection: %s AWSBIV004E Failed to shutdown input socket AWSBIV005I ** Result return = %lu ** AWSBIV006E Can't get user name. Usage: me".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1000. hwa-10.2.8-msg-awsbix002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIX002E (BIX) indica: "Customize failed executing: %s.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1001. hwa-10.2.8-msg-awsbix003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIX003E (BIX) indica: "FILE:%s does not exist. AWSBIX004I Installed %s AWSBIX005I Looking up user %s in /etc/passwd AWSBIX006W User %s not found in /etc/passwd. Trying yellow pages. AWSBIX007E Yellow Pages not installed or not accessible in PATH. AWSBIX008E User %s not fou".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1002. hwa-10.2.8-msg-awsbix018e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIX018E (BIX) indica: "Netman home %s does not exist. AWSBIX019E 'netman' directory tree exists partially or does not exist.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1003. hwa-10.2.8-msg-awsbix020e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIX020E (BIX) indica: "ERROR: Error occured while creating/updating product components file. AWSBIX021E An error occured executing commands.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1004. hwa-10.2.8-msg-awsbix022i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIX022I (BIX) indica: "Netman installed. AWSBIX023I Netman updated. Usage: %s [-V|-v|-U|-u] This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or Message ending in a <br/> tag is not the last item in the subcomponent.          ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1005. hwa-10.2.8-msg-awsbiy001w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIY001W (BIY) indica: "Running the sample database setup deletes".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1006. hwa-10.2.8-msg-awsbiy004i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIY004I (BIY) indica: "The sample job streams and jobs are not installed. Exiting. Press "Enter" key to continue. ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1007. hwa-10.2.8-msg-awsbiz001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBIZ001E (BIZ) indica: "Error: CreateProcess failed. AWSBIZ002E Error: system failed. AWSBIZ003I system return status %d. AWSBIZ004E %s does not exist. This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or Message ending in a <br".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1008. hwa-10.2.8-msg-awsbjb002i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJB002I (BJB) indica: "Starting clagent AWSBJB003I Read message: !1 AWSBJB004I Ok processing the message: !1 AWSBJB005I clagent down! AWSBJB006E Error processing the message: !1 AWSBJB007I Adapter Ok AWSBJB008E Adapter error: !1 AWSBJB009I Initialization clagent OK AWSBJB0".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1009. hwa-10.2.8-msg-awsbjb100i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJB100I (BJB) indica: "Job stream is in ready status AWSBJB101I Job stream is in hold status AWSBJB102I Job stream is in exec status AWSBJB103I Job stream is in stuck status AWSBJB104I Job stream is in abend status AWSBJB105I Job stream is in successful status AWSBJB106I J".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1010. hwa-10.2.8-msg-awsbjg001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJG001E (BJG) indica: "Router cannot initialize the communication or set the connection type and file descriptor for the connected socket to make an SSL connection to conman. The following error message is given: !1 AWSBJG002E Router is unable to create the stdlist file. U".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1011. hwa-10.2.8-msg-awsbjh005e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH005E (BJH) indica: "The datamigrate parameter "!1" has been supplied".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1012. hwa-10.2.8-msg-awsbjh006e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH006E (BJH) indica: "An incorrect value has been supplied for a parameter. AWSBJH007I Use the command "datamigrate -u" to see the usage and options. AWSBJH008I The parameter must be as follows: "!1". AWSBJH009E More than one object type parameter has been supplied. AWSBJ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1013. hwa-10.2.8-msg-awsbjh011e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH011E (BJH) indica: "The parameter "!1" is not a recognized datamigrate".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1014. hwa-10.2.8-msg-awsbjh012e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH012E (BJH) indica: "One or more required parameters of the "datamigrate"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1015. hwa-10.2.8-msg-awsbjh013e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH013E (BJH) indica: "Two or more incompatible parameters of the "datamigrate"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1016. hwa-10.2.8-msg-awsbjh014e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH014E (BJH) indica: "The supplied input file "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1017. hwa-10.2.8-msg-awsbjh015i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH015I (BJH) indica: "Check the supplied file name. Check that the file exists".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1018. hwa-10.2.8-msg-awsbjh016e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH016E (BJH) indica: "The supplied "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1019. hwa-10.2.8-msg-awsbjh017i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH017I (BJH) indica: "Check the supplied directory name. Check that the".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1020. hwa-10.2.8-msg-awsbjh018e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH018E (BJH) indica: "The temporary directory "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1021. hwa-10.2.8-msg-awsbjh019i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH019I (BJH) indica: "Check the supplied directory name. Check that the".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1022. hwa-10.2.8-msg-awsbjh020i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH020I (BJH) indica: "The import of object type "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1023. hwa-10.2.8-msg-awsbjh021i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH021I (BJH) indica: "Check the results of the import in the log file "!1". AWSBJH022E The import of object type "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1024. hwa-10.2.8-msg-awsbjh023w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH023W (BJH) indica: "The import of object type "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1025. hwa-10.2.8-msg-awsbjh024w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH024W (BJH) indica: "No object of type "!1" has been found. AWSBJH025I No objects of type "!1" can be found in the file".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1026. hwa-10.2.8-msg-awsbjh026e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH026E (BJH) indica: "The import of object type "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1027. hwa-10.2.8-msg-awsbjh027i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH027I (BJH) indica: "Check the log file "!1" and examine the errors.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1028. hwa-10.2.8-msg-awsbjh028i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH028I (BJH) indica: "The file of imported objects is empty.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1029. hwa-10.2.8-msg-awsbjh029e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH029E (BJH) indica: "The supplied input file "!1" is not readable by the user "!2" that is performing the data migration. AWSBJH030I The user might not have the correct access rights".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1030. hwa-10.2.8-msg-awsbjh031e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH031E (BJH) indica: "The application server is not running. The import cannot continue. AWSBJH032I Start the application server then rerun the "datamigrate" utility. AWSBJH033I The import of the topology has completed. Check the results for the individual object types in".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1031. hwa-10.2.8-msg-awsbjh035e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH035E (BJH) indica: "The migration was unable to export the data from the previous instance of HCL Workload Automation, because it could not copy the "dataexporter" program into the directory: "!1". AWSBJH036I Check that there is sufficient space in the fileset where the".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1032. hwa-10.2.8-msg-awsbjh104e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH104E (BJH) indica: "The supplied object type "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1033. hwa-10.2.8-msg-awsbjh105i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH105I (BJH) indica: "Permitted values are "topology", "calendars", "parms",".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1034. hwa-10.2.8-msg-awsbjh106i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH106I (BJH) indica: "Exporting object type "!1" from the".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1035. hwa-10.2.8-msg-awsbjh107i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBJH107I (BJH) indica: "The export has completed successfully. ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1036. hwa-10.2.8-msg-awsbwx002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSBWX002E (BWX) indica: "An error has occurred opening the file "!1" for writing. AWSBWX003E An error has occurred opening the file "!1" for reading. AWSBWX004E An error has occurred writing the file "!1". AWSBWX005E An error has occurred renaming the file "!1" in "!2". AWSB".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1037. hwa-10.2.8-msg-awscdw001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW001I (CDW) indica: "The cluster service is installed, configured, and running on the node "!1". AWSCDW002E The cluster service is installed and configured on the node "!1", but is not currently running. AWSCDW003E The cluster service is not installed on the node. AWSCDW".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1038. hwa-10.2.8-msg-awscdw034e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW034E (CDW) indica: "The program cannot determine the path to the custom HCL Workload Automation cluster resource type dll. AWSCDW035E The program cannot update the custom HCL Workload Automation cluster resource type dll. AWSCDW036W The program cannot delete the tempora".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1039. hwa-10.2.8-msg-awscdw038i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW038I (CDW) indica: "The custom HCL Workload Automation cluster resource type dll has been successfully upgraded on node "!1". AWSCDW039W The program cannot create the script to start or stop the HCL Workload Automation custom cluster resource instance. ===========".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1040. hwa-10.2.8-msg-awscdw042e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW042E (CDW) indica: "The command-line parameter "!1" is not correct. AWSCDW043E The context of the supplied command line string "!1"indicates that a pair of quotation symbols (') is required. However, the first of the pair is missing. AWSCDW044E The context of the suppli".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1041. hwa-10.2.8-msg-awscdw056e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW056E (CDW) indica: "VocÃª nÃ£o forneceu um nome".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1042. hwa-10.2.8-msg-awscdw057e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW057E (CDW) indica: "Ocorreu um erro ao gerar o".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1043. hwa-10.2.8-msg-awscdw058i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW058I (CDW) indica: "O coletor gerou com".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1044. hwa-10.2.8-msg-awscdw059i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW059I (CDW) indica: "Implementando o archive de".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1045. hwa-10.2.8-msg-awscdw060i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW060I (CDW) indica: "O coletor nÃ£o possui".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1046. hwa-10.2.8-msg-awscdw061e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW061E (CDW) indica: "Erro ao implementar o".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1047. hwa-10.2.8-msg-awscdw071e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW071E (CDW) indica: "VocÃª especificou um nome".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1048. hwa-10.2.8-msg-awscdw072e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW072E (CDW) indica: "VocÃª especificou um parÃ¢metro incorreto: "!1" AWSCDW073I O coletor implementou com".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1049. hwa-10.2.8-msg-awscdw075w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW075W (CDW) indica: "O agente nÃ£o pode".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1050. hwa-10.2.8-msg-awscdw076i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW076I (CDW) indica: "Somente o agente dinÃ¢mico serÃ¡ instalado. Qualquer outra opÃ§Ã£o serÃ¡ ignorada. AWSCDW077E Nenhum agente estÃ¡".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1051. hwa-10.2.8-msg-awscdw078e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSCDW078E (CDW) indica: "NÃ£o Ã© possÃ­vel".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1052. hwa-10.2.8-msg-awsdab001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDAB001I (DAB) indica: "HCL C @(#) D.02 $Header: /usr/local/SRC_CLEAR/maestro/JSS/utils/catalog/RCS/C.msg,v 7.80.1.16 1999/05/06 21:53:33 pl Exp $                 ^  F   æ   `       AWSDAE003E Unexpected file system error Reading $STDIN AWSDAE005E Unexpected file syste".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1053. hwa-10.2.8-msg-awsdab002i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDAB002I (DAB) indica: "@(#) Copyright IBM Corp. 1991, 2016 - Copyright HCL Technologies Ltd. 2016                      ¶  Ý       AWSDAH001I Your HCL Software is valid through !1. AWSDAH002E Your HCL Software demo has expired. AWSDAH003E Software is incompatible wi".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1054. hwa-10.2.8-msg-awsdal002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDAL002E (DAL) indica: "Unknown audit type !1 passed.               2  s    ð     	    AWSDBY002E Too many parameters in RUN command AWSDBY025E Expected "G", "P", or "S" AWSDBY026E Expected a number AWSDBY027E Missing close quote AWSDBY028E Missing program name AWSDB".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1055. hwa-10.2.8-msg-awsdcj001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDCJ001E (DCJ) indica: "Error opening existing stdin, Error: !1 AWSDCJ002E Error purging old stdin, Error: !1 AWSDCJ003E Error building stdin, Error: !1 AWSDCJ004E Error closing new stdin, Error: !1 AWSDCJ005E Error opening new stdin, Error: !1 AWSDCJ006E Error opening old ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1056. hwa-10.2.8-msg-awsdcj200w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDCJ200W (DCJ) indica: "Parado com saÃ­da %d AWSDCJ201I Parado normalmente AWSDCJ202W Parado por: AWSDCJ203W Parado por sinal: %d                          >         U       d  Ù    ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1057. hwa-10.2.8-msg-awsddw001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDDW001I (DDW) indica: "Building stdlist directory !1. AWSDDW052E Product '!1' is not installed under the group '!2'. AWSDDW053W No '!1' found in components file installed under '!2'. AWSDDW071E You specified an invalid product. AWSDDW100I SWITCHED               4   *     ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1058. hwa-10.2.8-msg-awsddw002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDDW002E (DDW) indica: "Unable to build stdlist directory !2. Errno = !1. AWSDDW008E An I/O error occurred while accessing a file. A memory dump has been taken to aid HCL Software Support with problem determination. AWSDDW051E Unknown product id <!1> found.               ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1059. hwa-10.2.8-msg-awsdeb001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEB001I (DEB) indica: "Getting a new socket: !1 AWSDEB002I Reading socket: !1 AWSDEB003I Writing socket: !1 AWSDEB004I Shutting down socket: !1 AWSDEB005I Closing socket: !1 AWSDEB006I Binding socket: !1 AWSDEB007I Connecting socket: !1 AWSDEB008I Accepting a connection: !".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1060. hwa-10.2.8-msg-awsdeb051e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEB051E (DEB) indica: "The program cannot authenticate the SSL peer certificate: the requested level is not matched. AWSDEB052E An error occurred in getaddrinfo: !1 (getting the host IP address using the host name). AWSDEB053E FIPS cannot be enabled. The connection is not ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1061. hwa-10.2.8-msg-awsdeb055e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEB055E (DEB) indica: "Ocorreu um erro durante uma conexÃ£o SSL usando as bibliotecas OpenSSL. AWSDEB056E Ocorreu um erro na conexÃ£o SSL usando o OpenSSL Toolkit. A conexÃ£o nÃ£o pode ser aceita. AWSDEB057E Ocorreu um erro na conexÃ£o SSL usando as bibliotecas OpenSSL. A ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1062. hwa-10.2.8-msg-awsdec001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEC001E (DEC) indica: "File system error !1 on events file. AWSDEC002E An internal error has occurred. The following UNIX system error occurred on an events file: "!1" at line = !2. AWSDEC003I End of file on events file. AWSDEC004E IPC error !1 on events file. AWSDEC005E D".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1063. hwa-10.2.8-msg-awsdec008e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEC008E (DEC) indica: "An event file was created by a newer version of HCL Workload Scheduler than this version, and is not compatible. AWSDEC009E An event file cannot be opened because it has been already opened by another process. AWSDEC014E The event file or the directo".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1064. hwa-10.2.8-msg-awsded001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDED001E (DED) indica: "internal error: time() failed AWSDED002E An internal error has occurred: mktime() failed. AWSDED003E An internal error has occurred: localtime() failed. AWSDED004E An internal error has occurred: gmtime() failed. AWSDED005E An internal error has occu".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1065. hwa-10.2.8-msg-awsdef001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEF001E (DEF) indica: "Can not acquire heap. AWSDEF002E On IPCDEST: !1 AWSDEF003E On IPCONNECT: !1 AWSDEF004E On IPCRECV: !1 AWSDEF005E On setting timeout: !1 AWSDEF006E On IPCREVCVCN: !1 AWSDEF007E On IPCGIVE: !1 AWSDEF008E On IPCGET: !1 AWSDEF009E This is not an IPC coma".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1066. hwa-10.2.8-msg-awsdef010i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEF010I (DEF) indica: "No error. !1    ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1067. hwa-10.2.8-msg-awsdeg001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEG001E (DEG) indica: "Error: no comarea exists yet. AWSDEG002E Error: This is not a valid comarea for isam access. AWSDEG003W Warn: Isam access on !1, this operation not implemented. AWSDEG004E Error: !1, is not open yet. AWSDEG005E Error: !1, is not locked yet. AWSDEG006".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1068. hwa-10.2.8-msg-awsdeg014e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEG014E (DEG) indica: "Error: On !1, Close error: !3 AWSDEG015E Error: On !1, Lock error: !3 AWSDEG016E Error: On !1, Already locked. AWSDEG017E Error: On !1, Unlock error: !3 AWSDEG018E Error: Can not malloc comarea: !1 AWSDEG019E Error: On !1, Can not open file: !3 AWSDE".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1069. hwa-10.2.8-msg-awsdeh001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEH001E (DEH) indica: "Error: Incorrect Delimiter AWSDEH002E Error: Call type mismatch on !1, requires !2 AWSDEH003W Warning: Requires type !1, operand type is !2 AWSDEH004E Error: Keyword not found. AWSDEH005E Error: Command not found, use Help. AWSDEH006E Error: Type not".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1070. hwa-10.2.8-msg-awsdei003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEI003E (DEI) indica: "System error !1 trying to open !2 for input. AWSDEI004E System error !1 trying to open !2 for output.                  8       q  Gá  F©  :         AWSDEJ002E The internal data structure area (comarea) could not be initialized. AWSDEJ003E Doing".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1071. hwa-10.2.8-msg-awsdek051e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEK051E (DEK) indica: "Options must precede arguments, use -- to close options. AWSDEK052E An option was not valid. AWSDEK053E An option was ambiguous. AWSDEK054E An option was not found. AWSDEK101E Error accessing !1: !2 AWSDEK301E Error opening work file !1: !2 AWSDEK302".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1072. hwa-10.2.8-msg-awsdek102e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEK102E (DEK) indica: "An error occurred while rebuilding !1: !2. !1 rebuilt successfully.# Usage: fileinfo [ -V|-U|path [...]# Usage: makesec [ -V | -U ]".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1073. hwa-10.2.8-msg-awsdek406e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEK406E (DEK) indica: "Error writing security file !1 to the screen. Usage: dummy [ -V | -U ]# usage: evtsize {-V | -U | -show <file_name> | -compact <file_name> [<new_size>] | <file_name> <new_size>} usage: mkproto [options][files ...]# Options are:# -n: Put line numbers ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1074. hwa-10.2.8-msg-awsdel001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEL001E (DEL) indica: "Error, attempt to open newer revision of file AWSDEL002E Error, cpudata file has not been opened AWSDEL003W End of chain/no more matches. AWSDEL004E Could not create a temporary file: !1 AWSDEL005E File system error: !1 AWSDEL006E cpu not specified i".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1075. hwa-10.2.8-msg-awsdem001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEM001E (DEM) indica: "There is an error in the workstation definition. The workstation definition for the "cpuname" keyword is not syntactically correct. It must start with an alphabetic character, followed by up to 15 alphanumeric bytes, including dashes and underscores.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1076. hwa-10.2.8-msg-awsden002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEN002E (DEN) indica: "Cannot change software to demo".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1077. hwa-10.2.8-msg-awsden003w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEN003W (DEN) indica: "Software has been converted to a seven day demo. AWSDEN004E This is not production software. AWSDEN005E Can't determine software type.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1078. hwa-10.2.8-msg-awsdeo001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEO001E (DEO) indica: "Snmp error for !1 in !2: !3 AWSDEO002E SNMP allocate error for !1 in !2: !3 AWSDEO003E SNMP unknown case is for !1 in !2: !3 AWSDEO004E OV no pmd. Doing !1 in !2. Error: !3 AWSDEO005I Normal exit for !1 in !2. AWSDEO006E OV unknown pmd command. !1, !".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1079. hwa-10.2.8-msg-awsdep001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEP001E (DEP) indica: "Fifo error in !1, call !2, error: !3 AWSDEP002E Fifo error opening connection for !1: !2 AWSDEP003E Fifo error allocating space in !1 for !2: !3 AWSDEP004E Fifo receive error on !1: !2 AWSDEP005E Unknown case in !2, on !1, line !3, value !4 AWSDEP006".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1080. hwa-10.2.8-msg-awsdeq001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEQ001E (DEQ) indica: "Error setting thread token !1:!2 message = !3. AWSDEQ002E Error creating file !1:!2 message = !3. AWSDEQ003E Error setting name pipe mode !1:!2 message = !3. AWSDEQ004E Error writing to file !1:!2 message = !3. AWSDEQ005E Error connecting to pipe !1:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1081. hwa-10.2.8-msg-awsdeq021e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEQ021E (DEQ) indica: "HCL Workload Scheduler Token Service is not running, restart the service.               }  C0  C$  Bÿ   %       Usage: !1 CSName InputFile OuputFile               ~  Ft  E¨  CL  \       AWSDEW001E Invalid flag Try -u for usage. AWSDEW003E More t".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1082. hwa-10.2.8-msg-awsder001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDER001E (DER) indica: "Malloc failed !1:!2 error = !3. AWSDER002E Calloc failed !1:!2 error = !3. AWSDER003E Realloc failed !1:!2 error = !3.                  +          V       z  ºN  ¹  µé         AWSDES001E Expected the keyword USERNAME. AWSDES002E Expected a val".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1083. hwa-10.2.8-msg-awsdet001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDET001E (DET) indica: "Error, attempt to open newer revision of file AWSDET002E Error, userdata file has not been opened AWSDET003E End of chain/no more matches. AWSDET004E Couldn't create a temporary file: !1 AWSDET005E File system error: !1 AWSDET006E user not specified ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1084. hwa-10.2.8-msg-awsdeu001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEU001E (DEU) indica: "**ERROR** Adding domain !1 would cause a loop in the domain hierarchy. AWSDEU002I At beginning of list. AWSDEU003I At end of list. AWSDEU004E Attempt to add item to list pointed to by null pointer. AWSDEU005E Attempt to delete from a list pointed to ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1085. hwa-10.2.8-msg-awsdev001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEV001E (DEV) indica: "Unable to open input file !1 for reading. AWSDEV002E Unable to examine input file !1. AWSDEV003E Unable to allocate input buffer. AWSDEV004E Unable to allocate output buffer. AWSDEV005E Unable to read input file !1. AWSDEV006E The user ID that is usi".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1086. hwa-10.2.8-msg-awsdez001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDEZ001E (DEZ) indica: "Call count exceeded, serious bug AWSDEZ002E ISSUEMSG Internal error at line %d AWSDEZ003E **ERROR**(cpu secs %li) AWSDEZ004E **ERROR**                  ,          Z          }         Õé  ÕÝ  Õµ   (       %*.*s%*.*s %*.*s%*.*s%*.*s%*.*sPage%5d#".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1087. hwa-10.2.8-msg-awsdfe001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFE001E (DFE) indica: "File system error %d opening uconfig. AWSDFE002E File system error %d creating uconfig. AWSDFE003E Error %d reading uconfig. AWSDFE004E File system error %d writing uconfig. AWSDFE005E File system error %d closing uconfig. Syntax: psetcode -action[pa".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1088. hwa-10.2.8-msg-awsdfe025w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFE025W (DFE) indica: "WARNING: Extra parameters ignored starting at: "!1" usage: psetcode -{h|c|d|i|n|U|u|V|v<validation code>|n<company name>} usage: psetcode -{h|d|i|U|V|v<validation code>} AWSDFE028I Company name: %s	Validation Code: %d Models allowed:# AWSDFE030E No m".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1089. hwa-10.2.8-msg-awsdff001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFF001I (DFF) indica: "Invoking prog =%s AWSDFF002E execv failed; error %d AWSDFF003E setuid failed; error %d                            ?         ìò  ìn  êR         AWSDFG002E STARTER:Error calling logon user : %d AWSDFG003E STARTER:Error setuid failed: %s AWSDFG0".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1090. hwa-10.2.8-msg-awsdfh001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFH001E (DFH) indica: "The following success condition comparison expression is missing one of a pair of parentheses: !1 AWSDFH002E The success condition comparison expression either contains an unsupported operator or an operator used incorrectly: !1.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1091. hwa-10.2.8-msg-awsdfh003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFH003E (DFH) indica: "The following output condition comparison expression is incorrect: "!1".                  m         Î    ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1092. hwa-10.2.8-msg-awsdfh004e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSDFH004E (DFH) indica: "The success condition comparison expression contains the following non-valid operand: !1. The operand must be an integer between -2147483647 and 2147483647.               ê      I=  Gâ  [       Licensed Materials - Property of IBM* and HCL**".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1093. hwa-10.2.8-msg-awsedw001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSEDW001E (EDW) indica: "The following value: "!2" for the following netman command line option: "!1" is not in the correct format. AWSEDW003W Not running with root permissions AWSEDW005E Netman was unable to open its configuration file: !1. The following error was given by ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1094. hwa-10.2.8-msg-awsedw002e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSEDW002E (EDW) indica: "System error AWSEDW004E Message file already opened by another process: !1, !2 AWSEDW006E Netman could not process the service information in its configuration file: "!1". If the problem is with a specific entry, the details are as follows (if the fo".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1095. hwa-10.2.8-msg-awsedw020e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSEDW020E (EDW) indica: "An internal error has occurred. Netman was unable to set up its TCP/IP port to listen for service requests. The following operating system message was received: !1. AWSEDW022E An internal error has occurred. Netman encountered an IPC error when waiti".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1096. hwa-10.2.8-msg-awsedw042i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSEDW042I (EDW) indica: "Terminating, no sons active AWSEDW052W IP address validation not performed for request: !1. Connection received from IP address: !2. !3. Service request accepted. AWSEDW053E Netman could not validate the IP address for a service.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1097. hwa-10.2.8-msg-awsfab003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB003E (FAB) indica: "The twsinst script cannot run on this operating system: !1. AWSFAB004E Only the user "root" can run the twsinst script. AWSFAB005E No parameters have been specified for twsinst. AWSFAB006I Use the command "!1" to see a list of the available parameter".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1098. hwa-10.2.8-msg-awsfab132e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB132E (FAB) indica: "The uninstallation process failed for one of these reasons:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1099. hwa-10.2.8-msg-awsfab133e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB133E (FAB) indica: "Either the "-password" parameter is missing, or an incorrect value has been supplied for a parameter. The parameter must be as follows: "!1". AWSFAB134E You specified an incorrect password for the user !1. AWSFAB135E The "!1" user account you supplie".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1100. hwa-10.2.8-msg-awsfab173e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB173E (FAB) indica: "Operating system version is not supported. AWSFAB174E AIX operating system maintanance package is not supported. AWSFAB175E Found library !1 but not !2. Softlink !3 to !4. AWSFAB176E Library libXp.so.6 and libXmu.so.6 are not found.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1101. hwa-10.2.8-msg-awsfab177e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB177E (FAB) indica: "Required libraries are not installed on the running system. AWSFAB178E 32-bit AIX operating system is not supported.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1102. hwa-10.2.8-msg-awsfab179e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB179E (FAB) indica: "The AIX maintanance package !1 is not supported.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1103. hwa-10.2.8-msg-awsfab180e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB180E (FAB) indica: "The AIX fix !1 was not found on the running system. AWSFAB181E C++ runtime level !1 not supported.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1104. hwa-10.2.8-msg-awsfab182i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB182I (FAB) indica: "Disk space successfully checked on file system AWSFAB183I Disk swap space successfully checked AWSFAB184I Memory requirements successfully checked AWSFAB185I Prerequisites check complete AWSFAB186I The path provided !1 does not contain a Websphere Ap".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1105. hwa-10.2.8-msg-awsfab204i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB204I (FAB) indica: "Release level !1 successfully checked. AWSFAB205E The operating system release level is not supported.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1106. hwa-10.2.8-msg-awsfab206i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB206I (FAB) indica: "Check security patches ... AWSFAB207I Check cluster patch !1 ... AWSFAB208I Opening text file !1. AWSFAB209I WebSphere patches successfully checked. AWSFAB210I The minimum patch !1 was found on the running system. AWSFAB211W The minimum required patc".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1107. hwa-10.2.8-msg-awsfab219e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB219E (FAB) indica: "Hardware model !1 not supported.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1108. hwa-10.2.8-msg-awsfab220w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB220W (FAB) indica: "Recommended memory requirements are not satisfied. AWSFAB221E The Memory requirements are not satisfied.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1109. hwa-10.2.8-msg-awsfab222i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB222I (FAB) indica: "No kernel requirement checks are necessary. AWSFAB223I Kernel parameters successfully checked. AWSFAB224W Kernel parameter !1 not defined. AWSFAB225E Kernel parameter !1 not defined. AWSFAB226I Base kernel level required value: !1. AWSFAB227I Kernel ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1110. hwa-10.2.8-msg-awsfab247e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB247E (FAB) indica: "The user account you specified: "!1" is a reserved IBM i User Profile. You cannot use a reserved account. Specify an existing user account different from the following reserved accounts: "QDBSHR", "QDFTOWN", "QDOC", "QLPAUTO", "QLPINSTALL", "QRJE", "".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1111. hwa-10.2.8-msg-awsfab284e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB284E (FAB) indica: "The Linux !1 service pack !2 is not supported. Update the Operating system to service pack !3. AWSFAB285I Update the patch.info file AWSFAB286E The eImage on your workstation is corrupt. You must run the TAR command on QP2TERM or AIXTERM shell to unt".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1112. hwa-10.2.8-msg-awsfab295w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB295W (FAB) indica: "You can add the runtime for Java job plug-ins only to dynamic agents or HCL Workload Automation for z/OS agents with dynamic capabilities.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1113. hwa-10.2.8-msg-awsfab296e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB296E (FAB) indica: "The operation -restore for the user !1 cannot be performed, because the instance you want to restore is not at version !2 or later. AWSFAB301I Usage:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1114. hwa-10.2.8-msg-awsfab302i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB302I (FAB) indica: "twsClusterUpg.vbs v. 1.0".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1115. hwa-10.2.8-msg-awsfab303e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB303E (FAB) indica: "The parameter !1 is invalid. AWSFAB304E You cannot specify the -passwords parameter if you do not specify the -groups parameter. AWSFAB305E You specified an invalid path. The specified path !1 is not valid either because it does not exist or because ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1116. hwa-10.2.8-msg-awsfab416e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB416E (FAB) indica: "A parameter to twsinst has been supplied that is not appropriate for the supplied installation type. Specify the -password parameter only when new installation type is specified. AWSFAB417E An incorrect value has been supplied for the parameter "-pas".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1117. hwa-10.2.8-msg-awsfab435i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB435I (FAB) indica: "Restoring the instance AWSFAB436E The agent update failed. The files of the previous version will be restored. After restoring the previous version, the agent will continue to work normally. AWSFAB437E The restore operation of the previous version co".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1118. hwa-10.2.8-msg-awsfab468e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB468E (FAB) indica: "The gateway_eif_port "!1" is already used by another instance installed in directory "!2". Please specify some other port value. ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1119. hwa-10.2.8-msg-awsfab470e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB470E (FAB) indica: "The reinstall of the selected instance failed, for one of the following reasons:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1120. hwa-10.2.8-msg-awsfab471e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB471E (FAB) indica: "The parameter you have supplied: "!1" must be followed by a value. AWSFAB472E The directory "!1" you have supplied with parameter: "!1" does not contain file "!1". AWSFAB473E You have supplied parameter: "!1" but you have not supplied parameter: "!1"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1121. hwa-10.2.8-msg-awsfab479i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB479I (FAB) indica: "Importing certificates. AWSFAB480E The supplied directory "!1" does not exist. AWSFAB482E If you set the -useencryption parameter to true, the -addjruntime parameter must also be set to true. This is because Java is required to set up the encryption.".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1122. hwa-10.2.8-msg-awsfab501e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAB501E (FAB) indica: "The "!1" file in the depot folder on the master domain manager <datadir>/ssl/depot (UNIX), <installation_dir>TWSssldepot (Windows) must contain a password encoded with Base64 encoding. AWSFAB502E Specify either the sslkeysfolder and sslpassword param".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1123. hwa-10.2.8-msg-awsfaf003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAF003E (FAF) indica: "The twspatch script cannot run on this operating system: !1. AWSFAF004E Only the user "root" can run the twspatch script. AWSFAF005E No parameters have been specified for twspatch. AWSFAF006I Use the command "twspatch -u" to see a list of the availab".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1124. hwa-10.2.8-msg-awsfaf046e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSFAF046E (FAF) indica: "The "!1" user account you supplied does not exist on the local computer. The patching cannot proceed. AWSFAF047E You specified an incorrect password for the user !1. AWSFAF048I The "!1" operation completed successfully. AWSFAF132E The uninstallation ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1125. hwa-10.2.8-msg-awsgtw101e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSGTW101E (GTW) indica: "The specified parameter "!1" is not valid. AWSGTW102E The arguments exceed the maximum input size. AWSGTW103E The parameter "!1" has been specified more than once. AWSGTW104E The parameters "!1" and "!2" are specified in the wrong order. AWSGTW105E T".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1126. hwa-10.2.8-msg-awsgtw120e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSGTW120E (GTW) indica: "The following error occurred while opening the template configuration file "!1": !2. AWSGTW121E The parameters "!1" and "!2" cannot both be specified. This is a dummy label. It must be the last label in every subcomponent. It ensures that a Label or ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1127. hwa-10.2.8-msg-awsita001e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA001E (ITA) indica: "O comando estÃ¡ incorreto e nÃ£o pode ser processado. AWSITA002E NÃ£o Ã© possÃ­vel salvar o trabalho com o ID "%1$s" no armazenamento de trabalhos. AWSITA003E NÃ£o Ã© possÃ­vel cancelar o trabalho com o ID "%1$s" porque ele nÃ£o estÃ¡ presente no arm".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1128. hwa-10.2.8-msg-awsita012e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA012E (ITA) indica: "A tarefa de cancelamento do trabalho falhou enquanto estava obtendo as informaÃ§Ãµes para conectar-se ao monitor de trabalho. O erro Ã© "%1$s". AWSITA013E A tarefa de cancelamento do trabalho falhou enquanto estava criando uma conexÃ£o com o monitor ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1129. hwa-10.2.8-msg-awsita077e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA077E (ITA) indica: "Encerramento anormal da tarefa (o cÃ³digo de saÃ­da Ã© o nÃºmero do sinal de encerramento). AWSITA078I A tarefa saiu com um cÃ³digo de saÃ­da nÃ£o-zero. AWSITA079E NÃ£o Ã© possÃ­vel converter um parÃ¢metro especificado para o".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1130. hwa-10.2.8-msg-awsita080e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA080E (ITA) indica: "O".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1131. hwa-10.2.8-msg-awsita081e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA081E (ITA) indica: "O agente nÃ£o pode enviar as informaÃ§Ãµes de recursos para "%1$s". O erro Ã©: "%2$s". AWSITA082E O agente recebeu uma resposta de erro ao enviar as informaÃ§Ãµes de recursos para o servidor. O cÃ³digo de erro Ã© "%1$s" e a mensagem de erro Ã© "%2$s"".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1132. hwa-10.2.8-msg-awsita115i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA115I (ITA) indica: "As propriedades de rastreios foram alteradas: nÃ­vel="%1$d", arquivos mÃ¡ximos="%2$d", tamanho do arquivo="%3$d". AWSITA116I A tarefa foi interrompida pelo usuÃ¡rio AWSITA117E A solicitaÃ§Ã£o de chamada nÃ£o estÃ¡ correta: "%1$s" estÃ¡ ausente. AWSIT".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1133. hwa-10.2.8-msg-awsita128e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA128E (ITA) indica: "Nenhum mÃ©todo localizado. AWSITA129E Nenhum arquivo de opÃ§Ãµes localizado para o mÃ©todo "%1$s". AWSITA130E O arquivo de opÃ§Ãµes "%1$s" nÃ£o existe. AWSITA131E O arquivo de opÃ§Ãµes "%1$s" Ã© muito grande. AWSITA132E NÃ£o foi possÃ­vel acessar o a".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1134. hwa-10.2.8-msg-awsita139e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA139E (ITA) indica: "A operaÃ§Ã£o solicitada nÃ£o pode ser concluÃ­da. O erro Ã©: "%1$s" AWSITA140E O campo Arquivo de".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1135. hwa-10.2.8-msg-awsita141e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA141E (ITA) indica: "A tarefa nÃ£o pode".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1136. hwa-10.2.8-msg-awsita142e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA142E (ITA) indica: "Nome de variÃ¡vel ausente apÃ³s a opÃ§Ã£o "%1$s". AWSITA143E Argumento(s) de comando inesperado(s) localizado(s). Insira um valor para a variÃ¡vel "%1$s" AWSITA145E O valor nÃ£o pode ser vazio. Tem certeza de que deseja remover "%1$s"? [y/n] AWSITA14".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1137. hwa-10.2.8-msg-awsita167e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA167E (ITA) indica: "NÃ£o Ã© possÃ­vel configurar as variÃ¡veis, porque a solicitaÃ§Ã£o XML especificada "%1$s" nÃ£o Ã© vÃ¡lida ou estÃ¡ vazia. AWSITA168I A variÃ¡vel "%1$s" foi configurada com Ãªxito para o valor "%2$s". AWSITA169I A variÃ¡vel "%1$s" foi removida com Ãª".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1138. hwa-10.2.8-msg-awsita172e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA172E (ITA) indica: "O valor inserido nÃ£o corresponde ao valor anterior. AWSITA173E NÃ£o Ã© possÃ­vel atualizar o valor da propriedade de rastreio especificado, devido a este erro: "%1$s" AWSITA174E NÃ£o Ã© possÃ­vel obter os valores das propriedades de rastreio, devido".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1139. hwa-10.2.8-msg-awsita176i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA176I (ITA) indica: "As propriedades de rastreamento sÃ£o: nÃ­vel="%1$s", mÃ¡ximo de arquivos="%2$s", tamanho do arquivo="%3$s". AWSITA177E O valor especificado para o argumento de comando "%1$s" deve ser um nÃºmero inteiro positivo vÃ¡lido. AWSITA178E O valor especifica".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1140. hwa-10.2.8-msg-awsita211w

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA211W (ITA) indica: "Falha ao definir o tamanho da pilha do conjunto de encaminhamentos do manipulador de comandos. O erro Ã© "%1$s". AWSITA212E Falha ao criar o conjunto de encadeamentos do manipulador de comando. O erro Ã© "%1$s". EstaÃ§Ã£o de trabalho Nome do Fluxo de".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1141. hwa-10.2.8-msg-awsita229e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA229E (ITA) indica: "O comando Wappman nÃ£o pode ser executado porque um ou mais argumentos de entrada estÃ£o ausentes. AWSITA230E Foi encontrado um erro ao processar o arquivo de propriedades "%1$s". AWSITA231E A propriedade da conexÃ£o de "%1$s" deve ser especificada. ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1142. hwa-10.2.8-msg-awsita264e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA264E (ITA) indica: "O parÃ¢metro, "%1$s", foi especificado mais de uma vez. AWSITA265E Os parÃ¢metros, "%1$s" e "%2$s", nÃ£o podem ser especificados. AWSITA266E O valor especificado para o parÃ¢metro %1$s nÃ£o Ã© vÃ¡lido. AWSITA267E O comando sendevent nÃ£o pode ser exe".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1143. hwa-10.2.8-msg-awsita278e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA278E (ITA) indica: "Ocorreu um erro interno. Ocorreu um erro ao ler o valor de "%1$s" do arquivo de configuraÃ§Ã£o "%2$s. A chave nÃ£o estÃ¡ presente ou o arquivo de configuraÃ§Ã£o nÃ£o pode ser lido AWSITA279E Ocorreu um erro interno. O evento nÃ£o foi enviado e foi ar".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1144. hwa-10.2.8-msg-awsita287i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA287I (ITA) indica: "Iniciando o subagente "%1$s". AWSITA288E O subagente JobManagerGW nÃ£o pode ser criado. O erro Ã© "%1$s". O cÃ³digo de erro Ã© "%2$d". AWSITA289E O subagente JobManagerGW nÃ£o pode ser criado. O erro Ã© "%1$s". O cÃ³digo de erro Ã© "%2$d". AWSITA290I".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1145. hwa-10.2.8-msg-awsita389i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA389I (ITA) indica: "NÃ£o hÃ¡ mensagens aguardando serem respondidas para o trabalho "%1$s". AWSITA390E NÃ£o Ã© possÃ­vel ler o arquivo de propriedades da mensagem para o trabalho com o ID "%1$s". O erro Ã© "%2$s". AWSITA391E A mensagem com ID "%1$s" para o trabalho com ".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1146. hwa-10.2.8-msg-awsita403e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA403E (ITA) indica: "O comando filemonitor nÃ£o pode ser executado porque um ou mais argumentos de entrada estÃ£o ausentes. AWSITA404E Evento incorreto. Os eventos com suporte sÃ£o fileCreated e fileModified. AWSITA405E O arquivo de propriedades da tarefa nÃ£o pode ser a".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1147. hwa-10.2.8-msg-awssam001i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSSAM001I (SAM) indica: "Configuring IBM System Automation for Multiplatforms for HCL Workload Automation !1 instance (!2). AWSSAM002E Only the user "root" can run the createResources script. AWSSAM003E The createResources script is being run from the wrong directory. AWSSAM".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1148. hwa-10.2.8-msg-awssas003e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSSAS003E (SAS) indica: "You specified an incorrect value for a parameter. The parameter must be as follows: "!1". AWSSAS004E You specified the "!1" more than once. AWSSAS005E You did not specify the "!1". AWSSAS006I To see a list of the available parameters, use the "-u" op".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1149. hwa-10.2.8-msg-awssas068i

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSSAS068I (SAS) indica: "To continue your subscription open the following link on your browser:".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1150. hwa-10.2.8-msg-awssas069e

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSSAS069E (SAS) indica: "You are trying to update an instance using the user "!1" but no instances were found belonging to him. Make sure to update the instance using the same login user used to install it. If you used "root" as login user make sure to specify the correct us".

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 1151. hwa-10.2.8-observability-splunk-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > splunk [observability_splunk]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a Observability for Splunk esta disponivel para monitorar metricas, eventos, audit e infrastructure logs do HWA. Ela fornece 5 dashboards no Splunk Enterprise: (1) Jobs and Job Streams (status de jobs, critical jobs e job streams); (2) KPIs and Workstations (KPIs do HWA por engine com drill-down para series temporais graficas); (3) Activity Monitoring (audit de acoes de usuario); (4) Infra Monitoring (detalhes de infraestrutura do deployment em Kubernetes); (5) Alerts (alertas customizados para eventos do HWA, com alertas pre-definidos de exemplo). A integracao usa o readme file oficial para deploy e customizacao.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a Observability for Splunk esta disponivel para monitorar metricas, eventos, audit e infrastructure logs do HWA?*

---

### 1152. hwa-10.2.8-ocli-context-list-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context list (alias l) exibe os contextos disponiveis no arquivo config.yaml; o contexto padrao e identificado com um asterisco (*); sintaxe 'ocli context [list | l]'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context list (alias l) exibe os contextos disponiveis no arquivo config?*

---

### 1153. hwa-10.2.8-ocli-context-new-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context new cria um novo contexto no arquivo config.yaml; o parametro context_name e obrigatorio e o comando solicita a URL (host e porta separados por ':'); se http ou https for informado sem porta, os valores padrao 80 e 443 sao adicionados; sintaxe 'ocli context new context_name'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context new cria um novo contexto no arquivo config?*

---

### 1154. hwa-10.2.8-ocli-context-remove-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context remove (alias rm) remove um contexto existente do arquivo config.yaml; o parametro context_name e obrigatorio; sintaxe 'ocli context [remove | rm] context_name'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context remove (alias rm) remove um contexto existente do arquivo config?*

---

### 1155. hwa-10.2.8-ocli-context-set-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context set atualiza e gerencia parametros ou propriedades de cada contexto no arquivo config.yaml; o parametro [parameter=value] e obrigatorio; se context_name for omitido, o parametro do contexto padrao e atualizado; niveis completos sao separados por ponto (ex.: connection.port=443); sintaxe 'ocli context set [context_name] parameter=value'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context set atualiza e gerencia parametros ou propriedades de cada contexto no arquivo config?*

---

### 1156. hwa-10.2.8-ocli-context-switch-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context switch (alias sw) altera o contexto padrao quando ha multiplos contextos no arquivo config.yaml; o parametro context_name e obrigatorio; sintaxe 'ocli context [switch | sw] context_name'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli context switch (alias sw) altera o contexto padrao quando ha multiplos contextos no arquivo config?*

---

### 1157. hwa-10.2.8-ocli-model-add-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model add (alias a) adiciona itens de agendamento ao banco a partir de um arquivo de definicao, requer acesso add, e pergunta se deseja substituir o item caso ele ja exista; detecta dependencias de loop em job streams.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model add (alias a) adiciona itens de agendamento ao banco a partir de um arquivo de definicao, requer acesso add, e pergunta se deseja substituir o item caso ele ja exista; detecta dependencias de loop em job streams?*

---

### 1158. hwa-10.2.8-ocli-model-catalog-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, os comandos model operam sobre as definicoes persistentes (folders, jobs, job streams, workstations, calendars, recursos, run cycles, variaveis) no banco de dados, distintos dos comandos plan que operam sobre instancias no plano de producao.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, os comandos model operam sobre as definicoes persistentes (folders, jobs, job streams, workstations, calendars, recursos, run cycles, variaveis) no banco de dados, distintos dos comandos plan que operam sobre instancias no plano de producao?*

---

### 1159. hwa-10.2.8-ocli-model-delete-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model delete (aliases de, del) remove itens de agendamento do banco, requer acesso delete, o item nao pode estar bloqueado por outro usuario, e o parametro ;noask remove a confirmacao por item; ao deletar um job stream referenciado em outros itens usa-se ;force para deletar tambem as referencias.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model delete (aliases de, del) remove itens de agendamento do banco, requer acesso delete, o item nao pode estar bloqueado por outro usuario, e o parametro ;noask remove a confirmacao por item; ao deletar um job stream referenciado em outros itens usa-se ;force para deletar tambem as referencias?*

---

### 1160. hwa-10.2.8-ocli-model-extract-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model extract (aliases create/cr, ext) copia definicoes de itens de agendamento do banco para um arquivo de texto, requer acesso display aos itens copiados e acesso modify apenas se usado o parametro ;lock; sintaxe 'ocli model create | cr | extract | ext filename from Scheduling item [;lock]'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model extract (aliases create/cr, ext) copia definicoes de itens de agendamento do banco para um arquivo de texto, requer acesso display aos itens copiados e acesso modify apenas se usado o parametro ;lock; sintaxe 'ocli model create | cr | extract | ext filename from Scheduling item [;lock]'?*

---

### 1161. hwa-10.2.8-ocli-model-list-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, oclu model list (aliases l, li) exibe uma lista de itens de um mesmo tipo e requer acesso list ao item; a sintaxe e 'ocli model list Scheduling item [;showid]' e aceita calendarios, domains, folders, job definitions, job streams, prompts, resources, run cycle groups, usuarios, variaveis, variable tables, workstations e workstation classes.

**Plataforma / Validação:** Distributed; Orchestration CLI

---

### 1162. hwa-10.2.8-ocli-model-lock-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model lock (alias lo) bloqueia o acesso a definicoes de itens de agendamento; sintaxe 'ocli model lock|lo Scheduling item', aceita calendarios, domains, folders, jobs, job streams, prompts, resources, run cycle groups, usuarios, variaveis, workstations e workstation classes.

**Plataforma / Validação:** Distributed; Orchestration CLI

---

### 1163. hwa-10.2.8-ocli-model-mkfolder-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model mkfolder (alias mf) cria novas pastas, inclusive sub-pastas sob pastas existentes, e requer acesso add; sintaxe 'ocli model mkfolder|mf foldername' ou 'ocli model mkfolder|mf /existing folder/foldername'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model mkfolder (alias mf) cria novas pastas, inclusive sub-pastas sob pastas existentes, e requer acesso add; sintaxe 'ocli model mkfolder|mf foldername' ou 'ocli model mkfolder|mf /existing folder/foldername'?*

---

### 1164. hwa-10.2.8-ocli-model-modify-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model modify (alias m) abre uma copia temporaria da definicao selecionada para edicao e substitui o item existente; sintaxe 'ocli model modify|m Scheduling item'. Se a chave for alterada, um novo item e criado sem modificar o existente; usa-se rename para renomear.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model modify (alias m) abre uma copia temporaria da definicao selecionada para edicao e substitui o item existente; sintaxe 'ocli model modify|m Scheduling item'?*

---

### 1165. hwa-10.2.8-ocli-model-replace-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model replace (alias rep) substitui definicoes de itens existentes a partir de um arquivo: se o item existe, e substituido; se nao, e criado; requer acesso modify para substituir ou add para criar, detecta dependencias de loop e com ;unlock pode atualizar itens bloqueados por outros (exigindo modify e unlock).

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model replace (alias rep) substitui definicoes de itens existentes a partir de um arquivo: se o item existe, e substituido; se nao, e criado; requer acesso modify para substituir ou add para criar, detecta dependencias de loop e com ;unlock pode atualizar itens bloqueados por outros (exigindo modify e unlock)?*

---

### 1166. hwa-10.2.8-ocli-model-rmfolder-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model rmfolder (alias rf) deleta pastas e sub-pastas que nao contem itens de agendamento; se contem, retorna erro; a pasta deve estar desbloqueada; sintaxe 'ocli model rmfolder | rf foldername', e '/@' deleta todas as pastas e sub-pastas na raiz.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli model rmfolder (alias rf) deleta pastas e sub-pastas que nao contem itens de agendamento; se contem, retorna erro; a pasta deve estar desbloqueada; sintaxe 'ocli model rmfolder | rf foldername', e '/@' deleta todas as pastas e sub-pastas na raiz?*

---

### 1167. hwa-10.2.8-ocli-plan-kill-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan kill ou k interrompe um job em progresso; jobs interrompidos terminam em ABEND, dependentes não são liberados e o agente não solicita confirmação individual ao aplicar a ação. Context: The jobs that are stopped by the kill command are finished in the ABEND state. Any jobs or job streams that are dependent on these jobs are not released ... the agent will not ask for your confirmation before taking action on each job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan kill ou k interrompe um job em progresso; jobs interrompidos terminam em ABEND, dependentes não são liberados e o agente não solicita confirmação individual ao aplicar a ação?*

---

### 1168. hwa-10.2.8-ocli-plan-reply-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan reply confirma um prompt especifico ou varios de uma vez e requer acesso reply aos prompts globais/nomeados ou aos prompts e seus jobs/job streams associados; sintaxe 'ocli plan reply #{message_number | prompt_name} [reply_value] [noask]', com reply_value yes ou no obrigatorio.

**Plataforma / Validação:** Distributed; Orchestration CLI

---

### 1169. hwa-10.2.8-ocli-plan-rerun-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan rerun (alias rr) reexecuta um job elegivel (SUCC, FAIL ou ABEND), coloca a reexecucao no mesmo job stream do job original com as dependencias associadas, e nao pede confirmacao por job a menos que noask seja removido; sintaxe 'ocli plan <rerun | rr> jobselect<...>'; aceita from=job, at=time, streamlogon|logon=new_logon, docommand, script, step, sameworkstation e noask.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan rerun (alias rr) reexecuta um job elegivel (SUCC, FAIL ou ABEND), coloca a reexecucao no mesmo job stream do job original com as dependencias associadas, e nao pede confirmacao por job a menos que noask seja removido; sintaxe 'ocli plan <rerun | rr> jobselect<?*

---

### 1170. hwa-10.2.8-ocli-plan-showjobs-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan showjobs (alias sj) exibe informacoes sobre jobs no plano; pode ser executado sozinho (formato standard) ou com parametros de filtro (keys, info, logon, keys retcod, deps, stdlist, short, single, showid, props); aceita wildcards para filtrar jobs e pastas; sintaxe 'ocli plan <showjobs | sj><jobselect><...>'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan showjobs (alias sj) exibe informacoes sobre jobs no plano; pode ser executado sozinho (formato standard) ou com parametros de filtro (keys, info, logon, keys retcod, deps, stdlist, short, single, showid, props); aceita wildcards para filtrar jobs e pastas; sintaxe 'ocli plan <showjobs | sj><jobselect><?*

---

### 1171. hwa-10.2.8-ocli-plan-submit-docommand-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan submit docommand (alias sbd) agenda o inicio de um comando como um job e requer acesso submit ao job; deve-se especificar o usuario com logon (linha de comando) ou user (config.yaml); o parametro obrigatorio e o cmd (ate 255 caracteres, entre aspas duplas); no Windows o sinal = deve ser mascarado como '\='.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan submit docommand (alias sbd) agenda o inicio de um comando como um job e requer acesso submit ao job; deve-se especificar o usuario com logon (linha de comando) ou user (config?*

---

### 1172. hwa-10.2.8-ocli-plan-submit-job-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan submit job (alias sbj) lanca um job no plano e requer acesso submitdb ao job; o unico parametro obrigatorio e o nome do job; aceita workstation (com wildcard), alias=name, into=[jobstream instance], joboptions (at, deadline, follows, maxdur, mindur, until, confirmed, critical, recovery, recoveryjob, abendprompt, vartable) e noask.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*

---

### 1173. hwa-10.2.8-ocli-plan-submit-sched-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan submit sched (alias sbs) inicia um job stream no plano e requer acesso submit ao job stream; o unico parametro obrigatorio e jstreamname; aceita workstation (wildcard), [folder/], alias=name, jstreamoptions (at, schedtime, deadline, follows, until, vartable) e noask.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli plan submit sched (alias sbs) inicia um job stream no plano e requer acesso submit ao job stream; o unico parametro obrigatorio e jstreamname; aceita workstation (wildcard), [folder/], alias=name, jstreamoptions (at, schedtime, deadline, follows, until, vartable) e noask?*

---

### 1174. hwa-10.2.8-ocli-release-job-persist-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, release job (rj) libera dependencias normais e de tempo apenas para o job em andamento; na reexecucao do mesmo job a dependencia persiste e, para remove-la permanentemente do job stream, usa-se deldep job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, release job (rj) libera dependencias normais e de tempo apenas para o job em andamento; na reexecucao do mesmo job a dependencia persiste e, para remove-la permanentemente do job stream, usa-se deldep job?*

---

### 1175. hwa-10.2.8-ocli-syntax-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, a sintaxe usa caracteres especiais como delimitadores e wildcards, e NAO usa opcoes estilo --flag: '=' atribui valor a um argumento (ex.: state = done), ';' separa argumentos (ex.: adj HCL#ABSENCES_JS.PAYROLL_JOB ;maxdur=80 ;onmaxdur kill), ',' adiciona multiplos valores (ex.: state = done, succ, succp), '+' inclui argumento especifico, '~' exclui argumento especifico, '@' e '?' sao wildcards e '\' escapa caracteres especiais.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, a sintaxe usa caracteres especiais como delimitadores e wildcards, e NAO usa opcoes estilo --flag: '=' atribui valor a um argumento (ex?*

---

### 1176. hwa-10.2.8-ocli-version-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli version (alias v) exibe a versao do Orchestration CLI instalado no sistema; sintaxe 'ocli [context|model|plan|plugin] version|v'.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Orchestration CLI, ocli version (alias v) exibe a versao do Orchestration CLI instalado no sistema; sintaxe 'ocli [context|model|plan|plugin] version|v'?*

---

### 1177. hwa-10.2.8-optman-aa-enautomaticfailoveractions

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enAutomaticFailoverActions" (abreviação "aa") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1178. hwa-10.2.8-optman-af-enautomaticfailover

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enAutomaticFailover" (abreviação "af") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1179. hwa-10.2.8-optman-ah-audithistory

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "auditHistory" (abreviação "ah") está configurada como "400".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1180. hwa-10.2.8-optman-al-approachinglateoffset

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "approachingLateOffset" (abreviação "al") está configurada como "120".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1181. hwa-10.2.8-optman-as-auditstore

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "auditStore" (abreviação "as") está configurada como "BOTH".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1182. hwa-10.2.8-optman-au-enadduser

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enAddUser" (abreviação "au") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1183. hwa-10.2.8-optman-aw-enaddworkstation

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enAddWorkstation" (abreviação "aw") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1184. hwa-10.2.8-optman-bp-baserecprompt

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "baseRecPrompt" (abreviação "bp") está configurada como "1000".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1185. hwa-10.2.8-optman-bu-binduser

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "bindUser" (abreviação "bu") está configurada como "wauser".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1186. hwa-10.2.8-optman-cd-startconditiondeadlineoffset

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "startConditionDeadlineOffset" (abreviação "cd") está configurada como "2400".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1187. hwa-10.2.8-optman-cf-encarryforward

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enCarryForward" (abreviação "cf") está configurada como "ALL".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1188. hwa-10.2.8-optman-ci-encfinternetworkdeps

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enCFInterNetworkDeps" (abreviação "ci") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1189. hwa-10.2.8-optman-cn-companyname

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "companyName" (abreviação "cn") está configurada como "LAB".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1190. hwa-10.2.8-optman-cs-carrystates

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "carryStates" (abreviação "cs") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1191. hwa-10.2.8-optman-da-endbaudit

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enDbAudit" (abreviação "da") está configurada como "1".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1192. hwa-10.2.8-optman-df-deploymentfrequency

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "deploymentFrequency" (abreviação "df") está configurada como "5".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1193. hwa-10.2.8-optman-dg-endbgetopsaudit

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enDbGetOpsAudit" (abreviação "dg") está configurada como "1".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1194. hwa-10.2.8-optman-display-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > optman [optman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, optman ls lista os valores de todas as global options e optman show exibe o valor de uma opção; ambos são somente leitura e requerem permissão DISPLAY no objeto GLOBALOPTS. Alterar com optman chg é mutativo e exige MODIFY.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar optman?*

---

### 1195. hwa-10.2.8-optman-dn-sccdusername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "sccdUserName" (abreviação "dn") está configurada como "wauser".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1196. hwa-10.2.8-optman-do-deadlineoffset

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "deadlineOffset" (abreviação "do") está configurada como "2".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1197. hwa-10.2.8-optman-dp-sccduserpassword

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "sccdUserPassword" (abreviação "dp") está configurada como "****".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1198. hwa-10.2.8-optman-du-sccdurl

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "sccdUrl" (abreviação "du") está configurada como "http://localhost:8080/maximo/oslc/os/oslcincident".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1199. hwa-10.2.8-optman-ea-useaesencryptionalgorithm

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "useAESEncryptionAlgorithm" (abreviação "ea") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1200. hwa-10.2.8-optman-ed-eneventdrivenworkloadautomation

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enEventDrivenWorkloadAutomation" (abreviação "ed") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1201. hwa-10.2.8-optman-ee-eventprocessoreifport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "eventProcessorEIFPort" (abreviação "ee") está configurada como "0".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1202. hwa-10.2.8-optman-ef-eventprocessoreifsslport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "eventProcessorEIFSSLPort" (abreviação "ef") está configurada como "31131".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1203. hwa-10.2.8-optman-eh-eneventprocessorhttpsprotocol

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enEventProcessorHttpsProtocol" (abreviação "eh") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1204. hwa-10.2.8-optman-er-enexpandedresources

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enExpandedResources" (abreviação "er") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1205. hwa-10.2.8-optman-es-enemptyschedsaresucc

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enEmptySchedsAreSucc" (abreviação "es") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1206. hwa-10.2.8-optman-fc-filestartconditionjobname

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "fileStartConditionJobName" (abreviação "fc") está configurada como "FILE_STARTCOND".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1207. hwa-10.2.8-optman-fd-folderdays

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "folderDays" (abreviação "fd") está configurada como "10".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1208. hwa-10.2.8-optman-iv-eninitialversionobjects

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enInitialVersionObjects" (abreviação "iv") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1209. hwa-10.2.8-optman-lb-enlogonbatch

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enLogonBatch" (abreviação "lb") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1210. hwa-10.2.8-optman-lc-logcleanupfrequency

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "logCleanupFrequency" (abreviação "lc") está configurada como "5".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1211. hwa-10.2.8-optman-ld-longdurationthreshold

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "longDurationThreshold" (abreviação "ld") está configurada como "150".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1212. hwa-10.2.8-optman-le-enlegacystartofdayevaluation

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enLegacyStartOfDayEvaluation" (abreviação "le") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1213. hwa-10.2.8-optman-lh-loghistory

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "logHistory" (abreviação "lh") está configurada como "10".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1214. hwa-10.2.8-optman-lm-logmanminmaxpolicy

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "logmanMinMaxPolicy" (abreviação "lm") está configurada como "BOTH".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1215. hwa-10.2.8-optman-ln-licensetype

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseType" (abreviação "ln") está configurada como "PERSERVER".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1216. hwa-10.2.8-optman-lo-licenseproxyserverport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseProxyServerPort" (abreviação "lo") está configurada como "0".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1217. hwa-10.2.8-optman-lp-licenseproxyserver

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseProxyServer" (abreviação "lp") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1218. hwa-10.2.8-optman-lt-logmansmoothpolicy

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "logmanSmoothPolicy" (abreviação "lt") está configurada como "-1".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1219. hwa-10.2.8-optman-lu-licenseserverurl

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseServerUrl" (abreviação "lu") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1220. hwa-10.2.8-optman-ml-minlen

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "minLen" (abreviação "ml") está configurada como "8".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1221. hwa-10.2.8-optman-ms-mailsendername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "mailSenderName" (abreviação "ms") está configurada como "TWS".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1222. hwa-10.2.8-optman-nn-servicenowusername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "servicenowUserName" (abreviação "nn") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1223. hwa-10.2.8-optman-np-servicenowuserpassword

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "servicenowUserPassword" (abreviação "np") está configurada como "****".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1224. hwa-10.2.8-optman-nt-notificationtimeout

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "notificationTimeout" (abreviação "nt") está configurada como "5".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1225. hwa-10.2.8-optman-nu-servicenowurl

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "servicenowUrl" (abreviação "nu") está configurada como "http://localhost:8080/api/now/table/incident".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1226. hwa-10.2.8-optman-od-enstartcondsuccondeadline

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enStartCondSuccOnDeadline" (abreviação "od") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1227. hwa-10.2.8-optman-pa-enplanaudit

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enPlanAudit" (abreviação "pa") está configurada como "1".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1228. hwa-10.2.8-optman-pb-licenseproxyuser

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseProxyUser" (abreviação "pb") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1229. hwa-10.2.8-optman-po-promotionoffset

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "promotionOffset" (abreviação "po") está configurada como "120".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1230. hwa-10.2.8-optman-pr-eneventdrivenworkloadautomationproxy

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enEventDrivenWorkloadAutomationProxy" (abreviação "pr") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1231. hwa-10.2.8-optman-ps-enpreventstart

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enPreventStart" (abreviação "ps") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1232. hwa-10.2.8-optman-pw-licenseproxypassword

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseProxyPassword" (abreviação "pw") está configurada como "****".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1233. hwa-10.2.8-optman-rc-riskconfidence

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "riskConfidence" (abreviação "rc") está configurada como "50".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1234. hwa-10.2.8-optman-rj-resubmitjobname

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "resubmitJobName" (abreviação "rj") está configurada como "MASTERAGENTS#RESTART_STARTCOND".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1235. hwa-10.2.8-optman-rq-encfresourcequantity

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enCFResourceQuantity" (abreviação "rq") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1236. hwa-10.2.8-optman-rs-enrolebasedsecurityfilecreation

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enRoleBasedSecurityFileCreation" (abreviação "rs") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1237. hwa-10.2.8-optman-rt-licenserefreshtoken

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "licenseRefreshToken" (abreviação "rt") está configurada como "License Refresh Token is absent".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1238. hwa-10.2.8-optman-rw-resubmitjobusername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "resubmitJobUserName" (abreviação "rw") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1239. hwa-10.2.8-optman-sc-enlistsecchk

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enListSecChk" (abreviação "sc") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1240. hwa-10.2.8-optman-sd-startofday

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "startOfDay" (abreviação "sd") está configurada como "0005".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1241. hwa-10.2.8-optman-se-enstrencrypt

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enStrEncrypt" (abreviação "se") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1242. hwa-10.2.8-optman-sf-ensslfullconnection

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enSSLFullConnection" (abreviação "sf") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1243. hwa-10.2.8-optman-sh-statshistory

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "statsHistory" (abreviação "sh") está configurada como "400".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1244. hwa-10.2.8-optman-sl-ensecfileextendedfields

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enSecFileExtendedFields" (abreviação "sl") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1245. hwa-10.2.8-optman-sn-smtpservername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpServerName" (abreviação "sn") está configurada como "localhost".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1246. hwa-10.2.8-optman-sp-smtpserverport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpServerPort" (abreviação "sp") está configurada como "25".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1247. hwa-10.2.8-optman-st-enforecaststarttime

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enForecastStartTime" (abreviação "st") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1248. hwa-10.2.8-optman-th-tecservername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "TECServerName" (abreviação "th") está configurada como "localhost".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1249. hwa-10.2.8-optman-tl-smtpusetls

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpUseTLS" (abreviação "tl") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1250. hwa-10.2.8-optman-tp-tecserverport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "TECServerPort" (abreviação "tp") está configurada como "5529".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1251. hwa-10.2.8-optman-ts-encentsec

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enCentSec" (abreviação "ts") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1252. hwa-10.2.8-optman-ua-smtpuseauthentication

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpUseAuthentication" (abreviação "ua") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1253. hwa-10.2.8-optman-ud-untildays

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "untilDays" (abreviação "ud") está configurada como "0".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1254. hwa-10.2.8-optman-un-smtpusername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpUserName" (abreviação "un") está configurada como "wauser".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1255. hwa-10.2.8-optman-up-smtpuserpassword

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpUserPassword" (abreviação "up") está configurada como "****".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1256. hwa-10.2.8-optman-us-smtpusessl

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "smtpUseSSL" (abreviação "us") está configurada como "NO".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1257. hwa-10.2.8-optman-wa-enworkloadserviceassurance

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enWorkloadServiceAssurance" (abreviação "wa") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1258. hwa-10.2.8-optman-we-workstationeventmgrlistinautomaticfailover

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "workstationEventMgrListInAutomaticFailover" (abreviação "we") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1259. hwa-10.2.8-optman-wi-enwhatifanalysis

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "enWhatIfAnalysis" (abreviação "wi") está configurada como "YES".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1260. hwa-10.2.8-optman-wl-workstationlimit

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "workstationLimit" (abreviação "wl") está configurada como "100".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1261. hwa-10.2.8-optman-wm-workstationmasterlistinautomaticfailover

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "workstationMasterListInAutomaticFailover" (abreviação "wm") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1262. hwa-10.2.8-optman-wn-defaultwkslicensetype

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "defaultWksLicenseType" (abreviação "wn") está configurada como "PERSERVER".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1263. hwa-10.2.8-optman-xl-maxlen

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "maxLen" (abreviação "xl") está configurada como "14".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1264. hwa-10.2.8-optman-xp-extrecprompt

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "extRecPrompt" (abreviação "xp") está configurada como "1000".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1265. hwa-10.2.8-optman-zp-zosserverport

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "zOSServerPort" (abreviação "zp") está configurada como "31217".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1266. hwa-10.2.8-optman-zr-zosremoteservername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "zOSRemoteServerName" (abreviação "zr") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1267. hwa-10.2.8-optman-zs-zosservername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "zOSServerName" (abreviação "zs") está configurada como "localhost".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1268. hwa-10.2.8-optman-zu-zosusername

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "zOSUserName" (abreviação "zu") está configurada como "".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1269. hwa-10.2.8-optman-zw-zosuserpassword

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global do optman "zOSUserPassword" (abreviação "zw") está configurada como "****".

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL9

---

### 1270. hwa-10.2.8-perf-datasource-tuning-0160

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), as configuracoes recomendadas do data source do Liberty (arquivo datasource.xml em <TWA_DATA_DIR>/usr/servers/engineServer/configDropins/overrides para MDM/BKM/DDM, e <DWC_DATA_DIR>/usr/servers/dwcServer/configDropins/overrides para DWC) sao: statementCacheSize=400, isolationLevel=TRANSACTION_READ_COMMITTED, connectionTimeout=180s, maxPoolSize=300, minPoolSize=0, reapTime=180s, purgePolicy=EntirePool. O Liberty le todos os .xml do diretorio overrides; o nome do arquivo e irrelevante. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.1 Data Source).

**Plataforma / Validação:** Distributed

---

### 1271. hwa-10.2.8-perf-event-processor-throughput-0163

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), o event processor (fila cache.dat) e um processo single-thread: sua capacidade de processamento e proporcional a velocidade do core e ao I/O, nao escala horizontalmente — apenas verticalmente (aumentando CPU e/ou I/O). Em regras de evento que disparam submissoes (ex.: job status change ou file creation), o throughput final de submissao depende estritamente da capacidade do event processor; no caso de status change o consumer e o batchman; no caso de file monitoring remoto, o proprio agent comunica com o event processor. Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.1).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), o event processor (fila cache?*

---

### 1272. hwa-10.2.8-perf-liberty-jvm-options-0162

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), as opcoes JVM recomendadas para o Liberty (arquivo jvm.options em <DWC_DATA_DIR>/usr/servers/dwcServer/configDropins/overrides) sao: -Xms<heap size>, -Xmx<heap size>, -Xmn<nursery size>, -Xgcpolicy:gencon, -Xdisableexplicitgc. Sizing: DWC heap 4096m para ate 50 usuarios/instancia e 6144m para ate 150 usuarios/instancia; MDM heap 4096m para ate 200 jobs/min e 6144m para mais de 200 jobs/min; nursery size = 1/4 do heap size. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.4).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), as opcoes JVM recomendadas para o Liberty (arquivo jvm?*

---

### 1273. hwa-10.2.8-ports-https-port-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 utiliza a porta 9443 como HTTPS_PORT padrão e a porta 9444 como HTTP_PORT, além das portas de bootstrap 12809 e 19402.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 utiliza a porta 9443 como HTTPS_PORT padrão e a porta 9444 como HTTP_PORT, além das portas de bootstrap 12809 e 19402.?*

---

### 1274. hwa-10.2.8-rbac-role-based-security-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 implementa um modelo de segurança baseado em papéis (role-based security model) que controla as permissões de acesso dos usuários aos objetos e às operações de agendamento.

**Plataforma / Validação:** Distributed

---

### 1275. hwa-10.2.8-recusal-resumecond-0001

**Regra Canônica / Evidência:**
In HCL Workload Automation 10.2.8 Distributed, there is no verified evidence of a 'resumecond' keyword (composer) or 'resumecond' command (conman) that controls resumption of suppressed (SUPPR) jobs or job streams. The documented mechanisms to control resumption of SUPPR jobs/job streams are start conditions, conditional dependencies (FOLLOWS ... IF with status conditions SUCC/FAIL/ABEND/SUPPR for jobs), the conman rerun and release commands, and RECOVERY RERUN with the documented syntax recovery rerun [same_workstation] [repeatevery hhmm] [for number attempts]. SFT examples referencing resumecond must therefore be treated as recusal-only (the assistant must answer that the feature is not documented) and must not assert any behavior for it.

**Plataforma / Validação:** Distributed

---

### 1276. hwa-10.2.8-runbook-cancel-job-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando cancel job (cj) com a opção ;pend adia o cancelamento até que todas as dependências associadas sejam resolvidas, e enquanto o cancelamento está postergado, a notação 'Cancel Pend' aparece na coluna Dependencies na exibição showjobs.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel job (cj) com a opção ;pend adia o cancelamento até que todas as dependências associadas sejam resolvidas, e enquanto o cancelamento está postergado, a notação 'Cancel Pend' aparece na coluna Dependencies na exibição showjobs?*

---

### 1277. hwa-10.2.8-runbook-release-job-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando ocli plan release job (rj) libera dependências normais e de tempo de um job, e aplica-se a jobs que estão aguardando a resolução de uma dependência (estado HOLD).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando ocli plan release job (rj) libera dependências normais e de tempo de um job, e aplica-se a jobs que estão aguardando a resolução de uma dependência (estado HOLD)?*

---

### 1278. hwa-10.2.8-runbook-release-sched-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando ocli plan release sched (rs) libera job streams de dependências (at, deadline, follows, needs, opens, prompt, priority, until, limit, carryforward), e requer acesso de release ao job stream.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*

---

### 1279. hwa-10.2.8-runbook-rerun-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O comando ocli plan rerun (ou rr) no HCL Workload Automation 10.2.8 pode ser executado quando um job está nos estados SUCC, FAIL ou ABEND, e coloca o rerun do job no mesmo job stream do job original, adicionando todas as dependências associadas do job original.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O comando ocli plan rerun (ou rr) no HCL Workload Automation 10.2.8 pode ser executado quando um job está nos estados SUCC, FAIL ou ABEND, e coloca o rerun do job no mesmo job stream do job original, adicionando todas as dependências associadas do job original?*

---

### 1280. hwa-10.2.8-runbook-rerun-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando rerun usa a opção ;noask para suprimir a solicitação de confirmação antes que o agente execute a ação em cada job qualificado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando rerun usa a opção ;noask para suprimir a solicitação de confirmação antes que o agente execute a ação em cada job qualificado?*

---

### 1281. hwa-10.2.8-runbook-showjobs-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a exibição padrão do comando showjobs é o formato standard, usado quando nenhuma opção é especificada, e as informações exibidas só são atualizadas enquanto o batchman (HCL Workload Automation) está em execução.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a exibição padrão do comando showjobs é o formato standard, usado quando nenhuma opção é especificada, e as informações exibidas só são atualizadas enquanto o batchman (HCL Workload Automation) está em execução?*

---

### 1282. hwa-10.2.8-runbook-showjobs-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção ;props do comando showjobs (sj) exibe detalhes de uma instância de job, incluindo Status, Internal Status, Return Code, Not Satisfied Dependencies, Rerun Options e, na seção Recovery Information, os campos Action e Message — usados para diagnosticar o motivo de um ABEND.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;props do comando showjobs (sj) exibe detalhes de uma instância de job, incluindo Status, Internal Status, Return Code, Not Satisfied Dependencies, Rerun Options e, na seção Recovery Information, os campos Action e Message — usados para diagnosticar o motivo de um ABEND?*

---

### 1283. hwa-10.2.8-runbook-showjobs-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção ;stdlist do comando showjobs (sj) exibe o log da saída do job (standard list files), incluindo no trailer informações como Exit Status, Elapsed Time, Job CPU usage e Job Memory usage — usada para localizar o log de saída após um ABEND.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;stdlist do comando showjobs (sj) exibe o log da saída do job (standard list files), incluindo no trailer informações como Exit Status, Elapsed Time, Job CPU usage e Job Memory usage — usada para localizar o log de saída após um ABEND?*

---

### 1284. hwa-10.2.8-runbook-showjobs-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção ;keys retcod do comando showjobs (sj) exibe o return code do job, e a opção ;props exibe na seção Runtime Information os campos Return Code e Return Code Mapping Expression, permitindo identificar o código de retorno de um job que terminou em ABEND.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;keys retcod do comando showjobs (sj) exibe o return code do job, e a opção ;props exibe na seção Runtime Information os campos Return Code e Return Code Mapping Expression, permitindo identificar o código de retorno de um job que terminou em ABEND?*

---

### 1285. hwa-10.2.8-sec-access-auditing-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
The official HCL Workload Automation 10.2.8 documentation does not document an access audit trail that identifies who/when for access attempts or a documented review flow. The security file documents permissions but not audit trails.

**Plataforma / Validação:** Distributed

---

### 1286. hwa-10.2.8-sec-access-control-list-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
O modelo de segurança baseado em funções (role-based security) do HCL Workload Automation 10.2.8 define quatro objetos de segurança gerenciáveis pela interface Manage Workload Security da Dynamic Workload Console ou pelo composer: access control lists (ACLs), folders, security roles e security domains.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1287. hwa-10.2.8-sec-awsjco084-e-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando UpdateStats executado em um plano grande falha com a mensagem AWSJCO084E ('The user UNAUTHENTICATED is not authorized to work with the planner process') quando o tempo de execução do job excede duas horas, pois esse é o timeout padrão das credenciais de usuário do WebSphere Application Server; a correção documentada é aumentar o atributo expiration do LTPA.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO084 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO084 no HWA?*
- *Qual é o significado da mensagem de erro AWSJCO084E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?*

---

### 1288. hwa-10.2.8-sec-config-dropins-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o atributo expiration da configuração LTPA (Lightweight Third Party Authentication) do WebSphere Application Server Liberty Base é editado no arquivo de configuração localizado em configDropins/defaults do engineServer, é expresso em minutos e tem valor padrão de 24 horas; após editar, o arquivo deve ser copiado para a pasta overrides do engineServer.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o atributo expiration da configuração LTPA (Lightweight Third Party Authentication) do WebSphere Application Server Liberty Base é editado no arquivo de configuração localizado em configDropins/defaults do engineServer, é expresso em minutos e tem valor padrão de 24 horas; após editar, o arquivo deve ser copiado para a pasta overrides do engineServer?*

---

### 1289. hwa-10.2.8-sec-encrypted-format-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
Quando o modelo de segurança baseado em funções está habilitado no HCL Workload Automation 10.2.8, as definições de objetos de segurança são salvas no banco de dados do master domain manager, o security file é convertido para um formato criptografado (por desempenho e segurança) e as configurações são sincronizadas automaticamente com o backup master.

**Plataforma / Validação:** Distributed

---

### 1290. hwa-10.2.8-sec-job-logon-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
The exact encryption algorithm applied to job logon/streamlogon passwords stored in user objects is not explicitly documented in HCL Workload Automation 10.2.8. The documentation describes the storage in user objects and centralized management but does not specify the internal cryptographic algorithm.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: The exact encryption algorithm applied to job logon/streamlogon passwords stored in user objects is not explicitly documented in HCL Workload Automation 10.2.8. The documentation describes the storage in user objects and centralized management but does not specify the internal cryptographic algorithm?*

---

### 1291. hwa-10.2.8-sec-object-type-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
A definição de security role no HCL Workload Automation 10.2.8 usa a sintaxe 'securityrole nome ... object_type access=acao[,acao]...' para conceder, de forma granular por tipo de objeto, as ações que usuários ou grupos podem executar (ex.: userobj access=modify ou altpass, schedule access=add,delete,display...).

**Plataforma / Validação:** Distributed

---

### 1292. hwa-10.2.8-sec-password-vault-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > password [password]]`

**Regra Canônica / Evidência:**
O recurso de password vaults no HCL Workload Automation 10.2.8 permite recuperar senhas de cofres de senhas (como CyberArk) definindo parâmetros na definição do job, usando a sintaxe ${vault:vault_wks#vault-profile-name:query-for-username} na seção <jsdl:password> do job, sem armazenar a senha em texto plano na definição.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: O recurso de password vaults no HCL Workload Automation 10.2.8 permite recuperar senhas de cofres de senhas (como CyberArk) definindo parâmetros na definição do job, usando a sintaxe ${vault:vault_wks#vault-profile-name:query-for-username} na seção <jsdl:password> do job, sem armazenar a senha em texto plano na definição?*

---

### 1293. hwa-10.2.8-sec-remote-trace-certs-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
O procedimento documentado no HCL Workload Automation 10.2.8 para coletar traces de um agente remoto com certificados de segurança customizados consiste em extrair o certificado do keystore do agente remoto, importá-lo em um keystore local (cujo nome deve ser TWSClientKeyStore.kdb) e criar um arquivo .ini com tcp_port=0, a porta do agente remoto em ssl_port e o caminho do keystore local em key_repository_path.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para coletar traces de um agente remoto com certificados de segurança customizados consiste em extrair o certificado do keystore do agente remoto, importá-lo em um keystore local (cujo nome deve ser TWSClientKeyStore?*

---

### 1294. hwa-10.2.8-sec-retry-bind-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para evitar o bloqueio de conta LDAP após uma tentativa de autenticação errada quando um hostname LDAP é mapeado para múltiplos endereços IP, o WebSphere Application Server disponibiliza as propriedades customizadas com.ibm.websphere.security.ldap.retryBind (default true; se false, o servidor não repete chamadas de bind LDAP) e com.ibm.websphere.security.registry.ldap.singleLDAP (default false; se true, o hostname não é resolvido para múltiplos IPs), configuradas em Security > User Registries > LDAP > Custom Properties.

**Plataforma / Validação:** distributed

---

### 1295. hwa-10.2.8-sec-ssl-auth-mode-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
A opção 'SSL auth mode' no HCL Workload Automation 10.2.8 controla o comportamento durante o handshake SSL com os valores caonly, string ou cpu, que definem como a validade do certificado do par e a emissão por uma CA reconhecida são verificadas (e opcionalmente a correspondência do CN).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção 'SSL auth mode' no HCL Workload Automation 10.2.8 controla o comportamento durante o handshake SSL com os valores caonly, string ou cpu, que definem como a validade do certificado do par e a emissão por uma CA reconhecida são verificadas (e opcionalmente a correspondência do CN)?*

---

### 1296. hwa-10.2.8-sec-ssl-cipher-suites-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > tls [tls]]`

**Regra Canônica / Evidência:**
A opção 'SSL cipher suites' (e 'CLI SSL cipher suites') no HCL Workload Automation 10.2.8 especifica algoritmos suportados apenas para o TLS versão 1.3 e não se aplica ao TLS versão 1.2 ou anterior.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção 'SSL cipher suites' (e 'CLI SSL cipher suites') no HCL Workload Automation 10.2.8 especifica algoritmos suportados apenas para o TLS versão 1.3 e não se aplica ao TLS versão 1.2 ou anterior?*

---

### 1297. hwa-10.2.8-sec-ssl-ciphers-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > ssl [ssl]]`

**Regra Canônica / Evidência:**
A keyword ssl_ciphers no HCL Workload Automation 10.2.8 define os ciphers que a workstation suporta durante uma conexão SSL; para usar uma classe de cipher OpenSSL, usa-se o comando openssl ciphers para listar as classes disponíveis.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A keyword ssl_ciphers no HCL Workload Automation 10.2.8 define os ciphers que a workstation suporta durante uma conexão SSL; para usar uma classe de cipher OpenSSL, usa-se o comando openssl ciphers para listar as classes disponíveis?*

---

### 1298. hwa-10.2.8-sec-ssl-config-xml-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
Para configurar o TLS em componentes Open Liberty do HCL Workload Automation 10.2.8, copia-se o arquivo ssl_config.xml da pasta configDropins/defaults para a pasta overrides dos servidores engineServer e dwcServer e define-se o atributo sslProtocol, por exemplo sslProtocol="TLSv1.3" (só 1.3) ou sslProtocol="TLSv1.2,TLSv1.3" sem espaços antes ou depois da vírgula.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Para configurar o TLS em componentes Open Liberty do HCL Workload Automation 10.2.8, copia-se o arquivo ssl_config?*

---

### 1299. hwa-10.2.8-sec-sso-key-share-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para usar Single Sign-On entre o Dynamic Workload Console e o engine, é necessário compartilhar corretamente as LTPA_keys conforme o capítulo de configuração SSL da Administration Guide; o compartilhamento também é exigido quando ocorrem os erros AWSUI0766E e AWSUI0833E, que surgem quando os valores de realm são iguais para mais de um WebSphere Application Server (DWC, conector z/OS ou engine), por exemplo quando todas as instâncias usam o mesmo LDAP user registry ou estão instaladas na mesma máquina.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0833E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0833E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0766E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0766E no HWA?*

---

### 1300. hwa-10.2.8-sec-tls-1-3-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
A configuração do protocolo TLS V1.3 no HCL Workload Automation 10.2.8 só pode ser definida usando certificados personalizados com chaves RSA de pelo menos 2K, sendo recomendado usar um certificado de comprimento 4K.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A configuração do protocolo TLS V1.3 no HCL Workload Automation 10.2.8 só pode ser definida usando certificados personalizados com chaves RSA de pelo menos 2K, sendo recomendado usar um certificado de comprimento 4K?*

---

### 1301. hwa-10.2.8-sec-tls-crt-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
O comando certman verify no HCL Workload Automation 10.2.8 valida certificados usando a sintaxe 'certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <working directory>]', verificando a senha da chave, a senha do stash (tls.sth), a data de expiração, o tamanho da chave, o formato .pem, a correspondência entre chave privada e pública e a adequação do tls.crt para conexões client e server.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O comando certman verify no HCL Workload Automation 10.2.8 valida certificados usando a sintaxe 'certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <working directory>]', verificando a senha da chave, a senha do stash (tls?*

---

### 1302. hwa-10.2.8-sec-tls-sth-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O comando certman extract no HCL Workload Automation 10.2.8 extrai certificados do keystore e truststore (em master domain manager, agente ou Dynamic Workload Console) com a sintaxe 'certman extract -outpath <output path> [-storepasswd <pw>] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <working directory>] [-cachain-splitted]', gerando os arquivos ca.crt, tls.crt, tls.key, tls.sth (password em Base64) e a subpasta additionalCAs.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O comando certman extract no HCL Workload Automation 10.2.8 extrai certificados do keystore e truststore (em master domain manager, agente ou Dynamic Workload Console) com a sintaxe 'certman extract -outpath <output path> [-storepasswd <pw>] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <working directory>] [-cachain-splitted]', gerando os arquivos ca?*

---

### 1303. hwa-10.2.8-sec-user-definition-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 as definições de usuário em workstations Windows são especificadas via composer na forma [workstation#]username, e o valor streamlogon em uma definição de job é apenas o nome de usuário sem o prefixo da workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1304. hwa-10.2.8-sec-user-definition-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 o comando altpass, usado para alterar a senha de um usuário (credencial de logon), exige a definição de usuário no formato workstation#username, podendo-se omitir o nome da workstation somente ao alterar a senha da workstation a partir da qual o comando é executado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 o comando altpass, usado para alterar a senha de um usuário (credencial de logon), exige a definição de usuário no formato workstation#username, podendo-se omitir o nome da workstation somente ao alterar a senha da workstation a partir da qual o comando é executado?*

---

### 1305. hwa-10.2.8-sec-user-object-credential-management-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > credential [credential]]`

**Regra Canônica / Evidência:**
O User Object Credential Management do HCL Workload Automation 10.2.8 permite atualizar de forma centralizada e segura as senhas armazenadas dentro de user objects, aplicando a mudança de forma consistente tanto na instância de banco de dados quanto nas instâncias de plano ativas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O User Object Credential Management do HCL Workload Automation 10.2.8 permite atualizar de forma centralizada e segura as senhas armazenadas dentro de user objects, aplicando a mudança de forma consistente tanto na instância de banco de dados quanto nas instâncias de plano ativas?*

---

### 1306. hwa-10.2.8-sec-variable-table-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 é necessário ter permissão 'use' para referenciar uma variable table a partir de outros objetos (job streams, run cycles e workstations), conforme definido no security file.

**Plataforma / Validação:** Distributed

---

### 1307. hwa-10.2.8-security-ldap-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: security > ldap [security_user_registry]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, e possivel configurar um user registry LDAP ou federated repository para o Dynamic Workload Console e demais componentes: o administrador adiciona o provider LDAP no template de configuracao de autenticacao, habilita o LDAP registry na seguranca do servidor de aplicacao (WebSphere Liberty) e aponta para o diretorio, depois mapeia os grupos/roles via Manage Roles no DWC. A troca de basicRegistry por LDAP permite SSO e centralizacao de usuarios.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, e possivel configurar um user registry LDAP ou federated repository para o Dynamic Workload Console e demais componentes: o administrador adiciona o provider LDAP no template de configuracao de autenticacao, habilita o LDAP registry na seguranca do servidor de aplicacao (WebSphere Liberty) e aponta para o diretorio, depois mapeia os grupos/roles via Manage Roles no DWC?*

---

### 1308. hwa-10.2.8-security-sso-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: security > sso [security_sso]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Single Sign-On (SSO) pode ser configurado usando LDAP, OIDC ou SAML: para OIDC, configura-se o provedor de identidade (IdP, ex.: Okta ou Keycloak), define-se a URL de redirect/callback para o DWC/MDM, e garante-se que os componentes baseados em WebSphere compartilhem as mesmas chaves de token; reiniciar os servicos apos as mudancas.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Single Sign-On (SSO) pode ser configurado usando LDAP, OIDC ou SAML: para OIDC, configura-se o provedor de identidade (IdP, ex?*

---

### 1309. hwa-10.2.8-securityfile-security-file-auth-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
A autorização de usuários no HCL Workload Automation 10.2.8 é configurada por meio do arquivo de segurança (Security file), que define os usuários e suas permissões de acesso ao master domain manager.

**Plataforma / Validação:** Distributed

---

### 1310. hwa-10.2.8-sfinal-change-0001

**Regra Canônica / Evidência:**
In HCL Workload Automation 10.2.8, customized FINAL and FINALPOSTREPORTS definitions must be merged with the current Sfinal definitions and applied without discarding existing customizations; after updating the definitions, old instances may need to be canceled and new instances submitted according to the documented procedure.

**Plataforma / Validação:** Distributed

---

### 1311. hwa-10.2.8-sfinal-role-0001

**Regra Canônica / Evidência:**
In HCL Workload Automation 10.2.8 Distributed, the optional Sfinal file supplies FINAL and FINALPOSTREPORTS job streams for automating production plan processing; FINAL runs the sequence corresponding to JnextPlan and FINALPOSTREPORTS follows successful SWITCHPLAN and includes CHECKSYNC for plan synchronization.

**Plataforma / Validação:** Distributed

---

### 1312. hwa-10.2.8-showcpus-default-scope-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, showcpus/sc sem domínio ou workstation mostra workstations do domínio local e, em domain manager, também domain managers conectados. Context: displays all the workstations that are in the domain of the workstation where the command was run, plus all the connected domain managers if the workstation is a domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, showcpus/sc sem domínio ou workstation mostra workstations do domínio local e, em domain manager, também domain managers conectados?*

---

### 1313. hwa-10.2.8-showfiles-states-0037

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, showfiles/sf usa yes, no, ? e vazio para indicar respectivamente arquivo disponível, ausente/indisponível, disponibilidade em verificação e ainda não verificado ou já consumido. Context: yes File exists and is available. no File is unavailable, or does not exist. ? Availability is being checked.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, showfiles/sf usa yes, no, ? e vazio para indicar respectivamente arquivo disponível, ausente/indisponível, disponibilidade em verificação e ainda não verificado ou já consumido?*

---

### 1314. hwa-10.2.8-showjobs-wildcard-all-jobs-0110

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o padrao `@#@.@` no comando showjobs (sj) filtra todos os jobs em todos os job streams definidos na pasta raiz (/), onde @ substitui um ou mais caracteres alfanumericos, # e o separador workstation, e o ponto (.) separa job stream de job. O padrao `/@/@#/@/@.@` filtra todos os jobs em job streams definidos em todas as pastas. Exemplo: `sj @#@.@;keys` (HCL oficial Wildcards: '@#@.@ Filters on all jobs in job streams defined in the root (/) folder').

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o padrao `@#@?*

---

### 1315. hwa-10.2.8-showjobs-wildcard-ws-filter-0111

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando showjobs (sj) aceita prefixo `workstation#` no jobselect para filtrar jobs de uma workstation especifica, com suporte a wildcards. Exemplos: `sj MDMDA#@.@` lista todos os jobs na workstation MDMDA; `sj @#@.@` lista jobs de todas as workstations; `sj sked1(1100 03/05/2023).@` seleciona todos os jobs no job stream sked1. O wildcard @ na posicao de workstation substitui qualquer nome de workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o comando showjobs (sj) aceita prefixo `workstation#` no jobselect para filtrar jobs de uma workstation especifica, com suporte a wildcards?*

---

### 1316. hwa-10.2.8-showprompts-access-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, showprompts requer acesso list ao objeto se enListSecChk estava yes no MDM quando o production plan foi criado ou estendido. Context: You must have list access to the object being shown if the enListSecChk option was set to yes on the master domain manager when the production plan was created or extended.

**Plataforma / Validação:** Distributed

---

### 1317. hwa-10.2.8-showschedules-rerun-total-0036

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > show [show]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, a lista de showschedules/ss não inclui jobs reexecutados em processos anteriores, mas o total ao final os inclui. Context: The list displayed in the output of the command does not include jobs that were rerun in previous scheduling processes, but the total shown at the end does.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, a lista de showschedules/ss não inclui jobs reexecutados em processos anteriores, mas o total ao final os inclui?*

---

### 1318. hwa-10.2.8-srv-traces-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > trace [trace]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, os traces do application server (Liberty) para os processos principais usam tws_info por padrão; o nível é alterado editando trace.xml e copiando de configDropins/templates para configDropins/overrides.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, os traces do application server (Liberty) para os processos principais usam tws_info por padrão; o nível é alterado editando trace?*

---

### 1319. hwa-10.2.8-startmon-event-monitoring-engine-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
O comando startmon inicia o processo monman, que ativa o mecanismo de monitoramento de eventos em uma workstation; o monman é iniciado automaticamente na próxima ativação do plano de produção quando a opção autostart monman = yes (padrão).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O comando startmon inicia o processo monman, que ativa o mecanismo de monitoramento de eventos em uma workstation; o monman é iniciado automaticamente na próxima ativação do plano de produção quando a opção autostart monman = yes (padrão)?*

---

### 1320. hwa-10.2.8-stdlist-jobman-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, um arquivo standard list é criado automaticamente para cada job iniciado por jobmon no Windows ou jobman no UNIX. Context: A standard list file is created automatically by jobmon in Windows or jobman in UNIX, for each job that jobmon and jobman launches.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, um arquivo standard list é criado automaticamente para cada job iniciado por jobmon no Windows ou jobman no UNIX?*

---

### 1321. hwa-10.2.8-stdlist-stdlist-stdout-stderr-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, um stdlist contém as saídas stdout e stderr do job. Context: A standard list file contains: ... The stdout output of the job. ... The stderr output of the job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, um stdlist contém as saídas stdout e stderr do job?*

---

### 1322. hwa-10.2.8-submit-docommand-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, submit docommand (sbd) submete um comando de sistema para ser executado como job. O comando deve estar entre aspas, requer acesso submit no security file e, se into não for usado, o job entra no job stream JOBS.

**Plataforma / Validação:** Distributed

---

### 1323. hwa-10.2.8-tls-custom-certificates-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
A documentação do HWA 10.2.8 (página "Configuring the TLS V1.3 security protocol") descreve a configuração do protocolo TLS V1.3 e afirma que ele só pode ser configurado usando certificados customizados com chaves RSA de no mínimo 2K, recomendando o uso de um certificado de 4K; o suporte a TLS V1.3 está disponível a partir do HCL Workload Automation 10.1 FP4.

**Plataforma / Validação:** Distributed

---

### 1324. hwa-10.2.8-tls-ssl-mdm-backup-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: security > tls [tls]]`

**Regra Canônica / Evidência:**
HWA Distributed 10.2.8 explicitly documents SSL connectivity between a master domain manager and a backup master domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 explicitly documents SSL connectivity between a master domain manager and a backup master domain manager?*

---

### 1325. hwa-10.2.8-trouble-awsjcl521e-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; composer) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, ao usar composer add/new para definir um usuario do Windows, o comando retorna AWSJCL521E 'The password specified for the Windows user does not comply with password security policy requirements' quando a senha fornecida nao atende a politica de seguranca de senhas; a causa e uma senha invalida (ou a palavra reservada de dez asteriscos '**********'), e a recuperacao e fornecer uma senha valida que cumpra a politica e evitar usar a sequencia de dez asteriscos como senha.

**Plataforma / Validação:** distributed; composer

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL521E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL521E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1326. hwa-10.2.8-trouble-awsjco084e-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; planner/UpdateStats) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o comando UpdateStats em um plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' quando o tempo de execucao do job ultrapassa duas horas; a causa documentada e o grande numero de jobs do plano fazendo o tempo de execucao exceder o timeout padrao de duas horas das credenciais do usuario do WebSphere Application Server; a recuperacao documentada e aumentar o timeout das credenciais do WAS para dar mais tempo ao UpdateStats.

**Plataforma / Validação:** distributed; planner/UpdateStats

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO084E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?*

---

### 1327. hwa-10.2.8-tune-bm-cache-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
The "bm cache" option is not documented in the HCL Workload Automation 10.2.8 localopts reference. The documented mailbox cache belongs to mailman (mm cache mailbox / mm cache size), not batchman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: The "bm cache" option is not documented in the HCL Workload Automation 10.2.8 localopts reference?*

---

### 1328. hwa-10.2.8-tune-bm-check-file-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
A opção bm check file no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar a existência de um arquivo usado como dependência, com padrão documentado de 120 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm check file no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar a existência de um arquivo usado como dependência, com padrão documentado de 120 segundos?*

---

### 1329. hwa-10.2.8-tune-bm-check-status-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
A opção bm check status no localopts do HCL Workload Automation 10.2.8 especifica o número de segundos que o Batchman espera entre verificações do status de uma dependência internetwork, com padrão documentado de 300 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm check status no localopts do HCL Workload Automation 10.2.8 especifica o número de segundos que o Batchman espera entre verificações do status de uma dependência internetwork, com padrão documentado de 300 segundos?*

---

### 1330. hwa-10.2.8-tune-bm-check-until-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
A opção bm check until no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda antes de reportar a expiração de um tempo Until, com padrão documentado de 300 segundos; valores abaixo do padrão podem sobrecarregar o sistema.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *Qual a regra documentada no HWA Distributed sobre: A opção bm check until no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda antes de reportar a expiração de um tempo Until, com padrão documentado de 300 segundos; valores abaixo do padrão podem sobrecarregar o sistema?*

---

### 1331. hwa-10.2.8-tune-bm-stats-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
A opção bm stats no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar suas estatísticas de inicialização e encerramento ao seu arquivo standard list, com padrão documentado de off.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm stats no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar suas estatísticas de inicialização e encerramento ao seu arquivo standard list, com padrão documentado de off?*

---

### 1332. hwa-10.2.8-tune-bm-verbose-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > batchman [batchman]]`

**Regra Canônica / Evidência:**
A opção bm verbose no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar todas as mensagens de status de jobs ao seu arquivo standard list, com padrão documentado de off.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm verbose no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar todas as mensagens de status de jobs ao seu arquivo standard list, com padrão documentado de off?*

---

### 1333. hwa-10.2.8-tune-command-handler-max-threads-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A propriedade CommandHandlerMaxThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, indica o número máximo de comandos que podem ser executados concorrentemente no agente, com padrão documentado de 100.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade CommandHandlerMaxThreads, na seção [Launchers] do JobManager?*

---

### 1334. hwa-10.2.8-tune-command-handler-min-threads-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A propriedade CommandHandlerMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, indica o número máximo de comandos que podem ser executados concorrentemente no agente, com padrão documentado de 20.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade CommandHandlerMinThreads, na seção [Launchers] do JobManager?*

---

### 1335. hwa-10.2.8-tune-executors-max-threads-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A propriedade ExecutorsMaxThreads, na seção [Launchers] do arquivo JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número máximo de jobs que o agente dinâmico pode executar concorrentemente, com padrão documentado de 400.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade ExecutorsMaxThreads, na seção [Launchers] do arquivo JobManager?*

---

### 1336. hwa-10.2.8-tune-executors-max-threads-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a concorrência de execução de jobs do agente dinâmico é governada pelas propriedades ExecutorsMinThreads e ExecutorsMaxThreads na seção [Launchers] do JobManager.ini, que definem os limites mínimo e máximo de jobs executados concorrentemente pelo agente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a concorrência de execução de jobs do agente dinâmico é governada pelas propriedades ExecutorsMinThreads e ExecutorsMaxThreads na seção [Launchers] do JobManager?*

---

### 1337. hwa-10.2.8-tune-executors-min-threads-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A propriedade ExecutorsMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número mínimo de jobs que o agente dinâmico pode executar concorrentemente, com padrão documentado de 38; o agente aloca dinamicamente mais threads conforme necessário até o valor de ExecutorsMaxThreads.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A propriedade ExecutorsMinThreads, na seção [Launchers] do JobManager?*

---

### 1338. hwa-10.2.8-tune-jm-file-no-root-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm file no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman execute comandos em dependências de arquivo como root, com padrão documentado de no.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm file no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman execute comandos em dependências de arquivo como root, com padrão documentado de no?*

---

### 1339. hwa-10.2.8-tune-jm-job-table-size-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm job table size no localopts do HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão documentado de 1024 entradas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm job table size no localopts do HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão documentado de 1024 entradas?*

---

### 1340. hwa-10.2.8-tune-jm-loaduserprofile-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm loaduserprofile, somente em sistemas Windows, no localopts do HCL Workload Automation 10.2.8 especifica se o processo jobman carrega o perfil de usuário e suas variáveis de ambiente antes de iniciar jobs, com padrão documentado de on.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm loaduserprofile, somente em sistemas Windows, no localopts do HCL Workload Automation 10.2.8 especifica se o processo jobman carrega o perfil de usuário e suas variáveis de ambiente antes de iniciar jobs, com padrão documentado de on?*

---

### 1341. hwa-10.2.8-tune-jm-look-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Jobman aguarda antes de procurar jobs concluídos e executar tarefas gerais de gerenciamento de jobs, com padrão documentado de 300 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Jobman aguarda antes de procurar jobs concluídos e executar tarefas gerais de gerenciamento de jobs, com padrão documentado de 300 segundos?*

---

### 1342. hwa-10.2.8-tune-jm-nice-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica o valor nice aplicado aos jobs lançados pelo Jobman para alterar sua prioridade no scheduler do kernel, com padrão documentado de zero; aplica-se apenas a jobs agendados pelo usuário root.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica o valor nice aplicado aos jobs lançados pelo Jobman para alterar sua prioridade no scheduler do kernel, com padrão documentado de zero; aplica-se apenas a jobs agendados pelo usuário root?*

---

### 1343. hwa-10.2.8-tune-jm-no-root-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman lance jobs como root, com padrão documentado de yes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman lance jobs como root, com padrão documentado de yes?*

---

### 1344. hwa-10.2.8-tune-jm-read-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > jobman [jobman]]`

**Regra Canônica / Evidência:**
A opção jm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Jobman aguarda por uma mensagem no arquivo courier.msg, com padrão documentado de 10 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Jobman aguarda por uma mensagem no arquivo courier?*

---

### 1345. hwa-10.2.8-tune-jvm-options-0044

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: dwc_api > dwc [dwc]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 documenta o aumento do heap do Java da Dynamic Workload Console editando o arquivo jvm.options do dwcServer do WebSphere Application Server Liberty, com exemplo de -Xms4096m -Xmx4096m e, em caso de alta carga (mais de 50 usuários concorrentes), 6144 como heap size e 1536 como nursery mem size; a RAM deve ser aproximadamente o dobro do heap.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 documenta o aumento do heap do Java da Dynamic Workload Console editando o arquivo jvm?*

---

### 1346. hwa-10.2.8-tune-mm-cache-mailbox-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção mm cache mailbox no localopts do HCL Workload Automation 10.2.8 habilita o Mailman a usar um cache de leitura para mensagens recebidas, com padrão documentado de yes; somente mensagens consideradas essenciais para a consistência da rede são armazenadas em cache.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm cache mailbox no localopts do HCL Workload Automation 10.2.8 habilita o Mailman a usar um cache de leitura para mensagens recebidas, com padrão documentado de yes; somente mensagens consideradas essenciais para a consistência da rede são armazenadas em cache?*

---

### 1347. hwa-10.2.8-tune-mm-read-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção mm read é documentada no HCL Workload Automation 10.2.8 como a opção que controla a periodicidade com que o mailman verifica o arquivo Mailbox.msg em busca de jobs concluídos; o valor padrão desta opção não é documentado na referência oficial de detalhes de localopts da versão 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm read é documentada no HCL Workload Automation 10.2.8 como a opção que controla a periodicidade com que o mailman verifica o arquivo Mailbox?*

---

### 1348. hwa-10.2.8-tune-mm-response-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção mm response no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda por uma resposta antes de reportar que uma workstation não está respondendo, com padrão documentado de 600 segundos e tempo mínimo de espera de 90 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm response no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda por uma resposta antes de reportar que uma workstation não está respondendo, com padrão documentado de 600 segundos e tempo mínimo de espera de 90 segundos?*

---

### 1349. hwa-10.2.8-tune-mm-retrylink-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção mm retrylink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda, após desvincular-se de uma workstation que não responde, antes de tentar vincular-se novamente, com padrão documentado de 600 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm retrylink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda, após desvincular-se de uma workstation que não responde, antes de tentar vincular-se novamente, com padrão documentado de 600 segundos?*

---

### 1350. hwa-10.2.8-tune-mm-unlink-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > mailman [mailman]]`

**Regra Canônica / Evidência:**
A opção mm unlink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda antes de desvincular-se de uma workstation que não está respondendo, com padrão documentado de 960 segundos; o tempo de espera não deve ser inferior ao tempo de resposta de nm response.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm unlink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda antes de desvincular-se de uma workstation que não está respondendo, com padrão documentado de 960 segundos; o tempo de espera não deve ser inferior ao tempo de resposta de nm response?*

---

### 1351. hwa-10.2.8-tune-nm-mortal-0039

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > netman [netman]]`

**Regra Canônica / Evidência:**
A opção nm mortal no localopts do HCL Workload Automation 10.2.8 especifica yes para que o Netman saia quando todos os seus processos filhos pararem, com padrão documentado de no.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção nm mortal no localopts do HCL Workload Automation 10.2.8 especifica yes para que o Netman saia quando todos os seus processos filhos pararem, com padrão documentado de no?*

---

### 1352. hwa-10.2.8-tune-nm-read-0037

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > netman [netman]]`

**Regra Canônica / Evidência:**
A opção nm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda por uma requisição de conexão antes de verificar sua fila de mensagens para comandos stop e start, com padrão documentado de 10 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção nm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda por uma requisição de conexão antes de verificar sua fila de mensagens para comandos stop e start, com padrão documentado de 10 segundos?*

---

### 1353. hwa-10.2.8-tune-nm-retry-0038

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > netman [netman]]`

**Regra Canônica / Evidência:**
A opção nm retry no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda antes de tentar novamente uma conexão que falhou, com padrão documentado de 800 segundos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção nm retry no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda antes de tentar novamente uma conexão que falhou, com padrão documentado de 800 segundos?*

---

### 1354. hwa-10.2.8-variable-plan-generation-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a sintaxe ^variablename^ é resolvida quando o plano é gerado ou estendido, enquanto a sintaxe ${variablename} é resolvida no momento da submissão (run time); a sintaxe ${variablename} não é suportada ao submeter um job stream pelo Self-Service Catalog.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a sintaxe ^variablename^ é resolvida quando o plano é gerado ou estendido, enquanto a sintaxe ${variablename} é resolvida no momento da submissão (run time); a sintaxe ${variablename} não é suportada ao submeter um job stream pelo Self-Service Catalog?*

---

### 1355. hwa-10.2.8-vartable-variable-table-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, uma tabela de variáveis é definida com o comando composer vartable, contendo membros no formato variablename "value" e o flag isdefault; a tabela padrão MAIN_TABLE não pode ser excluída; o flag isdefault marca a tabela como padrão (apenas uma pode ser padrão e marcá-la remove o padrão anterior).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1356. hwa-10.2.8-vm-0002-contrast-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.x (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > optman [optman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-vm-0002 (9.5 enRetainNameOnRerunFrom): na 9.5 a opcao enRetainNameOnRerunFrom estava ativa com default no; nas versoes 10.2.x o comportamento de retencao de nome em rerun deve ser confirmado na pagina de global options da versao correspondente, pois opcoes optman legadas foram removidas/alinhadas (ex.: enLegacyId removido); portanto o default e a existencia da opcao sao version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar optman?*

---

### 1357. hwa-10.2.8-vm-0006-contrast-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-vm-0006 (enRoleBasedSecurityFileCreation): na 9.5 o default da opcao rs era no (seguranca classica), enquanto na 10.2.8 o default e yes (seguranca baseada em papeis); SFT e procedimentos de seguranca devem declarar a versao e o default correto, pois o modelo de seguranca padrao muda na fronteira 9.5/10.2.x.

**Plataforma / Validação:** Distributed

---

### 1358. hwa-10.2.8-vm-9f-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3; 10.2.4; 10.2.7; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Embedded jobs (definição de job embutida em JSON/YAML via BUILTIN) foram introduzidos nas enhancements da versão 10.2.3 e documentados a partir da 10.2.4; a limitação 'Embedded jobs not supported by composer, dataextract, and dataimport commands' é documentada na 10.2.7 e 10.2.8. Na 10.2.0 embedded jobs não existiam.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1359. hwa-10.2.8-vm-9f-0010-contrast-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.3; 10.2.4; 10.2.7; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-vm-9f-0010 (embedded jobs): embedded jobs (definicoes BUILTIN em JSON/YAML) foram introduzidos nas enhancements da 10.2.3 e documentados a partir da 10.2.4; na 10.2.0 nao existiam, e a limitacao 'Embedded jobs not supported by composer, dataextract, and dataimport commands' vale para 10.2.7/10.2.8; portanto, disponibilidade e restricoes dos embedded jobs sao version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1360. hwa-10.2.8-vm-en-role-based-security-file-creation-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
Na versão 10.2.8 do HCL Workload Automation, a opção global enRoleBasedSecurityFileCreation (alias rs) tem valor padrão yes, ou seja, o modelo de segurança baseado em papéis fica habilitado na instalação.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?*

---

### 1361. hwa-10.2.8-vm-en-role-based-security-file-creation-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
Na versão 9.5 do HCL Workload Automation, a opção global enRoleBasedSecurityFileCreation (rs) tem valor padrão no, mantendo o modelo de segurança clássico (dumpsec/makesec) como padrão.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?*

---

### 1362. hwa-10.2.8-vm-en-role-based-security-file-creation-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation multi (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
O valor padrão da opção global enRoleBasedSecurityFileCreation (rs) difere entre versões: no na 9.5 (segurança clássica habilitada) e yes na 10.2.8 (segurança baseada em papéis habilitada), caracterizando uma diferença version-dependent do modelo de segurança padrão.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?*

---

### 1363. hwa-10.2.8-vm-orchestration-cli-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
O OCLI (Orchestration CLI) é documentado apenas na documentação do HCL Workload Automation distribuído (seção 'Orchestration CLI' do User's Guide and Reference, sob distr/src_ref); não é listado na documentação do HCL Workload Automation for Z (z/OS).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O OCLI (Orchestration CLI) é documentado apenas na documentação do HCL Workload Automation distribuído (seção 'Orchestration CLI' do User's Guide and Reference, sob distr/src_ref); não é listado na documentação do HCL Workload Automation for Z (z/OS)?*

---

### 1364. hwa-10.2.8-wa-pull-info-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > auth [auth]]`

**Regra Canônica / Evidência:**
In HCL Workload Automation Distributed 10.2.8, wa_pull_info is a collection script that produces environment and workstation information and can snapshot DB2 and Liberty data into a dated package, replacing the legacy tws_inst_pull_info. The -user parameter is mandatory and the output may contain sensitive data; share it only with authorized support and redact as needed.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wa_pull_info no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wa_pull_info para gerenciar auth?*
- *Qual a função do script wa_pull_info no HWA e que tipo de dados ele coleta?*

---

### 1365. hwa-10.2.8-wapullinfo-db2-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
wa_pull_info é um utilitário de captura de dados localizado em TWA_home/TWS/bin; ele tira um snapshot dos dados DB2 e WebSphere Application Server Liberty no MDM, salvando-os como um pacote datado; pode ser usado para backup do banco de dados DB2 e de arquivos de configuração.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wa_pull_info no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wa_pull_info para gerenciar mdm?*
- *Qual a função do script wa_pull_info no HWA e que tipo de dados ele coleta?*

---

### 1366. hwa-10.2.8-wsa-critical-keyword-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, trabalhos também podem ser marcados como críticos incluindo a palavra-chave critical na declaração do trabalho (job statement) ao criar ou modificar um job stream usando a linha de comando composer, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1367. hwa-10.2.8-wsa-hot-list-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Dynamic Workload Console fornece views especializadas para rastrear trabalhos críticos e seus predecessores, acessíveis pelo Dashboard ou por uma task usando o Orchestration Monitor, listando todos os trabalhos críticos do engine com status normal, potencial ou alto risco e permitindo navegar para a hot list, o caminho crítico, detalhes dos predecessores, logs de trabalhos e o confidence factor, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Dynamic Workload Console fornece views especializadas para rastrear trabalhos críticos e seus predecessores, acessíveis pelo Dashboard ou por uma task usando o Orchestration Monitor, listando todos os trabalhos críticos do engine com status normal, potencial ou alto risco e permitindo navegar para a hot list, o caminho crítico, detalhes dos predecessores, logs de trabalhos e o confidence factor, conforme documentação oficial?*

---

### 1368. hwa-10.2.8-wsa-jnext-plan-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as opções globais do Workload Service Assurance são modificadas no master domain manager usando a linha de comando optman e, na maioria dos casos, as alterações entram em vigor após a execução do próximo JnextPlan, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar jnextplan?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 1369. hwa-10.2.8-wsa-sla-report-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
The official HCL Workload Automation 10.2.8 Distributed documentation describes monitoring views for critical jobs (hot list, critical path, confidence factor) but does not document a report specifically named "SLA" or "Workload Service Assurance report" in the Dynamic Workload Console.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como o HWA Distributed monitora SLAs de execução e caminhos críticos de jobs?*

---

### 1370. hwa-10.2.8-wsa-time-planner-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, quando o Workload Service Assurance está habilitado, as threads de execução Time Planner e Plan Monitor, executando dentro do WebSphere Application Server Liberty, são acionadas para garantir que os trabalhos críticos sejam concluídos a tempo, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, quando o Workload Service Assurance está habilitado, as threads de execução Time Planner e Plan Monitor, executando dentro do WebSphere Application Server Liberty, são acionadas para garantir que os trabalhos críticos sejam concluídos a tempo, conforme documentação oficial?*

---

### 1371. hwa-8.3-cert-default-expiration-2014-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 8.3.0-8.6.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Na documentacao oficial do Tivoli Workload Scheduler 8.3 (IBM/HCL), os certificados padrao (default certificates) liberados nas versoes 8.3.0 a 8.6.0 expirariam em 10 de fevereiro de 2014; a IBM disponibilizou pacotes updCertsScripts_v<VERSAO> com scripts (updTrustStoresCerts, updKeyStoresCerts, updateTrustKeyStoresCerts) para renovar os certificados padrao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na documentacao oficial do Tivoli Workload Scheduler 8.3 (IBM/HCL), os certificados padrao (default certificates) liberados nas versoes 8.3.0 a 8.6.0 expirariam em 10 de fevereiro de 2014; a IBM disponibilizou pacotes updCertsScripts_v<VERSAO> com scripts (updTrustStoresCerts, updKeyStoresCerts, updateTrustKeyStoresCerts) para renovar os certificados padrao?*

---

### 1372. hwa-8.3-clisslserverauth-clisslserverauth-expiry-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 8.3.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
No Tivoli Workload Scheduler 8.3, a variavel CLISSLSERVERAUTH no arquivo localopts controla o comportamento da comunicacao apos a expiracao dos certificados padrao: com CLISSLSERVERAUTH=no no cliente de linha de comando remoto, a comunicacao continua funcionando apos a expiracao; com CLISSLSERVERAUTH=yes, a comunicacao para de funcionar.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No Tivoli Workload Scheduler 8.3, a variavel CLISSLSERVERAUTH no arquivo localopts controla o comportamento da comunicacao apos a expiracao dos certificados padrao: com CLISSLSERVERAUTH=no no cliente de linha de comando remoto, a comunicacao continua funcionando apos a expiracao; com CLISSLSERVERAUTH=yes, a comunicacao para de funcionar?*

---

### 1373. hwa-8.3-default-certs-dwc-connector-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 8.3.0 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No Tivoli Workload Scheduler 8.3, se os certificados padrao nao forem renovados antes da expiracao no Dynamic Workload Console e no distributed connector instalado no agente, a comunicacao entre a interface de usuario e o connector e interrompida.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No Tivoli Workload Scheduler 8.3, se os certificados padrao nao forem renovados antes da expiracao no Dynamic Workload Console e no distributed connector instalado no agente, a comunicacao entre a interface de usuario e o connector e interrompida?*

---

### 1374. hwa-9.5-perfreport-contrast-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2-perfreport-0002: na 9.5 (e versoes anteriores), o atraso medio de agendamento para submissions a agentes era o mesmo intervalo de 30-40 segundos para workloads de ate 1400 jobs/min; o relatorio de performance 10.2 reporta esse mesmo atraso como baseline, portanto o comportamento de agendamento nao mudou nessa faixa de carga entre 9.5 e 10.2, mas sobe sob picos de ~5000 jobs/min em ambientes especificos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2-perfreport-0002: na 9.5 (e versoes anteriores), o atraso medio de agendamento para submissions a agentes era o mesmo intervalo de 30-40 segundos para workloads de ate 1400 jobs/min; o relatorio de performance 10.2 reporta esse mesmo atraso como baseline, portanto o comportamento de agendamento nao mudou nessa faixa de carga entre 9.5 e 10.2, mas sobe sob picos de ~5000 jobs/min em ambientes especificos?*

---

### 1375. hwa-9.5-perfreport-contrast-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2-perfreport-0003: os valores de tuning de replicacao de plano (com.ibm.tws.planner.monitor.subProcessors=10, cachesize=70000, filecachesize=40000, cachemaxage=21600000) sao recomendados pelo relatorio de performance 10.2; na 9.5 esses valores nao eram descritos com os mesmos defaults de monitor do planner, portanto tuning de planner e version-dependent e nao deve ser copiado da 10.2 para a 9.5.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2-perfreport-0003: os valores de tuning de replicacao de plano (com?*

---

### 1376. hwa-9.5-real-composer-rest-fp2-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 Fix Pack 2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5 Fix Pack 2, o composer passou a usar REST APIs para criar definicoes de objetos (calendar, domain, prompt, resource, schedule, workstation e jobs); antes do FP2 o composer usava a sintaxe nativa. Comportamento real de 9.5 FP2 que habilita automacao REST de definicoes, e distinto das versoes 9.5 base.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual endpoint REST API V2 é utilizado para composer no HWA?*

---

### 1377. hwa-9.5-real-ocli-absent-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5, o Orchestration CLI (OCLI) nao existe: nao ha documentacao oficial de OCLI para a versao 9.5. O OCLI foi introduzido apenas na versao 10.1 Fix Pack 1 como interface de linha de comando para executar jobs/job streams no plano. Portanto, qualquer instrucao que use ocli ... para um ambiente 9.5 e invalida.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5, o Orchestration CLI (OCLI) nao existe: nao ha documentacao oficial de OCLI para a versao 9.5. O OCLI foi introduzido apenas na versao 10.1 Fix Pack 1 como interface de linha de comando para executar jobs/job streams no plano?*

---

### 1378. hwa-9.5-real-rs-default-no-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security [security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5, a opcao global enRoleBasedSecurityFileCreation (rs) tem valor padrao no, mantendo o modelo de seguranca classico (baseado em arquivos de usuario e listas de acesso legadas). A partir da 10.2.8 o padrao passa a ser yes (modelo baseado em papeis). Mudanca de default real entre 9.5 e 10.2.8.

**Plataforma / Validação:** Distributed

---

### 1379. hwa-lab-10.2.8-adhoc-dynamic-submit-ready-0018

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, an ad hoc submission without a date or run cycle using `conman sbj = MDMDA#LAB_DA_SCRIPT_01;noask` was accepted and placed in the default `MDMDA#JOBS` stream, but the job remained READY and no execution request appeared in JobManager_message.log.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1380. hwa-lab-10.2.8-adhoc-logon-0028

**Regra Canônica / Evidência:**
In the HWA laboratory, an ad hoc `sbd` job dispatched after the workstation limit was raised but failed with AWSITA066E when run as a privileged user; specifying `logon=wauser` caused the ad hoc `ls` command to complete successfully with return code 0.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1381. hwa-lab-10.2.8-agent-docker-install-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (host CachyOS), o dynamic agent foi instalado em container proprio (tws-agent, RHEL 9.8 UBI-init, rede docker hwa-mesh 172.18.0.0/24, IP 172.18.0.12) usando o kit HWA_10.2.8_LNX_X86_64_AGENT.zip (baixado do Google Drive, 669MB) com o script twsinst: 'twsinst -new -agent dynamic -acceptlicense yes -uname wauser -thiscpu AGT1 -tdwbhostname tws-hwa.lab -tdwbport 31116 -sslkeysfolder <pasta PEM com ca.crt/tls.key/tls.crt> -sslpassword <pw> -wauser wauser -wapassword <pw>'. Resultado: AWSFAB033I 'The installation has completed successfully'; instalacao em /opt/HCL/TWA_wauser (binarios TWS + TWSDATA), JobManager + agente ITA iniciados, TWS_TDWB_HOSTNAME=tws-hwa.lab TWS_TDWB_PORT=31116.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent)

---

### 1382. hwa-lab-10.2.8-agent-docker-job-executed-0003

**Regra Canônica / Evidência:**
No lab container, o agente dinamico TWS-AGENT executou jobs de verdade: job stream AGTTESTJS (job AGT_ECHO, DOCOMMAND 'echo AGT_DYNAMIC_OK; uname -a', STREAMLOGON wauser, TASKTYPE UNIX, RECOVERY STOP) definida via composer add (AWSJCL003I x2) e submetida com 'conman sbs TWS-AGENT#AGTTESTJS' resultou em SUCC rc0 nas duas instancias. Prova: os archives do JobManager do agente (TWSDATA/stdlist/JM/2026.09.09/archive/*.zip) contem out.log com 'AGT_DYNAMIC_OK' e 'Linux tws-agent.lab 7.2.2-1-cachyos ... x86_64 GNU/Linux', confirmando execucao real no container do agente (kernel do host, como esperado em docker).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent)

---

### 1383. hwa-lab-10.2.8-agent-docker-registered-plan-0002

**Regra Canônica / Evidência:**
No lab container, o agente instalado com -thiscpu AGT1 foi registrado pelo broker no banco como workstation dinamica 'TWS-AGENT' (mdl.wks_workstations: wks_agent_type A, node tws-agent, tcp 0) — o broker nomeia pela base 'TWS-AGENT', nao pelo -thiscpu. A workstation so aparece no 'conman showcpus' apos JnextPlan (extensao do plano), confirmando que workstation dinamica entra no plano via virada/extensao, nao em tempo real. Após JnextPlan o plano passou a run #29 (end 09/10 00:04) com TWS-AGENT como UNIX AGENT LIMIT 10 linkado (LBI J M).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

---

### 1384. hwa-lab-10.2.8-agent-restart-ready-0020

**Regra Canônica / Evidência:**
After ShutDownLwa and StartUpLwa, MDMDA returned with the JobManager flag and resource registration resumed, but a new ad hoc submission with a unique alias still remained READY; restart alone did not resolve dispatch.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1385. hwa-lab-10.2.8-agent-restart-reconnect-0048

**Regra Canônica / Evidência:**
In the HWA laboratory, after ShutDownLwa and StartUpLwa, dynamic agent MDMDA reconnected successfully with the JobManager flag preserved, LIMIT 10 and FENCE 0 maintained, and resource registration (AWSITA083I) continued after restart.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1386. hwa-lab-10.2.8-aida-alert-cycle-0075

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1387. hwa-lab-10.2.8-aida-alert-definitions-0070

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1388. hwa-lab-10.2.8-aida-anomaly-inject-0080

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1389. hwa-lab-10.2.8-aida-ash-container-runtime-0069

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1390. hwa-lab-10.2.8-aida-config-env-0065

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1391. hwa-lab-10.2.8-aida-credentials-0066

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1392. hwa-lab-10.2.8-aida-dwc-widget-blocked-0078

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1393. hwa-lab-10.2.8-aida-email-redis-0077

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1394. hwa-lab-10.2.8-aida-images-load-0062

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1395. hwa-lab-10.2.8-aida-kpi-catalog-0071

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1396. hwa-lab-10.2.8-aida-metric-format-0072

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1397. hwa-lab-10.2.8-aida-metrics-flow-0067

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1398. hwa-lab-10.2.8-aida-network-0064

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1399. hwa-lab-10.2.8-aida-oom-es-0063

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1400. hwa-lab-10.2.8-aida-rest-api-0074

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1401. hwa-lab-10.2.8-aida-retrain-behavior-0076

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1402. hwa-lab-10.2.8-aida-special-days-0073

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1403. hwa-lab-10.2.8-aida-tar-0061

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1404. hwa-lab-10.2.8-aida-ui-health-0068

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1405. hwa-lab-10.2.8-batchman-showcpus-0004

**Regra Canônica / Evidência:**
After the initial plan was generated in the WSL2 laboratory, conman showcpus reported Batchman LIVES for the MDM workstation and displayed the generated MDMXA x-agent workstation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1406. hwa-lab-10.2.8-bmdm-aes-keys-copied-0002

**Regra Canônica / Evidência:**
Apos instalar o BMDM, as chaves de criptografia AES do MDM foram copiadas de /opt/hwa/TWSDATA/ssl/aes (key.p12 + key.sth) do container tws-hwa para o mesmo caminho no tws-bmdm, permitindo ao BMDM descriptografar arquivos criptografados como o Symphony, conforme doc awspiinstallMDM/awspiinstallMDMasBKM.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

---

### 1407. hwa-lab-10.2.8-bmdm-boot-restart-auto-0005

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8, o boot automatico do BMDM apos 'docker restart tws-bmdm' foi validado: as units systemd em cascata (tws-hosts-fix -> tebctl-tws_cpa_agent_wauser -> tws-domain-start) restauraram o BMDM sem intervencao manual. Pitfall descoberto: o bind mount /data (sdb) vinha como root:root e o 'su - wauser' falhava ao gravar /data/appserver-start.log (Permission denied), impedindo o engine de subir. Fix: chown wauser:wauser /data (persistente no sdb) + linha defensiva 'chown wauser:wauser /data' no inicio do tws-domain-start.sh. Apos o fix, o engine Liberty subiu (porta 31116), netman/batchman/JobManager ativos, e 'conman showcpus' no BMDM mostra MDM_BK como *UNIX FTA full-status linkado ao master (MDM UNIX MASTER), Batchman LIVES nos dois lados.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm)

---

### 1408. hwa-lab-10.2.8-bmdm-container-install-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (host CachyOS), o Backup Master Domain Manager foi instalado em container proprio (tws-bmdm, RHEL 9.8 UBI-init, rede docker hwa-mesh 172.18.0.0/24, IP 172.18.0.11) apontando para o banco PostgreSQL JA EXISTENTE do MDM (172.18.0.10:5432/TWS, container tws-hwa). O serverinst.sh detectou o master existente e configurou automaticamente como BKM (WAINST054I Configuring BKM; WAINST023I completed successfully, rc=0), sem criar banco proprio. O PostgreSQL do MDM foi liberado para a rede (listen_addresses='*' + pg_hba com 172.18.0.0/24 e 172.17.0.0/16 scram-sha-256) e a senha do role postgres foi resetada para credencial dedicada (registrada em CREDENCIAIS-LAB.env fora do git).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm) + tws-hwa

---

### 1409. hwa-lab-10.2.8-bmdm-fta-fullstatus-in-plan-0003

**Regra Canônica / Evidência:**
No laboratorio, a workstation do backup (MDM_BK) foi registrada no plano como FTA full-status autolink: composer display CPU=MDM_BK mostra TYPE FTA, AUTOLINK ON, FULLSTATUS ON, NODE tws-bmdm.lab TCPADDR 31111 SECUREADDR 31113. Apos 'JnextPlan -for 0000' no MDM (run #23), 'conman sc' passou a exibir MDM_BK como 'UNIX FTA' com o Symphony enviado ao BMDM (arquivo Symphony de 52.768 bytes presente em /opt/hwa/TWS/TWSDATA do tws-bmdm as 02:30).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

---

### 1410. hwa-lab-10.2.8-bmdm-switchmgr-failover-e2e-0004

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8, o failover manual MDM->BMDM foi validado de ponta a ponta: 'conman switchmgr MASTERDM;MDM_BK' (executado como wauser no master) retornou AWSBHU120I 'changed the domain manager from workstation MDM to workstation MDM_BK'. Apos a propagacao, 'conman showcpus' executado no novo master (tws-bmdm) mostrou MDM_BK como *UNIX MASTER com Batchman LIVES, e o antigo MDM convertido a UNIX FTA (LTI JW MDEA), com todos os membros do dominio (LABPOOL, MASTERAGENTS, MDMDA, MDMXA, MDM_DWB, MDM_BKA) visiveis. Comportamento confirma a doc awsrgswitchmgr: 'the old domain manager is converted to a fault-tolerant agent in the domain'.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm master temporario)

---

### 1411. hwa-lab-10.2.8-bmevents-config-0084

**Regra Canônica / Evidência:**
In the HWA 10.2.8 lab, BmEvents.conf (TWA_DATA_DIR=/opt/hwa/TWSDATA/BmEvents.conf) was configured and validated for job scheduling status event reporting. Parameters used: OPTIONS=MASTER (report all scheduling events from the scheduling environment), LOGGING=ALL (log events from all jobs/job streams, no key filter), SYMEVNTS=YES (report status immediately after plan creation), CHSCHED=HIGH (event for any schedule status transaction), and EVENT=51 101 102 103 104 105 106 151 152 154 155 156 201 202 203 204 251 252 (which completely overrides the default list 51 101 102 105 151 152 155 201 202 203 204 251 252). Output destinations: PIPE=UNISONWORK/MAGENT.P (NetView agent), FILE=/opt/hwa/TWSDATA/event.log (ASCII/UTF-8) and JSON=/opt/hwa/TWSDATA/event.json (structured JSON for third-party monitoring). After a conman stop/start of the MDM production processes (batchman, mailman, jobman restart), the event.log and event.json files were created and populated. Submitting job stream MDMDA#EVTJS_TEST produced the full event lifecycle in event.json: 106 JobSubmit, 156 SchedSubmit, 103 JobLaunch, 104 JobDone, 154 SchedDone for job EVTJOB1, in addition to 51 ProcessReset and 251 LinkDropped at batchman restart.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1412. hwa-lab-10.2.8-boot-auto-container-mdm-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, ubi9/ubi-init), o boot completo do dominio TWS apos docker restart foi automatizado com 3 units systemd: (1) tws-boot-fixes (oneshot, antes do tebctl) que reaplica 'loopback tws-hwa.lab' no /etc/hosts (docker regenera o hosts a cada start) e remove User=wauser/PIDFile= da unit tebctl se presentes; (2) tebctl-tws_cpa_agent_wauser (enabled) que sobe o agente ITA + JobManager; (3) tws-domain-start (oneshot apos o tebctl) que faz systemctl start postgresql-18 (unit disabled nao sobe sozinha), startAppServer.sh (engine Liberty, aguarda a porta do engine) e conman start&link + startmon (netman/batchman). ACHADO: a unit tebctl original instalada tinha User=wauser + Type=forking + PIDFile=status.info; como o script tebctl quando rodado como root ja faz su - wauser internamente e o status.info e gravado como wauser, o systemd recusava: 'New main PID N does not belong to service, and PID file is not owned by root. Refusing.' -> start falhava com timeout apos 5min. Remover User= e PIDFile= resolve (o script ja faz o su). Validacao: docker restart tws-hwa -> ~100s depois agent/JobManager/netman/java/mailman/batchman todos up, Batchman LIVES, plano dia vigente 00:05 BR preservado, FINAL 2359 agendado.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1413. hwa-lab-10.2.8-broker-active-sc-0079

**Regra Canônica / Evidência:**
In the HWA laboratory, the broker workstation MDM_DWB is active and LINKED to the master. 'conman sc' shows: 'MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM'. Interpreting the state letters: L = LINKED (linked to master domain), T = TCP/network link, I = in-sync/active, J = JobManager/gateway process up, W = WAGENT/broker runtime up. This corrects the earlier assessment (evidence broker-topology-0070) that the broker runtime was down because JobManagerGW had autostart=no; the broker is in fact running and linked, and the REST API V2 on /twsd:31116 is served by this broker's gateway.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1414. hwa-lab-10.2.8-broker-topology-0070

**Regra Canônica / Evidência:**
In the HWA laboratory, the Dynamic Workload Broker workstation MDM_DWB exists (wks_agent_type='B' in mdl.wks_workstations) but the broker/gateway component is NOT running: JobManagerGW.ini has autostart=no (EIF port 31132), and no broker/JobManagerGW process is listening. The engine ports (31111 netman, 31113, 31114 agent, 31115/31116/31131 java/JobManager) are up, but the external JobManager REST service returned AWSJMR011E ServiceUnavailable earlier. CRITICAL jobs validated/ran SUCC in direct topology; the WSA global option (enWorkloadServiceAssurance, default YES) is not stored in local config files (it is a database global option).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1415. hwa-lab-10.2.8-broker-topology-correction-0080

**Regra Canônica / Evidência:**
CORRECTION to evidence hwa-lab-10.2.8-broker-topology-0070. On 2026-08-18, 'conman sc' (workstation status) shows MDM_DWB is ACTIVE and LINKED: 'MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM' (L=LINKED, J=JobManager/gateway up, W=WAGENT up). The 0070 conclusion that 'the broker runtime is not running' was based only on JobManagerGW.ini autostart=no and absence of a standalone JobManagerGW process, but the broker is actually running as part of the master engine and is LINKED. Consequently the REST API V2 on /twsd:31116 (validated live in evidence 0077) is served by the broker's gateway, and the port 31116 Java/JobManager listener is the broker. The broker activation follow-up (P2a) is therefore already satisfied; no separate JobManagerGW start is required.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1416. hwa-lab-10.2.8-calendar-freedays-0057

**Regra Canônica / Evidência:**
In the HWA laboratory, a calendar object was created with $calendar NAME followed by free dates in mm/dd/yy. The calendar name is limited to 8 characters in the root folder. A job stream referencing FREEDAYS LABCAL before ON RUNCYCLE validated and was added.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1417. hwa-lab-10.2.8-carryforward-0060

**Regra Canônica / Evidência:**
In the HWA laboratory, a job stream defined with CARRYFORWARD was submitted and its instance was marked [Carry], confirming the carryforward attribute is recognized in the plan.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1418. hwa-lab-10.2.8-claims-recovery-incident-0088

**Regra Canônica / Evidência:**
Incident and recovery of data/evidence/claims.jsonl (HWA training evidence). On 2026-08-18 a consolidation script run truncated claims.jsonl from 736 to 115 canonical records (the write failed partway, leaving the preserved prefix plus the manually appended recusal record). Recovery was performed from intact sources with precedence preserved > lab > shard > other: the 115 preserved prefix, 79 lab-validation-*.jsonl records, 524 research shard records (data/incoming/research/**/*.jsonl, schema-complete drafts), and 15 staging/other evidence records, plus the recusal record. The merged, deduplicated and normalized result is 677 valid records (verified=620, insufficient_evidence=34, community_practice=13, version_dependent=8, contradicted=2), all passing scripts/validate_evidence.py. Approximately 59 previously-integrated canonical records were not recoverable from any intact source (their source shards had been consumed during earlier integration); 93 SFT-referenced claim_ids now resolve to non-existent evidence records. SFT candidate files were re-audited: the 20 EDWA candidates reference only verified claims; the 34 syntax-rest candidates had 3 orphan claim_ids (hwa-10.2.8-fence-0001, hwa-10.2.8-limit-cpu-0001, hwa-10.2.8-rest-api-v2-endpoint-0011) which were repointed to verified lab claims (hwa-lab-10.2.8-fence-validation-0044, hwa-lab-10.2.8-limit-cpu-0074, hwa-lab-10.2.8-rest-v2-port-31116-live-0077). All candidate claim_ids now resolve to claims.jsonl.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1419. hwa-lab-10.2.8-cleanup-orphans-0083

**Regra Canônica / Evidência:**
In the HWA laboratory, remaining test/orphan model objects were removed from the database, leaving a clean model. Via 'echo y | composer delete MDMDA#<stream>' the 14 remaining MDMDA test job streams were deleted (CF_TEST, CONF_TEST, CONMAN_OPS, CPLXJOB2M, CPLXSTRM, DEAD_TEST, DEPS01, FENCE_TEST, KEYJOB_TEST, LAB_DA_EVERY2M, LAB_DA_SCRIPT2M, PROMPT_TEST, RECOVTEST, VARTEST) and 3 MDMXA streams (FINAL, FINALPOSTREPORTS, LAB_EVERY2M), each AWSBIA290I Total objects deleted: 1. composer delete only accepts job streams ([workstation#]jobstream). Run cycle groups, calendars and variable tables were removed via the REST API V2 DELETE /model/{runcyclegroup|calendar|variabletable}/{id} (using the def.id field, not the root id): LABRCG (f742ef0d), LABCAL (e121ba0f) and LABTAB (be717ca3) each returned HTTP 200 with {"deletedObjects":[...],"error":false}. The default variable table MAIN_TABLE (9223ee2a) could not be deleted (AWSJDB324E 'The default variable table cannot be deleted'), which is expected. Final model state: jobstreams=0, runcyclegroup=0, calendar=0, variabletable=1 (MAIN_TABLE only).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1420. hwa-lab-10.2.8-cleanup-test-0076

**Regra Canônica / Evidência:**
In the HWA laboratory, composer delete removed the persisted test job streams created during syntax/runtime validation. Using 'composer delete <ws>#<stream>' piped with confirmation 'y', the following streams were deleted (AWSBIA290I Total objects deleted: 1): HR_TEST3, HR_TEST4, HR_TEST5, JOIN_OK2, IF_OK2, CRIT_OK, TASK_OK, PRIO_TEST, REC1, REST_HOLD, MAXDUR_TEST, MINDUR_TEST, CALEND_TEST, OOVPAR_TEST, OOVDN_TEST, WS_TEST, DB_TEST, FTP_TEST, START_FILE, START_FILEMOD. Streams reported 'Total objects deleted: 0' with AWSJCL017W 'No objects have been found' were already absent (transient/on-demand streams or previously removed). A subsequent conman 'sj =MDMDA' query returned no remaining test-looking streams (HR_*, PRIO*, REC_*, TEST, JSDL, OOV*, JOIN, IF_*, CRIT, TASK, CAL*, PAYROLL, WS_*, DB_*, FTP_*, START_*, T1*), confirming cleanup. Composer delete requires an interactive confirmation ('Are you sure...') that must be answered via stdin (e.g. 'echo y | composer delete').

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1421. hwa-lab-10.2.8-complex-stream-execution-0036

**Regra Canônica / Evidência:**
In the HWA laboratory, the previously validated complex stream CPLXSTRM was added and submitted ad hoc to MDMDA. Its four dependent jobs executed in order with priorities 10, 20, HI and GO, and the stream completed SUCC under LIMIT 2.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1422. hwa-lab-10.2.8-composer-complex-validate-0034

**Regra Canônica / Evidência:**
In the HWA laboratory, a temporary Composer file containing two job streams, four dependent UNIX jobs, stream-level EVERY/EVERYENDTIME, job-level EVERY, UNTIL, LIMIT, ONOVERLAP, FOLLOWS and mixed priorities validated successfully with seven objects and was not added to the database.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1423. hwa-lab-10.2.8-composer-every-0010

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, a Composer job stream using an inclusive daily run cycle with `( AT 1351 EVERY 0002 EVERYENDTIME 1400 )` validated successfully and was added with four UNIX jobs targeted at MDMXA.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1424. hwa-lab-10.2.8-composer-jwt-lock-0108

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, foram validados segurança e locking do composer: (1) JWT: o composer aceita 'composer -jwt <token>' para autenticação (doc awsrgusingcomposer: 'retrieve the token from the Dynamic Workload Console... run the command with the -jwt parameter'); com um token inválido, o servidor rejeita com AWSITA400E wrapping AWSITA238E 'The user is not authorized to access the server' e a operação falha (Total objects: 0) — confirma que o token é validado no servidor (não é apenas sintaxe local); a geração real de JWT exige o DWC (não instalado no lab). (2) LOCK/UNLOCK: 'composer lock js=<obj>' retorna AWSBIA307I 'Total objects locked: 1'; o display do objeto lockado mostra a coluna 'Locked By' preenchida com o usuário; 'composer unlock' retorna AWSBIA308I 'Total objects unlocked: 1'; um lock do MESMO usuário em sessão subsequente não bloqueia (relock permitido, add/modify do mesmo usuário permitido) — o bloqueio efetivo é cross-user; 'composer extract ... ;lock' requer propriedade do lock (mesmo usuário: permitido).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1425. hwa-lab-10.2.8-composer-lock-contention-0109

**Regra Canônica / Evidência:**


**Plataforma / Validação:** HWA 10.2.8 Distributed

---

### 1426. hwa-lab-10.2.8-composer-name-order-errors-0035

**Regra Canônica / Evidência:**
In the HWA laboratory, Composer rejected a temporary complex definition when the job stream name exceeded 16 bytes and when RECOVERY appeared after PRIORITY; shortening the stream name and placing RECOVERY before PRIORITY produced a successful validation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1427. hwa-lab-10.2.8-composer-prompt-user-0107

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, foram criadas e validadas definições de prompt e user via composer: (1) PROMPTS usam o marcador '$prompt' seguido de 'nome "texto"' com prefixo ':' (display sem requerer resposta) ou '!' (display sem log); exemplo: LABP1 ':EDWA lab prompt test (informational)' e LABP2 '!EDWA lab prompt (not logged)'; validate/add AWSJCL003I, display prom=LABP1 mostra o texto; sem o marcador $prompt o arquivo falha com AWSBCZ021E 'A definition keyword was expected'. (2) USERS usam o formato 'username <nome>' / 'password "<pwd>"' / 'end' (ex.: LABTESTUSER, LABSECOND); validate/add AWSJCL003I, display user=<nome> mostra 'USERNAME <nome>'; o formato deve começar com 'username', não 'USER'. (3) O comando 'conman audit' NÃO existe (command not found) — o audit trail de mudanças (justification) fica registrado no banco/views, não via comando conman.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1428. hwa-lab-10.2.8-composer-rename-new-print-0105

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, foram validados comandos composer que estavam sem evidência de laboratório: (1) RENAME: a sintaxe real é 'composer rename <tipo>=<velho> <novo_id> [;preview]' onde o tipo (ex.: js=) é declarado APENAS no identificador antigo e o novo identificador NÃO leva prefixo de tipo; ';preview' anexado ao novo identificador (ou a keyword PREVIEW separada) executa dry-run sem persistir (AWSJCL558I 'The object ... will be renamed as ...', Total objects updated: 0); sem ;preview o rename persiste (AWSJCL003I 'rename completed successfully', 1 updated) e o objeto antigo deixa de existir; renomear de volta restaura o estado (rollback OK). Keyword inválida entre os argumentos (ex.: 'to') causa AWSBIA349E 'The supplied keyword is not valid for the supplied object. The command on this object requires one of the following keywords PREVIEW'. (2) NEW: o comando 'composer new <tipo>' abre um template interativo e NÃO aceita argumento de nome junto (AWSBIA003E 'A parameter or identifier has been supplied where it is not required'); templates em subfolder 'templates' do instalador; suporta calendar/domain/eventrule/folder/job/jobstream/parameter/prompt/resource/runcyclegroup/vartable/user/wat/ws/wsclass. (3) PRINT: 'composer print <objeto>' envia a lista formatada para a impressora padrão (comando lp); no lab sem lp configurado falha com 'sh: 1: lp: not found' — mas com um fake 'lp' no PATH captura a saída formatada (banner HCL Composer Page, tabela Workstation/Job Stream Name/Valid From/Updated On/Locked By, e a definição completa SCHEDULE/DESCRIPTION/ON RUNCYCLE/:/END).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1429. hwa-lab-10.2.8-composer-sft-batch-0096

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
The HCL Workload Automation 10.2.8 training pipeline generated a bilingual Composer SFT batch (68 candidates: 34 PT / 34 EN) from 19 verified composer claims (add, commands, delete, extract, if-conddep, join, notcommands, onlate, onoverlap, outputcond, recovery, recovery-rerun, runcyclegroup, task, validate), covering read_only/mutating/destructive risks, validated by validate_sft.py and audit_sft_metadata.py, and regenerated the independent factual evaluation gold to 672 cases (336 PT / 336 EN) with anti-leak gate active.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1430. hwa-lab-10.2.8-composer-syntax-format-0104

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, o composer CLI (10.2.8.0) aceita arquivos de definição em formato de sintaxe nativo (como os arquivos de exemplo Sfinal): job definitions com 'DOCOMMAND "comando"', 'STREAMLOGON', 'DESCRIPTION', 'TASKTYPE', 'RECOVERY'; job streams com 'SCHEDULE workstation#name', 'DESCRIPTION', 'ON RUNCYCLE RC1 "FREQ=DAILY;"', ':' seguido das referências de jobs 'workstation#jobname' e 'END'. Nesse formato, os jobs referenciados devem existir como job definitions no banco (criadas antes do job stream). Arquivos XML de regras de evento (eventRuleSet) devem usar a declaração '<?xml version="1.0"?>' SEM atributo encoding e o namespace oficial 'http://www.ibm.com/xmlns/prod/tws/1.0/event-management/rules' com schemaLocation EventRules.xsd; o elemento eventCondition usa eventProvider/eventType como atributos e 'scope' como elemento filho; o filtro usa attributeFilter name/operator/value; a ação usa actionProvider/actionType/responseType. Tentativas com encoding explícito (UTF-8/ISO-8859-1) falham com AWSBIA358E 'The encoding used is not that of the locale'.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1431. hwa-lab-10.2.8-composer-syntax-slash-vs-multiline-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master), um experimento controlado de 6 variacoes determinou a sintaxe de entrada real do composer add: (1) $JOBS + linha com separador '/' entre keyword blocks falha com AWSJOM918E 'Syntax error at line 2, starting from position 9'; (2) linha solta com '/' sem $JOBS falha AWSBCZ021E; (3) linha unica sem '/' sem $JOBS falha AWSBCZ021E; (4) $JOBS + multilinha (JOBNAME na linha 1, keywords em linhas proprias) FUNCIONA (AWSJCL003I jd=...); (5) $JOBS + linha unica (JOBNAME DOCOMMAND ... STREAMLOGON ...) FUNCIONA; (6) SCHEDULE com jobs inline keyword-por-linha estilo Sfinal FUNCIONA (8 objetos). Conclusao: o separador '/' que aparece no composer display e o FORMATO DE SAIDA (serializacao), nao a sintaxe de entrada; o claim WSL composer-syntax-format-0104 que descreve o formato com '/' deve ser lido como representacao do display, com risco de AWSJOM918E se o '/' for copiado como entrada. Jobs inline dentro de SCHEDULE (como no Sfinal) criam as job definitions e o stream em um unico composer add.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1432. hwa-lab-10.2.8-composer-update-ignore-workstation-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [ignore_workstation]]`

**Regra Canônica / Evidência:**
Para marcar uma workstation como ignorada no banco de dados do HWA sem deletá-la, utiliza-se a sintaxe do composer 'update cpu=<NOME>; set ignore=on; noask', fazendo com que a estação não entre nas próximas gerações do plano Symphony.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9; HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como desativar ou ignorar temporariamente uma workstation no plano de produção sem excluí-la?*
- *Qual a sintaxe correta do comando composer update para alterar o atributo ignore de uma workstation?*

---

### 1433. hwa-lab-10.2.8-configuredb-container-rhel9-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8 (UBI-init, Docker), configureDb.sh do HWA 10.2.8 completou com sucesso com PostgreSQL 18.6 (PGDG EL9), componente MDM, database TWS em loopback:5432, gerando os schemas HWA (mdl, dwb, evt, log, pln) identicos ao lab WSL2.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1434. hwa-lab-10.2.8-confirmed-job-0055

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with CONFIRMED completed execution and entered PEND with the [Confirmed] indicator; the stream remained READY. After conman confirm MDMDA#CONF_TEST.CNFJOB;SUCC, both the job and stream became SUCC.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1435. hwa-lab-10.2.8-conman-manipulation-0068

**Regra Canônica / Evidência:**
In the HWA laboratory, conman offers altpri, link, unlink, limit, release, resource as the runtime manipulation commands; there are no standalone shift or move commands. altpri requires the job in a targetable state; an attempt against a job not yet in selection returned AWSBHU072E no objects match.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1436. hwa-lab-10.2.8-conman-operations-0065

**Regra Canônica / Evidência:**
In the HWA laboratory, the following conman runtime operations were exercised successfully: rerun job (created a successor WAIT instance), confirm job (with SUCC argument), and cancel sched (stream became CANCL with [Cancelled]). The kill command reported AWSBHU085E when the job had already completed, confirming state validation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1437. hwa-lab-10.2.8-corpus-composer-expansion-0092

**Regra Canônica / Evidência:**
The HCL Workload Automation 10.2.8 training corpus was expanded with the official Composer / job-definition documentation. 42 additional official help.hcl-software.com 10.2.8 pages were downloaded into data/raw/HCL-HWA-10.2.8/ covering: the Composer command-line interface (awsrgcomposerquickcom, awsrgcompocom, awsrgcomposercom, awsrgusingcomposer, awsrgcomposedit, awsrgcomsyn, awsrgadd, awsrgcreateextract, awsrgdelete, awsrgdisplay, awsrglocksection, awsrgmodify, awsrgnew, awsrgprintlist, awsrgprintlist1, awsrgreplace, awsrgrename, awsrgunlock, awsrgvalidate, awsrglistfolder, awsrgmkfolder, awsrgremfolder, awsrgrenamefol), and the scheduling object definitions (awsrgwsdefn, awsrgwsclassdefn, awsrgdomaindef, awsrgjobdefn, awsrgjobdefn2, awsrgjsdefn, awsrgjobstreamdefkey, awsrgcalendef, awsrgfolderdef, awsrgparmdefn, awsrgvtabledefn, awsrgpromptdef, awsrgresdef, awsrgruncycgrpdef, awsrguserdefn, awsrgconddepjoin, awsrgcondlogic, awsrgonoverlap, awsrgdeadline, awsrgworkflowtrigger). The curation pipeline was re-run: extract_docs.py produced 21917 chunks (total composer/job-def html chunks 593; 211 composer/job-def chunks landed in train_full.jsonl, up from 116 EDWA html chunks before), dedup_and_split.py produced 16994 eligible records (train 15035 / eval 1678 / buffer 281), audit passed with 0 source-holdout overlap, validate_tokens 0 sequences above 2048 tokens, and simulate_dataset_quality.py returned APROVADO COM RESSALVAS with critical=[], security_hits={}, synthetic_in_training=0, unknown_version_share dropping to 0.0104.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1438. hwa-lab-10.2.8-corpus-edwa-expansion-0089

**Regra Canônica / Evidência:**
The HCL Workload Automation 10.2.8 training corpus was expanded with 22 official documentation pages covering EDWA (event-driven workload automation), BmEvents.conf and REST/event management, downloaded from help.hcl-software.com into data/raw/HCL-HWA-10.2.8/ (awsrgevntdrivworkauto, awsrgevntrulemgmntproc, awsrgeruledef, awsrgeventpro, awsrgtwsobjectsmonitor, awsrgfilemonitorevents, awsrgapplmonitor, awsrgdatesetmonitor, awsrgactionpro, awsrgtwsaction, awsrgmessagelogger, awsrggenericaction, awsrgmailsender, awsisnetvbmevents, awsisitmtepevents, awsrgdefineeventrule, awsrgtriggerruleelem, awsrgeventsend, awsrgeventsend4dyn, awsrgevtdef, awsrgprodproc, awsrgstartstop). The curation pipeline was re-run: extract_docs.py produced 21499 chunks (22 EDWA/BmEvents pages contributed ~221 chunks, 116 of which landed in train_full.jsonl), dedup_and_split.py produced 16846 eligible records (train 14933 / eval 1670 / buffer 243), audit_dataset.py passed with 0 shared hashes and 0 document-id overlap in the source-holdout cut, validate_tokens.py reported 0 sequences above the 2048-token limit, and simulate_dataset_quality.py returned verdict APROVADO COM RESSALVAS with critical=[], security_hits={}, synthetic_in_training=0, source-holdout provenance overlap 0/0/0, language_max_delta=0.0018, and unknown_version_share dropping to 0.0105.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1439. hwa-lab-10.2.8-deadline-onlate-0056

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with DEADLINE 0001 ONLATE KILL ran past its deadline; the stream became SUCC but the job DLJOB was suppressed and shown as HOLD with [Suppressed]; [Late] <00:01, demonstrating the deadline/onlate action.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1440. hwa-lab-10.2.8-deps-chain-abend-rollover-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, fuso America/Sao_Paulo, dominio MDM master), um job stream complexo (MDM#CPLXCHAIN) com dependencias encadeadas e um job que falha foi definido via composer e submetido ad hoc com 'conman sbs = MDM#CPLXCHAIN;noask' (submit schedule; sbj e para JOB individual e retorna AWSBHU072E para stream). Comportamento observado: o job raiz CPJ_A SUCC rc0; o job CPJ_B (FOLLOWS CPJ_A, DOCOMMAND 'exit 5') foi ABEND rc5; o job CPJ_C (FOLLOWS CPJ_B) ficou HOLD (dependencia quebrada pelo ABEND); o ramo paralelo CPJ_D (FOLLOWS CPJ_A) e CPJ_E (FOLLOWS CPJ_D) executaram SUCC rc0, confirmando que dependencias FOLLOWS independntes nao bloqueiam a execucao paralela. O stream ficou STUCK enquanto havia ABEND; o rerun manual do job ABEND ('conman rr = MDM#CPLXCHAIN.CPJ_B;noask') re-executou CPJ_B que ABEND novamente (rc5); confirmar/cancelar o ABEND do CPJ_B liberou CPJ_C que rodou SUCC e o stream terminou SUCC. Estados coletados: READY, EXEC, SUCC, ABEND, HOLD, STUCK. Os jobs executaram nativamente no master MDM (via seu JobManager) - diferenca do WSL onde jobs em dynamic agent ficavam READY por dispatch.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1441. hwa-lab-10.2.8-dwc-cert-ca-attempt-0079

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1442. hwa-lab-10.2.8-dwc-cert-keytool-0081

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1443. hwa-lab-10.2.8-dwc-configuredb-postgresql-0052

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1444. hwa-lab-10.2.8-dwc-configuredb-rhel9-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8 (UBI-init), configureDb.sh do kit DWC HWA 10.2.8 completou com sucesso com PostgreSQL 18.6: componente DWC, database TDWC criado (WAINST077I/052I), role dedicada postgresdwc como DB_USER - replicando o lab WSL2 (evidencia dwc-configuredb-postgresql-0052).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1445. hwa-lab-10.2.8-dwc-default-tasks-http-0060

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1446. hwa-lab-10.2.8-dwc-default-tasks-language-0058

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1447. hwa-lab-10.2.8-dwc-dwcinst-success-0053

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1448. hwa-lab-10.2.8-dwc-engine-connection-rest-0055

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1449. hwa-lab-10.2.8-dwc-engine-server-31116-0056

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1450. hwa-lab-10.2.8-dwc-login-requires-browser-headers-0001

**Regra Canônica / Evidência:**
O login do console DWC 10.2.8 via POST /console/j_security_check retorna 400 silencioso (sem log no Liberty) quando o request nao carrega headers de browser (User-Agent Mozilla + Origin + Referer da pagina de login); com os headers, o POST retorna 302 e o LtpaToken2 e emitido - protecao do form login contra requests sem origem.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1451. hwa-lab-10.2.8-dwc-login-wauser-0054

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1452. hwa-lab-10.2.8-dwc-not-installed-0049

**Regra Canônica / Evidência:**
In the HWA laboratory, the Dynamic Workload Console (DWC) could not be installed because no DWC installer image was available; the installed image provides only the MDM component plus DWC database helper files. The DWC/Graphical Designer validation remains pending.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1453. hwa-lab-10.2.8-dwc-ui-language-acceptlang-0057

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1454. hwa-lab-10.2.8-dwc-wauser-en-login-0059

**Regra Canônica / Evidência:**


**Plataforma / Validação:** Distributed (Linux/WSL2)

---

### 1455. hwa-lab-10.2.8-dwcinst-full-success-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8, o dwcinst.sh do DWC HWA 10.2.8 completou (WAINST023I) com PostgreSQL 18.6: dwcServer Liberty em /opt/hwa/DWC/usr/servers, console HTTPS 9443, admin dwcadmin, registry TWSRealm - replicando o lab WSL2 (evidencia dwc-dwcinst-success-0053). Requisitos adicionais: DWC_ADMIN_USER/DWC_ADMIN_PW obrigatorios no properties e usuario SO do admin deve existir (startAppServer exige o owner).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1456. hwa-lab-10.2.8-dynamic-agent-dispatch-pending-0011

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, Composer definitions targeted at dynamic agent MDMDA were validated, added and submitted, but remained READY during the observation window; the JobManager log showed resource registration but no job execution request. Dynamic-agent dispatch is therefore not yet validated in this lab.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1457. hwa-lab-10.2.8-dynamic-dispatch-diagnosis-0016

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, the MDMDA dynamic agent was linked and reported resource information to the engine, but submitted test streams remained READY and JobManager recorded no job execution request during observation; dynamic-agent execution is unresolved.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1458. hwa-lab-10.2.8-dynamic-pool-workstation-e2e-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), a criacao, configuracao e execucao de jobs em Dynamic Pools (workstations do tipo POOL sob BROKER) foi validada de ponta a ponta. Descobertas arquiteturais e comportamentais comprovadas: (1) Para criar uma workstation POOL no composer (TYPE POOL), a clausula FOR MAESTRO HOST deve apontar obrigatoriamente para uma workstation do tipo BROKER (ex: MDM_DWB); tentar apontar para o MDM (tipo MANAGER) falha com AWSJCO049E ('The host supplied cannot be used because it must be a workstation of type broker'). (2) A definicao correta no composer consiste em: 'CPUNAME <NOME> DESCRIPTION ... OS OTHER FOR MAESTRO HOST MDM_DWB TYPE POOL MEMBERS <DYNAMIC_AGENT> END'. Criou-se a workstation LABPOOL com membro MDMDA (AWSJCL003I). (3) O scheduler aloca automaticamente jobs agendados na workstation virtual LABPOOL para membros ativos do pool (execucao em MDMDA com tag {MDMDA} registrada no plano). (4) Foi validado o fluxo E2E: definicao de stream LABPOOL#POOL_STREAM com job LABPOOL#POOL_JOB -> adicao no composer -> submissao no plano via conman sbs (0AAAAAAAAAAAAAET) -> liberacao de LIMIT da CPU (lc LABPOOL;10;noask) -> execucao bem-sucedida em MDMDA com SUCC rc 0 (#J1045913938).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1459. hwa-lab-10.2.8-edwa-action-run-defect-0102

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, o endpoint POST /twsd/eventrule/engine/action_run/action/run (documentado no código como 'POST operation for run a List of ActionRun') sempre retorna HTTP 400 nesta versão (10.2.8.00): o provider RESTActionRunJsonListProvider chama por reflexão ActionRun.fromJsonList(String) (getMethod) e a classe com.ibm.tws.objects.log.ActionRun NÃO possui o método estático fromJsonList (o ActionRunHeader possui; o ActionRun apenas fromJson), causando NoSuchMethodException -> 400 antes de qualquer execução. O contrato decompilado mostra que, se o corpo fosse aceito, runActions(List<ActionRun>) chamaria EventRuleEngine.runActions -> ActionPlugInManager.getPlugIn(pluginName) -> securityOK(actionRun,user,groups) -> ActionHelper.executeAction(actionRun), ou seja, re-executaria a ação real (MSGLOG re-loga, TWSAction sbs re-submete job stream, MailSender re-envia e-mail). Portanto, a execução programática de ações EDWA via action/run NÃO é utilizável nesta versão por defeito do produto; os endpoints header/query (POST, com header How-Many + Content-Type application/json) e GET /action_run/{actionrunId} funcionam normalmente (HTTP 200).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1460. hwa-lab-10.2.8-edwa-cleanup-0086

**Regra Canônica / Evidência:**
In the HWA 10.2.8 lab, the EDWA test objects created during validation were removed. Via 'echo y | composer delete EVENTRULE <name>' the rules LAB_FILE_TRIGGER and LAB_EVT_JS were deleted (AWSBIA290I Total objects deleted: 1 each), and 'echo y | composer delete MDMDA#EVTJS_TEST' deleted the test job stream (AWSBIA290I Total objects deleted: 1). A 'conman deployconf MDMDA' was issued to refresh the monitoring configuration. Remaining event rules in the model: UPDATEFAILURE, UPDATESTATUS, UPDATESUCCESS (the three default GenericEventPlugIn 'Upgrade' rules shipped with the lab). Trigger files (/tmp/hwa_oneshot/trigger.txt, trigger2.txt) and the job output file were removed.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1461. hwa-lab-10.2.8-edwa-event-rule-e2e-container-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master, enEventDrivenWorkloadAutomation=YES, deploymentFrequency=5), o fluxo EDWA (event rule) foi validado de ponta a ponta. Uma event rule 'LAB_EVT_SBS' (ruleType=filter, isDraft=no, eventCondition GenericEventPlugIn eventType=Event1 com filtros Param1=TRIGGER_LAB e Workstation=MDM, acao TWSAction actionType=sbs) foi criada via composer XML (validate AWSBIA302I 'No errors', add AWSJCL003I erule=LAB_EVT_SBS) e ativou automaticamente em ~5min (deploymentFrequency) ficando 'active'. O comando 'sendevent Event1 GenericEventPlugIn Param1=TRIGGER_LAB Workstation=MDM' retornou AWSGTW113I e a acao sbs submeteu o job stream MDM#EVTJS_TEST no plano, que executou SUCC (EVTJOB1 SUCC rc0 #J12318 as 00:42 de 09/06) - prova de que a event rule acionou o submit (nao houve JnextPlan/sbs manual). Descobertas de sintaxe do XML da rule (AWSVAL): o parametro da acao TWSAction sbs e 'JobStreamName' (nome) + 'JobStreamWorkstationName' (workstation) - 'JobStream' nao e valido (AWSVAL005E); o eventType deve ser o definido no GenericEventPlugIn ('Event1', nao nome arbitrario - AWSVAL011E); Workstation do Event1 nao aceita wildcard (AWSVAL021E, wildcardAllowed=false). Ativacao via REST PUT /twsd/eventrule/deployment/rule_builder/start retornou HTTP 401 (exige autenticacao), por isso usou-se a ativacao automatica por deploymentFrequency.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1462. hwa-lab-10.2.8-edwa-rest-and-restart-0095

**Regra Canônica / Evidência:**
HWA 10.2.8 lab findings on the event-rule REST API and WSL restart procedure. (1) The Liberty engineServer registers an EventRuleEngineApplication under /twsd exposing REST resource classes for event rules: MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, RuleInstanceEventRuleResource, ActionRunEventRuleResource, PluginConfigurationEventRuleResource (paths visible in messages.log as /eventrule/engine/*, /eventrule/deployment/*, and /api/v2/eventrule). Direct GET/POST/OPTIONS against /eventrule/engine/messageLog, /messageLogRecord, /auditRecord, /actionRun, /ruleInstance, /pluginConfiguration and /eventrule/deployment/deploy all returned HTTP 404 even with basic auth and empty JSON or query params - the resources require specific sub-paths/params not discoverable without the deployed Swagger UI for that application, so event-rule CRUD/query over REST is not usable via the documented paths alone. (2) GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration consistently returns AWSJSY404E wrapping AWSBIN091E 'An error occurred obtaining the monitoring configuration file for workstation ... The workstation does not support monitoring.' for MDMDA and MDMXA even though monman + ssmagent EDWA are running and FileMonitor/TWSObjectsMonitor rules work - the REST read of the monitoring configuration is broken/unsupported on these broker-managed workstations, while event processing itself is functional. (3) WSL restart procedure: after a WSL Ubuntu reboot only the JobManager agent and the EDWA ssmagent start automatically (via the CPA systemd unit tebctl-tws_cpa_agent_wauser); the engineServer (Open Liberty) must be started with 'sudo -u wauser /opt/hwa/appservertools/startAppServer.sh' (equivalent to conman startappserver), then the production processes with 'conman start MDM' (batchman/mailman/jobman), and the monman event monitoring engine with 'conman startmon MDMDA' + 'conman startmon MDM' (monman does NOT auto-start on reboot even though conman sc shows the M flag from the plan). The WSL /etc/hosts regenerates on reboot and loses the '127.0.0.1 MDMHOST' alias, which must be re-added or the Resource Advisor logs AWSRES003E and AWSKRAE100E (heartbeat missed).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1463. hwa-lab-10.2.8-edwa-rule-builder-put-0101

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, os endpoints de gerenciamento do rule builder EDWA são PUT (não POST): PUT /twsd/eventrule/deployment/rule_builder/start e PUT /twsd/eventrule/deployment/rule_builder/stop retornam HTTP 204 No Content (o 405 documentado anteriormente ocorria porque o verbo POST era usado). O start dispara o build das regras pendentes dentro do ciclo de deployment: o log do engineServer registra AWSJCO125I 'The event rule UPDATEFAILURE/UPDATESTATUS/UPDATESUCCESS has been successfully built. The rule status is set to ACTIVE.'; o GET /twsd/eventrule/deployment/active_rules continua reportando AWSJCO119I 'No event rules are deployed.' mesmo com as 3 regras ativas (comportamento consistente com a documentação REST que lê a configuração de deployment, não o estado real das regras). O estado real das regras deve ser confirmado via 'composer list EVENTRULE' (3 regras active: UPDATEFAILURE, UPDATESTATUS, UPDATESUCCESS).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1464. hwa-lab-10.2.8-edwa-rules-0085

**Regra Canônica / Evidência:**
In the HWA 10.2.8 lab, event-driven workload automation (EDWA) was configured and validated end-to-end on the dynamic broker workstation. (1) The event rules are managed by the composer command line (add/validate/list/display EVENTRULE) with XML validated against EventRules.xsd; the exact syntax is 'add <file>' and 'validate <file>;syntax' (no 'EVENTRULE' type prefix). (2) A FileMonitor event rule (eventType FileCreated, filteringPredicate FileName/Workstation/SampleInterval) was added as non-draft (isDraft=no); the rule builder deployed it within the default deploymentFrequency (5 minutes) - status changed from 'activation pending' to 'active', and the generated monitoring configuration appeared in /opt/hwa/TWSDATA/EDWA/monconf/ (FileMonitor.cfg, activeRules.txt, deployconf.zip) with the ssmagent.bin EDWA instance reloading it. (3) Creating the monitored file /tmp/hwa_oneshot/trigger.txt was detected by the ssmagent (traps.log SNMP trap 'FileCreatedEvent event', Workstation=MDMDA) and delivered to the event processing server (running in the Open Liberty engineServer on MDM) which logged the rule instance and the resolved action message in the database (log.llrc_log_records: AWSMSL101I 'The message ... has been successfully logged', MessageLogger MSGLOG action with variables %{fileEvt1.FileName}/%{fileEvt1.Workstation} substituted). (4) A second rule with actionProvider TWSAction actionType sbs (SubmitJobStream, parameters JobStreamName=EVTJS_TEST + JobStreamWorkstationName=MDMDA) executed 'SBS MDMDA#EVTJS_TEST' (AWSTAP101I 'The job stream EVTJS_TEST has been successfully submitted') and the job stream + job EVTJOB1 actually ran (pln.pjor_job_runs status E, actual start/end timestamps, JobManager archive zip with script.sh/out.log/trace.log confirming the taskLauncher launched script.sh as user wauser). The monman flag M is present on MDM and MDMDA in conman showcpus.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1465. hwa-lab-10.2.8-edwa-sendevent-0093

**Regra Canônica / Evidência:**
In the HWA 10.2.8 lab, the GenericEventPlugIn custom-event path was validated end-to-end after the WSL server restart. The three default event rules (UPDATEFAILURE/UPDATESTATUS/UPDATESUCCESS, eventProvider=GenericEventPlugIn, eventType=Upgrade, filtering on Message/Workstation/UpgradeStatus) were confirmed active in the database (evt.eeru_event_rules status A, draft N). The event definitions were dumped with evtdef dumpdef, showing the Upgrade event properties Message (required, wildcard), Workstation (required) and UpgradeStatus (required, wildcard). Running 'sendevent -hostname 127.0.0.1 -sslport 31131 Upgrade MDMDA Message=Success_Upgrade Workstation=MDMDA UpgradeStatus=Completed' returned AWSGTW113I 'The event has been successfully sent.' and the event processing server logged AWSEVP001I 'The following event has been received: event type = UPGRADE' followed by AWSEVP007I 'The following event has matched an existing event condition'. The MessageLogger action of UPDATESUCCESS then executed: log.llrc_log_records shows the rule instance (llrc 903), the resolved event message 'Update agent MDMDA: Update successfully completed.' (904) and AWSMSL101I 'The message ... has been successfully logged' (905); the traceACT.log confirms ActionWrapper MSGLOG MessageLogger + ActionHelper.executeAction. The event processor runs on the MDM (AWSAEM006I 'This workstation MDM is the Event Processor Manager'). Key finding: the EIF transport to the event processor uses SSL on port 31131 (eventProcessorEIFSslPort default), so 'sendevent' must use -sslport (plain -port did not deliver); also the WSL reboot resets /etc/hosts so the 127.0.0.1 MDMHOST alias must be re-added, otherwise the Resource Advisor (AWSRES003E) and monitoring deployment fail.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1466. hwa-lab-10.2.8-edwa-sendevent-e2e-0103

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, o fluxo programático de automação orientada a eventos foi validado de ponta a ponta: (1) regra EDWA 'LAB_SENDEVT' (ruleType=filter, isDraft=no, eventCondition eventProvider=GenericEventPlugIn eventType=Event1 com filtros Param1=LAB_TRIGGER e Workstation=MDMDA, ação TWSAction sbs para MDMDA#EVTJS_TEST) criada via composer XML validado e adicionada (composer add, AWSJCL003I); (2) a regra é ativada imediatamente com PUT /twsd/eventrule/deployment/rule_builder/start (HTTP 204) disparando AWSJCO125I 'The event rule LAB_SENDEVT has been successfully built. The rule status is set to ACTIVE' (alternativa ao deploymentFrequency de 5 min); (3) o comando 'sendevent Event1 GenericEventPlugIn Param1=LAB_TRIGGER Workstation=MDMDA' retorna AWSGTW113I e o engineServer registra AWSEVP001I (event type = EVENT1; provider = GenericEventPlugIn; scope = LAB_TRIGGER on MDMDA), AWSEVP007I (matched an existing event condition), AWSAHL004I (event rule instance LAB_SENDEVT triggered), AWSAHL002I (action sbs started), AWSTAP101I ('The job stream EVTJS_TEST has been successfully submitted'), AWSAHL003I (action completed) e AWSAHL005I (event rule instance completed successfully); (4) o ActionRun correspondente aparece no REST POST /twsd/eventrule/engine/action_run/header/query como {id ...1219, actionType=sbs, ruleName=LAB_SENDEVT, pluginName=TWSAction, actionStatus=SUCCESSFUL, actionResult=MDMDA#EVTJS_TEST[(0010 22/08/2026),(0AAAAAAAAAAAAAPH)]}; (5) a nova instância MDMDA #EVTJS_TEST 0010 08/22 EXEC com EVTJOB1 WAIT aparece no plano (conman sj). Este é o caminho suportado e documentado para executar ações EDWA programaticamente, em contraste com o endpoint REST interno action/run (defeito hwa-lab-10.2.8-edwa-action-run-defect-0102).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1467. hwa-lab-10.2.8-edwa-twsobjectmonitor-0094

**Regra Canônica / Evidência:**
In the HWA 10.2.8 lab, the TWSObjectsMonitor event provider was validated end-to-end after the WSL server restart. An event rule LAB_TWS_OBJ (eventProvider=TWSObjectsMonitor, eventType=JobStatusChanged, filteringPredicate JobName=EVTJOB1, Workstation=MDMDA, Status=Successful) with a MessageLogger (MSGLOG) action was added via composer XML; the rule builder made it ACTIVE (AWSJCO125I) within the deployment cycle and the event processing server loaded the rule (traceACT: eventType JOBSTATUSCHANGED, verifySingleCondition JobName/Status). Submitting job stream MDMDA#EVTJS_TEST (containing EVTJOB1) and running conman startmon to start the monman monitoring engine produced: monman sent the EIF event 'JobStatusChanged ... EventProvider=TWSObjectsMonitor ... JobStreamName=EVTJS_TEST JobName=EVTJOB1 Status=Successful InternalStatus=SUCC Login=wauser'; the event processor logged AWSEVP001I 'event type = JOBSTATUSCHANGED; event provider = TWSObjectsMonitor; event scope = MDMDA # EVTJS_TEST . (MDMDA #) EVTJOB1 [Successful / SUCC]' and AWSEVP007I 'has matched an existing event condition'; the MessageLogger action executed (llrc: rule instance, resolved message 'LAB_TWS_OBJ: job EVTJOB1 Successful on MDMDA', AWSMSL101I 'The message ... has been successfully logged'; traceACT ActionWrapper MSGLOG + ActionHelper.executeAction).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1468. hwa-lab-10.2.8-edwa-twsobjectmonitor-jobstatuschanged-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), o provedor de eventos TWSObjectsMonitor foi validado com o evento JobStatusChanged e a acao MessageLogger (MSGLOG). Descobertas criticas de sintaxe e validacao: (1) O evento JobStatusChanged monitora mudancas de estado de jobs (JobName, Workstation, Status='Successful'). O atributo Status exige valor capitalizado ('Successful', e nao SUCC). (2) A acao MessageLogger (MSGLOG) exige obrigatoriamente o parametro 'ObjectKey' (omitir causa AWSVAL006E 'The mandatory parameter ObjectKey is not specified'). (3) O atributo 'Severity' da acao MSGLOG aceita valores como 'Info', 'Warning' e 'Error'; informar 'Information' e rejeitado com AWSVAL018E. A regra LAB_STATUS_RULE foi validada e adicionada com sucesso no composer (AWSJCL003I).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1469. hwa-lab-10.2.8-effective-host-profile-0022

**Regra Canônica / Evidência:**
In the HWA laboratory, MDMHOST is an intentional loopback alias and is consistently used by the MDMDA workstation NODE and JobManager ResourceAdvisorUrl; the real WSL hostname is DESKTOP-298GT47.localdomain. Changing to the real FQDN requires coordinated NODE, URL, DNS and certificate SAN changes.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1470. hwa-lab-10.2.8-empty-claims-resolved-0091

**Regra Canônica / Evidência:**
All 10 remaining orphan claims from the 2026-08-18 re-verification batch were resolved. (A) The 9 claims with empty recovered text (hwa-10.2.8-startmon-stopmon-0001, hwa-10.2.8-srv-traces-0003, hwa-10.2.8-upgrade-certs-required-0005, hwa-10.2.8-upgrade-gskit-openssl-0004, hwa-10.2.8-upgrade-order-0006, hwa-10.2.8-dwc-trace-configdropins-0001, hwa-10.2.8-dwc-trace-template-0002, hwa-10.2.8-ocli-release-job-persist-0001, hwa-10.2.8-mdm-aes-keys-0005) were recovered from data/hwa_tws_unified_dataset.json rag_corpus, which preserves the original verified_claim records (text, source_url, supporting_quote, risk) for those claim_ids; their claim text, official source and supporting quote were restored and status set back to verified. (B) hwa-10.2.8-dwc-mdm-distinct-0008 (DWC and MDM are distinct components; DWC version >= engine version) was upgraded from version_dependent to verified using the official IBM Dynamic Workload Console 10.2.0 Release Notes interoperability table (DWC 10.2.0 connects to MDM/DDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4 - i.e. same-version or earlier engines), corroborated by the 9.5 and 9.4 Release Notes tables. claims.jsonl final: 773 valid records (716 verified, 34 insufficient_evidence, 8 version_dependent, 13 community_practice, 2 contradicted).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1471. hwa-lab-10.2.8-every-schedule-valid-0017

**Regra Canônica / Evidência:**
The HWA 10.2.8 stream definition `ON RUNCYCLE RULE1 "FREQ=DAILY;" ( AT 1351 EVERY 0002 EVERYENDTIME 1400 )` is syntactically valid in Composer, and the submitted MDMDA instance reached READY; the observed READY state is therefore not evidence of a Composer schedule syntax error.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1472. hwa-lab-10.2.8-every-stream-job-execution-0037

**Regra Canônica / Evidência:**
In the HWA laboratory, an ad hoc submission of the stream CPLXJOB2M containing a job-level EVERY 0002 executed the first CPLX_EVERY instance at 14:59 and a second every run at 15:01; both completed SUCC with return code 0.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1473. hwa-lab-10.2.8-fence-validation-0044

**Regra Canônica / Evidência:**
In the HWA laboratory, with FENCE 20 on MDMDA, jobs of priority 10 and 20 entered the FENCE state and did not run, while jobs of priority 30, HI and GO ran SUCC. This confirms fence blocks jobs with priority less than or equal to the fence.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1474. hwa-lab-10.2.8-final-cycle-d1-rollover-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, RHEL9 UBI9, timezone America/Sao_Paulo), o ciclo FINAL de virada de plano (Sfinal) executou de ponta a ponta com sucesso: MDMXA#FINAL (2359 09/04 carry) executou STARTAPPSERVER->MAKEPLAN->SWITCHPLAN todos SUCC rc0, e o MDMXA#FINALPOSTREPORTS executou CHECKSYNC->CREATEPOSTREPORTS->UPDATESTATS todos SUCC rc0, gerando e ativando o plano de D+1 e instanciando automaticamente o proximo MDMXA#FINAL (2359 09/05) HOLD no schedule. Apos a virada, o plano de producao estendeu para o dia seguinte e o FINAL de hoje ficou agendado 23:59 pronto para rodar e gerar D+1 novamente - corrente auto-sustentavel de planos (dia vigente + D+1). Limit das workstations MDM/MDMXA precisou ser 10 (lc MDM;10;noask) para os jobs executarem.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1475. hwa-lab-10.2.8-first-jnextplan-0003

**Regra Canônica / Evidência:**
In the WSL2 laboratory, JnextPlan -for 0000 created the initial preproduction and production plans and loaded the resulting Symphony file into the database after MDM installation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1476. hwa-lab-10.2.8-follows-opens-validate-0039

**Regra Canônica / Evidência:**
In the HWA laboratory, a temporary Composer definition using FOLLOWS and OPENS validated successfully without persistence; DEP_B followed DEP_A and DEP_C required the file /tmp/hwa_dep_ready and followed DEP_B.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1477. hwa-lab-10.2.8-host-alias-gateway-0019

**Regra Canônica / Evidência:**
In the HWA laboratory, the WSL host is DESKTOP-298GT47.localdomain, while MDMHOST is an intentional /etc/hosts alias resolving to 127.0.0.1 and is consistently used by the MDM workstation NODE and direct ResourceAdvisorUrl. JobManagerGW autostart=no is not changed because the agent is configured for direct ResourceAdvisorUrl access rather than gateway routing.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1478. hwa-lab-10.2.8-jnextplan-from-timezone-0026

**Regra Canônica / Evidência:**
In the HWA laboratory, after ResetPlan, JnextPlan -from 08/17/2026 0000 -for 2400 created a plan reported as starting at 03:00 America/Sao_Paulo, demonstrating that omitting an explicit timezone can shift the interpreted start time in this environment.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1479. hwa-lab-10.2.8-jobs-next-day-after-plan-extension-0023

**Regra Canônica / Evidência:**
In the HWA laboratory, after JnextPlan -for 2400 extended the production plan through 08/18, ad hoc jobs submitted without into= were placed in the implicit MDMDA#JOBS instance scheduled at 0000 on 08/18. This was not caused by the job's own schedule; it followed the current plan's JOBS instance selection.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1480. hwa-lab-10.2.8-jobtypes-0064

**Regra Canônica / Evidência:**
In the HWA laboratory, job definitions using TASKTYPE DB, WEB and FTP all validated, were added and executed SUCC on dynamic agent MDMDA, confirming these integration job-type keywords are accepted and run.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1481. hwa-lab-10.2.8-keyjob-0058

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with KEYJOB ran and completed SUCC in the plan, confirming the keyjob attribute is accepted and marked in the plan.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1482. hwa-lab-10.2.8-limit-cpu-0074

**Regra Canônica / Evidência:**
In the HWA laboratory, the conman command 'lc MDMDA;5;noask' (limit cpu) was accepted ('Command forwarded to batchman for MDMDA'), demonstrating the limit cpu command syntax. Earlier the post-install MDM banner showed 'Limit: 0, Fence: 0'. A job stream whose jobs were HOLD due to the low limit ran to completion (BLK4 EXEC, SUC4 SUCC) once the limit condition cleared, confirming limit is the concurrency gate.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1483. hwa-lab-10.2.8-limit-follows-hold-0073

**Regra Canônica / Evidência:**
In the HWA laboratory, a submitted job stream went to HOLD because the dynamic agent workstation MDMDA has LIMIT 0 (post-install default), so jobs were not launched. Once the limit condition cleared, jobs ran (BLK/SUC completed SUCC). A job following a predecessor (FOLLOWS MDMDA#STREAM.JOB) executed SUCC normally, confirming internal follows dependency resolution. The conman 'release job ...;FOLLOWS' returned AWSBHU043E 'dependency not found' when the job was in HOLD due to limit rather than an actual external follows dependency; 'limit cpu MDMDA;5;noask' returned AWSBHU048E 'ambiguous selector' because the workstation selector matched multiple entries.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1484. hwa-lab-10.2.8-limit-zero-ready-rootcause-0027

**Regra Canônica / Evidência:**
In the HWA laboratory, MDMDA had workstation job limit 0 and the test jobs had priority 10; they remained READY. After `conman lc MDMDA;10`, the jobs were dispatched and completed successfully. HCL documents that limit 0 allows only HI/GO priority jobs from a READY stream, while `system` means no limit.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1485. hwa-lab-10.2.8-maxdur-kill-0059

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with MAXDUR 1 ONMAXDUR KILL running sleep 120 was killed at 1 minute: stream ABEND, job ABEND return code 143, marked [MaxDurationExceeded] [KillSubmitted] maxdur=00:01.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1486. hwa-lab-10.2.8-mdm-backup-restore-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master, PostgreSQL 18.6), o backup e restore do master domain manager foi validado de ponta a ponta, cobrindo lacuna que no corpus existia so como claim de doc (hwa-10.2.8-backup-backup-master-data-0001 recomenda backup dos master data files, sem procedimento validado). (1) Backup do banco: pg_dump -Fc do TWS gerou dump custom de ~444KB e do TDWC ~350KB (banco TWS = 17MB). (2) Backup do master data file Symphony: copia de /opt/hwa/TWSDATA/Symphony (~55KB). (3) PROVA DE RESTAURABILIDADE reversivel: criou-se banco clone TWS_BKPTEST, pg_restore do dump sem erros (rc=0), e o clone ficou identico ao original - 137/137 tabelas (information_schema excluindo pg_catalog/information_schema), 2 job streams de modelo (mdl.ajs_abstract_job_streams) e 30 instancias de job stream (mdl.jsi_job_stream_instances, o plano com Sfinal/FINAL diario) preservadas. O clone de teste foi removido (dropdb) - zero impacto no banco de producao TWS. Acesso ao postgres via runuser -l postgres (socket local); os dumps foram gravados em /data (mount sdb).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), PostgreSQL 18.6

---

### 1487. hwa-lab-10.2.8-mdm-serverinst-flags-validation-0001

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o instalador do Master Domain Manager (serverinst.sh) valida rigorosamente as seguintes regras e emite os respectivos códigos oficiais: (1) Rejeição de licença não aceita com WAINST036I ('Accept the license and terms conditions before proceeding with the installation'); (2) Exigência de SGBD suportado com WAINST033E ('Incorrect value for the option --rdbmstype. Expected values are < DB2 | ORACLE | MSSQL | IDS | POSTGRESQL >'); (3) Obrigatoriedade estrita de credenciais com WAINST024E ('The following option is required: --dbhostname' / '--wapassword'); (4) Validação ativa de conectividade com o banco via chamada prévia do configureDb.sh com ação test_connection_to_db (falha reportada como WAINST015E se o SGBD recusar a credencial); (5) Validação de propriedade dos binários do kit extraído com WAINST0517E ('The owner ... of the directory ... is not the same as the user who is installing the product').

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa)

---

### 1488. hwa-lab-10.2.8-mdmhost-dns-recovery-0161

**Regra Canônica / Evidência:**
Distinguish real plan corruption from DNS/link failure: with DNS failure the master-side plan state is consistent (planman showinfo run 18, Symphony file updated by deploy, batchman LIVES run 18) while only the workstation linkage and agent plan delivery are broken. planman resync/checksync/deploy do NOT fix hostname resolution; running them against an unresolved alias keeps the agent on the previous run.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1489. hwa-lab-10.2.8-mdmhost-dns-symphony-mismatch-0160

**Regra Canônica / Evidência:**
conman showcpus during the failure shows the dynamic agent stranded on the previous plan run: MDM run 18, MDMDA run 17 with empty state (no LTI flags), while MDMXA (extended agent, unixlocl method) is LINKED on run 18. The agent therefore never received the new Symphony (run 18) deployed by planman, producing the agent-side symptom "not got the latest Symphony file version" on start.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1490. hwa-lab-10.2.8-message-bia087e-0148

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
AWSBIA087E (syntax error no composer): o comando show nao existe no composer 10.2.8 — ao usar composer -jwt com 'show stl=...' o retorno e AWSBIA087E indicando erro de sintaxe. Comandos validos no composer 10.2.8: ls, add, validate, delete. Validado no lab: composer -jwt $JWT 'show stl=MDMDA;@#@.@' retornou AWSBIA389E -> AWSITA400E -> AWSITA238E para token valido, e AWSBIA087E para sintaxe invalida. Fonte: lab HWA 10.2.8 (WSL2) + Troubleshooting Guide.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA389E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA389E no HWA?*
- *Qual é o significado da mensagem de erro AWSITA238E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA238E no HWA?*
- *Qual é o significado da mensagem de erro AWSBIA087E no HWA e qual ação é recomendada?*

---

### 1491. hwa-lab-10.2.8-message-bia302i-0151

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
AWSBIA302I: mensagem informativa do composer indicando objeto validado/adicionado. Observada no lab: um arquivo Composer temporario com dois job streams, quatro jobs UNIX dependentes, EVERY/EVERYENDTIME no stream, EVERY/UNTIL/LIMIT/ONOVERLAP/FOLLOWS no job e prioridades mistas foi validado com sucesso com sete objetos e nao foi adicionado ao banco. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIA302I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIA302I no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual é o significado da mensagem de erro AWSBIA302I no HWA e qual ação é recomendada?*

---

### 1492. hwa-lab-10.2.8-mindur-continue-0061

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with MINDUR 0001 completed SUCC with the [MinDurationNotReached] [Continue] indicator, confirming the mindur minimum-duration monitoring attribute.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1493. hwa-lab-10.2.8-modify-replace-folder-0045

**Regra Canônica / Evidência:**
In the HWA laboratory, a folder LAB was created with composer mkfolder and navigated with chfolder; a job JOB_A was added inside it. composer replace updated JOB_A from lab_ls.sh/RECOVERY STOP to fail_continue.sh/RECOVERY CONTINUE, while composer modify failed in batch because it is interactive.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1494. hwa-lab-10.2.8-needs-missing-resource-0040

**Regra Canônica / Evidência:**
In the HWA laboratory, Composer rejected validation of a NEEDS dependency when the referenced resource MDMDA#RES01 did not exist, returning AWSJCO082E; FOLLOWS and OPENS in the same file validated successfully after NEEDS was removed.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1495. hwa-lab-10.2.8-needs-resource-create-blocked-0041

**Regra Canônica / Evidência:**
In the HWA laboratory, the `resource MDMDA#RES01;1;noask` command did not create a missing resource; it returned AWSBHU072E because no matching resource object existed. The NEEDS execution test therefore requires creating the persistent resource definition through the model/DWC/Composer resource-definition workflow before running the stream.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1496. hwa-lab-10.2.8-nightly-rollover-d1-real-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, America/Sao_Paulo), a virada noturna REAL do plano aconteceu automaticamente e sem intervencao manual, validando o modelo 'dia vigente 00:05 + D+1': o MDMXA#FINAL 2359 09/05 executou no horario agendado (23:59 BR) STARTAPPSERVER->MAKEPLAN->SWITCHPLAN todos SUCC rc0, seguido do MDMXA#FINALPOSTREPORTS 2359 09/05 com CHECKSYNC->CREATEPOSTREPORTS->UPDATESTATS SUCC rc0. O plano de producao virou para o dia seguinte: de '09/05 00:05 -> 09/06 00:04' (run 19) para '09/06 00:05 -> 09/07 00:04' (run 20), com o novo MDMXA#FINAL 2359 09/06 ja HOLD agendado (carryforward). Preproduction ate 09/20. Confirma a corrente auto-sustentavel de planos: cada dia as 23:59 o FINAL roda e gera/ativa o plano do dia seguinte (D+1), que comeca 00:05 - sem necessidade de JnextPlan manual.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1497. hwa-lab-10.2.8-onoverlap-0062

**Regra Canônica / Evidência:**
In the HWA laboratory, job streams with ONOVERLAP PARALLEL and ONOVERLAP DONOTSTART both validated and their jobs completed SUCC.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1498. hwa-lab-10.2.8-opens-file-dep-hostname-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, dominio MDM master), uma dependencia de arquivo OPENS foi validada ao vivo: o job MDM#CPJ_WAIT com 'OPENS /tmp/tws_file_trigger.txt' dentro do job stream CPLXOPENS, ao ser submetido via sbs, ficou HOLD com a dependencia 'tws_file_trigger.txt' listada (aguardando o arquivo). CAUSA RAIZ de nao liberar mesmo apos criar o arquivo: o agente/jobman nao conseguia reportar o recurso ao engine porque o hostname 'tws-hwa.lab' nao resolvia no container (o /etc/hosts so tinha localhost e os enderecos da interface associados ao hostname real 8189d3570cc2). O JobManager_message.log mostrava AWSITA081E repetido: 'The agent can not send the resource information a https://tws-hwa.lab:31116/JobManagerRESTWeb/JobScheduler/resource' com AWSITA366E 'Could not resolve hostname'. Apos adicionar 'loopback tws-hwa.lab' ao /etc/hosts, o monitor detectou o arquivo e o job executou SUCC rc0. O conman/composer conectavam normalmente (usam outro caminho de resolucao), mascarando o problema ate o teste de recurso de arquivo.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1499. hwa-lab-10.2.8-orphan-reverify-0090

**Regra Canônica / Evidência:**
All 93 orphaned SFT-referenced claim_ids (lost in the 2026-08-18 claims.jsonl truncation incident) were re-verified against official HCL documentation and consolidated back into data/evidence/claims.jsonl. The claim text and supporting context for each orphan were recovered from the approved SFT answers (data/sft/*.jsonl) that had been generated from the original verified claims. Four parallel hwa-source-verifier research batches (conman-ops 15, show-cmds 13, install-upgrade 22, plan-rest-dwc 43) opened the official help.hcl-software.com pages (with URL corrections where the inferred slugs 404'd, e.g. awsrgconmanretcod.html, awsadoptman.html, awsrgevtsize.html, awsrgcancelsched.html, awsrgplretrplan.html, awsrgplresyncplan.html, awsrgplchksyncplan.html, awsrgplunlkplan.html, awsrgchddjjch.html, eqqg1JWTAPIKey.html, r_kill.html, awsrgcreateextract.html, awsadtunemirr.html, awspiinstallDWCupgr.html, awspiparallelupgradefrom94TLS.html, awspiupgrading.html, awstrmakeplan5-8, awstrswitchplan3, awsrgstdlistformat5.html) and captured verbatim supporting quotes. Result: 83 re-verified as verified, 1 as version_dependent (hwa-10.2.8-dwc-mdm-distinct-0008: the DWC>=engine version rule was not found in the v1028 pages opened), and 9 as insufficient_evidence (records whose recovered claim text was empty: hwa-10.2.8-startmon-stopmon-0001, hwa-10.2.8-srv-traces-0003, hwa-10.2.8-upgrade-certs-required-0005, hwa-10.2.8-upgrade-gskit-openssl-0004, hwa-10.2.8-upgrade-order-0006, hwa-10.2.8-dwc-trace-configdropins-0001, hwa-10.2.8-dwc-trace-template-0002, hwa-10.2.8-ocli-release-job-persist-0001, hwa-10.2.8-mdm-aes-keys-0005 — these must be excluded from approved SFT data until the original claim text is recovered). claims.jsonl now has 772 valid records (705 verified); every SFT-referenced claim_id resolves to an existing claim.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1500. hwa-lab-10.2.8-plan-timezone-consolidated-0047

**Regra Canônica / Evidência:**
In the HWA laboratory, JnextPlan -for 0000 creates a zero-duration plan with no instances; JnextPlan -for 2400 extends the plan and shifts the implicit JOBS stream to the next day. ResetPlan without -scratch archives the current Symphony and preserves the preproduction plan. JnextPlan -from 08/17/2026 0000 -for 2400 created a plan starting at 03:00 America/Sao_Paulo, demonstrating that an unqualified -from is interpreted with a default timezone.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1501. hwa-lab-10.2.8-planman-0066

**Regra Canônica / Evidência:**
In the HWA laboratory, planman showinfo returned the production plan details (plan creation start 08/17/2026 03:00 America/Sao_Paulo, run number 6), and planman confirm updated the run number successfully (AWSJCL065I).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1502. hwa-lab-10.2.8-planman-resync-hot-recovery-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), o procedimento de sincronizacao e recuperacao a quente de plano via 'planman resync' foi validado com sucesso sem interrupcao do motor de producao. O comando envia a solicitacao simultaneamente para o batchman e para o Liberty application server (AWSBEH119I 'Resync command forwarded to batchman and application server'). Em seguida, monitora o ciclo de sincronizacao (AWSJCL070I 'Symphony file load is not yet started' seguido de AWSJCL074I 'Symphony file successfully loaded in Database'), recarregando o estado em memoria do Symphony para o banco PostgreSQL de forma transacional e consistente, mantendo o status do batchman inalterado (Batchman LIVES).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1503. hwa-lab-10.2.8-postgres-disabled-after-container-restart-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (ubi9/ubi-init, systemd), o servico postgresql-18 e unit systemd DISABLED (nao sobe sozinho no boot do container). Apos um docker stop/start de tws-hwa, o PostgreSQL ficou inativo (porta 5432 sem listener) enquanto o engineServer (Liberty java) subiu via tebctl/start_tws.sh e entrou em loop de retry 'Connection refused' (AWSJDB802E / DSRA0010E) sem completar o boot das aplicacoes (HTTP 404). ORDEM CORRETA de restart do dominio MDM no container: (1) systemctl start postgresql-18; (2) agente ITA via systemctl start tebctl-tws_cpa_agent_wauser; (3) startAppServer.sh (engineServer Liberty); (4) conman start&link + startmon para batchman. Efetivando o timezone America/Sao_Paulo no engine: parar via stopAppServer.sh, trocar o localtime, reiniciar startAppServer.sh (o engine Java so pega o TZ novo no boot).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1504. hwa-lab-10.2.8-postgres-schema-validation-0050

**Regra Canônica / Evidência:**
In the HWA laboratory, the PostgreSQL database TWS contains the HWA multi-schema structure: dwb (29 tables), evt (4), log (2), mdl (48), pln (13). Total 96 tables. The role twsuser exists and has usage privileges on these schemas. The role twsdbuser does not exist; the term twsuser is a PostgreSQL role, not a schema.

**Plataforma / Validação:** PostgreSQL 18.6 on WSL2 Ubuntu 22.04

---

### 1505. hwa-lab-10.2.8-postgresql-configuredb-0001

**Regra Canônica / Evidência:**
In the WSL2 laboratory, HWA 10.2.8 configureDb.sh completed successfully with PostgreSQL, component MDM, database TWS, local port 5432, and generated HWA schemas.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1506. hwa-lab-10.2.8-postinstall-limit-fence-check-0029

**Regra Canônica / Evidência:**
A mandatory HWA post-installation check must inspect workstation LIMIT, FENCE, link state and JobManager flag before diagnosing READY jobs. In the laboratory, MDMDA initially had LIMIT 0 and FENCE 0; raising LIMIT to 10 allowed priority-10 dynamic-agent jobs to execute.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1507. hwa-lab-10.2.8-priority-limit-validation-0043

**Regra Canônica / Evidência:**
In the HWA laboratory, PRIO_TEST with LIMIT 2 showed: priority 0 stayed HOLD (never launched), numeric priorities 10/20/50 ran SUCC, and HI/GO ran SUCC and could run despite LIMIT. This matches documented limit/priority behavior.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1508. hwa-lab-10.2.8-prompt-blocked-stream-0054

**Regra Canônica / Evidência:**
In the HWA laboratory, a job stream defined with PROMPT "Continue?" (inline text) was submitted and remained in HOLD with the dependent job also HOLD, confirming that a prompt blocks the stream until replied. The reply command requires a named prompt (1-8 bytes); an inline text prompt did not expose a reply name via conman reply.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1509. hwa-lab-10.2.8-recovery-rerun-0072

**Regra Canônica / Evidência:**
In the HWA laboratory, a job defined with RECOVERY RERUN in a job stream .def validated, added, and when the underlying command exited with rc 5 the job went ABEND and the scheduler automatically launched a recovery rerun ('>>rerun as J1'), which also ABEND (exit 5). This confirms automatic recovery rerun on job failure. The composer accepts 'RECOVERY RERUN' inline; the forms 'RECOVERY RERUN 2', 'RECOVERY RERUN SAME_WORKSTATION FOR 2 ATTEMPTS' were rejected at validate (AWSJOM915E/AWSJOM918E).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1510. hwa-lab-10.2.8-recovery-rerun-container-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, dominio MDM master), um job definido com RECOVERY RERUN (MDM#CPJ_ERR, DOCOMMAND 'echo CPLXERR_FAIL; exit 1') submetido via sbs no plano executou e ABEND rc1; o scheduler HCL disparou automaticamente o rerun de recuperacao ('>>rerun as CPJ_ERR ... [Recovery]') que tambem ABEND rc1. Confirma que o RECOVERY RERUN automatico sobre falha do job funciona no container (master MDM executa nativamente via JobManager). O stream (MDM#CPLXRERUN) terminou ABEND.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1511. hwa-lab-10.2.8-recovery-stop-continue-rerun-0038

**Regra Canônica / Evidência:**
In the HWA laboratory, RECOVTEST demonstrated recovery behavior: FAIL_STOP ended ABEND with return code 7; FAIL_CONT ended ABEND but used RECOVERY CONTINUE; FAIL_RERUN first ended ABEND and then reran after one minute, completing SUCC with return code 0 on the first retry.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1512. hwa-lab-10.2.8-resetplan-normal-0025

**Regra Canônica / Evidência:**
In the HWA laboratory, ResetPlan without -scratch archived the current Symphony, updated statistics and reset the production-plan information while preserving the preproduction plan; conman could not inspect jobs until a new Symphony was generated.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1513. hwa-lab-10.2.8-rest-api-0063

**Regra Canônica / Evidência:**
In the HWA laboratory, the JobManager REST endpoint (JobManagerRESTWeb/JobScheduler/job on port 31116) is reachable over HTTPS and issued an LtpaToken2 cookie after basic authentication, but returned fault AWSJMR011E ServiceUnavailable. The JobManagerGW has autostart=no (direct topology), so the JobManager REST service is not available for external job submission without the broker/gateway component.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1514. hwa-lab-10.2.8-rest-api-corpus-incorporation-0081

**Regra Canônica / Evidência:**
The HCL Workload Automation REST API V2 OpenAPI specification (WA_API3_v2.json, OpenAPI 3.1.0, spec version 2.1.6.0, 212 paths, security schemes JWT and Basic, servers at localhost:8080, 0.0.0.0:8080 and /) was captured from the live lab REST endpoint https://127.0.0.1:31116/twsd/WA_API3_v2.json (1,731,985 bytes) and incorporated into the training corpus. Two artifacts were added to data/raw: the raw WA_API3_v2.json (875 chunks) and a generated structured markdown WA_API3_v2_REST_API.md (304 chunks) documenting every endpoint/method, parameters, request body and responses. The extract_docs.py valid_extensions was extended to include .json, and infer_version maps the wa_api3_v2 document to version 10.2.8. After the curation pipeline (extract, dedup_and_split, audit, validate_tokens, simulate_dataset_quality), the corpus verdict is APROVADO COM RESSALVAS: unknown_version_share dropped from 0.0441 to 0.0106, 563 REST API chunks are in train_full, synthetic_in_training=0, security_hits empty, no token limit violations.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1515. hwa-lab-10.2.8-rest-api-v2-0071

**Regra Canônica / Evidência:**
In the HWA laboratory, the REST API V2 is active and functional on the MDM at https://MDMHOST:31116/twsd/ (NOT the JobManagerRESTWeb path). Swagger UI is served at /twsd/ and the OpenAPI 3.1.0 spec WA_API3_v2.json is retrievable with basic auth (wauser). GET /twsd/api/v2/model/jobdefinition returned 66 job definitions; GET /twsd/api/v2/model/jobstream returned 32 job streams; GET /twsd/api/v2/plan/job returned 81 plan jobs. The spec exposes model (jobdefinition/jobstream lock/unlock/bulk) and plan endpoints including /plan/job/action/{hold,kill,cancel,rerun,confirm-succ,confirm-abend,release} and /plan/job/submit. A POST submit of jobstream id returned AWSJDB101E 'object not found' because the payload used the model object id rather than a recognized submission identifier, confirming the endpoint accepts and validates requests against the database.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1516. hwa-lab-10.2.8-rest-api-v2-auth-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), a REST API V2 (engine https://localhost:31116/twsd/) foi validada de ponta a ponta com autenticacao basic auth de usuario TWS. DESCOBERTA CRITICA de auth: a senha do usuario (wauser) e validada pelo engine contra o campo interno user.twsuser.password (armazenado ENCRIPTADO {aes} em wauser_variables.xml, com a chave em passphrase_variables.xml wlp.password.encryption.key) - e NAO apenas contra a senha do SO. Mudar so a senha SO (chpasswd) mantem a REST em HTTP 401; e necessario: (1) reencriptar a nova senha com /opt/liberty/wlp/bin/securityUtility encode --encoding=aes --key=<chave-10dig> e atualizar user.twsuser.password nos wauser_variables.xml do engineServer (/opt/hwa/TWSDATA/usr/servers/engineServer/.../overrides/) e dwcServer (/opt/hwa/DWC/DWC_DATA/...), (2) reiniciar o engineServer (stopAppServer.sh/startAppServer.sh, AWSBHU622I), (3) entao basic auth funciona. Endpoints validados (GETs read-only com basic auth wauser): /twsd/api/v2/engine/info -> 200 {licenseType:PERSERVER, timezone America/Sao_Paulo}; /twsd/api/v2/plan/job/count -> 200 {count:13} (13 jobs no plano do dia vigente); /twsd/api/v2/plan/jobstream?limit=5 -> 200 com envelope {count,results} (jobstreams do plano, UUIDs, workstation /MDM, schedTime UTC + timeZone America/Sao_Paulo, jsStatusFlags carriedForward). Spec OpenAPI em /twsd/WA_API3_v2.json com 212 paths (plan/job, plan/jobstream, plan/job/action/*, model/*, engine/*). POST /twsd/api/v2/login retornou 401 (fluxo de login usa outro mecanismo); o acesso via basic auth direto nos recursos funciona.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), Liberty engineServer 31116

---

### 1517. hwa-lab-10.2.8-rest-api-v2-lifecycle-actions-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), o ciclo completo de operacao e gerenciamento de plano via REST API V2 (engine https://localhost:31116/twsd/api/v2) foi validado de ponta a ponta com autenticacao basic auth (wauser). Endpoints validados com sucesso (HTTP 200): (1) Consulta de definicoes do modelo: GET /twsd/api/v2/model/jobdefinition (retorna defs com task.other, userName, isCommand) e GET /twsd/api/v2/model/jobstream. (2) Submissao ad-hoc: POST /twsd/api/v2/plan/job/submit-ad-hoc-job com payload SubmitAdHocJobOptionsV2 (workstationKey /MDM, jobName, task.other) retornou HTTP 200 {'id': 'MDM;JOBS;...'}, instanciando o job na stream default JOBS em estado HOLD. (3) Alteracao dinamica de prioridade no plano: PUT /twsd/api/v2/plan/job/{job_id}/action/update-priority?priority=50 retornou HTTP 200, refletindo no conman sj como prioridade elevada (+10). (4) Liberacao no plano: PUT /twsd/api/v2/plan/job/{job_id}/action/release retornou HTTP 200, fazendo o job entrar imediatamente em EXEC e transitar para SUCC rc 0. (5) Consulta de Job Log real: GET /twsd/api/v2/plan/job/run/{run_id}/joblog retornou HTTP 200 com a saida completa do jobmanrc e JOBINFO (Exit Status: 0, Elapsed Time: 0:00:25). (6) Rerun de job via REST: PUT /twsd/api/v2/plan/job/run/{run_id}/action/rerun com header Content-Type: application/json e corpo {} retornou HTTP 200 (sem header retorna 415), gerando nova instancia '>>rerun step' (#J39010) que executou SUCC rc 0. (7) Comando de componente: PUT /twsd/api/v2/engine/run-component-command retornou HTTP 200 com payload estruturado AWSJCS027E demonstrando que componentId exige tipo AGENT (rejeita MANAGER).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), Liberty engineServer 31116

---

### 1518. hwa-lab-10.2.8-rest-v2-action-put-0078

**Regra Canônica / Evidência:**
In the HWA laboratory, the REST API V2 plan job action endpoints use PUT (not POST). The OpenAPI spec (WA_API3_v2.json, 1.73 MB) defines PUT /twsd/api/v2/plan/job/{job_id}/action/confirm-succ, /kill, /hold, /release, /rerun, /cancel, /confirm-abend, /release-dependencies, /update-priority, etc. A PUT to /plan/job/{job_id}/action/confirm-succ with the plan job UUID returned HTTP 500 with AWSJSY404E wrapping AWSBIN076E 'The operation cannot be performed. The job or the current instance of the job is in an incorrect state', because the target job ADHOC_AFTER_RESET was already in a terminal state. The endpoint recognized the job_id and executed the action handler (error is a valid state check, not a 404/405). The correct identifier is the plan job UUID (field 'id' from GET /plan/job, envelope {"count":N,"results":[...]}). POST (405) was the wrong method; PUT is correct.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1519. hwa-lab-10.2.8-rest-v2-port-31116-live-0077

**Regra Canônica / Evidência:**
In the HWA laboratory, the REST API V2 on port 31116 (/twsd) is fully functional. curl -v confirms TLS 1.3 connection with certificate CN=HWA-LAB issued by 'HWA Lab CA', and GET /twsd/ returns HTTP/1.1 200 OK serving an XSRF-TOKEN. Basic authentication with the wauser account is accepted (no login endpoint; /twsd/api/v2/login returns 404). Authenticated GET /twsd/api/v2/model/jobstream returns {"count":17,"results":[...]} (17 job streams), GET /twsd/api/v2/plan/job returns {"count":90,"results":[...]} (90 jobs), and GET /twsd/WA_API3_v2.json returns HTTP 200 with a 1,731,985-byte (1.73 MB) OpenAPI spec. The response envelope format is {"count":N,"results":[...]}. This confirms the REST API V2 endpoint (not the legacy /JobManagerRESTWeb/) is the live, authenticated interface on the master workstation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1520. hwa-lab-10.2.8-rest-v2-submit-action-200-0082

**Regra Canônica / Evidência:**
In the HWA laboratory, the REST API V2 full job lifecycle was validated end-to-end on the live /twsd:31116 endpoint. (1) POST /twsd/api/v2/plan/job/submit-ad-hoc-job with payload {"workstationKey":"/MDMDA","task":{"UNIX":{"taskString":"sleep 120","isCommand":"true","userName":"wauser"}}} returned HTTP 200 with {"id":"MDMDA;JOBS;SLEEP"}. The task is an object keyed by task type (UNIX) with taskString/isCommand/userName, NOT a raw JSDL string; the workstation is given as workstationKey (e.g. /MDMDA) not workstationId. (2) The returned id is a composite job key (MDMDA;JOBS;SLEEP), NOT the plan UUID; the plan job UUID is obtained from GET /plan/job (field 'id', e.g. 6d19eaf1-c9da-3799-96ed-131f07832a01 for the SLEEP job). (3) PUT /twsd/api/v2/plan/job/{uuid}/action/{hold,kill,confirm-succ} each returned HTTP 200 with the job id echoed. This closes follow-up P2c: actions use PUT + plan-job UUID; a clean non-error 200 was observed. Using the composite job key instead of the UUID caused AWSBIO006E 'Field SCHED-NAME has a null value'.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1521. hwa-lab-10.2.8-runbook-conclusion-0052

**Regra Canônica / Evidência:**
In the HWA laboratory, the runbook data/runbooks/hwa-10.2.8-wsl-lab.md now contains a Conclusion section summarizing validated outcomes, schema/role findings, wauser permissions, known gaps and a consolidated reference list.

**Plataforma / Validação:** WSL2 Ubuntu 22.04

---

### 1522. hwa-lab-10.2.8-serverinst-0002

**Regra Canônica / Evidência:**
In the WSL2 laboratory, HWA 10.2.8 serverinst.sh completed MDM installation in /opt/hwa after supplying Open Liberty, PostgreSQL, SSL certificate directory, a distinct workstation name and display name, and a pre-existing wauser account.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1523. hwa-lab-10.2.8-serverinst-full-success-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8 (UBI-init), o serverinst.sh HWA 10.2.8 completou a instalacao do MDM com PostgreSQL 18.6: WAINST023I success, servidores ativos (netman 31111/31113, JobManager 31114, EIF 31131, Liberty engineServer), JnextPlan -for 0000 carregou o Symphony (AWSJCL074I) e conman showcpus reportou Batchman LIVES para MDM com MDMXA x-agent - replicando o lab WSL2 em plataforma RHEL container.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1524. hwa-lab-10.2.8-serverinst-inst-dir-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8, serverinst.sh do HWA 10.2.8 rejeita instalacao com WAINST050E quando o INST_DIR (/opt/hwa) nao esta vazio; a pasta de certificados SSL (SSL_KEY_FOLDER) deve ficar FORA do INST_DIR.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1525. hwa-lab-10.2.8-serverinst-missing-cmp-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8 UBI (imagem ubi-init minimal), o twsinst aninhado do serverinst.sh HWA 10.2.8 falha com rc=127 (cmp: command not found) na fase de importacao de certificados; instalar diffutils resolve; o serverinst e rerunnable e retoma do passo falho.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1526. hwa-lab-10.2.8-serverinst-no-skip-twsinst-0001

**Regra Canônica / Evidência:**
O serverinst.sh HWA 10.2.8 nao possui caminho para pular o twsinst -new: apos uma instalacao fresh completa via twsinst direto, reexecutar o serverinst.sh (mesmo com SKIPCHECKEMPTYDIR=true) falha com AWSFAB022E (instalacao fresh com instancia previa em /opt/hwa/TWSDATA). Instalacao interrompida no meio nao e completavel pelo wrapper - recomecar do zero (apagar /opt/hwa e work_dir) com o serverinst.sh completo.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1527. hwa-lab-10.2.8-serverinst-wrapper-rerun-0001

**Regra Canônica / Evidência:**
Apos falha do twsinst interno (ex.: cmp ausente), reexecutar o wrapper serverinst.sh falha de novo com WAINST050E (INST_DIR nao vazio, pois a execucao parcial ja populou /opt/hwa); o AWSFAB057I 'script can be run again' refere-se ao twsinst interno, que deve ser invocado DIRETAMENTE com os parametros do log para retomar do passo falho.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1528. hwa-lab-10.2.8-sfinal-awsbhv082e-recovery-0001

**Regra Canônica / Evidência:**
No laboratório HWA 10.2.8 Distributed (container Docker tws-hwa), o job stream FINAL ancorado na workstation MDMXA (Extended Agent unixlocl) pode apresentar estado STUCK quando o job MAKEPLAN/SWITCHPLAN falha com AWSBHV082E (run number de Symnew idêntico ao Symphony anterior). O diagnóstico seguro exige validar a saúde do banco com 'optman ls', verificar consistência com 'planman showinfo' e NUNCA executar MakePlan manualmente. Se o plano já tiver sido estendido para a data corrente (Run == Confirm), a recuperação canônica é: (1) reiniciar o motor com 'conman start; mgr'; (2) reconciliar a instância residual com 'conman confirm MDMXA#FINAL(<sched_anterior>).SWITCHPLAN;succ'; (3) liberar o stream atual com 'conman release MDMXA#FINAL(<sched_atual>)', permitindo que STARTAPPSERVER, MAKEPLAN e SWITCHPLAN completem automaticamente com ReturnCode 0 no novo Run number.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

**Perguntas e Cenários Relacionados:**

- *Como recuperar o job stream FINAL em estado STUCK após erro AWSBHV082E no SwitchPlan sem rodar MakePlan na mão?*
- *Por que o conman sj MDM#FINAL.@ volta vazio se o stream FINAL está na workstation MDMXA?*
- *Qual o procedimento documentado para destravar a esteira FINALPOSTREPORTS quando o plano já foi estendido?*

---

### 1529. hwa-lab-10.2.8-sfinal-confrontation-0001

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, /opt/hwa/TWS/Sfinal e /opt/hwa/TWS/config/Sfinal são iguais, enquanto /opt/hwa/TWS/Sfinal2 difere na dependência do stream FINAL: Sfinal usa FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS e Sfinal2 usa a janela de dependência de MDMXA#FINALPOSTREPORTS.UPDATESTATS do ciclo anterior.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu

---

### 1530. hwa-lab-10.2.8-sfinal-confrontation-0002

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, os objetos FINAL e FINALPOSTREPORTS no banco correspondem à variante Sfinal, não à dependência alternativa de Sfinal2; o FINAL armazenado contém FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS e FINALPOSTREPORTS contém FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu

---

### 1531. hwa-lab-10.2.8-sfinal-confrontation-0003

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, o último FINAL executado concluiu STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, CHECKSYNC, CREATEPOSTREPORTS e UPDATESTATS com código 0; o MAKEPLAN registrou planman ext, AWSJCL062I, e o SWITCHPLAN registrou atualização do run number e término com Exit Status 0.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu

---

### 1532. hwa-lab-10.2.8-sfinal-definitions-removed-0001

**Regra Canônica / Evidência:**
No lab container RHEL 9.8, as definicoes de exemplo do Sfinal (MDMXA#FINAL e MDMXA#FINALPOSTREPORTS, importadas pelo instalador em 09/04) foram removidas do banco com composer delete (AWSJCL003I/AWSBIA290I), por decisao do dono do lab - o plano de producao ficou limpo (sem instancias) e o arquivo /opt/hwa/TWS/Sfinal foi preservado para reversao via composer add Sfinal.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1533. hwa-lab-10.2.8-sfinal-import-0006

**Regra Canônica / Evidência:**
In the WSL2 HWA 10.2.8 laboratory, the post-configuration process executed composer add Sfinal successfully and updated eight database objects: six jobs plus the FINAL and FINALPOSTREPORTS job streams on the MDMXA extended agent workstation.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1534. hwa-lab-10.2.8-sfinal-installed-by-installer-0001

**Regra Canônica / Evidência:**
No lab container RHEL 9.8, o instalador do MDM HWA 10.2.8 JA importa o Sfinal: os job streams MDMXA#FINAL e MDMXA#FINALPOSTREPORTS existem no banco (composer display retorna AWSBIA291I Total objects 1, atualizado 09/04/2026) sem composer add - replicando o achado WSL de que a ausencia de jobs apos JnextPlan -for 0000 e o horizonte zero, nao falta de importacao.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1535. hwa-lab-10.2.8-sfinal-plan-horizon-0007

**Regra Canônica / Evidência:**
In the WSL2 HWA 10.2.8 laboratory, JnextPlan -for 0000 created a zero-duration production plan with no job stream instances, while JnextPlan -for 2400 produced FINAL and FINALPOSTREPORTS instances with three jobs each at 23:59.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1536. hwa-lab-10.2.8-sft-audit-0075

**Regra Canônica / Evidência:**
Auditoria independente ADU (hwa-dataset-auditor, 2026-08-18) dos materiais HWA 10.2.8: 34 candidatos SFT (17 EN / 17 PT), 6 evidencias lab e 10 claims de matriz cross-version. Veredito: APROVADO COM RESSALVAS (apto experimental, nao producao imediata). Nenhum bloqueador de seguranca (senha lab 'padrao' ausente, '<REDACTED>' correto, version_scope integro), nenhum vazamento de versao. Achados: M1 (MAJOR) claim hwa-10.2.8-composer-if-conddep-0001 listava EXEC como condicao valida contradizendo a resposta SFT correta e a doc oficial (awsrgcondlogic.html: FAIL/ABEND/SUCC/SUPPR) — corrigido removendo EXEC da lista de status para jobs (EXEC permanece so em exemplos de join de job stream externa); M2 (MAJOR) candidatos de automacao citam evidencia que nao entalha a acao especifica (reapontar claims para allowlist/schema); M3 (MINOR) desequilibrio topico (automacao 30%); m1 qualificar EXEC na matriz; m2 resumecond claim insuficiente (uso apenas como recusa). RECOVERY RERUN sintaxe completa, onoverlap 39-dep (10.2.7+), TASK 4095, limit cpu/fence, onlate kill, REST V2 /twsd (10.1 FP1) confirmados em doc oficial 10.2.8.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1537. hwa-lab-10.2.8-sft-m2m3-rework-0087

**Regra Canônica / Evidência:**
The HWA 10.2.8 SFT candidate corpus was reworked to close the ADU audit findings M2 and M3. M2 (claim_ids not entailing): 12 ghost claim_ids referenced by candidates (hwa-10.2.8-composer-{join,if-conddep,outputcond,critical-0001,critical-0002,task,runcyclegroup-0001..0003,recovery,onlate,resumecond}-*) did not exist in data/evidence/claims.jsonl; they were repointed to verified claims (hwa-lab-10.2.8-syntax-resolved-0069, hwa-lab-10.2.8-composer-name-order-errors-0035, hwa-10.2.8-wsa-0009, hwa-lab-10.2.8-task-jsdl-validation-0012, hwa-lab-10.2.8-recovery-rerun-0072, hwa-lab-10.2.8-deadline-onlate-0056, hwa-10.2.8-gui-conddep-0001), removing 24 ghost references across 16 records; after the fix every cited claim_id exists in claims.jsonl. M3 (topic imbalance): 20 new bilingual candidates (10 EN + 10 PT) were generated exclusively from verified evidence covering previously under-represented topics: bmevents-config, edwa-rules, composer-order, conddep-status, limit-cpu, rest-submit, destructive-cancel, credential-submit, recusal-resumecond and version-awareness; each topic has exactly one EN+PT paraphrase pair. Final candidate corpus: 54 records (27 EN / 27 PT), risk read_only=42, mutating=4, destructive=4, credential_sensitive=4.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1538. hwa-lab-10.2.8-single-user-wauser-unification-0001

**Regra Canônica / Evidência:**
No padrao operacional e arquitetural do HWA 10.2.8, nao se criam multiplos usuarios de servico no SO para cada componente. Todos os componentes locais (TWS engine, netman, batchman, Liberty engineServer e Liberty dwcServer) sao unificados e vinculados exclusivamente ao usuario principal do produto no SO ('wauser'), mantendo a mesma credencial (usuario e senha) em todo o ecossistema. Apenas o SGBD (PostgreSQL) possui usuario e credencial proprios dedicados. No laboratorio container tws-hwa, o DWC foi reconfigurado para eliminar o usuario redundante 'dwcadmin': (1) O ownership de /opt/hwa/DWC e /opt/hwa/DWC/DWC_DATA foi atribuido a wauser:wauser; (2) /opt/hwa/DWC/appservertools/setEnv.sh foi ajustado para WA_USER=wauser; (3) /opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/configDropins/overrides/wauser_variables.xml foi atualizado com user.twsuser.id=wauser e a mesma senha encriptada {aes} do engine; (4) dwcServer foi iniciado com sucesso sob wauser (startAppServer.sh -direct) abrindo porta 9443 (HTTP 302 em /console/); (5) o usuario redundante dwcadmin foi removido do SO (userdel).

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1539. hwa-lab-10.2.8-startcond-filemonitor-0053

**Regra Canônica / Evidência:**
In the HWA laboratory, composer job streams using STARTCOND FILECREATED and FILEMODIFIED generated internal filemonitor jobs (filemonitorlauncher -event fileCreated -scanInterval N). The FILEMODIFIED variant triggered the dependent job, while the FILECREATED variant failed with AWSITA030E because the ${agent-config:bin-path} in the generated JSDL did not resolve to the actual filemonitorlauncher path (/opt/hwa/TWS/bin/filemonitorlauncher).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1540. hwa-lab-10.2.8-startofday-0005-0001

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, a opção global startOfDay foi alterada de 0000 para 0005 com optman chg sd=0005; o comando retornou AWSJCL050I Command chg completed successfully e optman ls confirmou startOfDay / sd = 0005.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu

---

### 1541. hwa-lab-10.2.8-startofday-0005-brt-anchor-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, America/Sao_Paulo), para o plano de producao nascer com o dia vigente iniciando as 00:05 BR e sempre D+1, o JnextPlan deve ser executado SEM o parametro -from (ou -from sem deslocar por timezone). Com optman sd=0005 e fuso America/Sao_Paulo, JnextPlan (sem -from) criou o plano com 'Plan creation start time: 09/05/2026 00:05 TZ America/Sao_Paulo' e 'Production plan end time: 09/06/2026 00:04'. O uso previo de 'JnextPlan -from 09/05/2026 0000' ancorava o inicio do dia de producao em 21:00 BR (heranca da meia-noite UTC do container original), deslocando o dia vigente 3h do calendario local; a doc (runbook WSL) adverte que -from sem timezone explicito pode ser deslocado na interpretacao. Aviso AWSJPL206W: timezones habilitados no banco mas o MDM nao inclui timezone - usa o do sistema.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1542. hwa-lab-10.2.8-startup-registration-recovery-0021

**Regra Canônica / Evidência:**
In the HWA laboratory, MDMDA logged four AWKRRP086E_DOMAIN_NOT_CREATED resource-registration errors during initial startup, followed by recurring AWSITA083I successful resource-information sends. After ShutDownLwa and StartUpLwa, JobManager restarted and AWSITA083I resumed without recurrence during the observation window.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1543. hwa-lab-10.2.8-submit-absolute-rejected-0024

**Regra Canônica / Evidência:**
In the HWA laboratory, sbd with at=absolute was rejected by conman with AWSBHU141E for submit docommand, while a numeric at value was accepted and created a time-held job. The absolute form must not be presented as a confirmed working immediate-submit syntax for this environment.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1544. hwa-lab-10.2.8-symphony-active-file-0159

**Regra Canônica / Evidência:**
planman showinfo on the master reports Plan last update 08/27/2026 15:10 and Run number 18, matching the Sinfonia mtime; the deploy at 18:13 wrote /opt/hwa/TWSDATA/Symphony (505376 bytes, same size as Sinfonia). DB plan and disk Symphony are therefore consistent: there was NO plan/database corruption.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1545. hwa-lab-10.2.8-syntax-resolved-0069

**Regra Canônica / Evidência:**
In the HWA laboratory, five composer syntax blockers were resolved by using the documented keyword placement: CRITICAL (keyword in the job statement with DEADLINE) validated/added and ran SUCC; TASK with XML JSDL (jsdl:jobDefinition/jsdl:executable) validated/added and ran SUCC; IF conditional requires the predecessor referenced as workstation#jobstream.jobname (FOLLOWS MDMDA#STREAM.JOB IF SUCC); JOIN uses a block 'JOIN n OF ... FOLLOWS <ws>#<stream>.<job> IF <cond> ... ENDJOIN'; runcyclegroup uses keyword 'runcyclegroup' (no $) with mandatory 'vartable' and 'on runcycle <name> "FREQ=..."' and closing 'end'. All ran SUCC.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1546. hwa-lab-10.2.8-task-jsdl-validation-0012

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, the initial TASK JSDL executable definition used for a dynamic-agent test was rejected by composer validate with AWSJCS029E XML definition incorrect; the four standard job definitions were not promoted as successful dynamic-agent executions.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1547. hwa-lab-10.2.8-thiscpu-displayname-scope-0008

**Regra Canônica / Evidência:**
In the HWA 10.2.8 laboratory, the nested twsinst invocation made by serverinst with -agent both rejected equal -thiscpu and -displayname values with AWSFAB164E. This is an observed constraint of that invocation; it is not evidence of a universal rule that the parameters must always differ.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1548. hwa-lab-10.2.8-timezone-sao-paulo-0001

**Regra Canônica / Evidência:**
No laboratorio container RHEL9 UBI9 (HWA 10.2.8, tws-hwa.lab), o timezone do SO foi alterado de UTC para America/Sao_Paulo via ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime + /etc/timezone, fazendo `date` passar de 'Sat Sep 5 03:13:08 UTC' para 'Sat Sep 5 00:13:08 -03'. Achado operacional: o dominio MDM roda como processos manuais nao-systemd (engineServer Java Liberty iniciado 04/09 22:06 UTC, netman ppid=1), orquestrados pelo agente ITA (unit tebctl-tws_cpa_agent_wauser.service) e pelo /opt/hwa/TWS/config/start_tws.sh, que condiciona o start do netman (conman 'start&link @!/@/@;noask') a existencia de arquivo Symphony (ausente no 10.2.8, plano no banco). Logo, trocar /etc/localtime nao efetiva timezone nos processos do MDM ja em memoria (engineServer Java mantem TZ de boot); so vale para processos novos; para valer 100% exige reiniciar o dominio.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1549. hwa-lab-10.2.8-tooling-0067

**Regra Canônica / Evidência:**
In the HWA laboratory, the composer/planman/conman tooling available included composer validate/add, planman showinfo/confirm, conman rerun/confirm/cancel/altpri. No separate audit, report, fbcount, dataextract, or workload-app export/import commands are exposed as standalone commands in this 10.2.8 installation; these capabilities are not directly invokable from the CLI tooling tested.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1550. hwa-lab-10.2.8-trilha3-edwa-failover-scope-constraints-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab, plano #22), a topologia atual tem um unico Master Domain Manager (MDM, tipo *UNIX MASTER) e agentes (MDMDA UNIX AGENT, MDMXA X-AGENT, broker MDM_DWB, pools LABPOOL/MASTERAGENTS); nao ha backup master domain manager nem fault-tolerant agent full-status configurado. Consequentemente, um teste empirico honesto de 'conman switchmgr' para failover MDM->BMDM nao pode ser executado neste ambiente: o comando exige um segundo engine (BMDM) elegivel que nao existe na topologia. O corpus/claims de failover (hwa-10.2.8-ha-switchmgr-0001, hwa-10.2.8-globalopts-enautomaticfailover-0001) permanecem validos como conhecimento oficial/documentado (evidence_tier official_primary), mas NAO devem ser rotulados 'lab_validated' sem um segundo engine.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

---

### 1551. hwa-lab-10.2.8-trilha3-edwa-failover-scope-constraints-0002

**Regra Canônica / Evidência:**
No container HWA 10.2.8 (tws-hwa.lab), o event processing engine esta ATIVO: o processo ssmagent.bin roda (pid ssmagent.bin -f /opt/hwa/TWSDATA/EDWA/ssm/config e -f /opt/hwa/TWSDATA/ssm/config) e a porta EIF SSL 31131 esta em LISTEN (globalopts: enEventDrivenWorkloadAutomation ed=YES, enEventProcessorHttpsProtocol eh=YES, eventProcessorEIFSSLPort ef=31131). Porem, o utilitario CLI 'evtdef' nao consegue concluir dumpdef/loaddef contra 127.0.0.1:31131: retorna AWSBEH023E/AWSBEH029E (unable to communicate / SSL connection fails) tanto sem -protocol quanto com -protocol https. Diagnostico: o cliente evtdef nao possui a truststore/certificado de cliente necessario para o handshake TLS com o event processor (que usa HTTPS). Logo, a manipulacao de definicoes de eventos via CLI (evtdef loaddef/dumpdef) esta bloqueada neste ambiente ate que a confianca TLS do cliente seja configurada, embora o event engine em si esteja operacional.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9

---

### 1552. hwa-lab-10.2.8-twsinst-aes-clean-each-rerun-0001

**Regra Canônica / Evidência:**
Cada rerun do twsinst HWA 10.2.8 que passa por runSecurityEncryption RECRIA key.p12/key.sth em <DATA_DIR>/TWSDATA/ssl/aes/; o rerun seguinte falha com 'A file named key.p12 already exists' - a limpeza do diretorio aes/ e prerequisito de CADA rerun, nao apenas do primeiro apos a falha original.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1553. hwa-lab-10.2.8-twsinst-flags-mutual-exclusion-0001

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 (twsinst LINUX_X86_64), foram validadas empiricamente no container as 4 regras críticas de consistência e exclusão mútua de flags: (1) Rejeição de -displayname iniciando com dígito (AWSFAB010E 'An incorrect value has been supplied for a parameter. The parameter must be as follows: -displayname <agent-name>'); (2) Rejeição de valores idênticos para -thiscpu e -displayname em instalação do tipo -agent both (AWSFAB164E 'The values specified for -thiscpu and -displayname cannot be the same'); (3) Exclusão mútua entre -sslkeysfolder e -wauser quando -jwt false (AWSFAB486E 'The parameter: -sslkeysfolder is mutually exclusive with the parameter: -wauser'); (4) Exigência mandatória de ao menos um método de segurança/credencial entre sslkeysfolder, wauser/wapassword ou apikey (AWSFAB502E 'Specify either the sslkeysfolder and sslpassword parameters, or the wauser and wapassword parameters, or apikey parameter').

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent)

---

### 1554. hwa-lab-10.2.8-twsinst-keystore-residue-0001

**Regra Canônica / Evidência:**
Reexecucao do twsinst HWA 10.2.8 apos falha parcial falha em runSecurityEncryption (AWSFAB474I) porque o keystore AES ja existe: 'Unable to create the PKCS#12 file ... A file named key.p12 already exists' - a ferramenta nao sobrescreve; remover os residuos key.p12/key.sth em <DATA_DIR>/TWSDATA/ssl/aes/ antes do rerun.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1555. hwa-lab-10.2.8-twsinst-libcrypt-0001

**Regra Canônica / Evidência:**
No RHEL 9, o comando makesec do HWA 10.2.8 falha na fase AWSFAB068I (Completing the installation) com rc=127: 'makesec: error while loading shared libraries: libcrypt.so.1: cannot open shared object file'. O RHEL 9 nativo tem libcrypt.so.2; o pacote libxcrypt-compat fornece libcrypt.so.1 exigida pelos binarios HWA.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1556. hwa-lab-10.2.8-variable-table-native-0046

**Regra Canônica / Evidência:**
In the HWA laboratory, variable table LABTAB was created with vartable/members/end syntax and variable VARMARK=LAB_VALUE_OK. A native UNIX docommand job using ${VARMARK} produced no substitution (VALUE_IS_), while the same job using ^VARMARK^ produced VALUE_IS_LAB_VALUE_OK.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1557. hwa-lab-10.2.8-vartable-caret-e2e-0106

**Regra Canônica / Evidência:**
No laboratório WSL2 HWA 10.2.8, a resolução de variáveis de VARIABLE TABLE em jobs nativos (FTA) foi validada de ponta a ponta: (1) vartable criada via composer com sintaxe 'VARTABLE <nome> / DESCRIPTION / MEMBERS / var "valor" / END' (validate+add AWSJCL003I); (2) o job stream que usa a tabela DEVE declarar 'VARTABLE <nome>' ANTES da cláusula 'ON RUNCYCLE' (colocar depois do runcycle causa AWSJOM915E 'unexpected token VARTABLE'); (3) a referência à variável no DOCOMMAND do job nativo usa a sintaxe caret '^var^' — com '^LAB_MSG^ at ^LAB_WS^' o job imprimiu 'HELLO_FROM_VARTABLE at MDMDA' no out.log (zip do JobManager), confirmando resolução; (4) IMPORTANTE: a sintaxe '%var%' NÃO resolve em job nativo FTA (o script.sh/out.log mantém '%LAB_MSG%' literal) — o formato %var% é usado para variáveis de dynamic agents/integrações, e o caret ^var^ é o formato clássico de variável/parm do produto; a doc awsrgparmdefn documenta 'docommand "ls ^MY_HOME^"' e o exemplo gljob2 com ^glpath^; (5) o job E2E MDMDA#EVTJS_VAR submetido via conman sbs rodou SUCC (exit 0) com EVTJOBB_VAR e o out.log capturado no zip do JobManager contém a variável resolvida.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1558. hwa-lab-10.2.8-vartable-resolution-and-missing-behavior-0001

**Regra Canônica / Evidência:**
No laboratorio container HWA 10.2.8 (tws-hwa.lab), a definicao de VARIABLE TABLE (VARTABLE), a atribuicao em job streams e o mecanismo de resolucao em tempo de submissao/execucao foram comprovados de ponta a ponta: (1) Sintaxe do composer: uma tabela de variaveis e definida como objeto standalone 'VARTABLE <nome> DESCRIPTION ... MEMBERS <var1> <valor1> ... END' (adicionada com AWSJCL003I). Nao se mistura a definicao da tabela com o schedule no mesmo arquivo sem separador de objeto (causa AWSJOM915E unexpected token SCHEDULE). (2) No job stream, a clausula 'VARTABLE <nome>' deve obrigatoriamente preceder a clausula 'ON RUNCYCLE' (ordem rigorosa de gramatica do composer). (3) Resolucao com caret (^VAR^): variaveis definidas na tabela sao substituidas no DOCOMMAND durante a expansao do JCL (comprovado: 'echo Var is ^LAB_MSG^ and port is ^LAB_PORT^' foi expandido para 'echo Var is MSG_VAL_CONTAINER_RHEL9 and port is 9090' no JCLFILE do jobmanrc e executado com SUCC rc 0, #J232316). (4) COMPORTAMENTO CRITICO DE VARIAVEL INEXISTENTE: quando um job nativo referencia uma variavel com caret que nao existe na VARTABLE vinculada (ex: ^VAR_QUE_NAO_EXISTE^), o scheduler NAO bloqueia o submit nem gera erro de sintaxe; em vez disso, o HWA preserva a string com caret literal no JCLFILE ('echo Var is ^VAR_QUE_NAO_EXISTE^') e executa o job normalmente (SUCC rc 0, #J232318) — o que significa que variaveis inexistentes passam silenciosamente para o script de execucao como strings literais em vez de causar abend de validacao.

**Plataforma / Validação:** Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init)

---

### 1559. hwa-lab-10.2.8-wauser-login-profile-env-0001

**Regra Canônica / Evidência:**
Em container RHEL 9.8 UBI, o login do usuario de instalacao (wauser) nao carregava o environment do HWA (conman: command not found) porque o useradd do UBI cria /home/<user>/.bash_profile, que MASCCARA o .profile - o source do tws_env.sh deve ir no .bash_profile (diferente do WSL2 Ubuntu, onde o useradd nao cria .bash_profile e o runbook usou .profile).

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd)

---

### 1560. hwa-lab-10.2.8-wauser-profile-0005

**Regra Canônica / Evidência:**
In the WSL2 HWA 10.2.8 laboratory, the installation user is wauser and its login profile sources /opt/hwa/TWS/tws_env.sh; a new login shell then exposes TWS_TISDIR, TISDIR, UNISONHOME, UNISONWORK, JAVA_HOME, PATH and LD_LIBRARY_PATH.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

---

### 1561. hwa-lab-10.2.8-wauser-sudo-0051

**Regra Canônica / Evidência:**
In the HWA laboratory, user wauser is NOT in sudoers; sudo -l -U wauser returns 'not allowed to run sudo'. Test scripts in /home/wauser/bin (fail_stop.sh, fail_continue.sh, rerun_once.sh, lab_ls.sh) run as wauser directly because they are owned by wauser:wauser with mode 755. No sudo is required for the HWA laboratory scripts.

**Plataforma / Validação:** WSL2 Ubuntu 22.04

---

### 1562. hwa-lab-9.4.0-switchplan-db-cpu-contention-0207

**Regra Canônica / Evidência:**
Contributing root cause reported by the DBA team: the TWS database server was under high CPU load during the incident window. This is consistent with DB-side lock contention blocking the planman confirm transaction and keeping SWITCHPLAN in EXEC for 10+ hours. Combined with enWorkloadServiceAssurance (wa) already NO, the operative failure chain was: DB server high CPU -> lock contention / slow transaction -> planman confirm hung -> SWITCHPLAN job stuck EXEC -> workstations not restarted (UNLINK).

**Plataforma / Validação:** Distributed

---

### 1563. hwa-lab-9.4.0-switchplan-db-lock-confirm-0201

**Regra Canônica / Evidência:**
Root cause chain of the hung switch: the plan switch had advanced to the planman confirm stage but the confirm could not commit because the plan database was locked; the FINAL/SWITCHPLAN wrapper remained in EXEC while the confirm was blocked. This is the documented IBM pattern of APAR IV89990 (PLANMAN CONFIRM HANGS), in which 'planman -timeout 3600 confirm' hangs and the Final SwitchPlan job keeps executing.

**Plataforma / Validação:** Distributed

---

### 1564. hwa-lab-9.4.0-switchplan-exec-hung-0200

**Regra Canônica / Evidência:**
On the IBM Workload Scheduler 9.4.0.6 production Master Domain Manager, the SWITCHPLAN job (final step of the daily plan switch, FINAL job stream) remained in EXEC for over 10 hours. Throughout the whole period all workstations appeared UNLINK while the current plan (conman sc) already showed today's date: the plan window had been extended but no workstation had received/restarted on the new Symphony run.

**Plataforma / Validação:** Distributed

---

### 1565. hwa-lab-9.4.0-switchplan-final-resolution-0206

**Regra Canônica / Evidência:**
Final resolution of the stale EXEC on 9.4.0.6: the hung OS process 'planman -timeout 3600 confirm' was still alive (found via ps -ef) while planman showinfo already reported Run number 6110 == Confirm run number 6110 - i.e. the confirm had committed and the process was a post-commit hang (APAR IV89990 signature). The process was killed (kill then kill -9); the SWITCHPLAN job then left EXEC and was reconciled with 'conman confirm <job>;succ' since the plan switch had effectively completed. No ResetPlan was required; planman showinfo remained 6110/6110.

**Plataforma / Validação:** Distributed

---

### 1566. hwa-lab-9.4.0-switchplan-iv89990-diagnostic-0204

**Regra Canônica / Evidência:**
Diagnostic rule confirmed in production 9.4.0.6: a SWITCHPLAN job stuck in EXEC with all workstations unlinked does NOT by itself indicate plan corruption. If planman showinfo shows Run number == Confirm run number, workstations are linked on the same run as the MDM and jobs dispatch/complete, the plan switch COMPLETED and the EXEC status is a stale wrapper artifact (APAR IV89990). Do NOT rerun SwitchPlan/Stageman (risk of AWSBHV082E same-run-number merge failure), do NOT start a second JnextPlan (risk of AWSJPL017E), and do NOT use ResetPlan -scratch as a routine response. Only if Confirm run number = Run number - 1 is the confirm genuinely uncommitted and the documented AWSJCL054E recovery applies (analyze messages.log, then rerun planman confirm and conman confirm).

**Plataforma / Validação:** Distributed

---

### 1567. hwa-lab-9.4.0-switchplan-lessons-0208

**Regra Canônica / Evidência:**
Operational lessons consolidated from the 2026-09-04 incident (9.4.0.6 EOL, Oracle): (1) A SWITCHPLAN job left in EXEC with the plan already confirmed (Run number == Confirm run number) does NOT block the next JnextPlan - the stale instance is archived with the old Symphony during stageman and the next FINAL/SWITCHPLAN starts as a new instance; AWSJPL017E is triggered by an unfinished planner operation, not by a job in EXEC. (2) conman kill is documented as ignored for jobs in EXEC - the recovery target is the hung OS process 'planman -timeout 3600 confirm' (APAR IV89990 signature); once the confirm has committed, killing that process frees the job, which is then reconciled with 'conman confirm <job>;succ'. (3) FINALPOSTREPORTS starts only after SWITCHPLAN completes successfully, so leaving the reconciled job in ABEND would suppress the post-processing chain. (4) Do NOT rerun SwitchPlan/Stageman (AWSBHV082E same-run-number merge risk), do NOT start a second JnextPlan (AWSJPL017E risk) and do NOT use ResetPlan -scratch as routine. (5) Operative failure chain of this incident: Oracle DB server high CPU -> lock contention -> planman confirm hung -> SWITCHPLAN EXEC for 10h -> workstations UNLINK.

**Plataforma / Validação:** Distributed

---

### 1568. hwa-lab-9.4.0-switchplan-recovery-start-unlock-0202

**Regra Canônica / Evidência:**
Recovery for the hung switch on 9.4.0.6: issuing conman start plus planman unlock on the MDM re-established the scheduling network - workstations linked again on the current plan run. No destructive plan operation was required: no ResetPlan, no second JnextPlan, no SwitchPlan rerun, no process kill.

**Plataforma / Validação:** Distributed

---

### 1569. hwa-lab-9.4.0-switchplan-validated-run6110-0203

**Regra Canônica / Evidência:**
Validation of the recovered switch on 9.4.0.6: planman showinfo reported Run number 6110 equal to Confirm run number 6110 (plan generated AND successfully confirmed); conman sc showed every workstation on the same run number 6110 as the MDM; a job rerun on a workstation completed SUCCESSFULLY, confirming end-to-end production health.

**Plataforma / Validação:** Distributed

---

### 1570. hwa-lab-9.4.0-switchplan-wsa-disabled-0205

**Regra Canônica / Evidência:**
On the incident MDM (IBM Workload Scheduler 9.4.0.6), the global option enWorkloadServiceAssurance (short name wa) was already disabled: optman ls / optman show wa reports wa=NO. No optman chg was executed during the recovery (only conman start and planman unlock), so the option was already NO when the SWITCHPLAN hang occurred. Consequence: the Workload Service Assurance rule-processing mechanism attributed to APAR IV89990 is ruled out as the hang mechanism in this instance, and the documented interim workaround (optman chg wa=NO) does not apply; the DB lock blocking planman confirm remains the active root cause.

**Plataforma / Validação:** Distributed

---

### 1571. hwa-master-domain-manager-registered-master-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O master domain manager é registrado no banco de dados do HCL Workload Automation com o nome de workstation 'master', conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O master domain manager é registrado no banco de dados do HCL Workload Automation com o nome de workstation 'master', conforme a documentação oficial?*

---

### 1572. hwa-official-10.2.8-fence-priority-0032

**Regra Canônica / Evidência:**
In HCL Workload Automation, `fence` prevents jobs whose priority is less than or equal to the fence from launching, regardless of the job-stream priority. Fence accepts 0 through 99, HI, GO or SYSTEM; SYSTEM sets the fence to zero.

**Plataforma / Validação:** Distributed

---

### 1573. hwa-official-10.2.8-jnextplan-noremove-0014

**Regra Canônica / Evidência:**
In HCL Workload Automation 10.2.8, JnextPlan -for 0000 removes successfully completed job-stream instances from the new production plan by default, while -for 0000 -noremove preserves them.

**Plataforma / Validação:** Distributed

---

### 1574. hwa-official-10.2.8-jnextplan-restart-0013

**Regra Canônica / Evidência:**
HCL Workload Automation 10.2.8 documents that every JnextPlan execution stops and restarts all workstations while moving from the old production plan to the new Symphony plan.

**Plataforma / Validação:** Distributed

---

### 1575. hwa-official-10.2.8-limit-fence-carryforward-0033

**Regra Canônica / Evidência:**
HCL Workload Automation documents that changes to workstation job limit and fence are carried forward during preproduction processing to the next day's production plan.

**Plataforma / Validação:** Distributed

---

### 1576. hwa-official-10.2.8-limit-zero-priority-0031

**Regra Canônica / Evidência:**
In HCL Workload Automation, `limit cpu` controls the number of concurrent jobs. With a workstation limit of 0, a READY job stream can launch only HI or GO jobs; setting the value to SYSTEM removes the limit for normal workstations, while SYSTEM has a special zero-limit behavior for extended agents.

**Plataforma / Validação:** Distributed

---

### 1577. hwa-official-composer-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, Composer create e extract são nomes alternativos para extrair definições de objetos do banco para um arquivo texto. Context: create... Extracts an object definition from the database and writes it in a text file. Synonym for the extract command.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1578. hwa-official-composer-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, composer validate verifica definições de objetos em arquivo e a opção ;syntax verifica erros de sintaxe sem aplicar o arquivo ao banco. Context: Performs the validation of the object definitions contained in a user file. ... syntax: Checks the file for syntax errors.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1579. hwa-official-composer-10.2.8-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, Composer lock adquire locks explícitos em objetos do banco e unlock normalmente requer o mesmo usuário e sessão, salvo autorização ou forced documentado. Context: With this command the user explicitly acquires locks of database objects.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 1580. hwa-official-message-10.2.8-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > message [message]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJPL017E indica que a criação do production plan foi bloqueada por uma ação anterior que não terminou com sucesso. Context: The production plan cannot be created because a previous action on the production plan did not complete successfully.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL017E no HWA e qual ação é recomendada?*

---

### 1581. hwa-official-message-10.2.8-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJPL704E indica que o planner não conseguiu estender o preproduction plan; tablespace e transaction logs são exemplos de causas de banco. Context: The planner is unable to extend the preproduction plan.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL704E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL704E no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL704E no HWA e qual ação é recomendada?*

---

### 1582. hwa-official-stageman-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, Stageman aceita -carryforward no, yes ou all; -log arquiva o plano antigo em TWS_home/schedlog, -nolog impede o arquivamento e o nome padrão usa o timestamp Myyyymmddhhtt. Context: -log Archives the old production plan in the directory TWS_home/schedlog... Myyyymmddhhtt.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, Stageman aceita -carryforward no, yes ou all; -log arquiva o plano antigo em TWS_home/schedlog, -nolog impede o arquivamento e o nome padrão usa o timestamp Myyyymmddhhtt?*

---

### 1583. hwa-official-tuning-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, a documentação oficial de tuning de replicação recomenda configurar com.ibm.tws.planner.monitor.subProcessors=10, filecachesize=40000 e cachesize=40000 em TWSConfig.properties; também documenta heap inicial 2048 e máximo 4096 para o application server do MDM. Context: com.ibm.tws.planner.monitor.subProcessors=10 ... filecachesize=40000 ... cachesize=40000.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, a documentação oficial de tuning de replicação recomenda configurar com?*

---

### 1584. hwa-operational-agent-naming-suffix-0009

**Regra Canônica / Evidência:**
As an operational naming convention, a dynamic agent installed on the same host as a base workstation can reuse the base name with an incremental suffix, such as MDM and MDM_1, provided the resulting workstation name is unique in the HCL Workload Automation network.

**Plataforma / Validação:** Distributed

---

### 1585. hwa-operational-jnextplan-caution-0015

**Regra Canônica / Evidência:**
In production, JnextPlan must be treated as a controlled plan-transition operation: inspect active and incomplete instances, verify carry-forward settings, avoid concurrent plan generation, capture logs, and compare the old and new plan before allowing normal processing.

**Plataforma / Validação:** Distributed

---

### 1586. hwa-operational-limit-zero-not-unlimited-0030

**Regra Canônica / Evidência:**
In HCL Workload Automation, workstation LIMIT 0 is not equivalent to unlimited execution: from a READY job stream it allows only jobs with HI or GO priority values to launch; the SYSTEM value represents no concurrency limit.

**Plataforma / Validação:** Distributed

---

### 1587. hwa-themaster-estados-internos-de-job-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
Os estados internos de job documentados no HCL Workload Automation incluem ABEND, ABENP, ADD, CANCL, DONE, ERROR, EXEC, EXTRN, FAIL, FENCE, HOLD, INTRO, PEND, READY, SCHED, SUCC, SUCCP, SUPPR e WAIT, conforme a documentação oficial do formato padrão do comando showjobs.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os estados internos de job documentados no HCL Workload Automation incluem ABEND, ABENP, ADD, CANCL, DONE, ERROR, EXEC, EXTRN, FAIL, FENCE, HOLD, INTRO, PEND, READY, SCHED, SUCC, SUCCP, SUPPR e WAIT, conforme a documentação oficial do formato padrão do comando showjobs?*

---

### 1588. hwa-themaster-final-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
Os job streams FINAL e FINALPOSTREPORTS são job streams de exemplo incluídos no arquivo Sfinal que automatizam o gerenciamento do plano de produção no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os job streams FINAL e FINALPOSTREPORTS são job streams de exemplo incluídos no arquivo Sfinal que automatizam o gerenciamento do plano de produção no HCL Workload Automation, conforme a documentação oficial?*

---

### 1589. hwa-themaster-final-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation descreve os job streams FINAL e FINALPOSTREPORTS como 'sample job streams' (job streams de exemplo) e 'optional FINAL job stream' que automatizam o gerenciamento do plano, e não os rotula explicitamente como 'system jobs', conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation descreve os job streams FINAL e FINALPOSTREPORTS como 'sample job streams' (job streams de exemplo) e 'optional FINAL job stream' que automatizam o gerenciamento do plano, e não os rotula explicitamente como 'system jobs', conforme a documentação oficial?*

---

### 1590. hwa-themaster-final-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
The FINAL and FINALPOSTREPORTS job streams are associated with the master domain manager configuration and the Sfinal file is located in TWS_home/config. The documentation does not explicitly state these streams run exclusively on the MDM workstation, but their Sfinal path and configuration steps (composer add Sfinal, JnextPlan) are documented in the MDM configuration section.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar mdm?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 1591. hwa-themaster-finalpostreports-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O job stream FINALPOSTREPORTS segue o job stream FINAL e inicia somente quando o último job listado no FINAL (SWITCHPLAN) é concluído com sucesso no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O job stream FINALPOSTREPORTS segue o job stream FINAL e inicia somente quando o último job listado no FINAL (SWITCHPLAN) é concluído com sucesso no HCL Workload Automation, conforme a documentação oficial?*

---

### 1592. hwa-themaster-finalpostreports-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O job stream FINALPOSTREPORTS é responsável por imprimir os relatórios pós-produção no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O job stream FINALPOSTREPORTS é responsável por imprimir os relatórios pós-produção no HCL Workload Automation, conforme a documentação oficial?*

---

### 1593. hwa-themaster-home-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O arquivo Sfinal, que contém as definições dos job streams FINAL e FINALPOSTREPORTS, é criado no diretório TWS_home do master domain manager e é adicionado ao banco de dados ao configurar o master domain manager no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O arquivo Sfinal, que contém as definições dos job streams FINAL e FINALPOSTREPORTS, é criado no diretório TWS_home do master domain manager e é adicionado ao banco de dados ao configurar o master domain manager no HCL Workload Automation, conforme a documentação oficial?*

---

### 1594. hwa-themaster-job-stream-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
The official HCL Workload Automation 10.2.8 documentation does not document a job stream named "THEMASTER". The documented internal job streams are FINAL and FINALPOSTREPORTS (defined in the Sfinal file) which automate plan management (plan extension, postproduction reports).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: The official HCL Workload Automation 10.2.8 documentation does not document a job stream named "THEMASTER"?*

---

### 1595. hwa-themaster-switchplan-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
SWITCHPLAN é documentado como o último job do job stream FINAL no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: SWITCHPLAN é documentado como o último job do job stream FINAL no HCL Workload Automation, conforme a documentação oficial?*

---

### 1596. hwa-version-matrix-certman-distributed-only-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, Certman fica em TWS_INST_DIR/TWS/bin e nao e suportado em sistemas operacionais IBM i; e uma ferramenta do produto Distributed.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, Certman fica em TWS_INST_DIR/TWS/bin e nao e suportado em sistemas operacionais IBM i; e uma ferramenta do produto Distributed?*

---

### 1597. hwa-version-matrix-certman-intro-10.2.3-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, a ferramenta Certman foi introduzida na versao 10.2.3 para gerenciar certificados; a partir dessa versao os certificados passaram a ser gerenciados pelo comando certman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed, a ferramenta Certman foi introduzida na versao 10.2.3 para gerenciar certificados; a partir dessa versao os certificados passaram a ser gerenciados pelo comando certman?*

---

### 1598. hwa-version-matrix-certman-not-before-1023-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.1; 10.2.0-10.2.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, antes da versao 10.2.3 os certificados eram gerados na instalacao pelo comando serverinst; o comando certman nao existia nessas versoes anteriores (9.5, 10.1, 10.2.0-10.2.2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário serverinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no serverinst para gerenciar cert?*

---

### 1599. hwa-version-matrix-certman-not-zos-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation for Z 10.2.5-10.2.8 (z/OS) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: security > cert [cert]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation for Z (z/OS), os certificados SSL sao gerenciados via RACF KEYRING ou keystore criado em UNIX System Services (USS), e nao pela ferramenta Certman do produto Distributed.

**Plataforma / Validação:** z/OS

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation for Z (z/OS), os certificados SSL sao gerenciados via RACF KEYRING ou keystore criado em UNIX System Services (USS), e nao pela ferramenta Certman do produto Distributed?*

---

### 1600. hwa-version-matrix-composer-rest-9.5fp2-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 Fix Pack 2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 9.5 Fix Pack 2 Distributed, o composer passou a usar REST APIs para criar definicoes de objetos (calendar, domain, prompt, resource, variable table, variable/parameter, Windows user, workstation, workstation class); um composer 9.5 FP2 nao pode criar definicoes em um master domain manager com versao anterior.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Qual endpoint REST API V2 é utilizado para composer no HWA?*

---

### 1601. hwa-version-matrix-ocli-intro-10.1-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, o Orchestration CLI (OCLI) foi introduzido na versao 10.1 Fix Pack 1 como a interface de linha de comando para executar jobs/job streams no plano e interagir com o servidor; nao existe documentacao oficial de OCLI para a versao 9.5.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed, o Orchestration CLI (OCLI) foi introduzido na versao 10.1 Fix Pack 1 como a interface de linha de comando para executar jobs/job streams no plano e interagir com o servidor; nao existe documentacao oficial de OCLI para a versao 9.5.?*

---

### 1602. hwa-version-matrix-ocli-model-intro-10.2.2-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.2 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.2 Distributed, o Orchestration CLI passou a suportar tres familias de comandos: context commands (list, new, remove, set, switch), model commands (add, delete, display, extract, list, listfolder, lock, mkfolder, modify, new, rename, renamefolder, replace, rmfolder, unlock) e plan commands; esta e a versao em que os comandos model foram introduzidos.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.2 Distributed, o Orchestration CLI passou a suportar tres familias de comandos: context commands (list, new, remove, set, switch), model commands (add, delete, display, extract, list, listfolder, lock, mkfolder, modify, new, rename, renamefolder, replace, rmfolder, unlock) e plan commands; esta e a versao em que os comandos model foram introduzidos?*

---

### 1603. hwa-version-matrix-ocli-model-newitems-10.2.3-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.3 Distributed, os comandos model do Orchestration CLI passaram a suportar novos itens de agendamento, ampliando o escopo de definicoes gerenciadas via ocli model.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.3 Distributed, os comandos model do Orchestration CLI passaram a suportar novos itens de agendamento, ampliando o escopo de definicoes gerenciadas via ocli model?*

---

### 1604. hwa-version-matrix-ocli-plan-growth-10.2.1-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.1 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.1 Distributed, o Orchestration CLI ampliou o conjunto de comandos plan adicionando altrpri (alterar prioridade), fence (definir prioridade de workstation) e limit cpu (limitar jobs simultaneos); ainda sem comandos model.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.1 Distributed, o Orchestration CLI ampliou o conjunto de comandos plan adicionando altrpri (alterar prioridade), fence (definir prioridade de workstation) e limit cpu (limitar jobs simultaneos); ainda sem comandos model?*

---

### 1605. hwa-version-matrix-ocli-plan-only-10.1-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1; 10.2.0 (Distributed; Orchestration CLI) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.1 e 10.2.0 Distributed, o Orchestration CLI suportava apenas comandos plan (adddep job/sched, altjob, cancel job/sched, confirm, deldep job/sched, kill, limit sched, listfolder, release job/sched, rerun, showcpu, showjobs, showschedules, submit docommand/job/sched); comandos model nao existiam nessas versoes.

**Plataforma / Validação:** Distributed; Orchestration CLI

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.1 e 10.2.0 Distributed, o Orchestration CLI suportava apenas comandos plan (adddep job/sched, altjob, cancel job/sched, confirm, deldep job/sched, kill, limit sched, listfolder, release job/sched, rerun, showcpu, showjobs, showschedules, submit docommand/job/sched); comandos model nao existiam nessas versoes?*

---

### 1606. hwa-version-matrix-ocli-zos-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1-10.2.8 (z/OS (HCL Workload Automation for Z)) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: cli_planning > ocli [ocli]]`

**Regra Canônica / Evidência:**
Orchestration CLI (OCLI) in HCL Workload Automation 10.2.8 connects to a "remote engine" via config.yaml (host, port defaults to 31116, protocol, jwt). The documentation does not specify z/OS engines; the remote engine is described generically. For HCL Workload Automation for Z, the native interface is WAPL/EQQ. OCLI connection to z/OS engines is not confirmed in the official 10.2.8 distributed documentation.

**Plataforma / Validação:** z/OS (HCL Workload Automation for Z)

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wapl no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wapl para gerenciar ocli?*
- *Como utilizar a Workload Automation Programming Language WAPL para z/OS?*

---

### 1607. hwa-version-matrix-oql-distributed-zos-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3-10.2.8 (Distributed e z/OS) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: observability > monitor [monitor]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation, o OQL aplica-se tanto ao ambiente Distributed quanto ao z/OS, permitindo monitorar o production plan de ambos; para z/OS, o plano corrente e espelhado em banco via componente Federator (instalado com o Dynamic Workload Console a partir da versao 10.2.3).

**Plataforma / Validação:** Distributed e z/OS

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation, o OQL aplica-se tanto ao ambiente Distributed quanto ao z/OS, permitindo monitorar o production plan de ambos; para z/OS, o plano corrente e espelhado em banco via componente Federator (instalado com o Dynamic Workload Console a partir da versao 10.2.3)?*

---

### 1608. iwa-10.2.5-composer-job-selector-0020

**Escopo & Contexto:** `[Escopo: IBM Workload Automation 10.2.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No IBM Workload Automation 10.2.5, os seletores documentados de definições de job nos comandos composer (display e extract) usam o formato [[folder/]workstation#][folder/]jobname: apenas o nome do job (workstation padrão = aquela em que o composer executa; pasta padrão '/'), workstation#job (ex.: CPU1#MYJOB) e formas qualificadas por pasta (ex.: CPU1#/SAPJOBS/MYJOB ou PROD/CPU1#/BATCH/MYJOB). Caracteres curinga são permitidos em workstation, pasta e nome do job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---
