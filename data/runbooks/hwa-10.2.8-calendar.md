# Calendar — criar e usar em runcycle (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.7 do PLANO_FECHAMENTO_LACUNAS.

## Criar o calendário

Arquivo com cabeçalho `$CALENDAR`. Formato: nome, depois datas MM/DD/YYYY:

```
$CALENDAR

LABCAL16
  10/13/2026
```

```bash
composer add /tmp/lab_cal17.txt
```

## Usar no job stream (FREEDAYS)

A keyword é `FREEDAYS <calendario>`, no nível do job stream, antes do ON:

```
SCHEDULE MDM#LAB_JS_CAL
DESCRIPTION "Job stream com calendario - fase 1 item 1.7"
FREEDAYS LABCAL16
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_UNIX_BASICO
END
```

Comportamento: o JnextPlan pula os dias listados no calendário ao gerar
as instâncias do stream. Útil para feriados e paradas programadas.

## Consultar

```bash
composer "display calendar=LABCAL16"
```

Saída:
```
LABCAL16
  10/13/2026
```

## Limpeza

```bash
echo y | composer "delete js=LAB_JS_CAL"
echo y | composer "delete calendar=LABCAL16"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `EXCEPT`/`INCLUDE` dão `unexpected token` | Não são keywords de runcycle | Usar `FREEDAYS <cal>` no stream |
| Runcycle "not compliant with ICalendar" | Expressão inválida nas aspas | Manter só FREQ/BYDAY; calendário vai em FREEDAYS |
| Stream gerou instância no feriado | Calendário não associado | Verificar `FREEDAYS` na definição |
