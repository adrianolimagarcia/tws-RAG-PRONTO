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

1. Verifique o estado do plano: `planman showinfo`.
2. Se o plano tem horizonte zerado e o `ext` retorna `AWSJPL017E`, mire na ultima operacao de troca de plano que nao completou.
3. Em ambiente com Dynamic Workload Broker (workstation do tipo `broker agent`, ex.: MDM_DWB):
   - O broker **nao aceita** `conman stop/start`: `conman stop <broker>` -> **AWSBHU159E** 'workstation is broker agent, where the command is not supported'.
   - O script **SwitchPlan** para TODAS as workstations do dominio e aborta ao emitir `stop <broker>`: `CONMAN:AWSBHU076E ... stop MDM_DWB for AWSBCT041I Service 2008 started on MDM_DWB`.
   - O `unlink` do broker **nao evita** o aborto (o `stop` e emitido independente do link).
   - Com o aborto: flag 'previous action did not complete' + batchman down -> `AWSJPL017E`.
4. Se o erro for `AWSJPL004E`, o `planman` esta sendo executado de um no cujo `thiscpu` (localopts) nao corresponde ao domain manager gravado no **MODELO** (objeto DOMAIN no banco). Execute a recuperacao a partir do no que o modelo indica (com `composer display domain=@`).

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

## Correcao definitiva do broker (decisao do dono)

O aborto do SwitchPlan no broker-agent so e evitado com uma destas acoes:
- **(a)** ajustar o `SwitchPlan`/`PostSwitchPlan` para pular workstations do tipo broker agent no comando `stop`;
- **(b)** remover/substituir a workstation do broker do domino (mais invasivo);
- **(c)** desabilitar o broker no laboratorio (perde cobertura dos testes de pool dinamico?LABPOOL/MDMDA).
> Recomendacao quando o broker for necessario: aplicar (a), preservando o pool dinamico; usar (c) apenas como fallback se o pool dinamico nao for mais objeto de teste do dataset.

## Reversao / Rollback
- `planman reset` mantem o plano corrente (nao destrutivo do plano ativo; so recalcula o preproduction).
- `planman crt`/`SwitchPlan` trocam o Symphony; o arquivo anterior fica preservado como `Sym...` em `$UNISONHOME`/TWSDATA ate o proximo ciclo.
- Antes de qualquer `crt`/`SwitchPlan`, garantir batchman com `planman unlock` + plano em estado limpo.

## Referencias
- Evidencias: `lab-validation-2026-09-10-stuck-plan-rootcause-switchplan-dwb.jsonl`, `lab-validation-2026-09-10-optman-users-calendar-planincident.jsonl`, `lab-validation-2026-09-10-switchplan-broker-rootcause-closed.jsonl`.
- Mensagens: AWSJPL017E, AWSJPL004E, AWSBHU159E, AWSBHU076E, AWSBCT041I, AWSJPL504I, AWSJCL058I, AWSJCL062I, AWSJCL064I, AWSBHU507I.