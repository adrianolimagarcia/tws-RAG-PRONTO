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

**Métrica.** Re-rodada em **`(0c35f01, 6910 docs)`** — HEAD capturado no lançamento do avaliador
(antes dos commits desta fase). Agregados **idênticos** ao baseline commitado —
`@1 53/70 (75,7%)` · `@3 61/70 (87,1%)` · `@5 65/70 (92,9%)` · `@10 68/70 (97,1%)` · `MRR 0,8214`.
Apenas o metadado `expected_claims` de 31/70 entradas difere (resolução de GT dependente do corpus).
Baseline intacto.

> **CORREÇÃO (2026-09-15, após a re-rodada de `173096f`):** ao contrário do que afirmei aqui, os
> artefatos desta fase **ENTRAM** no corpus indexado — a re-rodada em `173096f` reportou
> **`6919 docs`** (não `6910`). O `n_docs` **não é invariante** aos artefatos de lab; o que se mantém é o
> **agregado**: `@1 53/70` · `@10 68/70` · `MRR 0,8214` — idêntico em `0c35f01` (6910 docs) e em
> `173096f` (6919 docs). Citar sempre `(HEAD, n_docs)` medidos **na própria execução**.

**Limites declarados.** (i) A divergência **não** está provada como causa do boundary anômalo — é a causa
candidata forte porque explica a recusa das operações de plano e a estagnação do `Plan last update`;
(ii) o objeto `DOMAIN` data de 09/04/2026, **anterior** ao início da anomalia (09/13), então a divergência
pode ter sido latente e só passou a ter efeito quando o plano precisou de extensão; (iii) **causalidade
não concluída**.

## 5j. M1 executada — alinhamento do MODELO ao RUNTIME no domain manager (Opção A)

> Autorização `[VIGIA-ARQUITETO / DONO: DECISAO M1 AUTORIZADA]`. Pré-registro, stop criterion e mapa de
> reversão em `docs/lab-protocols/preregistration-2026-09-15-M1-domain-manager-alignment.jsonl`.
> Evidência: `lab-validation-2026-09-15-M1-domain-manager-alignment-executed.jsonl`.

**O objeto a editar é a WORKSTATION, não o DOMAIN.** O `DOMAIN` **não é editável**:
`replace domain=MASTERDM` devolve `AWSBIA094E One of these keywords: "UNLOCK" was expected at this point`.
A via correta é a das **duas etapas** prescritas pela mensagem oficial `AWSUI0818E`: *"the program must
first change the definition of the existing master domain manager to **remove the manager attribute**"*.

**Gramática correta (fonte: `/opt/hwa/TWS/man/composer/cat1/*.1` — o binário `man` não existe no container):**

| passo | comando |
|---|---|
| extrair | `composer "extract <arquivo> from workstation=<nome>"` (**o arquivo vem primeiro**) |
| editar | o arquivo **não** tem cabeçalho `WORKSTATION <nome>`: começa em `CPUNAME <nome>`, termina em `END` |
| aplicar | `composer` → `add <arquivo>` → responder **`y`** ao *"Do you want to replace the object?"* |

- O verbo é **`add` (a)** — `{add | a} filename [;unlock]`, *"from a text file"*. **`modify` (m) sem fonte
  de definição abre EDITOR e trava** (aconteceu; o processo morto deixa **lock órfão**).
- Sem `y` nada muda (`AWSJCL015W`). Sucesso = `AWSJCL003I ... completed successfully on object` +
  `AWSBIA288I Total objects updated: 1`.
- **Lock órfão:** `add` → `AWSJDB201E ... locked by user "wauser"`; `unlock ws=MDM` → `AWSJCL012E ...
  locked by the user "wauser" in a **different session**`. Solução na man page do `unlock`:
  **`unlock ws=<nome>;forced`** — *"allows the user who locked the object to unlock it regardless of the
  session"* → `AWSBIA308I Total objects unlocked: 1`.

**Mutação executada (15.09.2026, 13:04:57Z e 13:05:38Z):** (i) `MDM_BK`: `TYPE MANAGER` → `TYPE FTA`
(o domínio passa a exibir `DOMAIN MASTERDM / ISMASTER / END`, **sem** a linha `*MANAGER` — o estado
intermediário do `AWSUI0818E`); (ii) `MDM`: `TYPE FTA` → `TYPE MANAGER`.

**Validação funcional — o erro desapareceu:**

```
planman ext -days 1
AWSJPL504I The "planner" process unlocked the database.
AWSJCL062I The production plan (Symnew) has been successfully extended.
```

`composer display domain=@` → `DOMAIN MASTERDM / *MANAGER MDM / ISMASTER` (**alvo atingido**).
`Plan last update`: **`09/12/2026 23:59` → `09/15/2026 10:05`**.

**Limite novo, declarado e NÃO improvisado.** O `showinfo` passou a reportar o sintoma de **horizonte
zero** (`Production plan end time: (same as the start time of the last extension - ... "-for 0000")`;
`Run 72` / `Confirm 69`) e o `Symnew` gerado tem **23.392 B** contra **474.368 B** do `Symphony`. O
**plano ativo segue íntegro** (`tws-op sj` → `Scheduled for (Exp) 09/13/26 (#69) on MDM. Batchman LIVES.`;
`MDM ... *UNIX MASTER`; cobertura até `09/25/2026 21:05`). **`SwitchPlan` NÃO foi executado** (ativaria o
`Symnew` de horizonte zero) e a **recuperação pesada** do runbook (`planman reset` + `planman crt -days 3`
+ `SwitchPlan` + `planman ext`) **não foi executada** — é mutação nova, de escopo maior, que exige decisão.

> **MEDIÇÃO POSTERIOR (read-only, 15.09, com o freeze vigente) — dimensiona o limite corretamente:**
> - **O plano ATIVO tem horizonte COMPLETO**, provado por `conman "sj @#@.@"`: **78 instâncias em 09/16** e
>   cobertura contínua **até 09/25** (09/16–09/18 e 09/21–09/25 com 78/dia; 09/19 = 57; 09/20 = 69),
>   incluindo `LABPOOL#POOL_STREAM 0005 09/16` e `POOL_JOB`. Portanto a leitura do boundary de 16.09 é
>   **válida** e o congelamento de mutação **não custa cobertura**.
> - O horizonte zero é da **extensão PENDENTE** (`Symnew`), **não** do plano ativo. E o `Symnew` de
>   23.392 B **não é degenerado**: há precedente idêntico no lab — `Symnew.bak` = **19.584 B** (09/09).
> - O risco de um `SwitchPlan` prematuro continua real (trocaria o plano ativo por uma extensão de 0 dias),
>   mas a leitura correta é essa — **não** "o plano perdeu horizonte".

**Reversão:** `ws_mdm.def.PRE-M1` e `ws_mdmbk.def.PRE-M1` (definições completas pré-mutação, extraídas pelo
próprio produto, re-aplicáveis pelo mesmo `add`); snapshot `ha_snap_20260914-0035`. PostgreSQL não
tocado; Sfinal intacto; nada fora do lab.

**Métrica (re-rodada após a mutação, citando HEAD e n_docs medidos na execução):**
**`(173096f, 6919 docs)`** → `@1 53/70 (75,7%)` · `@3 61/70 (87,1%)` · `@5 65/70 (92,9%)` ·
`@10 68/70 (97,1%)` · `MRR 0,8214` — **agregados idênticos** ao baseline. A mutação M1 é do lab TWS e não
toca o corpus do RAG; o `n_docs` subiu de `6910` (execução em `0c35f01`) para `6919` porque **os artefatos
desta fase entram no glob indexado** — o agregado é que se mantém estável.

## 5k. Esteira desbloqueada e plano avançado — recuperação pelo caminho do produto

> Autorização `[VIGIA-ARQUITETO]` (FASE 1 read-only + FASE 2 desbloqueio). Evidência:
> `lab-validation-2026-09-15-esteira-unblocked-plan-advanced.jsonl`. Pré-estado em `/tmp/ha_fm/fase3/`.

**Diagnóstico.** O ABEND do `MDMXA#FINAL[(2359 09/13/26)].MAKEPLAN` (`#J894375`, 09/14 02:59:09 BR, rc=8)
morria em **`AWSJPL004E`** — a mesma divergência modelo×runtime que a M1 removeu. A cadeia estava
cascateada em 3 dias (`FINAL 09/13` STUCK → `09/14` HOLD → `09/15` HOLD, e os `FINALPOSTREPORTS` atrás).

**Medição read-only que corrige a premissa:** a anomalia do boundary **não é gated pela cadeia** — o
boundary de 09/13 (a **primeira** anomalia, 0 READY) ocorreu com a cadeia **SUCC** (`STARTAPPSERVER`/
`MAKEPLAN`/`SWITCHPLAN` SUCC em 09/13 00:00, `#J273030`); o ABEND só veio às 02:59 de 09/14. Cadeia e
boundary são **duas manifestações da mesma causa raiz**; o ABEND não causou a primeira anomalia.

**Sintaxe obtida na fonte (não inventada):** `/opt/hwa/TWS/man/conman/cat1/*.1`

- `rerun` = `{rerun | rr} jobselect` — *"Reruns a job"*; `jobselect` =
  `[jobstream_[folder/]workstation#]{jobstreamname(hhmm[date]).jobname}` (exemplo oficial: `rr main#sked1.job4`).
- `start` = `start [domain!][folder/]workstation [;mgr] [;noask] [;demgr]` — **`;mgr`** = *"starts the local
  workstation as the **domain manager**"* (o passo do protocolo do dono para a esteira).
- **Pré-condição da man page**: `conman start` **não** pode ser emitido enquanto `JnextPlan`/`stageman` roda
  (verificado: nenhum processo de plano em execução).

**Sequência executada (3 passos, todos do produto):**

| # | comando | resposta |
|---|---|---|
| A | `conman "start;mgr;noask"` | `AWSBHU507I A start command was issued for MDM.` |
| B | `conman "rr MDMXA#FINAL(2359 09/13/26).MAKEPLAN;noask"` | job re-lançado (`#J1190144`) — **ABEND de novo, mas com erro DIFERENTE**: `AWSJPL017E` (*"a previous action on the production plan did not complete successfully"*); **`AWSJPL004E` = 0 ocorrências** |
| C | `planman unlock` + novo `rerun` | `AWSJPL504I` + `AWSJCL050I`; então **MAKEPLAN SUCC** |

**O `AWSJPL017E` é exatamente o erro documentado** em `hwa-10.2.8-stuck-plan-recovery.md`: o Symnew
pendente deixa o ciclo incompleto, e *"`planman unlock` sozinho resolve `AWSJPL017E` na grande maioria dos
casos"*. **`planman unlock` não está entre os comandos proibidos.**

**Resultado.** A cadeia fez **o seu próprio `SWITCHPLAN`** (SUCC 10:28) — **nenhum `SwitchPlan` manual**:

```
FINAL 2359 09/13 -> SUCC      (MAKEPLAN SUCC, SWITCHPLAN SUCC)
FINAL 2359 09/14 -> SUCC      (MAKEPLAN SUCC, SWITCHPLAN SUCC)
FINAL 2359 09/15 -> HOLD (09/16)   FINAL 2359 09/16 -> HOLD (09/17)
```

E o estado preso terminou:

```
Production plan start of last extension: 09/26/2026 00:05
Production plan end time:                09/27/2026 00:04   <- horizonte REAL de 24h
Plan last update:                        09/15/2026 10:29
Run number: 74        Confirm run number: 74                <- a igualdade exigida pelo checklist
AWSJPL004E = 0        AWSJPL017E = 0
```

**Limites declarados.** (i) O boundary de 16.09 (20:58 BR) **segue não observado** — é a próxima medida, e
agora com plano estendido e `Run == Confirm` ela é limpa; (ii) o plano ainda contém os registros órfãos do
`AGT1` (`workstation AGT1` run 35 e `AGT1#CROSS_STREAM 0005 09/16 HOLD`), removidos do **modelo** na M-C;
(iii) **causalidade não provada** — a M1 removeu o `AWSJPL004E` (0 ocorrências) e a cadeia voltou a andar,
mas o boundary em si ainda não foi re-medido; (iv) não foram usados `planman reset|crt`, `JnextPlan`,
`SwitchPlan` manual, `conman submit|sbs|cs|altjob|switchmgr` nem `composer add|update`.

## 5l. Simulação do boundary — transição noturna antecipada por `RELEASE SCHED` (caminho do produto)

> Autorização `[VIGIA-ARQUITETO / DONO]`. Evidência:
> `lab-validation-2026-09-15-boundary-simulation-release-sched-clean.jsonl`. Pré-estado em `/tmp/ha_fm/fase4/`.
> **Sem alterar o relógio do SO** (proibido) — a antecipação é feita liberando a dependência de tempo.

**Sintaxe na fonte** (`/opt/hwa/TWS/man/conman/cat1/release.1`) — existem **dois** comandos distintos:

| comando | sintaxe | escopo |
|---|---|---|
| `RELEASE JOB` | `{release job \| rj} jobselect [;dependency] [;noask]` | libera **o job** |
| `RELEASE SCHED` | `{release sched \| rs} jstreamselect [;dependency] [;noask]` | *"Releases **job streams** from dependencies"* |

**Armadilhas medidas (não repetir):**
- `rj <stream>.<job>;at` libera **só o `at` do job** — o **stream continua HOLD**. Foi preciso `rs`.
- `rj`/`rs` **sem** argumento de dependência libera **TODAS** as dependências, inclusive os `follows`
  internos — poderia disparar o `SWITCHPLAN` antes do `MAKEPLAN` e **estragar a medição**. Sempre `;at`.
- **Não** usar `conman sbs` (cria/realoca instância **nova**).

**Comando executado:** `conman "rs MDMXA#FINAL(2359 09/15/26);at;noask"` →
`Command forwarded to batchman for MDMXA#FINAL[(2359 09/15/26),(0AAAAAAAAAAAAADP)]`.

**Sequência no merge (hora BR):**

```
10:57:13 BATCHMAN:#S1198843/Operator command: DEPENDENCY RELEASED ON MDMXA#FINAL[(2359 09/15/26),...];AT= 0259
10:57:16 AWSBHT036I Attempting to launch ...STARTAPPSERVER on MDMXA
10:57:18 ...STARTAPPSERVER (#J1198885) has completed SUCCESSFULLY
10:57:22 AWSBHT036I Attempting to launch ...MAKEPLAN
10:57:22 AWSBDW019I Launched job ...MAKEPLAN, #J1199022
```

**As 5 medições pedidas:**

| # | medição | resultado |
|---|---|---|
| a | `MAKEPLAN` SUCC ou ABEND? | **SUCC** — nenhum `AWSJPL004E`/`AWSJPL017E` |
| b | `SWITCHPLAN` via esteira? | **SUCC, limpo** — sem `SwitchPlan` manual |
| c | `Run`/`Confirm` em paridade? | **75 == 75** (antes 74/74); `Plan last update 10:57`; horizonte `09/28/2026 00:04` |
| d | órfãos do `AGT1` na transição? | **workstation desapareceu do plano** (`sc @` = 0, igual ao modelo) mas **28 instâncias totais do `AGT1` persistem** — **8 em `READY`** (`AGT1#CROSS_STREAM` e `AGT1#FTA_JOBSTREAM`, de 09/11 a 09/14) e **20 em `HOLD`** (09/15 a 09/24) |
| e | burst de READY do stream alvo | `STARTAPPSERVER` readiado e executado; `FINAL 09/16` e `09/17` enfileirados em HOLD |

**Leitura do (d):** o switch **sincroniza a tabela de workstations** com o modelo (o `AGT1` sai do plano),
mas **não purga as instâncias** — elas ficam presas em `READY` (`AGT1#CROSS_STREAM 2105 09/11…09/13`,
`AGT1#FTA_JOBSTREAM`) porque a estação não existe mais. A purga é **decisão separada, não autorizada**.

**Limites.** (i) Esta simulação antecipa a **transição noturna** (extensão/switch do plano); **não** mede o
*pass* de ready do boundary de produção das 21:00 BR, que segue armado em `vigia-h-0916`;
(ii) causalidade do boundary anômalo segue **não provada**. **Proibições respeitadas:** sem `date -s`/`timens`,
sem `planman reset|crt`, sem `JnextPlan`, sem `SwitchPlan` manual, sem `conman sbs`, SGBD compartilhado
intocado, `Sfinal` intacto.

## 5m. Boundary de 16.09 — primeira leitura PREMATURA (ramo `c` da árvore pré-registrada)

> Evidência: `lab-validation-2026-09-15-boundary-read-premature-branch-c.jsonl` (`result=PARTIAL`, `risk=read_only`).
> Árvore: `docs/lab-protocols/preregistration-2026-09-15-POS-boundary-16-09-decision-tree.md`.

**Fato decisivo (medido, não inferido).** A captura entregue abria com
`H: iniciado 2026-09-15 14:18:20 UTC | alvo epoch=1789481898 (2026-09-15 14:18:18 UTC)` — o **alvo usado foi
o instante atual**, não o epoch do boundary. O boundary de produção de 16.09 é o epoch **`1789516800` =
`2026-09-16 00:00:00 UTC` = `2026-09-15 21:00:00 BR`**; na leitura eram `2026-09-15 14:19:15 UTC` (11:19 BR),
**faltando 9,68 h**.

**Consequência.** A janela vazia (0 linhas / 0 READY / 0 `dR` / 0 `AWSBHT036I` / 0 BATCHMAN / 0 MAILMAN) **não é
anomalia nem normalidade: é ausência do evento**. É o ramo **(c)** — *"0 linhas na janela → leitura cedo
demais → RE-LER no tick seguinte, NÃO concluir NEGATIVO"*. Não é o ramo (d): o arquivo
`20260915_TWSMERGE.log` **existe** (325.171 B, modificado 10:59 BR) e só rola em ~03:05Z de 16.09 — logo o
boundary de 00:00Z **será gravado nele**, e as capturas armadas que o leem estão corretas.

**Nenhuma conclusão** de normalização ou de persistência da anomalia é emitida.

**Estado pré-boundary registrado (estado, não desfecho):**

| item | valor |
|---|---|
| `AGT1` no modelo / no plano | **0 / 0** (saiu dos dois; as **28 instâncias** seguem: 8 READY, 20 HOLD) |
| avisos `AGT1` em 15.09 | **130** `is NOT a AGENT` · **64** `unable to link` (registros do plano ainda dirigem tentativas) |
| master | `MDM 75 *UNIX MASTER ... 09/15/26 10:57` |
| alvos do boundary | `LABPOOL#POOL_STREAM 2105 09/15 HOLD 10(09/16)(00:00)` (e `2105 09/16 HOLD 10(09/17)`) |

**Critério reafirmado.** Os controles históricos `13 READY / 13 dR / 0 MAILMAN` (11–12.09) e
`0 READY / 20 MAILMAN` (13–14.09) estão **OBSOLETOS**: 2 das 13 instâncias do controle eram streams do `AGT1`
(removido do modelo pela M-C) e a composição mudou (as instâncias vigentes de `2105 09/15` são **20**, com
prefixos `LABPOOL#`/`MDM#` e streams `MDM#JS_CAL_*`/`MDM#JS_P_*` inexistentes no controle). Comparar
**conjunto × conjunto** (captura `vigia-boundary-set` → `/tmp/ha_fm/fase4/boundary_0916_SET.txt`), nunca
contagem × contagem; contagem de estado sempre com **total e por estado**.

**Limites.** O boundary segue **não observado** — a leitura correta ocorre ~5 min após `00:00Z` de 16.09;
nenhuma causalidade é afirmada; o congelamento de mutação permanece vigente; as três capturas
(`vigia-h-0916`, `vigia-chain-0916`, `vigia-boundary-set`) seguem **ACTIVE** com os alvos corretos.

## 5n. Boundary acelerado a pedido do dono — alvo executou limpo e a medida foi preservada

> Ordem direta do dono (*"acele o processo novamente"*). Evidência:
> `lab-validation-2026-09-15-boundary-accelerated-target-succ.jsonl` (`result=SUCCESS`, `risk=mutating`).
> Pré-estado em `/tmp/ha_fm/fase5/`.

**Como acelerar sem destruir a medida.** O *pass* automático do boundary (virada do dia do plano em `00:00Z`)
**não tem comando de produto** que o force — verificado nas man pages. O que se antecipa é o **efeito**:
liberar a dependência de tempo de um alvo. Liberar **todos** os 20 alvos deixaria o boundary sem nada para
readiar (um `0 READY` indistinguível da anomalia). Liberando **um só**, o resultado sai agora **e** os 19
restantes mantêm a leitura válida por **conjunto**.

**Comando:** `conman "rs LABPOOL#POOL_STREAM(2105 09/15);at;noask"` → `Command forwarded to batchman for
LABPOOL#POOL_STREAM[(2105 09/15/26),(0AAAAAAAAAAAAAHD)]` (seletor validado read-only antes).

**Desfecho (~60 s):** o stream **executou limpo** —

```
11:40:36 Received lB: ...POOL_JOB
11:40:36 AWSBHT083I ...POOL_JOB changing from state 16 to new state 15
11:40:37 ... changing from state 15 to new state 3
11:40:37 Job ...POOL_JOB has completed SUCCESSFULLY
11:40:37 AWSBHT071I Job stream ...POOL_STREAM[(2105 09/15/26),(0AAAAAAAAAAAAAHD)] has completed successfully.
11:40:37 AWSBHT075I Changing job stream ... status to SUCC.
```

| verificação | resultado |
|---|---|
| `AWSJPL004E` / `AWSJPL017E` no merge de 15.09 | **0 / 0** |
| linhas citando `AGT1` na janela de execução | **0** (sem interferência) |
| plano após a execução | **inalterado** (`Run 75 == Confirm 75`) — rodar stream não estende plano |
| alvos de boundary remanescentes | **19 de 20 seguem em HOLD** (20 totais, 19 HOLD) |

**Leitura.** O **alvo** do boundary executa limpo no estado pós-M1 — sinal **positivo**, mas **não** é a
medição do *pass* de ready do boundary, que segue **NÃO OBSERVADO** (leitura válida ~5 min após `00:00Z` de
16.09, coberta pelas três capturas armadas). **Nenhuma causalidade é afirmada**; congelamento de mutação de
plano/engine vigente (nada de `ext`/`SwitchPlan`/`composer`/purga).

## 5o. Boundary acelerado em lote — 7/10 SUCC e as instâncias órfãs do `AGT1` são INERTES

> Segunda ordem direta do dono. Evidência: `lab-validation-2026-09-15-boundary-accelerated-batch-agt1-inert.jsonl`
> (`result=SUCCESS`, `risk=mutating`). Pré-estado em `/tmp/ha_fm/fase5b/`.

Lote de **10 dos 19** alvos em HOLD liberados por `rs <stream>(2105 09/15);at;noask` (todos aceitos:
`Command forwarded to batchman`), preservando **9** para o boundary das 21:00 BR.

| alvo | desfecho |
|---|---|
| `LABPOOL#POOL_BALANCING` · `MDM#FRENTE1_STREAM` · `MDM#JS_ALTJOB_TEST` · `MDM#JS_CAL_BASE` · `MDM#JS_CAL_FREE` · `MDM#JS_CAL_NEXT` · `MDM#JS_CAL_PREV` | **SUCC** (7) |
| `AGT1#CROSS_STREAM` · `AGT1#FTA_JOBSTREAM` | **READY — sem tentativa de launch e sem erro** |
| `MDM#JS_ALTJOB3` | **READY** (causa não investigada) |

**Estado dos alvos de boundary** (total **e** por estado): **20 totais = 8 SUCC + 3 READY + 9 HOLD**
(os 7 do lote + o `LABPOOL#POOL_STREAM` do probe anterior = 8 SUCC).

**Achado novo — as instâncias órfãs do `AGT1` são INERTES.** Liberadas da dependência de tempo, as duas
instâncias do `AGT1` foram para `READY` **sem nenhuma tentativa de lançamento e sem erro** (`grep 'AGT1'`
na janela do lote: **vazio**). É coerente com a estação estar ausente dos **dois** lados: sem definição de
workstation no plano, o batchman não tem onde lançar e **não reclama** — os registros ficam parados em
`READY`, **sem dano ao plano**. Não se confirma, portanto, que os órfãos do `AGT1` atrapalhem a execução.

**Erros de plano:** `AWSJPL004E` = **0** e `AWSJPL017E` = **0**.

**Medida preservada:** **9 alvos em HOLD** (`MDM#JS_LOGON_TEST`, `MDM#JS_P_29030/7069/9574`,
`MDM#JS_PROMPT_RUN`, `MDM#JS_VAR_RUN`, `MDM#JS_VARTABLE_ERR/OK`, `TWS-AGENT_1#DYN_JOBSTREAM`) — o boundary
segue comparável por **conjunto**, agora com 9 esperadas.

**Limites.** O *pass* automático do boundary segue **não observado** e **não é antecipável** por comando de
produto; antecipou-se o **efeito** em 11 dos 20 alvos. Nenhuma causalidade é afirmada; congelamento de
mutação de plano/engine vigente.

## 5p. Aceleração final — 16/20 SUCC e o conjunto do boundary ZERADO por consumo

> Terceira ordem direta do dono. Evidência: `lab-validation-2026-09-15-boundary-accelerated-final-boundary-voided.jsonl`
> (`result=SUCCESS`, `risk=mutating`). Pré-estado em `/tmp/ha_fm/fase5c/`.

**Lote final:** os 9 alvos restantes liberados por `rs <stream>(2105 09/15);at;noask` (timeout defensivo nos
dois interativos). **8 SUCC** (`JS_LOGON_TEST`, `JS_P_29030/7069/9574`, `JS_VAR_RUN`, `JS_VARTABLE_ERR/OK`,
`DYN_JOBSTREAM`) e **1 STUCK** (`MDM#JS_PROMPT_RUN`).

**O STUCK do `JS_PROMPT_RUN` é comportamento CORRETO, não falha.** O merge registra a sequência de um stream
que exige prompt:

```
12:56:42 #S1231326/Operator command: DEPENDENCY RELEASED ON JS_PROMPT_RUN[(2105 09/15/26),(0AAAAAAAAAAAAAOL)];AT=
12:56:44 AWSBHT075I Changing job stream ... status to READY.
12:56:44 AWSBHT075I Changing job stream ... status to STUCK.
12:56:44 * AWSBHT069E The following job stream is in the "stuck" state: JS_PROMPT_RUN[(2105 09/15/26),(0AAAAAAAAAAAAAOL)]
```

com o job `JOB_PROMPTED` em `HOLD` aguardando resposta.

**Estado final dos 20 alvos de boundary** (total **e** por estado): **20 = 16 SUCC + 3 READY + 1 STUCK**.
Os 3 `READY` são os 2 do `AGT1` (**inertes** — estação ausente dos dois lados) e `MDM#JS_ALTJOB3` (causa não
investigada).

| verificação | resultado |
|---|---|
| `AWSJPL004E` / `AWSJPL017E` | **0 / 0** |
| plano | **inalterado** (`Run 75 == Confirm 75`) |
| alvos em HOLD para o boundary das 21:00 BR | **0** |

> ⚠️ **A MEDIÇÃO AUTOMÁTICA DO BOUNDARY DE 16.09 ESTÁ ANULADA POR CONSUMO.** Não haverá instâncias para
> readiar às 21:00 BR, e as três capturas armadas registrarão uma **janela vazia por consumo**, **não** por
> anomalia nem por normalidade. Este parágrafo existe para que esse `0 READY` não seja mal lido.

**Leitura.** No estado pós-M1 a **produção executa limpa**: 16 dos 20 alvos de boundary concluíram **SUCC**
sob demanda. **O *pass* automático do boundary segue NÃO OBSERVADO** e não é antecipável por comando de
produto. Nenhuma causalidade é afirmada; congelamento de mutação de plano/engine vigente.

## 5q. Conjunto do boundary repovoado por `SUBMIT SCHED` — a medição de hoje voltou a ser observável

> Quarta ordem direta do dono. Evidência: `lab-validation-2026-09-15-boundary-set-repopulated-via-submit-sched.jsonl`
> (`result=SUCCESS`, `risk=mutating`). Pré-estado em `/tmp/ha_fm/fase6/`.

**Como restaurar a medição depois de consumir o conjunto.** O `pass` de ready do boundary só tem o que
readiar se houver instâncias retidas. Submetendo instâncias **novas** agendadas para a janela do boundary,
o mecanismo volta a ser observável — sem custo adicional, porque o conjunto original já havia sido consumido.

**Sintaxe (fonte: `/opt/hwa/TWS/man/conman/cat1/submit.1`, seção `SUBMIT SCHED` — é assim que a man page
chama o submit de job stream, o `sbs`):**

```
{submit sched = | sbs =} [[folder/]workstation#][folder/]jstreamname [;jstreamoption[;...]] [;noask]
```

**Comando e resultado:** `conman "sbs = <stream>;at=0005;noask"` → 4 submetidos com sucesso
(`LABPOOL#POOL_STREAM`, `LABPOOL#POOL_BALANCING`, `MDM#FRENTE1_STREAM`, `MDM#JS_VARTABLE_OK`), todos com

```
LABPOOL#POOL_STREAM  0005 09/16 ... HOLD 10(09/16)(00:00)
```

**Achado de método — o `at` do `sbs` é UTC, não BR.** `at=0005` criou a instância rotulada **`0005 09/16`**
(= 00:05Z = 21:05 BR), que é **o mesmo instante** dos alvos de produção originais, estes rotulados
**`2105 09/15`** (= 21:05 BR). O plano exibe o schedtime em **BR**; o `at` do `sbs` trabalha em **UTC**.
A dualidade descrita em `hwa-lab-10.2.8-plan-timebase-utc-and-sbs-at-no-autorelease-0001` foi **reproduzida**.
O `HOLD 10(09/16)(00:00)` confirma que a instância é liberada **exatamente no boundary** (21:00 BR / 00:00Z).

**Recusa informativa:** `sbs = AGT1#CROSS_STREAM;at=0005` → `AWSJPL507E The submitted ad hoc job stream does
not exist` — o stream **saiu do modelo** (removido pela M-C). O registro órfão do `AGT1` é **defunto**: nem o
canal de submit o aceita.

| verificação | resultado |
|---|---|
| plano | **inalterado** (`Run 75 == Confirm 75`) — submeter não estende plano |
| `AWSJPL004E` / `AWSJPL017E` | **0 / 0** |
| conjunto repovoado | **4 instâncias**, todas `HOLD` até `00:00Z` |
| conjunto de **09/16** (boundary de **amanhã**, ~32 h) | **20 intactas em HOLD** — a medida limpa segue disponível |

**O que permite e o que não permite.** Permite observar **hoje** o *pass* de ready (o batchman liberando as
instâncias retidas às `00:00Z`) — o mecanismo que **nunca foi observado**. **Não** reproduz o boundary de
produção puro: as instâncias são **submetidas por nós**, não os alvos de produção originais.
Nenhuma causalidade é afirmada; congelamento de mutação de plano/engine vigente.

---

## 5r. Ingestão das man pages do produto — o conhecimento entrou, o número **piorou** (medido)

**Objetivo.** As man pages do produto (`/opt/hwa/TWS/man/{composer,conman}/cat1/`, 95 arquivos) tinham
**0 referências no loader** — a fonte autoritativa da sintaxe estava fora do corpus. A tese era que isso
explicava o buraco de recall da fatia procedimental.

**O que foi entregue.** `scripts/extract_man_pages.py` (versionado) lê as páginas do container e gera
`data/knowledge/man-pages-derived.jsonl` — 95 registros (composer 32 + conman 63) com paráfrase PT-BR,
sintaxe essencial e citação curta; 17 marcados `observed_in_lab`. Mais
`data/knowledge/lab-procedures-derived.jsonl` (item 2): 17 procedimentos desta sessão. **Licença respeitada**:
o texto cru não entra no git — só o script e o derivado.

**Armadilha de parser (corrigida, vale registrar).** A primeira versão citava a linha de **permissão**
("You must have rerun access…") porque o filtro de tamanho descartava a linha semântica **curta**
("Reruns a job.", 13 chars) e **não há seção `Authorization`** em várias páginas. E a extração de sintaxe
pegava só a **primeira** seção `Syntax`: em `submit.1` isso omitia a variante **SCHED** — justamente o `sbs`
usado no lab. Auditoria final: 0/95 com padrão de permissão.

**Medição (HEAD `fded8c4`, `PYTHONHASHSEED=0`).**

| cenário | n_docs | @1 | @5 | @10 | MRR |
|---|---|---|---|---|---|
| **default (fonte OFF)** | 6950 | **53/70** | 65 | 68 | **0,8214** |
| abatido (`RAG_DROP_SYNTHETIC=1`) | 6950 | **52/70** | 64 | 68 | **0,8128** |
| fonte **ON** | 7062 | **52/70** | 64 | 67 | **0,8105** |
| ON + abatido | 7062 | **51/70** | 64 | 67 | **0,8034** |

No benchmark cego v3 (262 perguntas): `@1` **183/262 → 180/262**; por fatia A `97/107 → 96/107`,
B `80/140 → 78/140`, D `6/15 → 6/15`. **25 perguntas mudaram de rank e TODAS pioraram — 0 melhoraram.**

**Mecanismo (diff por pergunta, não é não-determinismo).** Em `eval-0069` o top-3 passou a ser
`[man-conman-showjobs, distributed-conman-showjobs, man-conman-jobselect]` e o claim específico esperado
(`showjobs-wildcard-ws-filter-0111`) caiu para **19**. Em `eval-0031`, um doc do item 2
(`proc-esteira-cadeia-final`) tomou o rank 1 do `finalpostreports` esperado. 22 das 70 perguntas têm algum
doc derivado no top-3. As man pages são **vizinhas semânticas genérico-autoritativas** dos claims específicos
do lab e ganham deles — **o mesmo padrão genérico × específico** já visto na adjudicação dos 17 misses.

**Conclusão.** A ingestão **captura o conhecimento certo** mas **não melhora o recall medido**: nenhum
benchmark atual pergunta a sintaxe, então o benefício é invisível e o custo é visível. **Stop criterion do
vigia disparou** ("inflar o corpus a ponto de mover o número das 70 por competição de rank") e o caso foi
reportado. Boost/rerank **não** foram tocados.

**Estado deixado.** A fonte entra no loader atrás de `RAG_INGEST_DERIVED` (**default OFF**, o padrão
`RAG_DROP_*` já usado no arquivo), para não deixar um baseline regredido em silêncio. Ligar é decisão
explícita — e o ideal é existir uma **fatia de benchmark que pergunte a sintaxe**, senão o ganho não é medível.

## 5s. Leitura do boundary de 16.09 no alvo — o `TWSMERGE` do MDM **congelou antes do boundary**

**Alvo**: `2026-09-16 00:00:00Z` (21:00 BR de 15.09). Leituras em `00:02:21Z` e `00:11:50Z`. Congelamento
de mutação vigente; **nenhum** comando de mutação de plano foi usado.

**Resultado: nenhum ramo da árvore pré-registrada cobre o estado observado.**

| ramo | exigia | observado |
|---|---|---|
| (a) | janela do MDM não-vazia com `dR>0` E `MAILMAN=0`, **ou** PRIMÁRIO readiando por completo | janela **vazia**; `JS_VARTABLE_OK` segue HOLD → **não** |
| (b) | burst de READY com `LAUNCH=0`/`SUCC=0`, **ou** 0 READY com janela **não-vazia** | janela vazia → **não** |
| (c) | `0 linhas` = leitura cedo demais | confere o zero, mas a re-leitura 8 min depois dá o mesmo, com arquivo **inalterado** → **só em parte** |

**O que se sustenta e o que foi erratado:**

- **O `TWSMERGE` do MDM NÃO congelou** (errata de interpretação, `VIGIA-CORR-0916-MEDICAO-2`): o último
escritor é o **tick de 3 h do profiler do `MAILMAN`**, e o próprio produto reporta o período na linha
(`MAILMAN WORKING PROFILER OF THE LAST ===> 10815 seconds`). Cadência medida: `13:57:47 → 16:58:03 → 19:58:18`
(deltas `3:00:15` e `3:00:16`). **Próximo tick ~22:58:33 BR (01:58:33Z)** — se o arquivo se mover então,
**não** é "descongelamento", é o mesmo tick de 3 h. O mtime/tamanho idênticos em 4 leituras são coerentes
com o tick, não com travamento.
- **O silêncio tem causa medida**: o escritor periódico dos dias saudáveis era o **heartbeat de 10 min do
`AGT1`** (`MY:UNLINK AGT1`; **159 ocorrências em 12.09 contra 100 em 15.09**). Com o `AGT1` fora do **modelo**,
o heartbeat e as tentativas de link morreram — última menção a `AGT1` no arquivo: **`12:44:46`**, e
`unable to link` deixa de aparecer após a hora 10. **O silêncio é consequência da remoção do `AGT1`, não um
estado novo do log.** O nó está vivo (`mailman`/`batchman` ativos; `MONMAN` e `APPSRVMN` escrevendo).
- **Série por arquivo** (mesma janela): `10=481`, `11=77`, `12=79`, `13=22`, `14=22`, **`15=0`**. **ERRATA:**
as 22 linhas de 13.09/14.09 **não** são "pass degradado" — composição medida nos dois dias: **total 22 =
20 MAILMAN** (falhas de link do `AGT1`: `AWSBCV035W` + `AWSBCV082I`) **+ 2 BATCHMAN** (o próprio heartbeat
`MY:UNLINK AGT1`). Comparar 22 (com ruído do `AGT1`) com 0 (sem) compara **piso de ruído, não mecanismo**:
o 0 de hoje é **esperado** após a remoção. **O "terceiro estado" que a 1ª versão descreveu NÃO existe.**
- **O discriminador que sobrevive** (não afetado pelo `AGT1`): `Received dR: ... from cpu MDM_BK` e
`status to READY` do BATCHMAN. Série: `11.09 = 77/13 READY/13 dR/0 MAILMAN`, `12.09 = 79/13/13/0`,
`13.09 = 22/0/0/20`, `14.09 = 22/0/0/20`, **`15.09 = 0/0/0/0`** (no 15.09 não há nem o piso de ruído).
O que se sustenta é **`0 dR` E `0 READY`** — o master **não processou o boundary**.
- **Próximo evento de hora marcada**: o pass da **meia-noite local**, quando o stdlist do MDM vira —
medido `00:02–00:07 BR` nos dias 10 a 15.09.
- **O plano não avançou de dia**: `Scheduled for (Exp) 09/15/26 (#75)`, `Run 75 == Confirm 75`,
`Plan last update 09/15/2026 10:57`. Os daemons subiram às 10:57 — a mesma hora do last update
(coincidência registrada, sem interpretação causal).
- **Conjunto desta janela (cohort `0005 09/16`)**: **QUATRO instâncias, TODAS HOLD no MDM** —
  `LABPOOL#POOL_STREAM`, `LABPOOL#POOL_BALANCING`, `MDM#FRENTE1_STREAM`, `MDM#JS_VARTABLE_OK`
  (censo por **ENUMERAÇÃO** `sj @#@.@`, 953 linhas). **ERRATA — erro de medição corrigido**: a primeira
  versão desta seção afirmava que `POOL_STREAM` e `POOL_BALANCING` "saíram do plano"; **é falso**. Os dois
  streams pertencem à workstation **LABPOOL**, não a MDM/MDMXA — `sj MDM#POOL_STREAM.@` devolve
  `AWSBHU072E There are no objects` (**falso negativo de seletor**) mesmo com o objeto existindo.
  Confirmado: `sj LABPOOL#POOL_STREAM.@` → `HOLD 10(09/16)(00:00)`; `composer display jobstream=LABPOOL#POOL_STREAM`
  → 1 objeto contra 0 para `MDM#POOL_STREAM`. **O pitfall já estava documentado na skill `tws-hwa` e ainda
  assim foi violado** — a lição operacional é que censo de conjunto se faz por **enumeração**, nunca por nome
  nu com qualificador presumido.
- **O pass do boundary FUNCIONOU — no BMDM** (achado novo): o stdlist virou às `00:05:03Z`
  (`AWSDDW100I SWITCHED`, arquivo novo `20260916_TWSMERGE.log`) e o pass readiou **as quatro** instâncias
  ad-hoc — `POOL_STREAM`, `POOL_BALANCING`, `FRENTE1_STREAM`, `JS_VARTABLE_OK` → **READY**. O `sj` do BMDM
  concorda; o `sj` do MDM mantém as 4 em **HOLD**. É o **mesmo par de visões divergentes** já medido em
  13.09 e 14.09 (MDM sem o burst, BMDM com ele).
- **BMDM**: 1 linha, `FINALPOSTREPORTS → READY` às `00:00:05Z`. É o nome que o **D11** exclui deste
conjunto (0/4 dias de controle) — hoje ele readiou no instante do boundary de produção, não da
meia-noite local. Diferença real contra o controle.

**Pergunta aberta do `at` (o PASS libera o `at` do `sbs`?) — RESPOSTA PARCIAL**: um PASS **liberou** as 4
instâncias submetidas com `;at=` — **mas no BMDM, não no MDM**. É coerente com o claim medido
(`...plan-timebase-utc-and-sbs-at-no-autorelease-0001`: o `sbs;at` **não** auto-libera **fora** de um pass)
e agora há um caso **dentro** de um pass. **Ressalva registrada**: o pass que liberou foi o do **BMDM** e a
instância foi criada pelo **MDM** — **não** se pode escrever "o pass do MDM libera o `at`".

**Defeitos do payload recebido**: (i) a captura `/tmp/d11test/ev_full.txt` (167 B) continha apenas
**placeholders** (`"linha de merge com READY/dR/SUCC"` repetido), nenhum dado — **não usada**;
(ii) a injeção disparou **~5,5 min antes** do alvo (relógio `23:54:39Z` contra alvo `00:00:00Z`),
mesma classe do defeito de `14:18:22Z` já documentado.

**Estado deixado.** Nada mutado. Evidência:
`data/evidence/lab-validation-2026-09-16-boundary-16-09-reading-mdm-twsmerge-frozen.jsonl`
(gate `validate_lab_session.py` = **VÁLIDO**).

## 5t. Lab fora do ar em 16.09 — causa raiz e o evento do boundary **NÃO OBSERVADO**

**Causa raiz** (medida pelo VIGIA-ARQUITETO por journal do host + output do comando; reconferida aqui read-only):

| hora (BR) | evento |
|---|---|
| `15/09 23:55:32` | as capturas do boundary ficam `Deactivated successfully` — **nenhuma escreveu o alvo** |
| `15/09 23:55:42` | **SHUTDOWN do host** (última entrada do boot `-1`) |
| `16/09 01:03:35` | host volta (boot 0); `dockerd` restaura os 5 containers às `01:08:38` |
| `16/09 02:28:08` | sessão irmã `e9b3b8b7e0c4` roda `docker container prune -f` — escopo aprovado pelo dono: "imagens dangling + **containers parados**". A saída lista exatamente os 3 do lab e fecha com `Total reclaimed space: 12.3GB` |
| `16/09 02:28:14` | `docker image prune -f` (só dangling, 21,1 GB) — as imagens `ha_snap_20260914-0035_tws-*` e as tags `tws-hwa:lab-*` **sobrevivem** |

**O lab não desapareceu sozinho:** parou no reboot (**não tem restart policy** — o `dockerd` restaurou os 5 mas deixou os 3 **parados**) e foi **removido por um prune cujo escopo "containers parados" pegou os 3**; a camada gravável foi junto. **O `tws-watchdog` está correto** (`CRITICAL` real, email desativado por default → alarme só no journal).

**O evento do boundary está NÃO OBSERVADO, nunca negativo.** A janela da meia-noite local (`00:02–00:07 BR`, medida nos dias 10–15.09) caiu **integralmente dentro do período com o host desligado** (`23:55:42 → 01:03:35`). **Não há medição possível**; a medida limpa esperada para o dia de plano 09/16 está **perdida por indisponibilidade do host**. Não reinterpretar a série por isso.

**Inventário do snapshot 112 (btrfs, ID 379) — read-only:**

- Preserva `/var/lib/containerd`, inclusive a **camada gravável do `tws-hwa`** (containerd snapshot 7).
- `20260915_TWSMERGE.log`: **386880 B, mtime `22:58:33`** — o crescimento de `386657 B` (mtime 19:58) até aqui é o **tick de 3 h do profiler do MAILMAN**, exatamente como previsto, **não** um "descongelamento".
- `20260915_APPSRVMN.log` `23:54:48` · `20260915_MONMAN.log` `23:54:58` · banco `/var/lib/pgsql/18/data` `23:55:34`.
- **Estado preservado = PÓS-M1** (a M1 foi aplicada em 09/15 10:57) — diferente das imagens `ha_snap_20260914-0035_*`, que são de 09/14 00:35 e **não** contêm a M1.

**Não executado e não autorizado neste tick:** reconstrução dos containers ou `docker run` do lab — reconstruir a camada overlay a partir do snapshot btrfs **não é operação nativa do Docker** e mexe em infra do host com risco no banco do lab. **Decisão do dono.**

**Estado deixado.** Nada mutado; o snapshot 112 permanece intacto como ponto de reconstrução. Evidência:
`data/evidence/lab-validation-2026-09-16-lab-down-root-cause-and-snapshot-112-inventory.jsonl`.

## 5u. Reconstrução do lab **APLICADA** (autorizada pelo dono) — 3 containers de pé, binds no SDB, backup único e limpeza

**Aplicação**: `./docs/lab-up-2026-09-16.sh --image A --apply`, na ordem agent → bmdm → hwa. Os três subiram
(`UP` no stop_criterion). O `tws-hwa` usou o caminho **create + network connect + start**.

| container | imagem | rede primária | restart |
|---|---|---|---|
| `tws-agent` | `ha_snap_20260914-0035_tws-agent` | `hwa-mesh` | `unless-stopped` |
| `tws-bmdm` | `ha_snap_20260914-0035_tws-bmdm` | `hwa-mesh` | `unless-stopped` |
| `tws-hwa` | `tws-hwa:vigia-validacao-20260916` (**flatten do snapshot 112, PÓS-M1**) | `bridge` | `unless-stopped` |

**Diretriz 1 — binds no SDB (cumprida)**: todos os mounts de persistência apontam para
`/run/media/adriano/e681b5ac-…/hermes/docker/{tws-hwa,tws-bmdm,tws-agent}/…`. **Nenhum dado de lab no SDA.**

**Lab funcional**: `conman sj @#@.@` lê o plano (`TWS-AGENT_1 #DYN_JOBSTREAM 2105 09/25..27 HOLD`);
`conman sc @` mostra `MDMDA, MDMXA, MDM_BK, MDM_BKA, MDM_DWB` em **run 75** com papel `MASTER`;
`batchman`+`mailman` ativos no MDM e no BMDM. Portas no `tws-hwa`: **31116** (engineServer), 31114 (agent),
31113/31111 (netman), 5432 (postgres), 22 (sshd).

**Diretriz 2 — backup único**: a pasta `hermes/tws-lab-snapshots/` estava **vazia** (criada no mesmo dia),
logo **não havia snapshot anterior a substituir ou expurgar**. Gravada **1 cópia** — `tws-lab-20260916.tar`,
**7675786240 bytes (7,68 GB)**, `rc=0` em **2m57s**, e a pasta contém **apenas esse arquivo** (nenhum
`.tmp`, nenhuma cópia solta). SDB após o backup: **121 G usados / 809 G livres**.

**Diretriz 3 — limpeza**: `crazy_banzai` removido; **3 imagens legadas removidas** —
`ha_snap_20260914-0035_tws-hwa` (9,28 GB), `tws-hwa:lab-10.2.8-dwc` (9,04 GB) e `tws-hwa:lab-10.2.8`
(5,44 GB), **~23,8 GB**. Restam no Docker apenas as **3 imagens estritamente ativas**.

**Ressalvas registradas:**
- As imagens `ha_snap_20260914-0035_tws-bmdm` e `_tws-agent` **não** foram removidas: estão **em uso** — são
  exatamente as "imagens estritamente ativas" que a diretriz manda manter.
- O `df` do SDA **não se moveu** após as remoções (138 G usados / 94 G livres); `du /var/lib/docker` = 14 G e
  o btrfs reporta 129,33 GiB usados em Data. Em btrfs a devolução de espaço de camadas removidas pode não
  aparecer no `df` sem rebalance — **o ganho está confirmado no inventário do docker, não no `df`**.

**Reversão**: `./docs/lab-up-2026-09-16.sh --down --apply` — os binds `/data` não são tocados; o backup e o
snapshot btrfs 112 permanecem.

**Estado deixado.** Nenhum `prune` executado; snapshot 112 intacto; `/data` intocado. Evidência:
`data/evidence/lab-validation-2026-09-16-lab-reconstruction-applied-and-cleanup.jsonl`.

## 5v. Boundary de produção de 16.09 — **LIDO**, e o MDM perde o `MDM_BK` por falha de resolução de nome

Leitura executada **depois** do alvo (`2026-09-17 00:00:00Z` = 21:00 BR de 16.09), às `01:49Z`. Frente
read-only pré-registrada em `docs/lab-protocols/preregistration-2026-09-17-boundary-producao-16-09.md`.

| ramo | janela | linhas | `dR` | `READY` | veredito |
|---|---|---|---|---|---|
| **MDM** | `^(20:5[89]\|21:0[0-2]):` (BR) | 38 | **0** | **0** | **NÃO processado** |
| **BMDM** | `^00:00:0[0-9]` (UTC) | 24 | — | **20** | **processado** |

**Controles positivos no mesmo tick** (obrigatórios): MDM `20260912` = **79 linhas** (esperado 79) ✓ ·
BMDM `20260913` = **24/20** (esperado 24/20) ✓. Sem eles o resultado seria inconclusivo, não negativo.

**O achado:** as 38 linhas do MDM **não são silêncio** — são falha de resolução de nome no instante do boundary:

```
21:00:20 |MAILMAN:CRITICAL:getaddrinfo: gai_strerror=Name or service not known
21:00:20 |MAILMAN:CRITICAL:ipc_connect, error in getaddrinfo for server tws-bmdm
21:00:20 |MAILMAN:+ AWSBCV082I Workstation MDM_BK, message: AWSDEB052E
21:00:20 |MAILMAN:+ AWSBCV035W Mailman was unable to link to workstation: MDM_BK
21:00:20 |BATCHMAN:Workstation MDM_BK State is being changed: UNSETTING: LINKED
```

O MDM **perde o link com o `MDM_BK`** (o backup master) — e sem o backup master não há `dR` nem `READY`.

**Correção de conclusão prematura (registrada de propósito).** A tabela de correlação abaixo sugere 4/4 e
eu quase fechei causa raiz nela. **Não fecha:** o mecanismo **difere por dia**.

| arquivo | linhas | `dR` | `READY` | erro de resolução | qual erro |
|---|---|---|---|---|---|
| 10.09 | 481 | 2 | 3 | 0 | — |
| 11.09 | 77 | 13 | 13 | 0 | — |
| 12.09 | 79 | 13 | 13 | 0 | — |
| 13.09 | 22 | 0 | 0 | 1 | `unable to link ... AGT1` |
| 14.09 | 22 | 0 | 0 | 1 | `unable to link ... AGT1` |
| 15.09 | 0 | 0 | 0 | 0 | host desligado na janela |
| 16.09 | 38 | 0 | 0 | 7 | **`getaddrinfo` → `unable to link ... MDM_BK`** |

O unlink do **`AGT1`** é **normal** — o dia bom (12.09, 20:59:23) também o apresenta, seguido de
`Received dR: … from cpu MDM_BK` às 21:00:05. Logo **13.09 e 14.09 não são explicados por este mecanismo**.
O defeito de **hoje** é distinto e tem gatilho medido.

**Divergência de topologia (medida):** no snapshot 112 a `hwa-mesh` do `tws-bmdm` era estática (`…11`) e a do
`tws-agent` (`…12`); na reconstrução os dois subiram com **IP dinâmico**, enquanto o `tws-hwa` manteve o IP
fixo derivado do snapshot (`…10`). O MDM **não tem `tws-bmdm` em `/etc/hosts`** — depende do DNS embutido do
Docker, que respondeu NXDOMAIN naquele instante.

**O que NÃO se pode escrever:** "causa raiz fechada". A resolução de `tws-bmdm` **funciona agora** (medido:
`getent hosts tws-bmdm` responde), então o defeito é **intermitente** e exige teste dirigido. Hipótese a
testar: fixar a resolução do broker (IP estático na mesh como no original, ou entrada explícita) e observar o
boundary seguinte.

Evidência: `data/evidence/lab-validation-2026-09-17-boundary-producao-16-09-reading.jsonl` (gate VÁLIDO).

## 5w. Frente RAG — índice denso reconstruído (cobertura 100%) e a fusão **medida de verdade**

**O pré-requisito que faltava.** O índice em uso (`data/indexes/corpus_bge_m3.pt`, 09-09) tinha 2427 entradas
e cobria A `105/139`, B `149/188` e **D `0/16`** — medir fusão com ele devolvia **nulo artefatural**. Sem
isso, "a união não ajuda" seria conclusão sobre o índice, não sobre o método.

**Reconstruído** com a receita **exata** do gerador original (texto `[:500]`, `max_length=128`, CLS
normalizado L2, fp16, batch 64, `bge-m3`): **6969 docs em 570,2 s**, matriz `(6969, 1024)` fp16 = 13,61 MB.
`scripts/build_dense_index_v2.py`. Cobertura nova: **343/343 = 100%** (A, B e D).

**A fusão, medida com o baseline do próprio harness** (controle embutido: se o baseline não reproduzir
`@1 183/262`, o script declara a medição inválida — foi o que faltou nos trials anteriores):

| variante | @1 | @3 | @5 | @10 | MRR |
|---|---|---|---|---|---|
| **baseline** (lexical) | **183/262** | 209 | 221 | 232 | **0,7576** |
| cobertura (união, ordem lexical) | 181/262 | 207 | 219 | 230 | 0,7510 |
| rrf (fusão por rank) | 149/262 | 196 | 212 | 233 | 0,6771 |

Por fatia (@1): A `97→97→57` · B `80→78→86` · D `6→6→6`. O RRF repete o padrão dos 4 trials anteriores —
**ganha sem âncora (+6) e destrói com âncora (−40)**.

**Por que (recall@50 por ramo):** D — lexical `10/16` (62,5%), **denso `15/16` (93,8%)**, união **`16/16`**;
total — lexical 83,5%, denso 83,8%, união **93,8%**.

**Veredito:** o ramo denso **acha** os documentos (a união leva o recall@50 a 93,8% e a fatia D a 100%), mas o
`@1` **não melhora**. O gargalo é a **ordenação**, não a geração de candidatos: o scorer lexical dá ~0 aos
documentos que só o denso trouxe e os afunda, e no RRF os documentos de D ficam em ranks densos > 20 e não
alcançam o top-20 final. **"Embeddings como cobertura" fica refutado nas fatias reais**; o alvo passa a ser o
**re-ranker**.

Evidência: `data/evidence/lab-validation-2026-09-17-dense-index-rebuild-and-fusion-measured.jsonl`.
Scripts: `scripts/build_dense_index_v2.py`, `check_index_coverage.py`, `measure_fusion_v3.py`,
`probe_recall_at_50.py`.

## 5x. Frente RAG — anatomia da ordenação: **o gargalo é desempate fino entre claims quase-duplicados**

Três medições, todas nas 262 perguntas do blind v3, com o pool da união ordenado pelo lexical.

**(1) Onde está o documento certo** — a falha é de **quase-acerto**, não de recuperação:

| fatia | rank 1 | 2-3 | 4-10 | 11-20 | 21-50 | fora |
|---|---|---|---|---|---|---|
| A | 84/107 (78,5%) | 8 | 9 | 2 | 4 | 0 |
| B | 78/140 (55,7%) | 15 | **24** | 3 | 12 | 8 |
| D | 5/15 (33,3%) | 2 | 2 | 0 | **6 (40%)** | 0 |

**58 perguntas** têm o documento certo em **rank 2–10**.

**(2) O score do top-1 serve de gate?** Dentro de A sim (acertou mediana 34,97 vs errou 14,93); em B quase
não (13,61 vs 11,75). A vs B+D: medianas 34,04 vs 12,81 — mas **as faixas se sobrepõem** (mínimo de A = 6,04;
máximo de B+D = 58,18). ⇒ **gate por limiar puro de score está DESCARTADO por medição.**

**(3) Ablação do re-ranker que já existe** (`second_stage_rerank`): sem ele `@1 169/262` (MRR 0,7146); com ele
`@1 183/262` (MRR 0,7577). **É ganho líquido de +14 — não remover.**

**(4) Flips de rank-1:** mantém 155 · **perde 14** (A 1, B 13, D 0) · **ganha 28** (A 14, B 13, D 1) ⇒
`28 − 14 = +14`, exatamente o delta da ablação (consistência conferida). **A regressão concentra-se em B.**

**(5) Quem ocupa o rank-1 nos quase-acertos** (n=49): `canonical_claim` **29 (59,2%)**, `message_catalog` 8,
`lab_evidence` 7, `ragflow_runbook_chunk` 5. Distribuição do rank do doc certo: **r2=13, r3=13**, r4=8, r5=4,
r6=2, r7=4, r8=2, r9=1, r10=2.

**Hipótese refutada por medição:** eu ia propor *reforçar claims sobre chunks de runbook* — em 59% dos
quase-acertos o rank-1 **já é** outro `canonical_claim`, e a massa está em **r2–r3 (26 de 49)**.

**Diagnóstico:** o scorer lexical **não discrimina entre claims quase-duplicados**. Não falta candidato, não é
tipo errado no topo — é **desempate fino entre documentos parecidos**.

**Teto oracle:** corrigir só os quase-acertos de rank 2–10 levaria o `@1` de 183 para **232/262 (88,5%)**, sem
nenhum candidato novo. É o tamanho do prêmio.

**Desenho que o dado indica** — re-ranker **desafiante**: o rank-1 só cai se um candidato de rank 2–10 o
superar **por margem**. Protege A (rank-1 certo em 78,5%, perde só 1) e ataca B (perde 13).

**Ressalva de rigor:** a fatia D tem **n=15** — diferenças de 1–2 nela são **ruído** e não sustentam conclusão
própria. O que vale em D é a estrutura (40% em rank 21–50), não a contagem.

Evidência: `data/evidence/lab-validation-2026-09-17-ordering-anatomy-and-second-stage-ablation.jsonl`.
Scripts: `scripts/diagnose_ordering.py`, `ablate_second_stage.py`, `diagnose_rank1_flips.py`.

## 5y. Frente RAG — o re-ranker **desafiante** dá ganho real, mas **dependente de regime**

**Desenho testado** (não precisa de modelo novo): o rank-1 de produção só cai se um candidato de rank 2–20 o
superar **por margem**, segundo o **score denso** do índice v2.

**Varredura da margem** (262 perguntas do blind v3) — existe ótimo, e o controle de sanidade fecha:

| margem | @1 total | A | B | D |
|---|---|---|---|---|
| 0,06 | 190/262 (72,5%) | 86/107 | 95/140 | 9/15 |
| 0,08 | 195/262 (74,4%) | 89/107 | 97/140 | 9/15 |
| **0,10** | **198/262 (75,6%)** | 90/107 | **98/140** | 10/15 |
| 0,12 | 197/262 (75,2%) | 93/107 | 96/140 | 8/15 |
| 0,30 | 182/262 (69,5%) | 96/107 | 80/140 | 6/15 |

Trade-off exatamente o projetado: **A cede 7, B ganha 18**. Com promoção ≈0 (0,30) volta a ≈baseline ⇒ sanidade OK.

**Validação held-out externa** (margem **fixada em 0,10 antes** de ver estes dados): `holdout_100_unseen`
89→**85** (−4) · `blind_holdout_50_vault` 49→**48** (−1) · `realistic_blind_holdout_30` 28→**27** (−1).
**−6 em 180 perguntas.**

**Ressalva de controle:** esses três têm baseline de **89%, 98% e 93%** — são **fáceis, sem headroom**; testam
"em conjunto fácil o desafiante atrapalha", **não** o regime de quase-acertos onde ele deveria ajudar.

**Validação cruzada dentro do regime difícil** (5 folds, 262): em **cada** fold a margem vencedora escolhida
**fora do fold** foi **0,10**, e o held-out deu **198/262** ⇒ o **+15 sobrevive à validação cruzada**; a escolha
da margem é **estável**, não ponto de sorte.

**Consolidado nas 442 perguntas:** baseline **349 (79,0%)** vs desafiante **358 (81,0%)** = **+9 (+2,0 pp)**.

**Veredito:** o mecanismo está **provado** e o ganho é **real e reprodutível no regime com quase-acertos** —
o primeiro mecanismo de *ordenação* desta série a dar ganho líquido com controle honesto. Mas é
**dependente de regime** e **NÃO está pronto para produção**: falta uma **guarda** que desligue o desafiante
quando o baseline está confiante. A guarda por limiar do score do top-1 está **refutada** (§5x). Candidatas a
testar: (a) o **gap** rank-1↔rank-2 (não o score absoluto); (b) limiar **absoluto** de similaridade densa do
desafiante; (c) aplicar só quando o rank-1 **não** for claim exato.

Evidência: `data/evidence/lab-validation-2026-09-17-challenger-reranker-sweep-heldout-crossval.jsonl`.
Scripts: `scripts/challenger_margin_sweep.py`, `validate_challenger_holdout.py`, `challenger_crossval.py`.

## 5z. Frente RAG — as três guardas de confiança **testadas e reprovadas**: desafiante **REJEITADO**

Sandbox/read-only. Margem do desafiante **fixada em 0,10 antes** de ver os holdouts. Limiares das guardas
varridos **no v3** e aplicados **sem alteração** aos 180 externos. Critério declarado de antemão: ganho no v3
**E** não-negativo nos 180.

**Métricas por conjunto** (`n_docs` lido nesta execução = **6987**; índice construído com 6969):

| conjunto | n | baseline | desafiante | delta | ganhou | perdeu |
|---|---|---|---|---|---|---|
| blind v3 | 262 | 183 (69,8%) | 198 (75,6%) | **+15** | 26 | 11 |
| holdout_100 | 100 | 89 (89,0%) | 85 (85,0%) | −4 | 1 | 5 |
| holdout_50 | 50 | 49 (98,0%) | 48 (96,0%) | −1 | 0 | 1 |
| realistic_30 | 30 | 28 (93,3%) | 27 (90,0%) | −1 | 0 | 1 |
| **TOTAL** | **442** | **349 (79,0%)** | **358 (81,0%)** | **+9** | | |

**Guardas testadas** (v3 / externos):

| guarda | v3 @1 | Δ | externos | Δ | passa? |
|---|---|---|---|---|---|
| (a) `gap<−1,14` | 184 | **+1** | 166 | **+0** | literalmente sim |
| (a) `gap<0,08` | 186 | +3 | 164 | −2 | não |
| (a) `gap<0,596` | 188 | +5 | 160 | −6 | não |
| (a) `gap<1,707` | 196 | +13 | 161 | −5 | não |
| (b) `denso>0,64` | 200 | +17 | 161 | −5 | não |
| (b) `denso>0,731` | 186 | +3 | 165 | −1 | não |
| (c1) rank-1 não-claim | 190 | +7 | 165 | −1 | não |
| (c2) sem âncora exata | 200 | +17 | 162 | −4 | não |

**Por que o único "aprovado" não vale:** `gap<−1,14` dispara em **27/262**, muda **uma** pergunta
(**+0,38 pp** ≈ **0,13 erro-padrão** = ruído) e nos externos é **inerte** — 16 aplicações, **0 ganhos e
0 perdas**: o "+0" não é segurança, é **ausência de ação**. Além disso é **condição degenerada** (rank-2 com
score lexical *maior* que o rank-1 — ocorre em 47/262 e 25/180).

**Causa do fracasso (medida):** a **precisão do desafiante não transfere**. Quando dispara, acerta
**26/37 = 70,3%** no v3 e **1/8 = 12,5%** nos externos. E **nenhuma das três guardas prediz essa diferença**:
o mesmo regime de score denso tem precisão oposta — `denso>0,64` aplica 50 vezes no v3 (24 ganhos / 7 perdas)
e 13 nos externos (1 ganho / 6 perdas).

**DECISÃO: o re-ranker desafiante fica REJEITADO para produção.** Nenhuma alteração em
`data/eval/evaluate_rag_benchmark.py`; nenhuma mutação no lab.

**Lições registradas.**
1. **Critério binário pode ser satisfeito por ruído.** "Ganho no v3 E não-negativo nos externos" passou com
   **uma** pergunta. Critério correto: o efeito tem de **exceder o erro-padrão** *e* a guarda tem de
   **realmente atuar** no conjunto de validação (aplicações que não mudam nada não são evidência).
2. **`n_docs` não é invariante e o índice denso envelhece.** Nesta sessão o corpus foi de **6969 → 6987**
   (cada evidência gravada em `data/evidence/lab-validation-*.jsonl` **entra no glob indexado**). Reconstruir
   o índice após mudança material do corpus é **pré-requisito** de qualquer medição densa.

Evidência: `data/evidence/lab-validation-2026-09-17-challenger-guards-tested-and-rejected.jsonl`.
Script: `scripts/guard_probe.py` (+ `data/eval/guard_probe_records.json`).

## 5aa. Frente RAG / Opção B — anatomia dos quase-acertos e o **IDF** como única alavanca viva

Read-only. Sem fine-tuning (dataset de produto só para indexação/avaliação). Sem mutação no lab.

**O diagnóstico dos 49 quase-acertos separa DOIS problemas:**

| causa | n | % |
|---|---|---|
| **defeito de ordenação** — o scorer já tinha o certo em 1º e o `second_stage_rerank` inverteu | **19** | 39% |
| **erro real do scorer** — o rank-1 errado tem score maior | **30** | 61% |

Mecanismo do defeito: os boosts do `second_stage_rerank` são **absolutos e enormes** (`+32` termo-no-id,
`+45/+55` código-no-id, `+35` par-CLI, `+15/+20` trigram) contra base BM25 de ~5–20. Caso medido:
`message_catalog` com **34,673** recebeu **+45** pelo código no id → passou um chunk correto de **77,824**.

Nos 30 erros reais o padrão é **claim quase-duplicada** (`canonical_claim>canonical_claim` 11×,
`message_catalog>message_catalog` 5×) e o doc certo é o **mais longo em 17/30** (a penalidade de comprimento
morde o documento mais rico). O doc certo casa **110 termos exclusivos** (df mediano 164, 28 raros) contra
**40** do lado errado — **tem mais evidência textual e perde mesmo assim**.

`avg_dl` real = **58,33** (mediana 47, máx 447) vs **60 hardcoded** ⇒ normalização de comprimento **não é alavanca**.

**Experimento 1** (controle embutido: base chama as funções de produção e reproduz 183/262 e 166/180):

| variante | v3 | externos |
|---|---|---|
| base | 183 | 166 |
| boosts ×0,5 | 183 | 164 |
| boosts ×0,25 | 183 | 162 |
| boosts ×0,1 | 181 | 157 |
| boosts ×0,0 | 179 | 146 |
| **IDF** | **189** | **167** |
| IDF + boosts ×0,25 | 193 | 163 |

**Hipótese refutada:** reduzir os boosts **piora**. Os boosts enormes são **ganho líquido** e as 19 demissões
estão **entrelaçadas** com os ganhos (o second stage ganha 28 rank-1 e perde 14) — não dá para separar escalonando.

**O IDF é a única alavanca viva.** O scorer **não tem IDF**: termo em todos os 6969 docs pesa igual a termo em
um. Adicionar o fator clássico `ln((N−df+0,5)/(df+0,5)+1)`:

| conjunto | base | IDF | Δ |
|---|---|---|---|
| blind v3 | 183 | **189** | **+6** |
| holdout_100 | 89 | 89 | 0 |
| blind_holdout_50 | 49 | 49 | 0 |
| realistic_30 | 28 | **29** | +1 |

Por fatia (v3): **A 97→95 (−2) · B 80→87 (+7) · D 6→7 (+1)**.

**Vantagem metodológica decisiva:** o IDF **não tem parâmetro livre** — é a fórmula clássica aplicada direto,
então **não há ajuste no conjunto de teste a temer**, ao contrário do desafiante (margem escolhida no v3) e
das guardas. É a primeira variante que **melhora o v3 sem regredir em nenhum externo**.

**Mas não é resultado fechado:** McNemar no v3 ganhou 13 / perdeu 7, **p = 0,2632**; bootstrap pareado
(10.000) **+6,03 com IC95% [−3, +15]** — **o IC inclui zero**. ≈0,81 erro-padrão. **Promissor, não conclusivo.**
Não promover a produção antes de ampliar a amostra.

**Lições.**
1. **O controle embutido pegou um bug meu:** a 1ª versão do scorer de teste omitia o `FAMILY_BOOST` do
   `message_catalog` e dava base **178** em vez de **183** — sem o controle, todo o sweep seria reportado com
   base errada.
2. **Critério binário não basta:** um ganho pode satisfazer "melhora no v3 e não regride fora" e ainda ser
   ruído (p=0,26, IC incluindo zero). Exige-se o **intervalo**, não só o sinal.
3. **`n_docs` não é invariante:** 6969 quando o índice foi construído, **6993** nesta execução — cada evidência
   gravada em `data/evidence/lab-validation-*.jsonl` **entra no glob indexado**.

Evidência: `data/evidence/lab-validation-2026-09-17-nearmiss-diagnosis-and-lexical-enrichment-exp1.jsonl`.
Scripts: `scripts/diagnose_nearmiss_terms.py`, `lexical_enrichment_exp1.py`, `validate_idf_gain.py`.

### 5aa.1 O teste pedido pelo dono — a amostra ampliada **não** decide (e a contagem bruta mentiu)

Rodado base vs IDF em **toda a suite** (15 benchmarks, 819 linhas):

| medição | n | base | IDF | Δ | McNemar | p |
|---|---|---|---|---|---|---|
| suite **bruta** | 819 | 579 (70,7%) | 594 (72,5%) | +15 (+1,8 pp) | 36/21 | 0,0627 |
| suite **deduplicada** | **517** | 380 (73,5%) | 386 (74,7%) | **+6 (+1,2 pp)** | 18/12 | **0,3616** |
| blind v3 (onde nasceu) | 262 | 183 | 189 | +6 (+2,3 pp) | 13/7 | 0,2632 |

**A checagem de integridade invalidou o número bruto:** 270 dos 819 itens são **perguntas de texto repetido**
entre conjuntos (302 linhas extras) e **267 dos 270 grupos repetidos têm desfecho idêntico** — são
**duplicatas reais**, não itens distintos. A suite tem **517 perguntas únicas**. O `+15` com p=0,063 era
**artefato de contagem dupla**; o honesto é **+6, p=0,36**.

**IC95%:** simples `[+0, +30]` (limite inferior exatamente 0) · estratificado `[-1, +32]` (inclui 0).

**Por conjunto:** os **fáceis dão zero** (100%→100%, 98%→98%, 95%→95%, 89%→89%) — não há teto para ganhar;
os **difíceis dão o ganho** (v3 +6, virgin_expanded +3, virgin +3, virgin_en +3, golden_qa +1, fresh +1,
realistic +1, slice_d +1), com **uma exceção**: `holdout_40_test` **−4** (1 ganho / 5 perdidos, **p=1,0** —
indistinguível de ruído com n=40). Consistência: **8 positivos, 6 neutros, 1 negativo**.

**Quanto faltaria:** com a taxa honesta de ganho nas discordâncias (18/30 = 0,600) e taxa de discordância de
0,058, seriam necessárias **~101 discordâncias ≈ 1741 perguntas únicas** para p<0,05 — **3,4× a suite atual**.

**Veredito: o IDF permanece NEM CONFIRMADO NEM REFUTADO.** Direcionalmente positivo, nunca regride de forma
material, mas o efeito (+1,2 pp) está **abaixo do que 517 perguntas resolvem**. O teste pedido **não** mudou o
status — ao contrário do que a leitura bruta de 819 sugeria. **Não promover.**

**Lições.**
1. **Contar perguntas não é contar itens.** A suite parecia ter 819; 267 grupos são duplicatas reais. Sem a
   dedup eu teria reportado "**+15, p=0,063, a 14 perguntas de decidir**" — **falso por contagem dupla**.
   Regra: antes de calcular poder sobre suite agregada, deduplicar por texto **e** verificar se os grupos
   repetidos têm o mesmo desfecho (se tiverem → duplicata; se não → itens correlacionados, e o IC correto é o
   **estratificado**).
2. **Conjuntos fáceis diluem.** Baseline ≥89% dá zero por construção (sem teto): incluí-los aumenta o `n` sem
   aumentar o poder. Ganho de ordenação mede-se nos **difíceis** (baseline<85%): ali o IDF dá **+14/549
   (2,6 pp, p=0,076)**.
3. **Testar um ganho pequeno é caro.** +1,2 pp com ~6% de discordância exige ~1741 itens. A decisão econômica
   ("vale mudar o scorer por 1,2–2,6 pp?") pode ser tomada **antes** da significância, sem fingir que se obteve.

4. **Falso positivo do scanner de segredo ≠ segredo.** O `publish.sh` **abortou** o publish porque a string
   `10.2.8` seguida de `.00` casou o padrão de IPv4 — mas é a **versão do produto** ("HWA 10.2.8"), texto **já versionado**
   em `data/eval/blind_v3_slices.jsonl` e `data/evidence/claims.jsonl`. O script é **fail-closed por projeto**
   (as únicas isenções são o bloco `publish-patterns` e as fixtures do auto-teste): **não existe allowlist para
   arquivo legítimo, e a saída não é burlar o scanner.** A causa foi minha: o registro por pergunta guardava o
   **texto** da pergunta (campo `q`) — redundante, pois os benchmarks já o têm. Trocado pelo **índice** dentro
   do conjunto (campo `i`), seguindo a convenção de `idf_validation_perquestion.json` e
   `challenger_cv_perquestion.json`. **Medições idênticas antes e depois** (579/819 e 594/819).
   **Regra:** registros derivados **não** duplicam texto de entrada — guardar índice/referência, não conteúdo.

Evidência: `data/evidence/lab-validation-2026-09-17-idf-full-suite-test-inconclusive.jsonl`
(`result: PARTIAL`). Script: `scripts/idf_full_suite.py` (+ `data/eval/idf_suite_perquestion.json`).

## 5ab. Frente RAG — Fases 1 e 2 da ordenação: o defeito está localizado e não é consertável; o sinal semântico existe e a rota é o bloqueio

**Fase 1 — atribuição por componente (`scripts/attribute_ordering_flips.py`).** Controle **duplo**:
a ordenação instrumentada reproduz 183/262 **e** o score instrumentado de cada documento é idêntico ao de
produção (`max|diff| = 2,8e-14`). Dos 49 quase-acertos, **19 foram demotados** pelo 2º estágio e 30 são erro
real do scorer. Nos 19, o componente que dá a margem ao documento **errado** é **`ss_entidade_id` em 16/19
(84%)** — e em **14/19 o certo levou ZERO**. No conjunto **inteiro** dos 49, ele é o componente que favorece
o errado em **30/49 (61%)**: ou seja, além dos 16 demotados, ele também empurra o documento errado em **14
dos 30** casos que eu classifiquei como "erro real do scorer" — o dano é maior que o da demissão sozinha.
Delta médio `+37,6` (soma `+1204`, n=32). Dois defeitos de desenho: o boost **acumula sem teto** (medido
`+64` e `+102` sobre uma base de ordem 5–20) e **chaveia no ID**, que é artefato de nomenclatura
(`message_catalog` tem o código AWS no ID por construção).

**Fase 1b — o conserto NÃO existe (`scripts/entity_boost_fix_sweep.py`).** Controle `copy_asis` == produção
(183/262, 166/180):

| variante | v3 | externos | delta |
|---|---|---|---|
| base / copy_asis | 183 | 166 | — |
| `ent_cap1` (teto de 1 aplicação) | 183 | 165 | +0 / −1 |
| `ent_codes_only` (remove o genérico) | 186 | 159 | **+3 / −7** |
| `ent_off` (remove o bloco) | 185 | 154 | **+2 / −12** |
| `ent_cap_all` | 183 | 165 | +0 / −1 |

**Nenhuma passa.** As 16 demissões são o **preço** do +12,2 que o 2º estágio ganha nas perguntas com âncora —
trade estrutural, não bug. *Ressalva declarada: os externos são ricos em âncora, então o critério favorece
estruturalmente manter o boost.*

**Fase 2 — cross-encoder LARGE na GPU (`scripts/crossencoder_large_trial.py`, `scripts/crossencoder_route_eval.py`).**
O que faltava em 14.09 agora existe: `sentence-transformers 6.0.1` + `torch 2.5.1+cu121` + **`bge-reranker-large`
(2,2 GB) já em disco**. Controles: 183/262, 89/100, 49/50, 28/30 — todos batendo.

| rota | v3 | A | B | D | externos |
|---|---|---|---|---|---|
| baseline | 183 | 97 | 80 | 6 | 166 |
| CE puro (top-20) | 173 | — | — | — | — |
| CE puro (top-50) | 167 | 69 | **93** | 5 | 147 |
| híbrido pelo **campo `has_anchor`** | **197** | 97 | **97** | 3 | — |
| híbrido pelo **proxy (regex)** | 184 | — | — | — | **153** |

**Achado:** na fatia B o CE **large** leva **80 → 93 (+13)** — o modelo **médio** de 14.09 capturava só +3,6.
"Modelo médio falhou" **não era** "o método falhou"; valeu reabrir com o modelo maior já em disco.

**O bloqueio é a ROTA.** Com o campo `has_anchor` (rótulo do benchmark) o híbrido dá **197/262 (+14)** com A
**intacta** e B **+17**. Mas o proxy derivável acerta só **176/262 = 67,2%** (44 falso-âncora, 42 falso-não-âncora)
e o ganho **desaparece**: v3 +1 e externos **−13**. Usar o campo `has_anchor` em produção seria **usar o gabarito**.

**Próximo passo (não é "outro modelo"):** um **roteador confiável** — ou trocar a rota dura por um **blend de
scores** baseline+CE, que **elimina o roteador**. Vazamento medido: 15/262, 25/100, 17/50, 0/30.

**Evidência a favor do blend (sinal abaixo do rank 1).** Mesmo com o proxy **quebrado** (67%), o híbrido
melhora **@3 (79,8% → 81,3%)** e **MRR (0,7577 → 0,7668)** no v3 com o **@1 em paridade (183)**. Isto é, o
cross-encoder agrega sinal de ordenação **abaixo do rank 1** que a rota dura desperdiça — precisamente o que
um blend de scores aproveita **sem roteador**. É o argumento medido para atacar o blend em vez de melhorar o
classificador.

**Mas o blend foi TESTADO e REJEITADO — nos dois desenhos (§5ac).** O argumento acima estava incompleto.

## 5ac — O BLEND baseline×CE foi testado e REJEITADO (os dois desenhos)

**Desenho 1 — CE no LUGAR do 2º estágio** (`scripts/blend_base_ce.py`). Defeito **meu**, encontrado pelo
próprio controle: o script blendeou o CE com o score **pré-2ª-etapa**, ou seja, **substituiu** o 2º estágio.
O controle `alpha=0` reproduziu **169/262 e 141/180** (1º estágio), **não** a produção (183/166). Como o 2º
estágio vale **+14 no v3 e +25 nos externos**, o teste começava 25 pontos atrás. Nenhum alpha passa.

**Desenho 2 — CE SOMADO ao 2º estágio** (`scripts/blend_on_top_of_stage2.py`), que é o correto:
`final = (1−λ)·minmax(score_2ª_etapa) + λ·minmax(score_CE)`. **Controle `λ=0` reproduz a produção
EXATAMENTE (183/262, 166/180).**

```
  lam=0.0  v3 183 (+0)   externos 166 (+0)    <- controle
  lam=0.1  v3 179 (-4)   externos 162 (-4)
  lam=0.3  v3 179 (-4)   externos 159 (-7)
  lam=0.5  v3 185 (+2)   externos 156 (-10)
  lam=0.6  v3 186 (+3)   externos 156 (-10)   <- melhor v3, custa 10 externos
  lam=1.0  v3 173 (-10)  externos 146 (-20)
  -> NENHUM lambda passa
```

O `+3` no v3 é **nível-ruído**: o SE do @1 com n=262 e p≈0,70 é √(0,7·0,3/262) = 0,0283 → **~7,4 pontos**.

**Leitura (a parte que importa).** O blend **não elimina o roteador — ele HERDA o problema do roteador**.
A utilidade do CE é **dependente da fatia**: ganha +13 onde o baseline é fraco (B, sem âncora) e perde −28
onde é forte (A, com âncora). **Não existe peso global que separe os dois regimes** — é o mesmo muro da rota
dura, apenas redistribuído: trocar rota por blend não elimina a necessidade de decidir **por pergunta**,
apenas esconde a decisão dentro de um escalar que não pode estar certo nos dois regimes ao mesmo tempo.

**O que isto NÃO refuta:** o **sinal** do CE existe e é grande (B 80→97, **+17**, com rota perfeita). O que
está refutado é a hipótese de explorá-lo **sem uma decisão por pergunta confiável**.

**Em aberto (honesto):** (1) o ganho do CE só foi medido com rota **perfeita** no v3 — e `has_anchor` é
**rótulo de benchmark**; nos externos não existe rota perfeita medida, só o proxy de **67,2%** (44
falsos-âncora, 42 falsos-não-âncora); logo "o CE ajuda" está demonstrado **apenas no v3**. (2) O roteador
confiável segue **não resolvido**. (3) A regra do dono proíbe **treino** sobre datasets de produto, mas
classificação **zero-shot** por LLM é **inferência** — via não testada.

Evidência: `data/evidence/lab-validation-2026-09-17-blend-base-ce-rejected-both-designs.jsonl`
(`result: REJECTED`). Scripts: `scripts/blend_base_ce.py`, `scripts/blend_on_top_of_stage2.py`.
Scores crus do CE salvos em `hermes/neural-reranker/ce_scores_top20.json` (evita re-inferência).

## 5ad — O ROTEADOR: LLM e regex deployável, ambos REJEITADOS

**Achado prévio que muda o problema.** O campo `has_anchor` **é a própria fatia** (A=True 107/107,
B/D=False 155/155 — correlação perfeita). Não é "contém um código", é o rótulo da partição. Meu proxy
original procurava a coisa errada: incluía **nomes de comando** (`composer`, `conman`, `planman`, `helm`,
`kubernetes`) como "âncora" — mas os comandos aparecem justamente nas perguntas **B**. Isso explica os 44
falsos-âncora e os 67,2%.

**Bug de formato meu, confundido com falta de sinal.** Eu exigia `AWS`+3 letras+3 dígitos+letra, mas os
códigos AWSUI são `AWS`+2 letras+**4** dígitos+letra (`AWSUI0286E`). Corrigir o formato levou o detector de
**67,2% → 79,8% sem nenhum LLM**.

**Detectores medidos no v3** (contra o campo):

```
sempre-nao                       59,2%
proxy original (comandos)        67,2%   prec A 59,6%  rec 60,7%
E1 codigos (formato corrigido)   79,8%   prec A 100%   rec 50,5%   fp=0
E2 + secoes/views                83,6%   prec A 100%   rec 59,8%   fp=0
E3 + REST API V2                 85,1%   prec A 100%   rec 63,6%   fp=0  fn=39   <- MELHOR
T1 prefixos de template          63,7%   prec A  64,3% rec 25,2%   <- TAUTOLOGICO, recusado
LLM gemini-3.8-flash-none        63,3%   prec A  61,8% rec 70,0%   tp=21 fp=13 fn=9 tn=17
```

**O LLM foi pior que um regex trivial** (63,3% vs 80,2%) e apenas 4 pontos acima de "sempre não". Sugere
que A/B **não é uma distinção semântica que o modelo leia da pergunta** — provavelmente porque a partição
foi construída pelo autor do benchmark, não por uma propriedade do texto. Custo: 54.517 tokens em 60
chamadas → **401.609 tokens projetados** para 442, para um resultado pior.

**Recusei o detector tautológico.** Prefixos como *"Como solucionar ou diagnosticar a mensagem de erro"*
separam A de B a 63,7%, mas são o **template de geração do benchmark**, não propriedade da pergunta. Um
roteador baseado neles não funcionaria com pergunta real e inflaria a métrica. Reportado separado.

**A rota E3, medida** (controle 1 OK — baseline reconstruído == produção, 183/262 e 166/180):

```
  v3    baseline 183   CE 173   ROTA-E3 188 (+5)   | 68 p/ baseline, 194 p/ CE
  h100  baseline  89   CE  76   ROTA-E3  79 (-10)  | 32 p/ baseline,  68 p/ CE
  h50   baseline  49   CE  44   ROTA-E3  44 ( -5)  | 10 p/ baseline,  40 p/ CE
  r30   baseline  28   CE  26   ROTA-E3  27 ( -1)  | 11 p/ baseline,  19 p/ CE
  -> v3 +5 mas EXTERNOS 166 -> 150 (-16)  =>  NAO PASSA
```

**O muro real, agora com nome: a partição A/B do v3 NÃO descreve os externos.** O E3 roteia 68/262 para o
baseline no v3, mas só **32/100 no h100 e 10/50 no h50** — e esses conjuntos têm baseline de **89%** e
**98%**, ou seja, **comportam-se como A**. O detector não os vê, manda-os para o CE, e o CE os destrói.
**Um roteador calibrado no v3 não generaliza.**

**Ressalva declarada:** o controle de **alinhamento** falhou em **3 de 442** perguntas (o corpus cresce a
cada evidência gravada, mudando o top-20 entre a construção do cache e a reconstrução). O controle 1 passou
exato, então a medição é válida em geral, mas o `+5` do v3 carrega incerteza de **até 3 pontos**.

Evidência: `data/evidence/lab-validation-2026-09-17-llm-router-and-regex-router-both-rejected.jsonl`
(`result: REJECTED`). Scripts: `scripts/llm_router_pilot.py`, `scripts/router_e3_deployable.py`.
Caches ficaram em `hermes/neural-reranker/` (fora do repo, **não em `/tmp`** como em 14.09, cujo footprint
foi removido e custou ~300 s de reconstrução).

Evidências: `…ordering-attribution-and-entity-boost-fix-rejected.jsonl` (`result: REJECTED`) e
`…crossencoder-large-signal-exists-router-is-blocker.jsonl` (`result: PARTIAL`).

