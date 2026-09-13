# HWA 10.2.8 MDM + PostgreSQL em Container RHEL 9 (Docker) — Runbook

Status: executed in Docker container (RHEL 9.8 UBI-init, CachyOS host) on 2026-09-04.
Laboratory procedure. Reuse of lab passwords/self-signed certs in production is forbidden.

## Ambiente validado

- HCL Workload Automation MDM 10.2.8.00 Linux x86_64 (kit `HWA_10.2.8_MDM_LINUX_X86_64.zip`).
- Container: `registry.access.redhat.com/ubi9/ubi-init:latest` (systemd) com
  `--memory=4g --memory-swap=6g --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:rw`.
- PostgreSQL 18.6 (PGDG EL9) local, database `TWS`, schemas mdl/dwb/evt/log/pln.
- Open Liberty 26.0.0.3 (`/opt/liberty/wlp`) — SHA-256 `bf394f83...` idêntico ao lab WSL2.
- Java 21 embutido do HWA (IBM Semeru OpenJ9) + `java-21-openjdk-headless` p/ o Liberty.
- Usuário `wauser`; hostname do container `tws-hwa.lab` (`sysctl -w kernel.hostname`).
- Workstations: `MDM` (UNIX MASTER), `MDMDA` (agent), `MDMXA` (x-agent FINAL), `MDM_DWB` (broker).

## Pré-requisitos de PACOTES no RHEL 9 UBI (não documentados oficialmente — descobertos no lab)

```bash
dnf install -y unzip tar gzip openssl procps-ng passwd sudo hostname which curl \
  diffutils libxcrypt-compat java-21-openjdk-headless
```

| Pacote | Motivo | Falha sem ele |
|---|---|---|
| `diffutils` | `cmp` usado pelo twsinst na importação de certificados | `cmp: command not found`, rc=127 |
| `libxcrypt-compat` | `makesec` linkado contra `libcrypt.so.1` (RHEL 9 nativo só tem .so.2) | `makesec: error while loading shared libraries: libcrypt.so.1` |

Ubuntu/WSL2 não precisa deles (cmp e libcrypt.so.1 nativos) — por isso não aparecem nos
runbooks do lab WSL.

## Procedimento (uma passada só — crítico)

1. Extrair o kit e conferir `buildinfo.properties` (min wlp 26.0.0.3).
2. PostgreSQL: PGDG EL9 → initdb → start → senha do `postgres` (`ALTER USER ... PASSWORD`).
3. Open Liberty: download público IBM + extrair em `/opt/liberty` + `chmod -R a+rX`.
4. `useradd -m -s /bin/bash wauser`; hostname do container via sysctl.
5. Certificados lab em pasta FORA do INST_DIR (`/opt/ssl-certs`): `ca.crt` (CA self-signed),
   `tls.key`/`tls.crt` (server CN=tws-hwa.lab assinado pela CA); ownership `wauser`, 644.
   **NUNCA dentro do INST_DIR** (serverinst exige INST_DIR vazio — WAINST050E).
6. `configureDb.sh -f configureDbPostgresql.properties` (RDBMS_TYPE=POSTGRESQL,
   COMPONENT_TYPE=MDM, DB TWS, loopback:5432) → WAINST077I/WAINST052I.
7. `serverinst.sh -f serverinst.properties` COMPLETO, INST_DIR vazio, de UMA vez:
   `ACCEPTLICENSE=yes`, `THISCPU=MDM`, `DISPLAYNAME=MDMDA` (distintos — AWSFAB164E),
   `XANAME=MDMXA`, `WLP_INSTALL_DIR=/opt/liberty/wlp`, `WA_USER=wauser`,
   `RDBMS_TYPE=POSTGRESQL` + credenciais, `SSL_KEY_FOLDER=/opt/ssl-certs`, `START_SERVER=true`.
   → WAINST023I success; servidores: netman 31111/31113, JobManager 31114, EIF 31131.
8. `JnextPlan -for 0000` como wauser (com `source /opt/hwa/TWS/tws_env.sh`)
   → AWSJCL074I Symphony loaded.
9. Validar: `conman showcpus` → `Batchman LIVES`; `conman status`; `planman showinfo`.

## Pitfalls de rerun (todos observados)

- **serverinst.sh NÃO retoma**: reexecutar após falha parcial do twsinst falha no check de
  INST_DIR vazio (WAINST050E) ou no twsinst -new (AWSFAB022E "previous instance"). O
  `AWSFAB057I script can be run again` refere-se ao twsinst INTERNO (retoma do passo
  falho), mas deixa as fases configureDatasource/configureWlp/waPostConfigure órfãs.
  **Correto: recomeçar limpo** (`rm -rf /opt/hwa /tmp/wa10.2.8.00`) com o serverinst.sh.
- **Resíduos de keystore AES**: toda execução que passa por runSecurityEncryption cria
  `TWSDATA/ssl/aes/key.p12`+`key.sth`; o gerador PKCS#12 nunca sobrescreve. Antes de
  QUALQUER rerun do twsinst: `rm -f /opt/hwa/TWSDATA/ssl/aes/key.p12 .../key.sth`.
- INST_DIR deve estar vazio; certificados fora dele.
- Passwords nos logs do serverinst aparecem mascaradas (`xxxxx`) — o comando exato do
  twsinst fica registrado para reconstrução.
- No container, `hostnamectl set-hostname` falha ("Device or resource busy") — usar
  `sysctl -w kernel.hostname=<nome>`.

## Evidências

- `evidence/lab-validation-2026-09-04-*.jsonl`: configuredb-container-rhel9-0001,
  serverinst-inst-dir-0001, serverinst-missing-cmp-0001, serverinst-wrapper-rerun-0001,
  twsinst-keystore-residue-0001, twsinst-libcrypt-0001, twsinst-aes-clean-each-rerun-0001,
  serverinst-no-skip-twsinst-0001, serverinst-full-success-0001.
- Validação cruzada com o runbook WSL2 (`hwa-10.2.8-wsl-lab.md`): mesmas mensagens
  (WAINST077I/052I, AWSJCL074I, Batchman LIVES) e mesmos schemas.

---

# HWA 10.2.8 DWC (Dynamic Workload Console) — container RHEL 9 (Docker)

Status: installed and validated in the same container (RHEL 9.8 UBI-init) on 2026-09-04.

## Procedimento (após o MDM)

1. Extrair o kit DWC (`HWA_10.2.8_DWC_LINUX_X86_64.zip`) — o kit tem `configureDb.sh`,
   `dwcinst.sh` e os properties NA RAIZ (diferente do kit MDM, que usa TWS/LINUX_X86_64/).
2. `configureDb.sh -f configureDbPostgresql.properties` do DWC: COMPONENT_TYPE=DWC,
   DB_NAME=**TDWC** (não DWC), role dedicada `postgresdwc` (criar antes com LOGIN PASSWORD).
   → WAINST077I/WAINST052I.
3. `dwcinst.sh -f dwcinst.properties`: DWC_INST_DIR=/opt/hwa/DWC,
   WLP_INSTALL_DIR=/opt/liberty/wlp, RDBMS_TYPE=POSTGRESQL + credenciais TDWC,
   **DWC_ADMIN_USER + DWC_ADMIN_PW obrigatórios** (sem → WAINST024E), SSL_KEY_FOLDER,
   START_WLP=false (início manual). → WAINST023I; console em https://HOST:9443/console/.
4. **Criar o usuário SO do admin** (o dwcinst NÃO cria): `useradd -m -s /bin/bash dwcadmin`
   + `chown -R dwcadmin:dwcadmin /opt/hwa/DWC` — o `startAppServer.sh` só roda como o owner.
5. Iniciar: `su - dwcadmin -c 'cd /opt/hwa/DWC/appservertools && ./startAppServer.sh'`.
6. Login/validação via curl exige **headers de browser** (User-Agent + Origin + Referer do
   login.jsp): GET em URL protegida (cookie WASReqURL) → POST j_security_check com headers →
   302 + LtpaToken2 → GET /console/ → 200. Sem os headers: 400 silencioso (sem log).

## Achados DWC (evidências lab-validation-2026-09-04-dwc-*.jsonl)

- `dwc-configuredb-rhel9-0001` — configureDb DWC OK (TDWC) cross-plataforma WSL 0052.
- `dwcinst-full-success-0001` — dwcinst OK; DWC_ADMIN_USER/PW obrigatórios; usuário SO do
  admin não é criado pelo instalador (startAppServer "only the owner").
- `dwc-login-requires-browser-headers-0001` — POST j_security_check sem headers de browser
  → 400 silencioso; com headers → 302 + LtpaToken2 + dashboard 200 (não documentado no WSL).

## Environment do usuário de instalação (wauser) no login

- **Sintoma**: `su - wauser` (ou SSH) → `conman: command not found`; variáveis TWS_* ausentes.
- **Causa raiz (difere do WSL!)**: no UBI/RHEL o `useradd -m` cria `~/.bash_profile`
  (que mascara o `~/.profile` do runbook WSL). O source do env deve ir no `.bash_profile`.
- **Fix**: adicionar ao `/home/wauser/.bash_profile`:
  `if [ -f /opt/hwa/TWS/tws_env.sh ]; then . /opt/hwa/TWS/tws_env.sh; fi`
  (mesmo padrão com `/opt/hwa/DWC/dwc_env.sh` para o `dwcadmin`).
- **Validação**: `su - wauser -c 'conman showcpus'` → "Environment Successfully Set" +
  CPUID MDM/MDMXA. SSH com comando direto não lê login profile → usar sessão interativa
  ou `bash -lc "..."`.

## Sfinal — job streams FINAL e FINALPOSTREPORTS (IMPORTANTÍSSIMO)

O Sfinal é o coração da automação do plano de produção: os streams de exemplo
que o HWA instala para automatizar o ciclo diário (JnextPlan + relatórios).

- **O instalador JÁ importa o Sfinal** (serverinst/twsinst): os objetos existem no
  banco como `MDMXA#FINAL` e `MDMXA#FINALPOSTREPORTS` — verificado neste lab com
  `composer display js=MDMXA#FINAL` (AWSBIA291I Total objects: 1). NÃO é preciso
  `composer add Sfinal` (se rodar: AWSJCL015W "already exists").
- Arquivo fonte: `/opt/hwa/TWS/Sfinal` (idêntico a `/opt/hwa/TWS/config/Sfinal`).
- **Definição** (do arquivo): `SCHEDULE MDMXA#FINAL ON EVERYDAY AT 2359 MATCHING
  SAMEDAY CARRYFORWARD`; `FINALPOSTREPORTS` com `SCHEDTIME 2359`. O FINAL segue o
  SWITCHPLAN do ciclo anterior (PREVIOUS); o FINALPOSTREPORTS segue o SWITCHPLAN
  do FINAL.
- **Jobs**: FINAL = STARTAPPSERVER (roda startAppServer.sh), MAKEPLAN, SWITCHPLAN;
  FINALPOSTREPORTS = CHECKSYNC, CREATEPOSTREPORTS, UPDATESTATS (6 jobs + 2 streams
  no MDMXA — cross-check com o lab WSL `hwa-lab-10.2.8-sfinal-import-0006`).
- **Validação do plano (lição WSL 0007, replicada aqui)**:
  - `JnextPlan -for 0000` → plano zero-duration, SEM instâncias (horizonte zero).
  - `JnextPlan -for 2400` → instancia o FINAL às 23:59 do dia de produção.
  - ⚠️ Fora do timing (madrugada, depois do run 2400 do dia já ter passado) o
    `-for 2400` processa com "0 Jobs Logged" e o plano fica sem instâncias —
    validar DENTRO do dia de produção (antes das 23:59) ou conferir no ciclo
    noturno automático (batchman processa o run 2400 às 23:59).

## Modelo de plano (dia vigente 00:05 + D+1 automático) e timezone

**Modelo documentado (WSL, evidência startofday-0005)**: o dia de produção inicia às
`00:05` (`optman chg sd=0005` → AWSJCL050I), o plano é o do dia vigente e sempre avança
para D+1 automaticamente. O mecanismo de virada é o **Sfinal** (streams FINAL +
FINALPOSTREPORTS no MDMXA): o FINAL roda às 23:59 e executa STARTAPPSERVER → MAKEPLAN
(gera o plano de D+1) → SWITCHPLAN (ativa); o FINALPOSTREPORTS (após o SWITCHPLAN) roda
CHECKSYNC → CREATEPOSTREPORTS → UPDATESTATS. A corrente se auto-sustenta: cada plano
gerado contém o FINAL do dia seguinte.

**Aplicado no container (2026-09-05)**:
1. `optman chg sd=0005` → startOfDay = 0005 (AWSJCL050I; efetiva após o próximo JnextPlan).
2. `composer add Sfinal` → re-adiciona `MDMXA#FINAL` e `MDMXA#FINALPOSTREPORTS` (importados
   pelo instalador; removidos 2026-09-04 a pedido do dono — evidência sfinal-definitions-removed;
   re-adicionados pois são o mecanismo de virada D+1; NUNCA deletá-los: quebram o rollover,
   claim destructive-cleanup-lesson-0100).
3. `conman "lc MDM;10;noask"` + `conman "lc MDMXA;10;noask"` → LIMIT 10 (default pós-instalação
   é 0 = "no jobs run at any time"; a forma longa `limit cpu` dá AWSBHU048E de ambiguidade).
4. **Timezone**: o container nasceu UTC (default docker) → o "dia vigente" do TWS ficava 3h
   adiantado do fuso do dono (America/Sao_Paulo). Trocado via `ln -sf
   /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime` + `/etc/timezone`.
   ⚠️ A troca só vale p/ processos NOVOS: o domínio MDM roda como processos manuais não-systemd
   (engineServer Java Liberty + netman ppid=1, orquestrados pelo agente ITA — unit
   `tebctl-tws_cpa_agent_wauser.service` — e por `/opt/hwa/TWS/config/start_tws.sh`, que
   condiciona o start do netman a um arquivo Symphony ausente no 10.2.8). Para o fuso valer
   100% é preciso reiniciar o domínio (evidência timezone-sao-paulo-0001).

**Comandos do modelo (evitar -for 0000/default que só estendem sem instanciar o Sfinal)**:
- `JnextPlan -for 2400` → instancia FINAL/FINALPOSTREPORTS no plano do dia de produção.
- Extensão explícita: `JnextPlan -for 24:00` / `-days 1` / `-for 48:00`.
- JnextPlan repetidos com `-for 0000`/default (2026-09-04) esticaram o plano até ~09/25 sem
  instanciar o FINAL e deixaram um FINAL atrasado de 09/04 que rodou fora de hora
  (STARTAPPSERVER SUCC → MAKEPLAN ABEND rc8 → SWITCHPLAN/FINALPOSTREPORTS HOLD), travando a
  corrente. Recuperação documentada (runbook WSL, seção ResetPlan): `ResetPlan` sem `-scratch`
  (com backup) + rebuild `JnextPlan -from <dia> 0000 -for 2400`.

## Correção do modelo: dia de produção 00:05 BR + D+1 automático (2026-09-05)

**Sintoma**: JnextPlan com `-from <dia> 0000` ancorava o início do dia de produção em
`21:00 BR` (herança da meia-noite UTC do container original, criado em UTC) → o dia
vigente ficava deslocado 3h do calendário local. Aviso `AWSJPL206W`: timezones habilitados
no banco mas o MDM não inclui timezone → usa o do sistema.

**Causa raiz**: o `-from ... 0000` explícito força um corte de dia que não respeita o
`startOfDay`; a doc adverte que `-from` sem timezone explícito pode ser deslocado.

**Correção**: `optman chg sd=0005` (startOfDay 00:05) + timezone do SO
`America/Sao_Paulo` + **`JnextPlan` SEM `-from`** (após `ResetPlan -scratch`) →
`Plan creation start time: 09/05/2026 00:05 TZ America/Sao_Paulo`; production plan
09/05 00:05 → 09/06 00:04. Dia vigente alinhado ao calendário BR, sempre D+1.

**Ciclo FINAL validado (evidência final-cycle-d1-rollover)**: o FINAL do dia executa
STARTAPPSERVER→MAKEPLAN→SWITCHPLAN (SUCC rc0), o FINALPOSTREPORTS roda
CHECKSYNC→CREATEPOSTREPORTS→UPDATESTATS, e o plano de D+1 é ativado com o próximo
FINAL 23:59 já agendado (HOLD) — corrente auto-sustentável.

**ResetPlan**: sem `-scratch` preserva o preproduction plan (se o plano antigo estiver
viciado, o rebuild gera production vazio "0 streams"); `-scratch` zera produção E
preprodução → rebuild limpo do zero.

**Restart do domínio (evidência postgres-disabled-after-container-restart)**: o unit
`postgresql-18` é DISABLED — após `docker stop/start` o postgres não volta sozinho e o
engine entra em loop de `5432 refused` (AWSJDB802E). Ordem correta: (1) `systemctl start
postgresql-18`; (2) `systemctl start tebctl-tws_cpa_agent_wauser` (agente ITA); (3)
`startAppServer.sh` (engineServer); (4) `conman "start&link @!/@/@;noask"` + `startmon`
(batchman). O engine Java só pega o timezone novo no boot (stopAppServer.sh → trocar
localtime → startAppServer.sh).

## Exploração: jobs complexos com dependências e abend (2026-09-05)

Definições estilo Sfinal (keyword por linha, sem `/`) adicionadas via `composer add`; jobs
podem ser inline no SCHEDULE (como o Sfinal) — a forma com `$JOBS` + separador `/` falhou
com AWSJOM918E.

**Submit**: `sbj` é para JOB individual; para um job stream/schedule use `sbs` —
`conman "sbs = WS#STREAM;noask"` (com `=`; `sbj` em stream dá AWSBHU072E). O erro
AWSBHU711E (job name not supplied) ocorre ao emitir `rr` sem o nome do job.

**Comportamento coletado (evidências)**: numa cadeia A→B→C com ramo A→D→E, o job B
(`exit 5`) foi ABEND rc5 e parou o C (HOLD, dependência quebrada) mas os ramos paralelos
D/E executaram SUCC — dependências FOLLOWS independentes não bloqueiam paralelismo. Stream
fica STUCK enquanto há ABEND. Rerun manual do job ABEND (`conman "rr = WS#STREAM.JOB;noask"`)
re-executa e re-falha se o comando ainda falha. Confirmar/cancelar o ABEND libera os jobs
dependentes. **RECOVERY RERUN** num job que falha (rc1) dispara rerun automático de
recuperação (`>>rerun as ... [Recovery]`) que também ABEND. Jobs executam nativamente no
master MDM (via seu JobManager) — diferente do WSL onde dynamic agent ficava READY.

**Limpeza**: objetos de teste deletados via `composer delete` (Sfinal/FINAL preservado).

## Composer: matriz de sintaxe de entrada (2026-09-05) — esclarece claim 0104

Experimento controlado (6 variações, todas no container) para determinar a sintaxe de
arquivo aceita por `composer add` — investigação da aparente contradição com o claim
WSL `composer-syntax-format-0104` (que documentava `$JOBS` + separador `/`):

| # | Formato testado | Resultado |
|---|---|---|
| 1 | `$JOBS` + `JOB / DOCOMMAND "..." / STREAMLOGON ...` (com `/`) | **AWSJOM918E** syntax error line 2 |
| 2 | linha solta com `/` (sem `$JOBS`) | AWSBCZ021E (keyword esperada) |
| 3 | linha única sem `/` (sem `$JOBS`) | AWSBCZ021E |
| 4 | `$JOBS` + multilinha: `JOBNAME` na linha 1, keyword por linha | **FUNCIONA** (`AWSJCL003I`) |
| 5 | `$JOBS` + linha única `JOBNAME DOCOMMAND "..." STREAMLOGON ...` | **FUNCIONA** |
| 6 | `SCHEDULE` com jobs inline (keyword por linha, estilo Sfinal) | **FUNCIONA** (8 objetos) |

**Conclusão**: o separador `/` documentado no claim 0104 era o **formato de serialização
do `composer display`/extract** (como o composer *mostra* blocos), NÃO a sintaxe de
entrada. A sintaxe real de entrada aceita é: `$JOBS` header + job name numa linha e
keywords em linhas próprias (ou linha única); dentro de SCHEDULE os jobs inline seguem o
formato nativo do Sfinal (keyword por linha, sem `/`). O `/` como separador na entrada
dispara AWSJOM918E. (A pesquisa Perplexity corroborou: a forma canônica é keyword por
linha ou linha única; `/` não é suportado como separador de bloco.)

**Nota de precisão ao claim 0104**: o claim está correto no que VALIDA (formato nativo
aceito, jobs referenciados devem existir), mas a representação com `/` descrita ali é a
do display — recomendado ajustar a redação do claim para evitar que o `/` seja copiado
como sintaxe de entrada (candidato a revisão).

## Dependência por arquivo OPENS + resolução de hostname (2026-09-05)

**OPENS** (dependência de recurso/arquivo): job com `OPENS /tmp/arquivo` fica HOLD com o
arquivo listado em Dependencies até ele existir. Validado no container: após criar o
arquivo o job executou SUCC rc0.

**Achado crítico de configuração**: o OPENS não liberava mesmo após criar o arquivo, com o
`JobManager_message.log` cheio de `AWSITA081E` (agent can not send resource information a
`https://tws-hwa.lab:31116/JobManagerRESTWeb/JobScheduler/resource`) + `AWSITA366E Could
not resolve hostname`. Causa: o hostname `tws-hwa.lab` (definido na instalação via
`-hostname tws-hwa.lab`) NÃO estava no `/etc/hosts` do container (o hostname real do
container UBI é o ID do docker, ex. `8189d3570cc2`). O conman/composer funcionavam (outro
caminho de resolução), mascarando o problema até o teste de recurso de arquivo. **Fix**:
adicionar `tws-hwa.lab` → loopback no `/etc/hosts` (é o que o jobman usa para POSTar o
estado do recurso ao engine REST na 31116). Depois disso o OPENS passou a funcionar.
Evidência `opens-file-dep-hostname-0001`.

## Boot automático (2026-09-05) — evidência boot-auto-container-mdm

Três units garantem o domínio de pé após `docker restart` (validadas com restart real):
`tws-boot-fixes` (hosts + conserta unit tebctl) → `tebctl-tws_cpa_agent_wauser`
(agent+JobManager) → `tws-domain-start` (postgres + engine + start&link + startmon).
Achado: unit tebctl original com `User=wauser`+`Type=forking`+`PIDFile=` falha porque o
status.info é gravado como wauser e o systemd recusa PID file não-root — remover
`User=`/`PIDFile=` resolve (o script tebctl já faz `su - wauser`). Backup da unit em
`/etc/systemd/system/*.bak-*`; scripts em `/usr/local/sbin/{fix-tws-hosts,fix-tebctl-unit-boot,tws-domain-start}.sh`.

## Event rules (EDWA) — fluxo E2E validado no container (2026-09-06)

**Arquitetura**: enEventDrivenWorkloadAutomation (ed)=YES; event processor no engineServer
(Liberty); monman/ssmagent para alguns providers; 3 rules default (UPDATEFAILURE etc.).
Event rules = objetos XML via composer (`add <file>`, `validate <file>;syntax`), validados
contra EventRules.xsd. XML sem atributo encoding (senão AWSBIA358E).

**Fluxo validado (evidência edwa-event-rule-e2e-container)**: rule `LAB_EVT_SBS`
(ruleType=filter, GenericEventPlugIn `Event1`, filtros Param1=TRIGGER_LAB + Workstation=MDM,
ação TWSAction `sbs`) → composer add (AWSJCL003I, status *activation pending*) → ativou
sozinha em ~5min (deploymentFrequency=5) → `sendevent Event1 GenericEventPlugIn
Param1=TRIGGER_LAB Workstation=MDM` (AWSGTW113I) → ação sbs submeteu o job stream alvo →
EVTJOB1 executou SUCC rc0.

**Sintaxe do XML da event rule (erros AWSVAL descobertos)**:
- Ação TWSAction `sbs` exige **2 parâmetros**: `JobStreamName` (nome do stream) +
  `JobStreamWorkstationName` (workstation). `JobStream` não é válido (AWSVAL005E);
  JobStreamWorkstationName é obrigatório (AWSVAL006E).
- `eventType` deve ser um dos definidos no GenericEventPlugIn (config em
  `/opt/hwa/TWSDATA/eventPlugIn/config/GenericEventPlugIn/TWSPluginConfiguration.xml`):
  `Event1` (params Param1+Workstation) ou `Upgrade` (Message+Workstation+UpgradeStatus).
  Nome arbitrário → AWSVAL011E.
- `Workstation` do Event1 **não aceita wildcard** (wildcardAllowed=false) → AWSVAL021E.
- Ativação imediata via REST `PUT /twsd/eventrule/deployment/rule_builder/start` retorna
  HTTP 401 no container (exige autenticação) → usar a ativação automática (deploymentFrequency).

**Eventos custom**: definir no GenericEventPlugIn via `evtdef loaddef <file>` / `dumpdef`
(config XML em eventDefinitions.xsd).

## Backup/restore do MDM — validado (2026-09-07)

Evidência `hwa-lab-10.2.8-mdm-backup-restore-0001`. Preenchia lacuna: no corpus o backup
de master data era só claim de doc (hwa-10.2.8-backup-backup-master-data-0001).

**Master data files do MDM** (o que faz backup):
- Banco PostgreSQL (DBs `TWS` ~17MB e `TDWC`), acessado via `runuser -l postgres` (socket local).
- Master data file `Symphony` em `/opt/hwa/TWSDATA/Symphony` (~55KB, plano serializado).

**Procedimento validado (backup)**:
- `runuser -l postgres -c "pg_dump -Fc TWS -f /data/bkp_tws_<ts>.dump"` (444KB) e TDWC (350KB).
- `cp -a /opt/hwa/TWSDATA/Symphony /data/bkp_symphony_<ts>`.

**Prova de RESTAURABILIDADE (reversível, sem tocar produção)**:
1. `createdb TWS_BKPTEST` (clone)
2. `pg_restore -d TWS_BKPTEST /data/bkp_tws_<ts>.dump` → rc=0, sem erros
3. Validação: clone idêntico ao original — 137/137 tabelas; 2 job streams de modelo
   (`mdl.ajs_abstract_job_streams`); 30 instâncias de job stream (`mdl.jsi_job_stream_instances`).
4. `dropdb TWS_BKPTEST` (reversibilidade).

**Nota**: `pg_dump -Fc` (custom) + restore num clone é a forma segura de validar um backup
no lab — prova íntegro e restaurável sem risco ao ambiente de produção.

## REST API V2 (engine 31116) — auth validada + mecanismo da senha (2026-09-07)

Evidência `hwa-lab-10.2.8-rest-api-v2-auth-0001`. Cobre o maior gap de valor: claims de
REST V2 existiam como doc; agora validadas no container com dados reais do plano.

**Endpoints validados** (GETs, basic auth usuário TWS):
- `GET /twsd/api/v2/engine/info` → 200 `{licenseType:PERSERVER, timezone America/Sao_Paulo}`
- `GET /twsd/api/v2/plan/job/count` → 200 `{"count":13}` (jobs do plano do dia vigente)
- `GET /twsd/api/v2/plan/jobstream?limit=5` → 200 envelope `{count,results}` (UUIDs,
  workstation `/MDM`, schedTime UTC + timeZone America/Sao_Paulo, carriedForward)
- Spec OpenAPI em `/twsd/WA_API3_v2.json`: 212 paths (`plan/job`, `plan/jobstream`,
  `plan/job/*/action/*`, `model/*`, `engine/*`)
- `POST /twsd/api/v2/login` → 401 (usar basic auth direto nos recursos, como o WSL)

**DESCOBERTA CRÍTICA — mecanismo de autenticação da senha (aviso do dono confirmado)**:
O engine valida a senha do usuário contra o campo **interno `user.twsuser.password`**
(encriptado `{aes}`), NÃO só contra a senha do SO. Trocar só `chpasswd` mantém a REST em
401. Para redefinir a senha de forma a valer na REST:
1. Reencriptar a nova senha com a MESMA chave do servidor:
   `/opt/liberty/wlp/bin/securityUtility encode --encoding=aes --key=<wlp.password.encryption.key> <nova>`
   (chave em passphrase_variables.xml → `wlp.password.encryption.key`, 10 dígitos).
2. Atualizar `user.twsuser.password` nos `wauser_variables.xml` do engineServer
   (`/opt/hwa/TWSDATA/usr/servers/engineServer/configDropins/overrides/`) E do dwcServer
   (`/opt/hwa/DWC/DWC_DATA/...`). O `securityUtility` imprime warnings JVM no stdout antes
   do `{aes}` — filtrar a linha que começa com `{aes}`.
3. Reiniciar o engineServer: `stopAppServer.sh`/`startAppServer.sh` (AWSBHU622I stop issued).
4. Basic auth passa a funcionar.
- Credenciais de lab consolidadas em `sdb/hermes/docker/tws-hwa/data/CREDENCIAIS-LAB.env`
  (chmod 600, FORA do repo git público — não commitar).

## REST API V2 — Gerenciamento de Modelo, Submissão Ad-Hoc e Ações de Ciclo de Vida (2026-09-07)

Evidência `hwa-lab-10.2.8-rest-api-v2-lifecycle-actions-0001`. Validação completa do ciclo operacional via REST V2 no container:

1. **Modelo de Objetos**:
   - `GET /twsd/api/v2/model/jobdefinition` e `GET /twsd/api/v2/model/jobstream`: retornam as definições do banco (MDM), contendo o objeto de tarefa `task.other` (`taskString`, `userName`, `isCommand: true`).

2. **Submissão Ad-Hoc de Jobs no Plano**:
   - `POST /twsd/api/v2/plan/job/submit-ad-hoc-job`
   - Payload: `SubmitAdHocJobOptionsV2` com `workstationKey: "/MDM"`, `jobName`, e bloco `task.other`.
   - Comportamento: job é instanciado na stream default `#JOBS` em estado `HOLD` com id retornado `{"id": "MDM;JOBS;<NAME>"}`.

3. **Ações de Plano (Interação Dinâmica)**:
   - **Update Priority**: `PUT /twsd/api/v2/plan/job/{job_id}/action/update-priority?priority=50` → HTTP 200 (reflete como `+10` no conman sj).
   - **Release**: `PUT /twsd/api/v2/plan/job/{job_id}/action/release` → HTTP 200 (sai de HOLD e transita para EXEC e SUCC).
   - **Job Log**: `GET /twsd/api/v2/plan/job/run/{run_id}/joblog` → HTTP 200 (traz a saída completa do `jobmanrc` e `JOBINFO` com timestamp, tempos de CPU e Exit Status).
   - **Rerun**: `PUT /twsd/api/v2/plan/job/run/{run_id}/action/rerun` → HTTP 200 (exige header `Content-Type: application/json` com corpo `{}`; sem o header retorna HTTP 415). Gera a entrada `>>rerun step` no plano.

4. **Comandos de Componente / Engine**:
   - `PUT /twsd/api/v2/engine/run-component-command`: retorna payload estruturado; para comandos de executor/componente, restrito a workstations do tipo `AGENT` (`AWSJCS027E` se executado contra o MDM do tipo MANAGER).

## Padronização Operacional — Usuário Único (`wauser`) para Todo o Ecossistema (2026-09-08)

Evidência `hwa-lab-10.2.8-single-user-wauser-unification-0001`.

**Regra Padrão do Ambiente**:
Por diretriz operacional, não se pulverizam contas no SO para cada serviço. Todos os serviços e componentes do HWA no host/container pertencem e rodam sob o usuário do produto:
- **Usuário SO**: `wauser` (UID 1000)
- **TWS Engine / Agente**: `wauser`
- **Liberty engineServer (31116)**: `wauser`
- **Liberty dwcServer (9443)**: `wauser`
- **Mesma senha para todos os serviços TWS/Liberty**.
- **Apenas o SGBD** (PostgreSQL / DB2) mantém usuário e credencial dedicados (`postgres`).

**Ajuste realizado no DWC para eliminar o usuário separado (`dwcadmin`)**:
1. Ownership: `chown -R wauser:wauser /opt/hwa/DWC`
2. Configuração de ambiente do script: em `/opt/hwa/DWC/appservertools/setEnv.sh`, definido `WA_USER=wauser`.
3. Variáveis do Liberty: em `/opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/configDropins/overrides/wauser_variables.xml`, definido `user.twsuser.id` como `wauser`, com a mesma chave `{aes}` de senha do engine.
4. Execução: `su - wauser -c 'cd /opt/hwa/DWC/appservertools && ./startAppServer.sh -direct'` inicia o `dwcServer` como `wauser` na porta 9443.
5. Remoção: conta `dwcadmin` deletada do sistema operacional (`userdel`).

## Dynamic Pools e Resolução de Variáveis (VARTABLE) no Container (2026-09-08)

Evidências `hwa-lab-10.2.8-dynamic-pool-workstation-e2e-0001` e `hwa-lab-10.2.8-vartable-resolution-and-missing-behavior-0001`.

### 1. Workstations do Tipo POOL (Dynamic Workstations)
- **Regra de Gramática do Composer**: Na cláusula `FOR MAESTRO HOST <host>`, o host fornecido deve ser obrigatoriamente do tipo `BROKER` (ex: `MDM_DWB`). Tentar vincular a um `MANAGER` (`MDM`) resulta no erro `AWSJCO049E`.
- **Sintaxe Validada**:
  ```text
  CPUNAME LABPOOL
    DESCRIPTION "Dynamic pool de teste sob broker MDM_DWB"
    OS OTHER
    FOR MAESTRO HOST MDM_DWB
      TYPE POOL
    MEMBERS
      MDMDA
  END
  ```
- **Comportamento do Scheduler**: Jobs agendados na estação virtual `LABPOOL` são despachados dinamicamente para os agentes membros (`MDMDA`), marcando `{MDMDA}` na saída do `conman sj`. O limite da CPU deve ser liberado (`conman lc LABPOOL;10;noask`).

### 2. Tabelas de Variáveis (`VARTABLE`) e Substituição Caret (`^VAR^`)
- **Definição no Composer**: Declarada como objeto standalone:
  ```text
  VARTABLE LAB_VAR_TBL
    DESCRIPTION "Tabela de variaveis do lab"
    MEMBERS
      LAB_MSG "MSG_VAL_CONTAINER_RHEL9"
      LAB_PORT "9090"
  END
  ```
- **Ordem Obrigatória no Job Stream**: A diretiva `VARTABLE <nome>` deve vir obrigatoriamente **antes** de `ON RUNCYCLE`. Colocar após causa `AWSJOM915E`.
- **Substituição Caret**: Em jobs nativos (UNIX/WINDOWS), variáveis são referenciadas como `^VARNAME^` e expandidas no JCL pelo `jobmanrc` no momento da submissão.
- **Comportamento com Variável Ausente**: Se um job referenciar uma variável que não existe na VARTABLE vinculada (ex: `^VAR_INEXISTENTE^`), o HWA **não** bloqueia o agendamento nem gera erro de sintaxe; a string literal com os circunflexos é passada intacta para o comando de execução.

## EDWA: TWSObjectsMonitor (JobStatusChanged) e Sincronização a Quente (`planman resync`) (2026-09-08)

Evidências `hwa-lab-10.2.8-edwa-twsobjectmonitor-jobstatuschanged-0001` e `hwa-lab-10.2.8-planman-resync-hot-recovery-0001`.

### 1. TWSObjectsMonitor e Ação MessageLogger (MSGLOG)
- **Evento JobStatusChanged**: Requer atributos `JobName`, `Workstation` e `Status`. O valor de `Status` deve ser capitalizado (`Successful`, `Abend`, `Error`), pois usar mnemônicos como `SUCC` é rejeitado pelo validador.
- **Parâmetros da Ação MSGLOG**:
  - `Message`: Texto da notificação.
  - `ObjectKey`: **Obrigatório**. A omissão gera o erro `AWSVAL006E`.
  - `Severity`: Aceita `Info`, `Warning` ou `Error`. Informar `Information` causa erro `AWSVAL018E`.

### 2. Recuperação de Plano a Quente via `planman resync`
- **Comportamento Operacional**:
  1. O comando encaminha a requisição concorrentemente ao `batchman` e ao `engineServer` (`AWSBEH119I`).
  2. Inicia o dump transacional do arquivo `Symphony` para a base relacional (`AWSJCL070I`).
  3. Notifica a conclusão com `AWSJCL074I Symphony file successfully loaded in Database`.
- **Vantagem**: Permite restaurar a integridade entre o estado em memória do plano e o banco sem derrubar ou reiniciar o motor de produção.

## Pipeline SFT, Benchmark RAG Híbrido, CI Quality Gate e Watchdog (2026-09-08)

### 1. Pipeline de Instruction-Tuning e Function Calling (SFT)
- **Gerador**: `scripts/build_sft_dataset.py`.
- **Conteúdo Gerado**:
  - `data/sft/sft_chat_full.jsonl`: 50 exemplos ChatML bilíngues (PT-BR / EN) com prompts de sistema para engenharia de HWA e tópicos de troubleshooting de erros `AWS*`.
  - `data/sft/sft_function_calling.jsonl`: 10 exemplos estruturados de function-calling cobrindo schemas da REST API V2 (`hwa_rest_submit_adhoc_job`, `hwa_rest_job_action`, `hwa_rest_get_joblog`) e `hwa_cli_conman`.
  - **Splits Estratificados**: 80% treino (`train.jsonl`, 48 itens), 10% validação (`val.jsonl`, 6 itens) e 10% teste (`test.jsonl`, 6 itens).

### 2. Benchmark RAG Híbrido Expandido (35 Perguntas)
- **Dataset de Avaliação**: `data/eval/golden_qa_benchmark.jsonl` expandido para 35 pares cobrindo todo o ciclo operacional, incidentes, sintaxe de composer, EDWA, REST V2, pools e vartables.
- **Harness de Avaliação**: `data/eval/evaluate_rag_benchmark.py` indexa 1.833 documentos (claims canônicas, evidências de lab e seções funcionais dos runbooks fatiados).
- **Expansão Semântica**: Mecanismo de BM25 com boost técnico ponderado e mapa de sinônimos operacionais do produto.

### 3. CI Quality Gate e Watchdog Operacional
- **Quality Gate**: `scripts/ci_dataset_gate.py` integrado ao `publish.sh`, validando integridade de JSONL, scan anti-vazamento de credenciais e execução do benchmark de retrieval antes de qualquer commit.
- **Watchdog do Container**: `scripts/watchdog_tws_container.sh` monitora a saúde em tempo real (estado do container, porta 31116 do Liberty, processo `Batchman LIVES` e end time do plano de produção), emitindo relatório em JSON (`HEALTHY`).

## Operador CLI (`tws-op`) e Watchdog com Alertas por E-mail (2026-09-08)

### 1. Ferramenta de Operação do Agente (`tws-op`)
- Instalada em `/usr/local/bin/tws-op` no host CachyOS.
- Comandos suportados:
  - `tws-op status`: Exibe o estado do `conman` (Batchman) e da REST API V2 (`engine/info`).
  - `tws-op sj [filtro]`: Consulta jobs no plano (ex.: `tws-op sj @#FINAL.@`).
  - `tws-op submit-adhoc <nome> <cmd>`: Submete job ad-hoc na stream `#JOBS` via REST.
  - `tws-op action <job_id> <release|hold|cancel|rerun>`: Executa ação de ciclo de vida no plano via REST.
  - `tws-op joblog <run_id>`: Recupera a saída completa de execução (`jobmanrc` + `JOBINFO`).
  - `tws-op resync`: Executa o `planman resync` a quente.

### 2. Monitoramento Contínuo e Alerta por E-mail
- **Script**: `scripts/notify_watchdog_email.py`.
- **Destinatário**: `adrianolimagarcia@gmail.com`.
- **Remetente**: `twstest@haos.fyi` via SMTP SSL (`mail.haos.fyi:465`).
- **Agendamento**: Unit `tws-watchdog.service` com timer `tws-watchdog.timer` no systemd do host, executando checagens de saúde a cada 30 minutos.
- **Disparo**: Em caso de falha (queda do container, perda da porta 31116, Batchman inativo ou estagnação do plano), um e-mail de alerta detalhado é transmitido imediatamente.

## Catálogo de Opções Globais (`optman`) e Dicionário de Erros `AWS*` (2026-09-08)

### 1. Dicionário de Mensagens Canônicas do HWA (`data/evidence/aws_messages_dictionary.jsonl`)
- **Extração**: 335 códigos e mensagens `AWS*` extraídos dos catálogos compilados (`.cat`) e arquivos `.properties` do HWA 10.2.8.
- **Componentes Mapeados**:
  - `AWSBEH*`: Falhas de autenticação e comunicação SSL do conman/planman (ex.: `AWSBEH021E`, `AWSBEH029E`).
  - `AWSJDB*`: Erros de persistência relacional do engineServer (ex.: `AWSJDB802E` connection refused no PostgreSQL).
  - `AWSVAL*`: Erros de validação semântica de regras EDWA e objetos de modelo (ex.: `AWSVAL006E` ObjectKey obrigatório, `AWSVAL018E` Severity inválido, `AWSVAL021E` wildcard não permitido).
  - `AWSJCO*`: Restrições topológicas de agendamento (ex.: `AWSJCO049E` host de POOL exige BROKER).
  - `AWSJOM*`: Análise léxica e gramática do composer (ex.: `AWSJOM918E` barra de saída na entrada, `AWSJOM915E` ordem de VARTABLE).

### 2. Catálogo de Opções Globais do `optman` (`data/evidence/optman_global_options_catalog.jsonl`)
- **Extração**: 92 opções globais ativas extraídas via `optman ls` no container de produção.
- **Parâmetros Críticos Confirmados no Lab**:
  - `startOfDay / sd = 0005`: Ancoragem do modelo de produção diária às 00:05.
  - `enCarryForward / cf = ALL`: Transporte automático de jobs não concluídos para o dia seguinte.
  - `enEventDrivenWorkloadAutomation / ed = YES`: Ativação do motor de regras EDWA no Liberty.
  - `deploymentFrequency / df = 5`: Janela de sincronização automática de event rules (5 minutos).
  - `enAutomaticFailover / af = YES`: Failover automático habilitado para Master de backup.
  - `enRoleBasedSecurityFileCreation / rs = YES`: Geração de arquivos de segurança baseada em papéis.

## Trilha 3 — Restrições de escopo para EDWA/FileMonitor e failover (2026-09-08)

Estado factual do lab container (tws-hwa.lab, plano #22) registrado em
`lab-validation-2026-09-08-trilha3-edwa-failover-scope-constraints.jsonl`:

1. **Failover/switchmgr (hwa-10.2.8-ha-switchmgr-0001): NÃO é empiricamente validável
   nesta topologia** — existe apenas UM Master Domain Manager (MDM *UNIX MASTER) mais
   agentes (MDMDA UNIX AGENT, MDMXA X-AGENT, broker MDM_DWB, pools LABPOOL/MASTERAGENTS).
   Sem um BMDM/FTA full-status e banco espelhado não há segundo engine para `conman
   switchmgr`. Manter tais claims como `official_primary` (não promovê-las a
   `lab_validated`). Pré-requisito: provisionar BMDM.

2. **EDWA/evtdef (RESOLVIDO 2026-09-13):** o CLI evtdef e desbloqueado usando a porta
   **31116** (ITDWBServerSecurePort do CLIConfig), onde `evtdef dumpdef` retorna
   `AWSBEH123I` + o XML completo das definicoes de evento. A porta 31131 (ef=31131) NAO tem
   listener (Connection refused), daí o AWSBEH023E/029E — NAO era problema de truststore; a
   truststore de cliente existente (TWSClientTrustStore.p12) ja funciona com 31116.
   Evidencia: `lab-validation-2026-09-13-evtdef-tls-port-resolution.jsonl`.

Trilhas de lab futuras (fora do escopo deste boot): (a) provisionar BMDM p/ failover;
(b) habilitar truststore de cliente do evtdef e validar E2E FileMonitor FileCreated→MSGLOG.

## BMDM em container proprio (tws-bmdm) — failover MDM<->BMDM validado (2026-09-09)

Setup completo registrado em `lab-validation-2026-09-09-bmdm-container-failover-setup.jsonl`.

### Arquitetura
- MDM: container `tws-hwa` (172.18.0.10 na rede docker `hwa-mesh`), PostgreSQL local 172.18.0.10:5432/TWS.
- BMDM: container `tws-bmdm` (172.18.0.11, RHEL 9.8 UBI-init, 4G/6G, privileged, mounts sdb
  `hermes/docker/tws-bmdm/{data,ssl-certs}` + installers do tws-hwa).
- Rede: `docker network create --driver bridge --subnet 172.18.0.0/24 hwa-mesh`; tws-hwa foi
  conectado com `--ip 172.18.0.10` e o BMDM criado direto com `--ip 172.18.0.11`.

### Liberacao do banco para a rede (feito no MDM)
1. `sed -i "s/^#*listen_addresses.*/listen_addresses = '*'"'"'/ " postgresql.conf`
2. pg_hba.conf += `host all all 172.18.0.0/24 scram-sha-256` (+ 172.17.0.0/16)
3. `systemctl restart postgresql-18` (listen_addresses exige restart, nao reload)
4. `ALTER USER postgres PASSWORD '<dedicada>'` (registrada em CREDENCIAIS-LAB.env, fora do git)
5. Validar: `nc -w3 172.18.0.10 5432` a partir da rede hwa-mesh; engine MDM segue Batchman LIVES.

### Instalacao BKM (container tws-bmdm)
1. Pacotes: `dnf install -y --allowerasing unzip tar gzip openssl procps-ng passwd sudo hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless`
2. `useradd -m -s /bin/bash wauser` + chpasswd (mesma senha do ecossistema)
3. `sysctl -w kernel.hostname=tws-bmdm.lab`; /etc/hosts += `172.18.0.10 tws-hwa.lab` e `127.0.0.1 tws-bmdm.lab`
4. Extrair kit MDM (`/installers/HWA_10.2.8_MDM_LINUX_X86_64.zip` -> /tmp/kit) e openliberty.zip em /opt/liberty (atencao: zip cria /opt/liberty/wlp/wlp — mover conteudo p/ /opt/liberty/wlp)
5. PEM SSL: reutilizar a CA lab (ca.crt/tls.key/tls.crt do /opt/ssl-certs do tws-hwa) — montado em /opt/ssl-certs:ro
6. `serverinst.sh -f serverinst-bmdm.properties`: ACCEPTLICENSE=yes, INST_DIR=/opt/hwa/TWS,
   THISCPU=MDM_BK, DISPLAYNAME=MDM_BKA, XANAME=MDM_BKXA, COMPONENT_TYPE=MDM,
   RDBMS_TYPE=POSTGRESQL, DB_HOST_NAME=172.18.0.10, DB_PORT=5432, DB_NAME=TWS,
   DB_USER=postgres, WA_USER=wauser, WLP_INSTALL_DIR=/opt/liberty/wlp,
   SSL_KEY_FOLDER=/opt/ssl-certs, START_SERVER=true.
   → WAINST054I Configuring BKM (detectou master existente) + WAINST023I success rc=0.
   Binarios em /opt/hwa/TWS/TWS (UNISONHOME), dados em /opt/hwa/TWS/TWSDATA.
7. Corrigir `~wauser/.bash_profile` para source de `/opt/hwa/TWS/TWS/tws_env.sh`.

### Pos-instalacao (doc awspicfgbkmdm + awspiinstallMDMasBKM)
1. Copiar chaves AES: `cp /opt/hwa/TWSDATA/ssl/aes/key.p12 key.sth` do MDM para o BMDM (mesmo caminho).
2. `JnextPlan -for 0000` no MDM -> cria run novo e inclui MDM_BK no plano (workstation ja veio
   TYPE FTA / AUTOLINK ON / FULLSTATUS ON criada pelo BKM install; NODE tws-bmdm.lab TCPADDR 31111).
3. Limites: `conman "limit MDM_BK#;10"` e `conman "limit MDM_BKA#;10"` (o # evita AWSBHU048E
   ambiguous selector porque MDM_BK e prefixo de MDM_BKA).
4. Symphony chega ao BMDM automaticamente (52.768 bytes em /opt/hwa/TWS/TWSDATA/Symphony).

### Failover testado (ida e volta)
- `conman "switchmgr MASTERDM;MDM_BK"` -> AWSBHU120I changed MDM->MDM_BK; novo master mostra
  MDM_BK *UNIX MASTER Batchman LIVES e o MDM vira UNIX FTA (doc: old manager vira FTA).
- `conman "switchmgr MASTERDM;MDM"` (do BMDM) -> volta; estado final: MDM *UNIX MASTER, MDM_BK UNIX FTA.

### Pitfalls
- listen_addresses so muda com RESTART do postgres (pg_reload_conf nao basta).
- Nomes com prefixo comum (MDM_BK vs MDM_BKA): usar sufixo `#` no limit p/ evitar AWSBHU048E.
- Openliberty.zip gera diretorio duplo (wlp/wlp) — mover antes do serverinst.
- BMDM compartilha o MESMO banco (nao roda configureDb proprio nem cria schemas).

### Boot automatico do BMDM validado (restart real, 2026-09-09)
- `docker restart tws-bmdm` -> units em cascata (tws-hosts-fix -> tebctl -> tws-domain-start)
  restauram o BMDM sozinho como FTA full-status (evidencia ...-0005).
- **Pitfall**: bind mount `/data` (sdb) vem como root:root apos restart; o `su - wauser` falha
  ao gravar `/data/appserver-start.log` (Permission denied) e o engine nao sobe. Fix:
  `chown wauser:wauser /data` + linha defensiva no topo do `/usr/local/sbin/tws-domain-start.sh`.
