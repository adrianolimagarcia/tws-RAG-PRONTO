# Auto-failover: teste de isolamento de rede MDM↔BMDM (validado 2026-09-13)

## Objetivo
Verificar se isolar o link maestro (netman/mailman) entre MDM e BMDM — mantendo o PostgreSQL
acessível — dispara a promoção automática do backup após o threshold de 300s.

## Pré-condições
- MDM master, BMDM FTA, `enAutomaticFailover=yes` (af/aa), `mm resolve master=no`.
- Containers na bridge docker `hwa-mesh`; **iptables só existe no HOST** (o container não tem).
- Portas maestro: **31111/31113 (netman), 31114 (agent)**. PostgreSQL: **5432 (preservar)**.
  Health-check do failover usa engineServer (31115/31116/41114) + DB — **não** o link netman.

## Passos
1. **Snapshot antes**: `conman sc @`, `conman sj @`, `planman showinfo`; confirmar MDM master e
   MDM_BK com flags `LTI JW MDEA` (linkado).
2. **Isolar (host, DOCKER-USER)** — registrar exatamente as regras p/ reversão limpa:
   ```
   # substitua pelos IPs reais via `docker inspect ... ` na bridge hwa-mesh
   iptables -A DOCKER-USER -s <bmdm_ip> -d <mdm_ip>  -p tcp -m multiport --dports 31111,31113,31114 -j DROP
   iptables -A DOCKER-USER -s <mdm_ip>  -d <bmdm_ip> -p tcp -m multiport --dports 31111,31113,31114 -j DROP
   ```
3. **Observar** (~330s): `conman sc @` no backup — o MDM_BK perde as flags **L/T/W** (link down),
   mas MDM permanece "UNIX MASTER" e MDM_BK "UNIX FTA". Sem promoção.
4. **Reversão**: `iptables -D` das 2 regras (ou `iptables -F DOCKER-USER`).
5. **Relink**: do master, `conman "link MDM_BK;noask"` (ou aguardar `mm retrylink`).
6. **Snapshot depois**: confirmar MDM master, MDM_BK com flags LTI JW MDEA, planman rc=0.

## Resultado (validado 2026-09-13)
- **Isolar só o link maestro NÃO dispara o auto-failover** (338s > 300s sem promoção).
- O link cai (flags L/T/W somem) mas o backup continua podendo health-checkar o master via
  engineServer/Liberty e via banco → nenhuma condição de persistência (FTA/Liberty/DB) é atingida.
- PostgreSQL preservado (7 conexões do backup). Reversão limpa (0 regras), relink restaurado.
- Referência: `hwa-lab-10.2.8-autofailover-network-link-isolation-no-trigger-0001`.

## Limitações / riscos
- O trigger real exigiria **FTA/Liberty down** ou **engine sem DB** — escopo além desta autorização.
- Queda de **host** é inviável limpa neste lab (postgres colocalizado no tws-hwa).
- iptables no HOST: regras em DOCKER-USER não afetam o tráfego do docker; `iptables -D` preciso
  para reversão. Não usar `-F FORWARD` (quebraria regras do docker/ufw).
