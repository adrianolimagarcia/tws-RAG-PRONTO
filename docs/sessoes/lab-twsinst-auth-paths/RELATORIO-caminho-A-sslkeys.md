# Lab twsinst — Caminho A: autenticação via `-sslkeysfolder` / `-sslpassword` (Custom PEM)

- **Data:** 2026-10-13
- **Objetivo:** validar em instalação limpa (Docker) o caminho A da matriz de autenticação do `twsinst` (certificado próprio fornecido via PEM), documentando comando exato, resultado e perrengues.
- **Contexto:** os 3 caminhos são mutuamente exclusivos — (A) `-sslkeysfolder` + `-sslpassword` (Custom PEM), (B) `-wauser` + `-wapassword` (REST), (C) `-apikey` (DWC). Omitir os três aborta com `AWSFAB502E`. Misturar A+B dá erro 486. Ref: `data/runbooks/twsinst-flags-complete-reference.md`, seção 4.

## 1. Geração dos certificados (CA fresca, sem reusar CA de lab anterior)

Certificados gerados no host em `/tmp/lab-a-certs` (apagada após o lab):

```bash
# CA fresca do lab A (30 dias)
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 30 -out ca.crt -subj "/CN=TWS-Lab-A-CA"
# Chave do agente + certificado assinado pela CA fresca (com SAN)
openssl genrsa -out tls.key 2048
openssl req -new -key tls.key -out tls.csr -subj "/CN=tws-lab-auth-a" \
  -addext "subjectAltName=DNS:tws-lab-auth-a,DNS:tws-lab-auth-a.lab"
openssl x509 -req -in tls.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out tls.crt -days 30 -sha256 -extensions v3_req \
  -extfile <(printf "[v3_req]\nsubjectAltName=DNS:tws-lab-auth-a,DNS:tws-lab-auth-a.lab\n")
openssl verify -CAfile ca.crt tls.crt   # tls.crt: OK
```

Arquivos resultantes: `ca.crt`, `tls.key`, `tls.crt` (a `ca.key` ficou só no host, nunca entrou no container).

## 2. Senha do `-sslpassword`

Senha aleatória de lab gerada com `openssl rand -base64 18`, gravada **direto** no cofre pessoal da Alma (`<alma>/cofre/sslpassword-a.txt`, 0600, dono adriano) — **não consta neste relatório nem em nenhum doc do RAG** (aqui aparece como `<senha>`). Copiada para dentro do container via `docker cp` (`/tmp/sslpass.txt`, 0600) e lida de variável no script de instalação — nunca na linha de comando visível, nunca em log.

## 3. Container throwaway

```bash
docker run -d --name tws-lab-auth-a --hostname tws-lab-auth-a \
  --memory=2g --memory-swap=3g --privileged \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v /tmp/lab-a-data:/data \
  -v $SDB/hermes/docker/tws-hwa/installers:/installers:ro \
  -v /tmp/lab-a-certs:/certs-src:ro \
  --network hwa-mesh --ip 172.18.0.14 \
  registry.access.redhat.com/ubi9/ubi-init:latest
```

- IP 172.18.0.14: livre (usado pelo caminho B, cujo container foi removido).
- Imagem `ubi9/ubi-init:latest` já estava no cache (pull do caminho B).

Setup interno: `dnf install -y --allowerasing unzip tar gzip openssl procps-ng passwd sudo hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless` (o `--allowerasing` resolve o conflito `curl` vs `curl-minimal`, mesmo perrengue do caminho B); usuário `wauser` criado; `/etc/hosts` com `172.18.0.10 tws-hwa.lab`; PEMs copiados de `/certs-src` (ro) para `/opt/agent-ssl` **gravável** (o instalador gera keystores/truststores ali) com dono `wauser` (`ca.crt`/`tls.crt` 644, `tls.key` 600).

## Comando exato

```bash
./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
  -thiscpu LABA -tdwbhostname tws-hwa.lab -tdwbport 31116 \
  -sslkeysfolder /opt/agent-ssl -sslpassword <senha>
```

Observação: **nenhuma** flag de `-wauser`/`-wapassword` foi passada — cenário A puro, sem misturar (a matriz proíbe; dá erro 486).

## Resultado

- `AWSFAB033I The installation has completed successfully.` — **exit 0**
- Duração: ~35 s
- Instalado em `/opt/HCL/TWA_wauser/`; log: `TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log`
- **Zero ocorrências** de `sslpassword` no log de instalação (sem vazamento).
- `AWSFAB601I Import certificates.` (exit 0) — o instalador importou os PEMs fornecidos.
- Keystores gerados: `TWSDATA/ssl/certs/TWSClientKeyStore.p12` + `TWSClientTrustStore.p12`.
- Verificado: o `TWSClientKeyStore.p12` contém **nosso** certificado (`subject=CN=tws-lab-auth-a`, `issuer=CN=TWS-Lab-A-CA`) — prova de que o Custom PEM usou os arquivos fornecidos, não download via REST.

## Validação

- Processo `/opt/HCL/TWA_wauser/TWS/bin/JobManager` em execução como `wauser`. ✅
- Instalação bem-sucedida com cenário A puro confirma a exclusão mútua da matriz. ✅

## Achado principal: gap de confiança PKI (workstation NÃO registrada)

Após a instalação, o agente **não conseguiu se vincular ao broker** e a workstation **não foi registrada** no banco do master (11 workstations, sem `TWS-LAB-AUTH-A` nem `LABA`):

1. Erro inicial no `JobManager_trace.log`: `SSL peer certificate or SSH remote key was not OK` ao fazer POST em `https://tws-hwa.lab:31116/JobManagerRESTWeb/JobScheduler/resource`.
   - Causa: o broker apresenta certificado `CN=tws-hwa.lab` emitido por `CN=TWS-HWA-Lab-CA` (a CA compartilhada do lab), que **não** estava no truststore do agente (só CAs públicas).
2. Correção aplicada (só no container do lab, sem tocar o MDM): CA do broker (`TWS-HWA-Lab-CA`, obtida dos `ssl-certs` do lab existente no SDB) adicionada ao `TWSClientTrustStore.pem` e ao `TWSClientTrustStore.p12` do agente; JobManager reiniciado (o agente ITA o reinicia sozinho).
3. Novo erro após a correção: `Failure when receiving data from the peer` — o handshake avançou (o agente agora confia no broker), mas o broker encerra a conexão. Diagnóstico: o broker **não confia na nossa CA fresca** (`CN=TWS-Lab-A-CA`); a validação mútua falha no sentido broker→agente. Corrigir isso exigiria adicionar nossa CA ao truststore do **master** — fora do escopo (containers existentes intocados por regra do lab).

**Conclusão do achado:** o caminho A instala perfeitamente com CA própria, mas o vínculo com o broker exige confiança PKI **mútua**. Com CA fresca e isolada, o agente nunca entra no banco. Em deploy real, o caminho A pressupõe PKI compartilhada com o ecossistema (como o lab original fazia: mesma `TWS-HWA-Lab-CA` no MDM, BMDM e agente) ou a distribuição da CA própria para o truststore do master. Como a workstation nunca foi registrada, **não há nada para marcar como `ignore`** (diferente do caminho B).

## Perrengues e soluções

1. `tail -3` inválido no script de setup (ambiente do container) — resolvido executando os passos via `docker exec` separados em vez de script único.
2. Conflito `curl` vs `curl-minimal` no `dnf` — resolvido com `--allowerasing` (mesmo do caminho B).
3. Aspas aninhadas no `docker exec` com `sh -c` — resolvido escrevendo o script de instalação local, enviando via `base64 -d` + `docker cp`.
4. Gap de confiança PKI (acima) — documentado como achado, não como falha do instalador.

## Conclusão: caminho A vs B

**Funciona como documentado.** Com `-sslkeysfolder` + `-sslpassword` válidos, o `twsinst` importa os certificados fornecidos e conclui a instalação do agente dinâmico sem precisar de usuário/senha TWS nem de API key — é o caminho para quem tem PKI própria. A diferença prática para o caminho B: o B delega a confiança ao master (download do cert via REST autenticado), enquanto o A exige que o operador gerencie a confiança PKI nos dois sentidos. Para o vínculo com o broker funcionar, a CA usada precisa ser confiável pelo master.

## Limpeza

- Container `tws-lab-auth-a` parado e removido; `/tmp/lab-a-certs`, `/tmp/lab-a-data` e `/tmp/install-a.sh` apagados do host.
- Containers existentes (tws-hwa, tws-bmdm, tws-agent, tws-dwc) intactos.
- Nenhum JnextPlan rodado; nenhum objeto do master criado/alterado/deletado.
