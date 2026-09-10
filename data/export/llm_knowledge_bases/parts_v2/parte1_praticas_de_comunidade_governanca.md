# PARTE1 PRATICAS DE COMUNIDADE GOVERNANCA

## I. Praticas de Comunidade & Governanca

> 14 registros.

---

### 1. `com-change-0001`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `change`

**Afirmacao / Conteudo:**

Uma prática organizacional recomendada de gestão de mudanças é: (1) planejar a mudança em um workspace/pasta separada; (2) usar a palavra-chave draft no job stream para impedir que entre no preproduction plan; (3) revisar versões usando o versionamento baseado em auditoria (dbAudit=1 + auditStore=db) antes do Deploy; e (4) aplicar o Deploy no Graphical Designer. A exigência de aprovação/workflow é decisão da organização; o produto oferece as capacidades (draft, versionamento, auditoria com justificativa opcional), não um fluxo obrigatório.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | change_management |
| Justificativa | Combina as capacidades de produto documentadas (draft, versionamento, auditoria) em um fluxo organizacional seguro. |
| Capacidade | change_management |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=deploy |

**Perguntas relacionadas:**

- Como a palavra-chave draft impede que um job stream entre no plano de produção?


---

### 2. `com-change-0002`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `security` / `security`

**Afirmacao / Conteudo:**

Uma prática recomendada para mudanças em produção é exigir justificativa usando a capacidade opcional de auditoria do Dynamic Workload Console (Administration > Security > Auditing Preferences), que força cada usuário a fornecer um motivo para alterar um objeto, e usar a trilha de auditoria (usuário, data/hora, motivo) para revisão pós-mudança. A política de exigir justificativa é opcional e configurável; a HCL não a torna obrigatória por padrão.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | change_management |
| Justificativa | A auditoria de justificativa documenta o 'quem/quando/porquê' de cada mudança, suportando conformidade. |
| Capacidade | security |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=security_policy |


---

### 3. `com-config-0001`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `config`

**Afirmacao / Conteudo:**

Uma prática recomendada de configuração avançada é separar ambientes (dev/test/prod) usando folders/pastas distintas e instâncias dedicadas, e versionar as mudanças de configuração junto com as definições de jobs usando a auditoria de banco (dbAudit + auditStore=db). Isso é orientação organizacional; o produto fornece os mecanismos (folders, auditoria) mas não prescreve a separação.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | advanced_configuration |
| Justificativa | Separação de ambientes e versionamento de configuração reduzem risco em produção. |
| Capacidade | config_management |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=config |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de configuração avançada é separar ambientes (dev/test/prod) usando folders/pastas distintas e instâncias dedicadas, e versionar as mudanças de configuração junto com as definições de jobs usando a auditoria de banco (dbAudit + auditStore=db)?


---

### 4. `com-config-0002`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Uma prática recomendada de configuração avançada é sincronizar a configuração do site de recuperação de desastres (DR) com o site primário, incluindo o espelhamento do banco de dados e a cópia das chaves AES (TWA_DATA_DIR/ssl/aes) e certificados para o backup master domain manager, para garantir que o ambiente DR possa descriptografar o Symphony. Isso usa as capacidades documentadas (backup MDM com banco espelhado, chaves AES compartilhadas), mas a frequência e a política de sincronização são decisões organizacionais, não prescritas pela HCL.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | advanced_configuration |
| Justificativa | A HCL documenta os mecanismos (espelhamento, chaves AES), mas não prescreve a política de sincronização de configuração entre sites DR. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de configuração avançada é sincronizar a configuração do site de recuperação de desastres (DR) com o site primário, incluindo o espelhamento do banco de dados e a cópia das chaves AES (TWA_DATA_DIR/ssl/aes) e certificados para o backup master domain manager, para garantir que o ambiente DR possa descriptografar o Symphony?


---

### 5. `com-config-0003`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `composer`

**Afirmacao / Conteudo:**

Uma prática recomendada de configuração avançada para isolamento multi-tenancy é usar folders/pastas e security domains distintos por unidade de negócio ou aplicação, combinando a estrutura de pastas do composer com o modelo de segurança baseado em papéis (ACLs, security roles e security domains) para isolar o acesso de cada tenant aos seus objetos de agendamento. O produto fornece os mecanismos (folders, role-based security), mas o desenho de isolamento por tenant é decisão organizacional, não prescrita pela HCL.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | advanced_configuration |
| Justificativa | O modelo role-based security do produto suporta isolamento por domínio/pasta; a política de multi-tenancy é organizacional. |
| Capacidade | composer |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=composer |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar composer?


---

### 6. `com-monitoring-scripts-0004`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `conman`

**Afirmacao / Conteudo:**

Uma prática comum de comunidade em operações HCL Workload Automation é implementar scripts próprios de monitoramento operacional do ambiente (ex.: checagem de filesystem/health check do host, health check de processos do scheduler e serviços systemd) fora do escopo da documentação oficial HCL; tais scripts são customizações locais não prescritas pelo produto. Comandos de linha de comando HWA 10.2.8 usados dentro desses scripts (conman sc/showcpus, composer list/display, etc.) são documentados oficialmente, mas o script como um todo NÃO é procedimento oficial da HCL.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve scripts de monitoramento de host. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; UNIX/AIX/Linux local |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Scripts de monitoramento de filesystem, health check e systemd de uso comum em ambientes operacionais; não documentados oficialmente pela HCL. Aplicar por conta e risco. |
| Coletado em | 2026-08-19 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | operational_monitoring_scripts |
| Justificativa | Validação por pesquisa Perplexity (2026-08-19): os comandos usados (conman start/stop/startmon, twsinst, showcpus) são documentados em awsrgstartstop.html/awspiagentparams.html; o script local de monitoramento é prática de comunidade, não padrão HCL. Fonte local: data/raw/SCRIPT SHELL.pdf (8 chunks promovidos via unofficial_validation_results.jsonl como community_practice). |
| Capacidade | conman |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; UNIX/AIX/Linux local |
| Terminologia normalizada | command=conman |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar conman?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar conman?


---

### 7. `com-naming-0001`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

Uma prática organizacional recomendada é usar uma convenção de nomenclatura que codifique função e contexto no nome do job, por exemplo um prefixo por aplicação (FIN_, HR_, OPS_) e um sufixo que indique a classe de janela (crit, batch, maint). Isso NÃO é um padrão prescrito pelo HCL Workload Automation 10.2.8; o produto impõe apenas limites técnicos (job até 40 caracteres, começando com letra, alfanumérico/-/_).

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | naming_standards |
| Justificativa | Em operação de 3000+ jobs, nomes informativos reduzem confusão e facilitam triagem. A HCL documenta apenas os limites técnicos, não a convenção. |
| Capacidade | naming_convention |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=naming_convention |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Uma prática organizacional recomendada é usar uma convenção de nomenclatura que codifique função e contexto no nome do job, por exemplo um prefixo por aplicação (FIN_, HR_, OPS_) e um sufixo que indique a classe de janela (crit, batch, maint)?


---

### 8. `com-naming-0002`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `naming`

**Afirmacao / Conteudo:**

Uma prática recomendada de comunidade é usar um identificador de ambiente (DEV/TST/PRO) como parte do nome ou da pasta (folder) do job stream, isolando definições por ambiente. Não é um padrão obrigatório do produto; o HCL Workload Automation suporta folders e prefijos de pasta nos seletores [[folder/]workstation#][folder/]jobname.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | naming_standards |
| Justificativa | Isolar ambientes por folder/pasta reduz risco de promover definição errada entre dev e produção. |
| Capacidade | naming_convention |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=naming_convention |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada de comunidade é usar um identificador de ambiente (DEV/TST/PRO) como parte do nome ou da pasta (folder) do job stream, isolando definições por ambiente?


---

### 9. `com-quality-0001`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `quality`

**Afirmacao / Conteudo:**

Uma prática recomendada de qualidade é calcular o percentual de jobs concluídos pontualmente na janela, derivando de contadores já coletados pelo produto (Successful_runs, Abended_runs, Late_start_runs, Late_end_runs na view JOB_STATISTICS_V). A fórmula específica é decisão da organização; a HCL fornece os dados brutos, não o indicador prescrito.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | quality_metrics |
| Justificativa | Métricas objetivas de pontualidade permitem melhoria contínua baseada em dados. |
| Capacidade | sla_quality |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=conman, component=quality |


---

### 10. `com-quality-0002`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `jnextplan`

**Afirmacao / Conteudo:**

Uma prática recomendada é monitorar a taxa de incidentes recorrentes (ex.: mensagens AWSJPL017E de falha do JnextPlan) e a razão entre trabalho programado e não programado, usando a auditoria (enDbAudit/enPlanAudit) e o histórico de mensagens. Isso é uma escolha organizacional de melhoria, não um padrão do produto.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | quality_metrics |
| Justificativa | Reduzir incidências recorrentes e mudanças de emergência melhora a estabilidade operacional. |
| Capacidade | jnextplan |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | message=AWSJPL017E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJPL017E no HWA?
- Como solucionar ou diagnosticar o erro AWSJPL017E no HWA?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 11. `com-sla-0001`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `scheduling` / `deadline`

**Afirmacao / Conteudo:**

Uma prática organizacional recomendada é definir classes de SLA por criticidade de job (crítico, padrão, batch) e medir o atraso com as métricas que o produto já coleta (ex.: Late_start_runs e Late_end_runs na view JOB_STATISTICS_V, e o monitoramento de jobs críticos via approachingLateOffset/deadlineOffset). O SLA em si é uma decisão da organização, não um padrão prescrito pela HCL.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | sla |
| Justificativa | As views de job statistics fornecem os insumos objetivos (atraso, duração) para definir e medir SLAs. |
| Capacidade | deadline |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=conman, component=deadline |


---

### 12. `com-sla-0002`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `topology_ha` / `mdm`

**Afirmacao / Conteudo:**

Uma prática recomendada para recuperação de desastres é definir RTO (tempo alvo de recuperação) e RPO (perda de dados tolerável) para o ambiente HWA, usando como base as capacidades documentadas de backup/restauração (backup MDM com banco espelhado, cópia de arquivos de configuração e chaves AES TWA_DATA_DIR/ssl/aes). RTO/RPO são metas organizacionais, não valores prescritos pela HCL.

> **ATENCAO / RESSALVAS DE USO:** PRÁTICA ORGANIZACIONAL DE COMUNIDADE, não fato de produto. A HCL 10.2.8 não prescreve este padrão. Não usar como fato documentado; usar apenas para treinar distinção entre recomendação organizacional e capacidade de produto.

| Atributo | Valor |
| --- | --- |
| Status do conhecimento | community_practice |
| Confianca | high |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028 (organizational practice - no official source) |
| Titulo da fonte | Community/organizational practice (NOT official HCL documentation) |
| Citacao de suporte | Organizational recommendation; the HCL 10.2.8 documentation does not prescribe this standard. |
| Coletado em | 2026-08-17 |
| Responsavel | community |
| Status de revisao | draft |
| Pratica de comunidade | sim |
| Topico de comunidade | sla |
| Justificativa | O produto fornece os mecanismos (espelhamento, backup), mas os alvos de tempo são decisão de negócio. |
| Capacidade | mdm |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=rest_api_v2, component=master_domain_manager |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Uma prática recomendada para recuperação de desastres é definir RTO (tempo alvo de recuperação) e RPO (perda de dados tolerável) para o ambiente HWA, usando como base as capacidades documentadas de backup/restauração (backup MDM com banco espelhado, cópia de arquivos de configuração e chaves AES TWA_DATA_DIR/ssl/aes)?


---

### 13. `hwa-operational-agent-naming-suffix-0009`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

As an operational naming convention, a dynamic agent installed on the same host as a base workstation can reuse the base name with an incremental suffix, such as MDM and MDM_1, provided the resulting workstation name is unique in the HCL Workload Automation network.

> **ATENCAO / RESSALVAS DE USO:** Recommendation for identification and uniqueness, not an official universal syntax requirement. The laboratory used MDMDA instead. Do not promote this record to verified SFT without an official source. | Fonte primária original local: local operational convention derived from the HWA 10.2.8 laboratory

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | Distributed |
| Status do conhecimento | community_practice |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awspitwsinstparams.html |
| Titulo da fonte | Dynamic-agent naming convention |
| Citacao de suporte | MDM -> base workstation; MDM_1 -> dynamic agent on the same host. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | community_reviewed |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para install?
- Qual a regra documentada no HWA Distributed sobre: As an operational naming convention, a dynamic agent installed on the same host as a base workstation can reuse the base name with an incremental suffix, such as MDM and MDM_1, provided the resulting workstation name is unique in the HCL Workload Automation network?


---

### 14. `hwa-operational-jnextplan-caution-0015`

**Nivel de evidencia:** PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)
**Status do conhecimento:** current
**Taxonomia:** `cli_planning` / `jnextplan`

**Afirmacao / Conteudo:**

In production, JnextPlan must be treated as a controlled plan-transition operation: inspect active and incomplete instances, verify carry-forward settings, avoid concurrent plan generation, capture logs, and compare the old and new plan before allowing normal processing.

> **ATENCAO / RESSALVAS DE USO:** Operational safety guidance derived from the documented restart/removal semantics. It does not claim that JnextPlan alone automatically reruns completed jobs.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.x |
| Plataforma | Distributed |
| Status do conhecimento | community_practice |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html |
| Titulo da fonte | JnextPlan operational safeguards |
| Citacao de suporte | The command moves from an old to a new production plan and activates it across the network. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | jnextplan |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.x |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=planman, component=jnextplan |
| Status de revisao | community_reviewed |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: In production, JnextPlan must be treated as a controlled plan-transition operation: inspect active and incomplete instances, verify carry-forward settings, avoid concurrent plan generation, capture logs, and compare the old and new plan before allowing normal processing?


---
