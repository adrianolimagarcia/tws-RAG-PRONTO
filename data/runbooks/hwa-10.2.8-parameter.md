# Parameter / parms — parâmetros e override no submit (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.10 do PLANO_FECHAMENTO_LACUNAS.

## O que são "parms" no TWS

No composer, `parms` são os membros individuais das variable tables:

```bash
composer "extract /tmp/p.txt from parms=@"
```

```
$PARM

LAB_VT_18.LAB_AMBIENTE "homologacao"
LAB_VT_18.LAB_TENTATIVAS "3"
```

Formato: `vartable.variavel "valor"`, com cabeçalho `$PARM`.

## Override de vartable no submit (testado)

É possível trocar a vartable de um job stream na hora de submeter:

```bash
conman "sbs LAB_JS_VT;vartable=LAB_VT_ALT"
```

Teste realizado:
- Stream `LAB_JS_VT` usa `VARTABLE LAB_VT_18` (homologacao/3)
- Submit com `vartable=LAB_VT_ALT` (producao/9)
- Saída do job: `ambiente=producao tentativas=9` — override funcionou

Keywords aceitas no `sbs` (além de `vartable`/`vt`):
`NEEDS, OPENS, PROMPT, FOLLOWS, AT, UNTIL, PRIORITY, LIMIT, CARRYFORWARD, ALIAS, NOASK, ONUNTIL, DEADLINE, SCHEDTIME, JSUNTIL`

## Limpeza

```bash
echo y | composer "delete vartable=LAB_VT_ALT"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `parm=(X=y)` no sbs dá erro | Sintaxe não existe | Usar `vartable=NOME` |
| Override não surtiu efeito | Nome da vartable errado | `composer "display vartable=@"` para conferir |
