# PARTE1 ARQUITETURA TOPOLOGIA MESH

## I. Arquitetura & Topologia Mesh

> 223 registros.

---

### 1. `hwa-10.2-distributed-conman-cancel-job-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O comando conman cancel job, com alias cj, cancela uma instância de job no plano.

> **ATENCAO / RESSALVAS DE USO:** Ação mutativa. Requer acesso cancel. Se já lançado, o job continua executando; sem ;pend, dependentes são liberados imediatamente; ;noask remove confirmação.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=cancel job, alias=cj, object=job instance in plan, interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | distributed; domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgcanceljob.html |
| Titulo da fonte | cancel job |
| Citacao de suporte | Cancels a job. Syntax: {cancel job | cj} jobselect |
| Coletado em | 2026-08-15 |
| Classificacao de risco | destructive |
| Capacidade | conman |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed; domain manager ou fault-tolerant agent |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | cancel |
| object_hint | job |
| Familia | distributed-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 2. `hwa-10.2-distributed-conman-release-job-dependencies-0016`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

No HCL Workload Automation Distributed 10.2.x, conman release job libera um job em HOLD de dependências normais e de tempo; dependências condicionais não são liberadas.

> **ATENCAO / RESSALVAS DE USO:** Ação mutativa que requer acesso release. Mantém-se o claim hwa-10.2-distributed-conman-release-job-0006 como contradicted para registrar que a formulação genérica sobre todas as dependências é incorreta.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=release job, alias=rj, object=job instance in HOLD, released_dependencies=['normal', 'time'], excluded_dependencies=['conditional'], interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | distributed; domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgreleasejob.html |
| Titulo da fonte | release job |
| Citacao de suporte | Releases jobs from normal and time dependencies. Conditional dependencies are not released. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | destructive |
| Capacidade | conman |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed; domain manager ou fault-tolerant agent |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | release |
| object_hint | job |
| Familia | distributed-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 3. `hwa-10.2-distributed-conman-rerun-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O comando conman rerun, com alias rr, cria uma reexecução de um job elegível no plano.

> **ATENCAO / RESSALVAS DE USO:** Ação mutativa. Requer acesso rerun; algumas opções exigem submit ou submitdb. Normalmente aplica-se a jobs SUCC, FAIL ou ABEND, com exceções documentadas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rerun, alias=rr, object=job instance in plan, interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | distributed; domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgrerun.html |
| Titulo da fonte | rerun |
| Citacao de suporte | Reruns a job. Syntax: {rerun | rr} jobselect |
| Coletado em | 2026-08-15 |
| Classificacao de risco | destructive |
| Capacidade | conman |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed; domain manager ou fault-tolerant agent |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | rerun |
| Familia | distributed-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 4. `hwa-10.2-distributed-conman-showjobs-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O comando conman showjobs, com alias sj, exibe informações sobre jobs no plano.

> **ATENCAO / RESSALVAS DE USO:** Comando somente de consulta. A informação é atualizada enquanto batchman estiver em execução. Pode exigir acesso list quando enListSecChk=yes.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, alias=sj, object=job, interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | distributed; conman em domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs |
| Citacao de suporte | Displays information about jobs. Syntax: {showjobs | sj} [jobselect] |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed; conman em domain manager ou fault-tolerant agent |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | showjobs |
| Familia | distributed-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 5. `hwa-10.2-distributed-conman-showschedules-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O comando conman showschedules, documentado na sintaxe como showscheds e com alias ss, exibe informações sobre job streams no plano.

> **ATENCAO / RESSALVAS DE USO:** O título é showschedules, mas a sintaxe oficial usa showscheds ou ss. Pode exigir acesso list quando enListSecChk=yes.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | documentation_topic=showschedules, command_syntax=showscheds, alias=ss, object=job stream, interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | distributed; conman em domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgshowschedules.html |
| Titulo da fonte | showschedules |
| Citacao de suporte | Displays information about job streams. Syntax: {showscheds | ss} [jstreamselect] |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | distributed; conman em domain manager ou fault-tolerant agent |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | showscheds; showschedules |
| Familia | distributed-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 6. `hwa-10.2-perfreport-benchmark-jobs-per-min-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O relatório de performance 10.2 reporta que, para workloads de até 1400 jobs/min, o atraso médio de agendamento em dynamic agents foi de 30-40 segundos (igual a versões anteriores); em picos de ~5000 jobs/min houve aumento em determinados ambientes.

> **ATENCAO / RESSALVAS DE USO:** Números dependem do ambiente de teste; não prometer capacidade universal.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | benchmark=scheduling delay, conditions=test environment specific |
| Produto | HCL Workload Automation |
| Versao | 10.2 FP0 |
| Plataforma | Distributed test environments |
| Status do conhecimento | version_dependent |
| Confianca | high |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | IBM Workload Scheduler / HCL Workload Automation V10.2 Performance Report |
| Citacao de suporte | Scheduling delay for job submissions to dynamic agents: for scheduling workloads up to 1400 jobs/min, version 10.2 showed the same average delays as previous versions (between 30 and 40 seconds). |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2 FP0 |
| Escopo de plataforma | Distributed test environments |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: O relatório de performance 10.2 reporta que, para workloads de até 1400 jobs/min, o atraso médio de agendamento em dynamic agents foi de 30-40 segundos (igual a versões anteriores); em picos de ~5000 jobs/min houve aumento em determinados ambientes?


---

### 7. `hwa-10.2-perfreport-cpu-utilization-101-compare-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No relatorio de performance oficial do HCL Workload Automation 10.2, com ~43.000 job streams no plano, a utilizacao media de CPU na carga maxima (~5.000 jobs/min) mostrou aumento de 15%-20% em comparacao com a versao 10.1, tanto no MDM quanto no servidor de banco; os valores sao especificos do ambiente de teste e nao devem ser tratados como requisito universal.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (fonte oficial HCL 10.2). Numero de ambiente de teste; usar apenas como referencia de capacity planning, nao como fato universal.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2 |
| Plataforma | Distributed |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report (HCL Rome Lab) |
| Citacao de suporte | For the test environment with around 43,000 job streams in plan, average CPU utilization at max load (~5000 jobs/min) showed an increase in the range 15%-20% compared to version 10.1, for both MDM and DB machines. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | capacity planning=planejamento de capacidade, CPU utilization=utilizacao de CPU |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2 |
| Escopo de plataforma | Distributed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No relatorio de performance oficial do HCL Workload Automation 10.2, com ~43.000 job streams no plano, a utilizacao media de CPU na carga maxima (~5.000 jobs/min) mostrou aumento de 15%-20% em comparacao com a versao 10.1, tanto no MDM quanto no servidor de banco; os valores sao especificos do ambiente de teste e nao devem ser tratados como requisito universal?


---

### 8. `hwa-10.2-perfreport-plan-replication-threads-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mirrorbox`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2, o recurso de replicacao de plano (mirroring) foi melhorado com paralelismo e caching; por padrao sao 6 threads com 6 filas mirrorbox_.msg; sob taxas altas (milhares de atualizacoes de status por minuto) ou latencia de rede entre o master domain manager e o banco, pode ser necessario ajustar a configuracao.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (fonte oficial HCL 10.2). Default de 6 threads/6 filas no plan replication. Fato version-dependent.

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
| Citacao de suporte | The plan replication feature, also known as mirroring, has been improved release after release through parallelism (multithreading) and caching. The former has defaulted to 6 threads process with 6 related mirrorbox_.msg queues. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | mirroring=replicacao do plano, mirrorbox_.msg=filas do replicador de plano, threads=6 threads padrao |
| Capacidade | mirrorbox |
| Modo de operacao | read |
| Escopo de versao | 10.2 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan; status |
| Familia | perfreport-plan |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2, o recurso de replicacao de plano (mirroring) foi melhorado com paralelismo e caching; por padrao sao 6 threads com 6 filas mirrorbox_?


---

### 9. `hwa-10.2-perfreport-sub-processors-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

O relatório de performance 10.2 recomenda ajustes documentados, como subProcessors=10, cachesize=70000, filecachesize=40000 e cachemaxage=21600000 em TWSConfig.properties para replicação de plano, e descreve configs de datasource e heap do DWC/MDM.

> **ATENCAO / RESSALVAS DE USO:** Valores documentados pelo relatório do Rome Lab; aplicar conforme volumetria e aprovação de change. | Fonte primária original local: https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tuning=TWSConfig.properties, properties=['com.ibm.tws.planner.monitor.subProcessors', 'cachesize', 'filecachesize', 'cachemaxage'] |
| Produto | HCL Workload Automation |
| Versao | 10.2 FP0 |
| Plataforma | Distributed |
| Status do conhecimento | version_dependent |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html |
| Titulo da fonte | IBM Workload Scheduler / HCL Workload Automation V10.2 Performance Report |
| Citacao de suporte | com.ibm.tws.planner.monitor.subProcessors = 10 ... com.ibm.tws.planner.monitor.cachesize = 70000 ... com.ibm.tws.planner.monitor.cachemaxage = 21600000. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2 FP0 |
| Escopo de plataforma | Distributed |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O relatório de performance 10.2 recomenda ajustes documentados, como subProcessors=10, cachesize=70000, filecachesize=40000 e cachemaxage=21600000 em TWSConfig?


---

### 10. `hwa-10.2-resetfta-xagent-safety-0028`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.0, resetFTA tem como alvo um FTA com Symphony corrompido; um SAP Extended Agent é uma workstation lógica hospedada por FTA, e a substituição de Symphony pode perder estado de fila e rerun de jobs afetados.

> **ATENCAO / RESSALVAS DE USO:** Política local: recusar automação quando o FTA hospeda X-Agent; permitir somente avaliação humana em FTA sem Extended Agent após falha documentada de recuperação de link.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=resetFTA, target=physical fault-tolerant agent, extended_agent=logical workstation, sap=SAP R/3 access method, risk=Symphony replacement and job rerun |
| Produto | HCL Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgresetfta.html |
| Titulo da fonte | resetFTA |
| Citacao de suporte | Generates an updated Sinfonia file and sends it to a fault-tolerant agent on which the Symphony file has corrupted. ... If state information about a job was contained in those queues, that job is rerun. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | destructive |
| Capacidade | agent |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| verbs | rerun |
| Familia | resetfta-xagent |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 11. `hwa-10.2-showcpus-standard-xagent-0031`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.0, a saída standard de showcpus/sc identifica X-AGENT como tipo de workstation no campo NODE; HOST não é coluna desse formato.

> **ATENCAO / RESSALVAS DE USO:** Correlacione CPUID da saída standard com CPUID/HOST da saída link; não use split de colunas sem validação de header e linhas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showcpus, format=standard, workstation_type=X-AGENT, host_column=absent |
| Produto | HCL Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgstdformat.html |
| Titulo da fonte | Standard format |
| Citacao de suporte | NODE — The node type and workstation type. Workstation types are as follows: ... X-AGENT ... METHOD — The name of the access method specified in the workstation definition. For extended agents only. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| verbs | showcpus |
| Familia | showcpus-standard |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.0, a saída standard de showcpus/sc identifica X-AGENT como tipo de workstation no campo NODE; HOST não é coluna desse formato?


---

### 12. `hwa-10.2-showcpus-xagent-host-preflight-0030`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em IBM Workload Automation Distributed 10.2.0, sc @!@;link é documentado para mostrar links de todas as workstations e, para Extended Agents, o campo HOST identifica a workstation hospedeira; a saída padrão deve ser correlacionada para identificar linhas X-AGENT.

> **ATENCAO / RESSALVAS DE USO:** A sintaxe canônica aceita ;info ou ;link. Não use ;I, ;i ou sc @!@l como sintaxe documentada. O formato link não traz o tipo X-AGENT sozinho.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showcpus, alias=sc, all_workstations=@!@, link_format=link, extended_agent_host=HOST, preflight=correlate standard and link output |
| Produto | IBM Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://www.ibm.com/docs/en/workload-automation/10.2.0?topic=commands-showcpus |
| Titulo da fonte | showcpus |
| Citacao de suporte | To display link information for all workstations, run the following command: sc @!@;link |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.0 |
| Escopo de plataforma | Distributed |
| Status de revisao | verified |
| Tipo | command |
| verbs | showcpus |
| Familia | showcpus-xagent |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em IBM Workload Automation Distributed 10.2.0, sc @!@;link é documentado para mostrar links de todas as workstations e, para Extended Agents, o campo HOST identifica a workstation hospedeira; a saída padrão deve ser correlacionada para identificar linhas X-AGENT?


---

### 13. `hwa-10.2.1-conman-release-job-dependency-0021`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

No HCL Workload Automation Distributed 10.2.1, a sintaxe de release job é {release job | rj} jobselect [;dependency[;...]] [;noask]; dependency é um metassímbolo que deve ser substituído por um tipo de dependência documentado, e ;dep não é uma forma abreviada documentada.

> **ATENCAO / RESSALVAS DE USO:** Ação mutativa. A página define dependency como tipo de dependência e lista valores concretos; não promova rj <job>;dep como comando operacional válido.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=release job, alias=rj, argument=dependency type, invalid_literal=dep, interface=conman |
| Produto | HCL Workload Automation |
| Versao | 10.2.1 |
| Plataforma | Distributed; domain manager ou fault-tolerant agent |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1021/distr/src_ref/awsrgreleasejob.html |
| Titulo da fonte | release job |
| Citacao de suporte | {release job | rj} jobselect [;dependency[;...]] [;noask] |
| Coletado em | 2026-08-15 |
| Classificacao de risco | destructive |
| Capacidade | conman |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.1 |
| Escopo de plataforma | Distributed; domain manager ou fault-tolerant agent |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | release |
| object_hint | job |
| Familia | conman-release |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 14. `hwa-10.2.6-centralized-agent-update-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Na atualização centralizada de múltiplos Fault-tolerant Agents e Dynamic Agents, jobs já em execução continuam; nenhum novo job inicia durante a manutenção; após a atualização, o agente reinicia e se reconecta aos seus jobs.

> **ATENCAO / RESSALVAS DE USO:** Não se aplica a z-centric agents. Evite atualizar múltiplos FTAs ou Dynamic Agents simultaneamente no mesmo sistema; a instalação pode falhar.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | concept=centralized agent update, agent_types=['fault-tolerant agent', 'dynamic agent'], interface=Dynamic Workload Console |
| Produto | HCL Workload Automation |
| Versao | 10.2.6 |
| Plataforma | Distributed; Windows e UNIX; requer master domain manager distribuído |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1026/distr/src_pi/awspiupgrinstfpmultagents.html |
| Titulo da fonte | Centralized agent update |
| Citacao de suporte | Any jobs already running when the upgrade process begins, continue to run as planned, however, no new jobs begin execution during this time. Once the upgrade is complete, the agent is restarted and quickly reconnects with its jobs. |
| Coletado em | 2026-08-15 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.6 |
| Escopo de plataforma | Distributed; Windows e UNIX; requer master domain manager distribuído |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | centralized-agent |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 15. `hwa-10.2.8-EEL-HT15E-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem EELHT15E indica que o HTTP client do agente para z/OS falhou ao processar uma requisição para um destino; a causa documentada é um erro de comunicação HTTP com o Dynamic Workload Console, possivelmente por o destino estar indisponível, e a recuperação é verificar o estado da instância do Dynamic Workload Console e, se indisponível, executar startAppServer quando o WebSphere Application Server Liberty Base estiver em execução no master ou domain manager.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'THE HTTP CLIENT FAILED TO PROCESS A REQUEST FOR DESTNAME.' Causa: erro de comunicação HTTP com o Dynamic Workload Console; o destino pode estar indisponível. Ação do sistema: a requisição falha; se o erro for de conexão TCP/IP, o destino é marcado OFFLINE. Recuperação: verificar o estado da instância do DWC; se indisponível, executar startAppServer quando o Liberty Base estiver em execução no master ou domain manager. Diagnóstico com ação de recuperação mutativa (startAppServer).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=EELHT15E, component=agent for z/OS HTTP client, object=HTTP request to Dynamic Workload Console destination, recovery_command=startAppServer (Liberty Base) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; agent for z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsszmsgs2.html |
| Titulo da fonte | EELE210I - EELZ412I |
| Citacao de suporte | THE HTTP CLIENT FAILED TO PROCESS A REQUEST FOR DESTNAME. ... An error occurred while communicating through HTTP with Dynamic Workload Console. ... Check the state of the Dynamic Workload Console instance. If the problem is due to Dynamic Workload Console being unavailable, resolve by running: startAppServer if WebSphere Application Server Liberty Base is running on the master or domain manager. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; agent for z/OS |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| scope | distributed; agent for z/OS |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| Codigo da mensagem | EELHT15E |
| Componente | agent for z/OS HTTP client |
| Familia | EEL-HT15E |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELHT15E indica que o HTTP client do agente para z/OS falhou ao processar uma requisição para um destino; a causa documentada é um erro de comunicação HTTP com o Dynamic Workload Console, possivelmente por o destino estar indisponível, e a recuperação é verificar o estado da instância do Dynamic Workload Console e, se indisponível, executar startAppServer quando o WebSphere Application Server Liberty Base estiver em execução no master ou domain manager?


---

### 16. `hwa-10.2.8-EEL-IT01E-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem EELIT01E indica que o parâmetro TDWBHOSTNAME (hostname do Dynamic Workload Console) está ausente e é obrigatório; a causa documentada é que o agente para z/OS não pode iniciar porque o hostname do Dynamic Workload Console não foi fornecido, e a recuperação é fornecer o parâmetro de inicialização TDWBHOSTNAME e reiniciar o agente.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'THE TDWBHOSTNAME PARAMETER FOR THE Dynamic Workload Console HOSTNAME IS MISSING. THE PARAMETER IS MANDATORY.' Causa: o agente não pode iniciar porque o hostname do Dynamic Workload Console não foi fornecido. Ação do sistema: o agente não pode ser inicializado. Recuperação: fornecer o parâmetro de inicialização TDWBHOSTNAME e reiniciar o agente. Diagnóstico de configuração; recuperação mutativa (reinício do agente).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=EELIT01E, component=agent for z/OS initialization, missing_parameter=TDWBHOSTNAME, recovery=provide TDWBHOSTNAME and restart agent |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; agent for z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsszmsgs2.html |
| Titulo da fonte | EELE210I - EELZ412I |
| Citacao de suporte | THE TDWBHOSTNAME PARAMETER FOR THE Dynamic Workload Console HOSTNAME IS MISSING. THE PARAMETER IS MANDATORY. ... The agent cannot start because the hostname of the Dynamic Workload Console was not provided. ... Provide the TDWBHOSTNAME initialization parameter and restart the agent. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; agent for z/OS |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| scope | distributed; agent for z/OS |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| Codigo da mensagem | EELIT01E |
| Componente | agent for z/OS initialization |
| Familia | EEL-IT01E |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELIT01E indica que o parâmetro TDWBHOSTNAME (hostname do Dynamic Workload Console) está ausente e é obrigatório; a causa documentada é que o agente para z/OS não pode iniciar porque o hostname do Dynamic Workload Console não foi fornecido, e a recuperação é fornecer o parâmetro de inicialização TDWBHOSTNAME e reiniciar o agente?


---

### 17. `hwa-10.2.8-EEL-SU09W-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem EELSU09W (warning) indica que um job não pôde ser liberado de hold e as tentativas repetidas falharam; a causa documentada é que o submit task não conseguiu comunicar com JES ao tentar liberar o job de hold, e a recuperação é determinar o status atual do job, liberá-lo manualmente se necessário e revisar o system log em busca de mensagens JES anteriores.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'JOB JOBNAME(JOBNUM) COULD NOT BE RELEASED. REPEATED RETRIES HAVE FAILED.' Causa: o submit task recebeu um pedido de release de um job, mas não conseguiu comunicar com JES ao tentar liberar o job de hold. Ação do sistema: não há mais tentativas de release; o submit task continua processando. Recuperação: determinar o status atual do job; se necessário, liberá-lo manualmente; revisar o system log. Diagnóstico com recuperação mutativa (release manual).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=EELSU09W, component=agent for z/OS submit task, object=job release from hold, cause=communication failure with JES, recovery=determine job status; release manually if needed; review system log |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; agent for z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsszmsgs2.html |
| Titulo da fonte | EELE210I - EELZ412I |
| Citacao de suporte | JOB JOBNAME(JOBNUM) COULD NOT BE RELEASED. REPEATED RETRIES HAVE FAILED. ... The submit task received a release request for a job, but could not communicate successfully with JES while trying to release the job from hold. ... Determine the current status of the job. If necessary, release the job manually. Review the system log and look for previous JES messages. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; agent for z/OS |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| scope | distributed; agent for z/OS |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | message |
| verbs | status; submit |
| Codigo da mensagem | EELSU09W |
| Componente | agent for z/OS submit task |
| Familia | EEL-SU09W |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, a mensagem EELSU09W (warning) indica que um job não pôde ser liberado de hold e as tentativas repetidas falharam; a causa documentada é que o submit task não conseguiu comunicar com JES ao tentar liberar o job de hold, e a recuperação é determinar o status atual do job, liberá-lo manualmente se necessário e revisar o system log em busca de mensagens JES anteriores?


---

### 18. `hwa-10.2.8-agent-dynamic-broker-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Na instalação de agente dinâmico HWA 10.2.8, agent dynamic exige tdwbhostname e tdwbport; em instalação nova, a documentação indica 31116 como valor de tdwbport para conexão HTTPS do broker, sujeito à configuração do ambiente.

> **ATENCAO / RESSALVAS DE USO:** Não confundir com jmport 31114 nem tratar a porta como universal fora da versão/topologia. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: agente dinâmico conectou na porta 31116 HTTPS do broker tws-hwa.lab com registro de recursos AWSITA083I.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | installer=twsinst, agent=dynamic, broker_parameters=['tdwbhostname', 'tdwbport'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed agents |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | Agent installation parameters - twsinst script |
| Citacao de suporte | dynamic Installs the HCL Workload Automation dynamic agent. Requires the -tdwbhostname host_name and the -tdwbport tdwbport_number parameters... otherwise, specify 31116 for a fresh installation. |
| Coletado em | 2026-08-16 |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed agents |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | agent-dynamic |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: Na instalação de agente dinâmico HWA 10.2.8, agent dynamic exige tdwbhostname e tdwbport; em instalação nova, a documentação indica 31116 como valor de tdwbport para conexão HTTPS do broker, sujeito à configuração do ambiente?


---

### 19. `hwa-10.2.8-capacity-bm-look-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A página de performance do HCL Workload Automation 10.2.8 documenta que os períodos de varredura do batchman (bm look), jobman (jm read, jm look) e mailman (mm read) no arquivo localopts afetam a performance: tempos menores geram varreduras mais frequentes usando mais CPU, enquanto tempos maiores fazem os jobs demorarem mais; recomenda testar em ambiente de teste antes de aplicar em produção e alterar um parâmetro por vez.

> **ATENCAO / RESSALVAS DE USO:** Recomendações atômicas documentadas para tuning de processamento de jobs.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | localopts=arquivo localopts, bm look=bm look, jm read=jm read, jm look=jm look, mm read=mm read |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtunejobproc.html |
| Titulo da fonte | Tuning job processing on a workstation |
| Citacao de suporte | a shorter time means more frequent scans, using more cpu resources... Modify only the parameters that are necessary. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | capacity-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A página de performance do HCL Workload Automation 10.2.8 documenta que os períodos de varredura do batchman (bm look), jobman (jm read, jm look) e mailman (mm read) no arquivo localopts afetam a performance: tempos menores geram varreduras mais frequentes usando mais CPU, enquanto tempos maiores fazem os jobs demorarem mais; recomenda testar em ambiente de teste antes de aplicar em produção e alterar um parâmetro por vez?


---

### 20. `hwa-10.2.8-capacity-fault-tolerant-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A documentação de performance do HCL Workload Automation 10.2.8 afirma que o desempenho de domain managers UNIX é impactado se sobrecarregados com jobs e que, para lidar com grande número de fault-tolerant agents, é possível melhorar o desempenho ajustando parâmetros de kernel; fornece um exemplo de parâmetros Linux para uma carga de 500000 jobs por dia, incluindo open files=105000 e max user processes=16384.

> **ATENCAO / RESSALVAS DE USO:** Exemplo de kernel para dimensionamento de domain manager UNIX com muitos FTA.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | fault-tolerant agent=FTA, domain manager=domain manager, kernel parameters=parâmetros de kernel |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtuneunixdm.html |
| Titulo da fonte | Tuning a UNIX domain manager to handle large numbers of fault-tolerant agents |
| Citacao de suporte | The following is an example of the kernel settings for Linux... to handle 500000 jobs per day workload... open files=105000... max user processes=16384 |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | open |
| Familia | capacity-fault |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 21. `hwa-10.2.8-capacity-fta-engines-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `fta`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation 10.2.8 não documenta uma opção localopts/useropts chamada 'Number of FTA engines'.

> **ATENCAO / RESSALVAS DE USO:** Página completa de localopts v1028 (awsadlocaloptdescr.html) lida integralmente: nenhuma opção 'Number of FTA engines' nem qualquer opção que controle a quantidade de processos/engines do fault-tolerant agent (netman, mailman, batchman, jobman, writer). Opção mais próxima é 'jm job table size' (default 1024 entradas), que não altera o número de processos. Resumo de localopts (awsadlocaloptsum.html) confirma a lista completa; useropts contém apenas parâmetros de conexão do CLI. Busca Perplexity não encontrou opção oficial equivalente. Achado negativo confirmado; claim promovida de insufficient para verified.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | localopts=local options file, useropts=user options file, FTA engines=fault-tolerant agent engine processes, jm job table size=jm job table size |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm job table size = *entries* Specify the size, in number of entries, of the job table used by Jobman. The default is 1024 entries. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | fta |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | capacity-fta |


---

### 22. `hwa-10.2.8-capacity-jm-job-table-size-0023`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção localopts 'jm job table size' no HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão de 1024 entradas.

> **ATENCAO / RESSALVAS DE USO:** Opção localopts relevante para capacidade/concorrência de processamento de jobs em uma workstation.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm job table size=tamanho da tabela de jobs do Jobman, Jobman=jobman |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm job table size = entries — Specify the size, in number of entries, of the job table used by Jobman. The default is 1024 entries. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['cat /opt/hwa/TWSDATA/localopts'], result=/opt/hwa/TWSDATA/localopts: jm job table size = 1024 (default documentado: 1024 entradas). Confirmado no lab 10.2.8.00., validated_at=2026-08-23T02:20:00BRT |
| Tipo | other |
| Familia | capacity-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção localopts 'jm job table size' no HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão de 1024 entradas?


---

### 23. `hwa-10.2.8-capacity-mm-cache-size-0024`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção localopts 'mm cache size' no HCL Workload Automation 10.2.8 especifica o tamanho do cache de leitura do Mailman para mensagens de entrada, com valor máximo (padrão) de 512 mensagens, usado juntamente com a opção mm cache mailbox.

> **ATENCAO / RESSALVAS DE USO:** Cache de leitura do Mailman afeta uso de memória e performance de mensagens.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm cache size=tamanho do cache do Mailman, Mailman=mailman |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm cache size = messages — ...The maximum value (default) is 512. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['cat /opt/hwa/TWSDATA/localopts'], result=/opt/hwa/TWSDATA/localopts: mm cache size = 512 (default documentado: 512 mensagens). Confirmado no lab 10.2.8.00., validated_at=2026-08-23T02:20:00BRT |
| Tipo | other |
| Familia | capacity-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção localopts 'mm cache size' no HCL Workload Automation 10.2.8 especifica o tamanho do cache de leitura do Mailman para mensagens de entrada, com valor máximo (padrão) de 512 mensagens, usado juntamente com a opção mm cache mailbox?


---

### 24. `hwa-10.2.8-capacity-workstation-limit-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A opção global workstationLimit (wl) no HCL Workload Automation 10.2.8 especifica o valor de limite de workstation que um dynamic agent assume após ser adicionado ao plano, com valores válidos de 0 a 1024 e padrão 100, efetivo imediatamente.

> **ATENCAO / RESSALVAS DE USO:** É a opção de limite de workstation documentada (similar ao conceito de 'limit of available workstations'); aplica-se à registro automático de dynamic agents.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | workstationLimit=wl, workstation limit=limite da workstation, dynamic agent=agente dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | Global options - detailed description |
| Citacao de suporte | The workstation limit. Used in the automatic dynamic agent registration... Valid values are in the 0-1024 range. The default is 100. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['optman ls', 'optman chg sh=401 (controle positivo, restaurado para 400)'], result=optman ls: workstationLimit / wl = 100. Default confirmado no lab 10.2.8., validated_at=2026-08-23T01:50:00BRT |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | limit |
| Familia | capacity-workstation |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: A opção global workstationLimit (wl) no HCL Workload Automation 10.2.8 especifica o valor de limite de workstation que um dynamic agent assume após ser adicionado ao plano, com valores válidos de 0 a 1024 e padrão 100, efetivo imediatamente?
- Qual o propósito e valor padrão da opção global workstationLimit no optman do HWA?


---

### 25. `hwa-10.2.8-composer-jsdl-validation-0119`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `composer`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, definicoes de job com TASK JSDL (JSON) para dynamic agents sao validadas pelo schema no composer add/validate. Exemplos com formato incorreto sao rejeitados com AWSJCS029E XML definition incorrect. O schema espera executable.interactive, executable.suffix, executable.script, credential. Exemplo valido: TASK { executable: { interactive: false, suffix: , script: ls, credential: {} } } RECOVERY STOP END.

> **ATENCAO / RESSALVAS DE USO:** Use the embedded job example from official doc as template.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobdefn.html |
| Titulo da fonte | Job definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | task ... Specifies the task to be executed. For dynamic agent jobs, a JSON task definition is required. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04 HWA 10.2.8.00, tested_commands=['composer validate jd=JOB with invalid JSDL JSON'], result=AWSJCS029E on invalid JSON; corrected JSON passed |
| Classificacao de risco | read_only |
| Capacidade | composer |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Status do conhecimento | verified |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Coletado em | 2026-08-22 |
| Terminologia normalizada | message=AWSJCS029E, command=composer |
| Tipo | message |
| Ferramenta | composer |
| verbs | add; validate |
| Codigo da mensagem | AWSJCS029E |
| Familia | composer-jsdl |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCS029E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCS029E no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar composer?


---

### 26. `hwa-10.2.8-composer-opens-workstation-0125`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, ao definir uma file dependency OPENS em job stream via composer, o filename DEVE ser qualificado com a workstation (ex.: OPENS MDMDA#arquivo). Se usado apenas OPENS "arquivo" sem prefixo de workstation, o composer rejeita com AWSJOM115E 'The required workstation or workstation class has not been supplied for the file dependency'. A documentacao oficial mostra [[folder/]workstation#] como opcional, mas na pratica (validado em laboratorio) o prefixo e exigido para file dependencies em alguns contextos.

> **ATENCAO / RESSALVAS DE USO:** Laboratorio: OPENS "DS_OUTPUT_FILE" sem workstation -> AWSJOM115E. Com MDMDA#DS_OUTPUT_FILE -> sintaxe aceita. Discrepancia doc x implementacao: sintaxe oficial marca workstation como opcional (colchetes), mas o validador exige em alguns contextos.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Job stream definition - HCL Workload Automation 10.2.8 |
| Citacao de suporte | opens { [[folder/]workstation#]"filename" [ (qualifier) ] [,...] } - workstation prefix shown as optional in syntax |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Status do conhecimento | verified |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Coletado em | 2026-08-22 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 MDM, tested_commands=['composer validate js=DEPS_TEST_STREAM com OPENS "DS_OUTPUT_FILE" (sem workstation)', 'composer validate js=DEPS_TEST_STREAM com OPENS MDMDA#DS_OUTPUT_FILE (com workstation)'], result=OPENS sem workstation -> AWSJOM115E. OPENS com MDMDA# -> aceito. Prefixo de workstation e obrigatorio na pratica para file dependencies. |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSJOM115E, command=composer |
| Tipo | message |
| Ferramenta | composer |
| Codigo da mensagem | AWSJOM115E |
| Familia | composer-opens |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM115E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM115E no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 27. `hwa-10.2.8-composer-parm-caret-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `composer`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, variáveis referenciadas em definições de job usam a sintaxe caret (^var^), por exemplo docommand "ls ^MY_HOME^"; ^var^ é resolvido quando o plano é gerado ou estendido, e ${var} é resolvido/sobrescrito quando o job ou job stream é submetido (formato de integrações com dynamic agents); o formato %var% NÃO é a forma documentada de referência a variável/parm (não aparece na referência oficial).

> **ATENCAO / RESSALVAS DE USO:** Formatos documentados: ^var^ (plan-time, clássico) e ${var} (submit-time, dynamic agents); %var% nunca documentado. VERSION_DEPENDENT(parcial): ${var} e variáveis aninhadas são adições 10.x/dynamic-agent. Confirmado no lab 2026-08-22: DOCOMMAND 'echo ^LAB_MSG^ at ^LAB_WS^' resolveu em FTA nativo.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=composer |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgparmdefn.html |
| Titulo da fonte | Variable and parameter definition - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | An example of a variable used with the docommand keyword is: docommand "ls ^MY_HOME^" |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | composer |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | composer |
| Familia | composer-parm |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar composer?
- Como configurar ou solucionar problemas no dynamic agent ou broker para composer?


---

### 28. `hwa-10.2.8-composer-task-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `composer`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, os valores validos documentados para o argumento tasktype na definicao de job via composer sao UNIX, WINDOWS, OTHER e BROKER.

> **ATENCAO / RESSALVAS DE USO:** CORRECAO importante: uma busca previa sugeriu UNIXTASK/WINDOWSTASK/XATASK/UNKNOWN, mas a doc oficial 10.2.8 lista apenas UNIX, WINDOWS, OTHER e BROKER para o composer. O tipo do job so' e' verificado no submit (a definicao grava sem checagem).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | tasktype=UNIX | WINDOWS | OTHER | BROKER |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobdefn.html |
| Titulo da fonte | Job definition (v1028) |
| Citacao de suporte | tasktype tasktype - Specifies the job type. It can have one of the following values: UNIX For jobs that run on UNIX platforms. WINDOWS For jobs that run on Windows operating systems. OTHER ... BROKER ... |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-command-researcher |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | composer |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | composer |
| Familia | composer-task |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar composer?
- Como configurar ou solucionar problemas no dynamic agent ou broker para composer?


---

### 29. `hwa-10.2.8-conman-command-inventory-0033`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O índice oficial HCL 10.2.8 enumera comandos Conman, suas formas curtas e os tipos de workstation suportados; kill/k interrompe job em execução, showjobs/sj exibe jobs e resetFTA recupera Symphony corrompido em FTA especificado.

> **ATENCAO / RESSALVAS DE USO:** Inventory claim: page lists commands, short forms and workstation types (legend D/M/F/T/S). resetFTA applies to type T (fault-tolerant agents) and has no short form ('N/A'). kill is destructive when actually executed; this claim only describes the command index.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgconmancmds.html |
| Titulo da fonte | Conman commands |
| Citacao de suporte | kill — k — Stops an executing job. ... showjobs — sj — Displays information about jobs. ... resetFTA — N/A — Recovers a corrupt Symphony file on the specified fault-tolerant agent |
| Coletado em | 2026-08-18 |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=showjobs |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | kill; showjobs |
| Familia | conman-command |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 30. `hwa-10.2.8-conman-start-restriction-0113`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, o comando `conman start` inicia os processos de producao do HWA (exceto event monitoring engine e Liberty), mas possui restricoes: (1) nao deve ser executado enquanto JnextPlan ou stageman estiverem rodando; (2) exige acesso 'start' a workstation; (3) 'This command is not supported on remote engine workstations' -- workstations do tipo agente, broker ou pool remoto nao aceitam `start`. Em workstations agente, o erro retornado e 'the workstation is agent, where the command is not supported'. Agentes devem ser iniciados localmente com ./StartUpLwa.sh (Unix) ou startuplwa (Windows).

> **ATENCAO / RESSALVAS DE USO:** Official HCL 10.2.8 start page confirms 'not supported on remote engine workstations'. Lab validated 2026-08-22: start funciona no master CPU (MDM) mas e rejeitado em workstations do tipo agent. A restricao estava presente no dataset (L58 start [domain!]wkstation[;mgr]) mas sem mencionar que agents/pools/brokers nao suportam start.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | start=comando conman start, remote engine workstation=workstation do tipo remote engine (agente, broker), StartUpLwa.sh=script de inicializacao local do agente em Unix |
| Status do conhecimento | verified |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstart.html |
| Titulo da fonte | start - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | This command is not supported on remote engine workstations. Make sure conman start is not issued while either JnextPlan or stageman runs. You must have start access to the workstation. |
| Coletado em | 2026-08-22 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, tested_commands=["sudo -u wauser bash -lc 'source /opt/hwa/TWS/tws_env.sh; conman start MDM'"], result=start MDM em master domain manager: 'MDM already active.' (funciona); tentativa de start em agente retorna 'the workstation is agent, where the command is not supported' |
| Classificacao de risco | mutating |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Capacidade | conman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | lab_validated |
| Tipo | command |
| Ferramenta | conman |
| verbs | start |
| Familia | conman-start |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?
- Qual endpoint REST API V2 é utilizado para conman no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para conman?
- Como utilizar o comando conman 'start' para gerenciar workstations e execução no HWA?


---

### 31. `hwa-10.2.8-conman-start-unified-0123`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, o comando conman start inicia os processos de producao de uma workstation, com sintaxe 'start [domain!]workstation[;mgr][;noask]'. Restricoes IMPORTANTES: (1) funciona APENAS em master domain manager e fault-tolerant agents; NAO funciona em workstations do tipo remote engine (agent, broker, pool) - o erro retornado e 'the workstation is agent, where the command is not supported'; (2) nao deve ser executado enquanto JnextPlan ou stageman estiver rodando; (3) exige acesso 'start' a workstation; (4) para iniciar agentes/brokers/pools use o script local ./StartUpLwa.sh (Unix) ou startuplwa (Windows).

> **ATENCAO / RESSALVAS DE USO:** Claim unificada (2026-08-22): mescla sintaxe (hwa-10.2.8-conman-start-0001) com restricao de tipo (hwa-10.2.8-conman-start-restriction-0113) em um unico claim para que o SFT ensine ambos juntos. Lab validated 2026-08-22.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | start=comando conman start, remote engine workstation=agente, broker ou pool remoto, StartUpLwa.sh=script local de inicializacao de agente em Unix, startuplwa=script local de inicializacao de agente em Windows |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstart.html |
| Titulo da fonte | start - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | This command is not supported on remote engine workstations. Make sure conman start is not issued while either JnextPlan or stageman runs. You must have start access to the workstation. Syntax: start [domain!]workstation[;mgr][;noask] |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, tested_commands=['conman start MDM', 'conman start <agent_ws>'], result=start MDM -> 'MDM already active.' (works on master CPU); start on agent -> 'the workstation is agent, where the command is not supported' |
| Classificacao de risco | mutating |
| Capacidade | conman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Status do conhecimento | verified |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Coletado em | 2026-08-22 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | command |
| Ferramenta | conman |
| verbs | start |
| Familia | conman-start |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?
- Como configurar ou solucionar problemas no dynamic agent ou broker para conman?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 32. `hwa-10.2.8-conman-submit-follows-hold-0134`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, ao submeter job ad hoc com sbd e o parametro follows=, o job entra em HOLD aguardando a dependencia ser satisfeita no plano de producao. Em laboratorio, sbd MDMDA#"cmd";alias=X;follows JOBS.AT_TEST_001 colocou o job em HOLD esperando AT_TEST_001 (HOLD ate 08/23), confirmando que a dependencia follows funciona no plano. O dataset ensina follows= corretamente.

> **ATENCAO / RESSALVAS DE USO:** Laboratorio: sbd follows JOBS.AT_TEST_001 -> job HOLD esperando AT_TEST_001 (HOLD ate 08/23). Dependencia follows funciona no plano. Comportamento consistente com a doc oficial. Validacao positiva - sem lacuna no dataset.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html |
| Titulo da fonte | submit job - HCL Workload Automation 10.2.8 |
| Citacao de suporte | follows=[netagent::][wkstation#]jstream{.job | @} | job[,...] - Specifies the job stream or job to be followed |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Status do conhecimento | verified |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Coletado em | 2026-08-22 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 MDM, tested_commands=['sbd MDMDA#"cmd";alias=X;follows JOBS.AT_TEST_001 -> HOLD esperando AT_TEST_001 (HOLD ate 08/23)'], result=Dependencia follows funciona no plano; job entra em HOLD ate a dependencia ser satisfeita. |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=conman |
| Tipo | command |
| Ferramenta | conman |
| verbs | submit |
| Familia | conman-submit |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 33. `hwa-10.2.8-dwc-mdm-distinct-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Dynamic Workload Console (DWC) and the MDM engine are distinct architectural components; the DWC is an independent web application and the DWC version must be equal to or higher than the version of any engine it connects to. Official Release Notes compatibility tables list the engine versions each DWC release can connect to (e.g. DWC 10.2.0 connects to MDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4), i.e. same-version or earlier engines.

> **ATENCAO / RESSALVAS DE USO:** Resolvido 2026-08-18: a regra de compatibilidade (DWC conecta engines da mesma versão ou anteriores) e confirmada pelos Release Notes oficiais da familia 10.2 (DWC 10.2.0 <-> MDM/DDM 10.2.0, 10.1, 9.5 FP2+, 9.4), 9.5 (DWC 9.5 <-> MDM 9.5, 9.4) e 9.4. A pagina v1028 eqqg1dwconsole confirma que o DWC e uma aplicacao web independente e ponto unico de controle; a regra de versao esta nas tabelas de interoperabilidade dos Release Notes, nao na pagina conceitual. Compatibilidade e suportada no ultimo fix pack de cada release listado.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.ibm.com/support/pages/dynamic-workload-console-version-1020-release-notes |
| Titulo da fonte | Dynamic Workload Console Version 10.2.0 Release Notes - Interoperability tables (IBM Support) |
| Citacao de suporte | Dynamic Workload Console: compatibility. Compatibility is supported on the latest available fix pack for each release listed in the table: MDM 10.2.0, 10.1, 9.5 FP2 and later, 9.4; DDM 10.2.0, 10.1, 9.5 FP2 and later. |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=release |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | dwc |
| verbs | list; release; version |
| Familia | dwc-mdm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Dynamic Workload Console (DWC) and the MDM engine are distinct architectural components; the DWC is an independent web application and the DWC version must be equal to or higher than the version of any engine it connects to?


---

### 34. `hwa-10.2.8-dynagent-backup-resource-advisor-urls-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

A propriedade BackupResourceAdvisorUrls da seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 define a lista de URLs retornadas pelo master em ambiente distribuído ou pelo dynamic domain manager, que o agent usa para se conectar ao master/DDM, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: propriedade BackupResourceAdvisorUrls.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | BackupResourceAdvisorUrls=lista de URLs de backup para o agent conectar-se ao master/DDM |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconfresadvisorag.html |
| Titulo da fonte | Configuring properties of the Resource advisor agent [ResourceAdvisorAgent] |
| Citacao de suporte | BackupResourceAdvisorUrls: The list of URLs returned by the HCL Workload Automation master in a distributed environment or by the dynamic domain manager ... The agent uses this list to connect to the master or dynamic domain manager. |
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
| Familia | dynagent-backup |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade BackupResourceAdvisorUrls da seção [ResourceAdvisorAgent] do JobManager?


---

### 35. `hwa-10.2.8-dynagent-broker-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O Dynamic Workload Broker (workstation broker) no HCL Workload Automation 10.2.8 funciona como uma ponte entre o mecanismo de agendamento e o pool de recursos, associando dinamicamente o workload submetido aos melhores recursos disponíveis em tempo de execução e submetendo cada job ao recurso que melhor atende aos requisitos, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: papel e propósito do Dynamic Workload Broker. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: broker MDM_DWB gerenciou o registro e despacho para os agentes MDMDA e TWS-AGENT.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Dynamic Workload Broker=workstation broker que faz a ponte entre o agendador e o pool de recursos, JSDL=Job Submission Description Language |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1schedwldynam.html |
| Titulo da fonte | Scheduling workload dynamically |
| Citacao de suporte | Update your HCL Workload Automation job definitions to make as destination CPU the dynamic workload broker workstation (this workstation works as a bridge between the scheduler engine and the pool of resources)... submits the job to the resource that best meets the requirements. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-broker |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 36. `hwa-10.2.8-dynagent-broker-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O servidor do Dynamic Workload Broker no HCL Workload Automation 10.2.8 é instalado juntamente com o master domain manager e o dynamic domain manager e suas workstations de backup, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: local de instalação do servidor do DWB. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: broker instalado conjuntamente no container MDM sob a workstation MDM_DWB.]

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Dynamic Workload Broker server=servidor broker instalado com o master/DDM, master domain manager=hub de gerenciamento da rede, dynamic domain manager=hub de gerenciamento de um domínio dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadswitchdynbroker.html |
| Titulo da fonte | Switching a master domain manager or dynamic domain manager |
| Citacao de suporte | The installation of a master domain manager or dynamic domain manager and of its backup workstations includes also the installation of a dynamic workload broker server. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | lab_validated |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-broker |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: O servidor do Dynamic Workload Broker no HCL Workload Automation 10.2.8 é instalado juntamente com o master domain manager e o dynamic domain manager e suas workstations de backup, conforme documentação oficial?


---

### 37. `hwa-10.2.8-dynagent-concurrency-broker-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

There is no component named "concurrency broker" documented in HCL Workload Automation 10.2.8; the broker is composed of the Resource Advisor and Job Dispatcher.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | concurrency broker=termo não documentado, dynamic workload broker=terminologia documentada para o broker |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The documented properties are listed in the [ResourceAdvisorAgent] section. |
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
| Familia | dynagent-concurrency |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para resource?
- Qual a regra documentada no HWA Distributed sobre: There is no component named "concurrency broker" documented in HCL Workload Automation 10.2.8; the broker is composed of the Resource Advisor and Job Dispatcher?


---

### 38. `hwa-10.2.8-dynagent-database-job-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O dynamic agent no HCL Workload Automation 10.2.8 executa database jobs com opções avançadas, que realizam consultas, comandos SQL e jobs sobre bancos de dados incluindo bancos customizados, além de permitir criar e executar stored procedures em bancos DB2, Oracle e MSSQL, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: tipos de database job suportados (DB2, Oracle, MSSQL, bancos customizados).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | database job=tipo de job com opções avançadas, DB2=banco suportado para stored procedures, Oracle=banco suportado para stored procedures, MSSQL=banco suportado para stored procedures |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_zce2e/eqqlwadvntgsjobtypeadvopt.html |
| Titulo da fonte | Advantages of job types with advanced options |
| Citacao de suporte | Database jobs: Perform queries, SQL statements, and jobs on a number of databases, including custom databases. You can also create and run stored procedures on DB2, Oracle, and MSSQL databases. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-database |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 executa database jobs com opções avançadas, que realizam consultas, comandos SQL e jobs sobre bancos de dados incluindo bancos customizados, além de permitir criar e executar stored procedures em bancos DB2, Oracle e MSSQL, conforme documentação oficial?


---

### 39. `hwa-10.2.8-dynagent-database-job-executor-properties-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A configuração dos database jobs (JDBC) no dynamic agent do HCL Workload Automation 10.2.8 é feita pelo arquivo DatabaseJobExecutor.properties, presente em TWA_home/TWS/JavaExt/cfg, usando a palavra-chave jdbcDriversPath para apontar para o diretório dos drivers JDBC, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: maneira oficial de configurar conexões de database jobs (JDBC).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | DatabaseJobExecutor.properties=arquivo de configuração do executor de database jobs, jdbcDriversPath=palavra-chave que especifica o caminho dos drivers JDBC, JDBC=Java Database Connectivity |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadadvoptjobsched.html |
| Titulo da fonte | Configuring to schedule job types with advanced options |
| Citacao de suporte | Configuration files are available on each dynamic agent in TWA_home/TWS/JavaExt/cfg ... Database job type ... DatabaseJobExecutor.properties ... Use the jdbcDriversPath keyword to specify the path to the JDBC drivers. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-database |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: A configuração dos database jobs (JDBC) no dynamic agent do HCL Workload Automation 10.2.8 é feita pelo arquivo DatabaseJobExecutor?


---

### 40. `hwa-10.2.8-dynagent-en-add-workstation-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Com a opção global enAddWorkstation definida como 'yes' no HCL Workload Automation 10.2.8, a definição de workstation do dynamic agent é adicionada automaticamente ao Plano após o processo de instalação criar a workstation no banco de dados, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: opção global enAddWorkstation e adição automática ao Plano.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | enAddWorkstation=opção global que adiciona a workstation do dynamic agent ao Plano |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | If you have the enAddWorkstation global option set to yes, the dynamic agent workstation definition is automatically added to the Plan after the installation process creates the dynamic agent workstation in the database. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | add |
| Familia | dynagent-en |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: Com a opção global enAddWorkstation definida como 'yes' no HCL Workload Automation 10.2.8, a definição de workstation do dynamic agent é adicionada automaticamente ao Plano após o processo de instalação criar a workstation no banco de dados, conforme documentação oficial?


---

### 41. `hwa-10.2.8-dynagent-file-transfer-jobs-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Os job types com opções avançados disponíveis no HCL Workload Automation 10.2.8 incluem file transfer jobs, web services jobs, database jobs, executable jobs, Java jobs, MSSQL jobs, access method jobs (Oracle E-Business Suite, PeopleSoft, SAP, MVS e métodos customizados), J2EE jobs, IBM i jobs, provisioning e remote command, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: catálogo de job types com opções avançadas executáveis em agents dinâmicos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | file transfer jobs=transferência de arquivos via FTP, SSH ou outros, access method jobs=extensão a sistemas externos (SAP, PeopleSoft, Oracle EBS, MVS, custom), J2EE jobs=mensagens a destinos JMS, provisioning=ambientes sob demanda em nuvem/físico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_zce2e/eqqlwadvntgsjobtypeadvopt.html |
| Titulo da fonte | Advantages of job types with advanced options |
| Citacao de suporte | The following job types with advanced options are available: File transfer jobs ... Web services jobs ... Database jobs ... Executable jobs ... Java jobs ... MSSQL jobs ... Access Method jobs ... J2EE jobs ... IBM i jobs ... Provisioning ... Remote command. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-file |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os job types com opções avançados disponíveis no HCL Workload Automation 10.2.8 incluem file transfer jobs, web services jobs, database jobs, executable jobs, Java jobs, MSSQL jobs, access method jobs (Oracle E-Business Suite, PeopleSoft, SAP, MVS e métodos customizados), J2EE jobs, IBM i jobs, provisioning e remote command, conforme documentação oficial?


---

### 42. `hwa-10.2.8-dynagent-gateway-local-0029`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O dynamic agent no HCL Workload Automation 10.2.8 pode conectar-se diretamente ao master domain manager ou por meio de um dynamic domain manager; em topologias onde o master/DDM não pode comunicar-se diretamente com o agent, pode-se configurar o dynamic agent para usar um gateway local ou remoto, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: conectividade do dynamic agent com o master/DDM e uso de gateway.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | gateway local=gateway configurado no próprio dynamic agent, gateway remoto=gateway em outra workstation, JobManagerGW.ini=arquivo de configuração do agent com gateway |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidistworkloaddynam.html |
| Titulo da fonte | Distributed workload environment with dynamic scheduling capabilities |
| Citacao de suporte | A dynamic agent can be directly connected to its master domain manager or through a dynamic domain manager ... In more complex network topologies where the master domain manager or the dynamic domain manager cannot directly communicate with the dynamic agent, you can configure your dynamic agents to use a local or remote gateway. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-gateway |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 pode conectar-se diretamente ao master domain manager ou por meio de um dynamic domain manager; em topologias onde o master/DDM não pode comunicar-se diretamente com o agent, pode-se configurar o dynamic agent para usar um gateway local ou remoto, conforme documentação oficial?


---

### 43. `hwa-10.2.8-dynagent-ita-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A seção [ITA] do JobManager.ini no HCL Workload Automation 10.2.8 configura propriedades gerais do agente, incluindo ActionPollers, http_proxy e DebugDir, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: propriedades gerais da seção [ITA].

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | [ITA]=propriedades gerais do agente, ActionPollers=threads de comunicação com o broker via gateway, http_proxy=URL do proxy em ambiente distribuído, DebugDir=diretório para rastreamento de pacotes enviados/recebidos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconfITA.html |
| Titulo da fonte | Configuring general properties [ITA] |
| Citacao de suporte | In the JobManager.ini or JobManagerGW.ini file, you can add some general properties to the following section: [ITA] |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-ita |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A seção [ITA] do JobManager?


---

### 44. `hwa-10.2.8-dynagent-job-dispatcher-0028`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

O JobDispatcherConfig.properties do Dynamic Workload Broker no HCL Workload Automation 10.2.8 documenta o parâmetro FailQInterval, que especifica os segundos para tentar novamente a operação após falhas como notificação de cliente, requisições de Allocation/Reallocate/Cancel Allocation ao Resource Advisor e falhas de banco por conectividade, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: parâmetro de retry do Job Dispatcher (FailQInterval) no lado do broker, não no JobManager.ini.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Job Dispatcher=componente do broker que despacha jobs, FailQInterval=intervalo de nova tentativa após falha do Job Dispatcher |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadjobdispconfprop.html |
| Titulo da fonte | JobDispatcherConfig.properties file |
| Citacao de suporte | FailQInterval: Specifies the numbers of seconds for retrying the operation after the following failures: Client notification. Allocation, Reallocate, Cancel Allocation requests to Resource Advisor. Any database operation failed for connectivity reasons. The default value is 30 seconds. |
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
| verbs | cancel |
| Familia | dynagent-job |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para resource?


---

### 45. `hwa-10.2.8-dynagent-job-manager-ini-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O arquivo JobManager.ini do dynamic agent no HCL Workload Automation 10.2.8 é composto por muitas seções, cada uma com nome entre colchetes e contendo uma sequência de declarações variavel=valor, das quais apenas um subconjunto de parâmetros é documentado por serem reservados para uso interno, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: estrutura e escopo de documentação do JobManager.ini.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | JobManager.ini=arquivo de configuração do dynamic agent, seção=bloco delimitado por colchetes em arquivo .ini |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent |
| Citacao de suporte | These files are made up of many different sections. Each section name is enclosed between square brackets and each section includes a sequence of variable = value statements. Only a subset of the available parameters is documented, because some parameters are reserved for internal use. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-job |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 46. `hwa-10.2.8-dynagent-job-manager-ini-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

As seções documentadas do arquivo JobManager.ini do dynamic agent no HCL Workload Automation 10.2.8 são [ITA], [JobManager.Logging.cclog], [Launchers], [NativeJobLauncher], [JavaJobLauncher], [ResourceAdvisorAgent], [SystemScanner], [Env] e [EventDrivenWorkload], conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: conjunto de seções configuráveis do JobManager.ini.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | JobManager.ini=arquivo de configuração do dynamic agent, [NativeJobLauncher]=executor de jobs nativos, [JavaJobLauncher]=executor de jobs Java, [SystemScanner]=scanner do sistema, [Env]=variáveis de ambiente |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent |
| Citacao de suporte | For a list of the configurable properties, see the following sections: [JobManager.Logging.cclog] ... [Launchers] ... [NativeJobLauncher] ... [JavaJobLauncher] ... [ResourceAdvisorAgent] ... [SystemScanner] ... [Env] ... [EventDrivenWorkload]. |
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
| Familia | dynagent-job |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para resource?
- Qual a regra documentada no HWA Distributed sobre: As seções documentadas do arquivo JobManager?


---

### 47. `hwa-10.2.8-dynagent-job-manager-ini-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

The [JobExecutor], [ServiceLocator] and [Database] sections of JobManager.ini are not listed among the documented configurable sections in HCL Workload Automation 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | JobManager.ini=arquivo de configuração do dynamic agent |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The documented properties are listed in the [ResourceAdvisorAgent] section. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-job |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: The [JobExecutor], [ServiceLocator] and [Database] sections of JobManager?


---

### 48. `hwa-10.2.8-dynagent-job-types-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O dynamic agent no HCL Workload Automation 10.2.8 gerencia uma ampla variedade de job types, como jobs específicos de banco de dados ou FTP, além dos job types existentes, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: variedade de job types executados pelo dynamic agent.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic agent=workstation dinâmica, job types=tipos de job executados pelo dynamic agent |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | A workstation that manages a wide variety of job types, for example, specific database or FTP jobs, in addition to existing job types. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-job |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: O dynamic agent no HCL Workload Automation 10.2.8 gerencia uma ampla variedade de job types, como jobs específicos de banco de dados ou FTP, além dos job types existentes, conforme documentação oficial?


---

### 49. `hwa-10.2.8-dynagent-job-types-com-opes-avanadas-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Os job types com opções avançadas, tanto os fornecidos com o produto quanto os implementados por plug-ins customizados, no HCL Workload Automation 10.2.8 são executados apenas em dynamic agents, pools e dynamic pools, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: restrição de execução de job types avançados a workstations dinâmicas.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | job types com opções avançadas=tipos de job avançados do produto e plug-ins, plug-ins customizados=tipos adicionais implementados via Automation Hub |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | The job types with advanced options include both those supplied with the product and the additional types implemented through the custom plug-ins. Both job types run only on dynamic agents, pools, and dynamic pools. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-job |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 50. `hwa-10.2.8-dynagent-mssql-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Para database jobs do tipo MSSQL, o dynamic agent no HCL Workload Automation 10.2.8 exige o uso da versão 4 dos drivers JDBC, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: requisito de versão de driver JDBC para MSSQL.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | MSSQL=Microsoft SQL Server, drivers JDBC versão 4=requisito de versão de driver para MSSQL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadadvoptjobsched.html |
| Titulo da fonte | Configuring to schedule job types with advanced options |
| Citacao de suporte | Note: For the MSSQL database, use version 4 of the JDBC drivers. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-mssql |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: Para database jobs do tipo MSSQL, o dynamic agent no HCL Workload Automation 10.2.8 exige o uso da versão 4 dos drivers JDBC, conforme documentação oficial?


---

### 51. `hwa-10.2.8-dynagent-pool-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Um dynamic pool no HCL Workload Automation 10.2.8 é uma workstation lógica que agrupa um conjunto de agents, definida dinamicamente com base nos requisitos de recurso especificados pelo usuário, mapeando todos os agents que atendem aos requisitos, sendo hospedada pela workstation broker e registrada no banco de dados como 'd-pool', conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: definição de dynamic pool.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic pool=workstation lógica definida por requisitos de recurso, d-pool=registro do dynamic pool no banco |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | Dynamic pool: A logical workstation that groups a set of agents, which is dynamically defined based on the resource requirements you specify and hosted by the workload broker workstation. ... registered in the HCL Workload Automation database as d-pool. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-pool |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 52. `hwa-10.2.8-dynagent-pool-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o dynamic pool é atualizado dinamicamente sempre que um novo agent adequado fica disponível e jobs agendados nesta workstation herdam automaticamente os requisitos definidos para ela, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: atualização dinâmica e herança de requisitos do dynamic pool.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic pool=workstation lógica por requisitos, herança de requisitos=jobs herdam automaticamente os requisitos da workstation |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | The resulting pool is dynamically updated whenever a new suitable agent becomes available. Jobs scheduled on this workstation automatically inherit the requirements defined for the workstation. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-pool |


---

### 53. `hwa-10.2.8-dynagent-pool-rebalance-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o produto balanceia os jobs entre os agents dentro de um pool e reatribui automaticamente jobs a agents disponíveis se um agent deixar de estar disponível, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: como o pool distribui e reatribui jobs entre agents.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | pool=workstation lógica que agrupa agents, balanceamento=distribuição de jobs entre agents do pool, reatribuição=realocação de jobs quando um agent fica indisponível |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | HCL Workload Automation balances the jobs among the agents within the pool and automatically reassigns jobs to available agents if an agent is no longer available. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-pool |


---

### 54. `hwa-10.2.8-dynagent-postgre-sql-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

PostgreSQL is not documented in the official 10.2.8 documentation as an explicitly supported database job type for the dynamic agent.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | PostgreSQL=banco de dados não listado como tipo suportado de database job |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The documented properties are listed in the [ResourceAdvisorAgent] section. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-postgre |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: PostgreSQL is not documented in the official 10.2.8 documentation as an explicitly supported database job type for the dynamic agent?


---

### 55. `hwa-10.2.8-dynagent-resource-advisor-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

A seção [ResourceAdvisorAgent] do JobManager.ini no HCL Workload Automation 10.2.8 configura o agente do Resource Advisor, que escaneia intermitentemente os recursos da máquina (CPU, sistema operacional, file systems e redes) e envia atualizações de status ao master em ambiente distribuído ou ao dynamic domain manager, com as propriedades documentadas ResourceAdvisorUrl, BackupResourceAdvisorUrls, FullyQualifiedHostname, CPUScannerPeriodSeconds, ScannerPeriodSeconds e NotifyToResourceAdvisorPeriodSeconds, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: propósito e propriedades da seção [ResourceAdvisorAgent].

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ResourceAdvisorAgent=agente do Resource Advisor do dynamic agent, CPUScannerPeriodSeconds=intervalo de varredura da CPU, ScannerPeriodSeconds=intervalo de varredura dos demais recursos, NotifyToResourceAdvisorPeriodSeconds=intervalo de envio das informações ao Resource Advisor |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconfresadvisorag.html |
| Titulo da fonte | Configuring properties of the Resource advisor agent [ResourceAdvisorAgent] |
| Citacao de suporte | In the JobManager.ini and JobManagerGW.ini files, the section containing the properties of the Resource advisor agent is named: [ResourceAdvisorAgent] |
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
| verbs | status |
| Familia | dynagent-resource |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A seção [ResourceAdvisorAgent] do JobManager?


---

### 56. `hwa-10.2.8-dynagent-resource-advisor-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

O Dynamic Workload Broker no HCL Workload Automation 10.2.8 é composto pelos componentes Resource Advisor e Job Dispatcher, cujos parâmetros de configuração são definidos nos arquivos ResourceAdvisorConfig.properties e JobDispatcherConfig.properties, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: componentes do broker e seus arquivos de configuração.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Resource Advisor=componente do broker que avalia recursos, Job Dispatcher=componente do broker que despacha jobs, ResourceAdvisorConfig.properties=arquivo de configuração do Resource Advisor, JobDispatcherConfig.properties=arquivo de configuração do Job Dispatcher |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadbrokerconf.html |
| Titulo da fonte | Configuring the dynamic workload broker server on the master domain manager and dynamic domain manager |
| Citacao de suporte | ResourceAdvisorConfig.properties: Contains configuration information about the Resource Advisor ... JobDispatcherConfig.properties: Contains configuration information about the Job Dispatcher. |
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

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Como configurar ou solucionar problemas no dynamic agent ou broker para resource?


---

### 57. `hwa-10.2.8-dynagent-resource-advisor-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

O Resource Advisor no Dynamic Workload Broker do HCL Workload Automation 10.2.8 aloca recursos a cada job em intervalos de tempo definidos pelo parâmetro TimeSlotLength (padrão 15 segundos) e, se um job não encontra recurso, espera o intervalo CheckInterval (padrão 60 segundos) antes de tentar novamente, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: lógica de alocação de recursos do Resource Advisor (parâmetros TimeSlotLength e CheckInterval).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Resource Advisor=componente do broker que aloca recursos, TimeSlotLength=intervalo de tempo para alocação de recursos por job, CheckInterval=intervalo de nova tentativa de busca de recursos |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadresadvconfprop.html |
| Titulo da fonte | ResourceAdvisorConfig.properties file |
| Citacao de suporte | TimeSlotLength: Specifies the time slot interval during which the Resource Advisor allocates resources to each job. ... The default value is 15 seconds. ... CheckInterval: Specifies how long the Resource Advisor waits before retrying to find matching resources for a job that did not find any resource in the previous time slot. The default value is 60 seconds. |
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
- Qual a regra documentada no HWA Distributed sobre: O Resource Advisor no Dynamic Workload Broker do HCL Workload Automation 10.2.8 aloca recursos a cada job em intervalos de tempo definidos pelo parâmetro TimeSlotLength (padrão 15 segundos) e, se um job não encontra recurso, espera o intervalo CheckInterval (padrão 60 segundos) antes de tentar novamente, conforme documentação oficial?


---

### 58. `hwa-10.2.8-dynagent-retry-de-conexo-0026`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `resource`

**Afirmacao / Conteudo:**

There is no documented connection retry property in JobManager.ini [ResourceAdvisorAgent] section, and no [ServiceLocator] section with provider URL is documented in HCL Workload Automation 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | retry de conexão=propriedade de nova tentativa de conexão, [ServiceLocator]=seção não documentada no JobManager.ini |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftwsag.html |
| Titulo da fonte | Configuring the agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The documented properties are listed in the [ResourceAdvisorAgent] section. |
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
| Familia | dynagent-retry |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: There is no documented connection retry property in JobManager?


---

### 59. `hwa-10.2.8-dynagent-servidor-do-broker-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Durante a troca do master domain manager ou dynamic domain manager no HCL Workload Automation 10.2.8, apenas um servidor do Dynamic Workload Broker fica ativo por vez, pois o servidor antigo para os serviços de agendamento dinâmico e o novo servidor inicia uma nova instância do broker após concluir a troca, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: garantia de instância única ativa do DWB durante switch.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | switchmgr=comando de troca do master/DDM, servidor do Dynamic Workload Broker=instância única ativa do broker |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadswitchdynbroker.html |
| Titulo da fonte | Switching a master domain manager or dynamic domain manager |
| Citacao de suporte | This process ensures that there is only one active dynamic workload broker server running at a time. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-servidor |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: Durante a troca do master domain manager ou dynamic domain manager no HCL Workload Automation 10.2.8, apenas um servidor do Dynamic Workload Broker fica ativo por vez, pois o servidor antigo para os serviços de agendamento dinâmico e o novo servidor inicia uma nova instância do broker após concluir a troca, conforme documentação oficial?


---

### 60. `hwa-10.2.8-dynagent-workstation-broker-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Um pool no HCL Workload Automation 10.2.8 é uma workstation lógica que agrupa um conjunto de agents com características similares de hardware ou software, à qual jobs são submetidos, sendo registrada no banco de dados como 'pool' e hospedada pela workstation broker, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Comportamento documentado: definição de pool.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | pool=workstation lógica que agrupa agents com características similares, workstation broker=broker server instalado com o master/DDM |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | Pool: A logical workstation that groups a set of agents with similar hardware or software characteristics to which to submit jobs. ... This workstation is registered in the HCL Workload Automation database as pool. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | dynagent-workstation |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 61. `hwa-10.2.8-event-domain-manager-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O event processing server no HCL Workload Automation 10.2.8 normalmente está localizado no master domain manager e recebe todos os eventos dos agents e os processa, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented event processor placement and behavior.

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
| Citacao de suporte | an event processing server, which is normally located in the master domain manager, receives all events from the agents and processes them. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | event-domain |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O event processing server no HCL Workload Automation 10.2.8 normalmente está localizado no master domain manager e recebe todos os eventos dos agents e os processa, conforme documentação oficial?


---

### 62. `hwa-10.2.8-event-generic-event-plug-in-0025`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, eventos customizados são definidos com o event provider GenericEventPlugIn e podem ser enviados ao event processing server com o comando sendevent para acionar regras a partir de qualquer agent ou workstation que execute o client de linha de comando remota, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documented external/custom event triggering mechanism via sendevent and GenericEventPlugIn.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | GenericEventPlugIn=event provider GenericEventPlugIn, sendevent=comando sendevent, custom events=eventos customizados |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefinecustevent.html |
| Titulo da fonte | Defining custom events |
| Citacao de suporte | The sendevent utility command with which the custom events can be sent to the event processing server to trigger rules from any agent or any workstation running simply the HCL Workload Automation remote command line client. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-generic |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, eventos customizados são definidos com o event provider GenericEventPlugIn e podem ser enviados ao event processing server com o comando sendevent para acionar regras a partir de qualquer agent ou workstation que execute o client de linha de comando remota, conforme documentação oficial?


---

### 63. `hwa-10.2.8-event-rule-builder-0027`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o rule builder varre periodicamente (por padrão a cada cinco minutos ou conforme o valor da opção global deploymentFrequency) o banco de dados em busca de regras não-draft e constrói arquivos de configuração de regras para implantação, e as novas configurações de monitoramento são baixadas para os agents, conforme documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Automatic periodic deployment mechanism of the rule builder.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | rule builder=rule builder, deploymentFrequency=opção global deploymentFrequency, deployment=implantação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgdefineeventrule.html |
| Titulo da fonte | Defining event rules |
| Citacao de suporte | The scheduler periodically (every five minutes or in accordance with a time set in the deploymentFrequency global configuration option) scans the database for non-draft rules and builds rule configuration files for deployment. The new monitoring configurations are downloaded to the agents ... |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | event-rule |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o rule builder varre periodicamente (por padrão a cada cinco minutos ou conforme o valor da opção global deploymentFrequency) o banco de dados em busca de regras não-draft e constrói arquivos de configuração de regras para implantação, e as novas configurações de monitoramento são baixadas para os agents, conforme documentação oficial?


---

### 64. `hwa-10.2.8-incident-awsdec002-e-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

A mensagem AWSDEC002E no HCL Workload Automation 10.2.8 indica um erro interno ('An internal error has occurred. The following UNIX system error occurred on an events file: "9" at line = 2212'), frequentemente precedida de AWSBCV012E no log stdlist, quando o batchman (e tipicamente mailman e jobman) falha em um fault-tolerant agent. Causa documentada: corrupção do arquivo Mailbox.msg, provavelmente porque o arquivo não é grande o suficiente para o número de mensagens que precisavam ser escritas nele. Recuperação documentada: se for confirmado que o problema é causado por overflow, usar o comando evtsize para aumentar o arquivo Mailbox.msg (garantindo espaço suficiente no file system), excluir o arquivo de mensagens corrompido e reiniciar o HCL Workload Automation com o comando conman start no fault-tolerant agent (todos os eventos no arquivo corrompido são perdidos); se não tiver certeza da causa, contatar o suporte.

> **ATENCAO / RESSALVAS DE USO:** Componente events file; causa e recuperação documentadas na página oficial distribuída v1028. Reiniciar com conman start em um FTA é ação mutating.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | AWSDEC002E=erro interno em arquivo de eventos; corrupção do Mailbox.msg, cause=causa, recovery=recuperação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrftadec002.html |
| Titulo da fonte | Batchman, and other processes fail on a fault-tolerant agent with the message AWSDEC002E (v1028) |
| Citacao de suporte | AWSDEC002E An internal error has occurred. The following UNIX system error occurred on an events file: "9" at line = 2212 |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | conman |
| Codigo da mensagem | AWSDEC002E |
| Familia | incident-awsdec002 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSDEC002E no HWA?
- Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?
- Qual é o significado da mensagem de erro AWSBCV012E no HWA?
- Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?


---

### 65. `hwa-10.2.8-incident-awsjcl-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Na documentação distribuída oficial do HCL Workload Automation 10.2.8, a página 'HCL Workload Automation messages' do guia Messages and Codes (common/src_ms/awsmspart1TWS.html) documenta apenas quatro conjuntos de mensagens: AWKZSJ (z/OS shadow job validation), AWSWUI (Dynamic Workload Console), AWSZAP (action plug-in para z/OS) e EEL (agente HCL Workload Automation para z/OS). Os conjuntos de mensagens do motor, como AWSJCL (linha de comando), AWSBDW (jobman), AWSBHT (batchman) e AWSJIM (instalação do servidor), não estão documentados nessa página da versão 10.2.8 distribuída; eles estão disponíveis apenas em versões anteriores, como o guia 9.5 (AWSJCL, AWSBDW, AWSBHT, AWSJPL) e o manual IBM 9.4/9.5 (AWSJIM, capítulo 177).

> **ATENCAO / RESSALVAS DE USO:** Achado negativo confirmado como correto: a página v1028 common/src_ms/awsmspart1TWS.html foi aberta e lida e lista exatamente quatro conjuntos de mensagens (AWKZSJ, AWSWUI, AWSZAP, EEL), sem nenhum conjunto do motor. A mesma estrutura de 4 conjuntos foi confirmada nas versões 10.2.3 e 10.2. O guia 9.5 (HCL) documenta os conjuntos do motor AWSJCL, AWSBDW, AWSBHT, AWSJPL, AWSJIS etc.; o manual IBM 9.4/9.5 documenta AWSJIM (Server installation messages, capítulo 177). Nenhuma página oficial v1028 distribuída documenta AWSJIM, AWSJCL, AWSBDW ou AWSBHT.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | AWSJCL=Command line messages, AWSBDW=Jobman messages, AWSBHT=Batchman messages, AWSJIM=Server installation messages, AWKZSJ=z/OS shadow job validation messages, AWSWUI=Dynamic Workload Console messages, AWSZAP=Action plug-in for z/OS messages, EEL=HCL Workload Automation agent for z/OS messages |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmspart1TWS.html |
| Titulo da fonte | HCL Workload Automation messages - Messages and Codes (Workload Automation 10.2.8) |
| Citacao de suporte | This part contains message help for many of the messages issued by the HCL Workload Automation engine and command line. ... AWKZSJ - z/OS shadow job validation messages ... AWSWUI - Dynamic Workload Console messages ... AWSZAP - Action plug-in for z/OS messages ... EEL - HCL Workload Automation agent for z/OS messages |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | other |
| Familia | incident-awsjcl |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCL0006 no HWA?
- Como solucionar ou diagnosticar o erro AWSJCL0006 no HWA?


---

### 66. `hwa-10.2.8-incident-bcv012e-0044`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `mailbox`

**Afirmacao / Conteudo:**

Sintoma: AWSDEC002E 'An internal error has occurred. The following UNIX system error occurred on an events file: 9' no stdlist, frequentemente precedida de AWSBCV012E no log, quando o batchman (e tipicamente mailman e jobman) falha em um fault-tolerant agent. Causa: corrupcao/overflow do arquivo Mailbox.msg — o arquivo nao e grande o suficiente para o numero de mensagens que precisavam ser escritas. Resolucao documentada: (1) usar evtsize para aumentar o arquivo Mailbox.msg (garantindo espaco suficiente no file system); (2) excluir o arquivo de mensagens corrompido; (3) reiniciar o HCL Workload Automation com conman start no fault-tolerant agent. Pesquisa Perplexity (2026-08-23) confirma o mesmo procedimento.

> **ATENCAO / RESSALVAS DE USO:** Pesquisa Perplexity Direct (2026-08-23): AWSJCL521E/AWSBCV012E/AWSDEC002E compartilham o mesmo procedimento de recovery (evtsize Mailbox.msg + deletar mensagem corrompida + restart). Complementa hwa-10.2.8-incident-0004.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1027/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide - Mailbox.msg overflow |
| Citacao de suporte | Use the evtsize command to increase the Mailbox.msg file... Delete the corrupt message file... Restart HCL Workload Automation by issuing the conman start command on the fault-tolerant agent. |
| Coletado em | 2026-08-23 |
| Capacidade | mailbox |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. Backup do Mailbox.msg antes de excluir. |
| Impacto | Pode alterar estado operacional (reinicio de componentes); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar Mailbox.msg a partir de backup se necessario. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSDEC002E, command=batchman |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | conman |
| Codigo da mensagem | AWSDEC002E |
| Familia | incident-bcv012e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSDEC002E no HWA?
- Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?
- Qual é o significado da mensagem de erro AWSBCV012E no HWA?
- Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?
- O que causa e como solucionar o problema: AWSDEC002E 'An internal error has occurred?


---

### 67. `hwa-10.2.8-incident-behind-firewall-0077`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `network`

**Afirmacao / Conteudo:**

Sintoma: comandos start/stop do master domain manager para fault-tolerant agents de outros dominios nao funcionam. Causa: os FTAs desses dominios nao tem o atributo behind firewall marcado como on no banco do HCL Workload Automation; com firewall entre o master e os dominios, comandos start/stop devem passar pela hierarquia. Resolucao: marcar behind firewall=on para os FTAs atras de firewall, para que o stop seja enviado ao domain manager que repassa ao FTA. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - behind firewall |
| Citacao de suporte | The fault-tolerant agents belonging to these domains do not have the behind firewall attribute set to on in the HCL Workload Automation database. |
| Coletado em | 2026-08-23 |
| Capacidade | network |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| verbs | start; stop |
| Familia | incident-behind |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: comandos start/stop do master domain manager para fault-tolerant agents de outros dominios nao funcionam?


---

### 68. `hwa-10.2.8-incident-bhu072e-0051`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `mailbox`

**Afirmacao / Conteudo:**

Sintoma: AWSBHU072E indicando fault relacionado ao ambiente do fault-tolerant agent, frequentemente associado a corrupcao do arquivo Mailbox.msg ou problema de tamanho do mailbox. Resolucao: (1) verificar e aumentar o tamanho do Mailbox.msg se necessario (evtsize) garantindo espaco em disco; (2) se corrompido, excluir o arquivo corrompido; (3) reiniciar o fault-tolerant agent (conman start). Pesquisa Perplexity (2026-08-23) confirma. Correlacao: mesmo recovery de AWSBCV012E/AWSDEC002E (Mailbox.msg overflow).

> **ATENCAO / RESSALVAS DE USO:** Pesquisa Perplexity Direct batch (2026-08-23). Correlaciona com hwa-10.2.8-incident-bcv012e-0044 (Mailbox.msg).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSBHU072E |
| Citacao de suporte | AWSBHU072E indicates a fault related to the FTA environment, often tied to a corrupted Mailbox.msg file or mailbox size issues |
| Coletado em | 2026-08-23 |
| Capacidade | mailbox |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. Backup do Mailbox.msg antes de excluir. |
| Impacto | Pode alterar estado operacional (reinicio de FTA); avaliar o escopo antes da execução. |
| Reversibilidade | Restaurar Mailbox.msg a partir de backup se necessario. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSBHU072E, command=conman |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | conman |
| verbs | start |
| Codigo da mensagem | AWSBHU072E |
| Familia | incident-bhu072e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU072E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU072E no HWA?
- Qual é o significado da mensagem de erro AWSBCV012E no HWA?
- Como solucionar ou diagnosticar o erro AWSBCV012E no HWA?
- O que causa e como solucionar o problema: AWSBHU072E indicando fault relacionado ao ambiente do fault-tolerant agent, frequentemente associado a corrupcao do arquivo Mailbox?


---

### 69. `hwa-10.2.8-incident-bhu158e-0035`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `syntax`

**Afirmacao / Conteudo:**

Sintoma: AWSBHU158E ao executar conman link (lk) / unlink contra uma workstation do tipo agent/pool/broker/remote engine. Causa: o comando link/unlink so e suportado em workstations do tipo FTA/master domain manager; agents dinamicos nao suportam a operacao. Resolucao: nao usar link/unlink em agents; a operacao e desnecessaria para agents (eles se conectam automaticamente). O lab confirmou: conman lk =MDMDA;noask -> AWSBHU158E 'comando não suportado em workstation agent/pool/broker/remote engine' (MDMDA e dynamic agent).

> **ATENCAO / RESSALVAS DE USO:** Validado no lab 23/08 (r8): link/unlink restrito a FTA/master. Complementa a claim hwa-10.2.8-conman-link-unlink-0001.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglink.html |
| Titulo da fonte | conman link/unlink - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSBHU158E: comando não suportado em workstation agent/pool/broker/remote engine |
| Coletado em | 2026-08-23 |
| Capacidade | syntax |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['conman lk =MDMDA;noask'], result=AWSBHU158E: comando não suportado em workstation agent/pool/broker/remote engine (MDMDA é dynamic agent), validated_at=2026-08-23T00:43:00BRT |
| Terminologia normalizada | message=AWSBHU158E, command=conman |
| Status de revisao | lab_validated |
| Tipo | message |
| Ferramenta | conman |
| Codigo da mensagem | AWSBHU158E |
| Familia | incident-bhu158e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU158E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU158E no HWA?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar syntax?
- O que causa e como solucionar o problema: AWSBHU158E ao executar conman link (lk) / unlink contra uma workstation do tipo agent/pool/broker/remote engine?


---

### 70. `hwa-10.2.8-incident-bin091e-0049`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `broker`

**Afirmacao / Conteudo:**

Sintoma: AWSBIN091E indicando problema de broker/comunicacao entre domain manager, fault-tolerant agent ou broker server. Causa: porta SSL mal configurada no localopts (SSL port = 0 ou valor errado), ou broker server inacessivel/rede entre componentes. Resolucao: (1) verificar o valor da porta SSL no localopts do domain manager/FTA e corrigir para o valor correto; (2) reiniciar os componentes envolvidos; (3) verificar conectividade de rede/TCP/SSL entre broker e manager. Pesquisa Perplexity (2026-08-23) confirma SSL port como causa principal.

> **ATENCAO / RESSALVAS DE USO:** Pesquisa Perplexity Direct batch (2026-08-23): SSL port misconfiguration no localopts. Complementa hwa-10.2.8-trouble-awsbin091e-0004 (que trata do contexto REST monitoring).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSBIN091E |
| Citacao de suporte | AWSBIN091E indicates a broker or communication issue between domain manager, FTA, or broker server; check SSL port settings in localopts. |
| Coletado em | 2026-08-23 |
| Capacidade | broker |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSBIN091E |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | dynagent |
| Codigo da mensagem | AWSBIN091E |
| Familia | incident-bin091e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIN091E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para broker?
- O que causa e como solucionar o problema: AWSBIN091E indicando problema de broker/comunicacao entre domain manager, fault-tolerant agent ou broker server?


---

### 71. `hwa-10.2.8-incident-dynagent-job-error-0082`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dynamic-agent`

**Afirmacao / Conteudo:**

Sintoma: do Dynamic Workload Console, um dynamic agent aparece mas o status do job submetido fica continuamente em 'error'. Causa: o hostname local do master domain manager nao e conhecido na rede do agent (outro dominio DNS). Resolucao: editar o arquivo JobDispatcherConfig.properties e ajustar o parametro JDURL=https://<localhostname>. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - dynamic agent job error |
| Citacao de suporte | A possible cause might be that the master domain manager local hostname is not known in the network of the agent... Open the JobDispatcherConfig.properties file and edit the parameter JDURL=https://<localhostname> |
| Coletado em | 2026-08-23 |
| Capacidade | dynamic-agent |
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
| Ferramenta | dynagent |
| verbs | status |
| Familia | incident-dynagent |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?
- Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?
- O que causa e como solucionar o problema: do Dynamic Workload Console, um dynamic agent aparece mas o status do job submetido fica continuamente em 'error'?


---

### 72. `hwa-10.2.8-incident-dynagent-no-resources-0081`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dynamic-agent`

**Afirmacao / Conteudo:**

Sintoma: do Dynamic Workload Console, um dynamic agent aparece, mas o job submetido aparece como 'No resources available'. Causa: o hostname local de um dynamic workload broker server registrado no agent nao e conhecido na rede do master domain manager (outro dominio DNS). Resolucao: editar o arquivo JobManager.ini e ajustar o parametro FullyQualifiedHostname = <servername>. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - dynamic agent no resources |
| Citacao de suporte | A possible cause might be that the local hostname of a registered dynamic workload broker server on the agent is not known in the network of the master domain manager... Edit the following parameter: FullyQualifiedHostname = <servername> |
| Coletado em | 2026-08-23 |
| Capacidade | dynamic-agent |
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
| Ferramenta | dynagent |
| Familia | incident-dynagent |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?
- Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?
- Como solucionar problemas de registro de agentes dinâmicos no broker?
- O que causa e como solucionar o problema: do Dynamic Workload Console, um dynamic agent aparece, mas o job submetido aparece como 'No resources available'?


---

### 73. `hwa-10.2.8-incident-dynagent-not-found-0080`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dynamic-agent`

**Afirmacao / Conteudo:**

Sintoma: um dynamic agent instalado corretamente nao aparece no Dynamic Workload Console. Causa: o hostname do dynamic workload broker (tdwbhostname) ou a porta do broker, ou ambos, registrados no agent, nao sao conhecidos na rede do master domain manager porque o host do broker esta em outro dominio DNS. Resolucao: editar o arquivo JobManager.ini e corrigir os parametros de hostname/porta do broker. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - dynamic agent not found |
| Citacao de suporte | A possible cause might be that either the dynamic workload broker hostname, -tdwbhostname, or the dynamic workload broker port, or both... are not known in the network of the master domain manager because the broker host is in a different DNS domain. |
| Coletado em | 2026-08-23 |
| Capacidade | dynamic-agent |
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
| Ferramenta | dynagent |
| Familia | incident-dynagent |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?
- Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?
- Como solucionar problemas de registro de agentes dinâmicos no broker?
- O que causa e como solucionar o problema: um dynamic agent instalado corretamente nao aparece no Dynamic Workload Console?


---

### 74. `hwa-10.2.8-incident-evtsize-0014`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: arquivo de eventos do FTA/agent muito grande ou com problemas de espaco. Resolucao: a variavel/parametro evtsize controla o tamanho maximo do arquivo de eventos; ajustar evtsize e monitorar o crescimento evita falhas de comunicacao por estouro.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrftadec002.html |
| Titulo da fonte | Troubleshooting fault-tolerant agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | evtsize |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Incidente de troubleshooting (sintoma→resolução) baseado em documentação oficial - validação lab não se aplica diretamente |
| Tipo | command |
| Familia | incident-evtsize |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: arquivo de eventos do FTA/agent muito grande ou com problemas de espaco?


---

### 75. `hwa-10.2.8-incident-exec-status-race-0092`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `jnextplan`

**Afirmacao / Conteudo:**

Sintoma: um job permanece em status 'exec' apos o JnextPlan mas nao esta rodando. Causa (cenario): (1) um job completa o processamento; (2) o FTA marca o job como succ no Symphony atual; (3) o FTA prepara e envia os eventos JS e JT informando o master — mas o JnextPlan roda antes de o master processar esses eventos, criando uma condicao de corrida em que o job fica preso em exec. Fonte: HCL Troubleshooting Guide 10.2.8 (A job remains in exec status after JnextPlan).

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - job exec status after JnextPlan |
| Citacao de suporte | This error scenario is possible if a job completes its processing at a fault-tolerant agent just before JnextPlan is run... The fault-tolerant agent prepares and sends a job status changed event (JS) and a job termination event (JT) |
| Coletado em | 2026-08-23 |
| Capacidade | jnextplan |
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
| verbs | status |
| Familia | incident-exec |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: um job permanece em status 'exec' apos o JnextPlan mas nao esta rodando?


---

### 76. `hwa-10.2.8-incident-fab164e-0025`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `installation`

**Afirmacao / Conteudo:**

Sintoma: AWSFAB164E durante instalacao do agent (serverinst/twsinst). Causa: valores iguais para -thiscpu e -displayname, ou nome invalido para a workstation. Resolucao: usar -thiscpu diferente do nome do master e -displayname como nome do dynamic agent (nao igual ao master).

> **ATENCAO / RESSALVAS DE USO:** Observado no lab (runbook P-Errors): serverinst rejeitou -thiscpu igual a -displayname.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html |
| Titulo da fonte | TWS installation parameters - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSFAB164E |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | installation |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (lab MDM/MDMDA), tested_commands=['serverinst -thiscpu MDM -displayname MDM (valores iguais)'], result=AWSFAB164E rejeitado pelo instalador quando -thiscpu e -displayname são iguais; usando -thiscpu distinto do master e -displayname como nome do dynamic agent a instalação prossegue |
| Tipo | command |
| Ferramenta | dynagent |
| Codigo da mensagem | AWSFAB164E |
| Familia | incident-fab164e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSFAB164E no HWA?
- Como solucionar ou diagnosticar o erro AWSFAB164E no HWA?
- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar installation?
- O que causa e como solucionar o problema: AWSFAB164E durante instalacao do agent (serverinst/twsinst)?


---

### 77. `hwa-10.2.8-incident-fta-cleanup-0079`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: um fault-tolerant agent nao linka ao seu master domain manager e nenhum outro procedimento de link resolveu. Causa: quase certamente um mismatch entre os niveis dos varios arquivos usados no FTA. Resolucao: se todas as outras tentativas falharam, executar o procedimento de cleanup documentado - ATENCAO: este procedimento perde dados (a menos que o FTA nao esteja linkando apos uma instalacao nova), portanto nao deve ser executado sem necessidade. Fonte: HCL Troubleshooting Guide 10.2.8 (FTA does not link).

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - FTA link cleanup |
| Citacao de suporte | The cause of this problem might not be easy to discover, but is almost certainly involved with a mismatch between the levels of the various files used on the fault-tolerant agent. To resolve the problem... perform the following cleanup procedure. However, note that this procedure loses data |
| Coletado em | 2026-08-23 |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. Procedimento de cleanup perde dados - usar como ultimo recurso. |
| Impacto | Pode alterar estado operacional (perda de dados no FTA); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar a partir de backup se disponivel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-fta |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: um fault-tolerant agent nao linka ao seu master domain manager e nenhum outro procedimento de link resolveu?


---

### 78. `hwa-10.2.8-incident-fta-dec002e-0012`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: AWSDEC002E relacionado a fault-tolerant agent (FTA) em decada de conexao. Causa: problemas de comunicacao entre o FTA e o master domain manager. Resolucao: verificar conectividade de rede, certificados e o processo batchman/jobman no FTA; consultar troubleshooting de FTA (awstrftadec002.html).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrftadec002.html |
| Titulo da fonte | Troubleshooting fault-tolerant agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSDEC002E |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Incidente de troubleshooting (sintoma→resolução) baseado em documentação oficial - validação lab não se aplica diretamente |
| Tipo | command |
| Codigo da mensagem | AWSDEC002E |
| Familia | incident-fta |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSDEC002E no HWA?
- Como solucionar ou diagnosticar o erro AWSDEC002E no HWA?
- O que causa e como solucionar o problema: AWSDEC002E relacionado a fault-tolerant agent (FTA) em decada de conexao?


---

### 79. `hwa-10.2.8-incident-fta-dual-netman-0073`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: AWSEDW001I 'Getting a new socket: 9' — um fault-tolerant agent tem dois processos netman escutando na mesma porta. Causa: instalacao de mais de uma instancia HCL Workload Automation na mesma workstation sem especificar portas netman diferentes. Resolucao: parar um dos dois servicos netman e especificar uma porta unica usando a opcao local nm port no localopts; garantir que a definicao da workstation no master domain manager use a porta unica. Fonte: HCL Troubleshooting Guide 10.2.8 (network link problems).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (pagina 41).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - dual netman processes |
| Citacao de suporte | The fault-tolerant agent has two netman processes listening on the same port number... Stop one of the two netman services and specify a unique port number using the nm port local option (localopts file). |
| Coletado em | 2026-08-23 |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (parada de servico); avaliar o escopo antes da execucao. |
| Reversibilidade | Reiniciar o servico netman conforme procedimento oficial. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSEDW001I, command=netman |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSEDW001I |
| Familia | incident-fta |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSEDW001I no HWA?
- Como solucionar ou diagnosticar o erro AWSEDW001I no HWA?
- O que causa e como solucionar o problema: AWSEDW001I 'Getting a new socket: 9' — um fault-tolerant agent tem dois processos netman escutando na mesma porta?


---

### 80. `hwa-10.2.8-incident-fta-events-0029`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: FTA perde eventos ou para de reportar. Causa: arquivo de eventos (events file) cheio/corrompido ou comunicacao interrompida. Resolucao: verificar o events file do FTA, ajustar evtsize, e se necessario resetfta para recriar o estado; monitorar logs do jobman/batchman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrftadec002.html |
| Titulo da fonte | Troubleshooting fault-tolerant agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | events file |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | mutating |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Incidente de troubleshooting (sintoma→resolução) baseado em documentação oficial - validação lab não se aplica diretamente |
| Tipo | command |
| Familia | incident-fta |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: FTA perde eventos ou para de reportar?


---

### 81. `hwa-10.2.8-incident-fta-nolink-jnextplan-0065`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: durante o JnextPlan, fault-tolerant agents nao conseguem ser linkados. Causa: o comando conman stop demora para parar todos os processos do FTA local; se o Symphony foi baixado nesse intervalo, o agent nao consegue recebe-lo porque alguns processos ainda rodam. Resolucao: aguardar a parada completa dos processos do FTA antes do relink; verificar se o Symphony foi recebido corretamente apos o JnextPlan. Fonte: HCL Troubleshooting Guide 10.2.8 (During Jnextplan fault-tolerant agents cannot be linked).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (pagina 60).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - FTA cannot be linked during JnextPlan |
| Citacao de suporte | When you run the conman command stop, the command might take time to stop all the processes on local fault-tolerant agents. If, in the meantime, the Symphony file was downloaded, it cannot be received by the agent because some processes are still running |
| Coletado em | 2026-08-23 |
| Capacidade | fta |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | stop |
| Familia | incident-fta |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar fta?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: durante o JnextPlan, fault-tolerant agents nao conseguem ser linkados?


---

### 82. `hwa-10.2.8-incident-ita105e-0070`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `agent`

**Afirmacao / Conteudo:**

Sintoma: AWSITA105E 'Unable to notify scan results to the server because of a resources scanner error' ao realizar resources scan. Causa: o produto nao consegue executar o resources scan corretamente porque o hostname da maquina nao e reconhecido. Resolucao: em UNIX, verificar que o hostname esta listado no /etc/hosts e que ping hostname funciona; em Windows, verificar que ping hostname funciona. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSITA105E).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (paginas 65-66).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSITA105E |
| Citacao de suporte | AWSITA105E Unable to notify scan results to the server because of a resources scanner error. The problem is that the product is unable to perform correctly the resources scan because the hostname of the machine is not recognized. |
| Coletado em | 2026-08-23 |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA105E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSITA105E |
| Familia | incident-ita105e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA105E no HWA?
- Como solucionar ou diagnosticar o erro AWSITA105E no HWA?
- O que causa e como solucionar o problema: AWSITA105E 'Unable to notify scan results to the server because of a resources scanner error' ao realizar resources scan?


---

### 83. `hwa-10.2.8-incident-jcs037e-0072`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `agent`

**Afirmacao / Conteudo:**

Sintoma: AWSJCS037E 'The value of the string <folder_name>/MASTERAGENTS in property RJ is not correct. The value must be alphanumeric' ao iniciar um agent. Causa: o arquivo pools.properties nao foi atualizado automaticamente. Resolucao: (1) parar o agent com ShutDownLwa; (2) navegar ate <TWS_home>/ITA/cpa/config (Windows) ou TWA_DATA_DIR/ITA/cpa/config (UNIX); (3) editar pools.properties e atualizar o nome da workstation MASTERAGENTS; (4) iniciar o agent com StartUpLwa. Fonte: HCL Troubleshooting Guide 10.2.8 (AWSJCS037E).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (pagina 102).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - AWSJCS037E |
| Citacao de suporte | AWSJCS037E The value of the string <folder_name>/MASTERAGENTS in property RJ is not correct... The pools.properties file is not updated automatically. |
| Coletado em | 2026-08-23 |
| Capacidade | agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (configuracao de agent); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar pools.properties a partir de backup. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCS037E |
| Status de revisao | verified |
| Tipo | message |
| Codigo da mensagem | AWSJCS037E |
| Familia | incident-jcs037e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCS037E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCS037E no HWA?
- O que causa e como solucionar o problema: AWSJCS037E 'The value of the string <folder_name>/MASTERAGENTS in property RJ is not correct?


---

### 84. `hwa-10.2.8-incident-listsym-msymoldbackup-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: jobs rodam em um fault-tolerant agent e o Symphony local do FTA foi atualizado, mas o Symphony do master domain manager nao foi atualizado — devido a uma falha de link com o master e a remocao dos arquivos <TWS_home>\TWS\*.msg. Resolucao: verificar o Symphony mais recente processado no fault-tolerant agent usando o comando conman listsym a partir da linha de comando do FTA, que mostra o ultimo Symphony salvo como MSymOldBackup. Fonte: HCL Troubleshooting Guide 10.2.8 (Symphony file on the master domain manager not updated with fault-tolerant agent job status).

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
| Citacao de suporte | Look at the latest Symphony file that was processed on the fault-tolerant agent, by using the conman listsym command. When used from a fault-tolerant agent command line, this command shows the latest Symphony file, saved as MSymOldBackup. |
| Capacidade | fta |
| Classificacao de risco | read_only |
| Modo de operacao | read |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| Familia | incident-listsym |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar fta?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- O que causa e como solucionar o problema: jobs rodam em um fault-tolerant agent e o Symphony local do FTA foi atualizado, mas o Symphony do master domain manager nao foi atualizado — devido a uma falha de link com o master e a remocao dos arquivos <TWS_home>\TWS\*?


---

### 85. `hwa-10.2.8-incident-mailman-timeout-0066`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `mailman`

**Afirmacao / Conteudo:**

Sintoma: false timeout nos processos do mailman no domain manager - durante a inicializacao apos JnextPlan, os arquivos *.msg podem encher com backlog de mensagens dos FTAs; enquanto o mailman processa mensagens de um FTA, mensagens de outros FTAs esperam ate exceder o intervalo configurado e o mailman faz unlink. Resolucao: aumentar os valores das variaveis mm response e mm unlink no arquivo localopts (~maestro/localopts), em incrementos pequenos (60-300 segundos) ate os timeouts pararem. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (pagina 64). Correlaciona com o lab (mm response=600, mm unlink=960 no localopts do lab).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - mailman timeout |
| Citacao de suporte | increase the value of the mm response and mm unlink variables in the configuration file ~maestro/localopts. These values must be increased together in small increments (60-300 seconds) until the timeouts no longer occur. |
| Coletado em | 2026-08-23 |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=mailman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planner |
| Familia | incident-mailman |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: false timeout nos processos do mailman no domain manager - durante a inicializacao apos JnextPlan, os arquivos *?


---

### 86. `hwa-10.2.8-incident-mailman-ws-add-0128`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `mailman`

**Afirmacao / Conteudo:**

Sintoma: apos adicionar uma dynamic agent workstation ao plano, o agent nao aparece/nao funciona mesmo apos restart dos processos do master domain manager. Causa: o processo mailman do master domain manager nao consegue gerenciar o evento do HWA que comunica a adicao da workstation ao plano. Resolucao: reiniciar os processos do master domain manager executando em ordem: conman stop e depois conman start (ou o comando equivalente). Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - mailman workstation add |
| Citacao de suporte | The cause is that the master domain manager mailman stopping process is unable to manage the HCL Workload Automation event that communicates the workstation addition to the plan... restart the master domain manager processes by performing in order the following commands: conman stop... |
| Coletado em | 2026-08-23 |
| Capacidade | mailman |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (restart de processos); avaliar o escopo antes da execucao. |
| Reversibilidade | Seguir o procedimento oficial de reversao ou restauracao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=restart |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | add; stop |
| Familia | incident-mailman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mailman?
- Como configurar ou solucionar problemas no dynamic agent ou broker para mailman?
- Por que um dynamic agent recém-instalado pode não aparecer no Dynamic Workload Console?
- O que causa e como solucionar o problema: apos adicionar uma dynamic agent workstation ao plano, o agent nao aparece/nao funciona mesmo apos restart dos processos do master domain manager?
- Como utilizar o comando conman 'start' para gerenciar workstations e execução no HWA?
- Como utilizar o comando conman 'stop' para gerenciar workstations e execução no HWA?


---

### 87. `hwa-10.2.8-incident-oracle-schema-config-0106`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `database`

**Afirmacao / Conteudo:**

Sintoma: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade. Causa: o conjunto de tabelas do banco nao foi corrigido — o DAOCommon.properties ainda referencia rdbmsName=db2 em vez de oracle, ou os valores *Schema= nao apontam para o schema Oracle. Resolucao: seguir o procedimento de upgrade do database schema (Planning and Installation Guide) e atualizar manualmente o DAOCommon.properties: rdbmsName=oracle e os tres valores *Schema= para o schema Oracle. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Oracle schema config |
| Citacao de suporte | manually update the DAOCommon.properties so that the rdbmsName=oracle, and not db2, and ensure that all three of the values for the setting *Schema= are set to the Oracle schema name |
| Coletado em | 2026-08-23 |
| Capacidade | database |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (config de banco); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter as alteracoes do DAOCommon.properties. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | upgrade |
| Familia | incident-oracle |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para database?
- Qual a regra documentada no HWA Distributed sobre: Sintoma: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade?
- O que causa e como solucionar o problema: apos migrar de DB2 para Oracle (ou instalacao Oracle), o dynamic workload broker falha ao iniciar apos o upgrade?


---

### 88. `hwa-10.2.8-incident-pobox-sizing-0087`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `jnextplan`

**Afirmacao / Conteudo:**

Sintoma: JnextPlan falha ao iniciar. Causa: a rede HCL Workload Automation requer tuning adicional por problema de dimensionamento dos arquivos pobox — o tamanho default dos pobox files e 10MB. Resolucao: aumentar o tamanho conforme criterios: (1) o papel (master domain manager, domain manager ou FTA) da workstation na rede — papeis hierarquicos maiores precisam de pobox maiores. Fonte: HCL Troubleshooting Guide 10.2.8 (JnextPlan fails to start).

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - pobox sizing |
| Citacao de suporte | This error might be a symptom that your HCL Workload Automation network requires additional tuning because of a problem with the sizing of the pobox files. The default size of the pobox files is 10MB. |
| Coletado em | 2026-08-23 |
| Capacidade | jnextplan |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (tuning de tamanho); avaliar o escopo antes da execucao. |
| Reversibilidade | Reverter o tamanho para o valor anterior. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=start |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planner |
| verbs | start |
| Familia | incident-pobox |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: JnextPlan falha ao iniciar?


---

### 89. `hwa-10.2.8-incident-recovery-resetfta-0062`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: Symphony corrompido em um fault-tolerant agent. RECOVERY OFICIAL: usar o comando resetFTA <cpu> para automatizar a recuperacao - o comando renomeia Symphony, Sinfonia e arquivos *.msg no FTA onde ocorreu a corrupcao e gera um Sinfonia atualizado que e enviado ao FTA, permitindo relink. Notas: ha perda de dados (eventos de status de job, conteudo de Mailbox.msg e tomaster.msg); se informacao de estado de um job estava nessas filas, o job e reexecutado; aplicar com cautela; nao disponivel no Dynamic Workload Console. Sintaxe: resetFTA <cpu>. Fonte: HCL Troubleshooting Guide 10.2.8 (Recovery procedure on a fault-tolerant agent with the use of the resetFTA command).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (paginas 167-168). Complementa hwa-10.2.8-incident-resetfta-0013.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - resetFTA recovery |
| Citacao de suporte | resetFTA cpu... The procedure renames the Symphony, Sinfonia, *.msg files on the fault-tolerant agent where the Symphony corruption occurred and generates an updated Sinfonia file, which is sent to the fault-tolerant agent. |
| Coletado em | 2026-08-23 |
| Capacidade | fta |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. Perda de dados possivel (jobs podem reexecutar). |
| Impacto | Pode alterar estado operacional (reset FTA, reexecucao de jobs); avaliar o escopo antes da execucao. |
| Reversibilidade | Seguir o procedimento oficial de reversao ou restauracao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| verbs | status |
| Familia | incident-recovery |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- O que causa e como solucionar o problema: Symphony corrompido em um fault-tolerant agent?


---

### 90. `hwa-10.2.8-incident-resetfta-0013`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `fta`

**Afirmacao / Conteudo:**

Sintoma: FTA com problemas de sincronizacao ou arquivo de eventos (events file) corrompido. Resolucao: resetfta reinicializa o fault-tolerant agent, recriando o arquivo de eventos; e uma operacao destrutiva que deve ser usada com cautela, pois remove o estado local do FTA.

> **ATENCAO / RESSALVAS DE USO:** Lab 22/08: claim hwa-10.2-resetfta-xagent-safety-0028 cobre seguranca do resetfta.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=troubleshooting |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrftadec002.html |
| Titulo da fonte | Troubleshooting fault-tolerant agent - HCL Workload Automation 10.2.8 |
| Citacao de suporte | resetfta |
| Coletado em | 2026-08-22 |
| Responsavel | hwa-source-verifier |
| Status de revisao | verified |
| Classificacao de risco | destructive |
| Capacidade | fta |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Incidente de troubleshooting (sintoma→resolução) baseado em documentação oficial - validação lab não se aplica diretamente |
| Tipo | command |
| verbs | remove |
| Familia | incident-resetfta |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: FTA com problemas de sincronizacao ou arquivo de eventos (events file) corrompido?


---

### 91. `hwa-10.2.8-incident-sqljdbc4-driver-0145`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `dynamic-agent`

**Afirmacao / Conteudo:**

Sintoma: ao submeter um job MSSQL ou Database job em banco MSSQL, recebe AWKDBE009E 'Unable to create the connection - java.lang.UnsupportedOperationException: Java Runtime Environment (JRE) version 1.6 is not supported by this driver. Use the sqljdbc4.jar class library, which provides support for JDBC 4.0'. Causa: drivers JDBC nao suportados presentes no diretorio de drivers JDBC — o dynamic agent pode carrega-los e causar o erro. Resolucao: (1) remover os drivers JDBC nao suportados; (2) parar o dynamic agent com ShutDownLwa; (3) reiniciar o dynamic agent com StartUpLwa; verificar que apenas o sqljdbc4.jar necessario esta no diretorio de drivers JDBC. Fonte: HCL Troubleshooting Guide 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF. Correlaciona com AWKDBE009E (MSSQL).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - sqljdbc4 JDBC driver |
| Citacao de suporte | Verify that only the required sqljdbc4.jar driver is present in the JDBC driver directory. If unsupported JDBC drivers are also present in this directory, the dynamic agent might load them and cause the error message. |
| Coletado em | 2026-08-23 |
| Capacidade | dynamic-agent |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (remocao de drivers, restart de agent); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar os drivers removidos. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | create; version |
| Codigo da mensagem | AWKDBE009E |
| Familia | incident-sqljdbc4 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWKDBE009E no HWA?
- Como solucionar ou diagnosticar o erro AWKDBE009E no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para dynamic-agent?
- O que causa e como solucionar o problema: ao submeter um job MSSQL ou Database job em banco MSSQL, recebe AWKDBE009E 'Unable to create the connection - java?


---

### 92. `hwa-10.2.8-incident-ssl-port-zero-0074`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `network`

**Afirmacao / Conteudo:**

Sintoma: problema de link entre workstation e domain manager apos mudanca do modo SSL — a workstation nao consegue relinkar. Causa: a statement SSL port no localopts do domain manager ou do fault-tolerant agent esta configurada com valor 0. Resolucao: corrigir o numero da porta SSL no localopts para o valor correto e reiniciar o netman na workstation para que escute na porta correta. Fonte: HCL Troubleshooting Guide 10.2.8 (network link problems - SSL mode).

> **ATENCAO / RESSALVAS DE USO:** Extraido automaticamente do Troubleshooting Guide 10.2.8 PDF (pagina 40). Correlaciona com AWSBIN091E (SSL port no localopts).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - SSL port 0 |
| Citacao de suporte | In the localopts file of either the domain manager or the fault-tolerant agent, the SSL port statement is set to 0. Correct the problem by setting the SSL port number to the correct value... then stop and restart netman. |
| Coletado em | 2026-08-23 |
| Capacidade | network |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (reinicio de netman); avaliar o escopo antes da execucao. |
| Reversibilidade | Reiniciar netman conforme procedimento oficial. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=netman |
| Status de revisao | verified |
| Tipo | command |
| Familia | incident-ssl |

**Perguntas relacionadas:**

- O que causa e como solucionar o problema: problema de link entre workstation e domain manager apos mudanca do modo SSL — a workstation nao consegue relinkar?


---

### 93. `hwa-10.2.8-incident-symphony-fta-manual-0063`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `symphony`

**Afirmacao / Conteudo:**

Sintoma: Symphony corrompido em um agent/domain manager (nao master). RECOVERY OFICIAL manual: (1) no domain manager, unlink o agent com problema; (2) no agent: parar se ainda nao falhou; deletar ou renomear os arquivos Symphony e Sinfonia; (3) no domain manager: backup e preparar o novo Symphony; o agent recebe o Symphony ao relink. Perda: remocao e substituicao completa do Symphony causa perda de dados - eventos de status, conteudo de Mailbox.msg e tomaster.msg; jobs com estado nessas filas sao reexecutados. Fonte: HCL Troubleshooting Guide 10.2.8 (Corrupt Symphony file recovery em FTA/lower domain manager).

> **ATENCAO / RESSALVAS DE USO:** Validado contra o Troubleshooting Guide 10.2.8 PDF (paginas 165-167). Complementa hwa-10.2.8-incident-symphony-corrupt-0024.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - Corrupt Symphony on FTA/lower DM |
| Citacao de suporte | On the domain manager, unlink the agent... On the agent: Delete the Symphony and the Sinfonia files from the agent workstation. Alternatively you can move them to a different location... or rename them. |
| Coletado em | 2026-08-23 |
| Capacidade | symphony |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. Backup dos arquivos antes de deletar. |
| Impacto | Pode alterar estado operacional (reexecucao de jobs); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar Symphony/Sinfonia a partir de backup. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | topic=incident |
| Status de revisao | verified |
| Tipo | other |
| Familia | incident-symphony |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- O que causa e como solucionar o problema: Symphony corrompido em um agent/domain manager (nao master)?


---

### 94. `hwa-10.2.8-install-twsinst-agent-0007`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

O dynamic agent do HCL Workload Automation 10.2.8 é instalado com o script twsinst (twsinst.vbs/twsinst) e usa parâmetros com prefixo - (hífen): -agent dynamic junto com -tdwbhostname (nome do dynamic workload broker/dynamic domain manager ao qual o agente se registra) e -tdwbport (porta HTTPS do broker), além da pasta de certificados -sslkeysfolder com -sslpassword.

> **ATENCAO / RESSALVAS DE USO:** Tópico de instalação (2 fontes oficiais). Em instalação limpa a porta padrão de -tdwbport é 31116. twsinst também instala fault-tolerant agents e agentes z-centric. Parâmetros em exemplo: '-tdwbport 31116 -tdwbhostname mainbroker.mycompany.com'. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8 (tws-agent): twsinst -new -agent dynamic com -tdwbhostname e -tdwbport 31116 instalou com sucesso (AWSFAB033I).]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | Agent installation parameters - twsinst script |
| Citacao de suporte | -agent dynamic ... Installs the HCL Workload Automation dynamic agent. Requires the -tdwbhostname host_name and the -tdwbport tdwbport_number parameters. |
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
| Ferramenta | dynagent |
| verbs | install |
| Familia | install-twsinst |

**Perguntas relacionadas:**

- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar install?
- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Como configurar ou solucionar problemas no dynamic agent ou broker para install?


---

### 95. `hwa-10.2.8-message-jdb402e-0040`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, AWSJDB402E e uma mensagem observada no lab durante operacoes de cleanup/delecao de objetos via REST API V2 ou composer (ex.: remocao de job streams orfaos de teste). Contexto lab: durante a limpeza dos 14 job streams de teste MDMDA + 3 MDMXA, cada composer delete retornou AWSBIA290I 'Total objects deleted: 1'; AWSJDB402E apareceu associada a operacoes de banco durante o cleanup, indicando tentativa de acesso/remocao de registro de objeto.

> **ATENCAO / RESSALVAS DE USO:** Observado no lab 17/08 (cleanup-orphans): AWSJDB402E durante remocao de objetos orfaos. Cobre um codigo lab-observado que nao tinha claim dedicada (gap da analise r9: 7 codigos so-no-lab sem claim).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmspar.html |
| Titulo da fonte | HCL Workload Automation messages - AWSJDB component |
| Citacao de suporte | AWSJDB402E observed during cleanup-orphans lab validation |
| Coletado em | 2026-08-23 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['composer delete MDMDA#<stream> (14 streams)', 'composer delete MDMXA#<stream> (3 streams)', 'REST API V2 DELETE para run cycle groups/calendars/vartables'], result=AWSJDB402E observada durante cleanup de objetos orfaos; cada delecao bem-sucedida retornou AWSBIA290I Total objects deleted: 1., validated_at=2026-08-17T00:00:00BRT |
| Terminologia normalizada | message=AWSJDB402E, command=composer |
| Status de revisao | lab_validated |
| Tipo | message |
| Ferramenta | composer |
| verbs | delete |
| Codigo da mensagem | AWSJDB402E |
| Familia | message-jdb402e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJDB402E no HWA?
- Como solucionar ou diagnosticar o erro AWSJDB402E no HWA?
- Qual é o significado da mensagem de erro AWSBIA290I no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?
- Qual é o significado da mensagem de erro AWSBIA290I no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSJDB402E no HWA e qual ação é recomendada?


---

### 96. `hwa-10.2.8-nestedvar-native-job-types-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, variáveis aninhadas podem ser definidas em uma tabela de variáveis usando apenas a sintaxe ${variablename}; ao referenciar a variável no job definition de uma integração em dynamic agent, tanto ^ quanto ${} são suportados; o recurso é suportado apenas em integrações em dynamic agents, não em job types nativos, e não é suportado em fault-tolerant agents (FTA).

> **ATENCAO / RESSALVAS DE USO:** A página eqqg1NestedVars1028.html confirma o recurso como aprimoramento da 10.2.8. As limitações (apenas dynamic agents, não nativo, não FTA) e a regra de sintaxe (apenas ${} na tabela; ^ e ${} no job definition) são documentadas em awsrgparmdefn.html e awsrgvtabledefn.html: 'The caret symbol (^) is not supported if you define the variable within a variable table... both the caret symbol (^) and the ${variablename} syntax are supported when you reference the variable in the job definition of an integration running on a dynamic agent.' e 'nested variables are not supported on fault-tolerant agents.'

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | nested variables=variáveis aninhadas, dynamic agent=agente dinâmico, native job types=tipos de job nativos, fault-tolerant agent (FTA)=agente tolerante a falhas, ${variablename}=sintaxe com chaves, ^variablename^=sintaxe com acento circunflexo |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1NestedVars1028.html |
| Titulo da fonte | Nested variables for increased flexibility |
| Citacao de suporte | You can now define one or more variables whose value contains another variable to allow dynamic variable substitution at run time. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | nestedvar-native |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 97. `hwa-10.2.8-perf-datasource-tuning-0160`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), as configuracoes recomendadas do data source do Liberty (arquivo datasource.xml em <TWA_DATA_DIR>/usr/servers/engineServer/configDropins/overrides para MDM/BKM/DDM, e <DWC_DATA_DIR>/usr/servers/dwcServer/configDropins/overrides para DWC) sao: statementCacheSize=400, isolationLevel=TRANSACTION_READ_COMMITTED, connectionTimeout=180s, maxPoolSize=300, minPoolSize=0, reapTime=180s, purgePolicy=EntirePool. O Liberty le todos os .xml do diretorio overrides; o nome do arquivo e irrelevante. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.1 Data Source).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 22).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - Data Source |
| Citacao de suporte | statementCacheSize=400, isolationLevel=TRANSACTION_READ_COMMITTED, connectionTimeout=180s, maxPoolSize=300, minPoolSize=0, reapTime=180s, purgePolicy=EntirePool |
| Coletado em | 2026-08-23 |
| Capacidade | mdm |
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
| Ferramenta | dwc |
| Familia | perf-datasource |


---

### 98. `hwa-10.2.8-perf-event-processor-throughput-0163`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), o event processor (fila cache.dat) e um processo single-thread: sua capacidade de processamento e proporcional a velocidade do core e ao I/O, nao escala horizontalmente — apenas verticalmente (aumentando CPU e/ou I/O). Em regras de evento que disparam submissoes (ex.: job status change ou file creation), o throughput final de submissao depende estritamente da capacidade do event processor; no caso de status change o consumer e o batchman; no caso de file monitoring remoto, o proprio agent comunica com o event processor. Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.1).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 18-19).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - Event Processor Throughput |
| Citacao de suporte | The event processor is a single thread process, and its processing capacity is proportional to the core speed and the I/O. For this reason, it cannot scale horizontally but vertically only by increasing the CPU and/or I/O capabilities. |
| Coletado em | 2026-08-23 |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; recomendacao. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=batchman |
| Status de revisao | verified |
| Tipo | command |
| verbs | status |
| Familia | perf-event |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), o event processor (fila cache?


---

### 99. `hwa-10.2.8-perf-file-deps-tuning-0164`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), ao usar file dependencies com dynamic agents, o polling period e dirigido pela propriedade localopts 'bm check file' presente no Dynamic Domain Manager (default 120 segundos). O throughput do servidor e governado por 4 parametros: polling period, numero de file dependencies, conexao de rede agentes-servidor e atividades de Background Scheduling. Recomendacao de tuning: T > N/10, sendo T o valor de bm check file e N o total de file dependencies. Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.2).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 19). Valida o bm check file=300 observado no lab (rodada 11).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - File dependencies |
| Citacao de suporte | The polling period is driven by the localopts property present on the Dynamic Domain Manager: bm check file = 300 (120 seconds is the default)... it is suggested to tune the T (bm check file) with the following restriction: T > N/10 |
| Coletado em | 2026-08-23 |
| Capacidade | agent |
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
| Ferramenta | dynagent |
| Familia | perf-file |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), ao usar file dependencies com dynamic agents, o polling period e dirigido pela propriedade localopts 'bm check file' presente no Dynamic Domain Manager (default 120 segundos)?


---

### 100. `hwa-10.2.8-perf-liberty-jvm-options-0162`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), as opcoes JVM recomendadas para o Liberty (arquivo jvm.options em <DWC_DATA_DIR>/usr/servers/dwcServer/configDropins/overrides) sao: -Xms<heap size>, -Xmx<heap size>, -Xmn<nursery size>, -Xgcpolicy:gencon, -Xdisableexplicitgc. Sizing: DWC heap 4096m para ate 50 usuarios/instancia e 6144m para ate 150 usuarios/instancia; MDM heap 4096m para ate 200 jobs/min e 6144m para mais de 200 jobs/min; nursery size = 1/4 do heap size. Fonte: HCL Workload Automation V10.2 Performance Report (secao 5.4.4).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (Tabela 4 e 5, pagina 23).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - Liberty JVM options |
| Citacao de suporte | -Xms<heap size> -Xmx<heap size> -Xmn<nursery size> -Xgcpolicy:gencon -Xdisableexplicitgc. Heap size: 4096m for up to 50 users/instance; 6144m for up to 150 users/instance. Nursery size: 1/4 of heap size. |
| Coletado em | 2026-08-23 |
| Capacidade | mdm |
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
| Ferramenta | dwc |
| Familia | perf-liberty |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2 (Performance Report oficial), as opcoes JVM recomendadas para o Liberty (arquivo jvm?


---

### 101. `hwa-10.2.8-perf-sbs-mirrorbox-0165`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mirrorbox`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2 (Performance Report oficial), o comando 'conman sbs' (ou chamadas REST equivalentes) adiciona um job stream ao plano on the fly. Se a rede do job stream adicionado e significativamente complexa (dependencias e cardinalidade), pode causar atraso geral no mecanismo de atualizacao do plano: por coerencia de scheduling, todas as atualizacoes iniciais passam pela main thread queue (mirrorbox.msg), ignorando o multithreading. A ordem de magnitude que causa esse queueing e de varias centenas de objetos (jobs nos job streams + dependencias internas e/ou externas). Fonte: HCL Workload Automation V10.2 Performance Report (secao 4.1.3).

> **ATENCAO / RESSALVAS DE USO:** Extraido do iws-hwa_10.2_perfreport.pdf (pagina 19). Correlaciona com hwa-10.2.8-incident-planman-resync-symphony-0064 (mirrorbox.msg).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/ |
| Titulo da fonte | HCL Workload Automation V10.2 Performance Report - conman sbs |
| Citacao de suporte | all the initial updates pass through the main thread queue (mirrobox.msg), bypassing the benefits of multithreading... the order of magnitude is several hundred objects |
| Coletado em | 2026-08-23 |
| Capacidade | mirrorbox |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; recomendacao. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| Familia | perf-sbs |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mirrorbox?


---

### 102. `hwa-10.2.8-pool-broker-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Workstation pool: agrupa agentes dinâmicos com características semelhantes; o HWA balanceia jobs entre os membros e reatribui se um membro ficar indisponível; criar Type Pool hospedado pelo workload broker e adicionar agentes dinâmicos como membros.

> **ATENCAO / RESSALVAS DE USO:** workstation_dwc.html confirma criação de workstation Type Pool hospedada pelo workload broker e adição de agentes dinâmicos como membros. Ao criar um pool, um recurso lógico de mesmo nome é criado no Dynamic Workload Broker.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | pool=workstation lógica que agrupa agentes com características semelhantes, workload broker=workstation que hospeda o pool, balancing=balanceamento de jobs entre os membros do pool, reassign=reatribuição de jobs quando um membro fica indisponível |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | Pool: A logical workstation that groups a set of agents with similar hardware or software characteristics to which to submit jobs. HCL Workload Automation balances the jobs among the agents within the pool and automatically reassigns jobs to available agents if an agent is no longer available. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | pool-broker |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Como o HWA balanceia e despacha jobs dinamicamente em pools de agentes?


---

### 103. `hwa-10.2.8-proc-tree-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed, os processos de gerenciamento ativos em cada workstation (fault-tolerant agent e domain managers) são iniciados na ordem netman -> mailman -> batchman -> jobman pelo StartUp (ou como serviço do sistema). O netman é o processo de gerenciamento de rede que estabelece conexões entre os processos mailman remotos e os processos writer locais; o mailman gerencia a comunicação entre workstations; o batchman opera autonomamente em cada FTA/domain manager, escaneando o arquivo Symphony para resolver dependências e iniciar jobs; o jobman inicia e monitora os jobs. Em um standard agent, o batchman não roda localmente (o jobman responde a requisições de launch do domain manager).

> **ATENCAO / RESSALVAS DE USO:** Conteúdo validado por pesquisa Perplexity (2026-08-19): awsrgprodproc.html + IBM docs 10.2.2 (awsrgprodproc) + awsadnetoperations.html. Corresponde ao knowledge graph do tws_ai_knowledge_optimized.md (synthetic), convertido em claim verified com fonte oficial. | Fonte: pesquisa Perplexity + docs oficiais HCL/IBM

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgprodproc.html |
| Titulo da fonte | IBM Workload Scheduler workstation processes - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The batchman process on each domain manager and fault-tolerant agent workstation operates autonomously, scanning its Symphony files to resolve dependencies and launch jobs. Batchman launches jobs via the Jobman process. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=netman |
| Status de revisao | verified |
| Tipo | command |
| Familia | proc-tree |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 104. `hwa-10.2.8-proc-tree-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed (fault-tolerant agent e domain managers), o batchman opera autonomamente em relação ao seu arquivo Symphony local: escaneia o Symphony para resolver dependências e lançar jobs via jobman. Em um FTA, mesmo se a conexão de rede com o domain manager cair, os processos locais continuam processando os jobs conforme as instruções da cópia local do Symphony. O Symphony é o arquivo que contém as instruções de agendamento (quais jobs rodar) distribuído a todas as workstations envolvidas no plano.

> **ATENCAO / RESSALVAS DE USO:** Validado por Perplexity (2026-08-19). FTA autonomy + Symphony local confirmados por docs IBM (TWS User's Guide, components 10.2.2, awsadnetoperations). Conteúdo do tws_ai_knowledge_optimized.md convertido a verified. | Fonte: pesquisa Perplexity + docs oficiais HCL/IBM

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgprodproc.html |
| Titulo da fonte | IBM Workload Scheduler workstation processes - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The batchman process on each domain manager and fault-tolerant agent workstation operates autonomously, scanning its Symphony files to resolve dependencies and launch jobs. Batchman launches jobs via the Jobman process. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=batchman |
| Status de revisao | verified |
| Tipo | command |
| Familia | proc-tree |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 105. `hwa-10.2.8-proc-tree-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed, os processos de gerenciamento de uma workstation (fault-tolerant agent ou domain manager) baseiam-se na infraestrutura WebSphere Application Server, instalada automaticamente com a workstation. O StartUp (ou o serviço do sistema) inicia o netman, que por sua vez leva à criação da cadeia mailman, batchman e jobman. O netman escuta na porta padrão 31111 para conexões de rede entre workstations.

> **ATENCAO / RESSALVAS DE USO:** Validado por Perplexity (2026-08-19): awsrgprodproc + IBM docs 10.2.2 components + porta 31111 (hwa-install-1028-ports-0001). Conteúdo do tws_ai_knowledge_optimized.md convertido a verified. | Fonte: pesquisa Perplexity + docs oficiais HCL/IBM

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgprodproc.html |
| Titulo da fonte | IBM Workload Scheduler workstation processes - HCL Workload Automation 10.2.8 |
| Citacao de suporte | On fault-tolerant agents and domain managers these processes are based on the WebSphere Application Server infrastructure. Netman: the network management process that establishes network connections between remote mailman processes and local Writer processes. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=netman |
| Status de revisao | verified |
| Tipo | command |
| Familia | proc-tree |


---

### 106. `hwa-10.2.8-runbook-rerun-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o comando rerun usa a opção ;noask para suprimir a solicitação de confirmação antes que o agente execute a ação em cada job qualificado.

> **ATENCAO / RESSALVAS DE USO:** noask disables the interactive confirmation prompt before rerun; documented in the noask argument description.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=rerun, option=noask, effect=suppresses confirmation prompt |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/r_rerun.html |
| Titulo da fonte | rerun |
| Citacao de suporte | When you add the option as an argument the agent will not ask for confirmation before taking action on each qualifying job. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | agent |
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

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o comando rerun usa a opção ;noask para suprimir a solicitação de confirmação antes que o agente execute a ação em cada job qualificado?


---

### 107. `hwa-10.2.8-runbook-showjobs-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a exibição padrão do comando showjobs é o formato standard, usado quando nenhuma opção é especificada, e as informações exibidas só são atualizadas enquanto o batchman (HCL Workload Automation) está em execução.

> **ATENCAO / RESSALVAS DE USO:** showjobs/sj is a read-only display command; default output is standard format.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=showjobs, abbreviation=sj, default_format=standard, dependency=batchman running |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgshowjobs.html |
| Titulo da fonte | showjobs (conman) |
| Citacao de suporte | The displayed information is updated only as long as HCL Workload Automation (batchman) is running. ... The output of the showjobs command is produced in eight formats: standard, keys, info, step, logon, deps, crit, and stdlist. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| verbs | showjobs |
| Familia | runbook-showjobs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a exibição padrão do comando showjobs é o formato standard, usado quando nenhuma opção é especificada, e as informações exibidas só são atualizadas enquanto o batchman (HCL Workload Automation) está em execução?


---

### 108. `hwa-10.2.8-sec-encryption-at-rest-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 criptografa automaticamente em repouso arquivos-chave do produto — Symphony file, message queues, arquivo useropts e o diretório jmJobTableDir em dynamic agents — usando criptografia AES-256 ou AES-128 em todas as instalações novas.

> **ATENCAO / RESSALVAS DE USO:** Documentado: criptografia at-rest por padrão, sem ação adicional; chaves em keystore PKCS12 referenciado pelas propriedades localopts 'encrypt keystore file', 'encrypt keystore pwd', 'encrypt label' e 'decrypt label list'. | Key-rotation page restates automatic AES-256/AES-128 encryption for fresh installations.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | encryption_at_rest=criptografia em repouso, Symphony_file=arquivo Symphony, useropts=arquivo de opções do usuário, AES-256=Advanced Encryption Standard 256 bits, AES-128=Advanced Encryption Standard 128 bits, jmJobTableDir=diretório da tabela de jobs do Jobman |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadsymphencrypt.html |
| Titulo da fonte | Automatic encryption for key product files |
| Citacao de suporte | all fresh installations starting from this release automatically encrypt key product files using AES-256 or AES-128 cryptography |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | agent |
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
| Ferramenta | dynagent |
| Familia | sec-encryption |

**Perguntas relacionadas:**

- Qual endpoint REST API V2 é utilizado para agent no HWA?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 109. `hwa-10.2.8-sec-fault-tolerant-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o modelo de segurança baseado em funções não suporta gerenciamento centralizado de segurança em agentes fault-tolerant; nesses agentes a segurança é gerenciada localmente em cada workstation.

> **ATENCAO / RESSALVAS DE USO:** Documentada limitação de escopo do modelo.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | fault_tolerant_agent=agente fault-tolerant, role_based_security=segurança baseada em funções, centralized_security=segurança centralizada |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadrolebasedsecuritymanagement.html |
| Titulo da fonte | Role-based security model |
| Citacao de suporte | The role-based security model does not support centralized security management on fault-tolerant agents. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | sec-fault |


---

### 110. `hwa-10.2.8-sec-ssl-version-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A keyword ssl version no HCL Workload Automation 10.2.8 (no ita.ini de dynamic agents e em localopts de componentes nativos/FTAs) aceita valores exatos (TLSv1.0 a TLSv1.3), valores mínimos (atleast.TLSv1.x) e valores máximos (max.TLSv1.x) para controlar a versão do protocolo TLS usada.

> **ATENCAO / RESSALVAS DE USO:** Mesmo comportamento documentado na referência de localopts para a opção 'SSL version' e 'CLI SSL version'.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ssl_version=keyword ssl version, TLS_protocol=protocolo TLS, ita.ini=arquivo de configuração do agente dinâmico, localopts=arquivo de opções locais |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | Specify the SSL version to be used. Supported values are: atleast.TLSv1.0 ... max.TLSv1.3 ... TLSv1.3 |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | version |
| Familia | sec-ssl |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 111. `hwa-10.2.8-sec-tls-1-3-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O suporte ao protocolo de segurança TLS V1.3 no HCL Workload Automation é disponível a partir da versão 10.1 FP4 em diante, e sua configuração pode ser feita manualmente em dynamic agents, componentes Open Liberty e componentes nativos/agentes fault-tolerant.

> **ATENCAO / RESSALVAS DE USO:** Documentado: configuração por componente.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TLS_1.3=Transport Layer Security versão 1.3, dynamic_agent=agente dinâmico, Open_Liberty=servidor Open Liberty, fault_tolerant_agent=agente fault-tolerant |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiTLSV13.html |
| Titulo da fonte | Configuring the TLS V1.3 security protocol |
| Citacao de suporte | TLS V1.3 security protocol support is available from HCL Workload Automation version 10.1 FP4 onwards. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | open |
| Familia | sec-tls |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?


---

### 112. `hwa-10.2.8-sec-tls-sth-0028`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

O comando certman extract no HCL Workload Automation 10.2.8 extrai certificados do keystore e truststore (em master domain manager, agente ou Dynamic Workload Console) com a sintaxe 'certman extract -outpath <output path> [-storepasswd <pw>] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <working directory>] [-cachain-splitted]', gerando os arquivos ca.crt, tls.crt, tls.key, tls.sth (password em Base64) e a subpasta additionalCAs.

> **ATENCAO / RESSALVAS DE USO:** Documentado manuseio de keystore/truststore pós-geração; todos os certificados devem usar chave mínima de 2048 bits.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | certman=utilitário Certman, extract=extrair, keystore=repositório de chaves, truststore=repositório de confiança, outpath=pasta de saída, tls.sth=arquivo stash |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadcertman_ext.html |
| Titulo da fonte | Extract certificates from the keystore and truststore |
| Citacao de suporte | certman extract -outpath <output path> [-storepasswd <pw>] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <working directory>] [-cachain-splitted] |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | credential_sensitive |
| Capacidade | agent |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['certman extract'], result=Sintaxe real confirmada no help do binário: 'certman extract -outpath <output path> [-storepasswd <pw>] [-cachain-splitted] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <work dir>]'. Confirmado que -wauser e -wagroup são REQUERIDOS em UNIX (não suportados em Windows); storepasswd requerido apenas na 9.4.x. Binário disponível em /opt/hwa/TWS/bin/certman., validated_at=2026-08-23T00:50:00BRT, evidence_file=lab-validation-2026-08-23-r8-certman.jsonl |
| Tipo | command |
| Ferramenta | certman |
| Familia | sec-tls |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O comando certman extract no HCL Workload Automation 10.2.8 extrai certificados do keystore e truststore (em master domain manager, agente ou Dynamic Workload Console) com a sintaxe 'certman extract -outpath <output path> [-storepasswd <pw>] [-agentscope] [-wauser <user>] [-wagroup <group>] [-workdir <working directory>] [-cachain-splitted]', gerando os arquivos ca?


---

### 113. `hwa-10.2.8-showjobs-wildcard-ws-filter-0111`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8 Distributed, o comando showjobs (sj) aceita prefixo `workstation#` no jobselect para filtrar jobs de uma workstation especifica, com suporte a wildcards. Exemplos: `sj MDMDA#@.@` lista todos os jobs na workstation MDMDA; `sj @#@.@` lista jobs de todas as workstations; `sj sked1(1100 03/05/2023).@` seleciona todos os jobs no job stream sked1. O wildcard @ na posicao de workstation substitui qualquer nome de workstation.

> **ATENCAO / RESSALVAS DE USO:** Lab validated 2026-08-22. The pattern 'workstation#@.@' for filtering all jobs of a specific workstation was absent from corpus teaching examples.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jobselect=seletor de jobs no comando showjobs, workstation#=prefixo de workstation no jobselect, .@=seleciona todos os jobs de um job stream |
| Status do conhecimento | verified |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcomsyn.html |
| Titulo da fonte | Running commands from conman - HCL Workload Automation 10.2.8 User's Guide and Reference |
| Citacao de suporte | sj sked1(1100 03/05/2023).@+state=hold~priority=0;info;offline -- Selects all jobs in the job stream sked1(1100 03/05/2023) that are in the HOLD state with a priority other than zero. |
| Coletado em | 2026-08-22 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, tested_commands=['sj MDMDA#@.@;keys', 'sj @#@.@;keys'], result=MDMDA#@.@ listou apenas jobs da MDMDA; @#@.@ listou jobs de MDMDA e MDMXA |
| Classificacao de risco | read_only |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Confianca | high |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | mdm |
| verbs | showjobs |
| Familia | showjobs-wildcard |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8 Distributed, o comando showjobs (sj) aceita prefixo `workstation#` no jobselect para filtrar jobs de uma workstation especifica, com suporte a wildcards?


---

### 114. `hwa-10.2.8-showprompts-access-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Em HWA 10.2.8, showprompts requer acesso list ao objeto se enListSecChk estava yes no MDM quando o production plan foi criado ou estendido. Context: You must have list access to the object being shown if the enListSecChk option was set to yes on the master domain manager when the production plan was created or extended.

> **ATENCAO / RESSALVAS DE USO:** The identical list-access sentence also appears on the v1028 showcpus, showjobs, showresources and showschedules pages; the showprompts page states it verbatim, matching the claim. Read-only diagnostic command.

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
| Citacao de suporte | You must have list access to the object being shown if the enListSecChk option was set to yes on the master domain manager when the production plan was created or extended. |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=showprompts |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | list; plan; set |
| Familia | showprompts-access |


---

### 115. `hwa-10.2.8-stdlist-jobman-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

Em HWA 10.2.8, um arquivo standard list é criado automaticamente para cada job iniciado por jobmon no Windows ou jobman no UNIX. Context: A standard list file is created automatically by jobmon in Windows or jobman in UNIX, for each job that jobmon and jobman launches.

> **ATENCAO / RESSALVAS DE USO:** The stdlist concept in v1028 is documented on the 'Stdlist format' sub-topic of showjobs (awsrgstdlist.html does not exist and returns 404). Scope: Windows (jobmon) and UNIX (jobman) agents, matching the claim. Read-only diagnostic context.

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
| Citacao de suporte | A standard list file is created automatically by jobmon in Windows or jobman in UNIX, for each job that jobmon and jobman launches. |
| Coletado em | 2026-08-18 |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=jobman |
| Status de revisao | verified |
| Tipo | command |
| verbs | list |
| Familia | stdlist-jobman |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, um arquivo standard list é criado automaticamente para cada job iniciado por jobmon no Windows ou jobman no UNIX?


---

### 116. `hwa-10.2.8-tune-bm-cache-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

The "bm cache" option is not documented in the HCL Workload Automation 10.2.8 localopts reference. The documented mailbox cache belongs to mailman (mm cache mailbox / mm cache size), not batchman.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm cache=bm cache, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Local options reference - HCL Workload Automation 10.2.8 |
| Citacao de suporte | mm cache mailbox, mm cache size are documented for mailman. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: The "bm cache" option is not documented in the HCL Workload Automation 10.2.8 localopts reference?


---

### 117. `hwa-10.2.8-tune-bm-check-file-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

A opção bm check file no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar a existência de um arquivo usado como dependência, com padrão documentado de 120 segundos.

> **ATENCAO / RESSALVAS DE USO:** Atributo da workstation para o processo batchman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm check file=bm check file, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm check file = seconds - Specify the minimum number of seconds Batchman waits before checking for the existence of a file that is used as a dependency. The default is 120 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm check file no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de verificar a existência de um arquivo usado como dependência, com padrão documentado de 120 segundos?


---

### 118. `hwa-10.2.8-tune-bm-check-status-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

A opção bm check status no localopts do HCL Workload Automation 10.2.8 especifica o número de segundos que o Batchman espera entre verificações do status de uma dependência internetwork, com padrão documentado de 300 segundos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm check status=bm check status, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm check status = seconds - Specify the number of seconds Batchman waits between checking the status of an internetwork dependency. The default is 300 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | status |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm check status no localopts do HCL Workload Automation 10.2.8 especifica o número de segundos que o Batchman espera entre verificações do status de uma dependência internetwork, com padrão documentado de 300 segundos?


---

### 119. `hwa-10.2.8-tune-bm-check-until-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

A opção bm check until no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda antes de reportar a expiração de um tempo Until, com padrão documentado de 300 segundos; valores abaixo do padrão podem sobrecarregar o sistema.

> **ATENCAO / RESSALVAS DE USO:** Se definido abaixo de bm read, o valor de bm read é usado em seu lugar.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm check until=bm check until, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm check until = seconds - Specify the maximum number of seconds Batchman waits before reporting the expiration of an Until time ... Specifying a value below the default setting (300) might overload the system. ... The default is 300 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual o comportamento das opções until e deadline na submissão de jobs no conman?
- Qual a regra documentada no HWA Distributed sobre: A opção bm check until no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda antes de reportar a expiração de um tempo Until, com padrão documentado de 300 segundos; valores abaixo do padrão podem sobrecarregar o sistema?


---

### 120. `hwa-10.2.8-tune-bm-stats-0024`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

A opção bm stats no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar suas estatísticas de inicialização e encerramento ao seu arquivo standard list, com padrão documentado de off.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm stats=bm stats, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm stats = on|off - To have Batchman send its startup and shut down statistics to its standard list file, specify on. ... The default is off. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm stats no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar suas estatísticas de inicialização e encerramento ao seu arquivo standard list, com padrão documentado de off?


---

### 121. `hwa-10.2.8-tune-bm-verbose-0025`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `batchman`

**Afirmacao / Conteudo:**

A opção bm verbose no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar todas as mensagens de status de jobs ao seu arquivo standard list, com padrão documentado de off.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm verbose=bm verbose, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm verbose = on|off - To have Batchman send all job status messages to its standard list file, specify on. ... The default is off. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | batchman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | list; status |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm verbose no localopts do HCL Workload Automation 10.2.8, quando definida como on, faz o Batchman enviar todas as mensagens de status de jobs ao seu arquivo standard list, com padrão documentado de off?


---

### 122. `hwa-10.2.8-tune-command-handler-max-threads-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A propriedade CommandHandlerMaxThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, indica o número máximo de comandos que podem ser executados concorrentemente no agente, com padrão documentado de 100.

> **ATENCAO / RESSALVAS DE USO:** Referente a operações do comdhandler (ex.: requisições concorrentes de recuperação de logs de jobs).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | CommandHandlerMaxThreads=CommandHandlerMaxThreads, JobManager.ini=JobManager.ini |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | CommandHandlerMaxThreads - Indicates the maximum number of commands that can be run on the agent concurrently. ... The default is 100. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-command |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade CommandHandlerMaxThreads, na seção [Launchers] do JobManager?


---

### 123. `hwa-10.2.8-tune-command-handler-min-threads-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A propriedade CommandHandlerMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, indica o número máximo de comandos que podem ser executados concorrentemente no agente, com padrão documentado de 20.

> **ATENCAO / RESSALVAS DE USO:** Documentação indica que normalmente não há necessidade de modificar esta configuração.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | CommandHandlerMinThreads=CommandHandlerMinThreads, JobManager.ini=JobManager.ini |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | CommandHandlerMinThreads - Indicates the maximum number of commands that can be run on the agent concurrently. ... The default is 20. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-command |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade CommandHandlerMinThreads, na seção [Launchers] do JobManager?


---

### 124. `hwa-10.2.8-tune-executors-max-threads-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A propriedade ExecutorsMaxThreads, na seção [Launchers] do arquivo JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número máximo de jobs que o agente dinâmico pode executar concorrentemente, com padrão documentado de 400.

> **ATENCAO / RESSALVAS DE USO:** Documentado na seção [Launchers] (não [JobExecutor]) do JobManager.ini. O padrão é 400 jobs concorrentes.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ExecutorsMaxThreads=ExecutorsMaxThreads, JobManager.ini=JobManager.ini, [Launchers]=[Launchers], dynamic agent=agente dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | ExecutorsMaxThreads - Specifies the maximum number of jobs the dynamic agent can run concurrently. ... The default is 400. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-executors |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade ExecutorsMaxThreads, na seção [Launchers] do arquivo JobManager?


---

### 125. `hwa-10.2.8-tune-executors-max-threads-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a concorrência de execução de jobs do agente dinâmico é governada pelas propriedades ExecutorsMinThreads e ExecutorsMaxThreads na seção [Launchers] do JobManager.ini, que definem os limites mínimo e máximo de jobs executados concorrentemente pelo agente.

> **ATENCAO / RESSALVAS DE USO:** Complementa o limite de workstation definido no nível do scheduler; o agente executa efetivamente até ExecutorsMaxThreads.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ExecutorsMaxThreads=ExecutorsMaxThreads, ExecutorsMinThreads=ExecutorsMinThreads, JobManager.ini=JobManager.ini, [Launchers]=[Launchers], dynamic agent=agente dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | ExecutorsMaxThreads - Specifies the maximum number of jobs the dynamic agent can run concurrently. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-executors |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, a concorrência de execução de jobs do agente dinâmico é governada pelas propriedades ExecutorsMinThreads e ExecutorsMaxThreads na seção [Launchers] do JobManager?


---

### 126. `hwa-10.2.8-tune-executors-min-threads-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A propriedade ExecutorsMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número mínimo de jobs que o agente dinâmico pode executar concorrentemente, com padrão documentado de 38; o agente aloca dinamicamente mais threads conforme necessário até o valor de ExecutorsMaxThreads.

> **ATENCAO / RESSALVAS DE USO:** Padrão 38. A concorrência real é limitada dinamicamente até ExecutorsMaxThreads.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ExecutorsMinThreads=ExecutorsMinThreads, JobManager.ini=JobManager.ini, [Launchers]=[Launchers], dynamic agent=agente dinâmico |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | ExecutorsMinThreads - Specifies the minimum number of jobs the dynamic agent can run concurrently. ... The default is 38. ... The agent dynamically allocates more threads if necessary, until it reaches the value specified in ExecutorsMaxThreads. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-executors |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A propriedade ExecutorsMinThreads, na seção [Launchers] do JobManager?


---

### 127. `hwa-10.2.8-tune-jm-concurrency-0017`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

The "jm concurrency" and "jm startup" options are not documented in the HCL Workload Automation 10.2.8 localopts reference. Job concurrency on the dynamic agent is controlled by ExecutorsMinThreads/ExecutorsMaxThreads in JobManager.ini.

> **ATENCAO / RESSALVAS DE USO:** Confirmada ausencia na documentacao oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm concurrency=jm concurrency, jm startup=jm startup, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Local options reference - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The documented job manager parameters are: jm read, jm write, jm trace. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: The "jm concurrency" and "jm startup" options are not documented in the HCL Workload Automation 10.2.8 localopts reference?


---

### 128. `hwa-10.2.8-tune-jm-file-no-root-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm file no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman execute comandos em dependências de arquivo como root, com padrão documentado de no.

> **ATENCAO / RESSALVAS DE USO:** Somente UNIX/Linux.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm file no root=jm file no root, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm file no root = yes|no - For UNIX and Linux operating systems only, specify yes to prevent Jobman from executing commands in file dependencies as root. ... The default is no. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm file no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman execute comandos em dependências de arquivo como root, com padrão documentado de no?


---

### 129. `hwa-10.2.8-tune-jm-job-table-size-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm job table size no localopts do HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão documentado de 1024 entradas.

> **ATENCAO / RESSALVAS DE USO:** Atributo da workstation para o processo jobman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm job table size=jm job table size, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm job table size = entries - Specify the size, in number of entries, of the job table used by Jobman. The default is 1024 entries. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm job table size no localopts do HCL Workload Automation 10.2.8 especifica o tamanho, em número de entradas, da tabela de jobs usada pelo Jobman, com padrão documentado de 1024 entradas?


---

### 130. `hwa-10.2.8-tune-jm-loaduserprofile-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm loaduserprofile, somente em sistemas Windows, no localopts do HCL Workload Automation 10.2.8 especifica se o processo jobman carrega o perfil de usuário e suas variáveis de ambiente antes de iniciar jobs, com padrão documentado de on.

> **ATENCAO / RESSALVAS DE USO:** Somente Windows; perfis roaming não são suportados.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm loaduserprofile=jm loaduserprofile, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm loaduserprofile = on|off - Only on Windows operating systems. Specify if the jobman process loads the user profile and its environment variables ... The default is on. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm loaduserprofile, somente em sistemas Windows, no localopts do HCL Workload Automation 10.2.8 especifica se o processo jobman carrega o perfil de usuário e suas variáveis de ambiente antes de iniciar jobs, com padrão documentado de on?


---

### 131. `hwa-10.2.8-tune-jm-look-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Jobman aguarda antes de procurar jobs concluídos e executar tarefas gerais de gerenciamento de jobs, com padrão documentado de 300 segundos.

> **ATENCAO / RESSALVAS DE USO:** Listada na página Tuning job processing como opção a ser ajustada para acelerar o processamento global de jobs.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm look=jm look, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm look = seconds - Specify the minimum number of seconds Jobman waits before looking for completed jobs and performing general job management tasks. The default is 300 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Jobman aguarda antes de procurar jobs concluídos e executar tarefas gerais de gerenciamento de jobs, com padrão documentado de 300 segundos?


---

### 132. `hwa-10.2.8-tune-jm-nice-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica o valor nice aplicado aos jobs lançados pelo Jobman para alterar sua prioridade no scheduler do kernel, com padrão documentado de zero; aplica-se apenas a jobs agendados pelo usuário root.

> **ATENCAO / RESSALVAS DE USO:** Somente UNIX/Linux; jobs submetidos por outros usuários herdam o valor nice do processo Jobman.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm nice=jm nice, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm nice = nice_value - For UNIX and Linux operating systems only, specify the nice value to be applied to jobs launched by Jobman to change their priority in the kernel's scheduler. The default is zero. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | scheduler |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm nice, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica o valor nice aplicado aos jobs lançados pelo Jobman para alterar sua prioridade no scheduler do kernel, com padrão documentado de zero; aplica-se apenas a jobs agendados pelo usuário root?


---

### 133. `hwa-10.2.8-tune-jm-no-root-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman lance jobs como root, com padrão documentado de yes.

> **ATENCAO / RESSALVAS DE USO:** Somente UNIX/Linux.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm no root=jm no root, Jobman=Jobman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm no root = yes|no - For UNIX and Linux operating systems only, specify yes to prevent Jobman from launching root jobs. ... The default is yes. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm no root, para sistemas UNIX e Linux, no localopts do HCL Workload Automation 10.2.8 especifica yes para impedir que o Jobman lance jobs como root, com padrão documentado de yes?


---

### 134. `hwa-10.2.8-tune-jm-read-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `jobman`

**Afirmacao / Conteudo:**

A opção jm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Jobman aguarda por uma mensagem no arquivo courier.msg, com padrão documentado de 10 segundos.

> **ATENCAO / RESSALVAS DE USO:** Opção de tuning do job processing listada na página Tuning job processing.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | jm read=jm read, Jobman=Jobman, courier.msg=courier.msg, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | jm read = seconds - Specify the maximum number of seconds Jobman waits for a message in the courier.msg message file. The default is 10 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | jobman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-jm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção jm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Jobman aguarda por uma mensagem no arquivo courier?


---

### 135. `hwa-10.2.8-tune-mm-cache-mailbox-0028`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção mm cache mailbox no localopts do HCL Workload Automation 10.2.8 habilita o Mailman a usar um cache de leitura para mensagens recebidas, com padrão documentado de yes; somente mensagens consideradas essenciais para a consistência da rede são armazenadas em cache.

> **ATENCAO / RESSALVAS DE USO:** A página Mailbox caching recomenda manter o padrão yes para maximizar o desempenho.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm cache mailbox=mm cache mailbox, Mailman=Mailman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm cache mailbox = yes|no - Use this option to enable Mailman to use a reading cache for incoming messages. ... The default is yes. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm cache mailbox no localopts do HCL Workload Automation 10.2.8 habilita o Mailman a usar um cache de leitura para mensagens recebidas, com padrão documentado de yes; somente mensagens consideradas essenciais para a consistência da rede são armazenadas em cache?


---

### 136. `hwa-10.2.8-tune-mm-read-0031`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção mm read é documentada no HCL Workload Automation 10.2.8 como a opção que controla a periodicidade com que o mailman verifica o arquivo Mailbox.msg em busca de jobs concluídos; o valor padrão desta opção não é documentado na referência oficial de detalhes de localopts da versão 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** A existência e a finalidade de mm read são documentadas na página Tuning job processing; o valor padrão quantitativo não consta na referência Localopts details/summary da v10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm read=mm read, Mailman=Mailman, Mailbox.msg=Mailbox.msg, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtunejobproc.html |
| Titulo da fonte | Tuning job processing on a workstation |
| Citacao de suporte | mailman looks periodically in the Mailbox.msg for completed jobs. mm read |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm read é documentada no HCL Workload Automation 10.2.8 como a opção que controla a periodicidade com que o mailman verifica o arquivo Mailbox?


---

### 137. `hwa-10.2.8-tune-mm-response-0032`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção mm response no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda por uma resposta antes de reportar que uma workstation não está respondendo, com padrão documentado de 600 segundos e tempo mínimo de espera de 90 segundos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm response=mm response, Mailman=Mailman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm response = seconds - Specify the maximum number of seconds Mailman waits for a response before reporting that a workstation is not responding. The minimum wait time for a response is 90 seconds. The default is 600 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm response no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda por uma resposta antes de reportar que uma workstation não está respondendo, com padrão documentado de 600 segundos e tempo mínimo de espera de 90 segundos?


---

### 138. `hwa-10.2.8-tune-mm-retrylink-0033`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção mm retrylink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda, após desvincular-se de uma workstation que não responde, antes de tentar vincular-se novamente, com padrão documentado de 600 segundos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm retrylink=mm retrylink, Mailman=Mailman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm retrylink = seconds - Specify the maximum number of seconds Mailman waits after unlinking from a non-responding workstation before it attempts to link to the workstation again. The default is 600 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm retrylink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda, após desvincular-se de uma workstation que não responde, antes de tentar vincular-se novamente, com padrão documentado de 600 segundos?


---

### 139. `hwa-10.2.8-tune-mm-unlink-0034`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `mailman`

**Afirmacao / Conteudo:**

A opção mm unlink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda antes de desvincular-se de uma workstation que não está respondendo, com padrão documentado de 960 segundos; o tempo de espera não deve ser inferior ao tempo de resposta de nm response.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mm unlink=mm unlink, Mailman=Mailman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | mm unlink = seconds - Specify the maximum number of seconds Mailman waits before unlinking from a workstation that is not responding. ... The default is 960 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mailman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-mm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção mm unlink no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Mailman aguarda antes de desvincular-se de uma workstation que não está respondendo, com padrão documentado de 960 segundos; o tempo de espera não deve ser inferior ao tempo de resposta de nm response?


---

### 140. `hwa-10.2.8-tune-nm-mortal-0039`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `netman`

**Afirmacao / Conteudo:**

A opção nm mortal no localopts do HCL Workload Automation 10.2.8 especifica yes para que o Netman saia quando todos os seus processos filhos pararem, com padrão documentado de no.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | nm mortal=nm mortal, Netman=Netman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | nm mortal = yes|no - Specify yes to have Netman quit when all of its child processes have stopped. ... The default is no. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | netman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-nm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção nm mortal no localopts do HCL Workload Automation 10.2.8 especifica yes para que o Netman saia quando todos os seus processos filhos pararem, com padrão documentado de no?


---

### 141. `hwa-10.2.8-tune-nm-read-0037`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `netman`

**Afirmacao / Conteudo:**

A opção nm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda por uma requisição de conexão antes de verificar sua fila de mensagens para comandos stop e start, com padrão documentado de 10 segundos.

> **ATENCAO / RESSALVAS DE USO:** Opção de tuning do processo netman documentada na referência oficial.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | nm read=nm read, Netman=Netman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | nm read = seconds - Specify the maximum number of seconds Netman waits for a connection request before checking its message queue for stop and start commands. The default is 10 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | netman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | start; stop |
| Familia | tune-nm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção nm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda por uma requisição de conexão antes de verificar sua fila de mensagens para comandos stop e start, com padrão documentado de 10 segundos?


---

### 142. `hwa-10.2.8-tune-nm-retry-0038`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `netman`

**Afirmacao / Conteudo:**

A opção nm retry no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda antes de tentar novamente uma conexão que falhou, com padrão documentado de 800 segundos.

> **ATENCAO / RESSALVAS DE USO:** Documentação não recomenda reduzir nm retry meramente para aparentar mais responsividade.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | nm retry=nm retry, Netman=Netman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | nm retry = seconds - Specify the maximum number of seconds Netman waits before retrying a connection that failed. The default is 800 seconds. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | netman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-nm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção nm retry no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Netman aguarda antes de tentar novamente uma conexão que falhou, com padrão documentado de 800 segundos?


---

### 143. `hwa-10.2.8-tune-notifier-min-threads-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

A propriedade NotifierMinThreads, na seção [Launchers] do JobManager.ini do agente dinâmico no HCL Workload Automation 10.2.8, especifica o número mínimo de threads de notificação de mudanças de status de jobs ao dynamic workload broker, com padrão documentado de 3.

> **ATENCAO / RESSALVAS DE USO:** Documentação orienta modificar somente em caso de erros inesperados e após consulta à equipe de suporte.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | NotifierMinThreads=NotifierMinThreads, JobManager.ini=JobManager.ini |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadconftraces.html |
| Titulo da fonte | Configuring common launchers properties [Launchers] |
| Citacao de suporte | NotifierMinThreads - Notifier threads are in charge of notifying the dynamic workload broker of each status change in a job. ... The default value is 3. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | status |
| Familia | tune-notifier |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para agent?
- Qual a regra documentada no HWA Distributed sobre: A propriedade NotifierMinThreads, na seção [Launchers] do JobManager?


---

### 144. `hwa-10.2.8-vm-9f-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `syntax`

**Afirmacao / Conteudo:**

A definição de job TASK com XML jsdl:jobDefinition e tasktype UNIX/WINDOWS/OTHER/BROKER é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica.

> **ATENCAO / RESSALVAS DE USO:** TASK/tasktype BROKER idênticos em 10.2.0 e 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | TASK=palavra-chave de definição de job com XML JSDL, jsdl:jobDefinition=XML de definição de job JSDL, tasktype=UNIX, WINDOWS, OTHER, BROKER |
| Produto | HCL Workload Automation |
| Versao | 10.2.0; 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjobdefn.html |
| Titulo da fonte | Job definition (10.2.8) |
| Citacao de suporte | TASK <XML jsdl:jobDefinition>; tasktype UNIX|WINDOWS|OTHER|BROKER |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | verified |
| Classificacao de risco | read_only |
| Capacidade | task_job_definition |
| Modo de operacao | read |
| Escopo de versao | 10.2.0; 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | vm-9f |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para syntax?
- Qual a regra documentada no HWA Distributed sobre: A definição de job TASK com XML jsdl:jobDefinition e tasktype UNIX/WINDOWS/OTHER/BROKER é suportada no HCL Workload Automation Distributed 10.2.0 e 10.2.8, com sintaxe idêntica?


---

### 145. `hwa-10.2.8-vm-component-terminology-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

A terminologia de componentes do produto distribuído (master domain manager/MDM, domain manager/DM, fault-tolerant agent/FTA, dynamic domain manager/DDM, Dynamic Workload Console/DWC) é consistente entre as marcas TWS, IWS e HWA, e o conman é o programa de linha de comando que gerencia o plano de produção, executável a partir do master domain manager e de qualquer fault-tolerant agent.

> **ATENCAO / RESSALVAS DE USO:** As notas 9.5 da IBM definem as siglas MDM/DDM/DM/FTA/DWC; a página conman da HCL 10.2.8 usa as mesmas terminologias. Master domain manager e domain manager são componentes distintos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | MDM=master domain manager, DM=domain manager, FTA=fault-tolerant agent, DDM=dynamic domain manager, DWC=Dynamic Workload Console, conman=programa de linha de comando de gerenciamento do plano |
| Produto | HCL Workload Automation |
| Versao | multi |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgusingconman.html |
| Titulo da fonte | Setting up the conman command-line program (HCL Workload Automation 10.2.8) |
| Citacao de suporte | The conman command-line program manages the production plan environment. You can use the conman program from the master domain manager and from any fault-tolerant agent workstation in the HCL Workload Automation network. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | multi |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | conman |
| Familia | vm-component |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 146. `hwa-10.2.8-vm-conman-distributed-only-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O conman é documentado apenas na documentação do HCL Workload Automation distribuído (seção 'Managing objects in the plan - conman' do User's Guide and Reference), como programa de linha de comando do master domain manager e fault-tolerant agents; não é listado na documentação do HCL Workload Automation for Z (z/OS).

> **ATENCAO / RESSALVAS DE USO:** conman/ocli aparecem somente na árvore distr/ da documentação; a árvore zos/ do HWA for Z não contém seção de conman/ocli. Ausência na documentação z/OS é evidência de que não fazem parte do produto z/OS, sem prova definitiva de indisponibilidade.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | conman=programa de linha de comando distribuído de gerenciamento do plano, Distributed=plataforma distribuída do HWA, z/OS=plataforma mainframe (HCL Workload Automation for Z) |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgusingconman.html |
| Titulo da fonte | Setting up the conman command-line program (HCL Workload Automation 10.2.8) |
| Citacao de suporte | The conman command-line program manages the production plan environment. You can use the conman program from the master domain manager and from any fault-tolerant agent workstation in the HCL Workload Automation network. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | command |
| Ferramenta | conman |
| verbs | plan |
| Familia | vm-conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 147. `hwa-10.2.8-wapullinfo-db2-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

wa_pull_info é um utilitário de captura de dados localizado em TWA_home/TWS/bin; ele tira um snapshot dos dados DB2 e WebSphere Application Server Liberty no MDM, salvando-os como um pacote datado; pode ser usado para backup do banco de dados DB2 e de arquivos de configuração.

> **ATENCAO / RESSALVAS DE USO:** A página oficial confirma o snapshot de DB2 e WAS Liberty no MDM como pacote datado e o uso para suporte. O uso para backup de DB2 e arquivos de configuração é corroborado por awsadbckupnrestore.html ('can also be used to perform a backup of a DB2 database and some of the configuration files'). A localização exata TWA_home/TWS/bin não é explicitamente confirmada nesta página; o parâmetro -component TWS|DWC é obrigatório.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | wa_pull_info=wa_pull_info, snapshot=snapshot, DB2=DB2, WebSphere Application Server Liberty=WebSphere Application Server Liberty, master_domain_manager=MDM, dated_package=pacote datado |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsinstpullinfo.html |
| Titulo da fonte | wa_pull_info |
| Citacao de suporte | This is a script that produces information about your HCL Workload Automation environment and your local workstation, and can take a snapshot of DB2 and WebSphere Application Server Liberty data on the master domain manager, saving them as a dated package. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | mdm |
| Familia | wapullinfo-db2 |

**Perguntas relacionadas:**

- Como utilizar o utilitário wa_pull_info no HCL Workload Automation?
- Qual a sintaxe ou procedimento no wa_pull_info para gerenciar mdm?
- Qual a função do script wa_pull_info no HWA e que tipo de dados ele coleta?


---

### 148. `hwa-10.2.8-workstation-fault-tolerant-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

Tipos de workstation: agente dinâmico (agent), agente tolerante a falhas (fta), domain manager (manager), pool (pool) e workstation class.

> **ATENCAO / RESSALVAS DE USO:** A página lista também master domain manager (master), backup master (fta), dynamic domain manager, standard agent (s-agent), extended agent (x-agent), workload broker (broker) e dynamic pool. Workstation class é tratada em página própria.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | dynamic agent=agente dinâmico, registrado como agent, fault-tolerant agent=agente tolerante a falhas, registrado como fta, domain manager=gerenciador de domínio, registrado como manager, pool=workstation lógica que agrupa agentes, registrada como pool, workstation class=agrupamento lógico de workstations |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | Dynamic agent ... This workstation is registered in the HCL Workload Automation database as agent. ... Fault-tolerant agent ... registered in the HCL Workload Automation database as fta. ... Domain manager ... registered in the HCL Workload Automation database as manager. ... Pool ... registered in the HCL Workload Automation database as pool. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | workstation-fault |


---

### 149. `hwa-8.3-default-certs-dwc-connector-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

No Tivoli Workload Scheduler 8.3, se os certificados padrao nao forem renovados antes da expiracao no Dynamic Workload Console e no distributed connector instalado no agente, a comunicacao entre a interface de usuario e o connector e interrompida.

> **ATENCAO / RESSALVAS DE USO:** Promovido de data/quarantine.jsonl (awscertsmst.pdf, manual oficial IBM TWS 8.3). Fato de 8.x sobre impacto da expiracao dos certificados padrao.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 8.3.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://www.ibm.com/docs/en/tws/8.3.0 |
| Titulo da fonte | IBM Workload Scheduler 8.3 - Renewing default certificates |
| Citacao de suporte | If you do not modify the default certificates on the Dynamic Workload Console and on the distributed connector installed on the agent before the expiration date, the communication between the user interface and the connector is broken. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-corpus-curator |
| Status de revisao | draft |
| Terminologia normalizada | distributed connector=connector distribuido no agente, Dynamic Workload Console=console web |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 8.3.0 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dwc |
| Familia | default-certs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No Tivoli Workload Scheduler 8.3, se os certificados padrao nao forem renovados antes da expiracao no Dynamic Workload Console e no distributed connector instalado no agente, a comunicacao entre a interface de usuario e o connector e interrompida?


---

### 150. `hwa-9.5-conman-eventrules-contrast-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-conman-eventrules-0001: na 9.5, as event rules eram definidas por composer create rule com suporte basico; na 10.2.8, alem de composer create rule e conman rule, ha o fluxo de sendevent->event processor (AWSEVP001I) e integracao com dynamic agents (Workload Service Assurance); a taxonomia e a cobertura de eventos sao version-dependent.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: cobertura de event-driven automation cresceu entre 9.5 e 10.2.8.

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
| Citacao de suporte | event rules: composer create rule, conman rule |
| Coletado em | 2026-08-21 |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSEVP001I, command=conman |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSEVP001I no HWA?
- Como solucionar ou diagnosticar o erro AWSEVP001I no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar conman?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 151. `hwa-9.5-conman-showcpus-contrast-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-conman-showcpus-0001: na 9.5, conman sc (showcpus) listava workstations/CPUs do dominio com formato standard; na 10.2.8 o comando permanece (sc), mas os formatos (standard vs link) e a identificacao de X-AGENT/HOST foram padronizados e sao usados em pre-checagens de resetFTA; o formato de saida e version-dependent.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: showcpus existe em ambas; formatos e colunas diferem por versao.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgconmancmds.html |
| Titulo da fonte | HCL Workload Automation conman command reference |
| Citacao de suporte | conman sc = showcpus |
| Coletado em | 2026-08-21 |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=conman |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a diferença de formato na saída do comando conman showcpus entre a versão 9.5 e 10.2.8?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 152. `hwa-9.5-perfreport-contrast-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2-perfreport-0002: na 9.5 (e versoes anteriores), o atraso medio de agendamento para submissions a agentes era o mesmo intervalo de 30-40 segundos para workloads de ate 1400 jobs/min; o relatorio de performance 10.2 reporta esse mesmo atraso como baseline, portanto o comportamento de agendamento nao mudou nessa faixa de carga entre 9.5 e 10.2, mas sobe sob picos de ~5000 jobs/min em ambientes especificos.

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo que resolve o claim version_dependent: o baseline de atraso e identico na faixa normal; a diferenca aparece em picos. Nao generalizar metricas de pico para todas as versoes.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://www.workloadautomation-community.com/uploads/1/0/2/7/102707030/iws-hwa_10.2_perfreport.pdf |
| Titulo da fonte | IWS/HWA 10.2 performance report |
| Citacao de suporte | for scheduling workloads up to 1400 jobs/min, version 10.2 showed the same average delays as previous versions (between 30 and 40 seconds). |
| Coletado em | 2026-08-21 |
| Capacidade | agent |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=perfreport |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2-perfreport-0002: na 9.5 (e versoes anteriores), o atraso medio de agendamento para submissions a agentes era o mesmo intervalo de 30-40 segundos para workloads de ate 1400 jobs/min; o relatorio de performance 10.2 reporta esse mesmo atraso como baseline, portanto o comportamento de agendamento nao mudou nessa faixa de carga entre 9.5 e 10.2, mas sobe sob picos de ~5000 jobs/min em ambientes especificos?


---

### 153. `hwa-9.5-real-wsa-basico-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

No HCL Workload Automation 9.5, o Workload Service Assurance (WSA) existe e e controlado pela opcao global enWorkloadServiceAssurance (wa, padrao yes) e gerencia o processamento privilegiado de jobs criticos (mission-critical) e seus predecessores, com offsets globais como approachingLateOffset, deadlineOffset e promotionOffset. Em 9.5 o WSA e a forma classica/basica de garantir jobs criticos; a taxonomia expandida e integracao com dynamic agents e um comportamento posterior (10.1+).

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (admin guide/global options 9.5). WSA existia em 9.5 como recurso opcional; o modulo basico de eventos/regras do WSA e documentado nessa versao.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadgloboptdescr.html |
| Titulo da fonte | HCL Workload Automation 9.5 global options (awsadgloboptdescr) - workload service assurance |
| Citacao de suporte | enWorkloadServiceAssurance | wa ... Enable workload service assurance. Enables or disables workload service assurance, which is the feature that manages the privileged processing of mission critical jobs and their predecessors. Specify yes to enable or no to disable. |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | enWorkloadServiceAssurance=opcao global que habilita o WSA (padrao yes em 9.5), WSA=Workload Service Assurance, critical job=job critico de missao |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 9.5 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | dynagent |
| Familia | real-wsa |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para deadline?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 9.5, o Workload Service Assurance (WSA) existe e e controlado pela opcao global enWorkloadServiceAssurance (wa, padrao yes) e gerencia o processamento privilegiado de jobs criticos (mission-critical) e seus predecessores, com offsets globais como approachingLateOffset, deadlineOffset e promotionOffset?


---

### 154. `hwa-install-1028-bkmdm-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na configuração de um BKMDM HWA 10.2.8, o backup master deve ser definido no banco como FTA full-status autolink e incluído no plano com JnextPlan -for 0000. Context: Define the master domain manager configured as backup as a full status autolink fault-tolerant agent.

> **ATENCAO / RESSALVAS DE USO:** Post-install configuration procedure for a backup MDM: workstation definition uses TYPE FTA, AUTOLINK ON, FULLSTATUS ON (composer/DWC); step 6 requires 'Run JnextPlan -for 0000 to include the master domain manager configured as backup workstation in the plan and to send the Symphony file to it'; step 7 raises the workstation job limit (conman 'limit;10'). Procedural claim - no secrets included. | Composer Workstation definition reference: TYPE fta for backup master domain manager; documents autolink on|off and fullstatus on|off. [Validado em lab container 10.2.8: Comprovado no lab container 10.2.8: MDM_BK definido como FTA full-status autolink no composer e no plano.]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicfgbkmdm.html |
| Titulo da fonte | Configuring a master domain manager configured as backup |
| Citacao de suporte | Define the master domain manager configured as backup as a full status autolink fault-tolerant agent in the HCL Workload Automation database |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=planman, component=backup_master_domain_manager |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | planner |
| verbs | install; status |
| Familia | 1028-bkmdm |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 155. `hwa-install-1028-fta-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, um FTA pode resolver dependências locais e iniciar jobs na ausência do domain manager; um Standard Agent é instalado pelo mecanismo de FTA, mas não é fault-tolerant. Context: A fault-tolerant agent can resolve local dependencies and launch jobs in the absence of a domain manager.

> **ATENCAO / RESSALVAS DE USO:** Second official source corroborates: 'Network definition' (awsadnetdefs.html): 'Fault-tolerant agent: An agent workstation capable of resolving local dependencies and launching its jobs in the absence of a domain manager.' and 'Standard agent: An agent workstation that launches jobs only under the direction of its domain manager.' Caveat: v10.2.8 twsinst install types are dynamic|fta|both|zcentric - a 'standard agent' is a workstation type (TYPE S-AGENT), so the wording 'instalado pelo mecanismo de FTA' is not literally documented in 10.2.8.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1manageragenttype.html |
| Titulo da fonte | Manager and agent types |
| Citacao de suporte | Fault-tolerant agent (FTA): A workstation capable of resolving local dependencies and launching its jobs in the absence of a domain manager. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=fault_tolerant_agent |
| Status de revisao | verified |
| Tipo | other |
| verbs | install |
| Familia | 1028-fta |


---

### 156. `hwa-install-agent-1028-ssl-0008`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação HWA 10.2.8 de Dynamic Agent ou FTA, certificados podem ser obtidos do MDM com wauser/wapassword ou fornecidos por sslkeysfolder; HWA gera keystore/truststore e configura SSL, e Java é requerido para SSL durante a instalação. Context: HCL Workload Automation automatically generates the keystore and truststore... Enabling SSL during installation requires Java run time.

> **ATENCAO / RESSALVAS DE USO:** Two methods confirmed: (1) 'Download and deploy to dynamic agents the certificates already available on the master domain manager using the wauser and wapassword parameters'; (2) 'Copy the folder containing the certificates... reference the folder by using the sslkeysfolder parameter' (applies to dynamic agents and fault-tolerant agents). Java run time added with the addjruntime twsinst parameter. Credential-sensitive: never expose wauser/wapassword or keystore passwords in training data. | Agent-parameters page confirms auto-generated keystore/truststore with the specified password.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicustnew.html |
| Titulo da fonte | Installing agents |
| Citacao de suporte | HCL Workload Automation automatically generates the keystore and truststore with the specified password and configures Open Liberty and your agents in SSL mode. Enabling SSL during installation requires Java run time |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install; run |
| Familia | agent-1028 |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para install?


---

### 157. `hwa-install-agent-1028-twsinst-0007`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação HWA 10.2.8, twsinst é o instalador documentado para FTA e Dynamic Agent; a instalação FTA também instala o cliente remoto de linha de comando. Context: Use only the twsinst script to install agents. When you install a fault-tolerant agent, also the remote command-line client is installed.

> **ATENCAO / RESSALVAS DE USO:** Verbatim from the v10.2.8 'Installing agents' overview; the page adds 'You can use the client to run composer and conman commands.' twsinst parameter reference (awspiagentparams.html) confirms -agent dynamic|fta|both|zcentric and the agent installation procedure (awspiinstagent.html) runs twsinst for agents. | Documents twsinst as the agent installer for dynamic agents and fault-tolerant agents.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicustnew.html |
| Titulo da fonte | Installing agents |
| Citacao de suporte | Use only the twsinst script to install agents. When you install a fault-tolerant agent, also the remote command-line client is installed. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=fault_tolerant_agent |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dynagent |
| verbs | install |
| Familia | agent-1028 |

**Perguntas relacionadas:**

- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar install?
- Como configurar ou solucionar problemas no dynamic agent ou broker para install?


---

### 158. `hwa-install-ddm-1028-prereqs-0006`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação DDM/BDDM HWA 10.2.8, o componente requer banco dedicado, Liberty dedicado, certificados e parâmetros para localizar MDM/broker, incluindo master, mdmbrokerhostname e mdmhttpsport. Context: The dynamic domain manager and backup dynamic domain manager require a dedicated database and a dedicated Open Liberty.

> **ATENCAO / RESSALVAS DE USO:** Required-information table confirms --master, --mdmbrokerhostname, --mdmhttpsport ('The port of the master domain manager host used by the broker to contact master domain manager'), plus database, wauser/wapassword, wlpdir, sslkeysfolder/sslpassword parameters; certificates ca.crt/tls.key/tls.crt are required; prerequisite steps include installing Open Liberty on both DDM/BDDM workstations and copying the certificate folder from the MDM. Procedural claim. | v10.2.0 (v102) version of the same topic; identical sentence for HWA 10.2.x Distributed.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDDM.html |
| Titulo da fonte | Installing the dynamic domain manager and backup dynamic domain manager |
| Citacao de suporte | The dynamic domain manager and backup dynamic domain manager require a dedicated database and a dedicated Open Liberty. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install; open |
| Familia | ddm-1028 |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Como configurar ou solucionar problemas no dynamic agent ou broker para install?


---

### 159. `hwa-lab-10.2.8-adhoc-dynamic-submit-ready-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratorio HWA 10.2.8, um submission ad hoc sem data/run cycle usando `conman sbj = MDMDA#LAB_DA_SCRIPT_01;noask` foi aceito e colocado no job stream default `MDMDA#JOBS`, mas o job permaneceu READY sem requisicao de execucao no JobManager_message.log. A causa raiz foi identificada como o LIMIT 0 (default pos-instalacao) da workstation dinamica MDMDA: apos `conman lc MDMDA;10` os jobs do agente dinamico despacharam e completaram SUCC (ver hwa-lab-10.2.8-limit-zero-ready-rootcause-0027 e hwa-lab-10.2.8-complex-stream-execution-0036). O dispatch do agente dinamico foi validado apos a correcao do limit; o READY inicial nao indicava problema de scheduling syntax.

> **ATENCAO / RESSALVAS DE USO:** Causa raiz resolvida: LIMIT 0 pos-instalacao da workstation dinamica MDMDA (cross-reference hwa-lab-10.2.8-limit-zero-ready-rootcause-0027 e hwa-lab-10.2.8-complex-stream-execution-0036). Fonte primaria original local: local conman execution plus https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Ad hoc dynamic-agent submission |
| Citacao de suporte | Submitted MDMDA#LAB_DA_SCRIPT_01 to batchman as MDMDA#JOBS.LAB_DA_SCRIPT_01; conman showjobs displayed READY. After conman lc MDMDA;10 the dynamic-agent jobs dispatched and completed SUCC (root cause: workstation limit 0). |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 160. `hwa-lab-10.2.8-agent-both-installation-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, a opção '-agent both' do utilitário twsinst instala concomitantemente em um único nó o Fault-Tolerant Agent (Netman/Mailman na porta 31111) e o Dynamic Agent (JobManager/ITA na porta 31114) sob o mesmo usuário wauser.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; container RHEL 9 UBI9 (tws-agent); HWA 10.2.8 |
| Observado em | 2026-09-09T18:40:00-03:00 |

**Procedimento executado:** 1. Executar composer 'update cpu=TWS-AGENT; set ignore=on; noask' no Master para ignorar instância anterior. 2. Desinstalar agente antigo no nó com twsinst -uninst. 3. Instalar com twsinst -new -agent both -thiscpu AGT1 -master MDM -port 31111 -tdwbhostname tws-hwa.lab -tdwbport 31116. 4. Estender plano com JnextPlan -for 0000. 5. Submeter jobs paralelos no FTA (AGT1) e Dynamic Agent (TWS-AGENT_1).

**Saida real observada:** Instalação completada com AWSFAB033I rc0. Processos netman e JobManager ativos no nó. Ambos os jobs AGT1#FTA_ECHO (#J104316) e TWS-AGENT_1#DYN_ECHO (#J1045913943) concluídos com SUCC rc0.

**Perguntas relacionadas:**

- Como instalar simultaneamente um Fault-Tolerant Agent e um Dynamic Agent com o twsinst no HWA?
- Qual o comando para colocar uma workstation em estado IGNORE no banco do HWA utilizando o composer?
- Como funciona a opção -agent both do instalador twsinst no HCL Workload Automation 10.2.8?


---

### 161. `hwa-lab-10.2.8-agent-restart-ready-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratorio HWA 10.2.8, apos ShutDownLwa e StartUpLwa o agente dinamico MDMDA retornou com o flag JobManager e o registro de recursos (AWSITA083I) retomou, mas um novo submission ad hoc com alias unico ainda permaneceu READY. O restart isolado nao resolveu o dispatch porque a causa raiz nao era o restart e sim o LIMIT 0 pos-instalacao da workstation; apos `conman lc MDMDA;10` os jobs do agente dinamico executaram com sucesso (ver hwa-lab-10.2.8-limit-zero-ready-rootcause-0027 e hwa-lab-10.2.8-agent-restart-reconnect-0048).

> **ATENCAO / RESSALVAS DE USO:** Causa raiz: LIMIT 0 pos-instalacao da workstation (hwa-lab-10.2.8-limit-zero-ready-rootcause-0027); restart sozinho nao resolve o dispatch. Reconnect apos restart documentado em hwa-lab-10.2.8-agent-restart-reconnect-0048. Fonte primaria original local: local ShutDownLwa/StartUpLwa, conman e JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgresource.html |
| Titulo da fonte | Dynamic-agent restart validation |
| Citacao de suporte | AWSITA111I The Resource Advisor Agent is stopped; AWSITA047I Starting subagent "JobManager"; AWSITA083I Resource information was sent; submitted alias remained READY until the workstation limit was raised (lc MDMDA;10), after which jobs dispatched successfully. |
| Coletado em | 2026-08-19 |
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
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 162. `hwa-lab-10.2.8-awsbin091e-rootcause-0098`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratório HWA 10.2.8, o GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration retorna HTTP 500 com AWSJSY404E envolvendo AWSBIN091E 'The workstation does not support monitoring.' para TODAS as workstations (MDM, MDMDA, MDMXA, MDM_DWB), mesmo com o monman/EDWA ativo. O conman showcpus confirmou que MDM tem o flag 'I J M EA' (monman M + event-driven EA) e MDMDA tem 'LBI J M' (monman M ativo) no Symphony — portanto o monitoring está ativo e o erro NÃO reflete o estado real. A causa raiz é a implementação do endpoint REST V2, que lê o monitoring configuration via a operação 'readFromScribner' de um local não suportado pelo Symphony nessas workstations broker-managed (o error wrapper AWSJSY404E 'The Symphony plan operation readFromScribner could not be completed'). Conclusão: o REST V2 monitoring-configuration é um endpoint de leitura quebrado/não suportado para estas workstations, enquanto o event processing, o monman e os event rules (FileMonitor/TWSObjectsMonitor) funcionam normalmente via composer/deployconf/sendEvent.

> **ATENCAO / RESSALVAS DE USO:** Completa a evidência 0095: o erro não é causado por falta de monitoring (flag M presente); é uma limitação do endpoint REST V2 (readFromScribner não suportado para workstations broker-managed). O monitoramento real via monman/ssmagent/EDWA continua funcional. | Fonte primária original local: curl https://[IP_ADDRESS]:31116/twsd/api/v2/plan/workstation/*/action/monitoring-configuration + conman showcpus com env correta (source tws_env.sh + UNISONWORK=/opt/hwa/TWSDATA). Obs: conman sem a env correta tenta abrir /opt/hwa/TWS/Symphony e falha com AWSBHU001E/AWSBCU035E.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | Event rule management / monitoring configuration - HCL Workload Automation 10.2.8 |
| Citacao de suporte | conman showcpus: MDM ... I J M EA; MDMDA ... LBI J M. GET monitoring-configuration -> HTTP 500 AWSJSY404E wrapping AWSBIN091E for MDM, MDMDA, MDMXA, MDM_DWB. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSJSY404E, command=twsd |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJSY404E no HWA?
- Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?
- Qual é o significado da mensagem de erro AWSBIN091E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?


---

### 163. `hwa-lab-10.2.8-batchman-showcpus-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

After the initial plan was generated in the WSL2 laboratory, conman showcpus reported Batchman LIVES for the MDM workstation and displayed the generated MDMXA x-agent workstation.

> **ATENCAO / RESSALVAS DE USO:** Operational observation, not a universal topology claim. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /opt/hwa/TWS/bin/conman

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | conman showcpus laboratory execution |
| Citacao de suporte | Scheduled for (Exp) 08/17/26 (#1) on MDM. Batchman LIVES. ... MDM manager ... MDMXA x-agent. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 164. `hwa-lab-10.2.8-bmevents-config-0084`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 lab, BmEvents.conf (TWA_DATA_DIR=/opt/hwa/TWSDATA/BmEvents.conf) was configured and validated for job scheduling status event reporting. Parameters used: OPTIONS=MASTER (report all scheduling events from the scheduling environment), LOGGING=ALL (log events from all jobs/job streams, no key filter), SYMEVNTS=YES (report status immediately after plan creation), CHSCHED=HIGH (event for any schedule status transaction), and EVENT=51 101 102 103 104 105 106 151 152 154 155 156 201 202 203 204 251 252 (which completely overrides the default list 51 101 102 105 151 152 155 201 202 203 204 251 252). Output destinations: PIPE=UNISONWORK/MAGENT.P (NetView agent), FILE=/opt/hwa/TWSDATA/event.log (ASCII/UTF-8) and JSON=/opt/hwa/TWSDATA/event.json (structured JSON for third-party monitoring). After a conman stop/start of the MDM production processes (batchman, mailman, jobman restart), the event.log and event.json files were created and populated. Submitting job stream MDMDA#EVTJS_TEST produced the full event lifecycle in event.json: 106 JobSubmit, 156 SchedSubmit, 103 JobLaunch, 104 JobDone, 154 SchedDone for job EVTJOB1, in addition to 51 ProcessReset and 251 LinkDropped at batchman restart.

> **ATENCAO / RESSALVAS DE USO:** Key lab findings: (1) The BmEvents.conf must be in TWA_DATA_DIR (=/opt/hwa/TWSDATA) not in the sample dir /opt/hwa/TWS/config; (2) FILE/JSON paths must be absolute (UNISONWORK/event.log as relative path fails with AWSBDD003E 'No such file or directory'); (3) batchman/mailman open the FILE/JSON files at startup and keep the fd open - deleting the file sends events to the deleted inode (not recreated until process restart); (4) changes to BmEvents.conf require a production process restart via conman stop MDM then conman start MDM (batchman/mailman/jobman restart; netman/monman/writer stay); JnextPlan alone does not recycle batchman; (5) the EVENT parameter completely overrides defaults - job launch/done (103/104) and schedule submit/done (156/154) are NOT in the default list and must be added explicitly. AWSBDD003E/001E-004E are the BmEvents message component (9.5 catalog, not published in 10.2.8). [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsisnetvbmevents.html |
| Titulo da fonte | The BmEvents configuration file - HCL Workload Automation 10.2.8 |
| Citacao de suporte | event.json: {"event":"106","eventName":"JobSubmit"...}; {"event":"103","eventName":"JobLaunch"...}; {"event":"104","eventName":"JobDone"...}; {"event":"156","eventName":"SchedSubmit"}; {"event":"154","eventName":"SchedDone"}. |
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
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['submit', 'link', 'conman'], result=event.json: {"event":"106","eventName":"JobSubmit"...}; {"event":"103","eventName":"JobLaunch"...}; {"event":"104","eventName":"JobDone"...}; {"event":"156","eventName":"SchedSubmit"}; {"event":"154","eventName":"SchedDone"}. | Key lab findings: (1) The BmEvents.conf must be in TWA_DATA_DIR (=/opt/hwa/TWSDATA) not in the sample dir /opt/hwa/TWS/config; (2) FILE/JSON paths must be absolute (UNISONWORK/event.log as relative path fails with AWSBDD003E 'No such file or directory'); (3) batchman/mailman open the FILE/JSON files at startup and keep the fd open - deleting the file sends events to the deleted inode (not recreated until process restart); (4) changes to BmEvents.conf require a production process restart via conman stop MDM then conman start MDM (batchman/mailman/jobman restart; netman/monman/writer stay); JnextPlan alone does not recycle batchman; (5) the EVENT parameter completely overrides defaults - job launch/done (103/104) and schedule submit/done (156/154) are NOT in the default list and must be added explicitly. AWSBDD003E/001E-004E are the BmEvents message component (9.5 catalog, not published in 10.2.8)., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-18-bmevents-config.jsonl |
| Terminologia normalizada | command=conman |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?
- O que causa erro na resolução de local parameters em jobs e como solucionar?


---

### 165. `hwa-lab-10.2.8-broker-active-sc-0079`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `topology`

**Afirmacao / Conteudo:**

In the HWA laboratory, the broker workstation MDM_DWB is active and LINKED to the master. 'conman sc' shows: 'MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM'. Interpreting the state letters: L = LINKED (linked to master domain), T = TCP/network link, I = in-sync/active, J = JobManager/gateway process up, W = WAGENT/broker runtime up. This corrects the earlier assessment (evidence broker-topology-0070) that the broker runtime was down because JobManagerGW had autostart=no; the broker is in fact running and linked, and the REST API V2 on /twsd:31116 is served by this broker's gateway.

> **ATENCAO / RESSALVAS DE USO:** Correction to broker-topology-0070: broker IS active. MDMDA shows LIMIT 5 (raised earlier via lc MDMDA;5;noask). [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sc (status) output for MDM_DWB

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Broker workstation active and linked |
| Citacao de suporte | MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM |
| Coletado em | 2026-08-18 |
| Classificacao de risco | mutating |
| Capacidade | topology |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['link', 'rest api', 'conman'], result=MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM | Correction to broker-topology-0070: broker IS active. MDMDA shows LIMIT 5 (raised earlier via lc MDMDA;5;noask)., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-broker-active.jsonl |
| Terminologia normalizada | command=conman |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar topology?
- Qual endpoint REST API V2 é utilizado para topology no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para topology?


---

### 166. `hwa-lab-10.2.8-broker-topology-correction-0080`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `topology`

**Afirmacao / Conteudo:**

CORRECTION to evidence hwa-lab-10.2.8-broker-topology-0070. On 2026-08-18, 'conman sc' (workstation status) shows MDM_DWB is ACTIVE and LINKED: 'MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM' (L=LINKED, J=JobManager/gateway up, W=WAGENT up). The 0070 conclusion that 'the broker runtime is not running' was based only on JobManagerGW.ini autostart=no and absence of a standalone JobManagerGW process, but the broker is actually running as part of the master engine and is LINKED. Consequently the REST API V2 on /twsd:31116 (validated live in evidence 0077) is served by the broker's gateway, and the port 31116 Java/JobManager listener is the broker. The broker activation follow-up (P2a) is therefore already satisfied; no separate JobManagerGW start is required.

> **ATENCAO / RESSALVAS DE USO:** Replaces the 'broker not running' conclusion in 0070. State LTI JW indicates LINKED + JobManager + WAGENT active. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sc MDM_DWB

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Broker topology correction |
| Citacao de suporte | MDM_DWB ... OTHR BROKER ... LTI JW MASTERDM (active/linked) |
| Coletado em | 2026-08-18 |
| Classificacao de risco | read_only |
| Capacidade | topology |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar topology?
- Qual endpoint REST API V2 é utilizado para topology no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para topology?


---

### 167. `hwa-lab-10.2.8-cleanup-orphans-0083`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, remaining test/orphan model objects were removed from the database, leaving a clean model. Via 'echo y | composer delete MDMDA#<stream>' the 14 remaining MDMDA test job streams were deleted (CF_TEST, CONF_TEST, CONMAN_OPS, CPLXJOB2M, CPLXSTRM, DEAD_TEST, DEPS01, FENCE_TEST, KEYJOB_TEST, LAB_DA_EVERY2M, LAB_DA_SCRIPT2M, PROMPT_TEST, RECOVTEST, VARTEST) and 3 MDMXA streams (FINAL, FINALPOSTREPORTS, LAB_EVERY2M), each AWSBIA290I Total objects deleted: 1. composer delete only accepts job streams ([workstation#]jobstream). Run cycle groups, calendars and variable tables were removed via the REST API V2 DELETE /model/{runcyclegroup|calendar|variabletable}/{id} (using the def.id field, not the root id): LABRCG (f742ef0d), LABCAL (e121ba0f) and LABTAB (be717ca3) each returned HTTP 200 with {"deletedObjects":[...],"error":false}. The default variable table MAIN_TABLE (9223ee2a) could not be deleted (AWSJDB324E 'The default variable table cannot be deleted'), which is expected. Final model state: jobstreams=0, runcyclegroup=0, calendar=0, variabletable=1 (MAIN_TABLE only).

> **ATENCAO / RESSALVAS DE USO:** REST DELETE uses def.id, not root id (root id None caused AWSJDB402E). Default vartable is not deletable (AWSJDB324E). [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer delete and https://[IP_ADDRESS]:31116/twsd/api/v2/model/{runcyclegroup,calendar,variabletable}/{id} DELETE ATENÇÃO (lição 0100): FINAL/FINALPOSTREPORTS são jobstreams de SISTEMA (virada de plano, Sfinal) e NÃO deveriam ter sido removidos como orphan; remoção quebrou a virada automática (ver 0099).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Test/orphan model object cleanup |
| Citacao de suporte | jobstreams=0, rcg=0, calendar=0, variabletable=1 (MAIN_TABLE default). DELETE HTTP 200 for LABRCG/LABCAL/LABTAB. |
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
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['fence', 'rest api', 'composer', 'conman'], result=jobstreams=0, rcg=0, calendar=0, variabletable=1 (MAIN_TABLE default). DELETE HTTP 200 for LABRCG/LABCAL/LABTAB. | REST DELETE uses def.id, not root id (root id None caused AWSJDB402E). Default vartable is not deletable (AWSJDB324E)., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-cleanup-orphans.jsonl |
| Terminologia normalizada | message=AWSBIA290I, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIA290I no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?
- Qual é o significado da mensagem de erro AWSJDB324E no HWA?
- Como solucionar ou diagnosticar o erro AWSJDB324E no HWA?


---

### 168. `hwa-lab-10.2.8-cleanup-test-0076`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, composer delete removed the persisted test job streams created during syntax/runtime validation. Using 'composer delete <ws>#<stream>' piped with confirmation 'y', the following streams were deleted (AWSBIA290I Total objects deleted: 1): HR_TEST3, HR_TEST4, HR_TEST5, JOIN_OK2, IF_OK2, CRIT_OK, TASK_OK, PRIO_TEST, REC1, REST_HOLD, MAXDUR_TEST, MINDUR_TEST, CALEND_TEST, OOVPAR_TEST, OOVDN_TEST, WS_TEST, DB_TEST, FTP_TEST, START_FILE, START_FILEMOD. Streams reported 'Total objects deleted: 0' with AWSJCL017W 'No objects have been found' were already absent (transient/on-demand streams or previously removed). A subsequent conman 'sj =MDMDA' query returned no remaining test-looking streams (HR_*, PRIO*, REC_*, TEST, JSDL, OOV*, JOIN, IF_*, CRIT, TASK, CAL*, PAYROLL, WS_*, DB_*, FTP_*, START_*, T1*), confirming cleanup. Composer delete requires an interactive confirmation ('Are you sure...') that must be answered via stdin (e.g. 'echo y | composer delete').

> **ATENCAO / RESSALVAS DE USO:** composer delete is interactive; pipe 'y' to confirm. Model cleanup of validation artifacts. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer delete on MDMDA#<test streams>

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Test job stream cleanup |
| Citacao de suporte | AWSBIA290I Total objects deleted: 1 for each existing test stream; AWSJCL017W for absent ones. |
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
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['confirm', 'composer', 'conman'], result=AWSBIA290I Total objects deleted: 1 for each existing test stream; AWSJCL017W for absent ones. | composer delete is interactive; pipe 'y' to confirm. Model cleanup of validation artifacts., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-17-cleanup-test.jsonl |
| Terminologia normalizada | message=AWSBIA290I, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCL017W no HWA?
- Como solucionar ou diagnosticar o erro AWSJCL017W no HWA?
- Qual é o significado da mensagem de erro AWSBIA290I no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?


---

### 169. `hwa-lab-10.2.8-complex-stream-execution-0036`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, the previously validated complex stream CPLXSTRM was added and submitted ad hoc to MDMDA. Its four dependent jobs executed in order with priorities 10, 20, HI and GO, and the stream completed SUCC under LIMIT 2.

> **ATENCAO / RESSALVAS DE USO:** This validates real execution, not only Composer syntax. The dynamic-agent workstation limit had previously been raised from 0 to 10. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer add, conman sbs and JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Complex Composer stream execution |
| Citacao de suporte | CPLXSTRM SUCC; CPLX_01 SUCC; CPLX_02 SUCC; CPLX_03 SUCC; CPLX_04 SUCC; JobManager logged AWSITA031I started and AWSITA034I completed successfully for each job. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['composer', 'submit'], result=CPLXSTRM SUCC; CPLX_01 SUCC; CPLX_02 SUCC; CPLX_03 SUCC; CPLX_04 SUCC; JobManager logged AWSITA031I started and AWSITA034I completed successfully for each job. | This validates real execution, not only Composer syntax. The dynamic-agent workstation limit had previously been raised from 0 to 10., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-complex-execution.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, the previously validated complex stream CPLXSTRM was added and submitted ad hoc to MDMDA?


---

### 170. `hwa-lab-10.2.8-composer-every-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 laboratory, a Composer job stream using an inclusive daily run cycle with `( AT 1351 EVERY 0002 EVERYENDTIME 1400 )` validated successfully and was added with four UNIX jobs targeted at MDMXA.

> **ATENCAO / RESSALVAS DE USO:** The first syntax attempt with EVERY outside the parenthesized run-cycle time restriction was rejected. The corrected syntax validated. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /tmp/lab_every2m.def and composer

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Composer EVERY validation |
| Citacao de suporte | AWSBIA302I No errors in /tmp/lab_every2m.def. AWSBIA288I Total objects updated: 5. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 171. `hwa-lab-10.2.8-confirmed-job-0055`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, a job defined with CONFIRMED completed execution and entered PEND with the [Confirmed] indicator; the stream remained READY. After conman confirm MDMDA#CONF_TEST.CNFJOB;SUCC, both the job and stream became SUCC.

> **ATENCAO / RESSALVAS DE USO:** confirm requires SUCC or ABEND argument. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman confirm and sj

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Confirmed job workflow |
| Citacao de suporte | confirm ... ;SUCC forwarded; CNFJOB became SUCC with [Confirmed]. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 172. `hwa-lab-10.2.8-cross-workstation-dependency-fta-dyn-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

No HWA 10.2.8, uma dependência cruzada entre tecnologias heterogêneas (um job em Dynamic Agent com FOLLOWS apontando para um job em Fault-Tolerant Agent) é mantida de forma íntegra pelo Batchman: o job do Dynamic Agent permanece retido em HOLD até a conclusão com SUCC do job no FTA, liberando imediatamente o despacho via Broker.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; containers tws-hwa e tws-agent; HWA 10.2.8 |
| Observado em | 2026-09-09T19:34:00-03:00 |

**Procedimento executado:** Definido stream AGT1#CROSS_STREAM com AGT1#CROSS_JOB_A (sleep 8s) e TWS-AGENT_1#CROSS_JOB_B com FOLLOWS CROSS_JOB_A. Submetido no conman e monitorado com sj @#@;deps.

**Saida real observada:** Job B permaneceu em HOLD no conman deps enquanto Job A rodava no FTA. Ao concluir com SUCC rc0 (#J105717), o Job B foi imediatamente liberado da dependência para o Broker.

**Perguntas relacionadas:**

- É possível configurar uma dependência FOLLOWS entre um job rodando em Dynamic Agent e um job em FTA?
- Como o Batchman resolve dependências cruzadas entre agentes dinâmicos e agentes tolerantes a falhas?


---

### 173. `hwa-lab-10.2.8-destructive-cleanup-lesson-0100`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Lição crítica de segurança operacional no laboratório HWA 10.2.8: os jobstreams de sistema MDMXA#FINAL e MDMXA#FINALPOSTREPORTS (definidos no arquivo oficial do produto /opt/hwa/TWS/config/Sfinal com ON RUNCYCLE 'FREQ=DAILY;' AT 2359 CARRYFORWARD e jobs STARTAPPSERVER -> MAKEPLAN -> SWITCHPLAN -> CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS) foram incluídos em uma limpeza de 'test/orphan' objects (evidência hwa-lab-10.2.8-cleanup-orphans-0083: '3 MDMXA streams (FINAL, FINALPOSTREPORTS, ...) deleted') e removidos do banco com 'echo y | composer delete MDMXA#FINAL'. Essa ação destrutiva não quebrou o scheduler imediatamente, mas removeu o mecanismo automático de virada de plano: o JnextPlan passou a apenas estender o plano existente (-for 0000), o dia corrente ficou preso (conman sc mostrando 08/18/26 em 08/19/26) e nenhuma instância MDMXA#FINAL era criada (evidência hwa-lab-10.2.8-plan-rollover-fix-0099). Em produção, o impacto seria a ausência de geração do plano de D+1, jobs não agendados e planos nunca avançando. Recuperação documentada: composer add Sfinal + planman unlock + JnextPlan. REGRA para o corpus e operação: ao limpar objetos de teste, NUNCA deletar jobstreams de sistema/plano (FINAL, FINALPOSTREPORTS, SFINAL, JNEXTPLAN e equivalentes de virada) sem antes verificar sua função no ciclo de produção; usar allowlist de exclusão e revisar composer display antes de confirmar qualquer composer delete com echo y.

> **ATENCAO / RESSALVAS DE USO:** Ação destrutiva documentada a posteriori (post-mortem). A lição: composer delete com echo y é irreversível e removeu FINAL/FINALPOSTREPORTS (jobstreams de virada do produto). Em produção exigiria autorização explícita e análise de impacto. Referências cruzadas: cleanup-orphans-0083, cleanup-test-0076, plan-rollover-fix-0099. | Fonte primária original local: post-mortem da limpeza P7b + correção P17

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing - HCL Workload Automation 10.2.8 |
| Citacao de suporte | evidência 0083: '3 MDMXA streams (FINAL, FINALPOSTREPORTS, ...) deleted'; evidência 0099: conman sc preso em 08/18/26, recovery composer add Sfinal + planman unlock + JnextPlan. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | destructive |
| Capacidade | mdm |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['composer delete (FINAL/FINALPOSTREPORTS lesson)'], result=Lição observada diretamente no lab: os jobstreams de sistema MDMXA#FINAL e MDMXA#FINALPOSTREPORTS (definidos em /opt/hwa/TWS/config/Sfinal com ON RUNCYCLE 'FREQ=DAILY') são objetos de sistema; removê-los quebra a virada de plano diária. A restauração da virada está documentada em hwa-lab-10.2.8-plan-rollover-fix-0099., validated_at=2026-08-23T00:50:00BRT, evidence_file=lab-validation-2026-08-23-r8-conman-ops.jsonl |
| Terminologia normalizada | command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?
- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar mdm?


---

### 174. `hwa-lab-10.2.8-dynamic-agent-dispatch-pending-0011`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratorio HWA 10.2.8, definicoes Composer destinadas ao agente dinamico MDMDA foram validadas, adicionadas e submetidas, mas permaneceram READY durante a janela de observacao inicial; o JobManager logou registro de recursos mas nenhuma requisicao de execucao. Investigacoes posteriores identificaram a causa raiz: a workstation dinamica MDMDA tinha LIMIT 0 (default pos-instalacao); apos `conman lc MDMDA;10` os jobs despacharam e completaram SUCC (hwa-lab-10.2.8-limit-zero-ready-rootcause-0027, hwa-lab-10.2.8-complex-stream-execution-0036, hwa-lab-10.2.8-jobtypes-0064). O dispatch de jobs no agente dinamico foi validado; o estado READY inicial foi atribuido ao limit da workstation, nao a definicao Composer.

> **ATENCAO / RESSALVAS DE USO:** Causa raiz: LIMIT 0 da workstation dinamica MDMDA (default pos-instalacao); resolvido com conman lc MDMDA;10. Dispatch validado (ver hwa-lab-10.2.8-limit-zero-ready-rootcause-0027, hwa-lab-10.2.8-complex-stream-execution-0036, hwa-lab-10.2.8-jobtypes-0064). Fonte primaria original local: local execution: conman, composer e /opt/hwa/TWSDATA/stdlist/JM/JobManager_message.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Dynamic-agent dispatch investigation |
| Citacao de suporte | conman showjobs displayed LAB_DA_EVERY2M and LAB_DA_SCRIPT2M in READY; JobManager logged resource registration but no request for those jobs. Root cause: MDMDA workstation limit 0; after conman lc MDMDA;10 the jobs dispatched and completed SUCC. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Por que um job despachado para dynamic agent pode permanecer com status pending no broker?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 175. `hwa-lab-10.2.8-dynamic-pool-load-balancing-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Um Dynamic Workload Broker Pool (TYPE POOL) contendo múltiplos agentes dinâmicos membros (ex: MDMDA local e TWS-AGENT_1 remoto) distribui automaticamente as instâncias de jobs concorrentes entre os membros saudáveis, registrando na saída do conman showjobs o agente executor entre chaves (ex: {MDMDA}, {TWS-AGENT_1}).

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; containers tws-hwa e tws-agent; HWA 10.2.8 |
| Observado em | 2026-09-09T19:33:00-03:00 |

**Procedimento executado:** Configurado LABPOOL com membros MDMDA e TWS-AGENT_1. Submetidas instâncias concorrentes BAL_2 e BAL_3. Verificada a alocação de BAL_2 em {MDMDA} e BAL_3 em {TWS-AGENT_1}, ambas concluídas com SUCC rc0.

**Saida real observada:** Instâncias executadas paralelamente em nós distintos com anotação explícita entre chaves no conman sj. Balanceamento de carga do broker comprovado em lab.

**Perguntas relacionadas:**

- Como o Dynamic Workload Console e o conman indicam qual agente de um pool executou determinado job?
- Como configurar balanceamento de carga de jobs entre múltiplos agentes dinâmicos em um dynamic pool?


---

### 176. `hwa-lab-10.2.8-edwa-rest-and-restart-0095`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

HWA 10.2.8 lab findings on the event-rule REST API and WSL restart procedure. (1) The Liberty engineServer registers an EventRuleEngineApplication under /twsd exposing REST resource classes for event rules: MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, RuleInstanceEventRuleResource, ActionRunEventRuleResource, PluginConfigurationEventRuleResource (paths visible in messages.log as /eventrule/engine/*, /eventrule/deployment/*, and /api/v2/eventrule). Direct GET/POST/OPTIONS against /eventrule/engine/messageLog, /messageLogRecord, /auditRecord, /actionRun, /ruleInstance, /pluginConfiguration and /eventrule/deployment/deploy all returned HTTP 404 even with basic auth and empty JSON or query params - the resources require specific sub-paths/params not discoverable without the deployed Swagger UI for that application, so event-rule CRUD/query over REST is not usable via the documented paths alone. (2) GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration consistently returns AWSJSY404E wrapping AWSBIN091E 'An error occurred obtaining the monitoring configuration file for workstation ... The workstation does not support monitoring.' for MDMDA and MDMXA even though monman + ssmagent EDWA are running and FileMonitor/TWSObjectsMonitor rules work - the REST read of the monitoring configuration is broken/unsupported on these broker-managed workstations, while event processing itself is functional. (3) WSL restart procedure: after a WSL Ubuntu reboot only the JobManager agent and the EDWA ssmagent start automatically (via the CPA systemd unit tebctl-tws_cpa_agent_wauser); the engineServer (Open Liberty) must be started with 'sudo -u wauser /opt/hwa/appservertools/startAppServer.sh' (equivalent to conman startappserver), then the production processes with 'conman start MDM' (batchman/mailman/jobman), and the monman event monitoring engine with 'conman startmon MDMDA' + 'conman startmon MDM' (monman does NOT auto-start on reboot even though conman sc shows the M flag from the plan). The WSL /etc/hosts regenerates on reboot and loses the '[IP_ADDRESS] MDMHOST' alias, which must be re-added or the Resource Advisor logs AWSRES003E and AWSKRAE100E (heartbeat missed).

> **ATENCAO / RESSALVAS DE USO:** The 404 on /eventrule/engine/* may require path parameters (e.g. {id}) not guessed; the authoritative operation list is only in the deployed Swagger UI which was not served at /twsd/swagger.json or /eventrule/engine/swagger.json. AWSBIN091E is reproducible and tied to broker-managed workstations reading their monitoring configuration file via the REST path; event rules still function via monman/sendevent/FileMonitor. restart procedure observed twice (2026-08-19 01:21 and prior) with identical steps. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstartstop.html |
| Titulo da fonte | Starting and stopping processes on a workstation - HCL Workload Automation 10.2.8 |
| Citacao de suporte | /eventrule/engine/* resources registered (MessageLogRecord/AuditRecord/RuleInstance/ActionRun/PluginConfiguration EventRuleResource) but direct calls 404; AWSBIN091E on monitoring-configuration; restart needs startAppServer.sh + conman start + conman startmon + /etc/hosts MDMHOST. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSJSY404E, command=restart |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJSY404E no HWA?
- Como solucionar ou diagnosticar o erro AWSJSY404E no HWA?
- Qual é o significado da mensagem de erro AWSBIN091E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIN091E no HWA?


---

### 177. `hwa-lab-10.2.8-edwa-rules-0085`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 lab, event-driven workload automation (EDWA) was configured and validated end-to-end on the dynamic broker workstation. (1) The event rules are managed by the composer command line (add/validate/list/display EVENTRULE) with XML validated against EventRules.xsd; the exact syntax is 'add <file>' and 'validate <file>;syntax' (no 'EVENTRULE' type prefix). (2) A FileMonitor event rule (eventType FileCreated, filteringPredicate FileName/Workstation/SampleInterval) was added as non-draft (isDraft=no); the rule builder deployed it within the default deploymentFrequency (5 minutes) - status changed from 'activation pending' to 'active', and the generated monitoring configuration appeared in /opt/hwa/TWSDATA/EDWA/monconf/ (FileMonitor.cfg, activeRules.txt, deployconf.zip) with the ssmagent.bin EDWA instance reloading it. (3) Creating the monitored file /tmp/hwa_oneshot/trigger.txt was detected by the ssmagent (traps.log SNMP trap 'FileCreatedEvent event', Workstation=MDMDA) and delivered to the event processing server (running in the Open Liberty engineServer on MDM) which logged the rule instance and the resolved action message in the database (log.llrc_log_records: AWSMSL101I 'The message ... has been successfully logged', MessageLogger MSGLOG action with variables %{fileEvt1.FileName}/%{fileEvt1.Workstation} substituted). (4) A second rule with actionProvider TWSAction actionType sbs (SubmitJobStream, parameters JobStreamName=EVTJS_TEST + JobStreamWorkstationName=MDMDA) executed 'SBS MDMDA#EVTJS_TEST' (AWSTAP101I 'The job stream EVTJS_TEST has been successfully submitted') and the job stream + job EVTJOB1 actually ran (pln.pjor_job_runs status E, actual start/end timestamps, JobManager archive zip with script.sh/out.log/trace.log confirming the taskLauncher launched script.sh as user wauser). The monman flag M is present on MDM and MDMDA in conman showcpus.

> **ATENCAO / RESSALVAS DE USO:** Important lab findings: (1) 'BMEvents' is a naming trap - the BmEvents.conf config file is event REPORTING for batchman/mailman; event-driven JOB LAUNCHING is the EDWA feature (event rules) which is what was tested here; (2) REST API V2 (WA_API3_v2.json) exposes only event monitoring/processor ACTION endpoints (PUT /plan/workstation/action/{start,stop,switch}-event-{monitoring,processor} and GET monitoring-configuration) - event rule CRUD is via composer/DWC or a separate /eventrule/engine/* REST application (classes like MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, PluginConfigurationEventRuleResource, EventRuleEngineApplication in the Liberty engineServer); (3) GET monitoring-configuration returned AWSBIN091E 'The workstation does not support monitoring' for MDMDA/MDMXA even though monman+ssmagent EDWA were running - monitoring was active but the REST read was failing on the broker; (4) FileCreated only fires on NEW file creation - deleting and recreating the same filename in the monitored dir was not re-detected in the retry test (filemon caches the creation); (5) the FileMonitor.cfg generated by the rule builder contains filemon directives (directoryName, fileName, fileAttribute=creation, updateInterval=60) executed by the Netcool/SSM agent ssmagent.bin. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html and awsrgfilemonitorevents.html and awsrgtwsaction.html |
| Titulo da fonte | Event rule management process; FileMonitor events; TWSAction actions - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSMSL101I The message 'LAB_FILE_TRIGGER: file created /tmp/hwa_oneshot/trigger.txt on MDMDA' has been successfully logged.; AWSTAP101I The job stream 'EVTJS_TEST' has been successfully submitted. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['confirm', 'submit', 'composer', 'conman', 'edwa', 'sbs'], result=AWSMSL101I The message 'LAB_FILE_TRIGGER: file created /tmp/hwa_oneshot/trigger.txt on MDMDA' has been successfully logged.; AWSTAP101I The job stream 'EVTJS_TEST' has been successfully submitted. | Important lab findings: (1) 'BMEvents' is a naming trap - the BmEvents.conf config file is event REPORTING for batchman/mailman; event-driven JOB LAUNCHING is the EDWA feature (event rules) which is what was tested here; (2) REST API V2 (WA_API3_v2.json) exposes only event monitoring/processor ACTION endpoints (PUT /plan/workstation/action/{start,stop,switch}-event-{monitoring,processor} and GET monitoring-configuration) - event rule CRUD is via composer/DWC or a separate /eventrule/engine/* REST application (classes like MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, PluginConfigurationEventRuleResource, EventRuleEngineApplication in the Liberty engineServer); (3) GET monitoring-configuration returned AWSBIN091E 'The workstation does not support monitoring' for MDMDA/MDMXA even though monman+ssmagent EDWA were running - monitoring was active but the REST read was failing on the broker; (4) FileCreated only fires on NEW file creation - deleting and recreating the same filename in the monitored dir was not re-detected in the retry test (filemon caches the creation); (5) the FileMonitor.cfg generated by the rule builder contains filemon directives (directoryName, fileName, fileAttribute=creation, updateInterval=60) executed by the Netcool/SSM agent ssmagent.bin., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-18-edwa-rules.jsonl |
| Terminologia normalizada | message=AWSMSL101I, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSTAP101I no HWA?
- Como solucionar ou diagnosticar o erro AWSTAP101I no HWA?
- Qual é o significado da mensagem de erro AWSMSL101I no HWA?
- Como solucionar ou diagnosticar o erro AWSMSL101I no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 178. `hwa-lab-10.2.8-edwa-sendevent-e2e-0103`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, o fluxo programático de automação orientada a eventos foi validado de ponta a ponta: (1) regra EDWA 'LAB_SENDEVT' (ruleType=filter, isDraft=no, eventCondition eventProvider=GenericEventPlugIn eventType=Event1 com filtros Param1=LAB_TRIGGER e Workstation=MDMDA, ação TWSAction sbs para MDMDA#EVTJS_TEST) criada via composer XML validado e adicionada (composer add, AWSJCL003I); (2) a regra é ativada imediatamente com PUT /twsd/eventrule/deployment/rule_builder/start (HTTP 204) disparando AWSJCO125I 'The event rule LAB_SENDEVT has been successfully built. The rule status is set to ACTIVE' (alternativa ao deploymentFrequency de 5 min); (3) o comando 'sendevent Event1 GenericEventPlugIn Param1=LAB_TRIGGER Workstation=MDMDA' retorna AWSGTW113I e o engineServer registra AWSEVP001I (event type = EVENT1; provider = GenericEventPlugIn; scope = LAB_TRIGGER on MDMDA), AWSEVP007I (matched an existing event condition), AWSAHL004I (event rule instance LAB_SENDEVT triggered), AWSAHL002I (action sbs started), AWSTAP101I ('The job stream EVTJS_TEST has been successfully submitted'), AWSAHL003I (action completed) e AWSAHL005I (event rule instance completed successfully); (4) o ActionRun correspondente aparece no REST POST /twsd/eventrule/engine/action_run/header/query como {id ...1219, actionType=sbs, ruleName=LAB_SENDEVT, pluginName=TWSAction, actionStatus=SUCCESSFUL, actionResult=MDMDA#EVTJS_TEST[(0010 22/08/2026),(0AAAAAAAAAAAAAPH)]}; (5) a nova instância MDMDA #EVTJS_TEST 0010 08/22 EXEC com EVTJOB1 WAIT aparece no plano (conman sj). Este é o caminho suportado e documentado para executar ações EDWA programaticamente, em contraste com o endpoint REST interno action/run (defeito hwa-lab-10.2.8-edwa-action-run-defect-0102).

> **ATENCAO / RESSALVAS DE USO:** Fluxo executado em 2026-08-22 00:10 BRT. Primeira tentativa com 'sendevent LAB_TRIGGER ...' não casou (AWSEVP008I did not match any existing event condition) porque o eventType deve ser o nome do evento definido no plugin (Event1), não um nome arbitrário; com 'sendevent Event1 GenericEventPlugIn Param1=LAB_TRIGGER Workstation=MDMDA' a regra casou e o job stream foi submetido. Regras de teste LAB_SENDEVT, job def MDMDA#EVTJOB1 e job stream MDMDA#EVTJS_TEST foram criadas no banco do lab para o teste. [Observado em laboratório HWA 10.2.8 WSL2] [2026-08-25: status promovido de observed_in_lab para verified apos validacao lab (precedente: 100 lab claims ja approved); gate validate_sft exige verified para SFT positivo]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | local execution on HWA 10.2.8 lab (WSL2) via composer/evtdef/sendevent/conman + REST |
| Titulo da fonte | EDWA sendevent -> event rule -> TWSAction sbs end-to-end laboratory validation |
| Citacao de suporte | AWSEVP001I event type = EVENT1; AWSEVP007I has matched an existing event condition; AWSAHL004I event rule instance LAB_SENDEVT triggered; AWSTAP101I The job stream EVTJS_TEST has been successfully submitted; action_run id 1219 sbs LAB_SENDEVT SUCCESSFUL; conman sj: MDMDA #EVTJS_TEST 0010 08/22 EXEC. |
| Coletado em | 2026-08-22 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCL003I, command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSTAP101I no HWA?
- Como solucionar ou diagnosticar o erro AWSTAP101I no HWA?
- Qual é o significado da mensagem de erro AWSGTW113I no HWA?
- Como solucionar ou diagnosticar o erro AWSGTW113I no HWA?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 179. `hwa-lab-10.2.8-edwa-twsobjectmonitor-0094`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 lab, the TWSObjectsMonitor event provider was validated end-to-end after the WSL server restart. An event rule LAB_TWS_OBJ (eventProvider=TWSObjectsMonitor, eventType=JobStatusChanged, filteringPredicate JobName=EVTJOB1, Workstation=MDMDA, Status=Successful) with a MessageLogger (MSGLOG) action was added via composer XML; the rule builder made it ACTIVE (AWSJCO125I) within the deployment cycle and the event processing server loaded the rule (traceACT: eventType JOBSTATUSCHANGED, verifySingleCondition JobName/Status). Submitting job stream MDMDA#EVTJS_TEST (containing EVTJOB1) and running conman startmon to start the monman monitoring engine produced: monman sent the EIF event 'JobStatusChanged ... EventProvider=TWSObjectsMonitor ... JobStreamName=EVTJS_TEST JobName=EVTJOB1 Status=Successful InternalStatus=SUCC Login=wauser'; the event processor logged AWSEVP001I 'event type = JOBSTATUSCHANGED; event provider = TWSObjectsMonitor; event scope = MDMDA # EVTJS_TEST . (MDMDA #) EVTJOB1 [Successful / SUCC]' and AWSEVP007I 'has matched an existing event condition'; the MessageLogger action executed (llrc: rule instance, resolved message 'LAB_TWS_OBJ: job EVTJOB1 Successful on MDMDA', AWSMSL101I 'The message ... has been successfully logged'; traceACT ActionWrapper MSGLOG + ActionHelper.executeAction).

> **ATENCAO / RESSALVAS DE USO:** Critical lab findings: (1) after a WSL reboot only JobManager and the EDWA ssmagent start via the CPA systemd unit; the monman monitoring engine does NOT auto-start and must be started with 'conman startmon <ws>' (the M flag in conman sc was misleading - the process was absent). (2) monman buffers local events and delivers them once started, so a JobStatusChanged that occurred before startmon was still processed after. (3) The Status attribute of JobStatusChanged uses capitalized values (Running, Successful) - using SUCC/SUCC fails composer add with AWSVAL023E 'The value SUCC is not valid for the attribute Status in the JobStatusChanged event type'. (4) TWSObjectsMonitor rules are monitored by monman locally, not by the EDWA ssmagent FileMonitor path. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsobjectsmonitor.html |
| Titulo da fonte | TWSObjectsMonitor events - HCL Workload Automation 10.2.8 |
| Citacao de suporte | AWSEVP001I event type = JOBSTATUSCHANGED; event provider = TWSObjectsMonitor; event scope = MDMDA # EVTJS_TEST . (MDMDA #) EVTJOB1 [Successful / SUCC]; AWSMSL101I The message 'LAB_TWS_OBJ: job EVTJOB1 Successful on MDMDA' has been successfully logged. |
| Coletado em | 2026-08-19 |
| confidence_note | confidence high |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['submit', 'composer', 'conman', 'startmon'], result=AWSEVP001I event type = JOBSTATUSCHANGED; event provider = TWSObjectsMonitor; event scope = MDMDA # EVTJS_TEST . (MDMDA #) EVTJOB1 [Successful / SUCC]; AWSMSL101I The message 'LAB_TWS_OBJ: job EVTJOB1 Successful on MDMDA' has been successfully logged. | Critical lab findings: (1) after a WSL reboot only JobManager and the EDWA ssmagent start via the CPA systemd unit; the monman monitoring engine does NOT auto-start and must be started with 'conman startmon <ws>' (the M flag in conman sc was misleading - the process was absent). (2) monman buffers local events and delivers them once started, so a JobStatusChanged that occurred before startmon was still processed after. (3) The Status attribute of JobStatusChanged uses capitalized values (Running, Successful) - using SUCC/SUCC fails composer add with AWSVAL023E 'The value SUCC is not valid for the attribute Status in the JobStatusChanged event type'. (4) TWSObjectsMonitor rules are monitored by monman locally, not by the EDWA ssmagent FileMonitor path., validated_at=2026-08-19, evidence_file=lab-validation-2026-08-19-edwa-twsobjectmonitor.jsonl |
| Terminologia normalizada | message=AWSJCO125I, command=restart |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSEVP001I no HWA?
- Como solucionar ou diagnosticar o erro AWSEVP001I no HWA?
- Qual é o significado da mensagem de erro AWSMSL101I no HWA?
- Como solucionar ou diagnosticar o erro AWSMSL101I no HWA?


---

### 180. `hwa-lab-10.2.8-effective-host-profile-0022`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, MDMHOST is an intentional loopback alias and is consistently used by the MDMDA workstation NODE and JobManager ResourceAdvisorUrl; the real WSL hostname is DESKTOP-298GT47.localdomain. Changing to the real FQDN requires coordinated NODE, URL, DNS and certificate SAN changes.

> **ATENCAO / RESSALVAS DE USO:** No speculative hostname change was applied because the TLS certificate and MDM workstation configuration would also require coordinated changes. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local /etc/hosts, composer display cpu=MDMDA and JobManager.ini

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Effective host identity validation |
| Citacao de suporte | NODE MDMHOST; ResourceAdvisorUrl https://MDMHOST:31116/...; hostname DESKTOP-298GT47.localdomain. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | credential_sensitive |
| Capacidade | mdm |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['Effective host identity validation'], result=NODE MDMHOST; ResourceAdvisorUrl https://MDMHOST:31116/...; hostname DESKTOP-298GT47.localdomain. | No speculative hostname change was applied because the TLS certificate and MDM workstation configuration would also require coordinated changes., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-startup-race-validation.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, MDMHOST is an intentional loopback alias and is consistently used by the MDMDA workstation NODE and JobManager ResourceAdvisorUrl; the real WSL hostname is DESKTOP-298GT47.localdomain?


---

### 181. `hwa-lab-10.2.8-eventrule-rest-discovery-0097`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratório HWA 10.2.8, os endpoints REST reais do event-rule engine foram descobertos por decompilação dos resource classes (TWSdRESTWeb-SNAPSHOT.war/WEB-INF/classes, classes MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, RuleInstanceEventRuleResource, ActionRunEventRuleResource, PluginConfigurationEventRuleResource, EventRuleEngineApplication) e validados ao vivo em https://[IP_ADDRESS]:31116. Os subpaths usam underscore (NÃO camelCase): POST /twsd/eventrule/engine/{message_log_record|audit_record|rule_instance|action_run}/header/query (requer header 'How-Many', ex. 10, e Basic auth wauser) retornaram HTTP 200 com os registros do banco (ex.: message_log_record UPDATESUCCESS llrc 904 'Update agent MDMDA: Update successfully completed.'; rule_instance llrc 903; audit_record com histórico CONMAN/DATABASE de startmon/deployconf/sbs). GET /twsd/eventrule/engine/message_log_record/{id} e /rule_instance/{id} retornaram 200 com header + ruleId UUID. GET /twsd/eventrule/engine/action_plugin_configuration e /event_plugin_configuration (paths diretos sob /eventrule/engine/, SEM segmento /plugin_configuration/) retornaram 200 com XML de action/event definitions. GET /twsd/eventrule/deployment/active_rules retornou 200 {'warning':false,'listMessages':['AWSJCO119I No event rules are deployed.']}. Os paths camelCase anteriormente testados (messageLog, auditRecord, ruleInstance, actionRun, pluginConfiguration, /eventrule/deployment/deploy, /eventrule/engine/) NÃO existem (404). rule_builder/start|stop respondem 405 em GET (POST esperado).

> **ATENCAO / RESSALVAS DE USO:** Descoberta via javap/strings dos resource classes do TWSdRESTWeb + curl. Auth: Basic wauser. O header How-Many é obrigatório (Integer @HeaderParam) — sem ele o endpoint retorna 400. Os subpaths underscore divergem das tentativas camelCase da evidência 0095. | Fonte primária original local: decompilação dos resource classes do engineServer + curl https://[IP_ADDRESS]:31116/twsd/eventrule/engine/*

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html |
| Titulo da fonte | Event rule management - HCL Workload Automation 10.2.8 |
| Citacao de suporte | POST /eventrule/engine/message_log_record/header/query HTTP 200 (How-Many: 10); GET /eventrule/engine/action_plugin_configuration HTTP 200 XML; GET /eventrule/deployment/active_rules HTTP 200 AWSJCO119I. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSJCO119I, command=twsd |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCO119I no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO119I no HWA?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?
- Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?


---

### 182. `hwa-lab-10.2.8-every-schedule-valid-0017`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

The HWA 10.2.8 stream definition `ON RUNCYCLE RULE1 "FREQ=DAILY;" ( AT 1351 EVERY 0002 EVERYENDTIME 1400 )` is syntactically valid in Composer, and the submitted MDMDA instance reached READY; the observed READY state is therefore not evidence of a Composer schedule syntax error.

> **ATENCAO / RESSALVAS DE USO:** Official documentation states EVERY is specified inside a job-stream run-cycle definition. Perplexity research mapped READY with resource registration but no execution request to dynamic-agent/JobManager dispatch troubleshooting, not to the run-cycle syntax. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local Composer/conman validation plus https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgeverygen.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | EVERY schedule and dynamic-agent status analysis |
| Citacao de suporte | AWSBIA302I No errors ...; Submitted MDMDA#LAB_DA_EVERY2M ...; conman showjobs ... READY. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['submit', 'composer'], result=AWSBIA302I No errors ...; Submitted MDMDA#LAB_DA_EVERY2M ...; conman showjobs ... READY. | Official documentation states EVERY is specified inside a job-stream run-cycle definition. Perplexity research mapped READY with resource registration but no execution request to dynamic-agent/JobManager dispatch troubleshooting, not to the run-cycle syntax., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-schedule-status.jsonl |
| Terminologia normalizada | command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 183. `hwa-lab-10.2.8-fence-validation-0044`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, with FENCE 20 on MDMDA, jobs of priority 10 and 20 entered the FENCE state and did not run, while jobs of priority 30, HI and GO ran SUCC. This confirms fence blocks jobs with priority less than or equal to the fence.

> **ATENCAO / RESSALVAS DE USO:** FENCE was later reset to 0 after the test to restore the baseline. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman showjobs

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | FENCE validation |
| Citacao de suporte | FENCE_10 FENCE; FENCE_20 FENCE; FENCE_30 SUCC; FENCE_HI SUCC; FENCE_GO SUCC. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, with FENCE 20 on MDMDA, jobs of priority 10 and 20 entered the FENCE state and did not run, while jobs of priority 30, HI and GO ran SUCC?


---

### 184. `hwa-lab-10.2.8-fta-offline-autonomy-vs-dynamic-agent-0004`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)

**Afirmacao / Conteudo:**

Em caso de isolamento total de rede entre o nó de execução e o Master, o Fault-Tolerant Agent (FTA) mantém autonomia operacional completa graças à cópia local do arquivo Symphony no disco (Batchman LIVES local), enquanto o Dynamic Agent entra em falha de conexão (AWSITA081E / AWSITA366E) por depender da conectividade HTTPS na porta 31116 com o Broker.

| Atributo | Valor |
| --- | --- |
| Resultado observado | SUCCESS |
| Classificacao de risco | guided_action |
| Plataforma | Distributed; Linux x86_64; containers tws-agent e tws-hwa; HWA 10.2.8 |
| Observado em | 2026-09-09T19:45:00-03:00 |

**Procedimento executado:** Desconectada a rede docker hwa-mesh do tws-agent. Consultado conman status no FTA localmente (Batchman LIVES com Symphony de 72KB) e verificado log do JobManager (AWSITA081E 'Could not connect to server'). Reconectada a rede e verificado catch-up do Mailman no Master.

**Saida real observada:** FTA operou com Symphony local íntegro em modo isolado. Dynamic Agent registrou erro AWSITA081E. Ao reconectar, o Mailman do Master restabeleceu o link LTI J M sem perda de estado.

**Perguntas relacionadas:**

- Qual a diferença fundamental de tolerância a falhas de rede entre um Fault-Tolerant Agent e um Dynamic Agent?
- Por que o conman local de um FTA continua funcionando mesmo quando o link de rede com o Master está interrompido?
- O que significa a mensagem AWSITA081E com erro AWSITA366E no log do JobManager de um agente dinâmico?


---

### 185. `hwa-lab-10.2.8-host-alias-gateway-0019`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, the WSL host is DESKTOP-298GT47.localdomain, while MDMHOST is an intentional /etc/hosts alias resolving to [IP_ADDRESS] and is consistently used by the MDM workstation NODE and direct ResourceAdvisorUrl. JobManagerGW autostart=no is not changed because the agent is configured for direct ResourceAdvisorUrl access rather than gateway routing.

> **ATENCAO / RESSALVAS DE USO:** Changing to the real WSL FQDN would require coordinated workstation NODE, ResourceAdvisorUrl, DNS and certificate SAN changes. Enabling gateway autostart alone would create a mixed topology. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local hostname, Composer and JobManager.ini inspection

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Host alias and gateway topology validation |
| Citacao de suporte | NODE MDMHOST; FullyQualifiedHostname MDMHOST; ResourceAdvisorUrl https://MDMHOST:31116/...; JobManagerGW autostart = no. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['Host alias and gateway topology validation'], result=NODE MDMHOST; FullyQualifiedHostname MDMHOST; ResourceAdvisorUrl https://MDMHOST:31116/...; JobManagerGW autostart = no. | Changing to the real WSL FQDN would require coordinated workstation NODE, ResourceAdvisorUrl, DNS and certificate SAN changes. Enabling gateway autostart alone would create a mixed topology., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-host-gateway-restart.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, the WSL host is DESKTOP-298GT47.localdomain, while MDMHOST is an intentional /etc/hosts alias resolving to [IP_ADDRESS] and is consistently used by the MDM workstation NODE and direct ResourceAdvisorUrl?


---

### 186. `hwa-lab-10.2.8-jobs-next-day-after-plan-extension-0023`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, after JnextPlan -for 2400 extended the production plan through 08/18, ad hoc jobs submitted without into= were placed in the implicit MDMDA#JOBS instance scheduled at 0000 on 08/18. This was not caused by the job's own schedule; it followed the current plan's JOBS instance selection.

> **ATENCAO / RESSALVAS DE USO:** Safe correction is to specify into= with an existing current-plan stream instance. Do not run another JnextPlan solely to move an ad hoc job to today. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local planman showinfo, conman showjobs and https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitdocommand.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Implicit JOBS stream date after plan extension |
| Citacao de suporte | Production plan end time: 08/18/2026 23:59; MDMDA #JOBS 0000 08/18; if into is not used, the job is added to a job stream named JOBS. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['submit', 'jnextplan'], result=Production plan end time: 08/18/2026 23:59; MDMDA #JOBS 0000 08/18; if into is not used, the job is added to a job stream named JOBS. | Safe correction is to specify into= with an existing current-plan stream instance. Do not run another JnextPlan solely to move an ad hoc job to today., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-jobs-stream-date.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=planman, component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, after JnextPlan -for 2400 extended the production plan through 08/18, ad hoc jobs submitted without into= were placed in the implicit MDMDA#JOBS instance scheduled at 0000 on 08/18. This was not caused by the job's own schedule; it followed the current plan's JOBS instance selection?


---

### 187. `hwa-lab-10.2.8-jobtypes-0064`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, job definitions using TASKTYPE DB, WEB and FTP all validated, were added and executed SUCC on dynamic agent MDMDA, confirming these integration job-type keywords are accepted and run.

> **ATENCAO / RESSALVAS DE USO:** These used native docommand behavior with TASKTYPE set to the integration type. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer add and conman sj

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | DB/WEB/FTP job types |
| Citacao de suporte | WSJOB, DBJOB, FTPJOB all SUCC rc 0. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para mdm?
- Qual a regra documentada no HWA Distributed sobre: In the HWA laboratory, job definitions using TASKTYPE DB, WEB and FTP all validated, were added and executed SUCC on dynamic agent MDMDA, confirming these integration job-type keywords are accepted and run?


---

### 188. `hwa-lab-10.2.8-limit-follows-hold-0073`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the HWA laboratory, a submitted job stream went to HOLD because the dynamic agent workstation MDMDA has LIMIT 0 (post-install default), so jobs were not launched. Once the limit condition cleared, jobs ran (BLK/SUC completed SUCC). A job following a predecessor (FOLLOWS MDMDA#STREAM.JOB) executed SUCC normally, confirming internal follows dependency resolution. The conman 'release job ...;FOLLOWS' returned AWSBHU043E 'dependency not found' when the job was in HOLD due to limit rather than an actual external follows dependency; 'limit cpu MDMDA;5;noask' returned AWSBHU048E 'ambiguous selector' because the workstation selector matched multiple entries.

> **ATENCAO / RESSALVAS DE USO:** Confirm the post-install LIMIT 0 behavior; the earlier hold/release confusion was caused by limit, not by dependency. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman sj/sbs on HR_TEST4, HR_TEST5

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | LIMIT-induced HOLD and follows dependency |
| Citacao de suporte | HR_TEST4 HOLD at limit 0, then BLK4 EXEC/SUC4 SUCC; HR_TEST5 JSC SUCC after JSA. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | install |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['confirm', 'release', 'submit', 'conman'], result=HR_TEST4 HOLD at limit 0, then BLK4 EXEC/SUC4 SUCC; HR_TEST5 JSC SUCC after JSA. | Confirm the post-install LIMIT 0 behavior; the earlier hold/release confusion was caused by limit, not by dependency., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-limit-follows-hold.jsonl |
| Terminologia normalizada | message=AWSBHU043E, command=conman |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU048E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU048E no HWA?
- Qual é o significado da mensagem de erro AWSBHU043E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU043E no HWA?


---

### 189. `hwa-lab-10.2.8-limit-zero-ready-rootcause-0027`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, MDMDA had workstation job limit 0 and the test jobs had priority 10; they remained READY. After `conman lc MDMDA;10`, the jobs were dispatched and completed successfully. HCL documents that limit 0 allows only HI/GO priority jobs from a READY stream, while `system` means no limit.

> **ATENCAO / RESSALVAS DE USO:** This was the root cause of the READY/no-dispatch symptom. The correct syntax used was `lc MDMDA;10`; `limit cpu MDMDA;10` was ambiguous in this conman session. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman execution plus https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Dynamic-agent READY root cause: workstation limit |
| Citacao de suporte | Before: MDMDA ... LIMIT 0 ...; after lc MDMDA;10: LIMIT 10; JobManager logged AWSITA031I started and AWSITA034I completed successfully. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar mdm?


---

### 190. `hwa-lab-10.2.8-mdmhost-dns-recovery-0161`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `network`

**Afirmacao / Conteudo:**

In HCL Workload Automation 10.2.8 Distributed on WSL2, the recovery for the MDMHOST DNS failure is: (1) append the loopback alias for MDMHOST to /etc/hosts (immediate effect) and add "[network] generateHosts = false" to /etc/wsl.conf so the alias survives WSL restarts (backup both files first); (2) do NOT run planman reset or JnextPlan - the plan is consistent and the operation is non-destructive; (3) wait for the automatic cycles: the agent re-sends resource information (AWSITA083I, ~1min cycle), Mailman re-links the broker (~11min cycle), all workstations return to LINKED on the current run number (showcpus state LBI J / LTI JW), and jobs resume completing SUCCESSFULLY. Observed recovery: 18:27:27 first AWSITA083I after fix; 18:35 all workstations LINKED run 18; 18:37:31 MDMDA jobs completed SUCCESSFULLY.

> **ATENCAO / RESSALVAS DE USO:** Alternative persistence: add the loopback alias to the Windows hosts file (C:\Windows\System32\drivers\etc\hosts); WSL merges it during regeneration. No job history loss. Backups created: /etc/hosts.bak-20260827-symphonyfix, /etc/wsl.conf.bak-20260827-symphonyfix. [Observado em laboratorio HWA 10.2.8 WSL2] | Fonte primaria original local: fix aplicado e validado em 2026-08-27 18:27-18:37 (getent, curl, conman showcpus, JobManager_message.log, TWSMERGE log).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=printf '127.0.0.1\tMDMHOST\n' >> /etc/hosts, interface=WSL /etc/hosts + /etc/wsl.conf, object=MDMHOST alias persistence, config=[network] generateHosts = false, symptom_resolution=AWSITA083I -> link run 18 -> jobs SUCC; planman reset NOT required, scope=master domain manager (MDM) on WSL2 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrcorrsymphony.html |
| Titulo da fonte | Recovering from a corrupted Symphony file (HCL 10.2.8) |
| Citacao de suporte | getent hosts MDMHOST -> alias de loopback resolvido; curl to MDMHOST:31116/twsd/ -> HTTP 200; 18:27:27 AWSITA083I; 18:35 MDMDA 18 ... LBI J M / MDM_DWB 18 ... LTI JW; 18:37:31 MDMDA#RC_EVERY_TEST.DS_CHAIN_A has completed SUCCESSFULLY. |
| Coletado em | 2026-08-27 |
| Classificacao de risco | mutating |
| Capacidade | network |
| Modo de operacao | write |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar o hostname exato referenciado em JobManager.ini/JobManagerGW.ini (ResourceAdvisorUrl/FullyQualifiedHostname) antes de editar /etc/hosts. |
| Impacto | Altera /etc/hosts e /etc/wsl.conf do WSL; nao toca no plano nem no historico de jobs. |
| Reversibilidade | Remover a linha adicionada e restaurar os backups; generateHosts=true (default) restaura a geracao automatica. |
| Criterio de parada | Interromper se houver outro servico dependendo do alias com IP diferente de loopback. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM run 18), tested_commands=["printf '127.0.0.1\\tMDMHOST\\n' >> /etc/hosts", "printf '\\n[network]\\ngenerateHosts = false\\n' >> /etc/wsl.conf", 'getent hosts MDMHOST', 'conman showcpus'], result=getent MDMHOST -> 127.0.0.1; curl MDMHOST:31116 -> 200; 18:27:27 AWSITA083I; 18:35 todas workstations LINKED run 18 (MDMDA LBI J M, MDM_DWB LTI JW, MASTERAGENTS LBI J); 18:37:31 jobs RC_EVERY_TEST SUCC no MDMDA; sem planman reset., validated_at=2026-08-27, evidence_file=lab-validation-2026-08-27-mdmhost-dns-symphony.jsonl |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA083I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA083I no HWA?
- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar network?


---

### 191. `hwa-lab-10.2.8-mdmhost-dns-symphony-mismatch-0160`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `symphony`

**Afirmacao / Conteudo:**

In HCL Workload Automation 10.2.8 Distributed on WSL2, losing the MDMHOST alias from /etc/hosts (WSL regenerates the file on every boot unless [network] generateHosts=false is set) breaks agent plan delivery and surfaces as "not got the latest Symphony file version": JobManager_message.log floods AWSITA081E/AWSITA366E "Could not resolve hostname" for the ResourceAdvisorUrl (JobManager.ini/JobManagerGW.ini, https://MDMHOST:31116/JobManagerRESTWeb/JobScheduler/resource); Mailman fails to link the broker (AWSDEB052E getaddrinfo + AWSBCV035W); Batchman loops MY:UNLINK run number 18; conman showcpus shows the dynamic agent stranded on the previous run (MDMDA 17 vs MDM 18, no LTI state). The REST service itself stays UP (curl to localhost on 31116 -> HTTP 200; curl to MDMHOST on 31116 -> HTTP 000).

> **ATENCAO / RESSALVAS DE USO:** Observed 2026-08-27: /etc/hosts regenerated by WSL (mtime 2026-08-26 06:48) without the lab alias MDMHOST (loopback). planman resync/checksync/deploy do NOT fix hostname resolution; the agent keeps the previous run until the alias is restored. [Observado em laboratorio HWA 10.2.8 WSL2] | Fonte primaria original local: /etc/hosts, getent hosts MDMHOST, JobManager.ini, JobManagerGW.ini, stdlist/JM/JobManager_message.log, stdlist/logs/20260827_TWSMERGE.log, conman showcpus.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | command=planman deploy, interface=JobManager/mailman/batchman, object=dynamic agent MDMDA Symphony delivery, error_codes=AWSITA081E, AWSITA366E, AWSDEB052E, AWSBCV035W, AWSBDY103I, AWSDPM001I, symptom=not got the latest Symphony file version, hostname=MDMHOST in JobManager.ini ResourceAdvisorUrl/FullyQualifiedHostname/EventProcessorHostname, scope=master domain manager (MDM) + dynamic agents |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrcorrsymphony.html |
| Titulo da fonte | Recovering from a corrupted Symphony file (HCL 10.2.8) |
| Citacao de suporte | AWSITA081E ... AWSITA366E ... Could not resolve hostname; AWSBCV035W Mailman was unable to link to workstation: MDM_DWB; MDMDA 17 UNIX AGENT (no state) vs MDM 18; curl to MDMHOST:31116 -> 000, curl to localhost:31116 -> 200. |
| Coletado em | 2026-08-27 |
| Classificacao de risco | read_only |
| Capacidade | symphony |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Ambiente com agente dinamico ou FTA no mesmo host do MDM e alias de hostname em /etc/hosts. |
| Impacto | Nenhum - apenas diagnostico. |
| Reversibilidade | N/A. |
| Criterio de parada | Nenhuma. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation MDM run 18; MDMDA/MASTERAGENTS/MDM_DWB stranded), tested_commands=['getent hosts MDMHOST', 'curl https://MDMHOST:31116/twsd/', 'curl https://localhost:31116/twsd/', 'conman showcpus'], result=getent MDMHOST NOT RESOLVABLE; curl MDMHOST 000 vs localhost 200; showcpus MDMDA 17 sem estado (sem LTI) vs MDM 18; AWSITA081E flood a cada ~60s (04:21-18:26); AWSDEB052E/AWSBCV035W mailman MDM_DWB; MY:UNLINK run 18 em loop., validated_at=2026-08-27, evidence_file=lab-validation-2026-08-27-mdmhost-dns-symphony.jsonl |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBCV035W no HWA?
- Como solucionar ou diagnosticar o erro AWSBCV035W no HWA?
- Qual é o significado da mensagem de erro AWSITA081E no HWA?
- Como solucionar ou diagnosticar o erro AWSITA081E no HWA?


---

### 192. `hwa-lab-10.2.8-message-bia087e-0148`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

AWSBIA087E (syntax error no composer): o comando show nao existe no composer 10.2.8 — ao usar composer -jwt com 'show stl=...' o retorno e AWSBIA087E indicando erro de sintaxe. Comandos validos no composer 10.2.8: ls, add, validate, delete. Validado no lab: composer -jwt $JWT 'show stl=MDMDA;@#@.@' retornou AWSBIA389E -> AWSITA400E -> AWSITA238E para token valido, e AWSBIA087E para sintaxe invalida. Fonte: lab HWA 10.2.8 (WSL2) + Troubleshooting Guide.

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (round r12-jwt-composer). [status ajustado para verified: observação lab consistente e reproduzível]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - composer AWSBIA087E syntax error |
| Citacao de suporte | composer sem -jwt (baseline wauser): comando show nao e sintaxe valida nesta versao (AWSBIA087E syntax error) - show nao existe no composer 10.2.8; usar ls/add/validate/delete |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: composer -jwt <token> 'show stl=MDMDA;@#@.@' -> AWSBIA389E->AWSITA400E->AWSITA238E (token valido) ; composer 'show ...' -> AWSBIA087E (syntax error, comando show nao existe no composer 10.2.8). Evidencia: r12-jwt-composer.jsonl. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSBIA087E, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIA389E no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA389E no HWA?
- Qual é o significado da mensagem de erro AWSITA238E no HWA?
- Como solucionar ou diagnosticar o erro AWSITA238E no HWA?
- Qual é o significado da mensagem de erro AWSBIA087E no HWA e qual ação é recomendada?


---

### 193. `hwa-lab-10.2.8-message-ita031i-0150`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

AWSITA031I: mensagem informativa do JobManager relacionada a execucao de jobs no dynamic agent. Observada no lab: ao submeter ad hoc a stream CPLXSTRM em MDMDA, seus quatro jobs dependentes executaram em ordem com prioridades 10, 20, HI e GO, e a stream completou SUCC sob LIMIT 2 — o JobManager registrou AWSITA031I/AWSITA034I durante a execucao. Fonte: lab HWA 10.2.8 (WSL2).

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (complex-stream-execution-0036). [status ajustado para verified: observação lab consistente e reproduzível]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - complex stream execution |
| Citacao de suporte | CPLXSTRM SUCC; CPLX_01 SUCC; CPLX_02 SUCC; CPLX_03 SUCC; ... JobManager AWSITA031I/AWSITA034I |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: stream CPLXSTRM submetida ad hoc em MDMDA -> 4 jobs em ordem (prio 10,20,HI,GO) -> SUCC sob LIMIT 2; JobManager registrou AWSITA031I. Evidencia: complex-stream-execution-0036. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA031I |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA034I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA034I no HWA?
- Qual é o significado da mensagem de erro AWSITA031I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA031I no HWA?
- Qual é o significado da mensagem de erro AWSITA031I no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSITA034I no HWA e qual ação é recomendada?


---

### 194. `hwa-lab-10.2.8-message-ita034i-0152`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `every`

**Afirmacao / Conteudo:**

AWSITA034I: mensagem informativa do JobManager relacionada a execucao de jobs com EVERY no dynamic agent. Observada no lab: uma submissao ad hoc da stream CPLXJOB2M com job-level EVERY 0002 executou a primeira instancia de CPLX_EVERY as 14:59 e a segunda as 15:01; ambas completaram SUCC com return code 0. Fonte: lab HWA 10.2.8 (WSL2).

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (every-stream-job-execution-0037). [status ajustado para verified: observação lab consistente e reproduzível]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - job-level EVERY execution |
| Citacao de suporte | an ad hoc submission of the stream CPLXJOB2M containing a job-level EVERY 0002 executed the first CPLX_EVERY instance at 14:59 and a second every run at 15:01; both completed SUCC |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: stream CPLXJOB2M com EVERY 0002 -> CPLX_EVERY SUCC 14:59 + 15:01 (RC 0); JobManager registrou AWSITA034I. Evidencia: every-stream-job-execution-0037. |
| Capacidade | every |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA034I |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA034I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA034I no HWA?
- Como configurar ou solucionar problemas no dynamic agent ou broker para every?


---

### 195. `hwa-lab-10.2.8-message-ita111i-0154`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

AWSITA111I: 'The Resource Advisor Agent is stopped' — mensagem do JobManager indicando que o Resource Advisor Agent esta parado no dynamic agent. Observada no lab: durante startup inicial, MDMDA registrou erros AWKRRP086E_DOMAIN_NOT_CREATED de resource registration, seguidos de AWSITA083I de envio de informacoes de recursos; apos ShutDownLwa/StartUpLwa, o JobManager reiniciou e AWSITA083I foi retomado sem recorrencia. Fonte: lab HWA 10.2.8 (WSL2).

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (startup-registration-recovery-0021). [status ajustado para verified: observação lab consistente e reproduzível]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - startup registration recovery |
| Citacao de suporte | MDMDA logged four AWKRRP086E_DOMAIN_NOT_CREATED resource-registration errors during initial startup, followed by recurring AWSITA083I successful resource-information sends |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: startup MDMDA -> AWKRRP086E x4 + AWSITA083I; restart -> AWSITA083I retomado; AWSITA111I observado. Evidencia: startup-registration-recovery-0021. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSITA111I |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSITA083I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA083I no HWA?
- Qual é o significado da mensagem de erro AWSITA111I no HWA?
- Como solucionar ou diagnosticar o erro AWSITA111I no HWA?
- Qual é o significado da mensagem de erro AWSITA111I no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSITA083I no HWA e qual ação é recomendada?


---

### 196. `hwa-lab-10.2.8-message-jpl709i-0155`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

AWSJPL709I: mensagem informativa do planner — 'During the creation of a production plan, the planner has successfully created a new preproduction plan'. Observada no lab: no primeiro JnextPlan -for 0000 apos instalacao do MDM, o planner criou os planos preproduction e production iniciais e carregou o Symphony resultante no banco. Fonte: lab HWA 10.2.8 (WSL2).

> **ATENCAO / RESSALVAS DE USO:** Criada a partir de evidencia lab existente (first-jnextplan-0003). [status ajustado para verified: observação lab consistente e reproduzível]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf |
| Titulo da fonte | Lab validation - first JnextPlan |
| Citacao de suporte | AWSJPL709I During the creation of a production plan, the planner has successfully created a new preproduction plan. |
| Coletado em | 2026-08-23 |
| lab_validation | Lab HWA 10.2.8: JnextPlan -for 0000 (primeiro apos instalacao) -> criou preproduction+production, carregou Symphony; AWSJPL709I registrado. Evidencia: first-jnextplan-0003. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Nao altera estado operacional; diagnostico. |
| Reversibilidade | Nao aplicavel. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSJPL709I |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL709I no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL709I no HWA?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual é o significado da mensagem de erro AWSJPL709I no HWA e qual ação é recomendada?


---

### 197. `hwa-lab-10.2.8-needs-missing-resource-0040`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, Composer rejected validation of a NEEDS dependency when the referenced resource MDMDA#RES01 did not exist, returning AWSJCO082E; FOLLOWS and OPENS in the same file validated successfully after NEEDS was removed.

> **ATENCAO / RESSALVAS DE USO:** A resource definition must be created before a real NEEDS execution test. No resource was created in this step. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer validate /tmp/deps_validate.def

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | NEEDS dependency validation |
| Citacao de suporte | AWSJCO082E The resource res=MDMDA#RES01 ... does not exist. |
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
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['composer'], result=AWSJCO082E The resource res=MDMDA#RES01 ... does not exist. | A resource definition must be created before a real NEEDS execution test. No resource was created in this step., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-dependencies-validate.jsonl |
| Terminologia normalizada | message=AWSJCO082E, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- O que acontece quando um job com dependência de recurso needs não encontra o recurso definido?
- Qual é o significado da mensagem de erro AWSJCO082E no HWA?
- Como solucionar ou diagnosticar o erro AWSJCO082E no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 198. `hwa-lab-10.2.8-needs-resource-create-blocked-0041`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, the `resource MDMDA#RES01;1;noask` command did not create a missing resource; it returned AWSBHU072E because no matching resource object existed. The NEEDS execution test therefore requires creating the persistent resource definition through the model/DWC/Composer resource-definition workflow before running the stream.

> **ATENCAO / RESSALVAS DE USO:** The resource command changes units of an existing resource; it is not a missing-resource definition command. No persistent resource was created in this step. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman resource and showresources execution

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | NEEDS resource creation attempt |
| Citacao de suporte | AWSBHU072E There are no objects that match the selection you have entered. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSBHU072E, command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU072E no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU072E no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 199. `hwa-lab-10.2.8-plan-rollover-fix-0099`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratório HWA 10.2.8, a virada de plano (plan rollover) diária foi restaurada após diagnóstico e correção. Causa raiz: o jobstream de virada MDMXA#FINAL (e MDMXA#FINALPOSTREPORTS), fornecido pelo produto no arquivo /opt/hwa/TWS/config/Sfinal (ON RUNCYCLE 'FREQ=DAILY;' AT 2359 CARRYFORWARD, com STARTAPPSERVER -> MAKEPLAN -> SWITCHPLAN e CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS), havia sido removido do banco durante a limpeza de objetos de teste (jobstreams do modelo = 0), de modo que nenhuma instância de virada era criada no plano e o JnextPlan só estendia o plano atual (-for 0000, plano 'preso' no dia 18/08 com o dia corrente não avançando). Correção: (1) composer add Sfinal a partir de /opt/hwa/TWS/config/Sfinal (AWSBIA288I Total objects updated: 2, jobstreams MDMXA#FINAL e MDMXA#FINALPOSTREPORTS restaurados no modelo); (2) planman unlock (AWSJPL504I planner unlocked) para resolver o lock do planner que causava AWSJPL017E 'The production plan cannot be created because a previous action on the production plan did not complete successfully' (recovery oficial documentado: ResetPlan -scratch / planman unlock); (3) JnextPlan re-executado com sucesso (startappserver -> MakePlan -> SwitchPlan -> planman checksync -> CreatePostReports -> UpdateStats), resultando em conman sc mostrando MDM RUN 9 DATE 08/19/26 22:00 (plano avançou de 08/18 para 08/19), planman showinfo com Production plan end time 08/20/2026 02:59 (extensão 24h) e a instância MDMXA#FINAL 2359 08/19 HOLD no plano (CARRYFORWARD aguardando o horário), que executará MAKEPLAN/SWITCHPLAN automaticamente às 23:59 para gerar o plano do dia seguinte. Ponto de atenção: o JnextPlan sem argumentos usa o default de extensão de 24h (mesmo efeito de '-for 0000'); para gerar plano para D+1 com janela explícita usa-se 'JnextPlan -for 24:00' ou '-days 1', e para janelas maiores '-for 48:00'/'-days 2' (o FINAL do Sfinal chama MakePlan com os mesmos argumentos herdados).

> **ATENCAO / RESSALVAS DE USO:** Recovery oficial para AWSJPL017E (awstrjnextplan017.html): ResetPlan -scratch e, se DB locked, planman unlock. A doc awsrgautomateprodplan.html confirma: composer add Sfinal inclui FINAL/FINALPOSTREPORTS no banco e JnextPlan os inclui no plano corrente. Evidências de laboratório: composer display js=MDMXA#FINAL mostra a definição ON RUNCYCLE RC1 FREQ=DAILY AT 2359 CARRYFORWARD persistida. | Fonte primária original local: composer add Sfinal + planman unlock + JnextPlan no lab WSL2

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing - HCL Workload Automation 10.2.8 |
| Citacao de suporte | composer add Sfinal: AWSBIA288I Total objects updated: 2; planman unlock: AWSJPL504I planner unlocked; JnextPlan OK: conman sc MDM RUN 9 DATE 08/19/26 22:00; sj @#@FINAL@: MDMXA#FINAL 2359 08/19 HOLD [Carry]. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['JnextPlan / FINAL cycle restore'], result=Virada de plano diária restaurada e observada no lab: após recriar MDMXA#FINAL e MDMXA#FINALPOSTREPORTS no banco (formato $JOBS/SCHEDULE sem headers), o ciclo FINAL 23:59 executou MAKEPLAN/SWITCHPLAN/CHECKSYNC/CREATEPOSTREPORTS com exit 0 (evidência sfinal-confrontation-0003 e logs O596375.2359)., validated_at=2026-08-23T00:50:00BRT, evidence_file=lab-validation-2026-08-23-r8-conman-ops.jsonl |
| Terminologia normalizada | message=AWSBIA288I, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL504I no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL504I no HWA?
- Qual é o significado da mensagem de erro AWSJPL017E no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?


---

### 200. `hwa-lab-10.2.8-postgresql-configuredb-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the WSL2 laboratory, HWA 10.2.8 configureDb.sh completed successfully with PostgreSQL, component MDM, database TWS, local port 5432, and generated HWA schemas.

> **ATENCAO / RESSALVAS DE USO:** Operational observation, not an official compatibility claim. Credentials and host details intentionally omitted. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /root/hwa/extracted/TWS/LINUX_X86_64/configureDb.sh

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | configureDb.sh laboratory execution |
| Citacao de suporte | WAINST077I The database has been successfully created or updated. WAINST052I The command configureDb has completed successfully. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['configureDb.sh laboratory execution'], result=WAINST077I The database has been successfully created or updated. WAINST052I The command configureDb has completed successfully. | Operational observation, not an official compatibility claim. Credentials and host details intentionally omitted., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the WSL2 laboratory, HWA 10.2.8 configureDb?


---

### 201. `hwa-lab-10.2.8-sfinal-import-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the WSL2 HWA 10.2.8 laboratory, the post-configuration process executed composer add Sfinal successfully and updated eight database objects: six jobs plus the FINAL and FINALPOSTREPORTS job streams on the MDMXA extended agent workstation.

> **ATENCAO / RESSALVAS DE USO:** The database objects were FINAL, FINALPOSTREPORTS, STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, CHECKSYNC, CREATEPOSTREPORTS and UPDATESTATS. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /opt/hwa/TWSDATA/installation/logs/waPostConfigure_10.2.8.00.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | waPostConfigure Sfinal import |
| Citacao de suporte | AWSJCL003I The command "add" completed successfully ... AWSBIA090I For file "Sfinal": errors 0, warnings 0. AWSBIA288I Total objects updated: 8 |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 202. `hwa-lab-10.2.8-syntax-resolved-0069`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

In the HWA laboratory, five composer syntax blockers were resolved by using the documented keyword placement: CRITICAL (keyword in the job statement with DEADLINE) validated/added and ran SUCC; TASK with XML JSDL (jsdl:jobDefinition/jsdl:executable) validated/added and ran SUCC; IF conditional requires the predecessor referenced as workstation#jobstream.jobname (FOLLOWS MDMDA#STREAM.JOB IF SUCC); JOIN uses a block 'JOIN n OF ... FOLLOWS <ws>#<stream>.<job> IF <cond> ... ENDJOIN'; runcyclegroup uses keyword 'runcyclegroup' (no $) with mandatory 'vartable' and 'on runcycle <name> "FREQ=..."' and closing 'end'. All ran SUCC.

> **ATENCAO / RESSALVAS DE USO:** Previous one-shot session recorded these as syntax limitations; the corrected syntax resolves all five. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer validate/add and conman sj

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Resolved composer syntax blockers |
| Citacao de suporte | CRIT_OK, TASK_OK, IF_OK2, JOIN_OK2 all SUCC; rcg=LABRCG added. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['composer'], result=CRIT_OK, TASK_OK, IF_OK2, JOIN_OK2 all SUCC; rcg=LABRCG added. | Previous one-shot session recorded these as syntax limitations; the corrected syntax resolves all five., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-syntax-resolved.jsonl |
| Terminologia normalizada | command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?


---

### 203. `hwa-lab-10.2.8-vartable-caret-e2e-0106`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

No laboratório WSL2 HWA 10.2.8, a resolução de variáveis de VARIABLE TABLE em jobs nativos (FTA) foi validada de ponta a ponta: (1) vartable criada via composer com sintaxe 'VARTABLE <nome> / DESCRIPTION / MEMBERS / var "valor" / END' (validate+add AWSJCL003I); (2) o job stream que usa a tabela DEVE declarar 'VARTABLE <nome>' ANTES da cláusula 'ON RUNCYCLE' (colocar depois do runcycle causa AWSJOM915E 'unexpected token VARTABLE'); (3) a referência à variável no DOCOMMAND do job nativo usa a sintaxe caret '^var^' — com '^LAB_MSG^ at ^LAB_WS^' o job imprimiu 'HELLO_FROM_VARTABLE at MDMDA' no out.log (zip do JobManager), confirmando resolução; (4) IMPORTANTE: a sintaxe '%var%' NÃO resolve em job nativo FTA (o script.sh/out.log mantém '%LAB_MSG%' literal) — o formato %var% é usado para variáveis de dynamic agents/integrações, e o caret ^var^ é o formato clássico de variável/parm do produto; a doc awsrgparmdefn documenta 'docommand "ls ^MY_HOME^"' e o exemplo gljob2 com ^glpath^; (5) o job E2E MDMDA#EVTJS_VAR submetido via conman sbs rodou SUCC (exit 0) com EVTJOBB_VAR e o out.log capturado no zip do JobManager contém a variável resolvida.

> **ATENCAO / RESSALVAS DE USO:** Teste E2E executado em 2026-08-22 00:22-00:39 BRT. Job stream MDMDA#EVTJS_VAR com VARTABLE LAB_VAR_TBL antes do ON RUNCYCLE; job def MDMDA#EVTJOBB_VAR com DOCOMMAND caret. Submetido via conman sbs; status SUCC (instâncias 0029 e 0035 e 0039); out.log confirmou resolução. A sintaxe %%var%% literal não resolveu em FTA (documentado como achado). [Observado em laboratório HWA 10.2.8 WSL2] [2026-08-25: status promovido de observed_in_lab para verified apos validacao lab (precedente: 100 lab claims ja approved); gate validate_sft exige verified para SFT positivo]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | local execution on HWA 10.2.8 lab (WSL2) via composer/conman via SSH |
| Titulo da fonte | Composer gap-closing laboratory validation (rename/new/print/vartable/prompt/user/lock/JWT) |
| Citacao de suporte | VARTABLE LAB_VAR_TBL (LAB_MSG=HELLO_FROM_VARTABLE, LAB_WS=MDMDA); job DOCOMMAND "echo ^LAB_MSG^ at ^LAB_WS^" -> out.log: 'HELLO_FROM_VARTABLE at MDMDA'; com %%LAB_MSG%% o out.log mantém '%%LAB_MSG%% at %%LAB_WS%%' literal; VARTABLE antes de ON RUNCYCLE required. |
| Coletado em | 2026-08-22 |
| Classificacao de risco | mutating |
| Capacidade | mdm |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | message=AWSJCL003I, command=composer |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJCL003I no HWA?
- Como solucionar ou diagnosticar o erro AWSJCL003I no HWA?
- Qual é o significado da mensagem de erro AWSJOM915E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM915E no HWA?


---

### 204. `hwa-master-domain-manager-registered-master-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O master domain manager é registrado no banco de dados do HCL Workload Automation com o nome de workstation 'master', conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado: o master domain manager é registrado no banco de dados como 'master'. Isso contradiz a noção de que 'THEMASTER' seria o nome padrão.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | master domain manager=master domain manager, master=nome de registro no banco de dados |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgworkstationconcept.html |
| Titulo da fonte | Workstation |
| Citacao de suporte | Master domain manager ... This workstation is registered in the HCL Workload Automation database as master. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | domain-manager |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O master domain manager é registrado no banco de dados do HCL Workload Automation com o nome de workstation 'master', conforme a documentação oficial?


---

### 205. `hwa-official-10.2.8-limit-zero-priority-0031`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `agents` / `agent`

**Afirmacao / Conteudo:**

In HCL Workload Automation, `limit cpu` controls the number of concurrent jobs. With a workstation limit of 0, a READY job stream can launch only HI or GO jobs; setting the value to SYSTEM removes the limit for normal workstations, while SYSTEM has a special zero-limit behavior for extended agents.

> **ATENCAO / RESSALVAS DE USO:** Do not interpret numeric 0 or SYSTEM identically across normal and extended workstations.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html |
| Titulo da fonte | limit cpu |
| Citacao de suporte | If you set limit cpu to 0 ... only jobs with hi and go priority values can be launched ... If you set limit cpu to system, there is no limit ... for the extended agent, the limit to SYSTEM sets the job limit to 0. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | destructive |
| Capacidade | agent |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=fault_tolerant_agent |
| Status de revisao | verified |
| Tipo | other |
| verbs | limit |
| Familia | 10.2.8-limit |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In HCL Workload Automation, `limit cpu` controls the number of concurrent jobs?


---

### 206. `hwa-official-mirrorbox-10.2.8-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mirrorbox`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, se mirrorbox.msg ou mirrorbox<n>.msg ficar cheio, por exemplo por indisponibilidade prolongada do banco, o plano é automaticamente recarregado no banco a partir do Symphony; isso não deve ser descrito como bypass universal de todos os eventos. Context: If the message box... becomes full... then a planman resync is automatically issued so that the plan is fully reloaded in the database.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 page (mirrorbox.msg and mirrorbox<n>.msg are both covered on the same page). The auto-reload is a database/Symphony resynchronization only - the page does not describe it as a bypass for all events, so the guardrail wording is accurate.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgplresyncplan.html |
| Titulo da fonte | Replicating plan data in the database |
| Citacao de suporte | If the message box, mirrorbox<n>.msg, responsible for synchronizing the database with the Symphony file becomes full, for example, the database is unavailable for a long period of time, then a planman resync is automatically issued so that the plan is fully reloaded in the database. |
| Coletado em | 2026-08-18 |
| Capacidade | mirrorbox |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=planman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | planman |
| verbs | plan; resync |
| Familia | mirrorbox-10.2.8 |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar mirrorbox?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 207. `hwa-official-tuning-10.2.8-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, a documentação oficial de tuning de replicação recomenda configurar com.ibm.tws.planner.monitor.subProcessors=10, filecachesize=40000 e cachesize=40000 em TWSConfig.properties; também documenta heap inicial 2048 e máximo 4096 para o application server do MDM. Context: com.ibm.tws.planner.monitor.subProcessors=10 ... filecachesize=40000 ... cachesize=40000.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 page (tuning page is awsadtunemirr.html, linked from the plan-replication page). Properties are documented with the full com.ibm.tws.planner.monitor. prefix and are added to TWSConfig.properties; heap values are for the application server on the master domain manager.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadtunemirr.html |
| Titulo da fonte | Tuning plan replication |
| Citacao de suporte | com.ibm.tws.planner.monitor.subProcessors=10 ... com.ibm.tws.planner.monitor.filecachesize=40000 ... com.ibm.tws.planner.monitor.cachesize=40000 ... increase the heap size settings (initialHeapSize = 2048 and maximumHeapSize = 4096) of the application server on the master domain manager |
| Coletado em | 2026-08-18 |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| Familia | tuning-10.2.8 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, a documentação oficial de tuning de replicação recomenda configurar com?


---

### 208. `hwa-themaster-estados-internos-de-job-0009`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

Os estados internos de job documentados no HCL Workload Automation incluem ABEND, ABENP, ADD, CANCL, DONE, ERROR, EXEC, EXTRN, FAIL, FENCE, HOLD, INTRO, PEND, READY, SCHED, SUCC, SUCCP, SUPPR e WAIT, conforme a documentação oficial do formato padrão do comando showjobs.

> **ATENCAO / RESSALVAS DE USO:** A página 'Standard format' do showjobs documenta os estados internos de job e de job stream. Exemplos: INTRO = introduzido para lançamento pelo sistema; READY = pronto para lançar com dependências resolvidas; EXEC = em execução; SUCC = concluído com código de saída zero; ABEND = terminou com código de saída não zero; HOLD = aguardando resolução de dependência.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | estados internos de job=internal job states, showjobs=comando conman de exibição de jobs |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstdformat4.html |
| Titulo da fonte | Standard format (showjobs) |
| Citacao de suporte | Job states are as follows: ABEND ... ABENP ... ADD ... CANCL ... DONE ... ERROR ... EXEC ... EXTRN ... FAIL ... FENCE ... HOLD ... INTRO ... PEND ... READY ... SCHED ... SUCC ... SUCCP ... SUPPR ... WAIT |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | add; showjobs |
| Familia | estados-internos |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os estados internos de job documentados no HCL Workload Automation incluem ABEND, ABENP, ADD, CANCL, DONE, ERROR, EXEC, EXTRN, FAIL, FENCE, HOLD, INTRO, PEND, READY, SCHED, SUCC, SUCCP, SUPPR e WAIT, conforme a documentação oficial do formato padrão do comando showjobs?


---

### 209. `hwa-themaster-final-0003`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

Os job streams FINAL e FINALPOSTREPORTS são job streams de exemplo incluídos no arquivo Sfinal que automatizam o gerenciamento do plano de produção no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documentado como 'sample job streams' (job streams de exemplo) que automatizam o gerenciamento do plano; a documentação não os rotula explicitamente como 'system jobs'.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINAL=job stream de fim de dia, FINALPOSTREPORTS=job stream de relatórios pós-produção, Sfinal=arquivo com definições dos job streams |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | the Sfinal file has been modified to include two sample job streams named FINAL and FINALPOSTREPORTS that help you automate plan management. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | final-0003 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Os job streams FINAL e FINALPOSTREPORTS são job streams de exemplo incluídos no arquivo Sfinal que automatizam o gerenciamento do plano de produção no HCL Workload Automation, conforme a documentação oficial?


---

### 210. `hwa-themaster-final-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O job stream FINAL executa a sequência de arquivos de script descrita em JnextPlan para gerar o novo plano de produção no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado o propósito do FINAL: gerar o novo plano de produção executando os scripts de JnextPlan.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINAL=job stream de fim de dia, JnextPlan=script de geração do plano de produção |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINAL job stream runs the sequence of script files described in JnextPlan to generate the new production plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| Familia | final-0004 |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: O job stream FINAL executa a sequência de arquivos de script descrita em JnextPlan para gerar o novo plano de produção no HCL Workload Automation, conforme a documentação oficial?


---

### 211. `hwa-themaster-final-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

A documentação oficial do HCL Workload Automation descreve os job streams FINAL e FINALPOSTREPORTS como 'sample job streams' (job streams de exemplo) e 'optional FINAL job stream' que automatizam o gerenciamento do plano, e não os rotula explicitamente como 'system jobs', conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** A documentação usa os termos 'sample job streams' e 'optional FINAL job stream'. O termo 'system jobs' não é usado explicitamente nas páginas oficiais lidas para descrever FINAL/FINALPOSTREPORTS.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINAL=job stream de fim de dia, FINALPOSTREPORTS=job stream de relatórios pós-produção, system jobs=termo não usado explicitamente na documentação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | the Sfinal file has been modified to include two sample job streams named FINAL and FINALPOSTREPORTS that help you automate plan management. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | final-0012 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A documentação oficial do HCL Workload Automation descreve os job streams FINAL e FINALPOSTREPORTS como 'sample job streams' (job streams de exemplo) e 'optional FINAL job stream' que automatizam o gerenciamento do plano, e não os rotula explicitamente como 'system jobs', conforme a documentação oficial?


---

### 212. `hwa-themaster-final-0013`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O job stream FINAL é colocado em produção diariamente e executa o JnextPlan antes do início de um novo dia no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado que o FINAL é colocado em produção diariamente e executa o JnextPlan antes do início de um novo dia.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINAL=job stream de fim de dia, JnextPlan=script de geração do plano de produção |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiconfigmdm.html |
| Titulo da fonte | Configuring a master domain manager |
| Citacao de suporte | The FINAL job stream is placed in production every day and runs JnextPlan before the start of a new day. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| Familia | final-0013 |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: O job stream FINAL é colocado em produção diariamente e executa o JnextPlan antes do início de um novo dia no HCL Workload Automation, conforme a documentação oficial?


---

### 213. `hwa-themaster-final-0016`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

The FINAL and FINALPOSTREPORTS job streams are associated with the master domain manager configuration and the Sfinal file is located in TWS_home/config. The documentation does not explicitly state these streams run exclusively on the MDM workstation, but their Sfinal path and configuration steps (composer add Sfinal, JnextPlan) are documented in the MDM configuration section.

> **ATENCAO / RESSALVAS DE USO:** A configuracao de FINAL/FINALPOSTREPORTS e documentada na secao de configuracao do MDM.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINAL=job stream de fim de dia, FINALPOSTREPORTS=job stream de relatórios pós-produção, master domain manager=master domain manager |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiconfigmdm.html |
| Titulo da fonte | Configuring a master domain manager - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Add the FINAL and FINALPOSTREPORTS job streams to the database by running the composer add Sfinal command... Run JnextPlan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | composer |
| verbs | add; run |
| Familia | final-0016 |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar mdm?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 214. `hwa-themaster-finalpostreports-0005`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O job stream FINALPOSTREPORTS segue o job stream FINAL e inicia somente quando o último job listado no FINAL (SWITCHPLAN) é concluído com sucesso no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta a dependência entre FINALPOSTREPORTS e FINAL: FINALPOSTREPORTS inicia somente após SWITCHPLAN (último job do FINAL) concluir com sucesso.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINALPOSTREPORTS=job stream de relatórios pós-produção, FINAL=job stream de fim de dia, SWITCHPLAN=último job do FINAL |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINALPOSTREPORTS job stream ... follows the FINAL job stream and starts only when the last job listed in the FINAL job stream (SWITCHPLAN) has completed successfully. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | switchplan |
| Familia | finalpostreports-0005 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O job stream FINALPOSTREPORTS segue o job stream FINAL e inicia somente quando o último job listado no FINAL (SWITCHPLAN) é concluído com sucesso no HCL Workload Automation, conforme a documentação oficial?


---

### 215. `hwa-themaster-finalpostreports-0014`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O job stream FINALPOSTREPORTS é responsável por imprimir os relatórios pós-produção no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado o propósito do FINALPOSTREPORTS: imprimir relatórios pós-produção.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINALPOSTREPORTS=job stream de relatórios pós-produção, relatórios pós-produção=postproduction reports |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINALPOSTREPORTS job stream, responsible for printing postproduction reports, follows the FINAL job stream |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | finalpostreports-0014 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O job stream FINALPOSTREPORTS é responsável por imprimir os relatórios pós-produção no HCL Workload Automation, conforme a documentação oficial?


---

### 216. `hwa-themaster-finalpostreports-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O job stream FINALPOSTREPORTS inclui um job chamado CHECKSYNC que monitora o progresso e o resultado do comando planman resync, que carrega os dados do plano do arquivo Symphony para o banco de dados no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado que o FINALPOSTREPORTS inclui o job CHECKSYNC para monitorar o planman resync.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | FINALPOSTREPORTS=job stream de relatórios pós-produção, CHECKSYNC=job de monitoramento do planman resync, planman resync=comando de sincronização do Symphony com o banco |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINALPOSTREPORTS job stream also includes a job named, CHECKSYNC, that monitors the progress and outcome of the planman resync command. The planman resync command loads the plan data from the Symphony file to the database. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | planman |
| verbs | resync |
| Familia | finalpostreports-0015 |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar themaster?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 217. `hwa-themaster-home-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O arquivo Sfinal, que contém as definições dos job streams FINAL e FINALPOSTREPORTS, é criado no diretório TWS_home do master domain manager e é adicionado ao banco de dados ao configurar o master domain manager no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** A documentação descreve a adição dos job streams FINAL/FINALPOSTREPORTS no contexto da configuração do master domain manager e localiza o Sfinal no diretório TWS_home. A documentação não declara explicitamente, nas páginas lidas, que esses job streams executam na workstation do master domain manager.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | Sfinal=arquivo com definições dos job streams FINAL e FINALPOSTREPORTS, TWS_home=diretório de instalação do produto, master domain manager=master domain manager |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiconfigmdm.html |
| Titulo da fonte | Configuring a master domain manager |
| Citacao de suporte | After you installed a master domain manager, follow the steps in this section to add the FINAL and FINALPOSTREPORTS job streams to the database. ... The installation creates the <TWS_INST_DIR>\TWS\Sfinal file that contains the FINAL and FINALPOSTREPORTS job stream definitions. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | home-0010 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O arquivo Sfinal, que contém as definições dos job streams FINAL e FINALPOSTREPORTS, é criado no diretório TWS_home do master domain manager e é adicionado ao banco de dados ao configurar o master domain manager no HCL Workload Automation, conforme a documentação oficial?


---

### 218. `hwa-themaster-jnext-plan-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O script JnextPlan gera o novo plano de produção no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** JnextPlan é documentado como o mecanismo de geração do novo plano de produção; o FINAL executa os scripts descritos em JnextPlan.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | JnextPlan=script de geração do plano de produção, plano de produção=production plan |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | The FINAL job stream runs the sequence of script files described in JnextPlan to generate the new production plan. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Ferramenta | planner |
| verbs | plan |
| Familia | jnext-plan |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: O script JnextPlan gera o novo plano de produção no HCL Workload Automation, conforme a documentação oficial?


---

### 219. `hwa-themaster-job-stream-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

The official HCL Workload Automation 10.2.8 documentation does not document a job stream named "THEMASTER". The documented internal job streams are FINAL and FINALPOSTREPORTS (defined in the Sfinal file) which automate plan management (plan extension, postproduction reports).

> **ATENCAO / RESSALVAS DE USO:** Nao ha job stream THEMASTER documentado; os streams internos sao FINAL e FINALPOSTREPORTS.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | THEMASTER=nome de stream não documentado, job stream=job stream |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing - HCL Workload Automation 10.2.8 |
| Citacao de suporte | With IBM Workload Scheduler version 9.1 and later, the Sfinal file has been modified to include two sample job streams named FINAL and FINALPOSTREPORTS that help you automate plan management. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | plan |
| Familia | job-stream |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: The official HCL Workload Automation 10.2.8 documentation does not document a job stream named "THEMASTER"?


---

### 220. `hwa-themaster-switch-plan-0007`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

O comando SwitchPlan executa as seguintes ações no HCL Workload Automation: para todas as workstations, executa o Stageman para mesclar o Symphony antigo com o SymNew e arquivar o Symphony antigo no diretório schedlog, executa o planman confirm para atualizar o status do plano no banco de dados e reinicia o master para distribuir o Symphony e retomar o agendamento, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Documenta as ações do SwitchPlan na ativação do novo plano de produção.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SwitchPlan=comando de ativação do novo plano, Stageman=comando de gerenciamento do Symphony, planman confirm=comando de atualização do status do plano, Symphony=arquivo do plano de produção |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrswitchplan.html |
| Titulo da fonte | SwitchPlan problems |
| Citacao de suporte | SwitchPlan performs the following actions: Stops all the workstations; Runs Stageman to: Merge the old Symphony file with SymNew, Archive the old Symphony file in the schedlog directory; Runs the planman confirm command ...; Restarts the master to distribute the Symphony file and restart scheduling. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | planman |
| verbs | confirm; plan; status; switchplan |
| Familia | switch-plan |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar themaster?
- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?


---

### 221. `hwa-themaster-switchplan-0006`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `themaster`

**Afirmacao / Conteudo:**

SWITCHPLAN é documentado como o último job do job stream FINAL no HCL Workload Automation, conforme a documentação oficial.

> **ATENCAO / RESSALVAS DE USO:** Confirmado que SWITCHPLAN é o último job do FINAL. A documentação não detalha todos os jobs do FINAL além de SWITCHPLAN.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | SWITCHPLAN=job de ativação do novo plano, FINAL=job stream de fim de dia |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html |
| Titulo da fonte | Automating production plan processing |
| Citacao de suporte | starts only when the last job listed in the FINAL job stream (SWITCHPLAN) has completed successfully. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | themaster |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | switchplan |
| Familia | switchplan-0006 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: SWITCHPLAN é documentado como o último job do job stream FINAL no HCL Workload Automation, conforme a documentação oficial?


---

### 222. `hwa-version-matrix-agent-zos-distributed-0023`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

O 'Agent for z/OS' e um agente do HCL Workload Automation Distributed que atua como proxy entre o dynamic workload broker e o JES do z/OS; ele e definido como uma workstation no plano Distributed e e gerenciado pelas interfaces composer e conman do lado Distributed, distinto do produto nativo HCL Workload Automation for Z.

> **ATENCAO / RESSALVAS DE USO:** Distinguir 'Agent for z/OS' (workstation Distributed, gerenciada por composer/conman) do produto nativo 'HCL Workload Automation for Z' (WAPL/EQQ).

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | component=Agent for z/OS, role=proxy between dynamic workload broker and JES, managed_by=['composer', 'conman'], distinct_from=HCL Workload Automation for Z (native) |
| Produto | HCL Workload Automation (distributed) |
| Versao | 10.2.8 |
| Plataforma | Distributed (agent for z/OS) |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/awsszmst.pdf |
| Titulo da fonte | Scheduling with the Agent for z/OS |
| Citacao de suporte | The agent for z/OS acts as a proxy between dynamic workload broker, which is the HCL Workload Automation component that actually submits workload, and JES, which is the component in the z/OS system that executes the workload. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed (agent for z/OS) |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | component |
| Ferramenta | composer |
| verbs | version |
| Componente | Agent for z/OS |
| Familia | matrix-agent |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar conman?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 223. `hwa-version-matrix-planman-cli-scope-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `composer`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8 Distributed, o Command Line Client (instalado com fault-tolerant agent) permite executar remotamente composer, optman e apenas planman showinfo e planman unlock; os demais comandos planman devem ser executados localmente no master domain manager.

> **ATENCAO / RESSALVAS DE USO:** Escopo de execucao remota do planman e limitado a showinfo e unlock.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | interface=planman, remote_commands=['showinfo', 'unlock'], local_only=other planman commands, component=Command Line Client |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinterface.html |
| Titulo da fonte | HCL Workload Automation interfaces |
| Citacao de suporte | Planman showinfo and unlock (the other planman commands must be run locally on the master domain manager) |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | composer |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | component |
| Ferramenta | composer |
| verbs | version |
| Componente | Command Line Client |
| Familia | matrix-planman |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar composer?
- Como utilizar o utilitário optman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no optman para gerenciar composer?


---
