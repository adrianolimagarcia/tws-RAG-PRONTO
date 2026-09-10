# PARTE1 INSTALACAO MANUTENCAO

## I. Instalacao & Manutencao

> 71 registros.

---

### 1. `hwa-10.2.4-distributed-password-encryption-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

Em HCL Workload Automation, é opcional criptografar as senhas usadas na instalação, upgrade e gestão; o comando secure usa o método AES e imprime a senha criptografada na tela ou a salva em arquivo, e senhas de operadores PeopleSoft exibidas no console aparecem como asteriscos.

> **ATENCAO / RESSALVAS DE USO:** Senhas são dados sensíveis; recomenda-se criptografia (AES) e jamais instruir o usuário a fornecer senha em texto claro.

| Atributo | Valor |
| --- | --- |
| Fonte (URL) | https://www.ibm.com/docs/en/workload-automation/10.2.4?topic=components-encrypting-passwords-optional |
| Versao | 10.2.4 |
| Confianca | high |
| Coletado em | 2026-08-16 |
| Classificacao de risco | credential_sensitive |
| Terminologia normalizada | method=AES, command=secure, usage=encrypt passwords for install/upgrade/manage, storage=screen or file |
| Citacao de suporte | You can optionally encrypt the passwords that you will use while installing, upgrading, and managing IBM Workload Scheduler. The secure command uses the AES method and prints the encrypted password to the screen or saves it to a file. |
| Status do conhecimento | verified |
| Plataforma | distributed |
| Produto | HCL Workload Automation |
| Titulo da fonte | Encrypting passwords (optional) |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.4 |
| Escopo de plataforma | distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Status de revisao | verified |
| Tipo | command |
| verbs | upgrade |
| Familia | distributed-password |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation, é opcional criptografar as senhas usadas na instalação, upgrade e gestão; o comando secure usa o método AES e imprime a senha criptografada na tela ou a salva em arquivo, e senhas de operadores PeopleSoft exibidas no console aparecem como asteriscos?


---

### 2. `hwa-10.2.8-AWSWUI-0001E-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem AWSUI0001E indica que o user name tem um número incorreto de caracteres (intervalo permitido entre 3 e 60); a causa documentada é um valor de user name fora do intervalo permitido, e a recuperação é editar o response file (instalação silenciosa) ou reentrar o user name dentro do intervalo (instalação por wizard).

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'The user name has an incorrect number of characters. The permitted range is between 3 and 60.' Causa: o valor de user name não está dentro do intervalo permitido. Ação do sistema: wizard para com erro; silenciosa sai com erro. Recuperação: silenciosa - editar o response file com user name no intervalo e relançar; wizard - reentrar o user name no intervalo. Diagnóstico de instalação; não modifica estado do engine.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSUI0001E, component=Dynamic Workload Console installation (WUI), object=user name length, permitted_range=3-60 characters |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; Dynamic Workload Console installation |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsawswuimsgs.html |
| Titulo da fonte | AWSUI0001E - AWSUI6212W |
| Citacao de suporte | The user name has an incorrect number of characters. The permitted range is between 3 and 60. ... The value entered as user name does not fall within the permitted range. ... Edit the response file specifying a user name that falls within the supported range, and launch a new installation. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; Dynamic Workload Console installation |
| Tipo | message |
| Codigo da mensagem | AWSUI0001E |
| Componente | Dynamic Workload Console installation (WUI) |
| Familia | AWSWUI-0001E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSWUI0001E no HWA?
- Como solucionar ou diagnosticar o erro AWSWUI0001E no HWA?
- Qual a ação recomendada para a mensagem AWSUI0001E no DWC?
- Qual é o significado da mensagem de erro AWSUI0001E no HWA?
- Qual é o significado da mensagem de erro AWSUI0001E no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSWUI0001E no HWA e qual ação é recomendada?


---

### 3. `hwa-10.2.8-AWSWUI-0018E-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, a mensagem AWSUI0018E indica que são necessários privilégios de administrador para executar a instalação; a causa documentada é que privilégios de administrador são requeridos, e a recuperação é fazer login como Administrador e lançar uma nova instalação.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: 'You must have administrator privileges to run this installation.' Causa: privilégios de administrador são requeridos. Ação do sistema: wizard para com erro; silenciosa sai com erro. Recuperação: fazer login como Administrador e lançar nova instalação. Diagnóstico de instalação; não modifica estado do engine.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSUI0018E, component=Dynamic Workload Console installation (WUI), requirement=administrator privileges |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; Dynamic Workload Console installation |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsawswuimsgs.html |
| Titulo da fonte | AWSUI0001E - AWSUI6212W |
| Citacao de suporte | You must have administrator privileges to run this installation. ... Administrator's privileges are required to run the installation. ... Login as an Administrator and launch a new installation. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; Dynamic Workload Console installation |
| Tipo | message |
| verbs | login |
| Codigo da mensagem | AWSUI0018E |
| Componente | Dynamic Workload Console installation (WUI) |
| Familia | AWSWUI-0018E |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSUI0018E no HWA?
- Como solucionar ou diagnosticar o erro AWSUI0018E no HWA?
- Qual é o significado da mensagem de erro AWSWUI0018E no HWA?
- Como solucionar ou diagnosticar o erro AWSWUI0018E no HWA?
- Qual é o significado da mensagem de erro AWSUI0018E no HWA e qual ação é recomendada?
- Qual é o significado da mensagem de erro AWSWUI0018E no HWA e qual ação é recomendada?


---

### 4. `hwa-10.2.8-aida-intro-0001`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `aida` / `introduction`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o AI Data Advisor (AIDA) e um componente de IA/ML (disponivel desde V10.1) que analisa metricas historicas de workload coletadas pelo HWA, preve padroes futuros e detecta anomalias em tendencias de KPIs (ex.: jobs in plan by status, jobs in plan by workstation), gerando alertas exibidos no Workload Dashboard do Dynamic Workload Console e notificaveis por email. O pacote de instalacao Docker (HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz) contem 9 imagens pre-carregadas (hclcr.io/wa/workload-automation/hcl-aida-{ad,exporter,email,nginx,orchestrator,predictor,redis,config,ui}:10.2.8) e um diretorio docker-deployment com AIDA.sh, docker-compose.yml, common.env, Dockerfiles por servico, config/, nginx/cert/, redis/, keycloak/ e Licenses/.

> **ATENCAO / RESSALVAS DE USO:** Estrutura do pacote AIDA 10.2.8 validada em laboratorio (sha256 facc5bf6..., 930 arquivos). [Observado em laboratorio HWA 10.2.8 WSL2] Fontes: AIDA User's Guide 10.2.8 (help.hcl-software.com) e deploy README oficial no GitHub HCL-TECH-SOFTWARE. O AIDA.sh 10.2.8 exige CONTAINER_RUNTIME explicito (docker|podman) - diferenca vs GitHub publico 10.2.6 que auto-detecta; evidencia hwa-lab-10.2.8-aida-ash-container-runtime-0069.

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
| Citacao de suporte | AI Data Advisor (AIDA) is a component of HCL Workload Automation since V10.1, based on Artificial Intelligence and Machine Learning techniques. It enables fast and simplified data-driven decision making for an intelligent workload management. |
| Coletado em | 2026-08-25 |
| Capacidade | aida_install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, Docker 29.7.2, Docker Compose v5.5.0, pacote extraido em /opt/hwa/aida, tested_commands=['Get-FileHash HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz', 'tar -tzf | head', 'tar -xzf (docker-deployment + aida-images-hcl.tar.gz)'], result=SHA256 facc5bf669d9d15399e3e56cbf5116361e5a28bd7208c0b368bfd4b37fd1d378; 1.915.102.598 bytes; 930 arquivos; 9 imagens hcl-aida-*:10.2.8 + docker-deployment com AIDA.sh/docker-compose.yml/common.env/Dockerfiles., validated_at=2026-08-25T13:20:00BRT |
| Terminologia normalizada | topic=aida |
| Status de revisao | lab_validated |
| Tipo | other |
| verbs | plan; status |
| Familia | aida-intro |

**Perguntas relacionadas:**

- Como o AIDA atua na detecção de anomalias e predição de problemas no HWA?


---

### 5. `hwa-10.2.8-capacity-bm-look-0026`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

As opções localopts do HCL Workload Automation 10.2.8 relacionadas a performance têm padrões documentados: bm look (intervalo mínimo do batchman antes de varrer o arquivo de controle de produção) com padrão 5 segundos em instalação nova e 15 segundos em upgrade, e bm read (máximo de segundos que o batchman espera por mensagem no intercom.msg) com padrão 3 segundos em instalação nova e 10 segundos em upgrade.

> **ATENCAO / RESSALVAS DE USO:** Padrões documentados de opções de varredura do batchman, relevantes para performance; notar diferença fresh install vs upgrade.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm look=bm look, bm read=bm read, localopts=arquivo localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm look = seconds — ...default value is automatically set to 5 for improving product performance. The previous default value was 15 seconds... bm read = seconds — ...set to 3... The previous default value was 10 seconds |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES), tested_commands=['cat /opt/hwa/TWSDATA/localopts'], result=/opt/hwa/TWSDATA/localopts: bm look = 5, bm check file = 120, bm check status = 300, bm check until = 300, bm check deadline = 0. Confirmados no lab 10.2.8.00., validated_at=2026-08-23T02:20:00BRT |
| Tipo | other |
| verbs | upgrade |
| Familia | capacity-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: As opções localopts do HCL Workload Automation 10.2.8 relacionadas a performance têm padrões documentados: bm look (intervalo mínimo do batchman antes de varrer o arquivo de controle de produção) com padrão 5 segundos em instalação nova e 15 segundos em upgrade, e bm read (máximo de segundos que o batchman espera por mensagem no intercom?


---

### 6. `hwa-10.2.8-cert-permissions-version-dep-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Certificate file permissions (644 vs 755) in HWA 10.2.8 are flow-dependent and must match the exact installation procedure.

> **ATENCAO / RESSALVAS DE USO:** Procedure-dependent file permission rules.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | version_dependent |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing or upgrading Dynamic Workload Console |
| Citacao de suporte | Different flows specify 644 for file permissions and 755 for directory extraction; permissions are procedure-specific. |
| Coletado em | 2026-08-16 |
| Capacidade | install |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | topic=cert |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Certificate file permissions (644 vs 755) in HWA 10.2.8 are flow-dependent and must match the exact installation procedure?


---

### 7. `hwa-10.2.8-configafter-post-install-config-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `general_operations` / `config`

**Afirmacao / Conteudo:**

Após a instalação do HCL Workload Automation 10.2.8, os componentes devem ser configurados seguindo o procedimento de configuração documentado, que inclui a definição de opções globais, locais e de usuário, além da configuração de autenticação e comunicação segura.

> **ATENCAO / RESSALVAS DE USO:** Tópico mutante (configuração). Verificado na página oficial 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | phase=post-installation configuration, object=global, local and user options; authentication and secure communication |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiafter.html |
| Titulo da fonte | Configuring |
| Citacao de suporte | Configuring HCL Workload Automation components after installation. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | mutating |
| Capacidade | config_post_install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | install |
| Familia | configafter-post |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Após a instalação do HCL Workload Automation 10.2.8, os componentes devem ser configurados seguindo o procedimento de configuração documentado, que inclui a definição de opções globais, locais e de usuário, além da configuração de autenticação e comunicação segura?


---

### 8. `hwa-10.2.8-dbmigration-awspiupgrddb-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `migration`

**Afirmacao / Conteudo:**

A migração do banco de dados dos componentes de servidor do HCL Workload Automation 10.2.8 é executada pelo utilitário awspiupgrddb, que atualiza o esquema do banco de dados para a versão atual do produto.

> **ATENCAO / RESSALVAS DE USO:** Tópico destrutivo (migração de banco). Verificado na página oficial 10.2.8. Recomenda-se backup antes da execução.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | utility=awspiupgrddb, object=server components database schema migration |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrddb.html |
| Titulo da fonte | Upgrading the database for the server components |
| Citacao de suporte | Upgrading the database for the server components |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | migration |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Familia | dbmigration-awspiupgrddb |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A migração do banco de dados dos componentes de servidor do HCL Workload Automation 10.2.8 é executada pelo utilitário awspiupgrddb, que atualiza o esquema do banco de dados para a versão atual do produto?


---

### 9. `hwa-10.2.8-directupgrade-direct-upgrade-paths-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 suporta upgrade direto (direct upgrade) a partir das versões 9.5.0.x ou 10.x.x, sem necessidade de instalação paralela, seguindo os passos documentados para a versão 10.2.8.

> **ATENCAO / RESSALVAS DE USO:** Tópico destrutivo (upgrade). Verificado na página oficial 10.2.8. Requer backup e verificação de pré-requisitos.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | upgrade_type=direct upgrade, from_versions=9.5.0.x; 10.x.x, to_version=10.2.8 |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidirectupgrade.html |
| Titulo da fonte | Performing a direct upgrade from v 9.5.0.x or v 10.x.x to v 10.2.8 |
| Citacao de suporte | Detailed steps to perform a direct upgrade from version 9.5.0.x or v 10.x.x to version 10.2.8 |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | upgrade |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | upgrade |
| Familia | directupgrade-direct |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 suporta upgrade direto (direct upgrade) a partir das versões 9.5.0.x ou 10.x?


---

### 10. `hwa-10.2.8-dwc-cert-ownership-0006`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

UNIX certificate files in the documented DWC installation flow must be owned by the MDM installation user. Context: Certificate files on UNIX must be owned by the user account running the installation.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 DWC installation page (awsadinstallcerts.html 404s; certificate handling is documented in the DWC install/upgrade flow under distr/src_pi/). Certificate material is credential-sensitive. | Same sentence verbatim on the distinct v1028 DWC install page.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing the Dynamic Workload Console |
| Citacao de suporte | For UNIX systems, ensure that all the files have the ownership of the user who installed the master domain manager and the correct permissions (644). |
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
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | dwc-cert |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: UNIX certificate files in the documented DWC installation flow must be owned by the MDM installation user?


---

### 11. `hwa-10.2.8-dwc-certs-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In HWA 10.2.8, the documented DWC installation and upgrade flow requires ca.crt, tls.key, and tls.crt certificates. Context: Ensure you have the required certificate files ca.crt, tls.key, and tls.crt available before running the installer.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 DWC installation page. The certificates are required for HCL Workload Automation install/upgrade in general (not only DWC); for DWC they must be converted and copied locally before running dwcinst. | Same sentence verbatim; certs listed as HTML ul bullets on both pages.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing the Dynamic Workload Console |
| Citacao de suporte | Certificates are now required when installing or upgrading HCL Workload Automation. You can no longer install nor upgrade HCL Workload Automation without securing your environment with certificates. The required certificates are: ca.crt, tls.key, tls.crt |
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
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | upgrade |
| Familia | dwc-certs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In HWA 10.2.8, the documented DWC installation and upgrade flow requires ca?


---

### 12. `hwa-10.2.8-dwc-install-0020`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o Dynamic Workload Console e instalado como um componente distinto por meio do script dwcinst (dwcinst.sh em UNIX/Linux, dwcinst.vbs em Windows), separado da instalacao do MDM (serverinst); o processo e iniciado a partir do diretorio da imagem de instalacao do DWC e usa um arquivo de propriedades (dwcinst.properties) para os valores default.

> **ATENCAO / RESSALVAS DE USO:** Fonte: pesquisa Perplexity + webfetch 2026-08-19 (awspidwcinstsyntax v1028, awspiinstallDWC v1028). dwcinst e o script dedicado do DWC; serverinst instala os servidores (MDM/DDM) e twsinst instala agents.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html |
| Titulo da fonte | Dynamic Workload Console installation - dwcinst script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | This script installs the Dynamic Workload Console. Default values are stored in the dwcinst.properties file, located in the root directory of the installation image. |
| Coletado em | 2026-08-19 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar install?


---

### 13. `hwa-10.2.8-dwc-install-0021`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os pre-requisitos do Dynamic Workload Console incluem a instalacao de um runtime Web (WebSphere Application Server Liberty Base ou Open Liberty) e de um banco de dados suportado para o DWC (DB2, DB2 for z/OS, Oracle, Informix, MSSQL ou PostgreSQL), que deve existir antes da primeira instalacao do DWC; os requisitos de software detalhados sao publicados no artigo de System Requirements da HCL Support.

> **ATENCAO / RESSALVAS DE USO:** Fonte: pesquisa Perplexity + webfetch 2026-08-19 (eqqi1dwcprereq v1028, pagina oficial de pre-requisitos do DWC). O runtime Web e o banco devem estar instalados antes do dwcinst; --wlpdir e obrigatorio no dwcinst. [cross-ref auditor 2026-08-25: ver hwa-10.2.8-dwc-install-0023 - configureDb.sh cria o banco automaticamente se nao existir; a exigencia de banco pre-existente aplica-se ao dwcinst, precedido pelo configureDb]

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_inst/eqqi1dwcprereq.html |
| Titulo da fonte | Dynamic Workload Console prerequisites - HCL Workload Automation 10.2.8 |
| Citacao de suporte | The Dynamic Workload Console installation has the following prerequisites. WebSphere Application Server Liberty Base ... Before you install the Dynamic Workload Console for the first time, ensure you have a supported database installed. You can choose to use any of the supported relational database management systems (RDBMS). |
| Coletado em | 2026-08-19 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install; open |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os pre-requisitos do Dynamic Workload Console incluem a instalacao de um runtime Web (WebSphere Application Server Liberty Base ou Open Liberty) e de um banco de dados suportado para o DWC (DB2, DB2 for z/OS, Oracle, Informix, MSSQL ou PostgreSQL), que deve existir antes da primeira instalacao do DWC; os requisitos de software detalhados sao publicados no artigo de System Requirements da HCL Support?


---

### 14. `hwa-10.2.8-dwc-install-0022`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, os caminhos default de instalacao do Dynamic Workload Console sao /opt/wa/DWC em UNIX/Linux e %ProgramFiles%\wa\DWC em Windows; na arquitetura tipica o DWC e instalado em workstations proprias (por exemplo dois DWC em dois nos distintos compartilhando o mesmo banco remoto), separadas do master domain manager e dos agents.

> **ATENCAO / RESSALVAS DE USO:** Fonte: pesquisa Perplexity + webfetch 2026-08-19 (awspidwcinstsyntax v1028 e awspitypicalfullstack v1028). Instalacao tipica: dois DWC em dois nos distintos compartilhando o mesmo banco remoto.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html |
| Titulo da fonte | Dynamic Workload Console installation - dwcinst script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | --inst_dir ... The default values varies based on the operating system, as follows: On Windows operating systems %ProgramFiles%\wa\DWC; On UNIX operating systems /opt/wa/DWC; On z/OS operating system /opt/wa/DWC |
| Coletado em | 2026-08-19 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os caminhos default de instalacao do Dynamic Workload Console sao /opt/wa/DWC em UNIX/Linux e %ProgramFiles%\wa\DWC em Windows; na arquitetura tipica o DWC e instalado em workstations proprias (por exemplo dois DWC em dois nos distintos compartilhando o mesmo banco remoto), separadas do master domain manager e dos agents?


---

### 15. `hwa-10.2.8-dwc-install-0023`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `configuredb`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o script configureDb.sh do kit DWC com RDBMS_TYPE=POSTGRESQL e COMPONENT_TYPE=DWC cria automaticamente o banco do DWC se ele nao existir (mensagem WAINST0534W 'The database TDWC does not exist. It will be created.') e popula os schemas tdwc e fed (Federator, instalado junto desde 10.2.3); em PostgreSQL o rc=6 do dbTool (banco inexistente) e tratado como condicao normal de criacao, nao como erro.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25: configureDb.sh criou TDWC (schemas tdwc 48 tabelas, fed 7 tabelas) usando DB_ADMIN_USER=postgres e DB_USER=postgresdwc. O default do kit 10.2.8 para o nome do banco DWC e TDWC (nao DWC) nas properties configureDbPostgresql/dblighttool.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | destructive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstdbcfg.html |
| Titulo da fonte | Database configuration - configureDb script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | WAINST0534W The database TDWC does not exist. It will be created. | WAINST077I The database has been successfully created or updated. | WAINST052I The command configureDb has completed successfully. |
| Coletado em | 2026-08-25 |
| Capacidade | configuredb |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | Kit DWC 10.2.8 extraido; PostgreSQL 18 acessivel em localhost:5432; role DB admin (postgres) com senha lab; role DB user (postgresdwc) criada; certificados ca.crt/tls.key/tls.crt em pasta sslkeysfolder (ownership usuario MDM, 644); umask 022. |
| Impacto | Cria o banco TDWC e seus schemas (tdwc, fed) se nao existirem; operacao de escrita no servidor de banco. |
| Reversibilidade | DROP DATABASE TDWC e recriacao via configureDb.sh; em lab o banco e descartavel. |
| Criterio de parada | Interromper se configureDb.sh falhar na conexao (DB_ADMIN_USER sem permissao) ou reportar erro de SQL aplicado. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o script configureDb?


---

### 16. `hwa-10.2.8-dwc-install-0024`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `dwcinst`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o dwcinst.sh do kit DWC instala o servidor Dynamic Workload Console no Open Liberty informado por --wlpdir (obrigatorio) e usa WLP_USER_DIR=${DWC_INST_DIR}/usr (os arquivos do servidor dwcServer ficam em ${DWC_INST_DIR}/usr/servers/dwcServer, nao no diretorio usr do Liberty), com dados/logs em DWC_DATA_dir (por default ${DWC_INST_DIR}/DWC_DATA); o datasource jdbc/dwcdb e configurado para o banco informado (ex.: jdbc:postgresql://host:port/TDWC) e as senhas sao gravadas como {aes} criptografado com a chave wlp.password.encryption.key do passphrase_variables.xml.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25: dwcinst.sh -f dwcinst.properties instalou em /opt/hwa/DWC com wlpdir /opt/liberty/wlp, portas 9443 (HTTPS) / 9444 (HTTP) / 12809 (bootstrap) / 19402 (bootsec), registry via twaregistry.sh (10.2.8.00-2026.07), log em DWC_DATA/installation/logs/dwcinst_10.2.8.00.log. O servidor roda como o usuario DWC admin (WA_USER em appservertools/setEnv.sh).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | destructive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html |
| Titulo da fonte | Dynamic Workload Console installation - dwcinst script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | WAINST023I The installation has completed successfully. | WAINST006I Browse to this URL with a browser: https://<host>:9443/console/login.jsp |
| Coletado em | 2026-08-25 |
| Capacidade | dwcinst |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | Open Liberty instalado (wlpdir); banco TDWC criado e populado por configureDb.sh; certificados em sslkeysfolder; usuario admin DWC existente no SO; inst_dir diferente do diretorio da imagem; umask 022. |
| Impacto | Instala o DWC (aplicacao + datasource) em DWC_INST_DIR; registra a instancia via twaregistry. |
| Reversibilidade | Executar o uninstaller do DWC (uninstall) e remover DWC_INST_DIR; em lab o diretorio e descartavel. |
| Criterio de parada | Interromper se o prereq check falhar (SKIPCHECKPREREQ=false), se o datasource nao conectar ao banco ou se o certificado for rejeitado. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install; open |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o dwcinst?


---

### 17. `hwa-10.2.8-dwc-install-0025`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `dwc_user`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o usuario administrador do DWC (parametro --user, default dwcadmin) e o usuario do SO que o servidor dwcServer usa para executar (WA_USER em appservertools/setEnv.sh) e o principal do basicRegistry (user.twsuser.id/user.twsuser.password no wauser_variables.xml, grupo Admins via admin.group.name); e possivel trocar esse usuario apos a instalacao editando wauser_variables.xml (com senha {aes} re-gerada com a mesma chave wlp.password.encryption.key), ajustando WA_USER e a ownership da arvore DWC_INST_DIR, sem reinstalar.

> **ATENCAO / RESSALVAS DE USO:** Validado em laboratorio 2026-08-25: instalado com dwcadmin, o DWC foi trocado para wauser editando wauser_variables.xml (senha {aes} gerada com securityUtility encode --encoding=aes --key=<chave do passphrase_variables.xml>, round-trip conferido com PasswordCipherUtil.decipher), setEnv.sh (WA_USER=wauser) e chown -R wauser:wauser /opt/hwa/DWC; login validado com wauser (302 + LtpaToken2 + dashboard 200).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html |
| Titulo da fonte | Dynamic Workload Console installation - dwcinst script - HCL Workload Automation 10.2.8 |
| Citacao de suporte | User : dwcadmin | <variable name="user.twsuser.id" value="wauser"/> | WA_USER=wauser |
| Coletado em | 2026-08-25 |
| Capacidade | dwc_user |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00, DWC /opt/hwa/DWC, Open Liberty /opt/liberty/wlp, PostgreSQL 18 TDWC, tested_commands=['configureDb.sh -f configureDbPostgresql.properties (POSTGRESQL, COMPONENT_TYPE=DWC, DB_NAME=TDWC)', 'dwcinst.sh -f dwcinst.properties (ACCEPTLICENSE=yes, RDBMS_TYPE=POSTGRESQL, DWC_INST_DIR=/opt/hwa/DWC, WLP_INSTALL_DIR=/opt/liberty/wlp)', 'appservertools/startAppServer.sh (dwcServer)', 'POST /console/j_security_check (j_username=wauser)', 'POST /dwc/api/v1/engine/create + GET /dwc/api/v1/engine/{id}/checkConnection'], result=configureDb WAINST052I (banco TDWC criado, schemas tdwc 48 + fed 7); dwcinst WAINST023I; server 9443/9444; login 302+LtpaToken2+dashboard 200; engine connection MDM_LAB checkConnection successful, validated_at=2026-08-25T08:23:00BRT |
| Pre-condicoes | DWC instalado; acesso root no host para chown; chave de encriptacao wlp.password.encryption.key do passphrase_variables.xml; senha {aes} valida para o novo usuario. |
| Impacto | Altera a identidade que executa o servidor DWC e autentica no console; requer restart do dwcServer. |
| Reversibilidade | Reverter wauser_variables.xml/setEnv.sh para o usuario anterior e chown correspondente. |
| Criterio de parada | Interromper se a senha {aes} gerada nao decifrar para o valor esperado (round-trip) ou se o login apos restart falhar. |
| Terminologia normalizada | topic=dwc |
| Status de revisao | lab_validated |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | dwc-install |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o usuario administrador do DWC (parametro --user, default dwcadmin) e o usuario do SO que o servidor dwcServer usa para executar (WA_USER em appservertools/setEnv?


---

### 18. `hwa-10.2.8-dwcinst-params-0009`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `dwcinst`

**Afirmacao / Conteudo:**

The dwcinst command documents database parameters, required --wlpdir, and SSL options --sslkeysfolder and --sslpassword. Context: dwcinst syntax accepts database parameters, --wlpdir, and SSL parameters --sslkeysfolder and --sslpassword.

> **ATENCAO / RESSALVAS DE USO:** Verified on the official v1028 DWC installation page (awsaddwcinstcmd.html 404s; dwcinst syntax is documented in the DWC install flow and the linked 'dwcinst script' page). Database parameters (--rdbmstype, --dbhostname, --dbport, --dbname, --dbuser, --dbpassword), --wlpdir, --sslkeysfolder and --sslpassword all documented. Note: the parameter table on the page spells the SSL folder flag '--sslkesfolder' (typo) while the command examples use '--sslkeysfolder'. | dwcinst syntax page documents the same parameter set incl. --sslkeysfolder/--sslpassword and --wlpdir.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing the Dynamic Workload Console |
| Citacao de suporte | cscript dwcinst.vbs --acceptlicense yes --rdbmstype db_type --user dwc_admin_user --password dwc_pwd --dbname db_name --dbuser db_user --dbpassword db_pwd --dbhostname db_hostname --dbport db_port --wlpdir Liberty_installation_dir\wlp --sslkeysfolder certificate_files_path --sslpassword keystore_truststore_password |
| Coletado em | 2026-08-18 |
| Capacidade | dwcinst |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Terminologia normalizada | topic=dwcinst |
| Status de revisao | verified |
| Tipo | other |
| Familia | dwcinst-params |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: The dwcinst command documents database parameters, required --wlpdir, and SSL options --sslkeysfolder and --sslpassword?


---

### 19. `hwa-10.2.8-incident-awsjom179-e-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

A mensagem AWSJOM179E no HCL Workload Automation 10.2.8 é emitida ao tentar excluir a definição de uma workstation (via Composer ou Dynamic Workload Console) e o servidor workload broker está inacessível, com o texto 'An error occurred deleting definition of the workstation {0}. The workload broker server is currently unreachable.' Causa documentada: um dynamic domain manager foi removido sem seguir o procedimento de desinstalação descrito no Planning and Installation. Recuperação documentada: verificar que o dynamic domain manager foi realmente excluído (não apenas indisponível) e excluir as workstations conectadas a ele com o comando 'composer del ws <workstation_name>;force'.

> **ATENCAO / RESSALVAS DE USO:** Componente jobman/object management; causa e recuperação documentadas na página oficial distribuída v1028.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | AWSJOM179E=falha ao excluir definição de workstation; servidor workload broker inacessível, cause=causa, recovery=recuperação |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrcompdelwork.html |
| Titulo da fonte | Composer deletion of a workstation fails with the AWSJOM179E error (v1028) |
| Citacao de suporte | AWSJOM179E An error occurred deleting definition of the workstation {0}. The workload broker server is currently unreachable. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | command |
| Ferramenta | composer |
| Codigo da mensagem | AWSJOM179E |
| Familia | incident-awsjom179 |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM179E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM179E no HWA?
- Qual é o significado da mensagem de erro AWSJOM179 no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM179 no HWA?
- Qual é o significado da mensagem de erro AWSJOM179E no HWA e qual ação é recomendada?


---

### 20. `hwa-10.2.8-incident-upgrade-config-merge-0125`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `upgrade`

**Afirmacao / Conteudo:**

Sintoma: apos upgrade para versao 8.6, AWSBHU507I 'Killed A start command was issued' aparece. Causa: durante o upgrade, os arquivos de configuracao (tws_env.sh, tws_env.csh, jobmanrc, TWSCCLog.properties, StartUp, MakePlan, SwitchPlan, CreatePostReports, UpdateStats, ResetPlan, Sfinal) nao sao sobrescritos, mas a versao 8.6 deles e instalada sob tws_home/config. Resolucao: mesclar manualmente as duas versoes dos arquivos, modificando o arquivo sob tws_home. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - upgrade config merge |
| Citacao de suporte | During the upgrade to version 8.6, the following configuration files... are not overwritten but the 8.6 version of above files are installed under tws_home/config directory, and therefore to remove the above error message you must merge manually the two version of the files |
| Coletado em | 2026-08-23 |
| Capacidade | upgrade |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versao, plataforma, autorizacao e backup/rollback aplicaveis. |
| Impacto | Pode alterar estado operacional (merge de config); avaliar o escopo antes da execucao. |
| Reversibilidade | Restaurar os arquivos de configuracao anteriores. |
| Criterio de parada | Interromper diante de divergencia de versao, evidencia, autorizacao ou resultado inesperado. |
| Terminologia normalizada | message=AWSBHU507I, command=start |
| Status de revisao | verified |
| Tipo | message |
| Ferramenta | planner |
| verbs | merge; start; switchplan; upgrade |
| Codigo da mensagem | AWSBHU507I |
| Familia | incident-upgrade |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBHU507I no HWA?
- Como solucionar ou diagnosticar o erro AWSBHU507I no HWA?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- O que causa e como solucionar o problema: apos upgrade para versao 8?


---

### 21. `hwa-10.2.8-incident-variables-upgrade-0121`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `incidents` / `upgrade`

**Afirmacao / Conteudo:**

Sintoma: apos um upgrade, variaveis globais nao sao resolvidas. Causa: durante o upgrade, todas as statements do arquivo de seguranca relativas as variaveis globais foram copiadas pelo installation wizard para uma default variable table no novo arquivo de seguranca; as variaveis globais ficam desabilitadas e so podem ser usadas atraves das variable tables. Se o arquivo de seguranca for reconstruido usando o output do dumpsec anterior como input, o problema ocorre. Fonte: HCL Troubleshooting Guide 10.2.8.

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
| Titulo da fonte | HCL Workload Automation Troubleshooting Guide 10.2.8 - variables not resolved after upgrade |
| Citacao de suporte | During the upgrade, all the security file statements relating to your global variables were copied by the installation wizard into a default variable table in the new security file. Global variables are disabled and can only be used through the variable tables. |
| Coletado em | 2026-08-23 |
| Capacidade | upgrade |
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
| Familia | incident-variables |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Sintoma: apos um upgrade, variaveis globais nao sao resolvidas?
- O que causa e como solucionar o problema: apos um upgrade, variaveis globais nao sao resolvidas?


---

### 22. `hwa-10.2.8-install-configure-db-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação limpa do HCL Workload Automation 10.2.8, o banco de dados deve ser criado e populado (script configureDb) antes da instalação dos componentes; os componentes são então instalados na ordem: master domain manager e backup master domain manager, dynamic domain manager e backup dynamic domain manager, servidores Dynamic Workload Console e, por fim, dynamic agents.

> **ATENCAO / RESSALVAS DE USO:** Escopo: instalação limpa (fresh install) em plataforma distribuída 10.2.8. A ordem segue o cenário típico de instalação (banco antes dos componentes) e o componente serverinst instala MDM/backup/DDM/backup DDM; DWC via dwcinst e agents via twsinst. A página Upgrading descreve ordem diferente (DWC primeiro) que se aplica a upgrade, não a instalação limpa; não generalizar para upgrades.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstdbcfg.html |
| Titulo da fonte | Database configuration - configureDb script |
| Citacao de suporte | This script creates and populates the HCL Workload Automation database |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
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
| Familia | install-configure |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para install?
- Qual a regra documentada no HWA Distributed sobre: Na instalação limpa do HCL Workload Automation 10.2.8, o banco de dados deve ser criado e populado (script configureDb) antes da instalação dos componentes; os componentes são então instalados na ordem: master domain manager e backup master domain manager, dynamic domain manager e backup dynamic domain manager, servidores Dynamic Workload Console e, por fim, dynamic agents?


---

### 23. `hwa-10.2.8-install-configure-db-0002`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

O script configureDb cria e popula o banco de dados do HCL Workload Automation 10.2.8 e aceita os parâmetros rdbmstype, dbhostname, dbport, dbname, dbuser e dbpassword; os bancos suportados incluem DB2, PostgreSQL, MSSQL e Oracle; no DB2, a criação do banco e das tablespaces exige um dos grants mínimos SYSADM, SYSCTRL ou SELECT privilege no administrative view PRIVILEGES.

> **ATENCAO / RESSALVAS DE USO:** Escopo: 10.2.8 distribuído. A documentação oficial também lista IDS (Informix) como rdbmstype suportado, além de DB2/ORACLE/MSSQL/POSTGRESQL; a declaração 'DB2/PostgreSQL/MSSQL/Oracle' é correta mas não exaustiva. Grant DB2: 'SYSADM, SYSCTRL, SELECT privilege on the PRIVILEGES administrative view' confirmado na FAQ de grants mínimos.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstdbcfg.html |
| Titulo da fonte | Database configuration - configureDb script |
| Citacao de suporte | This script creates and populates the HCL Workload Automation database |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
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
| verbs | install |
| Familia | install-configure |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: O script configureDb cria e popula o banco de dados do HCL Workload Automation 10.2.8 e aceita os parâmetros rdbmstype, dbhostname, dbport, dbname, dbuser e dbpassword; os bancos suportados incluem DB2, PostgreSQL, MSSQL e Oracle; no DB2, a criação do banco e das tablespaces exige um dos grants mínimos SYSADM, SYSCTRL ou SELECT privilege no administrative view PRIVILEGES?


---

### 24. `hwa-10.2.8-install-dwcinst-install-0006`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 é instalado como componente distinto usando o script dwcinst (dwcinst.sh/dwcinst.vbs), com parâmetros como --rdbmstype, --dbname, --dbuser, --dbpassword, --dbport, --dbhostname, --wlpdir, --sslkeysfolder, --sslpassword, --user e --password; o DWC é um componente separado do master domain manager/dynamic domain manager (serverinst) e dos agents (twsinst).

> **ATENCAO / RESSALVAS DE USO:** Tópico de instalação (2 fontes oficiais). Desde a 10.2.3 o Federator também é instalado automaticamente com o DWC. O DWC usa o dwcinst enquanto componentes servidor usam serverinst e agents usam twsinst.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | Installing the Dynamic Workload Console |
| Citacao de suporte | ./dwcinst.sh --acceptlicense yes --rdbmstype db_type --user dwc_admin_user --password dwc_pwd --dbname db_name --dbuser db_user --dbpassword db_pwd --dbhostname db_hostname --dbport db_port --wlpdir Liberty_installation_dir/wlp --sslkeysfolder certificate_files_path --sslpassword keystore_truststore_password |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
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
| Ferramenta | dwc |
| verbs | install |
| Familia | install-dwcinst |

**Perguntas relacionadas:**

- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar install?
- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar install?


---

### 25. `hwa-10.2.8-install-sslkeysfolder-certs-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Certificados são obrigatórios na instalação do HCL Workload Automation 10.2.8: a pasta --sslkeysfolder deve conter os arquivos ca.crt, tls.key e tls.crt e a senha é fornecida com --sslpassword; o programa de instalação processa automaticamente os arquivos keystore e truststore a partir desses certificados PEM.

> **ATENCAO / RESSALVAS DE USO:** Tópico de certificados (2 fontes oficiais). A obrigatoriedade vale desde a versão 10.2.1 ('No, starting from version 10.2.1, certificates, either default or custom, are required when installing HCL Workload Automation'). Também confirmado nas páginas dwcinst e serverinst. Em UNIX, os arquivos devem pertencer ao usuário do MDM com permissão 644.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallMDMasBKM.html |
| Titulo da fonte | Installing the master domain manager as a backup master domain manager |
| Citacao de suporte | The installation program automatically processes the keystore and truststore files using the password you specify with the --sslpassword parameter. The folder must contain the following files: ca.crt ... tls.key ... tls.crt |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
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
| verbs | install |
| Familia | install-sslkeysfolder |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Certificados são obrigatórios na instalação do HCL Workload Automation 10.2.8: a pasta --sslkeysfolder deve conter os arquivos ca?


---

### 26. `hwa-10.2.8-limit-cpu-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In HCL Workload Automation Distributed 10.2.8, the default simultaneous job limit for a workstation after installation is zero and must be increased before any job can launch. The conman limit cpu (lc) command changes that value, from 0 to 1024 or system, and requires limit access.

> **ATENCAO / RESSALVAS DE USO:** Short form lc confirmed on the Conman commands list page. With limit 0, only jobs with hi/go priority launch; limit system means no limit (extended agent SYSTEM limit = 0). Limit changes carry forward to the next day's plan.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html |
| Titulo da fonte | limit cpu |
| Citacao de suporte | Changes the limit of jobs that can run simultaneously on a workstation. You must have limit access to the workstation. ... Supported values are from 0 to 1024 and system. ... When you first start HCL Workload Automation following installation, the workstation job limit is set to zero, and must be increased before any jobs are launched. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | conman |
| verbs | limit |
| Familia | limit-cpu |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar install?


---

### 27. `hwa-10.2.8-parallel-upgrade-tls12-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

Em um upgrade paralelo do HCL Workload Automation de 9.4.0.x para 10.2.8, TLS 1.2 deve ser habilitado no master domain manager 9.4 em nível anterior para permitir a comunicação entre componentes 9.4 e 10.2.8. Context: In back-level environments, for example 9.4, SSL is not enabled by default and TLS version 1.2 needs to be enabled on the back-level master domain manager to enable communication.

> **ATENCAO / RESSALVAS DE USO:** The procedure changes sslProtocol to TLSv1.2 in the JazzSM security.xml and com.ibm.ssl.protocol in ssl.client.props on the back-level (9.4) master domain manager, then restarts the MDM (stopWas.sh/startWas.sh) and the Dynamic Workload Console. Parent page (awspiparallelupgrade.html) lists 'Configuring TLS to the appropriate version' as a prerequisite before the parallel upgrade. TLS/SSL security claim - keep placeholders. | v1028 9.4->10.2.8 parallel-upgrade overview; same TLS-1.2 fact verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiparallelupgradefrom94TLS.html |
| Titulo da fonte | Configuring TLS to the appropriate version (Parallel upgrade from version 9.4.0.x to version 10.2.8) |
| Citacao de suporte | In back-level environments, for example 9.4, SSL is not enabled by default and TLS version 1.2 needs to be enabled on the back-level master domain manager to enable communication. |
| Coletado em | 2026-08-18 |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | topic=parallel |
| Status de revisao | verified |
| Tipo | other |
| verbs | upgrade; version |
| Familia | parallel-upgrade |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em um upgrade paralelo do HCL Workload Automation de 9.4.0.x para 10.2.8, TLS 1.2 deve ser habilitado no master domain manager 9.4 em nível anterior para permitir a comunicação entre componentes 9.4 e 10.2.8. Context: In back-level environments, for example 9.4, SSL is not enabled by default and TLS version 1.2 needs to be enabled on the back-level master domain manager to enable communication?


---

### 28. `hwa-10.2.8-postgresql-awspicreate-postgre-sqltables-0002`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `database`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o procedimento documentado para criar e popular o banco de dados PostgreSQL do master domain manager e do Dynamic Workload Console utiliza os guias 'Creating and populating the database for PostgreSQL for the master domain manager' e 'Creating and populating the database for PostgreSQL for the Dynamic Workload Console' da documentacao oficial (awspicreatePostgreSQLtables e awspicreatePostgreSQLtables_DWC).

> **ATENCAO / RESSALVAS DE USO:** Fonte: doc oficial HCL (pagina PostgreSQL). Referencia cruzada com lab 10.2.8.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/common/src_gi/eqqg1PostgreSQL1023.html |
| Titulo da fonte | Elevate your data management with PostgreSQL database - HCL Workload Automation 10.2.3 |
| Citacao de suporte | For more information about using PostgreSQL to create the database for the master domain manager and Dynamic Workload Console, see Creating and populating the database for PostgreSQL for the master domain manager and Creating and populating the database for PostgreSQL for the Dynamic Workload Console. |
| Coletado em | 2026-08-25 |
| Capacidade | postgresql |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=postgresql |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| Familia | postgresql-awspicreate |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o procedimento documentado para criar e popular o banco de dados PostgreSQL do master domain manager e do Dynamic Workload Console utiliza os guias 'Creating and populating the database for PostgreSQL for the master domain manager' e 'Creating and populating the database for PostgreSQL for the Dynamic Workload Console' da documentacao oficial (awspicreatePostgreSQLtables e awspicreatePostgreSQLtables_DWC)?


---

### 29. `hwa-10.2.8-postgresql-postgresql-mdm-db-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `database`

**Afirmacao / Conteudo:**

No HCL Workload Automation a partir da versao 10.2.3, o PostgreSQL pode ser usado para criar o banco de dados do master domain manager e do Dynamic Workload Console, substituindo OneDB e Informix que deixaram de ser suportados; o PostgreSQL e gratuito e open-source, oferece opcoes de performance, seguranca e configuracao, e sua customizacao suporta escalabilidade e disponibilidade para grandes volumes de dados.

> **ATENCAO / RESSALVAS DE USO:** Fonte: doc oficial HCL 10.2.3+ (pagina PostgreSQL). Confirmado no lab 10.2.8 via configureDb.sh (LAB hwa-lab-10.2.8-postgresql-configuredb-0001).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64 |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1023/common/src_gi/eqqg1PostgreSQL1023.html |
| Titulo da fonte | Elevate your data management with PostgreSQL database - HCL Workload Automation 10.2.3 |
| Citacao de suporte | You can now use the PostgreSQL database to create the database for the master domain manager and Dynamic Workload Console. PostgreSQL replaces OneDB and Informix, which are no longer supported. |
| Coletado em | 2026-08-25 |
| Capacidade | postgresql |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64 |
| Terminologia normalizada | topic=postgresql |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | open |
| Familia | postgresql-postgresql |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation a partir da versao 10.2.3, o PostgreSQL pode ser usado para criar o banco de dados do master domain manager e do Dynamic Workload Console, substituindo OneDB e Informix que deixaram de ser suportados; o PostgreSQL e gratuito e open-source, oferece opcoes de performance, seguranca e configuracao, e sua customizacao suporta escalabilidade e disponibilidade para grandes volumes de dados?


---

### 30. `hwa-10.2.8-rollback-no-rollback-doc-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

HCL Workload Automation 10.2.8 does not document a rollback/downgrade procedure after upgrade. The upgrading page warns that new database records may prevent rollback to a previous version. Backup does not equal a supported downgrade path.

> **ATENCAO / RESSALVAS DE USO:** Nao ha procedimento de rollback documentado para 10.2.8.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | object=rollback/restore after upgrade, confirmed=no official 10.2.8 page |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | low |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Using the new features introduced with the latest release creates new records in the database which are not compatible with previous versions and therefore you cannot roll back your environment to a previous version. |
| Coletado em | 2026-08-16 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | rollback; upgrade; version |
| Familia | rollback-no |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HCL Workload Automation 10.2.8 does not document a rollback/downgrade procedure after upgrade?


---

### 31. `hwa-10.2.8-runbook-pre-upgrade-os-prereq-0031`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, antes de iniciar o upgrade é preciso verificar os pré-requisitos mínimos suportados de sistema operacional, produto e banco de dados, e baixar as imagens de instalação.

> **ATENCAO / RESSALVAS DE USO:** Pre-upgrade prerequisite verification and image download; part of documented upgrade runbook.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | procedure=pre-upgrade, requirements=['verify supported OS/product/database', 'download installation images'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspibeforeupgr.html |
| Titulo da fonte | Before upgrading |
| Citacao de suporte | Before starting to upgrade the product, verify that your network has the minimum required supported versions of the operating system, product, and database. ... Before starting to upgrade, download the installation images. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | upgrade |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | upgrade |
| Familia | runbook-pre |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, antes de iniciar o upgrade é preciso verificar os pré-requisitos mínimos suportados de sistema operacional, produto e banco de dados, e baixar as imagens de instalação?


---

### 32. `hwa-10.2.8-runbook-pre-upgrade-stop-0030`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, antes do upgrade é necessário ter parado o processamento de workload no master domain manager, e é necessário mesclar as personalizações do script tws_env no novo script sem sobrescrever os parâmetros relacionados às bibliotecas OpenSSL.

> **ATENCAO / RESSALVAS DE USO:** Pre-upgrade steps: stop MDM workload and preserve tws_env customization. Destructive/mutating environment change.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | procedure=pre-upgrade, requirements=['stop workload processing on MDM', 'merge tws_env customizations', 'preserve OpenSSL parameters'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading |
| Citacao de suporte | Before upgrading, ensure that you have stopped workload processing on the master domain manager. If you have previously customized the tws_env script, merge your changes into the new version of the script. Ensure you do not overwrite the parameters related to OpenSSL libraries during the merge. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | upgrade |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| verbs | stop; upgrade |
| Familia | runbook-pre |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, antes do upgrade é necessário ter parado o processamento de workload no master domain manager, e é necessário mesclar as personalizações do script tws_env no novo script sem sobrescrever os parâmetros relacionados às bibliotecas OpenSSL?


---

### 33. `hwa-10.2.8-runbook-upgrade-order-dwc-0029`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, em um upgrade direto a partir de 9.5.0.x ou 10.x.x, a sequência documentada é: atualizar primeiro a Dynamic Workload Console e seu banco de dados, depois o dynamic domain manager e seus backups e o banco de dados, depois o master domain manager e seus backups e o banco de dados, e por fim os domain managers e os agents.

> **ATENCAO / RESSALVAS DE USO:** Documented upgrade order for direct upgrade; destructive/mutating (upgrade). Requires backup before upgrade.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | procedure=direct upgrade, order=['DWC and its database', 'DDM and backups and database', 'MDM and backups and database', 'domain managers and agents'] |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading |
| Citacao de suporte | In a direct upgrade procedure from version 9.5.0.x or 10.x.x, you upgrade the Dynamic Workload Console and its database, then upgrade the dynamic domain manager and its backups and the database, then master domain manager and its backups and the database, and finally the domain managers and their backups, and the agents. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | destructive |
| Capacidade | upgrade |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Tipo | other |
| Ferramenta | dwc |
| verbs | upgrade |
| Familia | runbook-upgrade |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, em um upgrade direto a partir de 9.5.0.x ou 10.x?


---

### 34. `hwa-10.2.8-themaster-resolved-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `twsinst`

**Afirmacao / Conteudo:**

RESOLUCAO de hwa-themaster-0001 (contradicted): o nome de workstation padrao do master domain manager no HCL Workload Automation 10.2.8 e MASTER (parametro -master do twsinst, default MASTER), e NAO THEMASTER; THEMASTER e um nome possivel, mas nao o default documentado. Claims que afirmam THEMASTER como padrao estao incorretos.

> **ATENCAO / RESSALVAS DE USO:** Resolve a contradicao: default documentado e MASTER; THEMASTER nao e o padrao.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | HCL Workload Automation twsinst parameters |
| Citacao de suporte | -master workstation ... If not specified, the default value is MASTER. |
| Coletado em | 2026-08-21 |
| Capacidade | twsinst |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | command=themaster |
| Status de revisao | verified |
| Tipo | command |
| Familia | themaster-resolved |

**Perguntas relacionadas:**

- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?


---

### 35. `hwa-10.2.8-tls-ssl-default-install-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Fresh HWA Distributed 10.2.8 installations install the master domain manager and dynamic domain manager in SSL mode by default.

> **ATENCAO / RESSALVAS DE USO:** Does not establish the default for BMDM or BDDM; upgrades from before 10.1 require separate treatment.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | credential_sensitive |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiMDMBrokerSSL.html |
| Titulo da fonte | Configuring your master domain manager and dynamic domain manager in SSL mode |
| Citacao de suporte | By default, starting from version 10.1 master domain manager and dynamic domain manager are installed in SSL mode. |
| Coletado em | 2026-08-15 |
| Capacidade | install |
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
| verbs | install |
| Familia | tls-ssl |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Fresh HWA Distributed 10.2.8 installations install the master domain manager and dynamic domain manager in SSL mode by default?


---

### 36. `hwa-10.2.8-tls12-parallel-upgrade-0007`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

TLS 1.2 is required for communication between 9.4.0.x and 10.2.8 components during parallel upgrade. Context: Communication between 9.4.0.x and 10.2.8 components during parallel upgrade requires TLS 1.2.

> **ATENCAO / RESSALVAS DE USO:** The lead sentence of the official page states the requirement verbatim; the same statement appears as the topic summary in the documentation tree of awspiparallelupgrade.html. Applies to the 9.4.0.x -> 10.2.8 parallel-upgrade path only; the 9.5.0.x/10.x.x paths have their own upgrade documents (awspiparallelupgradefrom95.html). TLS/SSL security claim. | v1028 page contains the identical sentence verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiparallelupgradefrom94TLS.html |
| Titulo da fonte | Configuring TLS to the appropriate version (Parallel upgrade from version 9.4.0.x to version 10.2.8) |
| Citacao de suporte | Setting TLS to version 1.2 is required to ensure communication between 9.4 and 10.2.8 components. |
| Coletado em | 2026-08-18 |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | topic=tls12 |
| Status de revisao | verified |
| Tipo | other |
| verbs | upgrade |
| Familia | tls12-parallel |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: TLS 1.2 is required for communication between 9.4.0.x and 10.2.8 components during parallel upgrade?


---

### 37. `hwa-10.2.8-trouble-awsjom179e-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a exclusao de uma workstation via Composer ou Dynamic Workload Console falha com AWSJOM179E 'An error occurred deleting definition of the workstation <name>. The workload broker server is currently unreachable'; a causa documentada e a remocao de um dynamic domain manager sem seguir o procedimento de desinstalacao do Planning and Installation; a recuperacao documentada e (1) verificar que o dynamic domain manager foi realmente excluido (nao apenas indisponivel) e (2) excluir as workstations com o comando composer del ws <workstation_name>;force.

> **ATENCAO / RESSALVAS DE USO:** Sintoma: AWSJOM179E ao excluir workstation. Causa: DDM removido incorretamente. Recuperacao: verificar e composer del ws <ws>;force. Diagnostico; a recuperacao usa composer del (destrutivo) e deve ser revisada conforme politica de seguranca.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | message=AWSJOM179E, component=composer / DWC (workstation deletion), symptom=falha ao excluir definicao de workstation, cause=dynamic domain manager removido sem o procedimento de desinstalacao, recovery=verificar exclusao do DDM e composer del ws <workstation>;force |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | distributed; composer/DWC |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrmst.pdf |
| Titulo da fonte | HCL Workload Automation troubleshooting guide - workstation deletion fails with AWSJOM179E |
| Citacao de suporte | AWSJOM179E An error occurred deleting definition of the workstation {0}. The workload broker server is currently unreachable. This problem occurs if you removed a dynamic domain manager without following the procedure that describes how to uninstall a dynamic domain manager. To remove workstations connected to the dynamic domain manager, perform the following steps: 1. Verify that the dynamic domain manager was deleted... 2. Delete the workstations using the following command: composer del ws <workstation_name>;force |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-message-triager |
| Status de revisao | draft |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | distributed; composer/DWC |
| Tipo | message |
| Ferramenta | composer |
| Codigo da mensagem | AWSJOM179E |
| Componente | composer / DWC (workstation deletion) |
| Familia | trouble-awsjom179e |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSJOM179E no HWA?
- Como solucionar ou diagnosticar o erro AWSJOM179E no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar install?


---

### 38. `hwa-10.2.8-tune-bm-look-0018`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

A opção bm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de escanear e atualizar seu arquivo de controle de produção; o padrão é 5 segundos em instalação limpa desde 9.4 FP1 e 15 segundos em upgrades que preservam o valor anterior.

> **ATENCAO / RESSALVAS DE USO:** Valor menor implica varreduras mais frequentes do Symphony, usando mais CPU.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm look=bm look, Batchman=Batchman, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm look = seconds - ... If you install the 9.4, FP1 version as a fresh installation, the default value is automatically set to 5 for improving product performance. The previous default value was 15 seconds and is maintained if you perform a product upgrade. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de escanear e atualizar seu arquivo de controle de produção; o padrão é 5 segundos em instalação limpa desde 9.4 FP1 e 15 segundos em upgrades que preservam o valor anterior?


---

### 39. `hwa-10.2.8-tune-bm-read-0019`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

A opção bm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda por uma mensagem no arquivo intercom.msg; o padrão é 3 segundos em instalação limpa desde 9.4 FP1 e 10 segundos em upgrades que preservam o valor anterior.

> **ATENCAO / RESSALVAS DE USO:** Valor menor aumenta o despertar do Batchman quando ocioso, aumentando o consumo de CPU.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | bm read=bm read, Batchman=Batchman, intercom.msg=intercom.msg, localopts=localopts |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadlocaloptdescr.html |
| Titulo da fonte | Localopts details |
| Citacao de suporte | bm read = seconds - Specify the maximum number of seconds Batchman waits for a message in the intercom.msg message file. ... If you install the 9.4, FP1 version as a fresh installation, the default value is automatically set to 3 ... The previous default value was 10 seconds and is maintained if you perform a product upgrade. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-security-lifecycle-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | tune-bm |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A opção bm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda por uma mensagem no arquivo intercom?


---

### 40. `hwa-10.2.8-upgrade-certs-required-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

Em HCL Workload Automation 10.2.8, instalação e upgrade de componentes server exigem certificados ca.crt, tls.key e tls.crt; certificados são obrigatórios e no upgrade paralelo devem ser extraídos do keystore/truststore da versão anterior antes do procedimento.

> **ATENCAO / RESSALVAS DE USO:** Certificados obrigatórios confirmados; operação sensível exige change aprovado. [texto recuperado do unified dataset rag_corpus (verified_claim original)] | Certs-required sentence verbatim; same text also on awspiinstallDWC.html.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiparallelupgradefrom95.html |
| Titulo da fonte | Parallel upgrade from version 9.5.0.x or 10.x.x to version 10.2.8 |
| Citacao de suporte | You can no longer install nor upgrade HCL Workload Automation without securing your environment with certificates. The required certificates are: ca.crt, tls.key, tls.crt. |
| Coletado em | 2026-08-16 |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | topic=upgrade |
| Status de revisao | verified |
| Tipo | other |
| verbs | upgrade |
| Familia | upgrade-certs |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, instalação e upgrade de componentes server exigem certificados ca?


---

### 41. `hwa-10.2.8-upgrade-gskit-openssl-0004`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

Em um upgrade de HCL Workload Automation para 10.2.8 vindo de 9.5 com certificados customizados, os parâmetros de certificados no localopts devem ser verificados; para certificados gerados com OpenSSL é preciso revisar paths (SSL key, SSL certified, SSL key pwd, SSL CA certified, SSL random seed), e para GSKit os parâmetros migram automaticamente para OpenSSL.

> **ATENCAO / RESSALVAS DE USO:** Upgrade 9.5→10.2.8 direto confirmado; não promove procedimento de certificado como instrução universal de change. [texto recuperado do unified dataset rag_corpus (verified_claim original)] | GSKit->OpenSSL migration statement verbatim on the 9.5/10.x parallel-upgrade path.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidirectupgrade.html |
| Titulo da fonte | Performing a direct upgrade from v 9.5.0.x or v 10.x.x to v 10.2.8 |
| Citacao de suporte | If you have used GSKit, the relevant parameters are automatically migrated to the new OpenSSL parameters ... If you have previously used certificates generated with OpenSSL, check the paths in the following section: SSL key, SSL certified, SSL key pwd, SSL CA certified, SSL random seed. |
| Coletado em | 2026-08-16 |
| Capacidade | upgrade |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | topic=upgrade |
| Status de revisao | verified |
| Tipo | other |
| verbs | upgrade |
| Familia | upgrade-gskit |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: Em um upgrade de HCL Workload Automation para 10.2.8 vindo de 9.5 com certificados customizados, os parâmetros de certificados no localopts devem ser verificados; para certificados gerados com OpenSSL é preciso revisar paths (SSL key, SSL certified, SSL key pwd, SSL CA certified, SSL random seed), e para GSKit os parâmetros migram automaticamente para OpenSSL?


---

### 42. `hwa-10.2.8-upgrade-order-0006`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

Em HCL Workload Automation Distributed 10.2.8, a boa prática de upgrade começa pelo Dynamic Workload Console; o upgrade direto de 9.5/10.x atualiza DWC e banco, depois dynamic domain manager e backups, master domain manager e backups, e por fim domain managers e agents.

> **ATENCAO / RESSALVAS DE USO:** Ordem de upgrade confirmada em 10.2.8; sequência de execução real depende do change aprovado. [texto recuperado do unified dataset rag_corpus (verified_claim original)] | v10.2.0 Upgrading page; version caveat: both 10.2.x Distributed, sentence verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading |
| Citacao de suporte | it is a good practice to start with the upgrade of the Dynamic Workload Console first ... you upgrade the Dynamic Workload Console and its database, then upgrade the dynamic domain manager and its backups and the database, then master domain manager and its backups and the database, and finally the domain managers and their backups, and the agents. |
| Coletado em | 2026-08-16 |
| Capacidade | upgrade |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | topic=upgrade |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | upgrade |
| Familia | upgrade-order |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, a boa prática de upgrade começa pelo Dynamic Workload Console; o upgrade direto de 9.5/10.x atualiza DWC e banco, depois dynamic domain manager e backups, master domain manager e backups, e por fim domain managers e agents?


---

### 43. `hwa-10.2.8-vm-direct-upgrade-0010`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No HCL Workload Automation 10.2.8, o upgrade é suportado a partir de 9.5.0.x ou 10.x.x por procedimento direto (direct upgrade) ou paralelo (parallel upgrade); a partir de 9.4.0.x apenas o upgrade paralelo é suportado.

> **ATENCAO / RESSALVAS DE USO:** Escopo Distributed. A página 10.2.8 documenta caminhos de upgrade direto/paralelo e paralelo-exclusivo para 9.4.0.x.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | direct upgrade=upgrade direto no mesmo hardware, parallel upgrade=upgrade paralelo com instalação ao lado da versão antiga, upgrade=procedimento de atualização de versão |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading (HCL Workload Automation 10.2.8 Planning and Installation) |
| Citacao de suporte | if you have installed version 9.5.0.x or 10.x.x and want to upgrade to version 10.2.8 with a direct upgrade procedure ... if you have installed version 9.4.0.x and want to upgrade to version 10.2.8. In this case, only a parallel upgrade is supported. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | upgrade |
| Familia | vm-direct |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o upgrade é suportado a partir de 9.5.0.x ou 10.x?


---

### 44. `hwa-10.2.8-vm-ispf-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

A interface de operação do HCL Workload Automation for Z (z/OS) é o diálogo ISPF (invocado pela CLIST de amostra EQQOPCAC ou pelo menu ISPF), e a documentação z/OS (Planning and Installation, Managing the Workload, Driving HCL Workload Automation for Z) não documenta os comandos conman nem o OCLI, que pertencem à documentação distribuída.

> **ATENCAO / RESSALVAS DE USO:** A documentação z/OS usa ISPF e interfaces de programação (EQQEXIT, APIs); conman/ocli não constam da árvore zos/. Trata-se de distinção de plataforma (Distributed vs z/OS são produtos separados), não de diferença entre versões.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | ISPF=interface de diálogo do produto z/OS, EQQOPCAC=CLIST de amostra para invocar o diálogo do HWA for Z, conman=CLI distribuída, OCLI=Orchestration CLI distribuída |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | z/OS |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/zos/src_inst/eqqi1dialinv.html |
| Titulo da fonte | Invoking the HCL Workload Automation for Z dialog (HCL Workload Automation for Z 10.2) |
| Citacao de suporte | You can invoke the HCL Workload Automation for Z dialog in the following ways: Using the EQQOPCAC sample CLIST, Modifying an existing ISPF selection menu, Selecting the main menu directly from TSO, Using the ISPF select service. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | z/OS |
| scope | boundary_zos |
| scope_note | Fronteira z/OS mantida: documenta distincao entre HWA Distributed e HWA for Z (z/OS). Nao generalizar comandos/erros para o motor nativo z/OS. |
| validation_scope | zos_boundary_explicit |
| scope_rationale | Scope is explicitly limited to z/OS or documents a z/OS-versus-distributed boundary; do not generalize to HWA Distributed 10.2.8. |
| Tipo | command |
| Ferramenta | conman |
| Familia | vm-ispf |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar install?


---

### 45. `hwa-10.2.8-vm-mixed-version-environment-0011`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

O HCL Workload Automation 10.2.8 suporta coexistência de versões (mixed-version environment) durante o upgrade: componentes como agentes, Dynamic Workload Console, dynamic domain managers e master domain manager podem ficar em níveis de versão diferentes, e o procedimento de upgrade paralelo instala componentes 10.2.8 lado a lado com os da versão anterior antes da troca.

> **ATENCAO / RESSALVAS DE USO:** A página de mixed-version environment dá exemplo de instalar um agente 10.2.x conectado a um master domain manager back-level, confirmando a coexistência entre 10.2.x e versões anteriores.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | mixed-version environment=ambiente com componentes em versões diferentes, coexistência=instalação lado a lado de versões diferentes, parallel upgrade=upgrade paralelo |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading (HCL Workload Automation 10.2.8 Planning and Installation) |
| Citacao de suporte | Because HCL Workload Automation supports compatibility with earlier versions, after upgrading the console, you can decide to proceed with upgrading in one of the following ways |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | upgrade; version |
| Familia | vm-mixed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 suporta coexistência de versões (mixed-version environment) durante o upgrade: componentes como agentes, Dynamic Workload Console, dynamic domain managers e master domain manager podem ficar em níveis de versão diferentes, e o procedimento de upgrade paralelo instala componentes 10.2.8 lado a lado com os da versão anterior antes da troca?


---

### 46. `hwa-10.2.8-vm-parallel-upgrade-0012`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

No upgrade paralelo para 10.2.8 a partir de 9.5.0.x ou 10.x.x, novos componentes 10.2.8 (Dynamic Workload Console, dynamic domain manager e master domain manager) são instalados como backup e ativados por switch, mantendo a versão anterior em execução lado a lado até a troca; o console 10.2.8 é instalado primeiro e passa a coexistir com os demais componentes ainda na versão antiga.

> **ATENCAO / RESSALVAS DE USO:** Escopo Distributed. Coexistência 10.2.x com versões anteriores 9.5.x/10.x.x é documentada na seção de upgrade/parallel upgrade.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | parallel upgrade=upgrade paralelo, backup master domain manager=master domain manager reserva, switchmgr=troca de master ativo para o reserva, coexistência=instalação lado a lado |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading (HCL Workload Automation 10.2.8 Planning and Installation) |
| Citacao de suporte | In a parallel upgrade procedure from version 9.5.0.x or 10.x.x, you upgrade WebSphere Application Server Liberty, upgrade the Dynamic Workload Console and its database, then upgrade the database for the server components and install a new dynamic domain manager and master domain manager configured as a backup, then switch them to become the master. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| verbs | upgrade |
| Familia | vm-parallel |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No upgrade paralelo para 10.2.8 a partir de 9.5.0.x ou 10.x?


---

### 47. `hwa-9.5-cert-permissions-contrast-0015`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** version_dependent
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

PAR CONTRASTIVO de hwa-10.2.8-cert-permissions-version-dep-0015: as permissoes de arquivos de certificado (644 vs 755) no HWA sao especificas de cada fluxo de instalacao/upgrade e de cada versao; o fluxo da 9.5 e o da 10.2.8 documentam permissoes distintas para os mesmos tipos de arquivo (por exemplo, extracao de diretorio com 755 e arquivos com 644).

> **ATENCAO / RESSALVAS DE USO:** Par contrastivo: confirmar as permissoes no fluxo exato e na versao exata antes de reproduzir em SFT.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5; 10.2.8 |
| Plataforma | Distributed |
| Classificacao de risco | read_only |
| Status do conhecimento | version_dependent |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWCupgr.html |
| Titulo da fonte | HCL Workload Automation DWC installation/upgrade |
| Citacao de suporte | Different flows specify 644 for file permissions and 755 for directory extraction; permissions are procedure-specific. |
| Coletado em | 2026-08-21 |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 9.5; 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | topic=cert |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2.8-cert-permissions-version-dep-0015: as permissoes de arquivos de certificado (644 vs 755) no HWA sao especificas de cada fluxo de instalacao/upgrade e de cada versao; o fluxo da 9.5 e o da 10.2.8 documentam permissoes distintas para os mesmos tipos de arquivo (por exemplo, extracao de diretorio com 755 e arquivos com 644)?


---

### 48. `hwa-9.5-real-autofailover-fp2-0004`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

O failover automatico do master/event manager foi introduzido no HCL Workload Automation 9.5 Fix Pack 2: com a lista de backups definida pelas opcoes workstationMasterListInAutomaticFailover e workstationEventMgrListInAutomaticFailover, a carga e transferida automaticamente para o backup; instalacoes novas de 9.5 FP2 ou posterior habilitam o recurso por padrao (yes), enquanto upgrades de 9.5/9.5 FP1 exigem habilitacao manual. Recurso NAO presente nas versoes 9.5 base / 9.5 FP1.

> **ATENCAO / RESSALVAS DE USO:** Claim REAL verificado em fonte oficial HCL (admin guide 9.5). Automatic failover e um marco de versao: 9.5 base/FP1 nao tinha; 9.5 FP2+ habilita por padrao em instalacao nova.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 9.5 Fix Pack 2 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v95/distr/src_ad/awsadmst.html |
| Titulo da fonte | HCL Workload Automation 9.5 Administration Guide - automatic failover |
| Citacao de suporte | Starting with version 9.5 Fix Pack 2, you can rely on the automatic failover feature, where, given a list of available backups, the workload is switched over to the backup. A fresh installation of IBM Workload Scheduler V9.5FP2 or later enables this feature by default (yes). |
| Coletado em | 2026-08-21 |
| Responsavel | hwa-version-matrix-analyst |
| Status de revisao | draft |
| Terminologia normalizada | automatic failover=failover automatico do master/event manager, workstationMasterListInAutomaticFailover=lista de backups elegiveis do master, workstationEventMgrListInAutomaticFailover=lista de backups do event manager |
| Capacidade | upgrade |
| Modo de operacao | read |
| Escopo de versao | 9.5 Fix Pack 2 |
| Escopo de plataforma | Distributed |
| Tipo | other |
| Familia | real-autofailover |


---

### 49. `hwa-install-1028-dm-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na configuração de um domain manager HWA 10.2.8, a workstation manager deve ser definida em um novo domínio, incluída no plano com JnextPlan -for 0000 e receber limite de jobs utilizável. Context: Create a new domain; TYPE MANAGER; Run JnextPlan -for 0000.

> **ATENCAO / RESSALVAS DE USO:** Steps confirmed verbatim: 'Create a new domain by running the following command: composer new domain'; 'Define the domain manager as a full status autolink fault-tolerant agent in the HCL Workload Automation database'; workstation definition uses 'TYPE MANAGER / AUTOLINK ON / FULLSTATUS ON'; final step 'Change the workstation limit to allow jobs to run on the workstation' (conman 'limit;10'). Procedural claim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspicfgdm.html |
| Titulo da fonte | Configuring a domain manager |
| Citacao de suporte | Run JnextPlan -for 0000 to include the domain manager workstation in the plan and to send the Symphony file to it. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=planman, component=install |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | planner |
| verbs | create; install; run |
| Familia | 1028-dm |

**Perguntas relacionadas:**

- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?
- Qual a regra documentada no HWA Distributed sobre: Na configuração de um domain manager HWA 10.2.8, a workstation manager deve ser definida em um novo domínio, incluída no plano com JnextPlan -for 0000 e receber limite de jobs utilizável?


---

### 50. `hwa-install-1028-mdm-first-plan-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na configuração inicial de um MDM HWA 10.2.8, a documentação orienta adicionar Sfinal, executar JnextPlan, verificar Batchman LIVES e revisar o limite de jobs da workstation, cujo padrão pós-instalação é zero. Context: composer add Sfinal; JnextPlan; Batchman LIVES; The default job limit after installation is 0.

> **ATENCAO / RESSALVAS DE USO:** Steps verified verbatim on the page: 'composer add Sfinal' (adds FINAL/FINALPOSTREPORTS definitions from <TWS_INST_DIR>/TWS/Sfinal); 'JnextPlan'; 'conman status ... the status that is returned by the command is Batchman LIVES'; 'Change the workstation limit value to run jobs' (conman 'limit ;10'). Also corroborated by 'Starting production plan processing' (awsrgstartprod.html): 'Increase the limit to allow jobs to run. The default job limit after installation is zero.'

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiconfigmdm.html |
| Titulo da fonte | Configuring a master domain manager |
| Citacao de suporte | The default job limit after installation is 0, so no jobs run at any time. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | command=batchman |
| Status de revisao | verified |
| Tipo | command |
| Ferramenta | composer |
| verbs | add; install; limit; plan |
| Familia | 1028-mdm |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar install?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 51. `hwa-install-1028-ports-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

HWA Distributed 10.2.8 documenta portas padrão incluindo 31111, 31115, 31116, 31113, 31114, 31117, 41114, 35116, 9443 e 9444; valores podem ser customizados. Context: Dynamic Workload Console — 9444 - HTTP_PORT; 9443 - HTTPS_PORT.

> **ATENCAO / RESSALVAS DE USO:** All ten claimed ports appear in the official list: 31111 (incoming/outcoming Netman port), 31115 (HTTP_PORT), 31116 (HTTPS Protocol port), 31113 (incoming SSL connections), 31114 (DDM JobManager port), 31117 (DDM ResourceAdvisor port), 41114 (BROKER_NETMAN_PORT), 35116 (CLI connections), DWC 9444 HTTP_PORT / 9443 HTTPS_PORT. Customizability corroborated by tcpaddr/secureaddr 'Specify a value in the range from 1 to 65535' (Workstation definition, awsrgwsdefn.html) and serverinst parameter ranges.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ad/awsadenablingports.html |
| Titulo da fonte | Enabling Ports |
| Citacao de suporte | Dynamic Workload Console - 9444 - HTTP_PORT; 9443 - HTTPS_PORT |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=install |
| Status de revisao | verified |
| Tipo | other |
| verbs | install |
| Familia | 1028-ports |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 documenta portas padrão incluindo 31111, 31115, 31116, 31113, 31114, 31117, 41114, 35116, 9443 e 9444; valores podem ser customizados?


---

### 52. `hwa-install-1028-prereq-scan-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HWA 10.2.8, o scanner de pré-requisitos verifica ambiente do SO, bibliotecas UNIX, disco, memória e memória virtual, mas não verifica requisitos de componentes externos como DB2. Context: It does not check the requirements for other components, such as DB2.

> **ATENCAO / RESSALVAS DE USO:** Verbatim scope list: 'The scan verifies that: The operating system is supported for the product. On UNIX operating systems, the necessary product libraries are installed. There is enough permanent and temporary disk space... There is enough memory and virtual memory.' plus 'The scan verifies only that the environment meets the requirements of HCL Workload Automation.' The DB2 sentence is verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspipart2TWS.html |
| Titulo da fonte | Installing from the command-line interface (section: Scanning system prerequisites for HCL Workload Automation) |
| Citacao de suporte | It does not check the requirements for other components, such as DB2. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=install |
| Status de revisao | verified |
| Tipo | other |
| verbs | install |
| Familia | 1028-prereq |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, o scanner de pré-requisitos verifica ambiente do SO, bibliotecas UNIX, disco, memória e memória virtual, mas não verifica requisitos de componentes externos como DB2. Context: It does not check the requirements for other components, such as DB2.?


---

### 53. `hwa-install-1028-topology-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, uma rede pode conter MDM, BMDM, DDMs, servidores DWC e agentes; DDMs e DWC são componentes opcionais conforme a topologia. Context: An HCL Workload Automation network is composed of a master domain manager, one or more Dynamic Workload Console servers, dynamic domain managers, and dynamic agents.

> **ATENCAO / RESSALVAS DE USO:** The page continues: 'You might also have fault-tolerant agents, extended agents, standard agents connected to the master domain manager or to domain managers.' Optionality of DDM/DWC is implied by 'one or more' / 'You might also have' phrasing; BMDM presence is described in the Manager and agent types page ('Backup master: A fault-tolerant agent or domain manager capable of assuming the responsibilities of the master domain manager').

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | read_only |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsenv.html |
| Titulo da fonte | Planning your HCL Workload Automation environment |
| Citacao de suporte | An HCL Workload Automation network is composed of a master domain manager, one or more Dynamic Workload Console servers, dynamic domain managers, and dynamic agents. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=backup_master_domain_manager |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | 1028-topology |

**Perguntas relacionadas:**

- Como configurar ou solucionar problemas no dynamic agent ou broker para install?
- Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, uma rede pode conter MDM, BMDM, DDMs, servidores DWC e agentes; DDMs e DWC são componentes opcionais conforme a topologia?


---

### 54. `hwa-install-dwc-1028-params-0005`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação DWC HWA 10.2.8, os parâmetros documentados incluem rdbmstype, user, password, dbname, dbuser, dbpassword, dbhostname, dbport, wlpdir, sslkeysfolder e sslpassword; duas instâncias podem compartilhar banco remoto. Context: two Dynamic Workload Console instances on two separate workstations, sharing the same remote database.

> **ATENCAO / RESSALVAS DE USO:** dwcinst syntax on the page confirms the exact parameter set: --rdbmstype, --user, --password, --dbname, --dbuser, --dbpassword, --dbhostname, --dbport, --wlpdir, --sslkeysfolder, --sslpassword. Full parameter reference: 'Dynamic Workload Console installation - dwcinst script' (awspidwcinstsyntax.html). Procedural claim; contains password parameters - keep placeholders, never real values. | Upgrade-flow page repeats the same sentence and parameter set verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWC.html |
| Titulo da fonte | Installing the Dynamic Workload Console servers |
| Citacao de suporte | the HCL Workload Automation administrator installs two Dynamic Workload Console instances on two separate workstations, sharing the same remote database. |
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
| validation_rationale | DWC (Dynamic Workload Console) não instalado no lab (sem imagem do instalador) - validação requer DWC |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=dynamic_workload_console |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install |
| Familia | dwc-1028 |

**Perguntas relacionadas:**

- O que causa erro na resolução de local parameters em jobs e como solucionar?
- Qual a regra documentada no HWA Distributed sobre: Na instalação DWC HWA 10.2.8, os parâmetros documentados incluem rdbmstype, user, password, dbname, dbuser, dbpassword, dbhostname, dbport, wlpdir, sslkeysfolder e sslpassword; duas instâncias podem compartilhar banco remoto?


---

### 55. `hwa-install-liberty-1028-procedure-0009`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação HWA 10.2.8, Open Liberty ou WebSphere Application Server Liberty Base é requerido em workstations de componentes server e DWC; a versão deve ser consultada no Related Software Report, e a instalação do produto usa o diretório via wlpdir. Context: Find out which version... by checking the required version... in Related Software Report.

> **ATENCAO / RESSALVAS DE USO:** Page confirms: 'Find out which version of Open Liberty is required, by checking the required version of the application server in Related Software Report'; installation by extracting the ZIP; and 'The value of the <install_dir> parameter must match the value to be defined for the wlpdir parameter when installing the master domain manager and its backup, dynamic domain manager and its backup, and the Dynamic Workload Console.' serverinst docs (awspitwsinstparams.html): '--wlpdir | w wlp_directory: Open Liberty profile installation directory. This parameter is required.'

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallLiberty.html |
| Titulo da fonte | Installing Open Liberty or WebSphere Application Server Liberty Base |
| Citacao de suporte | Open Liberty or WebSphere Application Server Liberty Base is required on all workstations where you plan to install the server components and the Dynamic Workload Console. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=dynamic_workload_console |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | dwc |
| verbs | install; open; version |
| Familia | liberty-1028 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na instalação HWA 10.2.8, Open Liberty ou WebSphere Application Server Liberty Base é requerido em workstations de componentes server e DWC; a versão deve ser consultada no Related Software Report, e a instalação do produto usa o diretório via wlpdir?


---

### 56. `hwa-install-mdm-1028-certificates-0003`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na instalação de componentes server HWA 10.2.8, os certificados requeridos são ca.crt, tls.key e tls.crt; esse conjunto não é universal para todos os agentes ou componentes. Context: The required certificates are: ca.crt, tls.key, tls.crt... ensure that the same certificates are present on all components.

> **ATENCAO / RESSALVAS DE USO:** Same certificate set appears on awspiinstallMDM.html, awspiinstallDDM.html, awspiinstallDWC.html and awspiagentparams.html (agents additionally use tls.sth). MDM page adds: 'To guarantee communication between all HCL Workload Automation components, ensure that the same certificates are present on all components.' So the certificate set is shared across server components; the agent folder additionally contains tls.sth. Credential-sensitive: certificate/key material - no real paths or key material in training data. | MDM install page contains the identical certificate list (space-separated, as in the page).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | credential_sensitive |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html |
| Titulo da fonte | Server components installation - serverinst script |
| Citacao de suporte | The required certificates are: ca.crt, tls.key, tls.crt |
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
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=fault_tolerant_agent |
| Status de revisao | verified |
| Tipo | other |
| Ferramenta | mdm |
| verbs | install |
| Familia | mdm-1028 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na instalação de componentes server HWA 10.2.8, os certificados requeridos são ca?


---

### 57. `hwa-lab-10.2.8-corpus-redaction-reclass-0101`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `twsinst`

**Afirmacao / Conteudo:**

No corpus de treinamento HWA 10.2.8, foi aplicada redação de dados sensíveis e reclassificação de chunks operacionais como prática de comunidade. (1) Redação: domínios/hostnames reais de empresa foram substituídos por placeholders genéricos nos chunks de SCRIPT SHELL.pdf (inbev.com -> [COMPANY].com) e TWS.pdf (orb-data.com, stlpr160.corp.anheuser-busch.com, hostnames STLPR160/STLPR162_BKM -> [COMPANY]/[HOSTNAME]) em data/corpus.jsonl e data/quarantine.jsonl; verificação posterior confirmou 0 hits restantes. (2) Reclassificação: os 29 chunks de data/raw/TWS.pdf (runbook operacional local em PT com comandos conman/twsinst/planman e sequências de restart/tracing/datagather) foram reclassificados de internal_operational_unreviewed para internal_operational_community_practice via unofficial_validation_results.jsonl (status community_practice, training_eligible=True, disclaimer explícito), após validação com pesquisa Perplexity confirmando que os comandos individuais (conman shut/start/startmon, twsinst -new -agent, planman unlock/resync, trace configDropins, datagather) são documentados oficialmente no Troubleshooting Guide 10.2.8 e nas páginas awsrgstartstop/awsrgusingconman/awspiagentparams, mas a sequência local do runbook é customização da equipe. Resultado: quarantine caiu de 272 para 235 chunks, treino representativo subiu para 15406, e 37 chunks community_practice (8 SCRIPT SHELL + 29 TWS.pdf) entraram no train_full com training_eligible=True. Os 94 chunks internal_operational_unreviewed restantes (iws-hwa-10.2-perfreport.pdf 25 verified oficial HCL Rome Lab; awscertsmst.pdf 69 obsolete oficial IBM TWS 8.x) permanecem fora do treino por design (benchmark/legado, claims atômicos registrados separadamente).

> **ATENCAO / RESSALVAS DE USO:** Validação por pesquisa Perplexity (2026-08-19) confirmou que os comandos individuais do TWS.pdf são oficiais (Troubleshooting Guide 10.2.8, awsrgstartstop, awsrgusingconman, awspiagentparams, planman unlock/resync) mas a sequência é runbook local -> community_practice com disclaimer. perfreport e awscertsmst são documentos oficiais (verified/obsolete) mantidos fora do treino. | Fonte primária original local: redação + reclassificação no corpus e unofficial_validation_results.jsonl

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstartstop.html |
| Titulo da fonte | Starting and stopping processes on a workstation - HCL Workload Automation 10.2.8 |
| Citacao de suporte | quarantine 272->235; train_full 37 community_practice chunks (8 SCRIPT SHELL + 29 TWS.pdf); redaction 0 remaining hits (inbev/orb-data/anheuser-busch/STLPR). |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | twsinst |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar twsinst?
- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?


---

### 58. `hwa-lab-10.2.8-dwc-not-installed-0049`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** obsolete
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

No laboratorio HWA 10.2.8, o Dynamic Workload Console (DWC) nao foi instalado porque nao havia imagem do instalador DWC disponivel; a imagem instalada prove apenas o componente MDM mais os arquivos helper de banco do DWC (dblighttool, FileUpdateDwcList). O DWC e um componente separado que requer o seu proprio instalador (dwcinst) e, portanto, a validacao do DWC/Graphical Designer permaneceu pendente neste lab.

> **ATENCAO / RESSALVAS DE USO:** SUPERSEDED 2026-08-25: DWC 10.2.8 foi instalado e configurado no lab (dwcinst.sh + configureDb.sh PostgreSQL, banco TDWC, engine connection MDM_LAB via REST /dwc/api/v1/engine). Evidencia: data/evidence/lab-validation-2026-08-25-dwc-install.jsonl. Claims novas: hwa-10.2.8-dwc-install-0023..0025, hwa-10.2.8-dwc-login-0001, hwa-10.2.8-dwc-engine-connection-0001/0002.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | obsolete |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitypicalfullstack.html |
| Titulo da fonte | Typical installation scenario - HCL Workload Automation 10.2.8 |
| Citacao de suporte | Full-stack HCL Workload Automation includes Dynamic Workload Console installations on their own workstations with their own application server (dwcinst); in this lab no DWC installer image was available, so only dblighttool and FileUpdateDwcList DWC database helper files are present. |
| Coletado em | 2026-08-19 |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | reviewed |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: No laboratorio HWA 10.2.8, o Dynamic Workload Console (DWC) nao foi instalado porque nao havia imagem do instalador DWC disponivel; a imagem instalada prove apenas o componente MDM mais os arquivos helper de banco do DWC (dblighttool, FileUpdateDwcList)?


---

### 59. `hwa-lab-10.2.8-edwa-cleanup-0086`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 lab, the EDWA test objects created during validation were removed. Via 'echo y | composer delete EVENTRULE <name>' the rules LAB_FILE_TRIGGER and LAB_EVT_JS were deleted (AWSBIA290I Total objects deleted: 1 each), and 'echo y | composer delete MDMDA#EVTJS_TEST' deleted the test job stream (AWSBIA290I Total objects deleted: 1). A 'conman deployconf MDMDA' was issued to refresh the monitoring configuration. Remaining event rules in the model: UPDATEFAILURE, UPDATESTATUS, UPDATESUCCESS (the three default GenericEventPlugIn 'Upgrade' rules shipped with the lab). Trigger files (/tmp/hwa_oneshot/trigger.txt, trigger2.txt) and the job output file were removed.

> **ATENCAO / RESSALVAS DE USO:** composer delete for event rules and job streams is interactive and requires the confirmation 'y' fed via stdin (echo y | composer delete ...); the earlier pipe attempt without the 'y' produced AWSDEI007E 'Too many characters in input line' and deleted 0 objects. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer delete

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsisnetvbmevents.html |
| Titulo da fonte | EDWA test object cleanup |
| Citacao de suporte | AWSBIA290I Total objects deleted: 1 (x3). |
| Coletado em | 2026-08-18 |
| Classificacao de risco | destructive |
| Capacidade | upgrade |
| Modo de operacao | guarded_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['edwa', 'composer', 'conman'], result=AWSBIA290I Total objects deleted: 1 (x3). | composer delete for event rules and job streams is interactive and requires the confirmation 'y' fed via stdin (echo y | composer delete ...); the earlier pipe attempt without the 'y' produced AWSDEI007E 'Too many characters in input line' and deleted 0 objects., validated_at=2026-08-18, evidence_file=lab-validation-2026-08-18-edwa-cleanup.jsonl |
| Terminologia normalizada | message=AWSBIA290I, command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSBIA290I no HWA?
- Como solucionar ou diagnosticar o erro AWSBIA290I no HWA?
- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar upgrade?


---

### 60. `hwa-lab-10.2.8-first-jnextplan-0003`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the WSL2 laboratory, JnextPlan -for 0000 created the initial preproduction and production plans and loaded the resulting Symphony file into the database after MDM installation.

> **ATENCAO / RESSALVAS DE USO:** Operational observation, not a universal version claim. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /opt/hwa/TWS/bin/JnextPlan

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | JnextPlan laboratory execution |
| Citacao de suporte | AWSJPL709I During the creation of a production plan, the planner has successfully created a new preproduction plan. AWSJCL058I The production plan (Symnew) has been successfully created. AWSJCL074I Symphony file successfully loaded in Database. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['jnextplan'], result=AWSJPL709I During the creation of a production plan, the planner has successfully created a new preproduction plan. AWSJCL058I The production plan (Symnew) has been successfully created. AWSJCL074I Symphony file successfully loaded in Database. | Operational observation, not a universal version claim., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], command=planman, component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?


---

### 61. `hwa-lab-10.2.8-limit-cpu-0074`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the HWA laboratory, the conman command 'lc MDMDA;5;noask' (limit cpu) was accepted ('Command forwarded to batchman for MDMDA'), demonstrating the limit cpu command syntax. Earlier the post-install MDM banner showed 'Limit: 0, Fence: 0'. A job stream whose jobs were HOLD due to the low limit ran to completion (BLK4 EXEC, SUC4 SUCC) once the limit condition cleared, confirming limit is the concurrency gate.

> **ATENCAO / RESSALVAS DE USO:** Selector ambiguity (AWSBHU048E) avoided by using short form 'lc <wks>;<n>;noask'. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman lc MDMDA;5;noask

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | limit cpu command |
| Citacao de suporte | Command forwarded to batchman for MDMDA; jobs ran after limit cleared. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['confirm', 'fence', 'conman'], result=Command forwarded to batchman for MDMDA; jobs ran after limit cleared. | Selector ambiguity (AWSBHU048E) avoided by using short form 'lc <wks>;<n>;noask'., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-limit-cpu.jsonl |
| Terminologia normalizada | command=conman |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar install?


---

### 62. `hwa-lab-10.2.8-orphan-reverify-0090`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

All 93 orphaned SFT-referenced claim_ids (lost in the 2026-08-18 claims.jsonl truncation incident) were re-verified against official HCL documentation and consolidated back into data/evidence/claims.jsonl. The claim text and supporting context for each orphan were recovered from the approved SFT answers (data/sft/*.jsonl) that had been generated from the original verified claims. Four parallel hwa-source-verifier research batches (conman-ops 15, show-cmds 13, install-upgrade 22, plan-rest-dwc 43) opened the official help.hcl-software.com pages (with URL corrections where the inferred slugs 404'd, e.g. awsrgconmanretcod.html, awsadoptman.html, awsrgevtsize.html, awsrgcancelsched.html, awsrgplretrplan.html, awsrgplresyncplan.html, awsrgplchksyncplan.html, awsrgplunlkplan.html, awsrgchddjjch.html, eqqg1JWTAPIKey.html, r_kill.html, awsrgcreateextract.html, awsadtunemirr.html, awspiinstallDWCupgr.html, awspiparallelupgradefrom94TLS.html, awspiupgrading.html, awstrmakeplan5-8, awstrswitchplan3, awsrgstdlistformat5.html) and captured verbatim supporting quotes. Result: 83 re-verified as verified, 1 as version_dependent (hwa-10.2.8-dwc-mdm-distinct-0008: the DWC>=engine version rule was not found in the v1028 pages opened), and 9 as insufficient_evidence (records whose recovered claim text was empty: hwa-10.2.8-startmon-stopmon-0001, hwa-10.2.8-srv-traces-0003, hwa-10.2.8-upgrade-certs-required-0005, hwa-10.2.8-upgrade-gskit-openssl-0004, hwa-10.2.8-upgrade-order-0006, hwa-10.2.8-dwc-trace-configdropins-0001, hwa-10.2.8-dwc-trace-template-0002, hwa-10.2.8-ocli-release-job-persist-0001, hwa-10.2.8-mdm-aes-keys-0005 — these must be excluded from approved SFT data until the original claim text is recovered). claims.jsonl now has 772 valid records (705 verified); every SFT-referenced claim_id resolves to an existing claim.

> **ATENCAO / RESSALVAS DE USO:** Research used Perplexity MCP for URL discovery plus official-page fetch for verbatim quotes. The 9 insufficient_evidence records have empty recovered claim text (their original claim text was not preserved in the SFT answers); they stay registered but are excluded from SFT promotion. Version scoping respected: 10.2.0 claims (hwa-liberty-install-10.2.0-0001, hwa-distributed-cancel-sched-pend-10.2.0-001) and 9.4/9.5 claims (hwa-official-awsjcl070i-9.4-0001, hwa-rest-twsd-31116-official-0022) keep their original version.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgconmancmds.html |
| Titulo da fonte | Conman commands - HCL Workload Automation 10.2.8 |
| Citacao de suporte | claims.jsonl 772 valid records; 93/93 orphan claim_ids resolved; 83 re-verified, 9 insufficient_evidence, 1 version_dependent. |
| Coletado em | 2026-08-18 |
| Classificacao de risco | read_only |
| Capacidade | install |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | command=conman |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Como utilizar o utilitário optman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no optman para gerenciar install?
- Como utilizar o utilitário conman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no conman para gerenciar install?


---

### 63. `hwa-lab-10.2.8-postinstall-limit-fence-check-0029`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

A mandatory HWA post-installation check must inspect workstation LIMIT, FENCE, link state and JobManager flag before diagnosing READY jobs. In the laboratory, MDMDA initially had LIMIT 0 and FENCE 0; raising LIMIT to 10 allowed priority-10 dynamic-agent jobs to execute.

> **ATENCAO / RESSALVAS DE USO:** FENCE was 0 in the lab. A nonzero fence can prevent jobs with priority less than or equal to the fence from launching. This operational checklist was missing from the prior dataset despite command-level limit/fence coverage. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local conman validation plus https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | Post-installation LIMIT and FENCE validation |
| Citacao de suporte | Before: MDMDA ... LIMIT 0 ...; after lc MDMDA;10, jobs started and completed successfully. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['fence', 'link'], result=Before: MDMDA ... LIMIT 0 ...; after lc MDMDA;10, jobs started and completed successfully. | FENCE was 0 in the lab. A nonzero fence can prevent jobs with priority less than or equal to the fence from launching. This operational checklist was missing from the prior dataset despite command-level limit/fence coverage., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-postinstall-limit-fence.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=master_domain_manager |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: A mandatory HWA post-installation check must inspect workstation LIMIT, FENCE, link state and JobManager flag before diagnosing READY jobs?


---

### 64. `hwa-lab-10.2.8-serverinst-0002`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the WSL2 laboratory, HWA 10.2.8 serverinst.sh completed MDM installation in /opt/hwa after supplying Open Liberty, PostgreSQL, SSL certificate directory, a distinct workstation name and display name, and a pre-existing wauser account.

> **ATENCAO / RESSALVAS DE USO:** Lab-only observation. The initial attempt failed because thiscpu and displayname were identical; a previous attempt also exposed a Liberty permissions requirement. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /root/hwa/extracted/TWS/LINUX_X86_64/serverinst.sh

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | serverinst.sh laboratory execution |
| Citacao de suporte | WAINST061I Performing post-configuration steps. WAINST052I The command waPostConfigure has completed successfully. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | credential_sensitive |
| Capacidade | install |
| Modo de operacao | sensitive_handling |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['serverinst.sh laboratory execution'], result=WAINST061I Performing post-configuration steps. WAINST052I The command waPostConfigure has completed successfully. | Lab-only observation. The initial attempt failed because thiscpu and displayname were identical; a previous attempt also exposed a Liberty permissions requirement., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17.jsonl |
| Terminologia normalizada | command=display |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar install?


---

### 65. `hwa-lab-10.2.8-thiscpu-displayname-scope-0008`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `twsinst`

**Afirmacao / Conteudo:**

In the HWA 10.2.8 laboratory, the nested twsinst invocation made by serverinst with -agent both rejected equal -thiscpu and -displayname values with AWSFAB164E. This is an observed constraint of that invocation; it is not evidence of a universal rule that the parameters must always differ.

> **ATENCAO / RESSALVAS DE USO:** Official references distinguish thiscpu as the installation workstation and displayname as the dynamic-agent name. The official agent reference also states that thiscpu cannot equal the master workstation name: https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /opt/hwa/TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | nested twsinst validation |
| Citacao de suporte | AWSFAB164E The values specified for "-thiscpu" and "-displayname" cannot be the same. |
| Coletado em | 2026-08-17 |
| Classificacao de risco | read_only |
| Capacidade | twsinst |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Terminologia normalizada | message=AWSFAB164E |
| Status de revisao | verified |

**Perguntas relacionadas:**

- Qual é o significado da mensagem de erro AWSFAB164E no HWA?
- Como solucionar ou diagnosticar o erro AWSFAB164E no HWA?
- Como utilizar o utilitário serverinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no serverinst para gerenciar twsinst?


---

### 66. `hwa-lab-10.2.8-tooling-0067`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the HWA laboratory, the composer/planman/conman tooling available included composer validate/add, planman showinfo/confirm, conman rerun/confirm/cancel/altpri. No separate audit, report, fbcount, dataextract, or workload-app export/import commands are exposed as standalone commands in this 10.2.8 installation; these capabilities are not directly invokable from the CLI tooling tested.

> **ATENCAO / RESSALVAS DE USO:** These features may require the broker/gateway, Dynamic Workload Console, or workload-app specific tooling not present in the direct MDM CLI environment. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local composer/planman/conman help and command attempts

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | medium |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html |
| Titulo da fonte | Tooling command availability |
| Citacao de suporte | 'dataextract: command not found'; no manual entry for audit/report/fbcount. |
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
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['rerun', 'confirm', 'cancel', 'composer', 'conman', 'planman'], result='dataextract: command not found'; no manual entry for audit/report/fbcount. | These features may require the broker/gateway, Dynamic Workload Console, or workload-app specific tooling not present in the direct MDM CLI environment., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-tooling.jsonl |
| Terminologia normalizada | command=composer |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Como utilizar o utilitário composer no HCL Workload Automation?
- Qual a sintaxe ou procedimento no composer para gerenciar install?
- Como utilizar o utilitário planman no HCL Workload Automation?
- Qual a sintaxe ou procedimento no planman para gerenciar install?


---

### 67. `hwa-lab-10.2.8-wauser-profile-0005`

**Nivel de evidencia:** VALIDADO EM LABORATORIO (comportamento de runtime observado)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

In the WSL2 HWA 10.2.8 laboratory, the installation user is wauser and its login profile sources /opt/hwa/TWS/tws_env.sh; a new login shell then exposes TWS_TISDIR, TISDIR, UNISONHOME, UNISONWORK, JAVA_HOME, PATH and LD_LIBRARY_PATH.

> **ATENCAO / RESSALVAS DE USO:** The installed image used tws_env.sh, not twa_env.sh. This is an environment-specific operational observation. [Observado em laboratório HWA 10.2.8 WSL2, status registrado como verified por validação prática] | Fonte primária original local: local execution: /home/wauser/.profile and /opt/hwa/TWS/tws_env.sh

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Status do conhecimento | verified |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmanageobjconman.html |
| Titulo da fonte | wauser login environment laboratory validation |
| Citacao de suporte | HCL Workload Scheduler Environment Successfully Set !!! TWS_TISDIR=/opt/hwa/TWS UNISONWORK=/opt/hwa/TWSDATA UNISONHOME=/opt/hwa/TWS |
| Coletado em | 2026-08-17 |
| Classificacao de risco | mutating |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed; Linux x86_64; WSL2 Ubuntu 22.04 |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| lab_validation | lab_environment=WSL2 Ubuntu 22.04, HWA 10.2.8.00 (MDM workstation, batchman LIVES) (Distributed; Linux x86_64; WSL2 Ubuntu 22.04), tested_commands=['wauser login environment laboratory validation'], result=HCL Workload Scheduler Environment Successfully Set !!! TWS_TISDIR=/opt/hwa/TWS UNISONWORK=/opt/hwa/TWSDATA UNISONHOME=/opt/hwa/TWS | The installed image used tws_env.sh, not twa_env.sh. This is an environment-specific operational observation., validated_at=2026-08-17, evidence_file=lab-validation-2026-08-17-profile.jsonl |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=install |
| Status de revisao | lab_validated |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: In the WSL2 HWA 10.2.8 laboratory, the installation user is wauser and its login profile sources /opt/hwa/TWS/tws_env?


---

### 68. `hwa-liberty-install-10.2.0-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Na documentação HWA Distributed 10.2.0, Open Liberty é requerido nos nós que receberão componentes server ou DWC; pode ser instalado extraindo o arquivo ZIP, e o diretório de instalação deve corresponder ao parâmetro wlpdir dos instaladores de MDM, backup MDM, DDM, backup DDM e DWC. Context: Open Liberty is required on all workstations where you plan to install the server components and the Dynamic Workload Console.

> **ATENCAO / RESSALVAS DE USO:** Terminology caveat: the v10.2.0 documentation names the required runtime 'WebSphere Application Server Liberty Base' (the 'Open Liberty' name appears in later fix packs such as 10.2.3+); the page confirms 'You can quickly install WebSphere Application Server Liberty Base by extracting an archive file on all supported platforms'. The wlpdir-correspondence statement is verbatim in the v10.2.8 Liberty page and wlpdir is the documented Liberty installation directory parameter of serverinst/dwcinst in both versions. This 10.2.0 evidence cannot by itself prove the identical runtime procedure for 10.2.8 - do not generalize across versions. | Corroborating page is v1028 while the claim is 10.2.0 (both 10.2.x Distributed).

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.0 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | medium |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v102/distr/src_pi/awspiinstallLiberty.html |
| Titulo da fonte | Installing WebSphere Application Server Liberty Base |
| Citacao de suporte | WebSphere Application Server Liberty Base is required on all workstations where you plan to install the server components and the Dynamic Workload Console. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.0 |
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
| Ferramenta | dwc |
| verbs | install; open; plan |
| Familia | install-10.2.0 |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: Na documentação HWA Distributed 10.2.0, Open Liberty é requerido nos nós que receberão componentes server ou DWC; pode ser instalado extraindo o arquivo ZIP, e o diretório de instalação deve corresponder ao parâmetro wlpdir dos instaladores de MDM, backup MDM, DDM, backup DDM e DWC?


---

### 69. `hwa-official-stageman-10.2.8-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `install`

**Afirmacao / Conteudo:**

Em HWA Distributed 10.2.8, Stageman leva job streams não concluídos para o novo plano, arquiva o production plan antigo, instala o novo production plan e envia uma cópia de Symphony a domain managers e agents durante a inicialização. Context: The stageman command carries forward uncompleted job streams, archives the old production plan, and installs the new production plan.

> **ATENCAO / RESSALVAS DE USO:** Verified verbatim on the official v1028 page (awsrgstageman.html 404s; correct page is awsrgchddjjch.html). Stageman requires build access to the Symphony file.

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
| Citacao de suporte | The stageman command carries forward uncompleted job streams, archives the old production plan, and installs the new production plan. A copy of Symphony, is sent to domain managers and agents as part of the initialization process for the new production plan. |
| Coletado em | 2026-08-18 |
| Capacidade | install |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=fault_tolerant_agent |
| Status de revisao | verified |
| Tipo | other |
| verbs | plan |
| Familia | stageman-10.2.8 |

**Perguntas relacionadas:**

- Qual a função do arquivo Symphony e como ele é gerado ou sincronizado?
- Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, Stageman leva job streams não concluídos para o novo plano, arquiva o production plan antigo, instala o novo production plan e envia uma cópia de Symphony a domain managers e agents durante a inicialização?


---

### 70. `hwa-themaster-domain-manager-0001`

**Nivel de evidencia:** FATO OFICIAL (documentacao HCL primaria)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `twsinst`

**Afirmacao / Conteudo:**

O nome de workstation padrão do master domain manager no HCL Workload Automation é MASTER, e não THEMASTER, conforme a documentação oficial do parâmetro -master do script twsinst.

> **ATENCAO / RESSALVAS DE USO:** A afirmação do usuário de que THEMASTER é o nome padrão do master domain manager é contradita pela documentação oficial, que documenta MASTER como valor padrão do parâmetro -master e registra o master domain manager no banco como 'master'. THEMASTER não aparece como nome reservado/padrão na documentação oficial.

| Atributo | Valor |
| --- | --- |
| Terminologia normalizada | THEMASTER=nome de workstation não documentado como padrão, master domain manager=master domain manager, MASTER=nome de workstation padrão documentado |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | contradicted |
| Confianca | high |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html |
| Titulo da fonte | Agent installation parameters - twsinst script |
| Citacao de suporte | -master workstation ... If not specified, the default value is MASTER. |
| Coletado em | 2026-08-17 |
| Responsavel | hwa-source-verifier |
| Status de revisao | draft |
| Classificacao de risco | read_only |
| Capacidade | twsinst |
| Modo de operacao | read |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |

**Perguntas relacionadas:**

- Como utilizar o utilitário twsinst no HCL Workload Automation?
- Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?


---

### 71. `hwa-upgrade-1028-rollback-0001`

**Nivel de evidencia:** FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)
**Status do conhecimento:** current
**Taxonomia:** `installation_upgrade` / `upgrade`

**Afirmacao / Conteudo:**

HWA informa que registros de banco criados por recursos da nova versão podem impedir rollback para a versão anterior; backup não equivale a downgrade suportado. Context: You cannot roll back your environment to a previous version.

> **ATENCAO / RESSALVAS DE USO:** Verbatim from the v10.2.8 'Upgrading' overview, stated after the parallel-upgrade description. The claim's added assertion that backup/restore is not a supported downgrade path is a reasonable inference from this sentence (incompatible database records) but is not separately documented - keep the statement scoped to 'cannot roll back'. Upgrade procedure claim; no secrets. | v10.2.0 Upgrading page; version caveat: both 10.2.x Distributed, sentence verbatim.

| Atributo | Valor |
| --- | --- |
| Produto | HCL Workload Automation |
| Versao | 10.2.8 |
| Plataforma | Distributed |
| Status do conhecimento | verified |
| Confianca | high |
| Classificacao de risco | mutating |
| Fonte (URL) | https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiupgrading.html |
| Titulo da fonte | Upgrading |
| Citacao de suporte | Using the new features introduced with the latest release creates new records in the database which are not compatible with previous versions and therefore you cannot roll back your environment to a previous version. |
| Coletado em | 2026-08-18 |
| Capacidade | upgrade |
| Modo de operacao | guided_action |
| Escopo de versao | 10.2.8 |
| Escopo de plataforma | Distributed |
| Pre-condicoes | Confirmar versão, plataforma, autorização e backup/rollback aplicáveis. |
| Impacto | Pode alterar estado operacional; avaliar o escopo antes da execução. |
| Reversibilidade | Seguir o procedimento oficial de reversão ou restauração aplicável. |
| Criterio de parada | Interromper diante de divergência de versão, evidência, autorização ou resultado inesperado. |
| validation_scope | common_practice_unvalidated |
| validation_rationale | Instalação/upgrade/rollback/TLS requerem cenário de instalação dedicado - não reproduzível no lab atual |
| Terminologia normalizada | product_standard=HCL Workload Automation, legacy_aliases=['Tivoli Workload Scheduler', 'TWS', 'Maestro'], component=upgrade |
| Status de revisao | verified |
| Tipo | other |
| verbs | rollback; upgrade; version |
| Familia | 1028-rollback |

**Perguntas relacionadas:**

- Qual a regra documentada no HWA Distributed sobre: HWA informa que registros de banco criados por recursos da nova versão podem impedir rollback para a versão anterior; backup não equivale a downgrade suportado?


---
