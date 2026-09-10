# PARTE2 RUNBOOK MDM SERVERINST TWSINST COMPLETE REFERENCE

## RUNBOOK: Referência Completa e Catálogo de Flags de Instalação do Master Domain Manager (`serverinst.sh` / `twsinst` / `configureDb.sh`) — HWA 10.2.8

**Arquivo de origem:** `data/runbooks/mdm-serverinst-twsinst-complete-reference.md`

### 1. Arquitetura de Instalação do MDM: `serverinst.sh` vs `twsinst`

No HCL Workload Automation Distributed, a instalação de um **Master Domain Manager (MDM)**, **Backup Master (BMDM)** ou **Dynamic Domain Manager (DDM)** difere fundamentalmente de um agente isolado:

1. **`serverinst.sh` como Maestro Orquestrador**:
   O operador executa o `serverinst.sh` (ou fornece o `serverinst.properties`). Ele é o script de nível superior que:
   - Valida pré-requisitos de sistema, portas e Java Liberty (`WLP`).
   - Testa a conectividade com o SGBD (`configureDb.sh`).
   - **Invoca o `twsinst` com a flag `-agent both` e `-caller MDM`** para instalar simultaneamente o nó Master (FTA) e o Agente Dinâmico local.
   - Configura o Open Liberty engineServer, datasources JDBC e certificados SSL/TLS.
   - Executa a pós-configuração (`waPostConfigure`) e inicializa o domínio.

2. **A Tríade Obrigatória de Workstations do MDM**:
   A instalação do MDM cria obrigatoriamente 3 estações lógicas no plano:
   - **`THISCPU` (Master FTA)**: O motor de agendamento principal (`MDM`), tipo `*UNIX MASTER`.
   - **`DISPLAYNAME` (Dynamic Agent Local)**: O agente dinâmico local gerenciado pelo broker (`MDMDA`), tipo `UNIX AGENT`. **Deve ser diferente de `THISCPU` sob pena de erro `AWSFAB164E`**.
   - **`XANAME` (Extended Agent)**: A estação lógica onde roda a esteira noturna do `FINAL` (`MDMXA`), tipo `OTHR X-AGENT` com método de acesso `unixlocl`.

---

### 2. Invocação Interna do `twsinst` pelo `serverinst.sh`

O script `serverinst.sh` monta e dispara a seguinte linha de comando para o `twsinst`:

```bash
${THIS_SCRIPT_DIR}/twsinst \
  -new \
  -inst_dir $INST_DIR \
  -agent both \
  -addjruntime true \
  -jmport $JM_PORT \
  -hostname $THIS_HOSTNAME \
  -displayname $DISPLAYNAME \
  -port $NETMAN_PORT \
  -netmansslport $NETMAN_SSL_PORT \
  -thiscpu $THISCPU \
  -master $MASTER \
  -company $COMPANY_NAME \
  -tdwbhostname $BROKER_HOSTNAME \
  -tdwbport $HTTPS_PORT \
  [-data_dir $DATA_DIR] \
  -wauser $WA_USER \
  -wapassword $WA_PASSWORD \
  -caller $COMPONENT_TYPE \
  [-sslpassword $SSL_PASSWORD -sslkeysfolder $SSL_KEY_FOLDER] \
  -useencryption $USE_ENCRYPTION \
  -encryptionpassword $ENCRYPTION_PASSWORD \
  -acceptlicense $ACCEPTLICENSE \
  -uname $WA_USER \
  -lang $INST_LANG \
  [-skipcheckprereq] \
  [-work_dir $WORK_DIR] \
  [-enablefips $ENABLE_FIPS]
```

*Nota*: No modo update (`--componenttype ...`), o `serverinst.sh` invoca `twsinst -restore $TWSINST_COMMON_PARMS`.

---

### 3. Catálogo Completo de Flags CLI do `serverinst.sh` (50 Flags)

| Flag CLI | Argumento | Default | Descrição |
|---|---|---|---|
| `--acceptlicense` / `-a` | `yes \| no` | `no` | Aceite mandatório dos termos de licença HCL. |
| `--inst_dir` / `-i` | `caminho` | `/opt/wa` | Diretório de instalação do servidor. **Deve estar rigorosamente vazio** (`WAINST050E`). |
| `--data_dir` | `caminho` | `${INST_DIR}/TWSDATA` | Diretório dedicado de dados em disco (planos, logs e filas de mensagens). |
| `--work_dir` | `caminho` | `$HOME/tmp/wa<ver>/WA_<user>` | Diretório de trabalho temporário do instalador. |
| `--thiscpu` | `string` | Hostname da máquina | Nome da workstation do servidor no plano (Master). |
| `--displayname` | `string` | Hostname da máquina | Nome atribuído ao dynamic agent local. Não pode ser igual ao `--thiscpu` (`AWSFAB164E`). |
| `--xaname` | `string` | `<hostname>_XA` | Nome da workstation Extended Agent para a esteira noturna do plano `FINAL`. |
| `--master` | `string` | `MASTER` | Nome da estação Master Domain Manager na rede. |
| `--hostname` | `FQDN` | Hostname da máquina | FQDN completo onde o servidor escuta. |
| `--domain` | `string` | `MASTERDM` | Nome do domínio inicial do HWA. |
| `--company` | `string` | `MYCOMPANY` | Nome da organização gravado nas licenças e arquivos de cabeçalho. |
| `--componenttype` | `MDM \| DDM` | `MDM` | Tipo de servidor: Master Domain Manager ou Dynamic Domain Manager. Se apontar para banco existente, autoconfigura como Backup (BKM/BDDM) com `WAINST054I`. |
| `--wauser` | `username` | `wauser` | Usuário do SO que será proprietário dos serviços e do Liberty. |
| `--wapassword` | `senha` | N/A | Senha do usuário do HWA. |
| `--wlpdir` / `-w` | `caminho` | N/A | Caminho de instalação do Open Liberty ou WebSphere Liberty Base (`/opt/liberty/wlp`). |
| `--httpport` | `1 a 65535` | `31115` | Porta HTTP não-segura do Liberty engineServer. |
| `--httpsport` | `1 a 65535` | `31116` | **Porta HTTPS segura da REST API V2 e Broker no Liberty**. |
| `--bootstrapport` / `-b` | `1 a 65535` | `2809` | Porta Bootstrap do Liberty. |
| `--bootsecport` / `-s` | `1 a 65535` | `9403` | Porta Bootstrap segura (SSL) do Liberty. |
| `--netmanport` | `1 a 65535` | `31111` | Porta TCP do Netman (comunicação sem SSL). |
| `--netmansslport` | `1 a 65535` | `31113` | Porta TCP do Netman com criptografia SSL/TLS. |
| `--jmport` | `1 a 65535` | `31114` | Porta TCP do JobManager do agente dinâmico local. |
| `--eifport` | `1 a 65535` | `31131` | Porta EIF do servidor de processamento de eventos (EDWA). |
| `--brwksname` | `string` | `<hostname>_DWB` | Nome da workstation do Dynamic Workload Broker no Composer. |
| `--brnetmanport` | `1 a 65535` | `41114` | Porta Netman exclusiva do Broker. |
| `--mdmbrokerhostname` | `FQDN` | N/A | Hostname do Broker Master (obrigatório se `--componenttype DDM`). |
| `--mdmhttpsport` | `1 a 65535` | `31116` | Porta HTTPS do Broker Master (obrigatório se `--componenttype DDM`). |
| `--rdbmstype` / `-r` | `DB2\|ORACLE\|MSSQL\|POSTGRESQL\|IDS` | N/A | Tipo de banco de dados relacional. |
| `--dbhostname` | `FQDN / IP` | N/A | Hostname ou IP do servidor de banco de dados. |
| `--dbport` | `1 a 65535` | N/A | Porta do banco de dados (ex: `5432` PostgreSQL, `50000` DB2, `1521` Oracle). |
| `--dbname` | `string` | `TWS` | Nome da base de dados do HWA. |
| `--dbuser` | `username` | N/A | Usuário do banco de dados com permissão nos schemas do HWA. |
| `--dbpassword` | `senha` | N/A | Senha do usuário de banco de dados. |
| `--dbserver` | `string` | N/A | Nome do servidor Informix (necessário apenas se `RDBMS_TYPE=IDS`). |
| `--dbdriverpath` | `caminho` | N/A | Caminho para o driver JDBC customizado (se não usar o padrão). |
| `--dbalternatenames` | `lista` | N/A | Hostnames alternativos de banco para topologias de alta disponibilidade (DB2 HADR/Oracle RAC). |
| `--dbalternateports` | `lista` | N/A | Portas alternativas de banco para alta disponibilidade. |
| `--sslkeysfolder` | `caminho` | N/A | Pasta contendo os certificados em formato `.PEM` (`ca.crt`, `tls.key`, `tls.crt`). **Não pode estar dentro de `INST_DIR`**. |
| `--sslpassword` | `senha` | N/A | Senha usada para gerar as keystores PKCS#12 e trusts a partir dos PEMs. |
| `--enablefips` | `true \| false` | `false` | Habilitação de FIPS (suporte desabilitado em 10.2.8). |
| `--skipcheckprereq` | `switch` | Desativado | Pula a verificação de pré-requisitos do sistema operacional. |
| `--skipcheckemptydir` | `switch` | Desativado | Ignora checagem de diretório de instalação vazio (não recomendado). |
| `--startserver` | `true \| false` | `true` | Inicia automaticamente o Liberty engineServer e processos ao fim da instalação. |
| `--override` | `true \| false` | `false` | Sobrescreve configurações anteriores em caso de reinstalação. |
| `--lang` | `código ISO` | `$LANG` | Idioma de exibição dos logs e mensagens. |
| `--optmanfordocker` | `switch` | Desativado | Ajusta parâmetros do `optman` para ambientes baseados em containers Docker. |
| `--licenserefreshtoken`| `string` | N/A | Token de renovação de licença HCL. |
| `--licenseserverurl` | `URL` | N/A | URL do License Server HCL. |
| `--isforzos` | `true \| false` | `false` | Configura integração nativa com controladores z/OS. |
| `--check` | `switch` | Desativado | Executa apenas a checagem de parâmetros de entrada sem instalar. |

---

### 4. Catálogo de Propriedades do Arquivo `serverinst.properties` (75 Chaves)

Quando o instalador é invocado com `serverinst.sh -f serverinst.properties`, os parâmetros são mapeados pelas chaves canônicas abaixo:

### A. Parâmetros Gerais e Identidade do Servidor
* `ACCEPTLICENSE`: `yes` ou `no`.
* `INST_DIR`: Diretório raiz dos binários (ex: `/opt/hwa/TWS`).
* `DATA_DIR`: Diretório de dados (ex: `/opt/hwa/TWS/TWSDATA`).
* `WORK_DIR`: Diretório temporário de execução.
* `WA_USER`: Usuário de serviço no SO (`wauser`).
* `WA_PASSWORD`: Senha do usuário `wauser`.
* `THISCPU`: Nome da workstation do Master (`MDM` ou `MDM_BK`).
* `DISPLAYNAME`: Nome do agente dinâmico local (`MDMDA` ou `MDM_BKA`).
* `XANAME`: Nome do extended agent para o plano noturno (`MDMXA` ou `MDM_BKXA`).
* `THIS_HOSTNAME`: Hostname qualificado do servidor (`tws-hwa.lab`).
* `MASTER`: Nome da estação Master do domínio (`MDM`).
* `DOMAIN`: Nome do domínio do HWA (`MASTERDM`).
* `COMPANY_NAME`: Nome da empresa.
* `COMPONENT_TYPE`: `MDM` ou `DDM`.
* `START_SERVER`: `true` ou `false`.
* `LANG`: Idioma das mensagens (`C`, `en`, etc.).

### B. Banco de Dados Relacional (RDBMS)
* `RDBMS_TYPE`: `POSTGRESQL`, `DB2`, `ORACLE`, `MSSQL`, ou `IDS`.
* `DB_HOST_NAME`: Hostname ou IP do servidor de banco (ex: `172.18.0.10` ou `localhost`).
* `DB_PORT`: Porta TCP do banco (ex: `5432`).
* `DB_NAME`: Nome da base de dados do HWA (ex: `TWS`).
* `DB_USER`: Usuário de banco com acesso aos schemas (`postgres` ou `twsuser`).
* `DB_PASSWORD`: Senha do usuário de banco.
* `DB_ADMIN_USER`: Usuário administrador do banco (para criação de schemas pelo `configureDb`).
* `DB_ADMIN_USER_PWD`: Senha do administrador de banco.
* `DB_SSL_CONNECTION`: `true` ou `false`.
* `DB_DRIVER_PATH`: Caminho alternativo do arquivo JAR JDBC.
* `DB_SERVER`: Nome da instância Informix (apenas para IDS).
* `USE_PARTITIONING`: `true` ou `false` para particionamento de tabelas de histórico.
* `SKIP_DB_CHECK`: `true` para ignorar validação de conexão prévia.
* `EXEC_GENERATED_SQL`: `true` para rodar DDLs automaticamente.

### C. WebSphere / Open Liberty (`WLP`)
* `WLP_INSTALL_DIR`: Diretório raiz do Liberty (`/opt/liberty/wlp`).
* `HTTP_PORT`: Porta HTTP (`31115`).
* `HTTPS_PORT`: Porta HTTPS (`31116`).
* `BOOTSTRAP_PORT`: Porta bootstrap (`2809`).
* `BOOTSTRAP_SEC_PORT`: Porta bootstrap SSL (`9403`).
* `SERVER_NAME`: Nome do servidor Liberty (`engineServer`).
* `WLP_USER`: Usuário dono do processo Liberty.
* `WLP_PASSWORD`: Senha codificada para o Liberty.

### D. Portas de Comunicação de Rede e Processos
* `NETMAN_PORT`: Porta TCP sem SSL do Netman (`31111`).
* `NETMAN_SSL_PORT`: Porta TCP segura em SSL do Netman (`31113`).
* `JM_PORT`: Porta do daemon JobManager (`31114`).
* `EIF_PORT`: Porta EIF para recepção de eventos EDWA (`31131`).
* `BROKER_NETMAN_PORT`: Porta Netman do Broker (`41114`).
* `BROKER_WORKSTATION_NAME`: Nome da estação Broker (`MDM_DWB`).
* `BROKER_HOSTNAME`: Hostname onde roda o Broker.
* `MDM_BROKER_HOSTNAME`: Hostname do Broker central (usado por DDMs).
* `MDM_HTTPS_PORT`: Porta HTTPS do Broker central.

### E. Certificados e Criptografia AES em Repouso
* `SSL_KEY_FOLDER`: Pasta contendo `ca.crt`, `tls.key`, `tls.crt` em formato PEM.
* `SSL_PASSWORD`: Senha para geração de keystores PKCS#12 (`TWSServerKeyFile.p12`).
* `USE_ENCRYPTION`: `true` para criptografar o arquivo `Symphony` e filas com AES-256.
* `ENCRYPTION_PASSWORD`: Senha para geração das chaves simétricas AES em repouso (`key.p12`).
* `TRUST_SERVER_KEY`: `true` para importar automaticamente chaves de servidores confiáveis.
* `ENABLE_FIPS`: `false` (obrigatório em 10.2.8).

### F. Licenciamento e Tablespaces Avançadas
* `LICENSE_SERVER_URL`: URL do License Server.
* `LICENSE_SERVER_ID`: Identificador do cliente de licença.
* `LICENSE_PROXY_SERVER`, `LICENSE_PROXY_PORT`, `LICENSE_PROXY_USER`, `LICENSE_PROXY_PASSWORD`.
* `IWS_TS_NAME`, `IWS_TS_PATH`: Tablespace padrão de tabelas de modelo.
* `IWS_LOG_TS_NAME`, `IWS_LOG_TS_PATH`: Tablespace de logs e auditoria.
* `IWS_PLAN_TS_NAME`, `IWS_PLAN_TS_PATH`: Tablespace dos objetos de plano.
* `TWS_TS_TEMP_NAME`: Tablespace temporária do banco.

---

### 5. Flags do `configureDb.sh` do MDM (30 Flags)

O utilitário `configureDb.sh` é executado antes do `serverinst.sh` para preparar o banco de dados:

```bash
./configureDb.sh --action install --rdbmstype POSTGRESQL --dbname TWS --dbuser postgres ...
```

| Flag CLI | Descrição |
|---|---|
| `--action` | Ação a executar: `install`, `upgrade` ou `drop`. |
| `--rdbmstype` | Tipo de SGBD (`POSTGRESQL`, `DB2`, `ORACLE`, `MSSQL`, `IDS`). |
| `--componenttype` | Componente do schema: `MDM` ou `DWC`. |
| `--dbhostname` | Hostname do SGBD. |
| `--dbport` | Porta TCP do SGBD. |
| `--dbname` | Nome do banco (`TWS` para MDM, `TDWC` para DWC). |
| `--dbuser` | Usuário de aplicação do banco. |
| `--dbpassword` | Senha do usuário de aplicação. |
| `--dbadminuser` | Usuário DBA com permissão para criar schemas e tabelas. |
| `--dbadminuserpw` | Senha do usuário DBA. |
| `--dbdriverpath` | Caminho do driver JDBC. |
| `--execsql` | `true` para executar os scripts DDL imediatamente. |
| `--skipdbcheck` | Pula teste prévio de conectividade. |
| `--usepartitioning` | Cria particionamento nas tabelas de histórico e eventos. |
| `--dbalternatenames` | Lista de hosts secundários para alta disponibilidade. |
| `--dbalternateports` | Lista de portas secundárias para alta disponibilidade. |
| `--iwstsname` / `--iwstspath` | Nome e caminho da tablespace primária. |
| `--iwslogtsname` / `--iwslogtspath` | Nome e caminho da tablespace de logs. |
| `--iwsplantsname` / `--iwsplantspath` | Nome e caminho da tablespace de plano. |
| `--iwstemptsname` | Nome da tablespace temporária. |
| `--zlocationname` | Location name DB2 z/OS (apenas z/OS). |
| `--zbufferpoolname` | Buffer pool DB2 z/OS (apenas z/OS). |
| `--log_dir` | Diretório de gravação dos logs do `configureDb`. |
| `--work_dir` | Diretório de staging temporário dos scripts SQL. |
| `--lang` | Idioma de exibição das mensagens. |
| `--force` | Força a execução ignorando avisos de versão de banco. |

---

### 6. Pitfalls e Regras de Ouro Comprovadas em Laboratório

1. **`AWSFAB164E` (Colisão de Nomes)**:
   Nunca passe `--thiscpu` com o mesmo valor de `--displayname`. No MDM, `--thiscpu` é o Master (ex: `MDM`) e `--displayname` é o agente dinâmico local (ex: `MDMDA`). Se forem iguais, o instalador aborta com `AWSFAB164E`.
2. **`WAINST050E` (Diretório Não Vazio)**:
   O `--inst_dir` não pode conter nenhum arquivo ou subdiretório residual de execuções anteriores. Sempre limpe `/opt/hwa` antes de rodar uma nova instalação.
3. **Certificados Fora do `INST_DIR`**:
   A pasta especificada em `--sslkeysfolder` (contendo `ca.crt`, `tls.key` e `tls.crt`) **nunca deve ser colocada dentro do `--inst_dir`**, pois isso faz o check de diretório vazio falhar (`WAINST050E`).
4. **Detecção Automática de Backup Master (`WAINST054I`)**:
   Quando o `serverinst.sh` é executado com `--componenttype MDM` apontando para um banco que já possui um Master configurado, ele não sobrescreve o banco: ele emite `WAINST054I Configuring BKM` e se auto-instala como **Backup Master Domain Manager (BMDM)**!
5. **Cópia Mandatória de Chaves AES no Backup**:
   Ao instalar um Backup Master Domain Manager, os arquivos `TWSDATA/ssl/aes/key.p12` e `key.sth` do Master original devem ser copiados obrigatoriamente para o Backup, caso contrário ele não consegue descriptografar o Symphony durante um failover.
