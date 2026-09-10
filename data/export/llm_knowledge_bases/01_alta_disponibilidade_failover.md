# ALTA DISPONIBILIDADE & FAILOVER

> Total de tópicos canônicos cobertos nesta seção: 12

---

### 1. hwa-10.2.8-capacity-symphony-file-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: topology_ha > switchmgr [switchmgr]]`

**Regra Canônica / Evidência:**
A documentação do HCL Workload Automation 10.2.8 afirma que o arquivo Symphony precisa de espaço suficiente no filesystem do master domain manager para expandir durante picos de carga; se não puder ser expandido pode ser corrompido, e se o Symphony for corrompido é preciso reiniciar o HCL Workload Automation perdendo a carga do plano atual, devendo-se monitorar o espaço disponível e, se necessário, usar um backup master com mais espaço via comando switchmgr.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar switchmgr?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*

---

### 2. hwa-10.2.8-conman-fta-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.x, comandos de Fault-Tolerant Agent (FTA) controlam participacao, failover e tolerancia a falhas do FTA. Status version_dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar failover?*

---

### 3. hwa-10.2.8-globalopts-enautomaticfailover-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI optman (Opções Globais do Master) > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a opção global enAutomaticFailover (alias af) habilita o failover automático para um engine de backup quando o master ativo fica indisponível; requer configurar workstationMasterListInAutomaticFailover e workstationEventMgrListInAutomaticFailover. Neste ambiente está YES, porém sem engines listados.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, a opção global enAutomaticFailover (alias af) habilita o failover automático para um engine de backup quando o master ativo fica indisponível; requer configurar workstationMasterListInAutomaticFailover e workstationEventMgrListInAutomaticFailover?*

---

### 4. hwa-10.2.8-globalopts-enautomaticfailoveractions-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Fault-Tolerant Agent (FTA) > Interface: CLI optman (Opções Globais do Master) > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation Distributed 10.2.8, a opção global enAutomaticFailoverActions (alias aa) tem valor 'YES' neste ambiente. enAutomaticFailoverActions | aa Enable or disable the automatic failover actions. This option enables or disables automatic failover actions, such as, the automatic switch of the master or the automatic restart of the fault-tolerant agent. 

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual o propósito e valor padrão da opção global enAutomaticFailoverActions no optman do HWA?*

---

### 5. hwa-10.2.8-ha-mdm-failover-switch-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Windows, Linux and UNIX with documented differences) > Componente: Backup Master Domain Manager (BMDM) > Interface: Geral > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
HWA Distributed 10.2.8 can automatically switch an unavailable master domain manager to an eligible backup master domain manager, subject to a Windows limitation.

**Plataforma / Validação:** Distributed; Windows, Linux and UNIX with documented differences

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 can automatically switch an unavailable master domain manager to an eligible backup master domain manager, subject to a Windows limitation?*

---

### 6. hwa-10.2.8-incident-switchmgr-jflag-0143

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: incidents > failover [failover]]`

**Regra Canônica / Evidência:**
Sintoma: apos rodar switchmgr, processos parecem nao ter sido mortos no UNIX domain manager anterior — o conman mostra output inesperado: o flag J relativo a workstation desligada permanece ativo (nenhuma mensagem de que o jobman nao esta rodando pode ser transmitida porque o mailman tambem nao esta rodando), e o conman mostra... Causa: comportamento esperado durante o switch de master. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar failover?*
- *O que causa e como solucionar o problema: apos rodar switchmgr, processos parecem nao ter sido mortos no UNIX domain manager anterior — o conman mostra output inesperado: o flag J relativo a workstation desligada permanece ativo (nenhuma mensagem de que o jobman nao esta rodando pode ser transmitida porque o mailman tambem nao esta rodando), e o conman mostra?*

---

### 7. hwa-10.2.8-incident-switchmgr-relink-all-0142

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > failover [failover]]`

**Regra Canônica / Evidência:**
Sintoma: em um cenario com mais de um comando switchmgr, um agent nao consegue relinkar corretamente. Causa: a interacao complexa de variaveis, ambientes, condicoes de rede e eventos de link/relink pode impedir o relink. Resolucao: nenhum evento ou mensagem e perdido; e possivel repetir o switchmgr se necessario; se apenas um agent estiver envolvido, a solucao mais facil e relinka-lo manualmente; para evitar identificar os agents nao linkados, rodar JnextPlan -for 0000, que relinka automaticamente todos os agents. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*
- *O que causa e como solucionar o problema: em um cenario com mais de um comando switchmgr, um agent nao consegue relinkar corretamente?*

---

### 8. hwa-10.2.8-incident-switchmgr-thiscpu-0067

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI planman / Scripts de Plano (Symphony) > Tópico: incidents > failover [failover]]`

**Regra Canônica / Evidência:**
Sintoma: ao alternar do master para o backup domain manager, o Symphony no backup pode corromper. Causa: a variavel thiscpu no arquivo localopts nao corresponde ao nome da workstation. Resolucao: alterar a variavel thiscpu para corresponder ao nome da workstation - o problema nao ocorre mais. Fonte: HCL Troubleshooting Guide 10.2.8 (The Symphony file on the backup domain manager is corrupted).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *O que causa e como solucionar o problema: ao alternar do master para o backup domain manager, o Symphony no backup pode corromper?*

---

### 9. hwa-9.5-conman-fta-contrast-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Dynamic Workload Broker / Dynamic Agent > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-conman-fta-0001: na 9.5, o FTA ja suportava failover e tolerancia a falhas do Symphony/plano; na 10.2.8 o FTA continua com papel central no failover, mas a orquestracao automatica (enAutomaticFailover) e a gestao por broker de dynamic agents ampliam os cenarios; a semantica de participacao/failover do FTA e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar failover?*
- *Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para failover?*

---

### 10. hwa-9.5-real-mmrresolve-fp2-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 Fix Pack 2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > switchmgr [switchmgr]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5 Fix Pack 2, a opcao global mm resolve master (mmResolveMaster) teve seu valor padrao alterado de yes para no: a partir do FP2, a variavel $MASTER nao e resolvida em JnextPlan e o host de agentes estendidos pode ser trocado por um comando conman switchmgr (short/long-term switch). Em 9.5 base e FP1 o padrao era yes. Mudanca de default real e version-dependent.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar switchmgr?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar switchmgr?*

---

### 11. hwa-9.5-real-switchmgr-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: topology_ha > failover [failover]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 9.5, o failover manual do domain manager e realizado pelo comando conman switchmgr (sinopse switchmgr domain;newmgr), que transfere a funcao de domain manager para uma workstation de backup, exigindo acesso start e stop na workstation de backup. Diferente da 10.2.8, onde o failover automatico e o padrao habilitado, na 9.5 o switch manual via switchmgr e o procedimento central documentado para troca de domain manager (curto ou longo prazo).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário switchmgr no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?*
- *Como utilizar o utilitário conman no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no conman para gerenciar failover?*

---

### 12. hwa-lab-10.2.8-switchmgr-failover-switchback-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: CLI conman (Monitoramento e Plano) > Tópico: high_availability > failover [switchmgr]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o comando conman 'switchmgr <DOMAIN>;<NOVO_MASTER>' comuta a gestão do domínio MASTERDM do Master principal (MDM) para o Backup Master (MDM_BK). O nó assumido torna-se *UNIX MASTER e executa jobs no plano de forma transparente, permitindo switchback posterior com 'switchmgr MASTERDM;MDM'.

**Plataforma / Validação:** Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa + tws-bmdm); HWA 10.2.8

**Perguntas e Cenários Relacionados:**

- *Como realizar o failover manual do Master para o Backup Master utilizando o comando switchmgr?*
- *Qual é o procedimento de switchback para devolver a gestão do domínio ao Master Domain Manager original?*
- *Qual mensagem conman confirma a comutação de domain manager com sucesso?*

---
