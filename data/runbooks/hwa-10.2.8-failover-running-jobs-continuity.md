# Failover MDM→BMDM: continuidade de jobs em execução (validado 2026-09-12)

## Objetivo
Provar que um job que está **em execução** sobre um agente **não é interrompido** quando o
master muda (failover manual MDM→BMDM via `conman switchmgr`).

## Pré-condições
- Domínio HWA 10.2.8 com MDM (tws-hwa) master e BMDM (tws-bmdm) FTA full-status autolink.
- Agente alvo (ex.: MDMDA) no plano do domínio (Run 68).
- Restrição: BMDM e MDM **compartilham o mesmo PostgreSQL** — a falha simulada é **só do engine**,
  nunca do banco.

## Passos (comandos exatos)
1. **Confirmar master atual** (idempotente):
   ```
   conman "switchmgr MASTERDM;<suspeito>"   # AWSBHU118W "já é o manager" = quem é o master
   ```
   ⚠️ **Aspas obrigatórias**: `conman "switchmgr MASTERDM;MDM_BK"`. Sem aspas o `;` é
   interpretado pelo shell como separador → `MDM_BK: command not found` e o switchmgr **não roda**
   (RC=127, sem efeito). Erro comum que parece "switch que não funciona".
2. **Submeter job longo** no agente (REST / tws-op):
   ```
   tws-op submit-adhoc --workstation MDMDA HAF_JOB_LONGO "sleep 600"
   ```
   Confirmar que entrou em **EXEC** (`conman sj MDMDA | grep <job>`).
3. **Failover no meio da execução** (do master atual):
   ```
   conman "switchmgr MASTERDM;MDM_BK"        # AWSBHU120I changed the domain manager
   ```
4. **Verificar continuidade**:
   - o processo do job continua vivo na estação (`ps -eo etime,cmd | grep "sleep 600"`);
   - aguardar a conclusão e conferir o `jm_exit.properties` do job no agente:
     `JOB_EXIT_CODE=0`, `JOB_ABEND=false`, `JOB_ELAPSED_TIME=600` (duração completa atravessando o switch);
   - stdlist arquivado: `TWSDATA/stdlist/JM/<data>/archive/<ws>#<stream>.<job>.JNUM-<runid>.zip`.
5. **Snapshot de comparabilidade** (antes/depois): `conman sc @`, `conman sj @`, `planman showinfo`.

## Reversão
`conman "switchmgr MASTERDM;MDM"` do master atual (AWSBHU120I → volta; confirmar AWSBHU118W).

## Resultado (validado 2026-09-12)
**SUCCESS** — o job em EXEC sobreviveu ao failover MDM→MDM_BK: processo intacto, terminou
**rc=0, JOB_ABEND=false, 600s completos**; stdlist arquivado. Referência de evidência:
`hwa-lab-10.2.8-running-job-failover-continuity-0001`.

## Observações / limitações
- O job **não ficou visível** em `conman sj @` da visão do novo master após o switch (possível
  divergência plano/visão pós-switchmgr — registrar como achado separado).
- Falha simulada é do **engine** (não host/DB). Não cobre queda de host nem do PostgreSQL.
- Evento do switch capturado: AWSBHU120I (sucesso); AWSBHU118W (já é o manager).
