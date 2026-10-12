# Instalação do Dynamic Workload Console 10.2.8 no lab (cachyosdell)

Data: 2026-10-12. Fase 2, itens 2.1/2.2 do PLANO_FECHAMENTO_LACUNAS.
Procedimento base: /root/hwa/dwc-install-validation.jsonl (validado em 2026-08-25 no WSL2/Ubuntu).

## Arquitetura (canônica do lab)

- DWC instalado **no host** em /opt/hwa/DWC (não em container — o procedimento validado era host-direct)
- **Banco de dados COMPARTILHADO com o TWS Master:** o DWC usa a mesma instância
  PostgreSQL 18 que roda no container tws-hwa (172.18.0.10:5432) — padrão suportado:
  mesma instância, databases separados (`TDWC` para o DWC, `TWS` para o engine)
- Open Liberty 26.0.0.3 em /opt/liberty/wlp (download de public.dhe.ibm.com)
- MDM: container tws-hwa (172.18.0.10:31116)

> **Nota de migração (2026-10-12):** inicialmente foi usado um PostgreSQL separado
> em container (`tws-dwcdb`). Por sugestão do usuário, migrou-se para a instância
> do Master: o database TDWC (55 tabelas) e a role `postgresdwc` já existiam no
> PostgreSQL do tws-hwa; o datasource do DWC foi apontado para 172.18.0.10 e o
> container separado foi removido.

## Pré-requisitos (desvios do procedimento validado)

| Item | Validado (WSL2) | Lab atual | Ação |
|------|-----------------|-----------|------|
| SO | Ubuntu 22.04 | CachyOS (Arch) | SKIPCHECKPREREQ=true (prereq checker não reconhece o SO) |
| PostgreSQL | local 127.0.0.1 | container tws-dwcdb (postgres:18) | DB_HOST_NAME=172.18.0.2 |
| Liberty | /opt/liberty/wlp | download manual | curl do openliberty-26.0.0.3.zip |
| MDM | 127.0.0.1 (MDMHOST) | tws-hwa:172.18.0.10 | /etc/hosts + hostname tws-hwa na conexão |
| wauser | existente | criado via useradd | senha twslab2026 |

## Passo 1 — Banco de dados (configureDb.sh)

```bash
# USA A INSTÂNCIA DO MASTER (tws-hwa) — não subir postgres separado
# O database TDWC e a role postgresdwc já existem no PostgreSQL do tws-hwa.
# Se precisar recriar:
docker exec -u postgres tws-hwa psql -c "CREATE ROLE postgresdwc WITH LOGIN PASSWORD 'dwcdbuser' CREATEDB;"
# (o configureDb.sh cria o database TDWC automaticamente se não existir)

# certificados
mkdir -p /root/hwa/dwc-certs
openssl req -x509 -newkey rsa:2048 -keyout tls.key -out tls.crt -days 825 -nodes -subj "/CN=dwc-lab"
cp tls.crt ca.crt && chown wauser:wauser tls.key tls.crt ca.crt

# properties (/root/hwa/configureDbPostgresql-lab.properties)
# DB_HOST_NAME=172.18.0.10 (PostgreSQL do Master), DB_ADMIN_USER=postgres
# (admin via peer auth no container; senha não necessária para configureDb)
# DB_USER=postgresdwc, DB_PASSWORD=dwcdbuser, DB_NAME=TDWC
# SSL_KEY_FOLDER=/root/hwa/dwc-certs, SSL_PASSWORD=twslab2026

cd /root/hwa/dwc-extracted && umask 022 && ./configureDb.sh -f /root/hwa/configureDbPostgresql-lab.properties
```

Saída: WAINST052I comando concluído com êxito. 55 tabelas (48 tdwc + 7 fed).

## Passo 2 — Instalação (dwcinst.sh)

```bash
# /root/hwa/dwcinst-lab.properties:
# ACCEPTLICENSE=yes, DWC_INST_DIR=/opt/hwa/DWC, DWC_ADMIN_USER=wauser, DWC_ADMIN_PW=twslab2026
# RDBMS_TYPE=POSTGRESQL, DB_NAME=TDWC, DB_HOST_NAME=172.18.0.10 (Master)
# WLP_INSTALL_DIR=/opt/liberty/wlp, START_WLP=false
# SKIPCHECKPREREQ=true (CachyOS não reconhecido)

cd /root/hwa/dwc-extracted && umask 022 && ./dwcinst.sh -f /root/hwa/dwcinst-lab.properties
```

Saída: WAINST023I instalação concluída com êxito. URL: https://cachyos-x8664:9443/console/login.jsp

## Passo 3 — Iniciar o servidor

```bash
chown -R wauser:wauser /opt/hwa/DWC /opt/liberty/wlp
chmod 755 /opt/hwa /opt/liberty
su - wauser -c "WLP_USER_DIR=/opt/hwa/DWC/usr /opt/liberty/wlp/bin/server start dwcServer"
```

## Passo 4 — Fix JSTL (problema encontrado)

**Sintoma:** GET /console/login.jsp retornava 302 em loop; trace mostrava
`JSPG0005E: o arquivo tld não pôde ser localizado para a uri [http://java.sun.com/jsp/jstl/core]`.

**Causa:** O Liberty 26.0.0.3 não resolve a TLD da JSTL para o JSP do DWC.

**Fix aplicado:**
1. Baixadas JSTL 3.0 (jakarta.servlet.jsp.jstl-api + impl) para
   `/opt/hwa/DWC/usr/servers/dwcServer/apps/DWC-10.2.8.00-SNAPSHOT.ear/Console.war/WEB-INF/lib/`
2. Alterado taglib em login.jsp de `http://java.sun.com/jsp/jstl/core` para `jakarta.tags.core`
   (backup em login.jsp.bak)

Após restart: GET /console/login.jsp -> 200.

## Passo 5 — Login e API

**Limitação conhecida:** POST /console/j_security_check retorna 400 (form login via browser
não funciona neste ambiente). **Workaround:** a API REST aceita basic auth diretamente.

```bash
# API funciona com basic auth
curl -sk -u wauser:twslab2026 https://localhost:9443/dwc/api/v1/engine/list
```

## Passo 6 — Conectar o engine MDM

```bash
# 1. importar certificado do MDM no truststore do DWC
echo | openssl s_client -connect tws-hwa:31116 2>/dev/null | openssl x509 > /tmp/mdm.crt
/opt/hwa/DWC/java/jre/bin/keytool -import -trustcacerts -alias mdm-tws-hwa \
  -file /tmp/mdm.crt -keystore /opt/hwa/DWC/usr/servers/dwcServer/resources/security/TWSServerTrustFile.p12 \
  -storepass twslab2026 -storetype PKCS12 -noprompt
# restart do dwcServer após importar

# 2. credenciais do MDM: usuário apiadmin (decodificado do {xor} no server.xml do MDM)
# apiadmin / wauser123!

# 3. criar conexão via API
curl -sk -u wauser:twslab2026 -H 'Content-Type: application/json' -X POST \
  -d '{"name":"MDM_LAB","type":"TWS","hostname":"tws-hwa","port":31116,
       "remoteServerName":"MDM",
       "credentials":{"user":"apiadmin","password":"wauser123!"},
       "showInDashboard":true}' \
  https://localhost:9443/dwc/api/v1/engine/create

# 4. validar
curl -sk -u wauser:twslab2026 https://localhost:9443/dwc/api/v1/engine/2/checkConnection
# -> {"successful":true,"message":"Connection to MDM_LAB: successful."}
```

## Troubleshooting

| Sintoma | Causa | Ação |
|---------|-------|------|
| WAINST213E prereq | SO não reconhecido (CachyOS) | SKIPCHECKPREREQ=true |
| login.jsp 302 loop | JSTL TLD não resolvida | Fix JSTL (passo 4) |
| j_security_check 400 | Form login com problema no Liberty 26 | Usar basic auth na API |
| checkConnection: PKIX path building failed | Cert do MDM não no truststore | Importar via keytool (passo 6.1) |
| checkConnection: 401 | Credenciais erradas pro MDM | Usar apiadmin/wauser123! (não wauser) |
| Permissão negada ao iniciar | /opt/hwa ou /opt/liberty sem acesso | chown/chmod (passo 3) |

## URLs e acessos

- DWC: https://cachyos-x8664:9443/console/ (ou https://localhost:9443/console/)
- Usuário DWC: wauser / twslab2026 (via API basic auth; form login com limitação)
- Engine: MDM_LAB -> tws-hwa:31116 (conectado)
- Banco: TDWC na instância PostgreSQL do Master (tws-hwa, 172.18.0.10:5432) — compartilhado com o database TWS do engine
