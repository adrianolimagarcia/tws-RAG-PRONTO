# PARTE2 RUNBOOK UPGRADE 9 5 PARA 10 2 3

## RUNBOOK: Runbook: Upgrade direto 9.5 -> HWA 10.2.3

**Arquivo de origem:** `data/runbooks/upgrade-9.5-para-10.2.3.md`

### Escopo

- Origem: IBM Workload Scheduler / HCL Workload Automation 9.5.0.x.
- Destino: HCL Workload Automation 10.2.3 Distributed (master/domain manager).
- Requisito: upgrade direto suportado sem instalacao paralela; confirmar a
  matriz de versoes e os requisitos de software do alvo antes de iniciar.

### Pre-flight (BEGIN)

1. Verificar espaco em disco, JDK/JRE suportado e banco de dados compativel
   com 10.2.3.
2. Backup dos arquivos de configuracao: `useropts`, `localopts`, `Security`,
   `Sfinal`, `globalopts`, `TWSConfig.properties` e planos forecast/archived.
3. Backup do banco de dados do engine (schema pln/dwb/evt/log) via ferramenta
   do SGBD, ou preparar um backup master domain manager com banco espelhado.
4. Anotar credenciais de instalacao, certificados (ca.crt, tls.key, tls.crt)
   e os valores de `--thiscpu`/`--displayname` (devem ser distintos quando o
   instalador exige).
5. Abortar o runbook (ABORT) se o backup de banco ou de configuracao falhar,
   ou se a matriz de compatibilidade nao cobrir 9.5 -> 10.2.3.

### Execucao

1. Parar o processamento de producao de forma controlada (conman stop) e
   confirmar que nenhum JnextPlan/stageman esta em execucao.
2. Executar o instalador do 10.2.3 sobre a instalacao 9.5, fornecendo os
   parametros de SSL e de banco.
3. Resolver falhas de instalacao com base nos logs; reexecutar o instalador
   com `-resume` quando houver suporte.
4. Ajustar permissoes de certificados e de diretorios conforme o fluxo exato
   documentado (644 vs 755 e especifico de cada passo).
5. Regenerar o plano: `JnextPlan -for 0000` para criar o preproduction plan.
6. Validar: `composer version`, `conman showcpus`, `conman status`,
   `planman showinfo` e consulta ao schema do banco.

### ABORT (rollback)

- Restaurar o banco a partir do backup e os arquivos de configuracao
  originais; reinstalar a 9.5 conforme o procedimento original.
- Acionar suporte se o JnextPlan falhar apos o upgrade ou se o banco nao
  responder ao schema do 10.2.3.

### Cenario SFT (begin/abort)

- begin: "Migrar IWS 9.5 para HWA 10.2.3" -> executar runbook (backup, upgrade,
  JnextPlan -for 0000, validar).
- abort: "Backup de banco indisponivel / matriz de compatibilidade nao cobre
  9.5->10.2.3" -> interromper antes de iniciar o instalador.

### Fontes

- Direct upgrade suportado a partir de 9.5.0.x/10.x.x (claim
  `hwa-10.2.8-directupgrade-0001`).
- Backup/restore de configuracao e backup master domain manager (10.2.8 docs).
