# Troubleshooting — AI Data Advisor (AIDA) 10.2.8 Docker

Sintomas, causas e soluções observadas/validadas em laboratório WSL2
(HWA 10.2.8, Docker 29.7.2, Compose v5.5.0). Evidência lab completa em
`data/evidence/lab-validation-2026-08-25-aida-docker.jsonl`; runbook P33 em
`data/runbooks/hwa-10.2.8-wsl-lab.md`.

---

## 1. Container aida-es em `Restarting` com ExitCode 137 / OOMKilled

**Sintoma:** `docker ps` mostra `aida-es` reiniciando; `docker inspect` retorna
`ExitCode=137 OOMKilled=true`. dmesg: `Memory cgroup out of memory: Killed
process (java) anon-rss:2089460kB`.

**Causa:** OpenSearch 2.19.6 com heap default (metade do limite do cgroup) +
Lucene mmap + Netty off-heap excedem o memory limit do container. Os limits
default do `docker-compose.yml` do pacote (es 8G) são inviáveis em máquinas com
pouca RAM.

**Solução (lab com 11.5GiB):**
```yaml
# docker-compose.yml, serviço es
environment:
  - "DISABLE_INSTALL_DEMO_CONFIG=true"
  - "ES_JAVA_OPTS=-Xms768m -Xmx768m"
  - "OPENSEARCH_JAVA_OPTS=-Xms768m -Xmx768m"   # OpenSearch 2.x lê esta variável
deploy:
  resources:
    reservations: { cpus: "1.5", memory: 1.5G }
    limits:       { cpus: "2",   memory: 3G }
```
Reduzir também limits de outros serviços: keycloak 768M, predictor 768M, ui 512M.
Recriar: `docker compose -f docker-compose.yml up -d`.

**Pré-requisito no HOST (não no container):**
```bash
sudo sysctl -w vm.max_map_count=262144
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```
O OpenSearch aborta se `vm.max_map_count < 262144` (o Dockerfile-es já grava essa
config no sysctl.conf da imagem, mas ela não é aplicada dentro do container).

---

## 2. `NameResolutionError: Failed to resolve 'wa-waserver'` (aida-exporter)

**Sintoma:** logs do exporter com `HTTPConnectionPool(host='wa-waserver',
port=31116): Max retries exceeded ... Failed to resolve 'wa-waserver'`; exporter
em restart-loop.

**Causa:** o hostname do servidor WA (ex.: `wa-waserver`) não resolve dentro da
rede docker quando o MDM/DWC rodam no host (fora do docker).

**Solução:** adicionar `extra_hosts` nos serviços AIDA:
```yaml
extra_hosts:
  - "wa-waserver:host-gateway"
  - "MDMHOST:host-gateway"
  - "host.docker.internal:host-gateway"
```
`host-gateway` = IP do gateway da bridge docker (ex.: 172.17.0.1), que alcança o
host WSL2 onde roda o engine REST V2 (31116).

---

## 3. UI do AIDA retorna HTTP 405 `Host not matching`

**Sintoma:** `https://localhost:9432/` → 405 com mensagem `Host not matching,
check the EXTERNAL_HOSTNAME environment variable.`

**Causa:** o nginx do AIDA valida o header Host contra `EXTERNAL_HOSTNAME`
(common.env). Acessar por hostname/porta diferente do configurado é recusado.

**Solução:**
```bash
# common.env
EXTERNAL_HOSTNAME=<IP-exato-usado-no-browser>
# ex.: EXTERNAL_HOSTNAME=127.0.0.1 -> usar https://127.0.0.1:9432/
./AIDA.sh restart
```
Este parâmetro também é obrigatório por segurança (previne HTTP Host Header
attacks — exigência HCL).

---

## 4. `Cannot extract kpi definitions` / `no kpi definition found for host`

**Sintoma:** exporter logs com `Cannot extract kpi definitions` ou `no kpi
definition found for host wa-waserver:31116`; índice `kpis-definition` vazio.

**Causa:**
- Endpoints `/twsd/engine/definition/{alert,kpi,aida_catalog}` exigem autenticação
  basic (401 sem credencial) — credenciais não configuradas ou erradas.
- O orchestrator ainda não processou as definições (agenda: predição a cada
  1440 min, alertas a cada 15 min).

**Solução:**
1. Confirmar credenciais no OpenSearch:
   ```bash
   docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/wa-credentials/_search?size=5"
   ```
   Esperado: doc `wa-waserver:31116` com `username=wauser`, password cifrado.
2. Recriar credenciais (fluxo não-interativo):
   ```bash
   docker compose --profile config up -d config
   ENCPASS=$(docker exec aida-config sh -c 'echo -n "<pw>" | openssl enc -AES-128-ECB -base64 -salt -pbkdf2 -pass env:OPENSSL_PASSWORD')
   printf 'y\n' | docker exec -i aida-config bash -c "source /config.sh && add_credentials wa-waserver:31116 <user> '$ENCPASS'"
   ```
   Nota: o dispatch final do config.sh é `$1 $2` (repassa só 2 args); com 3 args
   o fluxo cai no modo interativo e o input piped corrompe o doc (host='n'/'y').
   Use o `bash -c "source ... && add_credentials ..."` acima.
3. Aguardar o ciclo do orchestrator ou reiniciar o exporter.

---

## 5. Container aida-exporter/predictor em restart-loop

**Sintoma:** exporter ou predictor reiniciando; logs com `ConnectionError` para
`aida-es:9200`.

**Causa:** dependência do OpenSearch — os serviços tentam conectar antes do
aida-es estar pronto (ou o es está OOM, ver item 1).

**Solução:** corrigir o aida-es primeiro (item 1); depois reiniciar os
dependentes: `docker restart aida-exporter aida-predictor aida-orchestrator`.

---

## 6. `CONTAINER_RUNTIME is not set` ao executar AIDA.sh

**Sintoma:** `./AIDA.sh build-start` falha com `Error: CONTAINER_RUNTIME is not
set. Please export it before running this script.`

**Causa:** o AIDA.sh exige a variável de ambiente para detectar docker ou podman.

**Solução:**
```bash
export CONTAINER_RUNTIME=docker   # ou podman
```

---

## 7. OpenSearch cluster `yellow` (1 node)

**Sintoma:** `_cluster/health` → status yellow.

**Causa:** réplicas não alocadas (single-node lab; default replica count).

**Solução:** nenhuma — é o estado esperado em lab com 1 nó. Para silenciar:
```bash
curl -sk -u admin:admin -X PUT "https://localhost:9200/_settings" \
  -H 'Content-Type: application/json' -d '{"index":{"number_of_replicas":0}}'
```

---

## Referências

- AIDA User's Guide 10.2.8: https://help.hcl-software.com/workloadautomation/v1028/common/src_ai/awsaimst_welcome.html
- Deploy README oficial: https://github.com/HCL-TECH-SOFTWARE/HCL-AI-Data-Advisor-For-HCL-Workload-Automation
- Claims: `hwa-10.2.8-aida-*` (data/evidence/claims.jsonl)
- Evidência lab: `data/evidence/lab-validation-2026-08-25-aida-docker.jsonl`
- Runbook: seção P33 em `data/runbooks/hwa-10.2.8-wsl-lab.md`
---

## 8. Notificacao por email nao enviada (aida-email)

**Sintoma:** alertas gerados mas nenhum email recebido; logs do aida-email mostram
`Message Type message / Received Message: {}` sem envio.

**Causa:** SMTP nao configurado no common.env. Os parametros SMTP_SERVER, SMTP_PORT,
SENDER_MAILID, SENDER_MAILPWD, RECIPIENT_MAILIDS e HOST_IP sao obrigatorios apenas
"if you want to receive anomaly notification by email" (doc oficial); sem eles o
container processa as mensagens do Redis (internal event manager) mas nao envia.

**Solucao:**
```bash
# common.env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_MAILID=alertas@empresa.com
SENDER_MAILPWD=<senha>
RECIPIENT_MAILIDS=admin@empresa.com,ops@empresa.com
HOST_IP=<aida-ip>:9432
./AIDA.sh restart
```

## 9. Predicoes nao geradas (predictions index vazio)

**Sintoma:** `POST /api/actions/retrain` retorna `{"result":true}` mas o indice
OpenSearch `predictions` fica com count=0; retrain-details mostra
`predictionsSubmited: 0`.

**Causa:** o modelo (prophet/neural) precisa de uma serie temporal historica
minima de metricas; no lab com poucas horas de coleta, nao ha dados suficientes
para gerar predicoes (DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180).

**Solucao:** aguardar coleta de metricas por alguns dias (o retrain automatico
roda a cada 24h) ou verificar se o exporter esta coletando:
```bash
docker logs aida-exporter | tail    # deve mostrar "Kpis collected and saved"
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/metric-index-*/_count"
```

## 10. API REST do AIDA retorna 403/404

**Sintoma:** `/api/*` retorna 403 sem token; `Cannot GET /api/actions/retrain` ao
usar GET quando o endpoint e POST.

**Causa:** (a) falta o Bearer JWT do Keycloak; (b) metodo HTTP errado. O swagger
(https://<host>:9432/api/swagger/) documenta o metodo correto de cada endpoint.

**Solucao:**
```bash
TOKEN=$(curl -sk -X POST "https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password" -d "client_id=nginx" -d "username=aidaadmin" -d "password=<default-ou-alterada>")
curl -sk -H "Authorization: Bearer $TOKEN" "https://<host>:9432/api/kpi/list"   # POST
curl -sk -X POST -H "Authorization: Bearer $TOKEN" "https://<host>:9432/api/actions/retrain"  # POST
```

## 11. Ciclo de alertas nao roda (detectAlerts ausente)

**Sintoma:** `docker logs aida-orchestrator` nao mostra `callAlertAPI`.

**Causa:** o orchestrator agenda a deteccao de alertas via PROPHET_ORCHESTRATOR
`schedule_alert` (default 15 min) e predicoes via `schedule` (default 1440 min =
24h). Se o container reiniciou, o ciclo recomeca do boot.

**Solucao:** verificar o env e reiniciar se necessario:
```bash
docker exec aida-orchestrator sh -c 'echo $PROPHET_ORCHESTRATOR'  # {"schedule":1440,"schedule_alert":15}
docker restart aida-orchestrator
```
Log esperado (ciclo OK): `callAlertAPI - POST /detectAlerts status=200 for definition=...`

## 12. UI do AIDA nao acessivel / Keycloak realm aida

**Sintoma:** login direto na UI (https://<aida-ip>:9432) falha ou redireciona.

**Causa/contexto:** o realm Keycloak e "aida", client publico "nginx", usuarios
default aidaadmin (role aida-admin) e admin (role keycloak-admin, console em
https://<ip>:<porta>/keycloak/auth/admin). O EXTERNAL_HOSTNAME precisa ser o host
exato usado no browser (senão 405).

**Solucao:** logar com aidaadmin; verificar EXTERNAL_HOSTNAME; para acesso externo
sem Keycloak, usar o widget no Workload Dashboard do DWC (ou adicionar excecao de
certificado no antivirus, ex.: Kaspersky, que bloqueia o self-signed).

---

## 13. Predictor nao gera predicoes (retrain retorna true mas predictions vazio)

**Sintoma:** `POST /api/actions/retrain` retorna `{"result":true}`, mas o
indice OpenSearch `predictions` fica count=0; logs do predictor mostram
`Worker failed to boot` ou `plotly failed`.

**Causas possiveis:**
1. **Serie temporal insuficiente** — o modelo prophet/neural precisa de dias
   de metricas para treinar; com poucas horas de coleta, nao ha dados
   historicos minimos (DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180).
2. **Predictor sem acesso ao OpenSearch** — no boot o predictor pode falhar
   se o aida-es ainda nao estiver pronto (`ConnectionRefusedError`). O
   container reinicia (gunicorn) e recupera quando o es fica disponivel.
3. **Modelo prophet ausente** — logs mostram `Importing plotly failed` mas
   isso e apenas para graficos interativos, nao impede o treino.

**Solucoes:**
```bash
# 1. Verificar se o exporter esta coletando metricas
docker logs aida-exporter | grep "Kpis collected"
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/metric-index-*/_count"

# 2. Verificar se o predictor alcanca o OpenSearch
docker exec aida-predictor sh -c 'python3 -c "import urllib.request, ssl, base64;   ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE;   auth=base64.b64encode(b"admin:admin").decode();   r=urllib.request.urlopen(urllib.request.Request("https://aida-es:9200/",   headers={"Authorization":"Basic "+auth}), context=ctx, timeout=8); print(r.status)"'

# 3. Aguardar coleta de metricas por pelo menos 24h (ciclo de retrain automatico)
# 4. Forcar retrain manual via API
curl -sk -X POST -H "Authorization: Bearer $TOKEN" "https://127.0.0.1:9432/api/actions/retrain"
```

---

## 14. Keycloak — usuario nao consegue logar no AIDA

**Sintoma:** login na UI do AIDA (https://<aida-ip>:9432/) falha com
"Invalid username or password" ou redireciona para login novamente.

**Contexto:** o Keycloak do AIDA tem realm "aida" com client publico "nginx"
e dois usuarios default:
- `aidaadmin` / `admin` — role `aida-admin` (acesso a UI do AIDA, KPIs, alertas, special days, tuning)
- `admin` / `admin` — role `keycloak-admin` (acesso ao admin console do Keycloak)

**Solucoes:**
1. Verificar se o Keycloak esta rodando: `docker ps | grep aida-keycloak`
2. Testar o issuer: `curl -sk https://<host>:9432/keycloak/auth/realms/aida/.well-known/openid-configuration`
3. Obter token via API (testar credenciais):
   ```bash
   TOKEN=$(curl -sk -X POST "https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=password" -d "client_id=nginx" -d "username=aidaadmin" -d "password=<senha>")
   ```
4. Acessar o admin console: `https://<aida-ip>:9432/keycloak/auth/admin` (login admin/admin)
5. Verificar usuarios no realm: `GET /auth/admin/realms/aida/users` (token master realm)
6. Se o token expirou ou o client foi desconfigurado, recriar o realm a partir
   do `aida-realm.json` (em /opt/keycloak/data/import/ no container).

---

## 15. OpenSearch — indices amarelos/vermelhos ou disco cheio

**Sintoma:** `docker exec aida-es curl -sk -u admin:admin .../_cluster/health`
retorna status `yellow` ou `red`; indices com `docs.deleted` alto.

**Causa:** cluster single-node (yellow e normal); replicas nao alocadas por
falta de nos adicionais. Indices vermelhos indicam shards primarios nao
alocados (falta de disco ou config errada).

**Solucoes:**
```bash
# 1. Verificar saude do cluster
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/_cluster/health?pretty"

# 2. Verificar indices
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/_cat/indices?v"

# 3. Verificar disk space do container
docker exec aida-es df -h /usr/share/opensearch/data

# 4. Remover replicas em single-node (yellow -> green)
docker exec aida-es curl -sk -u admin:admin -X PUT "https://localhost:9200/_settings" \
  -H 'Content-Type: application/json' -d '{"index":{"number_of_replicas":0}}'

# 5. Se vm.max_map_count resetou apos reboot:
sudo sysctl -w vm.max_map_count=262144
# Persistir: echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

---

## 16. Certificados SSL — DWC_PUBLIC_KEY errado, self-signed bloqueado

**Sintoma:** AIDA nao consegue se conectar ao DWC; erro "certificate_unknown"
nos logs do aida-nginx; navegador bloqueia acesso com Kaspersky.

**Causa:** o `DWC_PUBLIC_KEY` no common.env precisa ser a chave publica do
certificado SSL do Liberty (DWC). Se o certificado do DWC foi alterado ou
regenerado, o AIDA nao valida a conexao.

**Solucoes:**
```bash
# 1. Obter a chave publica correta do DWC
openssl x509 -in /opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/resources/security/key.pem \
  -inform PEM -outform PEM 2>/dev/null | head -30

# 2. Atualizar DWC_PUBLIC_KEY no common.env
#    (substituir o certificado entre "-----BEGIN CERTIFICATE-----" e "-----END CERTIFICATE-----")

# 3. Reconstruir e reiniciar
./AIDA.sh build-start

# 4. Para Kaspersky (certificado self-signed):
#    Configuracoes -> Rede -> Excluir localhost:9443
#    Ou usar https://127.0.0.1:9432/ (se EXTERNAL_HOSTNAME=127.0.0.1)
```

---

## 17. Exporter — "Failed to download catalogs" / "no kpi definition found"

**Sintoma:** logs do exporter mostram `Failed to download catalogs` ou
`no kpi definition found for host wa-waserver:31116`; indices
kpis-definition e alert-definitions vazios.

**Causa:** o endpoint `/twsd/engine/definition/{alert,kpi,aida_catalog}`
exige autenticacao basic (401 sem credencial). O exporter le as credenciais
do indice wa-credentials no OpenSearch — se as credenciais estao ausentes
ou corrompidas, o exporter nao consegue baixar as definicoes.

**Solucoes:**
```bash
# 1. Verificar credenciais no OpenSearch
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/wa-credentials/_search?size=5"
# Esperado: doc com host=wa-waserver:31116, username=wauser

# 2. Recriar credenciais (fluxo nao-interativo)
docker compose --profile config up -d config
ENCPASS=$(docker exec aida-config sh -c 'echo -n "<pw>" | openssl enc -AES-128-ECB -base64 -salt -pbkdf2 -pass env:OPENSSL_PASSWORD')
printf 'y\n' | docker exec -i aida-config bash -c "source /config.sh && add_credentials wa-waserver:31116 <user> '\$ENCPASS'"

# 3. Verificar se o hostname wa-waserver resolve
docker exec aida-exporter sh -c 'python3 -c "import socket; print(socket.gethostbyname("wa-waserver"))"'
# Se falhar, adicionar extra_hosts no docker-compose.yml

# 4. Testar o endpoint manualmente
docker exec aida-exporter sh -c 'curl -sk -u wauser:<pw> "https://wa-waserver:31116/twsd/engine/definition/kpi" | head -c 300'
```

---

## 18. Docker network — containers nao se alcancam

**Sintoma:** logs de varios containers mostram `Failed to resolve '<hostname>'`
ou `Connection refused` para servicos internos (aida-es, aida-redis, wa-waserver).

**Causa:** Sem `extra_hosts`, os containers na rede docker bridge nao
resolvem o hostname do servidor WA (wa-waserver) nem do host WSL2. O
Docker Compose cria uma rede interna (aida-net) onde os servicos se
encontram pelo nome do servico no compose (ex.: aida-es, aida-redis).

**Solucoes:**
```bash
# 1. Verificar resolucao interna
docker exec aida-exporter sh -c 'python3 -c "import socket; [print(h, "->", socket.gethostbyname(h)) for h in ["aida-es","aida-redis","wa-waserver","host.docker.internal"]]"'

# 2. Adicionar extra_hosts no docker-compose.yml (se WA esta no host)
#    wa-waserver:host-gateway
#    MDMHOST:host-gateway
#    host.docker.internal:host-gateway

# 3. Recriar containers
docker compose up -d

# 4. Porta conflitante: verificar se 9432/9443/31116 ja estao em uso
netstat -tlnp 2>/dev/null | grep -E "9432|9443|31116"
```

---

## 19. AIDA REST API — 403/404 nos endpoints

**Sintoma:** chamadas para `/api/*` retornam 403 (Forbidden) ou 404 (Not Found).

**Causa:** 403 = falta do Bearer token JWT do Keycloak (ou token invalido);
404 = metodo HTTP errado (GET vs POST) ou path errado.

**Solucoes:**
```bash
# 1. Obter token (aidaadmin, realm aida, client nginx)
TOKEN=$(curl -sk -X POST "https://127.0.0.1:9432/keycloak/auth/realms/aida/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password" -d "client_id=nginx" -d "username=aidaadmin" -d "password=admin")

# 2. Testar com token
curl -sk -H "Authorization: Bearer $TOKEN" "https://127.0.0.1:9432/api/kpi/list"  # POST
curl -sk -X POST -H "Authorization: Bearer $TOKEN" "https://127.0.0.1:9432/api/actions/retrain"  # POST

# 3. Verificar documentacao dos endpoints (swagger)
#    https://<aida-ip>:9432/api/swagger/

# 4. Se o token expirou, obter um novo (default: expires_in = 300s = 5min)
```

---

## 20. HWA Messages — como usar o Message Help

**Sintoma:** mensagens de erro no log do MDM/DWC/agente como AWKTSA050E,
AWSITA104E, EQQQnnn, etc.

**Causa:** cada mensagem tem um codigo especifico com causa e acao
documentadas no guia Messages and Codes 10.2.8.

**Solucao:**
```bash
# 1. Acessar o Message Help online
#    https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmsghelp.html
#    (buscar pelo codigo exato da mensagem)

# 2. Troubleshooting Guide PDF (completo)
#    https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf
#    (download do PDF completo de troubleshooting)

# 3. Mensagens comuns ja documentadas no dataset:
#    - AWKTSA050E: dynamic agent SSL — verificar localopts, porta SSL
#      (claim hwa-10.2.8-incident-awktsa050e-restart-0001)
#    - AWSITA104E: resource scan agent — verificar porta SSL e restart
#    - EQQQnnn: scheduler messages (consultar o Message Help)

# 4. Support HCL (casos nao resolvidos):
#    https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0128257
#    (Dynamic Agent stops accepting connections from Master)
```

---

## 21. vm.max_map_count reseta apos reboot — persistencia

**Sintoma:** apos reiniciar o host, o OpenSearch (aida-es) nao sobe com
ExitCode 137/OOM, mesmo com os limites de memoria corretos.

**Causa:** o `vm.max_map_count` e um parametro do kernel, nao persistente
por padrao. O Dockerfile-es tenta gravar em /etc/sysctl.conf dentro da
imagem, mas isso nao afeta o HOST.

**Solucao (persistente):**
```bash
# Verificar valor atual
sysctl vm.max_map_count

# Definir ate o proximo reboot
sudo sysctl -w vm.max_map_count=262144

# Persistir entre reboots (Ubuntu/Debian)
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf

# Para WSL2, adicionar ao /etc/wsl.conf tb nao persiste entre wsl --shutdown
# Melhor: adicionar ao /etc/sysctl.conf e ao script de boot do WSL
# (opcional) /etc/init.wsl ou .profile com sysctl -w
```

---

## 22. Logs e tracing avancado — coleta de diagnosticos

**Sintoma:** precisa de logs detalhados para debugging.

**Procedimento:**
```bash
# 1. Coletar logs de todos os containers AIDA
./AIDA.sh dump  # cria diretorio docker_logs/ com logs individuais + nginx logs

# 2. Nivel de log (via common.env)
#    LOG_LEVEL=DEBUG (default INFO) — para todos exceto UI
#    DEBUG: (para UI) — em ./configuration.sh

# 3. Logs especificos por servico
docker logs aida-exporter    # coleta de metricas
docker logs aida-orchestrator # ciclo de predicao/alertas
docker logs aida-predictor    # treino do modelo
docker logs aida-ad           # deteccao de anomalias
docker logs aida-nginx        # proxy reverso (acessos, auth)
docker logs aida-keycloak     # autenticacao

# 4. OpenSearch slow queries
docker exec aida-es curl -sk -u admin:admin "https://localhost:9200/_cat/thread_pool?v"

# 5. FFDC (First Failure Data Capture) — erros do Liberty (DWC)
#    /opt/hwa/DWC/DWC_DATA/stdlist/appserver/dwcServer/logs/ffdc/
```

---

## 23. Alerta falso positivo — como reduzir sensibilidade

**Sintoma:** AIDA dispara alertas sem motivo aparente; KPIs estaveis mas
geram alert-instances.

**Causa:** a sensibilidade do modelo de deteccao pode estar muito alta para
o perfil de carga do ambiente.

**Solucoes:**
1. Aumentar a tolerancia via common.env (requer restart):
   ```
   ANOMALY_USE_TOLERANCE=true
   ANOMALY_FIXED_TOLERANCE=1.0
   ANOMALY_PERCENTAGE_TOLERANCE=0.02
   ```
2. Adicionar Special Days (feriados, ferias, janelas de manutencao) na UI
   do AIDA para aumentar a tolerancia em datas sazonais.
3. Pausar alertas individuais via UI (Alerts -> Alert Definitions -> Pause).
4. Aumentar `ALERT_ANOMALOUS_POINTS_REQUIRED` (de 10 para 15, por exemplo).
5. Verificar se o modelo ja foi retreinado com dados suficientes
   (retrain automatico a cada 24h).
