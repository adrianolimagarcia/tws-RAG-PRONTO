# Queda do engine do MDM: comportamento do backup (validado 2026-09-13)

## Objetivo
Medir o que acontece quando o engine do MDM (batchman/jobman) morre, com o backup BMDM no
ar — e documentar se há promoção automática (default) e como o backup reporta o MDM.

## Pré-condições
- MDM (tws-hwa) master; BMDM (tws-bmdm) FTA full-status.
- ⚠️ **PostgreSQL roda DENTRO do container do MDM (tws-hwa)** e é compartilhado com o BMDM.
  A queda simulada deve ser **APENAS do engine** (batchman+jobman), **nunca** do postgres nem do container.

## Passos
1. **Baseline** (read-only): `conman sc @` (confirmar MDM master), `planman showinfo` rc=0.
2. **T0 — derrubar o engine** (dentro do MDM, mantendo postgres/container):
   ```
   for p in $(ps -eo pid,comm | awk "/batchman|JOBMAN/{print \$1}"); do kill -9 $p; done
   ```
3. **Observar o backup (SOMENTE LEITURA)** por ~90s, a cada ~5s:
   ```
   conman sc @     # o MDM continua "UNIX MASTER"? o MDM_BK vira master? (de quem vê)
   ```
   ⚠️ **NÃO usar `conman "switchmgr MASTERDM;<node>"` como probe**: esse comando é MUTANTE —
   ele promove o nó alvo manualmente e confunde a medição. O probe correto é somente leitura
   (`conman sc @`).
4. **Medir a auto-recuperação do engine** (polls de 2s):
   `ps -eo comm | grep -cE "^(batchman|JOBMAN)$"` — observou-se 0 → 2 em ~31s.

## Resultado (validado 2026-09-13)
- **O backup NÃO promove automaticamente** com o default (enAutomaticFailover não configurado;
  globalopts vazio). O `sc @` do backup manteve MDM como "UNIX MASTER" e MDM_BK como FTA por ~90s.
- **O engine do MDM auto-recupera em ~31s** (supervisor CPA/tebctl religa batchman+jobman), então
  o kill não gera indisponibilidade sustentada.
- PostgreSQL permaneceu vivo; após a recuperação MDM voltou a master (planman rc=0).
- Referência: `hwa-lab-10.2.8-mdm-engine-failure-no-autofailover-0001`.

## Reversão / stop_criterion
- Auto-recuperação em ~31s; se não vier, religar manualmente:
  `su - wauser -c "cd /opt/hwa/TWS && . ./tws_env.sh; bin/conman \"start&link @!/@/@;noask\""`.
- stop_criterion: plano irrecuperável → religar o engine do MDM e parar.

## Limitações
- Falha simulada é **engine-only** (batchman+jobman). Não cobre queda de host, de rede nem do
  PostgreSQL — cenários que o backup detectaria de forma diferente.
- Para testar PROMOÇÃO AUTOMÁTICA, seria preciso habilitar `enAutomaticFailover` (globalopt) e
  refazer — **candidato a Teste B opção B, não executado até nova aprovação**.
