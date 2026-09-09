# Runbook: Recuperação da Esteira FINAL (Sfinal) e Erro AWSBHV082E sem MakePlan Manual

## Objetivo
Desbloquear o ciclo de virada diária do HCL Workload Automation (HWA 10.2.8) quando o job stream `FINAL` (ou `Sfinal`) ancorado em workstation estendida (`MDMXA`) entra em estado `STUCK` ou `HOLD`, com falha de `SWITCHPLAN` pelo erro `AWSBHV082E` (mesmo run number entre Symphony e Symnew), **sem executar MakePlan manualmente** e preservando a integridade transacional do plano de produção.

---

## 1. Regras de Ouro Operacionais
1. **NUNCA execute `MakePlan` manualmente no shell**: o `MakePlan` deve ser orquestrado estritamente pelo Batchman via stream `FINAL`. Execuções manuais criam arquivos `Symnew` fora de sincronia com a base relacional.
2. **NUNCA utilize `ResetPlan -scratch` como primeira alternativa**: a limpeza de rascunho descarta o preproduction plan e apaga histórico de instâncias agendadas.
3. **Auditar a saúde do banco relacional com `optman ls` antes de qualquer ação**: se o banco ou o Liberty estiverem instáveis, o plano não deve ser alterado.
4. **Verificar onde o stream está ancorado**: em instalações com Extended Agent (`unixlocl`), a esteira pode estar registrada em `MDMXA#FINAL` e não em `MDM#FINAL`.

---

## 2. Sintomas e Diagnóstico

### Sintoma 1: Stream em Estado STUCK no conman
```
%ss @#@
Workstation      Job Stream       SchedTime   State Pr Start  Elapse   #  OK Lim
MDMXA           #FINAL            2359 09/08  STUCK 10 02:32   00:00   3   1
MDMXA           #FINALPOSTREPORTS 2359 09/08  HOLD  10(09/08)  00:00   3   0
MDMXA           #FINAL            2359 09/09  HOLD  10(23:59)  00:00   3   0  [Carry]; MDMXA#FINAL(2359 09/08/26).SWITCHPLAN
```

### Sintoma 2: Erro no joblog do SwitchPlan (`AWSBHV082E`)
Ao inspecionar o log do job `SWITCHPLAN` em `/opt/hwa/TWSDATA/stdlist/<data>/O<jobnum>.<time>`:
```
14:29:01/STAGEMAN:AWSBHV082E The previous Symphony file and the Symnew
14:29:01/STAGEMAN:file have the same run number. They cannot be merged to
14:29:01/STAGEMAN:form the new Symphony file.
AWSBIS308I End of job
= Exit Status : 1
```

### Passo de Diagnóstico 1: Checar Saúde do Banco
Execute como usuário `wauser`:
```bash
optman ls
```
*Critério de Sucesso*: Retornar a lista de opções e concluir com `AWSJCL050I Command "ls" completed successfully.`

### Passo de Diagnóstico 2: Verificar Consistência do Plano (`planman showinfo`)
Execute como usuário `wauser`:
```bash
planman showinfo
```
Verifique os campos:
- `Production plan start time of last extension`
- `Run number`
- `Confirm run number`

**Diagnóstico da Condição**: Se `Run number == Confirm run number` (ex: 29 e 29) e a data de extensão já cobrir o dia atual, significa que **o plano já foi estendido com sucesso no passado**. A tentativa de rodar o `SWITCHPLAN` do dia anterior é redundante e falha porque o `stageman` recusa mesclar arquivos com o mesmo run number.

---

## 3. Procedimento de Resolução Canônica

### Passo 1: Garantir que o Batchman está Ativo
Se o `conman status` reportar `Batchman down`:
```bash
conman "start; mgr"
```
Valide com `conman status` até obter `Batchman LIVES.`

### Passo 2: Reconciliar a Instância Residual do Dia Anterior
Como o plano já avançou, confirme com sucesso o job `SWITCHPLAN` bloqueante da instância anterior:
```bash
conman "confirm MDMXA#FINAL(<sched_anterior>).SWITCHPLAN;succ"
```
*Exemplo real*:
```bash
conman "confirm MDMXA#FINAL(2359 09/08/26).SWITCHPLAN;succ"
```

### Passo 3: Liberar a Nova Instância do Dia
A nova instância do `FINAL` sairá da dependência bloqueada e ficará em `HOLD` devido ao flag `[Carry]`. Libere o stream para o Batchman:
```bash
conman "release MDMXA#FINAL(<sched_atual>)"
```
*Exemplo real*:
```bash
conman "release MDMXA#FINAL(2359 09/09/26)"
```

### Passo 4: Validação Automática da Execução
O Batchman iniciará a esteira sequencial automaticamente:
1. `STARTAPPSERVER` ➔ **SUCC (RC=0)**
2. `MAKEPLAN` ➔ **SUCC (RC=0)** (gera o novo `Symnew` com o próximo run number, sem intervenção manual)
3. `SWITCHPLAN` ➔ **SUCC (RC=0)**
4. `CHECKSYNC` ➔ **SUCC (RC=0)**
5. `CREATEPOSTREPORTS` ➔ **SUCC (RC=0)**
6. `UPDATESTATS` ➔ **SUCC (RC=0)**

Monitore o progresso com:
```bash
conman "sj MDMXA#FINAL.@; sj MDMXA#FINALPOSTREPORTS.@"
```

---

## 4. Evidências de Validação em Laboratório
- **Evidência**: `hwa-lab-10.2.8-sfinal-awsbhv082e-recovery-0001`
- **Ambiente**: Container `tws-hwa` (HWA 10.2.8 MDM, PostgreSQL 18.6, RHEL 9 UBI9)
- **Resultado**: Run Number avançou para `#30`, jobs completaram com `RC=0`, esteira do dia seguinte (`MDMXA#FINAL 2359 10/09`) gerada e estacionada em `HOLD` saudável.
