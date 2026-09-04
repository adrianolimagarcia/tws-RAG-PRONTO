# Troubleshooting — HWA 10.2.8 Componentes (Conman, OCLI, DWC, MDM, Dynamic Agent)

Sintomas, causas e soluções observadas/validadas em laboratório WSL2.

---

## 1. Conman — comandos falham ou conexão recusada

**Sintoma:** `conman` retorna `Connection refused`, `cannot connect to broker`,
ou `broker is not responding`.

**Causa:** o Conman conecta no broker (JnextPlan - JNP) via porta 31116 (TLS)
ou 41116 (TCP). Se o broker não está rodando ou o firewall bloqueia:

**Solução:**
```bash
# Verificar se o broker está rodando
ps -ef | grep "JnextPlan\|MailMan" | grep -v grep

# Verificar porta 31116
ss -tln | grep 31116

# Verificar conectividade
curl -sk https://MDMHOST:31116/twsd/ 2>/dev/null | head -c 200

# Forçar restart do broker (como wauser)
su - wauser -c 'cd /opt/hwa/MDM/bin && ./conmanrc stop'
su - wauser -c 'cd /opt/hwa/MDM/bin && ./conmanrc start'

# Verificar arquivo de configuração
cat $CONFHOME/config | grep -E "BROKER|HOST|PORT"
```

---

## 2. Conman — "showcpus" sem output ou incompleto

**Sintoma:** `conman showcpus` retorna vazio ou apenas cabeçalho.

**Causa:** o broker pode estar em manutenção ou o `conmanrc` não inicializou
completamente. O `showcpus` lista as workstations registradas no domínio.

**Solução:**
```bash
# Verificar se o broker está ativo (deve mostrar linhas de workstations)
conman showcpus | head -20

# Tentar com usuário explícito
conman @user=wauser showcpus

# Verificar se o engine server está rodando
ps -ef | grep -i engineServer | grep -v grep

# Verificar logs do broker
tail -100 $LOGDIR/broker.log 2>/dev/null | grep -i error
```

---

## 3. OCLI — "OCLI is not responding"

**Sintoma:** `ocli` ou `ocli -h <host>` retorna `OCLI is not responding`,
`Connection refused` ou `OCLI version mismatch`.

**Causa:** o OCLI (Orchestration CLI) conecta-se ao engine REST V2 via
HTTPS (porta 31116). O servidor REST pode estar inativo, ou o certificado
SSL não foi aceito, ou a versão do OCLI difere da do servidor.

**Solução:**
```bash
# Verificar versão do OCLI
ocli --version

# Verificar versão do servidor
curl -sk https://MDMHOST:31116/twsd/ | grep -oE "version[^<]+" | head -1

# Verificar conectividade REST
curl -sk -o /dev/null -w "%{http_code}" https://MDMHOST:31116/twsd/

# Forçar confirmação de certificado (primeira conexão)
ocli -h MDMHOST --accept-certificate

# Verificar engine server
ps -ef | grep engineServer | grep -v grep
```

---

## 4. OCLI — "F3-SNAPSHOT" e versão incompatível

**Sintoma:** OCLI informa `stable_F3-SNAPSHOT` (versão de desenvolvimento)
ou erro de versão ao conectar.

**Causa:** o OCLI `stable_F3-SNAPSHOT` é uma versão de desenvolvimento
(pré-release) do AIDA. O servidor pode estar rodando uma versão diferente.

**Solução:**
```bash
# Verificar a versão exata do OCLI e do servidor
ocli --version
curl -sk https://MDMHOST:31116/twsd/ | grep -oE "F3|SNAPSHOT|[0-9]+\.[0-9]+\.[0-9]+"

# Em caso de incompatibilidade, usar o OCLI do mesmo kit de instalação
# O OCLI fica em /opt/hwa/MDM/OCLI/
```

---

## 5. DWC — login loop (página de login volta após autenticar)

**Sintoma:** após logar no DWC (https://localhost:9443/console/login.jsp),
a página retorna ao login sem mensagem de erro.

**Causa:** cookie LTPA não aceito, cache do navegador, ou relógio do
servidor/cliente dessincronizado (LTPA token sensível a tempo).

**Solução:**
```bash
# 1. Limpar cache e cookies do navegador
# 2. Verificar sincronismo de horário
date; wsl -d Ubuntu -- date

# 3. Verificar se o LTPA token está sendo emitido
curl -sk -c /tmp/dwc-cookies.txt https://localhost:9443/console/login.jsp -o /dev/null
curl -sk -b /tmp/dwc-cookies.txt -c /tmp/dwc-cookies.txt -o /dev/null -w "%{http_code}\n" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://localhost:9443/console/login.jsp" \
  --data "j_username=wauser" --data "j_password=<senha>" \
  https://localhost:9443/console/j_security_check
grep -c LtpaToken2 /tmp/dwc-cookies.txt  # deve ser 1

# 4. Se LTPA não for emitido, verificar usuário/senha no basicRegistry
cat /opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/configDropins/overrides/authentication_config.xml
```

---

## 6. DWC — "Cannot read engine connection" ou engine offline

**Sintoma:** ao acessar o DWC, a engine connection MDM_LAB aparece como
offline ou "Cannot read engine connection".

**Causa:** o engine REST V2 não está acessível a partir do DWC. O hostname
`MDMHOST` não resolve, ou a porta 31116 está fechada, ou o certificado
SSL do engine não é confiável para o DWC.

**Solução:**
```bash
# 1. Verificar engine connection no banco
export PGPASSWORD=padrao
psql -h 127.0.0.1 -U postgresdwc -d TDWC -c "SELECT id, name, hostname, portnumber, remoteservername, username FROM tdwc.tdwc_engineconnection"

# 2. Verificar se o hostname MDMHOST resolve
cat /etc/hosts | grep MDMHOST

# 3. Verificar REST V2 do engine
curl -sk -o /dev/null -w "%{http_code}\n" https://MDMHOST:31116/twsd/

# 4. Verificar engineServer
ps -ef | grep engineServer | grep -v grep
```

---

## 7. MDM (engine) — engineServer não sobe

**Sintoma:** `engineServer` não inicia; log mostra `JVM terminated` ou
`OutOfMemoryError` ou `Port already in use`.

**Causa:** o engineServer (Java) pode estar sem memória suficiente (heap),
ou a porta 31116/31117 já está em uso, ou o arquivo de configuração
está corrompido.

**Solução:**
```bash
# 1. Verificar logs do engine
tail -100 /opt/hwa/MDM/engineServer/logs/engineServer.log 2>/dev/null | grep -iE "error|exception|outofmemory|killed"

# 2. Verificar porta
ss -tln | grep 31116

# 3. Ajustar heap (em engineServer.sh ou setEnv.sh)
#    -Xms512m -Xmx2048m

# 4. Reiniciar
su - wauser -c 'cd /opt/hwa/MDM/bin && ./engineServer stop'
su - wauser -c 'cd /opt/hwa/MDM/bin && ./engineServer start'
```

---

## 8. MDM — PostgreSQL "too many connections" ou "connection refused"

**Sintoma:** engineServer ou DWC não conseguem conectar ao PostgreSQL;
log mostra `too many connections` ou `connection refused` para 127.0.0.1:5432.

**Causa:** o PostgreSQL pode ter atingido o limite de conexões
(max_connections), ou o serviço não está rodando, ou o pg_hba.conf
não permite conexão do host/usuário.

**Solução:**
```bash
# 1. Verificar status do PostgreSQL
sudo -u postgres pg_isready 2>/dev/null || psql -h 127.0.0.1 -U postgres -c "SELECT 1" 2>&1

# 2. Verificar conexões ativas
export PGPASSWORD=padrao
psql -h 127.0.0.1 -U postgresdwc -d TDWC -c "SELECT count(*) FROM pg_stat_activity WHERE datname='TDWC'"

# 3. Aumentar max_connections (postgresql.conf)
#    max_connections = 200 (default 100)

# 4. Reiniciar PostgreSQL
#    sudo systemctl restart postgresql-18 2>/dev/null || pg_ctlcluster 18 main restart
```

---

## 9. Dynamic Agent — "AWKTSA050E" SSL certificate problem

**Sintoma:** log do agente dinâmico mostra `AWKTSA050E` (erro de
certificado SSL); agente não conecta ao master domain manager.

**Causa:** o certificado SSL do master não é confiável pelo agente, ou
a porta SSL está incorreta no `localopts`.

**Solução:**
```bash
# 1. Verificar localopts do agente
cat $AGENTDIR/localopts | grep -E "SSL|PORT|HOST|BROKER"

# 2. Verificar porta SSL (default 31116 para TLS)
#    SSLPort=31116 em localopts

# 3. Reiniciar o agente
cd $AGENTDIR && ./ShutDownLwa && ./StartUpLwa

# 4. Ou forçar download do certificado
cd $AGENTDIR && ./ShutDownLwa && rm -f cert/*.pem && ./StartUpLwa
```

---

## 10. Dynamic Agent — agente não registra no master

**Sintoma:** `conman showcpus` não mostra o agente; log do agente mostra
`cannot connect to broker` ou `broker not found`.

**Causa:** o agente não consegue alcançar o broker (hostname/porta errados
no localopts, ou firewall bloqueando).

**Solução:**
```bash
# 1. Verificar hostname do broker no localopts
cat $AGENTDIR/localopts | grep BROKERHOST

# 2. Verificar se o broker hostname resolve
ping -c 1 <broker-hostname>

# 3. Verificar conectividade com a porta do broker
timeout 3 bash -c '</dev/tcp/<broker-hostname>/31116' 2>/dev/null && echo "OK" || echo "FAIL"

# 4. Se necessário, editar localopts e reiniciar
#    BROKERHOST=<hostname-correto>
#    BROKERPORT=31116
```

---

## 11. REST API V2 — 401 Unauthorized / API Key inválida

**Sintoma:** chamadas para `https://MDMHOST:31116/twsd/` retornam
HTTP 401 Unauthorized.

**Causa:** a REST API V2 exige autenticação (basic auth, API Key, ou
JWT). Sem credenciais válidas, o endpoint retorna 401.

**Solução:**
```bash
# 1. Testar com basic auth (wauser)
curl -sk -u wauser:<senha> "https://MDMHOST:31116/twsd/engine/info"

# 2. Criar API Key (via OCLI ou comando)
#    ocli apikey create --name minha-key --user wauser

# 3. Usar API Key:
curl -sk -H "x-api-key: <api-key-value>" "https://MDMHOST:31116/twsd/engine/info"

# 4. Verificar endpoints REST V2
curl -sk -u wauser:<senha> "https://MDMHOST:31116/twsd/engine/workload"
```

---

## 12. Referências

- Troubleshooting Guide 10.2.8: https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf
- Messages and Codes: https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmst_welcome.html
- REST API V2: https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1restapiv2.html
- Developer's Guide (PDF): https://help.hcl-software.com/workloadautomation/v1028/awsddmst.pdf
- Message Help: https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmsghelp.html

## 13. Composer — syntax error ou falha ao compilar job stream

**Sintoma:** `composer` retorna syntax error, ou o job stream nao compila; mensagens AWSJCL521E, AWSBIN091E.

**Causa:** erro de sintaxe no JCL (Job Control Language) do composer, ou o arquivo de definicao (.jcl) tem formato incorreto.

**Solucao:**
```bash
# Validar sintaxe do JCL
composer parse /caminho/arquivo.jcl

# Verificar logs do composer
tail -100 <LOGDIR>/composer.log | grep -iE "error|syntax|invalid"

# Revisar o JCL: verificar delimitadores, chaves, variaveis
# Documentacao de sintaxe: help.hcl-software.com/v1028/distr/src_ref/awsrgcompsyntax.html
```

## 14. Planman — falha ao gerar plano (JnextPlan)

**Sintoma:** `planman` ou `JnextPlan` falha com mensagens AWSJPL017E, AWSJPL018E, ou o plano nao e gerado.

**Causa:** o JnextPlan (gerador de plano) pode falhar por conflitos de scheduling, dependencias nao resolvidas, ou recursos insuficientes.

**Solucao:**
```bash
# Verificar logs do JnextPlan
tail -200 <LOGDIR>/JnextPlan.log | grep -iE "error|exception|failed"

# Verificar se o JnextPlan esta rodando
ps -ef | grep JnextPlan | grep -v grep

# Forcar geracao de plano
conman "jnextplan"

# Verificar recursos do plano
conman "showjobs"
```

## 15. EDWA — event rule nao dispara

**Sintoma:** event rule configurada no EDWA (Event-driven Workload Automation) nao dispara quando a condicao ocorre.

**Causa:** configuracao de evento incorreta (filtro, acao, engine), ou o event processor nao esta rodando.

**Solucao:**
```bash
# Verificar se o event processor esta rodando
ps -ef | grep -i event | grep -v grep

# Verificar rules cadastradas
conman "switeventprocessor @rule=*"

# Verificar logs do EDWA
tail -100 <LOGDIR>/edwa.log | grep -iE "event|rule|trigger|error"

# Revisar a rule: condicao, acao, engine destino
# Documentacao: help.hcl-software.com/v1028/common/src_gi/eqqg1edwa.html
```

## 16. MailMan — email nao enviado

**Sintoma:** MailMan nao envia notificacoes por email; mensagens na fila do MailMan (mailbox).

**Causa:** configuracao SMTP incorreta (servidor, porta, autenticacao), ou o MailMan nao esta rodando.

**Solucao:**
```bash
# Verificar se o MailMan esta rodando
ps -ef | grep MailMan | grep -v grep

# Verificar a fila de mensagens
mailbox -l

# Verificar configuracao SMTP no arquivo de configuracao
cat <CONFHOME>/config | grep -iE "SMTP|MAIL|EMAIL"

# Forcar processamento da fila
mailbox -p
```

## 17. Broker — conexao recusada entre broker e agentes

**Sintoma:** agentes nao conseguem conectar ao broker; broker log mostra conexoes recusadas.

**Causa:** firewall, hostname incorreto, ou porta errada (31116 para TLS, 41116 para TCP).

**Solucao:**
```bash
# Verificar se o broker esta rodando
ps -ef | grep -i "JnextPlan|MailMan" | grep -v grep

# Verificar porta do broker
ss -tln | grep -E "31116|41116"

# Verificar hostname do broker no localopts do agente
cat <AGENTDIR>/localopts | grep -E "BROKERHOST|BROKERPORT"

# Testar conectividade
timeout 3 bash -c '</dev/tcp/<broker-host>/31116' 2>/dev/null && echo "OK" || echo "FAIL"
```

## 18. Referencias adicionais

- Conman syntax: https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgconman.html
- Planman/JnextPlan: https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgplanman.html
- Composer syntax: https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgcompsyntax.html
- EDWA event rules: https://help.hcl-software.com/workloadautomation/v1028/common/src_gi/eqqg1edwa.html
- MailMan: https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmailman.html
## 19. DWC — troca de certificado SSL (procedimento correto)

**Sintoma:** ao substituir o certificado self-signed do DWC por um assinado por CA,
o DWC para de responder (handshake TLS falha); curl retorna 000.

**Causa (2 tentativas documentadas em lab):**
- **Tentativa 1 (openssl pkcs12)**: o PKCS12 gerado por openssl e incompativel
  com o keystore que o Liberty espera — a cadeia valida (verify OK) mas o
  handshake falha com "TLSv1.3 alert decode error". (evidencia 0079)
- **Tentativa 2 (keytool -importkeystore)**: a conversao para keytool gera um
  keystore valido, mas o Liberty rejeita com **CWPKI0024E** — "The server
  certificate alias specified by the attribute serverKeyAlias is either not
  found in KeyStore ... or it is invalid". Ou seja, o DWC usa um
  `serverKeyAlias` especifico que nao e o 'default'. (evidencia 0081)

**Procedimento correto (requer senha do keystore original):**
```bash
# 1. Decifrar a senha {aes} do keystore original (ssl_variables.xml, chave 1787657107)
#    via Java com classpath completo do Liberty:
#    com.ibm.websphere.crypto.PasswordUtil.decode("{aes}...") com wlp.password.encryption.key setado

# 2. Listar o alias original do keystore:
keytool -list -keystore TWSServerKeyFile.p12 -storetype PKCS12 -storepass <senha-decifrada>

# 3. Gerar CSR com a MESMA chave do keystore original e assinar com a CA:
keytool -certreq -alias <alias-original> -keystore TWSServerKeyFile.p12 -storepass <senha> -file server.csr

# 4. Importar a cadeia assinada mantendo o alias original:
keytool -importcert -alias <alias-original> -file dwc-server.crt -keystore TWSServerKeyFile.p12 -storepass <senha>

# 5. Reiniciar o DWC (stopAppServer.sh + startAppServer.sh)
```

**Observacoes criticas:**
- O alias do keystore original deve ser PRESERVADO (nao usar 'default').
- A senha do keyStore e do trustStore sao DIFERENTES, ambas {aes} no
  ssl_variables.xml (chave wlp.password.encryption.key).
- Se trocar a senha do keystore, atualizar SOMENTE o keyStore.password {aes}
  (manter trustStore.password original).
- A cadeia validar (verify OK) nao garante handshake funcional — o formato e o
  alias importam.
- O metodo manual openssl/keytool com alias 'default' NAO funciona; em producao
  usar o procedimento oficial HCL de regeneracao de keystore.

**Referencias:** evidencias lab hwa-lab-10.2.8-dwc-cert-ca-attempt-0079 (openssl)
e hwa-lab-10.2.8-dwc-cert-keytool-0081 (keytool/CWPKI0024E).
