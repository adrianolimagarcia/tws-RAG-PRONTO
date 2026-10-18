# Extended Agents (XA) — conceito, configuração, ciclo de vida e troubleshooting

> Guia de enriquecimento do dataset tws-RAG-PRONTO. Registrado em 2026-10-18.
> Base: documentação oficial HCL Workload Automation (help.hcl-software.com / help.hcltechsw.com).
> Lacuna que este guia preenche: o corpus não tinha **nenhuma** ocorrência de "extended agent"
> nem "access method" — ver `PLANO_ENRIQUECIMENTO_DATASET.md`.

---

## 1. Conceito

Um **extended agent (XA)** é uma **workstation lógica** — uma definição no banco de dados do TWS,
sem nenhum processo/agente instalado nela — usada para estender o processamento de jobs a
sistemas e aplicações externas (SAP R/3, PeopleSoft, z/OS, Oracle Applications, métodos
customizados, unixssh/unixrsh).

Pontos-chave:

- O XA **é hospedado por uma workstation física**: pode ser o master domain manager, um
  domain manager ou um agent (FTA). **Nunca outro extended agent.**
- XAs são definidos na **root folder** do banco de dados; não podem ser definidos em outra pasta.
- Uma workstation física pode hospedar **no máximo 255 extended agents**; vários XAs podem
  compartilhar o mesmo access method.
- A comunicação com o sistema externo acontece através de um **access method**: um programa
  que **é executado pela workstation hospedeira sempre que o HCL Workload Automation
  submete um job ao sistema externo**. Ou seja: o método roda **sob demanda, por job** —
  não existe um "processo do XA" permanentemente no ar.
- Jobs num XA são definidos como em qualquer outra workstation, exceto que os atributos do
  job são ditados pelo sistema externo. O retorno da execução chega via **stdlist do job**,
  que fica armazenada **na workstation hospedeira** (não no XA).

## 2. Como configurar um extended agent (passo a passo)

### 2.1 Pré-requisitos

- A workstation hospedeira (FTA, master ou domain manager) instalada e linkada.
- O arquivo do access method presente no diretório `methods` da instalação do host:
  `<TWA_DATA_DIR>/methods` (UNIX) ou `<TWA_home>\methods` (Windows), com permissão de
  **leitura + execução** para o usuário de logon dos jobs (ou o logon definido no
  options file do método).
- Para SAP: as **SAP RFC libraries** instaladas antes (System Requirements Document da HCL).

### 2.2 Definir a workstation no composer

Sintaxe oficial (User's Guide and Reference, "Workstation definition"):

```
cpuname [folder/]workstation [description "description"]
os os-type
[node hostname] [tcpaddr port]
[domain domainname]
[for maestro [host [folder/]workstation [access method]]]
[type fta | s-agent | x-agent | manager | broker | agent | rem-eng | pool | d-pool]
[autolink on | off]
[behindfirewall on | off]
[fullstatus on | off]
...
```

Atributos para `TYPE X-AGENT`:

| Atributo | Valor para XA |
|---|---|
| `os` | `OTHER` |
| `node` | hostname/IP do sistema; usar **`NULL`** quando o host é `$MASTER`, ou para PeopleSoft, SAP e Oracle |
| `tcpaddr` | conforme o access method |
| `for maestro host` | a workstation hospedeira (`$MASTER`, `$MANAGER` ou o nome da FTA) |
| `access` | o **nome do arquivo do access method** (ex.: `r3batch`) |
| `type` | `x-agent` |
| `domain` | necessário apenas se host = `$MANAGER` |
| `autolink` | `OFF` |
| `behindfirewall` | `OFF` |
| `timezone`/`tz` | o fuso da workstation hospedeira |

### 2.3 Exemplo completo — XA para SAP (r3batch)

```
CPUNAME SAP_XA
   DESCRIPTION "SAP R/3 via r3batch"
   OS OTHER
   NODE none TCPADDR 31111
   FOR MAESTRO HOST FTA_SAP01 ACCESS "r3batch"
   TYPE X-AGENT
   AUTOLINK OFF
   BEHINDFIREWALL OFF
   FULLSTATUS OFF
END
```

Notas:

- `FOR MAESTRO HOST FTA_SAP01 ACCESS "r3batch"` = host físico + método entre aspas.
- Se a definição do XA estiver sem host ou sem access method, o composer retorna
  **AWSBIA140E** — "For an extended agent you must specify the host and the access method."
- Se o nome do método não existir no sistema, o composer avisa **AWSBIA145W** —
  "Access method !1 does not exist on your system!".
- Para alterar o access method num Symphony já gerado: rodar `JnextPlan -for 0000`.

### 2.4 Options files (exemplo SAP)

O `r3batch` usa arquivos de opções para conectar e lançar jobs na instância SAP:

| Arquivo | Escopo |
|---|---|
| `r3batch.opts` | global — vale para todas as instâncias `r3batch` |
| `<XA_Unique_ID>_r3batch.opts` | local — só para aquela XA (ex.: `S4HANAR3BW_r3batch.opts`); se existir, **ignora** o duplicado no global |

Opções principais: `ljuser` (usuário que lança/gerencia jobs), `ifuser` (usuário que lê
informações do job), `TWSXA_LANG` / `twsmeth_lang` / `twsmeth_cp` / `twsxa_cp` (idioma e
code pages — obrigatório alinhar em ambientes sem Unicode), `max_name_counter` /
`name_counter_policy` (variantes SAP), `rcmap` / `enable_appl_rc` (mapeamento de return
codes), `retrieve_joblog` / `retrieve_spoollist` / `retrieve_ipaklog` / `retrieve_pchainlog`,
`pchain_recover` (`rerun` | `restart`), `job_interceptable`.

**Importante:** se modificar os options files do `r3batch`, é preciso **parar e reiniciar os
processos de monitoramento do extended agent** (`r3evmon stop` / `r3evmon start`) para a
mudança valer. No UNIX, esse comando deve ser executado pelo **dono da instalação** do
HCL Workload Automation.

### 2.5 Definir e rodar jobs

- SAP jobs precisam estar definidos no HCL para serem executados sob seu controle; os jobs
  no SAP podem ser definidos com ferramentas SAP padrão ou via Dynamic Workload Console.
- Tipos referenciáveis: Standard R/3, BW Process Chains, BW InfoPackages.
- **InfoPackages:** no SAP, scheduling options com Start type = "Start later in background
  process" e Start time = "Immediate".
- **Process chains:** scheduling options = "Start Using Meta Chain or API" (se estiver em
  "Direct Scheduling", a chain dispara sozinha no SAP, fora do controle do HCL).
- Mapeamento de status HCL ↔ SAP: INTRO = Not Available; WAIT = Ready/Release;
  EXEC = Active; SUCC = Finished; ABEND = Canceled.

## 3. Ciclo de vida e operações — o ponto que mais confunde

### 3.1 O XA **não** aceita `conman start`

A referência oficial do `conman start` diz que, no início de cada período de produção, o
comando "causes the autolinked fault-tolerant agents and standard agents to be initialized
and started automatically" — **FTAs e standard agents, apenas**. O XA não tem processos
locais para iniciar: ele é lógico. **Basta dar start na FTA hospedeira**; o access method
é invocado sob demanda a cada job submetido ao XA.

### 3.2 Link/unlink

- "Extended agents are not linked; they communicate through a host." (referência do
  `conman link`) — o link/unlink se aplica à workstation hospedeira, não ao XA.
- O atributo `autolink` é **"Not applicable"** para o tipo extended agent.

### 3.3 Como ver o status do XA

O XA aparece no `conman showcpus` como tipo **X-AGENT**, com a coluna METHOD mostrando o
nome do access method (só para XAs). Flags de estado relevantes:

| Flag | Significado |
|---|---|
| `L` | link primário aberto (linked) |
| `H` | workstation linkada **através do host** |
| `X` | workstation linkada **como extended agent** |
| `I` / `J` | jobman do **host** completou inicialização / está rodando |
| `M` | monman rodando |

Exemplo de saída: `XA_FTA4 360 OTHR X-AGENT 10 0 03/05/2023 1348 L I J M DOMAIN1`.
Visto **do host**, o estado do XA é `LXI JX`; de qualquer outro lugar, `LHI JH`.
As flags `I`/`J` refletem os processos do **host** — o XA não tem processos próprios,
consistente com o modelo sob demanda.

### 3.4 Monitoramento de eventos SAP (r3evmon)

Para event rules baseadas em eventos SAP (requer **XBP 3.0+**), o monitoramento é feito
pelos processos `r3evmon` do XA: `r3evmon start` inicia o monitoramento de eventos SAP,
`r3evmon stop` para. Arquivos de controle por XA em
`<TWA_DATA_DIR>/methods/r3evmon_cfg/` (`XAname_r3evmon.cfg`, `XAname_r3idocmon.cfg`,
`XAname_r3xalmon.cfg`, ...); o usuário TWS precisa de leitura+escrita neles.

## 4. SAP r3batch em detalhe

- **Como o job é lançado:** o `r3batch` recebe as informações SAP-específicas do job,
  **faz uma cópia de um template job no SAP e o marca como "scheduled"**, depois monitora
  o job até a conclusão, escrevendo progresso e status no **stdlist na workstation host**.
- **Múltiplas instâncias SAP:** várias XAs podem usar o mesmo host, cada uma com seu
  options file local (`XA_Unique_ID_r3batch.opts`) apontando para uma instância SAP
  diferente — o unique identifier da XA é a chave.
- **BC-XBP 2.0:** habilita intercept jobs, track child jobs, keep all job attributes on
  rerun, raise events. Parent-child: um job SAP pode gerar subjobs dinamicamente; com a
  feature ativa (ABAP `INITXBP2`), o job HCL só termina quando parent **e** children
  terminarem (`EXEC` enquanto qualquer um roda; `SUCC`/`ABEND` conforme o conjunto).
- **BC-XBP 3.0:** monitoramento de eventos SAP (eventos do sistema, ex.: novo operation
  mode; e eventos de usuário, disparados por ABAP/processos externos). Critérios de
  interceptação configurados em perfis no DWC (Administration > Workload Design > Manage
  SAP Criteria Profiles); no 2.0, via table criteria no Monitor Workload.
- **Job throttling:** usa XBP 2.0/3.0 (interception + parent-child) para não sobrecarregar
  o SAP; não pode rodar junto com job interception.
- **Certificações:** HCL Workload Automation é certificado para SAP NetWeaver e SAP S/4HANA.

## 5. Troubleshooting

### 5.1 Jobs não lançam no XA

Causas documentadas ("Failure launching jobs on extended agents and dynamic agents"):

1. Access method **fora do diretório correto** no host do XA.
2. Método **não acessível** pelo HCL Workload Automation.
3. O usuário de logon dos jobs (ou o logon do options file do método) **sem permissão de
   leitura + execução** no método.
4. Checagens de dependência `opens` rodam como **root**, a menos que outro login seja
   especificado no options file do método.

### 5.2 Jobs parados / XA sem fluxo

- O XA só lança jobs **sob direção da workstation hospedeira**: se a FTA host estiver
  down ou unlinkada, nada flui para o XA.
- Com link down, mensagens ficam enfileiradas em `<TWA_home>/TWS/pobox/<workstation>.msg`
  até o link voltar.
- Para diagnosticar: ler o **stdlist do job** (`conman sj` ou console) — o erro do método
  (ex.: `EEWO0439E The required options are not specified either in the global or in the
  local options file`) aparece lá, no host.

### 5.3 Problemas conhecidos do SAP (r3batch / r3evmon)

- **Eventos IDoc duplicados** (`IDOCEventGenerated` repetido): resetar data/hora do próximo
  loop em `<data_dir>/methods/r3evmon_cfg/XAname_r3idocmon.cfg` — parar o `r3evmon`,
  apagar o arquivo (ou ajustar `start_date=YYYYMMDD` / `start_time=HHMMSS`) e reiniciar.
  Checar `idoc_no_history`: `OFF` sem arquivo = recupera **todos** os IDocs coincidentes,
  não só os atuais; `ON` (default) usa a data/hora do arquivo.
- **Nenhum evento gerado no monitoramento IDoc:** checar `idoc_no_history` e a data/hora
  no `XAname_r3idocmon.cfg`.
- **EEWO0778E** (dependência internetwork em evento SAP com XBP 2.0): verificar se o
  report **BTCTEST** existe no SAP (transações `sa38`/`se38`, buscar `BTC*`); se não
  existir, apontar `placeholder_abap_step` no options file local para outro report dummy
  existente (com XBP 2.0 o HCL cria um placeholder job por evento SAP).

### 5.4 Misconfigurações comuns

| Erro | Sintoma |
|---|---|
| HOST ou ACCESS ausentes na definição | composer **AWSBIA140E** |
| Nome do método ≠ arquivo em `methods/` | composer **AWSBIA145W**; em runtime, jobs falham ao lançar |
| Permissões do método / options files | jobs falham; `r3evmon` sem acesso aos cfgs |
| TCPADDR/porta errada na definição | host não linka (verificar netman/porta única por instância) |

## 6. Fontes (documentação oficial HCL)

- Workstation definition (sintaxe + atributos X-AGENT):
  https://help.hcl-software.com/workloadautomation/v1022/distr/src_ref/awsrgwsdefn.html
- Defining access methods for agents:
  https://help.hcl-software.com/workloadautomation/v1024/distr/src_ad/awsadextagent.html
- conman start (referência):
  https://help.hcl-software.com/workloadautomation/v101/distr/src_ref/awsrgstart.html
  (também: https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrgstart.html)
- conman link (referência — "Extended agents are not linked; they communicate through a host"):
  https://help.hcl-software.com/workloadautomation/v102/distr/src_ref/awsrglink.html
- Managing production for extended agents (stdlist no host):
  https://help.hcl-software.com/workloadautomation/v1022/distr/src_ad/awsadextagentsprod.html
- Failure launching jobs on extended agents and dynamic agents:
  https://help.hcl-software.com/workloadautomation/v102/distr/src_ad/awsadlaunchfailonextag.html
- HCL Workload Automation for SAP (visão geral + scheduling process):
  https://help.hcl-software.com/workloadautomation/v101/distr/src_tsweb/General_Help/sap_c.html
- SAP R/3 batch access method:
  https://help.hcl-software.com/workloadautomation/v1023/apps/src_usr/awsausapaccessmethod.html
- r3batch access method configuration (options files):
  https://help.hcl-software.com/workloadautomation/v1025/apps/src_usr/awsausapr3accmethconf.html
- Scheduling process for the agent workstation hosting r3batch:
  https://help.hcl-software.com/workloadautomation/v1026/apps/src_usr/awsausapschedpr.html
- Common options (r3batch):
  https://help.hcl-software.com/workloadautomation/v95/apps/src_usr/awsausapcomopts.html
- Monitoring SAP events (r3evmon start/stop):
  https://help.hcl-software.com/workloadautomation/v1023/apps/src_usr/awsaumonsapevts.html
- Other known problems (IDoc, EEWO0778E):
  https://help.hcl-software.com/workloadautomation/v1024/apps/src_usr/awsautshotherprobl.html
- showcpus (referência — XA como X-AGENT):
  https://help.hcl-software.com/workloadautomation/v1024/distr/src_ref/awsrgshowcpus.html
- Standard format (flags de estado L/H/X/I/J/M, coluna METHOD):
  https://help.hcl-software.com/workloadautomation/v1023/distr/src_ref/awsrgstdformat.html

