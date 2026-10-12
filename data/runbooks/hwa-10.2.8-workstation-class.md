# Workstation class — criar e consultar (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.12 do PLANO_FECHAMENTO_LACUNAS.

## Para que serve

Agrupa workstations com características comuns. Útil para:
- Aplicar configurações a várias workstations de uma vez
- Referenciar grupos em definições (ex: mesma classe de SO)

## Criar

```
CPUCLASS LAB_CLASS_DOC
  DESCRIPTION "Classe de teste - fase 1 item 1.12"
  MEMBERS
    MDMDA
    TWS-AGENT_1
END
```

```bash
composer add /tmp/lab_ws112.txt
```

**Nota:** o lab não tinha nenhuma classe definida — o teste acima foi criado,
validado e removido.

## Consultar

```bash
composer "display workstationclass=LAB_CLASS_DOC"
```

```
CPUCLASS LAB_CLASS_DOC
  DESCRIPTION "Classe de teste - fase 1 item 1.12"
  MEMBERS
  MDMDA
  TWS-AGENT_1
END
```

## Limpeza

```bash
echo y | composer "delete workstationclass=LAB_CLASS_DOC"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `extract from wsclass=@` dá erro | Keyword errada no extract | Usar `workstationclass` |
| Membro não entra na classe | Workstation não existe no DB | `composer "display ws=NOME"` para conferir |
