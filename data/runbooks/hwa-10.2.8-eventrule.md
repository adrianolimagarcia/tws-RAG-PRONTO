# Event rule — objeto e limitação do lab (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.9 do PLANO_FECHAMENTO_LACUNAS.

## Status: LIMITAÇÃO DO LAB

O motor de eventos (EDWA — Event-Driven Workload Automation) **não está ativo**
neste lab. Verificado em 2026-10-12:

- Nenhum processo de eventos rodando (`ps aux | grep -i event` vazio)
- `conman "showevents"`: comando não existe
- `composer "display erule=@"`: nenhuma regra no banco
- Plugins existem em `/opt/hwa/TWS/eventPlugIn/` (FileMonitor, MailSender,
  TWSAction, etc.) e o binário `monman` existe, mas o processador não foi iniciado

Ativar o EDWA exigiria subir o `monman`/event processor no MDM, o que é uma
mudança significativa no lab — fora do escopo deste item. Nenhuma regra foi
criada para não poluir o ambiente.

## Para referência futura (quando o EDWA for ativado)

Objetos envolvidos:
```bash
composer "display erule=@"     # lista regras
composer "display erule=NOME"  # detalha regra
```

Conceitos:
- **Evento**: condição monitorada (ex: arquivo criado, job com ABEND)
- **Ação**: o que fazer quando o evento dispara (ex: submeter job stream, enviar email)
- **Regra**: liga evento -> ação, com filtros

Plugins disponíveis no lab (`/opt/hwa/TWS/eventPlugIn/`):
FileMonitorPlugIn, MailSenderPlugIn, MessageLoggerPlugIn, TWSActionPlugIn,
GenericEventPlugIn, GenericActionPlugIn, DatasetMonitorPlugIn.

## Próximo passo sugerido

Ativar o event processor num exercício dedicado (Fase 2 ou posterior),
testar uma regra filemon -> submit, documentar e depois desativar.

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `display erule=@` vazio | Nenhuma regra criada (normal) | Criar regra quando EDWA ativo |
| Regra criada mas não dispara | Event processor parado | Iniciar monman no MDM |
