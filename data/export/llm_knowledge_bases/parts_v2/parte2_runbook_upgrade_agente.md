# PARTE2 RUNBOOK UPGRADE AGENTE

## RUNBOOK: Runbook: Upgrade centralizado de agentes (HWA 10.2.x)

**Arquivo de origem:** `data/runbooks/upgrade-agente.md`

### Escopo

- Atualizacao centralizada de multiplos FTA/dynamic agents.
- Comportamento documentado: jobs ja em execucao continuam; nenhum job novo
  inicia durante a manutencao; o agente reinicia ao concluir.

### Pre-flight (BEGIN)

1. Confirmar a janela de manutencao e comunicar os stakeholders (impacto: nao
   iniciam novos jobs durante a atualizacao).
2. Verificar pre-requisitos do pacote de atualizacao: JDK/JRE, pastas SSL
   (ca.crt, tls.key, tls.crt), credenciais e porta do `tdwbhostname`.
3. Para agentes dinamicos, confirmar `agent dynamic` com `tdwbhostname` e
   `tdwbport` (padrao 31116 em instalacao nova).
4. Testar a atualizacao em um agente piloto antes do lote completo.
5. Abortar (ABORT) se o piloto falhar ou se o pool de recursos nao tiver
   capacidade de absorver a manutencao.

### Execucao

1. Distribuir o pacote de atualizacao aos agentes do lote.
2. Executar a atualizacao de forma centralizada (lote controlado).
3. Aguardar o reinicio de cada agente ao concluir.
4. Validar cada agente: `conman showcpus` (agente online) e confirmar que o
   broker/dynamic agent se registraram no server.

### ABORT

- Interromper o lote se um agente nao reiniciar ou nao voltar online.
- Revalidar conectividade, certificados e versao do agente antes de continuar
  o lote; acionar suporte se necessario.

### Cenario SFT (begin/abort)

- begin: "Atualizar FTA/dynamic agents do HWA 10.2.8 centralizadamente" ->
  validar pre-requisitos, piloto, lote, validacao com showcpus.
- abort: "Agente piloto nao voltou online apos atualizacao" -> interromper o
  lote e diagnosticar.

### Fontes

- Atualizacao centralizada de FTA/dynamic agents (claims
  `hwa-10.2.6-centralized-agent-update-0001`,
  `hwa-10.2.8-centralized-agent-update-behavior-0013`).
- Instalacao de agente 10.2.8 (claims `hwa-10.2.8-agent-dynamic-broker-0003`,
  `hwa-10.2.8-agent-ssl-folder-0001`).
