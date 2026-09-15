# Runbook — E2E EDWA/EIF: JobStatusChanged -> LAB_STATUS_RULE -> MSGLOG (HWA 10.2.8)

**Produto:** HCL Workload Automation 10.2.8 (Distributed)
**Escopo:** validar a cadeia E2E de eventos EDWA/EIF que dispara uma regra de evento a partir de
uma mudança de status de job, no caminho **AGENDADO** do jobstream.
**Ambiente:** lab com MDM (`tws-hwa`) + backup (`tws-bmdm`); o **event rule engine (ACT)** e o
**listener EIF SSL** rodam no **bmdm**; o **MONMAN** (monitor manager) gera os eventos.

---

## 1. Objetivo

Provar, ponta a ponta, que uma mudança de status de um job do plano (JobStatusChanged) é:
1. **gerada** pelo `TWSObjectsMonitor` (MONMAN) e **entregue** ao listener EIF SSL (porta 31131, no bmdm);
2. **recebida** pelo motor de regras (ACT/EventProcessorManager);
3. avaliada e a regra `LAB_STATUS_RULE` **disparada**;
4. com a ação `MSGLOG` (plug-in `MessageLogger`) executada com sucesso.

Cada etapa tem uma linha de evidência distinta no `messages.log` do engineServer.

---

## 2. Precondições

| Item | Valor esperado | Como conferir |
|---|---|---|
| Regra de evento ativa | `LAB_STATUS_RULE` ACTIVE | `grep AWSJCO125I .../engineServer/logs/messages.log` |
| cfg do monitor presente | `TWSObjectsMonitor.cfg` + `activeRules.txt` | `ls /opt/hwa/TWS/TWSDATA/monconf/` |
| Regra do monitor | `JobStatusChanged JobName=<JOB> Workstation=<POOL> Status=SUCCESSFUL` | `activeRules.txt` |
| Listener EIF SSL | `31131` em LISTEN no **bmdm** | `ss -tlnp \| grep 31131` (no bmdm) |
| Certificado cliente | handshake SSL com `req_client_aut` | trace MONMAN: `certificate_validate(): ... succeded` |
| Jobstream do teste | `LABPOOL#POOL_STREAM` com job `LABPOOL#POOL_JOB` | `composer display jobstream=LABPOOL#POOL_STREAM` |
| TZ do container | **UTC** | `date -u` (o `messages.log` marca GMT real) |

---

## 3. Comandos exatos (observação read-only)

O caminho que **reproduz** o evento é a **ocorrência agendada** do jobstream (runcycle diário),
não a submissão on-demand. Para observar a próxima ocorrência agendada:

```bash
# (a) GERACAO — o monitor enviou o evento?
grep -a "Sending EIF Event" /opt/hwa/TWS/TWSDATA/stdlist/traces/<dia-DE-PRODUCAO>_MONMAN.log

# (b) ENTREGA — handshake SSL completo?
grep -aE "Connected to|Starting SSL handshake|certificate_validate" \
     /opt/hwa/TWS/TWSDATA/stdlist/traces/<dia-DE-PRODUCAO>_MONMAN.log

# (c) RECEPCAO + REGRA + ACAO — no engineServer do bmdm
grep -aE "AWSEVP001I|AWSAHL004I|AWSAHL002I|AWSAHL003I|AWSAHL005I" \
     /opt/hwa/TWS/TWSDATA/stdlist/appserver/engineServer/logs/messages.log
```

Para inspecionar o estado do plano (read-only):

```bash
conman "sj=LABPOOL#POOL_STREAM.@"          # instancias + status dos jobs
```

---

## 4. Evidência esperada (cadeia completa)

No `messages.log` do engineServer (bmdm), em sequência, para a mesma instância:

```
AWSEVP001I  event received: type="JOBSTATUSCHANGED"; provider="TWSObjectsMonitor";
            scope="LABPOOL # POOL_STREAM . (LABPOOL #) POOL_JOB [Successful / SUCC]"
AWSAHL004I  event rule instance "LAB_STATUS_RULE (...)" has been triggered.
AWSAHL002I  action "MSGLOG" for plug-in "MessageLogger" has been started
AWSAHL003I  action "MSGLOG" ... has successfully completed.
AWSAHL005I  event rule instance "LAB_STATUS_RULE (...)" has completed successfully.
```

No trace MONMAN (geração + entrega), antes das linhas acima:

```
Sending EIF Event: "JobStatusChanged;...;EventProvider="TWSObjectsMonitor";...;JobName="POOL_JOB";..."
Connected to [t_] <bmdm>:31131 ... ssl : req_client_aut [2] key_store_format [P12]
certificate_validate(): SSL certificate validation succeded.
```

---

## 5. Limitação conhecida (achado de lab)

- **Instância submetida por operador NÃO gera o evento — nem imediata, nem liberada.**
  - **V1 — imediata** (`sbs LABPOOL#POOL_STREAM`, sem `at`): transiciona na hora
    (HOLD→READY→EXEC em 1–2 s), o job conclui SUCC, mas o trace MONMAN tem **0**
    `Sending EIF Event` e o `messages.log` **não** recebe novo `AWSEVP001I`
    (instâncias 2221 / 2230).
  - **V2 — com `at=`** (`sbs ...;at=2236`): a instância fica **HOLD** e **não executa**.
    A causa do HOLD é o **mecanismo de release**, não o monitor: `sbs <stream>;at=<hhmm>`
    **não auto-libera** a instância (2236 ficou HOLD 16 min sem tentativa de release no TWSMERGE).
  - **Release forçado** (`release =LABPOOL#POOL_STREAM(2251 09/13)`): a instância liberada
    executa e conclui SUCC (TWSMERGE: READY→EXEC→SUCC), mas **também não emite**
    (trace **0**, `AWSEVP001I` inalterado). Instância 2251.
  - **Conclusão:** "instância submetida por operador (imediata **ou** liberada) não emite
    `JobStatusChanged`" está **duplamente suportada**; a hipótese "o monitor reporta apenas a
    ocorrência **planejada** do plano" sobe de hipótese para **suportada**. O cfg do monitor
    não tem filtro de `schedtime`, logo é **seleção do monitor**, não filtro de regra.
- **`LogEvents=NO`** no `monmaneif.conf` → não há log de recepção no listener; a prova de
  recepção é o `AWSEVP001I` do motor de regras.
- **Base de tempo do plano = UTC** (não BR): `at=` é lido em **UTC**; `sj`/batchman apenas
  **renderizam** em BR (container `tws-hwa`) ou UTC (`tws-bmdm`). Prova: `sbs ...;at=1951`
  submetido às 22:48 UTC voltou como `[(1951 09/14/26)]` (roll-forward — 19:51 UTC já passado).
  O `messages.log` marca GMT real.
- **Release de instância HOLD (sintaxe):** `conman "release =<ws>#<js>(<hhmm> <mm/dd>)"`
  (o `=` precede a seleção que contém `#`). Cancelamento: `conman "cs=<ws>#<js>(<hhmm> <mm/dd>);noask"`.

---

## 5b. Mecanismo de seleção do TWSObjectsMonitor

**Status: NÃO ESTABELECIDO.** O que segue é **observação direta**, sem inferir mecanismo.

**OBSERVADO (evidência):**
- Apenas as ocorrências **AGENDADAS** do plano (00:00 UTC, runcycle diário) emitiram EIF:
  `Sending EIF Event` em 12/09 00:00:06 e 13/09 00:00:07, com `AWSEVP001I → AWSAHL004I →
  AWSAHL002I → AWSAHL003I → AWSAHL005I` no `messages.log`.
- Instâncias submetidas por **operador** **não** emitiram — nem **imediata** (`sbs` sem `at`:
  2221/2230) nem **liberada pelo próprio plano** (`release`: 2251, `[Released]`, SUCC).
- Objetos fora da regra também não emitem (ex.: `JS_ALTJOB3` SUCC sem linha EIF).

**NÃO é evidência de mecanismo** (corrigido após verificação independente):
- A **ausência** de `ManageFilter::match` / `Realoading Symphony` numa janela **não** indica
  "o monitor não processou" — o dia de produção 20260911 tem `ManageFilter` = 0 e **mesmo assim**
  emitiu `Sending EIF Event` às 00:00:06 de 12/09. Logo MF/reload **não** são precursores do EIF.
- As rajadas `ManageFilter::match` + `Realoading Symphony` **correlacionam com operações de
  domínio/plano**, não com jobs (probe read-only):
  | rajada (UTC, bmdm) | evento no MDM (BR = UTC-3) |
  |---|---|
  | 09:07:15 / 09:08:27 / 09:10:03 | `AWSBCV116I Switching managers ... MDM_BK→MDM` ×4 (06:07:10 / 06:08:27 / 06:09:57) |
  | 15:19:13 / 15:21:18 | `AWSBCV116I Switching managers ... MDM→MDM_BK` (12:19:13 / 12:21:12) |
  | 20:07:13 | `AWSBDY109I ... MY:JOBMAN-DOWN` + `WRITER-DOWN/UP` (link MDM_BK reconfigurado, 17:07:03) |
  ⇒ MF/reload = **ciclo de reload/transporte do monitor reativo a mudança do Symphony/domínio**,
  não filtro de evento de job.
- O `TWSObjectsMonitor.cfg` é auto-gerado no Event Processor Server e deployado no agente
  (`monconf/`); a regra é `JobStatusChanged JobName=<JOB> Workstation=<POOL> Status=SUCCESSFUL`
  (sem filtro de `schedtime`). Isto **não** explica por que a ocorrência agendada emite e a de
  operador não — o mecanismo permanece **não estabelecido**.

**Discriminador (teste (c), bounded):** a ocorrência **PLANEJADA** `(0005 09/14)` — a mesma que **não
executou** no boundary — foi **liberada fora do plan start** (`release`) e **executou** (`SUCC`,
prova no TWSMERGE) **sem emitir** (trace = 0; `AWSEVP001I`/`AWSAHL004I` = 2/2; nenhum `ManageFilter`/
reload no MONMAN em ~10 min). ⇒ O discriminador **não** é a origem "planejada", é o **PASS DO PLAN
START**: "instância de operador (imediata **ou** liberada) não emite" fica **triplamente** suportada
(2221/2230 imediatas; 2251 liberada; e a própria ocorrência planejada liberada fora do start).
O par "ocorrida planejada emite" (2/2 em 09/12 e 09/13) deve ser lido como **"a ocorrência planejada
DO PASS DO PLAN START emite"**.

**Campos do payload do EIF** (evento positivo, 13/09 00:00:07):
`JobStatusChanged; TimeStamp; EventProvider="TWSObjectsMonitor"; PlanNumber="68"; HostName;
IPAddress; Workstation="LABPOOL"; JobStreamWorkstation="LABPOOL"; JobStreamId="0AAAAAAAAAAAAAHA";
JobStreamName="POOL_STREAM"; JobStreamSchedTime="2026-09-13T00:05:00Z/GMT"; JobName="POOL_JOB";
Priority="10"; **Monitored="false"**; ActualStart; EstimatedDuration; ActualDuration; ReturnCode="0";
Status="Successful"; InternalStatus="SUCC"; Login; EveryFrequency="0"; JobNumber="219408871";
ErrorMessage; END`. O significado de `Monitored="false"` **não** está provado neste lab — não usar
como discriminador sem prova.

## 5c. Pitfalls de sintaxe (conman)

- `conman "sc @;noask"` → **AWSBHU153E** (`noask` só é válido com `getmon`).
- `conman "sj @;noask"` → **AWSBHU039E**.
- **Correto:** `conman "sc @"` / `conman "sj @"` (sem `;noask`).
- Seleção de instância (contém `#`): `=` antes da seleção —
  `conman "release =<ws>#<js>(<hhmm> <mm/dd>)"`, `conman "cs=<ws>#<js>(<hhmm> <mm/dd>);noask"`.

## 5d. Anomalia do limite do dia (mass-READY sem launch) — observação

No boundary de **09/14 00:00:05Z** a passagem de release **readiou 20 streams** (schedtime `0005 09/14`)
e **não lançou nenhum**: zero `AWSBHT036I Attempting to launch`, zero `status to EXEC`, zero SUCC —
em qualquer merge. Contraste de 1 dia, **mesma passagem**: em 09/13 o mesmo `STUCK`
(`MDM#JS_PROMPT_RUN` + `AWSBHT069E`) foi seguido de `AWSBHT036I ... POOL_BALANCING` /
`... POOL_STREAM` → EXEC → SUCC em ~1 s → EIF às 00:00:07.

| dia (schedtime `0005 <dia>`) | READY | launch | SUCC | STUCK |
|---|---|---|---|---|
| 09/12 | 13 | 2 | 2 | 1 |
| 09/13 | 13 | 2 | 2 | 1 |
| **09/14** | **20** | **0** | **0** | 1 |

Candidatos (sem mutar): STUCK acumulado no plano (`JS_PROMPT_RUN` de 09/12 e 09/13 persistem) —
mas o mesmo STUCK em 09/13 não bloqueou; link AGT1 caído (`MY:UNLINK` a cada ~10 min, AGT1 em
**run 35** vs plano **69**) — candidato **fraco** para o `POOL_STREAM`, que em 09/13 rodou no pool
hospedado no MDM; condição do plano (`run 69`/`confirm 69`, sem divergência). **Mecanismo NÃO
ESTABELECIDO** — o bloqueio é do **mecanismo de limite de dia**, não do monitor de objetos.

**Método:** o campo `Plan last update` do `planman` **não** acompanha o dia — **não** serve como
sinal de rollover. O sinal é a troca de stdlist (`AWSDDW100I SWITCHED`), que em 09/14 ocorreu às
**00:08:33Z** (as capturas de B em 00:06:0x–00:06:46Z foram **antes** dessa troca).

**DISCRIMINADOR (desfecho observado às 03:06:18Z): o master NÃO faz o pass do limite de PRODUÇÃO.**
- **Pass da meia-noite LOCAL do MDM** (00:00:0x BR de 14.09) — **funcional**: **21 READY / 16 EXEC /
  15 SUCC** (`POOL_BALANCING`, `AGT1#CROSS_STREAM`, `FRENTE1_STREAM[(0005 09/14)]` → `has completed
  successfully` às 00:00:18). O processamento de plano do master está **vivo**.
- **Pass do limite do dia de PRODUÇÃO do MDM** (21:00:0x BR = 00:00Z) — **ausente**: **0 READY /
  0 EXEC** em 09/14 (controle 09/13 na mesma janela: **13 READY**).
- O BMDM fez **os dois**: produção (20 READY / 0 launch) e local (3 READY às 02:59–03:0x).
⇒ A anomalia é **específica do pass do limite do dia de PRODUÇÃO do master** — e é por isso que o
dia de produção 09/14 só foi readiado no MDM **por ação de operador** (a única `READY 0005 09/14` no
MDM antes do pass local era o `release` do teste (c), às 22:02:51 BR). O desfecho "processamento de
plano do master parado" foi **descartado**.
**Armadilha de método:** a contagem do pass local deve ser **separada por data** (`^00:00:0[0-9]
14\.09\.2026` vs `13\.09\.2026`) — o mesmo arquivo `20260913_TWSMERGE.log` contém as duas meia-noites.

### 5e. Mecanismo do pass do limite de PRODUÇÃO (read-only, parcialmente determinado)

**Cadeia causal identificada:**
1. O pass do limite de produção do master é **disparado por mensagens `dR` vindas do backup
   (MDM_BK)**. Contagem no `traces/20260913_TWSMERGE.log` do MDM: **13** `Received dR: … from cpu
   MDM_BK` nos boundaries **09/12** e **09/13**; **0** em **09/14**. As linhas `AWSBHT075I … status to
   READY` do master são **precedidas** por `Received dR: <pool>#<id> from cpu MDM_BK`. Sem `dR`, o
   master não readia nada.
2. **Em 09/14 o BMDM readiou e parou**: na visão do BMDM a janela do boundary tem **20 READY** e
   depois apenas o `STUCK` — **0** `AWSBHT036I Attempting to launch` e **0** mensagens `Received`
   (controle 09/13: **2** launches e **12** `Received` = `lB`/`jC`/`sJ`/`tJ`). Logo o backup não
   notificou o master → **0 `dR`** → o master não fez o pass.
3. **H1 POSITIVO — ADIAMENTO (~3 h), não ausência**: o pass da meia-noite local do MDM readiou
   **19 objetos** com schedtime `0005 09/14`, dos quais **19 são exatamente os mesmos** do boundary
   de produção do BMDM. A única exceção é **`POOL_STREAM`**, que já havia sido **consumido pelo
   release de operador** (teste (c), SUCC às 01:02Z). Correlato explicado: o BMDM readiou 20 e **não
   lançou nenhum** porque o **launch é do master**, que só processa no seu próprio pass.
4. O pass **local** do MDM é **outro gatilho**: não usa `dR` (0 nas duas janelas 00:00:0x BR) e é
   acionado por **start condition de arquivo** — `checking file lab_trigger.flag on cpu MDM` +
   `Received fC: /tmp/lab_trigger.flag` + `test -f /tmp/lab_trigger.flag` (7× em 14.09; **0** nos
   três boundaries de produção).

**Descartados por evidência:** horizonte do plano (**H2** — `end 09/25 21:04 BR`, folgado);
evento bloqueante no master (**H3** — janela 20:55–21:05 BR de 13.09 só tem o **ruído pré-existente
AGT1**: `AWSBCV082I errno=111` / `AWSBCV035W` / `MY:UNLINK`, zero `AWSDDW100I`, zero `AWSBHT069E`);
link AGT1 (controle negativo); ausência do pass (**H1** — foi **adiado**).

**INCONCLUSIVO (read-only):** **por que** o boundary do BMDM parou após a fase de `READY` em 09/14 —
o `STUCK` de `MDM#JS_PROMPT_RUN` ocorre nos **dois** dias e não bloqueou em 09/13; nenhum outro
evento distingue as duas janelas. Determinar isso exigiria **mutação** (não autorizada nesta frente).

## 5f. Série histórica do pass do boundary de PRODUÇÃO (read-only)

O pass do limite de dia de **produção** do master ocorre às **21:0x BR** (00:00Z) e readia o dia
de produção seguinte. Medido em `traces/` com filtro de data **estrito** (`^(20:5[89]|21:0[0-2]):.*<dd>\.09\.2026`
no MDM; `^00:00:0[0-9] <dd>\.09\.2026` no BMDM):

| arquivo (MDM) | linhas | READY | EXEC | SUCC | AWSBHT036I | Received | dR | PB/PS |
|---|---|---|---|---|---|---|---|---|
| 09/04–09/07 | — | 0–2 | 0–2 | 0–2 | 0–3 | 0–37 | 0 | 0/0 |
| 09/08, 09/09 | 0 | **0** | 0 | 0 | 0 | 0 | 0 | 0/0 |
| 09/10 | 481 | 3 | 2 | 2 | 0 | 94 | 2 | 0/0 |
| **09/11** | 77 | **13** | 2 | 2 | 0 | 25 | **13** | **1/1** |
| **09/12** | 79 | **13** | 2 | 2 | 0 | 26 | **13** | **1/1** |
| **09/13** | 22 | **0** | 0 | 0 | 0 | 1 | **0** | **0/0** |

| arquivo (BMDM, = `<dd−1>`) | linhas | READY | AWSBHT036I | Received | PB/PS |
|---|---|---|---|---|---|
| 09/09, 09/11 | 0 | 0 | 0 | 0 | 0/0 |
| 09/10 | 4 | 4 | 0 | 0 | 0/1 |
| **09/12** | 47 | 13 | **2** | **12** | 1/1 |
| **09/13** | 46 | 13 | **2** | **12** | 1/1 |
| **09/14** | 24 | **20** | **0** | **0** | 1/1 |

**Conclusões.** (1) `0 READY` no master no pass de produção **não é exclusivo de 09/14** — recorre em
09/08, 09/09 e 09/13 (janela vazia, só o ruído AGT1). É comportamento **intermitente** do mecanismo.
(2) No BMDM, o launch só ocorreu em 09/12 e 09/13. (3) A cadeia `dR → READY` explica integralmente o
pass do master: dR = 2/13/13/0 ↔ READY = 3/13/13/0. **Caveat:** 09/04–09/07 têm composição de plano
diferente (sem `POOL_*`, que só aparecem a partir de 09/08) — fora da comparação.

**Pitfalls de leitura (medidos):**
- **Dois `TWSMERGE` por nó, conteúdo DIFERENTE** (`stdlist/traces/` vs `stdlist/logs/`, inodes
  distintos). No MDM (20260912): `traces/` = 79 linhas/`dR=13`; `logs/` = 53 linhas/**`dR=0`**. No
  BMDM (20260912): `traces/` = 46 linhas/`Received=12`; `logs/` = 33 linhas/**`Received=0`**.
  ⇒ Quem medir `dR`/`Received` em `logs/` conclui **falsamente** "o dR nunca chega". **Rotular sempre
  o caminho e usar `traces/`.**
- **Pareamento arquivo↔dia**: os traces do MDM rolam à **00:00 BR**; os do BMDM à **00:04 UTC** — a
  meia-noite UTC do dia D fica no **fim** do arquivo **D−1**. Sem isso, todas as contagens saem 0.
- **Não derivar causa** de `stdlist/JM/JobManager_message.log` (só `AWSITA083I` periódico) nem de
  `<dd>_NETMAN.log` (não escrito no boundary).

## 5g. Série estendida + cruzamento com atividade de operador + origem do `dR`

**Série estendida (read-only, `traces/`).** Inventário: MDM `20260904…20260914` (09/01–09/03
ausentes); BMDM `20260908…20260914`. Mesmas janelas e pareamento do §5f. Números completos na
evidência `hwa-lab-10.2.8-operator-activity-cross-and-dr-origin-0001`.

**Marcador de atividade de operador (calibrado).** Aparece no merge como
`BATCHMAN:#S…/Operator command: <TIPO>` (ex.: `Operator command: SUBMIT SCHED=…POOL_STREAM[(2221 09/13/26),…]`).
Contagem **pré-boundary** (tempo `< 20:55` do próprio arquivo) de `Operator command: SUBMIT`:
MDM `09/04=0, 05=0, 06=1, 07=0, 08=3, 09=8, 10=4, 11=0, 12=1, 13=8`.

**Tabela cruzada** (evento do boundary no arquivo X : MDM READY/dR : BMDM READY/launch/Received : SUBMIT pré):

| arquivo X | MDM READY/dR | BMDM READY/launch/Recvd | SUBMIT pré |
|---|---|---|---|
| 09/04 | 0/0 | — | 0 |
| 09/05 | 2/0 | — | 0 |
| 09/06 | 0/0 | — | 1 |
| 09/07 | 1/0 | — | 0 |
| 09/08 | 0/0 | 0/0/0 | 3 |
| 09/09 | 0/0 | 4/0/0 | 8 |
| 09/10 | 3/2 | 0/0/0 | 4 |
| **09/11** | **13/13** | **13/2/12** | **0** |
| **09/12** | **13/13** | **13/2/12** | **1** |
| 09/13 | 0/0 | 20/0/0 | 8 |

**Veredito:** **correlaciona 6/6** na faixa comparável (09/08–09/13, única com `POOL_*`): os dois
únicos dias com pass **completo** são exatamente os dois com `SUBMIT ≤ 1`, e **todos** os dias com
`SUBMIT ≥ 3` tiveram pass parcial/vazio. **Correlação não é causalidade** — o mecanismo não está
estabelecido e a amostra é de 6 dias. **Limites declarados (sem inferir):** (L1) o marcador só vê o
que o batchman registra como `Operator command:` — `composer`/REST podem não aparecer, logo silêncio
de log **não** prova ausência de atividade; (L2) 09/04–09/07 são incomparáveis (sem `POOL_*`);
(L3) sem registro fora do horário de operação. Os 8 `SUBMIT` do arquivo 09/13 são **os meus testes**
de 13.09 ⇒ a hipótese 3 (efeito-de-operador) fica **suportada por correlação temporal**, com teste
controlado = janela congelada 14.09 18:00Z → 15.09 00:00Z.

**Origem do `dR` (parcial).** O `dR` é a **anunciação de READY entre master e backup**, bidirecional
e **não logada no lado emissor**: no MDM, `Received dR: … from cpu MDM_BK` precede imediatamente
`AWSBHT075I … status to READY` + `AWSBHT054I Resolving a dependency` (13 dR → 13 READY); no BMDM há
`Received dR: MDM#… from cpu MDM` às **03:00:05** (o pass da meia-noite local do master, 7/dia) e
`Received dR: MDMDA#JOBS from cpu MDM` (submits REST/API). **Limite (L4):** nenhum dos merges
registra `Sending dR` ⇒ **o que dispara o envio não é observável por log read-only**; o gatilho do
`dR` permanece **NÃO ESTABELECIDO** e exige mutação (Fase 2, não autorizada até o desfecho de C).

## 5h. Desfecho da captura C (boundary de produção de 09/15) — anomalia repetida com janela limpa

**Janela congelada confirmada limpa:** `Operator command:` no arquivo `20260914_TWSMERGE.log` do MDM em
todo o 14.09 antes do boundary = **0**. O congelamento valeu de 14.09 ~11:20Z até o boundary de 00:00Z
de 15.09 ⇒ o desfecho é um **teste controlado**.

**Desfecho (B) — anomalia REPETIDA.** MDM na janela de produção (20:5x/21:0x BR de 14.09): **0 READY,
0 dR, 0 AWSBHT036I** (contra 13/13/2 nos dias normais). BMDM na janela de 00:00:0x UTC de 15.09:
**20 READY, 0 launch, 0 Received** — repetição exata de 09/14. Interseção (discriminador
calendar-independent): BMDM readiou os pools (1/1), **MDM 0/0**.

**O pass da meia-noite LOCAL do master FUNCIONA** (captura D, 03:01:50Z; controle embutido do método
no pass de 14.09 = 462 linhas / 21 READY / 20 `AWSBHT036I`, exatamente o esperado): alvo de 15.09 =
292 linhas / **21 READY / 12 EXEC / 10 SUCC / 13 AWSBHT036I**, e a instância `#POOL_STREAM 0005 09/15`
chegou a **SUCC às 03:00**. Logo o processamento de plano do master está vivo — **o que falha é
especificamente o boundary de PRODUÇÃO de 00:00Z**.

**Assinatura por dia na janela de produção** (linhas/BATCHMAN/MAILMAN/READY/dR):

| dia | linhas | BATCHMAN | MAILMAN | READY | dR |
|---|---|---|---|---|---|
| 09/11 | 77 | 77 | **0** | 13 | 13 |
| 09/12 | 79 | 79 | **0** | 13 | 13 |
| 09/13 | 22 | 2 | **20** | 0 | 0 |
| 09/14 | 22 | 2 | **20** | 0 | 0 |

Nos dias **normais** a janela é 100% BATCHMAN (o próprio processamento do boundary). Nos **anômalos** o
processamento é substituído por **20 falhas de MAILMAN** no link do AGT1 (`ipc_send_bytes … Connection
refused`, `AWSBCV035W Mailman was unable to link to workstation: AGT1`) e **não há dR nem READY**.

**O que discrimina não é o UNLINK** (ele aparece em 09/12, 09/13 e 09/14) **e sim a falha de relink que
se segue a ele** a partir de 09/13. Diferença de origem: em 09/12 o `UNLINK` vem `from workstation
MDM_BK`; em 09/14 vem `from workstation MDM`. O `sc @` registra **run 69 desde 09/12/26 23:59** —
imediatamente antes do primeiro boundary anômalo (09/13 21:00 BR).

**Conclusões.** (1) **H\*-A (efeito-de-operador) REFUTADA**: a anomalia persistiu por 3 boundaries
consecutivos com **zero** atividade de operador na janela. (2) O estado é **persistente desde 09/13
21:00 BR**, não intermitente, co-localizado com o run 69. (3) Mecanismo candidato: o **relink do AGT1
falha no boundary de produção** e aborta o processamento do dia, enquanto o pass local funciona ⇒
aponta para **H\*-B (estado local do nó/link)**, não para operador nem calendário. O gatilho interno do
relink permanece **não observável por log** (limite L4, §5g).

## 6. Reversão

Procedimento é **read-only** — não há mutação a reverter. Se instâncias de teste ficarem
pendentes no plano (ex.: um `sbs ...;at=` que ficou em HOLD), cancelar a instância específica:

```bash
conman "cs=<ws>#<js>(<hhmm> <mm/dd>);noask"     # cancel sched da instância
conman "sj=<ws>#<js>.@"                          # conferir
```

Se qualquer mutação de config/modelo for necessária, tirar **snapshot docker datado** antes
(`docker commit <container> ha_snap_<YYYYMMDD_HHMM>_<container>`).

---

## 7. Claims / evidências de referência

- `hwa-lab-10.2.8-eif-e2e-generation-vs-delivery-rca-0001` — separação geração vs entrega.
- `hwa-lab-10.2.8-eif-e2e-ondemand-vs-scheduled-addendum-0001` — objetos existentes; on-demand não reproduz.
- `hwa-lab-10.2.8-twsobjectsmonitor-ondemand-not-reported-0001` — discriminante V1/V2 (observação negativa).
- `hwa-lab-10.2.8-eif-listener-31131-active-on-bmdm-correction-0001` — listener EIF no bmdm (correção).

## 5i. Fase 2 autorizada — divergência de DOMAIN MANAGER (modelo × runtime) e o `AWSJPL004E`

> Ordem `[VIGIA-ARQUITETO]`, mutação reversível no lab. Pré-registro, stop criterion e mapa de reversão em
> `docs/lab-protocols/preregistration-2026-09-15-fase2-resync-agt1.jsonl`. Evidência:
> `lab-validation-2026-09-15-root-cause-domain-manager-divergence-awsjpl004e.jsonl`.

**Achado central.** O **modelo** e o **runtime** divergem sobre quem é o domain manager:

- **Modelo** (`composer display domain=@`): `DOMAIN MASTERDM / *MANAGER MDM_BK / ISMASTER` — o banco aponta
  o **backup** como MANAGER do domínio (objeto atualizado em 09/04/2026).
- **Runtime** (`conman "sc @"`): `MDM ... *UNIX MASTER`; o container `tws-hwa` é o MDM e seu `localopts`
  usa `this_cpu = MDM`.

**Prova executável.** A extensão de plano foi **recusada**:

```
AWSJPL004E The workstation is not the master domain manager. The workstation name in the
"this_cpu" option: "MDM" in the localopts file does not match the workstation name of the
master domain manager in the database. The plan can be managed only on the master domain manager.
```

O runbook `hwa-10.2.8-stuck-plan-recovery.md` já prescrevia este caminho: *"Se o erro for `AWSJPL004E`,
o `planman` está sendo executado de um nó cujo `thiscpu` (localopts) não corresponde ao domain manager
gravado no MODELO (objeto DOMAIN no banco). Execute a recuperação a partir do nó que o modelo indica
(com `composer display domain=@`)."*

**Mutações executadas (todas reversíveis, em ordem):**

| # | Comando | Resultado | Efeito |
|---|---|---|---|
| 1 | `tws-op resync` (`planman resync` a quente) | `AWSBEH119I` + `AWSJCL072I`/`AWSJCL074I` *Symphony file successfully loaded in Database*; `BMPlanResync` copiou o Symphony para `Sinfonia.<epoch>` | **Neutro** — direção Symphony→DB; não descartou o AGT1 do plano |
| 2 | `planman unlock` | `AWSJPL504I The "planner" process unlocked the database` + `AWSJCL050I Command "UNLOCK" completed successfully` | **Havia lock órfão** (confirma fluxo interrompido); lock liberado |
| 3 | `planman ext -days 1` | **`AWSJPL004E`** — recusado | Nenhuma troca de Symnew; porém o `Run number` avançou 70 → 71 (o incremento ocorre antes da validação de nó) |

**Estado pós-mutações.** Plano operacional e saudável (`conman "sc @"` responde); `Run number 71` /
`Confirm run number 69`; `Plan last update` inalterado em `09/12/2026 23:59`; `AGT1` presente no plano
(run 35) e ausente do modelo.

**Sintomas que casam com o runbook.** `Run number` disparando (70 → 71) com `Confirm` parado em 69 é
listado como sinal de plano preso; e o `checklist-jnextplan-eol.md` exige `Run number == Confirm run
number` como **pré-condição** de qualquer `JnextPlan` — logo a extensão autorizada está **bloqueada** por
desenho enquanto o pendente existir.

**Conflito de estado — escalado, NÃO corrigido.** A correção exige decisão de papel/domínio (restaurar o
`MANAGER` do modelo para `MDM`, ou operar a partir do nó que o modelo indica). Não executada.

**Reversão disponível.** `Symphony.pre-extensao` e `planbox.msg.pre-extensao` (dentro do container);
snapshot `ha_snap_20260914-0035` (3 imagens, verificado) para restauração total; definições da M-C em
`/tmp/ha_fm/fase2/pre_*.txt`.

**Métrica.** Re-rodada em `(82b03c2, 6910 docs)`: agregados **idênticos** — `@1 53/70 (0,7571)` ·
`@10 68/70 (0,9714)` · `MRR 0,8214`. Apenas o metadado `expected_claims` de 31/70 entradas difere
(resolução de GT dependente do corpus). Baseline intacto.

**Limites declarados.** (i) A divergência **não** está provada como causa do boundary anômalo — é a causa
candidata forte porque explica a recusa das operações de plano e a estagnação do `Plan last update`;
(ii) o objeto `DOMAIN` data de 09/04/2026, **anterior** ao início da anomalia (09/13), então a divergência
pode ter sido latente e só passou a ter efeito quando o plano precisou de extensão; (iii) **causalidade
não concluída**.
