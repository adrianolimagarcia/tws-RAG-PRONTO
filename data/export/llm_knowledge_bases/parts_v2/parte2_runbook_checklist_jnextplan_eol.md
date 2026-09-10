# PARTE2 RUNBOOK CHECKLIST JNEXTPLAN EOL

## RUNBOOK: Checklist: JnextPlan / SwitchPlan em ambiente EOL (IBM TWS 9.4, banco Oracle)

**Arquivo de origem:** `data/runbooks/checklist-jnextplan-eol.md`

### Antes de cada JnextPlan (lado TWS - acesso proprio)

- [ ] `planman showinfo`: Run number == Confirm run number; fim do plano coerente; sem
      instancia FINAL/SWITCHPLAN residual em EXEC de ciclos anteriores.
- [ ] `conman "sj @#FINAL.@"`: nenhum MakePlan/SwitchPlan preso; jobs normais em fluxo.
- [ ] `messages.log` sem AWSJPL017E / AWSJDB* / AWSJPU* recentes (ultimas 24h).
- [ ] Symphony/SymNew: timestamps do ultimo switch ok; espaco em disco de TWS_HOME,
      stdlist e schedlog com folga.
- [ ] Sem operacoes concorrentes no plano: outro planman/forecast/trial, stageman, ResetPlan,
      ou edicao massiva de job streams/dominios.

### Banco Oracle (time DBA - sem acesso proprio: pedir e agendar)

- [ ] **Auto stats gathering** (janela padrao 22h-02h) NAO pode coincidir com a virada de
      plano; se o schema TWS estiver no conjunto, excluir as tabelas de plano ou mover a
      janela. (Hipotese principal do incidente: stats rodando na virada.)
- [ ] RMAN / dataguard / exports fora da janela do switch.
- [ ] Undo e temp dimensionados para a transacao de geracao/confirmacao de plano.
- [ ] Apos cada ciclo: AWR do intervalo (top SQL por CPU/elapsed, timed events, blocking
      sessions) revisado pelo DBA.
- [ ] Se travar: snapshot imediato de `v$session` (blocking), `dba_blockers`/`dba_waiters`,
      `v$locked_object` — identifica o session culpado em minutos, nao em horas.

### Monitoracao continua

- [ ] Diario pos-JnextPlan: idade do joblog `stdlist/<DATE>/JnextPlan*` (>2h apos o horario
      esperado = alerta).
- [ ] `grep -E "AWSJPL017E|AWSJDB801E|AWSJPU004E"` no messages.log das ultimas 24h.
- [ ] Timestamps de Symphony/SymNew: antigo >25h com JnextPlan devido = falha de switch.
- [ ] Drift de run number: MDM vs workstations criticas (diferenca = plano nao distribuido).
- [ ] Acumulo de instancias incompletas (carryforward/JSI): limpeza periodica para enxugar a
      transacao do confirm (valido em qualquer banco).

### Janelas (negociacao TWS <-> DBA)

- Switch do TWS FORA da janela de stats e backup do Oracle.
- Backup/manutencao do banco FORA da janela do JnextPlan.
- Toda execucao manual de recuperacao (kill de processo, confirm;succ) registrada com
  evidencia (horario, pid, saidas) para auditoria posterior.

### Referencias

- Evidencia lab: `data/evidence/lab-validation-2026-09-04-switchplan-iv89990.jsonl`
- Runbook de resolucao: `recovery-switchplan-stale-exec.md`
- Runbook relacionado: `recovery-jnextplan.md` (AWSJPL017E/AWSBHV082E)
- Docs IBM/HCL: SwitchPlan problems; JnextPlan problems; APAR IV89990; AWSJCL054E
