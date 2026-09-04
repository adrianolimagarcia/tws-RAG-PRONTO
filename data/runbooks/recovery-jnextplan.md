# Runbook: Recovery de JnextPlan / plano (HWA 10.2.8)

Status: procedimento de producao. Cobre falhas de JnextPlan, SwitchPlan e lock
de banco durante a geracao/troca do plano.

## Escopo

- `JnextPlan -for 0000` cria o preproduction plan; `-for 2400`/`-days`
  avancam o production plan. O plano e persistido no banco (schema pln).
- Erros tipicos: AWSJPL017E (plano nao criado por acao anterior nao concluida),
  AWSJPL018E (database already locked), AWSBHV082E (SwitchPlan: mesmo run
  number entre Symphony e Symnew).

## Pre-flight (BEGIN)

1. Confirmar que nenhum JnextPlan, stageman ou planman confirm concorrente
   esta em execucao.
2. Conferir `conman status` para verificar que os processos de producao estao
   parados ou prontos (conman start nao deve ser emitido durante JnextPlan).
3. Garantir espaco no tablespace do banco e snapshot de seguranca.
4. Abortar (ABORT) se houver processos concorrentes ou lock ativo nao
   explicado.

## Execucao

1. Identificar a acao/processo que falhou (AWSJPL017E) revisando os logs do
   planner; corrigir a causa antes de regerar.
2. Se AWSJPL018E (database already locked): identificar o processo detentor do
   lock; aguardar/limpar de forma controlada e reexecutar.
3. Se AWSBHV082E (SwitchPlan): verificar que planman confirm nao roda, rodar
   `planman showinfo`, e reexecutar o SwitchPlan.
4. Regenerar: `JnextPlan -for 0000` (preproduction) e depois `-for 2400`
   (production), conforme a necessidade.
5. Validar com `planman showinfo` e `conman showjobs` (jobs planejados visiveis
   no horario).

## ABORT

- Nao executar `planman reset -scratch` / `ResetPlan -scratch` sem intencao
  explicita de descartar o plano, aprovacao humana e `dbrunstats` antes de
  JnextPlan.
- Se o lock persistir ou o plano nao regenerar, abortar e acionar suporte
  preservando o Symphony/plano atual intacto.

## Cenario SFT (begin/abort)

- begin: "JnextPlan falhou com AWSJPL017E" -> identificar acao falha, corrigir,
  JnextPlan -for 0000, validar com planman showinfo.
- abort: "AWSJPL018E database locked persistente / divergencia de plano" ->
  nao forcar reset, acionar suporte.

## Fontes

- AWSJPL017E (claim `hwa-10.2.8-incident-0002`); AWSBHV082E (claim
  `hwa-10.2.8-awsbhv082e-0001`).
- JnextPlan -for 0000 (claim `hwa-10.2-distributed-jnextplan-for0000-0001`).
- plano em banco (runbook lab 10.2.8).
