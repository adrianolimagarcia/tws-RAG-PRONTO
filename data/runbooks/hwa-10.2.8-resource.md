# Resource numérico — criar, usar e observar alocação (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.6 do PLANO_FECHAMENTO_LACUNAS.

## Criar o resource

Arquivo com cabeçalho `$RESOURCES`. Formato: `WS#NOME quantidade "descrição"`
(quantidade direto após o nome — **não** existe keyword `NUM`):

```
$RESOURCES

MDM#LAB_RES 2 "Resource numerico de teste - fase 1 item 1.6"
```

```bash
composer add /tmp/lab_res16.txt
```

## Usar num job stream

`NEEDS` vai **no job stream, após o nome do job** (não na job definition):

```
SCHEDULE MDM#LAB_JS_RES1
DESCRIPTION "Job stream com resource - fase 1 item 1.6"
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_JOB_RES
 NEEDS MDM#LAB_RES
END
```

## Comportamento observado (teste com 3 jobs, resource NUM 2)

Job de teste: `sleep 25` para dar tempo de observar.

| Momento | js1 | js2 | js3 |
|---------|-----|-----|-----|
| t+10s | EXEC | EXEC | HOLD (aguardando resource) |
| t+35s | SUCC | SUCC | EXEC (liberou e iniciou) |

`conman "showresources"` durante o teste:
```
Workstation      Resource         Total Available     Qty UsedBy
MDM             #LAB_RES              2         1       1  MDM#LAB_JS_RES3[...].LAB_JOB_RES
```

- Total 2, 1 em uso pelo job do js3, 1 disponível.
- O 3o job ficou em HOLD até uma unidade liberar — alocação automática.

## Comandos úteis

```bash
conman "showresources"              # todos os resources e uso atual
composer "display res=MDM#LAB_RES"   # definição
```

## Limpeza

```bash
for i in 1 2 3; do conman "cancel LAB_JS_RES$i"; done   # confirma y
echo y | composer "delete js=LAB_JS_RES1"  # repetir p/ 2, 3
echo y | composer "delete job=MDM#LAB_JOB_RES"
echo y | composer "delete res=MDM#LAB_RES"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `unexpected token "NUM"` | Keyword não existe | Quantidade vai após o nome: `WS#NOME 2 "desc"` |
| `unexpected token "NEEDS"` no job | NEEDS não é de job | Colocar no job stream, após o job |
| Job em HOLD eterno | Resource esgotado por outro job | `showresources` para ver quem segura |
