# Processos do MDM: mailman, batchman, netman — saúde e portas (10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM). Fase 3, item 3.3 do PLANO_FECHAMENTO_LACUNAS.
Observado via `ps` e `ss` no container. Somente leitura.

## Processos e função

| Processo | Função | Porta(s) |
|----------|--------|----------|
| mailman | Comunicação entre workstations (troca de mensagens) | — (usa netman) |
| batchman | Execução do plano (dispara jobs, avalia dependências) | — |
| netman | Rede: aceita conexões das workstations | 31111 (TCP), 31113 (SSL) |
| monman | Monitoramento (autostart=yes no localopts) | — |
| appserver (Liberty) | Engine REST API, console interno | 31115, 31116 (HTTPS) |
| agent (no tws-agent) | Listener do dynamic agent | 31114 |
| EIF (eventos) | Recebimento de eventos via EIF | 31131 (SSL) |

## Verificar saúde

```bash
# processos rodando (como wauser no MDM):
ps aux | grep -E "mailman|batchman|netman" | grep -v grep

# portas escutando:
ss -tlnp | grep -E "3111"

# link com o MDM a partir de um FTA/agent:
# (dentro do container do agent)
conman "showcpus"   # deve listar LINKED
```

## Mapa de portas do lab

| Porta | Serviço | Onde |
|-------|---------|------|
| 31111 | netman TCP | tws-hwa, tws-bmdm |
| 31113 | netman SSL | tws-hwa, tws-bmdm |
| 31114 | agent listener | tws-agent |
| 31115 | appserver HTTP | tws-hwa |
| 31116 | appserver HTTPS / REST API | tws-hwa |
| 31131 | EIF SSL (eventos) | tws-hwa |
| 5432 | PostgreSQL (TWS + TDWC) | tws-hwa |

## Troubleshooting
| Sintoma | Verificar |
|---------|-----------|
| Agent UNLINK no `showcpus` | netman rodando? porta 31111 acessível? `mm unlink`/`mm retrylink` no localopts |
| `conman` não conecta | `HOST`/`PORT`/`PROTOCOL` no localopts; appserver rodando? |
| REST API não responde | Liberty rodando? porta 31116? certificado válido? |
| Jobs não disparam | batchman rodando? `bm check status` no localopts |
