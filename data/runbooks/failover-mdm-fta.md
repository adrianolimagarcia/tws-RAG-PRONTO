# Runbook: Failover MDM / FTA (HWA 10.2.8)

Status: procedimento de producao. Aplica-se ao failover automatico e manual
entre master domain manager e fault-tolerant agent / backup engine.

## Escopo

- Master domain manager (MDM) ativo e um engine de backup (backup MDM ou FTA).
- Opcao global `enAutomaticFailover` (af) e `enAutomaticFailoverActions` (aa)
  controlam a promocao automatica quando o master ativo fica indisponivel.

## Pre-flight (BEGIN)

1. Confirmar que o backup master/FTA esta online, alcancavel e com plano
   coerente.
2. Verificar `enAutomaticFailover=YES` no ambiente ativo.
3. Confirmar resolucao de hostname da workstation (ex.: alias do master em
   `/etc/hosts`) para evitar erros de heartbeat (AWSRES003E).
4. Abortar (ABORT) se houver divergencia de plano entre os engines; nunca
   forcar a promocao sobre um plano divergente.

## Execucao (failover automatico)

1. Master ativo indisponivel -> o backup assume conforme `enAutomaticFailover`.
2. Confirmar a promocao no console / via REST.
3. Monitorar o catch-up de jobs em execucao e do plano/banco apos a promocao.
4. Notificar times de monitoracao; nao iniciar novos deployments ate a
   estabilizacao.

## Execucao (failover manual)

1. Executar a sequencia documentada de switch do master ativo para o backup
   (rota/switch conforme a topologia), parando a producao de forma controlada.
2. Apontar agentes/console para o novo master.
3. Revalidar conectividade de todos os agentes (`conman showcpus`).

## Retorno (failback)

- Quando o master original voltar, reapresenta-lo como BACKUP, nao como ativo.
- Revalidar o plano antes de um novo failover.

## ABORT

- Abortar se a promocao automatica falhar e o backup nao assumir: restaurar o
  master original (se saudavel) e acionar suporte; nao emitir `resetFTA`
  sem diagnostico de Symphony corrompido e aprovacao humana.

## Cenario SFT (begin/abort)

- begin: "MDM ficou indisponivel, enAutomaticFailover habilitada" -> verificar
  backup online, confirmar promocao automatica, monitorar catch-up.
- abort: "Plano divergente entre engines / backup offline" -> nao promover,
  acionar suporte.

## Fontes

- `enAutomaticFailover`/`enAutomaticFailoverActions` (claim
  `hwa-10.2.8-globalopts-enautomaticfailover-0001` e
  `hwa-10.2.8-globalopts-enautomaticfailoveractions-0001`).
- AWSRES003E heartbeat (lab 10.2.8, alias de host em /etc/hosts).
