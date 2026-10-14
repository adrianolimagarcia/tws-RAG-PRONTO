# Lab twsinst — Caminho B: autenticação via `-wauser` / `-wapassword`

- **Data:** 2026-10-13
- **Objetivo:** validar em instalação limpa (Docker) o caminho B da matriz de autenticação do `twsinst` (download do certificado via REST com usuário/senha TWS), documentando comando exato, resultado e perrengues.
- **Contexto:** os 3 caminhos são mutuamente exclusivos — (A) `-sslkeysfolder` + `-sslpassword` (Custom PEM), (B) `-wauser` + `-wapassword` (REST), (C) `-apikey` (DWC). Omitir os três aborta com `AWSFAB502E`. Ref: `data/runbooks/twsinst-flags-complete-reference.md`, seção 4.

## Ambiente

| Item | Valor |
|---|---|
| Container | `tws-lab-auth-b` (throwaway, removido após o lab) |
| Imagem | `registry.access.redhat.com/ubi9/ubi-init:latest` (via `docker pull` — não estava no cache local) |
| Rede | `hwa-mesh` — IP `172.18.0.14` (livre; .10–.13 ocupados por tws-hwa/bmdm/agent/dwc) |
| Recursos | `--memory=2g --memory-swap=3g --privileged`, cgroup rw |
| Mídia | `HWA_10.2.8_LNX_X86_64_AGENT.zip` (669 MB), extraída em `/tmp/kit` |
| Master alvo | `tws-hwa.lab` (172.18.0.10), porta TDWB `31116` |

## Pré-requisitos resolvidos

1. **Senha do `wauser` não documentada** — o RAG redige senhas por política deliberada. Com autorização explícita do Adriano, a senha foi recuperada via `decryptAES` do `wauser_variables.xml` (chave `wlp.password.encryption.key` de `passphrase_variables.xml`), usando as classes do Liberty (`PasswordUtil.passwordDecode` + `AESKeyManager` com `KeyStringResolver` customizado), procedimento documentado no runbook WSL (P29). A senha está guardada no cofre pessoal da Alma (`<alma>/cofre/wauser.txt`, 0600) para reuso nos caminhos A e C — **não consta neste relatório nem em nenhum doc do RAG** (aqui aparece como `<senha>`).
2. **Conflito `curl` vs `curl-minimal`** no ubi9 — resolvido com `dnf install --allowerasing`.
3. Pacotes instalados: unzip tar gzip openssl procps-ng passwd sudo hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless. Usuário `wauser` criado; `/etc/hosts` com `tws-hwa.lab`.

## Comando exato

```bash
./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
  -thiscpu LABB -tdwbhostname tws-hwa.lab -tdwbport 31116 \
  -wauser wauser -wapassword <senha>
```

Observação: **nenhuma** flag de certificado (`-sslkeysfolder`/`-sslpassword`) foi passada — cenário B puro, sem misturar (o runbook antigo do lab misturava os dois; a matriz diz que é mutuamente exclusivo).

## Resultado

- `AWSFAB033I The installation has completed successfully.` — **exit 0**
- Duração: ~40 s (19:30:33 → 19:31:12 UTC)
- Instalado em `/opt/HCL/TWA_wauser/`; log: `TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log`
- O `AgentCertificateDownloader` executou o download do certificado via REST (é o mecanismo do caminho B) — a senha no log aparece mascarada como `wapassword ****` (sem vazamento).

## Validação

- Processo `/opt/HCL/TWA_wauser/TWS/bin/JobManager` em execução no container. ✅
- Instalação bem-sucedida implica que o download do certificado via REST com `-wauser`/`-wapassword` funcionou (falha de auth abortaria a instalação). ✅

## Observações / watch items

- **Nome da workstation no broker:** foi passado `-thiscpu LABB`, mas o runbook do lab observou que o broker pode registrar agentes dinâmicos com o prefixo do produto (`TWS-AGENT`, `TWS-AGENT_1`) em vez do `-thiscpu`. Não foi verificado neste ciclo (exigiria query no banco do MDM) — checar qual workstation foi criada **antes do próximo JnextPlan** para evitar colisão com o `TWS-AGENT` existente (container tws-agent).
- O container `tws-lab-auth-b` foi parado e removido após a validação; logs da instalação preservados neste diretório do RAG.

## Conclusão sobre o caminho B

**Funciona como documentado.** Com usuário/senha TWS válidos, o `twsinst` baixa o certificado do master via REST e conclui a instalação do agente dinâmico sem necessidade de certificados próprios. É o caminho mais simples quando não há PKI própria — dispensa gerar/distribuir `ca.crt`/`tls.key`/`tls.crt`.

## Prontidão para os próximos caminhos

- **Caminho A (Custom PEM):** sem bloqueio de credencial externa — gerar par self-signed fresco com `openssl` (`ca.crt` + `tls.key`/`tls.crt`; **não** reutilizar os da CA do lab para não duplicar identidade no broker); `-sslpassword` é de nossa escolha (o instalador gera o keystore). Container limpo novo.
- **Caminho C (API key DWC):** gerar JWT via `POST /twsd/api/v2/apikey` no DWC autenticado como usuário TWS — usa a mesma senha do cofre; procedimento de referência no runbook WSL (`hwa-10.2.8-wsl-lab.md`, P29).
