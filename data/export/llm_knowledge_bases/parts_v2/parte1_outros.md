# PARTE1 OUTROS

## I. Outros

> 382 registros.

---

### 1. `hwa-10.2-distributed-awsjdb801e-troubleshooting-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed, a mensagem AWSJDB801E indica um erro interno genérico de acesso ao banco; suas causas conhecidas incluem memória insuficiente do lock list do DB2 (DSRA0010E, SQL State 57011, Error -912), log de transações cheio, storage insuficiente no application heap, falha de autenticação de conexão e, em Oracle, ORA-01000 (máximo de cursores abertos).

> **ATENCAO / RESSALVAS DE USO:** Mensagem de diagnóstico; a causa exata é revelada pelo texto interno da própria mensagem e pelos logs (SystemOut.log). Não executar ações destrutivas sem confirmar a causa e a versão. Pesquisa Perplexity Direct (2026-08-23): AWSJDB801E e erro generico de acesso a banco; causa conhecida: transaction log do banco cheio. Verificar logs DB2 e uso de logs, aumentar logs ou configurar gerenciamento de log.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_tr/awstrdb2locklist.html |
| Versao | 10.2.x |
| Confianca | high |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Terminologia normalizada | message=AWSJDB801E, category=generic database access error, known_causes=['DB2 lock list insufficient', 'transaction log full', 'application heap storage', 'connection authorization failure', 'Oracle ORA-01000'] |
| Citacao de suporte | AWSJDB801E An internal error has been found while accessing the database. The internal error message is: "nullDSRA0010E: SQL State = 57011, Error Code = -912". Cause and solution: This indicates that the memory that DB2 allocates for its "lock list" is insufficient. |
| Status do conhecimento | verified |
| Plataforma | distributed |
| Produto | HCL Workload Automation |
| Titulo da fonte | JnextPlan fails with the DB2 error like: nullDSRA0010E |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed |
| Status de revisao | verified |
| Tipo | message |
| verbs | list |
| Codigo da mensagem | AWSJDB801E |
| Familia | distributed-awsjdb801e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJDB801E no HWA?
- Como solucionar ou diagnosticar o erro AWSJDB801E no HWA?
- Qual é o significado da mensagem de erro DSRA0010E no HWA?
- Como solucionar ou diagnosticar o erro DSRA0010E no HWA?
- Qual é o significado da mensagem de erro AWSJDB801E no HWA e qual ação é recomendada?


---

### 2. `hwa-10.2-distributed-rollback-requires-backup-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `backup`

**Afirmacao / Conteudo:**

No HCL Workload Automation, o rollback do master domain manager para um fix pack ou release anterior só é possível se um backup tiver sido criado antes da instalação do novo fix pack ou release.

> **ATENCAO / RESSALVAS DE USO:** Ação de recuperação destrutiva; sem backup prévio o rollback não é possível. | v10.2.1 Rollback procedure; version caveat: both 10.2.x Distributed, sentence verbatim.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/common/src_gi/eqqg1mdmrollback.html |
| Versao | 10.2.0 |
| Confianca | high |
| Coletado em | 2026-08-16 |
| Classificacao de risco | destructive |
| Terminologia normalizada | operation=rollback, requirement=prior backup, target=master domain manager |
| Citacao de suporte | To roll back a master domain manager to a previous fix pack level or release, you first need to create a backup before installing the new fix pack or release. This allows you to then perform a rollback procedure after the fix pack or release has been installed. |
| Status do conhecimento | verified |
| Plataforma | distributed |
| Produto | HCL Workload Automation |
| Titulo da fonte | Rollback procedure |
| Capacidade | backup_rollback |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Status de revisao | verified |
| Tipo | other |
| verbs | release; rollback |
| Familia | distributed-rollback |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation, o rollback do master domain manager para um fix pack ou release anterior só é possível se um backup tiver sido criado antes da instalação do novo fix pack ou release?


---

### 3. `hwa-10.2-perfreport-event-processor-single-thread-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `perfreport`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2, o event processor e um processo de thread unica e sua capacidade de processamento e proporcional a velocidade do core e ao I/O; por isso ele nao escala horizontalmente, apenas verticalmente (aumentando CPU e/ou I/O).

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (iws-hwa-10.2-perfreport.pdf, fonte oficial HCL). Fato de performance do 10.2: event processor single-thread, escala vertical. Nao generalizar para outras versoes sem fonte.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report (HCL Rome Lab) |
| Citacao de suporte | The event processor is a single thread process, and its processing capacity is proportional to the core speed and the I/O. For this reason, it cannot scale horizontally but vertically only by increasing the CPU and/or I/O capabilities. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | event processor=processo de processamento de eventos do HWA, escala=vertical apenas (single-thread) |
| Capacidade | perfreport_event_processor |
| Modo de operacao | read |
| Escopo de versao | 10.2 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | perfreport-event |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, o event processor e um processo de thread unica e sua capacidade de processamento e proporcional a velocidade do core e ao I/O; por isso ele nao escala horizontalmente, apenas verticalmente (aumentando CPU e/ou I/O)?


---

### 4. `hwa-10.2-perfreport-movehistorydata-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2, para gerenciar o crescimento das tabelas historicas do dynamic domain manager, a documentacao recomenda executar o script embutido movehistorydata.sh com parametros como -successfulJobsMaxAge 240, de preferencia agendado em um job em janela adequada.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (fonte oficial HCL 10.2). Pratica de manutencao das tabelas historicas do DDM via movehistorydata.sh. Valores de exemplo de configuracao (SuccessfulJobsMaxAge=360, MoveHistoryDataFrequencyInMins=720).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report (HCL Rome Lab) |
| Citacao de suporte | To avoid the behavior described above, it could be suggested to manage the policy in a more controlled way. For instance, a specific job could be used to run the cleanup invoking the built-in Workload Automation script: <INST_DIR>/TDWB/bin/movehistorydata.sh -successfulJobsMaxAge 240 |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | movehistorydata.sh=script de limpeza de historico do DDM, SuccessfulJobsMaxAge=idade maxima de jobs bem-sucedidos mantidos, MoveHistoryDataFrequencyInMins=frequencia do move de historico |
| Capacidade | movehistorydata |
| Modo de operacao | read |
| Escopo de versao | 10.2 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | perfreport-movehistorydata |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, para gerenciar o crescimento das tabelas historicas do dynamic domain manager, a documentacao recomenda executar o script embutido movehistorydata?


---

### 5. `hwa-10.2-perfreport-rome-lab-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `perfreport`

**Afirmacao / Conteudo:**

O relatório oficial de performance IBM Workload Scheduler/HCL Workload Automation V10.2 do Rome Lab, de autoria de Lorenzo Nichele e Paolo Cavazza, foi publicado na comunidade oficial HCL e aplica-se à versão 10.2 FP0 e fix packs subsequentes.

> **ATENCAO / RESSALVAS DE USO:** Hash SHA-256 do PDF local confere com o publicado. Os dados de performance são específicos dos ambientes de teste do relatório.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | document=iws-hwa_10.2_perfreport.pdf, authors=['Lorenzo Nichele', 'Paolo Cavazza'], version=10.2 FP0 |
| Produto | HCL Workload Automation |
| Versao | 10.2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | IBM Workload Scheduler / HCL Workload Automation V10.2 Performance Report |
| Citacao de suporte | IBM Workload Scheduler HCL Workload Automation V10.2 Performance Report ... Workload Automation Performance Team - HCL Software Rome Lab. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | perfreport |
| Modo de operacao | read |
| Escopo de versao | 10.2 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | perfreport-rome |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O relatório oficial de performance IBM Workload Scheduler/HCL Workload Automation V10.2 do Rome Lab, de autoria de Lorenzo Nichele e Paolo Cavazza, foi publicado na comunidade oficial HCL e aplica-se à versão 10.2 FP0 e fix packs subsequentes?


---

### 6. `hwa-10.2.3-dwc-derby-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.3, o Apache Derby não é mais suportado para o Dynamic Workload Console.

> **ATENCAO / RESSALVAS DE USO:** Escopo específico do DWC. Para ambientes anteriores que usam Derby, a documentação prescreve mover para outro banco de dados suportado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | component=Dynamic Workload Console, database=Apache Derby |
| Produto | HCL Workload Automation / Dynamic Workload Console |
| Versao | 10.2.3 |
| Plataforma | distributed; UNIX e Windows |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_pi/awspidwcexpsettings.html |
| Titulo da fonte | Connecting the Dynamic Workload Console to a new node or database |
| Citacao de suporte | If in your current environment you are using Derby, you can use this procedure to move to another supported database, because Derby is no longer supported starting from version 10.2.3. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | distributed; UNIX e Windows |
| Status de revisao | verified |
| Tipo | component |
| Ferramenta | dwc |
| Componente | Dynamic Workload Console |
| Familia | dwc-derby |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.3, o Apache Derby não é mais suportado para o Dynamic Workload Console?


---

### 7. `hwa-10.2.3-plan-definition-instance-0043`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `plan`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.3, definições de jobs e job streams no banco tornam-se instâncias no production plan; modificar uma instância não altera automaticamente a definição no banco.

> **ATENCAO / RESSALVAS DE USO:** A documentação também afirma que somente a instância pode ser modificada em certos cenários, mantendo a definição do banco inalterada.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | database=scheduling definitions, plan=job/job-stream instances, boundary=database versus production plan |
| Produto | HCL Workload Automation |
| Versao | 10.2.3 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_tsweb/General_Help/plans_c.html |
| Titulo da fonte | Plans |
| Citacao de suporte | Scheduling object definitions stored in the database, such as jobs and job streams, become instances in the production plan. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | plan_definition |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | plan-definition |

**Perguntas relacionadas:**

- O que acontece ao modificar uma instância de job no plano versus sua definição no banco?
- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, definições de jobs e job streams no banco tornam-se instâncias no production plan; modificar uma instância não altera automaticamente a definição no banco?


---

### 8. `hwa-10.2.3-preproduction-plan-0045`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `plan`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.3, o preproduction plan identifica antecipadamente instâncias de job streams e dependências externas do intervalo planejado; o banco é bloqueado durante sua geração para evitar conflitos.

> **ATENCAO / RESSALVAS DE USO:** A página documenta o lock durante geração; isso não autoriza manipular locks manualmente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | object=preproduction plan, contents=['job stream instances', 'external follows dependencies'], database_behavior=locked during generation |
| Produto | HCL Workload Automation |
| Versao | 10.2.3 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_tsweb/General_Help/awsrgpreprodplan.html |
| Titulo da fonte | Preproduction plan |
| Citacao de suporte | The preproduction plan is used to identify in advance the job stream instances and the job stream dependencies involved in a specified time period. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | preproduction_plan |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | preproduction-plan |

**Perguntas relacionadas:**

- O que acontece ao modificar uma instância de job no plano versus sua definição no banco?
- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, o preproduction plan identifica antecipadamente instâncias de job streams e dependências externas do intervalo planejado; o banco é bloqueado durante sua geração para evitar conflitos?


---

### 9. `hwa-10.2.3-production-plan-control-0042`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `plan`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.3, o production plan é o controle mestre de toda atividade de scheduling durante um production period definido pelo usuário.

> **ATENCAO / RESSALVAS DE USO:** Não extrapolar automaticamente para z/OS ou versões sem fonte correspondente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | object=production plan, scope=production period, role=master control for scheduling |
| Produto | HCL Workload Automation |
| Versao | 10.2.3 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_tsweb/General_Help/plans_c.html |
| Titulo da fonte | Plans |
| Citacao de suporte | A production plan ... is the master control for all job scheduling activity planned for a user-defined time interval, named the production period. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | production_plan |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | production-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, o production plan é o controle mestre de toda atividade de scheduling durante um production period definido pelo usuário?


---

### 10. `hwa-10.2.3-symnew-archived-plan-0046`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `symphony`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.3, Symnew é um plano temporário intermediário substituído pelo production plan quando este começa, enquanto archived plan é uma cópia de um production plan antigo armazenada no banco.

> **ATENCAO / RESSALVAS DE USO:** Não confundir Symnew, preproduction plan, Symphony e archived plan.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | temporary=Symnew plan, historical=archived plan, database=archived plan storage |
| Produto | HCL Workload Automation |
| Versao | 10.2.3 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/distr/src_tsweb/General_Help/plans_c.html |
| Titulo da fonte | Plans |
| Citacao de suporte | A Symnew plan is a temporary plan ... It is replaced by the production plan as soon as it starts. ... An archived plan is a copy of an old production plan ... stored in the database. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | symphony_symnew |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | symnew-archived |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.3, Symnew é um plano temporário intermediário substituído pelo production plan quando este começa, enquanto archived plan é uma cópia de um production plan antigo armazenada no banco?


---

### 11. `hwa-10.2.4-showcpus-link-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.4, showcpus ou sc suporta o formato ;link para exibir informações sobre workstations e links.

> **ATENCAO / RESSALVAS DE USO:** A sintaxe documentada inclui [;info|;link]. Não afirma que UNLINKED seja token literal da saída.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showcpus, alias=sc, format=link, objects=['workstations', 'links'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.4 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/docs/api/v1/content/SSGSPN_10.2.4/distr/src_ref/awsrgshowcpus.html |
| Titulo da fonte | showcpus |
| Citacao de suporte | Displays information about workstations and links. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.4 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| verbs | showcpus |
| Familia | showcpus-link |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, showcpus ou sc suporta o formato ;link para exibir informações sobre workstations e links?


---

### 12. `hwa-10.2.4-showjobs-hold-deps-0026`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.4, sj @#@.@+state=hold;deps é documentado para exibir jobs no estado HOLD no formato de dependências.

> **ATENCAO / RESSALVAS DE USO:** Sintaxe limitada ao exemplo oficial 10.2.4; deps documenta especificamente relações follows.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, alias=sj, selector=@#@.@+state=hold, format=deps, state=HOLD |
| Produto | HCL Workload Automation |
| Versao | 10.2.4 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/docs/api/v1/content/SSGSPN_10.2.4/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs |
| Citacao de suporte | To display the status of all jobs in the HOLD state ... sj @#@.@+state=hold;deps |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.4 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| verbs | showjobs |
| Familia | showjobs-hold |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, sj @#@?


---

### 13. `hwa-10.2.4-showjobs-props-unsatisfied-dependencies-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.4, showjobs ou sj com ;props exibe a propriedade runtime Not Satisfied Dependencies da instância de job selecionada.

> **ATENCAO / RESSALVAS DE USO:** props requer acesso display às propriedades da instância e não recupera informações de jobs arquivados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, alias=sj, option=props, property=Not Satisfied Dependencies |
| Produto | HCL Workload Automation |
| Versao | 10.2.4 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/docs/api/v1/content/SSGSPN_10.2.4/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs |
| Citacao de suporte | Runtime Information: ... Not Satisfied Dependencies |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.4 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| verbs | showjobs |
| Familia | showjobs-props |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.4, showjobs ou sj com ;props exibe a propriedade runtime Not Satisfied Dependencies da instância de job selecionada?


---

### 14. `hwa-10.2.5-distributed-user-object-credential-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `credential`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.5, o User Object Credential Management permite atualizar de forma centralizada e segura as senhas armazenadas nos user objects, aplicando a mudança de forma consistente no banco e nas instâncias do plano em uma única ação.

> **ATENCAO / RESSALVAS DE USO:** Funcionalidade de gestão de credenciais; não expõe a senha em si. Enquadra-se em tratamento de dado sensível. | Primary ibm.com/docs 403 (not fetchable). Corroborating page is v1028, claim is 10.2.5 — both 10.2.x Distributed, identical wording.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://www.ibm.com/docs/en/workload-automation/10.2.5?topic=wsv1e-user-object-credential-management-ensuring-operational-continuity-security |
| Versao | 10.2.5 |
| Confianca | high |
| Coletado em | 2026-08-16 |
| Classificacao de risco | credential_sensitive |
| Terminologia normalizada | scope=user object passwords, effect=centralized update across database and plan instances, feature=User Object Credential Management |
| Citacao de suporte | The User Object Credential Management enables you to securely update the passwords stored within user objects directly from a central point of control. This ensures that changes are applied consistently across both the database and plan instances. |
| Status do conhecimento | verified |
| Plataforma | distributed |
| Produto | HCL Workload Automation |
| Titulo da fonte | User Object Credential Management |
| Capacidade | credential |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.5 |
| Escopo de plataforma | distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Status de revisao | verified |
| Tipo | other |
| Familia | distributed-user |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.5, o User Object Credential Management permite atualizar de forma centralizada e segura as senhas armazenadas nos user objects, aplicando a mudança de forma consistente no banco e nas instâncias do plano em uma única ação?


---

### 15. `hwa-10.2.8-AWSWUI-0100E-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem AWSUI0100E indica que a lista de job streams não pôde ser carregada devido a um erro do engine IBM Workload Scheduler; a causa documentada é um erro ocorrido no engine, cujo ID é informado no texto da mensagem, e a recuperação é resolver o erro indicado e tentar novamente a operação.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'The job stream list cannot be loaded because of the following engine error: engine_error_message_ID'. Causa: erro ocorrido no engine IBM Workload Scheduler; o ID do erro é informado no texto da mensagem. Ação do sistema: a ação solicitada não foi concluída. Recuperação: resolver o erro indicado pelo ID e tentar novamente. Diagnóstico; não modifica estado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSUI0100E, component=Dynamic Workload Console (WUI), object=job stream list load, cause_source=engine error ID in message text |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; Dynamic Workload Console |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsawswuimsgs.html |
| Titulo da fonte | AWSUI0001E - AWSUI6212W |
| Citacao de suporte | The job stream list cannot be loaded because of the following engine error: engine_error_message_ID ... The job stream list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. ... Resolve the error and retry the operation. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; Dynamic Workload Console |
| Tipo | message |
| Ferramenta | scheduler |
| Codigo da mensagem | AWSUI0100E |
| Componente | Dynamic Workload Console (WUI) |
| Familia | AWSWUI-0100E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSUI0100E no HWA?
- Como solucionar ou diagnosticar o erro AWSUI0100E no HWA?
- Qual é o significado da mensagem de erro AWSWUI0100E no HWA?
- Como solucionar ou diagnosticar o erro AWSWUI0100E no HWA?
- Qual é o significado da mensagem de erro AWSWUI0100E no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSUI0100E no HWA e qual ação é recomendada?


---

### 16. `hwa-10.2.8-AWSZAP-002E-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem AWSZAP002E indica que a submissão de um job stream no subsistema z/OS não foi bem-sucedida; a causa é fornecida no texto da própria mensagem (campo reason), e a recuperação documentada é usar a mensagem de reason para determinar a causa, corrigir o problema se possível e tentar novamente, ou pesquisar a base de suporte IBM.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'Submission of job stream "job_stream_name" was not successful. Reason: "reason".' Causa: a página remete ao campo reason da própria mensagem. Ação do sistema: a operação não pode ser executada. Recuperação: usar a mensagem de reason; se corrigível, tentar novamente; senão, pesquisar a base de suporte IBM. Diagnóstico; não modifica estado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSZAP002E, component=action plug-in for z/OS (ZAP), object=job stream submission on z/OS subsystem, cause_source=reason field in message text |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; action plug-in for z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsawszapmsgs.html |
| Titulo da fonte | AWSZAP002E - AWSZAP006E |
| Citacao de suporte | Submission of job stream "job_stream_name" was not successful. Reason: "reason" ... Use the reason message to determine why the operation cannot be performed. If you can fix the problem, retry the operation. If you cannot resolve the problem, search the IBM Support database for a solution. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; action plug-in for z/OS |
| scope | distributed; action plug-in for z/OS |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| Codigo da mensagem | AWSZAP002E |
| Componente | action plug-in for z/OS (ZAP) |
| Familia | AWSZAP-002E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSZAP002E no HWA?
- Como solucionar ou diagnosticar o erro AWSZAP002E no HWA?
- Qual é o significado da mensagem de erro AWSZAP002E no HWA e qual ação é recomendada?


---

### 17. `hwa-10.2.8-AWSZAP-003E-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem AWSZAP003E indica que o valor de um parâmetro não está no formato correto key=value; a causa é remetida ao texto da mensagem, e a recuperação documentada é escrever o parâmetro indicado no formato correto e tentar novamente.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'The parameter value "parameter_value" is not in the correct format of: key=value.' Causa: a página remete ao texto da mensagem. Ação do sistema: a operação não pode ser executada. Recuperação: escrever o parâmetro indicado no formato correto (key=value) e tentar novamente. Diagnóstico; não modifica estado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSZAP003E, component=action plug-in for z/OS (ZAP), object=parameter format, expected_format=key=value |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; action plug-in for z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsawszapmsgs.html |
| Titulo da fonte | AWSZAP002E - AWSZAP006E |
| Citacao de suporte | The parameter value "parameter_value" is not in the correct format of: key=value. ... Write the indicated parameter in the correct format and retry the operation. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; action plug-in for z/OS |
| scope | distributed; action plug-in for z/OS |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| Codigo da mensagem | AWSZAP003E |
| Componente | action plug-in for z/OS (ZAP) |
| Familia | AWSZAP-003E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSZAP003E no HWA?
- Como solucionar ou diagnosticar o erro AWSZAP003E no HWA?
- Qual é o significado da mensagem de erro AWSZAP003E no HWA e qual ação é recomendada?


---

### 18. `hwa-10.2.8-aida-alert-definitions-0008`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `alerts`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor define alertas de anomalia por KPI com schema: definitionID (ex.: CONTINUOUS_JOBWKS), name, kpi (metric_name, ex.: application_wa_JobsByWorkstation_jobs), trigger {type: continuous|total, value: 10, timeFrame: 60, description}, periodicity ('1 hour'), isActive ('true'), alert-definition (CONTINUOUS|TOTAL). O trigger type 'continuous' detecta N anomalias CONSECUTIVAS dentro do periodo (ex.: 'Over 10 Consecutive Anomalies within 1 hour'); o 'total' detecta N anomalias TOTAIS no periodo ('Over 10 Anomalies within 1 hour'). O pacote instala 12 alert-definitions default (uma continuous + uma total para cada um de 6 KPIs): JOBWKS (jobs por workstation), JOBFOLDER (jobs por folder), JOBSTATUS (jobs por status), JOBTOTAL (total jobs), MESSAGE (message files fill percentile), INCOMPLETEPREDECESSOR_CRITICAL (WA critical job incomplete predecessor). As definicoes ficam no indice OpenSearch alert-definitions.

> **ATENCAO / RESSALVAS DE USO:** Extraido do indice OpenSearch alert-definitions do lab (12 docs reais). Validado em laboratorio 2026-08-25 via GET aida-es:9200/alert-definitions/_search. [Observado em laboratorio HWA 10.2.8 WSL2]

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
| Citacao de suporte | definitionID: CONTINUOUS_JOBWKS, trigger: {type: continuous, value: 10, timeFrame: 60, description: 'Over 10 Consecutive Anomalies within 1 hour'}, periodicity: '1 hour', isActive: 'true' |
| Coletado em | 2026-08-25 |
| Capacidade | aida_alerts |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, OpenSearch aida-es, tested_commands=['GET aida-es:9200/alert-definitions/_search?size=50'], result=12 alert-definitions com schema completo (definitionID, name, kpi, trigger{type,value,timeFrame,description}, periodicity, isActive, alert-definition). 6 KPIs x 2 tipos., validated_at=2026-08-25T14:40:00BRT |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| Familia | aida-alert |


---

### 19. `hwa-10.2.8-aida-alerts-default-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `alerts`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as alert definitions do AI Data Advisor ficam em um arquivo JSON dentro do HCL Workload Automation, recuperadas pelo AIDA Exporter e armazenadas no OpenSearch (indice alert-definitions); nao podem ser alteradas por usuarios. O pacote instala 12 definicoes default: para cada KPI de tendencia (jobs por folder/workstation/status/total, msgFileFill), uma definicao tipo continuous (10 anomalias CONSECUTIVAS em 60 min) e uma tipo total (10 anomalias TOTAIS em 60 min); para job history, continuous e total com value 2 e timeFrame 2880 min (2 dias); mais 2 para critical job incomplete predecessor (CONTINUOUS_INCOMPLETEPREDECESSOR_CRITICAL e TOTAL_INCOMPLETEPREDECESSOR_CRITICAL). Os usuarios podem pausar/resumir alertas (efeito imediato) e ativar/desativar a geracao, incluindo a opcao global Deactivate All Alerts. A sensibilidade pode ser ajustada via parametros ANOMALY_USE_TOLERANCE (default false), ANOMALY_FIXED_TOLERANCE (0.5), ANOMALY_PERCENTAGE_TOLERANCE (0.01), ALERT_ANOMALOUS_POINTS_REQUIRED e ALERT_ANOMALY_RANGE_MINUTES no common.env.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Alert definitions). Os 12 alert-definitions reais do lab (indice OpenSearch) batem exatamente: CONTINUOUS_*/TOTAL_* para JOBWKS/JOBFOLDER/JOBSTATUS/JOBTOTAL/MESSAGE com value=10 timeFrame=60. [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_alert_definition.html |
| Titulo da fonte | Alert definitions - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Alert definitions are contained in a json file inside HCL Workload Automation. It is retrieved by AIDA Exporter component and stored into the OpenSearch database. Alert definitions cannot be changed by users. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_alerts |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=aida |
| Status de revisao | verified |
| Tipo | other |
| verbs | status |
| Familia | aida-alerts |


---

### 20. `hwa-10.2.8-aida-concepts-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `concepts`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor (AIDA) define: KPI (indicador monitorado continuamente, ex.: numero de jobs concluidos no plano atual), Anomaly Source KPI (KPI cuja tendencia anomala disparou alerta), Correlated KPI (KPIs correlacionados adicionaveis a analise), Data Point (observacao singular de um KPI), Anomaly (ponto de dados fora da faixa esperada definida estatisticamente com base no historico), Alert (sequencia de anomalias de um KPI, ex.: 10 pontos consecutivos fora da faixa em 1 hora), Alert Instance (ocorrencia unica de um alerta, registrada no OpenSearch), Alert Severity (media dos desvios percentuais das anomalias que geraram o alerta; High > 30%, Medium 20-30%, Low < 20%), Anomaly Bounds (limites superior/inferior da faixa esperada), Alert Trigger (condicoes que definem um alerta; tipo continuous = pontos anomolos CONSECUTIVOS, total = pontos anomolos TOTAIS acima ou abaixo), Anomaly % (percentual de pontos fora da faixa no intervalo; <6 Low, 6-10 Medium, >10 High), Timerange (frequencia de checagem de anomalias, definida por PROPHET_ORCHESTRATOR schedule_alert do common.env) e Special Days (dias com sazonalidade - feriados, ferias - incluidos no modelo de predicao com tolerancia maior para evitar falsos positivos).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Basic concepts). Terminologia central do AIDA validada com os dados reais do lab (alert-definitions com trigger continuous/total value=10 timeFrame=60). [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_concepts.html |
| Titulo da fonte | Basic concepts - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Alert: Sequence of anomalies of a KPI. An alert is defined by a set of parameters and conditions... For example: 10 consecutive KPI data points that fall outside the expected range of values within 1 hour. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_concepts |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=aida |
| Status de revisao | verified |
| Tipo | other |
| Familia | aida-concepts |


---

### 21. `hwa-10.2.8-aida-credentials-0005`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `credentials`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as credenciais de conexao do AI Data Advisor ao servidor Workload Automation sao armazenadas CIFRADAS no OpenSearch (indice wa-credentials, doc id <host:port>), com a senha cifrada via openssl enc -AES-128-ECB -base64 -salt -pbkdf2 usando a chave derivada de OPENSSL_PASSWORD (definido no common.env). O fluxo interativo ./AIDA.sh add-credentials (ou config.sh add_credentials) coleta host (host:port), username, password, tipo de engine (y=distributed, n=zOS com engineName) e valida contra https://<host>/twsd/engine/info (distributed) ou /twsz/v1/<engineName>/engine/info (zOS). Para automacao sem TTY, chamar add_credentials <host> <user> <encrypted_password> direto no container aida-config (o dispatch final do config.sh so repassa 2 args: $1 $2).

> **ATENCAO / RESSALVAS DE USO:** Validado em lab: doc wa-credentials/_doc/wa-waserver:31116 com host/username/password (AES-128-ECB) / cypher='' / engine='d' / engineName=''. O fluxo interativo sem TTY corrompe os docs (host='n'/'y') - usar add_credentials com 3 args. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE. Quote oficial: "This password will be used to generate an encryption key to hide the Workload Automation server credentials" (ISO: senhas cifradas no banco).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| Titulo da fonte | AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | "This password will be used to generate an encryption key to hide the Workload Automation server credentials" (doc: segundo ISO, senhas devem ser cifradas no banco; parametro OPENSSL_PASSWORD do common.env define a chave) |
| Coletado em | 2026-08-25 |
| Capacidade | aida_credentials |
| Modo de operacao | mutate |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, aida-config + aida-es (OpenSearch), MDM_LAB com wauser, tested_commands=['docker exec aida-config bash -c "source /config.sh && add_credentials wa-waserver:31116 wauser <enc>"', 'GET aida-es:9200/wa-credentials/_search'], result=Doc gravado com host=wa-waserver:31116, username=wauser, password=cifrado AES-128-ECB, engine='d'. Senha gerada: echo -n '<pw>' | openssl enc -AES-128-ECB -base64 -salt -pbkdf2 -pass env:OPENSSL_PASSWORD., validated_at=2026-08-25T13:45:00BRT |
| Pre-condicoes | Confirmar versão 10.2.8, plataforma Distributed/Linux, autorização e backup/rollback aplicáveis antes da execução. |
| Impacto | Pode alterar estado operacional do AI Data Advisor (containers, configuração docker-compose/common.env, credenciais no OpenSearch); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar os arquivos de backup (docker-compose.yml.lab-bak*, common.env) e recriar os containers (./AIDA.sh down && ./AIDA.sh build-start) ou remover credenciais (delete_credentials). |
| Criterio de parada | Interromper diante de divergência de versão, falha de autenticação, OOM persistente, resolução DNS interna quebrada ou resultado inesperado. |
| Terminologia normalizada | command=add |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | mdm |
| verbs | add |
| Familia | aida-credentials |


---

### 22. `hwa-10.2.8-aida-es-oom-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `troubleshooting`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o container OpenSearch (aida-es) do AI Data Advisor pode falhar com ExitCode 137 / OOMKilled quando os limits de memoria default do docker-compose.yml (8G) e o heap default da JVM (metade do limite do cgroup) excedem a RAM disponivel no host; em maquinas com pouca RAM (ex.: 11.5GiB no lab), a correcao pratica e definir ES_JAVA_OPTS e OPENSEARCH_JAVA_OPTS=-Xms768m -Xmx768m, elevar o limit do es para 3G (reservation 1.5G) e reduzir limits de outros servicos (keycloak 768M, predictor 768M, ui 512M). O OpenSearch tambem exige vm.max_map_count >= 262144 no HOST (sysctl), nao dentro do container; o Dockerfile-es ja adiciona esta config ao /etc/sysctl.conf da imagem.

> **ATENCAO / RESSALVAS DE USO:** Causa raiz confirmada em lab via dmesg: 'Memory cgroup out of memory: Killed process (java) anon-rss:2089460kB' com limit 2G. Tambem notado: o AIDA.sh usa docker-compose.yml; o build do es baixa OpenSearch 2.19.6 e precisa de internet. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE.

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
| Citacao de suporte | If the Elasticsearch container fails to get up, verify the vm.max_map_count parameter is at minimum 262144 on the host machine (not inside the container). |
| Coletado em | 2026-08-25 |
| Capacidade | aida_troubleshoot |
| Modo de operacao | mutate |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, 11.5GiB RAM, Docker 29.7.2, tested_commands=['./AIDA.sh build-start', "docker inspect aida-es --format '{{.State.ExitCode}} {{.State.OOMKilled}}'", 'sudo dmesg | grep -i oom', 'sudo sysctl -w vm.max_map_count=262144'], result=Antes: ExitCode=137 OOMKilled=true RestartCount=9. Depois de ES_JAVA_OPTS=-Xms768m -Xmx768m + limit es 3G + reducao de outros limits: es Up estavel exit=0 oom=false; vm.max_map_count 65530->262144 persistido., validated_at=2026-08-25T13:35:00BRT |
| Pre-condicoes | Confirmar versão 10.2.8, plataforma Distributed/Linux, autorização e backup/rollback aplicáveis antes da execução. |
| Impacto | Pode alterar estado operacional do AI Data Advisor (containers, configuração docker-compose/common.env, credenciais no OpenSearch); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar os arquivos de backup (docker-compose.yml.lab-bak*, common.env) e recriar os containers (./AIDA.sh down && ./AIDA.sh build-start) ou remover credenciais (delete_credentials). |
| Criterio de parada | Interromper diante de divergência de versão, falha de autenticação, OOM persistente, resolução DNS interna quebrada ou resultado inesperado. |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| Familia | aida-es |


---

### 23. `hwa-10.2.8-aida-keycloak-email-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a seguranca de acesso ao AI Data Advisor usa Keycloak (deployment Docker): realm chamado 'aida', com usuarios default aidaadmin (senha admin, role aida-admin - permite login direto na UI do AIDA, trabalhar com todos os KPIs, gerenciar special days, customizar tuning e pausar alertas) e admin (senha admin, role keycloak-admin - acesso ao admin console do Keycloak para definir usuarios/passwords). O Keycloak admin console fica em https://<ip>:<porta>/keycloak/auth/admin. Se o Keycloak nao for usado, a autenticacao usa as roles do Dynamic Workload Console. A notificacao por email de alertas requer configuracao SMTP no common.env: SMTP_SERVER (hostname FQDN do SMTP), SMTP_PORT (porta TLS, ex.: 587), SENDER_MAILID (conta de email remetente), SENDER_MAILPWD (senha), RECIPIENT_MAILIDS (lista separada por virgula) e HOST_IP (IP:porta do AIDA). Alertas tambem aparecem no Anomaly Widget do Workload Dashboard e podem disparar event rules no HCL Workload Automation para abrir tickets.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Configuring security + Configuring email alert settings + Receiving alert notifications). Validado em lab: aidaadmin/admin autentica no realm aida (client nginx), role aida-admin confirmada no token JWT. [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_security.html |
| Titulo da fonte | Configuring security - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | "To manage access to AIDA, use Keycloak. ... userid: aidaadmin (default credential admin), role: aida-admin - With this role, a user can directly login to AIDA UI, from where... he can work with all KPIs, manage special days, customize prediction tuning parameters, and pause alerts." (credential default documentada; alterar em producao) |
| Coletado em | 2026-08-25 |
| Capacidade | aida_security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=aida |
| Status de revisao | verified |
| Tipo | other |
| verbs | login |
| Familia | aida-keycloak |


---

### 24. `hwa-10.2.8-aida-kpi-catalog-0009`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `kpis`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor define KPIs (Key Performance Indicators) com schema: name, metric_name (ex.: application_wa_JobsInPlanCount_job_total), frequency (240 segundos = METRICS_FETCH_INTERVAL), category (Jobs|Queue), subcategory (Trend|Trend_by_wks), type (total quando sem keyprop), keyprop (jobstatus quando quebra por status de job), keyPropValues ([SUCCESSFUL, UNDECIDED, WAITING, ERROR, BLOCKED, SUPPRESS, READY, HELD, RUNNING, CANCELED]), labels ([workstation] quando por workstation), workstation (ex.: /MDMDA), metric_description, esQuery (agregacao OpenSearch: match metricname + term properties.parsedTag + match properties.jobstatus + term properties.workstation), alert-definition (definicoes de alerta vinculadas, ex.: [TOTAL_JOBTOTAL]), isActive. O doc id e '<name><metric_name><tag>'. O exporter baixa os KPIs do MDM (GET /twsd/engine/definition/kpi) e os armazena no indice kpis-definition.

> **ATENCAO / RESSALVAS DE USO:** Extraido do indice OpenSearch kpis-definition do lab (6 docs reais). keyPropValues com os 10 status de job padrao. Workstations reais do lab: /MDMDA e /MDMXA. [Observado em laboratorio HWA 10.2.8 WSL2]

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
| Citacao de suporte | name: 'Number total jobs in plan', metric_name: 'application_wa_JobsInPlanCount_job_total', frequency: 240, category: 'Jobs', subcategory: 'Trend', type: 'total', alert-definition: ['TOTAL_JOBTOTAL'] |
| Coletado em | 2026-08-25 |
| Capacidade | aida_kpis |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, OpenSearch aida-es, tested_commands=['GET aida-es:9200/kpis-definition/_search?size=50'], result=6 KPI definitions reais com schema completo (name, metric_name, frequency 240, category, subcategory, keyprop/keyPropValues, esQuery, alert-definition, isActive)., validated_at=2026-08-25T14:42:00BRT |
| Terminologia normalizada | command=twsd |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | mdm |
| verbs | status |
| Familia | aida-kpi |


---

### 25. `hwa-10.2.8-aida-kpi-types-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `kpis`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor monitora KPIs definidos em um arquivo JSON dentro do HCL Workload Automation (nao modificaveis por usuarios do AIDA), expostos segundo o padrao OpenMetrics. Os KPIs sao: (1) Number of jobs in plan by folder (by status), metric application_wa_JobsByFolder_jobs, divisao por job status (10), frequencia 240s; (2) Number of jobs in plan by workstation (by status), application_wa_JobsByWorkstation_jobs, frequencia 240s; (3) Number of jobs in plan by status, application_wa_JobsInPlanCount_job, frequencia 240s; (4) Number of total jobs in plan, application_wa_JobsInPlanCount_job_total, frequencia 240s; (5) Job history (start time & duration), metric job_history, divisao start time/duration, frequencia 86400s (diaria); (6) Available space for WA message files, application_wa_msgFileFill_percent, divisao por 12 queues, frequencia 240s. Os 10 job status sao: WAITING, READY, RUNNING, SUCCESSFUL, ERROR, CANCELED, HELD, UNDECIDED, BLOCKED, SUPPRESS. As 12 queues incluem Appserverbox.msg, Courier.msg, mirrorbox.msg, Mailbox.msg, Monbox.msgn, Moncmd.msg, auditbox.msg, clbox.msg, planbox.msg, Intercom.msg, pobox messages, server.ms.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (KPIs for HWA). Os 6 KPIs reais do lab (kpis-definition no OpenSearch) batem com esta tabela: application_wa_JobsInPlanCount_job_total, application_wa_JobsInPlanCount_job, application_wa_JobsByWorkstation_jobs, application_wa_JobsByFolder_jobs, application_wa_msgFileFill_percent. [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_WA_KPIs.html |
| Titulo da fonte | KPIs for HCL Workload Automation - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | KPIs definitions and KPIs metrics cannot be modified by AIDA users. ... HCL Workload Automation and HCL Workload Automation for Z expose metrics and KPIs definitions according to the OpenMetrics standard. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_kpis |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| verbs | plan; start; status |
| Familia | aida-kpi |


---

### 26. `hwa-10.2.8-aida-metric-format-0010`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `metrics`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor armazena as metricas coletadas do Workload Automation no indice OpenSearch metric-index-<data> (ex.: metric-index-08-25-2026) com schema: metricname (ex.: application_wa_JobsInPlanCount_job_total), category (Jobs), subcategory (Trend), value (numero), @timestamp (epoch millis), properties (jobstatus quando quebra por status, mp_scope: application, parsedTag: wawaserver31116), tag (wa-waserver:31116), parsedTag (tag sem caracteres especiais), uuid, e keyprop (jobstatus) quando a metrica quebra por status. Exemplo real: {"metricname":"application_wa_JobsInPlanCount_job","keyprop":"jobstatus","properties":{"jobstatus":"SUCCESSFUL","mp_scope":"application","parsedTag":"wawaserver31116"},"value":26,"tag":"wa-waserver:31116"}. O aida-predictor e o aida-ad consomem essas series temporais.

> **ATENCAO / RESSALVAS DE USO:** Extraido do indice OpenSearch metric-index do lab (amostra real). @timestamp em epoch millis. [Observado em laboratorio HWA 10.2.8 WSL2]

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
| Citacao de suporte | {"metricname":"application_wa_JobsInPlanCount_job_total","category":"Jobs","subcategory":"Trend","value":235,"@timestamp":1787677029521,"tag":"wa-waserver:31116","parsedTag":"wawaserver31116"} |
| Coletado em | 2026-08-25 |
| Capacidade | aida_monitoring |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, OpenSearch aida-es, tested_commands=['GET aida-es:9200/metric-index-*/_search?size=5'], result=Schema de metrica confirmado: metricname, value, @timestamp (epoch millis), properties{jobstatus,mp_scope,parsedTag}, tag, parsedTag, uuid., validated_at=2026-08-25T14:44:00BRT |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| verbs | status |
| Familia | aida-metric |


---

### 27. `hwa-10.2.8-aida-network-host-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `networking`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, quando o Dynamic Workload Console/MDM engine rodam no HOST (fora do docker) e o AI Data Advisor roda em containers, os servicos AIDA precisam resolver o hostname do servidor WA (ex.: wa-waserver) via rede docker; em lab com host-only, e necessario adicionar extra_hosts no docker-compose.yml (ex.: 'wa-waserver:host-gateway', 'MDMHOST:host-gateway', 'host.docker.internal:host-gateway') para os containers alcancarem o gateway do host (<gateway>). Sem isso, o aida-exporter falha com NameResolutionError ('Failed to resolve wa-waserver').

> **ATENCAO / RESSALVAS DE USO:** Validado em lab: apos adicionar extra_hosts nos 11 servicos, resolucao OK (wa-waserver-><gateway>) e /metrics do MDM respondeu 200. O doc oficial assume resolucao DNS; em lab com host-only, extra_hosts e a solucao. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE.

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
| Citacao de suporte | Verify that the DWC_PUBLIC_KEY parameter in the common.env file is set to the DWC public key of the Liberty SSL certificates. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_troubleshoot |
| Modo de operacao | mutate |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, Docker bridge docker-deployment_aida-net, MDM em <host>:31116, tested_commands=['adicionar extra_hosts wa-waserver/MDMHOST/host.docker.internal:host-gateway nos 11 servicos', 'docker compose up -d', "docker exec aida-exporter python3 -c 'import socket; socket.gethostbyname(...)'"], result=Antes: NameResolutionError 'Failed to resolve wa-waserver'. Depois: wa-waserver-><gateway>, MDMHOST-><gateway>, aida-es-><gateway>; exporter acessou https://wa-waserver:31116/metrics com 200., validated_at=2026-08-25T13:40:00BRT |
| Pre-condicoes | Confirmar versão 10.2.8, plataforma Distributed/Linux, autorização e backup/rollback aplicáveis antes da execução. |
| Impacto | Pode alterar estado operacional do AI Data Advisor (containers, configuração docker-compose/common.env, credenciais no OpenSearch); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar os arquivos de backup (docker-compose.yml.lab-bak*, common.env) e recriar os containers (./AIDA.sh down && ./AIDA.sh build-start) ou remover credenciais (delete_credentials). |
| Criterio de parada | Interromper diante de divergência de versão, falha de autenticação, OOM persistente, resolução DNS interna quebrada ou resultado inesperado. |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | mdm |
| Familia | aida-network |


---

### 28. `hwa-10.2.8-aida-retrain-specialdays-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `prediction`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor executa um retrain automatico de todos os KPIs a cada 24 horas (iniciado no start do container Orchestrator); durante o retrain a area de predicao nao fica visivel. Os Special Days (feriados por pais ou datas customizadas, com propriedades name/date/repeat/end repeat/description/status Active|Draft e opcoes de repeticao daily/weekly/monthly/yearly) sao incluidos no modelo de predicao com nivel de tolerancia MAIOR que dias normais, para evitar alertas falsos positivos em datas sazonais (feriados, ferias, ciclos de negocio). O tuning de predicao por KPI permite ajustar a sensibilidade de deteccao de anomalias (mais sensibilidade = mais anomalias detectadas); o Global tuning sobrescreve todos os KPIs e as mudancas sao aplicadas apos o proximo retrain. O timerange (frequencia de checagem de anomalias) e definido pelo parametro PROPHET_ORCHESTRATOR schedule_alert do common.env (default 15 minutos).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Managing special days + Managing KPIs). No lab, o special-days-labels tem 95 docs (feriados por estado/pais, ex.: AO, AR, AW) e o PROPHET_ORCHESTRATOR do common.env confirmado como {"schedule":1440,"schedule_alert":15}. [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_special_days.html |
| Titulo da fonte | Managing special days - AI Data Advisor (AIDA) User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AIDA prediction model is automatically retrained every 24 hours. ... Every 24 hours AIDA runs an automatic retrain of all KPIs. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_predict |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| verbs | start; status |
| Familia | aida-retrain |


---

### 29. `hwa-10.2.8-aida-special-days-0011`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `prediction`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor usa o indice OpenSearch special-days-labels (95 docs) com feriados por estado/regiao para modelar sazonalidade no predictor: schema state (ex.: AO, AR, AW) e names (lista de nomes de feriados no idioma local, ex.: 'Ano novo', 'Carnaval', 'Dia Internacional da Mulher' para AO; 'Ano Nuevo [New Year's Day]' para AR). Esses feriados alimentam o modelo de predicao (prophet/neural) para ajustar as bandas de confianca em datas especiais.

> **ATENCAO / RESSALVAS DE USO:** Extraido do indice OpenSearch special-days-labels do lab (95 docs). [Observado em laboratorio HWA 10.2.8 WSL2]

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
| Citacao de suporte | {"state":"AO","names":["Ano novo","Carnaval","Dia Internacional da Mulher",...]} |
| Coletado em | 2026-08-25 |
| Capacidade | aida_predict |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, AIDA containers, OpenSearch aida-es, tested_commands=['GET aida-es:9200/special-days-labels/_search?size=3'], result=95 docs com feriados por estado (state + names). Ex.: AO, AR, AW., validated_at=2026-08-25T14:46:00BRT |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| Familia | aida-special |


---

### 30. `hwa-10.2.8-aida-ui-0007`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `ui`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a interface do AI Data Advisor (UI web) e acessivel em https://<aida-ip>:9432/ (porta default configurável via AIDA.sh set-custom-port) e responde HTTP 200 com uma SPA React (title 'AI Data Advisor (AIDA)'); o endpoint /healthz responde 200. O nginx do AIDA valida o header Host contra EXTERNAL_HOSTNAME (parametro do common.env, obrigatorio para evitar HTTP Host Header attacks): acessar via hostname/porta diferente (ex.: localhost vs <host>) retorna HTTP 405 'Host not matching'. Com Keycloak configurado, a UI e acessivel diretamente (https://aida-ip:9432/); sem Keycloak, o AIDA e acessado pelo widget de alerta no Workload Dashboard do DWC.

> **ATENCAO / RESSALVAS DE USO:** Validado em lab: <host>:9432 -> 200 (SPA 'AI Data Advisor (AIDA)'), /healthz -> 200; localhost:9432 -> 405 'Host not matching'. OpenSearch cluster yellow (1 node, esperado). DWC (9443) e MDM (31116) saudaveis durante o teste. [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE.

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
| Citacao de suporte | To prevent HTTP Host Header attacks, in the common.env file add the string EXTERNAL_HOSTNAME=IP where IP is the IP address of the machine where AIDA is being installed. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_ui |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, EXTERNAL_HOSTNAME=<host>, aida-nginx 0.0.0.0:9432, tested_commands=['curl -sk https://<host>:9432/', 'curl -sk https://<host>:9432/healthz', 'curl -sk https://localhost:9432/', 'GET aida-es:9200/_cluster/health'], result=<host>:9432 -> 200 (SPA React, title 'AI Data Advisor (AIDA)'); /healthz -> 200; localhost:9432 -> 405 'Host not matching, check the EXTERNAL_HOSTNAME environment variable'; cluster yellow 1 node., validated_at=2026-08-25T13:55:00BRT |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | set |
| Familia | aida-ui |


---

### 31. `hwa-10.2.8-capacity-en-event-driven-0005`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `globalopts`

**Afirmacao / Conteudo:**

A opção global enEventDrivenWorkloadAutomation (ed) no HCL Workload Automation 10.2.8 habilita ou desabilita a funcionalidade de event-driven workload automation, com padrão yes.

> **ATENCAO / RESSALVAS DE USO:** Requer JnextPlan e start/stopevtp ao habilitar/desabilitar.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enEventDrivenWorkloadAutomation=ed, event-driven workload automation=automação de carga orientada a eventos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | Enable event-driven workload automation. Enable or disable the event-driven workload automation feature... The default value is yes. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | globalopts_event_driven |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['optman ls', 'optman chg sh=401 (controle positivo, restaurado para 400)'], result=optman ls: enEventDrivenWorkloadAutomation / ed = YES. Default confirmado no lab 10.2.8., validated_at=2026-08-23T01:50:00BRT |
| Tipo | other |
| Familia | capacity-en |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção global enEventDrivenWorkloadAutomation (ed) no HCL Workload Automation 10.2.8 habilita ou desabilita a funcionalidade de event-driven workload automation, com padrão yes?
- Qual o propósito e valor padrão da opção global enEventDrivenWorkloadAutomation no optman do HWA?


---

### 32. `hwa-10.2.8-capacity-job-limit-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 o limite de jobs pode ser definido de duas formas documentadas: na definição do job stream, usando o argumento job limit, ou na definição da workstation, usando o comando limit cpu; por exemplo, definir o limite de uma workstation em 25 permite no máximo 25 jobs rodando concorrentemente nela.

> **ATENCAO / RESSALVAS DE USO:** Distingue limit cpu (workstation) versus limit job/limit sched (job stream).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | job limit=limite de job, limit cpu=limite de workstation |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsettinglimits.html |
| Titulo da fonte | Setting limits |
| Citacao de suporte | You can set a limit: In the job stream definition using the job limit argument; In the workstation definition using the limit cpu command... Setting the limit on a workstation to 25... allows... no more than 25 jobs running concurrently on that workstation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | capacity_limit_cpu |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | limit |
| Familia | capacity-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 o limite de jobs pode ser definido de duas formas documentadas: na definição do job stream, usando o argumento job limit, ou na definição da workstation, usando o comando limit cpu; por exemplo, definir o limite de uma workstation em 25 permite no máximo 25 jobs rodando concorrentemente nela?


---

### 33. `hwa-10.2.8-capacity-limit-cpu-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

O limite padrão documentado do número de jobs que podem rodar simultaneamente em uma workstation no HCL Workload Automation 10.2.8 é 1000 para cloud task launcher e 100 para todos os outros tipos de workstation.

> **ATENCAO / RESSALVAS DE USO:** Default per workstation type; o comando limit cpu permite alterar esse limite e exige acesso limit. O comportamento READY de limite 0 foi omitido desta unidade conforme escopo.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | limit cpu=limite de jobs simultâneos por workstation, cloud task launcher=cloud task launcher, job limit=limite de jobs |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_limitcpu.html |
| Titulo da fonte | limit cpu |
| Citacao de suporte | For cloud task launcher, the default value is 1000 and for all other types of workstations the value is 100. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | capacity_workstation_limits |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | limit |
| Familia | capacity-limit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O limite padrão documentado do número de jobs que podem rodar simultaneamente em uma workstation no HCL Workload Automation 10.2.8 é 1000 para cloud task launcher e 100 para todos os outros tipos de workstation?


---

### 34. `hwa-10.2.8-capacity-log-cleanup-frequency-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

A opção global logCleanupFrequency (lc) no HCL Workload Automation 10.2.8 define com que frequência a limpeza automática de instâncias de log (event rule e audit management) é executada, com valores válidos de 0 a 60 minutos e padrão 5 minutos; valor 0 desativa a limpeza automática.

> **ATENCAO / RESSALVAS DE USO:** Opção global de gerenciamento de logs relacionada a performance/concorrência.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | logCleanupFrequency=lc, Log cleanup frequency=frequência de limpeza de log |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | Specify how often the automatic cleanup of log instances is run. Valid values are in the 0-60 minutes range... The default value is 5 minutes. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['optman ls', 'optman chg sh=401 (controle positivo, restaurado para 400)'], result=optman ls: logCleanupFrequency / lc = 5. Default confirmado no lab 10.2.8., validated_at=2026-08-23T01:50:00BRT |
| Tipo | other |
| Familia | capacity-log |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: A opção global logCleanupFrequency (lc) no HCL Workload Automation 10.2.8 define com que frequência a limpeza automática de instâncias de log (event rule e audit management) é executada, com valores válidos de 0 a 60 minutos e padrão 5 minutos; valor 0 desativa a limpeza automática?
- Qual o propósito e valor padrão da opção global logCleanupFrequency no optman do HWA?


---

### 35. `hwa-10.2.8-capacity-log-history-0007`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

A opção global logHistory (lh) no HCL Workload Automation 10.2.8, usada na gestão de event rules, especifica o número de dias em que dados de regra, ação e mensagem são salvos, com padrão 10 dias e descarte FIFO (first-in first-out).

> **ATENCAO / RESSALVAS DE USO:** Controla retenção de logs de event rule management; afeta o consumo de disco conforme o volume de regras.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | logHistory=lh, Log history period=período de histórico de log, FIFO=FIFO |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | Enter the number of days for which you want to save rule instance, action run, and message log data... The default value is 10 days. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['optman ls', 'optman chg sh=401 (controle positivo, restaurado para 400)'], result=optman ls: logHistory / lh = 10. Default confirmado no lab 10.2.8., validated_at=2026-08-23T01:50:00BRT |
| Tipo | other |
| Familia | capacity-log |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: A opção global logHistory (lh) no HCL Workload Automation 10.2.8, usada na gestão de event rules, especifica o número de dias em que dados de regra, ação e mensagem são salvos, com padrão 10 dias e descarte FIFO (first-in first-out)?
- Qual o propósito e valor padrão da opção global logHistory no optman do HWA?


---

### 36. `hwa-10.2.8-capacity-oracle-tablespace-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não fornece uma fórmula quantitativa genérica de dimensionamento do banco de dados em função do número de jobs; apenas o exemplo Oracle 500000 jobs/dia com ~80GB .dbf.

> **ATENCAO / RESSALVAS DE USO:** Página v1028 'Oracle tablespace size' (awsadOracletablespace.html) lida: contém apenas o exemplo '500000 jobs per day, 80GB of .dbf file size is recommended', sem fórmula genérica por job. IBM Detailed System Requirements 10.2.7 confirma que o espaço é subjetivo ('The space required is very subjective'). Buscas Perplexity não encontraram fórmula oficial KB/job; fórmulas encontradas (ex.: 13KB/job) são de CA Workload Automation DE (Broadcom), não aplicáveis ao HWA. Achado negativo confirmado; claim promovida de insufficient para verified.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Oracle tablespace=tablespace Oracle, 500000 jobs/dia=500000 jobs per day, 80GB .dbf=80GB of .dbf file size, database sizing=dimensionamento do banco de dados |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadOracletablespace.html |
| Titulo da fonte | Oracle tablespace size |
| Citacao de suporte | For example, considering a workload of 500000 jobs per day, 80GB of .dbf file size is recommended. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | database_sizing |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | capacity-oracle |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não fornece uma fórmula quantitativa genérica de dimensionamento do banco de dados em função do número de jobs; apenas o exemplo Oracle 500000 jobs/dia com ~80GB?


---

### 37. `hwa-10.2.8-capacity-oracle-tablespace-size-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

A documentação de performance do HCL Workload Automation 10.2.8 recomenda, para Oracle (RDBMS), alocar tamanho adequado de tablespace/datafile e, como exemplo, para uma carga de 500000 jobs por dia recomenda cerca de 80GB de tamanho de arquivo .dbf.

> **ATENCAO / RESSALVAS DE USO:** Exemplo quantitativo oficial de dimensionamento de banco para 500000 jobs/dia em Oracle; não é uma fórmula genérica para N jobs.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tablespace=tablespace Oracle, datafile=.dbf |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadOracletablespace.html |
| Titulo da fonte | Oracle tablespace size |
| Citacao de suporte | considering a workload of 500000 jobs per day, 80GB of .dbf file size is recommended. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | database_sizing |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | capacity-oracle |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação de performance do HCL Workload Automation 10.2.8 recomenda, para Oracle (RDBMS), alocar tamanho adequado de tablespace/datafile e, como exemplo, para uma carga de 500000 jobs por dia recomenda cerca de 80GB de tamanho de arquivo?


---

### 38. `hwa-10.2.8-capacity-stats-history-0008`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `stdlist`

**Afirmacao / Conteudo:**

A opção global statsHistory (sh) no HCL Workload Automation 10.2.8 especifica por quantos dias as estatísticas de jobs são mantidas, com padrão 400 dias e descarte FIFO; a documentação afirma que isso não afeta os arquivos stdlist de jobs, que devem ser removidos com o comando rmstdlist.

> **ATENCAO / RESSALVAS DE USO:** Retenção de estatísticas afeta consumo de disco do banco; stdlist exige rmstdlist.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | statsHistory=sh, Job statistics history period=período de histórico de estatísticas de jobs, stdlist=arquivos de saída padrão |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | Specify the number of days for which you want to maintain job statistics... The default value is 400. This has no effect on job standard list files, which must be removed with the rmstdlist command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | stdlist |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['optman ls', 'optman chg sh=401 (controle positivo, restaurado para 400)'], result=optman ls: statsHistory / sh = 400 (dias de retencao). optman chg sh=401 -> AWSJCL050I Command "chg" completed successfully; sh passou a 401; restaurado para 400 com AWSJCL050I. Mecanismo de change validado., validated_at=2026-08-23T01:50:00BRT |
| Tipo | other |
| Familia | capacity-stats |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção global statsHistory (sh) no HCL Workload Automation 10.2.8 especifica por quantos dias as estatísticas de jobs são mantidas, com padrão 400 dias e descarte FIFO; a documentação afirma que isso não afeta os arquivos stdlist de jobs, que devem ser removidos com o comando rmstdlist?


---

### 39. `hwa-10.2.8-capacity-stdlist-retention-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `stdlist`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 a retenção dos arquivos stdlist (standard list) de jobs não é controlada por uma opção global de dias, mas pelo comando rmstdlist; a documentação global options afirma que os arquivos stdlist devem ser removidos com o comando rmstdlist.

> **ATENCAO / RESSALVAS DE USO:** Não há opção global documentada de retenção automática de stdlist por dias; a gestão é via rmstdlist.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | stdlist=arquivos de saída padrão, rmstdlist=comando de remoção de stdlist |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | This has no effect on job standard list files, which must be removed with the rmstdlist command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | stdlist |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | capacity-stdlist |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 a retenção dos arquivos stdlist (standard list) de jobs não é controlada por uma opção global de dias, mas pelo comando rmstdlist; a documentação global options afirma que os arquivos stdlist devem ser removidos com o comando rmstdlist?


---

### 40. `hwa-10.2.8-capacity-workstation-limit-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `globalopts`

**Afirmacao / Conteudo:**

Não há opção global documentada no HCL Workload Automation 10.2.8 chamada 'Number of submitted jobs' nem 'Limit of number of available workstations'; a opção documentada que controla limite de workstation é workstationLimit (wl).

> **ATENCAO / RESSALVAS DE USO:** Página completa de opções globais v1028 (awsadgloboptdescr.html) lida integralmente: não existe opção 'Number of submitted jobs' nem 'Limit of number of available workstations'; a única opção de limite de workstation é workstationLimit (wl), usada no registro automático de dynamic agents (default 100, faixa 0-1024). Buscas Perplexity não revelaram opção global documentada controlando jobs submetidos/concorrentes; limites de concorrência são por workstation (atributo Limit via conman lc) e por agente dinâmico (ExecutorsMinThreads/ExecutorsMaxThreads no JobManager.ini). Achado negativo confirmado; claim promovida de insufficient para verified.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | workstationLimit=wl, Number of submitted jobs=opção global não documentada, Limit of number of available workstations=opção global não documentada |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | workstationLimit | wl **The workstation limit.** Used in the automatic dynamic agent registration. This parameter specifies the dynamic agent workstation limit value that the dynamic agent workstation assumes after the workstation is added to the plan. You can later modify the dynamic agent workstation limit value by using the conman command line or the Dynamic Workload Console. Valid values are in the *0-1024* range. The default is *100*. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | globalopts_workstationlimit |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | limit |
| Familia | capacity-workstation |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Não há opção global documentada no HCL Workload Automation 10.2.8 chamada 'Number of submitted jobs' nem 'Limit of number of available workstations'; a opção documentada que controla limite de workstation é workstationLimit (wl)?


---

### 41. `hwa-10.2.8-certman-generate-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, o comando 'certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>]' gera um novo Certificate Authority (CA) e certificados TLS; keypasswd (minimo 6 caracteres) e outpath sao obrigatorios; o comando modifica permissoes apenas para novos arquivos criados no outpath; para definir wauser/wagroup o usuario que executa deve ter permissao de alterar owner e group.

> **ATENCAO / RESSALVAS DE USO:** Credential_sensitive (lida com senhas de chave privada e CA). Senhas com metacaracteres/wildcards devem ser entre aspas simples. Sintaxe usa prefixo '-' (certman nao segue o padrao '=' do OCLI). Recomendado salvar ca.key para futuras geracoes.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=certman generate, interface=certman, object=certificate authority (CA) and TLS certificates, required_options=keypasswd, outpath, optional_options=days, subj, keysize, cakeypasswd, cadays, casubj, wauser, wagroup, syntax=certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>], output_files=ca.crt, ca.key, tls.crt, tls.key, tls.sth |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman_gen.html |
| Titulo da fonte | Generate new certificates and a Certificate Authority (CA) |
| Citacao de suporte | certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>] |
| Coletado em | 2026-08-16 |
| Classificacao de risco | credential_sensitive |
| Capacidade | cert |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | certman |
| object_hint | generate |
| Familia | certman-generate |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, o comando 'certman generate -keypasswd <key pwd> -outpath <output path> [-days <valid days>] [-subj <full subject>] [-keysize <key size in bits>] [-cakeypasswd <ca key pwd>] [-cadays <ca valid days>] [-casubj <ca full subject>] [-wauser <user>] [-wagroup <group>]' gera um novo Certificate Authority (CA) e certificados TLS; keypasswd (minimo 6 caracteres) e outpath sao obrigatorios; o comando modifica permissoes apenas para novos arquivos criados no outpath; para definir wauser/wagroup o usuario que executa deve ter permissao de alterar owner e group?


---

### 42. `hwa-10.2.8-certman-location-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, a ferramenta Certman fica em TWS_INST_DIR/TWS/bin e suporta as acoes generate (novo CA), generate a partir de CA existente, extract de certificados de um keystore/truststore existente no master domain manager, verify da validade dos certificados, import de certificados do master domain manager para o Dynamic Workload Console e remove de um alias do keystore/truststore; Certman nao e suportado em sistemas operacionais IBM i; a versao pode ser verificada com 'certman version'.

> **ATENCAO / RESSALVAS DE USO:** Certman e um recurso novo a partir da versao 10.2.3 (Intel de introducao). Nao confundir com o fluxo OCLI. Not supported on IBM i.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=certman, interface=certman, path=TWS_INST_DIR/TWS/bin, actions=generate, generate from existing CA, extract, verify, import, remove alias, version_command=certman version, not_supported=IBM i operating systems |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman.html |
| Titulo da fonte | Managing certificates using Certman |
| Citacao de suporte | You can find Certman at the following path: TWS_INST_DIR/TWS/bin |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | certman |
| verbs | import; remove; verify |
| Familia | certman-location |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a ferramenta Certman fica em TWS_INST_DIR/TWS/bin e suporta as acoes generate (novo CA), generate a partir de CA existente, extract de certificados de um keystore/truststore existente no master domain manager, verify da validade dos certificados, import de certificados do master domain manager para o Dynamic Workload Console e remove de um alias do keystore/truststore; Certman nao e suportado em sistemas operacionais IBM i; a versao pode ser verificada com 'certman version'?


---

### 43. `hwa-10.2.8-certman-output-files-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, 'certman generate' produz na pasta outpath os arquivos ca.crt (Root CA), ca.key (chave privada da CA), tls.crt (certificado assinado e validado pela CA), tls.key (chave privada do certificado tls) e tls.sth (stash file do certificado contendo a senha codificada em Base64); a documentacao recomenda salvar ca.key para poder gerar ou substituir certificados no futuro e adicionar a CA ao SO e ao browser para confianca.

> **ATENCAO / RESSALVAS DE USO:** Informa sobre a natureza dos artefatos (stash contem senha codificada) - util para treinamento de manipulacao segura de certificados. ca.key deve ser protegido.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=certman generate, interface=certman, object=CA and certificate output files, ca_file=ca.crt (Root CA), ca.key (CA private key), tls_files=tls.crt, tls.key, tls.sth (stash with Base64 encoded password), recommendation=save ca.key; add CA to OS and browser trust |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman_gen.html |
| Titulo da fonte | Generate new certificates and a Certificate Authority (CA) |
| Citacao de suporte | The following output files are the CA and certificates you can find in the specified output folder: ca.crt, ca.key, tls.crt, tls.key, tls.sth |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | certman |
| object_hint | generate |
| Familia | certman-output |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, 'certman generate' produz na pasta outpath os arquivos ca?


---

### 44. `hwa-10.2.8-certman-version-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, a versao da ferramenta Certman pode ser verificada executando o comando 'certman version'; qualquer comando Certman tambem informa a localizacao dos arquivos de log.

> **ATENCAO / RESSALVAS DE USO:** Claim dedicado criado a partir da ressalva da auditoria para alinhar semanticamente o candidate function-call certman_version. Somente leitura.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=certman version, interface=certman, object=certman tool version, output=certman version number and log file location |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman.html |
| Titulo da fonte | Managing certificates using Certman |
| Citacao de suporte | To verify the version of Certman you are using, you can run the following command: certman version. Running any command of Certman, you can also see where the logs file is located. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | certman |
| verbs | version |
| Familia | certman-version |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, a versao da ferramenta Certman pode ser verificada executando o comando 'certman version'; qualquer comando Certman tambem informa a localizacao dos arquivos de log?


---

### 45. `hwa-10.2.8-cli-jwt-mutex-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `jwt`

**Afirmacao / Conteudo:**

In HWA CLI connection parameters, JWT token authentication is mutually exclusive with username and password.

> **ATENCAO / RESSALVAS DE USO:** Mutual exclusivity in authentication options.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsetupui.html |
| Titulo da fonte | Configuring UI and CLI connections |
| Citacao de suporte | When configuring CLI connections, JWT authentication cannot be used simultaneously with user and password parameters. |
| Coletado em | 2026-08-16 |
| Capacidade | jwt |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=cli |
| Status de revisao | verified |
| Tipo | other |
| Familia | cli-jwt |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: In HWA CLI connection parameters, JWT token authentication is mutually exclusive with username and password?


---

### 46. `hwa-10.2.8-dbviews-events-0170`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

As views de evento do banco do HCL Workload Automation: EVENT_RULES_V (event rules definidas), EVENT_CONDITIONS_V (eventos associados a cada event rule), EVENT_RULE_ACTIONS_V (acoes associadas a cada event rule), EVENT_RULE_INSTANCES_V (historico de event rules executadas), ACTION_RUNS_V (acoes executadas por cada event rule), ACTION_PARAMETERS_V (parametros associados as acoes executadas) e LOG_MESSAGES_V (mensagens logadas pelas acoes). Usadas para auditoria e diagnostico de event-driven workload automation (EDWA). Fonte: IBM Workload Scheduler Database Views.

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
| Titulo da fonte | IBM Workload Scheduler Database Views - Event views |
| Citacao de suporte | EVENT_RULES_V displays information about event rules. EVENT_RULE_INSTANCES_V displays information about run event rule history. |
| Coletado em | 2026-08-23 |
| Capacidade | log |
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
| Familia | dbviews-events |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual é o propósito da view de banco EVENT_RULE_INSTANCES_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional EVENT_RULE_INSTANCES_V no banco de dados do HWA?


---

### 47. `hwa-10.2.8-dbviews-job-history-0168`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

A view JOB_HISTORY_V do banco do HCL Workload Automation exibe informacoes sobre o historico de jobs (jobs executados e seus resultados). E a view principal para queries e reports de historico de execucao de jobs, incluindo campos como workstation, job name, start time e status. Usada em reports de producao (ex.: consultas com WHERE sobre Workstation_name, Job_name, Job_start_time). Fonte: IBM Workload Scheduler Database Views (JOB_HISTORY_V).

> **ATENCAO / RESSALVAS DE USO:** Extraido do awsdvmst.pdf. Correlaciona com AWSWUI0331E (query SQL com JOB_HISTORY_V).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | IBM Workload Scheduler Database Views - JOB_HISTORY_V |
| Citacao de suporte | JOB_HISTORY_V displays information about job history. |
| Coletado em | 2026-08-23 |
| Capacidade | db_views_job_history |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; referencia. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | scheduler |
| verbs | start; status |
| Familia | dbviews-job |

**Perguntas relacionadas:**

- Como consultar dependências e definições utilizando a view JOB_HISTORY_V no banco de dados?
- Qual é o propósito da view de banco JOB_HISTORY_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional JOB_HISTORY_V no banco de dados do HWA?


---

### 48. `hwa-10.2.8-dbviews-plan-jobs-0169`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

As views PLAN_JOBS_V e PLAN_JOB_STREAMS_V do banco do HCL Workload Automation exibem informacoes sobre os jobs e job streams no plano de producao corrente. As views PLAN_JOB_PREDECESSORS_V, PLAN_JOB_SUCCESSORS_V, PLAN_JOB_STREAM_PREDECESSORS_V e PLAN_JOB_STREAM_SUCCESSORS_V exibem os predecessores/sucessores de jobs e job streams no plano — usadas para consultas de dependencias e critical network. Fonte: IBM Workload Scheduler Database Views.

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
| Titulo da fonte | IBM Workload Scheduler Database Views - PLAN views |
| Citacao de suporte | PLAN_JOBS_V displays information about jobs in the plan. PLAN_JOB_SUCCESSORS_V displays information about jobs and job streams successors of a job in the plan. |
| Coletado em | 2026-08-23 |
| Capacidade | db_views_plan |
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
| Familia | dbviews-plan |

**Perguntas relacionadas:**

- Como consultar dependências e definições utilizando a view PLAN_JOB_SUCCESSORS_V no banco de dados?
- Como consultar dependências e definições utilizando a view PLAN_JOB_STREAMS_V no banco de dados?
- Qual é o propósito da view de banco PLAN_JOBS_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional PLAN_JOB_STREAMS_V no banco de dados do HWA?


---

### 49. `hwa-10.2.8-dwc-default-tasks-language-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_ui` / `language`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, as default tasks (predefined tasks) do Dynamic Workload Console sao criadas no idioma configurado no navegador no PRIMEIRO login do usuario e NAO sao traduzidas quando o idioma do navegador muda depois; para ter as default tasks em outro idioma, o administrador Liberty deve criar um novo usuario do DWC e faze-lo fazer o primeiro login com o navegador configurado nesse idioma. A propriedade precannedTaskCreation do TdwcGlobalSettings.xml (valores all|none|distributed|zos) controla se/quais tasks pre-definidas sao criadas e e lida apenas no primeiro login do usuario.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Troubleshooting browsers). Complementa hwa-10.2.8-dwc-ui-language-0001: a UI acompanha o navegador, mas as default tasks ficam no idioma do primeiro login. precannedTaskCreation documentado em Customizing your global settings (awsadglobsetcustom.html).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrdefaulttasks.html |
| Titulo da fonte | Default tasks are not converted into the language set in the browser - Troubleshooting - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The default tasks are created, using the current language set in the browser, when the new user logs into the Dynamic Workload Console for the first time... the administrator must create a new Dynamic Workload Console user, and use that to login for the first time using a browser configured with the requested language. |
| Coletado em | 2026-08-25 |
| Capacidade | dwc_ui_language |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | login |
| Familia | dwc-default |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, as default tasks (predefined tasks) do Dynamic Workload Console sao criadas no idioma configurado no navegador no PRIMEIRO login do usuario e NAO sao traduzidas quando o idioma do navegador muda depois; para ter as default tasks em outro idioma, o administrador Liberty deve criar um novo usuario do DWC e faze-lo fazer o primeiro login com o navegador configurado nesse idioma?


---

### 50. `hwa-10.2.8-dwc-derby-unsupported-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

Apache Derby database is unsupported for Dynamic Workload Console starting from HWA version 10.2.3. Context: Apache Derby is no longer supported as a database for Dynamic Workload Console starting from Version 10.2.3.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 DWC installation page ('If you are currently using Derby, you need to install a supported database and migrate your data'). awsaddwcprereq.html 404s in v1028; the version boundary (10.2.3) is confirmed.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing the Dynamic Workload Console |
| Citacao de suporte | This is necessary because Derby is no longer supported as of version 10.2.3. |
| Coletado em | 2026-08-18 |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | version |
| Familia | dwc-derby |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Apache Derby database is unsupported for Dynamic Workload Console starting from HWA version 10.2.3. Context: Apache Derby is no longer supported as a database for Dynamic Workload Console starting from Version 10.2.3.?


---

### 51. `hwa-10.2.8-dwc-login-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o login no Dynamic Workload Console usa o form login padrao do Liberty (POST /console/j_security_check com j_username/j_password): em caso de sucesso retorna 302 para /console/ e emite cookie LtpaToken2 (SSO); o registro de usuarios e o basicRegistry com realm TWSRealm, usuario principal definido por user.twsuser.id/user.twsuser.password (wauser_variables.xml) e grupo de administradores definido por admin.group.name (default Admins) no authentication_config.xml; apos o login o dashboard e servido em /console/dashboard/index.jsp.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25 via curl HTTPS localhost:9443 com wauser. A senha do usuario principal fica criptografada {aes} no wauser_variables.xml; usuarios adicionais podem ser declarados no authentication_config.xml (amostras nonadmin/analyst/developer/configurator/operator). [fix auditor 2026-08-25: supporting_quote e observacao de laboratorio, nao citacao literal da pagina citada; a evidencia primaria e o lab_validation]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/mng_eng_c.html |
| Titulo da fonte | Engine connections - Dynamic Workload Console User's Guide - HCL Workload Automation |
| Citacao de suporte | POST /console/j_security_check -> 302; Set-Cookie: LtpaToken2=...; GET /console/ -> 200; [dashboard/index.jsp] Initialization successful. |
| Coletado em | 2026-08-25 |
| Capacidade | dwc |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | DWC instalado e dwcServer iniciado; usuario admin valido (wauser_variables.xml); HTTPS 9443 acessivel. |
| Impacto | Acesso autenticado ao console; operacao de leitura no login page. |
| Reversibilidade | NA (login e nao-destrutivo). |
| Criterio de parada | Interromper se o POST retornar 400 (form invalido) ou se o login falhar com credenciais corretas. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | login |
| Familia | dwc-login |


---

### 52. `hwa-10.2.8-dwc-sso-basic-0005`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_ui` / `authentication`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Dynamic Workload Console (DWC) usa autenticacao baseada em LTPA (Lightweight Third Party Authentication) sobre o Liberty WebSphere. O login e feito via POST /console/j_security_check com j_username e j_password; o servidor retorna HTTP 302 com cookie LtpaToken2. O DWC suporta autenticacao por basicRegistry (usuarios definidos em authentication_config.xml) ou federated repositories (LDAP). O arquivo de configuracao de usuarios fica em DWC_DATA/usr/servers/dwcServer/configDropins/overrides/authentication_config.xml. O grupo administrador e definido pela propriedade admin.group.name (default: Admins) e o usuario instalador pertence a este grupo.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio em todas as sessoes de instalacao/configuracao do DWC. O authentication_config.xml foi editado diversas vezes para adicionar usuarios (wauser, wauser_en). [Fonte oficial HCL 10.2.8 + lab]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/tswebmst_welcome.html |
| Titulo da fonte | Dynamic Workload Console User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | POST /console/j_security_check -> HTTP 302 + LtpaToken2 cookie |
| Coletado em | 2026-08-25 |
| Capacidade | dwc_authentication |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, DWC 10.2.8 em /opt/hwa/DWC, tested_commands=["curl -sk -c /tmp/dwc.cookies -d 'j_username=wauser' -d 'j_password=<pw>' https://<host>:9443/console/j_security_check", 'grep -c LtpaToken2 /tmp/dwc.cookies', 'curl -sk -b /tmp/dwc.cookies https://<host>:9443/console/'], result=302 + LtpaToken2 + dashboard 200. authentication_config.xml editado e server restartado com sucesso., validated_at=2026-08-25T10:30:00BRT |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | login |
| Familia | dwc-sso |


---

### 53. `hwa-10.2.8-dwc-trace-configdropins-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

No HCL Workload Automation Distributed 10.2.8, os traces do Dynamic Workload Console são ativados editando o template trace.xml e copiando-o de configDropins/templates para configDropins/overrides; as alterações são efetivas imediatamente.

> **ATENCAO / RESSALVAS DE USO:** Tracing DWC confirmado em 10.2.8; paths de exemplo não promovidos como caminhos reais do ambiente. [texto recuperado do unified dataset rag_corpus (verified_claim original)]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstractiva_traces.html |
| Titulo da fonte | Activating and deactivating traces in Dynamic Workload Console |
| Citacao de suporte | Templates for the Dynamic Workload Console are stored in DWC_home/usr/servers/dwcServer/configDropins/templates ... copy the updated template file to the overrides folder ... Changes are effective immediately. |
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

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, os traces do Dynamic Workload Console são ativados editando o template trace?


---

### 54. `hwa-10.2.8-dwc-ui-language-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `dwc_ui` / `language`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o idioma da interface do Dynamic Workload Console segue o idioma configurado no navegador do usuario (header HTTP Accept-Language): nao existe seletor de idioma na pagina de login nem propriedade de idioma no TdwcGlobalSettings.xml; para mudar a interface de portugues para ingles basta configurar o navegador para ingles e refazer o login. O kit instala 14 locales em Console.war/locale/ (en, pt-br, es, fr, de, it, ja, ko, zh-CN, zh-TW, ru, hi, kn, ta).

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25 via curl com headers Accept-Language distintos: os textos localizados mudam e o atributo html lang permanece fixo ('en'). A pagina oficial Customizing your global settings confirma que TdwcGlobalSettings.xml nao possui propriedade de idioma. [Observado em laboratorio HWA 10.2.8 WSL2]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/awsadglobsetcustom.html |
| Titulo da fonte | Customizing your global settings - Dynamic Workload Console User's Guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | pt-BR -> 'Erro:', 'credencial incorreta', 'Nome de Usuario'; en-US -> 'Error:', 'Wrong credential', 'Username' (mesma pagina, apenas Accept-Language alterado) |
| Coletado em | 2026-08-25 |
| Capacidade | dwc_ui_language |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, DWC 10.2.8.00 /opt/hwa/DWC, HTTPS 9443, tested_commands=["curl -sk -H 'Accept-Language: pt-BR,pt;q=0.9' https://<host>:9443/console/login.jsp", "curl -sk -H 'Accept-Language: en-US,en;q=0.9' https://<host>:9443/console/login.jsp", 'diff /tmp/lg-pt.html /tmp/lg-en.html'], result=Textos do login page mudam conforme Accept-Language: pt-BR -> 'Erro:'/'credencial incorreta'/'Nome de Usuario'; en-US -> 'Error:'/'Wrong credential'/'Username'. TdwcGlobalSettings.xml nao controla idioma., validated_at=2026-08-25T11:20:00BRT |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | login |
| Familia | dwc-ui |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o idioma da interface do Dynamic Workload Console segue o idioma configurado no navegador do usuario (header HTTP Accept-Language): nao existe seletor de idioma na pagina de login nem propriedade de idioma no TdwcGlobalSettings?


---

### 55. `hwa-10.2.8-enigma-r3batch-sap-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `password`

**Afirmacao / Conteudo:**

Do not paste or request real passwords. In HCL Workload Automation Distributed 10.2.8, the r3batch access method connects the product to SAP R/3 systems, and SAP user passwords can be encrypted with the enigma utility (in TWA_home/methods) before being written into r3batch.opts files, producing {aes}... values. Perform this in the approved environment, never here in the conversation.

> **ATENCAO / RESSALVAS DE USO:** Verified on official v1028 pages: enigma encryption (awsausappswdencr.html), {aes}... value format in the SAP options file example (awsausapoptfileex.html), and r3batch connects to SAP R/3 (awsausapaccessmethod.html). The 'in TWA_home/methods' location detail is documented for the options file/enigma as TWA_home\methods on Windows (TWA_DATA_DIR/methods on UNIX) in the RFC-password topic; treat passwords and {aes} values as sensitive. | Shows the enigma-encrypted {aes} password format in the SAP options file (quote truncated before the secret).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/apps/src_usr/awsausappswdencr.html |
| Titulo da fonte | Encrypting SAP user passwords |
| Citacao de suporte | If you modify the file with a text editor, run the enigma program to encrypt the password before writing it in the file, as follows: enigma <password> ... The program returns an encrypted version that you can then enter in the options file. |
| Coletado em | 2026-08-18 |
| Capacidade | password |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Terminologia normalizada | topic=enigma |
| Status de revisao | verified |
| Tipo | other |
| Familia | enigma-r3batch |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Do not paste or request real passwords?


---

### 56. `hwa-10.2.8-eqq199e-distributed-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `error`

**Afirmacao / Conteudo:**

EQQ199E is an error code from HCL Workload Automation for Z (z/OS), not from the Distributed platform. The EQQ message prefix belongs to the z/OS engine; generalizing EQQ error codes to distributed environments is incorrect.

> **ATENCAO / RESSALVAS DE USO:** EQQ* pertence ao HWA for Z, nao distributed.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=EQQ199E, component=HWA for Z engine, scope=z/OS integration |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed (fora de escopo para claims de motor distributed) |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmst_welcome.html |
| Titulo da fonte | Messages and Codes - HCL Workload Automation 10.2.8 |
| Citacao de suporte | EQQ message codes are documented under HCL Workload Automation for Z. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | error |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed (fora de escopo para claims de motor distributed) |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| Codigo da mensagem | EQQ199E |
| Componente | HWA for Z engine |
| Familia | eqq199e-distributed |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro EQQ199E no HWA?
- Como solucionar ou diagnosticar o erro EQQ199E no HWA?
- Qual é o significado da mensagem de erro EQQ199E no HWA e qual ação é recomendada?


---

### 57. `hwa-10.2.8-event-action-helper-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

O event processing server no HCL Workload Automation 10.2.8 recebe os eventos e verifica se eles correspondem a alguma event rule implantada; se houver correspondência, chama um action helper para executar as ações, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented event rule evaluation behavior of the event processor.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event processing server=servidor de processamento de eventos, action helper=action helper, deployed event rule=regra de evento implantada |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | The event rule management process |
| Citacao de suporte | The event processing server receives the events and checks if they match any deployed event rule. If an event rule is matched, the event processing server calls an action helper to carry out the actions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_processor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-action |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 recebe os eventos e verifica se eles correspondem a alguma event rule implantada; se houver correspondência, chama um action helper para executar as ações, conforme documentação oficial?


---

### 58. `hwa-10.2.8-event-correlation-rule-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

Ao definir uma event rule no HCL Workload Automation 10.2.8, especifica-se um ou mais eventos, uma regra de correlação (correlation rule) e uma ou mais ações acionadas pelos eventos, além de opcionalmente datas de validade, um intervalo diário de atividade e um fuso horário comum, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented elements defined when creating an event rule.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | correlation rule=regra de correlação, validity dates=datas de validade, daily time interval of activity=intervalo diário de atividade, time zone=fuso horário |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | When you define an event rule, you specify one or more events, a correlation rule, and the one or more actions that are triggered by those events. Moreover, you can specify validity dates, a daily time interval of activity, and a common time zone for all the time restrictions that are set. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rule_definition |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-correlation |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: Ao definir uma event rule no HCL Workload Automation 10.2.8, especifica-se um ou mais eventos, uma regra de correlação (correlation rule) e uma ou mais ações acionadas pelos eventos, além de opcionalmente datas de validade, um intervalo diário de atividade e um fuso horário comum, conforme documentação oficial?


---

### 59. `hwa-10.2.8-event-designer-0033`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, a criação de event rules é feita no Workload Designer, dentro da área Designing your workload, na tarefa Creating an event rule, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented DWC location (Workload Designer) for creating event rules.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Workload Designer=Workload Designer, Creating an event rule=tarefa Creating an event rule, Designing your workload=Designing your workload |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/erd_editor_c.html |
| Titulo da fonte | Creating an event rule |
| Citacao de suporte | Go to Workload Designer and choose an engine. In the Explore area, select Create new + ... Define the event to be triggered ... Define the action to be performed ... Select the event rule and click Save. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | event_rule_creation |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-designer |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, a criação de event rules é feita no Workload Designer, dentro da área Designing your workload, na tarefa Creating an event rule, conforme documentação oficial?


---

### 60. `hwa-10.2.8-event-designer-0036`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

The menu paths Design > Orchestrate and Administration > Manage event rules are not documented in HCL Workload Automation 10.2.8. The documented DWC locations for working with event rules are the Workload Designer and the Monitor Event Rules task.

> **ATENCAO / RESSALVAS DE USO:** The exact menu paths Design > Orchestrate and Administration > Manage event rules are not documented; documented DWC locations are Workload Designer and the Monitor Event Rules task.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Workload Designer=Workload Designer, Monitor Event Rules=tarefa Monitor Event Rules |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/erd_editor_c.html |
| Titulo da fonte | Creating an event rule - HCL Workload Automation 10.2.8 |
| Citacao de suporte | You can create an event rule from the Workload Designer or from the Monitor Event Rules task. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| Familia | event-designer |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: The menu paths Design > Orchestrate and Administration > Manage event rules are not documented in HCL Workload Automation 10.2.8. The documented DWC locations for working with event rules are the Workload Designer and the Monitor Event Rules task?


---

### 61. `hwa-10.2.8-event-domain-manager-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

O event processing server no HCL Workload Automation 10.2.8 inicia automaticamente com o master domain manager e apenas um event processor pode estar ativo na rede por vez, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Single-active event processor constraint documented.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event processing server=servidor de processamento de eventos, master domain manager=master domain manager |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | The event rule management process |
| Citacao de suporte | The event processing server starts automatically with the master domain manager. Only one event processor may run in the network at any time. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_processor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-domain |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 inicia automaticamente com o master domain manager e apenas um event processor pode estar ativo na rede por vez, conforme documentação oficial?


---

### 62. `hwa-10.2.8-event-editing-event-rules-0035`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser editadas na tarefa Editing event rules, sob Designing your workload, e após a edição a regra pode ser monitorada pela tarefa Monitor Event Rules, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented DWC editing workflow for event rules.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Editing event rules=tarefa Editing event rules, Monitor Event Rules=tarefa Monitor Event Rules |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/manage_ev_rule.html |
| Titulo da fonte | Editing event rules |
| Citacao de suporte | Select the event rule checkbox and then select Save. ... Monitor your event rule definition. Go to Monitor Event Rules to verify that the event rule runs correctly. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | monitor |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-editing |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser editadas na tarefa Editing event rules, sob Designing your workload, e após a edição a regra pode ser monitorada pela tarefa Monitor Event Rules, conforme documentação oficial?


---

### 63. `hwa-10.2.8-event-en-event-driven-0013`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `globalopts`

**Afirmacao / Conteudo:**

O valor da opção global enEventDrivenWorkloadAutomation no HCL Workload Automation 10.2.8 pode ser alterado a qualquer momento caso o usuário não queira usar a automação orientada a eventos em sua rede, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Global option toggles use of the event-driven workload automation feature.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enEventDrivenWorkloadAutomation=opção global enEventDrivenWorkloadAutomation |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | The event rule management process |
| Citacao de suporte | You can at any time change the value of the enEventDrivenWorkloadAutomation global option if you do not want to use it in your HCL Workload Automation network. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | globalopts_event_driven |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-en |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O valor da opção global enEventDrivenWorkloadAutomation no HCL Workload Automation 10.2.8 pode ser alterado a qualquer momento caso o usuário não queira usar a automação orientada a eventos em sua rede, conforme documentação oficial?


---

### 64. `hwa-10.2.8-event-event-rule-actions-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule define um conjunto de ações que são executadas quando ocorrem condições de evento específicas, correlacionando eventos e acionando ações, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** DWC concept definition of an event rule.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event rule=regra de evento, event rule definition=definição de regra de evento |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/awsrgeventruleconcept.html |
| Titulo da fonte | Event rule |
| Citacao de suporte | An event rule defines a set of actions that run when specific event conditions occur. An event rule definition correlates events and trigger actions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rules_dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| Familia | event-event |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule define um conjunto de ações que são executadas quando ocorrem condições de evento específicas, correlacionando eventos e acionando ações, conforme documentação oficial?


---

### 65. `hwa-10.2.8-event-event-rule-definition-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

Uma event rule no HCL Workload Automation 10.2.8 é um objeto de agendamento que inclui os itens Events, Event-correlating conditions e Actions, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented structure of an event rule.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event rule=regra de evento, Events=eventos, Event-correlating conditions=condições de correlação de eventos, Actions=ações |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | In HCL Workload Automation an event rule is a scheduling object that includes the following items: Events, Event-correlating conditions, Actions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rule_structure |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-event |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: Uma event rule no HCL Workload Automation 10.2.8 é um objeto de agendamento que inclui os itens Events, Event-correlating conditions e Actions, conforme documentação oficial?


---

### 66. `hwa-10.2.8-event-event-rule-instance-status-0038`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o administrador ou operador revisa o status das instâncias de event rules e das ações executadas no banco de dados e nos logs, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Final step of the documented event rule management process.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event rule instance=instância de regra de evento, event rule instances and actions=instâncias de regras de evento e ações |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | The event rule management process |
| Citacao de suporte | The administrator or the operator reviews the status of event rule instances and actions in the database and logs. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | event-event |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o administrador ou operador revisa o status das instâncias de event rules e das ações executadas no banco de dados e nos logs, conforme documentação oficial?


---

### 67. `hwa-10.2.8-event-external-events-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, eventos externos, como mensagens escritas em arquivos de log, eventos enviados por aplicações de terceiros e arquivos criados, atualizados ou excluídos, podem ser usados para acionar regras, inclusive em nós que não executam o HCL Workload Automation via comando sendevent, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented external event usage to trigger rules.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | External events=eventos externos, sendevent=comando sendevent, third party applications=aplicações de terceiros |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | Events of this category can be messages written in log files, events sent by third party applications, or a file being created, updated, or deleted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-external |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, eventos externos, como mensagens escritas em arquivos de log, eventos enviados por aplicações de terceiros e arquivos criados, atualizados ou excluídos, podem ser usados para acionar regras, inclusive em nós que não executam o HCL Workload Automation via comando sendevent, conforme documentação oficial?


---

### 68. `hwa-10.2.8-event-file-monitor-events-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Os eventos do provider FileMonitor no HCL Workload Automation 10.2.8 são FileCreated, FileDeleted, ModificationCompleted e LogMessageWritten, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** File event types documented.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FileMonitor events=eventos FileMonitor, FileCreated=FileCreated, FileDeleted=FileDeleted, ModificationCompleted=ModificationCompleted, LogMessageWritten=LogMessageWritten |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgfilemonitorevents.html |
| Titulo da fonte | FileMonitor events |
| Citacao de suporte | FileMonitor events are: FileCreated, FileDeleted, ModificationCompleted, LogMessageWritten |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-file |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os eventos do provider FileMonitor no HCL Workload Automation 10.2.8 são FileCreated, FileDeleted, ModificationCompleted e LogMessageWritten, conforme documentação oficial?


---

### 69. `hwa-10.2.8-event-filter-rule-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

As event rules no HCL Workload Automation 10.2.8 são classificadas em filter, sequence e set, com base em suas características, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Rule classification documented in the User's Guide and Reference.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | filter rule=regra filter, sequence rule=regra sequence, set rule=regra set |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefineeventrule.html |
| Titulo da fonte | Defining event rules |
| Citacao de suporte | Based on their characteristics, rules are classified as: filter...sequence...set |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rule_types |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | set |
| Familia | event-filter |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: As event rules no HCL Workload Automation 10.2.8 são classificadas em filter, sequence e set, com base em suas características, conforme documentação oficial?


---

### 70. `hwa-10.2.8-event-generic-action-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Os action providers documentados no HCL Workload Automation 10.2.8 são GenericAction, MailSender, MessageLogger, TWSAction, TWSForZosAction e ServiceNow, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** ServiceNow is listed in the chapter table of contents as an action provider.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | GenericAction=action provider GenericAction, MailSender=action provider MailSender, MessageLogger=action provider MessageLogger, TWSAction=action provider TWSAction, TWSForZosAction=action provider TWSForZosAction, ServiceNow=action provider ServiceNow |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgactionpro.html |
| Titulo da fonte | Action providers and definitions |
| Citacao de suporte | This section gives details on the action types of the following action providers: GenericAction, MailSender, MessageLogger, TWSAction, TWSForZosAction |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Familia | event-generic |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os action providers documentados no HCL Workload Automation 10.2.8 são GenericAction, MailSender, MessageLogger, TWSAction, TWSForZosAction e ServiceNow, conforme documentação oficial?


---

### 71. `hwa-10.2.8-event-internal-events-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Os eventos detectáveis no HCL Workload Automation 10.2.8 são divididos em eventos internos (envolvendo status de objetos como jobs, job streams e workstations) e eventos externos (mensagens em arquivos de log, eventos de aplicações de terceiros e criação, atualização ou exclusão de arquivos), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Internal versus external event classification documented.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Internal events=eventos internos, External events=eventos externos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | Internal events ... External events ... messages written in log files, events sent by third party applications, or a file being created, updated, or deleted. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | event-internal |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os eventos detectáveis no HCL Workload Automation 10.2.8 são divididos em eventos internos (envolvendo status de objetos como jobs, job streams e workstations) e eventos externos (mensagens em arquivos de log, eventos de aplicações de terceiros e criação, atualização ou exclusão de arquivos), conforme documentação oficial?


---

### 72. `hwa-10.2.8-event-monitor-event-rules-0034`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser monitoradas pela tarefa Monitor Event Rules, criada em Monitoring and Reporting > All Configured Tasks > New, sob Event Monitoring Task, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented DWC location for monitoring event rule instances.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Monitor Event Rules=tarefa Monitor Event Rules, Event Monitoring Task=tarefa de monitoramento de eventos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/eri_query_t.html |
| Titulo da fonte | Monitoring event rules |
| Citacao de suporte | In the navigation bar, click Monitoring and Reporting > All Configured Tasks > New. In the Create Task panel, under Event Monitoring Task, select Monitor Event Rules and click Next. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-monitor |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, event rules podem ser monitoradas pela tarefa Monitor Event Rules, criada em Monitoring and Reporting > All Configured Tasks > New, sob Event Monitoring Task, conforme documentação oficial?


---

### 73. `hwa-10.2.8-event-not-draft-0026`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

As definições de event rules no HCL Workload Automation 10.2.8 podem ser salvas como Draft (isDraft=yes, salvas no banco mas não prontas para implantação/ativação) ou como Not draft (isDraft=no, em processo de implantação ou prontas para serem implantadas e ativadas no ambiente de agendamento), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Draft vs non-draft states control whether a rule is deployed and activated.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Draft=rascunho, Not draft=não-rascunho, isDraft=atributo isDraft, deploy=implantar |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefineeventrule.html |
| Titulo da fonte | Defining event rules |
| Citacao de suporte | Draft ... saved in the database but is not ready yet to be deployed and activated. This state is determined by the isDraft=yes attribute. Not draft ... being deployed or is ready to be deployed in the scheduling environment. This state is determined by the isDraft=no attribute. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | event_rule_draft |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-not |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: As definições de event rules no HCL Workload Automation 10.2.8 podem ser salvas como Draft (isDraft=yes, salvas no banco mas não prontas para implantação/ativação) ou como Not draft (isDraft=no, em processo de implantação ou prontas para serem implantadas e ativadas no ambiente de agendamento), conforme documentação oficial?


---

### 74. `hwa-10.2.8-event-object-related-events-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, os eventos são divididos nas categorias relacionados a objetos do HCL Workload Automation, monitoramento de arquivos, monitoramento de aplicações, eventos SAP, monitoramento de data sets e eventos genéricos, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** DWC event categories documented.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | HCL Workload Automation object related events=eventos relacionados a objetos, File monitoring events=eventos de monitoramento de arquivos, Application monitoring events=eventos de monitoramento de aplicações, SAP related events=eventos SAP, Data set monitoring=monitoramento de data sets, Generic events=eventos genéricos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/event_mgmt_c.html |
| Titulo da fonte | Event management |
| Citacao de suporte | Events are divided into the following major categories: HCL Workload Automation object related events ... File monitoring events ... Application monitoring events ... SAP related events ... Data set monitoring ... Generic events |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-object |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, os eventos são divididos nas categorias relacionados a objetos do HCL Workload Automation, monitoramento de arquivos, monitoramento de aplicações, eventos SAP, monitoramento de data sets e eventos genéricos, conforme documentação oficial?


---

### 75. `hwa-10.2.8-event-on-demand-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

A automação orientada a eventos no HCL Workload Automation 10.2.8 permite definir regras (event rules) que podem acionar a automação de workload sob demanda, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Rules trigger on-demand automation.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event rule=regra de evento, on-demand workload automation=automação de workload sob demanda |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | It provides the capability to define rules that can trigger on-demand workload automation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rules |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-on |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: A automação orientada a eventos no HCL Workload Automation 10.2.8 permite definir regras (event rules) que podem acionar a automação de workload sob demanda, conforme documentação oficial?


---

### 76. `hwa-10.2.8-event-plan-based-job-scheduling-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

A automação de workload orientada a eventos no HCL Workload Automation 10.2.8 adiciona a capacidade de executar automação de workload sob demanda, além do agendamento de jobs baseado em plano, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented purpose of event-driven workload automation.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event_driven_workload_automation=automação de workload orientada a eventos, plan-based job scheduling=agendamento de jobs baseado em plano, on-demand workload automation=automação de workload sob demanda |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | Event-driven workload automation adds the capability to perform on-demand workload automation in addition to plan-based job scheduling. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_driven_automation |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | event-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A automação de workload orientada a eventos no HCL Workload Automation 10.2.8 adiciona a capacidade de executar automação de workload sob demanda, além do agendamento de jobs baseado em plano, conforme documentação oficial?


---

### 77. `hwa-10.2.8-event-predefined-set-of-actions-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

O objetivo da automação orientada a eventos no HCL Workload Automation 10.2.8 é executar um conjunto predefinido de ações em resposta a eventos que ocorrem em nós que executam o HCL Workload Automation, inclusive em nós que não executam o HCL Workload Automation por meio do comando sendevent, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented purpose of the event-driven mechanism.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | predefined set of actions=conjunto predefinido de ações, sendevent=comando sendevent |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation |
| Citacao de suporte | The object of event-driven workload automation in HCL Workload Automation is to carry out a predefined set of actions in response to events that occur on nodes running HCL Workload Automation (but also on non-HCL Workload Automation ones, when you use the sendevent command line). |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_sendevent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | set |
| Familia | event-predefined |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O objetivo da automação orientada a eventos no HCL Workload Automation 10.2.8 é executar um conjunto predefinido de ações em resposta a eventos que ocorrem em nós que executam o HCL Workload Automation, inclusive em nós que não executam o HCL Workload Automation por meio do comando sendevent, conforme documentação oficial?


---

### 78. `hwa-10.2.8-event-predefined-set-of-actions-0037`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

O recurso event management no Dynamic Workload Console do HCL Workload Automation 10.2.8 permite lançar um conjunto predefinido de ações em resposta a eventos que ocorrem nos nós onde o HCL Workload Automation é executado, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** DWC concept of the event management feature.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event management=gerenciamento de eventos, predefined set of actions=conjunto predefinido de ações |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/event_mgmt_c.html |
| Titulo da fonte | Event management |
| Citacao de suporte | You can use the event management feature to launch a predefined set of actions in response to events that occur on the nodes where HCL Workload Automation runs. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_management |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | set |
| Familia | event-predefined |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O recurso event management no Dynamic Workload Console do HCL Workload Automation 10.2.8 permite lançar um conjunto predefinido de ações em resposta a eventos que ocorrem nos nós onde o HCL Workload Automation é executado, conforme documentação oficial?


---

### 79. `hwa-10.2.8-event-rule-name-0040`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

The official HCL Workload Automation 10.2.8 documentation does not describe a four-part event rule structure (event, actions, options, rule name). The documented structure is: events, event-correlating conditions, and actions (eventRule element with eventCondition + action).

> **ATENCAO / RESSALVAS DE USO:** A estrutura documentada em 10.2.8 e de 3 partes (eventos + condicoes + acoes), nao 4.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | event rule=regra de evento, Events=eventos, Actions=ações, options=opções, rule name=nome da regra |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntdrivworkauto.html |
| Titulo da fonte | Running event-driven workload automation - HCL Workload Automation 10.2.8 |
| Citacao de suporte | An event rule is a scheduling object that includes the following items: Events, Event-correlating conditions, Actions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rule_structure |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-rule |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: The official HCL Workload Automation 10.2.8 documentation does not describe a four-part event rule structure (event, actions, options, rule name)?


---

### 80. `hwa-10.2.8-event-run-command-0022`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

A ação RunCommand do provider GenericAction no HCL Workload Automation 10.2.8 executa comandos que não são do HCL Workload Automation na mesma máquina onde o event processor é executado, e apenas o usuário TWS_user está autorizado a executá-la, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Generic command-launch action documented with its TWS_user authorization constraint.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | RunCommand=ação RunCommand, GenericAction=action provider GenericAction, TWS_user=usuário TWS_user |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrggenericaction.html |
| Titulo da fonte | GenericAction actions |
| Citacao de suporte | This provider implements a single action named RunCommand that runs non-HCL Workload Automation commands. Commands are run on the same computer where the event processor runs. Only TWS_user is authorized to run the command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | event_generic_action |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | run |
| Familia | event-run |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A ação RunCommand do provider GenericAction no HCL Workload Automation 10.2.8 executa comandos que não são do HCL Workload Automation na mesma máquina onde o event processor é executado, e apenas o usuário TWS_user está autorizado a executá-la, conforme documentação oficial?


---

### 81. `hwa-10.2.8-event-save-as-draft-0029`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule é ativada e implantada desativando o seletor Save as draft e salvando novamente a regra, e a ativação pode ser verificada na tarefa Manage Event Rule, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented DWC deployment and activation of event rules via the draft toggle.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Save as draft=seletor Save as draft, deploy=implantar, Manage Event Rule=tarefa Manage Event Rule |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/erd_editor_c.html |
| Titulo da fonte | Creating an event rule |
| Citacao de suporte | To activate the rule, you need to deploy it in the scheduling environment by switching the draft toggle off, and save again. Go to Manage Event Rule to verify that the event rule is active. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | event_rule_activation |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-save |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: No Dynamic Workload Console do HCL Workload Automation 10.2.8, uma event rule é ativada e implantada desativando o seletor Save as draft e salvando novamente a regra, e a ativação pode ser verificada na tarefa Manage Event Rule, conforme documentação oficial?


---

### 82. `hwa-10.2.8-event-twsobjects-monitor-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

Os event providers documentados no HCL Workload Automation 10.2.8 são TWSObjectsMonitor, FileMonitor, TWSApplicationMonitor e DatasetMonitor, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented event provider set in 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TWSObjectsMonitor=event provider TWSObjectsMonitor, FileMonitor=event provider FileMonitor, TWSApplicationMonitor=event provider TWSApplicationMonitor, DatasetMonitor=event provider DatasetMonitor |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgeventpro.html |
| Titulo da fonte | Event providers and definitions |
| Citacao de suporte | This section gives details on the event types of the following event providers: TWSObjectsMonitor events, FileMonitor events, TWSApplicationMonitor events, DatasetMonitor events |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-twsobjects |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os event providers documentados no HCL Workload Automation 10.2.8 são TWSObjectsMonitor, FileMonitor, TWSApplicationMonitor e DatasetMonitor, conforme documentação oficial?


---

### 83. `hwa-10.2.8-event-validity-period-0039`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `event`

**Afirmacao / Conteudo:**

Uma event rule no HCL Workload Automation 10.2.8, quando implantada e sem atributos de validade ou intervalo de atividade especificados, permanece ativa perpetuamente em todos os momentos até ser alterada para o status de draft ou excluída do banco de dados, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented effect of deployment on rule active state.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | validity period=período de validade, activity time window=janela de tempo de atividade, deploy=implantar, draft status=status de rascunho |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefineeventrule.html |
| Titulo da fonte | Defining event rules |
| Citacao de suporte | If you do not specify these attributes, the rule is active perpetually at all times once it is deployed and until it is changed back to draft status or deleted from the database. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | event_rule_lifecycle |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | event-validity |

**Perguntas relacionadas:**

- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?
- Qual a regra documentada no HWA Distributed sobre: Uma event rule no HCL Workload Automation 10.2.8, quando implantada e sem atributos de validade ou intervalo de atividade especificados, permanece ativa perpetuamente em todos os momentos até ser alterada para o status de draft ou excluída do banco de dados, conforme documentação oficial?


---

### 84. `hwa-10.2.8-evtsize-evtsize-message-size-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `evtsize`

**Afirmacao / Conteudo:**

Não execute sem aprovação. No HCL Workload Automation Distributed 10.2.8, evtsize define o tamanho de arquivos de mensagens como Mailbox.msg e é usado para aumentar o arquivo após 'End of file on events file.'; requer usuário maestro/root ou Administrator e o engine deve estar parado. Confirme a janela e o procedimento aprovado.

> **ATENCAO / RESSALVAS DE USO:** Inferred URLs (awsrgeventsize.html, awsrgcomhevtsize.html) return 404; correct page is awsrgevtsize.html. Mailbox.msg is among the valid event file names (Courier.msg, Intercom.msg, Mailbox.msg, Planbox.msg, etc.). Claim is a usage/utility description (read-only as stated); actually executing evtsize with a size argument resizes a message file, so execution is mutating - do not run without the approved window.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevtsize.html |
| Titulo da fonte | evtsize |
| Citacao de suporte | Defines the size of the HCL Workload Automation message files. This command is used by the HCL Workload Automation administrator either to increase the size of a message file after receiving the message, 'End of file on events file.' ... You must be maestro or root in UNIX, or Administrator in Windows to run evtsize. Stop the HCL Workload Automation engine before running this command. |
| Coletado em | 2026-08-18 |
| Capacidade | evtsize |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=evtsize |
| Status de revisao | verified |
| Tipo | other |
| Familia | evtsize-evtsize |


---

### 85. `hwa-10.2.8-govern-audit-who-changed-what-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `audit`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, via Dynamic Workload Console administradores, operadores e schedulers podem revisar todas as alterações em objetos de agendamento no banco e no plano, descobrir qual usuário realizou uma alteração, e a data/hora da alteração; pode-se manter trilha de auditoria com o motivo da alteração e, opcionalmente, exigir justificativa para cada alteração.

> **ATENCAO / RESSALVAS DE USO:** Justification enforcement is an optional, configurable capability; HCL does not prescribe a mandatory change-policy standard.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | audit_who_changed_what=DWC records user, date/time and reason for scheduling object changes, change_justification=optional enforced policy requiring justification for changes |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/keepingtrack.html |
| Titulo da fonte | Keeping track of changes to scheduling objects - HCL Workload Automation 10.2.8 DWC |
| Citacao de suporte | discover which user performed a specific change, and the time and date when the change was performed. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | audit_review |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | govern-audit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, via Dynamic Workload Console administradores, operadores e schedulers podem revisar todas as alterações em objetos de agendamento no banco e no plano, descobrir qual usuário realizou uma alteração, e a data/hora da alteração; pode-se manter trilha de auditoria com o motivo da alteração e, opcionalmente, exigir justificativa para cada alteração?


---

### 86. `hwa-10.2.8-govern-auto-lock-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `govern`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, no Dynamic Workload Console os objetos são bloqueados automaticamente enquanto um usuário os mantém abertos com o botão Edit (edição); objetos abertos apenas com View (visualização) não são bloqueados.

> **ATENCAO / RESSALVAS DE USO:** Auto-lock in DWC mirrors composer lock behavior for concurrent editing control.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dwc_auto_lock=objects automatically locked while open in Edit mode, view_no_lock=objects opened with View are not locked |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglocksection.html |
| Titulo da fonte | lock - HCL Workload Automation 10.2.8 (See also) |
| Citacao de suporte | In the Dynamic Workload Console, objects are automatically locked as long as you or another user have them open using the Edit button. Objects are not locked if you or another user opened them with View. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | object_lock |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-auto |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, no Dynamic Workload Console os objetos são bloqueados automaticamente enquanto um usuário os mantém abertos com o botão Edit (edição); objetos abertos apenas com View (visualização) não são bloqueados?


---

### 87. `hwa-10.2.8-govern-draft-undraft-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `govern`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, pelo Dynamic Workload Console é possível definir um ou mais job streams como draft ou non-draft para controlar se eles são adicionados ao preproduction plan; essa ação requer acesso DRAFT ou MODIFY ao job stream.

> **ATENCAO / RESSALVAS DE USO:** DRAFT access only allows draft/undraft; MODIFY access allows modifying all properties.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | draft_undraft=DWC action to set job streams draft/non-draft controlling preproduction plan inclusion, draft_access=authorization required to set draft status |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/DraftUndraftWD.html |
| Titulo da fonte | Setting job streams in draft and non-draft status - HCL Workload Automation 10.2.8 DWC |
| Citacao de suporte | You can easily set one or more job streams in draft or non-draft status to control whether they are added to the preproduction plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | draft_status |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | modify; plan |
| Familia | govern-draft |


---

### 88. `hwa-10.2.8-govern-en-db-audit-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `audit`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a auditoria de banco de dados e de planos (enDbAudit e enPlanAudit) está habilitada por padrão e pode ser desabilitada via opções globais; a opção global auditStore define onde armazenar os registros de auditoria do banco de dados: em arquivo (file), no banco de dados (db) ou em ambos (both).

> **ATENCAO / RESSALVAS DE USO:** Documented audit of all user modifications to DB objects (including open-and-save) and to the plan (successful or not).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enDbAudit=enables auditing of database information, enPlanAudit=enables auditing of plan information, auditStore=file|db|both storage of database audit records |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadhowaudit.html |
| Titulo da fonte | Enabling and storing audit trails - HCL Workload Automation 10.2.8 Administration Guide |
| Citacao de suporte | By default, auditing is enabled. ... enDbAudit Enables auditing of the information available in the database. ... enPlanAudit Enables auditing of the information available in the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | audit_config |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-en |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a auditoria de banco de dados e de planos (enDbAudit e enPlanAudit) está habilitada por padrão e pode ser desabilitada via opções globais; a opção global auditStore define onde armazenar os registros de auditoria do banco de dados: em arquivo (file), no banco de dados (db) ou em ambos (both)?


---

### 89. `hwa-10.2.8-govern-graphical-designer-deploy-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `govern`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, no Graphical Designer do Dynamic Workload Console a ação Deploy salva no banco de dados os itens definidos no workspace; os itens só são gravados no banco quando o Deploy é concluído.

> **ATENCAO / RESSALVAS DE USO:** Deployment of definitions in DWC = workspace items committed to the database via Deploy; merge conflicts handled at deploy time.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | graphical_designer_deploy=save workspace items to the HCL Workload Automation database, workspace=canvas where job streams are designed before deployment |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/designer_overview.html |
| Titulo da fonte | Graphical Designer overview - HCL Workload Automation 10.2.8 DWC |
| Citacao de suporte | The items you defined in a workspace can be saved to the database by selecting Deploy. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | deploy_gd |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | gui |
| verbs | deploy |
| Familia | govern-graphical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, no Graphical Designer do Dynamic Workload Console a ação Deploy salva no banco de dados os itens definidos no workspace; os itens só são gravados no banco quando o Deploy é concluído?


---

### 90. `hwa-10.2.8-govern-job-name-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o nome de um job deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 40 caracteres.

> **ATENCAO / RESSALVAS DE USO:** Hard product constraint (40-char limit) documented for the job definition.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | job_name=must start with a letter; alphanumeric, dash, underscore; max 40 characters |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobdefn.html |
| Titulo da fonte | Job definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The job name must start with a letter, and can contain alphanumeric characters, dashes, and underscores. It can contain up to 40 characters. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | naming_job |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de um job deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, e pode ter no máximo 40 caracteres?


---

### 91. `hwa-10.2.8-govern-node-hostname-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para hostnames de workstation (atributo node) os caracteres válidos são alfanuméricos, incluindo hífen (-), e o comprimento máximo é de 51 caracteres.

> **ATENCAO / RESSALVAS DE USO:** Hard product constraint for the node (hostname) field of a workstation definition.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | node_hostname=valid characters alphanumeric including dash; max length 51 characters |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwsdefn.html |
| Titulo da fonte | Workstation definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | For host names, valid characters are alphanumeric, including dash (-). The maximum length is 51 characters. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | naming_workstation |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-node |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, para hostnames de workstation (atributo node) os caracteres válidos são alfanuméricos, incluindo hífen (-), e o comprimento máximo é de 51 caracteres?


---

### 92. `hwa-10.2.8-govern-pt-br-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não contém uma página ou tarefa denominada 'Manage change' nem 'Manage change > Monitor' com ação 'Deploy pending changes' no Dynamic Workload Console; as funções de mudança são documentadas como 'Keeping track of changes' (auditoria de justificativa/relatórios, verificação de versões e versionamento), sem tal tarefa ou ação.

> **ATENCAO / RESSALVAS DE USO:** Confirmed negative finding. The 10.2.8 DWC User's Guide change-management chapter is 'Keeping track of changes to scheduling objects' (with subsections Auditing justification and reporting, Checking version information, and business scenarios); no 'Manage change' task, no 'Manage change > Monitor' navigation and no 'Deploy pending changes' action exist anywhere in the v1028 DWC guide TOC or the Administration Guide. Pages actually opened: tswebmst_welcome.html, keepingtrack.html, awsadauditoverview.html, auditingsteps.html, awsadauditreps.html (v102).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | en=Manage change task; Deploy pending changes action; Keeping track of changes; Dynamic Workload Console, pt_br=tarefa Gerenciar mudanças; ação Implantar mudanças pendentes; Manter controle de mudanças; Console de Trabalho Dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/keepingtrack.html |
| Titulo da fonte | Keeping track of changes to scheduling objects (HCL Workload Automation 10.2.8 - Dynamic Workload Console User's Guide) |
| Citacao de suporte | From the Dynamic Workload Console, HCL Workload Automation administrators, operators, and schedulers can review all changes to scheduling objects, both in the database and in the plan, discover which user performed a specific change, and the time and date when the change was performed. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | deploy |
| Familia | govern-pt |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não contém uma página ou tarefa denominada 'Manage change' nem 'Manage change > Monitor' com ação 'Deploy pending changes' no Dynamic Workload Console; as funções de mudança são documentadas como 'Keeping track of changes' (auditoria de justificativa/relatórios, verificação de versões e versionamento), sem tal tarefa ou ação?


---

### 93. `hwa-10.2.8-govern-pt-br-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não prescreve um padrão organizacional de convenção de nomenclatura (ex.: para jobs, job streams ou workstations).

> **ATENCAO / RESSALVAS DE USO:** Confirmed negative finding. The 10.2.8 Best practices manual is limited to three topics: configuring the dynamic domain manager after install/upgrade, database recommendations, and ulimit resource settings; none prescribes an organizational naming-convention standard. The v1028 documentation tree contains no naming-convention policy or governance standard.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | en=organizational naming convention standard; naming policy, pt_br=padrão organizacional de convenção de nomenclatura; política de nomenclatura |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_bp/awsbpmst_welcome.html |
| Titulo da fonte | Best practices (HCL Workload Automation 10.2.8) |
| Citacao de suporte | Best practices provides information about best practices to be applied when installing, configuring and using the HCL Workload Automation family of products: HCL Workload Automation, HCL Workload Automation for Z, Dynamic Workload Console. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | naming_convention |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-pt |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não prescreve um padrão organizacional de convenção de nomenclatura (ex?


---

### 94. `hwa-10.2.8-govern-pt-br-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `quality`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não prescreve SLAs (acordos de nível de serviço) operacionais.

> **ATENCAO / RESSALVAS DE USO:** Confirmed negative finding. HCL documents technical metrics collection (Collecting job metrics, enDbAudit/enPlanAudit options, audit reports) but does not prescribe operational SLAs or service-level targets; the Best practices manual and Administration Guide contain no SLA policy.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | en=operational service level agreements (SLA), pt_br=acordos de nível de serviço operacionais (SLA) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_bp/awsbpmst_welcome.html |
| Titulo da fonte | Best practices (HCL Workload Automation 10.2.8) |
| Citacao de suporte | To achieve high availability and operational efficiency, it is critical to adhere to validated architectural and configuration standards. This manual serves as a technical reference for implementing these standards to minimize manual intervention and maximize system throughput. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | sla_quality |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-pt |


---

### 95. `hwa-10.2.8-govern-pt-br-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `quality`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não prescreve métricas de qualidade (organizacionais) para o agendamento.

> **ATENCAO / RESSALVAS DE USO:** Confirmed negative finding. The v1028 documentation set (Best practices, Administration Guide, DWC User's Guide) covers technical configuration best practices, audit reporting and job-metrics collection, but prescribes no organizational quality metrics or quality standard for scheduling operations.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | en=quality metrics standard; workload quality metrics, pt_br=métricas de qualidade (organizacionais); padrão de métricas |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_bp/awsbpmst_welcome.html |
| Titulo da fonte | Best practices (HCL Workload Automation 10.2.8) |
| Citacao de suporte | Best practices provides information about best practices to be applied when installing, configuring and using the HCL Workload Automation family of products: HCL Workload Automation, HCL Workload Automation for Z, Dynamic Workload Console. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | sla_quality |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-pt |


---

### 96. `hwa-10.2.8-govern-pt-br-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `change`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não prescreve uma política de mudanças padrão; a exigência de justificativa para mudanças é uma capacidade opcional configurável pelo administrador.

> **ATENCAO / RESSALVAS DE USO:** Confirmed negative finding with positive corroboration. HCL prescribes no default/organizational change policy; it documents the justification policy strictly as an optional, administrator-enabled capability under DWC Administration > Security > Auditing Preferences ('For each displayed engine, you can enable the justification policy').

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | en=mandatory change justification policy; optional capability; auditing preferences, pt_br=política de mudanças padrão; justificativa obrigatória; capacidade opcional; preferências de auditoria |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/keepingtrack.html |
| Titulo da fonte | Keeping track of changes to scheduling objects (HCL Workload Automation 10.2.8 - Dynamic Workload Console User's Guide) |
| Citacao de suporte | Administrators can optionally enforce a policy by which each user making a change to an object must provide a justification for the change. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | change_management |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-pt |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation 10.2.8 não prescreve uma política de mudanças padrão; a exigência de justificativa para mudanças é uma capacidade opcional configurável pelo administrador?


---

### 97. `hwa-10.2.8-govern-streamlogon-user-name-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o nome de usuário de streamlogon de um job pode conter até 47 caracteres.

> **ATENCAO / RESSALVAS DE USO:** Hard product constraint for the streamlogon user name of a job definition.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | streamlogon_user_name=max 47 characters |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobdefn.html |
| Titulo da fonte | Job definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | streamlogon username ... The name can contain up to 47 characters. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-streamlogon |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de usuário de streamlogon de um job pode conter até 47 caracteres?


---

### 98. `hwa-10.2.8-govern-workstation-name-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o nome de uma workstation deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, pode ter no máximo 16 caracteres, deve ser único e não pode ser igual aos nomes de classes de workstation.

> **ATENCAO / RESSALVAS DE USO:** Hard product constraint (16-char limit) documented in the cpuname attribute.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | workstation_name=must start with a letter; alphanumeric, dash, underscore; max 16 characters; unique; not equal to workstation class name |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwsdefn.html |
| Titulo da fonte | Workstation definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The name must start with a letter, and can contain alphanumeric characters, dashes, and underscores. It can contain up to 16 characters. ... Workstation names must be unique and cannot be the same as workstation class names. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | naming_workstation |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | govern-workstation |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o nome de uma workstation deve começar com uma letra, pode conter caracteres alfanuméricos, hífens e sublinhados, pode ter no máximo 16 caracteres, deve ser único e não pode ser igual aos nomes de classes de workstation?


---

### 99. `hwa-10.2.8-gui-jobdef-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `gui`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para criar uma definição de job executável pela Dynamic Workload Console, abre-se o Graphical Designer, na aba Assets clica-se no ícone +, seleciona-se Job definition, digita-se Executable na barra de busca, escolhe-se o tipo de job executável e clica-se em Next; em seguida configuram-se Workstation, Folder, Name e Task (por exemplo, Inline script) e informa-se o Command text or script name; o botão Add salva a definição de job no banco de dados.

> **ATENCAO / RESSALVAS DE USO:** Procedimento específico do DWC 10.2.8 (executável). Não generalizar para outras versões ou tipos de job.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/Creating_exec_jobs_t.html |
| Titulo da fonte | Managing job definitions |
| Citacao de suporte | From the Graphical Designer page, select the Assets tab and click the add icon +. From the drop-down menu, select Job definition. In the search bar, type Executable, then select the executable job type and click Next... In Task, from the drop-down menu, select Inline script... Click Add to add the job definition to the database. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | gui_job_definition |
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
| Familia | gui-jobdef |


---

### 100. `hwa-10.2.8-gui-jobdef-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `gui`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, um job em um job stream pode referenciar uma definição de job em vez de ser um job embutido; referenciar uma mesma definição de job em vários job streams evita duplicar a definição e permite que uma única alteração se propague a todos os job streams que a referenciam.

> **ATENCAO / RESSALVAS DE USO:** Conceito confirmado para distr 10.2.8; o mesmo conceito é citado na página de criação de job streams.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/Creating_exec_jobs_t.html |
| Titulo da fonte | Managing job definitions |
| Citacao de suporte | Jobs can either be an embedded job, or they can reference a job definition... David prefers to reference a job definition instead of creating an embedded job because he needs to use the same job definition in other job streams and he wants to avoid to duplicate the definition. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | gui_job_definition |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=gui |
| Tipo | other |
| Ferramenta | gui |
| Familia | gui-jobdef |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, um job em um job stream pode referenciar uma definição de job em vez de ser um job embutido; referenciar uma mesma definição de job em vários job streams evita duplicar a definição e permite que uma única alteração se propague a todos os job streams que a referenciam?


---

### 101. `hwa-10.2.8-gui-trigger-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `gui`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os triggers que podem ser associados a um job stream no Graphical Designer incluem o run cycle (dias/horas em que o job stream deve rodar) e o excluding run cycle (que prevalece sobre o run cycle e define quando o job stream não deve rodar); adicionalmente, desde 10.2.4, run cycle groups podem ser criados e atribuídos como triggers diretamente no Graphical Designer.

> **ATENCAO / RESSALVAS DE USO:** O trigger por evento ('event trigger') NÃO está documentado como trigger de job stream do Graphical Designer em v1028; os triggers documentados na GUI são Service, Run cycle e Excluding run cycle. Run cycle groups como triggers foi confirmado na página de enhancements 10.2.4.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/designer_overview.html |
| Titulo da fonte | Graphical Designer overview |
| Citacao de suporte | A run cycle specifies the days and times when a job stream is scheduled to run. Excluding run cycle ... specifies the days and times when a job stream must not run. Excluding run cycles take precedence over run cycles. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | gui_run_cycle_trigger |
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
| Familia | gui-trigger |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os triggers que podem ser associados a um job stream no Graphical Designer incluem o run cycle (dias/horas em que o job stream deve rodar) e o excluding run cycle (que prevalece sobre o run cycle e define quando o job stream não deve rodar); adicionalmente, desde 10.2.4, run cycle groups podem ser criados e atribuídos como triggers diretamente no Graphical Designer?


---

### 102. `hwa-10.2.8-incident-aix-timezone-smit-0123`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `timezone`

**Afirmacao / Conteudo:**

Sintoma: inconsistencia de horario em jobs no AIX master domain manager (ex.: schedtime ou start time incorretos). Causa: setting incorreto do time zone no AIX. Resolucao: no AIX master domain manager: (1) iniciar smit; (2) selecionar System Environments > Change/Show Date, Time, and Time Zone > Change Time Zone Using User Entered Values; (3) setar o time zone relevante. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AIX timezone smit |
| Citacao de suporte | The problem might be due to an incorrect setting of the time zone. Start smit... Set the relevant time zone. |
| Coletado em | 2026-08-23 |
| Capacidade | timezone |
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
| verbs | show; start |
| Familia | incident-aix |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: inconsistencia de horario em jobs no AIX master domain manager (ex?
- O que causa e como solucionar o problema: inconsistencia de horario em jobs no AIX master domain manager (ex?


---

### 103. `hwa-10.2.8-incident-alias-archive-search-0120`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `alias`

**Afirmacao / Conteudo:**

Sintoma: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece. Causa: jobs e job streams em status final sao armazenados no archive com seus nomes originais, nao seus aliases — qualquer busca/report de jobs completos deve ignorar os aliases. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - alias archive search |
| Citacao de suporte | Jobs and job streams in final status are stored in the archive with their original names, not their aliases, so any search or reporting of completed jobs must ignore the aliases. |
| Coletado em | 2026-08-23 |
| Capacidade | alias |
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
| verbs | archive; status |
| Familia | incident-alias |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece?
- O que causa e como solucionar o problema: um job ou job stream que usa alias completou, mas ao definir query/report para inclui-lo, ele nao aparece?


---

### 104. `hwa-10.2.8-incident-auth-config-xml-0147`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando. Causa: divergencia entre os arquivos authentication_config.xml no DWC e no master domain manager. Resolucao: localizar e comparar os arquivos authentication_config.xml em ambos: no master domain manager (UNIX: TWA_DATA_DIR/usr/servers/engineServer/configDropins/overrides; Windows: TWA_home\usr\servers\engineServer\configDropins\overrides) e no DWC (UNIX: DWC_DATA_dir/usr/servers/dwcServer/configDropins/overrides; Windows: DWC_home\usr\servers\dwcServer\configDropins\overrides) e alinha-los. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Ultima secao do PDF coberta (161/161).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - authentication_config.xml |
| Citacao de suporte | Locate the authentication_config.xml configuration files on both the Dynamic Workload Console and the master domain manager. The file is located in the following path for the master domain manager: TWA_DATA_DIR/usr/servers/engineServer/configDropins/overrides |
| Coletado em | 2026-08-23 |
| Capacidade | console |
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
| Ferramenta | dwc |
| Familia | incident-auth |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando?
- O que causa e como solucionar o problema: ao usar o Dynamic Workload Console, voce e inesperadamente solicitado a digitar suas credenciais de usuario para conectar, o que significa que a autenticacao conjunta (single sign-on) entre DWC e engine nao esta funcionando?


---

### 105. `hwa-10.2.8-incident-beh023e-0069`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `appserver`

**Afirmacao / Conteudo:**

Sintoma: AWSBEH023E 'Unable to establish communication with the server' durante MakePlan. Causa: o application server esta parado e o MakePlan nao consegue continuar. Resolucao: iniciar o WebSphere Application Server Liberty Base e verificar os logs do Liberty para identificar por que parou. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSBEH023E).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (pagina 95).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSBEH023E |
| Citacao de suporte | AWSBEH023E Unable to establish communication with the server. This error means that the application server is down and MakePlan cannot continue. |
| Coletado em | 2026-08-23 |
| Capacidade | appserver |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSBEH023E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | planner |
| Codigo da mensagem | AWSBEH023E |
| Familia | incident-beh023e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBEH023E no HWA?
- Como solucionar ou diagnosticar o erro AWSBEH023E no HWA?
- O que causa e como solucionar o problema: AWSBEH023E 'Unable to establish communication with the server' durante MakePlan?


---

### 106. `hwa-10.2.8-incident-bhu025e-0019`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `syntax`

**Afirmacao / Conteudo:**

Sintoma: AWSBHU025E ao usar into=JOBS#<jobstream_id>. Causa: o job stream ID nao e aceito na sintaxe into= com separador #; a forma correta para qualificar por ID usa separador ';' (jobstream_id;schedid) ou horario entre parenteses. Resolucao: usar into=STREAM(hhmm) ou into=jobstream_id;schedid.

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 22/08 (claim 0130).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html |
| Titulo da fonte | submit job - HCL Workload Automation 10.2.8 |
| Citacao de suporte | jobstream_id ;schedid |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | syntax |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['submit job ad hoc com into=JOBS#<id>'], result=into=JOBS#CF26233AAAAAAAAA (ID) -> AWSBHU025E - ID nao aceito nesta sintaxe; forma aceita: into=JOBS(0300) ou into=STREAM(hhmm) (lab-validation-2026-08-22-job-creation-gaps.jsonl), validated_at=2026-08-22T00:30:00BRT |
| Tipo | command |
| Codigo da mensagem | AWSBHU025E |
| Familia | incident-bhu025e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU025E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU025E no HWA?
- O que causa e como solucionar o problema: AWSBHU025E ao usar into=JOBS#<jobstream_id>?


---

### 107. `hwa-10.2.8-incident-bhu152e-0018`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `syntax`

**Afirmacao / Conteudo:**

Sintoma: AWSBHU152E 'There is more than one job stream instance with the given name' ao submeter job ad hoc com into=. Causa: a job stream alvo tem multiplas instancias no plano (ex.: dias diferentes ou instancias ABEND antigas). Resolucao: qualificar a instancia com into=STREAM(hhmm) ou into=STREAM(hhmm mm/dd).

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 22/08 (claim 0130): into=JOBS(0300) resolve.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html |
| Titulo da fonte | submit job - HCL Workload Automation 10.2.8 |
| Citacao de suporte | into=[folder/]jobstream_instance |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | syntax |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['submit job ad hoc com into=', 'conman sbj'], result=sbd into=JOBS -> AWSBHU152E (2 instancias: 08/17 ABEND + 08/22 READY); into=JOBS(0300 08/22) -> SUCC; into=JOBS(0300) so hora -> SUCC; schedtime= keyword separada -> AWSBHU152E (lab-validation-2026-08-22-job-creation-gaps.jsonl), validated_at=2026-08-22T00:30:00BRT |
| Tipo | command |
| Codigo da mensagem | AWSBHU152E |
| Familia | incident-bhu152e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU152E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU152E no HWA?
- O que causa e como solucionar o problema: AWSBHU152E 'There is more than one job stream instance with the given name' ao submeter job ad hoc com into=?


---

### 108. `hwa-10.2.8-incident-big-joblog-mdm-stop-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `application_server`

**Afirmacao / Conteudo:**

Sintoma: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente. Causa: problema conhecido que afeta OpenJDK v8, relacionado a uma questao temporaria do filesystem /tmp. Resolucao: o WebSphere Application Server Liberty Base reinicia automaticamente apos um curto periodo; se a questao temporaria do /tmp for resolvida, a operacao pode ser realizada novamente. Fonte: HCL Troubleshooting Guide 10.2.8 (Master Domain Manager may stop when trying to retrieve a big job log).

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
| Citacao de suporte | When trying to get a big job log (greater than 100 Mb) from the Dynamic Workload Console, the Master Domain Manager Liberty server could unexpectedly stop working due to a known issue affecting OpenJDK v8, which is related to a temporary issue with the /tmp filesystem. |
| Capacidade | application_server |
| Classificacao de risco | read_only |
| Modo de operacao | read |
| Terminologia normalizada | command=stop |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | mdm |
| verbs | stop |
| Familia | incident-big |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente?
- O que causa e como solucionar o problema: ao tentar recuperar um job log grande (maior que 100 Mb) pelo Dynamic Workload Console, o Liberty server do master domain manager pode parar inesperadamente?


---

### 109. `hwa-10.2.8-incident-browser-close-thread-0130`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar. Causa: comportamento normal de aplicacoes WEB — quando o browser do cliente e fechado, nenhuma notificacao e entregue ao servidor segundo o protocolo HTTP; por isso a ultima thread disparada continua processando mesmo apos o fechamento. Resolucao: nao precisa de acao — apenas aguardar. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - browser close thread |
| Citacao de suporte | This is normal behavior for any WEB application, when the client browser is closed no notification is delivered to the server according to the HTTP protocol specifications... the last triggered thread continues to process even after the browser window was closed. |
| Coletado em | 2026-08-23 |
| Capacidade | console |
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
| Familia | incident-browser |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar?
- O que causa e como solucionar o problema: ao executar uma acao no Dynamic Workload Console e fechar imediatamente o browser, o processamento parece continuar?


---

### 110. `hwa-10.2.8-incident-cluster-exe-0124`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `windows`

**Afirmacao / Conteudo:**

Sintoma: problema com Failover Clustering em Windows Server 2012. Causa: deprecacao da ferramenta cluster.exe command-line para Failover Clustering em Windows Server 2012. Resolucao: reinstalar a feature deprecated Failover Clustering cluster.exe. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - cluster.exe deprecated |
| Citacao de suporte | This occurs because of the deprecation of the cluster.exe command-line tool for Failover Clustering on Windows Server 2012 platforms. To avoid this problem, you must reinstall the deprecated Failover Clustering feature cluster.exe. |
| Coletado em | 2026-08-23 |
| Capacidade | windows |
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
| Familia | incident-cluster |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: problema com Failover Clustering em Windows Server 2012. Causa: deprecacao da ferramenta cluster?
- O que causa e como solucionar o problema: problema com Failover Clustering em Windows Server 2012?


---

### 111. `hwa-10.2.8-incident-critical-late-0140`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `critical-network`

**Afirmacao / Conteudo:**

Sintoma: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores. Resolucao: usando a tarefa successful predecessors, comparar o planned start, actual start e critical start de todos os predecessores do job atrasado; verificar se algum tem valores de tempo muito proximos ou planned start posterior ao critical start. Se for o caso: considerar mudar... Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - critical job late |
| Citacao de suporte | Using the successful predecessors task, compare the planned start, the actual start, and the critical start of all the predecessors of the late job. Check if any of them have time values that are too close together or have a planned start time that is later than the critical start time. |
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
| verbs | start |
| Familia | incident-critical |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores?
- O que causa e como solucionar o problema: um job definido como critical esta consistentemente atrasado apesar dos mecanismos de promocao aplicados a ele e seus predecessores?


---

### 112. `hwa-10.2.8-incident-db2-deadlock-timeout-0104`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: 'The current transaction has been rolled back because of a deadlock or timeout. Reason code 68' ao acessar um objeto. Causa: o objeto esta locked por outro usuario, ou por voce em outra sessao, mas o lock nao foi detectado pela aplicacao — a aplicacao espera ate ser interrompida pelo timeout do DB2. Resolucao: aumentar o timeout do DB2 (ou do Liberty) ou resolver o lock concorrente. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - DB2 deadlock timeout |
| Citacao de suporte | the object you are trying to access is locked by another user, or by you in another session, but the lock has not been detected by the application. So the application waits to get access until it is interrupted by the DB2 timeout |
| Coletado em | 2026-08-23 |
| Capacidade | database |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=lock |
| Status de revisao | verified |
| Tipo | command |
| Familia | incident-db2 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: 'The current transaction has been rolled back because of a deadlock or timeout?
- O que causa e como solucionar o problema: 'The current transaction has been rolled back because of a deadlock or timeout?


---

### 113. `hwa-10.2.8-incident-dwc-role-task-0129`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'. Causa: o usuario nao tem o role necessario para rodar a tarefa — para rodar uma tarefa e preciso um role que permita acessar os paineis do DWC relevantes ao tipo de tarefa. Resolucao: configurar os roles adequados para o usuario (ver Administration Guide, secao de roles do DWC). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - DWC role task |
| Citacao de suporte | You do not have the necessary role required to run the task. To run a task you must have a role that allows you to access the Dynamic Workload Console panels that are relevant to the type of task you need. |
| Coletado em | 2026-08-23 |
| Capacidade | console |
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
| Ferramenta | dwc |
| Familia | incident-dwc |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'?
- O que causa e como solucionar o problema: ao acessar um bookmark de tarefa no Dynamic Workload Console, recebe o erro 'User does not have access to view this page'?


---

### 114. `hwa-10.2.8-incident-event-lost-queue-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `events`

**Afirmacao / Conteudo:**

Sintoma: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue. Causa: a event queue e circular — eventos sao adicionados no fim e removidos do inicio; quando nao ha espaco para escrever no fim, o evento e escrito no inicio, sobrescrevendo o evento mais antigo. Resolucao: o evento sobrescrito nao pode ser recuperado; aumentar o tamanho da queue para evitar recorrencia (ver 'Managing the event queue' no Administration Guide). Fonte: HCL Troubleshooting Guide 10.2.8 (An event is lost).

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
| Citacao de suporte | The event queue is not big enough. The event queue is circular, with events being added at the end and removed from the beginning. However, if there is no room to write an event at the end of the queue it is written at the beginning, overwriting the event at the beginning of the queue. |
| Capacidade | events |
| Classificacao de risco | mutating |
| Modo de operacao | guided_action |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial (awstrmst.pdf, Troubleshooting Guide 10.2.8); sem prova de laboratório nesta fase (F3) — validação prática requer ambiente com o componente relevante ativo. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-event |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue?
- O que causa e como solucionar o problema: apos enviar um grande numero de eventos ao event processor, o(s) evento(s) mais recente(s) estao ausentes da event queue?


---

### 115. `hwa-10.2.8-incident-external-lock-timeout-0109`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto. Causa: o objeto esta locked de fora do HCL Workload Automation — por exemplo, pelo database administrator ou por uma funcao automatica do banco — e a aplicacao espera ate ser interrompida pelo timeout do application server. Resolucao: identificar e liberar o lock externo, ou ajustar os timeouts. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - external lock timeout |
| Citacao de suporte | the object you are trying to access is locked from outside HCL Workload Automation, maybe by the database administrator or an automatic database function. So the application waits to get access until it is interrupted by the application server timeout |
| Coletado em | 2026-08-23 |
| Capacidade | database |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=lock |
| Status de revisao | verified |
| Tipo | command |
| Familia | incident-external |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto?
- O que causa e como solucionar o problema: Request timed out (vmcid: IBM minor code: B01) ao acessar um objeto?


---

### 116. `hwa-10.2.8-incident-graphical-designer-java-0132`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: ao trabalhar com um job no Graphical Designer, recebe um erro (ex.: AWSITA122E ou AWKRAA209E - The job with advanced options with ID application_type was not found). Causa: um erro inesperado ocorreu ao executar um metodo Java; ou o job com advanced options nao pode ser encontrado. Resolucao: (1) checar o JobManager_message.log; (2) checar o log mais recente em /opt/ibm/TWA/TWS/JavaExt/eclipse/configuration/*.log; (3) se o job plug-in nao for encontrado: garantir que o job plug-in esta em /opt/IBM/TWA/TWS/JavaExt/eclipse/plugins e listado no config.ini. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Graphical Designer java |
| Citacao de suporte | An unexpected error occurred while running a Java method... Ensure that the job plug-in is present in the /opt/IBM/TWA/TWS/JavaExt/eclipse/plugins directory. |
| Coletado em | 2026-08-23 |
| Capacidade | console |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA122E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | gui |
| Codigo da mensagem | AWSITA122E |
| Familia | incident-graphical |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA122E no HWA?
- Como solucionar ou diagnosticar o erro AWSITA122E no HWA?
- Qual é o significado da mensagem de erro AWKRAA209E no HWA?
- Como solucionar ou diagnosticar o erro AWKRAA209E no HWA?
- O que causa e como solucionar o problema: ao trabalhar com um job no Graphical Designer, recebe um erro (ex?


---

### 117. `hwa-10.2.8-incident-hadr-db2-console-0131`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado. Causa: quando o no primario do DB2 para, cada request do DWC espera por um switch manual para o no standby. Resolucao: verificar que o no primario esta ativo e rodando. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - HADR DB2 console |
| Citacao de suporte | When DB2 primary node stops, every Dynamic Workload Console request waits for a manual switch to a standby node... verify that your primary node is up and running. |
| Coletado em | 2026-08-23 |
| Capacidade | console |
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
| Ferramenta | dwc |
| Familia | incident-hadr |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado?
- O que causa e como solucionar o problema: em uma configuracao de high availability disaster recovery (HADR) DB2, o Dynamic Workload Console exibe painel vazio ou bloqueado?


---

### 118. `hwa-10.2.8-incident-hold-at-past-0017`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `hold`

**Afirmacao / Conteudo:**

Sintoma: job submetido com at=HHMM fica HOLD e so executa no dia seguinte. Causa: o horario especificado ja passou no plano corrente; o job e agendado para a proxima ocorrencia valida (possivelmente no dia seguinte). Resolucao: verificar o horizonte do plano e usar at= com data explicita ou into=STREAM(hhmm) para controlar a instancia.

> **ATENCAO / RESSALVAS DE USO:** Lab 22/08: sbd at=1750 -> HOLD 08/23 (claim 0131).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.html |
| Titulo da fonte | Troubleshooting guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | at=hhmm next occurrence |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | hold |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Familia | incident-hold |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: job submetido com at=HHMM fica HOLD e so executa no dia seguinte?
- O que causa e como solucionar o problema: job submetido com at=HHMM fica HOLD e so executa no dia seguinte?


---

### 119. `hwa-10.2.8-incident-hold-deps-0016`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `hold`

**Afirmacao / Conteudo:**

Sintoma: job permanece em HOLD sem executar. Causa: dependencias nao satisfeitas (follows, needs, opens, prompt) ou horario agendado ainda nao alcancado (at= no futuro). Resolucao: verificar as dependencias com sj / showjobs (coluna de dependencias), liberar com rj (release job) quando apropriado, ou aguardar o horario.

> **ATENCAO / RESSALVAS DE USO:** Lab 22/08: sbd follows JOBS.AT_TEST_001 -> HOLD ate dependencia satisfeita (claim 0134).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.html |
| Titulo da fonte | Troubleshooting guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | job HOLD dependencies |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | hold |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | release; showjobs |
| Familia | incident-hold |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: job permanece em HOLD sem executar?


---

### 120. `hwa-10.2.8-incident-impersonate-right-0096`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `security`

**Afirmacao / Conteudo:**

Sintoma: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows. Causa: a conta de usuario usada para rodar a linha de comando do HWA nao tem o direito de usuario 'Impersonate a client after authentication' (setting de seguranca de um subconjunto de versoes Windows); o upgrade nao concede esse direito a usuarios existentes. Resolucao: conceder o direito de usuario 'Impersonate a client after authentication' a conta. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - impersonation level |
| Citacao de suporte | This issue occurs when the user account that is used to run the HCL Workload Automation command line does not have the user right: Impersonate a client after authentication |
| Coletado em | 2026-08-23 |
| Capacidade | security |
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
| verbs | upgrade |
| Familia | incident-impersonate |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows?
- O que causa e como solucionar o problema: erro de CLI do HWA com mensagem 'Either a required impersonation level was not provided, or the provided impersonation level is invalid' em Windows?


---

### 121. `hwa-10.2.8-incident-import-dwc-privileges-0133`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr.log. Causa: o usuario do banco com autoridade administrativa especificado para importar os settings nao tem os privilegios necessarios para drop das tabelas existentes do DWC criadas com DWC V8.6.0.0. Resolucao: fornecer ao usuario especificado o privilegio CONTROL sobre as tabelas (ou o privilegio equivalente) antes do import. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - import DWC privileges |
| Citacao de suporte | This might occur because the database user with administrative authority specified to import the settings does not have the privileges required to drop the existing Dynamic Workload Console tables |
| Coletado em | 2026-08-23 |
| Capacidade | database |
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
| Ferramenta | dwc |
| verbs | import |
| Familia | incident-import |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr?
- O que causa e como solucionar o problema: ao importar settings para o repository DB2, o import falha com erro DB2 SQLCODE -601 no SystemErr?


---

### 122. `hwa-10.2.8-incident-jar-corrupt-deploy-0099`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `deploy`

**Afirmacao / Conteudo:**

Sintoma: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy. Causa: o arquivo .jar identificado na mensagem esta corrompido. Resolucao: verificar e corrigir o formato do arquivo antes de tentar o deploy novamente. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - corrupt jar deploy |
| Citacao de suporte | The .jar file identified in the message is corrupt. Check and correct the format of the file before retrying the deploy. |
| Coletado em | 2026-08-23 |
| Capacidade | deploy |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=deploy |
| Status de revisao | verified |
| Tipo | command |
| verbs | deploy |
| Familia | incident-jar |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy?
- O que causa e como solucionar o problema: erro 'error reading <file_name>; Error opening zip file <file_name>' ao fazer deploy?


---

### 123. `hwa-10.2.8-incident-jco084e-0058`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `updatestats`

**Afirmacao / Conteudo:**

Sintoma: AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' ao executar UpdateStats em um plano grande. Causa: quando o UpdateStats roda por mais de duas horas (job run time excede 2h), o job falha com AWSJCO084E — o tempo excessivo faz a autenticacao expirar/ficar invalida. Resolucao: reduzir o tempo de execucao do UpdateStats (ex.: reduzir o volume de jobs no plano, otimizar a janela) ou investigar por que demora mais de 2h; a mensagem e enganosa (parece erro de autorizacao mas e timeout de execucao). Fonte: HCL Troubleshooting Guide 10.2.8 (UpdateStats fails if job run time exceeds two hours).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF — a resposta do batch perplexity (AWSJCO084E = autorizacao/locking) foi CORRIGIDA: a causa real documentada e UpdateStats > 2h (timeout), nao credenciais. Importante: enriquecimento validado contra material oficial.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - UpdateStats fails if job run time exceeds two hours |
| Citacao de suporte | UpdateStats fails if it runs more than two hours (message AWSJCO084E given)... AWSJCO084E The user "UNAUTHENTICATED" is not authorized to work with the "planner" process. Cause and solution: This error occurs because the large number of jobs in the plan... |
| Coletado em | 2026-08-23 |
| Capacidade | updatestats |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCO084E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | planner |
| verbs | run |
| Codigo da mensagem | AWSJCO084E |
| Familia | incident-jco084e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO084E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?
- O que causa e como solucionar o problema: AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' ao executar UpdateStats em um plano grande?


---

### 124. `hwa-10.2.8-incident-jco084e-timeout-config-0101`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `updatestats`

**Afirmacao / Conteudo:**

Sintoma: UpdateStats em plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' porque o job run time excedeu duas horas. Causa: o default timeout das credenciais de usuario do WebSphere Application Server e 2 horas. Resolucao: aumentar o timeout para dar mais tempo ao UpdateStats: (1) navegar ate <TWA_home>/usr/servers/... (caminho do Liberty); (2) ajustar o timeout das credenciais. Fonte: HCL Troubleshooting Guide 10.2.8 (UpdateStats fails if it runs more than two hours).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Complementa hwa-10.2.8-incident-jco084e-0058 com o passo de aumentar o timeout.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSJCO084E timeout |
| Citacao de suporte | This error occurs because the large number of jobs in the plan has caused the job run time to exceed two hours, which is the default timeout for the user credentials of the WebSphere Application Server. To increase the timeout so that the UpdateStats command has more time to run... |
| Coletado em | 2026-08-23 |
| Capacidade | updatestats |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (config de timeout); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter o timeout para o valor anterior. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCO084E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | planner |
| verbs | run |
| Codigo da mensagem | AWSJCO084E |
| Familia | incident-jco084e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO084E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?
- O que causa e como solucionar o problema: UpdateStats em plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' porque o job run time excedeu duas horas?


---

### 125. `hwa-10.2.8-incident-jco135w-0052`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `jobman`

**Afirmacao / Conteudo:**

Sintoma: AWSJCO135W (warning) do job manager relacionado a agendamento/dependencias, frequentemente ligado a problemas de storage/mailbox ou disponibilidade do job manager. Causa: warning do jobman quando um valor padrao e aplicado ao processamento de jobs criticos porque o produto perdeu a conexao com o banco, ou problemas de startup/disponibilidade do job manager. Resolucao: (1) verificar o log do job manager para o subcomponente e RC exatos; (2) checar mensagens anteriores que precedem o warning; (3) verificar conectividade de banco e espaco de storage/mailbox; (4) reiniciar o job manager se necessario. Pesquisa Perplexity (2026-08-23).

> **ATENCAO / RESSALVAS DE USO:** Pesquisa Perplexity Direct batch (2026-08-23). Complementa hwa-10.2.8-incident-0005.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSJCO135W |
| Citacao de suporte | AWSJCO135W indicates a job manager warning related to scheduling or dependency handling, often tied to storage or mailbox issues |
| Coletado em | 2026-08-23 |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCO135W, command=jobman |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSJCO135W |
| Familia | incident-jco135w |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO135W no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO135W no HWA?
- O que causa e como solucionar o problema: AWSJCO135W (warning) do job manager relacionado a agendamento/dependencias, frequentemente ligado a problemas de storage/mailbox ou disponibilidade do job manager?


---

### 126. `hwa-10.2.8-incident-jco136e-0071`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: AWSJCO136E 'No more than 5 users are allowed to perform this operation at the same time' ao usar o Plan View conectado ao engine. Causa: o numero maximo de usuarios que podem usar o Plan View conectado ao mesmo engine e cinco. Resolucao: se necessario, modificar o limite editando a propriedade com.ibm.tws.conn.plan.view.maxusers no arquivo TWSConfig.properties. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSJCO136E).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (pagina 134).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSJCO136E |
| Citacao de suporte | AWSJCO136E No more than 5 users are allowed to perform this operation at the same time. The maximum number of users that can use the Plan View connected to the same engine is five. |
| Coletado em | 2026-08-23 |
| Capacidade | console |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCO136E |
| Status de revisao | verified |
| Tipo | message |
| verbs | plan |
| Codigo da mensagem | AWSJCO136E |
| Familia | incident-jco136e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO136E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO136E no HWA?
- O que causa e como solucionar o problema: AWSJCO136E 'No more than 5 users are allowed to perform this operation at the same time' ao usar o Plan View conectado ao engine?


---

### 127. `hwa-10.2.8-incident-jom915e-0020`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `syntax`

**Afirmacao / Conteudo:**

Sintoma: AWSJOM915E ao validar definicoes de job com keywords fora da ordem canonica (ex.: RECOVERY depois de PRIORITY, ou VARTABLE depois de ON RUNCYCLE). Causa: a ordem de keywords no job statement e obrigatoria. Resolucao: seguir a ordem follows → needs → opens → priority → prompt → nop (e VARTABLE antes de ON RUNCYCLE).

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 22/08 (claims 0115/0116/0129).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Job stream definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | keyword order |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | syntax |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['composer validate/add com keywords fora de ordem'], result=AWSJOM915E quando RECOVERY depois de PRIORITY; quando VARTABLE depois de ON RUNCYCLE; PRIORITY em $JOBS (10/HI/99) rejeitado na linha 7; posicao independente (lab-validation-2026-08-22-job-creation-gaps.jsonl), validated_at=2026-08-22T00:30:00BRT |
| Tipo | command |
| Codigo da mensagem | AWSJOM915E |
| Familia | incident-jom915e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM915E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?
- O que causa e como solucionar o problema: AWSJOM915E ao validar definicoes de job com keywords fora da ordem canonica (ex?


---

### 128. `hwa-10.2.8-incident-keystore-reload-0108`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `security`

**Afirmacao / Conteudo:**

Sintoma: Exception = java.io.IOException: Keystore was tampered with, or password was incorrect ao usar SSL/certificados. Causa: o certificado nao foi recarregado ou regenerado apos qualquer mudanca na senha do keystore no servidor ou connector. Resolucao: recarregar ou regenerar o certificado e reiniciar o application server; para regenerar, usar comando openssl genrsa. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - keystore tampered |
| Citacao de suporte | The certificate has not been reloaded or regenerated. Any change to the keystore password on the server or connector requires the SSL certificate to be reloaded or regenerated to work correctly. |
| Coletado em | 2026-08-23 |
| Capacidade | security |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (regeneracao de certificado); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar o certificado anterior. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-keystore |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: Exception = java?


---

### 129. `hwa-10.2.8-incident-ldap-multihomed-0136`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `security`

**Afirmacao / Conteudo:**

Sintoma: conta LDAP bloqueada apos UMA tentativa de autenticacao errada. Causa: quando um unico hostname LDAP e mapeado para multiplos enderecos IP na configuracao de rede, se uma senha invalida e digitada no login, o WebSphere faz tantas tentativas de login quanto o numero de IPs associados + 1; se o numero resultante excede o maximo de falhas de login permitido pela politica de seguranca LDAP/AD local, a conta e bloqueada. Resolucao: alinhar o DNS (um IP por hostname) ou ajustar a politica de bloqueio. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - LDAP multihomed |
| Citacao de suporte | When a single LDAP hostname is mapped to multiple IP addresses in a network configuration, if an invalid password is entered during the login, WebSphere makes as many login attempts as the number of associated IP addresses plus 1. |
| Coletado em | 2026-08-23 |
| Capacidade | security |
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
| verbs | login |
| Familia | incident-ldap |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: conta LDAP bloqueada apos UMA tentativa de autenticacao errada?
- O que causa e como solucionar o problema: conta LDAP bloqueada apos UMA tentativa de autenticacao errada?


---

### 130. `hwa-10.2.8-incident-liberty-cpu-tuning-0137`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `performance`

**Afirmacao / Conteudo:**

Sintoma: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts). Resolucao: para reduzir o uso de CPU para ~1 segundo de CPU por hora e reduzir os EXCP counts por um fator de 10: (1) editar <USERDIR>/servers/dwcServer/server.xml adicionando <config updateTrigger=disabled/> apos a string de comentario; (2) substituir todas as strings scaninterval=5s por scaninterval=... (intervalo maior). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Liberty CPU tuning |
| Citacao de suporte | To reduce the CPU usage to about 1 CPU second per hour, and reduce the EXCP counts by a factor of 10... add the following row: <config updateTrigger=disabled/> |
| Coletado em | 2026-08-23 |
| Capacidade | performance |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (config de servidor); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter as alteracoes do server.xml. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-liberty |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts)?
- O que causa e como solucionar o problema: o WebSphere Application Server Liberty Base usa muito CPU e faz muitas operacoes de I/O (EXCP counts)?


---

### 131. `hwa-10.2.8-incident-local-params-files-0122`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `parameters`

**Afirmacao / Conteudo:**

Sintoma: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente. Causa: um ou ambos os arquivos onde os parametros sao armazenados foram deletados ou renomeados. Resolucao: verificar que os arquivos parameters e parameters.KEY existem em TWA_home/TWS — sao necessarios para resolver local parameters e nao devem ser deletados/renomeados. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - local parameters files |
| Citacao de suporte | One reason for this could be that one or both of the files where the parameters are stored have been deleted or renamed. Check that the following files can be found in the TWA_home/TWS directory: parameters, parameters.KEY |
| Coletado em | 2026-08-23 |
| Capacidade | parameters |
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
| Familia | incident-local |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: Sintoma: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente?
- O que causa e como solucionar o problema: um job ou job stream que usa local parameters tem os parametros resolvidos incorretamente?


---

### 132. `hwa-10.2.8-incident-msl018e-0034`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `syntax`

**Afirmacao / Conteudo:**

Sintoma: AWSMSL018E 'dependency does not exist' ao usar ocli plan release job sem o separador '=' na sintaxe. Causa: o comando ocli plan release exige job=<nome> com '='; sem o '=' o parser interpreta o argumento como outra coisa e reporta dependencia inexistente. Resolucao: usar a sintaxe completa 'ocli plan release job=WS#STREAM.JOB' (com '='). O lab confirmou: ocli plan release job=MDMDA#JOBS.R8REL2 -> Command forwarded for MDMDA#JOBS[(0300 23/08/26),...].R8REL2; job SUCC RC 0.

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 23/08 (r8): sintaxe real do ocli plan release job exige job= com '='. Complementa a claim hwa-10.2.8-ocli-release-job-persist-0001.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_release_job.html |
| Titulo da fonte | ocli plan release job - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSMSL018E dependency does not exist (sem '='); job=<nome> com '=' funciona |
| Coletado em | 2026-08-23 |
| Capacidade | syntax |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['ocli plan release job=MDMDA#JOBS.R8REL2 (com =)', 'ocli plan release MDMDA#JOBS.R8REL2 (sem =)'], result=Com '=': Command forwarded for MDMDA#JOBS[(0300 23/08/26),...].R8REL2; job SUCC RC 0. Sem '=': AWSMSL018E 'dependency does not exist' (falso negativo de sintaxe), validated_at=2026-08-23T00:43:00BRT |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. Verificar se o job está em estado liberável (HOLD/READY). |
| Impacto | Pode alterar estado operacional do job (liberar de dependências); avaliar o escopo antes da execução. |
| Reversibilidade | Reaplicar hold (conman h) ou re-submeter conforme procedimento oficial de reversão. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSMSL018E, command=ocli |
| Status de revisao | lab_validated |
| Tipo | message |
| Ferramenta | ocli |
| verbs | plan; release |
| Codigo da mensagem | AWSMSL018E |
| Familia | incident-msl018e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSMSL018E no HWA?
- Como solucionar ou diagnosticar o erro AWSMSL018E no HWA?
- O que causa e como solucionar o problema: AWSMSL018E 'dependency does not exist' ao usar ocli plan release job sem o separador '=' na sintaxe?


---

### 133. `hwa-10.2.8-incident-msp104e-0053`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `mail`

**Afirmacao / Conteudo:**

Sintoma: AWSMSP104E ao enviar alertas de email/eventos — problema com mail sender name ou configuracao SMTP. Causa: o dominio do servidor SMTP nao esta definido na opcao mailSenderName, ou SMTP mal configurado. Resolucao: (1) definir um sender valido com dominio (ex.: tws@seudominio.com) na opcao mailSenderName usando o comando de gerenciamento apropriado; (2) reiniciar o servico de mail; (3) verificar conectividade SMTP. Pesquisa Perplexity (2026-08-23) confirma. Complementa hwa-10.2.8-trouble-awsmsp104e-0007.

> **ATENCAO / RESSALVAS DE USO:** Pesquisa Perplexity Direct batch (2026-08-23).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSMSP104E |
| Citacao de suporte | AWSMSP104E indicates an issue with email alerts related to the mail sender name or SMTP setup; the SMTP server domain is not defined in the mailSenderName option |
| Coletado em | 2026-08-23 |
| Capacidade | mail |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSMSP104E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSMSP104E |
| Familia | incident-msp104e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSMSP104E no HWA?
- Como solucionar ou diagnosticar o erro AWSMSP104E no HWA?
- O que causa e como solucionar o problema: AWSMSP104E ao enviar alertas de email/eventos — problema com mail sender name ou configuracao SMTP?


---

### 134. `hwa-10.2.8-incident-mssql-cascade-30-0107`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro. Causa: deletar com opcao cascade uma linha que contem mais de 30 referencias nao e suportado em MSSQL. Resolucao: evitar cascade com mais de 30 referencias no MSSQL; dividir a operacao. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - MSSQL cascade |
| Citacao de suporte | Deleting with cascade option a row which contains more than 30 references is not supported in MSSQL. |
| Coletado em | 2026-08-23 |
| Capacidade | database |
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
| Familia | incident-mssql |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro?
- O que causa e como solucionar o problema: ao fazer record deletion com opcao cascade em MSSQL, recebe mensagem de erro?


---

### 135. `hwa-10.2.8-incident-oracle-permission-0105`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX. Causa: o usuario de administracao do Oracle nao tem permissao de leitura em todo o caminho do diretorio de instalacao do HWA. Resolucao: conceder permissao de leitura ao usuario do Oracle para cada diretorio do caminho (ex.: /opt, /myProducts e /TWS). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Oracle permission |
| Citacao de suporte | The problem could be that the Oracle administration user does not have read permission for the entire path of the HCL Workload Automation installation directory |
| Coletado em | 2026-08-23 |
| Capacidade | database |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (permissoes); avaliar o escopo antes da execucao. |
| Reversibilidade | Remover as permissoes concedidas. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-oracle |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX?
- O que causa e como solucionar o problema: apos instalar o HWA criando o diretorio de instalacao com o usuario root default, ao trocar para o usuario de administracao do Oracle nao e possivel fazer manutencao Oracle em UNIX?


---

### 136. `hwa-10.2.8-incident-oracle-reports-privileges-0139`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `reports`

**Afirmacao / Conteudo:**

Sintoma: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console. Causa: o usuario do banco especificado nas propriedades da engine connection nao tem os privilegios para rodar reports. Resolucao (somente Oracle): como administrador do Oracle: (1) atribuir ao usuario do banco o System privilege CREATE TABLE; (2) rodar o script (Windows: TWA_home\TWS\dbtools\oracle\script\d...). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Oracle reports privileges |
| Citacao de suporte | On Oracle databases only, you must run these steps, as Oracle database administrator, to allow the database user specified in the engine connection properties to run reports: Assign to the database user the CREATE TABLE Oracle System privilege. |
| Coletado em | 2026-08-23 |
| Capacidade | reports |
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
| verbs | create |
| Familia | incident-oracle |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console?
- O que causa e como solucionar o problema: erro WSWUI0331E ao rodar reports em um banco Oracle pelo Dynamic Workload Console?


---

### 137. `hwa-10.2.8-incident-rce012e-0078`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `remote-command`

**Afirmacao / Conteudo:**

Sintoma: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao. Causa: (1) o host name especificado para o computador onde a instancia do remote command roda nao existe; (2) o numero da porta esta incorreto (diferente do configurado para o protocolo); (3) o tipo de protocolo especificado nao consegue estabelecer conexao porque o computador remoto nao aceita aquele protocolo. Resolucao: validar hostname, porta e protocolo. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSKRCE012E |
| Citacao de suporte | After submitting a remote command job, error message AWKRCE012E indicates that an error has occurred establishing a connection. The host name specified for the computer does not exist. The port number is incorrect. |
| Coletado em | 2026-08-23 |
| Capacidade | remote-command |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSKRCE012E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSKRCE012E |
| Familia | incident-rce012e |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao?
- O que causa e como solucionar o problema: apos submeter um remote command job, AWSKRCE012E 'Could not establish a connection' indica erro ao estabelecer conexao?


---

### 138. `hwa-10.2.8-incident-remote-registry-0126`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `remote-command`

**Afirmacao / Conteudo:**

Sintoma: remote command job entra em ABEND com AWKRCE012E 'Could not establish a connection'. Causa: um servico Windows necessario pode estar parado — iniciar o servico Remote Registry no sistema remoto. Nota: um Remote Command job que roda em workstation Windows configurada com samba protocol version 2 ou 3, sem servidor SSH ativo, falha. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Complementa hwa-10.2.8-incident-rce012e-0078.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - remote registry |
| Citacao de suporte | A necessary Windows service might be stopped. Start the Remote Registry Windows service on the remote system. |
| Coletado em | 2026-08-23 |
| Capacidade | remote-command |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | message |
| verbs | version |
| Codigo da mensagem | AWKRCE012E |
| Familia | incident-remote |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWKRCE012E no HWA?
- Como solucionar ou diagnosticar o erro AWKRCE012E no HWA?
- O que causa e como solucionar o problema: remote command job entra em ABEND com AWKRCE012E 'Could not establish a connection'?


---

### 139. `hwa-10.2.8-incident-rmstdlist-aix-126-0113`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `stdlist`

**Afirmacao / Conteudo:**

Sintoma: o comando rmstdlist falha em AIX com exit code 126. Causa: pode haver muitos arquivos de log no diretorio stdlist. Resolucao: em AIX, remover regularmente os standard list files a cada 10-20 dias (ver User's Guide and Reference). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - rmstdlist AIX 126 |
| Citacao de suporte | This could be because there are too many log files in the stdlist directory. On AIX, you should regularly remove standard list files every 10-20 days. |
| Coletado em | 2026-08-23 |
| Capacidade | stdlist |
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
| verbs | list |
| Familia | incident-rmstdlist |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: o comando rmstdlist falha em AIX com exit code 126. Causa: pode haver muitos arquivos de log no diretorio stdlist?
- O que causa e como solucionar o problema: o comando rmstdlist falha em AIX com exit code 126?


---

### 140. `hwa-10.2.8-incident-rmstdlist-mtime-0112`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `stdlist`

**Afirmacao / Conteudo:**

Sintoma: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas. Causa: em UNIX, o comando usa a opcao -mtime do find, que e interpretada de forma diferente nas varias plataformas UNIX. Resolucao: considerar a interpretacao do -mtime na plataforma (ex.: rmstdlist -p 6 da os mesmos resultados que...). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - rmstdlist mtime |
| Citacao de suporte | This is because on UNIX platforms the command uses the -mtime option of the find command, which is interpreted differently on different UNIX platforms. |
| Coletado em | 2026-08-23 |
| Capacidade | stdlist |
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
| Familia | incident-rmstdlist |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas?
- O que causa e como solucionar o problema: o comando rmstdlist da resultados diferentes em plataformas UNIX distintas?


---

### 141. `hwa-10.2.8-incident-root-ownership-0115`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `permissions`

**Afirmacao / Conteudo:**

Sintoma: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos. Causa: diretorios ou arquivos com ownership root nao foram recriados durante a fase de inicializacao. Resolucao: em UNIX, criar o diretorio/arquivo deletado com twsuser e group ownership, ou modificar o ownership do que foi criado com root; em Windows, procedimento equivalente. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - root ownership |
| Citacao de suporte | This problem occurs because the directories or files with root ownership are not re-created during the initialization phase. Create the directory or file that you deleted with twsuser and group ownership. |
| Coletado em | 2026-08-23 |
| Capacidade | permissions |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (ownership); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter o ownership. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-root |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos?
- O que causa e como solucionar o problema: erro 'Permission denied' ou 'Bad file descriptor' em diretorios/arquivos?


---

### 142. `hwa-10.2.8-incident-schedlog-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `observability`

**Afirmacao / Conteudo:**

Sintoma: diagnosticar por que um job falhou ou nao iniciou. Resolucao: o schedlog (log do scheduler) registra as atividades de cada workstation; consultar o schedlog no diretorio de logs da workstation (TWS_home/stdlist e schedlog) para rastrear a causa raiz.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.html |
| Titulo da fonte | Troubleshooting guide - HCL Workload Automation 10.2.8 |
| Citacao de suporte | schedlog |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | observability |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | scheduler |
| Familia | incident-schedlog |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: diagnosticar por que um job falhou ou nao iniciou?
- O que causa e como solucionar o problema: diagnosticar por que um job falhou ou nao iniciou?


---

### 143. `hwa-10.2.8-incident-session-invalid-0135`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `console`

**Afirmacao / Conteudo:**

Sintoma: 'Session has become invalid' ao usar a interface do Dynamic Workload Console. Causa: a sessao de trabalho fechou — por logoff manual, timeout do HTTP session ou timeout da sessao LTPA (Lightweight Third Party Authentication), ou outro usuario invalidou a sessao logando com o mesmo User ID. Resolucao: verificar qual razao ocorreu, resolver o problema e logar novamente; se timeout, customizar os settings de timeout. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - session invalid |
| Citacao de suporte | Check which reason among those listed in the warning has occurred... If the session expired because either the HTTP session or the Lightweight Third Party Authentication (LTPA) session timeout was exceeded, you might decide to customize the timeout settings |
| Coletado em | 2026-08-23 |
| Capacidade | console |
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
| Familia | incident-session |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: 'Session has become invalid' ao usar a interface do Dynamic Workload Console?
- O que causa e como solucionar o problema: 'Session has become invalid' ao usar a interface do Dynamic Workload Console?


---

### 144. `hwa-10.2.8-incident-table-locked-db-gui-0110`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento. Causa: um usuario travou a tabela usando a linha de comando ou GUI do banco. DB2: apenas abrir a GUI do DB2 ja e suficiente para travar as tabelas, negando acesso a todos os processos do HWA. Oracle: abrir a linha de comando do Oracle sem auto-commit, ou a GUI, trava todas as tabelas. Resolucao: fechar a GUI/linha de comando do banco que esta segurando os locks. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Correlaciona com AWSJPL018E (database locked).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - table locked by DB GUI |
| Citacao de suporte | The probable cause is that a user has locked the table by using the database command-line or GUI. DB2: Just opening the DB2 GUI is sufficient to lock the database tables, denying access to all HCL Workload Automation processes. |
| Coletado em | 2026-08-23 |
| Capacidade | database |
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
| Ferramenta | gui |
| Familia | incident-table |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento?
- O que causa e como solucionar o problema: mensagem de erro indicando que uma funcao nao pode ser executada porque uma tabela, ou um objeto em uma tabela, esta locked — embora nenhuma operacao do HWA esteja em andamento?


---

### 145. `hwa-10.2.8-incident-tcl-hang-0093`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `windows`

**Afirmacao / Conteudo:**

Sintoma: em Windows, CreatePostReports.cmd, Makeplan.cmd, Updatestats.cmd ou rep8.cmd travam (hang) e os jobs nao completam. Causa: o interpretador Tool Command Language (TCL) trava sem retornar resposta ao chamador. Resolucao: esses jobs usam por default o interpretador TCL mas podem ser configurados para nao usa-lo — configurar para nao usar TCL evita o travamento. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - TCL hang Windows |
| Citacao de suporte | the Tool Command Language interpreter hangs not returning an answer to the caller and the jobs do not complete. These jobs use by default the Tool Command Language interpreter but can be configured to not use it. |
| Coletado em | 2026-08-23 |
| Capacidade | windows |
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
| Ferramenta | planner |
| Familia | incident-tcl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: em Windows, CreatePostReports?
- O que causa e como solucionar o problema: em Windows, CreatePostReports?


---

### 146. `hwa-10.2.8-incident-terminal-services-interactive-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `windows`

**Afirmacao / Conteudo:**

Sintoma: ao rodar um job interativo remotamente em um fault-tolerant agent Windows via Terminal Services (Dynamic Workload Console ou linha de comando), a janela do programa de aplicacao nao abre na tela do Terminal Services, embora o programa esteja rodando no FTA. Causa: limitacao do Terminal Services, sem workaround conhecido. Resolucao: jobs interativos devem ser executados por um usuario logado no proprio fault-tolerant agent; nao podem ser executados remotamente via Terminal Services. Jobs que nao requerem interacao do usuario nao sao afetados. Fonte: HCL Troubleshooting Guide 10.2.8 (Interactive jobs are not interactive using Terminal Services).

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
| Citacao de suporte | The problem is a limitation of Terminal Services, and there is no known workaround. All "interactive jobs" must be run by a user at the fault-tolerant agent, and cannot be run remotely, using Terminal Services. |
| Capacidade | windows |
| Classificacao de risco | read_only |
| Modo de operacao | read |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-terminal |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: ao rodar um job interativo remotamente em um fault-tolerant agent Windows via Terminal Services (Dynamic Workload Console ou linha de comando), a janela do programa de aplicacao nao abre na tela do Terminal Services, embora o programa esteja rodando no FTA?


---

### 147. `hwa-10.2.8-incident-time-misaligned-0103`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `timezone`

**Afirmacao / Conteudo:**

Sintoma: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo. Causa: o tempo configurado nas workstations onde o master e o engine estao instalados nao esta alinhado. Resolucao (workaround): alinhar o tempo de todas as workstations da rede IBM Workload Scheduler, mesmo que estejam em timezones diferentes. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - time misaligned |
| Citacao de suporte | This situation arises when the time set on the workstations where the master and the engine are installed are not aligned. As a workaround for this problem, align the time of all the workstations belonging to the IBM Workload Scheduler network |
| Coletado em | 2026-08-23 |
| Capacidade | timezone |
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
| Familia | incident-time |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo?
- O que causa e como solucionar o problema: a duracao de um job stream submetido pode ser calculada incorretamente, assim como outros calculos relacionados a tempo?


---

### 148. `hwa-10.2.8-incident-timezone-feature-0119`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `timezone`

**Afirmacao / Conteudo:**

Sintoma: o status relacionado a tempo de um job (ex.: 'Late') nao e reportado corretamente nas workstations porque a feature de time zone nao esta habilitada. Resolucao: habilitar a feature de time zone (ver User's Guide and Reference; ver Administration Guide para habilitar nas opcoes globais). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - time zone feature |
| Citacao de suporte | Enable the time zone feature to resolve this problem. |
| Coletado em | 2026-08-23 |
| Capacidade | timezone |
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
| verbs | status |
| Familia | incident-timezone |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: o status relacionado a tempo de um job (ex?
- O que causa e como solucionar o problema: o status relacionado a tempo de um job (ex?


---

### 149. `hwa-10.2.8-incident-ulimit-concurrent-jobs-0127`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `performance`

**Afirmacao / Conteudo:**

Sintoma: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes. Causa: memoria insuficiente e limite de processos por usuario para rodar os jobs concorrentemente. Resolucao: verificar e ajustar os ulimit settings (data, stack, etc.) — a submissao de um numero significativo de jobs Java requer grande quantidade de memoria; aumentar os valores de ulimit. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - ulimit concurrent jobs |
| Citacao de suporte | This problem is due to insufficient memory and the process number per user allocated to run the jobs concurrently... The submission of a significant number of Java jobs requires a large amount of memory. Change the value for data, stack |
| Coletado em | 2026-08-23 |
| Capacidade | performance |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (ulimit); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter os valores de ulimit. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-ulimit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes?
- O que causa e como solucionar o problema: memory dump ou mensagem 'resource temporarily unavailable' ao submeter muitos jobs Java concorrentes?


---

### 150. `hwa-10.2.8-incident-wui0331e-sql-0138`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `reports`

**Afirmacao / Conteudo:**

Sintoma: AWSWUI0331E 'The SQL query could not be validated' ao rodar um report no Dynamic Workload Console. Causa: erro de sintaxe no statement da query (ex.: 'sele' no lugar de 'select'). Resolucao: verificar se a query SQL esta correta e, opcionalmente, tentar rodar a mesma query a partir da linha de comando do DB2 para validar. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSWUI0331E SQL |
| Citacao de suporte | The validate failure is caused by a syntax error in the query statement, for example, a typing error... Verify the SQL query is correct. |
| Coletado em | 2026-08-23 |
| Capacidade | reports |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSWUI0331E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSWUI0331E |
| Familia | incident-wui0331e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSWUI0331E no HWA?
- Como solucionar ou diagnosticar o erro AWSWUI0331E no HWA?
- Qual a ação recomendada para a mensagem AWSUI0331E no DWC?
- O que causa e como solucionar o problema: AWSWUI0331E 'The SQL query could not be validated' ao rodar um report no Dynamic Workload Console?


---

### 151. `hwa-10.2.8-jobsstate-ready-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `monitor`

**Afirmacao / Conteudo:**

Os estados de exibição de jobs incluem: READY (todas as dependências resolvidas, pronto para lançar), EXEC (em execução), WAIT (em espera), ABEND (terminou anormalmente) e SUCC (concluído com sucesso).

> **ATENCAO / RESSALVAS DE USO:** Página documenta o formato standard do showjobs (Orchestration CLI). Estados adicionais documentados incluem HOLD, FAIL, PEND, SUPPR, INTRO, SCHED, entre outros; a lista não é exaustiva apenas com EXEC/WAIT/ABEND.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | READY=READY, EXEC=EXEC, WAIT=WAIT, ABEND=ABEND, SUCC=SUCC, job_state=estado do job |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/c_showjob_standard.html |
| Titulo da fonte | Standard format |
| Citacao de suporte | READY All the dependencies are resolved and the job stream is ready to launch. ... EXEC The selected job is running. ... WAIT Indicates the job is in wait. ... ABEND The job ended abnormally. ... SUCC The job is completed successfully. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | job_states |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | jobsstate-ready |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os estados de exibição de jobs incluem: READY (todas as dependências resolvidas, pronto para lançar), EXEC (em execução), WAIT (em espera), ABEND (terminou anormalmente) e SUCC (concluído com sucesso)?


---

### 152. `hwa-10.2.8-k8s-deploy-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os componentes podem ser implantados em Kubernetes/OpenShift usando helm charts: ha guias oficiais para Red Hat OpenShift, Azure AKS, Google GKE e AWS EKS. O deployment containerizado usa imagens do registry (hclcr.io) e o helm chart define os valores (values.yaml) para os componentes (MDM, DWC, agentes, AIDA).

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial HCL 10.2.8 (deploy guides para EKS, AKS, GKE, OpenShift). O helm chart do AIDA foi lido anteriormente (hcl-workload-automation-chart). [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1024/common/src_gi/eqqg1awseks.html |
| Titulo da fonte | Deploy HCL Workload Automation containers on AWS EKS - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Deploy HCL Workload Automation containerized product components on Amazon EKS / Azure AKS / Google GKE using a chart. |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_deploy |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | deploy |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?


---

### 153. `hwa-10.2.8-k8s-deploy-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o helm chart oficial de deployment em Kubernetes instala por padrao um unico servidor (master domain manager), um Dynamic Workload Console e um dynamic agent; para alta disponibilidade, a configuracao minima e composta por 2 Dynamic Workload Consoles e 2 servidores (master domain managers), e os componentes podem ser adicionados em multiplos namespaces e failure zones dentro de um mesmo cluster.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (HCL-TECH-SOFTWARE/hcl-workload-automation-chart). Detalha topologia default e requisito minimo de HA em K8s. [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideppec.html |
| Titulo da fonte | Considerations about deploying with containers - HCL Workload Automation 10.2.8 |
| Citacao de suporte | By default, a single server (master domain manager), Dynamic Workload Console (console) and dynamic agent is installed. To achieve high availability in an HCL Workload Automation environment, the minimum base configuration is composed of 2 Dynamic Workload Consoles and 2 servers (master domain managers). HCL Workload Automation can be deployed across a single cluster, but you can add multiple instances of the product components by using a different namespace in the cluster. |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_deploy |
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
- Como configurar ou solucionar problemas no dynamic agent ou broker para deployment?


---

### 154. `hwa-10.2.8-k8s-deploy-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes suporta plataformas amd64 nas seguintes infraestruturas: Amazon EKS, Azure AKS, Google GKE e Red Hat OpenShift (OCP); o suporte a OpenShift foi formalmente testado com OpenShift 4.14 no HCL Workload Automation 10.2.7, e para Server e Console deve-se alterar os parametros waserver.server.exposeServiceType e waconsole.console.exposeServiceType de LoadBalancer para Routes.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Supported Platforms / Openshift support). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideployazure.html |
| Titulo da fonte | Deploying on Azure AKS - HCL Workload Automation 10.2.8 |
| Citacao de suporte | HCL Workload Automation containers can be deployed into the following supported third-party cloud provider infrastructures: Amazon EKS, Microsoft Azure Kubernetes Service (AKS), Google Kubernetes Engine (GKE), OpenShift (OCP). HCL Workload Automation 10.2.7 was formally tested by using Openshift 4.14. For Server and Console component ensure to modify the value of these parameters: waserver.server.exposeServiceType, waconsole.console.exposeServiceType. From LoadBalancer to Routes |
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
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes suporta plataformas amd64 nas seguintes infraestruturas: Amazon EKS, Azure AKS, Google GKE e Red Hat OpenShift (OCP); o suporte a OpenShift foi formalmente testado com OpenShift 4.14 no HCL Workload Automation 10.2.7, e para Server e Console deve-se alterar os parametros waserver?


---

### 155. `hwa-10.2.8-k8s-deploy-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os recursos minimos documentados para deployment em Kubernetes sao: Server com limite de CPU 4 e memoria 16Gi (request CPU 1, memoria 4Gi, storage 10Gi), Console com limite CPU 4 e memoria 16Gi (request CPU 1, memoria 4Gi, storage 10Gi), e Dynamic Agent com request CPU 200m, memoria 200Mi e storage 2Gi; storage persistent via PVC criados pelo helm chart (um PVC por instancia de componente: data-wa-waserver-waserver0, data-wa-waconsole-waconsole0, data-wa-waagent-waagent0).

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Resources Required). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awspimst.pdf |
| Titulo da fonte | HCL Workload Automation Planning and Installation Version 10.2.8 (Deploying with containers) |
| Citacao de suporte | Server: CPU: 4, Memory: 16Gi (request CPU: 1, Memory: 4Gi, Storage: 10Gi); Console: CPU: 4, Memory: 16Gi (request CPU: 1, Memory: 4Gi, Storage: 10Gi); Dynamic Agent: CPU: 1, Memory: 2Gi (request CPU: 200m, Memory: 200Mi, Storage size: 2Gi) |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_deploy |
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
- Como configurar ou solucionar problemas no dynamic agent ou broker para deployment?


---

### 156. `hwa-10.2.8-k8s-deploy-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os secrets de senha em deployment Kubernetes sao armazenados em um objeto Secret do Kubernetes (wa-pwd-secret, tipo Opaque) com os campos WA_PASSWORD, DB_ADMIN_PASSWORD e DB_PASSWORD codificados em base64 no arquivo mysecret.yaml; opcionalmente o secret <release_name>-ssl-secret com SSL_PASSWORD pode forçar a senha do keystore, e a partir da versao 10.2, se as senhas do keystore secret e do secret opcional nao coincidirem, os keystores sao removidos e recriados com a senha definida, permitindo rotacao da senha do keystore.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Creating a secrets file). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideployazure.html |
| Titulo da fonte | Deploying on Azure AKS - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The mysecret.yaml file must contain the following parameters: WA_PASSWORD, DB_ADMIN_PASSWORD, DB_PASSWORD. Starting from v 10.2, if the passwords in the keystore secret and in the secret optionally created in step 3, do not match, keystores are removed and recreated from scratch using the password you defined. This mechanism allows you to rotate the keystore password when necessary. |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_secrets |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | k8s |
| verbs | deploy; release |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os secrets de senha em deployment Kubernetes sao armazenados em um objeto Secret do Kubernetes (wa-pwd-secret, tipo Opaque) com os campos WA_PASSWORD, DB_ADMIN_PASSWORD e DB_PASSWORD codificados em base64 no arquivo mysecret?


---

### 157. `hwa-10.2.8-k8s-deploy-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes criptografa dados em transito com TLS 1.2, dados em repouso com criptografia passiva de disco, secrets em Kubernetes Secrets aprovados, e logs livres de informacoes sensiveis; o chart instala os objetos wa-pwd-secret, certificados secret (wa-waserver/wa-waagent), network policies (mdm-network-policy, dwc-network-policy, da-network-policy) e services (wa-waserver-h, wa-waconsole-h, wa-waagent-h) por componente.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Details / Data encryption). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideppec.html |
| Titulo da fonte | Considerations about deploying with containers - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Data encryption: Data in transit encrypted using TLS 1.2, Data at rest encrypted using passive disk encryption, Secrets are stored in an approved Kubernetes Secrets, Logs are clear of all sensitive information. |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=k8s |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | deploy |
| Familia | k8s-deploy |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o deployment containerizado em Kubernetes criptografa dados em transito com TLS 1.2, dados em repouso com criptografia passiva de disco, secrets em Kubernetes Secrets aprovados, e logs livres de informacoes sensiveis; o chart instala os objetos wa-pwd-secret, certificados secret (wa-waserver/wa-waagent), network policies (mdm-network-policy, dwc-network-policy, da-network-policy) e services (wa-waserver-h, wa-waconsole-h, wa-waagent-h) por componente?


---

### 158. `hwa-10.2.8-k8s-deploy-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `kubernetes` / `deployment`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o armazenamento persistente em deployment Kubernetes usa PVCs com access mode ReadWriteOnce; os tipos de disco suportados por provedor incluem AWS EBS GP2/IO1 SSD (EKS), Azure File/Azure Disk SSD com volumeBindingMode WaitForFirstConsumer (AKS), e GCP Standard/Balanced/SSD Persistent Disks (GKE); para o banco MSSQL em nuvem (Azure SQL ou Google Cloud SQL for SQL Server), define-se type=MSSQL no values.yaml do server e console.

> **ATENCAO / RESSALVAS DE USO:** Fonte: README oficial do helm chart (sec. Storage classes static PV and dynamic provisioning / Configuring the Microsoft Azure SQL server database). [2026-08-25: fonte reescrita para URL oficial help.hcl-software.com v1028]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspideployazure.html |
| Titulo da fonte | Deploying on Azure AKS - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The volumeBindingMode must be set to WaitforFirstConsumer and not Immediate. AWS EBS GP2 SSD / IO1 SSD; Azure File SSD / Azure Disk SSD; GCP Standard/Balanced/SSD Persistent Disks. To use the database with both the server and console components, set the type parameter to type=MSSQL in the values.yaml file. |
| Coletado em | 2026-08-25 |
| Capacidade | k8s_storage |
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
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o armazenamento persistente em deployment Kubernetes usa PVCs com access mode ReadWriteOnce; os tipos de disco suportados por provedor incluem AWS EBS GP2/IO1 SSD (EKS), Azure File/Azure Disk SSD com volumeBindingMode WaitForFirstConsumer (AKS), e GCP Standard/Balanced/SSD Persistent Disks (GKE); para o banco MSSQL em nuvem (Azure SQL ou Google Cloud SQL for SQL Server), define-se type=MSSQL no values?


---

### 159. `hwa-10.2.8-limitcpu-ready-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

limit cpu controla o número máximo de jobs executados simultaneamente em uma workstation; um job com dependências satisfeitas pode permanecer READY se o limite da workstation impedir a execução; uma workstation com limit cpu 0 bloqueia o início normal de jobs (apenas jobs hi/go executam).

> **ATENCAO / RESSALVAS DE USO:** Corroboração: awsrgresdef.html afirma 'If the limit CPU set on the workstation does not allow it to run at the moment, it waits in READY state.' Default: 1000 para cloud task launcher, 100 para demais tipos. Comando exige acesso limit.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | limit cpu=comando que define o limite de jobs simultâneos por workstation, READY=estado do job com dependências resolvidas aguardando liberação do limite, hi/go=prioridades que executam mesmo com limite zero |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_limitcpu.html |
| Titulo da fonte | limit cpu |
| Citacao de suporte | You can use the limit cpu command to set the number of jobs that can run simultaneously on a workstation. ... If you set the limit to zero, only the jobs with hi or go priority run on the workstation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | capacity_limit_cpu |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | limit |
| Familia | limitcpu-ready |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: limit cpu controla o número máximo de jobs executados simultaneamente em uma workstation; um job com dependências satisfeitas pode permanecer READY se o limite da workstation impedir a execução; uma workstation com limit cpu 0 bloqueia o início normal de jobs (apenas jobs hi/go executam)?


---

### 160. `hwa-10.2.8-message-bdd003e-0041`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, AWSBDD003E foi observada no lab durante a configuracao e validacao do arquivo BmEvents.conf (TWA_DATA_DIR=/opt/hwa/TWSDATA/BmEvents.conf) para reporte de eventos de agendamento. Parametros validados: OPTIONS=MASTER, LOGGING=ALL, SYMEVNTS=YES, CHSCHED=HIGH e lista EVENT=51 101 102... que sobrescreve completamente o default. A mensagem esta associada ao processamento de eventos do BmEvents durante o ciclo de deploy da configuracao.

> **ATENCAO / RESSALVAS DE USO:** Observado no lab 18/08 (bmevents-config). Cobre um codigo lab-observado sem claim dedicada (gap r9: 7 codigos so-no-lab).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmspar.html |
| Titulo da fonte | HCL Workload Automation messages - AWSBDD component |
| Citacao de suporte | AWSBDD003E observed during BmEvents.conf configuration in the lab |
| Coletado em | 2026-08-23 |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['configuracao de BmEvents.conf (OPTIONS/LOGGING/SYMEVNTS/CHSCHED/EVENT)'], result=AWSBDD003E observada durante validacao da configuracao BmEvents; parametros aceitos e configuracao aplicada., validated_at=2026-08-18T00:00:00BRT |
| Terminologia normalizada | message=AWSBDD003E, command=deploy |
| Status de revisao | lab_validated |
| Tipo | message |
| verbs | deploy |
| Codigo da mensagem | AWSBDD003E |
| Familia | message-bdd003e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBDD003E no HWA?
- Como solucionar ou diagnosticar o erro AWSBDD003E no HWA?
- Qual é o significado da mensagem de erro AWSBDD003E no HWA e qual ação é recomendada?


---

### 161. `hwa-10.2.8-message-catalog-sets-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, o catalogo oficial de Messages and Codes em common/src_ms/awsmspart1TWS.html lista apenas quatro conjuntos de mensagens para HWA Distributed: AWKZSJ, AWSWUI, AWSZAP e EEL. As familias AWSBJV, AWSJCL, AWSJOL, AWSJSC, AWSFSE, AWSBMA e AWSIHS nao possuem pagina oficial de mensagens no catalogo 10.2.8; os codigos AWSJPL/AWSJCL relevantes para troubleshooting aparecem nas paginas de troubleshooting (awstrmakeplan, awstrswitchplan), e AWSJCL/AWSJOM existem em versoes mais antigas (ex.: v95).

> **ATENCAO / RESSALVAS DE USO:** Evidencia negativa importante para evitar generalizar codigos de mensagens de versoes antigas (v95/9.x) como sendo de 10.2.8. Evita SFT fabricado sobre familias de mensagens que nao existem no catalogo 10.2.8. Somente leitura.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | catalog=Messages and Codes, version=10.2.8, documented_sets_distributed=['AWKZSJ', 'AWSWUI', 'AWSZAP', 'EEL'], undocumented_families=['AWSBJV', 'AWSJCL', 'AWSJOL', 'AWSJSC', 'AWSFSE', 'AWSBMA', 'AWSIHS'], note=AWSJCL/AWSJOM documented only in older versions (e.g. v95); AWSJPL/AWSJCL troubleshooting codes appear in troubleshooting pages |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmspart1TWS.html |
| Titulo da fonte | HCL Workload Automation messages (Messages and Codes) |
| Citacao de suporte | HCL Workload Automation messages |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| Familia | message-catalog |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, o catalogo oficial de Messages and Codes em common/src_ms/awsmspart1TWS?


---

### 162. `hwa-10.2.8-monitor-db-views-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

As views de banco de dados no HCL Workload Automation 10.2.8 são documentadas como conjunto de views predefinidas para extrair informações do banco de dados e definir relatórios com ferramentas como Crystal Reports ou Brio, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Página oficial awsdvtwsviews.html lista as views documentadas; páginas individuais descrevem cada view. Uso para relatórios.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=Database Views (views de banco de dados), termo_pt_br=views de banco de dados para relatórios |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvtwsviews.html |
| Titulo da fonte | HCL Workload Automation views |
| Citacao de suporte | This chapter describes the views you can use to extract information from the HCL Workload Automation database. You can then use reporting tools, such as Crystal Reports or Brio, to define reports based on this information. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-db |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: As views de banco de dados no HCL Workload Automation 10.2.8 são documentadas como conjunto de views predefinidas para extrair informações do banco de dados e definir relatórios com ferramentas como Crystal Reports ou Brio, conforme documentação oficial?


---

### 163. `hwa-10.2.8-monitor-dwc-reporting-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A seção Reporting do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentada para recuperar dados do banco de dados de workload e visualizar, imprimir e salvar resultados, usando relatórios predefinidos ou relatórios personalizados (BIRT), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado que relatórios predefinidos geram relatórios históricos em painel integrado; relatórios personalizados usam templates BIRT.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=Reporting do Dynamic Workload Console, termo_pt_br=relatórios predefinidos e personalizados (BIRT) do DWC |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/reports_r.html |
| Titulo da fonte | Reporting |
| Citacao de suporte | You can use HCL Workload Automation reports to retrieve data from the HCL Workload Automation database. You can then view, print, and save the results in different kinds of output. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| Familia | monitor-dwc |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A seção Reporting do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentada para recuperar dados do banco de dados de workload e visualizar, imprimir e salvar resultados, usando relatórios predefinidos ou relatórios personalizados (BIRT), conforme documentação oficial?


---

### 164. `hwa-10.2.8-monitor-job-history-v-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view JOB_HISTORY_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre o histórico de execução de jobs, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Job_name, Job_run_date_time, Job_status, Return_code, Total_elapsed_time, Total_cpu_time, Rerun_type, Rerun_number, User_login.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=JOB_HISTORY_V, termo_pt_br=visão JOB_HISTORY_V (histórico de jobs) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobhistory.html |
| Titulo da fonte | JOB_HISTORY_V |
| Citacao de suporte | The JOB_HISTORY_V view displays information about job history. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-job |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_HISTORY_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional JOB_HISTORY_V no banco de dados do HWA?


---

### 165. `hwa-10.2.8-monitor-job-statistics-v-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view JOB_STATISTICS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações de estatísticas sobre jobs, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** View de estatísticas de jobs; colunas como Successful_runs, Abended_runs, Late_start_runs, Total_reruns, Average_elapsed_time, Last_run_date.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=JOB_STATISTICS_V, termo_pt_br=visão JOB_STATISTICS_V (estatísticas de jobs) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobstatistics.html |
| Titulo da fonte | JOB_STATISTICS_V |
| Citacao de suporte | The JOB_STATISTICS_V view displays information about jobs. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-job |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?


---

### 166. `hwa-10.2.8-monitor-job-statistics-v-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view JOB_STATISTICS_V no HCL Workload Automation 10.2.8 é documentada com colunas de estatísticas de jobs como Successful_runs, Abended_runs, Late_start_runs, Late_end_runs, Total_reruns, Average_elapsed_time, Total_elapsed_time e Total_cpu_time, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** View de estatísticas de jobs com contadores documentados de execuções bem-sucedidas, abend, atrasos e tempos de CPU/elapsed.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=JOB_STATISTICS_V, termo_pt_br=colunas de estatísticas em JOB_STATISTICS_V |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobstatistics.html |
| Titulo da fonte | JOB_STATISTICS_V |
| Citacao de suporte | Successful_runs - The number of times the job ran successfully. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | monitor-job |


---

### 167. `hwa-10.2.8-monitor-plan-job-streams-v-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view PLAN_JOB_STREAMS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os job streams presentes no plano, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Job_stream_id, Job_stream_name, Scheduled_time, Status, Late, Monitored, Total_jobs, Abend_jobs, Executing_jobs, Failed_jobs, Successful_jobs.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PLAN_JOB_STREAMS_V, termo_pt_br=visão PLAN_JOB_STREAMS_V (job streams no plano) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvplanjobStreams.html |
| Titulo da fonte | PLAN_JOB_STREAMS_V |
| Citacao de suporte | The PLAN_JOB_STREAMS_V view displays information about job streams in the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | monitor-plan |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco PLAN_JOB_STREAMS_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional PLAN_JOB_STREAMS_V no banco de dados do HWA?


---

### 168. `hwa-10.2.8-monitor-plan-jobs-v-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view PLAN_JOBS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre os jobs presentes no plano corrente, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Job_id, Job_name, Job_stream_name, Scheduled_time, Actual_start, Actual_end, Deadline, Status, Return_code, Priority, Critical, Monitored, Promoted.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PLAN_JOBS_V, termo_pt_br=visão PLAN_JOBS_V (jobs no plano) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvplanjobs.html |
| Titulo da fonte | PLAN_JOBS_V |
| Citacao de suporte | The PLAN_JOBS_V view displays information about jobs in plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | monitor-plan |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco PLAN_JOBS_V no HCL Workload Automation?


---

### 169. `hwa-10.2.8-monitor-plan-workstations-v-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

A view PLAN_WORKSTATIONS_V no HCL Workload Automation 10.2.8 é documentada para exibir informações sobre as workstations presentes no plano, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Colunas documentadas incluem Workstation_id, Workstation_type, Workstation_name, Workstation_original_name, Link_status, Ssl_communication, Fence, Version, Node_name, Time_zone.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | view=PLAN_WORKSTATIONS_V, termo_pt_br=visão PLAN_WORKSTATIONS_V (workstations no plano) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvplanworkstations.html |
| Titulo da fonte | PLAN_WORKSTATIONS_V |
| Citacao de suporte | The PLAN_WORKSTATIONS_V view displays information about workstations in the plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | monitor-plan |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco PLAN_WORKSTATIONS_V no HCL Workload Automation?


---

### 170. `hwa-10.2.8-monitor-predefined-reports-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

Os relatórios predefinidos do Dynamic Workload Console no HCL Workload Automation 10.2.8 incluem os tipos Job Run Statistics, Job Run History, Workstation Workload Summary, Workstation Workload Runtimes, Plan Reports e Custom SQL Reports, gerados em Monitoring and Reporting, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Lista documentada: Job Run Statistics, Job Run History, Workstation Workload Summary, Workstation Workload Runtimes, Plan Reports, Custom SQL Reports.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=relatórios predefinidos (predefined reports), termo_pt_br=relatórios predefinidos do DWC |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/awsrgpredefinedreports.html |
| Titulo da fonte | Predefined Reports |
| Citacao de suporte | You can generate the following reports from the Dynamic Workload Console using the predefined reports in Monitoring and Reporting from the navigation toolbar in the Dynamic Workload Console. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan; run |
| Familia | monitor-predefined |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os relatórios predefinidos do Dynamic Workload Console no HCL Workload Automation 10.2.8 incluem os tipos Job Run Statistics, Job Run History, Workstation Workload Summary, Workstation Workload Runtimes, Plan Reports e Custom SQL Reports, gerados em Monitoring and Reporting, conforme documentação oficial?


---

### 171. `hwa-10.2.8-monitor-rep-commands-list-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

Os comandos de relatório documentados no HCL Workload Automation 10.2.8 são rep1, rep2, rep3, rep4a, rep4b, rep7, rep8, rep11, reptr e xref, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Tabela documentada: rep1 Job Details Listing, rep2 Prompt Listing, rep3 Calendar Listing, rep4a Parameter Listing, rep4b Resource Listing, rep7 Job History Listing, rep8 Job Histogram, rep11 Planned Production Schedule, reptr Planned/Actual Production (09A/B/D, 10A/B), xref Cross Reference Report.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=comandos de relatório, termo_pt_br=comandos de relatório (rep1..rep11, reptr, xref) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgrepcom.html |
| Titulo da fonte | Command descriptions - Getting reports and statistics |
| Citacao de suporte | HCL Workload Automation report commands are listed in List of report commands. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | monitor-rep |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os comandos de relatório documentados no HCL Workload Automation 10.2.8 são rep1, rep2, rep3, rep4a, rep4b, rep7, rep8, rep11, reptr e xref, conforme documentação oficial?


---

### 172. `hwa-10.2.8-monitor-rep7-report-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

O comando de relatório rep7 no HCL Workload Automation 10.2.8 é documentado como 'Report 07 - Job History Listing', permitindo gerar um relatório de histórico de jobs, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Mecanismo documentado para histórico de jobs via comando de relatório rep7, executado a partir do prompt do sistema no master domain manager.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | comando=rep7, termo_pt_br=comando de relatório rep7 (Job History Listing) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgrepcom.html |
| Titulo da fonte | Command descriptions - Getting reports and statistics |
| Citacao de suporte | rep7 - Report 07 - Job History Listing |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-rep7 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O comando de relatório rep7 no HCL Workload Automation 10.2.8 é documentado como 'Report 07 - Job History Listing', permitindo gerar um relatório de histórico de jobs, conforme documentação oficial?


---

### 173. `hwa-10.2.8-monitor-wappman-import-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

O utilitário wappman no HCL Workload Automation 10.2.8 é documentado para importar, substituir, excluir, exportar, exibir e listar workload applications, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** wappman é documentado para workload applications, não para relatórios. Comandos documentados: -import, -replace, -delete, -export, -display, -list, -u, -V. Nota: -import/-replace/-delete são mutantes/destrutivos; -list/-display/-export são somente leitura.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | utilitario=wappman, termo_pt_br=utilitário wappman (gerenciamento de workload applications) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldappcmd.html |
| Titulo da fonte | wappman command |
| Citacao de suporte | Imports, replaces, deletes, exports, displays and lists a workload application. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | import |
| Familia | monitor-wappman |

**Perguntas relacionadas:**

- Como utilizar o utilitário wappman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no wappman para gerenciar monitor?


---

### 174. `hwa-10.2.8-monitor-workload-dashboard-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

O Workload Dashboard do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentado como um recurso de monitoramento que permite monitorar o progresso do plano, aberto em Boards > Workload Dashboard, com widgets predefinidos, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Workload Dashboard fornece visão consolidada do status da carga de trabalho para uma ou mais engines configuradas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | recurso=Workload Dashboard, termo_pt_br=Workload Dashboard do DWC |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/dashboardtask.html |
| Titulo da fonte | Workload Dashboard |
| Citacao de suporte | To open the Workload Dashboard, in the navigation bar at the top, click Boards > Workload Dashboard. The panel opens showing a number of predefined widgets which return the results for the most widely-used queries. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | monitor-workload |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O Workload Dashboard do Dynamic Workload Console no HCL Workload Automation 10.2.8 é documentado como um recurso de monitoramento que permite monitorar o progresso do plano, aberto em Boards > Workload Dashboard, com widgets predefinidos, conforme documentação oficial?


---

### 175. `hwa-10.2.8-observability-splunk-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `splunk`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a Observability for Splunk esta disponivel para monitorar metricas, eventos, audit e infrastructure logs do HWA. Ela fornece 5 dashboards no Splunk Enterprise: (1) Jobs and Job Streams (status de jobs, critical jobs e job streams); (2) KPIs and Workstations (KPIs do HWA por engine com drill-down para series temporais graficas); (3) Activity Monitoring (audit de acoes de usuario); (4) Infra Monitoring (detalhes de infraestrutura do deployment em Kubernetes); (5) Alerts (alertas customizados para eventos do HWA, com alertas pre-definidos de exemplo). A integracao usa o readme file oficial para deploy e customizacao.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Observability for Splunk). Tambem disponivel Observability for Dynatrace (v1022+). [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1ObservabilityforSplunk.html |
| Titulo da fonte | HCL Workload Automation Observability for Splunk - HCL Workload Automation 10.2.8 |
| Citacao de suporte | HCL Workload Automation Observability for Splunk is available to monitor HCL Workload Automation metrics, events, audit and infrastructure logs. |
| Coletado em | 2026-08-25 |
| Capacidade | observability_splunk |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | command=deploy |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | k8s |
| verbs | deploy; status |
| Familia | observability-splunk |

**Perguntas relacionadas:**

- Como implantar componentes do HWA no Kubernetes ou OpenShift usando Helm charts?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a Observability for Splunk esta disponivel para monitorar metricas, eventos, audit e infrastructure logs do HWA?


---

### 176. `hwa-10.2.8-perf-engine-heap-sizing-0159`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `perfreport`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), o sizing do JVM heap do engine (WebSphere Application Server Liberty Base) e recomendado conforme o throughput de scheduling desejado (jobs/min): 1-50 jobs/min = 2 GB; 50-100 = 2.5 GB; 100-200 = 4 GB; acima de 200 = 6 GB. Alem do heap, considerar a memoria nativa do processo Java e dos processos do HWA: a RAM das maquinas onde o Liberty roda precisa ser entre 50% e 100% maior que o JVM max heap size. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.3 Memory).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (Tabela 3, pagina 21). Complementa hwa-10.2.8-incident-jcs011e-oom-0068 (aumentar heap do Liberty) com valores concretos de sizing.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - Memory |
| Citacao de suporte | Scheduling throughput (jobs/min): 1-50 = 2 GB; 50-100 = 2.5 GB; 100-200 = 4 GB; >200 = 6 GB. The RAM of the machines where the WebSphere Application Server Liberty is running needs to be between 50% and 100% larger than the JVM max heap size. |
| Coletado em | 2026-08-23 |
| Capacidade | perfreport_heap_sizing |
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
| Familia | perf-engine |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), o sizing do JVM heap do engine (WebSphere Application Server Liberty Base) e recomendado conforme o throughput de scheduling desejado (jobs/min): 1-50 jobs/min = 2 GB; 50-100 = 2.5 GB; 100-200 = 4 GB; acima de 200 = 6 GB?


---

### 177. `hwa-10.2.8-perf-oracle-autoextend-0161`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `perfreport`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), para bancos Oracle e recomendavel habilitar a propriedade Datafile AUTOEXTEND (ON) dos datafiles, considerando que os settings e workload descritos causaram ocupacao de tablespace de cerca de 50 GB ou mais. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.3 Oracle database configuration).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 22). Complementa hwa-10.2.8-incident-oracle-schema-config-0106.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - Oracle AUTOEXTEND |
| Citacao de suporte | It is advisable to enable the Datafile AUTOEXTEND property (ON), considering that the settings and workload described in this section caused a table space occupancy of about 50 GB or greater. |
| Coletado em | 2026-08-23 |
| Capacidade | perfreport_oracle_autoextend |
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
| Familia | perf-oracle |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), para bancos Oracle e recomendavel habilitar a propriedade Datafile AUTOEXTEND (ON) dos datafiles, considerando que os settings e workload descritos causaram ocupacao de tablespace de cerca de 50 GB ou mais?


---

### 178. `hwa-10.2.8-ports-https-port-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 utiliza a porta 9443 como HTTPS_PORT padrão e a porta 9444 como HTTP_PORT, além das portas de bootstrap 12809 e 19402.

> **ATENCAO / RESSALVAS DE USO:** Tópico de leitura (portas). Verificado na página oficial 10.2.8. Confirma a porta HTTPS 9443 do DWC.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | component=Dynamic Workload Console (DWC), https_port=9443, http_port=9444, bootstrap_ports=12809; 19402 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadenablingports.html |
| Titulo da fonte | Enabling Ports |
| Citacao de suporte | Dynamic Workload Console - 9444 - HTTP_PORT; 9443 - HTTPS_PORT; 12809 - bootstrap port; 19402 - bootstrap security port |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | component |
| Ferramenta | dwc |
| Componente | Dynamic Workload Console (DWC) |
| Familia | ports-https |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 utiliza a porta 9443 como HTTPS_PORT padrão e a porta 9444 como HTTP_PORT, além das portas de bootstrap 12809 e 19402.?


---

### 179. `hwa-10.2.8-rbac-role-based-security-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 implementa um modelo de segurança baseado em papéis (role-based security model) que controla as permissões de acesso dos usuários aos objetos e às operações de agendamento.

> **ATENCAO / RESSALVAS DE USO:** Tópico de leitura/segurança. Verificado na página oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | security_model=role-based security model, object=user access permissions on scheduling objects |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadrolebasedsecuritymanagement.html |
| Titulo da fonte | Role-based security model |
| Citacao de suporte | Role-based security model |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | rbac-role |


---

### 180. `hwa-10.2.8-runbook-cancel-job-0010`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando cancel job (cj) cancela um job: se cancelado antes de ser lançado, o job não é lançado; se cancelado depois de lançado, ele continua executando; e se um job em execução é cancelado e completa em estado ABEND, nenhuma tentativa automática de recuperação é feita para relançar o job.

> **ATENCAO / RESSALVAS DE USO:** Cancelling a job is destructive (cancels launch/recovery). Official page documents the recovery-suppression caveat.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=cancel job, abbreviation=cj, effect=cancels a job, caveat=no automatic recovery if abend after cancel |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_cancel_job.html |
| Titulo da fonte | cancel job |
| Citacao de suporte | If you cancel a job before it is launched, the job is not launched. When you cancel a job after it is launched, it continues to run. If you cancel a job that is running and it completes in the ABEND state, no automatic job recovery steps are attempted to relaunch the job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | cancel_job |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | cancel |
| object_hint | job |
| Familia | runbook-cancel |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel job (cj) cancela um job: se cancelado antes de ser lançado, o job não é lançado; se cancelado depois de lançado, ele continua executando; e se um job em execução é cancelado e completa em estado ABEND, nenhuma tentativa automática de recuperação é feita para relançar o job?


---

### 181. `hwa-10.2.8-runbook-cancel-job-0011`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando cancel job (cj) com a opção ;pend adia o cancelamento até que todas as dependências associadas sejam resolvidas, e enquanto o cancelamento está postergado, a notação 'Cancel Pend' aparece na coluna Dependencies na exibição showjobs.

> **ATENCAO / RESSALVAS DE USO:** pend defers destructive cancellation; documented behavior.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=cancel job, option=pend, effect=deferred cancellation until dependencies resolved |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_cancel_job.html |
| Titulo da fonte | cancel job |
| Citacao de suporte | pend added Not started The job is not cancelled until all the associated dependencies are resolved. ... While the cancel action is postponed, the notation Cancel Pend is listed in the Dependencies column of the job in a showjobs display. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | show |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | cancel; showjobs |
| object_hint | job |
| Familia | runbook-cancel |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando cancel job (cj) com a opção ;pend adia o cancelamento até que todas as dependências associadas sejam resolvidas, e enquanto o cancelamento está postergado, a notação 'Cancel Pend' aparece na coluna Dependencies na exibição showjobs?


---

### 182. `hwa-10.2.8-runbook-database-view-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V exibe informações sobre jobs e registra métricas de execução de job em milissegundos, incluindo Average_elapsed_time (tempo médio de execução), Total_elapsed_time (soma do tempo de CPU e tempo de espera), Last_elapsed_time, Max_elapsed_time e Min_elapsed_time.

> **ATENCAO / RESSALVAS DE USO:** JOB_STATISTICS_V is a read-only DB view for job execution statistics; records elapsed/cpu time in ms.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | database_view=JOB_STATISTICS_V, columns=['Average_elapsed_time', 'Total_elapsed_time', 'Last_elapsed_time', 'Max_elapsed_time', 'Min_elapsed_time'], unit=milliseconds |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobstatistics.html |
| Titulo da fonte | JOB_STATISTICS_V |
| Citacao de suporte | Average_elapsed_time The average time the job took to run. This time is expressed in milliseconds. ... Total_elapsed_time The sum of the times the job used the CPU and the time the job waited for other processes to release the CPU for all its runs. This time is expressed in milliseconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | db_views_job_statistics |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | runbook-database |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?
- Qual é a estrutura e utilidade da view relacional JOB_STATISTICS_V no banco de dados do HWA?


---

### 183. `hwa-10.2.8-runbook-database-view-0033`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a view JOB_STATISTICS_V também registra contadores de execução de job, incluindo Successful_runs (número de execuções bem-sucedidas), Abended_runs (número de execuções anormais), Total_reruns (número total de reruns), Suppressed_runs, Late_start_runs e Late_end_runs.

> **ATENCAO / RESSALVAS DE USO:** JOB_STATISTICS_V is a read-only DB view with run count columns for consumption/usage reporting.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | database_view=JOB_STATISTICS_V, columns=['Successful_runs', 'Abended_runs', 'Total_reruns', 'Suppressed_runs', 'Late_start_runs', 'Late_end_runs'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_db/awsdvjobstatistics.html |
| Titulo da fonte | JOB_STATISTICS_V |
| Citacao de suporte | Successful_runs The number of times the job ran successfully. ... Abended_runs The number of times the job ended abnormally. ... Total_reruns The total number of times the job reran. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | db_views_job_statistics |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | runbook-database |

**Perguntas relacionadas:**

- Qual é o propósito da view de banco JOB_STATISTICS_V no HCL Workload Automation?


---

### 184. `hwa-10.2.8-runbook-rerun-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção rerun ;from=[[folder/]wkstat#]job permite especificar uma definição de job no banco de dados cujo arquivo/comando será executado no lugar do job selecionado, e permite rerun de jobs em estado SUPPR desde que não pertençam a job streams cancelados ou suprimidos.

> **ATENCAO / RESSALVAS DE USO:** from option is mutually exclusive with streamlogon/logon and docommand/script; requires submitdb access in conman. Rerun via from is a job relaunch (mutating).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rerun, option=from, scope=alternate job definition |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgrerun.html |
| Titulo da fonte | rerun (conman) |
| Citacao de suporte | from=[folder/]wkstat#job Specifies the name of a job defined in the database whose job file or command will be run in place of the job specified by jobselect. You can rerun jobs also in the SUPPR state, as long as they do not belong to job streams that are in the cancelled or suppressed state. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | rerun_job |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| verbs | rerun |
| Familia | runbook-rerun |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção rerun ;from=[[folder/]wkstat#]job permite especificar uma definição de job no banco de dados cujo arquivo/comando será executado no lugar do job selecionado, e permite rerun de jobs em estado SUPPR desde que não pertençam a job streams cancelados ou suprimidos?


---

### 185. `hwa-10.2.8-runbook-showjobs-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção ;props do comando showjobs (sj) exibe detalhes de uma instância de job, incluindo Status, Internal Status, Return Code, Not Satisfied Dependencies, Rerun Options e, na seção Recovery Information, os campos Action e Message — usados para diagnosticar o motivo de um ABEND.

> **ATENCAO / RESSALVAS DE USO:** showjobs ;props is the documented way to inspect recovery action/message and return code after a job ABENDs (read-only).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, option=props, fields=['Status', 'Internal Status', 'Return Code', 'Not Satisfied Dependencies', 'Rerun Options', 'Action', 'Message'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs (conman) |
| Citacao de suporte | props Displays the following information about the specified job instance ... Runtime Information - Status - Internal Status - Not Satisfied Dependencies - Return Code ... Recovery Information - Action - Message ... |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| verbs | rerun; showjobs; status |
| Familia | runbook-showjobs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;props do comando showjobs (sj) exibe detalhes de uma instância de job, incluindo Status, Internal Status, Return Code, Not Satisfied Dependencies, Rerun Options e, na seção Recovery Information, os campos Action e Message — usados para diagnosticar o motivo de um ABEND?


---

### 186. `hwa-10.2.8-runbook-showjobs-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção ;stdlist do comando showjobs (sj) exibe o log da saída do job (standard list files), incluindo no trailer informações como Exit Status, Elapsed Time, Job CPU usage e Job Memory usage — usada para localizar o log de saída após um ABEND.

> **ATENCAO / RESSALVAS DE USO:** showjobs ;stdlist retrieves the job log/output; documented as read-only. Archived jobs are not retrievable via stdlist.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, option=stdlist, fields=['Exit Status', 'Elapsed Time', 'Job CPU usage', 'Job Memory usage'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs (conman) |
| Citacao de suporte | To display the log from the standard list files for the job ... Exit Status Is the status of the job when it completed. ... Elapsed Time Is the elapsed time for the job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| verbs | list; showjobs; status |
| Familia | runbook-showjobs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;stdlist do comando showjobs (sj) exibe o log da saída do job (standard list files), incluindo no trailer informações como Exit Status, Elapsed Time, Job CPU usage e Job Memory usage — usada para localizar o log de saída após um ABEND?


---

### 187. `hwa-10.2.8-runbook-showjobs-0035`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção ;keys retcod do comando showjobs (sj) exibe o return code do job, e a opção ;props exibe na seção Runtime Information os campos Return Code e Return Code Mapping Expression, permitindo identificar o código de retorno de um job que terminou em ABEND.

> **ATENCAO / RESSALVAS DE USO:** Read-only diagnostics for return code inspection after ABEND.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, options=['keys retcod', 'props'], fields=['Return Code', 'Return Code Mapping Expression'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs (conman) |
| Citacao de suporte | retcod Displays the return code for the job. This argument must be used in conjunction with the keys argument, for example: %sj @; keys retcod ... props ... Return Code ... Return Code Mapping Expression |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| verbs | showjobs |
| Familia | runbook-showjobs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção ;keys retcod do comando showjobs (sj) exibe o return code do job, e a opção ;props exibe na seção Runtime Information os campos Return Code e Return Code Mapping Expression, permitindo identificar o código de retorno de um job que terminou em ABEND?


---

### 188. `hwa-10.2.8-sap-r3batch-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `password`

**Afirmacao / Conteudo:**

Não cole nem peça senhas reais. No HCL Workload Automation Distributed 10.2.8, o access method r3batch conecta o produto a sistemas SAP R/3 e as senhas de usuário SAP podem ser criptografadas com o utilitário enigma (em TWA_home/methods) antes de gravar nos arquivos r3batch.opts, gerando valores {aes}.... Execute isso no ambiente aprovado, nunca aqui na conversa.

> **ATENCAO / RESSALVAS DE USO:** Portuguese duplicate of hwa-10.2.8-enigma-0001; same evidence: enigma (awsausappswdencr.html), {aes} format (awsausapoptfileex.html), r3batch/SAP R/3 (awsausapaccessmethod.html). Never request or paste real SAP passwords in conversations. | SAP options file stores the enigma-encrypted {aes} password value (quote truncated before the secret).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/apps/src_usr/awsausappswdencr.html |
| Titulo da fonte | Encrypting SAP user passwords |
| Citacao de suporte | If you modify the file with a text editor, run the enigma program to encrypt the password before writing it in the file ... The program returns an encrypted version that you can then enter in the options file. |
| Coletado em | 2026-08-18 |
| Capacidade | password_encryption |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Claim sensível de segurança/credenciais - não validável no lab por design (política: não manipular credenciais reais) |
| Terminologia normalizada | topic=sap |
| Status de revisao | verified |
| Tipo | other |
| Familia | sap-r3batch |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Não cole nem peça senhas reais?


---

### 189. `hwa-10.2.8-sec-access-auditing-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

The official HCL Workload Automation 10.2.8 documentation does not document an access audit trail that identifies who/when for access attempts or a documented review flow. The security file documents permissions but not audit trails.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia de auditoria de acesso com identificacao de quem/quando.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | access_auditing=auditoria de acesso, audit_trail=trilha de auditoria, review_workflow=fluxo de revisão |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadusrauthorization.html |
| Titulo da fonte | User authorization - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The security file defines access permissions for each user or group; audit logging is not documented in this section. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-access |


---

### 190. `hwa-10.2.8-sec-awsjco084-e-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando UpdateStats executado em um plano grande falha com a mensagem AWSJCO084E ('The user UNAUTHENTICATED is not authorized to work with the planner process') quando o tempo de execução do job excede duas horas, pois esse é o timeout padrão das credenciais de usuário do WebSphere Application Server; a correção documentada é aumentar o atributo expiration do LTPA.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awstrmst.pdf p.71 (LACUNA4 2026-08-23); mensagem AWSJCO084E documentada para UpdateStats em plano grande.

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
| Capacidade | auth |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Citacao de suporte | This error occurs because the large number of jobs in the plan has caused the job run time to exceed two hours, which is the default timeout for the user credentials of the WebSphere Application Server. |
| Terminologia normalizada | message=AWSJCO084E, scope=UpdateStats em plano grande, purpose=documentar causa de timeout de credenciais do WebSphere Application Server |
| Responsavel | hwa-security-lifecycle-verifier |
| Tipo | message |
| Ferramenta | planner |
| Codigo da mensagem | AWSJCO084E |
| Familia | sec-awsjco084 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO084 no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO084 no HWA?
- Qual é o significado da mensagem de erro AWSJCO084E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?


---

### 191. `hwa-10.2.8-sec-config-dropins-0031`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o atributo expiration da configuração LTPA (Lightweight Third Party Authentication) do WebSphere Application Server Liberty Base é editado no arquivo de configuração localizado em configDropins/defaults do engineServer, é expresso em minutos e tem valor padrão de 24 horas; após editar, o arquivo deve ser copiado para a pasta overrides do engineServer.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awstrmst.pdf p.71 (LACUNA4 2026-08-23); caminho base TWA_home/usr/servers/engineServer/configDropins/defaults; sem valores sensíveis (keysPassword não incluído).

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
| Capacidade | auth |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Citacao de suporte | Edit the expiration attribute for LTPA as necessary. The attribute is expressed in minutes and the default value is 24 hours. |
| Terminologia normalizada | option=expiration (LTPA), scope=WebSphere Application Server Liberty Base engineServer, purpose=definir timeout da sessão de autenticação LTPA |
| Responsavel | hwa-security-lifecycle-verifier |
| Tipo | other |
| Familia | sec-config |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o atributo expiration da configuração LTPA (Lightweight Third Party Authentication) do WebSphere Application Server Liberty Base é editado no arquivo de configuração localizado em configDropins/defaults do engineServer, é expresso em minutos e tem valor padrão de 24 horas; após editar, o arquivo deve ser copiado para a pasta overrides do engineServer?


---

### 192. `hwa-10.2.8-sec-job-logon-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `password`

**Afirmacao / Conteudo:**

The exact encryption algorithm applied to job logon/streamlogon passwords stored in user objects is not explicitly documented in HCL Workload Automation 10.2.8. The documentation describes the storage in user objects and centralized management but does not specify the internal cryptographic algorithm.

> **ATENCAO / RESSALVAS DE USO:** revalidacao pendente: sem 2a fonte oficial encontrada (2026-08-23); manter em backlog de revalidacao

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | streamlogon=logon de job stream, job_logon=logon de job, user_object=objeto de usuário |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgusingstreamlogon.html |
| Titulo da fonte | Using STREAMLOGON - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The user name and password are stored in the user object... managed centrally. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | password |
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
| Ferramenta | joblog |
| Familia | sec-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: The exact encryption algorithm applied to job logon/streamlogon passwords stored in user objects is not explicitly documented in HCL Workload Automation 10.2.8. The documentation describes the storage in user objects and centralized management but does not specify the internal cryptographic algorithm?


---

### 193. `hwa-10.2.8-sec-object-type-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

A definição de security role no HCL Workload Automation 10.2.8 usa a sintaxe 'securityrole nome ... object_type access=acao[,acao]...' para conceder, de forma granular por tipo de objeto, as ações que usuários ou grupos podem executar (ex.: userobj access=modify ou altpass, schedule access=add,delete,display...).

> **ATENCAO / RESSALVAS DE USO:** Documentado para conceder privilégio mínimo por tipo de objeto; capacidade do produto, não política de hardening.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | security_role=função de segurança, securityrole=palavra-chave de definição de função, object_type=tipo de objeto, access=permissão/lista de ações |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsecurityroledefn.html |
| Titulo da fonte | Security role definition |
| Citacao de suporte | Syntax securityrole security_role_name [description "description"] object_type access[=action[,action]...] end |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | add; delete; display; modify |
| Familia | sec-object |


---

### 194. `hwa-10.2.8-sec-password-vault-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `password`

**Afirmacao / Conteudo:**

O recurso de password vaults no HCL Workload Automation 10.2.8 permite recuperar senhas de cofres de senhas (como CyberArk) definindo parâmetros na definição do job, usando a sintaxe ${vault:vault_wks#vault-profile-name:query-for-username} na seção <jsdl:password> do job, sem armazenar a senha em texto plano na definição.

> **ATENCAO / RESSALVAS DE USO:** Documentado: integração de cofre de senhas (CyberArk) configurada via definição de job; agente dinâmico especificado interage com o cofre e retorna a senha para executar o job. | Examples page shows ${vault:...} syntax inside <jsdl:password>; quote verbatim including the source typo 'tom'.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | password_vault=cofre de senhas, job_definition=definição de job, vault_wks=workstation que interage com o cofre, vault-profile-name=nome do perfil do cofre, query-for-username=consulta de usuário |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgpwdvault.html |
| Titulo da fonte | Obtaining passwords from password vaults |
| Citacao de suporte | Define parameters in the job definition to retrieve passwords from password vaults. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | password |
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
| Familia | sec-password |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: O recurso de password vaults no HCL Workload Automation 10.2.8 permite recuperar senhas de cofres de senhas (como CyberArk) definindo parâmetros na definição do job, usando a sintaxe ${vault:vault_wks#vault-profile-name:query-for-username} na seção <jsdl:password> do job, sem armazenar a senha em texto plano na definição?


---

### 195. `hwa-10.2.8-sec-remote-trace-certs-0030`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

O procedimento documentado no HCL Workload Automation 10.2.8 para coletar traces de um agente remoto com certificados de segurança customizados consiste em extrair o certificado do keystore do agente remoto, importá-lo em um keystore local (cujo nome deve ser TWSClientKeyStore.kdb) e criar um arquivo .ini com tcp_port=0, a porta do agente remoto em ssl_port e o caminho do keystore local em key_repository_path.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awstrmst.pdf p.36 (LACUNA4 2026-08-23); keystore ad hoc local com nome obrigatório TWSClientKeyStore.kdb; sem valores reais de credenciais.

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
| Capacidade | cert |
| Modo de operacao | guided_action |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Citacao de suporte | If you are collecting the traces for a remote agent for which you customized the security certificates, you must import the certificate on the local agent and specify the name of the .ini file that contains this configuration. |
| Terminologia normalizada | key=tcp_port / ssl_port / key_repository_path, scope=arquivo .ini de coleta de traces do agente, purpose=coletar traces de agente remoto com certificados customizados |
| Responsavel | hwa-security-lifecycle-verifier |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Comportamento documentado em fonte oficial; sem prova de laboratório nesta fase (LACUNA4) — validação prática requer ambiente ativo com REST API/configuração disponível. |
| Tipo | other |
| verbs | import |
| Familia | sec-remote |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O procedimento documentado no HCL Workload Automation 10.2.8 para coletar traces de um agente remoto com certificados de segurança customizados consiste em extrair o certificado do keystore do agente remoto, importá-lo em um keystore local (cujo nome deve ser TWSClientKeyStore?


---

### 196. `hwa-10.2.8-sec-retry-bind-0029`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para evitar o bloqueio de conta LDAP após uma tentativa de autenticação errada quando um hostname LDAP é mapeado para múltiplos endereços IP, o WebSphere Application Server disponibiliza as propriedades customizadas com.ibm.websphere.security.ldap.retryBind (default true; se false, o servidor não repete chamadas de bind LDAP) e com.ibm.websphere.security.registry.ldap.singleLDAP (default false; se true, o hostname não é resolvido para múltiplos IPs), configuradas em Security > User Registries > LDAP > Custom Properties.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awstrmst.pdf p.123 (LACUNA4 2026-08-23); APAR WebSphere PK42672; complementa a causa documentada de bloqueio de conta LDAP.

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
| Capacidade | auth |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Citacao de suporte | in the administration console click Security > User Registries > LDAP > Custom Properties and set to true the property com.ibm.websphere.security.ldap.retryBind. If this property is set to false, the Application Server does not retry LDAP bind calls. The default value is true. |
| Terminologia normalizada | option=com.ibm.websphere.security.ldap.retryBind + com.ibm.websphere.security.registry.ldap.singleLDAP, scope=WebSphere Application Server LDAP Custom Properties, purpose=prevenir bloqueio de conta LDAP por múltiplas tentativas de bind |
| Responsavel | hwa-security-lifecycle-verifier |
| Tipo | other |
| Familia | sec-retry |


---

### 197. `hwa-10.2.8-sec-ssl-auth-mode-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

A opção 'SSL auth mode' no HCL Workload Automation 10.2.8 controla o comportamento durante o handshake SSL com os valores caonly, string ou cpu, que definem como a validade do certificado do par e a emissão por uma CA reconhecida são verificadas (e opcionalmente a correspondência do CN).

> **ATENCAO / RESSALVAS DE USO:** Documentado em localopts.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SSL_auth_mode=modo de autenticação SSL, caonly=apenas CA, string=string, cpu=nome da workstation, CN=Common Name |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | The behavior of HCL Workload Automation during an SSL handshake is based on the value of the SSL authentication mode option |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção 'SSL auth mode' no HCL Workload Automation 10.2.8 controla o comportamento durante o handshake SSL com os valores caonly, string ou cpu, que definem como a validade do certificado do par e a emissão por uma CA reconhecida são verificadas (e opcionalmente a correspondência do CN)?


---

### 198. `hwa-10.2.8-sec-ssl-cipher-suites-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `tls`

**Afirmacao / Conteudo:**

A opção 'SSL cipher suites' (e 'CLI SSL cipher suites') no HCL Workload Automation 10.2.8 especifica algoritmos suportados apenas para o TLS versão 1.3 e não se aplica ao TLS versão 1.2 ou anterior.

> **ATENCAO / RESSALVAS DE USO:** Documentado na referência de localopts.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SSL_cipher_suites=suites de cipher SSL, TLS_1.3=Transport Layer Security versão 1.3 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | Specify one or more supported algorithms for TLS version 1.3, This option does not apply to TLS version 1.2 or earlier. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | tls |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção 'SSL cipher suites' (e 'CLI SSL cipher suites') no HCL Workload Automation 10.2.8 especifica algoritmos suportados apenas para o TLS versão 1.3 e não se aplica ao TLS versão 1.2 ou anterior?


---

### 199. `hwa-10.2.8-sec-ssl-ciphers-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `ssl`

**Afirmacao / Conteudo:**

A keyword ssl_ciphers no HCL Workload Automation 10.2.8 define os ciphers que a workstation suporta durante uma conexão SSL; para usar uma classe de cipher OpenSSL, usa-se o comando openssl ciphers para listar as classes disponíveis.

> **ATENCAO / RESSALVAS DE USO:** A opção 'SSL ciphers' também documentada em localopts.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ssl_ciphers=keyword ssl ciphers, cipher=algoritmo de cifra, OpenSSL=biblioteca OpenSSL, cipher_class=classe de cipher |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | Define the ciphers that the workstation supports during an SSL connection. If you want to use an OpenSSL cipher class, use the following command to find out the list of available classes: openssl ciphers |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | ssl |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A keyword ssl_ciphers no HCL Workload Automation 10.2.8 define os ciphers que a workstation suporta durante uma conexão SSL; para usar uma classe de cipher OpenSSL, usa-se o comando openssl ciphers para listar as classes disponíveis?


---

### 200. `hwa-10.2.8-sec-ssl-config-xml-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

Para configurar o TLS em componentes Open Liberty do HCL Workload Automation 10.2.8, copia-se o arquivo ssl_config.xml da pasta configDropins/defaults para a pasta overrides dos servidores engineServer e dwcServer e define-se o atributo sslProtocol, por exemplo sslProtocol="TLSv1.3" (só 1.3) ou sslProtocol="TLSv1.2,TLSv1.3" sem espaços antes ou depois da vírgula.

> **ATENCAO / RESSALVAS DE USO:** Documentado: requer reinício do Open Liberty após a modificação.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ssl_config.xml=arquivo de configuração SSL, engineServer=servidor do motor, dwcServer=servidor do Dynamic Workload Console, sslProtocol=atributo do protocolo SSL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | sslProtocol="TLSv1.2,TLSv1.3" No spaces can be used before or after the comma. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| verbs | open |
| Familia | sec-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Para configurar o TLS em componentes Open Liberty do HCL Workload Automation 10.2.8, copia-se o arquivo ssl_config?


---

### 201. `hwa-10.2.8-sec-sso-key-share-0033`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, para usar Single Sign-On entre o Dynamic Workload Console e o engine, é necessário compartilhar corretamente as LTPA_keys conforme o capítulo de configuração SSL da Administration Guide; o compartilhamento também é exigido quando ocorrem os erros AWSUI0766E e AWSUI0833E, que surgem quando os valores de realm são iguais para mais de um WebSphere Application Server (DWC, conector z/OS ou engine), por exemplo quando todas as instâncias usam o mesmo LDAP user registry ou estão instaladas na mesma máquina.

> **ATENCAO / RESSALVAS DE USO:** Extraída de awstrmst.pdf p.120 (LACUNA4 2026-08-23); erros AWSUI0766E/AWSUI0833E e colisão de realm documentados na mesma passagem.

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
| Capacidade | auth |
| Modo de operacao | read |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide Version 10.2.8 |
| Citacao de suporte | If you set up to use Single Sign-On between the Dynamic Workload Console and the HCL Workload Automation engine, make sure you correctly shared the LTPA_keys as described in the chapter on configuring SSL in the Administration Guide. |
| Terminologia normalizada | key=LTPA_keys, scope=Single Sign-On entre Dynamic Workload Console e engine, purpose=autenticação conjunta (SSO) |
| Responsavel | hwa-security-lifecycle-verifier |
| Tipo | other |
| Ferramenta | dwc |
| Familia | sec-sso |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSUI0833E no HWA?
- Como solucionar ou diagnosticar o erro AWSUI0833E no HWA?
- Qual é o significado da mensagem de erro AWSUI0766E no HWA?
- Como solucionar ou diagnosticar o erro AWSUI0766E no HWA?


---

### 202. `hwa-10.2.8-sec-tls-1-3-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

A configuração do protocolo TLS V1.3 no HCL Workload Automation 10.2.8 só pode ser definida usando certificados personalizados com chaves RSA de pelo menos 2K, sendo recomendado usar um certificado de comprimento 4K.

> **ATENCAO / RESSALVAS DE USO:** Documentado requisito mínimo de tamanho de chave para TLS 1.3.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TLS_1.3=Transport Layer Security versão 1.3, RSA_key=chave RSA, certificate=certificado |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | The configuration of the TLS V1.3 security protocol can only be set using custom certificates with RSA keys of at least 2K. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-tls |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A configuração do protocolo TLS V1.3 no HCL Workload Automation 10.2.8 só pode ser definida usando certificados personalizados com chaves RSA de pelo menos 2K, sendo recomendado usar um certificado de comprimento 4K?


---

### 203. `hwa-10.2.8-sec-tls-crt-0027`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

O comando certman verify no HCL Workload Automation 10.2.8 valida certificados usando a sintaxe 'certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <working directory>]', verificando a senha da chave, a senha do stash (tls.sth), a data de expiração, o tamanho da chave, o formato .pem, a correspondência entre chave privada e pública e a adequação do tls.crt para conexões client e server.

> **ATENCAO / RESSALVAS DE USO:** Documentado; -inpath contém tls.crt, tls.key, tls.sth e ca.crt. Senha não incluída no registro.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | certman=utilitário Certman, verify=verificar, tls.crt=certificado TLS, tls.key=chave privada, tls.sth=arquivo stash, minkeysize=tamanho mínimo da chave |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman_ver.html |
| Titulo da fonte | Verify the validity of certificates |
| Citacao de suporte | certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <working directory>] |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | cert |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['certman verify'], result=Sintaxe real confirmada no help do binário: 'certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <work dir>]'. Execução real: 'certman verify -inpath /opt/hwa/TWSDATA/ssl/depot -keypasswd dummy -workdir /tmp' -> WACERT009I verificou ca.crt e tls.crt; WACERT021I 'The certificate chain is valid' para o CA; WACERT030E quando a senha do stash (tls.sth) não confere com a chave privada - comportamento real de validação de senha., validated_at=2026-08-23T00:50:00BRT, evidence_file=lab-validation-2026-08-23-r8-certman.jsonl |
| Tipo | command |
| Ferramenta | certman |
| verbs | verify |
| Familia | sec-tls |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O comando certman verify no HCL Workload Automation 10.2.8 valida certificados usando a sintaxe 'certman verify -inpath <input path> -keypasswd <key pwd> [-minkeysize <minimum key size>] [-workdir <working directory>]', verificando a senha da chave, a senha do stash (tls?


---

### 204. `hwa-10.2.8-sec-user-definition-0008`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 o comando altpass, usado para alterar a senha de um usuário (credencial de logon), exige a definição de usuário no formato workstation#username, podendo-se omitir o nome da workstation somente ao alterar a senha da workstation a partir da qual o comando é executado.

> **ATENCAO / RESSALVAS DE USO:** Documentado comportamento de alteração de senha de logon; sem valores de senha no registro.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | altpass=comando altpass (alterar senha), user_definition=definição de usuário, password=senha |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgusingstreamlogon.html |
| Titulo da fonte | Using the HCL Workload Automation user and streamlogon definitions |
| Citacao de suporte | when you use the altpass command, you must use the user definition in the format workstation#username |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | log |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | sec-user |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 o comando altpass, usado para alterar a senha de um usuário (credencial de logon), exige a definição de usuário no formato workstation#username, podendo-se omitir o nome da workstation somente ao alterar a senha da workstation a partir da qual o comando é executado?


---

### 205. `hwa-10.2.8-sec-user-object-credential-management-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `credential`

**Afirmacao / Conteudo:**

O User Object Credential Management do HCL Workload Automation 10.2.8 permite atualizar de forma centralizada e segura as senhas armazenadas dentro de user objects, aplicando a mudança de forma consistente tanto na instância de banco de dados quanto nas instâncias de plano ativas.

> **ATENCAO / RESSALVAS DE USO:** Documentado como melhoria da 10.2.5 mantida na 10.2.8; senhas de jobs ficam armazenadas nos user objects e são gerenciadas centralmente. | 10.2.5 changed-features page repeats the same capability statement verbatim.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | User_Object_Credential_Management=gerenciamento de credenciais de user objects, user_object=objeto de usuário, credential=credencial |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1userobjcred.html |
| Titulo da fonte | User Object Credential Management - Ensuring operational continuity and security |
| Citacao de suporte | The User Object Credential Management enables you to securely update the passwords stored within user objects directly from a central point of control. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | credential |
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
| Familia | sec-user |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O User Object Credential Management do HCL Workload Automation 10.2.8 permite atualizar de forma centralizada e segura as senhas armazenadas dentro de user objects, aplicando a mudança de forma consistente tanto na instância de banco de dados quanto nas instâncias de plano ativas?


---

### 206. `hwa-10.2.8-sec-variable-table-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `security`

**Afirmacao / Conteudo:**

There is no documented "secure variable" feature, confidentiality flag per variable, or per-variable encryption mechanism in HCL Workload Automation 10.2.8 Distributed. Variable tables should not be treated as secure secret stores.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia de mecanismo de "secure variable" documentado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | secure_variable=variável segura, variable_table=tabela de variáveis, encryption_at_rest=criptografia em repouso |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtsecurity.html |
| Titulo da fonte | Variable table security - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Variable tables are not encrypted; access control is based on the security file permissions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | variable_table_security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-variable |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: There is no documented "secure variable" feature, confidentiality flag per variable, or per-variable encryption mechanism in HCL Workload Automation 10.2.8 Distributed?


---

### 207. `hwa-10.2.8-sec-variable-table-0026`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 é necessário ter permissão 'use' para referenciar uma variable table a partir de outros objetos (job streams, run cycles e workstations), conforme definido no security file.

> **ATENCAO / RESSALVAS DE USO:** Requisito de permissão documentado.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | use=usar/referenciar, variable_table=tabela de variáveis, security_file=arquivo de segurança |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtsecurity.html |
| Titulo da fonte | Variable table security |
| Citacao de suporte | You need use access to be able to reference a variable table from other objects (job streams, run cycles and workstations). |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | run |
| Familia | sec-variable |


---

### 208. `hwa-10.2.8-sec-vartable-permissions-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 o mapeamento de permissões de variable tables para variáveis internas é documentado: acesso 'modify' à tabela permite adicionar, deletar e modificar variáveis; 'display' permite exibir; 'unlock' permite desbloquear; e o acesso 'use' é necessário para referenciar a tabela a partir de job streams, run cycles e workstations.

> **ATENCAO / RESSALVAS DE USO:** Documentado na tabela de relacionamento entre variable tables e variáveis contidas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | modify=modificar, display=exibir, unlock=desbloquear, use=usar/referenciar, variable=variável |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtsecurity.html |
| Titulo da fonte | Variable table security |
| Citacao de suporte | You need use access to be able to reference a variable table from other objects (job streams, run cycles and workstations). |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | variable_table_security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | display; modify; run |
| Familia | sec-vartable |


---

### 209. `hwa-10.2.8-security-ldap-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `ldap`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, e possivel configurar um user registry LDAP ou federated repository para o Dynamic Workload Console e demais componentes: o administrador adiciona o provider LDAP no template de configuracao de autenticacao, habilita o LDAP registry na seguranca do servidor de aplicacao (WebSphere Liberty) e aponta para o diretorio, depois mapeia os grupos/roles via Manage Roles no DWC. A troca de basicRegistry por LDAP permite SSO e centralizacao de usuarios.

> **ATENCAO / RESSALVAS DE USO:** Fonte oficial 10.2.8 (Configuring a user registry) + technote HCL (SSO Authentication using LDAP, OIDC and SAML). [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicfgLDAP.html |
| Titulo da fonte | Configuring a user registry - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Configure a federated repository or LDAP user registry and map roles via Manage Roles in the Dynamic Workload Console. Enable LDAP registry in the app server security config and grant roles to groups/users via the Manage Roles page. |
| Coletado em | 2026-08-25 |
| Capacidade | security_user_registry |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=security |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | security-ldap |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, e possivel configurar um user registry LDAP ou federated repository para o Dynamic Workload Console e demais componentes: o administrador adiciona o provider LDAP no template de configuracao de autenticacao, habilita o LDAP registry na seguranca do servidor de aplicacao (WebSphere Liberty) e aponta para o diretorio, depois mapeia os grupos/roles via Manage Roles no DWC?


---

### 210. `hwa-10.2.8-security-sso-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `sso`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Single Sign-On (SSO) pode ser configurado usando LDAP, OIDC ou SAML: para OIDC, configura-se o provedor de identidade (IdP, ex.: Okta ou Keycloak), define-se a URL de redirect/callback para o DWC/MDM, e garante-se que os componentes baseados em WebSphere compartilhem as mesmas chaves de token; reiniciar os servicos apos as mudancas.

> **ATENCAO / RESSALVAS DE USO:** Technote HCL/IBM (SSO using LDAP/OIDC/SAML). Complementa a claim hwa-10.2.8-security-ldap-0001. [Fonte oficial HCL 10.2.8]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/single-sign-sso-authentication-configuration-using-ldap-oidc-and-saml |
| Titulo da fonte | Single Sign-On (SSO) Authentication Configuration using LDAP, OIDC and SAML - IBM/HCL |
| Citacao de suporte | For SSO/OIDC, configure the IdP (e.g., Okta/Keycloak), set the redirect/callback URL to the DWC/MDM, and ensure the WebSphere-based components share the same token keys. Restart services after changes. |
| Coletado em | 2026-08-25 |
| Capacidade | security_sso |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=security |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | security-sso |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Single Sign-On (SSO) pode ser configurado usando LDAP, OIDC ou SAML: para OIDC, configura-se o provedor de identidade (IdP, ex?


---

### 211. `hwa-10.2.8-securityfile-security-file-auth-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

A autorização de usuários no HCL Workload Automation 10.2.8 é configurada por meio do arquivo de segurança (Security file), que define os usuários e suas permissões de acesso ao master domain manager.

> **ATENCAO / RESSALVAS DE USO:** Tópico sensível a credenciais (definição de usuários/permissões). Verificado na página oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | security_file=Security file, object=user authorization and access permissions |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadusrauthorization.html |
| Titulo da fonte | Configuring user authorization (Security file) |
| Citacao de suporte | Configuring user authorization (Security file) |
| Coletado em | 2026-08-16 |
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
| Tipo | other |
| Familia | securityfile-security |


---

### 212. `hwa-10.2.8-sfinal-change-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

In HCL Workload Automation 10.2.8, customized FINAL and FINALPOSTREPORTS definitions must be merged with the current Sfinal definitions and applied without discarding existing customizations; after updating the definitions, old instances may need to be canceled and new instances submitted according to the documented procedure.

> **ATENCAO / RESSALVAS DE USO:** Changing local FINAL definitions is an operational change; validate in a lab and approve before applying to an active plan.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiparallelupgradefrom95FINALjs.html |
| Titulo da fonte | Customizing and submitting the optional FINAL job stream |
| Citacao de suporte | Merge the job streams with file Sfinal so the new definitions have the same customization plus the new required attributes... delete current final job stream instances and submit the new instances. |
| Coletado em | 2026-08-21 |


---

### 213. `hwa-10.2.8-sfinal-role-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

In HCL Workload Automation 10.2.8 Distributed, the optional Sfinal file supplies FINAL and FINALPOSTREPORTS job streams for automating production plan processing; FINAL runs the sequence corresponding to JnextPlan and FINALPOSTREPORTS follows successful SWITCHPLAN and includes CHECKSYNC for plan synchronization.

> **ATENCAO / RESSALVAS DE USO:** Official documentation supports the role and ordering, not the local Sfinal2 variant as a universal requirement.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINAL job stream runs the sequence of script files described in JnextPlan... FINALPOSTREPORTS ... starts only when the last job listed in FINAL (SWITCHPLAN) has completed successfully... includes CHECKSYNC. |
| Coletado em | 2026-08-21 |


---

### 214. `hwa-10.2.8-showcpus-default-scope-0035`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, showcpus/sc sem domínio ou workstation mostra workstations do domínio local e, em domain manager, também domain managers conectados. Context: displays all the workstations that are in the domain of the workstation where the command was run, plus all the connected domain managers if the workstation is a domain manager.

> **ATENCAO / RESSALVAS DE USO:** Applies to the default scope of sc/showcpus with no domain and no workstation specified. Scope caveat: the doc also shows that conman "sc @" lists only the workstations of the local domain, without the connected domain managers. Read-only diagnostic command.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowcpus.html |
| Titulo da fonte | showcpus |
| Citacao de suporte | displays all the workstations that are in the domain of the workstation where the command was run, plus all the connected domain managers if the workstation is a domain manager. |
| Coletado em | 2026-08-18 |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showcpus |
| Status de revisao | verified |
| Tipo | other |
| verbs | run; showcpus |
| Familia | showcpus-default |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, showcpus/sc sem domínio ou workstation mostra workstations do domínio local e, em domain manager, também domain managers conectados?


---

### 215. `hwa-10.2.8-showfiles-states-0037`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, showfiles/sf usa yes, no, ? e vazio para indicar respectivamente arquivo disponível, ausente/indisponível, disponibilidade em verificação e ainda não verificado ou já consumido. Context: yes File exists and is available. no File is unavailable, or does not exist. ? Availability is being checked.

> **ATENCAO / RESSALVAS DE USO:** The empty (blank) state is documented as <blank>, matching the 'já consumido / ainda não verificado' reading of the claim. States apply to the state argument of showfiles/sf. Read-only diagnostic command.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowfiles.html |
| Titulo da fonte | showfiles |
| Citacao de suporte | yes File exists and is available. no File is unavailable, or does not exist. ? Availability is being checked. <blank> The file has not yet been checked, or the file was available and used to satisfy a job or job stream dependency. |
| Coletado em | 2026-08-18 |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showfiles |
| Status de revisao | verified |
| Tipo | other |
| Familia | showfiles-states |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, showfiles/sf usa yes, no, ? e vazio para indicar respectivamente arquivo disponível, ausente/indisponível, disponibilidade em verificação e ainda não verificado ou já consumido?


---

### 216. `hwa-10.2.8-showjobs-wildcard-all-jobs-0110`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, o padrao `@#@.@` no comando showjobs (sj) filtra todos os jobs em todos os job streams definidos na pasta raiz (/), onde @ substitui um ou mais caracteres alfanumericos, # e o separador workstation, e o ponto (.) separa job stream de job. O padrao `/@/@#/@/@.@` filtra todos os jobs em job streams definidos em todas as pastas. Exemplo: `sj @#@.@;keys` (HCL oficial Wildcards: '@#@.@ Filters on all jobs in job streams defined in the root (/) folder').

> **ATENCAO / RESSALVAS DE USO:** Corroborated by official HCL 10.2.8 Wildcards page. The pattern '@#@.@' was absent from the corpus before this addition (0 occurrences). Lab validated 2026-08-22 via SSH as wauser on MDM lab.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | showjobs=comando conman showjobs (sj), wildcard @=substitui um ou mais caracteres alfanumericos, @#@.@=todos os jobs em job streams da pasta raiz, workstation #=separador entre workstation e objeto de scheduling |
| Status do conhecimento | verified |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwildcards.html |
| Titulo da fonte | Wildcards - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | @#@.@ - Filters on all jobs in job streams defined in the root (/) folder. @#/@/@.@ - Filters all jobs in job streams defined in all folders. @ - Replaces one or more alphanumeric characters. |
| Coletado em | 2026-08-22 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, tested_commands=['sj @#@.@;keys', 'sj MDMDA#@.@;keys'], result=sj @#@.@;keys listou jobs de MDMDA e MDMXA (STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, etc.); sj MDMDA#@.@;keys listou todos jobs da MDMDA (ADHOC_*, CPLX_EVERY, FAIL_*, PRIO_*, EVTJOB* etc.) |
| Classificacao de risco | read_only |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Status de revisao | lab_validated |
| Tipo | other |
| verbs | showjobs |
| Familia | showjobs-wildcard |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o padrao `@#@?


---

### 217. `hwa-10.2.8-showschedules-rerun-total-0036`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, a lista de showschedules/ss não inclui jobs reexecutados em processos anteriores, mas o total ao final os inclui. Context: The list displayed in the output of the command does not include jobs that were rerun in previous scheduling processes, but the total shown at the end does.

> **ATENCAO / RESSALVAS DE USO:** The supporting sentence is on the showschedules reference page (Results section), not on awsrgrerun.html as the inferred_url suggested. The v1028 syntax block uses the alias showscheds/ss. Read-only diagnostic command.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowschedules.html |
| Titulo da fonte | showschedules |
| Citacao de suporte | The list displayed in the output of the command does not include jobs that were rerun in previous scheduling processes, but the total shown at the end does. |
| Coletado em | 2026-08-18 |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=rerun |
| Status de revisao | verified |
| Tipo | command |
| verbs | list; rerun; showschedules |
| Familia | showschedules-rerun |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, a lista de showschedules/ss não inclui jobs reexecutados em processos anteriores, mas o total ao final os inclui?


---

### 218. `hwa-10.2.8-srv-traces-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `trace`

**Afirmacao / Conteudo:**

No HCL Workload Automation Distributed 10.2.8, os traces do application server (Liberty) para os processos principais usam tws_info por padrão; o nível é alterado editando trace.xml e copiando de configDropins/templates para configDropins/overrides.

> **ATENCAO / RESSALVAS DE USO:** Tracing server confirmado em 10.2.8; alteração de trace é mutativa e requer janela de manutenção. [texto recuperado do unified dataset rag_corpus (verified_claim original)]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrchtraceprops.html |
| Titulo da fonte | Setting the traces on the application server for the major HCL Workload Automation processes |
| Citacao de suporte | The trace for these communications is set to tws_info by default ... To modify the trace level on the WebSphere Application Server Liberty Base, edit the trace.xml file as necessary. |
| Coletado em | 2026-08-16 |
| Capacidade | trace |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=srv |
| Status de revisao | verified |
| Tipo | other |
| Familia | srv-traces |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation Distributed 10.2.8, os traces do application server (Liberty) para os processos principais usam tws_info por padrão; o nível é alterado editando trace?


---

### 219. `hwa-10.2.8-startmon-event-monitoring-engine-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

O comando startmon inicia o processo monman, que ativa o mecanismo de monitoramento de eventos em uma workstation; o monman é iniciado automaticamente na próxima ativação do plano de produção quando a opção autostart monman = yes (padrão).

> **ATENCAO / RESSALVAS DE USO:** startmon é uma ação mutating (inicia processo). A parte de auto-início do monman é confirmada pela página Localopts details: 'autostart monman = yes|no ... Restarts the monitoring engine automatically when the next production plan is activated (on Windows also when HCL Workload Automation is restarted). The default is Yes.' Requer permissão de start em objetos cpu no arquivo de segurança.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | startmon=startmon, stopmon=stopmon, monman=monman, event_monitoring_engine=mecanismo de monitoramento de eventos, autostart monman=autostart monman, production_plan=plano de produção |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstartmon.html |
| Titulo da fonte | startmon |
| Citacao de suporte | Starts the monman process that turns on the event monitoring engine on the workstation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | monitor |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | startmon-event |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O comando startmon inicia o processo monman, que ativa o mecanismo de monitoramento de eventos em uma workstation; o monman é iniciado automaticamente na próxima ativação do plano de produção quando a opção autostart monman = yes (padrão)?


---

### 220. `hwa-10.2.8-stdlist-stdlist-stdout-stderr-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `stdlist`

**Afirmacao / Conteudo:**

Em HWA 10.2.8, um stdlist contém as saídas stdout e stderr do job. Context: A standard list file contains: ... The stdout output of the job. ... The stderr output of the job.

> **ATENCAO / RESSALVAS DE USO:** The claim isolates the stdout/stderr items of a four-item list; the full list also includes header/trailer banners and echoed commands. Scope: Windows and UNIX agents (jobmon/jobman). Read-only diagnostic context.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstdlistformat5.html |
| Titulo da fonte | Stdlist format |
| Citacao de suporte | A standard list file contains: Header and trailer banners. Echoed commands. The stdout output of the job. The stderr output of the job. |
| Coletado em | 2026-08-18 |
| Capacidade | stdlist |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=stdlist |
| Status de revisao | verified |
| Tipo | other |
| verbs | list |
| Familia | stdlist-stdlist |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, um stdlist contém as saídas stdout e stderr do job?


---

### 221. `hwa-10.2.8-submit-docommand-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation Distributed 10.2.8, submit docommand (sbd) submete um comando de sistema para ser executado como job. O comando deve estar entre aspas, requer acesso submit no security file e, se into não for usado, o job entra no job stream JOBS.

> **ATENCAO / RESSALVAS DE USO:** Inferred URL awsrgshowprompts.html was wrong; correct page is awsrgsubmitdocommand.html. Short form sbd confirmed on the Conman commands list page. Command limited to 255 characters; submitting from non-master workstations requires useropts connection credentials to the master domain manager (credential-related note, no credentials disclosed).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitdocommand.html |
| Titulo da fonte | submit docommand |
| Citacao de suporte | Submits a command to be launched as a job. ... The entire command must be enclosed in quotes ("). ... To run this command, in the security file you must have submit access for the job ... If into is not used, the job is added to a job stream named JOBS. |
| Coletado em | 2026-08-18 |
| Capacidade | security |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=submit |
| Status de revisao | verified |
| Tipo | command |
| verbs | submit |
| Familia | submit-docommand |


---

### 222. `hwa-10.2.8-tls-custom-certificates-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

A documentação do HWA 10.2.8 (página "Configuring the TLS V1.3 security protocol") descreve a configuração do protocolo TLS V1.3 e afirma que ele só pode ser configurado usando certificados customizados com chaves RSA de no mínimo 2K, recomendando o uso de um certificado de 4K; o suporte a TLS V1.3 está disponível a partir do HCL Workload Automation 10.1 FP4.

> **ATENCAO / RESSALVAS DE USO:** Confirmado com duas fontes oficiais HCL. A página v1028 (awspiTLSV13.html) foi aberta e lida e declara textualmente que a configuração do TLS V1.3 só pode ser feita com certificados customizados com chaves RSA de no mínimo 2K, recomendando 4K. A página correspondente na documentação v10.1 (mesmo título, mesmo caminho src_pi/awspiTLSV13.html) contém texto idêntico e corrobora o requisito de chave RSA de no mínimo 2K. Requisito exato documentado preservado (RSA de no mínimo 2K).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tls_1_3=TLS V1.3 security protocol, custom_certificates=custom certificates, rsa_key_minimum=RSA keys of at least 2K (2048 bits), recommended_key=4k-length certificate, availability=HCL Workload Automation version 10.1 FP4 onwards |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | The configuration of the TLS V1.3 security protocol can only be set using custom certificates with RSA keys of at least 2K. ... If you want to configure your environment with the TLS V1.3 protocol, it is recommended to use a 4k-length certificate. Note: TLS V1.3 security protocol support is available from HCL Workload Automation version 10.1 FP4 onwards. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | cert |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | tls-custom |


---

### 223. `hwa-10.2.8-trouble-awsjco084e-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

TROUBLESHOOTING: no HCL Workload Automation 10.2.8, o comando UpdateStats em um plano grande falha com AWSJCO084E 'The user UNAUTHENTICATED is not authorized to work with the planner process' quando o tempo de execucao do job ultrapassa duas horas; a causa documentada e o grande numero de jobs do plano fazendo o tempo de execucao exceder o timeout padrao de duas horas das credenciais do usuario do WebSphere Application Server; a recuperacao documentada e aumentar o timeout das credenciais do WAS para dar mais tempo ao UpdateStats.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: AWSJCO084E em UpdateStats de plano grande. Causa: timeout de 2h das credenciais WAS excedido. Recuperacao: aumentar o timeout das credenciais WAS. Diagnostico; nao modifica plano.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSJCO084E, component=planner / UpdateStats, symptom=UpdateStats falha com UNAUTHENTICATED, cause=tempo de execucao > 2h (timeout padrao das credenciais do WAS), recovery=aumentar o timeout das credenciais do WebSphere Application Server |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; planner/UpdateStats |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation troubleshooting guide - UpdateStats fails |
| Citacao de suporte | This error occurs because the large number of jobs in the plan has caused the job run time to exceed two hours, which is the default timeout for the user credentials of the WebSphere Application Server. To increase the timeout so that the UpdateStats command has more time to run, perform the following steps |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Capacidade | auth |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; planner/UpdateStats |
| Tipo | message |
| Ferramenta | planner |
| Codigo da mensagem | AWSJCO084E |
| Componente | planner / UpdateStats |
| Familia | trouble-awsjco084e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO084E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO084E no HWA?


---

### 224. `hwa-10.2.8-trouble-awsmsp104e-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a acao de envio automatico de e-mail de uma event rule falha com AWSMSP104E 'The mail <mailID> has not been successfully delivered to <recipient>', com a causa documentada: o dominio do servidor SMTP nao esta definido na opcao global de remetente de e-mail mailSenderName (ms); a recuperacao e definir o dominio do SMTP na opcao global mailSenderName (ms).

> **ATENCAO / RESSALVAS DE USO:** Sintoma: AWSMSP104E ao disparar evento com acao de e-mail. Causa documentada: dominio do SMTP ausente na opcao mailSenderName (ms). Recuperacao documentada: preencher o dominio do servidor SMTP na opcao global. Diagnostico; nao expoe credenciais.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSMSP104E, component=event manager / event rules (acao de e-mail), symptom=acao de envio de email falha, cause=dominio do SMTP nao definido em mailSenderName (ms), recovery=definir o dominio do servidor SMTP na opcao global mailSenderName (ms) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; event rules |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation troubleshooting guide - mail send action fails |
| Citacao de suporte | The mail send action failed because the domain name of the SMTP server was not defined in the mail sender name global option: mailSenderName (ms). |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; event rules |
| Tipo | message |
| Codigo da mensagem | AWSMSP104E |
| Componente | event manager / event rules (acao de e-mail) |
| Familia | trouble-awsmsp104e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSMSP104E no HWA?
- Como solucionar ou diagnosticar o erro AWSMSP104E no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 225. `hwa-10.2.8-tune-jm-promoted-nice-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

A opção jm promoted nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 atribui o valor de prioridade a um job crítico que precisa ser promovido no workload service assurance, com padrão documentado de -1; a promoção é efetiva apenas com valores negativos.

> **ATENCAO / RESSALVAS DE USO:** Somente UNIX/Linux; combina com jm nice somando valores.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm promoted nice=jm promoted nice, workload service assurance=workload service assurance, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm promoted nice = nice_value - Used in workload service assurance. ... assigns the priority value to a critical job that needs to be promoted so that the operating system processes it before others. ... The default is -1. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_jm_promoted_nice |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm promoted nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 atribui o valor de prioridade a um job crítico que precisa ser promovido no workload service assurance, com padrão documentado de -1; a promoção é efetiva apenas com valores negativos?


---

### 226. `hwa-10.2.8-tune-jm-promoted-priority-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

A opção jm promoted priority, para sistemas Windows, no localopts do HCL Workload Automation 10.2.8 define a prioridade pela qual o sistema operacional processa um job crítico quando é promovido, com padrão documentado de AboveNormal.

> **ATENCAO / RESSALVAS DE USO:** Somente Windows.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm promoted priority=jm promoted priority, workload service assurance=workload service assurance, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm promoted priority = value - Used in workload service assurance. For Windows operating systems only ... The possible values are: High, AboveNormal (the default), Normal, BelowNormal, Low or Idle. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_jm_promoted_priority |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm promoted priority, para sistemas Windows, no localopts do HCL Workload Automation 10.2.8 define a prioridade pela qual o sistema operacional processa um job crítico quando é promovido, com padrão documentado de AboveNormal?


---

### 227. `hwa-10.2.8-tune-jvm-options-0044`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `dwc_api` / `dwc`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 documenta o aumento do heap do Java da Dynamic Workload Console editando o arquivo jvm.options do dwcServer do WebSphere Application Server Liberty, com exemplo de -Xms4096m -Xmx4096m e, em caso de alta carga (mais de 50 usuários concorrentes), 6144 como heap size e 1536 como nursery mem size; a RAM deve ser aproximadamente o dobro do heap.

> **ATENCAO / RESSALVAS DE USO:** Arquivo editado: DWC_DATA_dir/usr/servers/dwcServer/configDropins/overrides/jvm.options; requer parar/iniciar o Liberty.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Dynamic Workload Console=Dynamic Workload Console, Liberty=WebSphere Application Server Liberty, jvm.options=jvm.options, -Xmx=-Xmx, -Xms=-Xms |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/DWC-awsadincreaseheap.html |
| Titulo da fonte | Dynamic Workload Console - Increasing application server heap size |
| Citacao de suporte | Here is an example: -Xms4096m, -Xmx4096m ... Note: In case of high workload (more than 50 concurrent users) use 6144 as heap size and 1536 as nursery mem size. The above suggested settings must be applied when the RAM configuration value twice the value of the heap size. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | dwc |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| Familia | tune-jvm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 documenta o aumento do heap do Java da Dynamic Workload Console editando o arquivo jvm?


---

### 228. `hwa-10.2.8-tune-limit-cpu-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o limite (Limit) definido na definição de workstation, por exemplo com o comando limit cpu, estabelece o número máximo de jobs que o HCL Workload Automation pode lançar e manter em execução concorrentemente naquela workstation.

> **ATENCAO / RESSALVAS DE USO:** O limite pode ser definido na definição de job stream (job limit) ou na definição de workstation (limit cpu).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Limit=Limit, limit cpu=limit cpu, workstation=workstation |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsettinglimits.html |
| Titulo da fonte | Setting limits |
| Citacao de suporte | Setting the limit on a workstation to 25, for example, allows HCL Workload Automation to have no more than 25 jobs running concurrently on that workstation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | capacity_limit_cpu |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | limit |
| Familia | tune-limit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o limite (Limit) definido na definição de workstation, por exemplo com o comando limit cpu, estabelece o número máximo de jobs que o HCL Workload Automation pode lançar e manter em execução concorrentemente naquela workstation?


---

### 229. `hwa-10.2.8-tune-mm-cache-size-0029`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

A opção mm cache size no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de mensagens em cache, quando mm cache mailbox está habilitado; segundo a referência de detalhes de localopts, o valor máximo (padrão) documentado é 512.

> **ATENCAO / RESSALVAS DE USO:** Conflito com a página Mailbox caching, que declara padrão de 32 mensagens e máximo de 512; ver claim hwa-10.2.8-tune-0030.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm cache size=mm cache size, Mailman=Mailman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm cache size = messages - Specify this option if you also use mm cache mailbox. The maximum value (default) is 512. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_mm_cache_size |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm cache size no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de mensagens em cache, quando mm cache mailbox está habilitado; segundo a referência de detalhes de localopts, o valor máximo (padrão) documentado é 512.?


---

### 230. `hwa-10.2.8-tune-mm-cache-size-0030`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

Segundo a página Mailbox caching do HCL Workload Automation 10.2.8, o valor padrão do parâmetro mm cache size é de 32 mensagens e o máximo é 512, aplicável quando mm cache mailbox está habilitado.

> **ATENCAO / RESSALVAS DE USO:** Conflito preservado: a página Localopts details declara valor máximo (padrão) de 512. Valores maiores aumentam desempenho mas degradam a recuperação após falha e aumentam o uso de memória.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm cache size=mm cache size, Mailman=Mailman, mm cache mailbox=mm cache mailbox |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadmailboxcache.html |
| Titulo da fonte | Mailbox caching - advantages and disadvantages |
| Citacao de suporte | The default value for this parameter is 32 messages, and the maximum is 512. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_mm_cache_size |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Segundo a página Mailbox caching do HCL Workload Automation 10.2.8, o valor padrão do parâmetro mm cache size é de 32 mensagens e o máximo é 512, aplicável quando mm cache mailbox está habilitado?


---

### 231. `hwa-10.2.8-tune-mm-resolve-0035`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

A opção mm resolve master no localopts do HCL Workload Automation 10.2.8 controla se a variável $MASTER é resolvida no início do dia de produção; desde a versão 9.5 Fix Pack 2 o padrão documentado é no.

> **ATENCAO / RESSALVAS DE USO:** Deve-se manter o mesmo valor em master domain manager e backup domain manager.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm resolve master=mm resolve master, Mailman=Mailman, $MASTER=$MASTER, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm resolve master = yes|no - When set to yes the $MASTER variable is resolved at the beginning of the production day. ... Starting from Version 9.5 Fix Pack 2, the default is no. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_mm_resolve_master |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm resolve master no localopts do HCL Workload Automation 10.2.8 controla se a variável $MASTER é resolvida no início do dia de produção; desde a versão 9.5 Fix Pack 2 o padrão documentado é no?


---

### 232. `hwa-10.2.8-tune-mo-sleep-0040`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `localopts`

**Afirmacao / Conteudo:**

There is no "mo sleep" or event processor loop interval tuning option documented in the HCL Workload Automation 10.2.8 localopts reference. The documented event-related options are management options (can be event processor, autostart monman), not performance tuning.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mo sleep=mo sleep, event processor=event processor, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Local options reference - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The localopts parameters related to event management are: autostart monman, can be event processor. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | localopts_event_processor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mo |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: There is no "mo sleep" or event processor loop interval tuning option documented in the HCL Workload Automation 10.2.8 localopts reference?


---

### 233. `hwa-10.2.8-tune-pln-buffpool-0043`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 documenta que, para planos com mais de 200.000 jobs, deve-se aumentar o número de páginas (NPAGES) do buffer pool TWS_PLN_BUFFPOOL para 182000 e do TWS_BUFFPOOL para 50000 usando o comando ALTER BUFFERPOOL.

> **ATENCAO / RESSALVAS DE USO:** Aplicável quando o plano Symphony é replicado no banco de dados em ambientes com mais de 200.000 jobs.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TWS_PLN_BUFFPOOL=TWS_PLN_BUFFPOOL, TWS_BUFFPOOL=TWS_BUFFPOOL, NPAGES=NPAGES, ALTER BUFFERPOOL=ALTER BUFFERPOOL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtunedbconfigparams.html |
| Titulo da fonte | Optimizing the replication of the Symphony file in the database |
| Citacao de suporte | increase the number of pages (NPAGES) of the TWS_PLN_BUFFPOOL parameter to 182000 and the TWS_BUFFPOOL parameter to 50000 by using the ALTER BUFFERPOOL command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | database_tuning |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-pln |


---

### 234. `hwa-10.2.8-tune-tuning-the-database-0041`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `database`

**Afirmacao / Conteudo:**

O tópico Tuning the database do HCL Workload Automation 10.2.8 declara que o tuning do banco de dados requer etapas específicas que variam conforme o banco de dados e que informações detalhadas devem ser consultadas na documentação relevante do produto de banco de dados; não fornece recomendações quantitativas próprias nesta página.

> **ATENCAO / RESSALVAS DE USO:** As recomendações quantitativas de DB2 constam na subpágina Optimizing the replication of the Symphony file in the database (ver hwa-10.2.8-tune-0042 e 0043).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Tuning the database=Tuning the database, DB2=DB2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtunedb.html |
| Titulo da fonte | Tuning the database |
| Citacao de suporte | Tuning the database requires specific steps which vary depending on the database. To find detailed and specific information consult the relevant product documentation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | database_tuning |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-tuning |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O tópico Tuning the database do HCL Workload Automation 10.2.8 declara que o tuning do banco de dados requer etapas específicas que variam conforme o banco de dados e que informações detalhadas devem ser consultadas na documentação relevante do produto de banco de dados; não fornece recomendações quantitativas próprias nesta página?


---

### 235. `hwa-10.2.8-variable-plan-generation-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a sintaxe ^variablename^ é resolvida quando o plano é gerado ou estendido, enquanto a sintaxe ${variablename} é resolvida no momento da submissão (run time); a sintaxe ${variablename} não é suportada ao submeter um job stream pelo Self-Service Catalog.

> **ATENCAO / RESSALVAS DE USO:** Para ${variablename} ser resolvido na submissão, uma opção no job definition que indica resolver variáveis no run time deve ser especificada. No Self-Service Catalog, variáveis devem ser especificadas no formato ^variablename^.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ^variablename^=sintaxe com acento circunflexo, ${variablename}=sintaxe com chaves, plan generation=geração do plano, plan extension=extensão do plano, submission time=momento da submissão, Self-Service Catalog=Catálogo de Autoatendimento |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgparmdefn.html |
| Titulo da fonte | Variable and parameter definition |
| Citacao de suporte | Specify the variable in this format if you want it resolved when the plan is generated or extended. ... Specify the variable in this format if you want it resolved or overwritten when the job or job stream is submitted to be run. ... When submitting a job stream from the Self-Service Catalog that contains variables or that has a variable table associated to it, variables specified in this format, ${variablename}, are not supported. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan; run |
| Familia | variable-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a sintaxe ^variablename^ é resolvida quando o plano é gerado ou estendido, enquanto a sintaxe ${variablename} é resolvida no momento da submissão (run time); a sintaxe ${variablename} não é suportada ao submeter um job stream pelo Self-Service Catalog?


---

### 236. `hwa-10.2.8-vm-0006-contrast-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-vm-0006 (enRoleBasedSecurityFileCreation): na 9.5 o default da opcao rs era no (seguranca classica), enquanto na 10.2.8 o default e yes (seguranca baseada em papeis); SFT e procedimentos de seguranca devem declarar a versao e o default correto, pois o modelo de seguranca padrao muda na fronteira 9.5/10.2.x.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: default no (9.5) vs yes (10.2.8).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | HCL Workload Automation global options |
| Citacao de suporte | enRoleBasedSecurityFileCreation | rs ... The default value is yes, which means that the role-based security model is enabled. |
| Coletado em | 2026-08-21 |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=vm |
| Status de revisao | reviewed |


---

### 237. `hwa-10.2.8-vm-9f-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `syntax`

**Afirmacao / Conteudo:**

O bloco JOIN (join <name> <n|ALL> of description "..." ... endjoin, com follows <pred> if <cond>) é suportado na definição de job stream do HCL Workload Automation Distributed tanto na 10.2.0 quanto na 10.2.8, com sintaxe e semântica idênticas.

> **ATENCAO / RESSALVAS DE USO:** JOIN presente e idêntico em 10.2.0 e 10.2.8. Células 10.1/9.5: insufficient_evidence.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | join=bloco de junção de dependências condicionais em job stream, endjoin=fim do bloco join, follows=dependência de precedência |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcondepsjoin_intro.html |
| Titulo da fonte | Join (HCL Workload Automation 10.2.8) |
| Citacao de suporte | join <name> <n|ALL> of description "..." ... endjoin |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | join_syntax |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | vm-9f |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O bloco JOIN (join <name> <n|ALL> of description "?


---

### 238. `hwa-10.2.8-vm-9f-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

A palavra-chave onoverlap (parallel|enqueue|donotstart) é suportada na definição de job stream do HCL Workload Automation Distributed 10.2.0 e 10.2.8, com os três valores idênticos. PORÉM, o limite de 39 dependências manuais com enqueue e a mensagem AWSJOM138E são documentados apenas na 10.2.8 (introduzidos na 10.2.7, fix KB0128221); a página 10.2.0 não menciona esse limite.

> **ATENCAO / RESSALVAS DE USO:** Os três valores onoverlap são estáveis 10.2.0-10.2.8. O limite de 39 e AWSJOM138E são version_dependent (10.2.7+).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | onoverlap=palavra-chave de comportamento de sobreposição de instâncias, parallel=iniciar instância mesmo com a anterior em execução, enqueue=aguardar a instância anterior terminar, donotstart=não iniciar a nova instância, enqueue_39_limit=limite de 39 dependências manuais com enqueue (10.2.7+), AWSJOM138E=mensagem de erro do limite de 39 |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | version_dependent |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgonoverlap.html |
| Titulo da fonte | onoverlap (10.2.8) |
| Citacao de suporte | onoverlap parallel|enqueue|donotstart ... AWSJOM138E ... 39 |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM138E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM138E no HWA?


---

### 239. `hwa-10.2.8-vm-9f-0008-contrast-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `incidents` / `aws`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-vm-9f-0008 (onoverlap + limite 39 deps): a keyword onoverlap (parallel|enqueue|donotstart) e suportada em 10.2.0 e 10.2.8, mas o limite de 39 dependencias manuais com enqueue e a mensagem AWSJOM138E sao documentados apenas a partir da 10.2.7 (fix KB0128221); na 10.2.0 a pagina nao menciona o limite; portanto, o limite nao deve ser generalizado para 10.2.0.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: limite documentado so na 10.2.7+; 10.2.0 sem limite documentado.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.7; 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgonoverlap.html |
| Titulo da fonte | HCL Workload Automation onoverlap keyword |
| Citacao de suporte | AWSJOM138E ... 39 |
| Coletado em | 2026-08-21 |
| Capacidade | aws |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.7; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSJOM138E |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM138E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM138E no HWA?


---

### 240. `hwa-10.2.8-vm-en-retain-name-on-rerun-from-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `globalopts`

**Afirmacao / Conteudo:**

Na versão 10.2.8 do HCL Workload Automation, enRetainNameOnRerunFrom permanece deprecated (desde 10.1), com valor padrão no, fazendo com que jobs reexecutados recebam o nome do rerun from em vez do nome original; a documentação não informa uma opção substituta.

> **ATENCAO / RESSALVAS DE USO:** Nenhuma opção substituta documentada; o comportamento efetivo é atribuir o nome do rerun from aos jobs reexecutados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enRetainNameOnRerunFrom=opção global descontinuada de retenção de nome em rerun, rerun=comando conman de reexecução |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description (HCL Workload Automation 10.2.8) |
| Citacao de suporte | Note: Starting from version 10.1, this option is deprecated and must not be modified. By default, its value is set to no. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | globalopts_retain_name_rerun |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | rerun |
| Familia | vm-en |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na versão 10.2.8 do HCL Workload Automation, enRetainNameOnRerunFrom permanece deprecated (desde 10.1), com valor padrão no, fazendo com que jobs reexecutados recebam o nome do rerun from em vez do nome original; a documentação não informa uma opção substituta?


---

### 241. `hwa-10.2.8-vm-en-role-based-security-file-creation-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

Na versão 10.2.8 do HCL Workload Automation, a opção global enRoleBasedSecurityFileCreation (alias rs) tem valor padrão yes, ou seja, o modelo de segurança baseado em papéis fica habilitado na instalação.

> **ATENCAO / RESSALVAS DE USO:** Aplica-se a instalação nova na 10.2.8; a documentação indica que em upgrade o valor efetivo pode diferir (clássico/no para compatibilidade).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enRoleBasedSecurityFileCreation=opção global do optman que habilita o modelo de segurança baseado em papéis (role-based security), rs=alias da opção enRoleBasedSecurityFileCreation, role-based security=modelo de segurança baseado em domínios, papéis e listas de controle de acesso |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description (HCL Workload Automation 10.2.8) |
| Citacao de suporte | enRoleBasedSecurityFileCreation | rs ... The default value is yes, which means that the role-based security model is enabled for your installation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | vm-en |

**Perguntas relacionadas:**

- Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?


---

### 242. `hwa-10.2.8-vm-en-role-based-security-file-creation-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

Na versão 9.5 do HCL Workload Automation, a opção global enRoleBasedSecurityFileCreation (rs) tem valor padrão no, mantendo o modelo de segurança clássico (dumpsec/makesec) como padrão.

> **ATENCAO / RESSALVAS DE USO:** Aplica-se a 9.5; difere do padrão yes documentado para 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enRoleBasedSecurityFileCreation=opção global do optman que habilita o modelo de segurança baseado em papéis, role-based security=modelo de segurança baseado em papéis, classic security=modelo clássico de segurança gerenciado por dumpsec e makesec |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description (HCL Workload Automation 9.5) |
| Citacao de suporte | The default value is no, which means that the role-based security model is not enabled for your installation. You continue to use the classic security model that allows you to update your security file by using dumpsec and makesec commands from the command line. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | vm-en |

**Perguntas relacionadas:**

- Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?


---

### 243. `hwa-10.2.8-vm-en-role-based-security-file-creation-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

O valor padrão da opção global enRoleBasedSecurityFileCreation (rs) difere entre versões: no na 9.5 (segurança clássica habilitada) e yes na 10.2.8 (segurança baseada em papéis habilitada), caracterizando uma diferença version-dependent do modelo de segurança padrão.

> **ATENCAO / RESSALVAS DE USO:** Registro version_dependent: citar ambas as páginas. Padrão muda de no (9.5) para yes (10.2.8).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enRoleBasedSecurityFileCreation=opção global de seleção do modelo de segurança, role-based security=segurança baseada em papéis, classic security=segurança clássica |
| Produto | HCL Workload Automation |
| Versao | multi |
| Plataforma | Distributed |
| Status do conhecimento | version_dependent |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description (HCL Workload Automation 10.2.8) |
| Citacao de suporte | enRoleBasedSecurityFileCreation | rs ... The default value is yes, which means that the role-based security model is enabled for your installation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | multi |
| Escopo de plataforma | Distributed |

**Perguntas relacionadas:**

- Qual o propósito e valor padrão da opção global enRoleBasedSecurityFileCreation no optman do HWA?


---

### 244. `hwa-10.2.8-vm-linhagem-de-marca-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `version`

**Afirmacao / Conteudo:**

A linhagem de marcas do produto distribuído é: Tivoli Workload Scheduler 8.5 -> IBM Workload Scheduler 9.x (ex.: 9.5) -> HCL Workload Automation 10.1 -> HCL Workload Automation 10.2.x (10.2.8), sendo a versão 10.2.x sucessora da linha IBM 10.2 e da linha TWS/IWS 9.x e 8.5.x.

> **ATENCAO / RESSALVAS DE USO:** Título 9.5 usa 'IBM Workload Scheduler'; documentação 10.1 e 10.2.8 já usa 'HCL Workload Automation', evidenciando a transição de marca para a HCL.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TWS=Tivoli Workload Scheduler, IWS=IBM Workload Scheduler, HWA=HCL Workload Automation, linhagem de marca=sucessão de marcas IBM Tivoli -> IBM -> HCL |
| Produto | HCL Workload Automation |
| Versao | multi |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/ibm-workload-scheduler-version-95-release-notes |
| Titulo da fonte | IBM Workload Scheduler Version 9.5 Release Notes (IBM) |
| Citacao de suporte | © Copyright International Business Machines Corporation 2006, 2016 ... © Copyright HCL Technologies Limited 2016, 2021. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | version_history |
| Modo de operacao | read |
| Escopo de versao | multi |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | vm-linhagem |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A linhagem de marcas do produto distribuído é: Tivoli Workload Scheduler 8.5 -> IBM Workload Scheduler 9.x (ex?


---

### 245. `hwa-10.2.8-vm-scheduler-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `version`

**Afirmacao / Conteudo:**

O produto distribuído IBM era chamado Tivoli Workload Scheduler (TWS) nas versões 8.x e ainda na 9.1 (nota oficial 'Release Notes for Tivoli Workload Scheduler, version 9.1'), passando a ser documentado como IBM Workload Scheduler na versão 9.5 (título 'IBM Workload Scheduler Version 9.5 Release Notes').

> **ATENCAO / RESSALVAS DE USO:** A página 9.1 da IBM lista compatibilidade com MDM/FTA 8.5/8.5.1/8.6, evidenciando a linhagem TWS 8.5. A página 9.5 já usa o nome IBM Workload Scheduler, com copyright conjunto IBM e HCL.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TWS=Tivoli Workload Scheduler, IWS=IBM Workload Scheduler, Tivoli Workload Scheduler=nome original do produto IBM, IBM Workload Scheduler=renomeação do produto a partir da linha 9.x |
| Produto | HCL Workload Automation |
| Versao | 8.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/release-notes-tivoli-workload-scheduler-version-91 |
| Titulo da fonte | Release Notes for Tivoli Workload Scheduler, version 9.1 (IBM) |
| Citacao de suporte | This document supplies the release notes for IBM® Tivoli® Workload Scheduler, version 9.1. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | version_history |
| Modo de operacao | read |
| Escopo de versao | 8.5 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| verbs | release; version |
| Familia | vm-scheduler |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O produto distribuído IBM era chamado Tivoli Workload Scheduler (TWS) nas versões 8.x e ainda na 9.1 (nota oficial 'Release Notes for Tivoli Workload Scheduler, version 9.1'), passando a ser documentado como IBM Workload Scheduler na versão 9.5 (título 'IBM Workload Scheduler Version 9.5 Release Notes')?


---

### 246. `hwa-10.2.8-wa-pull-info-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `auth`

**Afirmacao / Conteudo:**

In HCL Workload Automation Distributed 10.2.8, wa_pull_info is a collection script that produces environment and workstation information and can snapshot DB2 and Liberty data into a dated package, replacing the legacy tws_inst_pull_info. The -user parameter is mandatory and the output may contain sensitive data; share it only with authorized support and redact as needed.

> **ATENCAO / RESSALVAS DE USO:** Verified parts: script purpose, DB2/Liberty snapshot as dated package ('The wa_pull_info script replaces the back-level tws_inst_pull_info script, which is no longer supported'; '-user ... This parameter is mandatory'). Corroborated by the 'Data capture utility' troubleshooting page (awstrmetronome.html, v1028). The final clause about the output containing sensitive data and needing redaction was NOT found verbatim on the opened official pages - treat that clause as unverified operational guidance. Confidence medium for the composite claim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsinstpullinfo.html |
| Titulo da fonte | wa_pull_info |
| Citacao de suporte | This is a script that produces information about your HCL Workload Automation environment and your local workstation, and can take a snapshot of DB2 and WebSphere Application Server Liberty data on the master domain manager, saving them as a dated package. |
| Coletado em | 2026-08-18 |
| Capacidade | auth |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=wa |
| Status de revisao | verified |
| Tipo | other |
| Familia | wa-pull |

**Perguntas relacionadas:**

- Como utilizar o utilitário wa_pull_info no HCL Workload Automation?
- Qual a sintaxe ou procedimento no wa_pull_info para gerenciar auth?
- Qual a função do script wa_pull_info no HWA e que tipo de dados ele coleta?


---

### 247. `hwa-10.2.8-wsa-en-service-assurance-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

O Workload Service Assurance do HCL Workload Automation 10.2.8 é habilitado/desabilitado pela opção global enWorkloadServiceAssurance (abreviação wa), que está habilitada por padrão (YES), conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Opção global que controla o processamento privilegiado de trabalhos críticos; padrão YES.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enWorkloadServiceAssurance=enWorkloadServiceAssurance (wa) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | Enables or disables privileged processing of mission-critical jobs and their predecessors. The default value is YES. Specify NO to disable. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_enable |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-en |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O Workload Service Assurance do HCL Workload Automation 10.2.8 é habilitado/desabilitado pela opção global enWorkloadServiceAssurance (abreviação wa), que está habilitada por padrão (YES), conforme documentação oficial?


---

### 248. `hwa-10.2.8-wsa-estimated-duration-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a duração estimada (estimated duration) de um trabalho é baseada nas estatísticas coletadas de execuções anteriores do trabalho, o que afeta a precisão dos tempos calculados para redes críticas que incluem trabalhos executados pela primeira vez; para um shadow job, a duração estimada é sempre o valor padrão de um minuto, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a base estatística da duração estimada usada no cálculo dos tempos críticos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | estimated duration=duração estimada, shadow job=shadow job |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefiningcriticaljobs.html |
| Titulo da fonte | Planning critical jobs |
| Citacao de suporte | The estimated duration of a job is based on the statistics collected from previous runs of the job. In the case of a shadow job, the estimated duration is always set to the default value of one minute. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_estimated_duration |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-estimated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a duração estimada (estimated duration) de um trabalho é baseada nas estatísticas coletadas de execuções anteriores do trabalho, o que afeta a precisão dos tempos calculados para redes críticas que incluem trabalhos executados pela primeira vez; para um shadow job, a duração estimada é sempre o valor padrão de um minuto, conforme documentação oficial?


---

### 249. `hwa-10.2.8-wsa-hot-list-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Dynamic Workload Console fornece views especializadas para rastrear trabalhos críticos e seus predecessores, acessíveis pelo Dashboard ou por uma task usando o Orchestration Monitor, listando todos os trabalhos críticos do engine com status normal, potencial ou alto risco e permitindo navegar para a hot list, o caminho crítico, detalhes dos predecessores, logs de trabalhos e o confidence factor, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta as views do DWC para monitoramento do WSA.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Dynamic Workload Console=Dynamic Workload Console, hot list=hot list, critical path=caminho crítico, confidence factor=fator de confiança |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | The Dynamic Workload Console provides specialized views for tracking the progress of critical jobs and their predecessors. You can access the views from the Dashboard or create a task to monitor critical tasks using Orchestration Monitor. The initial view lists all critical jobs for the engine, showing the status: normal, potential risk, or high risk. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list; status |
| Familia | wsa-hot |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o Dynamic Workload Console fornece views especializadas para rastrear trabalhos críticos e seus predecessores, acessíveis pelo Dashboard ou por uma task usando o Orchestration Monitor, listando todos os trabalhos críticos do engine com status normal, potencial ou alto risco e permitindo navegar para a hot list, o caminho crítico, detalhes dos predecessores, logs de trabalhos e o confidence factor, conforme documentação oficial?


---

### 250. `hwa-10.2.8-wsa-jm-promoted-nice-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção local jm promoted nice define o valor nice atribuído a trabalhos críticos ou predecessores que precisam ser promovidos em sistemas UNIX e Linux, para que recebam mais recursos e sejam processados antes de outros trabalhos; o padrão é -1, números menores representam prioridades maiores, e se um inteiro positivo for especificado o valor padrão é usado, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a opção local jm promoted nice (UNIX/Linux).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm promoted nice=jm promoted nice, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | Sets the nice value to be assigned to critical jobs or critical job predecessors that need to be promoted on UNIX and Linux operating systems... The default is -1 and lower numbers represent higher priorities. If you specify a positive integer, the default value is used. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_promoted_nice |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção local jm promoted nice define o valor nice atribuído a trabalhos críticos ou predecessores que precisam ser promovidos em sistemas UNIX e Linux, para que recebam mais recursos e sejam processados antes de outros trabalhos; o padrão é -1, números menores representam prioridades maiores, e se um inteiro positivo for especificado o valor padrão é usado, conforme documentação oficial?


---

### 251. `hwa-10.2.8-wsa-jm-promoted-priority-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção local jm promoted priority define o valor de prioridade para trabalhos críticos ou predecessores que precisam ser promovidos em sistemas Windows, com valores possíveis High, AboveNormal, Normal, BelowNormal e Low ou Idle, sendo o padrão AboveNormal, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a opção local jm promoted priority (Windows).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm promoted priority=jm promoted priority, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | Sets the priority value for critical jobs or critical job predecessors that need to be promoted so that Windows operating systems assign them more resources... The possible values are: High, AboveNormal, Normal, BelowNormal, Low or Idle. The default is AboveNormal. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_promoted_priority |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção local jm promoted priority define o valor de prioridade para trabalhos críticos ou predecessores que precisam ser promovidos em sistemas Windows, com valores possíveis High, AboveNormal, Normal, BelowNormal e Low ou Idle, sendo o padrão AboveNormal, conforme documentação oficial?


---

### 252. `hwa-10.2.8-wsa-long-duration-threshold-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção global longDurationThreshold (abreviação ld) é um valor percentual (padrão 150) pelo qual, se a duração real de um trabalho atingir 150% ou mais da duração estimada, o trabalho é considerado de duração longa e é adicionado à hot list visível no Dynamic Workload Console, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o limiar de duração longa e inclusão na hot list.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | longDurationThreshold=longDurationThreshold (ld), hot list=hot list |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | The longDurationThreshold global option is a percentage value. The default is 150. Using the default value, if the actual duration of a job is 150% of the estimated duration or longer, the job is considered to have a long duration and is added to the hot list. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_long_duration_threshold |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | wsa-long |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global longDurationThreshold (abreviação ld) é um valor percentual (padrão 150) pelo qual, se a duração real de um trabalho atingir 150% ou mais da duração estimada, o trabalho é considerado de duração longa e é adicionado à hot list visível no Dynamic Workload Console, conforme documentação oficial?
- Qual o propósito e valor padrão da opção global longDurationThreshold no optman do HWA?


---

### 253. `hwa-10.2.8-wsa-promoted-job-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, quando o critical start time de um trabalho está se aproximando e o trabalho ainda não iniciou, o mecanismo de promoção (promotion) é usado: o trabalho promovido recebe recursos adicionais do sistema operacional e sua submissão é priorizada, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a promoção automática de prioridade de trabalhos críticos na aproximação do deadline.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | promotion=promoção, promoted job=trabalho promovido |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | When the critical start time of a job is approaching and the job has not started, the promotion mechanism is used. A promoted job is assigned additional operating system resources and its submission is prioritized. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_promotion |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | wsa-promoted |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, quando o critical start time de um trabalho está se aproximando e o trabalho ainda não iniciou, o mecanismo de promoção (promotion) é usado: o trabalho promovido recebe recursos adicionais do sistema operacional e sua submissão é priorizada, conforme documentação oficial?


---

### 254. `hwa-10.2.8-wsa-promotion-offset-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção global promotionOffset (abreviação po) determina o intervalo de tempo antes do critical start time em que um trabalho se torna elegível para promoção; seu valor padrão é 120 segundos, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a opção global de promoção e seu padrão.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | promotionOffset=promotionOffset (po) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | The promotionoffset global option determines the length of time before the critical start time that a job becomes eligible for promotion. The default setting is 120 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_promotion_offset |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start |
| Familia | wsa-promotion |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a opção global promotionOffset (abreviação po) determina o intervalo de tempo antes do critical start time em que um trabalho se torna elegível para promoção; seu valor padrão é 120 segundos, conforme documentação oficial?
- Qual o propósito e valor padrão da opção global promotionOffset no optman do HWA?


---

### 255. `hwa-10.2.8-wsa-promotion-offset-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os trabalhos promovidos são selecionados para submissão depois de trabalhos com prioridades 'high' e 'go', mas antes de todos os demais trabalhos, e o timing das promoções é controlado pela opção global promotionoffset, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a posição dos trabalhos promovidos na fila de submissão.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | promotionOffset=promotionOffset, priority=prioridade |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Processing and monitoring critical jobs |
| Citacao de suporte | The timing of promotions is controlled by the global option promotionoffset. Promoted jobs are selected for submission after jobs that have priorities of high and go, but before all other jobs. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_promotion_selection |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-promotion |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os trabalhos promovidos são selecionados para submissão depois de trabalhos com prioridades 'high' e 'go', mas antes de todos os demais trabalhos, e o timing das promoções é controlado pela opção global promotionoffset, conforme documentação oficial?


---

### 256. `hwa-10.2.8-wsa-security-file-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, é obrigatório que os usuários que possuem as instâncias executando trabalhos críticos estejam autorizados a trabalhar com todos os trabalhos, job streams e workstations associados, devendo ter direitos DISPLAY, MODIFY e LIST no arquivo de segurança para todos os objetos JOB, SCHEDULE e CPU, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Requisito de segurança do arquivo de segurança para o WSA funcionar.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | security file=arquivo de segurança |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgenablewsa.html |
| Titulo da fonte | Enabling and configuring workload service assurance |
| Citacao de suporte | It is mandatory that the users who own the HCL Workload Automation instances running critical jobs are authorized to work with all jobs, job streams, and workstations associated with these jobs. These users must therefore have DISPLAY, MODIFY, and LIST rights in the security file for all the JOB, SCHEDULE and CPU associated objects. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_security_requirements |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | display; list; modify |
| Familia | wsa-security |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, é obrigatório que os usuários que possuem as instâncias executando trabalhos críticos estejam autorizados a trabalhar com todos os trabalhos, job streams e workstations associados, devendo ter direitos DISPLAY, MODIFY e LIST no arquivo de segurança para todos os objetos JOB, SCHEDULE e CPU, conforme documentação oficial?


---

### 257. `hwa-10.2.8-wsa-service-assurance-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

O Workload Service Assurance é um recurso opcional do HCL Workload Automation 10.2.8 que permite marcar trabalhos como críticos para o negócio (mission-critical) e assegurar que sejam processados em tempo hábil, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o propósito geral do WSA: flag de trabalhos críticos e processamento em tempo hábil.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Workload Service Assurance=WSA, critical job=trabalho crítico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Using workload service assurance |
| Citacao de suporte | Workload service assurance is an optional feature that provides the means to flag jobs as mission critical for your business and to ensure that they are processed in a timely manner. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_introduction |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsa-service |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O Workload Service Assurance é um recurso opcional do HCL Workload Automation 10.2.8 que permite marcar trabalhos como críticos para o negócio (mission-critical) e assegurar que sejam processados em tempo hábil, conforme documentação oficial?


---

### 258. `hwa-10.2.8-wsa-service-class-0029`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

> **ATENCAO / RESSALVAS DE USO:** Service class/policy/srvclass sao conceitos do HWA for Z (z/OS), nao distributed.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | service class=classe de serviço |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Workload service assurance - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The service class/service policy mechanism is available only on HCL Workload Automation for Z. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_critical_flag |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| verbs | set |
| Familia | wsa-service |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?


---

### 259. `hwa-10.2.8-wsa-service-policy-0030`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

> **ATENCAO / RESSALVAS DE USO:** Service class/policy/srvclass sao conceitos do HWA for Z (z/OS), nao distributed.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | service policy=política de serviço |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Workload service assurance - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The service class/service policy mechanism is available only on HCL Workload Automation for Z. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_critical_flag |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| verbs | set |
| Familia | wsa-service |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?


---

### 260. `hwa-10.2.8-wsa-sla-report-0028`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

The official HCL Workload Automation 10.2.8 Distributed documentation describes monitoring views for critical jobs (hot list, critical path, confidence factor) but does not document a report specifically named "SLA" or "Workload Service Assurance report" in the Dynamic Workload Console.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia de um relatorio nomeado "SLA" no DWC; WSA e um recurso de monitoramento de jobs criticos, nao um relatorio.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SLA report=relatório SLA, Workload Service Assurance report=relatório WSA |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcritjobproc.html |
| Titulo da fonte | Critical job processing - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The hot list contains the critical jobs whose start time is approaching... The critical path... The confidence factor. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | wsa-sla |

**Perguntas relacionadas:**

- Como o HWA Distributed monitora SLAs de execução e caminhos críticos de jobs?


---

### 261. `hwa-10.2.8-wsa-srvclass-srvpol-zos-0031`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `wsa`

**Afirmacao / Conteudo:**

Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform. In Distributed 10.2.8, the critical job flag is set with the "critical" keyword in the job statement.

> **ATENCAO / RESSALVAS DE USO:** Service class/policy/srvclass sao conceitos do HWA for Z (z/OS), nao distributed.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | srvclass=srvclass, srvpol=srvpol |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Workload service assurance - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The service class/service policy mechanism is available only on HCL Workload Automation for Z. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | wsa_critical_flag |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | mdm |
| verbs | set |
| Familia | wsa-srvclass |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Service class and service policy are concepts documented only for HCL Workload Automation for Z (z/OS integration with WLM), not for the Distributed platform?


---

### 262. `hwa-10.2.8-wsa-time-planner-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, quando o Workload Service Assurance está habilitado, as threads de execução Time Planner e Plan Monitor, executando dentro do WebSphere Application Server Liberty, são acionadas para garantir que os trabalhos críticos sejam concluídos a tempo, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta o mecanismo computacional do WSA (Time Planner e Plan Monitor).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Time Planner=Time Planner, Plan Monitor=Plan Monitor |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwkldserviceassurance.html |
| Titulo da fonte | Using workload service assurance |
| Citacao de suporte | Two additional threads of execution, Time Planner and Plan Monitor, that run within WebSphere Application Server Liberty, are thereafter engaged to make sure that the critical jobs are completed on time. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| verbs | plan |
| Familia | wsa-time |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, quando o Workload Service Assurance está habilitado, as threads de execução Time Planner e Plan Monitor, executando dentro do WebSphere Application Server Liberty, são acionadas para garantir que os trabalhos críticos sejam concluídos a tempo, conforme documentação oficial?


---

### 263. `hwa-10.2.8-wsclass-workstation-class-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `workstation`

**Afirmacao / Conteudo:**

Workstation class: agrupamento lógico de workstations para que jobs sejam direcionados à classe em vez de CPUs individuais; membros podem ser nomes explícitos ou o caractere curinga @.

> **ATENCAO / RESSALVAS DE USO:** CORREÇÃO: o caractere curinga documentado é '@' (não '*'). Membros podem ser nomes explícitos de workstations ou o curinga @. Nome da classe até 16 caracteres; não pode haver mesmo nome para workstation e workstation class.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | workstation class=agrupamento lógico de workstations (cpuclass), members=lista de workstations membros da classe, wildcard=caractere curinga @ que inclui todas as workstations |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgwsclassdefn.html |
| Titulo da fonte | Workstation class definition |
| Citacao de suporte | A workstation class is a group of workstations for which common jobs and job streams can be written. ... The @ wildcard character means that the workstation class includes all workstations. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | workstation_class |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | wsclass-workstation |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Workstation class: agrupamento lógico de workstations para que jobs sejam direcionados à classe em vez de CPUs individuais; membros podem ser nomes explícitos ou o caractere curinga @?


---

### 264. `hwa-8.3-cert-default-expiration-2014-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Na documentacao oficial do Tivoli Workload Scheduler 8.3 (IBM/HCL), os certificados padrao (default certificates) liberados nas versoes 8.3.0 a 8.6.0 expirariam em 10 de fevereiro de 2014; a IBM disponibilizou pacotes updCertsScripts_v<VERSAO> com scripts (updTrustStoresCerts, updKeyStoresCerts, updateTrustKeyStoresCerts) para renovar os certificados padrao.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (awscertsmst.pdf, manual oficial IBM TWS 8.3). Fato historico de certificados padrao 8.3-8.6: expiracao em 2014 e scripts updCertsScripts. NAO generalizar para HWA 10.x (certificados passaram a ser gerados via certman/ssls a partir de 10.2.3).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 8.3.0-8.6.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.ibm.com/docs/en/tws/8.3.0 |
| Titulo da fonte | IBM Workload Scheduler 8.3 - Renewing default certificates |
| Citacao de suporte | The default certificates released with the Tivoli Workload Scheduler V8.3.0, V8.4.0, V8.5.0, V8.5.1, and V8.6.0 general availability components expire on February 10, 2014. Tivoli Workload Scheduler provides a package that contains new default certificates and a set of scripts that you can use to renew them. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | certificados padrao=default certificates, updCertsScripts=pacote de scripts de renovacao, expiracao=10/02/2014 |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 8.3.0-8.6.0 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | cert-default |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na documentacao oficial do Tivoli Workload Scheduler 8.3 (IBM/HCL), os certificados padrao (default certificates) liberados nas versoes 8.3.0 a 8.6.0 expirariam em 10 de fevereiro de 2014; a IBM disponibilizou pacotes updCertsScripts_v<VERSAO> com scripts (updTrustStoresCerts, updKeyStoresCerts, updateTrustKeyStoresCerts) para renovar os certificados padrao?


---

### 265. `hwa-8.3-clisslserverauth-clisslserverauth-expiry-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

No Tivoli Workload Scheduler 8.3, a variavel CLISSLSERVERAUTH no arquivo localopts controla o comportamento da comunicacao apos a expiracao dos certificados padrao: com CLISSLSERVERAUTH=no no cliente de linha de comando remoto, a comunicacao continua funcionando apos a expiracao; com CLISSLSERVERAUTH=yes, a comunicacao para de funcionar.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (awscertsmst.pdf, manual oficial IBM TWS 8.3). Fato especifico de 8.x; a gestao de certificados mudou no HWA 10.2.3+.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 8.3.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.ibm.com/docs/en/tws/8.3.0 |
| Titulo da fonte | IBM Workload Scheduler 8.3 - Renewing default certificates (CLISSLSERVERAUTH) |
| Citacao de suporte | If you have an SSL connection that uses default certificates between the remote command-line client and the master domain manager: The variable CLISSLSERVERAUTH=no in the remote command-line client localopts file ... The communication continues to work after the default certificates expiration date. The variable CLISSLSERVERAUTH=yes ... The communication does not work after the default certificates expiration date. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | CLISSLSERVERAUTH=variavel do localopts que controla autenticacao SSL do cliente de linha de comando, localopts=arquivo de opcoes locais |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 8.3.0 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | clisslserverauth-clisslserverauth |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No Tivoli Workload Scheduler 8.3, a variavel CLISSLSERVERAUTH no arquivo localopts controla o comportamento da comunicacao apos a expiracao dos certificados padrao: com CLISSLSERVERAUTH=no no cliente de linha de comando remoto, a comunicacao continua funcionando apos a expiracao; com CLISSLSERVERAUTH=yes, a comunicacao para de funcionar?


---

### 266. `hwa-9.5-perfreport-contrast-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2-perfreport-0003: os valores de tuning de replicacao de plano (com.ibm.tws.planner.monitor.subProcessors=10, cachesize=70000, filecachesize=40000, cachemaxage=21600000) sao recomendados pelo relatorio de performance 10.2; na 9.5 esses valores nao eram descritos com os mesmos defaults de monitor do planner, portanto tuning de planner e version-dependent e nao deve ser copiado da 10.2 para a 9.5.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: tuning de planner reportado para 10.2; nao assumir que os mesmos defaults valem na 9.5.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html |
| Titulo da fonte | HCL Workload Automation JnextPlan reference (planner monitor properties) |
| Citacao de suporte | com.ibm.tws.planner.monitor.subProcessors = 10 ... com.ibm.tws.planner.monitor.cachemaxage = 21600000. |
| Coletado em | 2026-08-21 |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=perfreport |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2-perfreport-0003: os valores de tuning de replicacao de plano (com?


---

### 267. `hwa-9.5-real-rs-default-no-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5, a opcao global enRoleBasedSecurityFileCreation (rs) tem valor padrao no, mantendo o modelo de seguranca classico (baseado em arquivos de usuario e listas de acesso legadas). A partir da 10.2.8 o padrao passa a ser yes (modelo baseado em papeis). Mudanca de default real entre 9.5 e 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (global options 9.5). Contrasta com 10.2.8 (default yes). Nao generalizar o default de seguranca entre versoes.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | HCL Workload Automation 9.5 global options - enRoleBasedSecurityFileCreation |
| Citacao de suporte | enRoleBasedSecurityFileCreation | rs ... The default value is no, which means that the classic security model is used. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | enRoleBasedSecurityFileCreation=opcao global de modelo de seguranca (classico vs papeis), classic security=modelo classico de seguranca (default em 9.5) |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | real-rs |


---

### 268. `hwa-lab-10.2.8-adhoc-logon-0028`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

In the HWA laboratory, an ad hoc `sbd` job dispatched after the workstation limit was raised but failed with AWSITA066E when run as a privileged user; specifying `logon=wauser` caused the ad hoc `ls` command to complete successfully with return code 0.

> **ATENCAO / RESSALVAS DE USO:** For this lab's dynamic-agent executor, ad hoc commands should specify a permitted non-privileged logon such as wauser. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local JobManager_message.log and conman showjobs

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Ad hoc dynamic-agent logon validation |
| Citacao de suporte | AWSITA066E Privileged user is not allowed to run jobs on this executor; subsequent ADHOC_LIMIT_LOGON SUCC ... return code 0. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | credential_sensitive |
| Capacidade | log |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['sbd'], result=AWSITA066E Privileged user is not allowed to run jobs on this executor; subsequent ADHOC_LIMIT_LOGON SUCC ... return code 0. | For this lab's dynamic-agent executor, ad hoc commands should specify a permitted non-privileged logon such as wauser., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-limit-rootcause.jsonl |
| Terminologia normalizada | message=AWSITA066E |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA066E no HWA?
- Como solucionar ou diagnosticar o erro AWSITA066E no HWA?


---

### 269. `hwa-lab-10.2.8-agent-docker-install-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (host CachyOS), o dynamic agent foi instalado em container proprio (tws-agent, RHEL 9.8 UBI-init, rede docker hwa-mesh 172.18.0.0/24, IP 172.18.0.12) usando o kit HWA_10.2.8_LNX_X86_64_AGENT.zip (baixado do Google Drive, 669MB) com o script twsinst: 'twsinst -new -agent dynamic -acceptlicense yes -uname wauser -thiscpu AGT1 -tdwbhostname tws-hwa.lab -tdwbport 31116 -sslkeysfolder <pasta PEM com ca.crt/tls.key/tls.crt> -sslpassword <pw> -wauser wauser -wapassword <pw>'. Resultado: AWSFAB033I 'The installation has completed successfully'; instalacao em /opt/HCL/TWA_wauser (binarios TWS + TWSDATA), JobManager + agente ITA iniciados, TWS_TDWB_HOSTNAME=tws-hwa.lab TWS_TDWB_PORT=31116.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T05:50:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | AWSFAB067I Start up / AWSFAB068I Completing / AWSFAB139I Installing registries / AWSFAB033I completed successfully. JobManager_message.log: AWSITA047I Starting subagent JobManager; AWSITA050I agent open for e-business; AWSITA083I Resource information was sent to https://tws-hwa.lab:31116/JobManagerRESTWeb/... |
| observations | Diferente do kit MDM (serverinst), o kit AGENT so traz twsinst. -tdwbhostname deve resolver para o broker (MDM_DWB roda no container do MDM). Com -jwt false, twsinst usa -wauser/-wapassword para baixar CA certs do broker e gera keystores na pasta sslkeysfolder (precisa ser gravavel, nao o mount ro). |


---

### 270. `hwa-lab-10.2.8-agent-docker-job-executed-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No lab container, o agente dinamico TWS-AGENT executou jobs de verdade: job stream AGTTESTJS (job AGT_ECHO, DOCOMMAND 'echo AGT_DYNAMIC_OK; uname -a', STREAMLOGON wauser, TASKTYPE UNIX, RECOVERY STOP) definida via composer add (AWSJCL003I x2) e submetida com 'conman sbs TWS-AGENT#AGTTESTJS' resultou em SUCC rc0 nas duas instancias. Prova: os archives do JobManager do agente (TWSDATA/stdlist/JM/2026.09.09/archive/*.zip) contem out.log com 'AGT_DYNAMIC_OK' e 'Linux tws-agent.lab 7.2.2-1-cachyos ... x86_64 GNU/Linux', confirmando execucao real no container do agente (kernel do host, como esperado em docker).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T06:03:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | conman sj: TWS-AGENT #AGTTESTJS 0302 09/09 SUCC; AGT_ECHO SUCC rc 0. out.log: AGT_DYNAMIC_OK / Linux tws-agent.lab 7.2.2-1-cachyos x86_64 GNU/Linux. |
| observations | Limite da workstation precisou ser liberado (conman 'limit TWS-AGENT#;10') apos entrar no plano (default 0). Validacao completa: install -> registro no broker -> JnextPlan -> job executado no agente docker. |


---

### 271. `hwa-lab-10.2.8-agent-docker-registered-plan-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No lab container, o agente instalado com -thiscpu AGT1 foi registrado pelo broker no banco como workstation dinamica 'TWS-AGENT' (mdl.wks_workstations: wks_agent_type A, node tws-agent, tcp 0) — o broker nomeia pela base 'TWS-AGENT', nao pelo -thiscpu. A workstation so aparece no 'conman showcpus' apos JnextPlan (extensao do plano), confirmando que workstation dinamica entra no plano via virada/extensao, nao em tempo real. Após JnextPlan o plano passou a run #29 (end 09/10 00:04) com TWS-AGENT como UNIX AGENT LIMIT 10 linkado (LBI J M).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T05:57:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | mdl.wks_workstations: TWS-AGENT|A|tws-agent|0. conman showcpus: TWS-AGENT 29 UNIX AGENT 10 LBI J M. |
| observations | Pitfall JnextPlan: a primeira virada com a nova workstation falhou com AWSJPL006E (database object workstation cannot be loaded) porque o node 'tws-agent' sem '.lab' nao resolvia; adicionar '172.18.0.12 tws-agent.lab tws-agent' ao /etc/hosts do MDM resolveu (RC=0 na virada seguinte). Tambem: nome de job stream max 16 chars (AWSJOM012E) e job precisa de definicao inline no SCHEDULE (jd nao existe se referenciado vazio - AWSJDB303E). |


---

### 272. `hwa-lab-10.2.8-aida-alert-cycle-0075`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | docker logs aida-orchestrator; GET aida-es:9200/alert-definitions/_search |
| Pre-condicoes | AIDA rodando com metricas coletadas do MDM |
| sanitized_output | O aida-orchestrator executa o ciclo de deteccao de alertas a cada 15 minutos (PROPHET_ORCHESTRATOR schedule_alert=15): log mostra 'callAlertAPI - POST /detectAlerts status=200 for definition=<DEFINITION_ID>' repetidamente para as 12 alert-definitions (TOTAL_MESSAGE, CONTINUOUS_MESSAGE, etc.). O endpoint /detectAlerts do aida-ad responde 200. O indice alert-instances (criado pelo AD quando um alerta dispara) permanece vazio porque nenhuma anomalia foi detectada ainda (metricas estaveis no lab). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura de logs). |
| Criterio de parada | NA. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_using_AIDA.html |
| performed_at | 2026-08-25T15:30:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Ciclo de alertas do AIDA validado: orchestrator -> aida-ad /detectAlerts a cada 15min. Sem anomalias detectadas no lab (metricas estaveis), nenhum alert-instance criado - comportamento esperado. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 273. `hwa-lab-10.2.8-aida-alert-definitions-0070`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | GET aida-es:9200/alert-definitions/_search?size=50 (via docker exec aida-es curl -sk -u admin:admin) |
| Pre-condicoes | AIDA rodando (aida-es up); exporter coletou definicoes (alert-definitions com 12 docs) |
| sanitized_output | Indice alert-definitions contem 12 definicoes reais de alerta, 2 por KPI (uma continuous + uma total), para 6 KPIs. Schema de cada doc: definitionID (ex.: CONTINUOUS_JOBWKS, TOTAL_JOBWKS), name (ex.: 'Continuous anomalies for jobs in plan by workstation'), kpi (metric_name, ex.: application_wa_JobsByWorkstation_jobs), trigger {type: continuous|total, value: 10, timeFrame: 60, description: 'Over 10 Consecutive Anomalies within 1 hour' | 'Over 10 Anomalies within 1 hour'}, periodicity: '1 hour', isActive: 'true', alert-definition: CONTINUOUS|TOTAL. KPIs cobertos: JOBWKS (jobs por workstation), JOBFOLDER (jobs por folder), JOBSTATUS (jobs por status), JOBTOTAL (total de jobs), MESSAGE (message files fill percentile, application_wa_msgFileFill_percent), INCOMPLETEPREDECESSOR_CRITICAL (WA critical job incomplete predecessor, application_wa_criticalJob_incompletePredecessor_jobs). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura do indice OpenSearch). |
| Criterio de parada | Interromper se o indice nao existir (exporter ainda nao rodou). |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| performed_at | 2026-08-25T14:40:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Schema real das alert-definitions do AIDA 10.2.8: trigger type 'continuous' = N anomalias CONSECUTIVAS no periodo; 'total' = N anomalias totais no periodo. value=10 e timeFrame=60 (minutos) sao os defaults. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 274. `hwa-lab-10.2.8-aida-anomaly-inject-0080`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | 1) POST /twsd/api/v2/model/job (criar definicao FAIL_AIDA_TEST com task inexistente) 2) POST /twsd/api/v2/plan/job/submit (submeter ao plano, id 0d5a44db-a32b-3295-8532-c6b2f99077ca) 3) GET /twsd/api/v2/plan/job (verificar) 4) GET aida-es:9200/metric-index-*/_search?q=metricname:application_wa_JobsInPlanCount_job |
| Pre-condicoes | MDM REST V2 ativo (31116); AIDA coletando metricas (3121 docs); Usuario wauser com acesso submit |
| sanitized_output | Job de falha submetido via REST API V2 (submit retornou successfulResourceResponses com id 0d5a44db...). O plano tinha 235 jobs (muitos de rodadas anteriores: DS_CHAIN_A x100+, FAIL_STOP, FAIL_CONT, FAIL_RERUN, PRIO_*, R7JOB*, EVTJOB*). KPI jobs in plan by status no OpenSearch: SUCCESSFUL=26, READY=0, ERROR=7, HELD=2, WAITING=200 (amostra ts=1787686039743). INVOCACOES do AIDA: 3121 metricas coletadas; predictions index count=0; retrain-details: retrainProgress=false, predictionsSubmited=0; alert/instance/list: result=[], count=0. NENHUMA anomalia detectada ou alerta gerado apos a submissao do job de falha. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Remover o job do plano (DELETE /twsd/api/v2/plan/job/{id}) se necessario. |
| Criterio de parada | Interromper se o MDM ou AIDA travar. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_using_AIDA.html |
| performed_at | 2026-08-25T19:40:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | DESCOBERTA: a submissao de um job de falha individual (ou mesmo os 7 jobs em ERROR ja existentes no plano) NAO gera alerta no AIDA com apenas ~4h de dados coletados. O AIDA detecta ANOMALIAS DE TENDENCIA em KPIs (comparando com faixa estatistica do historico); sem baseline historico (dias), o modelo nao define as faixas esperadas e as predicoes ficam em 0 (retrain aceito mas sem serie suficiente). O ciclo de coleta e deteccao (detectAlerts a cada 15min) funciona; o que falta e TEMPO de coleta para o predictor calibrar. Conclusao: para validar deteccao de alerta real, e necessario deixar o lab coletando por 24h+ (retrain automatico diario) e injetar uma DISTORCAO de tendencia (ex.: muitos jobs falhando num periodo), nao um job unico. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 275. `hwa-lab-10.2.8-aida-ash-container-runtime-0069`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | sed -n '1,60p' AIDA.sh; grep -n 'CONTAINER_RUNTIME' AIDA.sh |
| Pre-condicoes | Pacote AIDA 10.2.8 extraido (docker-deployment/AIDA.sh) |
| sanitized_output | AIDA.sh 10.2.8: a funcao detect_container_runtime() NAO auto-detecta o runtime. Se CONTAINER_RUNTIME nao estiver setado, imprime 'Error: CONTAINER_RUNTIME is not set. Please export it before running this script.' e sai com exit 1 (linhas 40-51). Valores aceitos: docker ou podman (CONTAINER_RUNTIME externamente setado). Diferenca vs GitHub publico (main, 10.2.6): o script publico auto-detecta via command -v podman/docker; o 10.2.8 exige a variavel explicita. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura do script). |
| Criterio de parada | NA. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T14:10:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Confirma claim hwa-10.2.8-aida-install-0002 (CONTAINER_RUNTIME obrigatorio) com prova direta do script do pacote 10.2.8. O GitHub publico (branch main, tags :10.2.6) tem comportamento diferente (auto-deteccao) - nao usar o GitHub como fonte para o comportamento do AIDA.sh 10.2.8. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 276. `hwa-lab-10.2.8-aida-config-env-0065`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | editar common.env: LICENSE=notaccepted->accept; WA_OMETRICS/METADATA/RECORDS/ALERT_CONFIG/KPI_CONFIG/WA_CATALOGS de https://WA_URL/... para https://MDMHOST:31116/...; HOST_IP=127.0.0.1:9432; EXTERNAL_HOSTNAME=127.0.0.1 |
| Pre-condicoes | Pacote AIDA extraido (docker-deployment/common.env); MDM REST V2 ativo no host em 127.0.0.1:31116 |
| sanitized_output | common.env ajustado para o lab: LICENSE=accept; URLs do WA apontando para MDMHOST:31116 (metrics, twsd/engine/historical_metric/{metadata,record}, twsd/engine/definition/{alert,kpi,aida_catalog}); HOST_IP=127.0.0.1:9432; EXTERNAL_HOSTNAME=127.0.0.1 (anti Host Header attack); OPENSSL_PASSWORD mantido do pacote (usado p/ cifrar credenciais do engine). Parametros observados no arquivo: LOG_LEVEL, ESCONFIG (admin:admin@aida-es:9200), REDIS_HOST/PSWD/PORT, DEFAULT_SHARD_COUNT, DEFAULT_REPLICA_COUNT, MODEL=prophet, PREDICTION_RECURRENCE=daily, ADAPTIVE_PREDICTION, MIN/MAX_INTERVAL_WIDTH, MAX_BAND_RATIO, MIN_SAMPLES_FOR_LAGS, CLAMP_LOWER_TO_ZERO, TOLERANCE_MILLIS=240000, MINIMUM_SEVERITY_FOR_MAIL=high, ANOMALY_USE_TOLERANCE, METRICS_FETCH_INTERVAL=240, EXPORTER_EXECUTION_INTERVAL=86400, PROPHET_ORCHESTRATOR={"schedule":1440,"schedule_alert":15}, DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_PREDICTIONS_AND_ALERTS=14, MAXIMUM_DAYS_OF_OLDER_DATA=180, RESOLVE_ALERTS_AFTER_DAYS=1. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Restaurar common.env original (backup) ou reverter os valores alterados. |
| Criterio de parada | Interromper se o common.env ficar malformado (LICENSE nao aceito). |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:27:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | EXTERNAL_HOSTNAME e obrigatorio para evitar vulnerabilidade de Host Header attack (o nginx recusa host nao listado com 'Host not matching'). Com EXTERNAL_HOSTNAME=127.0.0.1, a UI so responde em https://127.0.0.1:9432 (localhost:9432 retorna 405). [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 277. `hwa-lab-10.2.8-aida-credentials-0066`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | docker exec aida-config bash -c "source /config.sh && add_credentials wa-waserver:31116 wauser <enc-password>" (senha cifrada via openssl enc -AES-128-ECB -base64 -salt -pbkdf2 -pass env:OPENSSL_PASSWORD); verificar GET aida-es:9200/wa-credentials/_search |
| Pre-condicoes | aida-config rodando com common.env (OPENSSL_PASSWORD definido); aida-es (OpenSearch) acessivel; MDM_LAB com usuario wauser valido |
| sanitized_output | add_credentials gravou no OpenSearch (indice wa-credentials, doc id wa-waserver:31116): host=wa-waserver:31116, username=wauser, password=<AES-128-ECB cifrado>, cypher='', engine='d' (distributed), engineName=''. O config.sh so repassa 2 args no dispatch final ($1 $2); para 3 args (host user encpass) e preciso chamar via 'bash -c source /config.sh && add_credentials ...' ou o fluxo cai no modo interativo (os prompts engolem o input piped e gravam host='n'/'y'). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | credential_sensitive |
| Reversibilidade | delete-credentials ou DELETE do doc no OpenSearch (aida-es:9200/wa-credentials/_doc/wa-waserver:31116). |
| Criterio de parada | Interromper se as credenciais gravadas tiverem host/user vazios (modo interativo corrompido). |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:42:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | As credenciais do engine ficam armazenadas CIFRADAS no OpenSearch (AES-128-ECB com chave derivada de OPENSSL_PASSWORD), conforme doc (passwords must be encrypted inside the database). O fluxo interativo (./AIDA.sh add-credentials) exige TTY; em automacao use add_credentials com 3 args direto no container config. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 278. `hwa-lab-10.2.8-aida-dwc-widget-blocked-0078`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | navegador Edge (CDP) em https://localhost:9443/console/login.jsp; validador visual do AIDA widget no Workload Dashboard |
| Pre-condicoes | DWC 10.2.8 ativo (9443); AIDA ativo (9432); Certificado self-signed do lab |
| sanitized_output | Tentativa de validar visualmente o AIDA widget no Workload Dashboard do DWC via navegador automatizado foi BLOQUEADA pelo Kaspersky Premium: 'Problema de verificacao do certificado detectado - Um ou mais certificados deste site sao invalidos... Impedimos o acesso a este site'. O certificado self-signed do lab (CN=HWA-LAB) dispara o bloqueio do antivirus no navegador. A validacao visual do widget requer excecao manual no Kaspersky ou certificado confiavel. No lado servidor, a integracao esta funcional: AIDA API /api/* responde com token Keycloak (aidaadmin realm aida), alertas detectam (detectAlerts 200), DWC 9443 saudavel. |
| Resultado observado | PARTIAL |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consulta; remover excecao do Kaspersky se adicionada). |
| Criterio de parada | Interromper se o navegador nao carregar o login do DWC. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_alert_notification.html |
| performed_at | 2026-08-25T16:00:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | O widget do AIDA no Workload Dashboard (Anomaly Widget, mostra alertas das ultimas 24h) nao pôde ser validado visualmente no lab devido ao bloqueio Kaspersky do certificado self-signed. Evidencia servidor confirma o funcionamento: API autenticada, ciclo de alertas ativo. Revalidacao visual requer excecao de certificado. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 279. `hwa-lab-10.2.8-aida-email-redis-0077`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | docker logs aida-email; docker exec aida-email sh -c 'echo SMTP_SERVER=$SMTP_SERVER' |
| Pre-condicoes | AIDA rodando (aida-email up) |
| sanitized_output | O container aida-email (responde 'Mail container.' em :5000) consome mensagens do Redis (internal event manager): logs mostram 'Message Type message / Received Message: {}' ciclicamente. Com SMTP nao configurado (SMTP_SERVER/SMTP_PORT/SENDER_MAILID/RECIPIENT_MAILIDS vazios no common.env), nenhum email e enviado - comportamento esperado (parametros marcados 'mandatory if you want to receive anomaly notification by email' na doc). O email e disparado quando o aida-ad detecta um alerta e publica no Redis; sem SMTP, o envio e silenciosamente ignorado. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura de logs/config). |
| Criterio de parada | NA. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_mail_cfg.html |
| performed_at | 2026-08-25T15:50:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Fluxo de email do AIDA: aida-ad detecta alerta -> publica no Redis -> aida-email consome e envia via SMTP. Parametros SMTP obrigatorios apenas se quiser notificacao por email (doc oficial). No lab sem SMTP, o container processa mensagens mas nao envia. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 280. `hwa-lab-10.2.8-aida-images-load-0062`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | export CONTAINER_RUNTIME=docker; cd docker-deployment; cat ../aida-images-hcl.tar.gz | docker load |
| Pre-condicoes | Pacote extraido em /opt/hwa/aida; Docker ativo |
| sanitized_output | docker load carregou 9 imagens: hclcr.io/wa/workload-automation/hcl-aida-{nginx,predictor,email,ad,redis,orchestrator,exporter,config,ui}:10.2.8. Tamanhos: predictor 7.74GB (2.07GB compressed), ad/exporter/orchestrator/email ~3.1-3.2GB cada, nginx 2.3GB, ui 353MB, config 258MB, redis 263MB. OpenSearch e Keycloak NAO estao no tar: sao construidos pelos Dockerfile-es (base registry.access.redhat.com/ubi9/ubi + download opensearch-2.19.6-linux-x64.tar.gz do artifacts.opensearch.org) e Dockerfile-keycloak (base quay.io/keycloak/keycloak:26.6.4) durante o build. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | docker image rm hclcr.io/wa/workload-automation/hcl-aida-*:10.2.8 |
| Criterio de parada | Interromper se docker load falhar ou alguma imagem nao carregar. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:24:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Instalacao offline (HCL Flexera): ./AIDA.sh load carrega as 9 imagens AIDA do pacote; es e keycloak exigem internet no build (registries redhat/quay + artifacts.opensearch.org). O comando load do AIDA.sh itera sobre ../aida-*.t*. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 281. `hwa-lab-10.2.8-aida-kpi-catalog-0071`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | GET aida-es:9200/kpis-definition/_search?size=50 |
| Pre-condicoes | AIDA rodando; exporter baixou KPI definitions do MDM (6 docs) |
| sanitized_output | Indice kpis-definition contem 6 definicoes reais de KPI. Schema: name, metric_name (ex.: application_wa_JobsInPlanCount_job_total), frequency: 240 (segundos, = METRICS_FETCH_INTERVAL), category: Jobs|Queue, subcategory: Trend|Trend_by_wks, type: total (quando sem keyprop), keyprop: jobstatus (quando quebra por status), keyPropValues: [SUCCESSFUL, UNDECIDED, WAITING, ERROR, BLOCKED, SUPPRESS, READY, HELD, RUNNING, CANCELED], labels: [workstation] (quando por workstation), workstation: /MDMDA ou /MDMXA, metric_description, esQuery (consulta OpenSearch para agregar: match metricname + term properties.parsedTag + match properties.jobstatus + term properties.workstation), alert-definition: [TOTAL_JOBTOTAL] etc., isActive: true. Doc id: '<name><metric_name><tag>' (ex.: 'Number total jobs in planapplication_wa_JobsInPlanCount_job_totalwa-waserver:31116'). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura do indice). |
| Criterio de parada | Interromper se o indice nao existir. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| performed_at | 2026-08-25T14:42:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | KPIs do AIDA sao definidos por metric_name do MDM (prefixo application_wa_), com frequencia de coleta 240s. Os 10 status de job (SUCCESSFUL..CANCELED) sao os keyPropValues padrao. Workstations reais do lab: /MDMDA e /MDMXA. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 282. `hwa-lab-10.2.8-aida-metric-format-0072`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | GET aida-es:9200/metric-index-*/_search?size=5 |
| Pre-condicoes | AIDA rodando; exporter coletou metricas do MDM |
| sanitized_output | Indice metric-index-<data> (ex.: metric-index-08-25-2026) armazena as metricas coletadas com schema: metricname (ex.: application_wa_JobsInPlanCount_job_total), category (Jobs), subcategory (Trend), value (numero), @timestamp (epoch millis), properties {jobstatus: SUCCESSFUL, mp_scope: application, parsedTag: wawaserver31116}, tag (wa-waserver:31116), parsedTag (wawaserver31116), uuid (random), e keyprop (jobstatus) quando a metrica quebra por status. Exemplo real: {"metricname":"application_wa_JobsInPlanCount_job_total","value":235,"properties":{"parsedTag":"wawaserver31116"},"tag":"wa-waserver:31116"}; e {"metricname":"application_wa_JobsInPlanCount_job","keyprop":"jobstatus","properties":{"jobstatus":"SUCCESSFUL","mp_scope":"application","parsedTag":"wawaserver31116"},"value":26}. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura do indice). |
| Criterio de parada | Interromper se o indice nao existir. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| performed_at | 2026-08-25T14:44:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | O metric-index acumula series temporais por KPI+tag+keyprop; o predictor/ad consomem esses dados. parsedTag = tag sem caracteres especiais. @timestamp em epoch millis. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 283. `hwa-lab-10.2.8-aida-metrics-flow-0067`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | docker restart aida-exporter; docker logs aida-exporter; GET aida-es:9200/_cat/indices e /metric-index-*/_count |
| Pre-condicoes | Credenciais wa-waserver:31116 gravadas (evidencia 0066); MDM REST V2 ativo (metrics endpoint sem auth) |
| sanitized_output | Exporter (up, sem restart-loop) processou 6 KPI definitions de wa-waserver:31116 e inseriu 80 metricas ('Total metrics to insert: 80; bulkKPIsInDatabase called with 80 metrics; Kpis collected and saved'). Metric-index: count cresceu 1->80+ (81 apos nova coleta). Indices OpenSearch criados: metric-index-<data>, alert-definitions (12 docs), kpis-definition, wa-credentials (1), special-days-labels (95), predictions, security-auditlog. /metrics do MDM responde 200 sem auth; /twsd/engine/historical_metric/metadata exige auth (401 sem credencial). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura de logs/indices; restart do exporter e reversivel). |
| Criterio de parada | Interromper se o exporter entrar em restart-loop ou nao coletar metricas. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:50:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Fluxo completo validado: exporter autentica no MDM (wauser), baixa KPI definitions, coleta metricas de /metrics e /historical_metric/*, grava no OpenSearch. METRICS_FETCH_INTERVAL=240s (endpoint /metrics expira apos ~10min sem poll). O orchestrator agenda predicoes a cada 1440 min e deteccao de alertas a cada 15 min. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 284. `hwa-lab-10.2.8-aida-network-0064`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | adicionar extra_hosts (wa-waserver, MDMHOST, host.docker.internal -> host-gateway) nos 11 servicos do docker-compose.yml; docker compose up -d |
| Pre-condicoes | AIDA em docker (bridge network docker-deployment_aida-net); MDM engine (REST V2) rodando no host WSL2 em 127.0.0.1:31116 |
| sanitized_output | Sem extra_hosts, o exporter falhava com 'Failed to resolve wa-waserver' e 'NameResolutionError: HTTPConnection(host=wa-waserver, port=31116)'. Apos adicionar extra_hosts 'wa-waserver:host-gateway', 'MDMHOST:host-gateway', 'host.docker.internal:host-gateway' nos 11 servicos: resolucao OK (wa-waserver -> 172.17.0.1, MDMHOST -> 172.17.0.1, host.docker.internal -> 172.17.0.1, aida-es -> 172.18.0.3 via DNS docker). O exporter passou a acessar https://wa-waserver:31116/metrics com HTTP 200. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Remover o bloco extra_hosts do docker-compose.yml e recriar os containers. |
| Criterio de parada | Interromper se a resolucao DNS interna quebrar. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:35:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Quando o MDM/DWC rodam no HOST (fora do docker), os containers AIDA precisam de extra_hosts apontando para o gateway (host-gateway) para resolver o hostname do servidor WA. O doc oficial assume resolucao DNS; em lab com host-only, extra_hosts e necessario. O alias MDMHOST (ja usado no /etc/hosts do lab) resolve 127.0.0.1 no host. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 285. `hwa-lab-10.2.8-aida-oom-es-0063`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | ./AIDA.sh build-start; docker inspect aida-es --format '{{.State.ExitCode}} {{.State.OOMKilled}}'; sudo dmesg | grep -i oom |
| Pre-condicoes | docker-compose.yml com valores DEFAULT do pacote (es limits memory 8G, predictor 8G); Lab WSL2 com 11.5GiB RAM total |
| sanitized_output | aida-es entrava em Restarting com ExitCode=137 e OOMKilled=true (RestartCount 9). dmesg: 'Memory cgroup out of memory: Killed process (java) total-vm:5175364kB anon-rss:2089460kB' com limit do container es em 2G. Causa: OpenSearch 2.19.6 com heap default (metade do limite do cgroup) + Lucene mmap + Netty off-heap excediam o limite. Correcao no lab: (1) definir ES_JAVA_OPTS e OPENSEARCH_JAVA_OPTS=-Xms768m -Xmx768m; (2) elevar limits do es para 3G (reservation 1.5G); (3) reduzir limites de keycloak (1G), predictor (768M), ui (512M); (4) vm.max_map_count=262144 (era 65530). Apos ajustes: es Up estavel, exit=0, oom=false. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Restaurar docker-compose.yml.lab-bak e valores default. |
| Criterio de parada | Interromper se o lab travar por falta de memoria. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:30:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Em maquina com 11.5GiB de RAM, os limites default do compose (es 8G, predictor 8G) causam OOM. O minimo pratico no lab: es heap 768m + limit 3G; soma de reservas ~2.8GB. A doc oficial pede 32Gi/8Gi request p/ AIDA - inviavel em notebook; validacao lab usou valores reduzidos. OpenSearch tambem exige vm.max_map_count >= 262144 no host (sysctl persistido em /etc/sysctl.conf). [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 286. `hwa-lab-10.2.8-aida-rest-api-0074`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | token=$(curl -sk -X POST https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token -d 'grant_type=password' -d 'client_id=nginx' -d 'username=<aida-user>' -d 'password=<lab-password>'); curl -sk -H 'Authorization: Bearer $token' https://<host>:9432/api/<endpoint> |
| Pre-condicoes | AIDA rodando com Keycloak (realm aida); Usuario aidaadmin habilitado no realm; Client nginx (public) no realm aida |
| sanitized_output | API interna do AIDA descoberta via swagger (GET /api/swagger/ -> swagger-ui-init.js com spec OpenAPI 3.0, title 'AIDA', servers [/api]). 23 endpoints em 6 tags: KPIs (POST /kpi, POST /kpi/list, GET /kpi/category/list, PUT /kpi/updateAll); Alerts (POST /alert/definition/list, POST /alert/definition, PUT /alert/definition/update, PUT /alert/definition/updateAll, POST /alert/instance, POST /alert/instance/list, PUT /alert/instance/update); Metrics (POST /metric/instance/list); Special Days (POST /special-day/list, PUT /special-day/add, PUT /special-day/update, DELETE /special-day/delete, POST /special-day/holidays, GET /special-day/holidays/list); Actions (GET /actions/retrain, GET /actions/retrain/retrain-details, GET /actions/retrain/last-retrain); JWT (POST /jwt, GET /jwt/create-session). Schemas: SpecialDay, KPI, AlertDefinition, AlertInstance, MetricInstance, MetricDefinition, MetricProperties, MetricPropertiesInstance. Autenticacao: token Keycloak realm 'aida' (issuer https://<host>:9432/keycloak/auth/realms/aida), client publico 'nginx', usuarios do realm: aidaadmin (role aida-admin) e aidauser. Respostas reais: POST /api/kpi/list -> KPIs com last24hAlerts:0; GET /api/kpi/category/list -> Jobs(5)/Queue(1); POST /api/alert/instance/list -> count 0; GET /api/special-day/holidays/list -> feriados por pais (AO, AR, AW); GET /api/actions/retrain/last-retrain -> count false. O nginx valida o JWT (location /api/ faz discovery/introspection contra o Keycloak). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consultas HTTP autenticadas). |
| Criterio de parada | Interromper se o token nao for emitido ou as APIs retornarem 403 persistente. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| performed_at | 2026-08-25T15:00:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | A API interna do AIDA (sob /api) permite consultar KPIs, alertas, metricas, feriados e acionar retrain - tudo com token Keycloak (realm aida). Usuarios default do realm: aidaadmin (role aida-admin) e aidauser. O client 'nginx' e publico (sem secret). [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 287. `hwa-lab-10.2.8-aida-retrain-behavior-0076`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | POST /api/actions/retrain (token aidaadmin); GET /api/actions/retrain/retrain-details; GET aida-es:9200/predictions/_count |
| Pre-condicoes | AIDA rodando; Usuario aidaadmin autenticado (realm aida) |
| sanitized_output | POST /api/actions/retrain retorna {"result":true} (aceito). GET /api/actions/retrain/retrain-details retorna {"result":{"retrainProgress":false,"predictionsSubmited":0,"predictionsInProgress":0,"predictionsFailed":0}}. O indice predictions permanece com count=0 mesmo apos 90s do retrain. Diagnostico: com apenas ~1h de metricas coletadas (lab), o modelo prophet/neural nao tem serie temporal suficiente para gerar predicoes (DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180); o retrain e aceito mas nao produz predicoes ate haver historico minimo. O predictor (gunicorn, porta 5000) responde 'Prophet container.' e alcanca o OpenSearch (admin:admin -> 200). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consultas; retrain aceito mas sem efeito sem dados historicos). |
| Criterio de parada | Interromper se o retrain travar os containers. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsai_working_with_KPIs.html |
| performed_at | 2026-08-25T15:40:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | O retrain via API funciona (result:true) mas predicoes exigem serie temporal historica minima; no lab com poucos dados, predictions fica 0. O retrain automatico roda a cada 24h (doc oficial). Com dias de coleta de metricas, o fluxo de predicao deve gerar docs em predictions. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 288. `hwa-lab-10.2.8-aida-special-days-0073`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | GET aida-es:9200/special-days-labels/_search?size=3 |
| Pre-condicoes | AIDA rodando; OpenSearch populado |
| sanitized_output | Indice special-days-labels contem 95 docs com feriados por estado/regiao (schema: state (ex.: AO, AR, AW), names: [lista de nomes de feriados no idioma local, ex.: 'Ano novo', 'Carnaval', 'Dia Internacional da Mulher' para AO; 'Año Nuevo [New Year's Day]', 'Día de Carnaval' para AR; 'Aña Nobo [New Year's Day]', 'Dia Di Betico' para AW]). Usado pelo predictor para modelar sazonalidade de feriados. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (leitura do indice). |
| Criterio de parada | NA. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html |
| performed_at | 2026-08-25T14:46:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | special-days-labels alimenta o modelo de predicao com feriados (95 regioes/estados). [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 289. `hwa-lab-10.2.8-aida-tar-0061`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | Get-FileHash / sha256sum G:\HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz; tar -tzf | head; tar -xzf (docker-deployment + aida-images-hcl.tar.gz) |
| Pre-condicoes | Pacote HWA 10.2.8 Docker AIDA Linux x86_64 presente em G:; Docker 29.7.2 + Docker Compose v5.5.0 no WSL2 Ubuntu 22.04 |
| sanitized_output | SHA256 do tar.gz = facc5bf669d9d15399e3e56cbf5116361e5a28bd7208c0b368bfd4b37fd1d378; tamanho 1.915.102.598 bytes (~1.8 GB); 930 arquivos. Conteudo: aida-images-hcl.tar.gz (1.909.158.244 bytes, contem 9 imagens hclcr.io/wa/workload-automation/hcl-aida-*:10.2.8) + docker-deployment/ com AIDA.sh, docker-compose.yml, docker-compose.dev.yml, docker-compose.debug.yml, common.env, config/, nginx/cert/, redis/, keycloak/, Licenses/, ILMT/, hcl-readme/ e Dockerfiles por servico (ad, config, email, es, exporter, keycloak, nginx, orchestrator, predictor, redis, ui). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consulta/hash de arquivo; extração reversível por remocao de /opt/hwa/aida). |
| Criterio de parada | Interromper se o hash divergir do esperado ou a extracao falhar. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:20:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Estrutura do pacote AIDA 10.2.8: imagens pre-carregadas (aida-images-hcl.tar.gz) + docker-deployment. AIDA.sh oferece load/build/build-start/start/stop/restart/down/down-volumes/first-start/add-credentials/update-credentials/delete-credentials/set-custom-port/dump. Exige CONTAINER_RUNTIME=docker|podman. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 290. `hwa-lab-10.2.8-aida-ui-health-0068`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | curl -sk https://127.0.0.1:9432/ ; curl -sk https://127.0.0.1:9432/healthz ; GET aida-es:9200/_cluster/health |
| Pre-condicoes | AIDA build-start concluido (10 containers up); EXTERNAL_HOSTNAME=127.0.0.1 |
| sanitized_output | https://127.0.0.1:9432/ -> HTTP 200 (SPA React, title 'AI Data Advisor (AIDA)', manifest.json, main.bc059b31.js). /healthz -> 200. https://localhost:9432/ -> HTTP 405 'Host not matching, check the EXTERNAL_HOSTNAME environment variable'. Cluster OpenSearch: status yellow, 1 node (esperado p/ single-node lab). Containers: aida-nginx (0.0.0.0:9432->9432), aida-keycloak (8080/8443/9000), aida-es (9200/9300/9600), aida-ui (9000), aida-ad/predictor/email (5000), aida-redis (6379), aida-orchestrator, aida-exporter, aida-config (transiente). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consultas HTTP). |
| Criterio de parada | Interromper se a UI nao responder 200 em 127.0.0.1:9432. |
| evidence_url | https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation |
| performed_at | 2026-08-25T13:55:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | A UI do AIDA (https://<aida-ip>:9432) e acessivel via browser; o DWC (9443) e o MDM (31116) continuaram saudaveis durante todo o teste. No lab sem Keycloak configurado externamente, o acesso a UI e via widget de alerta no Workload Dashboard do DWC (Keycloak opcional habilita acesso direto). OpenSearch yellow em single-node e normal. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 291. `hwa-lab-10.2.8-bmdm-aes-keys-copied-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Apos instalar o BMDM, as chaves de criptografia AES do MDM foram copiadas de /opt/hwa/TWSDATA/ssl/aes (key.p12 + key.sth) do container tws-hwa para o mesmo caminho no tws-bmdm, permitindo ao BMDM descriptografar arquivos criptografados como o Symphony, conforme doc awspiinstallMDM/awspiinstallMDMasBKM.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T02:26:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | key.p12 (515 bytes) + key.sth copiados; ownership wauser:wauser em /opt/hwa/TWS/TWSDATA/ssl/aes. |
| observations | Chaves identicas entre MDM e BMDM: pre-requisito para leitura do Symphony no failover. |


---

### 292. `hwa-lab-10.2.8-bmdm-boot-restart-auto-0005`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8, o boot automatico do BMDM apos 'docker restart tws-bmdm' foi validado: as units systemd em cascata (tws-hosts-fix -> tebctl-tws_cpa_agent_wauser -> tws-domain-start) restauraram o BMDM sem intervencao manual. Pitfall descoberto: o bind mount /data (sdb) vinha como root:root e o 'su - wauser' falhava ao gravar /data/appserver-start.log (Permission denied), impedindo o engine de subir. Fix: chown wauser:wauser /data (persistente no sdb) + linha defensiva 'chown wauser:wauser /data' no inicio do tws-domain-start.sh. Apos o fix, o engine Liberty subiu (porta 31116), netman/batchman/JobManager ativos, e 'conman showcpus' no BMDM mostra MDM_BK como *UNIX FTA full-status linkado ao master (MDM UNIX MASTER), Batchman LIVES nos dois lados.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T04:50:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | systemctl: tws-hosts-fix active, tebctl active, tws-domain-start active. ss: 31116/31111/31113/31114 LISTEN. conman showcpus (tws-bmdm): MDM_BK *UNIX FTA LIMIT 10 I J M A; MDM UNIX MASTER LTI JW MDEA. |
| observations | Ownership do /data (bind mount root:root) e o unico ajuste necessario no boot do BMDM; documentado para replicacao. |


---

### 293. `hwa-lab-10.2.8-bmdm-container-install-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (host CachyOS), o Backup Master Domain Manager foi instalado em container proprio (tws-bmdm, RHEL 9.8 UBI-init, rede docker hwa-mesh 172.18.0.0/24, IP 172.18.0.11) apontando para o banco PostgreSQL JA EXISTENTE do MDM (172.18.0.10:5432/TWS, container tws-hwa). O serverinst.sh detectou o master existente e configurou automaticamente como BKM (WAINST054I Configuring BKM; WAINST023I completed successfully, rc=0), sem criar banco proprio. O PostgreSQL do MDM foi liberado para a rede (listen_addresses='*' + pg_hba com 172.18.0.0/24 e 172.17.0.0/16 scram-sha-256) e a senha do role postgres foi resetada para credencial dedicada (registrada em CREDENCIAIS-LAB.env fora do git).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm) + tws-hwa |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T02:25:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | WAINST062I Checking input / WAINST208I Checking WLP / WAINST060I Installing binaries / WAINST054I Configuring BKM / WAINST202I Configuring broker / WAINST200I Configuring WLP / WAINST201I Configuring data source / WAINST203I Configuring SFinal / WAINST0229I Importing certificates / WAINST061I post-config / WAINST023I completed successfully; SERVERINST_RC=0. |
| observations | Backup compartilha o MESMO banco TWS do master (sem banco proprio), conforme doc awspiinstallMDMasBKM. Container BMDM: /opt/hwa/TWS/TWS (binarios, UNISONHOME), /opt/hwa/TWS/TWSDATA (dados). |


---

### 294. `hwa-lab-10.2.8-bmdm-fta-fullstatus-in-plan-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio, a workstation do backup (MDM_BK) foi registrada no plano como FTA full-status autolink: composer display CPU=MDM_BK mostra TYPE FTA, AUTOLINK ON, FULLSTATUS ON, NODE tws-bmdm.lab TCPADDR 31111 SECUREADDR 31113. Apos 'JnextPlan -for 0000' no MDM (run #23), 'conman sc' passou a exibir MDM_BK como 'UNIX FTA' com o Symphony enviado ao BMDM (arquivo Symphony de 52.768 bytes presente em /opt/hwa/TWS/TWSDATA do tws-bmdm as 02:30).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T02:30:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | conman sc: MDM 23 *UNIX MASTER; MDM_BK 23 UNIX FTA LIMIT 10 LTI JW M A. No BMDM: 'conman showcpus' -> Batchman LIVES, plano #23, MDM_BK *UNIX FTA. |
| observations | FTA full-status autolink confirmado nos dois lados; BMDM enxerga todo o dominio e o Symphony sincronizado via banco compartilhado. |


---

### 295. `hwa-lab-10.2.8-bmdm-switchmgr-failover-e2e-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8, o failover manual MDM->BMDM foi validado de ponta a ponta: 'conman switchmgr MASTERDM;MDM_BK' (executado como wauser no master) retornou AWSBHU120I 'changed the domain manager from workstation MDM to workstation MDM_BK'. Apos a propagacao, 'conman showcpus' executado no novo master (tws-bmdm) mostrou MDM_BK como *UNIX MASTER com Batchman LIVES, e o antigo MDM convertido a UNIX FTA (LTI JW MDEA), com todos os membros do dominio (LABPOOL, MASTERAGENTS, MDMDA, MDMXA, MDM_DWB, MDM_BKA) visiveis. Comportamento confirma a doc awsrgswitchmgr: 'the old domain manager is converted to a fault-tolerant agent in the domain'.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | mutating |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-bmdm master temporario) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T02:32:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | AWSBHU120I switchmgr MASTERDM;MDM_BK -> domain manager changed MDM->MDM_BK. conman showcpus (tws-bmdm): MDM_BK 23 *UNIX MASTER; MDM 23 UNIX FTA. |
| observations | Reversivel: o MDM original retoma o papel de master no proximo JnextPlan ou via novo switchmgr. Teste concluido e master retornado ao MDM apos validacao. |


---

### 296. `hwa-lab-10.2.8-boot-auto-container-mdm-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, ubi9/ubi-init), o boot completo do dominio TWS apos docker restart foi automatizado com 3 units systemd: (1) tws-boot-fixes (oneshot, antes do tebctl) que reaplica 'loopback tws-hwa.lab' no /etc/hosts (docker regenera o hosts a cada start) e remove User=wauser/PIDFile= da unit tebctl se presentes; (2) tebctl-tws_cpa_agent_wauser (enabled) que sobe o agente ITA + JobManager; (3) tws-domain-start (oneshot apos o tebctl) que faz systemctl start postgresql-18 (unit disabled nao sobe sozinha), startAppServer.sh (engine Liberty, aguarda a porta do engine) e conman start&link + startmon (netman/batchman). ACHADO: a unit tebctl original instalada tinha User=wauser + Type=forking + PIDFile=status.info; como o script tebctl quando rodado como root ja faz su - wauser internamente e o status.info e gravado como wauser, o systemd recusava: 'New main PID N does not belong to service, and PID file is not owned by root. Refusing.' -> start falhava com timeout apos 5min. Remover User= e PIDFile= resolve (o script ja faz o su). Validacao: docker restart tws-hwa -> ~100s depois agent/JobManager/netman/java/mailman/batchman todos up, Batchman LIVES, plano dia vigente 00:05 BR preservado, FINAL 2359 agendado.

| Atributo | Valor |
| --- | --- |
| Resultado observado | apos docker restart: tws-boot-fixes active, tebctl active, tws-domain-start active; processos agent/JobManager/netman/java/mailman/batchman up; portas 31111/31114/5432 listening; Batchman LIVES Limit 10; hosts com tws-hwa.lab; unit tebctl sem User/PIDFile. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | medium |
| sanitized_output | 3 units (tws-boot-fixes, tebctl, tws-domain-start) sobem o dominio sozinho; achado: PIDFile nao-root recusado pelo systemd -> remover User=/PIDFile=; docker restart validado em ~100s |
| performed_at | 2026-09-05T23:32:11.386375-03:00 |
| performed_by | hermes-lab |


---

### 297. `hwa-lab-10.2.8-carryforward-0060`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `plan`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job stream defined with CARRYFORWARD was submitted and its instance was marked [Carry], confirming the carryforward attribute is recognized in the plan.

> **ATENCAO / RESSALVAS DE USO:** Carryforward carries an unfinished stream to the next plan. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sj CF_TEST

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Carryforward attribute |
| Citacao de suporte | CF_TEST SUCC [Carry]; CFJOB SUCC. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | carryforward |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['confirm', 'submit'], result=CF_TEST SUCC [Carry]; CFJOB SUCC. | Carryforward carries an unfinished stream to the next plan., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-carryforward.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=plan |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, a job stream defined with CARRYFORWARD was submitted and its instance was marked [Carry], confirming the carryforward attribute is recognized in the plan?


---

### 298. `hwa-lab-10.2.8-composer-syntax-slash-vs-multiline-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master), um experimento controlado de 6 variacoes determinou a sintaxe de entrada real do composer add: (1) $JOBS + linha com separador '/' entre keyword blocks falha com AWSJOM918E 'Syntax error at line 2, starting from position 9'; (2) linha solta com '/' sem $JOBS falha AWSBCZ021E; (3) linha unica sem '/' sem $JOBS falha AWSBCZ021E; (4) $JOBS + multilinha (JOBNAME na linha 1, keywords em linhas proprias) FUNCIONA (AWSJCL003I jd=...); (5) $JOBS + linha unica (JOBNAME DOCOMMAND ... STREAMLOGON ...) FUNCIONA; (6) SCHEDULE com jobs inline keyword-por-linha estilo Sfinal FUNCIONA (8 objetos). Conclusao: o separador '/' que aparece no composer display e o FORMATO DE SAIDA (serializacao), nao a sintaxe de entrada; o claim WSL composer-syntax-format-0104 que descreve o formato com '/' deve ser lido como representacao do display, com risco de AWSJOM918E se o '/' for copiado como entrada. Jobs inline dentro de SCHEDULE (como no Sfinal) criam as job definitions e o stream em um unico composer add.

| Atributo | Valor |
| --- | --- |
| Resultado observado | Matriz: / no input -> AWSJOM918E (header) / AWSBCZ021E (sem header); multilinha com $JOBS -> ok; linha unica com $JOBS -> ok; SCHEDULE inline estilo Sfinal -> ok (AWSBIA288I Total objects updated: 8). |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | AWSJOM918E com separador / | AWSBCZ021E sem header | multilinha+$JOBS OK | linha unica+$JOBS OK | SCHEDULE inline Sfinal OK (8 objetos) |
| performed_at | 2026-09-05T21:50:53.842799-03:00 |
| performed_by | hermes-lab |


---

### 299. `hwa-lab-10.2.8-configuredb-container-rhel9-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8 (UBI-init, Docker), configureDb.sh do HWA 10.2.8 completou com sucesso com PostgreSQL 18.6 (PGDG EL9), componente MDM, database TWS em loopback:5432, gerando os schemas HWA (mdl, dwb, evt, log, pln) identicos ao lab WSL2.

| Atributo | Valor |
| --- | --- |
| command | cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./configureDb.sh -f /installers/lab/configureDbPostgresql.properties |
| Pre-condicoes | HWA 10.2.8, kit MDM extraido no host (btrfs sdb) e montado em /installers; SO: Red Hat Enterprise Linux 9.8 (Plow) UBI-init, container Docker com systemd (CachyOS host); PostgreSQL 18.6 local PGDG EL9, role admin postgres com senha lab, pg_hba scram em loopback:5432; RDBMS_TYPE=POSTGRESQL, COMPONENT_TYPE=MDM, DB_NAME=TWS, DB_USER=postgres, EXEC_GENERATED_SQL=TRUE; hostname do container: tws-hwa.lab (sysctl kernel.hostname) |
| sanitized_output | WAINST093I Checking connection to the database TWS ... WAINST091I Check version. WAINST0534W The database TWS does not exist. It will be created. WAINST092I Update database. WAINST077I The database has been successfully created or updated. WAINST052I The command configureDb has completed successfully. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | DROP DATABASE TWS e reexecutar configureDb.sh |
| Criterio de parada | Interromper se a checagem de conexao falhar ou se o log apresentar erro de criacao de schema |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028 |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Validacao cross-plataforma da claim hwa-lab-10.2.8-postgresql-configuredb-0001 (lab WSL2 Ubuntu 22.04): mesmas mensagens WAINST077I/WAINST052I e mesmos schemas (mdl/dwb/evt/log/pln). Diferencas de ambiente: RHEL 9.8 + PGDG EL9 em vez de Ubuntu 22.04 + PGDG apt; execucao do kit via bind mount btrfs do host. PostgreSQL 18.6 idem lab WSL. |
| performed_at | 2026-09-04T18:50:27.906954-03:00 |


---

### 300. `hwa-lab-10.2.8-deps-chain-abend-rollover-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, fuso America/Sao_Paulo, dominio MDM master), um job stream complexo (MDM#CPLXCHAIN) com dependencias encadeadas e um job que falha foi definido via composer e submetido ad hoc com 'conman sbs = MDM#CPLXCHAIN;noask' (submit schedule; sbj e para JOB individual e retorna AWSBHU072E para stream). Comportamento observado: o job raiz CPJ_A SUCC rc0; o job CPJ_B (FOLLOWS CPJ_A, DOCOMMAND 'exit 5') foi ABEND rc5; o job CPJ_C (FOLLOWS CPJ_B) ficou HOLD (dependencia quebrada pelo ABEND); o ramo paralelo CPJ_D (FOLLOWS CPJ_A) e CPJ_E (FOLLOWS CPJ_D) executaram SUCC rc0, confirmando que dependencias FOLLOWS independntes nao bloqueiam a execucao paralela. O stream ficou STUCK enquanto havia ABEND; o rerun manual do job ABEND ('conman rr = MDM#CPLXCHAIN.CPJ_B;noask') re-executou CPJ_B que ABEND novamente (rc5); confirmar/cancelar o ABEND do CPJ_B liberou CPJ_C que rodou SUCC e o stream terminou SUCC. Estados coletados: READY, EXEC, SUCC, ABEND, HOLD, STUCK. Os jobs executaram nativamente no master MDM (via seu JobManager) - diferenca do WSL onde jobs em dynamic agent ficavam READY por dispatch.

| Atributo | Valor |
| --- | --- |
| Resultado observado | sj MDM#CPLXCHAIN mostrou: CPJ_A SUCC rc0, CPJ_B ABEND rc5 (original e rerun manual #J14421), CPJ_C HOLD depois SUCC apos liberar B, CPJ_D SUCC, CPJ_E SUCC; stream SUCC final. rr sem nome de job deu AWSBHU711E; rr com seletor completo forwarded to batchman. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | CPJ_A SUCC rc0 | CPJ_B ABEND rc5 | CPJ_C HOLD depois SUCC | CPJ_D SUCC | CPJ_E SUCC | stream STUCK depois SUCC | sbj->AWSBHU072E, sbs aceito, rr sem nome AWSBHU711E |
| performed_at | 2026-09-05T21:26:37.853584-03:00 |
| performed_by | hermes-lab |


---

### 301. `hwa-lab-10.2.8-dwc-cert-ca-attempt-0079`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | 1) openssl genrsa -out hwa-ca.key 4096; openssl req -x509 -new -key hwa-ca.key -sha256 -days 3650 -out hwa-ca.crt (CN=HWA-Lab-CA); 2) openssl genrsa -out dwc-server.key 2048; openssl req -new -key dwc-server.key -out dwc-server.csr (CN=localhost, SAN DNS:localhost,DNS:MDMHOST,IP:127.0.0.1); 3) openssl x509 -req -in dwc-server.csr -CA hwa-ca.crt -CAkey hwa-ca.key -CAcreateserial -out dwc-server.crt; 4) openssl pkcs12 -export -in dwc-server.crt -inkey dwc-server.key -out dwc-server.p12 -name default -passout pass:password; 5) cp dwc-server.p12 para TWSServerKeyFile.p12; 6) instalar hwa-ca.crt no Windows CurrentUser\Root; 7) atualizar DWC_PUBLIC_KEY no common.env do AIDA |
| Pre-condicoes | DWC 10.2.8 com keystore original (TWSServerKeyFile.p12, self-signed CN=HWA-LAB); senha do keystore cifrada {aes} no ssl_variables.xml (chave 1787657107) |
| sanitized_output | Tentativa de substituir o certificado self-signed do DWC por certificado assinado por CA criada no lab (HWA-Lab-CA): 1) CA e server cert criados e cadeia validada (openssl verify: OK); 2) novo keystore PKCS12 (senha 'password') instalado em TWSServerKeyFile.p12; 3) CA instalada no Windows trust store (CurrentUser\Root, thumbprint 12118045FF92DE1754BF664439BC035AEF0B4504); 4) DWC_PUBLIC_KEY do AIDA atualizado com o novo cert. RESULTADO: a cadeia do certificado apresentado validava (openssl s_client verify: OK) MAS o handshake TLS falhava com 'TLSv1.3 alert decode error / SSL routines::unexpected eof' e curl retornava 000; a porta 9443 abria (CWWKO0219I) mas nao completava o handshake. Tambem ocorreu CWPKI0033E (keystore password incorrect) ao manter a senha {aes} original com o novo keystore de senha 'password' - exigia atualizar o {aes} do keyStore (mantendo o do trustStore original, que tem senha propria). DIAGNOSTICO: o PKCS12 gerado por openssl e incompativel com o keystore que o Liberty/WebSphere espera (formato/atributos diferentes); a troca de certificado do DWC requer usar keytool (Java) para gerar o PKCS12 no formato Liberty ou regenerar via ssl_admin/regenServerKeyStore. AMBIENTE RESTAURADO: keystore original + ssl_variables.xml original restaurados; DWC login 200, MDM 200, AIDA 200, metricas continuaram coletando (2161). |
| Resultado observado | PARTIAL |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Restaurar TWSServerKeyFile.p12.bak + ssl_variables.xml original (executado; ambiente voltou 100%). |
| Criterio de parada | Interromper e restaurar se o DWC nao responder (handshake TLS falho). |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/tswebmst_welcome.html |
| performed_at | 2026-08-25T18:15:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | LICAO APRENDIDA: para trocar o certificado SSL do DWC (Liberty), usar keytool/Java para gerar o PKCS12 (nao openssl pkcs12). O keystore do Liberty requer formato especifico; openssl gera um p12 que valida a cadeia mas falha o handshake TLS. A senha do trustStore e DIFERENTE da do keyStore (ambas cifradas {aes} no ssl_variables.xml, chave 1787657107). O bloqueio do Kaspersky no navegador continua (certificado self-signed do lab), e a validacao visual do widget AIDA no Workload Dashboard requer certificado confiavel via keytool (pendente). [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 302. `hwa-lab-10.2.8-dwc-cert-keytool-0081`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | 1) openssl pkcs12 -export -in dwc-server.crt -inkey dwc-server.key -out dwc-server-openssl.p12 -name default -passout pass:password 2) keytool -importkeystore -srckeystore dwc-server-openssl.p12 -srcstoretype PKCS12 -srcstorepass password -destkeystore dwc-server-keytool.p12 -deststoretype PKCS12 -deststorepass password -srcalias default -destalias default 3) cp dwc-server-keytool.p12 TWSServerKeyFile.p12 4) atualizar ssl_variables.xml keyStore.password para {aes} de 'password' (manter trustStore original) 5) restart dwcServer |
| Pre-condicoes | DWC 10.2.8 com keystore original; Certificado assinado por HWA-Lab-CA (tentativa anterior, evidencia 0079); keytool disponivel (openjdk) |
| sanitized_output | Segunda tentativa de troca do certificado SSL do DWC, desta vez gerando o PKCS12 via keytool (conversao do openssl p12) para tentar o formato Liberty. O keystore keytool-gerado listava 1 entrada (alias 'default', PrivateKeyEntry, cadeia CA-signed SHA256withRSA valida). Instalado em TWSServerKeyFile.p12 + ssl_variables.xml com keyStore.password = {aes de 'password'} (ARDBIp67...) e trustStore original. RESULTADO: o Liberty NAO aceitou o alias - erro CWPKI0024E 'The server certificate alias specified by the attribute serverKeyAlias is either not found in KeyStore ... or it is invalid'; a porta 9443 abria (CWWKO0219I) mas o handshake TLS falhava; curl 000. O keystore original usa um alias que nao e 'default' (nao foi possivel listar sem a senha original, cifrada {aes} com chave 1787657107; a decifracao via PasswordCipherUtil exigiria classpath completo do Liberty). AMBIENTE RESTAURADO: keystore original + ssl_variables.xml original restaurados; DWC login 200. |
| Resultado observado | PARTIAL |
| Versao do produto | 10.2.8 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Restaurar TWSServerKeyFile.p12.bak + ssl_variables.xml original (executado; DWC voltou a 200). |
| Criterio de parada | Interromper e restaurar se o DWC nao responder (CWPKI0024E/Falha de handshake). |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/tswebmst_welcome.html |
| performed_at | 2026-08-25T17:40:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | LICOES DA 2ª TENTATIVA: (1) o formato openssl pkcs12 falha o handshake (decode error, evidencia 0079); (2) a conversao via keytool gera keystore valido que ainda falha com CWPKI0024E (alias inesperado) - o Liberty/DWC usa um serverKeyAlias especifico que nao e o 'default'; (3) para trocar o certificado do DWC corretamente, e preciso: decifrar a senha {aes} do keystore original (via Java com classpath completo do Liberty), listar o alias original, e REGERAR o keystore mantendo esse alias - ou usar o procedimento oficial do Liberty (ssl_admin / keytool com o alias correto). A troca de certificado do DWC em producao requer acesso ao procedimento oficial HCL de regeneracao de keystore; o metodo manual openssl/keytool com alias 'default' NAO funciona. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 303. `hwa-lab-10.2.8-dwc-configuredb-postgresql-0052`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | cd /root/hwa/dwc-extracted && umask 022 && ./configureDb.sh -f configureDbPostgresql.properties |
| Pre-condicoes | HWA 10.2.8.00, kit DWC extraido em /root/hwa/dwc-extracted; SO: Ubuntu 22.04 no WSL2; PostgreSQL 18 local em 127.0.0.1:5432 (role postgres admin, role postgresdwc criada); Certificados ca.crt/tls.key/tls.crt em /root/hwa/dwc-certs (ownership wauser, 644); umask 022; RDBMS_TYPE=POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC, DB_ADMIN_USER=postgres, DB_USER=postgresdwc |
| sanitized_output | WAINST0229I Importing certificates from <sslkeysfolder>. | WAINST093I Checking connection to the database TDWC on host <dbhost> on port 5432 with user postgres. | WAINST0534W The database TDWC does not exist. It will be created. | WAINST092I Update database. | WAINST077I The database has been successfully created or updated. | WAINST052I The command configureDb has completed successfully. Log: <workdir>/installation/logs/configureDb_10.2.8.00.log. Schemas criados: tdwc (48 tabelas), fed (7 tabelas, Federator). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | destructive |
| Reversibilidade | DROP DATABASE TDWC e recriacao via configureDb.sh; em lab o banco e descartavel. |
| Criterio de parada | Interromper se configureDb.sh falhar na conexao (DB_ADMIN_USER sem permissao) ou reportar erro de SQL aplicado. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstdbcfg.html |
| performed_at | 2026-08-25T08:23:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Para POSTGRESQL o rc=6 do dbTool (banco inexistente) e tratado como condicao normal de criacao; o banco e criado automaticamente. DWC database default e TDWC (nao DWC) nas properties do kit 10.2.8. Federator (schema fed) criado junto desde 10.2.3. |


---

### 304. `hwa-lab-10.2.8-dwc-configuredb-rhel9-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8 (UBI-init), configureDb.sh do kit DWC HWA 10.2.8 completou com sucesso com PostgreSQL 18.6: componente DWC, database TDWC criado (WAINST077I/052I), role dedicada postgresdwc como DB_USER - replicando o lab WSL2 (evidencia dwc-configuredb-postgresql-0052).

| Atributo | Valor |
| --- | --- |
| command | cd /installers/dwc-extracted && umask 022 && ./configureDb.sh -f /installers/lab/dwc-configureDbPostgresql.properties |
| Pre-condicoes | HWA 10.2.8, kit DWC extraido (raiz do kit tem configureDb.sh proprio, distinto do kit MDM); SO: container RHEL 9.8 UBI-init (Docker), CachyOS host; PostgreSQL 18.6 PGDG EL9, role admin postgres + role postgresdwc criada (LOGIN PASSWORD) antes do configureDb; RDBMS_TYPE=POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC, DB_ADMIN_USER=postgres, DB_USER=postgresdwc, loopback:5432 |
| sanitized_output | WAINST093I Checking connection to the database TDWC ... WAINST091I Check version. WAINST0534W The database TDWC does not exist. It will be created. WAINST092I Update database. WAINST077I The database has been successfully created or updated. WAINST052I The command configureDb has completed successfully. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | DROP DATABASE TDWC e reexecutar configureDb do DWC |
| Criterio de parada | Interromper se a conexao falhar ou erro de schema |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Cross-plataforma da evidencia WSL2 0052. Database default do DWC 10.2.8 e TDWC (nao DWC). Diferente do MDM, o rc=6 do dbTool (banco inexistente) relatado no WSL nao apareceu como condicao no log - fluxo direto de criacao. dwcinst.sh lancado em sequencia. |
| performed_at | 2026-09-04T19:33:37.042596-03:00 |


---

### 305. `hwa-lab-10.2.8-dwc-default-tasks-http-0060`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | 1) login como novo usuario via curl (POST /console/j_security_check + Accept-Language en-US) 2) GET /console/ e probes de endpoints REST (dwc/api/v1/task, dwc/rest/task/list, etc.) 3) SELECT username, count(*) FROM tdwc.tdwc_querytask GROUP BY username |
| Pre-condicoes | Novo usuario DWC criado e autenticado (evidencia 0059); Servidor DWC ativo e banco TDWC acessivel |
| sanitized_output | Apos login HTTP puro (curl) e acesso ao console/ via HTTP, o banco tdwc.tdwc_querytask NAO contem default tasks para o novo usuario (wauser=21 tasks, <dwc-user>=0). O usuario original wauser tem 21 default tasks (nomes em ingles: 'All Critical Jobs in plan (Distributed)', 'All Jobs in plan (zOS)', etc.). Probes de endpoints REST de task retornaram 404/400 (nao encontrados via HTTP puro). Conclusao laboratorial: a criacao das default tasks NAO e disparada pelo POST de login HTTP — requer sessao interativa da UI (SPA/JS) no primeiro login. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consulta read-only ao banco e probes HTTP). |
| Criterio de parada | Interromper se o servidor nao responder ou se a consulta ao banco falhar. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrdefaulttasks.html |
| performed_at | 2026-08-25T12:20:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Descoberta lab complementar a claim hwa-10.2.8-dwc-default-tasks-language-0002: o primeiro login 'com navegador' do doc oficial deve ser uma sessao interativa (UI), nao um POST HTTP puro. Nao contradiz a claim; refina o entendimento de quando as default tasks sao criadas. Vale revalidacao com navegador real (ex.: via CDP/Playwright) antes de generalizar. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 306. `hwa-lab-10.2.8-dwc-default-tasks-language-0058`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | webfetch https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrdefaulttasks.html (Troubleshooting: Default tasks are not converted into the language set in the browser) |
| Pre-condicoes | Usuario DWC existente que fez o primeiro login com navegador em um idioma X; Default/predefined tasks criadas nesse primeiro login no idioma X |
| sanitized_output | Doc oficial 10.2.8: 'The default tasks are created, using the current language set in the browser, when the new user logs into the Dynamic Workload Console for the first time... To have the default tasks translated into a different language, the WebSphere Application Server Liberty Base administrator must create a new Dynamic Workload Console user, and use that to login to the Dynamic Workload Console for the first time using a browser configured with the requested language.' Ou seja: trocar o idioma do navegador depois NAO traduz as default tasks ja criadas. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consulta documental). |
| Criterio de parada | NA. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrdefaulttasks.html |
| performed_at | 2026-08-25T11:25:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Complementa a evidencia 0057: a UI segue o navegador, mas as default tasks ficam congeladas no idioma do PRIMEIRO login do usuario. Solucao oficial: criar novo usuario DWC e fazer o primeiro login dele com navegador no idioma desejado. A propriedade precannedTaskCreation do TdwcGlobalSettings.xml controla SE/QUAIS tasks sao criadas (all|none|distributed|zos) e e lida apenas no primeiro login. [Fonte oficial HCL 10.2.8] |
| evidence_source_type | official_documentation |


---

### 307. `hwa-lab-10.2.8-dwc-dwcinst-success-0053`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | cd /root/hwa/dwc-extracted && umask 022 && ./dwcinst.sh -f dwcinst.properties |
| Pre-condicoes | HWA 10.2.8.00, kit DWC extraido; Open Liberty 26.0.0.3 em /opt/liberty/wlp (--wlpdir obrigatorio); Banco TDWC criado e populado por configureDb.sh (passo anterior); DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp; ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DB_USER=postgresdwc; Usuario admin DWC (wauser) existente no SO; SSL_KEY_FOLDER=/root/hwa/dwc-certs, SSL_PASSWORD=<lab>; START_WLP=false (inicio manual pos-instalacao); umask 022 |
| sanitized_output | WAINST208I Checking WLP. | WAINST204I Installing installation tools. | WAINST053I Installing java. | WAINST206I Installing Jdbc drivers. | WAINST536I Installing Db Tools. | WAINST207I Installing WLP profile. | WAINST200I Configuring WLP. | WAINST201I Configuring data source. | WAINST0229I Importing certificates from <sslkeysfolder>. | WAINST0520I FIPS mode is not enabled in your environment. | WAINST055I Updating registry. | WAINST023I The installation has completed successfully. | WAINST006I Browse to this URL with a browser: https://<host>:9443/console/login.jsp | User : dwcadmin. Log: <DWC_DATA>/installation/logs/dwcinst_10.2.8.00.log. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | destructive |
| Reversibilidade | Executar o uninstaller do DWC e remover DWC_INST_DIR; em lab o diretorio e descartavel. |
| Criterio de parada | Interromper se o prereq check falhar (SKIPCHECKPREREQ=false), se o datasource nao conectar ao banco ou se o certificado for rejeitado. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html |
| performed_at | 2026-08-25T08:25:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | WLP_USER_DIR=${DWC_INST_DIR}/usr (dwcServer em /opt/hwa/DWC/usr/servers, nao no usr do Liberty). Registro via twaregistry.sh em /opt/hwa/Registry (build 10.2.8.00-2026.07). Datasource jdbc/dwcdb -> jdbc:postgresql://<dbhost>:5432/TDWC; senhas {aes} com chave do passphrase_variables.xml. |


---

### 308. `hwa-lab-10.2.8-dwc-engine-connection-rest-0055`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | curl -sk -b <cookies> -X POST -H 'Content-Type: application/json' -d '{"name":"MDM_LAB","type":"TWS","hostname":"MDMHOST","port":31116,"remoteServerName":"MDM","credentials":{"user":"wauser","password":"<lab>"},"showInDashboard":true}' https://<host>:9443/dwc/api/v1/engine/create && curl -sk -b <cookies> https://<host>:9443/dwc/api/v1/engine/1/checkConnection && curl -sk -b <cookies> https://<host>:9443/dwc/api/v1/engine/1/info |
| Pre-condicoes | DWC 10.2.8.00 instalado; sessao autenticada (cookies LtpaToken2); Engine MDM acessivel: engineServer iniciado, https://MDMHOST:31116/twsd/ responde 200; MDMHOST resolvido no /etc/hosts do host do DWC (127.0.0.1 MDMHOST); Credenciais de engine validas (wauser) |
| sanitized_output | POST /dwc/api/v1/engine/create -> HTTP 200 {"successful":true,"message":"MDM_LAB created successfully."} | GET /dwc/api/v1/engine/1/checkConnection -> HTTP 200 {"successful":true,"message":"Connection to MDM_LAB: successful."} | GET /dwc/api/v1/engine/1/info -> HTTP 200 (NAME MDM_LAB, TYPE maestro, HOST MDMHOST, PORT 31116). Persistencia: tdwc_engineconnection id=1 (enginetype=2), tdwc_credential, tdwc_preferenceable (preferencetype=3). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | DELETE /dwc/api/v1/engine/{engine_id} remove a conexao. |
| Criterio de parada | Interromper se create retornar erro de schema/FK ou se checkConnection falhar (engine inacessivel). |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/mng_eng_c.html |
| performed_at | 2026-08-25T08:48:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | engine_id e NUMERICO (id da tabela), nao o nome - usar /1 em vez de /MDM_LAB (nome causa NumberFormatException em EngineAppService.findEngine). checkConnection e GET (POST -> 405). GET /list retorna items vazio no lab mesmo com engine criada (filtros dashboard/SSC). |


---

### 309. `hwa-lab-10.2.8-dwc-engine-server-31116-0056`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | su - wauser -c 'cd /opt/hwa/appservertools && ./startAppServer.sh' && curl -sk -o /dev/null -w '%{http_code}' https://MDMHOST:31116/twsd/ |
| Pre-condicoes | MDM 10.2.8.00 instalado (serverinst) em /opt/hwa; engineServer (Open Liberty do MDM) com WLP_USER_DIR=/opt/hwa/usr, WLP_OUTPUT_DIR=/opt/hwa/TWSDATA/stdlist/appserver; Alias MDMHOST no /etc/hosts do host do DWC; Porta HTTPS 31116 (REST API V2 /twsd) |
| sanitized_output | AWSBHU620I A start command was issued for the application server on workstation "MDM". | Portas: 31116 LISTEN (java engineServer). | curl -k https://MDMHOST:31116/twsd/ -> HTTP 200 | GET /twsd/api/v2/model/jobdefinition (basic auth) -> HTTP 200. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | stopAppServer.sh para o engineServer; inicio e reversivel. |
| Criterio de parada | Interromper se o engineServer nao subir (log de erro no WLP_OUTPUT_DIR) ou a porta 31116 nao abrir. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html |
| performed_at | 2026-08-25T08:41:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | A REST API V2 em /twsd:31116 e servida pelo engineServer (Liberty do MDM), nao por processo separado; com o engineServer parado a porta 31116 nao responde (curl 000) e o checkConnection do DWC falha. O alias MDMHOST foi adicionado ao /etc/hosts (127.0.0.1 MDMHOST) para resolucao no host do DWC. |


---

### 310. `hwa-lab-10.2.8-dwc-login-requires-browser-headers-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

O login do console DWC 10.2.8 via POST /console/j_security_check retorna 400 silencioso (sem log no Liberty) quando o request nao carrega headers de browser (User-Agent Mozilla + Origin + Referer da pagina de login); com os headers, o POST retorna 302 e o LtpaToken2 e emitido - protecao do form login contra requests sem origem.

| Atributo | Valor |
| --- | --- |
| command | curl -sk -c cookies https://HOST:9443/console/ && curl -sk -b cookies -c cookies -H 'User-Agent: Mozilla/5.0' -H 'Origin: https://HOST:9443' -H 'Referer: https://HOST:9443/console/login.jsp' --data-urlencode 'j_username=dwcadmin' --data-urlencode 'j_password [REDACTED]' -o /dev/null -w '%{http_code}' https://HOST:9443/console/j_security_check && curl -sk -b cookies -o /dev/null -w '%{http_code}' https://HOST:9443/console/ |
| Pre-condicoes | DWC 10.2.8 instalado (dwcinst OK) e dwcServer rodando em container RHEL 9.8; Usuario admin dwcadmin com senha {aes} (wauser_variables.xml + passphrase_variables.xml com wlp.password.encryption.key); Fluxo: GET em URL protegida (gera cookie WASReqURL) -> POST j_security_check -> GET /console/; curl SEM headers de browser: POST retorna 400 com corpo vazio e Connection: Close, sem nenhuma entrada em messages.log/trace.log |
| sanitized_output | Sem headers: POST j_security_check -> HTTP 400 (corpo vazio). Com headers (UA Mozilla + Origin + Referer): POST -> HTTP 302 (redirect /console/) + Set-Cookie LtpaToken2; GET /console/ -> HTTP 200 com o dashboard. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | credential_sensitive |
| Reversibilidade | NA (login nao-destrutivo); logout via /console/logout |
| Criterio de parada | Interromper se o POST retornar algo alem de 302 com os headers corretos |
| performed_by | hermes-lab (container tws-hwa) |
| observations | A evidencia do lab WSL (dwc-login-wauser-0054) documentou o fluxo curl basico sem mencionar headers; neste container o request sem headers de browser e rejeitado com 400 antes do handler de autenticacao (nenhum CWWKS de falha registrado). Provavel protecao do form login do Liberty (webAppSecurity) contra CSRF/requests sem origem. O cookie WASReqURL e emitido no GET de URL protegida. Login validado com dashboard HTTP 200. |
| performed_at | 2026-09-04T19:46:26.897476-03:00 |


---

### 311. `hwa-lab-10.2.8-dwc-login-wauser-0054`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | curl -sk -c <cookies> https://<host>:9443/console/login.jsp && curl -sk -b <cookies> -d 'j_username=wauser&j_password=<lab>' https://<host>:9443/console/j_security_check && curl -sk -b <cookies> https://<host>:9443/console/ |
| Pre-condicoes | DWC 10.2.8.00 instalado e dwcServer iniciado (appservertools/startAppServer.sh); Usuario admin DWC = wauser (troca pos-instalacao: wauser_variables.xml user.twsuser.id/password {aes}, WA_USER=wauser, chown); HTTPS 9443 acessivel; Senha {aes} gerada com securityUtility encode --encoding=aes --key=<chave passphrase_variables.xml> |
| sanitized_output | POST /console/j_security_check -> HTTP 302 (Location: https://<host>:9443/console/) | Set-Cookie: LtpaToken2=... | GET /console/ -> HTTP 200 | messages.log: [dashboard/index.jsp] Initialization successful. Realm TWSRealm (basicRegistry), grupo Admins via admin.group.name. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | credential_sensitive |
| Reversibilidade | NA (login e nao-destrutivo). |
| Criterio de parada | Interromper se o POST retornar 400 (form invalido) ou se o login falhar com credenciais corretas. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/mng_eng_c.html |
| performed_at | 2026-08-25T08:38:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Login usa form padrao do Liberty (j_security_check), nao endpoint REST proprio. A senha {aes} foi validada por round-trip com PasswordCipherUtil.decipher (valor esperado retornado). Usuarios adicionais podem ser declarados em authentication_config.xml. |


---

### 312. `hwa-lab-10.2.8-dwc-ui-language-acceptlang-0057`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | curl -sk -H 'Accept-Language: pt-BR,pt;q=0.9' https://<host>:9443/console/login.jsp -o /tmp/lg-pt.html && curl -sk -H 'Accept-Language: en-US,en;q=0.9' https://<host>:9443/console/login.jsp -o /tmp/lg-en.html && diff /tmp/lg-pt.html /tmp/lg-en.html |
| Pre-condicoes | DWC 10.2.8.00 instalado e dwcServer ativo (HTTPS 9443); Kit com locales Console.war/locale/{en,pt-br,...}.json (14 idiomas); Nenhum seletor de idioma no login page |
| sanitized_output | Ambas as paginas tem <html lang="en"> fixo, mas os TEXTOS diferem conforme Accept-Language: pt-BR -> 'Erro:', 'credencial incorreta', 'Nome de Usuario'; en-US -> 'Error:', 'Wrong credential', 'Username'. TdwcGlobalSettings.xml nao possui propriedade de idioma (pagina oficial Customizing your global settings lista apenas videos, graphViews, precannedTaskCreation, user registry, timeouts etc.). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | read_only |
| Reversibilidade | NA (consulta read-only; basta reverter o header/idioma do navegador). |
| Criterio de parada | Interromper se as paginas forem identicas (idioma nao reagiria ao header) ou se o servidor nao responder. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/awsadglobsetcustom.html |
| performed_at | 2026-08-25T11:20:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | O idioma da interface do DWC segue o idioma do navegador (header HTTP Accept-Language), nao configuracao de servidor. Para mudar de portugues para ingles: configurar o navegador para ingles e refazer login. Kit suporta 14 idiomas em Console.war/locale/. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 313. `hwa-lab-10.2.8-dwc-wauser-en-login-0059`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

| Atributo | Valor |
| --- | --- |
| command | 1) securityUtility encode --encoding=aes --key=<chave-lab> <lab-password> 2) adicionar <user> no basicRegistry (authentication_config.xml) com password {aes} e como member do grupo Admins 3) stopAppServer.sh && startAppServer.sh 4) curl -sk -c sess.txt https://<host>:9443/console/login.jsp -o /dev/null 5) curl -sk -b sess.txt -c sess.txt -H 'Accept-Language: en-US,en;q=0.9' --data 'j_username=<dwc-user>' --data 'j_password=<lab-password>' https://<host>:9443/console/j_security_check |
| Pre-condicoes | DWC 10.2.8.00 instalado e dwcServer ativo (HTTPS 9443); authentication_config.xml com basicRegistry realm=TWSRealm e grupo Admins; securityUtility do Liberty (/opt/liberty/wlp/bin) com a mesma chave aes usada na instalacao |
| sanitized_output | Novo usuario administrativo criado no basicRegistry com senha {aes} re-gerada (mesma chave da instalacao) e adicionado ao grupo Admins; servidor reiniciado (dwcServer started). Login via POST /console/j_security_check com Accept-Language en-US -> HTTP 302 + cookie LtpaToken2 emitido; GET /console/ -> HTTP 200 com UI em ingles (login page mostra 'Username', dashboard mostra 'Workload dashboard'). O login page com en-US exibe 'Username' (vs 'Nome de Usuario' com pt-BR), confirmando que a UI segue o Accept-Language do navegador para o novo usuario. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed (Linux/WSL2) |
| Classificacao de risco | mutating |
| Reversibilidade | Remover o <user> do basicRegistry e do grupo Admins em authentication_config.xml e reiniciar o dwcServer. |
| Criterio de parada | Interromper se o login nao retornar 302 + LtpaToken2 ou se a UI nao responder 200. |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/awsadglobsetcustom.html |
| performed_at | 2026-08-25T12:10:00-03:00 |
| performed_by | operador do laboratorio WSL2 (HWA/TWS dataset) |
| observations | Opcao A do runbook P32b: criar novo usuario DWC com primeiro login em ingles funciona — login OK e UI carrega em ingles. Confirma a claim hwa-10.2.8-dwc-ui-language-0001 para um segundo usuario, alem do wauser original. [Observado em laboratorio HWA 10.2.8 WSL2] |


---

### 314. `hwa-lab-10.2.8-dwcinst-full-success-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8, o dwcinst.sh do DWC HWA 10.2.8 completou (WAINST023I) com PostgreSQL 18.6: dwcServer Liberty em /opt/hwa/DWC/usr/servers, console HTTPS 9443, admin dwcadmin, registry TWSRealm - replicando o lab WSL2 (evidencia dwc-dwcinst-success-0053). Requisitos adicionais: DWC_ADMIN_USER/DWC_ADMIN_PW obrigatorios no properties e usuario SO do admin deve existir (startAppServer exige o owner).

| Atributo | Valor |
| --- | --- |
| command | cd /installers/dwc-extracted && umask 022 && ./dwcinst.sh -f /installers/lab/dwcinst.properties && useradd -m -s /bin/bash dwcadmin && chown -R dwcadmin:dwcadmin /opt/hwa/DWC && su - dwcadmin -c 'cd /opt/hwa/DWC/appservertools && ./startAppServer.sh' |
| Pre-condicoes | HWA 10.2.8, kit DWC extraido (configureDb.sh do DWC ja executado: DB TDWC + role postgresdwc); SO: container RHEL 9.8 UBI-init (Docker); dwcinst.properties: ACCEPTLICENSE=yes, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp, RDBMS_TYPE=POSTGRESQL, DB TDWC, DWC_ADMIN_USER=dwcadmin, DWC_ADMIN_PW=<lab>, SSL_KEY_FOLDER=/opt/ssl-certs, START_WLP=false; Open Liberty (mesmo do MDM) em /opt/liberty/wlp, certs lab em /opt/ssl-certs |
| sanitized_output | dwcinst: WAINST200I Configuring WLP. WAINST201I Configuring data source. WAINST0229I Importing certificates. WAINST055I Updating registry. WAINST023I The installation has completed successfully. Browse to: https://tws-hwa.lab:9443/console/login.jsp User: dwcadmin. startAppServer: Server dwcServer started with process ID. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | Parar dwcServer (stopAppServer.sh) e reinstalar DWC |
| Criterio de parada | Interromper se dwcinst falhar (WAINST024E sem DWC_ADMIN_PW) ou o servidor nao subir |
| performed_by | hermes-lab (container tws-hwa) |
| observations | 1a execucao falhou com WAINST024E (--password obrigatorio) porque o dwcinst.properties nao tinha DWC_ADMIN_USER/DWC_ADMIN_PW (campos existem no template do kit). O dwcinst NAO cria o usuario SO do admin: startAppServer.sh como wauser falhou ('only the owner dwcadmin can run'); criado useradd dwcadmin + chown -R do DWC_INST_DIR. DWC instalado ao lado do MDM 10.2.8 (mesmo container, mesmo Liberty, mesmo PostgreSQL). |
| performed_at | 2026-09-04T19:45:50.540410-03:00 |


---

### 315. `hwa-lab-10.2.8-dynamic-dispatch-diagnosis-0016`

**Nivel de evidencia:** NAO CLASSIFICADO (tratar com cautela; nao afirmar como fato do produto)

**Afirmacao / Conteudo:**

In the HWA 10.2.8 laboratory, the MDMDA dynamic agent was linked and reported resource information to the engine, but submitted test streams remained READY and JobManager recorded no job execution request during observation; dynamic-agent execution is unresolved.

> **ATENCAO / RESSALVAS DE USO:** The initial AWKRRP086E_DOMAIN_NOT_CREATED error was later followed by successful resource registration. No successful job log or return code was observed.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | insufficient_evidence |
| Confianca | high |
| Fonte (URL) | local execution: /opt/hwa/TWSDATA/stdlist/JM/JobManager_message.log and conman showcpus |
| Titulo da fonte | Dynamic-agent dispatch diagnosis |
| Citacao de suporte | AWSITA083I Resource information was sent ...; conman showjobs displayed the submitted MDMDA streams in READY. |
| Coletado em | 2026-08-17 |


---

### 316. `hwa-lab-10.2.8-dynamic-pool-workstation-e2e-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), a criacao, configuracao e execucao de jobs em Dynamic Pools (workstations do tipo POOL sob BROKER) foi validada de ponta a ponta. Descobertas arquiteturais e comportamentais comprovadas: (1) Para criar uma workstation POOL no composer (TYPE POOL), a clausula FOR MAESTRO HOST deve apontar obrigatoriamente para uma workstation do tipo BROKER (ex: MDM_DWB); tentar apontar para o MDM (tipo MANAGER) falha com AWSJCO049E ('The host supplied cannot be used because it must be a workstation of type broker'). (2) A definicao correta no composer consiste em: 'CPUNAME <NOME> DESCRIPTION ... OS OTHER FOR MAESTRO HOST MDM_DWB TYPE POOL MEMBERS <DYNAMIC_AGENT> END'. Criou-se a workstation LABPOOL com membro MDMDA (AWSJCL003I). (3) O scheduler aloca automaticamente jobs agendados na workstation virtual LABPOOL para membros ativos do pool (execucao em MDMDA com tag {MDMDA} registrada no plano). (4) Foi validado o fluxo E2E: definicao de stream LABPOOL#POOL_STREAM com job LABPOOL#POOL_JOB -> adicao no composer -> submissao no plano via conman sbs (0AAAAAAAAAAAAAET) -> liberacao de LIMIT da CPU (lc LABPOOL;10;noask) -> execucao bem-sucedida em MDMDA com SUCC rc 0 (#J1045913938).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - Workstation POOL (LABPOOL) criada sob BROKER MDM_DWB, erro AWSJCO049E documentado ao tentar usar MANAGER, stream submetida e executada em MDMDA com SUCC rc 0. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | composer add LABPOOL (TYPE POOL FOR MAESTRO HOST MDM_DWB MEMBERS MDMDA); AWSJCO049E if host=MDM; sbs LABPOOL#POOL_STREAM; lc LABPOOL;10; POOL_JOB SUCC rc 0 #J1045913938 {MDMDA} |
| performed_at | 2026-09-08T12:43:50.552446-03:00 |
| performed_by | hermes-lab |


---

### 317. `hwa-lab-10.2.8-edwa-event-rule-e2e-container-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master, enEventDrivenWorkloadAutomation=YES, deploymentFrequency=5), o fluxo EDWA (event rule) foi validado de ponta a ponta. Uma event rule 'LAB_EVT_SBS' (ruleType=filter, isDraft=no, eventCondition GenericEventPlugIn eventType=Event1 com filtros Param1=TRIGGER_LAB e Workstation=MDM, acao TWSAction actionType=sbs) foi criada via composer XML (validate AWSBIA302I 'No errors', add AWSJCL003I erule=LAB_EVT_SBS) e ativou automaticamente em ~5min (deploymentFrequency) ficando 'active'. O comando 'sendevent Event1 GenericEventPlugIn Param1=TRIGGER_LAB Workstation=MDM' retornou AWSGTW113I e a acao sbs submeteu o job stream MDM#EVTJS_TEST no plano, que executou SUCC (EVTJOB1 SUCC rc0 #J12318 as 00:42 de 09/06) - prova de que a event rule acionou o submit (nao houve JnextPlan/sbs manual). Descobertas de sintaxe do XML da rule (AWSVAL): o parametro da acao TWSAction sbs e 'JobStreamName' (nome) + 'JobStreamWorkstationName' (workstation) - 'JobStream' nao e valido (AWSVAL005E); o eventType deve ser o definido no GenericEventPlugIn ('Event1', nao nome arbitrario - AWSVAL011E); Workstation do Event1 nao aceita wildcard (AWSVAL021E, wildcardAllowed=false). Ativacao via REST PUT /twsd/eventrule/deployment/rule_builder/start retornou HTTP 401 (exige autenticacao), por isso usou-se a ativacao automatica por deploymentFrequency.

| Atributo | Valor |
| --- | --- |
| Resultado observado | event rule LAB_EVT_SBS criada (activation pending -> active em ~5min); sendevent Event1 -> AWSGTW113I -> MDM#EVTJS_TEST submetido -> EVTJOB1 SUCC rc0 #J12318 (00:42 09/06); XML validado com AWSBIA302I No errors. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | event rule LAB_EVT_SBS filter Event1 -> active; sendevent -> AWSGTW113I -> sbs submeteu EVTJS_TEST -> EVTJOB1 SUCC rc0; params corretos JobStreamName+JobStreamWorkstationName; Workstation sem wildcard |
| performed_at | 2026-09-06T00:43:07.117159-03:00 |
| performed_by | hermes-lab |


---

### 318. `hwa-lab-10.2.8-edwa-twsobjectmonitor-jobstatuschanged-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), o provedor de eventos TWSObjectsMonitor foi validado com o evento JobStatusChanged e a acao MessageLogger (MSGLOG). Descobertas criticas de sintaxe e validacao: (1) O evento JobStatusChanged monitora mudancas de estado de jobs (JobName, Workstation, Status='Successful'). O atributo Status exige valor capitalizado ('Successful', e nao SUCC). (2) A acao MessageLogger (MSGLOG) exige obrigatoriamente o parametro 'ObjectKey' (omitir causa AWSVAL006E 'The mandatory parameter ObjectKey is not specified'). (3) O atributo 'Severity' da acao MSGLOG aceita valores como 'Info', 'Warning' e 'Error'; informar 'Information' e rejeitado com AWSVAL018E. A regra LAB_STATUS_RULE foi validada e adicionada com sucesso no composer (AWSJCL003I).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - Regra LAB_STATUS_RULE adicionada no composer; erros de validacao AWSVAL006E (ObjectKey obrigatorio) e AWSVAL018E (Severity aceita Info, rejeita Information) documentados. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | composer add lab_status_rule.xml; AWSVAL006E ObjectKey mandatory; AWSVAL018E Severity Info valid; AWSJCL003I add erule=LAB_STATUS_RULE completed |
| performed_at | 2026-09-08T13:52:37.674165-03:00 |
| performed_by | hermes-lab |


---

### 319. `hwa-lab-10.2.8-final-cycle-d1-rollover-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, RHEL9 UBI9, timezone America/Sao_Paulo), o ciclo FINAL de virada de plano (Sfinal) executou de ponta a ponta com sucesso: MDMXA#FINAL (2359 09/04 carry) executou STARTAPPSERVER->MAKEPLAN->SWITCHPLAN todos SUCC rc0, e o MDMXA#FINALPOSTREPORTS executou CHECKSYNC->CREATEPOSTREPORTS->UPDATESTATS todos SUCC rc0, gerando e ativando o plano de D+1 e instanciando automaticamente o proximo MDMXA#FINAL (2359 09/05) HOLD no schedule. Apos a virada, o plano de producao estendeu para o dia seguinte e o FINAL de hoje ficou agendado 23:59 pronto para rodar e gerar D+1 novamente - corrente auto-sustentavel de planos (dia vigente + D+1). Limit das workstations MDM/MDMXA precisou ser 10 (lc MDM;10;noask) para os jobs executarem.

| Atributo | Valor |
| --- | --- |
| Resultado observado | sj @#@FINAL@ mostrou FINAL 09/04 SUCC (STARTAPPSERVER #J9311 rc0, MAKEPLAN #J9460 rc0, SWITCHPLAN #J9614 rc0) e FINALPOSTREPORTS 09/04 SUCC (CHECKSYNC #J9813, CREATEPOSTREPORTS #J9814, UPDATESTATS #J10105 todos rc0); plano estendido; novo FINAL 09/05 23:59 HOLD agendado. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | FINAL 09/04: STARTAPPSERVER SUCC rc0, MAKEPLAN SUCC rc0, SWITCHPLAN SUCC rc0 | FINALPOSTREPORTS 09/04: CHECKSYNC SUCC, CREATEPOSTREPORTS SUCC, UPDATESTATS SUCC | novo FINAL 2359 09/05 HOLD encadeado |
| performed_at | 2026-09-05T21:10:58.413301-03:00 |
| performed_by | hermes-lab |


---

### 320. `hwa-lab-10.2.8-keyjob-0058`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `jobdef`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job defined with KEYJOB ran and completed SUCC in the plan, confirming the keyjob attribute is accepted and marked in the plan.

> **ATENCAO / RESSALVAS DE USO:** CRITICAL attribute was rejected in all tested positions and requires WSA enabled. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer add and conman sj KEYJOB_TEST

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Keyjob attribute |
| Citacao de suporte | KJJOB SUCC in KEYJOB_TEST stream. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | keyjob |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=jobdef |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, a job defined with KEYJOB ran and completed SUCC in the plan, confirming the keyjob attribute is accepted and marked in the plan?


---

### 321. `hwa-lab-10.2.8-maxdur-kill-0059`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `jobdef`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job defined with MAXDUR 1 ONMAXDUR KILL running sleep 120 was killed at 1 minute: stream ABEND, job ABEND return code 143, marked [MaxDurationExceeded] [KillSubmitted] maxdur=00:01.

> **ATENCAO / RESSALVAS DE USO:** ONMAXDUR STOP was not accepted; KILL action worked. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sj MAXDUR_TEST

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Max duration kill behavior |
| Citacao de suporte | MXJOB ABEND rc 143 [MaxDurationExceeded] [KillSubmitted] maxdur=00:01. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | maxdur_kill |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['kill', 'submit'], result=MXJOB ABEND rc 143 [MaxDurationExceeded] [KillSubmitted] maxdur=00:01. | ONMAXDUR STOP was not accepted; KILL action worked., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-maxdur.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=jobdef |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, a job defined with MAXDUR 1 ONMAXDUR KILL running sleep 120 was killed at 1 minute: stream ABEND, job ABEND return code 143, marked [MaxDurationExceeded] [KillSubmitted] maxdur=00:01.?


---

### 322. `hwa-lab-10.2.8-mdm-backup-restore-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, MDM master, PostgreSQL 18.6), o backup e restore do master domain manager foi validado de ponta a ponta, cobrindo lacuna que no corpus existia so como claim de doc (hwa-10.2.8-backup-backup-master-data-0001 recomenda backup dos master data files, sem procedimento validado). (1) Backup do banco: pg_dump -Fc do TWS gerou dump custom de ~444KB e do TDWC ~350KB (banco TWS = 17MB). (2) Backup do master data file Symphony: copia de /opt/hwa/TWSDATA/Symphony (~55KB). (3) PROVA DE RESTAURABILIDADE reversivel: criou-se banco clone TWS_BKPTEST, pg_restore do dump sem erros (rc=0), e o clone ficou identico ao original - 137/137 tabelas (information_schema excluindo pg_catalog/information_schema), 2 job streams de modelo (mdl.ajs_abstract_job_streams) e 30 instancias de job stream (mdl.jsi_job_stream_instances, o plano com Sfinal/FINAL diario) preservadas. O clone de teste foi removido (dropdb) - zero impacto no banco de producao TWS. Acesso ao postgres via runuser -l postgres (socket local); os dumps foram gravados em /data (mount sdb).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - pg_dump TWS 444KB + TDWC 350KB; Symphony 55KB copiado; pg_restore em clone TWS_BKPTEST rc=0 sem erros; clone identico (137/137 tabelas, 2 job streams modelo, 30 instancias plano); clone removido. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), PostgreSQL 18.6 |
| Classificacao de risco | read_only |
| sanitized_output | pg_dump -Fc TWS -> 444KB, TDWC -> 350KB; Symphony -> 55KB; pg_restore -d TWS_BKPTEST rc=0; clone 137/137 tabelas; 2 ajs_abstract_job_streams; 30 jsi_job_stream_instances; dropdb TWS_BKPTEST |
| performed_at | 2026-09-07T16:00:36.204942-03:00 |
| performed_by | hermes-lab |


---

### 323. `hwa-lab-10.2.8-mdm-serverinst-flags-validation-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o instalador do Master Domain Manager (serverinst.sh) valida rigorosamente as seguintes regras e emite os respectivos códigos oficiais: (1) Rejeição de licença não aceita com WAINST036I ('Accept the license and terms conditions before proceeding with the installation'); (2) Exigência de SGBD suportado com WAINST033E ('Incorrect value for the option --rdbmstype. Expected values are < DB2 | ORACLE | MSSQL | IDS | POSTGRESQL >'); (3) Obrigatoriedade estrita de credenciais com WAINST024E ('The following option is required: --dbhostname' / '--wapassword'); (4) Validação ativa de conectividade com o banco via chamada prévia do configureDb.sh com ação test_connection_to_db (falha reportada como WAINST015E se o SGBD recusar a credencial); (5) Validação de propriedade dos binários do kit extraído com WAINST0517E ('The owner ... of the directory ... is not the same as the user who is installing the product').

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | read_only |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-hwa) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T07:15:00BRT |
| performed_by | hermes-agent-hwa |
| tested_commands | ./serverinst.sh --acceptlicense no --check true; ./serverinst.sh --acceptlicense yes --check true; ./serverinst.sh --acceptlicense yes --rdbmstype POSTGRESQL --check true; ./serverinst.sh --acceptlicense yes --rdbmstype POSTGRESQL --dbhostname localhost --dbname TWS --dbuser postgres --dbpassword pass --check true; ./serverinst.sh --acceptlicense yes --rdbmstype POSTGRESQL --dbhostname 127.0.0.1 --dbname TWS --dbuser postgres --dbpassword <pw> --wapassword <pw> --wlpdir /opt/liberty/wlp --inst_dir /tmp/test_not_empty --check true |
| sanitized_output | Comprovados códigos oficiais WAINST036I, WAINST033E, WAINST024E, WAINST015E e WAINST0517E. |
| observations | Todas as 50 flags CLI do serverinst.sh, as 75 propriedades de serverinst.properties e as 30 flags do configureDb.sh foram mapeadas em data/runbooks/mdm-serverinst-twsinst-complete-reference.md. |


---

### 324. `hwa-lab-10.2.8-mindur-continue-0061`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job defined with MINDUR 0001 completed SUCC with the [MinDurationNotReached] [Continue] indicator, confirming the mindur minimum-duration monitoring attribute.

> **ATENCAO / RESSALVAS DE USO:** MINDUR accepts a time value; ONMINDUR/PERCENT actions were not accepted by this engine. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sj MINDUR_TEST

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Min duration behavior |
| Citacao de suporte | MNJOB SUCC [MinDurationNotReached] [Continue] mindur=00:01. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=monitor |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, a job defined with MINDUR 0001 completed SUCC with the [MinDurationNotReached] [Continue] indicator, confirming the mindur minimum-duration monitoring attribute?


---

### 325. `hwa-lab-10.2.8-nightly-rollover-d1-real-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, America/Sao_Paulo), a virada noturna REAL do plano aconteceu automaticamente e sem intervencao manual, validando o modelo 'dia vigente 00:05 + D+1': o MDMXA#FINAL 2359 09/05 executou no horario agendado (23:59 BR) STARTAPPSERVER->MAKEPLAN->SWITCHPLAN todos SUCC rc0, seguido do MDMXA#FINALPOSTREPORTS 2359 09/05 com CHECKSYNC->CREATEPOSTREPORTS->UPDATESTATS SUCC rc0. O plano de producao virou para o dia seguinte: de '09/05 00:05 -> 09/06 00:04' (run 19) para '09/06 00:05 -> 09/07 00:04' (run 20), com o novo MDMXA#FINAL 2359 09/06 ja HOLD agendado (carryforward). Preproduction ate 09/20. Confirma a corrente auto-sustentavel de planos: cada dia as 23:59 o FINAL roda e gera/ativa o plano do dia seguinte (D+1), que comeca 00:05 - sem necessidade de JnextPlan manual.

| Atributo | Valor |
| --- | --- |
| Resultado observado | as 00:21 de 09/06: FINAL 09/05 SUCC (STARTAPPSERVER #J6599, MAKEPLAN #J6741, SWITCHPLAN #J6896 rc0), FINALPOSTREPORTS 09/05 SUCC (CHECKSYNC #J7130, CREATEPOSTREPORTS #J7131, UPDATESTATS #J7415); plano 09/06 00:05 -> 09/07 00:04 run 20; novo FINAL 09/06 23:59 HOLD. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | FINAL 09/05 23:59 SUCC (3 jobs rc0) + FINALPOSTREPORTS SUCC (3 jobs rc0) | plano virou p/ 09/06 00:05 (run 20) | novo FINAL 09/06 agendado |
| performed_at | 2026-09-06T00:22:27.372550-03:00 |
| performed_by | hermes-lab |


---

### 326. `hwa-lab-10.2.8-opens-file-dep-hostname-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, dominio MDM master), uma dependencia de arquivo OPENS foi validada ao vivo: o job MDM#CPJ_WAIT com 'OPENS /tmp/tws_file_trigger.txt' dentro do job stream CPLXOPENS, ao ser submetido via sbs, ficou HOLD com a dependencia 'tws_file_trigger.txt' listada (aguardando o arquivo). CAUSA RAIZ de nao liberar mesmo apos criar o arquivo: o agente/jobman nao conseguia reportar o recurso ao engine porque o hostname 'tws-hwa.lab' nao resolvia no container (o /etc/hosts so tinha localhost e os enderecos da interface associados ao hostname real 8189d3570cc2). O JobManager_message.log mostrava AWSITA081E repetido: 'The agent can not send the resource information a https://tws-hwa.lab:31116/JobManagerRESTWeb/JobScheduler/resource' com AWSITA366E 'Could not resolve hostname'. Apos adicionar 'loopback tws-hwa.lab' ao /etc/hosts, o monitor detectou o arquivo e o job executou SUCC rc0. O conman/composer conectavam normalmente (usam outro caminho de resolucao), mascarando o problema ate o teste de recurso de arquivo.

| Atributo | Valor |
| --- | --- |
| Resultado observado | CPJ_WAIT HOLD aguardando tws_file_trigger.txt; apos criar o arquivo continuou HOLD (AWSITA081E/AWSITA366E could not resolve hostname); apos adicionar tws-hwa.lab apontando para loopback no /etc/hosts o job rodou SUCC rc0 e o stream CPLXOPENS SUCC. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | OPENS HOLD ate arquivo existir; fix: /etc/hosts com tws-hwa.lab no loopback; AWSITA081E/AWSITA366E could not resolve hostname; depois SUCC rc0 |
| performed_at | 2026-09-05T22:22:01.770362-03:00 |
| performed_by | hermes-lab |


---

### 327. `hwa-lab-10.2.8-planman-resync-hot-recovery-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), o procedimento de sincronizacao e recuperacao a quente de plano via 'planman resync' foi validado com sucesso sem interrupcao do motor de producao. O comando envia a solicitacao simultaneamente para o batchman e para o Liberty application server (AWSBEH119I 'Resync command forwarded to batchman and application server'). Em seguida, monitora o ciclo de sincronizacao (AWSJCL070I 'Symphony file load is not yet started' seguido de AWSJCL074I 'Symphony file successfully loaded in Database'), recarregando o estado em memoria do Symphony para o banco PostgreSQL de forma transacional e consistente, mantendo o status do batchman inalterado (Batchman LIVES).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - planman resync encaminhado para batchman e appserver (AWSBEH119I) e sincronizado com sucesso no PostgreSQL (AWSJCL074I) a quente. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | planman resync -> AWSBEH119I forwarded to batchman and application server; AWSJCL070I Symphony load not yet started; AWSJCL074I Symphony file successfully loaded in Database |
| performed_at | 2026-09-08T13:52:26.790114-03:00 |
| performed_by | hermes-lab |


---

### 328. `hwa-lab-10.2.8-postgres-disabled-after-container-restart-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (ubi9/ubi-init, systemd), o servico postgresql-18 e unit systemd DISABLED (nao sobe sozinho no boot do container). Apos um docker stop/start de tws-hwa, o PostgreSQL ficou inativo (porta 5432 sem listener) enquanto o engineServer (Liberty java) subiu via tebctl/start_tws.sh e entrou em loop de retry 'Connection refused' (AWSJDB802E / DSRA0010E) sem completar o boot das aplicacoes (HTTP 404). ORDEM CORRETA de restart do dominio MDM no container: (1) systemctl start postgresql-18; (2) agente ITA via systemctl start tebctl-tws_cpa_agent_wauser; (3) startAppServer.sh (engineServer Liberty); (4) conman start&link + startmon para batchman. Efetivando o timezone America/Sao_Paulo no engine: parar via stopAppServer.sh, trocar o localtime, reiniciar startAppServer.sh (o engine Java so pega o TZ novo no boot).

| Atributo | Valor |
| --- | --- |
| Resultado observado | apos docker stop/start, postgresql-18 inativo e engine em loop de connection refused; systemctl start postgresql-18 + restart do engine (stopAppServer.sh/startAppServer.sh) resolveram; engine bootou CWWKF0011I ready em ~30s e Event Processor na porta 31116. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | medium |
| sanitized_output | postgresql-18 unit disabled; docker restart: postgres down; engine loop 5432 refused AWSJDB802E; fix: systemctl start postgresql-18 + restart engine; CWWKF0011I ready |
| performed_at | 2026-09-05T21:11:56.457388-03:00 |
| performed_by | hermes-lab |


---

### 329. `hwa-lab-10.2.8-postgres-schema-validation-0050`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

In the HWA laboratory, the PostgreSQL database TWS contains the HWA multi-schema structure: dwb (29 tables), evt (4), log (2), mdl (48), pln (13). Total 96 tables. The role twsuser exists and has usage privileges on these schemas. The role twsdbuser does not exist; the term twsuser is a PostgreSQL role, not a schema.

> **ATENCAO / RESSALVAS DE USO:** HWA on PostgreSQL uses schema separation. twsuser is the role, not a schema; tables live in dwb/evt/log/mdl/pln. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local pg_tables and pg_namespace queries on TWS database

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | PostgreSQL 18.6 on WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | PostgreSQL schema and role inventory |
| Citacao de suporte | dwb 29 tables, evt 4, log 2, mdl 48, pln 13; twsuser role present; twsdbuser absent. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | PostgreSQL 18.6 on WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=log |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, the PostgreSQL database TWS contains the HWA multi-schema structure: dwb (29 tables), evt (4), log (2), mdl (48), pln (13)?


---

### 330. `hwa-lab-10.2.8-priority-limit-validation-0043`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `show`

**Afirmacao / Conteudo:**

In the HWA laboratory, PRIO_TEST with LIMIT 2 showed: priority 0 stayed HOLD (never launched), numeric priorities 10/20/50 ran SUCC, and HI/GO ran SUCC and could run despite LIMIT. This matches documented limit/priority behavior.

> **ATENCAO / RESSALVAS DE USO:** Priority 0 prevents launch; HI/GO bypass the workstation CPU limit; the stream showed STUCK with LIMIT 2 while jobs queued. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman showjobs and JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Priority and LIMIT validation |
| Citacao de suporte | PRIO_00 HOLD; PRIO_10 SUCC; PRIO_20 SUCC; PRIO_50 SUCC; PRIO_HI SUCC; PRIO_GO SUCC. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | show |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=show |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, PRIO_TEST with LIMIT 2 showed: priority 0 stayed HOLD (never launched), numeric priorities 10/20/50 ran SUCC, and HI/GO ran SUCC and could run despite LIMIT?


---

### 331. `hwa-lab-10.2.8-recovery-rerun-container-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, dominio MDM master), um job definido com RECOVERY RERUN (MDM#CPJ_ERR, DOCOMMAND 'echo CPLXERR_FAIL; exit 1') submetido via sbs no plano executou e ABEND rc1; o scheduler HCL disparou automaticamente o rerun de recuperacao ('>>rerun as CPJ_ERR ... [Recovery]') que tambem ABEND rc1. Confirma que o RECOVERY RERUN automatico sobre falha do job funciona no container (master MDM executa nativamente via JobManager). O stream (MDM#CPLXRERUN) terminou ABEND.

| Atributo | Valor |
| --- | --- |
| Resultado observado | sj MDM#CPLXRERUN mostrou CPJ_ERR ABEND rc1 (#J14174) seguido de '>>rerun as CPJ_ERR ABEND rc1 (#J14201; [Recovery])'; stream ABEND. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | CPJ_ERR ABEND rc1 | >>rerun as CPJ_ERR ABEND rc1 [Recovery] | stream ABEND |
| performed_at | 2026-09-05T21:26:58.259738-03:00 |
| performed_by | hermes-lab |


---

### 332. `hwa-lab-10.2.8-rest-api-v2-auth-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), a REST API V2 (engine https://localhost:31116/twsd/) foi validada de ponta a ponta com autenticacao basic auth de usuario TWS. DESCOBERTA CRITICA de auth: a senha do usuario (wauser) e validada pelo engine contra o campo interno user.twsuser.password (armazenado ENCRIPTADO {aes} em wauser_variables.xml, com a chave em passphrase_variables.xml wlp.password.encryption.key) - e NAO apenas contra a senha do SO. Mudar so a senha SO (chpasswd) mantem a REST em HTTP 401; e necessario: (1) reencriptar a nova senha com /opt/liberty/wlp/bin/securityUtility encode --encoding=aes --key=<chave-10dig> e atualizar user.twsuser.password nos wauser_variables.xml do engineServer (/opt/hwa/TWSDATA/usr/servers/engineServer/.../overrides/) e dwcServer (/opt/hwa/DWC/DWC_DATA/...), (2) reiniciar o engineServer (stopAppServer.sh/startAppServer.sh, AWSBHU622I), (3) entao basic auth funciona. Endpoints validados (GETs read-only com basic auth wauser): /twsd/api/v2/engine/info -> 200 {licenseType:PERSERVER, timezone America/Sao_Paulo}; /twsd/api/v2/plan/job/count -> 200 {count:13} (13 jobs no plano do dia vigente); /twsd/api/v2/plan/jobstream?limit=5 -> 200 com envelope {count,results} (jobstreams do plano, UUIDs, workstation /MDM, schedTime UTC + timeZone America/Sao_Paulo, jsStatusFlags carriedForward). Spec OpenAPI em /twsd/WA_API3_v2.json com 212 paths (plan/job, plan/jobstream, plan/job/action/*, model/*, engine/*). POST /twsd/api/v2/login retornou 401 (fluxo de login usa outro mecanismo); o acesso via basic auth direto nos recursos funciona.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - REST v2 autenticada via basic auth apos atualizar user.twsuser.password {aes} + restart engine; engine/info 200, plan/job/count 200 count=13, plan/jobstream 200 count=5; spec 212 paths. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), Liberty engineServer 31116 |
| Classificacao de risco | read_only |
| sanitized_output | basic auth wauser OK apos user.twsuser.password atualizado ({aes}, securityUtility encode --encoding=aes) + restart engineServer; GET engine/info 200 PERSERVER America/Sao_Paulo; plan/job/count 200 count=13; plan/jobstream 200; POST login 401 (usar basic auth) |
| performed_at | 2026-09-07T20:59:42.641161-03:00 |
| performed_by | hermes-lab |


---

### 333. `hwa-lab-10.2.8-rest-api-v2-lifecycle-actions-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), o ciclo completo de operacao e gerenciamento de plano via REST API V2 (engine https://localhost:31116/twsd/api/v2) foi validado de ponta a ponta com autenticacao basic auth (wauser). Endpoints validados com sucesso (HTTP 200): (1) Consulta de definicoes do modelo: GET /twsd/api/v2/model/jobdefinition (retorna defs com task.other, userName, isCommand) e GET /twsd/api/v2/model/jobstream. (2) Submissao ad-hoc: POST /twsd/api/v2/plan/job/submit-ad-hoc-job com payload SubmitAdHocJobOptionsV2 (workstationKey /MDM, jobName, task.other) retornou HTTP 200 {'id': 'MDM;JOBS;...'}, instanciando o job na stream default JOBS em estado HOLD. (3) Alteracao dinamica de prioridade no plano: PUT /twsd/api/v2/plan/job/{job_id}/action/update-priority?priority=50 retornou HTTP 200, refletindo no conman sj como prioridade elevada (+10). (4) Liberacao no plano: PUT /twsd/api/v2/plan/job/{job_id}/action/release retornou HTTP 200, fazendo o job entrar imediatamente em EXEC e transitar para SUCC rc 0. (5) Consulta de Job Log real: GET /twsd/api/v2/plan/job/run/{run_id}/joblog retornou HTTP 200 com a saida completa do jobmanrc e JOBINFO (Exit Status: 0, Elapsed Time: 0:00:25). (6) Rerun de job via REST: PUT /twsd/api/v2/plan/job/run/{run_id}/action/rerun com header Content-Type: application/json e corpo {} retornou HTTP 200 (sem header retorna 415), gerando nova instancia '>>rerun step' (#J39010) que executou SUCC rc 0. (7) Comando de componente: PUT /twsd/api/v2/engine/run-component-command retornou HTTP 200 com payload estruturado AWSJCS027E demonstrando que componentId exige tipo AGENT (rejeita MANAGER).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - REST v2 model/jobdefinition (200), model/jobstream (200), submit-ad-hoc-job (200), update-priority (200), release (200), run/{run_id}/joblog (200), run/{run_id}/action/rerun (200 SUCC), engine/run-component-command (200 AWSJCS027E). |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init), Liberty engineServer 31116 |
| Classificacao de risco | low |
| sanitized_output | POST submit-ad-hoc-job -> HTTP 200; PUT update-priority -> HTTP 200; PUT release -> HTTP 200 (EXEC -> SUCC); GET run/{run_id}/joblog -> HTTP 200 (jobmanrc log); PUT run/{run_id}/action/rerun -> HTTP 200 (>>rerun step SUCC); PUT run-component-command -> HTTP 200 (AWSJCS027E AGENT required) |
| performed_at | 2026-09-07T21:05:35.399930-03:00 |
| performed_by | hermes-lab |


---

### 334. `hwa-lab-10.2.8-runbook-conclusion-0052`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `runbook`

**Afirmacao / Conteudo:**

In the HWA laboratory, the runbook data/runbooks/hwa-10.2.8-wsl-lab.md now contains a Conclusion section summarizing validated outcomes, schema/role findings, wauser permissions, known gaps and a consolidated reference list.

> **ATENCAO / RESSALVAS DE USO:** Runbook consolidation closes the executable validation sequence. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local file data/runbooks/hwa-10.2.8-wsl-lab.md

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Runbook conclusion |
| Citacao de suporte | Conclusion section added; DWC and -scratch remain pending. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | runbook_conclusion |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=runbook |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, the runbook data/runbooks/hwa-10.2.8-wsl-lab?


---

### 335. `hwa-lab-10.2.8-serverinst-full-success-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8 (UBI-init), o serverinst.sh HWA 10.2.8 completou a instalacao do MDM com PostgreSQL 18.6: WAINST023I success, servidores ativos (netman 31111/31113, JobManager 31114, EIF 31131, Liberty engineServer), JnextPlan -for 0000 carregou o Symphony (AWSJCL074I) e conman showcpus reportou Batchman LIVES para MDM com MDMXA x-agent - replicando o lab WSL2 em plataforma RHEL container.

| Atributo | Valor |
| --- | --- |
| command | rm -rf /opt/hwa /tmp/wa10.2.8.00 && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./serverinst.sh -f /installers/lab/serverinst.properties && su - wauser -c 'source /opt/hwa/TWS/tws_env.sh && JnextPlan -for 0000' && su - wauser -c 'source /opt/hwa/TWS/tws_env.sh && conman showcpus' |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init (Docker, systemd), CachyOS host; diffutils + libxcrypt-compat + java-21-openjdk-headless + curl instalados no container; PostgreSQL 18.6 PGDG EL9 com database TWS populado (configureDb.sh executado antes); Open Liberty em /opt/liberty/wlp (SHA-256 identico ao lab WSL), wauser, certs lab em /opt/ssl-certs (fora do INST_DIR); serverinst.properties: THISCPU=MDM, DISPLAYNAME=MDMDA, XANAME=MDMXA, RDBMS_TYPE=POSTGRESQL, DOMAIN=MASTERDM, USE_ENCRYPTION=true; INST_DIR /opt/hwa vazio antes da execucao (reinstalacao limpa) |
| sanitized_output | serverinst.sh: WAINST202I Configuring broker. WAINST200I Configuring WLP. WAINST201I Configuring data source. WAINST203I Configuring SFinal. WAINST0229I Importing certificates. WAINST061I Performing post-configuration steps. WAINST023I The installation has completed successfully. JnextPlan: AWSJCL074I Symphony file successfully loaded in Database. conman showcpus: Scheduled for (Exp) 09/04/26 (#1) on MDM. Batchman LIVES. MDM 1 *UNIX MASTER ... MDMXA 1 OTHR X-AGENT ... MASTERDM. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | Reinstalacao: rm -rf /opt/hwa e reexecucao; banco TWS preservado (DROP DATABASE opcional p/ reset total) |
| Criterio de parada | Interromper se qualquer fase WAINST falhar; limpar aes residuos antes de reruns |
| evidence_url | https://help.hcl-software.com/workloadautomation/v1028 |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Instalacao completa do MDM 10.2.8 em RHEL 9 container validada ponta a ponta (instalacao + plano + Batchman). Requisitos adicionais vs Ubuntu/WSL2: diffutils (cmp), libxcrypt-compat (libcrypt.so.1 p/ makesec), certs fora do INST_DIR, limpeza de residuos aes entre reruns, e instalacao em UMA passada pelo serverinst.sh (sem retomada via twsinst direto). Cross-plataforma: mesmas mensagens de sucesso do lab WSL2 (AWSJCL074I, Batchman LIVES). |
| performed_at | 2026-09-04T19:10:33.130996-03:00 |


---

### 336. `hwa-lab-10.2.8-serverinst-inst-dir-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8, serverinst.sh do HWA 10.2.8 rejeita instalacao com WAINST050E quando o INST_DIR (/opt/hwa) nao esta vazio; a pasta de certificados SSL (SSL_KEY_FOLDER) deve ficar FORA do INST_DIR.

| Atributo | Valor |
| --- | --- |
| command | cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./serverinst.sh -f /installers/lab/serverinst.properties |
| Pre-condicoes | HWA 10.2.8, configureDb.sh ja executado com sucesso (DB TWS com schemas); INST_DIR=/opt/hwa continha a pasta ssl/ com os certificados PEM (ca.crt, tls.crt, tls.key); SSL_KEY_FOLDER apontava para /opt/hwa/ssl; Open Liberty instalado em /opt/liberty/wlp, usuario wauser existente, hostname tws-hwa.lab |
| sanitized_output | WAINST050E The directory /opt/hwa should be empty. WAINST035I For more details see the installation log file. |
| Resultado observado | REJECTED |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | Mover SSL_KEY_FOLDER para fora do INST_DIR (ex.: /opt/ssl-certs), esvaziar o INST_DIR e reexecutar serverinst.sh |
| Criterio de parada | Interromper apos WAINST050E (validacao de diretorio vazio) |
| performed_by | hermes-lab (container tws-hwa) |
| observations | serverinst exige INST_DIR vazio (validacao de fresh install). Certificados devem morar fora do INST_DIR - o lab WSL2 usou pasta separada (ex.: dwc-certs). Fix aplicado: mv /opt/hwa/ssl /opt/ssl-certs, rmdir /opt/hwa, SSL_KEY_FOLDER=/opt/ssl-certs no properties; reexecucao em andamento. |
| performed_at | 2026-09-04T18:52:37.906686-03:00 |


---

### 337. `hwa-lab-10.2.8-serverinst-missing-cmp-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8 UBI (imagem ubi-init minimal), o twsinst aninhado do serverinst.sh HWA 10.2.8 falha com rc=127 (cmp: command not found) na fase de importacao de certificados; instalar diffutils resolve; o serverinst e rerunnable e retoma do passo falho.

| Atributo | Valor |
| --- | --- |
| command | dnf install -y diffutils && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./serverinst.sh -f /installers/lab/serverinst.properties |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init (Docker), imagem minimal sem diffutils; serverinst.sh executado apos configureDb OK; binarios instalados em /opt/hwa (1.5G); Falha ocorreu em: AWSFAB601I Import certificates / AWSFAB474I Run security scripts (twsinst line 11180); Liberty OK, wauser OK, SSL_KEY_FOLDER=/opt/ssl-certs (fora do INST_DIR) |
| sanitized_output | AWSFAB601I Import certificates. AWSFAB474I Run security scripts. twsinst: line 11180: cmp: command not found (x7). AWSFAB035E The installation failed. execute_command_quiet rc=127. WAINST015E The following command failed: ./twsinst ... exitValue = 127. AWSFAB057I The script can be run again. It retries the failed step. |
| Resultado observado | FAIL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | dnf install diffutils e reexecutar serverinst.sh (rerunnable, retoma do passo falho) |
| Criterio de parada | Interromper se a reexecucao falhar em outro passo |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Requisito de pacote nao documentado: imagens RHEL UBI minimal nao incluem diffutils (cmp). O lab WSL2 (Ubuntu 22.04) tinha cmp presente, por isso nao apareceu la. O serverinst.sh e explicitamente rerunnable (AWSFAB057I). Apos dnf install diffutils, reexecucao lancada. |
| performed_at | 2026-09-04T18:53:34.144223-03:00 |


---

### 338. `hwa-lab-10.2.8-serverinst-no-skip-twsinst-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

O serverinst.sh HWA 10.2.8 nao possui caminho para pular o twsinst -new: apos uma instalacao fresh completa via twsinst direto, reexecutar o serverinst.sh (mesmo com SKIPCHECKEMPTYDIR=true) falha com AWSFAB022E (instalacao fresh com instancia previa em /opt/hwa/TWSDATA). Instalacao interrompida no meio nao e completavel pelo wrapper - recomecar do zero (apagar /opt/hwa e work_dir) com o serverinst.sh completo.

| Atributo | Valor |
| --- | --- |
| command | rm -rf /opt/hwa /tmp/wa10.2.8.00 && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./serverinst.sh -f /installers/lab/serverinst.properties |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init; twsinst -new completou AWSFAB033I (instalacao fresh OK) via invocacao direta; Fases do wrapper (configureDatasource/configureWlp/waPostConfigure) ficaram pendentes; serverinst.sh reexecutado com SKIPCHECKEMPTYDIR=true: passou WAINST050E mas o twsinst -new interno falhou AWSFAB022E (instancia previa em /opt/hwa/TWSDATA); configureDb.sh ja executado (banco TWS com schemas - nao precisa refazer) |
| sanitized_output | serverinst.sh: WAINST062I Checking input. WAINST208I Checking WLP. WAINST060I Installing binaries. twsinst: AWSFAB022E You are running a fresh installation but the installation script has found a previous instance of HCL Workload Automation ... in /opt/hwa/TWSDATA. WAINST015E The following command failed. SERVERINST_EXIT=1. |
| Resultado observado | FAIL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | rm -rf /opt/hwa /tmp/wa10.2.8.00 e reexecucao do serverinst.sh completo (pacotes de sistema diffutils/libxcrypt-compat permanecem instalados no container) |
| Criterio de parada | Interromper se a instalacao limpa falhar em qualquer passo |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Licao: em container RHEL, a instalacao do MDM deve ser feita de UMA vez pelo serverinst.sh completo (com diffutils + libxcrypt-compat pre-instalados e certs fora do INST_DIR); a rota de retomada via twsinst direto funciona para o twsinst mas deixa as fases de configuracao orfas. Reinstalacao limpa lancada com todos os fixes. |
| performed_at | 2026-09-04T19:04:23.288313-03:00 |


---

### 339. `hwa-lab-10.2.8-serverinst-wrapper-rerun-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Apos falha do twsinst interno (ex.: cmp ausente), reexecutar o wrapper serverinst.sh falha de novo com WAINST050E (INST_DIR nao vazio, pois a execucao parcial ja populou /opt/hwa); o AWSFAB057I 'script can be run again' refere-se ao twsinst interno, que deve ser invocado DIRETAMENTE com os parametros do log para retomar do passo falho.

| Atributo | Valor |
| --- | --- |
| command | cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./twsinst -new -inst_dir /opt/hwa -agent both -addjruntime true -jmport 31114 -hostname tws-hwa.lab -displayname MDMDA -port 31111 -netmansslport 31113 -thiscpu MDM -master MDM -company LAB -tdwbhostname tws-hwa.lab -tdwbport 31116 -data_dir /opt/hwa/TWSDATA -wauser wauser -wapassword REDACTED -acceptlicense yes -uname wauser -lang C -caller MDM -work_dir /tmp/wa10.2.8.00 -sslpassword REDACTED -sslkeysfolder /opt/ssl-certs -useencryption true -encryptionpassword REDACTED |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init; 1a execucao serverinst.sh: WAINST050E (dir nao vazio - certs dentro do INST_DIR); corrigido movendo certs; 2a execucao serverinst.sh: instalou binarios em /opt/hwa (1.5G) e falhou no twsinst (cmp ausente); corrigido com dnf install diffutils; 3a execucao serverinst.sh: falhou de novo com WAINST050E porque /opt/hwa ja estava populado pela 2a; Retomada via twsinst direto com os MESMOS parametros que o serverinst.sh usou (visiveis no log) |
| sanitized_output | 1a: WAINST050E The directory /opt/hwa should be empty. 2a: ... cmp: command not found ... AWSFAB057I The script can be run again. It retries the failed step. 3a: WAINST050E (INST_DIR populado pela execucao parcial anterior). Retomada: invocacao direta do twsinst com -caller MDM. |
| Resultado observado | PARTIAL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | Para recomeco limpo: apagar /opt/hwa e /tmp/wa10.2.8.00 e reexecutar serverinst.sh do zero |
| Criterio de parada | Interromper se o twsinst direto falhar sem mensagem de retomada |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Licao operacional: o wrapper serverinst.sh valida INST_DIR vazio a cada execucao e NAO retoma; a retomada real (AWSFAB057I) e do twsinst interno. O comando exato do twsinst fica registrado no log do serverinst (com senhas mascaradas xxxxx) - reconstruir com os valores do properties. Estado parcial preservado em /opt/hwa e /tmp/wa10.2.8.00. |
| performed_at | 2026-09-04T18:55:17.508899-03:00 |


---

### 340. `hwa-lab-10.2.8-sfinal-awsbhv082e-recovery-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `sfinal`

**Afirmacao / Conteudo:**

No laboratório HWA 10.2.8 Distributed (container Docker tws-hwa), o job stream FINAL ancorado na workstation MDMXA (Extended Agent unixlocl) pode apresentar estado STUCK quando o job MAKEPLAN/SWITCHPLAN falha com AWSBHV082E (run number de Symnew idêntico ao Symphony anterior). O diagnóstico seguro exige validar a saúde do banco com 'optman ls', verificar consistência com 'planman showinfo' e NUNCA executar MakePlan manualmente. Se o plano já tiver sido estendido para a data corrente (Run == Confirm), a recuperação canônica é: (1) reiniciar o motor com 'conman start; mgr'; (2) reconciliar a instância residual com 'conman confirm MDMXA#FINAL(<sched_anterior>).SWITCHPLAN;succ'; (3) liberar o stream atual com 'conman release MDMXA#FINAL(<sched_atual>)', permitindo que STARTAPPSERVER, MAKEPLAN e SWITCHPLAN completem automaticamente com ReturnCode 0 no novo Run number.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | observed_in_lab |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Classificacao de risco | read_only |
| Fonte (URL) | lab://tws-hwa/stdlist/2026.09.09/O491002.1428 |
| Titulo da fonte | HWA 10.2.8 Container Lab Execution: SwitchPlan AWSBHV082E Recovery and Automation |
| Citacao de suporte | STAGEMAN:AWSBHV082E The previous Symphony file and the Symnew file have the same run number. They cannot be merged... Scheduled for (Exp) 09/09/26 (#30) on MDM. Batchman LIVES. |
| Coletado em | 2026-09-09 |
| Capacidade | plan_management |
| Modo de operacao | write |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=conman confirm / release, error_code=AWSBHV082E, schedule=FINAL / FINALPOSTREPORTS, workstation=MDMXA |

**Perguntas relacionadas:**

- Como recuperar o job stream FINAL em estado STUCK após erro AWSBHV082E no SwitchPlan sem rodar MakePlan na mão?
- Por que o conman sj MDM#FINAL.@ volta vazio se o stream FINAL está na workstation MDMXA?
- Qual o procedimento documentado para destravar a esteira FINALPOSTREPORTS quando o plano já foi estendido?


---

### 341. `hwa-lab-10.2.8-sfinal-confrontation-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, /opt/hwa/TWS/Sfinal e /opt/hwa/TWS/config/Sfinal são iguais, enquanto /opt/hwa/TWS/Sfinal2 difere na dependência do stream FINAL: Sfinal usa FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS e Sfinal2 usa a janela de dependência de MDMXA#FINALPOSTREPORTS.UPDATESTATS do ciclo anterior.

> **ATENCAO / RESSALVAS DE USO:** This is a lab observation, not a general product claim. No database mutation was performed.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu |
| Status do conhecimento | observed_in_lab |
| Confianca | high |
| Fonte (URL) | local read-only comparison: /opt/hwa/TWS/Sfinal, /opt/hwa/TWS/config/Sfinal, /opt/hwa/TWS/Sfinal2 |
| Titulo da fonte | Sfinal/Sfinal2 laboratory comparison |
| Citacao de suporte | diff Sfinal vs config/Sfinal: no differences; diff Sfinal vs Sfinal2: dependency line differs. |
| Coletado em | 2026-08-21 |


---

### 342. `hwa-lab-10.2.8-sfinal-confrontation-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, os objetos FINAL e FINALPOSTREPORTS no banco correspondem à variante Sfinal, não à dependência alternativa de Sfinal2; o FINAL armazenado contém FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS e FINALPOSTREPORTS contém FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS.

> **ATENCAO / RESSALVAS DE USO:** The result establishes which dependency variant is installed; it does not establish that Sfinal2 would select planman crt.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu |
| Status do conhecimento | observed_in_lab |
| Confianca | high |
| Fonte (URL) | local read-only composer display of MDMXA#FINAL and MDMXA#FINALPOSTREPORTS |
| Titulo da fonte | Database FINAL definitions laboratory validation |
| Citacao de suporte | FINAL: FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS; FINALPOSTREPORTS: FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS. |
| Coletado em | 2026-08-21 |


---

### 343. `hwa-lab-10.2.8-sfinal-confrontation-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, o último FINAL executado concluiu STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, CHECKSYNC, CREATEPOSTREPORTS e UPDATESTATS com código 0; o MAKEPLAN registrou planman ext, AWSJCL062I, e o SWITCHPLAN registrou atualização do run number e término com Exit Status 0.

> **ATENCAO / RESSALVAS DE USO:** This validates the observed cycle only.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu |
| Status do conhecimento | observed_in_lab |
| Confianca | high |
| Fonte (URL) | local read-only logs: /opt/hwa/TWSDATA/stdlist/2026.08.20/O596375.2359 and O596516.2359 |
| Titulo da fonte | FINAL execution validation |
| Citacao de suporte | Running planman ext; AWSJCL062I The production plan (Symnew) has been successfully extended; AWSJCL065I Run number has been successfully updated; Exit Status 0. |
| Coletado em | 2026-08-21 |


---

### 344. `hwa-lab-10.2.8-sfinal-definitions-removed-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No lab container RHEL 9.8, as definicoes de exemplo do Sfinal (MDMXA#FINAL e MDMXA#FINALPOSTREPORTS, importadas pelo instalador em 09/04) foram removidas do banco com composer delete (AWSJCL003I/AWSBIA290I), por decisao do dono do lab - o plano de producao ficou limpo (sem instancias) e o arquivo /opt/hwa/TWS/Sfinal foi preservado para reversao via composer add Sfinal.

| Atributo | Valor |
| --- | --- |
| command | composer delete js=MDMXA#FINAL (y) && composer delete js=MDMXA#FINALPOSTREPORTS (y) |
| Pre-condicoes | MDM 10.2.8 com Sfinal importado pelo instalador (js=MDMXA#FINAL e js=MDMXA#FINALPOSTREPORTS no banco, Updated 09/04/2026); Plano de producao corrente vazio (sem instancias - JnextPlan de validacao nao materializou o FINAL fora do run 2400); Decisao do dono: remover as definicoes de exemplo do banco |
| sanitized_output | composer delete js=MDMXA#FINAL -> AWSJCL003I completed successfully + AWSBIA290I Total objects deleted: 1. composer delete js=MDMXA#FINALPOSTREPORTS -> idem. Validacao pos-delete: composer display de ambos retorna 0 objetos; conman showjobs: 0 instancias FINAL. /opt/hwa/TWS/Sfinal preservado (2671 bytes). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | composer add Sfinal (arquivo /opt/hwa/TWS/Sfinal preservado) reimporta os 8 objetos (6 jobs + 2 streams) |
| Criterio de parada | Interromper se o delete retornar erro ou remover outros objetos |
| performed_by | hermes-lab (container tws-hwa) |
| observations | A remocao das definicoes nao afeta o MDM (batchman/netman ativos); apenas o ciclo noturno de exemplo (FINAL EVERYDAY AT 2359) deixara de ser instanciado. Reversao documentada. O runbook do container registra o Sfinal como IMPORTANTISSIMO (ciclo de automacao do plano) - a remocao foi decisao de lab, nao falha de instalacao. |
| performed_at | 2026-09-04T23:41:57.078406-03:00 |


---

### 345. `hwa-lab-10.2.8-sfinal-installed-by-installer-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No lab container RHEL 9.8, o instalador do MDM HWA 10.2.8 JA importa o Sfinal: os job streams MDMXA#FINAL e MDMXA#FINALPOSTREPORTS existem no banco (composer display retorna AWSBIA291I Total objects 1, atualizado 09/04/2026) sem composer add - replicando o achado WSL de que a ausencia de jobs apos JnextPlan -for 0000 e o horizonte zero, nao falta de importacao.

| Atributo | Valor |
| --- | --- |
| command | composer display js=MDMXA#FINAL && composer display js=MDMXA#FINALPOSTREPORTS && JnextPlan -for 0000 && JnextPlan -for 2400 && conman showjobs |
| Pre-condicoes | MDM 10.2.8 instalado (serverinst SUCCESS) com Sfinal em /opt/hwa/TWS/Sfinal (SCHEDULE EVERYDAY AT 2359, CARRYFORWARD); JnextPlan -for 0000 cria plano zero-duration sem instancias (mesmo comportamento do lab WSL hwa-lab-10.2.8-sfinal-plan-horizon-0007); FINAL: STARTAPPSERVER, MAKEPLAN, SWITCHPLAN (3 jobs); FINALPOSTREPORTS: CHECKSYNC, CREATEPOSTREPORTS, UPDATESTATS (3 jobs) no MDMXA |
| sanitized_output | composer display js=MDMXA#FINAL: 'Workstation MDMXA / Job Stream FINAL / Valid From - / Updated On 09/04/2026' + AWSBIA291I Total objects: 1. composer display js=MDMXA#FINALPOSTREPORTS: idem (Total objects 1). JnextPlan -for 0000 e -for 2400: AWSJCL074I Symphony loaded + AWSJCL066I statistics collected. conman showjobs apos -for 2400 fora do timing (01:0x, pos-run 2400 do dia): sem instancias FINAL (0). |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | non_mutating |
| Reversibilidade | NA (somente leitura/consulta) |
| Criterio de parada | Interromper se composer display nao encontrar os objetos (objetos ausentes = importacao falhou) |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Validacao documental: os 8 objetos (6 jobs + 2 streams) estao no banco importados pelo instalador em 09/04/2026 - o usuario reportou 'nao tem os jobs da Sfinal' ao olhar o plano; a causa e o horizonte do plano (JnextPlan -for 0000 = zero-duration; run 2400 = 23:59 do dia de producao), nao a ausencia das definicoes. O run 2400 validado FORA do timing (madrugada, apos o run do dia) processa com 0 Jobs Logged - reforcar no runbook: validar dentro do dia de producao ou no ciclo noturno automatico. |
| performed_at | 2026-09-04T22:12:02.724234-03:00 |


---

### 346. `hwa-lab-10.2.8-single-user-wauser-unification-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No padrao operacional e arquitetural do HWA 10.2.8, nao se criam multiplos usuarios de servico no SO para cada componente. Todos os componentes locais (TWS engine, netman, batchman, Liberty engineServer e Liberty dwcServer) sao unificados e vinculados exclusivamente ao usuario principal do produto no SO ('wauser'), mantendo a mesma credencial (usuario e senha) em todo o ecossistema. Apenas o SGBD (PostgreSQL) possui usuario e credencial proprios dedicados. No laboratorio container tws-hwa, o DWC foi reconfigurado para eliminar o usuario redundante 'dwcadmin': (1) O ownership de /opt/hwa/DWC e /opt/hwa/DWC/DWC_DATA foi atribuido a wauser:wauser; (2) /opt/hwa/DWC/appservertools/setEnv.sh foi ajustado para WA_USER=wauser; (3) /opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/configDropins/overrides/wauser_variables.xml foi atualizado com user.twsuser.id=wauser e a mesma senha encriptada {aes} do engine; (4) dwcServer foi iniciado com sucesso sob wauser (startAppServer.sh -direct) abrindo porta 9443 (HTTP 302 em /console/); (5) o usuario redundante dwcadmin foi removido do SO (userdel).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - DWC e Engine unificados sob usuario unico wauser:wauser; dwcServer rodando como wauser na porta 9443 (HTTP 302); dwcadmin removido do SO; CREDENCIAIS-LAB.env atualizado. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | chown -R wauser:wauser /opt/hwa/DWC; setEnv.sh WA_USER=wauser; dwcServer wauser_variables.xml user.twsuser.id=wauser; dwcServer PID rodando como wauser; porta 9443 HTTP 302; userdel dwcadmin |
| performed_at | 2026-09-08T09:05:07.772062-03:00 |
| performed_by | hermes-lab |


---

### 347. `hwa-lab-10.2.8-startofday-0005-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, a opção global startOfDay foi alterada de 0000 para 0005 com optman chg sd=0005; o comando retornou AWSJCL050I Command chg completed successfully e optman ls confirmou startOfDay / sd = 0005.

> **ATENCAO / RESSALVAS DE USO:** The active production plan was not regenerated in this action. Per HCL documentation, the change takes effect for plan processing after JnextPlan; no JnextPlan, SwitchPlan, ResetPlan, Sfinal replacement, or Symphony deletion was executed.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu |
| Status do conhecimento | observed_in_lab |
| Confianca | high |
| Fonte (URL) | local execution: optman chg sd=0005 and optman ls |
| Titulo da fonte | startOfDay 00:05 laboratory change |
| Citacao de suporte | AWSJCL050I Command "chg" completed successfully; startOfDay / sd = 0005 |
| Coletado em | 2026-08-21 |


---

### 348. `hwa-lab-10.2.8-startofday-0005-brt-anchor-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, America/Sao_Paulo), para o plano de producao nascer com o dia vigente iniciando as 00:05 BR e sempre D+1, o JnextPlan deve ser executado SEM o parametro -from (ou -from sem deslocar por timezone). Com optman sd=0005 e fuso America/Sao_Paulo, JnextPlan (sem -from) criou o plano com 'Plan creation start time: 09/05/2026 00:05 TZ America/Sao_Paulo' e 'Production plan end time: 09/06/2026 00:04'. O uso previo de 'JnextPlan -from 09/05/2026 0000' ancorava o inicio do dia de producao em 21:00 BR (heranca da meia-noite UTC do container original), deslocando o dia vigente 3h do calendario local; a doc (runbook WSL) adverte que -from sem timezone explicito pode ser deslocado na interpretacao. Aviso AWSJPL206W: timezones habilitados no banco mas o MDM nao inclui timezone - usa o do sistema.

| Atributo | Valor |
| --- | --- |
| Resultado observado | JnextPlan sem -from apos ResetPlan -scratch: Plan creation start time 09/05/2026 00:05 TZ America/Sao_Paulo; production plan 09/05 00:05 -> 09/06 00:04; preproduction ate 09/20 00:05; Run 19. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | JnextPlan sem -from: Plan creation start time: 09/05/2026 00:05 TZ America/Sao_Paulo; end 09/06/2026 00:04; com -from 0000 o inicio caia em 21:00 BR |
| performed_at | 2026-09-05T21:11:21.949458-03:00 |
| performed_by | hermes-lab |


---

### 349. `hwa-lab-10.2.8-timezone-sao-paulo-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container RHEL9 UBI9 (HWA 10.2.8, tws-hwa.lab), o timezone do SO foi alterado de UTC para America/Sao_Paulo via ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime + /etc/timezone, fazendo `date` passar de 'Sat Sep 5 03:13:08 UTC' para 'Sat Sep 5 00:13:08 -03'. Achado operacional: o dominio MDM roda como processos manuais nao-systemd (engineServer Java Liberty iniciado 04/09 22:06 UTC, netman ppid=1), orquestrados pelo agente ITA (unit tebctl-tws_cpa_agent_wauser.service) e pelo /opt/hwa/TWS/config/start_tws.sh, que condiciona o start do netman (conman 'start&link @!/@/@;noask') a existencia de arquivo Symphony (ausente no 10.2.8, plano no banco). Logo, trocar /etc/localtime nao efetiva timezone nos processos do MDM ja em memoria (engineServer Java mantem TZ de boot); so vale para processos novos; para valer 100% exige reiniciar o dominio.

| Atributo | Valor |
| --- | --- |
| Resultado observado | date passou de 'Sat Sep 5 03:13:08 UTC' para 'Sat Sep 5 00:13:08 -03' (America/Sao_Paulo). Processos do MDM (engineServer 169384, netman 170438) seguem com TZ de boot (UTC) em memoria ate reiniciar o dominio. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | date antes: Sat Sep 5 03:13:08 UTC | date depois: Sat Sep 5 00:13:08 -03 | unit: tebctl-tws_cpa_agent_wauser.service (ExecStart tebctl-tws_cpa_agent_wauser start) | start_tws.sh: condiciona netman a $DHOME/Symphony | default pos-instalacao: UTC |
| performed_at | 2026-09-05T00:14:06.530381-03:00 |
| performed_by | hermes-lab |


---

### 350. `hwa-lab-10.2.8-trilha3-edwa-failover-scope-constraints-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab, plano #22), a topologia atual tem um unico Master Domain Manager (MDM, tipo *UNIX MASTER) e agentes (MDMDA UNIX AGENT, MDMXA X-AGENT, broker MDM_DWB, pools LABPOOL/MASTERAGENTS); nao ha backup master domain manager nem fault-tolerant agent full-status configurado. Consequentemente, um teste empirico honesto de 'conman switchmgr' para failover MDM->BMDM nao pode ser executado neste ambiente: o comando exige um segundo engine (BMDM) elegivel que nao existe na topologia. O corpus/claims de failover (hwa-10.2.8-ha-switchmgr-0001, hwa-10.2.8-globalopts-enautomaticfailover-0001) permanecem validos como conhecimento oficial/documentado (evidence_tier official_primary), mas NAO devem ser rotulados 'lab_validated' sem um segundo engine.

| Atributo | Valor |
| --- | --- |
| Resultado observado | REJECTED |
| Classificacao de risco | read_only |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-08T18:30:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | conman sc: MDM *UNIX MASTER; MDMDA UNIX AGENT; MDMXA X-AGENT; MDM_DWB BROKER; LABPOOL/MASTERAGENTS POOL. Nenhuma workstation tipo BACKUP MASTER/FTA full-status. |
| observations | Validar switchmgr/failover exige provisionar um BMDM ou FTA full-status e um banco espelhado; fica como pendencia de lab (trilha futura) e como claim oficial_primary, nao lab_validated. |


---

### 351. `hwa-lab-10.2.8-trilha3-edwa-failover-scope-constraints-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No container HWA 10.2.8 (tws-hwa.lab), o event processing engine esta ATIVO: o processo ssmagent.bin roda (pid ssmagent.bin -f /opt/hwa/TWSDATA/EDWA/ssm/config e -f /opt/hwa/TWSDATA/ssm/config) e a porta EIF SSL 31131 esta em LISTEN (globalopts: enEventDrivenWorkloadAutomation ed=YES, enEventProcessorHttpsProtocol eh=YES, eventProcessorEIFSSLPort ef=31131). Porem, o utilitario CLI 'evtdef' nao consegue concluir dumpdef/loaddef contra 127.0.0.1:31131: retorna AWSBEH023E/AWSBEH029E (unable to communicate / SSL connection fails) tanto sem -protocol quanto com -protocol https. Diagnostico: o cliente evtdef nao possui a truststore/certificado de cliente necessario para o handshake TLS com o event processor (que usa HTTPS). Logo, a manipulacao de definicoes de eventos via CLI (evtdef loaddef/dumpdef) esta bloqueada neste ambiente ate que a confianca TLS do cliente seja configurada, embora o event engine em si esteja operacional.

| Atributo | Valor |
| --- | --- |
| Resultado observado | PARTIAL |
| Classificacao de risco | read_only |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-08T18:31:00BRT |
| performed_by | hermes-agent-hwa |
| sanitized_output | ssmagent.bin em execucao (2 configs); ss -tlnp mostra *:31131 LISTEN (java, engine); optman: ed=YES eh=YES ef=31131; evtdef -host 127.0.0.1 -port 31131 [-protocol https] dumpdef -> AWSBEH023E + AWSBEH029E (SSL handshake do cliente falha). |
| observations | O achado real e bloqueio de TLS do cliente evtdef (truststore/cert ausente), NAO engine desligado. Registra-se PARTIAL: engine ativo e porta EIF SSL 31131 ouvindo, mas CLI de eventos sem truststore de cliente. Para validacao E2E de EDWA/FileMonitor, configurar a confianca TLS do cliente (ou usar o caminho via banco/DWC) e depois disparar o evento. |


---

### 352. `hwa-lab-10.2.8-twsinst-aes-clean-each-rerun-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Cada rerun do twsinst HWA 10.2.8 que passa por runSecurityEncryption RECRIA key.p12/key.sth em <DATA_DIR>/TWSDATA/ssl/aes/; o rerun seguinte falha com 'A file named key.p12 already exists' - a limpeza do diretorio aes/ e prerequisito de CADA rerun, nao apenas do primeiro apos a falha original.

| Atributo | Valor |
| --- | --- |
| command | rm -f /opt/hwa/TWSDATA/ssl/aes/key.p12 /opt/hwa/TWSDATA/ssl/aes/key.sth && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./twsinst -new -inst_dir /opt/hwa -agent both -addjruntime true -jmport 31114 -hostname tws-hwa.lab -displayname MDMDA -port 31111 -netmansslport 31113 -thiscpu MDM -master MDM -company LAB -tdwbhostname tws-hwa.lab -tdwbport 31116 -data_dir /opt/hwa/TWSDATA -wauser wauser -wapassword REDACTED -acceptlicense yes -uname wauser -lang C -caller MDM -work_dir /tmp/wa10.2.8.00 -sslpassword REDACTED -sslkeysfolder /opt/ssl-certs -useencryption true -encryptionpassword REDACTED |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init; Sequencia: rerun2 passou por runSecurityEncryption (criou key.p12) e falhou no makesec (libcrypt); apos libxcrypt-compat, rerun3 falhou na runSecurityEncryption com 'key.p12 already exists'; Key.p12/key.sth recriados a cada passagem pela fase AWSFAB474I Run security scripts; Fase AWSFAB601I Import certificates conclui OK (EXIT 0) antes da falha |
| sanitized_output | runSecurityEncryption: generating ssl password .../ssl/aes/key.sth ... generating encrypt keystore file .../ssl/aes/key.p12 ... Unable to create the PKCS#12 file '.../key.p12'. A file named '.../key.p12' already exists. ACTION STEP: AWSFAB474I Run security scripts. EXIT VALUE: 1. |
| Resultado observado | FAIL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | rm dos residuos aes antes de cada rerun do twsinst |
| Criterio de parada | Interromper apos instalacao completar ou falha em passo novo |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Padrao confirmado em 2 ciclos: toda execucao que alcanca runSecurityEncryption deixa key.p12+key.sth; o gerador PKCS#12 nunca sobrescreve. Loop de instalacao: limpar aes/ + rerun. Rerun4 lancado apos limpeza com libxcrypt-compat ja instalado (makesec deve passar agora). |
| performed_at | 2026-09-04T18:59:25.815503-03:00 |


---

### 353. `hwa-lab-10.2.8-twsinst-flags-mutual-exclusion-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 (twsinst LINUX_X86_64), foram validadas empiricamente no container as 4 regras críticas de consistência e exclusão mútua de flags: (1) Rejeição de -displayname iniciando com dígito (AWSFAB010E 'An incorrect value has been supplied for a parameter. The parameter must be as follows: -displayname <agent-name>'); (2) Rejeição de valores idênticos para -thiscpu e -displayname em instalação do tipo -agent both (AWSFAB164E 'The values specified for -thiscpu and -displayname cannot be the same'); (3) Exclusão mútua entre -sslkeysfolder e -wauser quando -jwt false (AWSFAB486E 'The parameter: -sslkeysfolder is mutually exclusive with the parameter: -wauser'); (4) Exigência mandatória de ao menos um método de segurança/credencial entre sslkeysfolder, wauser/wapassword ou apikey (AWSFAB502E 'Specify either the sslkeysfolder and sslpassword parameters, or the wauser and wapassword parameters, or apikey parameter').

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | read_only |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent) |
| Versao do produto | 10.2.8 |
| performed_at | 2026-09-09T06:30:00BRT |
| performed_by | hermes-agent-hwa |
| tested_commands | ./twsinst -new -acceptlicense yes -uname wauser -apikey dummy -displayname 1AGT; ./twsinst -new -acceptlicense yes -uname wauser -agent both -tdwbhostname tws-hwa.lab -tdwbport 31116 -apikey dummy -thiscpu TESTCPU -displayname TESTCPU; ./twsinst -new -acceptlicense yes -uname wauser -agent dynamic -tdwbhostname tws-hwa.lab -tdwbport 31116 -sslkeysfolder /opt/agent-ssl -sslpassword LabPass -wauser wauser -wapassword Pass -jwt false; ./twsinst -new -acceptlicense yes -uname wauser -agent dynamic -tdwbhostname tws-hwa.lab -tdwbport 31116 -jwt false |
| sanitized_output | Comprovados códigos AWSFAB010E, AWSFAB164E, AWSFAB486E e AWSFAB502E conforme esperado. |
| observations | Todas as 52 flags do script twsinst foram mapeadas no runbook data/runbooks/twsinst-flags-complete-reference.md com base na leitura direta do código shell e documentação oficial HCL. |


---

### 354. `hwa-lab-10.2.8-twsinst-keystore-residue-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Reexecucao do twsinst HWA 10.2.8 apos falha parcial falha em runSecurityEncryption (AWSFAB474I) porque o keystore AES ja existe: 'Unable to create the PKCS#12 file ... A file named key.p12 already exists' - a ferramenta nao sobrescreve; remover os residuos key.p12/key.sth em <DATA_DIR>/TWSDATA/ssl/aes/ antes do rerun.

| Atributo | Valor |
| --- | --- |
| command | rm -f /opt/hwa/TWSDATA/ssl/aes/key.p12 /opt/hwa/TWSDATA/ssl/aes/key.sth && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./twsinst -new -inst_dir /opt/hwa -agent both -addjruntime true -jmport 31114 -hostname tws-hwa.lab -displayname MDMDA -port 31111 -netmansslport 31113 -thiscpu MDM -master MDM -company LAB -tdwbhostname tws-hwa.lab -tdwbport 31116 -data_dir /opt/hwa/TWSDATA -wauser wauser -wapassword REDACTED -acceptlicense yes -uname wauser -lang C -caller MDM -work_dir /tmp/wa10.2.8.00 -sslpassword REDACTED -sslkeysfolder /opt/ssl-certs -useencryption true -encryptionpassword REDACTED |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init; Execucao parcial anterior (falha no cmp) deixou key.p12 (515 bytes) e key.sth (12 bytes) em /opt/hwa/TWSDATA/ssl/aes/; diffutils ja instalado (cmp OK nesta execucao); importAgentCert.sh completou (EXIT 0); falha em runSecurityEncryption (EXIT 1) |
| sanitized_output | generating ssl password .../ssl/aes/key.sth ... generating encrypt keystore file .../ssl/aes/key.p12 ... Unable to create the PKCS#12 file '.../key.p12'. A file named '.../key.p12' already exists. runSecurityEncryption: generating encrypt keystore file ... completed with error: 1. ACTION STEP: AWSFAB474I Run security scripts. EXIT VALUE: 1. |
| Resultado observado | FAIL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | rm dos residuos aes (key.p12, key.sth) e reexecucao do twsinst |
| Criterio de parada | Interromper se o rerun falhar em outro passo apos limpeza |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Residuo de execucao parcial impede o rerun do twsinst: o gerador de keystore PKCS#12 nao sobrescreve arquivo existente. key.p12 criado na execucao anterior tinha 515 bytes (timestamp 21:52 = 2a execucao) e key.sth 12 bytes (21:55 = tentativa atual) - mistura de estados. Limpeza aplicada e rerun lancado. |
| performed_at | 2026-09-04T18:56:50.151010-03:00 |


---

### 355. `hwa-lab-10.2.8-twsinst-libcrypt-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No RHEL 9, o comando makesec do HWA 10.2.8 falha na fase AWSFAB068I (Completing the installation) com rc=127: 'makesec: error while loading shared libraries: libcrypt.so.1: cannot open shared object file'. O RHEL 9 nativo tem libcrypt.so.2; o pacote libxcrypt-compat fornece libcrypt.so.1 exigida pelos binarios HWA.

| Atributo | Valor |
| --- | --- |
| command | dnf install -y libxcrypt-compat && cd /installers/mdm-extracted/TWS/LINUX_X86_64 && umask 022 && ./twsinst -new -inst_dir /opt/hwa -agent both -addjruntime true -jmport 31114 -hostname tws-hwa.lab -displayname MDMDA -port 31111 -netmansslport 31113 -thiscpu MDM -master MDM -company LAB -tdwbhostname tws-hwa.lab -tdwbport 31116 -data_dir /opt/hwa/TWSDATA -wauser wauser -wapassword REDACTED -acceptlicense yes -uname wauser -lang C -caller MDM -work_dir /tmp/wa10.2.8.00 -sslpassword REDACTED -sslkeysfolder /opt/ssl-certs -useencryption true -encryptionpassword REDACTED |
| Pre-condicoes | HWA 10.2.8, container RHEL 9.8 UBI-init (Docker); Falhas anteriores resolvidas: diffutils (cmp), residuos de keystore aes; Certificados importados OK (TWSClientKeyStore.p12 criado), falha em AWSFAB068I Completing the installation; makesec -l Security.conf falhou por libcrypt.so.1 ausente |
| sanitized_output | ACTION STEP: AWSFAB068I Completing the installation. EXIT VALUE: 127. STANDARD ERROR: makesec: error while loading shared libraries: libcrypt.so.1: cannot open shared object file: No such file or directory. The following command failed: makesec -l Security.conf. |
| Resultado observado | FAIL |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | dnf install libxcrypt-compat e reexecucao do twsinst |
| Criterio de parada | Interromper se o rerun falhar em outro passo |
| performed_by | hermes-lab (container tws-hwa) |
| observations | Binarios HWA 10.2.8 linkados contra libcrypt.so.1 (glibc/libxcrypt antigo). Ubuntu 22.04 (lab WSL) fornece libcrypt.so.1 nativamente - por isso nao apareceu la. No RHEL 9 e necessario o pacote de compatibilidade libxcrypt-compat. Apos instalacao, rerun lancado. |
| performed_at | 2026-09-04T18:57:58.377992-03:00 |


---

### 356. `hwa-lab-10.2.8-vartable-resolution-and-missing-behavior-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No laboratorio container HWA 10.2.8 (tws-hwa.lab), a definicao de VARIABLE TABLE (VARTABLE), a atribuicao em job streams e o mecanismo de resolucao em tempo de submissao/execucao foram comprovados de ponta a ponta: (1) Sintaxe do composer: uma tabela de variaveis e definida como objeto standalone 'VARTABLE <nome> DESCRIPTION ... MEMBERS <var1> <valor1> ... END' (adicionada com AWSJCL003I). Nao se mistura a definicao da tabela com o schedule no mesmo arquivo sem separador de objeto (causa AWSJOM915E unexpected token SCHEDULE). (2) No job stream, a clausula 'VARTABLE <nome>' deve obrigatoriamente preceder a clausula 'ON RUNCYCLE' (ordem rigorosa de gramatica do composer). (3) Resolucao com caret (^VAR^): variaveis definidas na tabela sao substituidas no DOCOMMAND durante a expansao do JCL (comprovado: 'echo Var is ^LAB_MSG^ and port is ^LAB_PORT^' foi expandido para 'echo Var is MSG_VAL_CONTAINER_RHEL9 and port is 9090' no JCLFILE do jobmanrc e executado com SUCC rc 0, #J232316). (4) COMPORTAMENTO CRITICO DE VARIAVEL INEXISTENTE: quando um job nativo referencia uma variavel com caret que nao existe na VARTABLE vinculada (ex: ^VAR_QUE_NAO_EXISTE^), o scheduler NAO bloqueia o submit nem gera erro de sintaxe; em vez disso, o HWA preserva a string com caret literal no JCLFILE ('echo Var is ^VAR_QUE_NAO_EXISTE^') e executa o job normalmente (SUCC rc 0, #J232318) — o que significa que variaveis inexistentes passam silenciosamente para o script de execucao como strings literais em vez de causar abend de validacao.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS - VARTABLE LAB_VAR_TBL criada, resolucao caret ^VAR^ comprovada em producao, e descoberto que variaveis ausentes permanecem como literais sem abend do scheduler. |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; RHEL9 UBI9 container (ubi9/ubi-init) |
| Classificacao de risco | low |
| sanitized_output | composer add VARTABLE LAB_VAR_TBL; JS_VARTABLE_OK -> JCLFILE: echo Var is MSG_VAL_CONTAINER_RHEL9 and port is 9090 (SUCC rc 0); JS_VARTABLE_ERR -> JCLFILE: echo Var is ^VAR_QUE_NAO_EXISTE^ (literal string preserved, SUCC rc 0) |
| performed_at | 2026-09-08T12:45:19.801072-03:00 |
| performed_by | hermes-lab |


---

### 357. `hwa-lab-10.2.8-wauser-login-profile-env-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em container RHEL 9.8 UBI, o login do usuario de instalacao (wauser) nao carregava o environment do HWA (conman: command not found) porque o useradd do UBI cria /home/<user>/.bash_profile, que MASCCARA o .profile - o source do tws_env.sh deve ir no .bash_profile (diferente do WSL2 Ubuntu, onde o useradd nao cria .bash_profile e o runbook usou .profile).

| Atributo | Valor |
| --- | --- |
| command | cat >> /home/wauser/.bash_profile <<EOF ... if [ -f /opt/hwa/TWS/tws_env.sh ]; then . /opt/hwa/TWS/tws_env.sh; fi ... EOF (mesmo padrao para dwcadmin com /opt/hwa/DWC/dwc_env.sh) |
| Pre-condicoes | MDM 10.2.8 instalado em /opt/hwa/TWS com tws_env.sh (gera 'HCL Workload Scheduler Environment Successfully Set'); wauser criado via useradd -m -s /bin/bash (UBI: cria .bash_profile default de 141 bytes que sourcea .bashrc); Estado do bug: su - wauser -c 'conman showcpus' -> bash: conman: command not found |
| sanitized_output | su - wauser -c 'conman showcpus' -> 'HCL Workload Scheduler Environment Successfully Set !!!' + banner CONMAN build 20260723, Installed for user wauser; CPUID MDM (*UNIX MASTER) e MDMXA (OTHR X-AGENT) listados. TWS_TISDIR=/opt/hwa/TWS. |
| Resultado observado | SUCCESS |
| Versao do produto | 10.2.8.00 |
| Plataforma | Distributed; Linux x86_64; container RHEL 9.8 UBI9 (ubi-init, systemd) |
| Classificacao de risco | mutating |
| Reversibilidade | Remover o bloco adicionado ao .bash_profile (backup .bash_profile.bak) |
| Criterio de parada | Interromper se o login shell do wauser falhar apos o source (testar su - wauser -c 'conman showcpus') |
| performed_by | hermes-lab (container tws-hwa) |
| observations | O ssh com comando direto (ssh host 'comando') NAO le login profile - usar sessao interativa ou bash -lc. A causa raiz e a diferenca de distro: UBI useradd cria .bash_profile (mascara .profile), Ubuntu/WSL nao. Tambem aplicado dwc_env.sh ao .bash_profile do dwcadmin (DWC). |
| performed_at | 2026-09-04T20:43:16.698290-03:00 |


---

### 358. `hwa-lab-10.2.8-wauser-sudo-0051`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `security`

**Afirmacao / Conteudo:**

In the HWA laboratory, user wauser is NOT in sudoers; sudo -l -U wauser returns 'not allowed to run sudo'. Test scripts in /home/wauser/bin (fail_stop.sh, fail_continue.sh, rerun_once.sh, lab_ls.sh) run as wauser directly because they are owned by wauser:wauser with mode 755. No sudo is required for the HWA laboratory scripts.

> **ATENCAO / RESSALVAS DE USO:** wauser does not need sudo for the laboratory; HWA user environment is loaded via /opt/hwa/TWS/tws_env.sh. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local sudo -l -U wauser and id wauser

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | wauser sudo permissions |
| Citacao de suporte | User wauser is not allowed to run sudo on DESKTOP-298GT47. Scripts run as wauser directly. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | user_permissions |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (WSL2 Ubuntu 22.04), tested_commands=['rerun'], result=User wauser is not allowed to run sudo on DESKTOP-298GT47. Scripts run as wauser directly. | wauser does not need sudo for the laboratory; HWA user environment is loaded via /opt/hwa/TWS/tws_env.sh., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-wauser-sudo.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=security_policy |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, user wauser is NOT in sudoers; sudo -l -U wauser returns 'not allowed to run sudo'?


---

### 359. `hwa-lab-9.4.0-switchplan-db-cpu-contention-0207`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Contributing root cause reported by the DBA team: the TWS database server was under high CPU load during the incident window. This is consistent with DB-side lock contention blocking the planman confirm transaction and keeping SWITCHPLAN in EXEC for 10+ hours. Combined with enWorkloadServiceAssurance (wa) already NO, the operative failure chain was: DB server high CPU -> lock contention / slow transaction -> planman confirm hung -> SWITCHPLAN job stuck EXEC -> workstations not restarted (UNLINK).

> **ATENCAO / RESSALVAS DE USO:** Second-hand report (DBA); quantitative CPU evidence (graphs/snapshots) not captured in this dataset - confidence medium. Database vendor: Oracle (administered by a separate team; operator has no direct DB access). Preventive direction for Oracle: request from the DBA team (1) an AWR report for the incident window (top SQL by CPU/elapsed, top timed events, blocking sessions), (2) confirmation of whether the Oracle automatic statistics gathering job (default 22:00-02:00 window) ran during the plan switch and whether the TWS schema is in its set, (3) RMAN backup/dataguard/export activity in the same window, (4) blocking-session analysis (v$session, dba_blockers/dba_waiters, v$locked_object) for the planman session, (5) undo/temp sizing for the plan-generation transaction. Exclude the TWS plan tables from the stats window and keep heavy DB jobs out of the JnextPlan window.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | DBA team report on 2026-09-04 (DB server CPU load during incident window) |
| Titulo da fonte | DB server high CPU load as contributing cause |
| Citacao de suporte | DBA report: TWS database server under high CPU load at incident time; DB lock blocking planman confirm. |
| Coletado em | 2026-09-04 |


---

### 360. `hwa-lab-9.4.0-switchplan-db-lock-confirm-0201`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Root cause chain of the hung switch: the plan switch had advanced to the planman confirm stage but the confirm could not commit because the plan database was locked; the FINAL/SWITCHPLAN wrapper remained in EXEC while the confirm was blocked. This is the documented IBM pattern of APAR IV89990 (PLANMAN CONFIRM HANGS), in which 'planman -timeout 3600 confirm' hangs and the Final SwitchPlan job keeps executing.

> **ATENCAO / RESSALVAS DE USO:** DB lock observed on the MDM required planman unlock. The stale-EXEC behavior persisted even after the confirm had effectively succeeded, matching the IV89990 symptom pattern. IBM APAR IV89990 abstract verified on 2026-09-04 (https://www.ibm.com/support/pages/apar/IV89990): 'TWS Final SwitchPlan job stays executing due to hung process: planman -timeout 3600 confirm'; product IBM Workload Scheduler, version registered 9L3 (9.3). Caveat: the full APAR fix-pack list is login-gated and was NOT verified here; per unverified community summary the fix shipped in 9.4 FP1 and later cumulative fix packs, which would imply 9.4.0.6 (FP6) already contains it - confirm exact fix-pack inclusion with HCL/IBM before attributing a new hang to an unfixed IV89990. Reported official interim mitigation for affected pre-fix levels: disable Workload Service Assurance (optman chg wa=NO) - unverified in this dataset.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/apar/IV89990 |
| Titulo da fonte | IBM APAR IV89990 - PLANMAN CONFIRM HANGS |
| Citacao de suporte | TWS Final SwitchPlan job stays executing due to hung process: planman -timeout 3600 confirm. |
| Coletado em | 2026-09-04 |


---

### 361. `hwa-lab-9.4.0-switchplan-exec-hung-0200`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

On the IBM Workload Scheduler 9.4.0.6 production Master Domain Manager, the SWITCHPLAN job (final step of the daily plan switch, FINAL job stream) remained in EXEC for over 10 hours. Throughout the whole period all workstations appeared UNLINK while the current plan (conman sc) already showed today's date: the plan window had been extended but no workstation had received/restarted on the new Symphony run.

> **ATENCAO / RESSALVAS DE USO:** Real production incident, IBM TWS 9.4.0.6 (pre-HCL branding). Symptom collected before any intervention. Cross-refs canonical claims hwa-10.2.8-incident-switchplan-confirm-0057 and hwa-official-message-10.2.8-0006 (same symptom family documented for 10.2.8).

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | conman sc / conman showcpus on production MDM (9.4.0.6) |
| Titulo da fonte | SWITCHPLAN hung in EXEC with all workstations UNLINK |
| Citacao de suporte | SWITCHPLAN in EXEC >10h; conman sc shows plan date = today while all workstations are UNLINK. |
| Coletado em | 2026-09-04 |


---

### 362. `hwa-lab-9.4.0-switchplan-final-resolution-0206`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Final resolution of the stale EXEC on 9.4.0.6: the hung OS process 'planman -timeout 3600 confirm' was still alive (found via ps -ef) while planman showinfo already reported Run number 6110 == Confirm run number 6110 - i.e. the confirm had committed and the process was a post-commit hang (APAR IV89990 signature). The process was killed (kill then kill -9); the SWITCHPLAN job then left EXEC and was reconciled with 'conman confirm <job>;succ' since the plan switch had effectively completed. No ResetPlan was required; planman showinfo remained 6110/6110.

> **ATENCAO / RESSALVAS DE USO:** Kill was safe because the confirm had already committed (run == confirm 6110) and planman unlock had freed the DB lock earlier. conman kill would NOT have worked (documented as ignored for EXEC jobs); the target was the OS process. Marking SWITCHPLAN SUCC unblocked the FINALPOSTREPORTS chain.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | local recovery executed on 2026-09-04 on production MDM (9.4.0.6) |
| Titulo da fonte | Kill hung planman confirm + confirm job SUCC |
| Citacao de suporte | ps -ef: planman -timeout 3600 confirm alive; after kill, SWITCHPLAN left EXEC; conman confirm <job>;succ -> SUCC. |
| Coletado em | 2026-09-04 |


---

### 363. `hwa-lab-9.4.0-switchplan-iv89990-diagnostic-0204`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Diagnostic rule confirmed in production 9.4.0.6: a SWITCHPLAN job stuck in EXEC with all workstations unlinked does NOT by itself indicate plan corruption. If planman showinfo shows Run number == Confirm run number, workstations are linked on the same run as the MDM and jobs dispatch/complete, the plan switch COMPLETED and the EXEC status is a stale wrapper artifact (APAR IV89990). Do NOT rerun SwitchPlan/Stageman (risk of AWSBHV082E same-run-number merge failure), do NOT start a second JnextPlan (risk of AWSJPL017E), and do NOT use ResetPlan -scratch as a routine response. Only if Confirm run number = Run number - 1 is the confirm genuinely uncommitted and the documented AWSJCL054E recovery applies (analyze messages.log, then rerun planman confirm and conman confirm).

> **ATENCAO / RESSALVAS DE USO:** Production confirmation of the guidance in runbook data/runbooks/recovery-jnextplan.md and claims hwa-10.2.8-incident-switchplan-confirm-0057 / hwa-official-message-10.2.8-0006. IV89990 attribution here is at the SYMPTOM-PATTERN level (plan confirmed but SWITCHPLAN job stays EXEC); the active root cause in this instance was the DB lock blocking planman confirm, not a proven unfixed product defect. Fix-pack inclusion of IV89990 in 9.4.0.6 (FP6) is UNVERIFIED (IBM full APAR is login-gated). Engage HCL/IBM support citing IV89990 to (a) confirm whether the running 9.4.0.6 (FP6) build contains the fix and (b) get supported guidance to clear the stale EXEC before a later JnextPlan cycle if it persists. If the hang recurs and the build predates the fix, the reported interim mitigation is disabling Workload Service Assurance (optman chg wa=NO) under change control.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/support/pages/apar/IV89990 |
| Titulo da fonte | Stale EXEC vs uncommitted confirm discrimination |
| Citacao de suporte | Run number 6110 == Confirm run number 6110 -> switch completed; treat remaining EXEC as artifact, do not replay the switch. |
| Coletado em | 2026-09-04 |


---

### 364. `hwa-lab-9.4.0-switchplan-lessons-0208`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Operational lessons consolidated from the 2026-09-04 incident (9.4.0.6 EOL, Oracle): (1) A SWITCHPLAN job left in EXEC with the plan already confirmed (Run number == Confirm run number) does NOT block the next JnextPlan - the stale instance is archived with the old Symphony during stageman and the next FINAL/SWITCHPLAN starts as a new instance; AWSJPL017E is triggered by an unfinished planner operation, not by a job in EXEC. (2) conman kill is documented as ignored for jobs in EXEC - the recovery target is the hung OS process 'planman -timeout 3600 confirm' (APAR IV89990 signature); once the confirm has committed, killing that process frees the job, which is then reconciled with 'conman confirm <job>;succ'. (3) FINALPOSTREPORTS starts only after SWITCHPLAN completes successfully, so leaving the reconciled job in ABEND would suppress the post-processing chain. (4) Do NOT rerun SwitchPlan/Stageman (AWSBHV082E same-run-number merge risk), do NOT start a second JnextPlan (AWSJPL017E risk) and do NOT use ResetPlan -scratch as routine. (5) Operative failure chain of this incident: Oracle DB server high CPU -> lock contention -> planman confirm hung -> SWITCHPLAN EXEC for 10h -> workstations UNLINK.

> **ATENCAO / RESSALVAS DE USO:** Lesson claim aggregating semantics validated during the incident and against IBM AWSJCL054E / APAR IV89990 / HCL AWSJPL017E references. Runbooks generated from this evidence: data/runbooks/recovery-switchplan-stale-exec.md and data/runbooks/checklist-jnextplan-eol.md.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | consolidated from local recovery and official IBM/HCL references (2026-09-04) |
| Titulo da fonte | Consolidated operational lessons |
| Citacao de suporte | Stale EXEC does not block next JnextPlan; kill target is the hung planman OS process; reconcile with conman confirm <job>;succ. |
| Coletado em | 2026-09-04 |


---

### 365. `hwa-lab-9.4.0-switchplan-recovery-start-unlock-0202`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Recovery for the hung switch on 9.4.0.6: issuing conman start plus planman unlock on the MDM re-established the scheduling network - workstations linked again on the current plan run. No destructive plan operation was required: no ResetPlan, no second JnextPlan, no SwitchPlan rerun, no process kill.

> **ATENCAO / RESSALVAS DE USO:** conman start releases the restart/distribution phase of the switch; planman unlock clears the DB lock blocking planman confirm. Consistent with runbook data/runbooks/recovery-jnextplan.md (unlock before any reset decision).

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | local recovery executed on 2026-09-04 on production MDM (9.4.0.6) |
| Titulo da fonte | Recovery: conman start + planman unlock |
| Citacao de suporte | conman start + planman unlock -> workstations LINKED on the current plan run. |
| Coletado em | 2026-09-04 |


---

### 366. `hwa-lab-9.4.0-switchplan-validated-run6110-0203`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Validation of the recovered switch on 9.4.0.6: planman showinfo reported Run number 6110 equal to Confirm run number 6110 (plan generated AND successfully confirmed); conman sc showed every workstation on the same run number 6110 as the MDM; a job rerun on a workstation completed SUCCESSFULLY, confirming end-to-end production health.

> **ATENCAO / RESSALVAS DE USO:** Equal run/confirm-run plus matching workstation run numbers is the objective success criterion. The SWITCHPLAN job remained EXEC after recovery (stale wrapper artifact, see IV89990) without affecting production.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | planman showinfo and conman sc output on production MDM (9.4.0.6) |
| Titulo da fonte | Plan/network consistency check after recovery |
| Citacao de suporte | Run number: 6110; Confirm run number: 6110; all workstations on run 6110; job rerun completed SUCCESSFULLY. |
| Coletado em | 2026-09-04 |


---

### 367. `hwa-lab-9.4.0-switchplan-wsa-disabled-0205`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

On the incident MDM (IBM Workload Scheduler 9.4.0.6), the global option enWorkloadServiceAssurance (short name wa) was already disabled: optman ls / optman show wa reports wa=NO. No optman chg was executed during the recovery (only conman start and planman unlock), so the option was already NO when the SWITCHPLAN hang occurred. Consequence: the Workload Service Assurance rule-processing mechanism attributed to APAR IV89990 is ruled out as the hang mechanism in this instance, and the documented interim workaround (optman chg wa=NO) does not apply; the DB lock blocking planman confirm remains the active root cause.

> **ATENCAO / RESSALVAS DE USO:** Alias wa for enWorkloadServiceAssurance verified against official IBM 9.4 documentation (optman reference and global options summary). 'ws' is NOT a global option short name - it is a licenseType value (ws=perServer, wa=perJob); optman chg ws=NO is invalid. Operator-confirmed on 2026-09-04: wa was already NO before the incident started; no optman chg was performed at any point during the incident.

| Atributo | Valor |
| --- | --- |
| Produto | IBM Workload Scheduler |
| Versao | 9.4.0.6 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | optman ls / optman show wa on production MDM (9.4.0.6) |
| Titulo da fonte | WSA global option state at incident time |
| Citacao de suporte | enWorkloadServiceAssurance (wa) = NO; no optman chg executed during the incident. |
| Coletado em | 2026-09-04 |


---

### 368. `hwa-official-10.2.8-fence-priority-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

In HCL Workload Automation, `fence` prevents jobs whose priority is less than or equal to the fence from launching, regardless of the job-stream priority. Fence accepts 0 through 99, HI, GO or SYSTEM; SYSTEM sets the fence to zero.

> **ATENCAO / RESSALVAS DE USO:** A high-priority job stream does not by itself bypass a workstation fence.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgfence.html |
| Titulo da fonte | fence |
| Citacao de suporte | Jobs are not launched on the workstation if their priorities are less than or equal to the job fence ... Entering system sets the job fence to zero. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | capacity_fence |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=capacity |
| Status de revisao | verified |
| Tipo | other |
| Familia | 10.2.8-fence |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In HCL Workload Automation, `fence` prevents jobs whose priority is less than or equal to the fence from launching, regardless of the job-stream priority?


---

### 369. `hwa-official-10.2.8-limit-fence-carryforward-0033`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

HCL Workload Automation documents that changes to workstation job limit and fence are carried forward during preproduction processing to the next day's production plan.

> **ATENCAO / RESSALVAS DE USO:** Validate the effective value after plan generation, not only the temporary current-plan value.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html |
| Titulo da fonte | limit cpu and workstation controls |
| Citacao de suporte | When you change the limit, it is carried forward during preproduction processing to the next day's production plan. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | capacity_limit_fence |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=capacity |
| Status de revisao | verified |
| Tipo | other |
| verbs | limit; plan |
| Familia | 10.2.8-limit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HCL Workload Automation documents that changes to workstation job limit and fence are carried forward during preproduction processing to the next day's production plan?


---

### 370. `hwa-official-cycle-10.2.8-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `plan`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, MakePlan replana ou estende o preproduction plan e produz Symnew. Context: MakePlan performs ... Replans or extends the preproduction plan. Produces the Symnew file.

> **ATENCAO / RESSALVAS DE USO:** Official v1028 page; the standalone MakePlan reference page (awsrgmakeplan.html) does not exist in v1028 - content lives in 'Creating and extending the production plan' (awsrgprepostcom.html) and Troubleshooting 'MakePlan problems'.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmakeplan.html |
| Titulo da fonte | MakePlan problems |
| Citacao de suporte | MakePlan performs the following actions: Replans or extends the preproduction plan. Produces the Symnew file. |
| Coletado em | 2026-08-18 |
| Capacidade | makeplan |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=plan |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | planner |
| verbs | plan |
| Familia | cycle-10.2.8 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, MakePlan replana ou estende o preproduction plan e produz Symnew?


---

### 371. `hwa-official-message-10.2.8-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `error`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, AWSJPL006E indica que um objeto do banco não pôde ser carregado e a página aponta conexão quebrada com o banco. Context: This error means that a connection with the database is broken.

> **ATENCAO / RESSALVAS DE USO:** Verified verbatim on the official v1028 Troubleshooting page (message text 'A database object "xxxx" cannot be loaded from the database' also matches).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmakeplan6.html |
| Titulo da fonte | An internal error has occurred - AWSJPL006E |
| Citacao de suporte | This error means that a connection with the database is broken. |
| Coletado em | 2026-08-18 |
| Capacidade | error |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSJPL006E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSJPL006E |
| Familia | message-10.2.8 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL006E no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL006E no HWA?
- Qual é o significado da mensagem de erro AWSJPL006E no HWA e qual ação é recomendada?


---

### 372. `hwa-official-message-10.2.8-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `message`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, AWSJPL017E indica que a criação do production plan foi bloqueada por uma ação anterior que não terminou com sucesso. Context: The production plan cannot be created because a previous action on the production plan did not complete successfully.

> **ATENCAO / RESSALVAS DE USO:** Verified verbatim on the official v1028 Troubleshooting page; the 9.5 message catalog (awsmsawsjpl.html) carries the same message text.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmakeplan7.html |
| Titulo da fonte | The production plan cannot be created - AWSJPL017E |
| Citacao de suporte | The production plan cannot be created because a previous action on the production plan did not complete successfully. |
| Coletado em | 2026-08-18 |
| Capacidade | message |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSJPL017E |
| Status de revisao | verified |
| Tipo | message |
| verbs | plan |
| Codigo da mensagem | AWSJPL017E |
| Familia | message-10.2.8 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL017E no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?
- Qual é o significado da mensagem de erro AWSJPL017E no HWA e qual ação é recomendada?


---

### 373. `hwa-official-message-10.2.8-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, AWSJPL704E indica que o planner não conseguiu estender o preproduction plan; tablespace e transaction logs são exemplos de causas de banco. Context: The planner is unable to extend the preproduction plan.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 Troubleshooting page, including the tablespace/transaction-log database causes and the 'planner is unable to extend the preproduction plan' text. Validação oficial (PDF p.96): AWSJPL704E An internal error - planner unable to extend the preproduction plan; causas raiz variadas associadas ao MakePlan nao conseguir estender o preproduction plan.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmakeplan8.html |
| Titulo da fonte | An internal error has occurred - AWSJPL704E |
| Citacao de suporte | Different root causes are associated with this issue, typically always related to the database, for example, no space for the tablespace or full transaction logs. |
| Coletado em | 2026-08-18 |
| Capacidade | log |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSJPL704E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | planner |
| verbs | plan |
| Codigo da mensagem | AWSJPL704E |
| Familia | message-10.2.8 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL704E no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL704E no HWA?
- Qual é o significado da mensagem de erro AWSJPL704E no HWA e qual ação é recomendada?


---

### 374. `hwa-official-stageman-10.2.8-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `observability` / `log`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, Stageman aceita -carryforward no, yes ou all; -log arquiva o plano antigo em TWS_home/schedlog, -nolog impede o arquivamento e o nome padrão usa o timestamp Myyyymmddhhtt. Context: -log Archives the old production plan in the directory TWS_home/schedlog... Myyyymmddhhtt.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 page: -carryforward accepts yes|no|all; -log archives in TWS_home/schedlog; default naming convention Myyyymmddhhtt; -nolog prevents archiving.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgchddjjch.html |
| Titulo da fonte | The stageman command |
| Citacao de suporte | -carryforward{yes|no|all} ... -log Archives the old production plan in the directory TWS_home/schedlog with file name log_file ... Myyyymmddhhtt ... -nolog Does not archive the old production plan. |
| Coletado em | 2026-08-18 |
| Capacidade | log |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=log |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | stageman-10.2.8 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, Stageman aceita -carryforward no, yes ou all; -log arquiva o plano antigo em TWS_home/schedlog, -nolog impede o arquivamento e o nome padrão usa o timestamp Myyyymmddhhtt?


---

### 375. `hwa-operational-limit-zero-not-unlimited-0030`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `capacity`

**Afirmacao / Conteudo:**

In HCL Workload Automation, workstation LIMIT 0 is not equivalent to unlimited execution: from a READY job stream it allows only jobs with HI or GO priority values to launch; the SYSTEM value represents no concurrency limit.

> **ATENCAO / RESSALVAS DE USO:** This is a high-value post-installation and READY-state troubleshooting fact.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html |
| Titulo da fonte | limit cpu |
| Citacao de suporte | If you set limit cpu to 0: For a job stream in the READY state, only jobs with hi and go priority values can be launched ... If you set limit cpu to system, there is no limit. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | capacity_limit_cpu |
| Modo de operacao | read |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=capacity |
| Status de revisao | verified |
| Tipo | other |
| verbs | limit |
| Familia | limit-zero |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In HCL Workload Automation, workstation LIMIT 0 is not equivalent to unlimited execution: from a READY job stream it allows only jobs with HI or GO priority values to launch; the SYSTEM value represents no concurrency limit?


---

### 376. `hwa-version-matrix-certman-distributed-only-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, Certman fica em TWS_INST_DIR/TWS/bin e nao e suportado em sistemas operacionais IBM i; e uma ferramenta do produto Distributed.

> **ATENCAO / RESSALVAS DE USO:** Certman e Distributed-only; nao aplicar a z/OS.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tool=Certman, path=TWS_INST_DIR/TWS/bin, not_supported=IBM i operating systems, platform=Distributed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman.html |
| Titulo da fonte | Managing certificates using Certman |
| Citacao de suporte | Certman is not supported on IBM i operative systems. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | command |
| Ferramenta | certman |
| verbs | version |
| Familia | matrix-certman |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8 Distributed, Certman fica em TWS_INST_DIR/TWS/bin e nao e suportado em sistemas operacionais IBM i; e uma ferramenta do produto Distributed?


---

### 377. `hwa-version-matrix-certman-intro-10.2.3-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed, a ferramenta Certman foi introduzida na versao 10.2.3 para gerenciar certificados; a partir dessa versao os certificados passaram a ser gerenciados pelo comando certman.

> **ATENCAO / RESSALVAS DE USO:** Certman e um recurso novo a partir de 10.2.3. Nao usar certman para versoes anteriores.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tool=Certman, introduced=10.2.3, purpose=manage certificates, replaces=serverinst certificate generation |
| Produto | HCL Workload Automation |
| Versao | 10.2.3 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1chngdfeat1023.html |
| Titulo da fonte | Changed features and feature capabilities in version 10.2.3 |
| Citacao de suporte | Certificates now managed using the certman command |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.3 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | certman |
| verbs | version |
| Familia | matrix-certman |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed, a ferramenta Certman foi introduzida na versao 10.2.3 para gerenciar certificados; a partir dessa versao os certificados passaram a ser gerenciados pelo comando certman?


---

### 378. `hwa-version-matrix-certman-not-before-1023-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed, antes da versao 10.2.3 os certificados eram gerados na instalacao pelo comando serverinst; o comando certman nao existia nessas versoes anteriores (9.5, 10.1, 10.2.0-10.2.2).

> **ATENCAO / RESSALVAS DE USO:** Generalizacao perigosa evitada: certman nao existe antes de 10.2.3; versoes anteriores usavam serverinst.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tool=Certman, not_present=before 10.2.3, previous_method=serverinst certificate generation |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.1; 10.2.0-10.2.2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1chngdfeat1023.html |
| Titulo da fonte | Changed features and feature capabilities in version 10.2.3 |
| Citacao de suporte | While in previous versions it was possible to generate certificates at installation time using the serverinst command, the new certman command can now manage certificates more efficiently and easily. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.1; 10.2.0-10.2.2 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | certman |
| verbs | version |
| Familia | matrix-certman |

**Perguntas relacionadas:**

- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar cert?


---

### 379. `hwa-version-matrix-certman-not-zos-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `security` / `cert`

**Afirmacao / Conteudo:**

Em HCL Workload Automation for Z (z/OS), os certificados SSL sao gerenciados via RACF KEYRING ou keystore criado em UNIX System Services (USS), e nao pela ferramenta Certman do produto Distributed.

> **ATENCAO / RESSALVAS DE USO:** Certman nao e a ferramenta de certificados para z/OS; z/OS usa RACF/USS.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tool=Certman, z_os_certificate_management=['RACF KEYRING', 'USS keystore'], platform=z/OS |
| Produto | HCL Workload Automation for Z |
| Versao | 10.2.5-10.2.8 |
| Plataforma | z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_zce2e/eqqlwsslzcert.html |
| Titulo da fonte | Customizing the SSL connection with the Z controller when using your certificates (USS) |
| Citacao de suporte | import the certificates in a RACF KEYRING or in a keystore created in the UNIX System Services. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | cert |
| Modo de operacao | read |
| Escopo de versao | 10.2.5-10.2.8 |
| Escopo de plataforma | z/OS |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | command |
| Ferramenta | certman |
| verbs | version |
| Familia | matrix-certman |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation for Z (z/OS), os certificados SSL sao gerenciados via RACF KEYRING ou keystore criado em UNIX System Services (USS), e nao pela ferramenta Certman do produto Distributed?


---

### 380. `hwa-version-matrix-oql-distributed-zos-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `observability` / `monitor`

**Afirmacao / Conteudo:**

Em HCL Workload Automation, o OQL aplica-se tanto ao ambiente Distributed quanto ao z/OS, permitindo monitorar o production plan de ambos; para z/OS, o plano corrente e espelhado em banco via componente Federator (instalado com o Dynamic Workload Console a partir da versao 10.2.3).

> **ATENCAO / RESSALVAS DE USO:** OQL e REST V2 cobrem z/OS, mas para z/OS exigem o Federator (DWC 10.2.3+) para espelhar o plano corrente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=OQL, platforms=['distributed', 'z/OS'], z_os_prerequisite=Federator mirroring (DWC 10.2.3+), related=REST API V2, Orchestration Monitor |
| Produto | HCL Workload Automation |
| Versao | 10.2.3-10.2.8 |
| Plataforma | Distributed e z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1026/distr/src_ref/oql.html |
| Titulo da fonte | Using Orchestration Query Language |
| Citacao de suporte | You can monitor the HCL Workload Automation production plan environment, both distributed and z/OS, by using the OQL, which applies to REST API V2 and the Orchestration Monitor of the Dynamic Workload Console. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | monitor |
| Modo de operacao | read |
| Escopo de versao | 10.2.3-10.2.8 |
| Escopo de plataforma | Distributed e z/OS |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | mdm |
| verbs | plan; version |
| Familia | matrix-oql |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation, o OQL aplica-se tanto ao ambiente Distributed quanto ao z/OS, permitindo monitorar o production plan de ambos; para z/OS, o plano corrente e espelhado em banco via componente Federator (instalado com o Dynamic Workload Console a partir da versao 10.2.3)?


---

### 381. `hwa-version-matrix-zos-operator-commands-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `general_operations` / `zos`

**Afirmacao / Conteudo:**

Em HCL Workload Automation for Z (z/OS), o produto pode ser iniciado, parado, cancelado ou modificado usando os comandos de operador z/OS SSTART, PSTOP, CANCEL e MODIFY (F), emitidos de um console MCS ou via SDSF.

> **ATENCAO / RESSALVAS DE USO:** Controle do motor z/OS e via comandos de operador z/OS, nao via conman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=z/OS operator commands, commands=['SSTART', 'PSTOP', 'CANCEL', 'MODIFY (F)'], platform=z/OS |
| Produto | HCL Workload Automation for Z |
| Versao | 10.2.5-10.2.8 |
| Plataforma | z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1025/zos/src_man/eqqr1suppzoscomm.html |
| Titulo da fonte | Supported z/OS commands |
| Citacao de suporte | You can start, stop, cancel, or modify HCL Workload Automation for Z using the following z/OS operator commands: SSTART PSTOP CANCEL MODIFY |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | zos_operator_commands |
| Modo de operacao | read |
| Escopo de versao | 10.2.5-10.2.8 |
| Escopo de plataforma | z/OS |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | mdm |
| verbs | cancel; modify; version |
| Familia | matrix-zos |

**Perguntas relacionadas:**

- Como utilizar a Workload Automation Programming Language WAPL para z/OS?
- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation for Z (z/OS), o produto pode ser iniciado, parado, cancelado ou modificado usando os comandos de operador z/OS SSTART, PSTOP, CANCEL e MODIFY (F), emitidos de um console MCS ou via SDSF?


---

### 382. `hwa-version-matrix-zos-wapl-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `general_operations` / `zos`

**Afirmacao / Conteudo:**

Em HCL Workload Automation for Z (z/OS), a Workload Automation Programming Language (WAPL) combina comandos core, comandos de Data Access (PIF nativo), Current Plan Operation commands, Function Based commands (PIF estendido), comandos TSO do HWA for Z e Batch Loader; e a linguagem de comando nativa do produto z/OS.

> **ATENCAO / RESSALVAS DE USO:** Interface nativa do z/OS e WAPL, nao OCLI/composer/conman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=WAPL, components=['core commands', 'Data Access (PIF)', 'Current Plan Operation commands', 'Function Based commands', 'TSO commands', 'Batch Loader'], platform=z/OS |
| Produto | HCL Workload Automation for Z |
| Versao | 10.2.4-10.2.8 |
| Plataforma | z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1024/zos/src_wapl/c_command_language.html |
| Titulo da fonte | Command language |
| Citacao de suporte | The WAPL command language is a combination of Workload Automation Programming Language core commands, Data Access commands (native PIF requests), Current Plan Operation commands, Function Based commands (extended PIF requests), HCL Workload Automation for Z TSO commands, and Batch Loader. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | zos_wapl |
| Modo de operacao | read |
| Escopo de versao | 10.2.4-10.2.8 |
| Escopo de plataforma | z/OS |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | mdm |
| verbs | plan; version |
| Familia | matrix-zos |

**Perguntas relacionadas:**

- Como utilizar o utilitário wapl no HCL Workload Automation?
- Qual a sintaxe ou procedimento no wapl para gerenciar zos?
- O que é a linguagem WAPL e como ela é utilizada no Workload Automation for Z?
- Como utilizar a Workload Automation Programming Language WAPL para z/OS?


---
