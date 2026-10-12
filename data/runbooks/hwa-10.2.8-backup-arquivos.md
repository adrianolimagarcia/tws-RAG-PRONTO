# Backup de arquivos críticos do TWS (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM). Fase 4, item 4.2 do PLANO_FECHAMENTO_LACUNAS.
**Testado de verdade**: backup tar + verificação de integridade + restore de teste executados.

## O que copiar (por prioridade)

| Prioridade | Caminho | Conteúdo | Tamanho lab |
|------------|---------|----------|-------------|
| 1 | `/opt/hwa/TWSDATA` | Symphony (plano atual), Sinfonia, Jobtable, Security, localopts, EDWA | 565 MB |
| 2 | `/opt/hwa/TWS/JnextPlan` | Próximo plano | 8 KB |
| 3 | `/opt/hwa/TWS/Symphony` | Cópia do plano atual | — |
| 4 | Database TWS | ver runbook hwa-10.2.8-backup-banco.md | 23 MB |

`/opt/hwa/TWS` (1,2 GB) são binários — reinstaláveis, backup opcional.

## Backup (testado)

```bash
# TWSDATA sem logs (suficiente para DR):
docker exec tws-hwa bash -c 'tar -czf /tmp/twsdata_backup.tgz --exclude="*.log" --exclude="stdlist" /opt/hwa/TWSDATA'
# resultado no lab: 17 MB, 504 arquivos, 1,1s

# JnextPlan (arquivo único):
docker exec tws-hwa bash -c 'cp /opt/hwa/TWS/JnextPlan /tmp/'
```

## Verificação de integridade (testada)

```bash
# 1. integridade do tar:
docker exec tws-hwa bash -c 'tar -tzf /tmp/twsdata_backup.tgz > /dev/null && echo TAR_OK'
# 2. restore de teste num dir temporário + diff dos arquivos críticos:
docker exec tws-hwa bash -c 'mkdir -p /tmp/restore_test && tar -xzf /tmp/twsdata_backup.tgz -C /tmp/restore_test && diff -q /tmp/restore_test/opt/hwa/TWSDATA/Symphony /opt/hwa/TWSDATA/Symphony && diff -q /tmp/restore_test/opt/hwa/TWSDATA/localopts /opt/hwa/TWSDATA/localopts && echo RESTORE_OK; rm -rf /tmp/restore_test'
# resultado no lab: SYMPHONY_IDENTICO, LOCALOPTS_IDENTICO
```

## Restore real (emergência)

Com o engine parado:
```bash
# 1. backup do estado atual quebrado (por segurança): tar -czf /tmp/twsdata_quebrado.tgz /opt/hwa/TWSDATA
# 2. rm -rf /opt/hwa/TWSDATA && mkdir /opt/hwa/TWSDATA
# 3. tar -xzf /tmp/twsdata_backup.tgz -C /
# 4. chown -R wauser:wauser /opt/hwa/TWSDATA
# 5. reinicia os processos e valida
```

## Troubleshooting

| Sintoma | Causa | Ação |
|---------|-------|------|
| tar reclama de arquivos mudando | engine escrevendo durante backup | normal; para backup 100% consistente, pare o engine ou use o backup do banco |
| `diff` diverge no Symphony | plano mudou entre backup e verificação | esperado se o plano rodou no intervalo; refaça o backup |
| Permissão negada no restore | owner errado | `chown -R wauser:wauser` após extrair |
