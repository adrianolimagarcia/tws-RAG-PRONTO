# PARTE1 ALTA DISPONIBILIDADE FAILOVER

## I. Alta Disponibilidade & Failover

> 32 registros.

---

### 1. `hwa-10.2.7-planman-resync-0051`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `planman`

**Afirmacao / Conteudo:**

Na documentação oficial do IBM Workload Scheduler 10.2.7, planman resync executado no master domain manager replica no banco todos os dados atualmente armazenados no Symphony; executá-lo no backup master que não está ativo não replica os dados.

> **ATENCAO / RESSALVAS DE USO:** Este claim não confirma planman checksync, unlock, reset, tuning ou qualquer correção manual adicional.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=planman resync, source=Symphony, destination=database tables, required_node=active master domain manager |
| Produto | IBM Workload Scheduler |
| Versao | 10.2.7 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1027/distr/src_tr/awstrrealignsymphdb.html |
| Titulo da fonte | Synchronizing the database with the Symphony file |
| Citacao de suporte | On the master domain manager ... planman resync ... All of the plan data currently stored in the Symphony file is replicated in database tables. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | mutating |
| Capacidade | planman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.7 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento cross-version (9.5/10.1/10.2.x) - lab é 10.2.8.00 apenas |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planman |
| verbs | resync |
| Familia | planman-resync |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar planman?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 2. `hwa-10.2.8-backup-backup-master-data-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `backup`

**Afirmacao / Conteudo:**

HWA Distributed 10.2.8 recommends frequently backing up master data files to offline storage or a backup master domain manager.

> **ATENCAO / RESSALVAS DE USO:** Plan synchronization is not a complete database backup.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Windows and UNIX |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadbckupnrestore.html |
| Titulo da fonte | Backing up and restoring the database |
| Citacao de suporte | To minimize downtime during disaster recovery, back up your master data files frequently to either offline storage or a backup master domain manager. |
| Coletado em | 2026-08-15 |
| Capacidade | backup_mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Windows and UNIX |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=backup |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| Familia | backup-backup |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 recommends frequently backing up master data files to offline storage or a backup master domain manager?


---

### 3. `hwa-10.2.8-capacity-symphony-file-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `switchmgr`

**Afirmacao / Conteudo:**

A documentação do HCL Workload Automation 10.2.8 afirma que o arquivo Symphony precisa de espaço suficiente no filesystem do master domain manager para expandir durante picos de carga; se não puder ser expandido pode ser corrompido, e se o Symphony for corrompido é preciso reiniciar o HCL Workload Automation perdendo a carga do plano atual, devendo-se monitorar o espaço disponível e, se necessário, usar um backup master com mais espaço via comando switchmgr.

> **ATENCAO / RESSALVAS DE USO:** Efeito documentado do crescimento do plano/Symphony sobre o filesystem.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Symphony file=arquivo Symphony, master domain manager=master domain manager, switchmgr=comando switchmgr |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadavoidfullfilesys.html |
| Titulo da fonte | Avoiding full file systems |
| Citacao de suporte | If the Symphony file, in particular, cannot be expanded to contain all the required records, it might become corrupted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | switchmgr |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | capacity-symphony |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar switchmgr?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 4. `hwa-10.2.8-conman-fta-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `failover`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.x, comandos de Fault-Tolerant Agent (FTA) controlam participacao, failover e tolerancia a falhas do FTA. Status version_dependent.

> **ATENCAO / RESSALVAS DE USO:** Validado no lab container 10.2.8: agente ITA, JobManager e MDMXA operando sob conman.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_ref/awsrgconmancmds.html |
| Titulo da fonte | HCL Workload Automation command reference |
| Citacao de suporte | FTA: failover, fault-tolerance |
| Coletado em | 2026-08-21 |
| Capacidade | failover |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=conman |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar failover?


---

### 5. `hwa-10.2.8-conman-switcheventprocessor-0010`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O comando conman 'switcheventprocessor' (alias 'switchevtp') alterna o servidor de processamento de eventos entre o master domain manager e o backup master (ou vice-versa) em HCL Workload Automation 10.2.8, com sintaxe {switcheventprocessor|switchevtp} [folder/]workstation (sem wildcards). Exige permissão start/stop em objetos cpu no security file.

> **ATENCAO / RESSALVAS DE USO:** Mutating/de alto impacto: o estado de correlação de regras pendentes é perdido na migração; recomenda-se planman deploy antes. Requer revisão antes de automação.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=switcheventprocessor, alias=switchevtp, interface=conman, object=event processing server (master/backup), access=start and stop on cpu objects |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgswevtproc.html |
| Titulo da fonte | Switcheventprocessor - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | Switches the event processing server from the master domain manager to the backup master or vice versa... Permission to start and stop actions on cpu objects is required. Syntax: {switcheventprocessor | switchevtp} [folder/]workstation |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-command-researcher |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | conman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | conman |
| verbs | start; stop |
| Familia | conman-switcheventprocessor |

**Perguntas relacionadas:**

- Como utilizar o utilitário switcheventprocessor no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switcheventprocessor para gerenciar conman?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?
- Como utilizar o comando conman 'switcheventprocessor' para gerenciar workstations e execução no HWA?


---

### 6. `hwa-10.2.8-govern-audit-files-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `audit`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os arquivos de auditoria são nomeados yyyymmdd e criados nos diretórios <TWA_home>/TWS/audit/plan e <TWA_home>/TWS/audit/database no master domain manager e no backup master domain manager; quando auditStore=db, a tabela AUDIT_STORE_RECORDS_V é criada no banco de dados.

> **ATENCAO / RESSALVAS DE USO:** Audit records logged as JSON lines on MDM and BMDM; one file per UTC day.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | audit_files=<TWA_home>/TWS/audit/plan and /database, named yyyymmdd, audit_store_table=AUDIT_STORE_RECORDS_V database table |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadhowaudit.html |
| Titulo da fonte | Enabling and storing audit trails - HCL Workload Automation 10.2.8 Administration Guide |
| Citacao de suporte | The files are called yyyymmdd, and are created in the following directories: <TWA_home>/TWS/audit/plan <TWA_home>/TWS/audit/database ... The AUDIT_STORE_RECORDS_V table is created in the HCL Workload Automation database. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | audit_storage |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | govern-audit |


---

### 7. `hwa-10.2.8-ha-mdm-failover-switch-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `failover`

**Afirmacao / Conteudo:**

HWA Distributed 10.2.8 can automatically switch an unavailable master domain manager to an eligible backup master domain manager, subject to a Windows limitation.

> **ATENCAO / RESSALVAS DE USO:** On Windows only a short-term switch can be automatic; no equivalent automatic DDM-to-BDDM claim was established.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Windows, Linux and UNIX with documented differences |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadautoswitchmdm.html |
| Titulo da fonte | Automatic failover |
| Citacao de suporte | a long-term switchmgr operation is triggered and the workload is automatically switched to an eligible backup master domain manager. |
| Coletado em | 2026-08-15 |
| Capacidade | failover |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Windows, Linux and UNIX with documented differences |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=ha |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| Familia | ha-mdm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 can automatically switch an unavailable master domain manager to an eligible backup master domain manager, subject to a Windows limitation?


---

### 8. `hwa-10.2.8-ha-switchmgr-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In HWA Distributed 10.2.8, switchmgr supports MDM-to-BMDM, domain-manager-to-backup-domain-manager, and DDM-to-BDDM switching.

> **ATENCAO / RESSALVAS DE USO:** HCL says switchmgr must only be used as part of specific documented procedures; no autonomous execution. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: conman switchmgr MASTERDM;MDM_BK promoveu BMDM para *UNIX MASTER (AWSBHU120I) e reverteu com sucesso.]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | mutating |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgswitchmgr.html |
| Titulo da fonte | switchmgr |
| Citacao de suporte | Switches domain management... from a master domain manager to a backup master domain manager... [and] from a dynamic domain manager to a backup dynamic domain manager. |
| Coletado em | 2026-08-15 |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=switchmgr |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | mdm |
| Familia | ha-switchmgr |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar mdm?


---

### 9. `hwa-10.2.8-incident-planman-resync-symphony-0064`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `planman`

**Afirmacao / Conteudo:**

Sintoma: dados do plano no banco nao atualizados em relacao ao Symphony. RECOVERY OFICIAL: rodar planman resync no master domain manager para atualizar o banco com a informacao mais recente do Symphony (se rodar no backup master quando nao esta atuando como master, os dados nao sao replicados). Nota: se o mirrorbox.msg (fila que sincroniza banco com Symphony) encher - ex.: banco indisponivel por periodo longo - um planman resync e emitido automaticamente para recarregar o plano no banco. Fonte: HCL Troubleshooting Guide 10.2.8 (Synchronizing the database with the Symphony file).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (pagina 158). Complementa hwa-10.2.7-planman-resync-0051.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - planman resync |
| Citacao de suporte | If you suspect the plan data loaded in the database is not up-to-date, you can run planman resync to update the database with the latest information in the Symphony file... a planman resync is automatically issued so that the plan is fully reloaded in the database. |
| Coletado em | 2026-08-23 |
| Capacidade | planman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado do banco (recarga do plano); avaliar o escopo antes da execucao. |
| Reversibilidade | Seguir o procedimento oficial de reversao ou restauracao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=planman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planman |
| verbs | resync |
| Familia | incident-planman |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar planman?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- O que causa e como solucionar o problema: dados do plano no banco nao atualizados em relacao ao Symphony?


---

### 10. `hwa-10.2.8-incident-recovery-logman-resetplan-0061`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `symphony`

**Afirmacao / Conteudo:**

Sintoma: Symphony corrompido no master e o procedimento com backup master domain manager nao pode ser executado. RECOVERY OFICIAL alternativo (logman + ResetPlan): (1) garantir processos parados (conman stop); (2) copiar a informacao do planman showinfo; (3) rodar ResetPlan (Symphony corrompido arquivado em schedlog); (4) rodar JnextPlan com -from = horario de inicio da primeira instancia de job stream incompleta (do planman showinfo) e -to = data fim do plano; so instancias incompletas entram no novo Symphony; (5) verificar o plano e status; (6) deletar instancias que nao se quer rodar; (7) aumentar o job limit das workstations (ResetPlan zera); (8) o Symphony e distribuido e a producao recomeca. Notas: status resetam para HOLD/READY; jobs SUCC rodam de novo; eventos UNTIL/DEADLINE/MAXDUR podem ser re-disparados; prompts nao sao recuperados. Fonte: HCL Troubleshooting Guide 10.2.8 (Recover using the logman and ResetPlan commands).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (paginas 161-164). Detalha o uso de JnextPlan -from/-to no recovery.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Recover using logman and ResetPlan |
| Citacao de suporte | Run JnextPlan, setting the -from parameter to the start time of the first incomplete job stream instance... and the -to parameter to the end date of your plan. Only incomplete job stream instances will be included in the new Symphony file. |
| Coletado em | 2026-08-23 |
| Capacidade | symphony |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. ResetPlan zera job limits - planejar restauracao. |
| Impacto | Pode alterar estado operacional (reset de plano, status HOLD/READY); avaliar o escopo antes da execucao. |
| Reversibilidade | Seguir o procedimento oficial de reversao ou restauracao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | stop |
| Familia | incident-recovery |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar symphony?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar symphony?
- O que causa e como solucionar o problema: Symphony corrompido no master e o procedimento com backup master domain manager nao pode ser executado?


---

### 11. `hwa-10.2.8-incident-switchmgr-jflag-0143`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `failover`

**Afirmacao / Conteudo:**

Sintoma: apos rodar switchmgr, processos parecem nao ter sido mortos no UNIX domain manager anterior — o conman mostra output inesperado: o flag J relativo a workstation desligada permanece ativo (nenhuma mensagem de que o jobman nao esta rodando pode ser transmitida porque o mailman tambem nao esta rodando), e o conman mostra... Causa: comportamento esperado durante o switch de master. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - switchmgr J flag |
| Citacao de suporte | When a shutdown command is sent to a workstation, some unexpected output might be shown by the status of the processes shown by conman... The J flag relative to the shut workstation remains active |
| Coletado em | 2026-08-23 |
| Capacidade | failover |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=switchmgr |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| Familia | incident-switchmgr |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar failover?
- O que causa e como solucionar o problema: apos rodar switchmgr, processos parecem nao ter sido mortos no UNIX domain manager anterior — o conman mostra output inesperado: o flag J relativo a workstation desligada permanece ativo (nenhuma mensagem de que o jobman nao esta rodando pode ser transmitida porque o mailman tambem nao esta rodando), e o conman mostra?


---

### 12. `hwa-10.2.8-incident-switchmgr-relink-all-0142`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `failover`

**Afirmacao / Conteudo:**

Sintoma: em um cenario com mais de um comando switchmgr, um agent nao consegue relinkar corretamente. Causa: a interacao complexa de variaveis, ambientes, condicoes de rede e eventos de link/relink pode impedir o relink. Resolucao: nenhum evento ou mensagem e perdido; e possivel repetir o switchmgr se necessario; se apenas um agent estiver envolvido, a solucao mais facil e relinka-lo manualmente; para evitar identificar os agents nao linkados, rodar JnextPlan -for 0000, que relinka automaticamente todos os agents. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Complementa hwa-10.2.8-incident-switchmgr-thiscpu-0067.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - switchmgr relink all |
| Citacao de suporte | you can, in any case, issue the following command, which automatically relinks all agents without needing to specifically identify the unlinked ones: JnextPlan -for 0000 |
| Coletado em | 2026-08-23 |
| Capacidade | failover |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (relink de agents via JnextPlan); avaliar o escopo antes da execucao. |
| Reversibilidade | Seguir o procedimento oficial de reversao ou restauracao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=switchmgr |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planner |
| Familia | incident-switchmgr |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: em um cenario com mais de um comando switchmgr, um agent nao consegue relinkar corretamente?


---

### 13. `hwa-10.2.8-incident-switchmgr-thiscpu-0067`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `failover`

**Afirmacao / Conteudo:**

Sintoma: ao alternar do master para o backup domain manager, o Symphony no backup pode corromper. Causa: a variavel thiscpu no arquivo localopts nao corresponde ao nome da workstation. Resolucao: alterar a variavel thiscpu para corresponder ao nome da workstation - o problema nao ocorre mais. Fonte: HCL Troubleshooting Guide 10.2.8 (The Symphony file on the backup domain manager is corrupted).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (pagina 156). Tema failover/switchmgr.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - switchmgr thiscpu |
| Citacao de suporte | The 'thiscpu' variable in the localopts file does not match the workstation name. Change the variable to match the workstation name and the problem no longer occurs. |
| Coletado em | 2026-08-23 |
| Capacidade | failover |
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
| Familia | incident-switchmgr |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- O que causa e como solucionar o problema: ao alternar do master para o backup domain manager, o Symphony no backup pode corromper?


---

### 14. `hwa-10.2.8-install-backup-mdm-existing-db-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

O backup master domain manager do HCL Workload Automation 10.2.8 é configurado para apontar para o banco de dados já existente do master domain manager (compartilhando o mesmo banco, sem banco próprio separado) e, após a instalação, as chaves de criptografia devem ser copiadas da pasta TWA_DATA_DIR/ssl/aes do master domain manager para a pasta TWA_DATA_DIR/ssl/aes do backup master domain manager para que ele consiga descriptografar arquivos como o Symphony.

> **ATENCAO / RESSALVAS DE USO:** Sensível (chaves de criptografia). A página confirma também que 'The new backup master domain manager is configured to point to the existing database instance' (mesmo banco). IMPORTANTE: os detalhes de rsync/scp, chown para o usuário hwa e chmod 700 no diretório / 600 nos arquivos NÃO são documentados nestas fontes oficiais e NÃO foram incluídos como verificado. A criptografia do Symphony com AES-256/AES-128 é corroborada pela página serverinst (opções --useencryption/--encryptionpassword). [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8 (tws-bmdm): serverinst.sh configurou BKM contra banco compartilhado 172.18.0.10:5432/TWS (WAINST054I).]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDMasBKM.html |
| Titulo da fonte | Installing the master domain manager as a backup master domain manager |
| Citacao de suporte | it is crucial to use the same encryption keys as those on the master domain manager, to ensure it can correctly decrypt encrypted files, such as the Symphony file. ... Copy the files from the TWA_DATA_DIR\ssl\aes folder on the master domain manager to the TWA_DATA_DIR\ssl\aes folder on the backup master domain manager. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | credential_sensitive |
| Capacidade | install |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=install |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install |
| Familia | install-backup |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: O backup master domain manager do HCL Workload Automation 10.2.8 é configurado para apontar para o banco de dados já existente do master domain manager (compartilhando o mesmo banco, sem banco próprio separado) e, após a instalação, as chaves de criptografia devem ser copiadas da pasta TWA_DATA_DIR/ssl/aes do master domain manager para a pasta TWA_DATA_DIR/ssl/aes do backup master domain manager para que ele consiga descriptografar arquivos como o Symphony?


---

### 15. `hwa-10.2.8-install-jnextplan-after-backup-0008`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Após instalar o backup master domain manager do HCL Workload Automation 10.2.8, pode-se executar opcionalmente o comando JnextPlan -for 0000 para estender em 0 horas e 0 minutos o plano de produção (Symphony) e adicionar ao plano a estação de trabalho recém-criada.

> **ATENCAO / RESSALVAS DE USO:** Ação mutável sobre o plano de produção (estende o Symphony e remove instâncias concluídas com sucesso). A referência do comando confirma: 'The JnextPlan -for 0000 command extends by 0 hours and 0 minutes the production plan and adds into the production plan (Symphony) the newly-created workstation, user, and calendar definitions'. O JnextPlan é executado no master domain manager. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: JnextPlan -for 0000 executado no MDM inseriu a workstation MDM_BK no plano Symphony (run #23).]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDMasBKM.html |
| Titulo da fonte | Installing the master domain manager as a backup master domain manager |
| Citacao de suporte | You can also optionally run JnextPlan -for 0000 to extend by 0 hours and 0 minutes the production plan and add into the production plan (Symphony) the newly-created workstation |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=install |
| Tipo | other |
| Ferramenta | planner |
| verbs | install |
| Familia | install-jnextplan |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 16. `hwa-10.2.8-install-serverinst-install-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

O master domain manager e o backup master domain manager do HCL Workload Automation 10.2.8 são instalados com o script serverinst.sh (serverinst.vbs no Windows), usando parâmetros prefixados --rdbmstype, --dbhostname, --dbport, --dbname, --dbuser, --dbpassword, --wauser, --wapassword, --wlpdir, --sslkeysfolder, --sslpassword, --inst_dir e --licenseserverid; os valores podem ser definidos no arquivo serverinst.properties (localizado em image_location/TWS/interp_name) e, se um parâmetro for definido tanto no arquivo quanto na linha de comando, o valor da linha de comando tem precedência.

> **ATENCAO / RESSALVAS DE USO:** Escopo: instalação (destrutiva) 10.2.8 distribuído. serverinst também instala DDM e backup DDM (--componenttype MDM|DDM) conforme a página de referência serverinst. Não generalizar parâmetros para outras versões.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDMasBKM.html |
| Titulo da fonte | Installing the master domain manager as a backup master domain manager |
| Citacao de suporte | A properties file named serverinst.properties is available ... The file is located in image_location/TWS/interp_name. ... If a parameter is specified both in the properties file and in the command line, the command line value takes precedence. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | destructive |
| Capacidade | install |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=install |
| Tipo | other |
| verbs | install |
| Familia | install-serverinst |

**Perguntas relacionadas:**

- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar install?
- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 17. `hwa-10.2.8-mdm-aes-keys-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Na instalação de BMDM HWA 10.2.8, a documentação exige as mesmas chaves de criptografia do MDM para descriptografar arquivos como Symphony e orienta copiar os arquivos da pasta ssl/aes do MDM para a pasta correspondente do BMDM.

> **ATENCAO / RESSALVAS DE USO:** Claim versionada; nunca coletar, copiar ou expor chaves reais no dataset. Procedimento permanece mutável e requer revisão humana. [texto recuperado do unified dataset rag_corpus (verified_claim original)] | Same version 10.2.8 as the claim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDM.html |
| Titulo da fonte | Installing the master domain manager and backup master domain manager |
| Citacao de suporte | it is crucial to use the same encryption keys as those on the master domain manager... Copy the files from the TWA_DATA_DIR\ssl\aes folder on the master domain manager to the ... backup master domain manager. |
| Coletado em | 2026-08-16 |
| Capacidade | mdm |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Terminologia normalizada | topic=mdm |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| Familia | mdm-aes |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: Na instalação de BMDM HWA 10.2.8, a documentação exige as mesmas chaves de criptografia do MDM para descriptografar arquivos como Symphony e orienta copiar os arquivos da pasta ssl/aes do MDM para a pasta correspondente do BMDM?


---

### 18. `hwa-10.2.8-rest-api-v2-endpoint-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

REST API V2 is recommended for modern integrations; the documented REST endpoint is /twsd/ with default HTTPS port 31116 for MDM/BMDM. Context: Access the REST API using https://hostname:port_number/twsd where 31116 is the default HTTPS port.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 page (awsddrestapi.html is under common/src_dgd/, not distr/src_ref/). V2 recommendation and /twsd endpoint with default HTTPS port 31116 confirmed.

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
| Citacao de suporte | REST API V2 have been implemented and are easier to configure, more powerful and flexible. It is highly recommended to use them for any future integration. ... https://hostname:port_number/twsd ... The default is 31116. |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | mdm |
| Familia | rest-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Qual a regra documentada no HWA Distributed sobre: REST API V2 is recommended for modern integrations; the documented REST endpoint is /twsd/ with default HTTPS port 31116 for MDM/BMDM?


---

### 19. `hwa-10.2.8-rest-service-url-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Para MDM ou BMDM HWA Distributed 10.2.8, a URL documentada do serviço REST é https://hostname:port_number/twsd e a porta HTTPS padrão é 31116. Context: https://hostname:port_number/twsd ... The HTTPS port number of the master domain manager or backup domain manager. The default is 31116.

> **ATENCAO / RESSALVAS DE USO:** Verified verbatim on the official v1028 page; hostname is that of the master domain manager or backup master domain manager.

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
| Citacao de suporte | https://hostname:port_number/twsd ... The HTTPS port number of the master domain manager or backup domain manager. The default is 31116. |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | mdm |
| Familia | rest-service |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Qual a regra documentada no HWA Distributed sobre: Para MDM ou BMDM HWA Distributed 10.2.8, a URL documentada do serviço REST é https://hostname:port_number/twsd e a porta HTTPS padrão é 31116. Context: https://hostname:port_number/twsd?


---

### 20. `hwa-10.2.8-restore-resolved-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

RESOLUCAO de hwa-10.2.8-restore-0001 (contradicted): na documentacao 10.2.8, a pagina 'Backing up and restoring the database' NAO fornece etapas explicitas de restore de banco; o que ela documenta como recuperacao e: (1) backup dos arquivos de configuracao e planos, (2) uso de um backup master domain manager acessando banco espelhado para disaster recovery, e (3) restauracao dos arquivos de configuracao. A restauracao efetiva do banco e executada pelo DBA com a ferramenta do SGBD, fora do escopo da pagina.

> **ATENCAO / RESSALVAS DE USO:** Resolve a contradicao: a pagina documenta backup de configuracao + backup MDM com banco espelhado para DR, mas a restauracao do banco em si e responsabilidade do DBA.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadbckupnrestore.html |
| Titulo da fonte | HCL Workload Automation backing up and restoring the database |
| Citacao de suporte | Set up a backup master domain manager that accesses a different database than the master domain manager, and get your database administrator to set up database mirroring. |
| Coletado em | 2026-08-21 |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=restore |
| Status de revisao | verified |
| Tipo | other |
| Familia | restore-resolved |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: RESOLUCAO de hwa-10.2.8-restore-0001 (contradicted): na documentacao 10.2.8, a pagina 'Backing up and restoring the database' NAO fornece etapas explicitas de restore de banco; o que ela documenta como recuperacao e: (1) backup dos arquivos de configuracao e planos, (2) uso de um backup master domain manager acessando banco espelhado para disaster recovery, e (3) restauracao dos arquivos de configuracao?


---

### 21. `hwa-10.2.8-sec-encrypted-format-0023`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

Quando o modelo de segurança baseado em funções está habilitado no HCL Workload Automation 10.2.8, as definições de objetos de segurança são salvas no banco de dados do master domain manager, o security file é convertido para um formato criptografado (por desempenho e segurança) e as configurações são sincronizadas automaticamente com o backup master.

> **ATENCAO / RESSALVAS DE USO:** Documentado: criptografia do security file e sincronização com backup master. | Security management overview states the same security-file-to-encrypted-format conversion.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | security_file=arquivo de segurança, encrypted_format=formato criptografado, master_domain_manager=gerenciador de domínio mestre, backup_master=master de backup |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadrolebasedsecuritymanagement.html |
| Titulo da fonte | Role-based security model |
| Citacao de suporte | your security file is updated and converted into an encrypted format (for performance and security), replacing the previous file. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | security |
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
| Familia | sec-encrypted |


---

### 22. `hwa-10.2.8-tls-ssl-mdm-backup-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `tls`

**Afirmacao / Conteudo:**

HWA Distributed 10.2.8 explicitly documents SSL connectivity between a master domain manager and a backup master domain manager.

> **ATENCAO / RESSALVAS DE USO:** No explicit DDM-to-BDDM pairing was established.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadscenSSLnetwork.html |
| Titulo da fonte | Scenario: SSL Communication across the fault-tolerant agent network |
| Citacao de suporte | You can enable the SSL connection... [for] Master domain manager and backup master domain manager. |
| Coletado em | 2026-08-15 |
| Capacidade | tls |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=tls |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| Familia | tls-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 explicitly documents SSL connectivity between a master domain manager and a backup master domain manager?


---

### 23. `hwa-9.5-conman-fta-contrast-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `topology_ha` / `failover`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-conman-fta-0001: na 9.5, o FTA ja suportava failover e tolerancia a falhas do Symphony/plano; na 10.2.8 o FTA continua com papel central no failover, mas a orquestracao automatica (enAutomaticFailover) e a gestao por broker de dynamic agents ampliam os cenarios; a semantica de participacao/failover do FTA e version-dependent.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: papel do FTA evolui entre versoes; nao generalizar cenario de failover.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_ref/awsrgconmancmds.html |
| Titulo da fonte | HCL Workload Automation command reference |
| Citacao de suporte | FTA: failover, fault-tolerance |
| Coletado em | 2026-08-21 |
| Capacidade | failover |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=conman |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar failover?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como configurar ou solucionar problemas no dynamic agent ou broker para failover?


---

### 24. `hwa-9.5-real-mmrresolve-fp2-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `switchmgr`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5 Fix Pack 2, a opcao global mm resolve master (mmResolveMaster) teve seu valor padrao alterado de yes para no: a partir do FP2, a variavel $MASTER nao e resolvida em JnextPlan e o host de agentes estendidos pode ser trocado por um comando conman switchmgr (short/long-term switch). Em 9.5 base e FP1 o padrao era yes. Mudanca de default real e version-dependent.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (global options 9.5). Default de mmResolveMaster mudou para no no 9.5 FP2; generalizar para 9.5 base seria errado.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 Fix Pack 2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | HCL Workload Automation 9.5 global options - mm resolve master |
| Citacao de suporte | When it is set to no, the $MASTER variable is not resolved at JnextPlan and the host of any extended agent can be switched after a conman switchmgr command (short- and long-term switch). Starting from Version 9.5 Fix Pack 2, the default is no (for previous releases, it was set to yes). |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | mm resolve master=opcao global que controla a resolucao de $MASTER, $MASTER=variavel de referencia ao master domain manager |
| Capacidade | switchmgr |
| Modo de operacao | read |
| Escopo de versao | 9.5 Fix Pack 2 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | conman |
| verbs | version |
| Familia | real-mmrresolve |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar switchmgr?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar switchmgr?


---

### 25. `hwa-9.5-real-switchmgr-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `failover`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5, o failover manual do domain manager e realizado pelo comando conman switchmgr (sinopse switchmgr domain;newmgr), que transfere a funcao de domain manager para uma workstation de backup, exigindo acesso start e stop na workstation de backup. Diferente da 10.2.8, onde o failover automatico e o padrao habilitado, na 9.5 o switch manual via switchmgr e o procedimento central documentado para troca de domain manager (curto ou longo prazo).

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (conman reference 9.5 e admin guide 9.5). switchmgr e o comando de failover manual; usa-se depois de reduzir o fence para zero e restaurar apos o switch.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ref/awsrgconmanpro.html |
| Titulo da fonte | HCL Workload Automation 9.5 conman commands (awsrgconmanpro) |
| Citacao de suporte | switchmgr Switch the domain manager functionality to a workstation. start, stop ... switchmgr domain;newmgr ... You must have start and stop access to the backup domain manager. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | switchmgr=comando conman de failover manual do domain manager, backup domain manager=domain manager de reserva, fence=job fence restaurado apos o switch |
| Capacidade | failover |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | conman |
| verbs | start; stop |
| Familia | real-switchmgr |

**Perguntas relacionadas:**

- Como utilizar o utilitário switchmgr no HCL Workload Automation?
- Qual a sintaxe ou procedimento no switchmgr para gerenciar failover?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar failover?


---

### 26. `hwa-9.5-real-twsd-31116-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5 Fix Pack 7 Distributed (MDM ou BMDM), o servico REST usa o contexto HTTPS /twsd e a porta padrao 31116; tambem em 10.2.8 o porto padrao do REST permanece 31116, mas em 9.5 o contexto e /twsd na raiz do servidor (não e o caminho /twsd/api da V2).

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (9.5 FP7 REST configuration). Porta 31116 e estavel entre 9.5 e 10.2.8; a sintaxe de caminhos V1 vs V2 e que muda.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 Fix Pack 7 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/common/src_dgd/awsddsus.html |
| Titulo da fonte | HCL Workload Automation 9.5 REST API - configuring |
| Citacao de suporte | The REST service uses the HTTPS context /twsd and the default port is 31116. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | /twsd=contexto HTTPS do servico REST, 31116=porta padrao do servico REST |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 9.5 Fix Pack 7 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | mdm |
| Familia | real-twsd |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para /twsd/api no HWA?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5 Fix Pack 7 Distributed (MDM ou BMDM), o servico REST usa o contexto HTTPS /twsd e a porta padrao 31116; tambem em 10.2.8 o porto padrao do REST permanece 31116, mas em 9.5 o contexto e /twsd na raiz do servidor (não e o caminho /twsd/api da V2)?


---

### 27. `hwa-distributed-rest-api-v2-base-url-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `rest`

**Afirmacao / Conteudo:**

A REST API V2 do HCL Workload Automation 10.2.8 é acessada pela URL base https://<hostname>:<port_number>/twsd, onde <hostname> é o master domain manager ou backup master domain manager e <port_number> é a porta HTTPS desses componentes, cujo padrão (default) é 31116.

> **ATENCAO / RESSALVAS DE USO:** Confirmado com fonte oficial HCL (página v1028 awsddrestapi.html aberta e lida): base URL oficial da REST API é https://hostname:port_number/twsd com porta HTTPS padrão 31116 do master/backup master domain manager. A página equivalente na documentação v10.1 (mesmo título awsddrestapi.html) corrobora a mesma URL base /twsd e porta padrão 31116. Este registro substitui a classificação anterior "somente aprovação operacional humana" por verificação com evidência web oficial versionada.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | rest_api_v2=REST API V2, base_url=https://hostname:port_number/twsd, twsd_base_path=/twsd, default_https_port=31116, host=master domain manager or backup master domain manager |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HCL Workload Automation with REST API |
| Citacao de suporte | After installing your master domain manager or backup master domain manager, you can access the available REST API services by connecting to the following URL: https://hostname:port_number/twsd ... port_number: The HTTPS port number of the master domain manager or backup domain manager. The default is 31116. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | rest |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | restv2 |
| Familia | rest-api |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para rest no HWA?
- Qual a regra documentada no HWA Distributed sobre: A REST API V2 do HCL Workload Automation 10.2.8 é acessada pela URL base https://<hostname>:<port_number>/twsd, onde <hostname> é o master domain manager ou backup master domain manager e <port_number> é a porta HTTPS desses componentes, cujo padrão (default) é 31116.?


---

### 28. `hwa-install-bkmdm-1028-keys-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Ao instalar o backup master domain manager (BMDM) no HCL Workload Automation 10.2.8, a documentação exige usar as MESMAS chaves de criptografia AES do master domain manager (MDM) para que o BMDM possa descriptografar arquivos criptografados, como o arquivo Symphony. O passo documentado é: (1) fazer backup dos arquivos de TWA_DATA_DIR\ssl\aes no BMDM e (2) copiar os arquivos de TWA_DATA_DIR\ssl\aes do MDM para TWA_DATA_DIR\ssl\aes no BMDM. As chaves de criptografia AES são aplicáveis a partir da versão 10.1 (no upgrade paralelo a partir de versão anterior a 10.1, este passo pode ser ignorado).

> **ATENCAO / RESSALVAS DE USO:** Confirmado com duas fontes oficiais HCL 10.2.8 lidas integralmente. A página awspiinstallMDM.html (passo 7 do procedimento de instalação) exige usar as mesmas chaves AES do MDM para que o BMDM descriptografe arquivos como o Symphony, com as etapas exatas (backup dos arquivos em TWA_DATA_DIR/ssl/aes no BMDM e cópia do MDM para o BMDM). A mesma instrução (passo 4) aparece em awspiparallelupgradefrom95installMDM.html, que ainda acrescenta: 'Encryption keys are applicable beginning with version 10.1. If you are upgrading from a version earlier than 10.1, step 4 does not apply and can be skipped.' [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: copia de key.p12 e key.sth do MDM para o BMDM permitiu a leitura do Symphony de 52KB.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | BMDM=backup master domain manager, MDM=master domain manager, AES=chaves de criptografia simétrica AES, TWA_DATA_DIR=diretório de dados HWA (TWA_DATA_DIR), ssl/aes=caminho das chaves AES: TWA_DATA_DIR/ssl/aes, Symphony=arquivo Symphony (plano de produção), backup MDM=backup master domain manager |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDM.html |
| Titulo da fonte | Installing the master domain manager and backup master domain manager |
| Citacao de suporte | If you are installing a backup master domain manager, it is crucial to use the same encryption keys as those on the master domain manager, to ensure it can correctly decrypt encrypted files, such as the Symphony file. To achieve this, perform the following steps: 1. Backup the files located in the TWA_DATA_DIR\ssl\aes folder on the backup master domain manager. 2. Copy the files from the TWA_DATA_DIR\ssl\aes folder on the master domain manager to the TWA_DATA_DIR\ssl\aes folder on the backup master domain manager. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | credential_sensitive |
| Capacidade | install |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install |
| Familia | bkmdm-1028 |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: Ao instalar o backup master domain manager (BMDM) no HCL Workload Automation 10.2.8, a documentação exige usar as MESMAS chaves de criptografia AES do master domain manager (MDM) para que o BMDM possa descriptografar arquivos criptografados, como o arquivo Symphony?


---

### 29. `hwa-install-mdm-1028-params-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação MDM/BMDM HWA 10.2.8, os parâmetros documentados incluem rdbmstype, dbhostname, dbport, dbname, dbuser, dbpassword, wauser, wapassword, wlpdir, sslkeysfolder, sslpassword, inst_dir e licenseserverid. Context: The following information is required... Database information... Open Liberty information... Security information... Licensing information.

> **ATENCAO / RESSALVAS DE USO:** All 13 parameters appear in the required-information table and in the sample serverinst command on the page (database / HCL Workload Automation user / Open Liberty / security / installation directory / licensing groups). Full parameter reference: awspitwsinstparams.html. Procedural, password-bearing claim - use only parameter names, never values.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDM.html |
| Titulo da fonte | Installing the master domain manager and backup master domain manager |
| Citacao de suporte | --rdbmstype <db_type> --dbhostname <db_hostname> --dbport <db_port> --dbname <db_name> --dbuser <db_user> --dbpassword <db_password> --wauser <wa_user> --wapassword <wa_password> --wlpdir <Liberty_installation_dir> --sslkeysfolder <certificate_files_path> --sslpassword <keystore_truststore_password> --inst_dir <installation_dir> --licenseserverid <license_server_ID> |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=backup_master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install; open |
| Familia | mdm-1028 |

**Perguntas relacionadas:**

- Como os parâmetros de instalação do MDM são configurados e validados no HWA 10.2.8?
- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 30. `hwa-install-mdm-1028-prereqs-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Antes de instalar um MDM HWA 10.2.8, a documentação requer Liberty no nó, banco criado/populado, usuário administrativo, licença configurada e, em UNIX, umask 022; o BMDM aponta para o banco existente e não requer criar/popular o banco. Context: Before starting the installation... Installing Open Liberty... Creating and populating the database... Creating the HCL Workload Automation administrative user... Ensure you have created a license server... umask is set to 022.

> **ATENCAO / RESSALVAS DE USO:** 'Before you begin' checklist confirmed: 1) Installing Open Liberty or WebSphere Application Server Liberty Base; 2) Creating and populating the database; 3) Creating the HCL Workload Automation administrative user; 4) 'Ensure you have created a license server and made a note of the server ID'; 5) 'On UNIX operating systems, ensure that umask is set to 022' (umask 022 command). Backup MDM database note is verbatim. The 9.4->10.2.8 parallel-upgrade variant (awspiinstallMDMasBKM.html) additionally requires converting default certificates and upgrading DB tables.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDM.html |
| Titulo da fonte | Installing the master domain manager and backup master domain manager |
| Citacao de suporte | When installing a backup master domain manager, the backup points to the existing HCL Workload Automation database. In this case, creating and populating the database is not required. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=backup_master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install; open |
| Familia | mdm-1028 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Antes de instalar um MDM HWA 10.2.8, a documentação requer Liberty no nó, banco criado/populado, usuário administrativo, licença configurada e, em UNIX, umask 022; o BMDM aponta para o banco existente e não requer criar/popular o banco?


---

### 31. `hwa-lab-10.2.8-switchmgr-failover-switchback-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando conman 'switchmgr <DOMAIN>;<NOVO_MASTER>' comuta a gestão do domínio MASTERDM do Master principal (MDM) para o Backup Master (MDM_BK). O nó assumido torna-se *UNIX MASTER e executa jobs no plano de forma transparente, permitindo switchback posterior com 'switchmgr MASTERDM;MDM'.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa + tws-bmdm); HWA 10.2.8 |
| Observado em | 2026-09-09T19:30:00-03:00 |

**Procedimento executado:** 1. Disparado 'switchmgr MASTERDM;MDM_BK' no MDM (AWSBHU120I). 2. Verificado no tws-bmdm o status de *UNIX MASTER e Batchman LIVES. 3. Submetido job no FTA AGT1 a partir do BMDM (SUCC rc0). 4. Executado switchback 'switchmgr MASTERDM;MDM' do tws-bmdm, restabelecendo o MDM como *UNIX MASTER.

**Saida real observada:** Failover e switchback completados com status oficial AWSBHU120I. Ambos os nós processaram e transmitiram comandos com zero corrupção de Symphony.

**Perguntas relacionadas:**

- Como realizar o failover manual do Master para o Backup Master utilizando o comando switchmgr?
- Qual é o procedimento de switchback para devolver a gestão do domínio ao Master Domain Manager original?
- Qual mensagem conman confirma a comutação de domain manager com sucesso?


---

### 32. `hwa-rest-twsd-31116-official-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Para HCL Workload Automation 9.5 Fix Pack 7 em ambiente Distributed com MDM ou BMDM, o serviço REST usa o contexto HTTPS /twsd e a porta padrão é 31116. Context: https://hostname:port_number/twsd ... The default is 31116.

> **ATENCAO / RESSALVAS DE USO:** Official 9.5 FP7 documentation opened (welcome page states 'updated for HCL Workload Automation Version 9.5 Fix Pack 7'). Answer to 'Posso assumir que ele autoriza a chamada?': no - the page documents the endpoint URL and port, not automatic authorization; authentication is still required for REST calls.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/common/src_dgd/awsddrestapi.html |
| Titulo da fonte | Driving HCL Workload Automation with REST API |
| Citacao de suporte | https://hostname:port_number/twsd ... The HTTPS port number of the master domain manager or backup domain manager. The default is 31116. |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=twsd |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | mdm |
| Familia | twsd-31116 |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para mdm no HWA?
- Qual a regra documentada no HWA Distributed sobre: Para HCL Workload Automation 9.5 Fix Pack 7 em ambiente Distributed com MDM ou BMDM, o serviço REST usa o contexto HTTPS /twsd e a porta padrão é 31116. Context: https://hostname:port_number/twsd?


---
