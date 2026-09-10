# ARQUITETURA & TOPOLOGIA MESH

> Total de tópicos canônicos cobertos nesta seção: 89

---

### 1. hwa-10.2-perfreport-benchmark-jobs-per-min-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 FP0 (Distributed test environments) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O relatório de performance 10.2 reporta que, para workloads de até 1400 jobs/min, o atraso médio de agendamento em dynamic agents foi de 30-40 segundos (igual a versões anteriores); em picos de ~5000 jobs/min houve aumento em determinados ambientes.

**Plataforma / Validação:** Distributed test environments

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: O relatório de performance 10.2 reporta que, para workloads de até 1400 jobs/min, o atraso médio de agendamento em dynamic agents foi de 30-40 segundos (igual a versões anteriores); em picos de ~5000 jobs/min houve aumento em determinados ambientes?*

---

### 2. hwa-10.2-resetfta-xagent-safety-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.0, resetFTA tem como alvo um FTA com Symphony corrompido; um SAP Extended Agent é uma workstation lógica hospedada por FTA, e a substituição de Symphony pode perder estado de fila e rerun de jobs afetados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 3. hwa-10.2.6-centralized-agent-update-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.6 (Distributed; Windows e UNIX; requer master domain manager distribuído) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Na atualização centralizada de múltiplos Fault-tolerant Agents e Dynamic Agents, jobs já em execução continuam; nenhum novo job inicia durante a manutenção; após a atualização, o agente reinicia e se reconecta aos seus jobs.

**Plataforma / Validação:** Distributed; Windows e UNIX; requer master domain manager distribuído

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 4. hwa-10.2.8-agent-dynamic-broker-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed agents) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Na instalação de agente dinâmico HWA 10.2.8, agent dynamic exige tdwbhostname e tdwbport; em instalação nova, a documentação indica 31116 como valor de tdwbport para conexão HTTPS do broker, sujeito à configuração do ambiente.

**Plataforma / Validação:** Distributed agents

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: Na instalação de agente dinâmico HWA 10.2.8, agent dynamic exige tdwbhostname e tdwbport; em instalação nova, a documentação indica 31116 como valor de tdwbport para conexão HTTPS do broker, sujeito à configuração do ambiente?*

---

### 5. hwa-10.2.8-capacity-fault-tolerant-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A documentação de performance do HCL Workload Automation 10.2.8 afirma que o desempenho de domain managers UNIX é impactado se sobrecarregados com jobs e que, para lidar com grande número de fault-tolerant agents, é possível melhorar o desempenho ajustando parâmetros de kernel; fornece um exemplo de parâmetros Linux para uma carga de 500000 jobs por dia, incluindo open files=105000 e max user processes=16384.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 6. hwa-10.2.8-capacity-fta-engines-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: agents > fta [fta]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não documenta uma opção localopts/useropts chamada 'Number of FTA engines'.

**Plataforma / Validação:** Distributed

---

### 7. hwa-10.2.8-capacity-workstation-limit-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A opção global workstationLimit (wl) no HCL Workload Automation 10.2.8 especifica o valor de limite de workstation que um dynamic agent assume após ser adicionado ao plano, com valores válidos de 0 a 1024 e padrão 100, efetivo imediatamente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: A opção global workstationLimit (wl) no HCL Workload Automation 10.2.8 especifica o valor de limite de workstation que um dynamic agent assume após ser adicionado ao plano, com valores válidos de 0 a 1024 e padrão 100, efetivo imediatamente?*
- *Qual o propósito e valor padrão da opção global workstationLimit no optman do HWA?*

---

### 8. hwa-10.2.8-composer-jsdl-validation-0119

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, definicoes de job com TASK JSDL (JSON) para dynamic agents sao validadas pelo schema no composer add/validate. Exemplos com formato incorreto sao rejeitados com AWSJCS029E XML definition incorrect. O schema espera executable.interactive, executable.suffix, executable.script, credential. Exemplo valido: TASK { executable: { interactive: false, suffix: , script: ls, credential: {} } } RECOVERY STOP END.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCS029E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCS029E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*

---

### 9. hwa-10.2.8-composer-parm-caret-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, variáveis referenciadas em definições de job usam a sintaxe caret (^var^), por exemplo docommand "ls ^MY_HOME^"; ^var^ é resolvido quando o plano é gerado ou estendido, e ${var} é resolvido/sobrescrito quando o job ou job stream é submetido (formato de integrações com dynamic agents); o formato %var% NÃO é a forma documentada de referência a variável/parm (não aparece na referência oficial).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para composer?*

---

### 10. hwa-10.2.8-composer-task-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, os valores validos documentados para o argumento tasktype na definicao de job via composer sao UNIX, WINDOWS, OTHER e BROKER.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para composer?*

---

### 11. hwa-10.2.8-conman-command-inventory-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O índice oficial HCL 10.2.8 enumera comandos Conman, suas formas curtas e os tipos de workstation suportados; kill/k interrompe job em execução, showjobs/sj exibe jobs e resetFTA recupera Symphony corrompido em FTA especificado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 12. hwa-10.2.8-conman-start-restriction-0113

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando `conman start` inicia os processos de producao do HWA (exceto event monitoring engine e Liberty), mas possui restricoes: (1) nao deve ser executado enquanto JnextPlan ou stageman estiverem rodando; (2) exige acesso 'start' a workstation; (3) 'This command is not supported on remote engine workstations' -- workstations do tipo agente, broker ou pool remoto nao aceitam `start`. Em workstations agente, o erro retornado e 'the workstation is agent, where the command is not supported'. Agentes devem ser iniciados localmente com ./StartUpLwa.sh (Unix) ou startuplwa (Windows).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para conman?*
- *Como utilizar o comando conman 'start' para gerenciar workstations e execução no HWA?*

---

### 13. hwa-10.2.8-conman-start-unified-0123

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o comando conman start inicia os processos de producao de uma workstation, com sintaxe 'start [domain!]workstation[;mgr][;noask]'. Restricoes IMPORTANTES: (1) funciona APENAS em master domain manager e fault-tolerant agents; NAO funciona em workstations do tipo remote engine (agent, broker, pool) - o erro retornado e 'the workstation is agent, where the command is not supported'; (2) nao deve ser executado enquanto JnextPlan ou stageman estiver rodando; (3) exige acesso 'start' a workstation; (4) para iniciar agentes/brokers/pools use o script local ./StartUpLwa.sh (Unix) ou startuplwa (Windows).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para conman?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 14. hwa-10.2.8-dynagent-broker-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O Dynamic Workload Broker (workstation broker) no HCL Workload Automation 10.2.8 funciona como uma ponte entre o mecanismo de agendamento e o pool de recursos, associando dinamicamente o workload submetido aos melhores recursos disponíveis em tempo de execução e submetendo cada job ao recurso que melhor atende aos requisitos, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 15. hwa-10.2.8-dynagent-broker-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O servidor do Dynamic Workload Broker no HCL Workload Automation 10.2.8 é instalado juntamente com o master domain manager e o dynamic domain manager e suas workstations de backup, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: O servidor do Dynamic Workload Broker no HCL Workload Automation 10.2.8 é instalado juntamente com o master domain manager e o dynamic domain manager e suas workstations de backup, conforme documentação oficial?*

---

### 16. hwa-10.2.8-dynagent-database-job-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O dynamic agent no HCL Workload Automation 10.2.8 executa database jobs com opções avançadas, que realizam consultas, comandos SQL e jobs sobre bancos de dados incluindo bancos customizados, além de permitir criar e executar stored procedures em bancos DB2, Oracle e MSSQL, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 executa database jobs com opções avançadas, que realizam consultas, comandos SQL e jobs sobre bancos de dados incluindo bancos customizados, além de permitir criar e executar stored procedures em bancos DB2, Oracle e MSSQL, conforme documentação oficial?*

---

### 17. hwa-10.2.8-dynagent-database-job-executor-properties-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A configuração dos database jobs (JDBC) no dynamic agent do HCL Workload Automation 10.2.8 é feita pelo arquivo DatabaseJobExecutor.properties, presente em TWA_home/TWS/JavaExt/cfg, usando a palavra-chave jdbcDriversPath para apontar para o diretório dos drivers JDBC, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: A configuração dos database jobs (JDBC) no dynamic agent do HCL Workload Automation 10.2.8 é feita pelo arquivo DatabaseJobExecutor?*

---

### 18. hwa-10.2.8-dynagent-en-add-workstation-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Com a opção global enAddWorkstation definida como 'yes' no HCL Workload Automation 10.2.8, a definição de workstation do dynamic agent é adicionada automaticamente ao Plano após o processo de instalação criar a workstation no banco de dados, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: Com a opção global enAddWorkstation definida como 'yes' no HCL Workload Automation 10.2.8, a definição de workstation do dynamic agent é adicionada automaticamente ao Plano após o processo de instalação criar a workstation no banco de dados, conforme documentação oficial?*

---

### 19. hwa-10.2.8-dynagent-file-transfer-jobs-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Os job types com opções avançados disponíveis no HCL Workload Automation 10.2.8 incluem file transfer jobs, web services jobs, database jobs, executable jobs, Java jobs, MSSQL jobs, access method jobs (Oracle E-Business Suite, PeopleSoft, SAP, MVS e métodos customizados), J2EE jobs, IBM i jobs, provisioning e remote command, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os job types com opções avançados disponíveis no HCL Workload Automation 10.2.8 incluem file transfer jobs, web services jobs, database jobs, executable jobs, Java jobs, MSSQL jobs, access method jobs (Oracle E-Business Suite, PeopleSoft, SAP, MVS e métodos customizados), J2EE jobs, IBM i jobs, provisioning e remote command, conforme documentação oficial?*

---

### 20. hwa-10.2.8-dynagent-gateway-local-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O dynamic agent no HCL Workload Automation 10.2.8 pode conectar-se diretamente ao master domain manager ou por meio de um dynamic domain manager; em topologias onde o master/DDM não pode comunicar-se diretamente com o agent, pode-se configurar o dynamic agent para usar um gateway local ou remoto, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 pode conectar-se diretamente ao master domain manager ou por meio de um dynamic domain manager; em topologias onde o master/DDM não pode comunicar-se diretamente com o agent, pode-se configurar o dynamic agent para usar um gateway local ou remoto, conforme documentação oficial?*

---

### 21. hwa-10.2.8-dynagent-ita-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A seção [ITA] do JobManager.ini no HCL Workload Automation 10.2.8 configura propriedades gerais do agente, incluindo ActionPollers, http_proxy e DebugDir, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A seção [ITA] do JobManager?*

---

### 22. hwa-10.2.8-dynagent-job-manager-ini-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O arquivo JobManager.ini do dynamic agent no HCL Workload Automation 10.2.8 é composto por muitas seções, cada uma com nome entre colchetes e contendo uma sequência de declarações variavel=valor, das quais apenas um subconjunto de parâmetros é documentado por serem reservados para uso interno, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 23. hwa-10.2.8-dynagent-job-manager-ini-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
The [JobExecutor], [ServiceLocator] and [Database] sections of JobManager.ini are not listed among the documented configurable sections in HCL Workload Automation 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: The [JobExecutor], [ServiceLocator] and [Database] sections of JobManager?*

---

### 24. hwa-10.2.8-dynagent-job-types-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O dynamic agent no HCL Workload Automation 10.2.8 gerencia uma ampla variedade de job types, como jobs específicos de banco de dados ou FTP, além dos job types existentes, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 gerencia uma ampla variedade de job types, como jobs específicos de banco de dados ou FTP, além dos job types existentes, conforme documentação oficial?*

---

### 25. hwa-10.2.8-dynagent-job-types-com-opes-avanadas-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Os job types com opções avançadas, tanto os fornecidos com o produto quanto os implementados por plug-ins customizados, no HCL Workload Automation 10.2.8 são executados apenas em dynamic agents, pools e dynamic pools, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 26. hwa-10.2.8-dynagent-mssql-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Para database jobs do tipo MSSQL, o dynamic agent no HCL Workload Automation 10.2.8 exige o uso da versão 4 dos drivers JDBC, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: Para database jobs do tipo MSSQL, o dynamic agent no HCL Workload Automation 10.2.8 exige o uso da versão 4 dos drivers JDBC, conforme documentação oficial?*

---

### 27. hwa-10.2.8-dynagent-pool-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Um dynamic pool no HCL Workload Automation 10.2.8 é uma workstation lógica que agrupa um conjunto de agents, definida dinamicamente com base nos requisitos de recurso especificados pelo usuário, mapeando todos os agents que atendem aos requisitos, sendo hospedada pela workstation broker e registrada no banco de dados como 'd-pool', conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 28. hwa-10.2.8-dynagent-pool-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o dynamic pool é atualizado dinamicamente sempre que um novo agent adequado fica disponível e jobs agendados nesta workstation herdam automaticamente os requisitos definidos para ela, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 29. hwa-10.2.8-dynagent-pool-rebalance-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o produto balanceia os jobs entre os agents dentro de um pool e reatribui automaticamente jobs a agents disponíveis se um agent deixar de estar disponível, conforme documentação oficial.

**Plataforma / Validação:** Distributed

---

### 30. hwa-10.2.8-dynagent-postgre-sql-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
PostgreSQL is not documented in the official 10.2.8 documentation as an explicitly supported database job type for the dynamic agent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: PostgreSQL is not documented in the official 10.2.8 documentation as an explicitly supported database job type for the dynamic agent?*

---

### 31. hwa-10.2.8-dynagent-servidor-do-broker-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Durante a troca do master domain manager ou dynamic domain manager no HCL Workload Automation 10.2.8, apenas um servidor do Dynamic Workload Broker fica ativo por vez, pois o servidor antigo para os serviços de agendamento dinâmico e o novo servidor inicia uma nova instância do broker após concluir a troca, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: Durante a troca do master domain manager ou dynamic domain manager no HCL Workload Automation 10.2.8, apenas um servidor do Dynamic Workload Broker fica ativo por vez, pois o servidor antigo para os serviços de agendamento dinâmico e o novo servidor inicia uma nova instância do broker após concluir a troca, conforme documentação oficial?*

---

### 32. hwa-10.2.8-dynagent-workstation-broker-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Um pool no HCL Workload Automation 10.2.8 é uma workstation lógica que agrupa um conjunto de agents com características similares de hardware ou software, à qual jobs são submetidos, sendo registrada no banco de dados como 'pool' e hospedada pela workstation broker, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 33. hwa-10.2.8-incident-awsdec002-e-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
A mensagem AWSDEC002E no HCL Workload Automation 10.2.8 indica um erro interno ('An internal error has occurred. The following UNIX system error occurred on an events file: "9" at line = 2212'), frequentemente precedida de AWSBCV012E no log stdlist, quando o batchman (e tipicamente mailman e jobman) falha em um fault-tolerant agent. Causa documentada: corrupção do arquivo Mailbox.msg, provavelmente porque o arquivo não é grande o suficiente para o número de mensagens que precisavam ser escritas nele. Recuperação documentada: se for confirmado que o problema é causado por overflow, usar o comando evtsize para aumentar o arquivo Mailbox.msg (garantindo espaço suficiente no file system), excluir o arquivo de mensagens corrompido e reiniciar o HCL Workload Automation com o comando conman start no fault-tolerant agent (todos os eventos no arquivo corrompido são perdidos); se não tiver certeza da causa, contatar o suporte.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEC002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?*
- *Qual é o significado da mensagem de erro AWSBCV012E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?*

---

### 34. hwa-10.2.8-incident-bcv012e-0044

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > mailbox [mailbox]]`

**Regra Canônica / Evidência:**
Sintoma: AWSDEC002E 'An internal error has occurred. The following UNIX system error occurred on an events file: 9' no stdlist, frequentemente precedida de AWSBCV012E no log, quando o batchman (e tipicamente mailman e jobman) falha em um fault-tolerant agent. Causa: corrupcao/overflow do arquivo Mailbox.msg — o arquivo nao e grande o suficiente para o numero de mensagens que precisavam ser escritas. Resolucao documentada: (1) usar evtsize para aumentar o arquivo Mailbox.msg (garantindo espaco suficiente no file system); (2) excluir o arquivo de mensagens corrompido; (3) reiniciar o HCL Workload Automation com conman start no fault-tolerant agent. Pesquisa Perplexity (2026-08-23) confirma o mesmo procedimento.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEC002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?*
- *Qual é o significado da mensagem de erro AWSBCV012E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?*
- *O que causa e como solucionar o problema: AWSDEC002E 'An internal error has occurred?*

---

### 35. hwa-10.2.8-incident-behind-firewall-0077

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > network [network]]`

**Regra Canônica / Evidência:**
Sintoma: comandos start/stop do master domain manager para fault-tolerant agents de outros dominios nao funcionam. Causa: os FTAs desses dominios nao tem o atributo behind firewall marcado como on no banco do HCL Workload Automation; com firewall entre o master e os dominios, comandos start/stop devem passar pela hierarquia. Resolucao: marcar behind firewall=on para os FTAs atras de firewall, para que o stop seja enviado ao domain manager que repassa ao FTA. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: comandos start/stop do master domain manager para fault-tolerant agents de outros dominios nao funcionam?*

---

### 36. hwa-10.2.8-incident-bhu072e-0051

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > mailbox [mailbox]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU072E indicando fault relacionado ao ambiente do fault-tolerant agent, frequentemente associado a corrupcao do arquivo Mailbox.msg ou problema de tamanho do mailbox. Resolucao: (1) verificar e aumentar o tamanho do Mailbox.msg se necessario (evtsize) garantindo espaco em disco; (2) se corrompido, excluir o arquivo corrompido; (3) reiniciar o fault-tolerant agent (conman start). Pesquisa Perplexity (2026-08-23) confirma. Correlacao: mesmo recovery de AWSBCV012E/AWSDEC002E (Mailbox.msg overflow).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU072E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU072E no HWA?*
- *Qual é o significado da mensagem de erro AWSBCV012E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?*
- *O que causa e como solucionar o problema: AWSBHU072E indicando fault relacionado ao ambiente do fault-tolerant agent, frequentemente associado a corrupcao do arquivo Mailbox?*

---

### 37. hwa-10.2.8-incident-bhu158e-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU158E ao executar conman link (lk) / unlink contra uma workstation do tipo agent/pool/broker/remote engine. Causa: o comando link/unlink so e suportado em workstations do tipo FTA/master domain manager; agents dinamicos nao suportam a operacao. Resolucao: nao usar link/unlink em agents; a operacao e desnecessaria para agents (eles se conectam automaticamente). O lab confirmou: conman lk =MDMDA;noask -> AWSBHU158E 'comando não suportado em workstation agent/pool/broker/remote engine' (MDMDA e dynamic agent).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU158E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU158E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar syntax?*
- *O que causa e como solucionar o problema: AWSBHU158E ao executar conman link (lk) / unlink contra uma workstation do tipo agent/pool/broker/remote engine?*

---

### 38. hwa-10.2.8-incident-bin091e-0049

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: incidents > broker [broker]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBIN091E indicando problema de broker/comunicacao entre domain manager, fault-tolerant agent ou broker server. Causa: porta SSL mal configurada no localopts (SSL port = 0 ou valor errado), ou broker server inacessivel/rede entre componentes. Resolucao: (1) verificar o valor da porta SSL no localopts do domain manager/FTA e corrigir para o valor correto; (2) reiniciar os componentes envolvidos; (3) verificar conectividade de rede/TCP/SSL entre broker e manager. Pesquisa Perplexity (2026-08-23) confirma SSL port como causa principal.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIN091E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para broker?*
- *O que causa e como solucionar o problema: AWSBIN091E indicando problema de broker/comunicacao entre domain manager, fault-tolerant agent ou broker server?*

---

### 39. hwa-10.2.8-incident-evtsize-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: arquivo de eventos do FTA/agent muito grande ou com problemas de espaco. Resolucao: a variavel/parametro evtsize controla o tamanho maximo do arquivo de eventos; ajustar evtsize e monitorar o crescimento evita falhas de comunicacao por estouro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: arquivo de eventos do FTA/agent muito grande ou com problemas de espaco?*

---

### 40. hwa-10.2.8-incident-exec-status-race-0092

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: um job permanece em status 'exec' apos o JnextPlan mas nao esta rodando. Causa (cenario): (1) um job completa o processamento; (2) o FTA marca o job como succ no Symphony atual; (3) o FTA prepara e envia os eventos JS e JT informando o master — mas o JnextPlan roda antes de o master processar esses eventos, criando uma condicao de corrida em que o job fica preso em exec. Fonte: HCL Troubleshooting Guide 10.2.8 (A job remains in exec status after JnextPlan).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: um job permanece em status 'exec' apos o JnextPlan mas nao esta rodando?*

---

### 41. hwa-10.2.8-incident-fab164e-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: incidents > installation [installation]]`

**Regra Canônica / Evidência:**
Sintoma: AWSFAB164E durante instalacao do agent (serverinst/twsinst). Causa: valores iguais para -thiscpu e -displayname, ou nome invalido para a workstation. Resolucao: usar -thiscpu diferente do nome do master e -displayname como nome do dynamic agent (nao igual ao master).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSFAB164E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSFAB164E no HWA?*
- *Como utilizar o utilitário serverinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no serverinst para gerenciar installation?*
- *O que causa e como solucionar o problema: AWSFAB164E durante instalacao do agent (serverinst/twsinst)?*

---

### 42. hwa-10.2.8-incident-fta-cleanup-0079

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: um fault-tolerant agent nao linka ao seu master domain manager e nenhum outro procedimento de link resolveu. Causa: quase certamente um mismatch entre os niveis dos varios arquivos usados no FTA. Resolucao: se todas as outras tentativas falharam, executar o procedimento de cleanup documentado - ATENCAO: este procedimento perde dados (a menos que o FTA nao esteja linkando apos uma instalacao nova), portanto nao deve ser executado sem necessidade. Fonte: HCL Troubleshooting Guide 10.2.8 (FTA does not link).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: um fault-tolerant agent nao linka ao seu master domain manager e nenhum outro procedimento de link resolveu?*

---

### 43. hwa-10.2.8-incident-fta-dec002e-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: AWSDEC002E relacionado a fault-tolerant agent (FTA) em decada de conexao. Causa: problemas de comunicacao entre o FTA e o master domain manager. Resolucao: verificar conectividade de rede, certificados e o processo batchman/jobman no FTA; consultar troubleshooting de FTA (awstrftadec002.html).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEC002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?*
- *O que causa e como solucionar o problema: AWSDEC002E relacionado a fault-tolerant agent (FTA) em decada de conexao?*

---

### 44. hwa-10.2.8-incident-fta-dual-netman-0073

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: AWSEDW001I 'Getting a new socket: 9' — um fault-tolerant agent tem dois processos netman escutando na mesma porta. Causa: instalacao de mais de uma instancia HCL Workload Automation na mesma workstation sem especificar portas netman diferentes. Resolucao: parar um dos dois servicos netman e especificar uma porta unica usando a opcao local nm port no localopts; garantir que a definicao da workstation no master domain manager use a porta unica. Fonte: HCL Troubleshooting Guide 10.2.8 (network link problems).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSEDW001I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSEDW001I no HWA?*
- *O que causa e como solucionar o problema: AWSEDW001I 'Getting a new socket: 9' — um fault-tolerant agent tem dois processos netman escutando na mesma porta?*

---

### 45. hwa-10.2.8-incident-fta-events-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: FTA perde eventos ou para de reportar. Causa: arquivo de eventos (events file) cheio/corrompido ou comunicacao interrompida. Resolucao: verificar o events file do FTA, ajustar evtsize, e se necessario resetfta para recriar o estado; monitorar logs do jobman/batchman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: FTA perde eventos ou para de reportar?*

---

### 46. hwa-10.2.8-incident-fta-nolink-jnextplan-0065

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: durante o JnextPlan, fault-tolerant agents nao conseguem ser linkados. Causa: o comando conman stop demora para parar todos os processos do FTA local; se o Symphony foi baixado nesse intervalo, o agent nao consegue recebe-lo porque alguns processos ainda rodam. Resolucao: aguardar a parada completa dos processos do FTA antes do relink; verificar se o Symphony foi recebido corretamente apos o JnextPlan. Fonte: HCL Troubleshooting Guide 10.2.8 (During Jnextplan fault-tolerant agents cannot be linked).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar fta?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: durante o JnextPlan, fault-tolerant agents nao conseguem ser linkados?*

---

### 47. hwa-10.2.8-incident-listsym-msymoldbackup-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: jobs rodam em um fault-tolerant agent e o Symphony local do FTA foi atualizado, mas o Symphony do master domain manager nao foi atualizado — devido a uma falha de link com o master e a remocao dos arquivos <TWS_home>\TWS\*.msg. Resolucao: verificar o Symphony mais recente processado no fault-tolerant agent usando o comando conman listsym a partir da linha de comando do FTA, que mostra o ultimo Symphony salvo como MSymOldBackup. Fonte: HCL Troubleshooting Guide 10.2.8 (Symphony file on the master domain manager not updated with fault-tolerant agent job status).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar fta?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: jobs rodam em um fault-tolerant agent e o Symphony local do FTA foi atualizado, mas o Symphony do master domain manager nao foi atualizado — devido a uma falha de link com o master e a remocao dos arquivos <TWS_home>\TWS\*?*

---

### 48. hwa-10.2.8-incident-mailman-timeout-0066

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > mailman [mailman]]`

**Regra Canônica / Evidência:**
Sintoma: false timeout nos processos do mailman no domain manager - durante a inicializacao apos JnextPlan, os arquivos *.msg podem encher com backlog de mensagens dos FTAs; enquanto o mailman processa mensagens de um FTA, mensagens de outros FTAs esperam ate exceder o intervalo configurado e o mailman faz unlink. Resolucao: aumentar os valores das variaveis mm response e mm unlink no arquivo localopts (~maestro/localopts), em incrementos pequenos (60-300 segundos) ate os timeouts pararem. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: false timeout nos processos do mailman no domain manager - durante a inicializacao apos JnextPlan, os arquivos *?*

---

### 49. hwa-10.2.8-incident-mailman-ws-add-0128

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > mailman [mailman]]`

**Regra Canônica / Evidência:**
Sintoma: apos adicionar uma dynamic agent workstation ao plano, o agent nao aparece/nao funciona mesmo apos restart dos processos do master domain manager. Causa: o processo mailman do master domain manager nao consegue gerenciar o evento do HWA que comunica a adicao da workstation ao plano. Resolucao: reiniciar os processos do master domain manager executando em ordem: conman stop e depois conman start (ou o comando equivalente). Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar mailman?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para mailman?*
- *Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?*
- *O que causa e como solucionar o problema: apos adicionar uma dynamic agent workstation ao plano, o agent nao aparece/nao funciona mesmo apos restart dos processos do master domain manager?*
- *Como utilizar o comando conman 'start' para gerenciar workstations e execução no HWA?*
- *Como utilizar o comando conman 'stop' para gerenciar workstations e execução no HWA?*

---

### 50. hwa-10.2.8-incident-oracle-schema-config-0106

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade. Causa: o conjunto de tabelas do banco nao foi corrigido — o DAOCommon.properties ainda referencia rdbmsName=db2 em vez de oracle, ou os valores *Schema= nao apontam para o schema Oracle. Resolucao: seguir o procedimento de upgrade do database schema (Planning and Installation Guide) e atualizar manualmente o DAOCommon.properties: rdbmsName=oracle e os tres valores *Schema= para o schema Oracle. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para database?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade?*
- *O que causa e como solucionar o problema: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade?*

---

### 51. hwa-10.2.8-incident-pobox-sizing-0087

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: JnextPlan falha ao iniciar. Causa: a rede HCL Workload Automation requer tuning adicional por problema de dimensionamento dos arquivos pobox — o tamanho default dos pobox files e 10MB. Resolucao: aumentar o tamanho conforme criterios: (1) o papel (master domain manager, domain manager ou FTA) da workstation na rede — papeis hierarquicos maiores precisam de pobox maiores. Fonte: HCL Troubleshooting Guide 10.2.8 (JnextPlan fails to start).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: JnextPlan falha ao iniciar?*

---

### 52. hwa-10.2.8-incident-recovery-resetfta-0062

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: Symphony corrompido em um fault-tolerant agent. RECOVERY OFICIAL: usar o comando resetFTA <cpu> para automatizar a recuperacao - o comando renomeia Symphony, Sinfonia e arquivos *.msg no FTA onde ocorreu a corrupcao e gera um Sinfonia atualizado que e enviado ao FTA, permitindo relink. Notas: ha perda de dados (eventos de status de job, conteudo de Mailbox.msg e tomaster.msg); se informacao de estado de um job estava nessas filas, o job e reexecutado; aplicar com cautela; nao disponivel no Dynamic Workload Console. Sintaxe: resetFTA <cpu>. Fonte: HCL Troubleshooting Guide 10.2.8 (Recovery procedure on a fault-tolerant agent with the use of the resetFTA command).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: Symphony corrompido em um fault-tolerant agent?*

---

### 53. hwa-10.2.8-incident-resetfta-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > fta [fta]]`

**Regra Canônica / Evidência:**
Sintoma: FTA com problemas de sincronizacao ou arquivo de eventos (events file) corrompido. Resolucao: resetfta reinicializa o fault-tolerant agent, recriando o arquivo de eventos; e uma operacao destrutiva que deve ser usada com cautela, pois remove o estado local do FTA.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: FTA com problemas de sincronizacao ou arquivo de eventos (events file) corrompido?*

---

### 54. hwa-10.2.8-incident-sqljdbc4-driver-0145

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: incidents > dynamic-agent [dynamic-agent]]`

**Regra Canônica / Evidência:**
Sintoma: ao submeter um job MSSQL ou Database job em banco MSSQL, recebe AWKDBE009E 'Unable to create the connection - java.lang.UnsupportedOperationException: Java Runtime Environment (JRE) version 1.6 is not supported by this driver. Use the sqljdbc4.jar class library, which provides support for JDBC 4.0'. Causa: drivers JDBC nao suportados presentes no diretorio de drivers JDBC — o dynamic agent pode carrega-los e causar o erro. Resolucao: (1) remover os drivers JDBC nao suportados; (2) parar o dynamic agent com ShutDownLwa; (3) reiniciar o dynamic agent com StartUpLwa; verificar que apenas o sqljdbc4.jar necessario esta no diretorio de drivers JDBC. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKDBE009E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKDBE009E no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?*
- *O que causa e como solucionar o problema: ao submeter um job MSSQL ou Database job em banco MSSQL, recebe AWKDBE009E 'Unable to create the connection - java?*

---

### 55. hwa-10.2.8-incident-ssl-port-zero-0074

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: incidents > network [network]]`

**Regra Canônica / Evidência:**
Sintoma: problema de link entre workstation e domain manager apos mudanca do modo SSL — a workstation nao consegue relinkar. Causa: a statement SSL port no localopts do domain manager ou do fault-tolerant agent esta configurada com valor 0. Resolucao: corrigir o numero da porta SSL no localopts para o valor correto e reiniciar o netman na workstation para que escute na porta correta. Fonte: HCL Troubleshooting Guide 10.2.8 (network link problems - SSL mode).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa e como solucionar o problema: problema de link entre workstation e domain manager apos mudanca do modo SSL — a workstation nao consegue relinkar?*

---

### 56. hwa-10.2.8-incident-symphony-fta-manual-0063

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: Symphony corrompido em um agent/domain manager (nao master). RECOVERY OFICIAL manual: (1) no domain manager, unlink o agent com problema; (2) no agent: parar se ainda nao falhou; deletar ou renomear os arquivos Symphony e Sinfonia; (3) no domain manager: backup e preparar o novo Symphony; o agent recebe o Symphony ao relink. Perda: remocao e substituicao completa do Symphony causa perda de dados - eventos de status, conteudo de Mailbox.msg e tomaster.msg; jobs com estado nessas filas sao reexecutados. Fonte: HCL Troubleshooting Guide 10.2.8 (Corrupt Symphony file recovery em FTA/lower domain manager).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: Symphony corrompido em um agent/domain manager (nao master)?*

---

### 57. hwa-10.2.8-install-twsinst-agent-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
O dynamic agent do HCL Workload Automation 10.2.8 é instalado com o script twsinst (twsinst.vbs/twsinst) e usa parâmetros com prefixo - (hífen): -agent dynamic junto com -tdwbhostname (nome do dynamic workload broker/dynamic domain manager ao qual o agente se registra) e -tdwbport (porta HTTPS do broker), além da pasta de certificados -sslkeysfolder com -sslpassword.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar install?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*

---

### 58. hwa-10.2.8-messages-awktsa050e-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: messages > awktsa [messages_dynamic_agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWKTSA050E indica um problema de certificado SSL no dynamic agent: o agente nao consegue estabelecer uma conexao SSL com o master domain manager. A causa comum e a porta SSL incorreta no arquivo localopts do agente, ou o certificado do master nao e confiavel pelo agente. A solucao inclui verificar o parametro SSLPort no localopts (default 31116), reiniciar o agente (ShutDownLwa / StartUpLwa) e, se necessario, forcar o download do certificado removendo os arquivos .pem do diretorio cert/ e reiniciando. A mensagem AWKTSA050E faz parte do conjunto AWKTSA (dynamic agent messages).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWKTSA050E no HWA?*
- *Como solucionar ou diagnosticar o erro AWKTSA050E no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para awktsa?*

---

### 59. hwa-10.2.8-messages-awsita104e-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: messages > awsita [messages_dynamic_agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA104E indica que o dynamic agent (fault-tolerant agent) nao conseguiu interpretar a saida do scanner de recursos de hardware (hardware scan). A causa pode ser formato inesperado da saida do scanner, permissoes incorretas do executavel do scanner, ou configuracao SSL/HTTPS incorreta. A solucao inclui verificar o scanner e suas permissoes, revisar a configuracao do scanner de recursos no localopts do agente e do domain manager, e corrigir configuracoes SSL/HTTPS se usadas para os resultados do scan. A referencia oficial esta em https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrdynagtrscanres.html.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA104E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA104E no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para awsita?*
- *Qual é o significado da mensagem de erro AWSITA104E no HWA e qual ação é recomendada?*

---

### 60. hwa-10.2.8-messages-awsita238e-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: messages > awsita [messages_dynamic_agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a mensagem AWSITA238E indica que o usuario nao tem autorizacao para acessar o servidor (The user is not authorized to access the server). A causa pode ser: o usuario configurado no dynamic agent nao tem permissoes adequadas no master domain manager, ou as configuracaoes de autenticacao/SSO do broker/dispatcher estao incorretas. A solucao inclui verificar as permissoes do usuario no servidor, revisar as configuracaoes de autenticacao do broker, e renovar/refresh as credenciais ou tokens de acesso. AWSITA238E faz parte do conjunto AWSITA (resource scan agent messages).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA238E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA238E no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para awsita?*
- *Qual é o significado da mensagem de erro AWSITA238E no HWA e qual ação é recomendada?*

---

### 61. hwa-10.2.8-nestedvar-native-job-types-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, variáveis aninhadas podem ser definidas em uma tabela de variáveis usando apenas a sintaxe ${variablename}; ao referenciar a variável no job definition de uma integração em dynamic agent, tanto ^ quanto ${} são suportados; o recurso é suportado apenas em integrações em dynamic agents, não em job types nativos, e não é suportado em fault-tolerant agents (FTA).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 62. hwa-10.2.8-perf-file-deps-tuning-0164

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), ao usar file dependencies com dynamic agents, o polling period e dirigido pela propriedade localopts 'bm check file' presente no Dynamic Domain Manager (default 120 segundos). O throughput do servidor e governado por 4 parametros: polling period, numero de file dependencies, conexao de rede agentes-servidor e atividades de Background Scheduling. Recomendacao de tuning: T > N/10, sendo T o valor de bm check file e N o total de file dependencies. Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), ao usar file dependencies com dynamic agents, o polling period e dirigido pela propriedade localopts 'bm check file' presente no Dynamic Domain Manager (default 120 segundos)?*

---

### 63. hwa-10.2.8-pool-broker-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Workstation pool: agrupa agentes dinâmicos com características semelhantes; o HWA balanceia jobs entre os membros e reatribui se um membro ficar indisponível; criar Type Pool hospedado pelo workload broker e adicionar agentes dinâmicos como membros.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Como o HWA balanceia e despacha jobs dinamicamente em pools de agentes?*

---

### 64. hwa-10.2.8-proc-tree-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, os processos de gerenciamento ativos em cada workstation (fault-tolerant agent e domain managers) são iniciados na ordem netman -> mailman -> batchman -> jobman pelo StartUp (ou como serviço do sistema). O netman é o processo de gerenciamento de rede que estabelece conexões entre os processos mailman remotos e os processos writer locais; o mailman gerencia a comunicação entre workstations; o batchman opera autonomamente em cada FTA/domain manager, escaneando o arquivo Symphony para resolver dependências e iniciar jobs; o jobman inicia e monitora os jobs. Em um standard agent, o batchman não roda localmente (o jobman responde a requisições de launch do domain manager).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 65. hwa-10.2.8-proc-tree-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed (fault-tolerant agent e domain managers), o batchman opera autonomamente em relação ao seu arquivo Symphony local: escaneia o Symphony para resolver dependências e lançar jobs via jobman. Em um FTA, mesmo se a conexão de rede com o domain manager cair, os processos locais continuam processando os jobs conforme as instruções da cópia local do Symphony. O Symphony é o arquivo que contém as instruções de agendamento (quais jobs rodar) distribuído a todas as workstations envolvidas no plano.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 66. hwa-10.2.8-proc-tree-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed, os processos de gerenciamento de uma workstation (fault-tolerant agent ou domain manager) baseiam-se na infraestrutura WebSphere Application Server, instalada automaticamente com a workstation. O StartUp (ou o serviço do sistema) inicia o netman, que por sua vez leva à criação da cadeia mailman, batchman e jobman. O netman escuta na porta padrão 31111 para conexões de rede entre workstations.

**Plataforma / Validação:** Distributed

---

### 67. hwa-10.2.8-sec-encryption-at-rest-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 criptografa automaticamente em repouso arquivos-chave do produto — Symphony file, message queues, arquivo useropts e o diretório jmJobTableDir em dynamic agents — usando criptografia AES-256 ou AES-128 em todas as instalações novas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual endpoint REST API V2 é utilizado para agent no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 68. hwa-10.2.8-sec-fault-tolerant-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o modelo de segurança baseado em funções não suporta gerenciamento centralizado de segurança em agentes fault-tolerant; nesses agentes a segurança é gerenciada localmente em cada workstation.

**Plataforma / Validação:** Distributed

---

### 69. hwa-10.2.8-sec-ssl-version-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A keyword ssl version no HCL Workload Automation 10.2.8 (no ita.ini de dynamic agents e em localopts de componentes nativos/FTAs) aceita valores exatos (TLSv1.0 a TLSv1.3), valores mínimos (atleast.TLSv1.x) e valores máximos (max.TLSv1.x) para controlar a versão do protocolo TLS usada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 70. hwa-10.2.8-sec-tls-1-3-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
O suporte ao protocolo de segurança TLS V1.3 no HCL Workload Automation é disponível a partir da versão 10.1 FP4 em diante, e sua configuração pode ser feita manualmente em dynamic agents, componentes Open Liberty e componentes nativos/agentes fault-tolerant.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*

---

### 71. hwa-10.2.8-tune-jm-concurrency-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
The "jm concurrency" and "jm startup" options are not documented in the HCL Workload Automation 10.2.8 localopts reference. Job concurrency on the dynamic agent is controlled by ExecutorsMinThreads/ExecutorsMaxThreads in JobManager.ini.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: The "jm concurrency" and "jm startup" options are not documented in the HCL Workload Automation 10.2.8 localopts reference?*

---

### 72. hwa-10.2.8-tune-notifier-min-threads-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
A propriedade NotifierMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número mínimo de threads de notificação de mudanças de status de jobs ao dynamic workload broker, com padrão documentado de 3.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para agent?*
- *Qual a regra documentada no HWA Distributed sobre: A propriedade NotifierMinThreads, na seção [Launchers] do JobManager?*

---

### 73. hwa-10.2.8-vm-9f-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: general_operations > syntax [task_job_definition]]`

**Regra Canônica / Evidência:**
A definição de job TASK com XML jsdl:jobDefinition e tasktype UNIX/WINDOWS/OTHER/BROKER é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para syntax?*
- *Qual a regra documentada no HWA Distributed sobre: A definição de job TASK com XML jsdl:jobDefinition e tasktype UNIX/WINDOWS/OTHER/BROKER é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica?*

---

### 74. hwa-10.2.8-vm-conman-distributed-only-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O conman é documentado apenas na documentação do HCL Workload Automation distribuído (seção 'Managing objects in the plan - conman' do User's Guide and Reference), como programa de linha de comando do master domain manager e fault-tolerant agents; não é listado na documentação do HCL Workload Automation for Z (z/OS).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 75. hwa-10.2.8-workstation-fault-tolerant-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Geral > Tópico: agents > agent [agent]]`

**Regra Canônica / Evidência:**
Tipos de workstation: agente dinâmico (agent), agente tolerante a falhas (fta), domain manager (manager), pool (pool) e workstation class.

**Plataforma / Validação:** Distributed

---

### 76. hwa-9.5-conman-eventrules-contrast-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-eventrules-0001: na 9.5, as event rules eram definidas por composer create rule com suporte basico; na 10.2.8, alem de composer create rule e conman rule, ha o fluxo de sendevent->event processor (AWSEVP001I) e integracao com dynamic agents (Workload Service Assurance); a taxonomia e a cobertura de eventos sao version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSEVP001I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSEVP001I no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 77. hwa-9.5-conman-showcpus-contrast-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-showcpus-0001: na 9.5, conman sc (showcpus) listava workstations/CPUs do dominio com formato standard; na 10.2.8 o comando permanece (sc), mas os formatos (standard vs link) e a identificacao de X-AGENT/HOST foram padronizados e sao usados em pre-checagens de resetFTA; o formato de saida e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a diferença de formato na saída do comando conman showcpus entre a versão 9.5 e 10.2.8?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 78. hwa-install-1028-bkmdm-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na configuração de um BKMDM HWA 10.2.8, o backup master deve ser definido no banco como FTA full-status autolink e incluído no plano com JnextPlan -for 0000. Context: Define the master domain manager configured as backup as a full status autolink fault-tolerant agent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 79. hwa-install-1028-fta-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, um FTA pode resolver dependências locais e iniciar jobs na ausência do domain manager; um Standard Agent é instalado pelo mecanismo de FTA, mas não é fault-tolerant. Context: A fault-tolerant agent can resolve local dependencies and launch jobs in the absence of a domain manager.

**Plataforma / Validação:** Distributed

---

### 80. hwa-install-agent-1028-ssl-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação HWA 10.2.8 de Dynamic Agent ou FTA, certificados podem ser obtidos do MDM com wauser/wapassword ou fornecidos por sslkeysfolder; HWA gera keystore/truststore e configura SSL, e Java é requerido para SSL durante a instalação. Context: HCL Workload Automation automatically generates the keystore and truststore... Enabling SSL during installation requires Java run time.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*

---

### 81. hwa-install-agent-1028-twsinst-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação HWA 10.2.8, twsinst é o instalador documentado para FTA e Dynamic Agent; a instalação FTA também instala o cliente remoto de linha de comando. Context: Use only the twsinst script to install agents. When you install a fault-tolerant agent, also the remote command-line client is installed.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar install?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*

---

### 82. hwa-install-ddm-1028-prereqs-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação DDM/BDDM HWA 10.2.8, o componente requer banco dedicado, Liberty dedicado, certificados e parâmetros para localizar MDM/broker, incluindo master, mdmbrokerhostname e mdmhttpsport. Context: The dynamic domain manager and backup dynamic domain manager require a dedicated database and a dedicated Open Liberty.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*

---

### 83. hwa-lab-10.2.8-agent-both-installation-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) & Dynamic Agent > Interface: CLI twsinst / composer > Tópico: installation > agent_both [agent_both]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção '-agent both' do utilitário twsinst instala concomitantemente em um único nó o Fault-Tolerant Agent (Netman/Mailman na porta 31111) e o Dynamic Agent (JobManager/ITA na porta 31114) sob o mesmo usuário wauser.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como instalar simultaneamente um Fault-Tolerant Agent e um Dynamic Agent com o twsinst no HWA?*
- *Qual o comando para colocar uma workstation em estado IGNORE no banco do HWA utilizando o composer?*
- *Como funciona a opção -agent both do instalador twsinst no HCL Workload Automation 10.2.8?*

---

### 84. hwa-lab-10.2.8-awsbin091e-rootcause-0098

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No laboratório HWA 10.2.8, o GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration retorna HTTP 500 com AWSJSY404E envolvendo AWSBIN091E 'The workstation does not support monitoring.' para TODAS as workstations (MDM, MDMDA, MDMXA, MDM_DWB), mesmo com o monman/EDWA ativo. O conman showcpus confirmou que MDM tem o flag 'I J M EA' (monman M + event-driven EA) e MDMDA tem 'LBI J M' (monman M ativo) no Symphony — portanto o monitoring está ativo e o erro NÃO reflete o estado real. A causa raiz é a implementação do endpoint REST V2, que lê o monitoring configuration via a operação 'readFromScribner' de um local não suportado pelo Symphony nessas workstations broker-managed (o error wrapper AWSJSY404E 'The Symphony plan operation readFromScribner could not be completed'). Conclusão: o REST V2 monitoring-configuration é um endpoint de leitura quebrado/não suportado para estas workstations, enquanto o event processing, o monman e os event rules (FileMonitor/TWSObjectsMonitor) funcionam normalmente via composer/deployconf/sendEvent.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJSY404E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?*
- *Qual é o significado da mensagem de erro AWSBIN091E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?*

---

### 85. hwa-lab-10.2.8-fta-offline-autonomy-vs-dynamic-agent-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent & Dynamic Agent > Interface: CLI conman / Logs de Agente > Tópico: architecture > fault_tolerance [fta_vs_dynagent]]`

**Regra Canônica / Evidência:**
Em caso de isolamento total de rede entre o nó de execução e o Master, o Fault-Tolerant Agent (FTA) mantém autonomia operacional completa graças à cópia local do arquivo Symphony no disco (Batchman LIVES local), enquanto o Dynamic Agent entra em falha de conexão (AWSITA081E / AWSITA366E) por depender da conectividade HTTPS na porta 31116 com o Broker.

**Plataforma / Validação:** Distributed; Linux x86_64; containers tws-agent e tws-hwa; HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Qual a diferença fundamental de tolerância a falhas de rede entre um Fault-Tolerant Agent e um Dynamic Agent?*
- *Por que o conman local de um FTA continua funcionando mesmo quando o link de rede com o Master está interrompido?*
- *O que significa a mensagem AWSITA081E com erro AWSITA366E no log do JobManager de um agente dinâmico?*

---

### 86. hwa-lab-10.2.8-message-ita031i-0150

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
AWSITA031I: mensagem informativa do JobManager relacionada a execucao de jobs no dynamic agent. Observada no lab: ao submeter ad hoc a stream CPLXSTRM em MDMDA, seus quatro jobs dependentes executaram em ordem com prioridades 10, 20, HI e GO, e a stream completou SUCC sob LIMIT 2 — o JobManager registrou AWSITA031I/AWSITA034I durante a execucao. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA034I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA034I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA031I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA031I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA031I no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSITA034I no HWA e qual ação é recomendada?*

---

### 87. hwa-lab-10.2.8-message-ita111i-0154

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: Geral > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
AWSITA111I: 'The Resource Advisor Agent is stopped' — mensagem do JobManager indicando que o Resource Advisor Agent esta parado no dynamic agent. Observada no lab: durante startup inicial, MDMDA registrou erros AWKRRP086E_DOMAIN_NOT_CREATED de resource registration, seguidos de AWSITA083I de envio de informacoes de recursos; apos ShutDownLwa/StartUpLwa, o JobManager reiniciou e AWSITA083I foi retomado sem recorrencia. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSITA083I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA083I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA111I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSITA111I no HWA?*
- *Qual é o significado da mensagem de erro AWSITA111I no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSITA083I no HWA e qual ação é recomendada?*

---

### 88. hwa-version-matrix-agent-zos-distributed-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation (distributed) 10.2.8 (Distributed (agent for z/OS)) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O 'Agent for z/OS' e um agente do HCL Workload Automation Distributed que atua como proxy entre o dynamic workload broker e o JES do z/OS; ele e definido como uma workstation no plano Distributed e e gerenciado pelas interfaces composer e conman do lado Distributed, distinto do produto nativo HCL Workload Automation for Z.

**Plataforma / Validação:** Distributed (agent for z/OS)

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 89. hwa-version-matrix-planman-cli-scope-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: cli_planning > composer [composer]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o Command Line Client (instalado com fault-tolerant agent) permite executar remotamente composer, optman e apenas planman showinfo e planman unlock; os demais comandos planman devem ser executados localmente no master domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Como utilizar o utilitário optman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no optman para gerenciar composer?*

---
