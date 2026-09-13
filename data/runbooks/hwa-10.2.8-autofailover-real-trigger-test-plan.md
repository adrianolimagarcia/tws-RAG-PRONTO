# PLANO — Auto-failover: teste do trigger real (FTA/Liberty down OU engine↔DB)
**STATUS: DOCUMENTADO, NÃO EXECUTADO — aguarda decisão explícita do dono.**
Escopo novo: mudança de requisito de lab (exige banco preservável na queda do trigger).

## Contexto / por que este teste
O isolamento só do link netman (31111/31113/31114) NÃO disparou auto-failover
(claim hwa-lab-10.2.8-autofailover-network-link-isolation-no-trigger-0001): o backup segue
health-checkando o master via engineServer/Liberty e via banco. A doc oficial HCL 10.2.8
(awsadautoswitchmdm.html) define o trigger permanente (~300s, com polling de 10s) quando
PERSISTE uma de:
  1. **FTA down** (processos Batchman/Mailman/Jobman — o master tenta 3 restarts; se falharem → switch).
  2. **Liberty/engineServer down** (watchdog tenta restart; se falhar → switchmgr + switcheventprocessor).
  3. **Engine sem comunicação com o banco** (outage de rede p/ o DB).

## Restrição crítica de LAB (por que não executado agora)
O **PostgreSQL roda DENTRO do tws-hwa (MDM)** e é compartilhado com o BMDM. Logo:
- **Queda de host / engine↔DB**: derrubar o host ou o acesso ao DB derruba o banco do backup também
  → o backup fica sem DB e NÃO promove de forma limpa. **Inviável neste lab.**
- Para testar o trigger real com integridade é preciso um lab com **DB preservável na queda do
  trigger** (banco em host separado/replicado, ou os nós com DB próprio sincronizado).

## O que derrubar (parametrização, quando houver lab adequado)

### Opção A — FTA do master down (sem tocar DB)
- Alvo: processos do FTA do MDM: `netman`, `mailman`, `batchman`, `jobman` (cadeia
  `netman→mailman→batchman→JOBMAN`), OU apenas a cadeia de agendamento.
- **Segurar a auto-recuperação**: o `mailman` (pai) religa batchman em ~15-31s; e o master faz
  3 tentativas de restart. Para o trigger é preciso que as 3 tentativas FALHEM (manter down).
- Métrica: `t_promote` (timestamp da promoção do backup); esperado ~300s (threshold).

### Opção B — Liberty/engineServer down (sem tocar DB)
- Alvo: o processo java do `engineServer` (Liberty) no MDM.
- O watchdog tenta restart; se falhar → switchmgr + switcheventprocessor.
- Métrica: `t_promote`.

### Opção C — engine↔DB unreachable (APENAS se DB preservável p/ o backup)
- Bloquear a comunicação do engine do MDM com o postgres, MAS garantir que o backup alcance um DB
  íntegro (requer DB externo/replicado). No lab atual inviável (mesmo postgres).

## Metricas (todas, para qualquer opcao)
- `t0` (início da queda), `t_link_down` (flags L/T/W somem no sc @ do backup),
  `t_promote` (backup vira UNIX MASTER), duração total.
- Snapshot `sc @`, `sj @`, `planman showinfo` antes/depois.
- Confirmar `mm resolve master=no`, `af=yes`, `aa=yes`.

## Reversão
- Opção A: religar a cadeia via `conman "start&link @!/@/@;noask"` + `startmon` (ou restart do
  engineServer); o master volta.
- Opção B: reiniciar o engineServer (startAppServer.sh).
- Opção C: desbloquear o acesso ao DB.
- Depois da promoção automática: **switch manual de volta ao MDM** (`conman "switchmgr MASTERDM;MDM"`)
  e confirmar relink dos agentes.

## stop_criterion
- Se o plano ficar irrecuperável OU postgres perder contato OU ambos os nós caírem → restaurar o
  componente derrubado e parar imediatamente.

## Riscos (classificação)
- **Opção A** (FTA down): `mutating`, reversível (conman start), risco médio.
- **Opção B** (Liberty down): `mutating`, reversível (startAppServer), risco médio-alto (afeta REST).
- **Opção C** (DB): `mutating`/`destructive` se mal isolado; só em lab com DB preservável.

## Referências
- Doc oficial: help.hcl-software.com/workloadautomation/v1028 awsadautoswitchmdm.html
- Achado base: hwa-lab-10.2.8-autofailover-network-link-isolation-no-trigger-0001
