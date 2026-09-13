# Promoção/Demoção BMDM↔MDM (validado 2026-09-13)

## Objetivo
Validar que a promoção do BMDM a master e a demolição de volta ao MDM são operações
completas, reversíveis, com relink dos agentes, e que não resetam o limit das estações.

## Pré-condições
- MDM (tws-hwa) master, BMDM (tws-bmdm) FTA full-status autolink.
- Plano do domínio (Run 69 no teste).

## Passos
1. **Probe do master atual** (idempotente):
   ```
   conman "switchmgr MASTERDM;<node>"   # AWSBHU118W "já é o manager" = node é o master
   ```
   ⚠️ **Sempre proteger o `;` com aspas**. Sem aspas o shell interpreta `;` como separador
   → `conman switchmgr MASTERDM` roda **sem alvo** e o resto vira comando (`MDM_BK: command not found`).
   O switchmgr então **não efetua nada** (parece "não funcionar"). É a causa nº1 de falso negativo.
2. **Promover BMDM** (do master atual):
   ```
   conman "switchmgr MASTERDM;MDM_BK"     # AWSBHU120I changed the domain manager MDM -> MDM_BK
   ```
   Após ~12s estabilizar; repetir o probe até AWSBHU118W estável (durante o switch pode retornar
   AWSBHU120I transitório — aguardar settle).
3. **Confirmar operação como master** (do novo master):
   `planman showinfo` (rc=0), `conman sj @`, e `conman sc @` para o relink dos agentes.
4. **Demover** (do master atual = BMDM):
   ```
   conman "switchmgr MASTERDM;MDM"        # AWSBHU120I -> MDM master; confirmar AWSBHU118W
   ```
5. **Checar limit da estação TWS-AGENT** após a demolição:
   - `conman sc @ | grep TWS-AGENT` — o **limit deve permanecer** (10), **não** resetar para 0.
   - Se resetar para 0 → `AWSBHU048E` (warning de workstation limit 0).

## Resultado (validado 2026-09-13)
**SUCCESS** — promoção (MDM_BK master, planman rc=0, agentes relinkados) e demolição (MDM master,
relink reverso) reversíveis. **TWS-AGENT limit permaneceu 10 em antes/promovido/demovido** — sem
reset para 0 e **sem AWSBHU048E**. Referências: `hwa-lab-10.2.8-bmdm-promotion-demotion-0001`.

## Observações / limitações
- Durante o switch, `conman sc @` pode mostrar temporariamente o modelo divergente do runtime
  (plan×model). O sinal autoritativo de quem é o master é o probe **AWSBHU118W** (estável).
- `tws-op status` do host continua reportando "on MDM" (configurado para .10) mesmo após o BMDM
  virar master — é ferramenta apontada ao nó fixo, não o estado real.
- AGT1 estava em Run 35 (≠ domínio Run 69) — condição pré-existente do lab.
