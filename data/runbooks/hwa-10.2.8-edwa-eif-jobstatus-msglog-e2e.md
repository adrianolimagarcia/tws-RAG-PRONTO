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
