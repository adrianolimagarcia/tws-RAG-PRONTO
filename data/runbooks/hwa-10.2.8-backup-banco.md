# Backup e restore do banco de dados TWS (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM), PostgreSQL 18. Fase 4, item 4.1 do PLANO_FECHAMENTO_LACUNAS.
**Testado de verdade**: backup + restore + validação de integridade executados no lab.

## Inventário

| Database | Tamanho | Tabelas | Papel |
|----------|---------|---------|-------|
| TWS | 23 MB | 137 (incl. views) | Engine TWS (plano, definições, histórico) |
| TDWC | — | 55 | Dynamic Workload Console |
| postgres | — | — | admin |

## Backup (online, sem parar serviços)

```bash
# dentro do container tws-hwa, como postgres:
docker exec tws-hwa bash -c "su postgres -c 'pg_dump -Fc -f /tmp/tws_backup.dump TWS'"
```

- Formato custom (`-Fc`): compacto + permite restore seletivo com `pg_restore -l/-L`.
- Resultado no lab: **658K, 1,0s**. `pg_dump` é online e não bloqueia o engine.

Para o TDWC (DWC), mesmo comando trocando o nome do database.

## Restore de teste (validado)

**NUNCA restaure por cima do TWS de produção do lab.** Use database de teste:

```bash
# 1. cria database de teste
docker exec tws-hwa bash -c "su postgres -c 'createdb TWS_RESTORE_TEST'"

# 2. restore
docker exec tws-hwa bash -c "su postgres -c 'pg_restore -d TWS_RESTORE_TEST /tmp/tws_backup.dump'"
# resultado no lab: 3,5s, exit 0

# 3. valida: compara row counts de TODAS as tabelas
# (script percorreu schemaname.tablename em pg_tables nos dois DBs)
# resultado no lab: 0 divergências em todas as tabelas

# 4. limpa
docker exec tws-hwa bash -c "su postgres -c 'dropdb TWS_RESTORE_TEST' && rm -f /tmp/tws_backup.dump"
```

## Restore real (emergência)

Só com o engine parado:

```bash
# 1. para os processos TWS no MDM
# 2. dropdb TWS && createdb TWS
# 3. pg_restore -d TWS /caminho/do/backup.dump
# 4. reinicia os processos e valida com conman
```

## Troubleshooting

| Sintoma | Causa | Ação |
|---------|-------|------|
| `pg_dump: connection refused` | PostgreSQL parado | `systemctl status postgresql` no tws-hwa |
| restore reclama de objetos existentes | database não estava vazio | usar database recém-criado |
| backup muito maior que o esperado | logs/blob acumulados | verificar `pg_database_size` antes |
