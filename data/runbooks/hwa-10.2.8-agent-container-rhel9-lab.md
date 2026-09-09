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
   O broker cria a workstation no banco — **nome = TWS-AGENT** (base), NÃO o `-thiscpu`.
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

## Evidências

- `data/evidence/lab-validation-2026-09-09-agent-docker-container.jsonl`:
  hwa-lab-10.2.8-agent-docker-install-0001, -registered-plan-0002, -job-executed-0003.

## Pitfalls (todos observados no lab)

- Kit AGENT ≠ kit MDM: só `twsinst` (sem `serverinst.sh`).
- Nome de workstation do broker é `TWS-AGENT` (prefixo do produto), não o `-thiscpu`.
- Workstation dinâmica só entra no plano via JnextPlan/ResetPlan (não em tempo real).
- `AWSJPL006E` na virada: node sem FQDN resolvível → adicionar alias `.lab` no /etc/hosts do MDM.
- Job stream name máx. 16 chars (`AWSJOM012E`); job referenciado sem definição inline → `AWSJDB303E`.
- `-sslkeysfolder` deve ser gravável (instalador gera keystores; mount `:ro` falha).
- Limit default 0 pós-entrada no plano → `conman "limit <WS>#;10"` (o `#` evita AWSBHU048E
  quando o nome é prefixo de outro, ex.: MDM_BK vs MDM_BKA).
