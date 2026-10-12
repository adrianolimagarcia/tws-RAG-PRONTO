# Job UNIX docommand — criar, executar e ver saída (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.2 do PLANO_FECHAMENTO_LACUNAS.

## Criar a job definition

O arquivo precisa começar com o cabeçalho `$JOBS`:

```
$JOBS

MDM#LAB_UNIX_BASICO
 DOCOMMAND "echo hello-lab && date && hostname"
 STREAMLOGON wauser
 DESCRIPTION "Job UNIX basico de teste - fase 1 item 1.2"
 TASKTYPE UNIX
 RECOVERY STOP
```

Adicionar ao banco:
```bash
composer add /tmp/lab_job.txt
```

## Criar o job stream

```
SCHEDULE MDM#LAB_JS_BASICO
DESCRIPTION "Job stream de teste - fase 1 item 1.2"
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_UNIX_BASICO
END
```

```bash
composer add /tmp/lab_js.txt
```

## Submeter ad-hoc e acompanhar

```bash
conman "sbs LAB_JS_BASICO"   # submit job stream -> batchman
conman "ss" | grep LAB_JS     # estado: SUCC
```

Saída observada (stdlist via `conman "sj LAB_JS_BASICO;stdlist"`):
```
hello-lab
Mon Oct 12 10:59:18 -03 2026
tws-hwa
= Exit Status           : 0
= Elapsed Time (hh:mm:ss) : 0:00:00
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `composer add` reclama de keyword | Falta o cabeçalho `$JOBS` no arquivo | Adicionar `$JOBS` na 1a linha |
| `composer create` pede jobstream | `create` é para job streams, não jobs | Usar `composer add` com arquivo |
| `conman "submit X"` dá erro de selector | Sintaxe errada | Usar `conman "sbs NOME"` |
