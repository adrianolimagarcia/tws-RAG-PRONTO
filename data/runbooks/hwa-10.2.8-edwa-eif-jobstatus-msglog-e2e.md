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
