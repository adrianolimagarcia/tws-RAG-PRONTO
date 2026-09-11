# Runbook — Stuck Production Plan (AWSJPL017E) — HWA 10.2.8

> Objetivo: diagnosticar e recuperar um plano de producao preso no HCL Workload Automation 10.2.8 (Distributed), inclusive quando a causa raiz e o aborto do SwitchPlan no Dynamic Workload Broker.
> Ambiente de validacao: laboratorio containerizado (MDM + Backup MDM + FTA/DA + broker). Mensagens citadas sao saida real de conman/planman.

## Sinais de alarme (sintomas)

| Sintoma | Comando de verificacao | Resultado esperado num plano SAUDÁVEL |
|---|---|---|
| `planman ext`/`crt` falha | `planman ext -days 1` | **AWSJPL017E** 'The production plan cannot be created because a previous action on the production plan did not complete successfully' |
| Horizonte zerado | `planman showinfo` | `Production plan end time: (same as the start time of the last extension - created/extended with -for 0000)` e `time extension: 00:00` |
| Run number disparando | `planman showinfo` | Run number avanca varias vezes sem controle (ex.: 31 -> 33 -> 37) |
| Batchman abaixo | `conman status` | `Batchman down` |
| No nao autorizado a planificar | `planman ext` | **AWSJPL004E** 'this_cpu "X" does not match the workstation name of the master domain manager in the database' |

## Diagnostico (raiz)

> **CORRECAO (2026-09-11)**: a causa real de `AWSJPL017E` NAO e o broker. Ver evidencias `hwa-lab-10.2.8-awsjpl017e-real-root-cause-pending-symnew-0015`.

1. Verifique o estado do plano: `planman showinfo`.
2. **Causa real de `AWSJPL017E`**: o planner recusa uma segunda operacao de plano enquanto uma anterior esta PENDENTE. `planman ext`/`crt` cria um **Symnew pendente** (nao ativado); um segundo `ext`/`crt` SEM `SwitchPlan` entre eles retorna `AWSJPL017E`. Determinismo provado: `ext -> ext` = AWSJPL017E; `ext -> SwitchPlan -> ext` = OK.
3. **Gatilho tipico**: um `JnextPlan` interrompido no meio (ex.: SIGKILL dos containers) deixa um Symnew pendente, bloqueando operacoes seguintes ate `planman unlock` ou um novo ciclo completo.
4. **O broker NAO e a causa**: os erros `AWSBHU159E`/`AWSBHU076E`/`AWSBCT041I` durante o `SwitchPlan` sao NAO-FATAIS (ruido) — o SwitchPlan stock completa com rc=0 e nao seta o flag.
5. Se o erro for `AWSJPL004E`, o `planman` esta sendo executado de um no cujo `thiscpu` (localopts) nao corresponde ao domain manager gravado no **MODELO** (objeto DOMAIN no banco). Execute a recuperacao a partir do no que o modelo indica (com `composer display domain=@`).

## Recuperacao

### Correcao imediata (primeiro sempre tentar isto)
```bash
planman unlock        # AWSJPL504I - libera lock orfao e limpa o flag 'did not complete'
planman ext -days N   # AWSJCL062I - volta a funcionar IMEDIATAMENTE
```
> `planman unlock` sozinho resolve `AWSJPL017E` na grande maioria dos casos, pois ele **nao indica corrupcao do Symphony**, apenas fluxo interrompido com lock orfao.

### Restaurar o batchman (se ficou down)
```bash
conman "link <broker>"        # se o broker foi desvinculado durante o diagnostico (opcional)
conman "start&link @!/@/@;noask"   # AWSBHU507I - sobe netman/batchman
conman status                 # Batchman LIVES
```

### Recuperacao pesada (so quando o horizonte esta realmente destruido)
```bash
planman unlock                # libera o lock
planman reset                 # reset do preproduction plan, mantem o corrente (awsjcl064i/awsjcl065i)
planman crt -days 3           # AWSJCL058I 'The production plan (Symnew) has been successfully created'
# trocar o Symnew pelo plano ativo:
#  - MDM:  /opt/hwa/TWS/SwitchPlan
#  - BMDM: /opt/hwa/TWS/TWS/SwitchPlan
planman ext -days N           # AWSJCL062I - confirma horizonte restaurado
```
> Execute pelo no que o **modelo** considera domain manager; em no divergente, pare em `AWSJPL004E` antes de avançar.

## Correcao definitiva (o que realmente resolve)

- **`AWSJPL017E`**: nao ha 'correcao de script' necessaria — e o comportamento correto do planner. A prevencao e **nao sobrepor operacoes de plano**: entre um `ext`/`crt` e o proximo, execute `SwitchPlan` (ou um `JnextPlan` completo). Se o flag ja estiver setado, `planman unlock` limpa.
- **Broker (MDM_DWB)**: os erros `AWSBHU159E`/`AWSBHU076E`/`AWSBCT041I` no `SwitchPlan` sao ruido NAO-FATAL (o script completa rc=0). Nao ha necessidade de patchar o SwitchPlan nem desabilitar o broker. O broker nao aceita `conman stop/start` por design (AWSBHU159E documentado); isso nao afeta a virada de plano.
- **`AWSJPL004E`**: execute as operacoes de plano a partir do no que o MODELO do banco considera domain manager (`composer display domain=@`).

## Reversao / Rollback
- `planman reset` mantem o plano corrente (nao destrutivo do plano ativo; so recalcula o preproduction).
- `planman crt`/`SwitchPlan` trocam o Symphony; o arquivo anterior fica preservado como `Sym...` em `$UNISONHOME`/TWSDATA ate o proximo ciclo.
- Antes de qualquer `crt`/`SwitchPlan`, garantir batchman com `planman unlock` + plano em estado limpo.

## Referencias
- Evidencias: `lab-validation-2026-09-10-stuck-plan-rootcause-switchplan-dwb.jsonl`, `lab-validation-2026-09-10-optman-users-calendar-planincident.jsonl`, `lab-validation-2026-09-10-switchplan-broker-rootcause-closed.jsonl`.
- Mensagens: AWSJPL017E, AWSJPL004E, AWSBHU159E, AWSBHU076E, AWSBCT041I, AWSJPL504I, AWSJCL058I, AWSJCL062I, AWSJCL064I, AWSBHU507I.