# JobManager.ini do dynamic agent — referência do lab (10.2.8)

Data: 2026-10-12. Lab: tws-agent (TWS-AGENT_1, dynamic agent). Fase 3, item 3.2.
Arquivo real: `/opt/HCL/TWA_wauser/TWSDATA/ITA/cpa/config/JobManager.ini`.
Somente leitura — nenhuma alteração foi feita.

## Parâmetros principais

| Parâmetro | Valor no lab | Significado |
|-----------|--------------|-------------|
| ThisWorkstation | TWS-AGENT_1 | Nome da workstation no domínio |
| EventProcessorWorkstation | MDM | Para onde envia eventos de status |
| EventProcessorHostname | tws-hwa.lab | Host do MDM |
| EventProcessorPort | 31116 | Porta REST do engine |
| EventProcessorEifSslPort | 31131 | Porta EIF SSL para eventos |
| autostart | yes | Inicia junto com o agente |
| keepalive | yes | Reinicia se o processo morrer |
| min_up_time | 60 | Tempo mín (s) antes de considerar estável |
| status_timeout | 300 | Timeout (s) de status |
| check_status | no | Não verifica status externamente |

## Logging (tuning)

| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| JobManager.loggerhd.fileName | .../stdlist/JM/JobManager_message.log | Arquivo de log |
| JobManager.loggerhd.maxFileBytes | 1024000 | Rotação a cada ~1MB |
| JobManager.loggerhd.maxFiles | 3 | Mantém 3 arquivos |
| JobManager.ffdc.maxDiskSpace | 10000000 | Limite de 10MB para FFDC |
| JobManager.ffdc.quotaPolicy | QUOTA_AUTODELETE | Apaga antigos automaticamente |

## Quando mexer (tuning)
- `EventProcessorHostname/Port`: se o MDM mudar de host ou porta
- `keepalive = no`: apenas para debug (não recomendado em produção)
- Logs: aumente `maxFiles` se precisar de histórico maior para troubleshooting

## Troubleshooting
| Sintoma | Verificar |
|---------|-----------|
| Agent não reporta status | `EventProcessorHostname` resolvível? porta 31116 acessível? |
| JobManager cai em loop | `min_up_time`, logs em `.../stdlist/JM/` |
| Disco cheio de logs | `maxFileBytes`/`maxFiles`/`quotaPolicy` |
