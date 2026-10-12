# Disaster Recovery do lab TWS (10.2.8) — procedimento passo a passo

Data: 2026-10-12. Fase 4, item 4.3 do PLANO_FECHAMENTO_LACUNAS.
Cenário: perda do MDM (tws-hwa) ou corrupção do banco/plano. Procedimento validado
por partes nos runbooks hwa-10.2.8-backup-banco.md e hwa-10.2.8-backup-arquivos.md.

## Pré-requisitos (ter em mãos ANTES do desastre)

- [ ] Backup `pg_dump -Fc` do database TWS (e TDWC, se usa DWC)
- [ ] Backup tar de `/opt/hwa/TWSDATA` (sem logs)
- [ ] Cópia de `/opt/hwa/TWS/JnextPlan`
- [ ] Anotação: versão exata (10.2.8.00), hostname, IPs, senhas de serviço em cofre

## Ordem de restore (não inverter)

### 1. Infraestrutura
1. Recrie o container/host do MDM (mesmo hostname `tws-hwa`, mesma rede `hwa-mesh`)
2. Instale PostgreSQL 18 e restaure o acesso (`postgres` superuser)

### 2. Banco de dados (primeiro, antes dos arquivos)
```bash
su postgres -c 'createdb TWS'
su postgres -c 'pg_restore -d TWS /backup/tws_backup.dump'
# valide: contagem de tabelas e row counts (ver runbook de backup-banco)
```

### 3. Arquivos
```bash
tar -xzf /backup/twsdata_backup.tgz -C /
cp /backup/JnextPlan /opt/hwa/TWS/JnextPlan
chown -R wauser:wauser /opt/hwa/TWSDATA
```

### 4. Serviços (nesta ordem)
1. PostgreSQL (já no passo 2)
2. Processos TWS: netman → mailman → batchman → monman → appserver/engine
3. DWC (se aplicável): dwcServer, reconecte o engine

### 5. Verificação pós-restore
```bash
# como wauser, com tws_env.sh:
conman "sc"          # CPUs linkados? MDM, BMDM, agents
conman "ss"          # plano íntegro? job streams nos estados esperados
conman "sj <stream>" # spot-check de jobs
# DWC: login em https://<host>:9443/console, engine com checkConnection OK
```

## RTO/RPO medidos no lab (referência)

| Etapa | Tempo medido |
|-------|--------------|
| pg_dump TWS (23 MB) | 1,0s |
| pg_restore TWS | 3,5s |
| tar TWSDATA (sem logs) | 1,1s |

RPO ≈ intervalo entre backups (sugestão lab: diário). RTO ≈ minutos (restore) + reinstalação se perdeu o host.

## Troubleshooting

| Sintoma pós-restore | Causa provável | Ação |
|---------------------|----------------|------|
| Engine não sobe | localopts com hostname/IP antigo | conferir `/opt/hwa/TWSDATA/localopts` |
| Agents não linkam | certificados SSL não restaurados | restaurar `/opt/hwa/TWSDATA/Security` |
| Plano vazio | Symphony não restaurado ou JnextPlan faltando | verificar arquivos do passo 3 |
| DWC não conecta no engine | engine connection aponta host antigo | recriar engine connection no DWC |
