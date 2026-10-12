# Variable table — criar e usar variáveis num job (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.8 do PLANO_FECHAMENTO_LACUNAS.

## Criar a vartable

Sem cabeçalho especial (o extract mostra o objeto puro):

```
VARTABLE LAB_VT_18
  DESCRIPTION "Vartable de teste - fase 1 item 1.8"
  MEMBERS
  LAB_AMBIENTE "homologacao"
  LAB_TENTATIVAS "3"
END
```

```bash
composer add /tmp/lab_vt18.txt
```

## Referenciar no job stream

`VARTABLE` vai **no nível do job stream**, antes do ON:

```
SCHEDULE MDM#LAB_JS_VT
DESCRIPTION "Job stream com vartable - fase 1 item 1.8"
VARTABLE LAB_VT_18
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_JOB_VT
END
```

## Sintaxe da variável no job: `^NOME^`

Com circunflexos — **não** `%NOME%`:

```
MDM#LAB_JOB_VT
 DOCOMMAND "echo ambiente=^LAB_AMBIENTE^ tentativas=^LAB_TENTATIVAS^"
 ...
```

Saída observada:
```
ambiente=homologacao tentativas=3
```

## Atualizar definição existente

`composer add` num objeto que já existe pode não atualizar; usar `replace`:

```bash
composer replace /tmp/lab_job18.txt
```

## Limpeza

```bash
conman "cancel LAB_JS_VT"              # confirma y
echo y | composer "delete js=LAB_JS_VT"
echo y | composer "delete job=MDM#LAB_JOB_VT"
echo y | composer "delete vartable=LAB_VT_18"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Variável sai literal (`%X%`) | Sintaxe errada | Usar `^X^` com circunflexos |
| `unexpected token "VARTABLE"` no job | VARTABLE não é de job | Colocar no nível do job stream |
| `add` não atualiza objeto existente | Comportamento do add | Usar `composer replace` |
| Variável vazia no job | Vartable não associada ao stream | Verificar `VARTABLE` na definição do stream |
