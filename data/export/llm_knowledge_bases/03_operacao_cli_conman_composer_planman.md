# OPERACAO CLI (CONMAN/COMPOSER/PLANMAN)

> Total de tópicos canônicos cobertos nesta seção: 366

---

### 1. com-change-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > change [change_management]]`

**Regra Canônica / Evidência:**
Uma prática organizacional recomendada de gestão de mudanças é: (1) planejar a mudança em um workspace/pasta separada; (2) usar a palavra-chave draft no job stream para impedir que entre no preproduction plan; (3) revisar versões usando o versionamento baseado em auditoria (dbAudit=1 + auditStore=db) antes do Deploy; e (4) aplicar o Deploy no Graphical Designer. A exigência de aprovação/workflow é decisão da organização; o produto oferece as capacidades (draft, versionamento, auditoria com justificativa opcional), não um fluxo obrigatório.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a palavra-chave draft impede que um job stream entre no plano de produção?*

---

### 2. com-config-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > config [config_management]]`

**Regra Canônica / Evidência:**
Uma prática recomendada de configuração avançada é separar ambientes (dev/test/prod) usando folders/pastas distintas e instâncias dedicadas, e versionar as mudanças de configuração junto com as definições de jobs usando a auditoria de banco (dbAudit + auditStore=db). Isso é orientação organizacional; o produto fornece os mecanismos (folders, auditoria) mas não prescreve a separação.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de configuração avançada é separar ambientes (dev/test/prod) usando folders/pastas distintas e instâncias dedicadas, e versionar as mudanças de configuração junto com as definições de jobs usando a auditoria de banco (dbAudit + auditStore=db)?*

---

### 3. com-config-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Uma prática recomendada de configuração avançada é sincronizar a configuração do site de recuperação de desastres (DR) com o site primário, incluindo o espelhamento do banco de dados e a cópia das chaves AES (TWA_DATA_DIR/ssl/aes) e certificados para o backup master domain manager, para garantir que o ambiente DR possa descriptografar o Symphony. Isso usa as capacidades documentadas (backup MDM com banco espelhado, chaves AES compartilhadas), mas a frequência e a política de sincronização são decisões organizacionais, não prescritas pela HCL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de configuração avançada é sincronizar a configuração do site de recuperação de desastres (DR) com o site primário, incluindo o espelhamento do banco de dados e a cópia das chaves AES (TWA_DATA_DIR/ssl/aes) e certificados para o backup master domain manager, para garantir que o ambiente DR possa descriptografar o Symphony?*

---

### 4. com-monitoring-scripts-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; UNIX/AIX/Linux local) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Uma prática comum de comunidade em operações HCL Workload Automation é implementar scripts próprios de monitoramento operacional do ambiente (ex.: checagem de filesystem/health check do host, health check de processos do scheduler e serviços systemd) fora do escopo da documentação oficial HCL; tais scripts são customizações locais não prescritas pelo produto. Comandos de linha de comando HWA 10.2.8 usados dentro desses scripts (conman sc/showcpus, composer list/display, etc.) são documentados oficialmente, mas o script como um todo NÃO é procedimento oficial da HCL.

**Plataforma / Validação:** Distributed; UNIX/AIX/Linux local

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 5. com-naming-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_convention]]`

**Regra Canônica / Evidência:**
Uma prática organizacional recomendada é usar uma convenção de nomenclatura que codifique função e contexto no nome do job, por exemplo um prefixo por aplicação (FIN_, HR_, OPS_) e um sufixo que indique a classe de janela (crit, batch, maint). Isso NÃO é um padrão prescrito pelo HCL Workload Automation 10.2.8; o produto impõe apenas limites técnicos (job até 40 caracteres, começando com letra, alfanumérico/-/_).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Uma prática organizacional recomendada é usar uma convenção de nomenclatura que codifique função e contexto no nome do job, por exemplo um prefixo por aplicação (FIN_, HR_, OPS_) e um sufixo que indique a classe de janela (crit, batch, maint)?*

---

### 6. com-naming-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_convention]]`

**Regra Canônica / Evidência:**
Uma prática recomendada de comunidade é usar um identificador de ambiente (DEV/TST/PRO) como parte do nome ou da pasta (folder) do job stream, isolando definições por ambiente. Não é um padrão obrigatório do produto; o HCL Workload Automation suporta folders e prefijos de pasta nos seletores [[folder/]workstation#][folder/]jobname.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de comunidade é usar um identificador de ambiente (DEV/TST/PRO) como parte do nome ou da pasta (folder) do job stream, isolando definições por ambiente?*

---

### 7. com-quality-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > quality [sla_quality]]`

**Regra Canônica / Evidência:**
Uma prática recomendada de qualidade é calcular o percentual de jobs concluídos pontualmente na janela, derivando de contadores já coletados pelo produto (Successful_runs, Abended_runs, Late_start_runs, Late_end_runs na view JOB_STATISTICS_V). A fórmula específica é decisão da organização; a HCL fornece os dados brutos, não o indicador prescrito.

**Plataforma / Validação:** Distributed

---

### 8. com-quality-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Uma prática recomendada é monitorar a taxa de incidentes recorrentes (ex.: mensagens AWSJPL017E de falha do JnextPlan) e a razão entre trabalho programado e não programado, usando a auditoria (enDbAudit/enPlanAudit) e o histórico de mensagens. Isso é uma escolha organizacional de melhoria, não um padrão do produto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 9. hwa-10.1-fp6-final-postreports-0050

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 6 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Na documentação oficial do HCL Workload Automation 10.1 FP6, Sfinal inclui os job streams de exemplo FINAL e FINALPOSTREPORTS; FINALPOSTREPORTS segue FINAL após SWITCHPLAN concluir com sucesso e inclui CHECKSYNC para monitorar planman resync.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 10. hwa-10.1-real-enretain-deprecated-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1, a opcao global enRetainNameOnRerunFrom (conman rerun) foi descontinuada: a partir da 10.1 ela nao e mais suportada e e forcada para o valor no, devendo permanecer sem modificacao. Na 9.5 ela ainda era uma opcao ativa. Mudanca real de deprecation entre 9.5 e 10.1.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 11. hwa-10.1-real-restv2-planfilter-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 suporta planFilter com capacidades de filtro semelhantes a sintaxe Conman e OQL para ordenar resultados, permitindo filtrar jobs e job streams do plano via um unico parametro. Recurso de filtro do plano que nao existia na REST API V1 da 9.5.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*

---

### 12. hwa-10.1-real-sfinal-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 6 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Na documentacao oficial do HCL Workload Automation 10.1 Fix Pack 6, o Sfinal inclui os job streams de exemplo FINAL e FINALPOSTREPORTS; FINALPOSTREPORTS segue FINAL apos a conclusao, e a sequencia e executada no final do JnextPlan. Comportamento documentado em 10.1 FP6 para automatizar o ciclo de producao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Na documentacao oficial do HCL Workload Automation 10.1 Fix Pack 6, o Sfinal inclui os job streams de exemplo FINAL e FINALPOSTREPORTS; FINALPOSTREPORTS segue FINAL apos a conclusao, e a sequencia e executada no final do JnextPlan?*

---

### 13. hwa-10.1-restv2-planfilter-0041

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.1 Fix Pack 1, REST API V2 suporta planFilter com capacidades de filtro semelhantes à sintaxe Conman e OQL para ordenar resultados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*

---

### 14. hwa-10.2-conman-batch-double-quotes-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.0, comandos conman emitidos em batch ou inline pelo shell devem ser delimitados por aspas duplas; aspas simples não são a forma documentada pela HCL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 15. hwa-10.2-conman-command-inventory-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O índice oficial HCL 10.2.0 enumera comandos conman e tipos de workstation suportados para HCL Workload Automation Distributed.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 16. hwa-10.2-conman-sj-root-folder-selector-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.0, sj é alias de showjobs e o seletor @#@.@ filtra jobs de job streams definidos na pasta raiz (/).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 17. hwa-10.2-conman-ss-optional-selector-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.0, ss é alias de showscheds, aceita um seletor de job stream opcional e exibe informações sobre job streams.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 18. hwa-10.2-distributed-conman-cancel-job-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed; domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman cancel job, com alias cj, cancela uma instância de job no plano.

**Plataforma / Validação:** distributed; domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 19. hwa-10.2-distributed-conman-release-job-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'release job' (rj) no HCL Workload Automation 10.2.x libera um job em estado HOLD das suas dependências normais e de tempo (at, deadline, every, follows, needs, opens, priority, prompt, until) apenas para a execução atual; dependências condicionais (condições de status/saída) NÃO são liberadas e devem ser liberadas explicitamente ou confirmadas em status SUCC. A remoção permanente de uma dependência exige o comando deldep. Sintaxe: {release job | rj} jobselect [;dependency[;...]] [;noask].

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*

---

### 20. hwa-10.2-distributed-conman-release-job-dependencies-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed; domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.x, conman release job libera um job em HOLD de dependências normais e de tempo; dependências condicionais não são liberadas.

**Plataforma / Validação:** distributed; domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 21. hwa-10.2-distributed-conman-rerun-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed; domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman rerun, com alias rr, cria uma reexecução de um job elegível no plano.

**Plataforma / Validação:** distributed; domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 22. hwa-10.2-distributed-conman-showjobs-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed; conman em domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman showjobs, com alias sj, exibe informações sobre jobs no plano.

**Plataforma / Validação:** distributed; conman em domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 23. hwa-10.2-distributed-conman-showschedules-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed; conman em domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman showschedules, documentado na sintaxe como showscheds e com alias ss, exibe informações sobre job streams no plano.

**Plataforma / Validação:** distributed; conman em domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 24. hwa-10.2-distributed-conman-submit-sched-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman submit sched, abreviado sbs, submete uma definição de job stream e adiciona sua instância ao plano de produção atual.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 25. hwa-10.2-distributed-jnextplan-for0000-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.x (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed, o comando JnextPlan -for 0000 estende por 0 horas o production plan, adiciona ao Symphony as definições novas de workstation, usuário e calendário do banco e remove todas as instâncias de job stream concluídas com sucesso; com a opção -noremove essas instâncias concluídas não são removidas.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que acontece ao modificar uma instância de job no plano versus sua definição no banco?*

---

### 26. hwa-10.2-distributed-rollback-requires-backup-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > backup [backup_rollback]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation, o rollback do master domain manager para um fix pack ou release anterior só é possível se um backup tiver sido criado antes da instalação do novo fix pack ou release.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation, o rollback do master domain manager para um fix pack ou release anterior só é possível se um backup tiver sido criado antes da instalação do novo fix pack ou release?*

---

### 27. hwa-10.2-perfreport-event-processor-single-thread-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > perfreport [perfreport_event_processor]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2, o event processor e um processo de thread unica e sua capacidade de processamento e proporcional a velocidade do core e ao I/O; por isso ele nao escala horizontalmente, apenas verticalmente (aumentando CPU e/ou I/O).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, o event processor e um processo de thread unica e sua capacidade de processamento e proporcional a velocidade do core e ao I/O; por isso ele nao escala horizontalmente, apenas verticalmente (aumentando CPU e/ou I/O)?*

---

### 28. hwa-10.2-perfreport-movehistorydata-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > database [movehistorydata]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2, para gerenciar o crescimento das tabelas historicas do dynamic domain manager, a documentacao recomenda executar o script embutido movehistorydata.sh com parametros como -successfulJobsMaxAge 240, de preferencia agendado em um job em janela adequada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, para gerenciar o crescimento das tabelas historicas do dynamic domain manager, a documentacao recomenda executar o script embutido movehistorydata?*

---

### 29. hwa-10.2-perfreport-rome-lab-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > perfreport [perfreport]]`

**Regra Canônica / Evidência:**
O relatório oficial de performance IBM Workload Scheduler/HCL Workload Automation V10.2 do Rome Lab, de autoria de Lorenzo Nichele e Paolo Cavazza, foi publicado na comunidade oficial HCL e aplica-se à versão 10.2 FP0 e fix packs subsequentes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O relatório oficial de performance IBM Workload Scheduler/HCL Workload Automation V10.2 do Rome Lab, de autoria de Lorenzo Nichele e Paolo Cavazza, foi publicado na comunidade oficial HCL e aplica-se à versão 10.2 FP0 e fix packs subsequentes?*

---

### 30. hwa-10.2.0-jnextplan-options-0049

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Na documentação oficial do HCL Workload Automation 10.2.0, JnextPlan aceita -from, -to, -for, -days e -noremove; -to é mutuamente exclusivo com -for e -days.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Na documentação oficial do HCL Workload Automation 10.2.0, JnextPlan aceita -from, -to, -for, -days e -noremove; -to é mutuamente exclusivo com -for e -days?*

---

### 31. hwa-10.2.1-conman-release-job-dependency-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.1 (Distributed; domain manager ou fault-tolerant agent) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.1, a sintaxe de release job é {release job | rj} jobselect [;dependency[;...]] [;noask]; dependency é um metassímbolo que deve ser substituído por um tipo de dependência documentado, e ;dep não é uma forma abreviada documentada.

**Plataforma / Validação:** Distributed; domain manager ou fault-tolerant agent

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 32. hwa-10.2.3-plan-definition-instance-0043

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > plan [plan_definition]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.3, definições de jobs e job streams no banco tornam-se instâncias no production plan; modificar uma instância não altera automaticamente a definição no banco.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que acontece ao modificar uma instância de job no plano versus sua definição no banco?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, definições de jobs e job streams no banco tornam-se instâncias no production plan; modificar uma instância não altera automaticamente a definição no banco?*

---

### 33. hwa-10.2.3-preproduction-plan-0045

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > plan [preproduction_plan]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.3, o preproduction plan identifica antecipadamente instâncias de job streams e dependências externas do intervalo planejado; o banco é bloqueado durante sua geração para evitar conflitos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que acontece ao modificar uma instância de job no plano versus sua definição no banco?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, o preproduction plan identifica antecipadamente instâncias de job streams e dependências externas do intervalo planejado; o banco é bloqueado durante sua geração para evitar conflitos?*

---

### 34. hwa-10.2.3-production-plan-control-0042

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > plan [production_plan]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.3, o production plan é o controle mestre de toda atividade de scheduling durante um production period definido pelo usuário.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, o production plan é o controle mestre de toda atividade de scheduling durante um production period definido pelo usuário?*

---

### 35. hwa-10.2.3-symnew-archived-plan-0046

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > symphony [symphony_symnew]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.3, Symnew é um plano temporário intermediário substituído pelo production plan quando este começa, enquanto archived plan é uma cópia de um production plan antigo armazenada no banco.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, Symnew é um plano temporário intermediário substituído pelo production plan quando este começa, enquanto archived plan é uma cópia de um production plan antigo armazenada no banco?*

---

### 36. hwa-10.2.3-symphony-database-replication-0044

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.3 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: general_operations > symphony [symphony_replication]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.3, os dados do production plan são armazenados no arquivo Symphony e replicados no banco de dados; o Symphony é continuamente atualizado durante a produção.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, os dados do production plan são armazenados no arquivo Symphony e replicados no banco de dados; o Symphony é continuamente atualizado durante a produção?*

---

### 37. hwa-10.2.7-planman-resync-0051

**Escopo & Contexto:** `[Escopo: IBM Workload Scheduler 10.2.7 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Na documentação oficial do IBM Workload Scheduler 10.2.7, planman resync executado no master domain manager replica no banco todos os dados atualmente armazenados no Symphony; executá-lo no backup master que não está ativo não replica os dados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 38. hwa-10.2.8-awsbhv082e-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation Distributed 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
AWSBHV082E occurs when the Symphony and Symnew files have the same run number and cannot be merged. This is documented in the HCL Workload Automation 10.2.8 Troubleshooting page (awstrswitchplan3.html). A documented cause is running Stageman twice on the same Symnew file without resetting the plan or deleting the Symphony file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 39. hwa-10.2.8-backup-backup-master-data-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Windows and UNIX) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: general_operations > backup [backup_mdm]]`

**Regra Canônica / Evidência:**
HWA Distributed 10.2.8 recommends frequently backing up master data files to offline storage or a backup master domain manager.

**Plataforma / Validação:** Distributed; Windows and UNIX

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 recommends frequently backing up master data files to offline storage or a backup master domain manager?*

---

### 40. hwa-10.2.8-cal-job-stream-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > calendar [calendar_definition]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, um calendário criado pode ser adicionado a um job stream arrastando-o da aba Assets para o workspace do job stream no Graphical Designer e, em seguida, implantando (Deploy) o workspace.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um calendário criado pode ser adicionado a um job stream arrastando-o da aba Assets para o workspace do job stream no Graphical Designer e, em seguida, implantando (Deploy) o workspace?*

---

### 41. hwa-10.2.8-capacity-application-heap-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
A página de escalabilidade do HCL Workload Automation 10.2.8 documenta que, em ambientes com grande número de objetos de agendamento, há impacto em JnextPlan, em reporting e na implantação de event rules, e que a resolução costuma incluir aumentar o heap do application server e aumentar a capacidade máxima de log do DB2.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: A página de escalabilidade do HCL Workload Automation 10.2.8 documenta que, em ambientes com grande número de objetos de agendamento, há impacto em JnextPlan, em reporting e na implantação de event rules, e que a resolução costuma incluir aumentar o heap do application server e aumentar a capacidade máxima de log do DB2.?*

---

### 42. hwa-10.2.8-capacity-deployment-frequency-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
A opção global deploymentFrequency (df) no HCL Workload Automation 10.2.8, usada na gestão de event rules, define em minutos com que frequência as regras são verificadas para detectar mudanças a implantar, com valores válidos de 0 a 60, padrão 5 minutos; valor 0 desativa a implantação automática exigindo o comando planman deploy.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 43. hwa-10.2.8-capacity-en-event-driven-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > globalopts [globalopts_event_driven]]`

**Regra Canônica / Evidência:**
A opção global enEventDrivenWorkloadAutomation (ed) no HCL Workload Automation 10.2.8 habilita ou desabilita a funcionalidade de event-driven workload automation, com padrão yes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção global enEventDrivenWorkloadAutomation (ed) no HCL Workload Automation 10.2.8 habilita ou desabilita a funcionalidade de event-driven workload automation, com padrão yes?*
- *Qual o propósito e valor padrão da opção global enEventDrivenWorkloadAutomation no optman do HWA?*

---

### 44. hwa-10.2.8-capacity-jnext-plan-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não documenta um limite quantitativo específico de tamanho do arquivo Symphony/plano que indique quando executar JnextPlan ou arquivar.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 45. hwa-10.2.8-capacity-job-limit-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > capacity [capacity_limit_cpu]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 o limite de jobs pode ser definido de duas formas documentadas: na definição do job stream, usando o argumento job limit, ou na definição da workstation, usando o comando limit cpu; por exemplo, definir o limite de uma workstation em 25 permite no máximo 25 jobs rodando concorrentemente nela.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 o limite de jobs pode ser definido de duas formas documentadas: na definição do job stream, usando o argumento job limit, ou na definição da workstation, usando o comando limit cpu; por exemplo, definir o limite de uma workstation em 25 permite no máximo 25 jobs rodando concorrentemente nela?*

---

### 46. hwa-10.2.8-capacity-limit-cpu-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > capacity [capacity_workstation_limits]]`

**Regra Canônica / Evidência:**
O limite padrão documentado do número de jobs que podem rodar simultaneamente em uma workstation no HCL Workload Automation 10.2.8 é 1000 para cloud task launcher e 100 para todos os outros tipos de workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O limite padrão documentado do número de jobs que podem rodar simultaneamente em uma workstation no HCL Workload Automation 10.2.8 é 1000 para cloud task launcher e 100 para todos os outros tipos de workstation?*

---

### 47. hwa-10.2.8-capacity-limit-cpu-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'limit cpu' (lc) no HCL Workload Automation 10.2.8 altera o limite de jobs que podem rodar simultaneamente em uma workstation, com sintaxe {limit cpu | lc} [folder/]workstation;limit[;noask], em que limit aceita valores de 0 a 1024 ou a palavra system, e exige acesso limit à workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 48. hwa-10.2.8-capacity-limit-cpu-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, definir o comando conman limit cpu como 0 faz com que apenas jobs com prioridade hi e go sejam iniciados na workstation; definir como system remove o limite de jobs simultâneos, e para o extended agent o valor system define o limite de jobs como 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 49. hwa-10.2.8-capacity-limit-sched-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'limit sched' (ls) no HCL Workload Automation 10.2.8 altera o limite definido na definição de um job stream no plano, com sintaxe {limit sched | ls} jstreamselect;limit[;noask], em que limit aceita valores de 0 a 1024, e exige acesso limit ao job stream.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 50. hwa-10.2.8-capacity-oracle-tablespace-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > database [database_sizing]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não fornece uma fórmula quantitativa genérica de dimensionamento do banco de dados em função do número de jobs; apenas o exemplo Oracle 500000 jobs/dia com ~80GB .dbf.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não fornece uma fórmula quantitativa genérica de dimensionamento do banco de dados em função do número de jobs; apenas o exemplo Oracle 500000 jobs/dia com ~80GB?*

---

### 51. hwa-10.2.8-capacity-oracle-tablespace-size-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > database [database_sizing]]`

**Regra Canônica / Evidência:**
A documentação de performance do HCL Workload Automation 10.2.8 recomenda, para Oracle (RDBMS), alocar tamanho adequado de tablespace/datafile e, como exemplo, para uma carga de 500000 jobs por dia recomenda cerca de 80GB de tamanho de arquivo .dbf.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação de performance do HCL Workload Automation 10.2.8 recomenda, para Oracle (RDBMS), alocar tamanho adequado de tablespace/datafile e, como exemplo, para uma carga de 500000 jobs por dia recomenda cerca de 80GB de tamanho de arquivo?*

---

### 52. hwa-10.2.8-capacity-workstation-limit-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > globalopts [globalopts_workstationlimit]]`

**Regra Canônica / Evidência:**
Não há opção global documentada no HCL Workload Automation 10.2.8 chamada 'Number of submitted jobs' nem 'Limit of number of available workstations'; a opção documentada que controla limite de workstation é workstationLimit (wl).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Não há opção global documentada no HCL Workload Automation 10.2.8 chamada 'Number of submitted jobs' nem 'Limit of number of available workstations'; a opção documentada que controla limite de workstation é workstationLimit (wl)?*

---

### 53. hwa-10.2.8-cliauth-conman-composer-auth-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O acesso autenticado do cliente de linha de comando (conman/composer) ao master domain manager no HCL Workload Automation 10.2.8 é configurado por meio de parâmetros de conexão que podem ser fornecidos no comando, em arquivo de propriedades customizado, no useropts, no localopts ou no jobmanager.ini, usando autenticação por username/password ou por JWT.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 54. hwa-10.2.8-composer-notcommands-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os comandos 'resource' e 'submit' não existem no conjunto de comandos composer; a lista oficial de comandos composer documentada é: add, authenticate, chfolder, continue, create, delete, display, edit, exit, extract, help, list, listfolder, lock, mkfolder, modify, new, print, redo, rmfolder, rename, renamefolder, replace, system command, unlock, update, validate e version (resource e submit são comandos do conman).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 55. hwa-10.2.8-composer-resumecond-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
In HCL Workload Automation 10.2.8 Distributed, there is no verified evidence of a "resumecond" keyword (composer) or "resumecond" command (conman). The documented mechanisms to control resumption of SUPPR jobs/job streams are start conditions, conditional dependencies (FOLLOWS ... IF) and the conman rerun/release commands.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 56. hwa-10.2.8-configafter-post-install-config-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: general_operations > config [config_post_install]]`

**Regra Canônica / Evidência:**
Após a instalação do HCL Workload Automation 10.2.8, os componentes devem ser configurados seguindo o procedimento de configuração documentado, que inclui a definição de opções globais, locais e de usuário, além da configuração de autenticação e comunicação segura.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Após a instalação do HCL Workload Automation 10.2.8, os componentes devem ser configurados seguindo o procedimento de configuração documentado, que inclui a definição de opções globais, locais e de usuário, além da configuração de autenticação e comunicação segura?*

---

### 57. hwa-10.2.8-conman-altjob-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'altjob' (alias 'aj') modifica um job no plano antes de ele ser executado em HCL Workload Automation 10.2.8, com sintaxe {altjob|aj} jobselect [;streamlogon|logon=new_logon] [;docommand="new_command" | ;script="new_script"] [;noask]. Exige acesso de 'submit' ao job. Docommand e script são mutuamente exclusivos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 58. hwa-10.2.8-conman-at-absolute-0121

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o parametro at no submit sched e submit job aceita a opcao absolute ou abs para forcar interpretacao como tempo absoluto. Necessaria quando o master domain manager usa enLegacyStartOfDayEvaluation e enTimeZone=yes. Sem absolute o at pode ser rejeitado com AWSBHU141E.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU141E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU141E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 59. hwa-10.2.8-conman-eventrules-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, event rules sao criadas/desdobradas via composer create rule e gerenciadas por conman rule, suportando automacao event-driven. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 60. hwa-10.2.8-conman-fence-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando conman 'fence' (alias 'f') define o job fence de uma workstation: jobs não são lançados se suas prioridades forem menores ou iguais ao fence. Sintaxe: {fence | f} workstation ;pri [;noask]. Valores de pri: 0 a 99, hi, go ou system (system define o fence como zero). Requer acesso 'fence' à workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o comando conman fence para alterar o limite de execução em workstations no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 61. hwa-10.2.8-conman-jobman-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, o comando jobman gerencia acoes de jobs individuais; exemplos de acoes incluem jobman -refresh (atualizar status de jobs), jobman -stop (parar processamento de jobs), e selecao de opcoes de nivel de job. Status version_dependent (sintaxe exata pode variar por versao).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 62. hwa-10.2.8-conman-limitcpu-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o comando conman 'limit cpu' (alias 'lc') define o número máximo de jobs que podem rodar simultaneamente numa workstation. Sintaxe: {limit cpu | lc} [folder/]workstation ;limit [;noask]. Valores suportados: 0 a 1024 e system. limit 0 = apenas jobs com prioridade hi/go são lançados (para job stream READY); system = sem limite (para extended agent, system define o limite como 0). Requer acesso 'limit' à workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 63. hwa-10.2.8-conman-link-unlink-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, conman link (lk) abre links de comunicação entre workstations e exige acesso link; unlink fecha esses links e exige acesso unlink. Ambos aceitam wildcards, não são suportados em remote engine workstations e extended agents não são linkados porque se comunicam via host.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 64. hwa-10.2.8-conman-listsucc-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'listsucc' lista os sucessores de um job no plano em HCL Workload Automation 10.2.8, com sintaxe listsucc jobselect. Exige acesso de 'rerun' ao job e requer a replicação de dados do plano habilitada no banco de dados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 65. hwa-10.2.8-conman-mailman-logman-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, mailman e logman tratam mensageria e log de eventos de jobs/planos (notificacao e gerenciamento de logs). Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 66. hwa-10.2.8-conman-planman-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, o comando planman gerencia implantacao de planos e aplicacao de regras; inclui planman -suspend e planman -resume (suspender/retomar o plano de producao) e opcoes especificas de plano. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 67. hwa-10.2.8-conman-recovery-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, comandos de recovery do conman incluem recover, resetFTA e conman start/stop para recuperar ou reiniciar o ambiente de console/processamento de eventos. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 68. hwa-10.2.8-conman-release-sched-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'release sched' (alias 'rs') libera job streams de dependências no plano de produção do HCL Workload Automation 10.2.8, permitindo especificar o tipo de dependência (at, carryforward, deadline, follows, limit, needs, opens, priority, prompt, until) e usando ;noask para suprimir a confirmação. Requer acesso de 'release' ao job stream no security file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*

---

### 69. hwa-10.2.8-conman-reply-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'reply' (alias 'rep') responde a prompts de job ou job stream no plano em HCL Workload Automation 10.2.8, com sintaxe {reply|rep} {promptname | [workstation#]msgnum} ;reply [;noask]. Requer acesso de 'reply' ao prompt nomeado/global. Resposta Y satisfaz a dependência do prompt; N não a satisfaz e o prompt não é reemitido.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 70. hwa-10.2.8-conman-rerun-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Yes, with authorization. In HCL Workload Automation Distributed 10.2.8, conman rerun (rr) can rerun jobs in SUCC, FAIL, or ABEND state, requires rerun access to the job, and places the rerun job in the same job stream with the original dependencies. Confirm the target and approval before executing.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 71. hwa-10.2.8-conman-rerunsucc-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'rerunsucc' reexecuta um job e seus sucessores no plano em HCL Workload Automation 10.2.8, com sintaxe rerunsucc jobselect [;internal][;all]. Requer acesso de 'rerun' ao job e plan data replication habilitado. ;internal reexecuta apenas sucessores do mesmo job stream; ;all inclui sucessores em job streams externos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 72. hwa-10.2.8-conman-return-code-limit-0039

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, somente submit sched e submit job possuem códigos de retorno Conman específicos; os outros comandos retornam 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Quais comandos conman possuem códigos de retorno específicos documentados?*
- *Como o conman reporta return codes na submissão de schedules e jobs?*

---

### 73. hwa-10.2.8-conman-return-codes-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, o return code Conman 10 indica erro em submit sched e 11 indica erro em submit job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como o conman reporta return codes na submissão de schedules e jobs?*

---

### 74. hwa-10.2.8-conman-running-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O programa conman em HCL Workload Automation 10.2.8 pode ser executado em modo interativo ou em lote. Em lote, os comandos devem ser envolvidos em aspas duplas: conman "sj&sp" (executa sj e sp e sai), conman "sj&sp&" (mantém o prompt), conman cfile (lê comandos de arquivo) e cat cfile | conman (pipe). Parâmetros de conexão incluem -host, -port, -protocol, -proxy, -proxyport, -jwt, -username, -password, -timeout; e custom params -cf e -file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 75. hwa-10.2.8-conman-securityfile-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a segurança das interfaces de linha de comando (incluindo conman) é controlada pelo security file, onde se define para cada usuário quais objetos de agendamento pode acessar e quais ações pode executar. A opção global enListSecChk, quando yes, faz com que comandos de listagem como showdomain e showresources exijam acesso de 'list' ao objeto no security file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 76. hwa-10.2.8-conman-showcpus-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, conman sc (showcpus) lista workstations/CPUs do dominio; parte do conjunto de comandos de display do conman. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 77. hwa-10.2.8-conman-showdomain-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'showdomain' (aliases 'showdom', 'sd') exibe informações de domínio em HCL Workload Automation 10.2.8, com sintaxe {showdomain|showdom|sd} [domain] [;info] [;offline]. O default é o domínio onde o conman está rodando; wildcards são permitidos. Exige acesso de 'list' ao objeto se enListSecChk=yes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 78. hwa-10.2.8-conman-showresources-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'showresources' (alias 'sr') exibe informações sobre recursos no plano em HCL Workload Automation 10.2.8, com sintaxe {showresources|sr} [[folder/]workstation#][folder/]resourcename [;keys] [;offline] [;showid] ou [;deps[;keys|info|logon]]. Exige acesso de 'list' ao objeto se enListSecChk=yes. ;showid exibe identificador único de recurso.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 79. hwa-10.2.8-conman-start-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No. In HCL Workload Automation Distributed 10.2.8, conman start must not be issued while JnextPlan or stageman is running. It starts the production processes (except the event monitoring engine and Liberty) and requires start access; the shutdown command stops netman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 80. hwa-10.2.8-conman-startstop-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, conman start/stop e conman stopevtproc/startevtproc controlam inicio/parada do processamento e do event processor. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 81. hwa-10.2.8-conman-status-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
In HCL Workload Automation Distributed 10.2.8, conman status (stat) displays the conman banner and the production status, including Batchman LIVES, the workstation Limit and Fence, and the production plan mode (Def or Exp).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 82. hwa-10.2.8-conman-stop-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Não. No HCL Workload Automation Distributed 10.2.8, o conman start não deve ser emitido enquanto JnextPlan ou stageman estiver em execução. Ele inicia os processos de produção (exceto event monitoring engine e Liberty) e requer acesso start; o comando shutdown para o netman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 83. hwa-10.2.8-conman-submit-adhoc-into-joins-0118

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao submeter um job ad hoc com submit job = job sem ;into=stream, o job e adicionado ao job stream padrao JOBS do plano do dia corrente. Apos JnextPlan, o job que estava em JOBS do dia anterior cai para o dia seguinte, dando a impressao de que o job sumiu.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 84. hwa-10.2.8-conman-submit-at-nextday-0131

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao submeter job ad hoc com sbd ;at=HHMM, o job e agendado para a proxima ocorrencia valida no plano. Se o plano atual termina no dia seguinte (ex.: 08/23 02:59) e o horario especificado ja passou ou esta alem do horizonte, o job fica HOLD agendado para o dia seguinte (08/23). Isso confirma o comportamento documentado na Lacuna E: ad hoc sem into= vai para a instancia JOBS do plano e pode cair no dia seguinte.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 85. hwa-10.2.8-conman-submit-follows-hold-0134

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao submeter job ad hoc com sbd e o parametro follows=, o job entra em HOLD aguardando a dependencia ser satisfeita no plano de producao. Em laboratorio, sbd MDMDA#"cmd";alias=X;follows JOBS.AT_TEST_001 colocou o job em HOLD esperando AT_TEST_001 (HOLD ate 08/23), confirmando que a dependencia follows funciona no plano. O dataset ensina follows= corretamente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar mdm?*

---

### 86. hwa-10.2.8-conman-submit-into-multi-instance-0130

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao submeter job ad hoc com sbd ;into=STREAM, se existir mais de uma instancia da job stream no plano (ex.: JOBS com instancias de dias diferentes), o comando falha com AWSBHU152E 'There is more than one job stream instance with the given name'. A solucao e qualificar a instancia com a data/horario agendado: into=JOBS(0300 08/22). O dataset ensina into=reports sem mencionar a necessidade de desambiguar multiplas instancias.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU152E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU152E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 87. hwa-10.2.8-conman-submit-into-plan-0117

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, ao submeter um job ad hoc com submit job = job;into=stream, o job stream alvo deve ter uma instancia NO PLANO DE PRODUCAO ATUAL, nao apenas no banco de dados. Se o stream so existe como definicao, o job e aceito mas nao aparece em sj. Use submit sched = stream primeiro para criar a instancia no plano.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 88. hwa-10.2.8-conman-submit-job-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'submit job' (alias 'sbj') submete um job para lançamento no plano em HCL Workload Automation 10.2.8, com sintaxe {submit job= | sbj=} [workstation#][folder/]jobname [;alias[=name]] [;into=...] [;joboption] [;vartable=tablename] [;noask]. Exige acesso de 'submit' (submitdb) no security file e permite opções como at, deadline, follows, needs, opens, prompt, recovery, maxdur, mindur, every, até.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 89. hwa-10.2.8-conman-submit-until-deadline-0132

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, as keywords until= e deadline= na submissao ad-hoc sbd definem limites de tempo: until=HHMM limita o tempo maximo de execucao (o job deve terminar ate o horario), deadline=HHMM define o prazo final (com carryforward). Em laboratorio, sbd com until=1800 e deadline=1800 executaram imediatamente com SUCC RC=0, e o deadline exibiu nota <08/23 indicando carryforward. O dataset menciona until/deadline na sintaxe mas nao exemplifica o comportamento.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *Como definir limites de horário e prazo na submissão ad-hoc sbd do conman?*

---

### 90. hwa-10.2.8-conman-switcheventprocessor-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'switcheventprocessor' (alias 'switchevtp') alterna o servidor de processamento de eventos entre o master domain manager e o backup master (ou vice-versa) em HCL Workload Automation 10.2.8, com sintaxe {switcheventprocessor|switchevtp} [folder/]workstation (sem wildcards). Exige permissão start/stop em objetos cpu no security file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switcheventprocessor no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switcheventprocessor para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como utilizar o comando conman 'switcheventprocessor' para gerenciar workstations e execução no HWA?*

---

### 91. hwa-10.2.8-conman-tellop-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman 'tellop' (alias 'to') envia uma mensagem para o console do HCL Workload Automation 10.2.8, com sintaxe {tellop|to} [text] (até 900 caracteres). No master domain manager a mensagem é enviada a todos os workstations linkados; em um domain manager, aos agentes do seu domínio e subdomínios; em um workstation comum, somente ao seu domain manager. A mensagem só é exibida se o nível de console for maior que zero.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 92. hwa-10.2.8-dbviews-deps-0171

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [db_views_dependencies]]`

**Regra Canônica / Evidência:**
As views de dependencia do banco do HCL Workload Automation: JOB_DEPS_V (jobs/job streams que dependem de um job), JOB_STREAM_DEPS_V (jobs/job streams que dependem de um job stream), FILE_REFS_V (jobs/job streams que dependem de um arquivo), INTERNETWORK_DEPS_V (jobs/job streams que dependem de uma dependencia internetwork) e JOB_DEFINITION_REFS_V (job streams em que um job aparece). Usadas para consultar a teia de dependencias de um objeto (quem depende de quem). Fonte: IBM Workload Scheduler Database Views.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_STREAM_DEPS_V no HCL Workload Automation?*
- *Qual é o propósito da view de banco JOB_DEPS_V no HCL Workload Automation?*
- *Como consultar dependências e definições utilizando a view JOB_DEPS_V no banco de dados?*

---

### 93. hwa-10.2.8-dbviews-job-history-0168

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [db_views_job_history]]`

**Regra Canônica / Evidência:**
A view JOB_HISTORY_V do banco do HCL Workload Automation exibe informacoes sobre o historico de jobs (jobs executados e seus resultados). E a view principal para queries e reports de historico de execucao de jobs, incluindo campos como workstation, job name, start time e status. Usada em reports de producao (ex.: consultas com WHERE sobre Workstation_name, Job_name, Job_start_time). Fonte: IBM Workload Scheduler Database Views (JOB_HISTORY_V).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como consultar dependências e definições utilizando a view JOB_HISTORY_V no banco de dados?*
- *Qual é o propósito da view de banco JOB_HISTORY_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional JOB_HISTORY_V no banco de dados do HWA?*

---

### 94. hwa-10.2.8-dbviews-plan-jobs-0169

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [db_views_plan]]`

**Regra Canônica / Evidência:**
As views PLAN_JOBS_V e PLAN_JOB_STREAMS_V do banco do HCL Workload Automation exibem informacoes sobre os jobs e job streams no plano de producao corrente. As views PLAN_JOB_PREDECESSORS_V, PLAN_JOB_SUCCESSORS_V, PLAN_JOB_STREAM_PREDECESSORS_V e PLAN_JOB_STREAM_SUCCESSORS_V exibem os predecessores/sucessores de jobs e job streams no plano — usadas para consultas de dependencias e critical network. Fonte: IBM Workload Scheduler Database Views.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como consultar dependências e definições utilizando a view PLAN_JOB_SUCCESSORS_V no banco de dados?*
- *Como consultar dependências e definições utilizando a view PLAN_JOB_STREAMS_V no banco de dados?*
- *Qual é o propósito da view de banco PLAN_JOBS_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional PLAN_JOB_STREAMS_V no banco de dados do HWA?*

---

### 95. hwa-10.2.8-distributed-cli-api-key-jwt-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Sim. No HCL Workload Automation versão 10.2.8 (distributed): Em HCL Workload Automation 10.2.8, composer, conman, wappman e ocli podem autenticar por API Key (JSON Web Token) em vez de usuário e senha; o token pode ser informado com o parâmetro -jwt ou adicionado no arquivo useropts. Trata-se de autenticação; um token é dado sensível. Instruções de uso devem evitar expor o valor do token em texto claro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário wappman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wappman para gerenciar conman?*

---

### 96. hwa-10.2.8-dwc-apikey-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: dwc_api > authentication [authentication]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a autenticacao via API Key substitui usuario/senha para os comandos composer, conman, wappman e ocli: basta gerar uma API Key (Personal ou Service) e usa-la com o parametro -jwt ou no config.yaml, em vez de fornecer credenciais a cada execucao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar authentication?*
- *Como utilizar o utilitário wappman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wappman para gerenciar authentication?*

---

### 97. hwa-10.2.8-dwc-restv2-jwt-cli-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: dwc_api > authentication [authentication]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a autenticacao por API Key (JWT) pode ser usada nos comandos CLI (composer, conman, wappman, ocli) via parametro -jwt ou configuracao no useropts, dispensando usuario e senha. O config.yaml do ocli e atualizado automaticamente com a API Key.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar authentication?*
- *Como utilizar o utilitário wappman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wappman para gerenciar authentication?*

---

### 98. hwa-10.2.8-event-action-helper-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_processor]]`

**Regra Canônica / Evidência:**
O event processing server no HCL Workload Automation 10.2.8 recebe os eventos e verifica se eles correspondem a alguma event rule implantada; se houver correspondência, chama um action helper para executar as ações, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 recebe os eventos e verifica se eles correspondem a alguma event rule implantada; se houver correspondência, chama um action helper para executar as ações, conforme documentação oficial?*

---

### 99. hwa-10.2.8-event-correlation-rule-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_definition]]`

**Regra Canônica / Evidência:**
Ao definir uma event rule no HCL Workload Automation 10.2.8, especifica-se um ou mais eventos, uma regra de correlação (correlation rule) e uma ou mais ações acionadas pelos eventos, além de opcionalmente datas de validade, um intervalo diário de atividade e um fuso horário comum, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: Ao definir uma event rule no HCL Workload Automation 10.2.8, especifica-se um ou mais eventos, uma regra de correlação (correlation rule) e uma ou mais ações acionadas pelos eventos, além de opcionalmente datas de validade, um intervalo diário de atividade e um fuso horário comum, conforme documentação oficial?*

---

### 100. hwa-10.2.8-event-designer-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > event [event_rule_creation]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, a criação de event rules é feita no Workload Designer, dentro da área Designing your workload, na tarefa Creating an event rule, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, a criação de event rules é feita no Workload Designer, dentro da área Designing your workload, na tarefa Creating an event rule, conforme documentação oficial?*

---

### 101. hwa-10.2.8-event-domain-manager-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_processor]]`

**Regra Canônica / Evidência:**
O event processing server no HCL Workload Automation 10.2.8 inicia automaticamente com o master domain manager e apenas um event processor pode estar ativo na rede por vez, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 inicia automaticamente com o master domain manager e apenas um event processor pode estar ativo na rede por vez, conforme documentação oficial?*

---

### 102. hwa-10.2.8-event-en-event-driven-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > globalopts [globalopts_event_driven]]`

**Regra Canônica / Evidência:**
O valor da opção global enEventDrivenWorkloadAutomation no HCL Workload Automation 10.2.8 pode ser alterado a qualquer momento caso o usuário não queira usar a automação orientada a eventos em sua rede, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O valor da opção global enEventDrivenWorkloadAutomation no HCL Workload Automation 10.2.8 pode ser alterado a qualquer momento caso o usuário não queira usar a automação orientada a eventos em sua rede, conforme documentação oficial?*

---

### 103. hwa-10.2.8-event-event-rule-actions-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > event [event_rules_dwc]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule define um conjunto de ações que são executadas quando ocorrem condições de evento específicas, correlacionando eventos e acionando ações, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule define um conjunto de ações que são executadas quando ocorrem condições de evento específicas, correlacionando eventos e acionando ações, conforme documentação oficial?*

---

### 104. hwa-10.2.8-event-event-rule-definition-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_structure]]`

**Regra Canônica / Evidência:**
Uma event rule no HCL Workload Automation 10.2.8 é um objeto de agendamento que inclui os itens Events, Event-correlating conditions e Actions, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: Uma event rule no HCL Workload Automation 10.2.8 é um objeto de agendamento que inclui os itens Events, Event-correlating conditions e Actions, conforme documentação oficial?*

---

### 105. hwa-10.2.8-event-filter-rule-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_types]]`

**Regra Canônica / Evidência:**
As event rules no HCL Workload Automation 10.2.8 são classificadas em filter, sequence e set, com base em suas características, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: As event rules no HCL Workload Automation 10.2.8 são classificadas em filter, sequence e set, com base em suas características, conforme documentação oficial?*

---

### 106. hwa-10.2.8-event-not-draft-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_draft]]`

**Regra Canônica / Evidência:**
As definições de event rules no HCL Workload Automation 10.2.8 podem ser salvas como Draft (isDraft=yes, salvas no banco mas não prontas para implantação/ativação) ou como Not draft (isDraft=no, em processo de implantação ou prontas para serem implantadas e ativadas no ambiente de agendamento), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: As definições de event rules no HCL Workload Automation 10.2.8 podem ser salvas como Draft (isDraft=yes, salvas no banco mas não prontas para implantação/ativação) ou como Not draft (isDraft=no, em processo de implantação ou prontas para serem implantadas e ativadas no ambiente de agendamento), conforme documentação oficial?*

---

### 107. hwa-10.2.8-event-on-demand-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rules]]`

**Regra Canônica / Evidência:**
A automação orientada a eventos no HCL Workload Automation 10.2.8 permite definir regras (event rules) que podem acionar a automação de workload sob demanda, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: A automação orientada a eventos no HCL Workload Automation 10.2.8 permite definir regras (event rules) que podem acionar a automação de workload sob demanda, conforme documentação oficial?*

---

### 108. hwa-10.2.8-event-plan-based-job-scheduling-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_driven_automation]]`

**Regra Canônica / Evidência:**
A automação de workload orientada a eventos no HCL Workload Automation 10.2.8 adiciona a capacidade de executar automação de workload sob demanda, além do agendamento de jobs baseado em plano, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A automação de workload orientada a eventos no HCL Workload Automation 10.2.8 adiciona a capacidade de executar automação de workload sob demanda, além do agendamento de jobs baseado em plano, conforme documentação oficial?*

---

### 109. hwa-10.2.8-event-planman-deploy-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando planman deploy está disponível para implantar regras manualmente a qualquer momento, e planman deploy -scratch reduz o tempo de implantação quando um grande número de regras novas ou alteradas precisa ser implantado, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 110. hwa-10.2.8-event-planman-deploy-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
There is no conman command named "deployevtproc" documented in HCL Workload Automation 10.2.8. The documented deployment mechanism for event rules is setting isDraft="no" followed by the rule builder (deploymentFrequency default 5 min) or planman deploy/planman deploy -scratch.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 111. hwa-10.2.8-event-predefined-set-of-actions-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_sendevent]]`

**Regra Canônica / Evidência:**
O objetivo da automação orientada a eventos no HCL Workload Automation 10.2.8 é executar um conjunto predefinido de ações em resposta a eventos que ocorrem em nós que executam o HCL Workload Automation, inclusive em nós que não executam o HCL Workload Automation por meio do comando sendevent, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O objetivo da automação orientada a eventos no HCL Workload Automation 10.2.8 é executar um conjunto predefinido de ações em resposta a eventos que ocorrem em nós que executam o HCL Workload Automation, inclusive em nós que não executam o HCL Workload Automation por meio do comando sendevent, conforme documentação oficial?*

---

### 112. hwa-10.2.8-event-predefined-set-of-actions-0037

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > event [event_management]]`

**Regra Canônica / Evidência:**
O recurso event management no Dynamic Workload Console do HCL Workload Automation 10.2.8 permite lançar um conjunto predefinido de ações em resposta a eventos que ocorrem nos nós onde o HCL Workload Automation é executado, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O recurso event management no Dynamic Workload Console do HCL Workload Automation 10.2.8 permite lançar um conjunto predefinido de ações em resposta a eventos que ocorrem nos nós onde o HCL Workload Automation é executado, conforme documentação oficial?*

---

### 113. hwa-10.2.8-event-rule-name-0040

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_structure]]`

**Regra Canônica / Evidência:**
The official HCL Workload Automation 10.2.8 documentation does not describe a four-part event rule structure (event, actions, options, rule name). The documented structure is: events, event-correlating conditions, and actions (eventRule element with eventCondition + action).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: The official HCL Workload Automation 10.2.8 documentation does not describe a four-part event rule structure (event, actions, options, rule name)?*

---

### 114. hwa-10.2.8-event-run-command-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_generic_action]]`

**Regra Canônica / Evidência:**
A ação RunCommand do provider GenericAction no HCL Workload Automation 10.2.8 executa comandos que não são do HCL Workload Automation na mesma máquina onde o event processor é executado, e apenas o usuário TWS_user está autorizado a executá-la, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A ação RunCommand do provider GenericAction no HCL Workload Automation 10.2.8 executa comandos que não são do HCL Workload Automation na mesma máquina onde o event processor é executado, e apenas o usuário TWS_user está autorizado a executá-la, conforme documentação oficial?*

---

### 115. hwa-10.2.8-event-save-as-draft-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > event [event_rule_activation]]`

**Regra Canônica / Evidência:**
No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule é ativada e implantada desativando o seletor Save as draft e salvando novamente a regra, e a ativação pode ser verificada na tarefa Manage Event Rule, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule é ativada e implantada desativando o seletor Save as draft e salvando novamente a regra, e a ativação pode ser verificada na tarefa Manage Event Rule, conforme documentação oficial?*

---

### 116. hwa-10.2.8-event-showcpus-getmon-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O componente monman é instalado em cada agent do HCL Workload Automation 10.2.8, onde verifica eventos locais e os encaminha ao event processing server, sendo gerenciado pelos comandos conman deployconf, showcpus getmon, startmon e stopmon, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar os comandos showcpus e getmon no conman para monitorar estações e eventos?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 117. hwa-10.2.8-event-starteventprocessor-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Os comandos conman starteventprocessor, stopeventprocessor e switcheventprocessor são usados para gerenciar o event processing server no HCL Workload Automation 10.2.8, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switcheventprocessor no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switcheventprocessor para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 118. hwa-10.2.8-event-validity-period-0039

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > event [event_rule_lifecycle]]`

**Regra Canônica / Evidência:**
Uma event rule no HCL Workload Automation 10.2.8, quando implantada e sem atributos de validade ou intervalo de atividade especificados, permanece ativa perpetuamente em todos os momentos até ser alterada para o status de draft ou excluída do banco de dados, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: Uma event rule no HCL Workload Automation 10.2.8, quando implantada e sem atributos de validade ou intervalo de atividade especificados, permanece ativa perpetuamente em todos os momentos até ser alterada para o status de draft ou excluída do banco de dados, conforme documentação oficial?*

---

### 119. hwa-10.2.8-fence-conman-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, o comando conman fence (f) altera o job fence de uma workstation. Jobs não são iniciados se a prioridade for menor ou igual ao fence; o valor padrão após a instalação é zero e o comando requer acesso fence.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 120. hwa-10.2.8-globalopts-audithistory-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_audithistory]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global auditHistory (alias ah) tem valor '400' neste ambiente. auditHistory | ah Audit history period. Used in audit management. This setting applies only when the auditStore option is set to db . Enter the number of days for which you want to save audit record data. Audit records are discarded on a FI

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global auditHistory (alias ah) tem valor '400' neste ambiente?*

---

### 121. hwa-10.2.8-globalopts-carrystates-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_carrystates]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global carryStates (alias cs) configura quais estados são carregados (carry-forward) para o próximo ciclo de planejamento; neste ambiente está vazio (herdando o padrão de enCarryForward).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global carryStates (alias cs) configura quais estados são carregados (carry-forward) para o próximo ciclo de planejamento; neste ambiente está vazio (herdando o padrão de enCarryForward)?*

---

### 122. hwa-10.2.8-globalopts-companyname-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_companyname]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global companyName (alias cn) tem valor 'MYCOMPANY' neste ambiente. companyName | cn Company name. Specify the name of your company. The maximum length is 40 bytes. If the name contains spaces, enclose the name in double quotation marks ("). If you use the Japanese-Katakana language set, enclose the name wi

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global companyName (alias cn) tem valor 'MYCOMPANY' neste ambiente?*

---

### 123. hwa-10.2.8-globalopts-defaultwkslicensetype-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_defaultwkslicensetype]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global defaultWksLicenseType (alias wn) define o tipo de licença padrão usado pelos componentes Workload Scheduler quando não especificado por objeto; o valor PERSERVER (deste ambiente) licencia por servidor.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global defaultWksLicenseType (alias wn) define o tipo de licença padrão usado pelos componentes Workload Scheduler quando não especificado por objeto; o valor PERSERVER (deste ambiente) licencia por servidor?*
- *Qual o propósito e valor padrão da opção global defaultWksLicenseType no optman do HWA?*

---

### 124. hwa-10.2.8-globalopts-enadduser-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_enadduser]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enAddUser (alias au) tem valor 'YES' neste ambiente. enAddUser | au Enable the automatic user addition into the Symphony file. This option enables the automatic addition of a user into the Symphony file after you create or modify the user in the database. If you specify "yes", the user is aut

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enAddUser (alias au) tem valor 'YES' neste ambiente?*

---

### 125. hwa-10.2.8-globalopts-encarryforward-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_encarryforward]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enCarryForward (alias cf) habilita o carry-forward de jobs/estados não concluídos para o próximo plano de produção; o valor ALL (presente neste ambiente) carrega todos os estados elegíveis em vez de descartá-los ou reexecutá-los.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enCarryForward (alias cf) habilita o carry-forward de jobs/estados não concluídos para o próximo plano de produção; o valor ALL (presente neste ambiente) carrega todos os estados elegíveis em vez de descartá-los ou reexecutá-los?*

---

### 126. hwa-10.2.8-globalopts-encfinternetworkdeps-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_encfinternetworkdeps]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enCFInterNetworkDeps (alias ci) controla se dependências entre redes são consideradas nas decisões de carry-forward (ex.: cross-site/cross-network); neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enCFInterNetworkDeps (alias ci) controla se dependências entre redes são consideradas nas decisões de carry-forward (ex?*

---

### 127. hwa-10.2.8-globalopts-endbgetopsaudit-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_endbgetopsaudit]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enDbGetOpsAudit tem valor '1' neste ambiente. Habilita a auditoria de operações GET (leitura) no banco de dados; complementa enDbAudit. Neste ambiente é 1 (ligado).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enDbGetOpsAudit tem valor '1' neste ambiente?*
- *Qual o propósito e valor padrão da opção global enDbGetOpsAudit no optman do HWA?*

---

### 128. hwa-10.2.8-globalopts-enemptyschedsaresucc-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_enemptyschedsaresucc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enEmptySchedsAreSucc (alias es) tem valor 'NO' neste ambiente. enEmptySchedsAreSucc | es Job streams without jobs policy. Specify the behavior of job streams without any jobs. If set to yes , the job streams that contain no jobs are set to SUCC after their dependencies are resolved. If set to no , the 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enEmptySchedsAreSucc (alias es) tem valor 'NO' neste ambiente?*

---

### 129. hwa-10.2.8-globalopts-eneventdrivenworkloadautomationproxy-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_eneventdrivenworkloadautomationproxy]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enEventDrivenWorkloadAutomationProxy (alias pr) tem valor 'NO' neste ambiente. enEventDrivenWorkloadAutomationProxy | pr Enable event-driven workload automation proxy. Enable or disable the event-driven workload automation proxy feature. To enable, specify yes . To disable, specify no . The default value is no . Run J

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enEventDrivenWorkloadAutomationProxy (alias pr) tem valor 'NO' neste ambiente?*
- *Qual o propósito e valor padrão da opção global enEventDrivenWorkloadAutomationProxy no optman do HWA?*
- *Como configurar a opção global enEventDrivenWorkloadAutomationProxy no Master Domain Manager?*

---

### 130. hwa-10.2.8-globalopts-eneventprocessorhttpsprotocol-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_eneventprocessorhttpsprotocol]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enEventProcessorHttpsProtocol (alias eh) tem valor 'YES' neste ambiente. enEventProcessorHttpsProtocol | eh Enable event processor HTTPS protocol. Used in event rule management. Enables or disables the use of the HTTPS protocol to connect to the event processor server. To enable, enter yes . To disable, enter no

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enEventProcessorHttpsProtocol (alias eh) tem valor 'YES' neste ambiente?*
- *Qual o propósito e valor padrão da opção global enEventProcessorHttpsProtocol no optman do HWA?*

---

### 131. hwa-10.2.8-globalopts-enforecaststarttime-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_enforecaststarttime]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enForecastStartTime (alias st) tem valor 'NO' neste ambiente. enForecastStartTime | st Enable forecast start time. Only applicable when workload service assurance is enabled (see enWorkloadServiceAssurance ). Enter yes to enable the calculation of the predicted start time of each job when running a fo

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enForecastStartTime (alias st) tem valor 'NO' neste ambiente?*

---

### 132. hwa-10.2.8-globalopts-eninitialversionobjects-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_eninitialversionobjects]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enInitialVersionObjects (alias iv) tem valor 'NO' neste ambiente. Controla a criação de objetos de versão inicial (version objects) no plano; usado em ambientes com versioning de definições. Neste ambiente é NO (desligado).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enInitialVersionObjects (alias iv) tem valor 'NO' neste ambiente?*

---

### 133. hwa-10.2.8-globalopts-enlegacystartofdayevaluation-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_enlegacystartofdayevaluation]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enLegacyStartOfDayEvaluation (alias le) tem valor 'NO' neste ambiente. enLegacyStartOfDayEvaluation | le Evaluate start-of-day. Specify how the startOfDay option is to be managed across the HCL Workload Automation network. This is a legacy setting and should always be set to no starting from release 9.4.0 and 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global enLegacyStartOfDayEvaluation (alias le) tem valor 'NO' neste ambiente?*

---

### 134. hwa-10.2.8-globalopts-enwhatifanalysis-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_enwhatifanalysis]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enWhatIfAnalysis (alias wi) habilita a análise What-If, permitindo simular mudanças no plano sem afetar a execução em produção; neste ambiente está YES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enWhatIfAnalysis (alias wi) habilita a análise What-If, permitindo simular mudanças no plano sem afetar a execução em produção; neste ambiente está YES?*

---

### 135. hwa-10.2.8-globalopts-eventprocessoreifport-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_eventprocessoreifport]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global eventProcessorEIFPort (alias ee) tem valor '0' neste ambiente. eventProcessorEIFPort | ee Tivoli ® event integration facility port. Used in event rule management. Specify the port number where the event processor server receives events from the Tivoli ® Event Integration Facility (EIF). Valid values ar

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global eventProcessorEIFPort (alias ee) tem valor '0' neste ambiente?*
- *Qual o propósito e valor padrão da opção global eventProcessorEIFPort no optman do HWA?*

---

### 136. hwa-10.2.8-globalopts-folderdays-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_folderdays]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global folderDays (alias fd) define por quantos dias o histórico é retido dentro de pastas/grupos de planos e jobs, afetando limpeza e consultas históricas; neste ambiente é 10.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global folderDays (alias fd) define por quantos dias o histórico é retido dentro de pastas/grupos de planos e jobs, afetando limpeza e consultas históricas; neste ambiente é 10.?*

---

### 137. hwa-10.2.8-globalopts-licenseproxyserverport-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_licenseproxyserverport]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global licenseProxyServerPort (alias lo) tem valor '0' neste ambiente. licenseProxyServerPort | lo Port of the proxy server The port of the proxy server the master domain manager uses to connect to the Internet. This option is required if you are using a proxy server. The default value is null because it must 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global licenseProxyServerPort (alias lo) tem valor '0' neste ambiente?*
- *Qual o propósito e valor padrão da opção global licenseProxyServerPort no optman do HWA?*
- *Como configurar a opção global licenseProxyServerPort no Master Domain Manager?*

---

### 138. hwa-10.2.8-globalopts-mailsendername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_mailsendername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global mailSenderName (alias ms) tem valor 'TWS' neste ambiente. mailSenderName | ms Mail sender name. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify a string to be used as the sender of the emails. The default value is TWS . Change

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global mailSenderName (alias ms) tem valor 'TWS' neste ambiente?*
- *Qual o propósito e valor padrão da opção global mailSenderName no optman do HWA?*

---

### 139. hwa-10.2.8-globalopts-maxlen-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_maxlen]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global maxLen (alias xl) tem valor '14' neste ambiente. maxLen | xl Maximum preproduction plan length. Specify the maximum length of the preproduction plan in days after it is automatically extended or created. The value for maxLen must be greater than or equal to the value for minLen and must b

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global maxLen (alias xl) tem valor '14' neste ambiente?*

---

### 140. hwa-10.2.8-globalopts-minlen-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_minlen]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global minLen (alias ml) tem valor '8' neste ambiente. minLen | ml Minimum preproduction plan length. Specify the minimum length in days of the preproduction plan that can pass after the production plan is created or extended, without extending the preproduction plan. If the days left in the pr

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global minLen (alias ml) tem valor '8' neste ambiente?*

---

### 141. hwa-10.2.8-globalopts-notificationtimeout-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_notificationtimeout]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global notificationTimeout (alias nt) tem valor '5' neste ambiente. notificationTimeout | nt Notification timeout. Used in cross dependencies. Specify how many days HCL Workload Automation must retry sending notifications about job status changes to the remote engine if the notification fails. When this tim

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global notificationTimeout (alias nt) tem valor '5' neste ambiente?*

---

### 142. hwa-10.2.8-globalopts-sccdusername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_sccdusername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global sccdUserName tem valor 'wauser' neste ambiente. Usuário para autenticação na integração SCCM. Neste ambiente está vazio.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global sccdUserName tem valor 'wauser' neste ambiente?*

---

### 143. hwa-10.2.8-globalopts-smtpservername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_smtpservername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpServerName (alias sn) tem valor 'localhost' neste ambiente. smtpServerName | sn SMTP server name. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify the name of the SMTP server to be used by the mail plug-in. The default value is l

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpServerName (alias sn) tem valor 'localhost' neste ambiente?*

---

### 144. hwa-10.2.8-globalopts-smtpserverport-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_smtpserverport]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpServerPort (alias sp) tem valor '25' neste ambiente. smtpServerPort | sp SMTP Server port. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify the port number used to connect to the SMTP server by the mail plug-in. Valid valu

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpServerPort (alias sp) tem valor '25' neste ambiente?*
- *Qual o propósito e valor padrão da opção global smtpServerPort no optman do HWA?*

---

### 145. hwa-10.2.8-globalopts-smtpusername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_smtpusername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global smtpUserName (alias un) tem valor 'wauser' neste ambiente. smtpUserName | un SMTP server user name. Used in event rule management. If you deploy rules implementing an action that sends emails via an SMTP server, specify the SMTP server user name. The default value is the name of the HCL Workload Au

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global smtpUserName (alias un) tem valor 'wauser' neste ambiente?*

---

### 146. hwa-10.2.8-globalopts-tecservername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_tecservername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global TECServerName (alias th) tem valor 'localhost' neste ambiente. Nome do servidor Tivoli Enterprise Console (TEC) para onde eventos de workload são enviados; neste ambiente é 'localhost' (TEC local ou não integrado).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global TECServerName (alias th) tem valor 'localhost' neste ambiente?*
- *Qual o propósito e valor padrão da opção global TECServerName no optman do HWA?*

---

### 147. hwa-10.2.8-globalopts-tecserverport-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_tecserverport]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global TECServerPort (alias tp) tem valor '5529' neste ambiente. Porta do servidor Tivoli Enterprise Console (TEC) que recebe eventos; neste ambiente é 5529 (porta padrão do TEC).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global TECServerPort (alias tp) tem valor '5529' neste ambiente?*
- *Qual o propósito e valor padrão da opção global TECServerPort no optman do HWA?*

---

### 148. hwa-10.2.8-globalopts-untildays-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_untildays]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global untilDays (alias ud) tem valor '0' neste ambiente. untilDays | ud Remove obsolete job and job stream instances from the plan. If an until time (latest start time) has not been specified for a job or job stream, then the default until time is calculated adding the value of this option, expre

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o comportamento das opções until e deadline na submissão de jobs no conman?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global untilDays (alias ud) tem valor '0' neste ambiente?*

---

### 149. hwa-10.2.8-globalopts-useaesencryptionalgorithm-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_useaesencryptionalgorithm]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global useAESEncryptionAlgorithm tem valor 'YES' neste ambiente. Quando definido, usa o algoritmo de criptografia AES (mais forte) em vez do padrão para senhas/strings; complementa enStrEncrypt. Neste ambiente está vazio (usa padrão).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global useAESEncryptionAlgorithm tem valor 'YES' neste ambiente?*
- *Qual o propósito e valor padrão da opção global useAESEncryptionAlgorithm no optman do HWA?*

---

### 150. hwa-10.2.8-globalopts-zosservername-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_zosservername]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global zOSServerName (alias zs) tem valor 'localhost' neste ambiente. zOSServerName | zs HCL Workload Automation for Z connector server name . Used in event rule management. If you deploy rules implementing an action that submits job streams to the HCL Workload Automation for Z controller, specify the name or

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global zOSServerName (alias zs) tem valor 'localhost' neste ambiente?*

---

### 151. hwa-10.2.8-globalopts-zosserverport-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI optman (Opções Globais do Master) > Tópico: general_operations > globalopts [globalopts_zosserverport]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global zOSServerPort (alias zp) tem valor '31217' neste ambiente. zOSServerPort | zp HCL Workload Automation for Z connector server port . Used in event rule management. If you deploy rules implementing an action that submits job streams to the HCL Workload Automation for Z controller, specify the bootstr

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, a opção global zOSServerPort (alias zp) tem valor '31217' neste ambiente?*
- *Qual o propósito e valor padrão da opção global zOSServerPort no optman do HWA?*

---

### 152. hwa-10.2.8-govern-audit-files-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: general_operations > audit [audit_storage]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os arquivos de auditoria são nomeados yyyymmdd e criados nos diretórios <TWA_home>/TWS/audit/plan e <TWA_home>/TWS/audit/database no master domain manager e no backup master domain manager; quando auditStore=db, a tabela AUDIT_STORE_RECORDS_V é criada no banco de dados.

**Plataforma / Validação:** Distributed

---

### 153. hwa-10.2.8-govern-audit-who-changed-what-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > audit [audit_review]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, via Dynamic Workload Console administradores, operadores e schedulers podem revisar todas as alterações em objetos de agendamento no banco e no plano, descobrir qual usuário realizou uma alteração, e a data/hora da alteração; pode-se manter trilha de auditoria com o motivo da alteração e, opcionalmente, exigir justificativa para cada alteração.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, via Dynamic Workload Console administradores, operadores e schedulers podem revisar todas as alterações em objetos de agendamento no banco e no plano, descobrir qual usuário realizou uma alteração, e a data/hora da alteração; pode-se manter trilha de auditoria com o motivo da alteração e, opcionalmente, exigir justificativa para cada alteração?*

---

### 154. hwa-10.2.8-govern-auto-lock-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > govern [object_lock]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, no Dynamic Workload Console os objetos são bloqueados automaticamente enquanto um usuário os mantém abertos com o botão Edit (edição); objetos abertos apenas com View (visualização) não são bloqueados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, no Dynamic Workload Console os objetos são bloqueados automaticamente enquanto um usuário os mantém abertos com o botão Edit (edição); objetos abertos apenas com View (visualização) não são bloqueados?*

---

### 155. hwa-10.2.8-govern-draft-keyword-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a palavra-chave draft de uma definição de job stream marca o job stream como rascunho, fazendo com que ele NÃO seja adicionado ao preproduction plan; após remover a palavra-chave draft é preciso executar JnextPlan para que o job stream entre no preproduction plan e no production plan.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Como a palavra-chave draft impede que um job stream entre no plano de produção?*

---

### 156. hwa-10.2.8-govern-draft-undraft-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > govern [draft_status]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, pelo Dynamic Workload Console é possível definir um ou mais job streams como draft ou non-draft para controlar se eles são adicionados ao preproduction plan; essa ação requer acesso DRAFT ou MODIFY ao job stream.

**Plataforma / Validação:** Distributed

---

### 157. hwa-10.2.8-govern-en-db-audit-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > audit [audit_config]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a auditoria de banco de dados e de planos (enDbAudit e enPlanAudit) está habilitada por padrão e pode ser desabilitada via opções globais; a opção global auditStore define onde armazenar os registros de auditoria do banco de dados: em arquivo (file), no banco de dados (db) ou em ambos (both).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a auditoria de banco de dados e de planos (enDbAudit e enPlanAudit) está habilitada por padrão e pode ser desabilitada via opções globais; a opção global auditStore define onde armazenar os registros de auditoria do banco de dados: em arquivo (file), no banco de dados (db) ou em ambos (both)?*

---

### 158. hwa-10.2.8-govern-graphical-designer-deploy-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > govern [deploy_gd]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, no Graphical Designer do Dynamic Workload Console a ação Deploy salva no banco de dados os itens definidos no workspace; os itens só são gravados no banco quando o Deploy é concluído.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, no Graphical Designer do Dynamic Workload Console a ação Deploy salva no banco de dados os itens definidos no workspace; os itens só são gravados no banco quando o Deploy é concluído?*

---

### 159. hwa-10.2.8-govern-job-name-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_job]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o nome de um job deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 40 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de um job deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 40 caracteres?*

---

### 160. hwa-10.2.8-govern-job-stream-name-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_jobstream]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o nome de um job stream deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 16 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de um job stream deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 16 caracteres?*

---

### 161. hwa-10.2.8-govern-node-hostname-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_workstation]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para hostnames de workstation (atributo node) os caracteres válidos são alfanuméricos, incluindo hífen (-), e o comprimento máximo é de 51 caracteres.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para hostnames de workstation (atributo node) os caracteres válidos são alfanuméricos, incluindo hífen (-), e o comprimento máximo é de 51 caracteres?*

---

### 162. hwa-10.2.8-govern-pt-br-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_convention]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não prescreve um padrão organizacional de convenção de nomenclatura (ex.: para jobs, job streams ou workstations).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não prescreve um padrão organizacional de convenção de nomenclatura (ex?*

---

### 163. hwa-10.2.8-govern-pt-br-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > quality [sla_quality]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não prescreve SLAs (acordos de nível de serviço) operacionais.

**Plataforma / Validação:** Distributed

---

### 164. hwa-10.2.8-govern-pt-br-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > quality [sla_quality]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não prescreve métricas de qualidade (organizacionais) para o agendamento.

**Plataforma / Validação:** Distributed

---

### 165. hwa-10.2.8-govern-pt-br-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > change [change_management]]`

**Regra Canônica / Evidência:**
A documentação oficial do HCL Workload Automation 10.2.8 não prescreve uma política de mudanças padrão; a exigência de justificativa para mudanças é uma capacidade opcional configurável pelo administrador.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não prescreve uma política de mudanças padrão; a exigência de justificativa para mudanças é uma capacidade opcional configurável pelo administrador?*

---

### 166. hwa-10.2.8-govern-workstation-name-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > naming [naming_workstation]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o nome de uma workstation deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, pode ter no máximo 16 caracteres, deve ser único e não pode ser igual aos nomes de classes de workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de uma workstation deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, pode ter no máximo 16 caracteres, deve ser único e não pode ser igual aos nomes de classes de workstation?*

---

### 167. hwa-10.2.8-gui-conddep-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > gui [gui_join_dependency]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, uma condição de join agrega múltiplas dependências de diferentes predecessores em uma única dependência e libera o job sucessor quando o número mínimo configurado de dependências é satisfeito; se nenhum número mínimo for especificado, todas as dependências predecessoras devem ser satisfeitas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, uma condição de join agrega múltiplas dependências de diferentes predecessores em uma única dependência e libera o job sucessor quando o número mínimo configurado de dependências é satisfeito; se nenhum número mínimo for especificado, todas as dependências predecessoras devem ser satisfeitas?*

---

### 168. hwa-10.2.8-gui-jobdef-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > gui [gui_job_definition]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para criar uma definição de job executável pela Dynamic Workload Console, abre-se o Graphical Designer, na aba Assets clica-se no ícone +, seleciona-se Job definition, digita-se Executable na barra de busca, escolhe-se o tipo de job executável e clica-se em Next; em seguida configuram-se Workstation, Folder, Name e Task (por exemplo, Inline script) e informa-se o Command text or script name; o botão Add salva a definição de job no banco de dados.

**Plataforma / Validação:** Distributed

---

### 169. hwa-10.2.8-gui-jobdef-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > gui [gui_job_definition]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, um job em um job stream pode referenciar uma definição de job em vez de ser um job embutido; referenciar uma mesma definição de job em vários job streams evita duplicar a definição e permite que uma única alteração se propague a todos os job streams que a referenciam.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um job em um job stream pode referenciar uma definição de job em vez de ser um job embutido; referenciar uma mesma definição de job em vários job streams evita duplicar a definição e permite que uma única alteração se propague a todos os job streams que a referenciam?*

---

### 170. hwa-10.2.8-gui-trigger-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > gui [gui_run_cycle_trigger]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os triggers que podem ser associados a um job stream no Graphical Designer incluem o run cycle (dias/horas em que o job stream deve rodar) e o excluding run cycle (que prevalece sobre o run cycle e define quando o job stream não deve rodar); adicionalmente, desde 10.2.4, run cycle groups podem ser criados e atribuídos como triggers diretamente no Graphical Designer.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os triggers que podem ser associados a um job stream no Graphical Designer incluem o run cycle (dias/horas em que o job stream deve rodar) e o excluding run cycle (que prevalece sobre o run cycle e define quando o job stream não deve rodar); adicionalmente, desde 10.2.4, run cycle groups podem ser criados e atribuídos como triggers diretamente no Graphical Designer?*

---

### 171. hwa-10.2.8-incident-abend-recovery-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > abend [abend]]`

**Regra Canônica / Evidência:**
Sintoma: job terminou em ABEND. Resolucao: verificar o stdlist para o estado ABEND, consultar o schedlog/log do job para a causa, corrigir o problema (script, dependencia, recurso) e reexecutar com rerun (conman) ou release (rj) conforme a politica de recovery definida na job definition (RECOVERY STOP/RERUN).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar abend?*
- *O que causa e como solucionar o problema: job terminou em ABEND?*

---

### 172. hwa-10.2.8-incident-awsdeq024-e-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
A mensagem AWSDEQ024E no HCL Workload Automation 10.2.8 é recebida ao tentar efetuar login no conman em um sistema operacional Windows, com o texto 'Error owner is not of type user in TOKENUTILS.C;1178'. Causa documentada: uma variedade de causas relacionadas a usuários e permissões no servidor. Recuperação documentada: verificar a senha do usuário <TWS_user> (correta, conta não bloqueada, senha não expirada); assegurar que o serviço Tivoli Token Service (tokensrv) seja iniciado pelo usuário administrativo do HWA (não pela conta Local System) e atualizar a senha no serviço se ela mudou; verificar a propriedade dos arquivos (.exe e .dll em <TWA_home>\TWS\bin de <TWS_user>, .cmd de Administrator, corrigindo com setown -u e depois emitir StartUp, conman e 'link @!@;noask'); e conferir os direitos avançados do usuário (Act as part of the operating system, Adjust memory quotas, Log on as a batch job, Log on as a service, Log on locally, Replace a process level token, Impersonate a client after authentication).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEQ024 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEQ024 no HWA?*
- *Qual é o significado da mensagem de erro AWSDEQ024E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEQ024E no HWA?*
- *Qual é o significado da mensagem de erro AWSDEQ024E no HWA e qual ação é recomendada?*

---

### 173. hwa-10.2.8-incident-awsjcl070i-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCL070I ao carregar o Symphony. Causa: aviso informativo durante a sincronizacao banco/Symphony; pode indicar jobs que nao foram incluidos. Resolucao: verificar se a definicao do job existe no banco e se o JnextPlan foi executado apos alteracoes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL070I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL070I no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: AWSJCL070I ao carregar o Symphony?*

---

### 174. hwa-10.2.8-incident-awsjco135-w-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
A mensagem AWSJCO135W no HCL Workload Automation 10.2.8 é um aviso emitido quando o valor padrão é aplicado ao processamento de jobs críticos porque o produto perdeu a conexão com o seu banco de dados. Causa documentada: perda de conexão do HCL Workload Automation com o banco de dados, fazendo com que o valor padrão seja aplicado ao processamento de jobs críticos para as opções approachingLateOffset (al), deadlineOffset (do) e longDurationThreshold (ld), e a mensagem de aviso AWSJCO135W seja emitida para informar o que aconteceu. Recuperação documentada: a página documenta que alterações nessas opções se tornam efetivas ao executar JnextPlan ou reiniciar o WebSphere Application Server Liberty (stopappserver e startappserver), mas não prescreve uma recuperação específica para a perda de conexão do banco em si.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO135 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO135 no HWA?*
- *Qual é o significado da mensagem de erro AWSJCO135W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO135W no HWA?*
- *Qual é o significado da mensagem de erro AWSJCO135W no HWA e qual ação é recomendada?*

---

### 175. hwa-10.2.8-incident-awsjpl017-e-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
A mensagem AWSJPL017E no HCL Workload Automation 10.2.8 é emitida pelo JnextPlan quando o plano de produção não pode ser criado porque uma ação anterior no plano não foi concluída com sucesso ('The production plan cannot be created because a previous action on the production plan did not complete successfully. See the message help for more details.'). Causa documentada: um JnextPlan foi iniciado antes de o JnextPlan anterior ter executado o comando SwitchPlan. Recuperação documentada: resetar o plano com o comando 'ResetPlan -scratch'; se o reset indicar que o banco de dados está bloqueado, executar 'planman unlock'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL017 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017 no HWA?*

---

### 176. hwa-10.2.8-incident-bhu470i-0036

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > message [message]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU470I 'A startmon/stopmon command was issued for <ws>' ao executar conman startmon (startm) / stopmon (stopm) em uma workstation. Causa: mensagem informativa (nao erro) confirmando que o comando de iniciar/parar o monitoramento (monman) foi aceito e encaminhado para a workstation. Resolucao: nenhuma acao necessaria; a mensagem confirma a operacao. O lab confirmou: conman startm MDMDA;noask / conman stopm MDMDA;noask -> AWSBHU470I 'A startmon/stopmon command was issued for MDMDA' (2x, incl. restart).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU470I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU470I no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar message?*
- *O que causa e como solucionar o problema: AWSBHU470I 'A startmon/stopmon command was issued for <ws>' ao executar conman startmon (startm) / stopmon (stopm) em uma workstation?*

---

### 177. hwa-10.2.8-incident-bhu510e-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > syntax [syntax]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHU510E ao submeter job ad hoc com conman submit job (sbj) quando ja existe um job com o mesmo nome no plano. Causa: o nome do job (alias) ja esta em uso na job stream alvo. Resolucao: usar rerun (rr) para reexecutar o job existente, ou submeter com um alias diferente (alias=NOVO_NOME). O lab confirmou: sbj = MDMDA#R7JOB2;noask -> Submitted as MDMDA#JOBS.R7JOB2; duplicata -> AWSBHU510E 'job already exists, use rerun or alias'; com alias=R7JOB2B aceito. hold= NAO e keyword de sbj.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU510E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU510E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar syntax?*
- *O que causa e como solucionar o problema: AWSBHU510E ao submeter job ad hoc com conman submit job (sbj) quando ja existe um job com o mesmo nome no plano?*

---

### 178. hwa-10.2.8-incident-bhv082e-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSBHV082E durante SwitchPlan. Causa: falha na troca do plano de producao. Resolucao: seguir o troubleshooting de SwitchPlan (awstrswitchplan3.html), verificando consistencia do Symphony e do banco antes de repetir a operacao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: AWSBHV082E durante SwitchPlan?*

---

### 179. hwa-10.2.8-incident-checksync-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: banco e Symphony dessincronizados apos falha ou rollback. Resolucao: o processo CHECKSYNC (parte do FINAL) verifica a sincronizacao; se houver divergencia, usar planman resync ou os passos de 'Synchronizing the database with the Symphony file' do guia de troubleshooting.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar symphony?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: banco e Symphony dessincronizados apos falha ou rollback?*

---

### 180. hwa-10.2.8-incident-cli-raster-font-0097

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > cli [cli]]`

**Regra Canônica / Evidência:**
Sintoma: comandos da interface de linha de comando do HWA (conman, composer, etc.) apresentam problema de exibicao. Causa: a fonte default usada na janela do command prompt (Raster fonts). Resolucao: clicar no icone no canto superior esquerdo da janela, selecionar Properties, aba Font, mudar de Raster fonts para Lucida Console. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar cli?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar cli?*
- *O que causa e como solucionar o problema: comandos da interface de linha de comando do HWA (conman, composer, etc?*

---

### 181. hwa-10.2.8-incident-conman-nologin-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > connection [connection]]`

**Regra Canônica / Evidência:**
Sintoma: conman nao conecta ao master domain manager. Causa: problemas de rede, porta errada, ou autenticacao (credenciais/useropts). Resolucao: verificar useropts, conectividade com a porta do master, e certificados; no Windows, seguir o troubleshooting especifico de login.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar connection?*
- *O que causa e como solucionar o problema: conman nao conecta ao master domain manager?*

---

### 182. hwa-10.2.8-incident-conwinlog-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: conman nao consegue logar em workstation Windows. Causa: problemas de autenticacao/credenciais ou configuracao de login no Windows. Resolucao: verificar o arquivo de login e as credenciais da conta de servico; consultar troubleshooting de Conman em Windows (awstrconwinlog.html).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar windows?*
- *O que causa e como solucionar o problema: conman nao consegue logar em workstation Windows?*

---

### 183. hwa-10.2.8-incident-cscript-missing-0089

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > windows [windows]]`

**Regra Canônica / Evidência:**
Sintoma: em Windows, JnextPlan ou ResetPlan falham com 'cscript' is not recognized as an internal or external command, operable program or batch file. Causa: o utilitario cscript, que roda arquivos com extensao .vbs, nao esta instalado. Resolucao: instalar o utilitario cscript no Windows e reexecutar JnextPlan ou ResetPlan. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: em Windows, JnextPlan ou ResetPlan falham com 'cscript' is not recognized as an internal or external command, operable program or batch file?*
- *O que causa e como solucionar o problema: em Windows, JnextPlan ou ResetPlan falham com 'cscript' is not recognized as an internal or external command, operable program or batch file?*

---

### 184. hwa-10.2.8-incident-deploy-swap-space-0100

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > deploy [deploy]]`

**Regra Canônica / Evidência:**
Sintoma: ao usar planman deploy -scratch para deploy de todas as regras nao-draft, ocorre AWSJCS011E com 'ACTEX0023E The Active Correlation Technology compiler cannot communicate with the external Java compiler. java.io.IOException: Not enough space'. Causa: espaco de swap (memoria virtual) insuficiente para executar a operacao. Resolucao: criar mais espaco de swap ou aguardar menos processos ativos antes de tentar novamente. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCS011E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCS011E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar deploy?*
- *O que causa e como solucionar o problema: ao usar planman deploy -scratch para deploy de todas as regras nao-draft, ocorre AWSJCS011E com 'ACTEX0023E The Active Correlation Technology compiler cannot communicate with the external Java compiler?*

---

### 185. hwa-10.2.8-incident-deq024e-0050

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > security [security]]`

**Regra Canônica / Evidência:**
Sintoma: AWSDEQ024E ao efetuar login no conman em Windows — 'Error owner is not of type user in TOKENUTILS.C;1178'. Causa: problema de login/permissao relacionado a conta TWS_user — senha incorreta, conta bloqueada (lockout) ou expirada. Resolucao: (1) verificar se a senha do TWS_user esta correta e nao expirada; (2) verificar se a conta nao esta bloqueada; (3) checar credenciais e permissoes no lado do servidor; (4) corrigir o useropts se necessario. Pesquisa Perplexity (2026-08-23) confirma.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEQ024E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEQ024E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar security?*
- *O que causa e como solucionar o problema: AWSDEQ024E ao efetuar login no conman em Windows — 'Error owner is not of type user in TOKENUTILS?*

---

### 186. hwa-10.2.8-incident-event-rule-notrigger-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > events [events]]`

**Regra Canônica / Evidência:**
Sintoma: uma event rule foi criada, mas a acao requerida nao e disparada quando a condicao de evento e encontrada. Diagnostico (checklist oficial de 12 passos): (1) event management habilitado (optman ls, enEventDrivenWorkloadAutomation / ed = YES; se NO, optman chg ed=YES e JnextPlan -for 0000); (2) workstation habilitada para processamento de eventos (localopts 'can be event processor = yes'); (3) event processor instalado e rodando (conman showcpus; state MDE); (4) definicao da workstation no plano; (5) regra na configuracao de monitoramento (showcpus ;getmon); (6) regra ativa; (7) nova configuracao deployada (conman deploy); (8) deploy correto (mensagens DEPLOY do monman); (9) SSM agent rodando (regras FileMonitor); (10) eventos recebidos (SystemOut AWSEVP001I); (11) regra executada (AWSAHL004I); (12) problema de visualizacao no console. Fonte: HCL Troubleshooting Guide 10.2.8 (Troubleshooting an event rule that does not trigger the required action).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSEVP001I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSEVP001I no HWA?*
- *Qual é o significado da mensagem de erro AWSAHL004I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSAHL004I no HWA?*
- *O que causa e como solucionar o problema: uma event rule foi criada, mas a acao requerida nao e disparada quando a condicao de evento e encontrada?*

---

### 187. hwa-10.2.8-incident-ffdc-cleanup-0086

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > composer [composer]]`

**Regra Canônica / Evidência:**
Sintoma: sair da linha de comando do composer ou conman demora anormalmente em ambiente Windows. Causa: grande numero de arquivos nas pastas Conman-FFDC e Composer-FFDC. Resolucao: limpar as pastas Conman-FFDC e Composer-FFDC removendo os arquivos de trace localizados em stdlist/JM. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar composer?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar composer?*
- *O que causa e como solucionar o problema: sair da linha de comando do composer ou conman demora anormalmente em ambiente Windows?*

---

### 188. hwa-10.2.8-incident-jcs011e-oom-0068

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJCS011E 'An internal error has occurred. The error is the following: java.lang.OutOfMemoryError' durante a fase JnextPlan. Causa: os processos rodando no WebSphere Application Server Liberty Base durante o JnextPlan precisam de mais memoria virtual Java. Resolucao: aumentar o tamanho do heap Java default do Liberty Base (ver secao sobre aumentar application server heap size no Administration Guide). Fonte: HCL Troubleshooting Guide 10.2.8 (JnextPlan fails with a Java out-of-memory error).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCS011E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCS011E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: AWSJCS011E 'An internal error has occurred?*

---

### 189. hwa-10.2.8-incident-jdb801e-0046

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJDB801E ao executar JnextPlan/MakePlan ou operacoes de plano — erro generico de acesso ao banco. Causa: transaction log do banco cheio (DB2: aumentar capacidade maxima do log; Oracle: ajustar configuracoes de log/undo). Resolucao: (1) identificar o banco (DB2/Oracle); (2) aumentar a capacidade do transaction log (DB2: increase maximum log capacity; Oracle: ajustar redo/undo); (3) liberar espaco se necessario; (4) reexecutar a operacao de plano. Pesquisa Perplexity (2026-08-23): AWSJDB801E geralmente indica transaction log full que impede o JnextPlan de acessar o banco.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB801E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB801E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: AWSJDB801E ao executar JnextPlan/MakePlan ou operacoes de plano — erro generico de acesso ao banco?*

---

### 190. hwa-10.2.8-incident-jdb801e-locklist-0088

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > database [database]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJDB801E 'An internal error has been found while accessing the database' — JnextPlan falha com erro DB2 nullDSRA0010E. Causa: a memoria que o DB2 aloca para sua lock list e insuficiente. Resolucao: monitorar o valor da lock list entre as tarefas administrativas do DB2 (ver Administration Guide) e aumentar conforme necessario. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB801E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB801E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: AWSJDB801E 'An internal error has been found while accessing the database' — JnextPlan falha com erro DB2 nullDSRA0010E?*

---

### 191. hwa-10.2.8-incident-jnextplan-slow-0090

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: JnextPlan esta inaceitavelmente lento. Causa (3 possiveis): (1) tracing demais — reduzir os processos monitorados pelo tracing; (2) application server tracing demais; (3) outra causa relacionada a performance. Resolucao: reduzir o tracing (ver Quick reference: how to modify log and trace levels) e verificar o tracing do application server. Fonte: HCL Troubleshooting Guide 10.2.8 (JnextPlan is slow).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: JnextPlan esta inaceitavelmente lento?*
- *O que causa e como solucionar o problema: JnextPlan esta inaceitavelmente lento?*

---

### 192. hwa-10.2.8-incident-jnextplan-txlog-0054

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: JnextPlan falha com a mensagem de banco 'The transaction log for the database is full'. Causa: o numero de instancias de Job Scheduler que o JnextPlan precisa processar gera mais transacoes do que os arquivos de transaction log default suportam (DB2: ~180.000 instancias; Oracle: depende da configuracao). Resolucao: alterar os parametros de criacao dos arquivos de log para garantir mais espaco de log; possivelmente aumentar o heap Java no application server. Fonte: HCL Troubleshooting Guide 10.2.8, secao JnextPlan problems.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: JnextPlan falha com a mensagem de banco 'The transaction log for the database is full'?*
- *O que causa e como solucionar o problema: JnextPlan falha com a mensagem de banco 'The transaction log for the database is full'?*

---

### 193. hwa-10.2.8-incident-joblog-wildcard-0146

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > conman [conman]]`

**Regra Canônica / Evidência:**
Sintoma: o job log nao e exibido ao submeter conman sj;stdlist com wildcard no lugar do nome da workstation (ex.: %sj @#jobstreamA.jobA;stdlist). Causa: em um cenario onde um job stream foi cancelado e um request e feito para exibir o job log de um job definido naquele job stream, usando wildcard no lugar do nome da workstation, o job log nao pode ser exibido. Resolucao (workaround): evitar wildcard no lugar do nome da workstation ao requisitar o job log — usar o nome da CPU em vez disso. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *O que causa e como solucionar o problema: o job log nao e exibido ao submeter conman sj;stdlist com wildcard no lugar do nome da workstation (ex?*

---

### 194. hwa-10.2.8-incident-jpl006e-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJPL006E durante MakePlan. Causa: falha ao criar o plano de producao (ex.: problema de banco ou Symphony). Resolucao: consultar o guia de troubleshooting de MakePlan (awstrmakeplan6.html) e seguir os passos de recuperacao, incluindo ResetPlan -scratch se o plano ficar inconsistente.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL006E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL006E no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: AWSJPL006E durante MakePlan?*

---

### 195. hwa-10.2.8-incident-jpl017e-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully'. Causa: acao anterior no plano nao concluiu (ex.: JnextPlan interrompido). Resolucao: resetar o plano com ResetPlan -scratch e, se necessario, liberar o lock com planman unlock.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar plan?*
- *O que causa e como solucionar o problema: AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully'?*

---

### 196. hwa-10.2.8-incident-jpl017e-reset-0055

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Sintoma: JnextPlan falha com AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully' (pagina oficial: JnextPlan fails - AWSJPL017E). Causa: um JnextPlan foi lancado antes do JnextPlan anterior ter executado o comando SwitchPlan, deixando o plano em estado inconsistente; a situacao pode nao se resolver sozinha. Resolucao: (1) resetar o plano com ResetPlan -scratch; (2) se o reset mostrar database locked, executar planman unlock. Fonte: HCL Troubleshooting Guide 10.2.8 (JnextPlan fails - AWSJPL017E message).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar jnextplan?*
- *O que causa e como solucionar o problema: JnextPlan falha com AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully' (pagina oficial: JnextPlan fails - AWSJPL017E)?*

---

### 197. hwa-10.2.8-incident-jpl018e-0048

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJPL018E indicando database locked durante operacoes de plano (JnextPlan/planman). Causa: (1) operacao MakePlan anterior deixou um global lock pendente; (2) problema de autenticacao no useropts (erro de autorizacao); (3) lock manual na tabela via DB2 GUI/comando direto. Resolucao: (1) executar planman unlock para resetar o global lock; (2) verificar credenciais no useropts; (3) se lock manual no banco, liberar a tabela. Pesquisa Perplexity (2026-08-23) confirma as 3 causas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL018E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar plan?*
- *O que causa e como solucionar o problema: AWSJPL018E indicando database locked durante operacoes de plano (JnextPlan/planman)?*

---

### 198. hwa-10.2.8-incident-jpl704e-0059

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > makeplan [makeplan]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJPL704E 'An internal error has occurred. The planner is unable to extend the preproduction plan' quando o MakePlan roda. Causa: o MakePlan nao consegue estender o preproduction plan — causas raiz variadas (lock pendente de operacao anterior, problemas de banco, plano em estado inconsistente). Resolucao: investigar as causas raiz associadas (global lock set -> planman unlock; erro de banco; MakePlan anterior nao completou), tratar a causa e reexecutar o MakePlan. Fonte: HCL Troubleshooting Guide 10.2.8 (An internal error has occurred - AWSJPL704E).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL704E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL704E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar makeplan?*
- *O que causa e como solucionar o problema: AWSJPL704E 'An internal error has occurred?*

---

### 199. hwa-10.2.8-incident-jsy404e-0038

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: AWSJSY404E indica problema no processamento do arquivo Symphony (inacessível, locked ou corrompido/dessincronizado entre master e domain managers). Causa: Symphony inacessível ou bloqueado por outro processo, ou dados do Symphony corrompidos/dessincronizados entre o master domain manager e os agents/domain managers. Resolucao (procedimento oficial de troubleshooting): (1) parar o agent ou domain manager; (2) deletar o arquivo <TWA_home>/TWS/Symphony no agent/domain manager; (3) copiar o arquivo <TWA_home>/TWS/Sinfonia do master domain manager para <TWA_home>/TWS no agent; (4) emitir um link para o master domain manager original (envia o Symphony de volta); (5) verificar o tamanho do arquivo. Se o Symphony estiver locked por outro processo: parar todos os processos HWA e reexecutar stageman (e planman se necessario) para obter acesso exclusivo.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJSY404E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar symphony?*
- *Qual é o significado da mensagem de erro AWSJSY404E no HWA e qual ação é recomendada?*
- *O que causa e como solucionar o problema: AWSJSY404E indica problema no processamento do arquivo Symphony (inacessível, locked ou corrompido/dessincronizado entre master e domain managers)?*

---

### 200. hwa-10.2.8-incident-makeplan-lock-0056

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > makeplan [makeplan]]`

**Regra Canônica / Evidência:**
Sintoma: MakePlan falha ao iniciar. Causa: o global lock pode ter ficado em 'set' (nao resetado). Resolucao: (1) usar planman unlock para resetar o global lock; (2) reexecutar o job para recuperar — o preproduction plan e automaticamente reverificado e atualizado, e o Symnew e criado novamente. Como parar: parar o job pode NAO parar o processamento que ainda roda no Liberty Base ou no banco; forcar o fechamento da statement de banco se uma statement rodar tempo demais e causar abend no MakePlan; reiniciar o Liberty Base se necessario. Fonte: HCL Troubleshooting Guide 10.2.8 (MakePlan fails to start).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar makeplan?*
- *O que causa e como solucionar o problema: MakePlan falha ao iniciar?*

---

### 201. hwa-10.2.8-incident-makeplan-retry-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: MakePlan falha e o plano fica em estado inconsistente. Resolucao: aguardar a conclusao da acao anterior (ou usar planman unlock se pendente), verificar logs de MakePlan (awstrmakeplan6/7), e repetir o JnextPlan; em ultimo caso ResetPlan -scratch.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar plan?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: MakePlan falha e o plano fica em estado inconsistente?*

---

### 202. hwa-10.2.8-incident-max-40-deps-0118

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > dependencies [dependencies]]`

**Regra Canônica / Evidência:**
Sintoma: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta. Causa: a instancia de Job Scheduler ja tem o numero maximo (40) de dependencias definidas; normalmente um erro alertaria sobre o limite, mas a mensagem pode nao ser exibida se houver atraso na propagacao das atualizacoes do Symphony pela rede ou se a atualizacao coincidiu com atualizacoes de outros usuarios. Resolucao: reduzir o numero de dependencias para abaixo de 40. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta?*
- *O que causa e como solucionar o problema: uma dependencia adicionada a uma instancia de Job Scheduler nao aparece quando a lista de dependencias e reaberta?*

---

### 203. hwa-10.2.8-incident-mirroring-disabled-0144

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > console [console]]`

**Regra Canônica / Evidência:**
Sintoma: erro com com.ibm.tws.dao.plan.SymphonyJobStreamDAO.queryJobStreams ao usar o Dynamic Workload Console. Causa: a feature de plan data replication (tambem conhecida como mirroring) esta desabilitada no master domain manager. Resolucao (workaround): fazer log-out e log-in no Dynamic Workload Console. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 204. hwa-10.2.8-incident-mm-symphony-timeout-0075

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > network [network]]`

**Regra Canônica / Evidência:**
Sintoma: timeout durante o download do Symphony ao instalar um backup domain manager (AWSDEB003I 'Writing socket Resource temporarily unavailable'). Causa: no localopts do master domain manager, o timeout mm symphony download esta configurado com 0 minutos. Resolucao: corrigir configurando mm symphony download timeout para 1 minuto. Fonte: HCL Troubleshooting Guide 10.2.8 (Timeout during Symphony download).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEB003I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEB003I no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: timeout durante o download do Symphony ao instalar um backup domain manager (AWSDEB003I 'Writing socket Resource temporarily unavailable')?*

---

### 205. hwa-10.2.8-incident-planman-resync-symphony-0064

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > planman [planman]]`

**Regra Canônica / Evidência:**
Sintoma: dados do plano no banco nao atualizados em relacao ao Symphony. RECOVERY OFICIAL: rodar planman resync no master domain manager para atualizar o banco com a informacao mais recente do Symphony (se rodar no backup master quando nao esta atuando como master, os dados nao sao replicados). Nota: se o mirrorbox.msg (fila que sincroniza banco com Symphony) encher - ex.: banco indisponivel por periodo longo - um planman resync e emitido automaticamente para recarregar o plano no banco. Fonte: HCL Troubleshooting Guide 10.2.8 (Synchronizing the database with the Symphony file).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: dados do plano no banco nao atualizados em relacao ao Symphony?*

---

### 206. hwa-10.2.8-incident-planman-unlock-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: operacoes de plano falham com lock pendente (ex.: AWSJPL017E apos acao interrompida). Resolucao: usar planman unlock para liberar o lock do plano antes de tentar nova operacao.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar plan?*
- *O que causa e como solucionar o problema: operacoes de plano falham com lock pendente (ex?*

---

### 207. hwa-10.2.8-incident-question-marks-stdlist-0114

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > stdlist [stdlist]]`

**Regra Canônica / Evidência:**
Sintoma: mensagens nos logs ou traces contem '???' (question marks) para o record type e object. Causa: o processo que precisa escrever a mensagem de log nao consegue obter o nome do Job Scheduler — por exemplo, quando um Job Scheduler e dependente de um Job Scheduler que nao esta no plano atual (Symphony file); o processo escreve '???' no lugar do nome faltante. A mensagem contem o ID do Job Scheduler. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: mensagens nos logs ou traces contem '???' (question marks) para o record type e object?*
- *O que causa e como solucionar o problema: mensagens nos logs ou traces contem '???' (question marks) para o record type e object?*

---

### 208. hwa-10.2.8-incident-recovery-logman-resetplan-0061

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: Symphony corrompido no master e o procedimento com backup master domain manager nao pode ser executado. RECOVERY OFICIAL alternativo (logman + ResetPlan): (1) garantir processos parados (conman stop); (2) copiar a informacao do planman showinfo; (3) rodar ResetPlan (Symphony corrompido arquivado em schedlog); (4) rodar JnextPlan com -from = horario de inicio da primeira instancia de job stream incompleta (do planman showinfo) e -to = data fim do plano; so instancias incompletas entram no novo Symphony; (5) verificar o plano e status; (6) deletar instancias que nao se quer rodar; (7) aumentar o job limit das workstations (ResetPlan zera); (8) o Symphony e distribuido e a producao recomeca. Notas: status resetam para HOLD/READY; jobs SUCC rodam de novo; eventos UNTIL/DEADLINE/MAXDUR podem ser re-disparados; prompts nao sao recuperados. Fonte: HCL Troubleshooting Guide 10.2.8 (Recover using the logman and ResetPlan commands).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar symphony?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar symphony?*
- *O que causa e como solucionar o problema: Symphony corrompido no master e o procedimento com backup master domain manager nao pode ser executado?*

---

### 209. hwa-10.2.8-incident-resetplan-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > plan [plan]]`

**Regra Canônica / Evidência:**
Sintoma: plano de producao corrompido ou inconsistente (erros AWSJPL*). Resolucao: ResetPlan -scratch recria o plano a partir do banco, descartando o Symphony atual; e necessario rodar JnextPlan em seguida para regenerar o plano. Sempre fazer backup do Symphony antes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: plano de producao corrompido ou inconsistente (erros AWSJPL*)?*

---

### 210. hwa-10.2.8-incident-ssl-change-delete-symphony-0076

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > network [network]]`

**Regra Canônica / Evidência:**
Sintoma: apos mudanca do modo SSL entre uma workstation e seu domain manager, a workstation nao consegue relinkar. Causa: os arquivos Symphony e de mensagens na workstation ficam desatualizados/inconsistentes apos a mudanca de SSL. Resolucao: deletar o arquivo Symphony e os arquivos Sinfonia/message files na workstation apos a mudanca de modo SSL, para que os dados correspondam. Fonte: HCL Troubleshooting Guide 10.2.8 (After changing SSL mode, a workstation cannot link).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos mudanca do modo SSL entre uma workstation e seu domain manager, a workstation nao consegue relinkar?*
- *O que causa e como solucionar o problema: apos mudanca do modo SSL entre uma workstation e seu domain manager, a workstation nao consegue relinkar?*

---

### 211. hwa-10.2.8-incident-stats-jnextplan-frequency-0117

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > statistics [statistics]]`

**Regra Canônica / Evidência:**
Sintoma: job statistics nao sao atualizadas diariamente. Causa: job statistics sao atualizadas pelo JnextPlan; se o JnextPlan roda com frequencia menor que diaria, as statistics so sao atualizadas quando o JnextPlan roda. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: job statistics nao sao atualizadas diariamente?*
- *O que causa e como solucionar o problema: job statistics nao sao atualizadas diariamente?*

---

### 212. hwa-10.2.8-incident-stdlist-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > observability [observability]]`

**Regra Canônica / Evidência:**
Sintoma: necessidade de diagnosticar jobs sem executar ou com erro. Resolucao: o comando conman stdlist exibe a lista padrao (stdlist) de jobs com estado, e os logs (schedlog/stdlist files) mostram detalhes de execucao; consultar o guia de troubleshooting para localizar os arquivos de log por workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar observability?*
- *O que causa e como solucionar o problema: necessidade de diagnosticar jobs sem executar ou com erro?*

---

### 213. hwa-10.2.8-incident-switchplan-confirm-0057

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > switchplan [switchplan]]`

**Regra Canônica / Evidência:**
Sintoma: SwitchPlan falha ao iniciar, ou AWSJCL054E 'The command CONFIRM has failed' + AWSJPL016E 'An internal error has occurred. A global option confirm run member cannot be set' — indicando que a ultima etapa do SwitchPlan (planman confirm) falhou. Resolucao: (1) se planman confirm nao esta rodando: verificar os logs, rodar planman showinfo e reexecutar SwitchPlan; (2) se planman confirm falhou: rodar manualmente planman confirm e conman confirm; (3) se confirm ja rodou e a data fim do plano foi atualizada: rodar conman start. Se conman stop travar, matar o comando conman (pode impactar a distribuicao do plano). Fonte: HCL Troubleshooting Guide 10.2.8 (SwitchPlan problems).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL016E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL016E no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL054E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL054E no HWA?*
- *O que causa e como solucionar o problema: SwitchPlan falha ao iniciar, ou AWSJCL054E 'The command CONFIRM has failed' + AWSJPL016E 'An internal error has occurred?*

---

### 214. hwa-10.2.8-incident-symphony-corrupt-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: Symphony corrompido (erros ao ler o plano). Resolucao: o guia de troubleshooting cobre recovery de Symphony corrompido; os passos incluem parar o master, fazer backup, e usar ResetPlan -scratch + JnextPlan para regenerar o Symphony a partir do banco.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: Symphony corrompido (erros ao ler o plano)?*

---

### 215. hwa-10.2.8-incident-symphony-master-0060

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > symphony [symphony]]`

**Regra Canônica / Evidência:**
Sintoma: Symphony corrompido no master domain manager - shutdown de processos (especialmente batchman) com erros referentes ao Symphony no stdlist, ou mensagem especifica de corrupcao. Causa normal: file system cheio (evitar com monitoramento regular). RECOVERY OFICIAL (ordem estrita): (1) no backup master: switchmgr + verificar que assumiu como master; (2) do novo master, setar job limit=0 no master antigo (conman ou DWC) para impedir lancamento de jobs; (3) no master original: parar todos os processos HWA e renomear Sinfonia e Symphony corrompido; (4) no master atual: verificar link com todos os agents exceto o master antigo, verificar status dos jobs, e switchmgr de volta. Nota: informacao perdida - eventos suspensos no master durante a recuperacao. Fonte: HCL Troubleshooting Guide 10.2.8 (Corrupt Symphony recovery).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar symphony?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar symphony?*
- *O que causa e como solucionar o problema: Symphony corrompido no master domain manager - shutdown de processos (especialmente batchman) com erros referentes ao Symphony no stdlist, ou mensagem especifica de corrupcao?*

---

### 216. hwa-10.2.8-incident-timezone-liberty-0102

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > timezone [timezone]]`

**Regra Canônica / Evidência:**
Sintoma: planman showinfo exibe horarios inconsistentes (ex.: timezone da workstation GMT+2 mas o showinfo mostra outro horario). Causa: a Java virtual machine do WebSphere Application Server Liberty Base nao reconhece o timezone configurado no sistema operacional. Resolucao (workaround): setar o timezone definido no arquivo server.xml igual ao timezone definido para a workstation no banco do HWA: (1) parar o Liberty; (2) editar o server.xml; (3) reiniciar. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar timezone?*
- *O que causa e como solucionar o problema: planman showinfo exibe horarios inconsistentes (ex?*

---

### 217. hwa-10.2.8-incident-upgrade-config-merge-0125

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Sintoma: apos upgrade para versao 8.6, AWSBHU507I 'Killed A start command was issued' aparece. Causa: durante o upgrade, os arquivos de configuracao (tws_env.sh, tws_env.csh, jobmanrc, TWSCCLog.properties, StartUp, MakePlan, SwitchPlan, CreatePostReports, UpdateStats, ResetPlan, Sfinal) nao sao sobrescritos, mas a versao 8.6 deles e instalada sob tws_home/config. Resolucao: mesclar manualmente as duas versoes dos arquivos, modificando o arquivo sob tws_home. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU507I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU507I no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: apos upgrade para versao 8?*

---

### 218. hwa-10.2.8-incident-ws-no-link-hosts-0091

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > network [network]]`

**Regra Canônica / Evidência:**
Sintoma: uma workstation nao linka apos o JnextPlan em UNIX ou Windows. Causa: a workstation nao reconhece seu proprio endereco IP e hostname. Resolucao: adicionar o IP e hostname da workstation ao arquivo hosts (C:\Windows\System32\Drivers\etc\hosts em Windows ou /etc/hosts em UNIX) no formato: IPaddress hostname hostname.domain. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Sintoma: uma workstation nao linka apos o JnextPlan em UNIX ou Windows?*
- *O que causa e como solucionar o problema: uma workstation nao linka apos o JnextPlan em UNIX ou Windows?*

---

### 219. hwa-10.2.8-incident-zos-shadow-carryforward-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > planner [planner]]`

**Regra Canônica / Evidência:**
Sintoma: um z/OS shadow job definido no ambiente distributed, ligado com sucesso a um job z/OS remoto, nunca completa e e carregado indefinidamente (carried forward). Causa: uma operacao Refresh Current Plan executada na instancia remota HCL Workload Automation for Z scratcha o plano corrente, removendo o binding da instancia do job z/OS remoto. Resolucao: cancelar manualmente a instancia do z/OS shadow job no plano do engine distributed (ver o topico cancel job em 'Managing objects in the plan - conman' do User's Guide and Reference). Fonte: HCL Troubleshooting Guide 10.2.8 (A bound z/OS shadow job is carried forward indefinitely).

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar planner?*
- *O que causa e como solucionar o problema: um z/OS shadow job definido no ambiente distributed, ligado com sucesso a um job z/OS remoto, nunca completa e e carregado indefinidamente (carried forward)?*

---

### 220. hwa-10.2.8-install-backup-mdm-existing-db-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
O backup master domain manager do HCL Workload Automation 10.2.8 é configurado para apontar para o banco de dados já existente do master domain manager (compartilhando o mesmo banco, sem banco próprio separado) e, após a instalação, as chaves de criptografia devem ser copiadas da pasta TWA_DATA_DIR/ssl/aes do master domain manager para a pasta TWA_DATA_DIR/ssl/aes do backup master domain manager para que ele consiga descriptografar arquivos como o Symphony.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: O backup master domain manager do HCL Workload Automation 10.2.8 é configurado para apontar para o banco de dados já existente do master domain manager (compartilhando o mesmo banco, sem banco próprio separado) e, após a instalação, as chaves de criptografia devem ser copiadas da pasta TWA_DATA_DIR/ssl/aes do master domain manager para a pasta TWA_DATA_DIR/ssl/aes do backup master domain manager para que ele consiga descriptografar arquivos como o Symphony?*

---

### 221. hwa-10.2.8-install-jnextplan-after-backup-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Após instalar o backup master domain manager do HCL Workload Automation 10.2.8, pode-se executar opcionalmente o comando JnextPlan -for 0000 para estender em 0 horas e 0 minutos o plano de produção (Symphony) e adicionar ao plano a estação de trabalho recém-criada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 222. hwa-10.2.8-jnextplan-activation-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
JnextPlan moves the production plan from the old plan to a new Symphony file and activates it across the HWA network. Context: Generates the production plan and makes it available to all workstations in the network.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 223. hwa-10.2.8-jnextplan-architecture-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Modeling data/database, production plan, Symphony and JnextPlan are distinct artifacts and operational layers in HWA Distributed. Context: JnextPlan moves from the old production plan to a new Symphony and activates it across the network.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 224. hwa-10.2.8-jobsstate-ready-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > monitor [job_states]]`

**Regra Canônica / Evidência:**
Os estados de exibição de jobs incluem: READY (todas as dependências resolvidas, pronto para lançar), EXEC (em execução), WAIT (em espera), ABEND (terminou anormalmente) e SUCC (concluído com sucesso).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Os estados de exibição de jobs incluem: READY (todas as dependências resolvidas, pronto para lançar), EXEC (em execução), WAIT (em espera), ABEND (terminou anormalmente) e SUCC (concluído com sucesso)?*

---

### 225. hwa-10.2.8-jwtfile-jwt-token-location-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O arquivo .jwt_token usado pelos clientes de linha de comando (composer/conman/OCLI) do HCL Workload Automation é armazenado no diretório useropts do usuário; a localização exata não foi confirmada em página oficial 10.2.8 (fontes divergem entre user_home/.TWS/useropts e TWA_DATA_DIR/useropts/<user_id>).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 226. hwa-10.2.8-limit-cpu-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
In HCL Workload Automation Distributed 10.2.8, the default simultaneous job limit for a workstation after installation is zero and must be increased before any job can launch. The conman limit cpu (lc) command changes that value, from 0 to 1024 or system, and requires limit access.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar install?*

---

### 227. hwa-10.2.8-limitcpu-ready-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > capacity [capacity_limit_cpu]]`

**Regra Canônica / Evidência:**
limit cpu controla o número máximo de jobs executados simultaneamente em uma workstation; um job com dependências satisfeitas pode permanecer READY se o limite da workstation impedir a execução; uma workstation com limit cpu 0 bloqueia o início normal de jobs (apenas jobs hi/go executam).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: limit cpu controla o número máximo de jobs executados simultaneamente em uma workstation; um job com dependências satisfeitas pode permanecer READY se o limite da workstation impedir a execução; uma workstation com limit cpu 0 bloqueia o início normal de jobs (apenas jobs hi/go executam)?*

---

### 228. hwa-10.2.8-mdm-aes-keys-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Na instalação de BMDM HWA 10.2.8, a documentação exige as mesmas chaves de criptografia do MDM para descriptografar arquivos como Symphony e orienta copiar os arquivos da pasta ssl/aes do MDM para a pasta correspondente do BMDM.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Na instalação de BMDM HWA 10.2.8, a documentação exige as mesmas chaves de criptografia do MDM para descriptografar arquivos como Symphony e orienta copiar os arquivos da pasta ssl/aes do MDM para a pasta correspondente do BMDM?*

---

### 229. hwa-10.2.8-monitor-wappman-commands-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
The official wappman reference in HCL Workload Automation 10.2.8 documents only workflow application management commands: import, replace, delete, export, display, list. There are no report commands documented for wappman; reporting is handled by conman showjobs/showschedules/status and the report utility commands.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wappman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wappman para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 230. hwa-10.2.8-perf-engine-heap-sizing-0159

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > perfreport [perfreport_heap_sizing]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), o sizing do JVM heap do engine (WebSphere Application Server Liberty Base) e recomendado conforme o throughput de scheduling desejado (jobs/min): 1-50 jobs/min = 2 GB; 50-100 = 2.5 GB; 100-200 = 4 GB; acima de 200 = 6 GB. Alem do heap, considerar a memoria nativa do processo Java e dos processos do HWA: a RAM das maquinas onde o Liberty roda precisa ser entre 50% e 100% maior que o JVM max heap size. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.3 Memory).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), o sizing do JVM heap do engine (WebSphere Application Server Liberty Base) e recomendado conforme o throughput de scheduling desejado (jobs/min): 1-50 jobs/min = 2 GB; 50-100 = 2.5 GB; 100-200 = 4 GB; acima de 200 = 6 GB?*

---

### 231. hwa-10.2.8-perf-oracle-autoextend-0161

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > perfreport [perfreport_oracle_autoextend]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), para bancos Oracle e recomendavel habilitar a propriedade Datafile AUTOEXTEND (ON) dos datafiles, considerando que os settings e workload descritos causaram ocupacao de tablespace de cerca de 50 GB ou mais. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.3 Oracle database configuration).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), para bancos Oracle e recomendavel habilitar a propriedade Datafile AUTOEXTEND (ON) dos datafiles, considerando que os settings e workload descritos causaram ocupacao de tablespace de cerca de 50 GB ou mais?*

---

### 232. hwa-10.2.8-perf-sbs-mirrorbox-0165

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mirrorbox [mirrorbox]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2 (Performance Report oficial), o comando 'conman sbs' (ou chamadas REST equivalentes) adiciona um job stream ao plano on the fly. Se a rede do job stream adicionado e significativamente complexa (dependencias e cardinalidade), pode causar atraso geral no mecanismo de atualizacao do plano: por coerencia de scheduling, todas as atualizacoes iniciais passam pela main thread queue (mirrorbox.msg), ignorando o multithreading. A ordem de magnitude que causa esse queueing e de varias centenas de objetos (jobs nos job streams + dependencias internas e/ou externas). Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.3).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar mirrorbox?*

---

### 233. hwa-10.2.8-planman-reset-scratch-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, 'Planman reset -scratch' remove o preproduction plan mantendo o arquivo Symphony; o preproduction plan sera recriado com base nas informacoes de modelagem do banco na proxima geracao, incluindo todas as instancias de job stream no intervalo do plano; os passos sao: manter Symphony, atualizar estatisticas de jobs e descartar o preproduction plan; com -scratch, executar dbrunstats antes do JnextPlan.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 234. hwa-10.2.8-planman-showinfo-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, planman showinfo exibe informacoes do plano de producao atual, incluindo caminho de instalacao, inicio e fim do plano de producao, duracao apos ultima extensao, data/hora da ultima atualizacao (JnextPlan ou planman), fim do preproduction plan, inicio da primeira instancia de job stream nao concluida, run number (total de geracoes) e confirm run number; sintaxe 'planman [connection_parameters] showinfo' e roda no master domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 235. hwa-10.2.8-planman-showinfo-localopts-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
The planman showinfo command displays production plan timestamps formatted according to the localopts date format. Context: Displays information about the current production plan formatted using the dateformat configured in localopts.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 236. hwa-10.2.8-planman-unlock-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, planman unlock libera as entradas do banco que permanecem bloqueadas quando o processamento do plano termina de forma anormal; apenas usuarios com acesso build no tipo de arquivo prodsked (security file no master domain manager) podem executar; sintaxe 'planman [connection_parameters] unlock' e o comando roda no master domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 237. hwa-10.2.8-resetplan-scratch-option-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > resetplan [resetplan]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o script ResetPlan com a opcao -scratch descarta o plano de producao atual: arquiva o arquivo Symphony, apaga os dados do plano replicados no banco, atualiza as estatisticas de jobs e descarta tambem o preproduction plan; sem -scratch, ele reinicia (reset) o plano mantendo o preproduction plan e preservando as instancias de job stream que nao estavam COMPLETE; sintaxe 'ResetPlan [connection_parameters] [-scratch]', roda no master domain manager e cria um joblog em <TWS_INST_DIR>/TWS/stdlist/<DATE>.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 238. hwa-10.2.8-restocli-ocli-interface-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O Orchestration CLI (OCLI) é a nova interface de linha de comando do HCL Workload Automation 10.2.8 para executar jobs ou job streams e interagir com o servidor, sendo um aplicativo standalone que substitui o conman e se conecta configurando o arquivo config.yaml, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*

---

### 239. hwa-10.2.8-restv2-planfilter-0151

**Escopo & Contexto:** `[Escopo: HWA 10.2.8 (distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > plan_filter [plan_filter]]`

**Regra Canônica / Evidência:**
Na REST API V2 do HWA 10.2.8, o parametro 'plan_filter' de GET /twsd/api/v2/plan/job aceita sintaxe Conman-like para filtrar jobs do plano: 'plan_filter=/MDMDA#/' retorna os jobs da workstation MDMDA (count=224 no lab), e o wildcard oficial '/@/@#/@/@.@' retorna todos (count=236). Filtro de plano via parametro unico confirmado.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar plan_filter?*
- *Qual endpoint REST API V2 é utilizado para /twsd/api/v2/plan/job no HWA?*

---

### 240. hwa-10.2.8-restv2-rest-api-v2-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
A URL base da REST API v2 é https://<host>:<port>/twsd (porta HTTPS padrão 31116); a v2 é recomendada para novas integrações, com filtros planFilter (estilo conman) e OQL, e endpoints que operam por ID ou por filtro.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*

---

### 241. hwa-10.2.8-runbook-cancel-job-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > runbook [cancel_job]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando cancel job (cj) cancela um job: se cancelado antes de ser lançado, o job não é lançado; se cancelado depois de lançado, ele continua executando; e se um job em execução é cancelado e completa em estado ABEND, nenhuma tentativa automática de recuperação é feita para relançar o job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel job (cj) cancela um job: se cancelado antes de ser lançado, o job não é lançado; se cancelado depois de lançado, ele continua executando; e se um job em execução é cancelado e completa em estado ABEND, nenhuma tentativa automática de recuperação é feita para relançar o job?*

---

### 242. hwa-10.2.8-runbook-cancel-sched-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > runbook [cancel_jobstream]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando cancel sched (cs) cancela um job stream: se cancelado antes de iniciar, o job stream não executa; se cancelado após iniciar, os jobs já iniciados completam e os demais jobs do job stream são cancelados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel sched (cs) cancela um job stream: se cancelado antes de iniciar, o job stream não executa; se cancelado após iniciar, os jobs já iniciados completam e os demais jobs do job stream são cancelados?*

---

### 243. hwa-10.2.8-runbook-command-for-removal-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, não existe um comando conman 'suppress' para remover uma instância de job stream do plano; o estado SUPPR é um estado automático atribuído quando dependências condicionais de predecessores não são resolvidas, e o comando conman documentado para remover/parar uma instância de job stream é o cancel sched (cs).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 244. hwa-10.2.8-runbook-command-list-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a lista de comandos conman não inclui um comando 'suppress'; o comando documentado para cancelar um job stream no plano é 'cancel { job | sched }' (formas curtas cj | cs).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é a lista completa e inventário de comandos suportados no conman do HWA Distributed?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 245. hwa-10.2.8-runbook-conman-shutdown-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, para interromper todos os processos do HCL Workload Automation incluindo o WebSphere Application Server Liberty, usa-se conman shutdown seguido de stopAppServer (no UNIX) ou conman shutdown -appsrv / shutdown -appsrv (no Windows).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 246. hwa-10.2.8-runbook-conman-start-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando conman start inicia os processos de produção do HCL Workload Automation (exceto o motor de monitoramento de eventos e o WebSphere Application Server Liberty), e é usado no início de cada período de produção para reiniciar o HCL Workload Automation após o processamento de pré-produção.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 247. hwa-10.2.8-runbook-conman-start-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando conman start stlouis!@ inicia todas as workstations do domínio especificado, e um usuário executando conman no master domain manager pode iniciar qualquer workstation da rede.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 248. hwa-10.2.8-runbook-conman-stop-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando conman stop interrompe os processos de produção do HCL Workload Automation exceto os processos netman, monman, writer e appservman, e requer acesso de stop à workstation; para parar o netman, use o comando shutdown.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como utilizar o comando conman 'stop' para gerenciar workstations e execução no HWA?*

---

### 249. hwa-10.2.8-runbook-database-view-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [db_views_job_statistics]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V exibe informações sobre jobs e registra métricas de execução de job em milissegundos, incluindo Average_elapsed_time (tempo médio de execução), Total_elapsed_time (soma do tempo de CPU e tempo de espera), Last_elapsed_time, Max_elapsed_time e Min_elapsed_time.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?*
- *Qual é a estrutura e utilidade da view relacional JOB_STATISTICS_V no banco de dados do HWA?*

---

### 250. hwa-10.2.8-runbook-database-view-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [db_views_job_statistics]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V também registra contadores de execução de job, incluindo Successful_runs (número de execuções bem-sucedidas), Abended_runs (número de execuções anormais), Total_reruns (número total de reruns), Suppressed_runs, Late_start_runs e Late_end_runs.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?*

---

### 251. hwa-10.2.8-runbook-jnext-plan-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o script JnextPlan gerencia todo o processo de passar de um plano de produção (Symphony) antigo para um novo, incluindo sua ativação na rede; a cada execução do JnextPlan todas as workstations são paradas e reiniciadas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 252. hwa-10.2.8-runbook-jnext-plan-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção -for do JnextPlan especifica a extensão do plano em tempo, no formato [h]hh[:]mm (horas e minutos), e é mutuamente exclusiva com a opção -to; sem -to, -for ou -days, o comprimento padrão do plano de produção é de um dia.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção -for do JnextPlan especifica a extensão do plano em tempo, no formato [h]hh[:]mm (horas e minutos), e é mutuamente exclusiva com a opção -to; sem -to, -for ou -days, o comprimento padrão do plano de produção é de um dia?*

---

### 253. hwa-10.2.8-runbook-jnext-plan-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção -days n do JnextPlan especifica o número de dias para criar ou estender o plano de produção, e é mutuamente exclusiva com a opção -to.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção -days n do JnextPlan especifica o número de dias para criar ou estender o plano de produção, e é mutuamente exclusiva com a opção -to?*

---

### 254. hwa-10.2.8-runbook-jnext-plan-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o JnextPlan cria o arquivo de log (joblog) no diretório <TWS_INST_DIR>\TWS\stdlist\<DATE>, onde <TWS_INST_DIR> é o diretório de instalação e <DATE> é a data em que o script foi executado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o JnextPlan cria o arquivo de log (joblog) no diretório <TWS_INST_DIR>\TWS\stdlist\<DATE>, onde <TWS_INST_DIR> é o diretório de instalação e <DATE> é a data em que o script foi executado?*

---

### 255. hwa-10.2.8-runbook-jnext-plan-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o JnextPlan pode ser executado apenas a partir de um shell no master domain manager, pelo usuário TWS_user (se não desabilitado pelo security file) ou por root (UNIX)/Administrator (Windows), se não desabilitado pelas configurações do security file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 256. hwa-10.2.8-runbook-jnext-plan-for-0000-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando JnextPlan -for 0000 estende o plano de produção em 0 horas e 0 minutos e adiciona ao plano (Symphony) as definições recém-criadas de workstations, usuários e calendários do banco de dados, além de remover todas as instâncias de job streams concluídas com sucesso.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 257. hwa-10.2.8-runbook-release-job-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > runbook [release_dependency]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando release job remove a dependência somente para o job em progresso; quando o mesmo job é rerun, a dependência persiste, e para removê-la permanentemente do job stream é preciso usar o comando deldep job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando release job remove a dependência somente para o job em progresso; quando o mesmo job é rerun, a dependência persiste, e para removê-la permanentemente do job stream é preciso usar o comando deldep job?*

---

### 258. hwa-10.2.8-runbook-rerun-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > runbook [rerun_job]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção rerun ;from=[[folder/]wkstat#]job permite especificar uma definição de job no banco de dados cujo arquivo/comando será executado no lugar do job selecionado, e permite rerun de jobs em estado SUPPR desde que não pertençam a job streams cancelados ou suprimidos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção rerun ;from=[[folder/]wkstat#]job permite especificar uma definição de job no banco de dados cujo arquivo/comando será executado no lugar do job selecionado, e permite rerun de jobs em estado SUPPR desde que não pertençam a job streams cancelados ou suprimidos?*

---

### 259. hwa-10.2.8-sap-r3batch-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > password [password_encryption]]`

**Regra Canônica / Evidência:**
Não cole nem peça senhas reais. No HCL Workload Automation Distributed 10.2.8, o access method r3batch conecta o produto a sistemas SAP R/3 e as senhas de usuário SAP podem ser criptografadas com o utilitário enigma (em TWA_home/methods) antes de gravar nos arquivos r3batch.opts, gerando valores {aes}.... Execute isso no ambiente aprovado, nunca aqui na conversa.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Não cole nem peça senhas reais?*

---

### 260. hwa-10.2.8-sec-variable-table-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > security [variable_table_security]]`

**Regra Canônica / Evidência:**
There is no documented "secure variable" feature, confidentiality flag per variable, or per-variable encryption mechanism in HCL Workload Automation 10.2.8 Distributed. Variable tables should not be treated as secure secret stores.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: There is no documented "secure variable" feature, confidentiality flag per variable, or per-variable encryption mechanism in HCL Workload Automation 10.2.8 Distributed?*

---

### 261. hwa-10.2.8-sec-vartable-permissions-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > security [variable_table_security]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 o mapeamento de permissões de variable tables para variáveis internas é documentado: acesso 'modify' à tabela permite adicionar, deletar e modificar variáveis; 'display' permite exibir; 'unlock' permite desbloquear; e o acesso 'use' é necessário para referenciar a tabela a partir de job streams, run cycles e workstations.

**Plataforma / Validação:** Distributed

---

### 262. hwa-10.2.8-showjobs-rerun-options-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman sj (showjobs) exibe informações sobre jobs e seu status atual; a opção ;props inclui propriedades do job, como Rerun Options (opções de rerun) e Recovery Information (informações de recuperação).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 263. hwa-10.2.8-showjobs-wildcard-at-0112

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, o wildcard @ (arroba) no comando showjobs (sj) e em outros comandos conman que operam sobre jobs e job streams substitui um ou mais caracteres alfanumericos e e usado nas posicoes de workstation, job stream e job dentro do seletor. Combinado com o separador # (workstation) e . (ponto, entre job stream e job), o padrao `@#@.@` seleciona todos os jobs de todos os job streams de todas as workstations da pasta raiz. Outros wildcards incluem ? (um caractere alfanumerico) e % (um caractere numerico).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 264. hwa-10.2.8-startmon-stopmon-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Os comandos conman startmon (startm) e stopmon (stopm) iniciam e param o monman/event monitoring engine em uma workstation; o monitoring engine reinicia automaticamente na ativação do próximo production plan, a menos que a opção local autostart monman esteja desabilitada.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 265. hwa-10.2.8-startstop-command-start-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Os processos de um workstation do HCL Workload Automation 10.2.8 são iniciados e interrompidos pelos comandos conman startappserver e conman stopappserver, que gerenciam os servidores de aplicação (Liberty) dos componentes.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 266. hwa-10.2.8-status-production-plan-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman status (ou stat) exibe o banner do conman e o status de produção do HCL Workload Automation; na segunda linha de saída, após a palavra 'schedule', o modo do plano de produção (arquivo Symphony) é mostrado entre parênteses, onde Def significa plano em modo não expandido e Exp significa plano em modo expandido.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 267. hwa-10.2.8-trouble-awsbhv082e-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; planman) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o SwitchPlan pode falhar na inicializacao com AWSBHV082E quando o arquivo Symphony anterior e o Symnew tem o mesmo numero de run; a causa e um plano anterior/novo inconsistente, e a recuperacao documentada e: (1) confirmar que o planman confirm nao esta em execucao e verificar os logs, (2) executar planman showinfo, e (3) reexecutar o SwitchPlan.

**Plataforma / Validação:** distributed; planman

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 268. hwa-10.2.8-trouble-awsbin091e-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; monitoring) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a consulta de configuracao de monitoramento via REST (GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration) pode retornar AWSJSY404E com a causa AWSBIN091E 'The workstation does not support monitoring'; a causa e a workstation nao estar configurada/qualificada para monitoramento, e a recuperacao e verificar se o monman esta ativo na workstation (ex.: confirmar via conman showcpus que o flag M de monman esta presente) e revisar a configuracao de monitoramento da workstation antes de consultar.

**Plataforma / Validação:** distributed; monitoring

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJSY404E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?*
- *Qual é o significado da mensagem de erro AWSBIN091E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?*

---

### 269. hwa-10.2.8-trouble-awsdeq024e-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; conman (Windows)) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8 em Windows, a tentativa de login no conman retorna AWSDEQ024E 'Error owner is not of type user in TOKENUTILS.C'; a causa documentada e uma variedade de problemas relacionados a usuarios e permissoes no servidor; a recuperacao documentada inclui verificar (1) que a senha do <TWS_user> esteja correta, a conta nao esteja bloqueada e a senha nao tenha expirado, e (2) que o Tivoli Token Service (tokensrv) seja iniciado pelo usuario administrativo do HWA (nao pela conta Local System) nas propriedades do servico.

**Plataforma / Validação:** distributed; conman (Windows)

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSDEQ024E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSDEQ024E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 270. hwa-10.2.8-trouble-awsjdb801e-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; JnextPlan/DB2) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o JnextPlan pode falhar com a mensagem geral de acesso a banco de dados AWSJDB801E quando o numero de instancias de Job Scheduler que o JnextPlan precisa processar gera transacoes alem da capacidade dos arquivos de log de transacao do banco (em DB2 esse numero e 180.000 instancias; em Oracle depende da configuracao); a recuperacao documentada e alterar os parametros de criacao dos arquivos de log para gerar mais espaco de log e, se necessario, aumentar o heap do Java do application server.

**Plataforma / Validação:** distributed; JnextPlan/DB2

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJDB801E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJDB801E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 271. hwa-10.2.8-trouble-awsjom138e-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.7; 10.2.8 (distributed; conman/jobman) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a mensagem AWSJOM138E ocorre quando o numero total de dependencias manuais mais a dependencia interna do onoverlap excede 40 em uma definicao de job stream; a causa e a combinacao excessiva de dependencias manuais (com onoverlap enqueue), e a recuperacao e reduzir o numero de dependencias manuais da definicao do job stream (o limite de 39 dependencias manuais e a mensagem sao documentados apenas a partir da 10.2.7/10.2.8).

**Plataforma / Validação:** distributed; conman/jobman

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM138E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM138E no HWA?*
- *Qual é o significado da mensagem de erro AWSJOM138E no HWA e qual ação é recomendada?*

---

### 272. hwa-10.2.8-trouble-awsjpl017e-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; JnextPlan) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o JnextPlan falha com AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully'; a causa documentada e um JnextPlan iniciado antes de o JnextPlan anterior executar o comando SwitchPlan (acao anterior no plano nao concluida); a recuperacao documentada e (1) executar ResetPlan -scratch e (2) reexecutar o JnextPlan.

**Plataforma / Validação:** distributed; JnextPlan

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 273. hwa-10.2.8-trouble-awsjpl018e-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; JnextPlan/planman) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a mensagem AWSJPL018E indica que o banco de dados do engine esta bloqueado (database already locked) durante operacoes de plano (JnextPlan/planman); a causa e outro processo de gerenciamento de plano em execucao segurando o lock do banco, e a recuperacao e identificar e aguardar/limpar o processo concorrente (ex.: verificar se planman confirm ou JnextPlan ainda esta em execucao) antes de reexecutar a operacao de plano.

**Plataforma / Validação:** distributed; JnextPlan/planman

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL018E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual é o significado da mensagem de erro AWSJPL018E no HWA e qual ação é recomendada?*

---

### 274. hwa-10.2.8-tune-jm-promoted-nice-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_jm_promoted_nice]]`

**Regra Canônica / Evidência:**
A opção jm promoted nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 atribui o valor de prioridade a um job crítico que precisa ser promovido no workload service assurance, com padrão documentado de -1; a promoção é efetiva apenas com valores negativos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm promoted nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 atribui o valor de prioridade a um job crítico que precisa ser promovido no workload service assurance, com padrão documentado de -1; a promoção é efetiva apenas com valores negativos?*

---

### 275. hwa-10.2.8-tune-jm-promoted-priority-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_jm_promoted_priority]]`

**Regra Canônica / Evidência:**
A opção jm promoted priority, para sistemas Windows, no localopts do HCL Workload Automation 10.2.8 define a prioridade pela qual o sistema operacional processa um job crítico quando é promovido, com padrão documentado de AboveNormal.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção jm promoted priority, para sistemas Windows, no localopts do HCL Workload Automation 10.2.8 define a prioridade pela qual o sistema operacional processa um job crítico quando é promovido, com padrão documentado de AboveNormal?*

---

### 276. hwa-10.2.8-tune-limit-cpu-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > capacity [capacity_limit_cpu]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o limite (Limit) definido na definição de workstation, por exemplo com o comando limit cpu, estabelece o número máximo de jobs que o HCL Workload Automation pode lançar e manter em execução concorrentemente naquela workstation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o limite (Limit) definido na definição de workstation, por exemplo com o comando limit cpu, estabelece o número máximo de jobs que o HCL Workload Automation pode lançar e manter em execução concorrentemente naquela workstation?*

---

### 277. hwa-10.2.8-tune-logbufsz-0042

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: observability > log [log]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 documenta que, em ambientes com mais de 200.000 jobs, os seguintes parâmetros de configuração do DB2 são sugeridos quando o plano Symphony é replicado no banco de dados: LOGBUFSZ = 2150, DBHEAP = AUTOMATIC (ou maior que LOGBUFSZ), LOGFILSIZ = 3000, LOGPRIMARY = 200, LOGSECOND = 40 e PAGE_AGE_TRGT_MCR = 120.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 278. hwa-10.2.8-tune-mm-cache-size-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_mm_cache_size]]`

**Regra Canônica / Evidência:**
A opção mm cache size no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de mensagens em cache, quando mm cache mailbox está habilitado; segundo a referência de detalhes de localopts, o valor máximo (padrão) documentado é 512.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm cache size no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de mensagens em cache, quando mm cache mailbox está habilitado; segundo a referência de detalhes de localopts, o valor máximo (padrão) documentado é 512.?*

---

### 279. hwa-10.2.8-tune-mm-cache-size-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_mm_cache_size]]`

**Regra Canônica / Evidência:**
Segundo a página Mailbox caching do HCL Workload Automation 10.2.8, o valor padrão do parâmetro mm cache size é de 32 mensagens e o máximo é 512, aplicável quando mm cache mailbox está habilitado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Segundo a página Mailbox caching do HCL Workload Automation 10.2.8, o valor padrão do parâmetro mm cache size é de 32 mensagens e o máximo é 512, aplicável quando mm cache mailbox está habilitado?*

---

### 280. hwa-10.2.8-tune-mm-resolve-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_mm_resolve_master]]`

**Regra Canônica / Evidência:**
A opção mm resolve master no localopts do HCL Workload Automation 10.2.8 controla se a variável $MASTER é resolvida no início do dia de produção; desde a versão 9.5 Fix Pack 2 o padrão documentado é no.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção mm resolve master no localopts do HCL Workload Automation 10.2.8 controla se a variável $MASTER é resolvida no início do dia de produção; desde a versão 9.5 Fix Pack 2 o padrão documentado é no?*

---

### 281. hwa-10.2.8-tune-mm-sound-off-0036

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
A opção mm sound off no localopts do HCL Workload Automation 10.2.8 especifica como o Mailman responde ao comando conman tellop ?; quando yes, o Mailman exibe informações sobre cada tarefa que executa, com padrão documentado de no.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 282. hwa-10.2.8-tune-mo-sleep-0040

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > localopts [localopts_event_processor]]`

**Regra Canônica / Evidência:**
There is no "mo sleep" or event processor loop interval tuning option documented in the HCL Workload Automation 10.2.8 localopts reference. The documented event-related options are management options (can be event processor, autostart monman), not performance tuning.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: There is no "mo sleep" or event processor loop interval tuning option documented in the HCL Workload Automation 10.2.8 localopts reference?*

---

### 283. hwa-10.2.8-tune-pln-buffpool-0043

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > database [database_tuning]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 documenta que, para planos com mais de 200.000 jobs, deve-se aumentar o número de páginas (NPAGES) do buffer pool TWS_PLN_BUFFPOOL para 182000 e do TWS_BUFFPOOL para 50000 usando o comando ALTER BUFFERPOOL.

**Plataforma / Validação:** Distributed

---

### 284. hwa-10.2.8-tune-tuning-the-database-0041

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: general_operations > database [database_tuning]]`

**Regra Canônica / Evidência:**
O tópico Tuning the database do HCL Workload Automation 10.2.8 declara que o tuning do banco de dados requer etapas específicas que variam conforme o banco de dados e que informações detalhadas devem ser consultadas na documentação relevante do produto de banco de dados; não fornece recomendações quantitativas próprias nesta página.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O tópico Tuning the database do HCL Workload Automation 10.2.8 declara que o tuning do banco de dados requer etapas específicas que variam conforme o banco de dados e que informações detalhadas devem ser consultadas na documentação relevante do produto de banco de dados; não fornece recomendações quantitativas próprias nesta página?*

---

### 285. hwa-10.2.8-useropts-useropts-connection-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O arquivo useropts do HCL Workload Automation 10.2.8 fica no diretório user_home/.TWS do usuário e armazena parâmetros de conexão específicos do usuário para o cliente de linha de comando (conman/composer). A autenticação pode usar username/password ou JWT, e o parâmetro JWT sempre tem precedência sobre username e password.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 286. hwa-10.2.8-vm-9f-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > syntax [join_syntax]]`

**Regra Canônica / Evidência:**
O bloco JOIN (join <name> <n|ALL> of description "..." ... endjoin, com follows <pred> if <cond>) é suportado na definição de job stream do HCL Workload Automation Distributed tanto na 10.2.0 quanto na 10.2.8, com sintaxe e semântica idênticas.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O bloco JOIN (join <name> <n|ALL> of description "?*

---

### 287. hwa-10.2.8-vm-9f-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > syntax [conditional_dependency]]`

**Regra Canônica / Evidência:**
A dependência condicional IF (follows <ws>#<stream>.<job> if <condition>) é suportada na definição de job stream do HCL Workload Automation Distributed na 10.2.0 e 10.2.8. A documentação oficial 10.2.8 lista como condições de status para jobs: FAIL, ABEND, SUCC e SUPPR; o status EXEC não consta da lista oficial de condições de dependência.

**Plataforma / Validação:** Distributed

---

### 288. hwa-10.2.8-vm-9f-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
O comando conman limit cpu ({limit cpu|lc} [folder/]workstation;limit[;noask]) aceita valores de 0 a 1024 e system, e o comando fence ({fence|f} workstation;pri) aceita 0-99, hi, go e system, de forma idêntica no HCL Workload Automation Distributed 10.2.0 e 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 289. hwa-10.2.8-vm-component-terminology-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation multi (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
A terminologia de componentes do produto distribuído (master domain manager/MDM, domain manager/DM, fault-tolerant agent/FTA, dynamic domain manager/DDM, Dynamic Workload Console/DWC) é consistente entre as marcas TWS, IWS e HWA, e o conman é o programa de linha de comando que gerencia o plano de produção, executável a partir do master domain manager e de qualquer fault-tolerant agent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar mdm?*

---

### 290. hwa-10.2.8-vm-en-retain-name-on-rerun-from-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
A opção global enRetainNameOnRerunFrom do HCL Workload Automation (conman rerun) foi descontinuada a partir da versão 10.1: a partir dela não é mais suportada e é forçada para o valor no, devendo permanecer sem modificação.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 291. hwa-10.2.8-vm-en-retain-name-on-rerun-from-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Na versão 9.5 do IBM/HCL Workload Automation, enRetainNameOnRerunFrom ainda era uma opção ativa (sem nota de deprecation), com valor padrão no: definir yes fazia os jobs reexecutados com o comando conman rerun manterem o nome original do job.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 292. hwa-10.2.8-vm-en-retain-name-on-rerun-from-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > globalopts [globalopts_retain_name_rerun]]`

**Regra Canônica / Evidência:**
Na versão 10.2.8 do HCL Workload Automation, enRetainNameOnRerunFrom permanece deprecated (desde 10.1), com valor padrão no, fazendo com que jobs reexecutados recebam o nome do rerun from em vez do nome original; a documentação não informa uma opção substituta.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na versão 10.2.8 do HCL Workload Automation, enRetainNameOnRerunFrom permanece deprecated (desde 10.1), com valor padrão no, fazendo com que jobs reexecutados recebam o nome do rerun from em vez do nome original; a documentação não informa uma opção substituta?*

---

### 293. hwa-10.2.8-vm-ispf-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (z/OS) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI conman (Monitoramento e Plano) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
A interface de operação do HCL Workload Automation for Z (z/OS) é o diálogo ISPF (invocado pela CLIST de amostra EQQOPCAC ou pelo menu ISPF), e a documentação z/OS (Planning and Installation, Managing the Workload, Driving HCL Workload Automation for Z) não documenta os comandos conman nem o OCLI, que pertencem à documentação distribuída.

**Plataforma / Validação:** z/OS

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar install?*

---

### 294. hwa-10.2.8-vm-linhagem-de-marca-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation multi (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > version [version_history]]`

**Regra Canônica / Evidência:**
A linhagem de marcas do produto distribuído é: Tivoli Workload Scheduler 8.5 -> IBM Workload Scheduler 9.x (ex.: 9.5) -> HCL Workload Automation 10.1 -> HCL Workload Automation 10.2.x (10.2.8), sendo a versão 10.2.x sucessora da linha IBM 10.2 e da linha TWS/IWS 9.x e 8.5.x.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A linhagem de marcas do produto distribuído é: Tivoli Workload Scheduler 8.5 -> IBM Workload Scheduler 9.x (ex?*

---

### 295. hwa-10.2.8-vm-scheduler-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 8.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > version [version_history]]`

**Regra Canônica / Evidência:**
O produto distribuído IBM era chamado Tivoli Workload Scheduler (TWS) nas versões 8.x e ainda na 9.1 (nota oficial 'Release Notes for Tivoli Workload Scheduler, version 9.1'), passando a ser documentado como IBM Workload Scheduler na versão 9.5 (título 'IBM Workload Scheduler Version 9.5 Release Notes').

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O produto distribuído IBM era chamado Tivoli Workload Scheduler (TWS) nas versões 8.x e ainda na 9.1 (nota oficial 'Release Notes for Tivoli Workload Scheduler, version 9.1'), passando a ser documentado como IBM Workload Scheduler na versão 9.5 (título 'IBM Workload Scheduler Version 9.5 Release Notes')?*

---

### 296. hwa-10.2.8-wsa-approaching-late-offset-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global approachingLateOffset (abreviação al) determina o intervalo de tempo antes do critical start time a partir do qual um trabalho da rede crítica que ainda não iniciou é alertado como risco potencial, sendo adicionado à hot list; o padrão é 120 segundos e o valor é verificado regularmente, sem necessidade de executar JnextPlan para as mudanças entrarem em vigor, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global approachingLateOffset (abreviação al) determina o intervalo de tempo antes do critical start time a partir do qual um trabalho da rede crítica que ainda não iniciou é alertado como risco potencial, sendo adicionado à hot list; o padrão é 120 segundos e o valor é verificado regularmente, sem necessidade de executar JnextPlan para as mudanças entrarem em vigor, conforme documentação oficial?*
- *Qual o propósito e valor padrão da opção global approachingLateOffset no optman do HWA?*

---

### 297. hwa-10.2.8-wsa-critical-start-dates-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, no cenário documentado de Workload Service Assurance, ao executar JnextPlan são calculadas as datas de início crítico do trabalho crítico e de todos os trabalhos identificados como seus predecessores, e um trabalho que atrasa pode ser promovido automaticamente para receber maior prioridade de submissão e recursos de sistema, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, no cenário documentado de Workload Service Assurance, ao executar JnextPlan são calculadas as datas de início crítico do trabalho crítico e de todos os trabalhos identificados como seus predecessores, e um trabalho que atrasa pode ser promovido automaticamente para receber maior prioridade de submissão e recursos de sistema, conforme documentação oficial?*

---

### 298. hwa-10.2.8-wsa-en-service-assurance-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_enable]]`

**Regra Canônica / Evidência:**
O Workload Service Assurance do HCL Workload Automation 10.2.8 é habilitado/desabilitado pela opção global enWorkloadServiceAssurance (abreviação wa), que está habilitada por padrão (YES), conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O Workload Service Assurance do HCL Workload Automation 10.2.8 é habilitado/desabilitado pela opção global enWorkloadServiceAssurance (abreviação wa), que está habilitada por padrão (YES), conforme documentação oficial?*

---

### 299. hwa-10.2.8-wsa-estimated-duration-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_estimated_duration]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a duração estimada (estimated duration) de um trabalho é baseada nas estatísticas coletadas de execuções anteriores do trabalho, o que afeta a precisão dos tempos calculados para redes críticas que incluem trabalhos executados pela primeira vez; para um shadow job, a duração estimada é sempre o valor padrão de um minuto, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a duração estimada (estimated duration) de um trabalho é baseada nas estatísticas coletadas de execuções anteriores do trabalho, o que afeta a precisão dos tempos calculados para redes críticas que incluem trabalhos executados pela primeira vez; para um shadow job, a duração estimada é sempre o valor padrão de um minuto, conforme documentação oficial?*

---

### 300. hwa-10.2.8-wsa-jm-promoted-nice-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_promoted_nice]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção local jm promoted nice define o valor nice atribuído a trabalhos críticos ou predecessores que precisam ser promovidos em sistemas UNIX e Linux, para que recebam mais recursos e sejam processados antes de outros trabalhos; o padrão é -1, números menores representam prioridades maiores, e se um inteiro positivo for especificado o valor padrão é usado, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção local jm promoted nice define o valor nice atribuído a trabalhos críticos ou predecessores que precisam ser promovidos em sistemas UNIX e Linux, para que recebam mais recursos e sejam processados antes de outros trabalhos; o padrão é -1, números menores representam prioridades maiores, e se um inteiro positivo for especificado o valor padrão é usado, conforme documentação oficial?*

---

### 301. hwa-10.2.8-wsa-jm-promoted-priority-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_promoted_priority]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção local jm promoted priority define o valor de prioridade para trabalhos críticos ou predecessores que precisam ser promovidos em sistemas Windows, com valores possíveis High, AboveNormal, Normal, BelowNormal e Low ou Idle, sendo o padrão AboveNormal, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção local jm promoted priority define o valor de prioridade para trabalhos críticos ou predecessores que precisam ser promovidos em sistemas Windows, com valores possíveis High, AboveNormal, Normal, BelowNormal e Low ou Idle, sendo o padrão AboveNormal, conforme documentação oficial?*

---

### 302. hwa-10.2.8-wsa-jnext-plan-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, quando o comando JnextPlan é executado para incluir um novo trabalho crítico no plano de produção, todos os trabalhos que são predecessores diretos ou indiretos do trabalho crítico são identificados e, junto com o trabalho crítico, formam uma critical network, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, quando o comando JnextPlan é executado para incluir um novo trabalho crítico no plano de produção, todos os trabalhos que são predecessores diretos ou indiretos do trabalho crítico são identificados e, junto com o trabalho crítico, formam uma critical network, conforme documentação oficial?*

---

### 303. hwa-10.2.8-wsa-localopts-wsa-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, as opções locais do Workload Service Assurance são definidas editando o arquivo *twshome*\localopts em cada workstation onde os trabalhos críticos serão executados, e é necessário executar JnextPlan ou reiniciar o agente para que as alterações nas opções locais entrem em vigor, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as opções locais do Workload Service Assurance são definidas editando o arquivo *twshome*\localopts em cada workstation onde os trabalhos críticos serão executados, e é necessário executar JnextPlan ou reiniciar o agente para que as alterações nas opções locais entrem em vigor, conforme documentação oficial?*

---

### 304. hwa-10.2.8-wsa-long-duration-threshold-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > wsa [wsa_long_duration_threshold]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global longDurationThreshold (abreviação ld) é um valor percentual (padrão 150) pelo qual, se a duração real de um trabalho atingir 150% ou mais da duração estimada, o trabalho é considerado de duração longa e é adicionado à hot list visível no Dynamic Workload Console, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global longDurationThreshold (abreviação ld) é um valor percentual (padrão 150) pelo qual, se a duração real de um trabalho atingir 150% ou mais da duração estimada, o trabalho é considerado de duração longa e é adicionado à hot list visível no Dynamic Workload Console, conforme documentação oficial?*
- *Qual o propósito e valor padrão da opção global longDurationThreshold no optman do HWA?*

---

### 305. hwa-10.2.8-wsa-promoted-job-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_promotion]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, quando o critical start time de um trabalho está se aproximando e o trabalho ainda não iniciou, o mecanismo de promoção (promotion) é usado: o trabalho promovido recebe recursos adicionais do sistema operacional e sua submissão é priorizada, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, quando o critical start time de um trabalho está se aproximando e o trabalho ainda não iniciou, o mecanismo de promoção (promotion) é usado: o trabalho promovido recebe recursos adicionais do sistema operacional e sua submissão é priorizada, conforme documentação oficial?*

---

### 306. hwa-10.2.8-wsa-promotion-offset-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_promotion_offset]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, a opção global promotionOffset (abreviação po) determina o intervalo de tempo antes do critical start time em que um trabalho se torna elegível para promoção; seu valor padrão é 120 segundos, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global promotionOffset (abreviação po) determina o intervalo de tempo antes do critical start time em que um trabalho se torna elegível para promoção; seu valor padrão é 120 segundos, conforme documentação oficial?*
- *Qual o propósito e valor padrão da opção global promotionOffset no optman do HWA?*

---

### 307. hwa-10.2.8-wsa-promotion-offset-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_promotion_selection]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os trabalhos promovidos são selecionados para submissão depois de trabalhos com prioridades 'high' e 'go', mas antes de todos os demais trabalhos, e o timing das promoções é controlado pela opção global promotionoffset, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os trabalhos promovidos são selecionados para submissão depois de trabalhos com prioridades 'high' e 'go', mas antes de todos os demais trabalhos, e o timing das promoções é controlado pela opção global promotionoffset, conforme documentação oficial?*

---

### 308. hwa-10.2.8-wsa-security-file-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_security_requirements]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, é obrigatório que os usuários que possuem as instâncias executando trabalhos críticos estejam autorizados a trabalhar com todos os trabalhos, job streams e workstations associados, devendo ter direitos DISPLAY, MODIFY e LIST no arquivo de segurança para todos os objetos JOB, SCHEDULE e CPU, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é obrigatório que os usuários que possuem as instâncias executando trabalhos críticos estejam autorizados a trabalhar com todos os trabalhos, job streams e workstations associados, devendo ter direitos DISPLAY, MODIFY e LIST no arquivo de segurança para todos os objetos JOB, SCHEDULE e CPU, conforme documentação oficial?*

---

### 309. hwa-10.2.8-wsa-service-assurance-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > wsa [wsa_introduction]]`

**Regra Canônica / Evidência:**
O Workload Service Assurance é um recurso opcional do HCL Workload Automation 10.2.8 que permite marcar trabalhos como críticos para o negócio (mission-critical) e assegurar que sejam processados em tempo hábil, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O Workload Service Assurance é um recurso opcional do HCL Workload Automation 10.2.8 que permite marcar trabalhos como críticos para o negócio (mission-critical) e assegurar que sejam processados em tempo hábil, conforme documentação oficial?*

---

### 310. hwa-10.2.8-wsa-service-class-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: general_operations > wsa [wsa_critical_flag]]`

**Regra Canônica / Evidência:**
Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?*

---

### 311. hwa-10.2.8-wsa-service-policy-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: general_operations > wsa [wsa_critical_flag]]`

**Regra Canônica / Evidência:**
Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?*

---

### 312. hwa-10.2.8-wsa-srvclass-srvpol-zos-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: general_operations > wsa [wsa_critical_flag]]`

**Regra Canônica / Evidência:**
Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?*

---

### 313. hwa-10.2.8-wsa-symphony-file-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: general_operations > wsa [wsa_symphony_times]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os tempos calculados para cada trabalho da rede crítica são adicionados ao arquivo Symphony, que contém todas as informações do plano e é distribuído a todas as workstations onde os trabalhos serão executados, conforme documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os tempos calculados para cada trabalho da rede crítica são adicionados ao arquivo Symphony, que contém todas as informações do plano e é distribuído a todas as workstations onde os trabalhos serão executados, conforme documentação oficial?*

---

### 314. hwa-10.2.8-wsclass-workstation-class-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > workstation [workstation_class]]`

**Regra Canônica / Evidência:**
Workstation class: agrupamento lógico de workstations para que jobs sejam direcionados à classe em vez de CPUs individuais; membros podem ser nomes explícitos ou o caractere curinga @.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Workstation class: agrupamento lógico de workstations para que jobs sejam direcionados à classe em vez de CPUs individuais; membros podem ser nomes explícitos ou o caractere curinga @?*

---

### 315. hwa-9.4.0-incident-switchplan-exec-hung-0001

**Escopo & Contexto:** `[Escopo: IBM Workload Scheduler 9.4.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > switchplan [switchplan]]`

**Regra Canônica / Evidência:**
Sintoma e recuperacao no IBM Workload Scheduler 9.4 (Distributed): um job SWITCHPLAN do FINAL pode permanecer em EXEC por horas mesmo com o plano ja confirmado (Run number == Confirm run number), quando o processo 'planman -timeout 3600 confirm' fica pendurado (padrao do APAR IV89990 - PLANMAN CONFIRM HANGS). Recuperacao segura sem ResetPlan: (1) confirmar plano consistente com planman showinfo (Run == Confirm); (2) identificar e encerrar somente o processo OS 'planman ... confirm' pendurado (conman kill e documentado como ignorado para job em EXEC); (3) reconciliar o job com 'conman confirm <job>;succ', pois o switch efetivamente completou e o FINALPOSTREPORTS depende do SWITCHPLAN SUCC; (4) nao reexecutar SwitchPlan/Stageman (risco AWSBHV082E), nao disparar segundo JnextPlan (risco AWSJPL017E) e nao usar ResetPlan -scratch como rotina. O EXEC residual nao bloqueia o proximo JnextPlan: a instancia antiga e arquivada com o Symphony anterior no stageman e o FINAL seguinte e instancia nova.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*

---

### 316. hwa-9.5-conman-jobman-contrast-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-jobman-0001: na 9.5, o jobman (gerenciador de acoes de jobs, ex.: jobman -refresh) era um binario CLI estavel; na 10.2.8 a interface jobman foi consolidada/estendida no contexto dos novos processos, mas a sintaxe exata das opcoes (ex.: -refresh, -stop) permanece version-dependent e nao deve ser usada de forma universal.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 317. hwa-9.5-conman-mailman-logman-contrast-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-mailman-logman-0001: na 9.5, mailman e logman ja existiam como processos de notificacao (e-mail) e log de eventos de jobs/planos; na 10.2.8 eles permanecem, mas a configuracao e a integracao com o event processor e o schema de log em banco foram estendidos; o comportamento de base e o mesmo, mas detalhes de configuracao sao version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 318. hwa-9.5-conman-planman-contrast-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-planman-0001: na 9.5, o planman gerenciava planos baseados em arquivos (Symphony) com planman -suspend/-resume; na 10.2.8 o planman opera sobre plano persistido em banco (schema pln), mantendo -suspend/-resume mas com comandos adicionais de showinfo/confirm; o modelo de armazenamento do plano difere e e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 319. hwa-9.5-conman-recovery-contrast-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-recovery-0001: na 9.5, a recuperacao de console/processamento de eventos era feita com conman start/stop e recover; o comando resetFTA ja existia para FTA com Symphony corrompido; na 10.2.8 resetFTA e restrito a emergencia (precondicoes: FTA fisico, sem hosted extended agent, aprovacao humana) e NAO deve ser usado em automacao; a politica de recuperacao e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 320. hwa-9.5-conman-startstop-contrast-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-startstop-0001: na 9.5, conman start/stop controlava os processos de producao; na 10.2.8 o conman start nao deve ser emitido enquanto JnextPlan ou stageman estiver em execucao e os processos de event monitoring/Liberty sao gerenciados separadamente (startappserver/starteventprocessor); a regra de seguranca ao iniciar/parar e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 321. hwa-9.5-jwtfile-contrast-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.x (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-jwtfile-0001: na 9.5, os clientes de linha de comando (composer/conman) autenticavam com usuario/senha via arquivos de propriedades, sem o arquivo .jwt_token; o arquivo .jwt_token (armazenado em useropts) passou a ser o mecanismo de autenticacao dos clientes CLI a partir da 10.2.x; portanto, a localizacao e a existencia do .jwt_token sao version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 322. hwa-9.5-real-rest-v1-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5 Distributed, a REST API disponivel e a versao 1 (V1): ela permite criar GUI ou CLI proprias para executar as funcoes dos programas composer, conman e planman e do Dynamic Workload Console. A REST API V2 so foi introduzida na versao 10.1 Fix Pack 1. Portanto, automaao REST para 9.5 deve usar a sintaxe V1, nao os endpoints/sintaxe da V2.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar conman?*

---

### 323. hwa-install-1028-dm-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na configuração de um domain manager HWA 10.2.8, a workstation manager deve ser definida em um novo domínio, incluída no plano com JnextPlan -for 0000 e receber limite de jobs utilizável. Context: Create a new domain; TYPE MANAGER; Run JnextPlan -for 0000.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: Na configuração de um domain manager HWA 10.2.8, a workstation manager deve ser definida em um novo domínio, incluída no plano com JnextPlan -for 0000 e receber limite de jobs utilizável?*

---

### 324. hwa-install-bkmdm-1028-keys-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Ao instalar o backup master domain manager (BMDM) no HCL Workload Automation 10.2.8, a documentação exige usar as MESMAS chaves de criptografia AES do master domain manager (MDM) para que o BMDM possa descriptografar arquivos criptografados, como o arquivo Symphony. O passo documentado é: (1) fazer backup dos arquivos de TWA_DATA_DIR\ssl\aes no BMDM e (2) copiar os arquivos de TWA_DATA_DIR\ssl\aes do MDM para TWA_DATA_DIR\ssl\aes no BMDM. As chaves de criptografia AES são aplicáveis a partir da versão 10.1 (no upgrade paralelo a partir de versão anterior a 10.1, este passo pode ser ignorado).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Ao instalar o backup master domain manager (BMDM) no HCL Workload Automation 10.2.8, a documentação exige usar as MESMAS chaves de criptografia AES do master domain manager (MDM) para que o BMDM possa descriptografar arquivos criptografados, como o arquivo Symphony?*

---

### 325. hwa-jnextplan-syntax-gap-0048

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
A sintaxe exata do comando JnextPlan no HCL Workload Automation 10.2.8 é: JnextPlan [-V | -U] | [-from mm/dd/[yy]yy[hh[:]mm[tz | timezone tzname]]] {-to mm/dd/[yy]yy[hh[:]mm[tz | timezone tzname]] | -for [h]hh[:]mm [-days n] | -days n} [-noremove]. Opções principais: -from (início do plano, usado apenas se não existir plano de produção; padrão 'today + startOfDay'), -to (próximo início do dia de processamento; mutuamente exclusivo com -for e -days), -for (extensão do plano em hhhmm; mutuamente exclusivo com -to), -days n (número de dias para criar/estender o plano; mutuamente exclusivo com -to) e -noremove (garante que instâncias de job streams concluídas não sejam removidas do novo plano). Sem -to, -for ou -days, a duração padrão do plano é um dia. A opção -scratch NÃO é documentada para JnextPlan no 10.2.8; -scratch é opção do comando ResetPlan.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: A sintaxe exata do comando JnextPlan no HCL Workload Automation 10.2.8 é: JnextPlan [-V | -U] | [-from mm/dd/[yy]yy[hh[:]mm[tz | timezone tzname]]] {-to mm/dd/[yy]yy[hh[:]mm[tz | timezone tzname]] | -for [h]hh[:]mm [-days n] | -days n} [-noremove]?*

---

### 326. hwa-lab-10.2.8-corpus-redaction-reclass-0101

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI conman (Monitoramento e Plano) > Tópico: installation_upgrade > twsinst [twsinst]]`

**Regra Canônica / Evidência:**
No corpus de treinamento HWA 10.2.8, foi aplicada redação de dados sensíveis e reclassificação de chunks operacionais como prática de comunidade. (1) Redação: domínios/hostnames reais de empresa foram substituídos por placeholders genéricos nos chunks de SCRIPT SHELL.pdf (inbev.com -> [COMPANY].com) e TWS.pdf (orb-data.com, stlpr160.corp.anheuser-busch.com, hostnames STLPR160/STLPR162_BKM -> [COMPANY]/[HOSTNAME]) em data/corpus.jsonl e data/quarantine.jsonl; verificação posterior confirmou 0 hits restantes. (2) Reclassificação: os 29 chunks de data/raw/TWS.pdf (runbook operacional local em PT com comandos conman/twsinst/planman e sequências de restart/tracing/datagather) foram reclassificados de internal_operational_unreviewed para internal_operational_community_practice via unofficial_validation_results.jsonl (status community_practice, training_eligible=True, disclaimer explícito), após validação com pesquisa Perplexity confirmando que os comandos individuais (conman shut/start/startmon, twsinst -new -agent, planman unlock/resync, trace configDropins, datagather) são documentados oficialmente no Troubleshooting Guide 10.2.8 e nas páginas awsrgstartstop/awsrgusingconman/awspiagentparams, mas a sequência local do runbook é customização da equipe. Resultado: quarantine caiu de 272 para 235 chunks, treino representativo subiu para 15406, e 37 chunks community_practice (8 SCRIPT SHELL + 29 TWS.pdf) entraram no train_full com training_eligible=True. Os 94 chunks internal_operational_unreviewed restantes (iws-hwa-10.2-perfreport.pdf 25 verified oficial HCL Rome Lab; awscertsmst.pdf 69 obsolete oficial IBM TWS 8.x) permanecem fora do treino por design (benchmark/legado, claims atômicos registrados separadamente).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar twsinst?*
- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?*

---

### 327. hwa-lab-10.2.8-destructive-cleanup-lesson-0100

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
Lição crítica de segurança operacional no laboratório HWA 10.2.8: os jobstreams de sistema MDMXA#FINAL e MDMXA#FINALPOSTREPORTS (definidos no arquivo oficial do produto /opt/hwa/TWS/config/Sfinal com ON RUNCYCLE 'FREQ=DAILY;' AT 2359 CARRYFORWARD e jobs STARTAPPSERVER -> MAKEPLAN -> SWITCHPLAN -> CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS) foram incluídos em uma limpeza de 'test/orphan' objects (evidência hwa-lab-10.2.8-cleanup-orphans-0083: '3 MDMXA streams (FINAL, FINALPOSTREPORTS, ...) deleted') e removidos do banco com 'echo y | composer delete MDMXA#FINAL'. Essa ação destrutiva não quebrou o scheduler imediatamente, mas removeu o mecanismo automático de virada de plano: o JnextPlan passou a apenas estender o plano existente (-for 0000), o dia corrente ficou preso (conman sc mostrando 08/18/26 em 08/19/26) e nenhuma instância MDMXA#FINAL era criada (evidência hwa-lab-10.2.8-plan-rollover-fix-0099). Em produção, o impacto seria a ausência de geração do plano de D+1, jobs não agendados e planos nunca avançando. Recuperação documentada: composer add Sfinal + planman unlock + JnextPlan. REGRA para o corpus e operação: ao limpar objetos de teste, NUNCA deletar jobstreams de sistema/plano (FINAL, FINALPOSTREPORTS, SFINAL, JNEXTPLAN e equivalentes de virada) sem antes verificar sua função no ciclo de produção; usar allowlist de exclusão e revisar composer display antes de confirmar qualquer composer delete com echo y.

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar mdm?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar mdm?*

---

### 328. hwa-lab-10.2.8-eventrule-rest-discovery-0097

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No laboratório HWA 10.2.8, os endpoints REST reais do event-rule engine foram descobertos por decompilação dos resource classes (TWSdRESTWeb-SNAPSHOT.war/WEB-INF/classes, classes MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, RuleInstanceEventRuleResource, ActionRunEventRuleResource, PluginConfigurationEventRuleResource, EventRuleEngineApplication) e validados ao vivo em https://[IP_ADDRESS]:31116. Os subpaths usam underscore (NÃO camelCase): POST /twsd/eventrule/engine/{message_log_record|audit_record|rule_instance|action_run}/header/query (requer header 'How-Many', ex. 10, e Basic auth wauser) retornaram HTTP 200 com os registros do banco (ex.: message_log_record UPDATESUCCESS llrc 904 'Update agent MDMDA: Update successfully completed.'; rule_instance llrc 903; audit_record com histórico CONMAN/DATABASE de startmon/deployconf/sbs). GET /twsd/eventrule/engine/message_log_record/{id} e /rule_instance/{id} retornaram 200 com header + ruleId UUID. GET /twsd/eventrule/engine/action_plugin_configuration e /event_plugin_configuration (paths diretos sob /eventrule/engine/, SEM segmento /plugin_configuration/) retornaram 200 com XML de action/event definitions. GET /twsd/eventrule/deployment/active_rules retornou 200 {'warning':false,'listMessages':['AWSJCO119I No event rules are deployed.']}. Os paths camelCase anteriormente testados (messageLog, auditRecord, ruleInstance, actionRun, pluginConfiguration, /eventrule/deployment/deploy, /eventrule/engine/) NÃO existem (404). rule_builder/start|stop respondem 405 em GET (POST esperado).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCO119I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCO119I no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar mdm?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 329. hwa-lab-10.2.8-message-bhu712e-0149

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
AWSBHU712E: mensagem de erro relacionada a prompt no conman — observada no lab ao validar comportamento de prompt. Uma job stream definida com PROMPT 'Continue?' (inline text) foi submetida e permaneceu em HOLD com o job dependente tambem HOLD, confirmando que um prompt bloqueia a stream ate ser respondido. O comando reply exige um prompt nomeado (1-8 bytes); um prompt inline nao expoe nome de reply via conman reply. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHU712E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHU712E no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual é o significado da mensagem de erro AWSBHU712E no HWA e qual ação é recomendada?*

---

### 330. hwa-lab-10.2.8-message-bis356i-0158

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
AWSBIS356I: mensagem informativa do ResetPlan. Observada no lab: ResetPlan sem -scratch arquivou o Symphony atual, atualizou as estatisticas e resetou as informacoes do production plan preservando o preproduction plan; o conman nao conseguiu inspecionar jobs ate um novo Symphony ser gerado. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBIS356I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBIS356I no HWA?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual é o significado da mensagem de erro AWSBIS356I no HWA e qual ação é recomendada?*

---

### 331. hwa-lab-10.2.8-message-jcl058i-0156

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
AWSJCL058I: mensagem informativa do JnextPlan indicando criacao bem-sucedida do production plan. Observada no lab: no primeiro JnextPlan -for 0000, apos AWSJPL709I, o planner criou o production plan e carregou o Symphony (AWSJCL058I The production plan was created). Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL709I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL709I no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL058I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL058I no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL058I no HWA e qual ação é recomendada?*

---

### 332. hwa-lab-10.2.8-message-jcl062i-0157

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
AWSJCL062I: mensagem informativa do JnextPlan/SwitchPlan indicando atualizacao do run number. Observada no lab: o ultimo FINAL executado concluiu STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, CHECKSYNC, CREATEPOSTREPORTS e UPDATESTATS com codigo 0; o MAKEPLAN registrou planman ext + AWSJCL062I, e o SWITCHPLAN registrou atualizacao do run number e termino com Exit Status 0. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL062I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL062I no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual é o significado da mensagem de erro AWSJCL062I no HWA e qual ação é recomendada?*

---

### 333. hwa-lab-10.2.8-message-jpl709i-0155

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
AWSJPL709I: mensagem informativa do planner — 'During the creation of a production plan, the planner has successfully created a new preproduction plan'. Observada no lab: no primeiro JnextPlan -for 0000 apos instalacao do MDM, o planner criou os planos preproduction e production iniciais e carregou o Symphony resultante no banco. Fonte: lab HWA 10.2.8 (WSL2).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL709I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL709I no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual é o significado da mensagem de erro AWSJPL709I no HWA e qual ação é recomendada?*

---

### 334. hwa-lab-10.2.8-plan-rollover-fix-0099

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64; WSL2 Ubuntu 22.04) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > mdm [mdm]]`

**Regra Canônica / Evidência:**
No laboratório HWA 10.2.8, a virada de plano (plan rollover) diária foi restaurada após diagnóstico e correção. Causa raiz: o jobstream de virada MDMXA#FINAL (e MDMXA#FINALPOSTREPORTS), fornecido pelo produto no arquivo /opt/hwa/TWS/config/Sfinal (ON RUNCYCLE 'FREQ=DAILY;' AT 2359 CARRYFORWARD, com STARTAPPSERVER -> MAKEPLAN -> SWITCHPLAN e CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS), havia sido removido do banco durante a limpeza de objetos de teste (jobstreams do modelo = 0), de modo que nenhuma instância de virada era criada no plano e o JnextPlan só estendia o plano atual (-for 0000, plano 'preso' no dia 18/08 com o dia corrente não avançando). Correção: (1) composer add Sfinal a partir de /opt/hwa/TWS/config/Sfinal (AWSBIA288I Total objects updated: 2, jobstreams MDMXA#FINAL e MDMXA#FINALPOSTREPORTS restaurados no modelo); (2) planman unlock (AWSJPL504I planner unlocked) para resolver o lock do planner que causava AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully' (recovery oficial documentado: ResetPlan -scratch / planman unlock); (3) JnextPlan re-executado com sucesso (startappserver -> MakePlan -> SwitchPlan -> planman checksync -> CreatePostReports -> UpdateStats), resultando em conman sc mostrando MDM RUN 9 DATE 08/19/26 22:00 (plano avançou de 08/18 para 08/19), planman showinfo com Production plan end time 08/20/2026 02:59 (extensão 24h) e a instância MDMXA#FINAL 2359 08/19 HOLD no plano (CARRYFORWARD aguardando o horário), que executará MAKEPLAN/SWITCHPLAN automaticamente às 23:59 para gerar o plano do dia seguinte. Ponto de atenção: o JnextPlan sem argumentos usa o default de extensão de 24h (mesmo efeito de '-for 0000'); para gerar plano para D+1 com janela explícita usa-se 'JnextPlan -for 24:00' ou '-days 1', e para janelas maiores '-for 48:00'/'-days 2' (o FINAL do Sfinal chama MakePlan com os mesmos argumentos herdados).

**Plataforma / Validação:** Distributed; Linux x86_64; WSL2 Ubuntu 22.04

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL504I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL504I no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL017E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?*

---

### 335. hwa-lab-10.2.8-planman-resync-vs-checksync-and-localopts-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Plan Synchronization (planman) & Local Options (localopts) > Interface: CLI planman / localopts > Tópico: operations > plan_sync [resync_vs_checksync]]`

**Regra Canônica / Evidência:**
Enquanto 'planman checksync' apenas valida e carrega o arquivo Symphony existente na base relacional (AWSJCL074I), 'planman resync' envia a ordem formal de ressincronização diretamente aos processos Batchman e Liberty engineServer (AWSBEH119I). No Backup Master, a diretiva 'thiscpu' no arquivo localopts deve obrigatoriamente refletir o nome de workstation do backup (ex: thiscpu = MDM_BK), sob risco de conflito de identidade de processos durante um evento de failover.

**Plataforma / Validação:** Distributed; Linux x86_64; containers tws-hwa e tws-bmdm; HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Qual a diferença operacional entre os comandos planman resync e planman checksync?*
- *Qual mensagem conman/planman confirma o encaminhamento do comando resync para o batchman e application server?*
- *Por que a variável thiscpu no arquivo localopts do Backup Master não pode ser idêntica à do Master principal?*

---

### 336. hwa-lab-10.2.8-planman-showinfo-checksync-auditlog-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Production Plan Engine (planman) > Interface: CLI planman / Logs do Sistema > Tópico: operations > plan_lifecycle [showinfo_checksync]]`

**Regra Canônica / Evidência:**
No HWA 10.2.8, o comando 'planman showinfo' exibe os marcos temporais de produção e pré-produção (start time, end time de extensão, run number e timezone), enquanto 'planman checksync' valida e sincroniza o arquivo Symphony em disco/memória diretamente no PostgreSQL (AWSJCL074I), com todos os eventos e comandos de operador auditados em TWSMERGE.log.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Para que serve o comando planman checksync e qual mensagem confirma o sucesso?*
- *Quais informações são retornadas pelo comando planman showinfo?*
- *Onde ficam gravados os logs centrais consolidados de auditoria do TWS nos servidores Linux?*

---

### 337. hwa-official-awsjcl070i-9.4-0001

**Escopo & Contexto:** `[Escopo: IBM Workload Scheduler 9.4.0 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em IBM Workload Scheduler 9.4.0, AWSJCL070I 'Symphony file load is not yet started' é documentada em cenários nos quais CHECKSYNC ou planman resync não terminam; a página de suporte exige investigação adicional e não estabelece uma correção universal para outras releases. Context: The following message is outputted repeatedly... AWSJCL070I Symphony file load is not yet started.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL070I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL070I no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 338. hwa-official-conman-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, showjobs suporta os formatos standard, keys, info, step, logon, deps, crit e stdlist. Context: The output of the showjobs command is produced in eight formats: standard, keys, info, step, logon, deps, crit, and stdlist.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 339. hwa-official-conman-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, showschedules suporta os formatos standard, keys e deps. Context: The output of the command is produced in three formats: standard, keys, and deps.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 340. hwa-official-cycle-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > jnextplan [jnextplan]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, JnextPlan gerencia a transição do plano antigo para o novo e cada execução para e reinicia todas as workstations. Context: Every time you run JnextPlan all workstations are stopped and restarted.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Como configurar e qual o comportamento de jnextplan no HWA?*

---

### 341. hwa-official-cycle-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: general_operations > plan [makeplan]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, MakePlan replana ou estende o preproduction plan e produz Symnew. Context: MakePlan performs ... Replans or extends the preproduction plan. Produces the Symnew file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, MakePlan replana ou estende o preproduction plan e produz Symnew?*

---

### 342. hwa-official-cycle-10.2.8-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, SwitchPlan para workstations, executa Stageman, executa planman confirm para atualizar o status do plano e reinicia o scheduling. Context: Runs the planman confirm command to update the database plan status information.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 343. hwa-official-message-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJPL018E indica lock global não resetado após interrupção de MakePlan e a documentação recomenda planman unlock. Context: The previous operation of MakePlan is stopped and the global lock is not reset. To recover the situation run planman unlock.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL018E no HWA?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual é o significado da mensagem de erro AWSJPL018E no HWA e qual ação é recomendada?*

---

### 344. hwa-official-message-10.2.8-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > message [message]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSBHV082E ocorre quando Symphony e Symnew têm o mesmo run number e não podem ser mesclados. Context: The previous Symphony file and Symnew file have the same run number. They cannot be merged.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual é o significado da mensagem de erro AWSBHV082E no HWA e qual ação é recomendada?*

---

### 345. hwa-official-message-10.2.8-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJCL054E e AWSJPL016E aparecem no cenário em que a etapa final planman confirm de SwitchPlan falha. Context: These error messages are present when the last step of the SwitchPlan, that is planman confirm fails.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL016E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL016E no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL054E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL054E no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL054E no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSJPL016E no HWA e qual ação é recomendada?*

---

### 346. hwa-official-message-10.2.8-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > message [message]]`

**Regra Canônica / Evidência:**
AWSJCL070I é uma mensagem informativa do IBM/HCL Workload Scheduler cujo texto documentado é 'Symphony file load is not yet started' (o carregamento do arquivo Symphony ainda não foi iniciado), conforme páginas oficiais IBM para as versões 9.4.0, 9.5.0 e 10.1.0. Não se trata da mensagem de 'comando não reconhecido': essa é a AWSJCL002E ('...is not a recognizable HCL Workload Automation command'), documentada no guia 9.5. AWSJCL070I não consta da referência oficial de mensagens AWSJCL da versão 9.5 (os códigos documentados saltam de AWSJCL054E para AWSJCL075E) nem das páginas Messages and Codes distribuídas das versões HCL 10.2.8, 10.2.3 e 10.2.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJCL070I no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL070I no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJCL002E no HWA?*
- *Qual é o significado da mensagem de erro AWSJCL070I no HWA e qual ação é recomendada?*

---

### 347. hwa-official-mirrorbox-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > mirrorbox [mirrorbox]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, se mirrorbox.msg ou mirrorbox<n>.msg ficar cheio, por exemplo por indisponibilidade prolongada do banco, o plano é automaticamente recarregado no banco a partir do Symphony; isso não deve ser descrito como bypass universal de todos os eventos. Context: If the message box... becomes full... then a planman resync is automatically issued so that the plan is fully reloaded in the database.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar mirrorbox?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 348. hwa-official-planman-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, planman showinfo reporta tempos do production plan, última atualização, run number e confirm run number. Context: The output of this command shows ... run number ... confirm run number.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 349. hwa-official-planman-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, planman resync replica manualmente dados do Symphony para o banco. Context: To manually replicate plan data from the Symphony file to the database, run the planman resync command.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 350. hwa-official-planman-10.2.8-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, planman checksync escreve em stdout mensagens de progresso e status da replicação. Context: Messages are written to standard output with the progress and status of the command.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 351. hwa-official-planman-10.2.8-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, planman unlock libera locks associados à criação ou extensão do production plan e requer build access no objeto prodsked. Context: When HCL Workload Automation starts to create the production plan, it locks the definitions.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*

---

### 352. hwa-official-stageman-10.2.8-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, Stageman leva job streams não concluídos para o novo plano, arquiva o production plan antigo, instala o novo production plan e envia uma cópia de Symphony a domain managers e agents durante a inicialização. Context: The stageman command carries forward uncompleted job streams, archives the old production plan, and installs the new production plan.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, Stageman leva job streams não concluídos para o novo plano, arquiva o production plan antigo, instala o novo production plan e envia uma cópia de Symphony a domain managers e agents durante a inicialização?*

---

### 353. hwa-official-stageman-10.2.8-003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, executar Stageman duas vezes sobre o mesmo Symnew é uma causa documentada de AWSBHV082E quando o plano não foi resetado ou o Symphony não foi removido. Context: The Stageman process ran twice on the same Symnew file without resetting the plan or deleting the Symphony file.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSBHV082E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSBHV082E no HWA?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 354. hwa-planman-showinfo-resync-unlock-0047

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: cli_planning > planman [planman]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os comandos planman são: 'planman [connection_parameters] showinfo' (exibe informações do plano de produção atual: caminho de instalação, início e fim do plano, duração após a última extensão, data/hora da última atualização, fim do plano de pré-produção, início da primeira job stream não concluída, run number e confirm run number); 'planman [connection_parameters] resync' (replica manualmente os dados do plano do arquivo Symphony para o banco de dados); e 'planman [connection_parameters] unlock' (desbloqueia as entradas do banco de dados que permaneceram bloqueadas quando a criação do plano de produção terminou de forma anormal). Todos são executados no master domain manager.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar planman?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 355. hwa-themaster-final-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O job stream FINAL executa a sequência de arquivos de script descrita em JnextPlan para gerar o novo plano de produção no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: O job stream FINAL executa a sequência de arquivos de script descrita em JnextPlan para gerar o novo plano de produção no HCL Workload Automation, conforme a documentação oficial?*

---

### 356. hwa-themaster-final-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O job stream FINAL é colocado em produção diariamente e executa o JnextPlan antes do início de um novo dia no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: O job stream FINAL é colocado em produção diariamente e executa o JnextPlan antes do início de um novo dia no HCL Workload Automation, conforme a documentação oficial?*

---

### 357. hwa-themaster-finalpostreports-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O job stream FINALPOSTREPORTS inclui um job chamado CHECKSYNC que monitora o progresso e o resultado do comando planman resync, que carrega os dados do plano do arquivo Symphony para o banco de dados no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar themaster?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 358. hwa-themaster-jnext-plan-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O script JnextPlan gera o novo plano de produção no HCL Workload Automation, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *Qual a regra documentada no HWA Distributed sobre: O script JnextPlan gera o novo plano de produção no HCL Workload Automation, conforme a documentação oficial?*

---

### 359. hwa-themaster-switch-plan-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > themaster [themaster]]`

**Regra Canônica / Evidência:**
O comando SwitchPlan executa as seguintes ações no HCL Workload Automation: para todas as workstations, executa o Stageman para mesclar o Symphony antigo com o SymNew e arquivar o Symphony antigo no diretório schedlog, executa o planman confirm para atualizar o status do plano no banco de dados e reinicia o master para distribuir o Symphony e retomar o agendamento, conforme a documentação oficial.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar themaster?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 360. hwa-version-matrix-composer-conman-9.5-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 9.5 Distributed, os programas de linha de comando composer (definicoes no banco) e conman (objetos no plano) estao presentes e documentados; composer gerencia objetos de scheduling no banco e conman gerencia o plano de producao Symphony.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 361. hwa-version-matrix-distributed-tools-not-zos-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation / HCL Workload Automation for Z 9.5-10.2.8 (Distributed vs z/OS) > Componente: Workload Automation for Z (z/OS Engine) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Os programas composer, conman e planman sao ferramentas do HCL Workload Automation Distributed; o produto nativo HCL Workload Automation for Z (z/OS) usa a Workload Automation Programming Language (WAPL), comandos EQQ*, comandos TSO e Batch Loader, e nao usa composer/conman/planman como interface nativa.

**Plataforma / Validação:** Distributed vs z/OS

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário wapl no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wapl para gerenciar conman?*
- *O que é a linguagem WAPL e como ela é utilizada no Workload Automation for Z?*
- *Como utilizar a Workload Automation Programming Language WAPL para z/OS?*

---

### 362. hwa-version-matrix-ocli-replaces-conman-10.2.8-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8 Distributed, o Orchestration CLI e descrito como uma aplicacao standalone projetada para substituir os comandos composer e conman, oferecendo uma interface mais moderna e versatil.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*

---

### 363. hwa-version-matrix-oql-intro-10.1-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.1 Fix Pack 1 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.1 Fix Pack 1, a REST API V2 introduziu o Orchestration Query Language (OQL) como sintaxe de consulta mais simples que permite ordenar resultados, alem do planFilter similar a sintaxe conman.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar conman?*
- *Qual endpoint REST API V2 é utilizado para conman no HWA?*

---

### 364. hwa-version-matrix-rest-9.5-v1-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI conman (Monitoramento e Plano) > Tópico: cli_planning > conman [conman]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 9.5 Distributed, a REST API permitia criar GUI ou CLI propria para executar as funcoes dos programas composer, conman e planman e do Dynamic Workload Console; nesta versao a REST API V2 ainda nao existia (introduzida em 10.1 FP1).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar conman?*
- *Como utilizar o utilitário planman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no planman para gerenciar conman?*

---

### 365. hwa-version-matrix-zos-operator-commands-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation for Z 10.2.5-10.2.8 (z/OS) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: general_operations > zos [zos_operator_commands]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation for Z (z/OS), o produto pode ser iniciado, parado, cancelado ou modificado usando os comandos de operador z/OS SSTART, PSTOP, CANCEL e MODIFY (F), emitidos de um console MCS ou via SDSF.

**Plataforma / Validação:** z/OS

**Perguntas e Cenários Relacionados:**

- *Como utilizar a Workload Automation Programming Language WAPL para z/OS?*
- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation for Z (z/OS), o produto pode ser iniciado, parado, cancelado ou modificado usando os comandos de operador z/OS SSTART, PSTOP, CANCEL e MODIFY (F), emitidos de um console MCS ou via SDSF?*

---

### 366. hwa-version-matrix-zos-wapl-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation for Z 10.2.4-10.2.8 (z/OS) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: general_operations > zos [zos_wapl]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation for Z (z/OS), a Workload Automation Programming Language (WAPL) combina comandos core, comandos de Data Access (PIF nativo), Current Plan Operation commands, Function Based commands (PIF estendido), comandos TSO do HWA for Z e Batch Loader; e a linguagem de comando nativa do produto z/OS.

**Plataforma / Validação:** z/OS

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário wapl no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no wapl para gerenciar zos?*
- *O que é a linguagem WAPL e como ela é utilizada no Workload Automation for Z?*
- *Como utilizar a Workload Automation Programming Language WAPL para z/OS?*

---
