# PARTE2 RUNBOOK RECOVERY SWITCHPLAN STALE EXEC

## RUNBOOK: Runbook: SwitchPlan em EXEC residual / processo planman confirm pendurado (IBM TWS 9.4 EOL)

**Arquivo de origem:** `data/runbooks/recovery-switchplan-stale-exec.md`

### Escopo

- Sintoma: SWITCHPLAN em EXEC prolongado (>1h); workstations podem ficar UNLINK (nao
  reiniciadas na distribuicao); plano ja aparece na data atual no conman sc.
- Causa tipica: processo `planman -timeout 3600 confirm` **pendurado** mantem o job em EXEC
  (APAR IV89990 - PLANMAN CONFIRM HANGS), mesmo com o confirm ja commitado no banco.
- Discriminador: `planman showinfo` com **Run number == Confirm run number** = switch
  concluido; EXEC e artefato do processo pendurado (NAO corromper, NAO resetar).

### Pre-flight (BEGIN)

1. `planman showinfo` — confirmar Run number == Confirm run number e janelas do plano
   coerentes (switch efetivamente concluido).
2. Localizar o processo pendurado:
   - Linux: `ps -ef | grep -E 'planman|stageman'`
   - Windows: `tasklist | findstr /i planman`
   - Procurar `planman ... confirm` com etime alto e CPU parada (amostrar 2x com ~30s).
3. Confirmar que NAO ha stageman ativo, segundo JnextPlan nem ResetPlan concorrente.
4. Obter o nome exato do job: `conman "sj @#FINAL.@;state=EXEC"`.

### Execucao

1. Se o processo `planman -timeout 3600 confirm` estiver pendurado E o plano estiver
   confirmado: encerrar **somente esse processo** (`kill <pid>`; `kill -9` se necessario).
   NUNCA matar batchman/netman/mailman.
2. Rechecar o job: `conman "sj @#FINAL.SWITCHPLAN"` — deve sair de EXEC (provavelmente
   para ABEND, o que e esperado).
3. Reconciliar o job: `conman "confirm <nome_exato>;succ"` — o switch completou sua missao;
   marcar SUCC destrava o FINALPOSTREPORTS (que so inicia apos SWITCHPLAN SUCC).
4. Validar: `planman showinfo` (inalterado), `conman "sj @#FINAL.SWITCHPLAN"` = SUCC,
   `conman status` = Batchman LIVES.

### ABORT (nao fazer)

- NAO reexecutar SwitchPlan/Stageman — risco AWSBHV082E (Symphony/Symnew mesmo run number
  nao mergeiam).
- NAO disparar segundo JnextPlan — risco AWSJPL017E (acao anterior incompleta).
- NAO usar ResetPlan -scratch como rotina; somente no fluxo AWSJPL017E e com aprovacao.
- NAO usar `conman kill` para job em EXEC — acao documentada como ignorada.
- Se houver historico de `conman start` durante stageman: validar integridade de
  Symphony/SymNew antes do proximo switch (risco de corrupcao).

### Notas de semantica (validado)

- EXEC residual NAO bloqueia o proximo JnextPlan: a instancia antiga e arquivada com o
  Symphony anterior no stageman; o FINAL do dia seguinte e instancia nova (run novo).
- AWSJPL017E e disparado por operacao de planner incompleta (MakePlan/planman/lock/reset),
  nao por um job em EXEC no plano.

### Fontes

- IBM Support: AWSJCL054E - SWITCHPLAN hangs in EXEC state
  (https://www.ibm.com/support/pages/awsjcl054e-tws-error-switchplan-hangs-exec-state)
- IBM APAR IV89990 - PLANMAN CONFIRM HANGS
  (https://www.ibm.com/support/pages/apar/IV89990)
- HCL: SwitchPlan problems / AWSJPL017E (v1028)
- Evidencia lab: `data/evidence/lab-validation-2026-09-04-switchplan-iv89990.jsonl`
  (claims hwa-lab-9.4.0-switchplan-* 0200-0208)
- Claims canonicas: `hwa-9.4.0-incident-switchplan-exec-hung-0001`,
  `hwa-10.2.8-incident-switchplan-confirm-0057`, `hwa-official-message-10.2.8-0006`
- Runbook relacionado: `recovery-jnextplan.md` (AWSJPL017E/AWSBHV082E); checklist
  preventivo: `checklist-jnextplan-eol.md`
