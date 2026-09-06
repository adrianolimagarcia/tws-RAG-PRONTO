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
