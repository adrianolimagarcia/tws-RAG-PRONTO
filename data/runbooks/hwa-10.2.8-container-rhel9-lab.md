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
