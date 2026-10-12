# Recovery — ABEND, RECOVERY STOP e rerun (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, variação de job.

## Job com falha proposital

```
MDM#LAB_JOB_FAIL
 DOCOMMAND "echo vai falhar && exit 3"
 STREAMLOGON wauser
 DESCRIPTION "Job que falha - fase 1 variacao recovery"
 TASKTYPE UNIX
 RECOVERY STOP
```

Resultado: `ABEND 10 11:19 00:00 3` (return code 3 visível no `sj`).

## Opções de RECOVERY na job definition

| Opção | Comportamento após ABEND |
|-------|--------------------------|
| `RECOVERY STOP` | Para; stream fica ABEND; operador decide |
| `RECOVERY CONTINUE` | Continua para o próximo job |
| `RECOVERY RERUN` | Reexecuta automaticamente |

## Rerun manual

```bash
conman "rerun LAB_JS_FAIL.LAB_JOB_FAIL"
```

Sintaxe: `rerun <stream>.<job>` (sem `#`, sem workstation).
Resultado: cria nova instância marcada como `>>rerun as LAB_JOB_FAIL`.

## Descoberta importante

**O rerun usa a definição do job como estava no plano, NÃO a definição
atualizada no banco.** Teste: corrigi o DOCOMMAND no DB via
`composer replace`, fiz rerun — a nova instância rodou o comando antigo
("vai falhar"). Para usar a definição nova, é preciso resubmeter o stream
(`sbs`) ou atualizar a instância no plano.

## Comandos relacionados

```bash
conman "rerun STREAM.JOB"       # reexecuta job em ABEND
conman "kill STREAM.JOB"        # mata job em EXEC
conman "cancel STREAM"          # cancela instância do plano
```

## Limpeza

```bash
conman "cancel LAB_JS_FAIL"                 # confirma y
echo y | composer "delete js=LAB_JS_FAIL"
echo y | composer "delete job=MDM#LAB_JOB_FAIL"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `rerun STREAM` dá erro de sintaxe | Falta o nome do job | `rerun STREAM.JOB` |
| Rerun rodou comando antigo | Usa definição do plano | Resubmeter com `sbs` para pegar definição nova |
| Job ABEND sem RC visível | Falha antes de executar | Ver stdlist para o erro real |
