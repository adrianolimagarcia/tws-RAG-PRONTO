# Job stream — ciclo de vida completo no plano (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.4 do PLANO_FECHAMENTO_LACUNAS.

## Criar a definição

```
SCHEDULE MDM#LAB_JS_CICLO
DESCRIPTION "Job stream ciclo de vida - fase 1 item 1.4"
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_UNIX_BASICO
END
```

```bash
composer add /tmp/lab_js14.txt
```

## Entrar no plano (3 formas)

| Forma | Comando | Quando usar |
|-------|---------|-------------|
| JnextPlan diário | automático à meia-noite | produção normal |
| Ad-hoc | `conman "sbs LAB_JS_CICLO"` | testes, reexecução |
| Com data/hora | `conman "sbs LAB_JS_CICLO;at=..."` | agendar teste |

## Estados observados no lab

```
conman "ss"                          # lista job streams no plano
conman "sj LAB_JS_CICLO"             # detalha jobs do stream
```

| Estado | Significado | Visto no lab |
|--------|-------------|--------------|
| HOLD | Aguardando tempo/dependência | Job com `AT 1409` ficou `HOLD 10(14:09)` |
| READY | Pronto, aguardando slot | Stream recém-submetido antes do job rodar |
| EXEC | Executando | (rápido demais para capturar no teste) |
| SUCC | Concluiu OK (return code 0) | `LAB_JS_AT` após release |
| STUCK | Travado aguardando operador | `JS_PROMPT_RUN` (item 1.1) |
| CANCL | Cancelado pelo operador | `cancel JS_PROMPT_RUN` (item 1.1) |
| ABEND | Falhou (return code != 0) | — |

## Time restriction (AT) — testado

`AT` vai **no job stream, após o nome do job** (não na job definition):

```
SCHEDULE MDM#LAB_JS_AT
:
MDM#LAB_UNIX_BASICO
 AT 1409
END
```

Comportamento: o job nasce em `HOLD` aguardando o horário.

## Liberar um job em HOLD antes da hora

```bash
conman "release LAB_JS_AT.LAB_UNIX_BASICO"
```

Resultado observado: job saiu de HOLD e concluiu SUCC, com a marca `[Released]`
na coluna de dependências. Sintaxe: `release <stream>.<job>` (sem `#`, sem workstation).

## Remover do plano e do banco

```bash
conman "cancel LAB_JS_AT"              # tira a instância do plano (confirma y)
composer "delete js=LAB_JS_AT"          # apaga a definição (confirma y)
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `AT` dá `unexpected token` no job | AT não é keyword de job | Colocar no job stream, após o job |
| `sbs` diz "does not exist" | Job stream não está no DB | `composer add` antes do `sbs` |
| Stream em HOLD eterno | Dependência nunca satisfeita | `release` ou investigar a dependência |
