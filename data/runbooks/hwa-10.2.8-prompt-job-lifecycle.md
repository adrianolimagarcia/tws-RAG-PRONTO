# Job com PROMPT de operador — ciclo de vida e limpeza (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.1 do PLANO_FECHAMENTO_LACUNAS.

## Definições usadas

Job stream (estava em DRAFT):
```
SCHEDULE MDM#JS_PROMPT_RUN
DESCRIPTION "Teste de workflow com prompt de operador"
DRAFT
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#JOB_PROMPTED
PROMPT PRM_LAB
END
```

Job:
```
MDM#JOB_PROMPTED
 DOCOMMAND "echo '=== JOB LIBERADO PELO OPERADOR VIA PROMPT! ===' && date"
 STREAMLOGON wauser
 DESCRIPTION "Job com aprovacao de prompt"
 TASKTYPE UNIX
 RECOVERY STOP
```

Prompt:
```
PRM_LAB "Deseja liberar o job critico?"
```

## Comportamento observado

- O job entra em espera aguardando resposta do operador ao prompt PRM_LAB.
- Sem resposta, as instâncias do job stream ficam em estado **STUCK** indefinidamente
  (observado: 4 instâncias STUCK de 10/08 a 10/11).
- Um job stream em DRAFT gera instâncias no plano normalmente.

## Limpeza de instâncias STUCK

**Recomendação: CANCEL, não responder ao prompt.** Responder "yes" executaria o job
de teste sem valor; cancelar é limpo e não deixa rastro enganoso de SUCC.

```bash
# no MDM, como wauser com tws_env.sh carregado:
conman "cancel JS_PROMPT_RUN"   # confirma com 'y' para cada instância
```

Resultado: instâncias STUCK -> CANCL.

## Remoção definitiva do banco de dados

```bash
composer "delete js=JS_PROMPT_RUN"   # confirmar com 'y'
composer "delete job=MDM#JOB_PROMPTED"
composer "delete prompt=PRM_LAB"
```

Após a remoção, nenhuma instância nova é gerada no plano.

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Job stream STUCK há dias | Prompt sem resposta do operador | `conman "cancel <stream>"` |
| Instâncias novas continuam aparecendo | Definição ainda existe no DB | `composer "delete js=<nome>"` |
| `cancel #NOME` dá erro de sintaxe | conman não aceita `#` no nome | usar `cancel NOME` sem `#` |
