# Lab twsinst — Caminho C (JWT via API Key) do zero + refresh do plano

- **Data:** 2026-10-13 (~22:17–22:35 UTC)
- **Objetivo:** validar de ponta a ponta o caminho C de autenticação do twsinst (JWT/API Key em vez de `-wauser`/`-wapassword`), com workstation de nome novo, incluindo o refresh leve do plano (`JnextPlan -for 0000 -noremove`) e um job de teste executado na nova workstation.
- **Contexto:** caminhos A e B já validados (relatórios anteriores neste diretório). Por decisão do usuário, o lab foi feito do zero com nome diferente (`TWS-LAB-AUTH-D`).
- **Senha/JWT:** usados transientemente do cofre da Alma (`<alma>/cofre/wauser.txt`); **não constam neste relatório** (aparecem como `<senha>` / `<JWT>`).

## Ambiente

| Item | Valor |
|---|---|
| Container | `tws-lab-auth-d` (throwaway, removido após o lab) |
| Hostname do container | `tws-lab-auth-d` (igual ao nome da workstation, de propósito) |
| Imagem | `registry.access.redhat.com/ubi9/ubi-init:latest` |
| Rede | `hwa-mesh` — IP `172.18.0.14` |
| Recursos | `--memory=2g --memory-swap=3g --privileged`, cgroup rw |
| Mídia | `HWA_10.2.8_LNX_X86_64_AGENT.zip` (669 MB), copiada já extraída para `/tmp/kit` no container |
| Master alvo | `tws-hwa.lab` (172.18.0.10), porta TDWB `31116` |
| Pré-requisitos | mesmos do caminho B (dnf --allowerasing p/ conflito curl/curl-minimal; pacotes unzip tar gzip openssl procps-ng passwd sudo hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless; usuário `wauser`; `/etc/hosts` com `tws-hwa.lab`) |

## Geração do JWT (API Key)

**Desvio do plano original:** o endpoint do DWC (`https://127.0.0.1:9443/twsd/api/v2/apikey`) exigiu o parâmetro `engines` e, mesmo com ele, retornou `AUTHORIZATION_ERROR` com basic auth. O endpoint equivalente no **engine do MDM** (`https://172.18.0.10:31116/twsd/api/v2/apikey`) funcionou com basic auth (`wauser:<senha>`).

Detalhes do endpoint (descobertos por tentativa):
- Método: `POST`, Content-Type `application/json`, basic auth com usuário/senha do TWS.
- Body: `{"label":"<nome>","type":"PERSONAL"}` — o campo de nome é `label` (outros nomes dão `AWSJOM001E`); `type` é obrigatório e o enum é **maiúsculo**: `PERSONAL` ou `SERVICE` (minúsculas dão `AWSMAC020E`).
- Resposta: `{"token":"<JWT>"}` (JWT RS256, ~1132 bytes).
- Arquivo temporário `/tmp/jwt-c.txt` (0600) destruído com `shred -u` após o uso.

## Flags do twsinst para JWT (verificado via `twsinst -u`)

- `-apikey <apikey>` — "Use esse parâmetro para especificar a APIKey a ser usada para autenticar com o gerenciador de domínios principal. Obtenha a string a ser fornecida com esse parâmetro do Dynamic Workload Console antes de executar o comando."
- Alternativa: `-jwt true` + `-wauser`/`-wapassword` (o instalador baixa o token JWT do broker usando as credenciais). Não usada aqui — o caminho C puro usa só `-apikey`.

## Comando exato

```bash
./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
  -thiscpu TWS-LAB-AUTH-D \
  -tdwbhostname tws-hwa.lab -tdwbport 31116 \
  -apikey <JWT>
```

Cenário C puro: sem `-wauser`/`-wapassword`, sem flags de certificado.

## Resultado da instalação

- `AWSFAB033I The installation has completed successfully.` — **exit 0**
- Duração: **~2,5 min** (161 s — mais lento que o caminho B, 38 s)
- Instalado em `/home/wauser/TWA/`; `JobManager` em execução no container. ✅
- Nota: `AWSFAB239W` ("installing a dynamic agent but you provided some parameters that are not necessary... ignored") — parâmetros supérfluos ignorados; variável interna `JWT =` aparece vazia no log (o token viaja no `APIKEY`).
- Arquivo `/tmp/.jwt` no container removido com `shred -u` após o uso. ✅

## Desvios e achados (documentados)

1. **O JWT vaza em plaintext no log de instalação (1 ocorrência).** O log registra `APIKEY = <JWT>` na seção `checkSSLValuesForAgent` de `TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log`. Mesma classe do achado do caminho B (`tdwb_pwd` em claro). Como o container é throwaway e foi removido, o log foi destruído junto; não reutilizar logs de instalação sem redigir.
2. **Endpoint do DWC vs engine:** `POST /twsd/api/v2/apikey` no DWC (:9443) não autenticou com basic auth neste lab; no engine MDM (:31116) funcionou. (RAG registra validação anterior no DWC em 22/08 — comportamento pode variar por configuração.)
3. **Workstation auto-criada nasce com `LIMIT 0`** (mesmo achado do caminho B). Correção aplicada antes do teste: `conman "limit cpu=TWS-LAB-AUTH-D;10"`.

## Registro no master

```
TWS-LAB-AUTH-D    agent    -                          10/13/2026  -
```

Tipo `agent` (dynamic), OS UNIX, via broker `MDM_DWB`, com AGENTID. Não ignorada. O broker registrou exatamente o `-thiscpu` (= hostname do container).

## Refresh do plano

```bash
JnextPlan -for 0000 -noremove   # como wauser, no MDM
```

- O refresh puxou a definição nova para o Symphony **sem rolar o dia** (plano #103 → **#104**, mesma data de produção).
- Ressalva observada: `AWSJPL804W` sobre job stream antigo de 9/9/26 (warning, não erro — o mesmo do caminho B); workstations paradas/reiniciadas brevemente, como esperado.

## Validação ponta a ponta

1. `conman showcpus` (plano #104): `TWS-LAB-AUTH-D  104  UNIX AGENT ... LBI J  M` — **no plano e linkada**. ✅
2. Job de teste: definição `TWS-LAB-AUTH-D#TESTECHO` (`DOCOMMAND "/bin/echo hello-lab-d"`, `STREAMLOGON wauser`, `TASKTYPE UNIX`) + job stream `MDM#LABTESTD`, criados via `composer add` (job primeiro, depois o stream).
3. Submit ad hoc: `conman "sbs MDM#LABTESTD"` → instância criada.
4. Após o ajuste de `limit` (item 3 dos achados), o job executou: **`(TWS-LAB-AUTH-D#)TESTECHO  SUCC  RC=0  #J308443732`**. ✅

## Limpeza

- Container `tws-lab-auth-d` parado e removido. ✅
- Arquivos temporários do JWT (`/tmp/jwt-c.txt` no host, `/tmp/.jwt` no container) destruídos com `shred -u`. ✅
- Objetos de teste `jd=TWS-LAB-AUTH-D#TESTECHO` e `js=MDM#LABTESTD` **mantidos no DB** (documentação viva do teste; remover com `composer "delete"` se o usuário preferir — notar que o anterior `TWS-LAB-AUTH-C#TESTECHO`/`MDM#LABTESTC` já foi removido nesta sessão).
- Registros de API Key criados durante o lab (`lab-path-c`, `lab-path-c-jwt`): os
  tokens foram destruídos após o uso e, ao final da sessão, **todas as 3 API keys
  de teste foram revogadas** — tabela `mdl.aky_api_keys` zerada no banco do
  engine (verificado). Nada pendente de revogação.

## Conclusão

**Caminho C validado de ponta a ponta:** API key gerada via REST (`POST /twsd/api/v2/apikey` no engine, body `{"label","type":"PERSONAL"}`), instalação com `-apikey` OK (`AWSFAB033I`), registro automático no master com o nome exato, `JnextPlan -for 0000 -noremove` puxa a workstation para o plano sem rolar o dia, e job de teste executa com sucesso no agente. Aprendizados novos para o runbook: (1) formato exato do POST de criação da API key; (2) o JWT vaza em plaintext no log de instalação (`APIKEY = <JWT>`); (3) o endpoint do DWC pode exigir `engines` e não aceitar basic auth — o do engine MDM funcionou.

---

*Relatório não commitado — deixado para revisão do usuário. Senha e JWT sempre redigidos como `<senha>` / `<JWT>`.*
