#!/bin/bash
# watchdog_tws_container.sh — Monitoramento de Saúde Operacional do HWA 10.2.8
set -e

CONTAINER="tws-hwa"

# 1. Checar container Docker
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
  echo "{\"status\": \"CRITICAL\", \"message\": \"Container ${CONTAINER} nao esta rodando!\"}"
  exit 2
fi

# 2. Checar porta 31116 (Liberty engineServer)
PORT_OK=$(docker exec "$CONTAINER" ss -tln | grep -c ":31116 " || true)
if [ "$PORT_OK" -lt 1 ]; then
  echo "{\"status\": \"CRITICAL\", \"message\": \"Porta 31116 (engineServer) nao esta aberta!\"}"
  exit 3
fi

# 3. Checar status do batchman no conman
BATCHMAN_STATUS=$(docker exec "$CONTAINER" su - wauser -c "cd /opt/hwa/TWS && conman status" 2>&1 | grep -iE "Batchman LIVES" || true)
if [ -z "$BATCHMAN_STATUS" ]; then
  echo "{\"status\": \"WARNING\", \"message\": \"Batchman nao esta em estado LIVES!\"}"
  exit 4
fi

# 4. Checar plano atual
PLAN_INFO=$(docker exec "$CONTAINER" su - wauser -c "cd /opt/hwa/TWS && planman showinfo" 2>&1 | grep -iE "Production plan end time|Run number" | tr '\n' ' | ')

echo "{\"status\": \"HEALTHY\", \"engine_port_31116\": \"OPEN\", \"batchman\": \"LIVES\", \"plan\": \"${PLAN_INFO}\"}"
exit 0
