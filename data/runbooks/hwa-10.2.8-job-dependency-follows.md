# Dependência FOLLOWS entre jobs (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, variação de job.

## Definição

`FOLLOWS` vai no job stream, após o job dependente:

```
SCHEDULE MDM#LAB_JS_DEP
DESCRIPTION "Job stream com dependencia - fase 1 variacao"
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_JOB_DEP1
MDM#LAB_JOB_DEP2
 FOLLOWS LAB_JOB_DEP1
END
```

## Comportamento observado

| Momento | DEP1 | DEP2 |
|---------|------|------|
| t+6s | EXEC | HOLD (aguardando DEP1) |
| t+20s | SUCC | SUCC (liberou após DEP1) |

O job dependente só inicia após o antecessor concluir com sucesso.

## Variações de FOLLOWS

- `FOLLOWS job` — após SUCC do antecessor
- `FOLLOWS job;SUCC` — explícito
- Dependência entre streams: `FOLLOWS OUTRO_STREAM.JOB`
- Múltiplas: várias linhas FOLLOWS (todas precisam concluir)

## Limpeza

```bash
conman "cancel LAB_JS_DEP"                  # confirma y
echo y | composer "delete js=LAB_JS_DEP"
echo y | composer "delete job=MDM#LAB_JOB_DEP1"
echo y | composer "delete job=MDM#LAB_JOB_DEP2"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Job em HOLD eterno | Antecessor em ABEND/STUCK | Ver estado do antecessor; `rerun` ou `release` |
| `FOLLOWS` dá erro de sintaxe | Nome do job errado | Usar só o nome do job (sem workstation) |
| Dependência circular | A segue B e B segue A | Revisar o desenho do stream |
