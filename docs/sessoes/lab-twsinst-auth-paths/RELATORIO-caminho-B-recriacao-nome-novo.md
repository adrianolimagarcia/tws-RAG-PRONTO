# Lab twsinst — Caminho B recriado do zero com NOME NOVO + refresh do plano

- **Data:** 2026-10-13 (~21:52–22:10 UTC)
- **Objetivo:** revalidar de ponta a ponta o caminho B (`-wauser`/`-wapassword`) com workstation de nome novo, incluindo o refresh leve do plano (`JnextPlan -for 0000 -noremove`) e um job de teste executado na nova workstation.
- **Contexto:** a workstation anterior do lab (TWS-LAB-AUTH-B) está no DB com `ignore=on` (mantida assim — inofensiva, não bloqueia a nova). Por decisão do usuário, o lab foi refeito do zero com nome diferente em vez de reutilizar o anterior.
- **Senha:** usada transientemente do cofre da Alma (`<alma>/cofre/wauser.txt`); **não consta neste relatório** (aparece como `<senha>`).

## Ambiente

| Item | Valor |
|---|---|
| Container | `tws-lab-auth-c` (throwaway, removido após o lab) |
| Hostname do container | `tws-lab-auth-c` (igual ao nome da workstation, de propósito) |
| Imagem | `registry.access.redhat.com/ubi9/ubi-init:latest` (já estava no cache local) |
| Rede | `hwa-mesh` — IP `172.18.0.14` |
| Recursos | `--memory=2g --memory-swap=3g --privileged`, cgroup rw |
| Mídia | `HWA_10.2.8_LNX_X86_64_AGENT.zip` (669 MB), extraída em `/tmp/kit` |
| Master alvo | `tws-hwa.lab` (172.18.0.10), porta TDWB `31116` |
| Pré-requisitos | mesmos do lab anterior (dnf --allowerasing p/ conflito curl/curl-minimal; pacotes unzip tar gzip openssl procps-ng passwd sudo hostname which curl diffutils libxcrypt-compat java-21-openjdk-headless; usuário `wauser`; `/etc/hosts` com `tws-hwa.lab`) |

## Desvios do plano original (documentados)

1. **`-thishost` NÃO é flag válida do twsinst.** Verificado via `twsinst -u`: só existe `-thiscpu` ("HCL Workload Automation workstation name; if the host name starts with a number, -thiscpu must be specified"). A flag foi omitida do comando — o hostname do container (`tws-lab-auth-c`) já cumpre o papel de identificar o host.
2. **A senha aparece em PLAINTEXT no log de instalação (4 ocorrências).** O `twsinst` registra `tdwb_pwd=<senha>` 1x na linha de comando java do instalador e 3x em linhas `INFO: key tdwb_pwd value <senha>` em `TWSDATA/installation/logs/twsinst_LINUX_X86_64_wauser_10.2.8.00.log`. O parâmetro `-wapassword` continua mascarado (`****`), mas o `tdwb_pwd` (mesma credencial, usada p/ o download REST) não é. **Isso corrige a afirmação de "zero vazamento" do relatório do caminho B anterior** — a checagem anterior só cobriu o `-wapassword`. Como o container é throwaway e foi removido, o log foi destruído junto; não reutilizar logs de instalação sem redigir.
3. **Workstation auto-criada vem com LIMIT 0 no plano.** Após o JnextPlan, `conman showcpus` mostrava `TWS-LAB-AUTH-C` com `LIMIT 0` — jobs submetidos ficavam em `READY` eternamente. Correção: `conman "limit cpu=TWS-LAB-AUTH-C;10"` (sintaxe `limit <nome>;<n>` dá "ambiguous selector"; usar `limit cpu=<nome>;<n>`). Após o ajuste, o job despachou imediatamente.

## Comando exato

```bash
./twsinst -new -agent dynamic -acceptlicense yes -uname wauser \
  -thiscpu TWS-LAB-AUTH-C \
  -tdwbhostname tws-hwa.lab -tdwbport 31116 \
  -wauser wauser -wapassword <senha>
```

Cenário B puro: nenhuma flag de certificado.

## Resultado da instalação

- `AWSFAB033I The installation has completed successfully.` — **exit 0**
- Duração: **38 s**
- Instalado em `/opt/HCL/TWA_wauser/`; `JobManager` em execução no container. ✅
- Arquivo de senha temporário (`/tmp/.wp`) removido com `shred -u` após o uso. ✅

## Registro no master

`composer "display cpu=@"` (nota: nesta build do composer, `; noask` quebra o comando — usar sem):

```
TWS-LAB-AUTH-C    agent    -                          10/13/2026  -
CPUNAME TWS-LAB-AUTH-C
  DESCRIPTION "This workstation was automatically created."
  OS UNIX
  NODE tws-lab-auth-c SECUREADDR 31114
  FOR MAESTRO HOST MDM_DWB
    AGENTID "0F9840E79311307ABDE81505FA762DA9"
    TYPE AGENT
```

O broker registrou exatamente o nome passado em `-thiscpu` (= hostname do container). TWS-LAB-AUTH-B segue com `Ignored=Y`.

## Refresh do plano

```bash
JnextPlan -for 0000 -noremove   # como wauser, no MDM
```

- **Exit 0.** `enCarryForward` já estava em `ALL` (verificado via `optman ls` antes).
- O refresh estendeu o plano em 0h e puxou a definição nova para o Symphony **sem rolar o dia** (plano #102 → #103, mesma data de produção).
- Ressalva observada: `AWSJPL804W` sobre um job stream antigo de 9/9/26 no preproduction plan (warning, não erro); workstations foram paradas/reiniciadas brevemente, como esperado.

## Validação ponta a ponta

1. `conman showcpus` (plano #103): `TWS-LAB-AUTH-C  103  UNIX AGENT ... LBI J  M` — **no plano e linkada** (mesmo estado da MDMDA, agente saudável). ✅
2. Job de teste: definição `TWS-LAB-AUTH-C#TESTECHO` (`DOCOMMAND "/bin/echo hello-lab-c"`, `STREAMLOGON wauser`, `TASKTYPE UNIX`) + job stream `MDM#LABTESTC`, criados via `composer add` de arquivos (notas: `composer add` lê arquivo **dentro do container** — `docker cp` + `chmod 644`; definição de job usa header `$JOBS` e keyword `DOCOMMAND`, não `SCRIPTNAME`/`ARGS`; o job precisa existir antes do stream que o referencia).
3. Submit ad hoc: `conman "sbs MDM#LABTESTC"` → instância criada.
4. Após o ajuste de `limit` (item 3 dos desvios), o job executou: **`(TWS-LAB-AUTH-C#)TESTECHO  SUCC  RC=0  #J308443731`**. ✅

## Limpeza

- Container `tws-lab-auth-c` parado e removido. ✅
- Objetos de teste `jd=TWS-LAB-AUTH-C#TESTECHO` e `js=MDM#LABTESTC` **mantidos no DB** (documentação viva do teste; remover com `composer "delete"` se o usuário preferir).
- TWS-LAB-AUTH-B segue com `ignore=on`.

## Conclusão

**Caminho B revalidado de ponta a ponta com nome novo:** instalação OK, registro automático no master com o nome exato, `JnextPlan -for 0000 -noremove` puxa a workstation para o plano sem rolar o dia, e job de teste executa com sucesso no agente dinâmico. Três aprendizados novos para o runbook: (1) `-thishost` não existe no twsinst; (2) `tdwb_pwd` vaza em plaintext no log de instalação — redigir antes de arquivar; (3) workstation auto-criada nasce com `LIMIT 0` — ajustar via `conman "limit cpu=<nome>;<n>"` antes de testar jobs.

---
*Relatório não commitado — deixado para revisão do usuário. Senha sempre redigida como `<senha>`.*
