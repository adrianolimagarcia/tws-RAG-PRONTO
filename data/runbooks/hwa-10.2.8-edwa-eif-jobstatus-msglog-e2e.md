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

- **Submissão on-demand (`sbs`) NÃO gera o evento.** Testado V1 (`sbs LABPOOL#POOL_STREAM`):
  o job concluiu SUCC mas o trace MONMAN teve **0** `Sending EIF Event` e o `messages.log`
  **não** recebeu novo `AWSEVP001I`. O cfg do monitor não tem filtro de `schedtime`, logo o
  gap é **comportamento de seleção do monitor** (reporta a ocorrência agendada), não filtro de regra.
- **`LogEvents=NO`** no `monmaneif.conf` → não há log de recepção no listener; a prova de
  recepção é o `AWSEVP001I` do motor de regras.
- **TZ:** o container do bmdm roda em **UTC**; o `messages.log` marca GMT real.

---

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
