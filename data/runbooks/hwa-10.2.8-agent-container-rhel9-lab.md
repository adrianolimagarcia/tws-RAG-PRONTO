# HWA 10.2.8 Dynamic Agent em Container RHEL 9 (Docker) — Runbook

Status: executed in Docker container (RHEL 9.8 UBI-init, CachyOS host) on 2026-09-09.
Laboratory procedure. Reuse of lab passwords/self-signed certs in production is forbidden.

## Escopo

Instalar um **dynamic agent** do HCL Workload Automation 10.2.8 em container proprio
(`tws-agent`) e conectá-lo ao broker do MDM existente (`tws-hwa`, broker `MDM_DWB`),
validando execução de jobs de ponta a ponta. Complementa o runbook do BMDM
(hwa-10.2.8-container-rhel9-lab.md).

## Arquitetura (lab)

| Componente | Container | IP (rede hwa-mesh 172.18.0.0/24) | Papel |
|---|---|---|---|
| MDM + broker | tws-hwa | 172.18.0.10 | master, PostgreSQL, MDM_DWB (broker, 31116) |
| BMDM | tws-bmdm | 172.18.0.11 | backup master (FTA full-status) |
| **Agent** | **tws-agent** | **172.18.0.12** | **dynamic agent (kit AGENT)** |

## Pré-requisitos

- Kit `HWA_10.2.8_LNX_X86_64_AGENT.zip` (669MB; neste lab veio do Google Drive — o kit
  MDM NÃO contém o instalador de agente standalone com `twsinst` na raiz).
- Broker acessível: `-tdwbhostname` deve resolver para o host onde o broker roda
  (aqui `tws-hwa.lab` → 172.18.0.10, porta HTTPS do broker 31116).
- Certificados PEM: `ca.crt`, `tls.key`, `tls.crt` (CA lab; mesmo padrão do MDM/BMDM).
  A pasta PEM deve ser **gravável** pelo instalador (ele gera keystores/truststores).
- Usuário de SO `wauser` (mesma senha do ecossistema) + credencial REST do broker
  (`-wauser/-wapassword` ou `-apikey`).

## Procedimento

1. **Container**: mesmo padrão dos demais (UBI-init, `--privileged`, cgroup rw, 2G/3G):
   ```bash
   SDB=/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/docker
   mkdir -p $SDB/tws-agent/{data,installers,ssl-certs}
   docker run -d --name tws-agent --hostname tws-agent \
     --memory=2g --memory-swap=3g --privileged \
     -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
     -v $SDB/tws-agent/data:/data \
     -v $SDB/tws-agent/installers:/installers:ro \
     -v $SDB/tws-agent/ssl-certs:/opt/ssl-certs:ro \
     --network hwa-mesh --ip 172.18.0.12 \
     registry.access.redhat.com/ubi9/ubi-init:latest
   ```
2. **SO**: `dnf install -y --allowerasing unzip tar gzip openssl procps-ng passwd sudo
   hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless`; criar
   `wauser` com a mesma senha; `sysctl -w kernel.hostname=tws-agent.lab`;
   `/etc/hosts`: `172.18.0.10 tws-hwa.lab` e `127.0.0.1 tws-agent.lab`.
3. **Kit**: extrair em `/tmp/kit` (`unzip -q`). Binário: `TWS/LINUX_X86_64/twsinst`.
4. **Pasta PEM gravável** (o mount `/opt/ssl-certs` é `:ro`): copiar PEMs para
   `/opt/agent-ssl` com ownership `wauser` (644; `tls.key` 600).
5. **Instalar**:
   ```bash
   cd /tmp/kit/TWS/LINUX_X86_64
   ./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
     -thiscpu AGT1 -tdwbhostname tws-hwa.lab -tdwbport 31116 \
     -sslkeysfolder /opt/agent-ssl -sslpassword <pw> \
     -wauser wauser -wapassword <pw>
   # -> AWSFAB033I The installation has completed successfully.
   # Instala em /opt/HCL/TWA_wauser (TWS + TWSDATA)
   ```
6. **Registro no broker** (automático, ~1-2 min): o JobManager do agente envia recursos
   (`AWSITA083I Resource information was sent to https://tws-hwa.lab:31116/JobManagerRESTWeb/...`).
   O broker cria a workstation no banco — o nome registrado deriva do **hostname do
   container**:
   - Neste lab (09/09), o hostname era `tws-agent` e o `-thiscpu` era `AGT1` →
     o broker registrou **`TWS-AGENT`** (base do hostname), NÃO o `-thiscpu`.
   - Nos labs de 13/10 (caminhos B e C), o hostname do container foi feito **igual**
     ao `-thiscpu` (ex.: `TWS-LAB-AUTH-C`) → o broker registrou **exatamente o
     `-thiscpu`**.
   - **Recomendação prática:** dar ao container um hostname igual ao `-thiscpu`
     pretendido, para os dois baterem (ver "Achados", item 1).
7. **Incluir no plano** (a workstation só aparece após virada/extensão do plano):
   ```bash
   # no MDM, como wauser:
   JnextPlan          # virada normal (ou -for 0000 p/ extensão curta)
   conman "limit TWS-AGENT#;10"     # liberar limite (default 0)
   ```
   Pitfall: se a primeira virada falhar com `AWSJPL006E` (workstation cannot be loaded),
   garantir que o node resolva no MDM: `/etc/hosts` → `172.18.0.12 tws-agent.lab tws-agent`.
8. **Validar execução**:
   ```bash
   # definir stream (nome <= 16 chars; job INLINE com DOCOMMAND — sem isso AWSJDB303E)
   composer add agt_jobstream.def   # SCHEDULE TWS-AGENT#AGTTESTJS ... : TWS-AGENT#AGT_ECHO DOCOMMAND "..." STREAMLOGON wauser TASKTYPE UNIX RECOVERY STOP
   conman "sbs TWS-AGENT#AGTTESTJS"
   conman sj "@#AGTTESTJS.@"        # -> SUCC rc0
   # prova real: out.log nos archives do JobManager do agente:
   # /opt/HCL/TWA_wauser/TWSDATA/stdlist/JM/<data>/archive/*.zip -> out.log
   ```

## Validação observada (2026-09-09)

- Instalação: `AWSFAB033I` rc ok; JobManager + agente ITA ativos no tws-agent.
- Registro: workstation `TWS-AGENT` (tipo A) no banco; heartbeat `AWSITA083I` a cada 2min.
- Plano: run #29 (end 09/10 00:04); `TWS-AGENT 29 UNIX AGENT 10 LBI J M`.
- Job: `AGTTESTJS/AGT_ECHO` → SUCC rc0 (2 instâncias); out.log contém
  `AGT_DYNAMIC_OK` + `Linux tws-agent.lab 7.2.2-1-cachyos x86_64 GNU/Linux`.

## 9. Modo Híbrido: Instalação com BOTH (FTA + Dynamic Agent Concomitantes)

O utilitário `twsinst` suporta o parâmetro `-agent both`, permitindo que um único nó execute
tanto como Fault-Tolerant Agent clássico (Symphony / Netman / Mailman na porta 31111) quanto como
Dynamic Agent moderno (Broker / JobManager na porta 31114).

### Passos de Execução:
1. **Marcar Workstation Antiga como Ignorada no Master (se aplicável)**:
   ```bash
   composer "update cpu=TWS-AGENT; set ignore=on; noask"
   # Verifica com: composer "display cpu=TWS-AGENT" -> Coluna Ignored = Y
   ```
2. **Desinstalação Limpa do Agente Anterior**:
   ```bash
   # Deve ser executado a partir do diretório de instalação da instância:
   cd /opt/HCL/TWA_wauser/TWS
   ./twsinst -uninst -uname wauser -wait 0
   ```
3. **Instalação com -agent both**:
   ```bash
   cd /installers/extracted/TWS/LINUX_X86_64
   ./twsinst -new -agent both -acceptlicense yes -uname wauser \
     -thiscpu AGT1 -master MDM -port 31111 \
     -tdwbhostname tws-hwa.lab -tdwbport 31116 \
     -sslkeysfolder /opt/agent-ssl -sslpassword <pw> \
     -wauser wauser -wapassword <pw>
   # -> AWSFAB033I The installation has completed successfully.
   ```
4. **Cadastrar a Workstation FTA no Composer**:
   ```bash
   composer "add agt1_fta.def"
   # CPUNAME AGT1
   #   OS UNIX NODE tws-agent.lab TCPADDR 31111 DOMAIN MASTERDM
   #   FOR MAESTRO TYPE FTA AUTOLINK ON FULLSTATUS ON
   # END
   ```
5. **Estender o Plano e Liberar Limits**:
   ```bash
   JnextPlan -for 0000
   conman "limit AGT1# 10"
   conman "limit TWS-AGENT_1# 10"
   ```
6. **Validação**: Ambos os jobs executam em paralelo:
   - `AGT1#FTA_JOBSTREAM.FTA_ECHO` -> `SUCC rc0` via Netman/Jobman.
   - `TWS-AGENT_1#DYN_JOBSTREAM.DYN_ECHO` -> `SUCC rc0` via Broker/JobManager.


## Pitfalls (todos observados no lab)

- Kit AGENT ≠ kit MDM: só `twsinst` (sem `serverinst.sh`).
- Nome da workstation no broker deriva do **hostname do container** (lab 09/09:
  `tws-agent` → `TWS-AGENT`; labs 13/10: hostname = `-thiscpu` → registra o
  `-thiscpu` exato). Para os dois baterem, hostname do container = `-thiscpu`.
- Workstation dinâmica só entra no plano via JnextPlan/ResetPlan (não em tempo real).
- `AWSJPL006E` na virada: node sem FQDN resolvível → adicionar alias `.lab` no /etc/hosts do MDM.
- Job stream name máx. 16 chars (`AWSJOM012E`); job referenciado sem definição inline → `AWSJDB303E`.
- `-sslkeysfolder` deve ser gravável (instalador gera keystores; mount `:ro` falha).
- Limit default 0 pós-entrada no plano → `conman "limit <WS>#;10"` (o `#` evita AWSBHU048E
  quando o nome é prefixo de outro, ex.: MDM_BK vs MDM_BKA).

## Achados do lab twsinst (caminhos de autenticação B/A, 2026-10-13)

1. **`-thishost` não existe no twsinst 10.2.8** (verificado via `twsinst -u`).
   O hostname do container cumpre o papel de identificar o host. O nome que vai para o
   master é o `-thiscpu` (máx. 16 chars, sem espaços, não começa com número, ≠ nome
   do master). Observação do lab: para dynamic agents, o broker pode registrar o nome
   derivado do **hostname** em vez do `-thiscpu` — dar ao container um hostname igual
   ao `-thiscpu` pretendido para os dois baterem.

2. **A senha vaza em plaintext no log de instalação.** O `-wapassword` é mascarado
   (`****`), mas o `tdwb_pwd` (mesma credencial, usada no download REST) é registrado
   em claro: 1x na linha de comando java do instalador + 3x em
   `INFO: key tdwb_pwd value ...` no log
   `TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log`.
   Destruir o log (ou redigir o `tdwb_pwd`) após a instalação. Em containers throwaway
   o log é destruído com a remoção do container.

3. **Workstation auto-criada nasce com `LIMIT 0` no plano** — jobs submetidos ficam
   em `READY` eternamente. Liberar antes de testar:
   `conman "limit cpu=<NOME>;10"` (com ponto-e-vírgula; a forma com espaço,
   `limit cpu=<nome> <n>`, dá "ambiguous selector").

4. **Sintaxe do composer 10.2.8 (lab):** `; noask` quebra o `display`
   (usar sem: `composer "display cpu=@"`); `composer add` lê arquivo **dentro do
   container** (fazer `docker cp` + `chmod 644` antes); definição de job usa header
   `$JOBS` e keyword `DOCOMMAND` (não `SCRIPTNAME`/`ARGS`); o job precisa existir
   antes do stream que o referencia (criar o job primeiro, depois o stream).

5. **Caminho C (JWT via `-apikey`, 2026-10-13):** gerar a API key via
   `POST https://<MDM>:31116/twsd/api/v2/apikey` (basic auth com usuário/senha
   do TWS; body `{"label":"<nome>","type":"PERSONAL"}` — o campo de nome é
   `label`, e `type` é enum **maiúsculo**: `PERSONAL` ou `SERVICE`); instalar com
   `./twsinst ... -thiscpu <NOME> -tdwbhostname <mdm> -tdwbport 31116 -apikey <JWT>`
   (cenário C puro: sem `-wauser`/`-wapassword`, sem flags de certificado).
   O JWT vaza em plaintext no log de instalação (`APIKEY = <JWT>` na seção
   `checkSSLValuesForAgent`) — destruir o log após a instalação.
   Nota: o endpoint do DWC (`:9443/twsd/api/v2/apikey`) exigiu o parâmetro
   `engines` e retornou erro de autenticação com basic auth neste lab; o endpoint
   do engine MDM (`:31116`) funcionou.
   **Variante não validada neste lab:** `-jwt true` + `-wauser`/`-wapassword`
   (sem `-apikey`) — o instalador baixa o token JWT do broker usando as
   credenciais, em vez de exigir o JWT pronto. Ver
   `twsinst-flags-complete-reference.md`, seção 4.
## Como criar e apagar uma API key (JWT) — 2026-10-13

Operações validadas no lab contra o **engine do MDM** (`tws-hwa`, 172.18.0.10).
O endpoint do DWC (`https://<DWC>:9443/twsd/api/v2/apikey`) **não** funcionou
neste lab: exigiu o parâmetro `engines` e retornou `AUTHORIZATION_ERROR` com
basic auth. Usar o endpoint do engine, em **HTTPS** (HTTP puro na 31116 não
responde — é a porta do netman; o `twsd` REST do engine atende em TLS).

- **Criar:** `POST https://<MDM>:31116/twsd/api/v2/apikey`
  - basic auth com usuário/senha do TWS, `-k` (cert self-signed),
    `Content-Type: application/json`
  - body exato: `{"label":"<nome>","type":"PERSONAL"}` — o campo de nome é
    `label` (outros nomes dão `AWSJOM001E`); `type` é obrigatório e o enum é
    **maiúsculo**: `PERSONAL` ou `SERVICE` (minúsculas dão `AWSMAC020E`)
  - resposta `201`: `{"token":"<JWT>"}` (JWT RS256, ~1132 bytes, TTL 1 ano)
  - efeito colateral observado: criar uma key `PERSONAL` com label X também
    cria uma key `SERVICE` de mesmo label (com usuário derivado `<label>-<hash>`)
- **Descobrir o id da key:** o UUID está no claim `apikeyUuid` do payload do
  JWT (decodificar o segmento do meio em base64url); ou consultar o banco:
  tabela `mdl.aky_api_keys` no postgres (DB `TWS`, dentro do container do MDM)
  — colunas `aky_id` (uuid, PK), `aky_label`, `aky_user`, `aky_type` (`P`/`S`),
  `aky_created`, `aky_expiration`
- **Listar:** `GET https://<MDM>:31116/twsd/api/v2/apikey` — ⚠️ **não
  confiável nesta versão**: retornou `{"count":0}` mesmo com 5 keys válidas no
  banco (e `?limit=100` devolveu HTTP 500). Para conferir de verdade, usar o
  banco (`SELECT count(*) FROM mdl.aky_api_keys;`) ou `GET` por id
- **Apagar:** `DELETE https://<MDM>:31116/twsd/api/v2/apikey/{apiKeyId}`
  (basic auth) → `200`; `GET` do mesmo id depois retorna `404`. Ciclo
  completo validado em 2026-10-13 (criar → apagar → 404; tabela zerada no banco)
- **Segurança:** o token JWT só é exibido **uma vez**, na resposta do POST —
  não salvar em disco (ou salvar `0600` e destruir com `shred -u` após o uso).
  Sem o token, a key é inutilizável, mas o registro continua válido por 1 ano:
  apagar o registro via `DELETE` quando não for mais preciso. Nos relatórios,
  segredos sempre redigidos como `<JWT>` / `<senha>` — nunca valores reais.

## Caminho A funcional em deploy real: PKI compartilhada com o master (procedimento)

O lab do caminho A (2026-10-13, relatório em
`docs/sessoes/lab-twsinst-auth-paths/RELATORIO-caminho-A-sslkeys.md`) provou que o
`twsinst` instala perfeitamente com `-sslkeysfolder` + `-sslpassword`, mas a
workstation **nunca foi registrada** no master: com CA fresca e isolada, a
confiança PKI não é mútua — o agente não confia no broker (cert `CN=tws-hwa.lab`
emitido pela CA do ecossistema) e o broker não confia no agente (cert emitido
pela CA fresca). Para o caminho A funcionar, a CA usada precisa ser confiável
pelos dois lados. Este é o procedimento.

### 1. Onde fica a CA do master

No container do MDM (`tws-hwa`, verificado em 2026-10-14):

| Item | Caminho |
|---|---|
| CA do ecossistema (cert) | `/opt/hwa/TWSDATA/ssl/depot/ca.crt` (também em `/opt/ssl-certs/ca.crt`) — `CN=TWS-HWA-Lab-CA`, self-signed |
| Truststore do master | `/opt/hwa/TWSDATA/ssl/certs/TWSClientTrustStore.p12` e `.pem` |
| Keystore do master | `/opt/hwa/TWSDATA/ssl/certs/TWSClientKeyStore.p12` |

⚠️ **A `ca.key` (chave privada da CA) NÃO está no master** (verificado com
`find` no container). Sem ela, o operador não consegue assinar certificados
novos a partir do container. Opções:
- (a) usar a `ca.key` do ponto onde os certificados foram gerados originalmente
  (neste lab, fora do container);
- (b) gerar uma CA nova dedicada e distribuí-la (ver item 4).

### 2. Assinar o certificado do agente com a CA do ecossistema

Com a `ca.key` + `ca.crt` da CA do ecossistema em mãos (no host, nunca dentro do
container do agente):

```bash
# Chave do agente + CSR (CN = hostname do agente; SAN com hostname e FQDN —
# o broker valida o hostname)
openssl genrsa -out agent-tls.key 2048
openssl req -new -key agent-tls.key -out agent-tls.csr -subj "/CN=<hostname-agente>" \
  -addext "subjectAltName=DNS:<hostname-agente>,DNS:<hostname-agente>.lab"
# Assinar com a CA do ecossistema
openssl x509 -req -in agent-tls.csr -CA ca-ecossistema.crt -CAkey ca-ecossistema.key \
  -CAcreateserial -out agent-tls.crt -days 365 -sha256 \
  -extfile <(printf "[v3_req]\nsubjectAltName=DNS:<hostname-agente>,DNS:<hostname-agente>.lab\n")
openssl verify -CAfile ca-ecossistema.crt agent-tls.crt   # agent-tls.crt: OK
```

### 3. Direção agente→broker: o agente confia no master

Monte a pasta PEM para o `twsinst` com **a CA do ecossistema** + o cert do agente:

```bash
# /opt/agent-ssl (gravável, dono wauser):
#   ca.crt          <- CA do ecossistema (/opt/hwa/TWSDATA/ssl/depot/ca.crt do master)
#   tls.key         <- agent-tls.key (600)
#   tls.crt         <- agent-tls.crt (644)
./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
  -thiscpu <NOME> -tdwbhostname <master> -tdwbport 31116 \
  -sslkeysfolder /opt/agent-ssl -sslpassword <senha>
```

O instalador gera os keystores do agente
(`TWSDATA/ssl/certs/TWSClientKeyStore.p12` e `TWSClientTrustStore.{p12,pem}`) já
confiando no broker — foi exatamente assim que o lab original (09/09) funcionou:
mesma CA nos 3 nós (MDM, BMDM, agente).

Correção pós-instalação (se o agente já foi instalado com outra CA): anexar a CA
do ecossistema ao truststore do agente e reiniciar o JobManager (o agente ITA o
reinicia sozinho):

```bash
# no container do agente, como root:
TS=/opt/HCL/TWA_wauser/TWSDATA/ssl/certs
cat /caminho/ca-ecossistema.crt >> $TS/TWSClientTrustStore.pem
keytool -importcert -trustcacerts -alias ecossistema-ca \
  -file /caminho/ca-ecossistema.crt -keystore $TS/TWSClientTrustStore.p12 \
  -storetype PKCS12 -storepass <senha-do-keystore>   # VERIFICAR NO AMBIENTE
```

### 4. Direção broker→agente: o master confia no agente (CA própria isolada)

Se em vez da CA do ecossistema você optou por CA própria isolada, o broker
encerra o handshake (`Failure when receiving data from the peer` — observado no
lab). É preciso adicionar sua CA ao truststore do **master**:

```bash
# no container do master (tws-hwa), como root:
TS=/opt/hwa/TWSDATA/ssl/certs
cp /caminho/sua-ca.crt $TS/   # guardar cópia junto aos demais certs
cat /caminho/sua-ca.crt >> $TS/TWSClientTrustStore.pem
keytool -importcert -trustcacerts -alias minha-ca-isolada \
  -file /caminho/sua-ca.crt -keystore $TS/TWSClientTrustStore.p12 \
  -storetype PKCS12 -storepass <senha-do-keystore>   # VERIFICAR NO AMBIENTE
# reiniciar o broker/master para recarregar o truststore   # VERIFICAR NO AMBIENTE
```

### Resumo da decisão

| Situação | O que fazer |
|---|---|
| Você tem a `ca.key` da CA do ecossistema | Itens 2 + 3: assine o cert do agente com ela |
| Você NÃO tem a `ca.key` | Item 4: distribua sua CA própria para o truststore do master |
| Dúvida sobre a senha do keystore `.p12` | Gerenciada pelo produto; não invente — verifique no ambiente antes de rodar o keytool |
