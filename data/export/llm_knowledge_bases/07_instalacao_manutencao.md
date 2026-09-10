# INSTALACAO & MANUTENCAO

> Total de tópicos canônicos cobertos nesta seção: 57

---

### 1. hwa-10.2.4-distributed-password-encryption-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.4 (distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation, é opcional criptografar as senhas usadas na instalação, upgrade e gestão; o comando secure usa o método AES e imprime a senha criptografada na tela ou a salva em arquivo, e senhas de operadores PeopleSoft exibidas no console aparecem como asteriscos.

**Plataforma / Validação:** distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation, é opcional criptografar as senhas usadas na instalação, upgrade e gestão; o comando secure usa o método AES e imprime a senha criptografada na tela ou a salva em arquivo, e senhas de operadores PeopleSoft exibidas no console aparecem como asteriscos?*

---

### 2. hwa-10.2.8-AWSWUI-0001E-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; Dynamic Workload Console installation) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWSUI0001E indica que o user name tem um número incorreto de caracteres (intervalo permitido entre 3 e 60); a causa documentada é um valor de user name fora do intervalo permitido, e a recuperação é editar o response file (instalação silenciosa) ou reentrar o user name dentro do intervalo (instalação por wizard).

**Plataforma / Validação:** distributed; Dynamic Workload Console installation

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSWUI0001E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSWUI0001E no HWA?*
- *Qual a ação recomendada para a mensagem AWSUI0001E no DWC?*
- *Qual é o significado da mensagem de erro AWSUI0001E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0001E no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSWUI0001E no HWA e qual ação é recomendada?*

---

### 3. hwa-10.2.8-AWSWUI-0018E-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; Dynamic Workload Console installation) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWSUI0018E indica que são necessários privilégios de administrador para executar a instalação; a causa documentada é que privilégios de administrador são requeridos, e a recuperação é fazer login como Administrador e lançar uma nova instalação.

**Plataforma / Validação:** distributed; Dynamic Workload Console installation

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0018E no HWA?*
- *Qual é o significado da mensagem de erro AWSWUI0018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSWUI0018E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0018E no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSWUI0018E no HWA e qual ação é recomendada?*

---

### 4. hwa-10.2.8-aida-intro-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: aida > introduction [aida_install]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o AI Data Advisor (AIDA) e um componente de IA/ML (disponivel desde V10.1) que analisa metricas historicas de workload coletadas pelo HWA, preve padroes futuros e detecta anomalias em tendencias de KPIs (ex.: jobs in plan by status, jobs in plan by workstation), gerando alertas exibidos no Workload Dashboard do Dynamic Workload Console e notificaveis por email. O pacote de instalacao Docker (HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz) contem 9 imagens pre-carregadas (hclcr.io/wa/workload-automation/hcl-aida-{ad,exporter,email,nginx,orchestrator,predictor,redis,config,ui}:10.2.8) e um diretorio docker-deployment com AIDA.sh, docker-compose.yml, common.env, Dockerfiles por servico, config/, nginx/cert/, redis/, keycloak/ e Licenses/.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como o AIDA atua na detecção de anomalias e predição de problemas no HWA?*

---

### 5. hwa-10.2.8-capacity-bm-look-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
As opções localopts do HCL Workload Automation 10.2.8 relacionadas a performance têm padrões documentados: bm look (intervalo mínimo do batchman antes de varrer o arquivo de controle de produção) com padrão 5 segundos em instalação nova e 15 segundos em upgrade, e bm read (máximo de segundos que o batchman espera por mensagem no intercom.msg) com padrão 3 segundos em instalação nova e 10 segundos em upgrade.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: As opções localopts do HCL Workload Automation 10.2.8 relacionadas a performance têm padrões documentados: bm look (intervalo mínimo do batchman antes de varrer o arquivo de controle de produção) com padrão 5 segundos em instalação nova e 15 segundos em upgrade, e bm read (máximo de segundos que o batchman espera por mensagem no intercom?*

---

### 6. hwa-10.2.8-cert-permissions-version-dep-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Certificate file permissions (644 vs 755) in HWA 10.2.8 are flow-dependent and must match the exact installation procedure.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Certificate file permissions (644 vs 755) in HWA 10.2.8 are flow-dependent and must match the exact installation procedure?*

---

### 7. hwa-10.2.8-dbmigration-awspiupgrddb-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > migration [migration]]`

**Regra Canônica / Evidência:**
A migração do banco de dados dos componentes de servidor do HCL Workload Automation 10.2.8 é executada pelo utilitário awspiupgrddb, que atualiza o esquema do banco de dados para a versão atual do produto.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A migração do banco de dados dos componentes de servidor do HCL Workload Automation 10.2.8 é executada pelo utilitário awspiupgrddb, que atualiza o esquema do banco de dados para a versão atual do produto?*

---

### 8. hwa-10.2.8-directupgrade-direct-upgrade-paths-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 suporta upgrade direto (direct upgrade) a partir das versões 9.5.0.x ou 10.x.x, sem necessidade de instalação paralela, seguindo os passos documentados para a versão 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 suporta upgrade direto (direct upgrade) a partir das versões 9.5.0.x ou 10.x?*

---

### 9. hwa-10.2.8-dwc-cert-ownership-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
UNIX certificate files in the documented DWC installation flow must be owned by the MDM installation user. Context: Certificate files on UNIX must be owned by the user account running the installation.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: UNIX certificate files in the documented DWC installation flow must be owned by the MDM installation user?*

---

### 10. hwa-10.2.8-dwc-certs-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
In HWA 10.2.8, the documented DWC installation and upgrade flow requires ca.crt, tls.key, and tls.crt certificates. Context: Ensure you have the required certificate files ca.crt, tls.key, and tls.crt available before running the installer.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: In HWA 10.2.8, the documented DWC installation and upgrade flow requires ca?*

---

### 11. hwa-10.2.8-dwc-install-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o Dynamic Workload Console e instalado como um componente distinto por meio do script dwcinst (dwcinst.sh em UNIX/Linux, dwcinst.vbs em Windows), separado da instalacao do MDM (serverinst); o processo e iniciado a partir do diretorio da imagem de instalacao do DWC e usa um arquivo de propriedades (dwcinst.properties) para os valores default.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário serverinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no serverinst para gerenciar install?*

---

### 12. hwa-10.2.8-dwc-install-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os pre-requisitos do Dynamic Workload Console incluem a instalacao de um runtime Web (WebSphere Application Server Liberty Base ou Open Liberty) e de um banco de dados suportado para o DWC (DB2, DB2 for z/OS, Oracle, Informix, MSSQL ou PostgreSQL), que deve existir antes da primeira instalacao do DWC; os requisitos de software detalhados sao publicados no artigo de System Requirements da HCL Support.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os pre-requisitos do Dynamic Workload Console incluem a instalacao de um runtime Web (WebSphere Application Server Liberty Base ou Open Liberty) e de um banco de dados suportado para o DWC (DB2, DB2 for z/OS, Oracle, Informix, MSSQL ou PostgreSQL), que deve existir antes da primeira instalacao do DWC; os requisitos de software detalhados sao publicados no artigo de System Requirements da HCL Support?*

---

### 13. hwa-10.2.8-dwc-install-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, os caminhos default de instalacao do Dynamic Workload Console sao /opt/wa/DWC em UNIX/Linux e %ProgramFiles%\wa\DWC em Windows; na arquitetura tipica o DWC e instalado em workstations proprias (por exemplo dois DWC em dois nos distintos compartilhando o mesmo banco remoto), separadas do master domain manager e dos agents.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, os caminhos default de instalacao do Dynamic Workload Console sao /opt/wa/DWC em UNIX/Linux e %ProgramFiles%\wa\DWC em Windows; na arquitetura tipica o DWC e instalado em workstations proprias (por exemplo dois DWC em dois nos distintos compartilhando o mesmo banco remoto), separadas do master domain manager e dos agents?*

---

### 14. hwa-10.2.8-dwc-install-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > configuredb [configuredb]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o script configureDb.sh do kit DWC com RDBMS_TYPE=POSTGRESQL e COMPONENT_TYPE=DWC cria automaticamente o banco do DWC se ele nao existir (mensagem WAINST0534W 'The database TDWC does not exist. It will be created.') e popula os schemas tdwc e fed (Federator, instalado junto desde 10.2.3); em PostgreSQL o rc=6 do dbTool (banco inexistente) e tratado como condicao normal de criacao, nao como erro.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o script configureDb?*

---

### 15. hwa-10.2.8-dwc-install-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > dwcinst [dwcinst]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o dwcinst.sh do kit DWC instala o servidor Dynamic Workload Console no Open Liberty informado por --wlpdir (obrigatorio) e usa WLP_USER_DIR=${DWC_INST_DIR}/usr (os arquivos do servidor dwcServer ficam em ${DWC_INST_DIR}/usr/servers/dwcServer, nao no diretorio usr do Liberty), com dados/logs em DWC_DATA_dir (por default ${DWC_INST_DIR}/DWC_DATA); o datasource jdbc/dwcdb e configurado para o banco informado (ex.: jdbc:postgresql://host:port/TDWC) e as senhas sao gravadas como {aes} criptografado com a chave wlp.password.encryption.key do passphrase_variables.xml.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o dwcinst?*

---

### 16. hwa-10.2.8-dwc-install-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > dwc_user [dwc_user]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o usuario administrador do DWC (parametro --user, default dwcadmin) e o usuario do SO que o servidor dwcServer usa para executar (WA_USER em appservertools/setEnv.sh) e o principal do basicRegistry (user.twsuser.id/user.twsuser.password no wauser_variables.xml, grupo Admins via admin.group.name); e possivel trocar esse usuario apos a instalacao editando wauser_variables.xml (com senha {aes} re-gerada com a mesma chave wlp.password.encryption.key), ajustando WA_USER e a ownership da arvore DWC_INST_DIR, sem reinstalar.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o usuario administrador do DWC (parametro --user, default dwcadmin) e o usuario do SO que o servidor dwcServer usa para executar (WA_USER em appservertools/setEnv?*

---

### 17. hwa-10.2.8-dwcinst-params-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > dwcinst [dwcinst]]`

**Regra Canônica / Evidência:**
The dwcinst command documents database parameters, required --wlpdir, and SSL options --sslkeysfolder and --sslpassword. Context: dwcinst syntax accepts database parameters, --wlpdir, and SSL parameters --sslkeysfolder and --sslpassword.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: The dwcinst command documents database parameters, required --wlpdir, and SSL options --sslkeysfolder and --sslpassword?*

---

### 18. hwa-10.2.8-incident-awsjom179-e-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
A mensagem AWSJOM179E no HCL Workload Automation 10.2.8 é emitida ao tentar excluir a definição de uma workstation (via Composer ou Dynamic Workload Console) e o servidor workload broker está inacessível, com o texto 'An error occurred deleting definition of the workstation {0}. The workload broker server is currently unreachable.' Causa documentada: um dynamic domain manager foi removido sem seguir o procedimento de desinstalação descrito no Planning and Installation. Recuperação documentada: verificar que o dynamic domain manager foi realmente excluído (não apenas indisponível) e excluir as workstations conectadas a ele com o comando 'composer del ws <workstation_name>;force'.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM179E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM179E no HWA?*
- *Qual é o significado da mensagem de erro AWSJOM179 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM179 no HWA?*
- *Qual é o significado da mensagem de erro AWSJOM179E no HWA e qual ação é recomendada?*

---

### 19. hwa-10.2.8-incident-variables-upgrade-0121

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: incidents > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Sintoma: apos um upgrade, variaveis globais nao sao resolvidas. Causa: durante o upgrade, todas as statements do arquivo de seguranca relativas as variaveis globais foram copiadas pelo installation wizard para uma default variable table no novo arquivo de seguranca; as variaveis globais ficam desabilitadas e so podem ser usadas atraves das variable tables. Se o arquivo de seguranca for reconstruido usando o output do dumpsec anterior como input, o problema ocorre. Fonte: HCL Troubleshooting Guide 10.2.8.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Sintoma: apos um upgrade, variaveis globais nao sao resolvidas?*
- *O que causa e como solucionar o problema: apos um upgrade, variaveis globais nao sao resolvidas?*

---

### 20. hwa-10.2.8-install-configure-db-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação limpa do HCL Workload Automation 10.2.8, o banco de dados deve ser criado e populado (script configureDb) antes da instalação dos componentes; os componentes são então instalados na ordem: master domain manager e backup master domain manager, dynamic domain manager e backup dynamic domain manager, servidores Dynamic Workload Console e, por fim, dynamic agents.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*
- *Qual a regra documentada no HWA Distributed sobre: Na instalação limpa do HCL Workload Automation 10.2.8, o banco de dados deve ser criado e populado (script configureDb) antes da instalação dos componentes; os componentes são então instalados na ordem: master domain manager e backup master domain manager, dynamic domain manager e backup dynamic domain manager, servidores Dynamic Workload Console e, por fim, dynamic agents?*

---

### 21. hwa-10.2.8-install-configure-db-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
O script configureDb cria e popula o banco de dados do HCL Workload Automation 10.2.8 e aceita os parâmetros rdbmstype, dbhostname, dbport, dbname, dbuser e dbpassword; os bancos suportados incluem DB2, PostgreSQL, MSSQL e Oracle; no DB2, a criação do banco e das tablespaces exige um dos grants mínimos SYSADM, SYSCTRL ou SELECT privilege no administrative view PRIVILEGES.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: O script configureDb cria e popula o banco de dados do HCL Workload Automation 10.2.8 e aceita os parâmetros rdbmstype, dbhostname, dbport, dbname, dbuser e dbpassword; os bancos suportados incluem DB2, PostgreSQL, MSSQL e Oracle; no DB2, a criação do banco e das tablespaces exige um dos grants mínimos SYSADM, SYSCTRL ou SELECT privilege no administrative view PRIVILEGES?*

---

### 22. hwa-10.2.8-install-dwcinst-install-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
O Dynamic Workload Console (DWC) do HCL Workload Automation 10.2.8 é instalado como componente distinto usando o script dwcinst (dwcinst.sh/dwcinst.vbs), com parâmetros como --rdbmstype, --dbname, --dbuser, --dbpassword, --dbport, --dbhostname, --wlpdir, --sslkeysfolder, --sslpassword, --user e --password; o DWC é um componente separado do master domain manager/dynamic domain manager (serverinst) e dos agents (twsinst).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário serverinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no serverinst para gerenciar install?*
- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar install?*

---

### 23. hwa-10.2.8-install-serverinst-install-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
O master domain manager e o backup master domain manager do HCL Workload Automation 10.2.8 são instalados com o script serverinst.sh (serverinst.vbs no Windows), usando parâmetros prefixados --rdbmstype, --dbhostname, --dbport, --dbname, --dbuser, --dbpassword, --wauser, --wapassword, --wlpdir, --sslkeysfolder, --sslpassword, --inst_dir e --licenseserverid; os valores podem ser definidos no arquivo serverinst.properties (localizado em image_location/TWS/interp_name) e, se um parâmetro for definido tanto no arquivo quanto na linha de comando, o valor da linha de comando tem precedência.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário serverinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no serverinst para gerenciar install?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 24. hwa-10.2.8-install-sslkeysfolder-certs-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Certificados são obrigatórios na instalação do HCL Workload Automation 10.2.8: a pasta --sslkeysfolder deve conter os arquivos ca.crt, tls.key e tls.crt e a senha é fornecida com --sslpassword; o programa de instalação processa automaticamente os arquivos keystore e truststore a partir desses certificados PEM.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Certificados são obrigatórios na instalação do HCL Workload Automation 10.2.8: a pasta --sslkeysfolder deve conter os arquivos ca?*

---

### 25. hwa-10.2.8-parallel-upgrade-tls12-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Em um upgrade paralelo do HCL Workload Automation de 9.4.0.x para 10.2.8, TLS 1.2 deve ser habilitado no master domain manager 9.4 em nível anterior para permitir a comunicação entre componentes 9.4 e 10.2.8. Context: In back-level environments, for example 9.4, SSL is not enabled by default and TLS version 1.2 needs to be enabled on the back-level master domain manager to enable communication.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em um upgrade paralelo do HCL Workload Automation de 9.4.0.x para 10.2.8, TLS 1.2 deve ser habilitado no master domain manager 9.4 em nível anterior para permitir a comunicação entre componentes 9.4 e 10.2.8. Context: In back-level environments, for example 9.4, SSL is not enabled by default and TLS version 1.2 needs to be enabled on the back-level master domain manager to enable communication?*

---

### 26. hwa-10.2.8-postgresql-awspicreate-postgre-sqltables-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > database [postgresql]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o procedimento documentado para criar e popular o banco de dados PostgreSQL do master domain manager e do Dynamic Workload Console utiliza os guias 'Creating and populating the database for PostgreSQL for the master domain manager' e 'Creating and populating the database for PostgreSQL for the Dynamic Workload Console' da documentacao oficial (awspicreatePostgreSQLtables e awspicreatePostgreSQLtables_DWC).

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o procedimento documentado para criar e popular o banco de dados PostgreSQL do master domain manager e do Dynamic Workload Console utiliza os guias 'Creating and populating the database for PostgreSQL for the master domain manager' e 'Creating and populating the database for PostgreSQL for the Dynamic Workload Console' da documentacao oficial (awspicreatePostgreSQLtables e awspicreatePostgreSQLtables_DWC)?*

---

### 27. hwa-10.2.8-postgresql-postgresql-mdm-db-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > database [postgresql]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation a partir da versao 10.2.3, o PostgreSQL pode ser usado para criar o banco de dados do master domain manager e do Dynamic Workload Console, substituindo OneDB e Informix que deixaram de ser suportados; o PostgreSQL e gratuito e open-source, oferece opcoes de performance, seguranca e configuracao, e sua customizacao suporta escalabilidade e disponibilidade para grandes volumes de dados.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation a partir da versao 10.2.3, o PostgreSQL pode ser usado para criar o banco de dados do master domain manager e do Dynamic Workload Console, substituindo OneDB e Informix que deixaram de ser suportados; o PostgreSQL e gratuito e open-source, oferece opcoes de performance, seguranca e configuracao, e sua customizacao suporta escalabilidade e disponibilidade para grandes volumes de dados?*

---

### 28. hwa-10.2.8-rollback-no-rollback-doc-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
HCL Workload Automation 10.2.8 does not document a rollback/downgrade procedure after upgrade. The upgrading page warns that new database records may prevent rollback to a previous version. Backup does not equal a supported downgrade path.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HCL Workload Automation 10.2.8 does not document a rollback/downgrade procedure after upgrade?*

---

### 29. hwa-10.2.8-runbook-pre-upgrade-os-prereq-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, antes de iniciar o upgrade é preciso verificar os pré-requisitos mínimos suportados de sistema operacional, produto e banco de dados, e baixar as imagens de instalação.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, antes de iniciar o upgrade é preciso verificar os pré-requisitos mínimos suportados de sistema operacional, produto e banco de dados, e baixar as imagens de instalação?*

---

### 30. hwa-10.2.8-runbook-pre-upgrade-stop-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, antes do upgrade é necessário ter parado o processamento de workload no master domain manager, e é necessário mesclar as personalizações do script tws_env no novo script sem sobrescrever os parâmetros relacionados às bibliotecas OpenSSL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, antes do upgrade é necessário ter parado o processamento de workload no master domain manager, e é necessário mesclar as personalizações do script tws_env no novo script sem sobrescrever os parâmetros relacionados às bibliotecas OpenSSL?*

---

### 31. hwa-10.2.8-runbook-upgrade-order-dwc-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, em um upgrade direto a partir de 9.5.0.x ou 10.x.x, a sequência documentada é: atualizar primeiro a Dynamic Workload Console e seu banco de dados, depois o dynamic domain manager e seus backups e o banco de dados, depois o master domain manager e seus backups e o banco de dados, e por fim os domain managers e os agents.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, em um upgrade direto a partir de 9.5.0.x ou 10.x?*

---

### 32. hwa-10.2.8-themaster-resolved-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > twsinst [twsinst]]`

**Regra Canônica / Evidência:**
RESOLUCAO de hwa-themaster-0001 (contradicted): o nome de workstation padrao do master domain manager no HCL Workload Automation 10.2.8 e MASTER (parametro -master do twsinst, default MASTER), e NAO THEMASTER; THEMASTER e um nome possivel, mas nao o default documentado. Claims que afirmam THEMASTER como padrao estao incorretos.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?*

---

### 33. hwa-10.2.8-tls-ssl-default-install-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Fresh HWA Distributed 10.2.8 installations install the master domain manager and dynamic domain manager in SSL mode by default.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Fresh HWA Distributed 10.2.8 installations install the master domain manager and dynamic domain manager in SSL mode by default?*

---

### 34. hwa-10.2.8-tls12-parallel-upgrade-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
TLS 1.2 is required for communication between 9.4.0.x and 10.2.8 components during parallel upgrade. Context: Communication between 9.4.0.x and 10.2.8 components during parallel upgrade requires TLS 1.2.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: TLS 1.2 is required for communication between 9.4.0.x and 10.2.8 components during parallel upgrade?*

---

### 35. hwa-10.2.8-trouble-awsjom179e-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; composer/DWC) > Componente: Dynamic Workload Console (DWC) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a exclusao de uma workstation via Composer ou Dynamic Workload Console falha com AWSJOM179E 'An error occurred deleting definition of the workstation <name>. The workload broker server is currently unreachable'; a causa documentada e a remocao de um dynamic domain manager sem seguir o procedimento de desinstalacao do Planning and Installation; a recuperacao documentada e (1) verificar que o dynamic domain manager foi realmente excluido (nao apenas indisponivel) e (2) excluir as workstations com o comando composer del ws <workstation_name>;force.

**Plataforma / Validação:** distributed; composer/DWC

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM179E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM179E no HWA?*
- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar install?*

---

### 36. hwa-10.2.8-tune-bm-look-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
A opção bm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de escanear e atualizar seu arquivo de controle de produção; o padrão é 5 segundos em instalação limpa desde 9.4 FP1 e 15 segundos em upgrades que preservam o valor anterior.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm look no localopts do HCL Workload Automation 10.2.8 especifica o número mínimo de segundos que o Batchman aguarda antes de escanear e atualizar seu arquivo de controle de produção; o padrão é 5 segundos em instalação limpa desde 9.4 FP1 e 15 segundos em upgrades que preservam o valor anterior?*

---

### 37. hwa-10.2.8-tune-bm-read-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
A opção bm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda por uma mensagem no arquivo intercom.msg; o padrão é 3 segundos em instalação limpa desde 9.4 FP1 e 10 segundos em upgrades que preservam o valor anterior.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: A opção bm read no localopts do HCL Workload Automation 10.2.8 especifica o número máximo de segundos que o Batchman aguarda por uma mensagem no arquivo intercom?*

---

### 38. hwa-10.2.8-upgrade-certs-required-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, instalação e upgrade de componentes server exigem certificados ca.crt, tls.key e tls.crt; certificados são obrigatórios e no upgrade paralelo devem ser extraídos do keystore/truststore da versão anterior antes do procedimento.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation 10.2.8, instalação e upgrade de componentes server exigem certificados ca?*

---

### 39. hwa-10.2.8-upgrade-gskit-openssl-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Em um upgrade de HCL Workload Automation para 10.2.8 vindo de 9.5 com certificados customizados, os parâmetros de certificados no localopts devem ser verificados; para certificados gerados com OpenSSL é preciso revisar paths (SSL key, SSL certified, SSL key pwd, SSL CA certified, SSL random seed), e para GSKit os parâmetros migram automaticamente para OpenSSL.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: Em um upgrade de HCL Workload Automation para 10.2.8 vindo de 9.5 com certificados customizados, os parâmetros de certificados no localopts devem ser verificados; para certificados gerados com OpenSSL é preciso revisar paths (SSL key, SSL certified, SSL key pwd, SSL CA certified, SSL random seed), e para GSKit os parâmetros migram automaticamente para OpenSSL?*

---

### 40. hwa-10.2.8-upgrade-order-0006

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation Distributed 10.2.8, a boa prática de upgrade começa pelo Dynamic Workload Console; o upgrade direto de 9.5/10.x atualiza DWC e banco, depois dynamic domain manager e backups, master domain manager e backups, e por fim domain managers e agents.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HCL Workload Automation Distributed 10.2.8, a boa prática de upgrade começa pelo Dynamic Workload Console; o upgrade direto de 9.5/10.x atualiza DWC e banco, depois dynamic domain manager e backups, master domain manager e backups, e por fim domain managers e agents?*

---

### 41. hwa-10.2.8-vm-direct-upgrade-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o upgrade é suportado a partir de 9.5.0.x ou 10.x.x por procedimento direto (direct upgrade) ou paralelo (parallel upgrade); a partir de 9.4.0.x apenas o upgrade paralelo é suportado.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No HCL Workload Automation 10.2.8, o upgrade é suportado a partir de 9.5.0.x ou 10.x?*

---

### 42. hwa-10.2.8-vm-mixed-version-environment-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
O HCL Workload Automation 10.2.8 suporta coexistência de versões (mixed-version environment) durante o upgrade: componentes como agentes, Dynamic Workload Console, dynamic domain managers e master domain manager podem ficar em níveis de versão diferentes, e o procedimento de upgrade paralelo instala componentes 10.2.8 lado a lado com os da versão anterior antes da troca.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: O HCL Workload Automation 10.2.8 suporta coexistência de versões (mixed-version environment) durante o upgrade: componentes como agentes, Dynamic Workload Console, dynamic domain managers e master domain manager podem ficar em níveis de versão diferentes, e o procedimento de upgrade paralelo instala componentes 10.2.8 lado a lado com os da versão anterior antes da troca?*

---

### 43. hwa-10.2.8-vm-parallel-upgrade-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
No upgrade paralelo para 10.2.8 a partir de 9.5.0.x ou 10.x.x, novos componentes 10.2.8 (Dynamic Workload Console, dynamic domain manager e master domain manager) são instalados como backup e ativados por switch, mantendo a versão anterior em execução lado a lado até a troca; o console 10.2.8 é instalado primeiro e passa a coexistir com os demais componentes ainda na versão antiga.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: No upgrade paralelo para 10.2.8 a partir de 9.5.0.x ou 10.x?*

---

### 44. hwa-9.5-cert-permissions-contrast-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-cert-permissions-version-dep-0015: as permissoes de arquivos de certificado (644 vs 755) no HWA sao especificas de cada fluxo de instalacao/upgrade e de cada versao; o fluxo da 9.5 e o da 10.2.8 documentam permissoes distintas para os mesmos tipos de arquivo (por exemplo, extracao de diretorio com 755 e arquivos com 644).

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: PAR CONTRASTIVO de hwa-10.2.8-cert-permissions-version-dep-0015: as permissoes de arquivos de certificado (644 vs 755) no HWA sao especificas de cada fluxo de instalacao/upgrade e de cada versao; o fluxo da 9.5 e o da 10.2.8 documentam permissoes distintas para os mesmos tipos de arquivo (por exemplo, extracao de diretorio com 755 e arquivos com 644)?*

---

### 45. hwa-9.5-real-autofailover-fp2-0004

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 9.5 Fix Pack 2 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
O failover automatico do master/event manager foi introduzido no HCL Workload Automation 9.5 Fix Pack 2: com a lista de backups definida pelas opcoes workstationMasterListInAutomaticFailover e workstationEventMgrListInAutomaticFailover, a carga e transferida automaticamente para o backup; instalacoes novas de 9.5 FP2 ou posterior habilitam o recurso por padrao (yes), enquanto upgrades de 9.5/9.5 FP1 exigem habilitacao manual. Recurso NAO presente nas versoes 9.5 base / 9.5 FP1.

**Plataforma / Validação:** Distributed

---

### 46. hwa-install-1028-mdm-first-plan-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: CLI composer (Definições de Banco e Modelagem) > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na configuração inicial de um MDM HWA 10.2.8, a documentação orienta adicionar Sfinal, executar JnextPlan, verificar Batchman LIVES e revisar o limite de jobs da workstation, cujo padrão pós-instalação é zero. Context: composer add Sfinal; JnextPlan; Batchman LIVES; The default job limit after installation is 0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário composer no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no composer para gerenciar install?*
- *Como executar a virada de plano ou recuperação com JnextPlan e ResetPlan?*

---

### 47. hwa-install-1028-ports-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
HWA Distributed 10.2.8 documenta portas padrão incluindo 31111, 31115, 31116, 31113, 31114, 31117, 41114, 35116, 9443 e 9444; valores podem ser customizados. Context: Dynamic Workload Console — 9444 - HTTP_PORT; 9443 - HTTPS_PORT.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HWA Distributed 10.2.8 documenta portas padrão incluindo 31111, 31115, 31116, 31113, 31114, 31117, 41114, 35116, 9443 e 9444; valores podem ser customizados?*

---

### 48. hwa-install-1028-prereq-scan-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HWA 10.2.8, o scanner de pré-requisitos verifica ambiente do SO, bibliotecas UNIX, disco, memória e memória virtual, mas não verifica requisitos de componentes externos como DB2. Context: It does not check the requirements for other components, such as DB2.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Em HWA 10.2.8, o scanner de pré-requisitos verifica ambiente do SO, bibliotecas UNIX, disco, memória e memória virtual, mas não verifica requisitos de componentes externos como DB2. Context: It does not check the requirements for other components, such as DB2.?*

---

### 49. hwa-install-1028-topology-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, uma rede pode conter MDM, BMDM, DDMs, servidores DWC e agentes; DDMs e DWC são componentes opcionais conforme a topologia. Context: An HCL Workload Automation network is composed of a master domain manager, one or more Dynamic Workload Console servers, dynamic domain managers, and dynamic agents.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como configurar ou solucionar problemas no dynamic agent ou broker para install?*
- *Qual a regra documentada no HWA Distributed sobre: Em HWA Distributed 10.2.8, uma rede pode conter MDM, BMDM, DDMs, servidores DWC e agentes; DDMs e DWC são componentes opcionais conforme a topologia?*

---

### 50. hwa-install-dwc-1028-params-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação DWC HWA 10.2.8, os parâmetros documentados incluem rdbmstype, user, password, dbname, dbuser, dbpassword, dbhostname, dbport, wlpdir, sslkeysfolder e sslpassword; duas instâncias podem compartilhar banco remoto. Context: two Dynamic Workload Console instances on two separate workstations, sharing the same remote database.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual a regra documentada no HWA Distributed sobre: Na instalação DWC HWA 10.2.8, os parâmetros documentados incluem rdbmstype, user, password, dbname, dbuser, dbpassword, dbhostname, dbport, wlpdir, sslkeysfolder e sslpassword; duas instâncias podem compartilhar banco remoto?*

---

### 51. hwa-install-liberty-1028-procedure-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação HWA 10.2.8, Open Liberty ou WebSphere Application Server Liberty Base é requerido em workstations de componentes server e DWC; a versão deve ser consultada no Related Software Report, e a instalação do produto usa o diretório via wlpdir. Context: Find out which version... by checking the required version... in Related Software Report.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na instalação HWA 10.2.8, Open Liberty ou WebSphere Application Server Liberty Base é requerido em workstations de componentes server e DWC; a versão deve ser consultada no Related Software Report, e a instalação do produto usa o diretório via wlpdir?*

---

### 52. hwa-install-mdm-1028-certificates-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação de componentes server HWA 10.2.8, os certificados requeridos são ca.crt, tls.key e tls.crt; esse conjunto não é universal para todos os agentes ou componentes. Context: The required certificates are: ca.crt, tls.key, tls.crt... ensure that the same certificates are present on all components.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na instalação de componentes server HWA 10.2.8, os certificados requeridos são ca?*

---

### 53. hwa-install-mdm-1028-params-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na instalação MDM/BMDM HWA 10.2.8, os parâmetros documentados incluem rdbmstype, dbhostname, dbport, dbname, dbuser, dbpassword, wauser, wapassword, wlpdir, sslkeysfolder, sslpassword, inst_dir e licenseserverid. Context: The following information is required... Database information... Open Liberty information... Security information... Licensing information.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como os parâmetros de instalação do MDM são configurados e validados no HWA 10.2.8?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*

---

### 54. hwa-install-mdm-1028-prereqs-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Backup Master Domain Manager (BMDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Antes de instalar um MDM HWA 10.2.8, a documentação requer Liberty no nó, banco criado/populado, usuário administrativo, licença configurada e, em UNIX, umask 022; o BMDM aponta para o banco existente e não requer criar/popular o banco. Context: Before starting the installation... Installing Open Liberty... Creating and populating the database... Creating the HCL Workload Automation administrative user... Ensure you have created a license server... umask is set to 022.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Antes de instalar um MDM HWA 10.2.8, a documentação requer Liberty no nó, banco criado/populado, usuário administrativo, licença configurada e, em UNIX, umask 022; o BMDM aponta para o banco existente e não requer criar/popular o banco?*

---

### 55. hwa-liberty-install-10.2.0-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > install [install]]`

**Regra Canônica / Evidência:**
Na documentação HWA Distributed 10.2.0, Open Liberty é requerido nos nós que receberão componentes server ou DWC; pode ser instalado extraindo o arquivo ZIP, e o diretório de instalação deve corresponder ao parâmetro wlpdir dos instaladores de MDM, backup MDM, DDM, backup DDM e DWC. Context: Open Liberty is required on all workstations where you plan to install the server components and the Dynamic Workload Console.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: Na documentação HWA Distributed 10.2.0, Open Liberty é requerido nos nós que receberão componentes server ou DWC; pode ser instalado extraindo o arquivo ZIP, e o diretório de instalação deve corresponder ao parâmetro wlpdir dos instaladores de MDM, backup MDM, DDM, backup DDM e DWC?*

---

### 56. hwa-themaster-domain-manager-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Instalação / Utilitários de Setup > Tópico: installation_upgrade > twsinst [twsinst]]`

**Regra Canônica / Evidência:**
O nome de workstation padrão do master domain manager no HCL Workload Automation é MASTER, e não THEMASTER, conforme a documentação oficial do parâmetro -master do script twsinst.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Como utilizar o utilitário twsinst no HCL Workload Automation?*
- *Qual a sintaxe ou procedimento no twsinst para gerenciar twsinst?*

---

### 57. hwa-upgrade-1028-rollback-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: installation_upgrade > upgrade [upgrade]]`

**Regra Canônica / Evidência:**
HWA informa que registros de banco criados por recursos da nova versão podem impedir rollback para a versão anterior; backup não equivale a downgrade suportado. Context: You cannot roll back your environment to a previous version.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual a regra documentada no HWA Distributed sobre: HWA informa que registros de banco criados por recursos da nova versão podem impedir rollback para a versão anterior; backup não equivale a downgrade suportado?*

---
