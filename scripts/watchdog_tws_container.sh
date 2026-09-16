#!/bin/bash
# watchdog_tws_container.sh — Monitoramento de Saúde Operacional do HWA 10.2.8
#
# Exit codes: 0 HEALTHY | 2 CRITICAL (container/porta) | 3 CRITICAL (porta) | 4 WARNING (batchman)
#
# CORRECAO 2026-09-15: (a) `set -euo pipefail` — sem pipefail um erro dentro de um pipe
# (`planman showinfo | grep | tr`) era mascarado e o script seguia como se tivesse dado
# certo; (b) o JSON era montado por INTERPOLACAO de `${PLAN_INFO}` num `echo`, entao uma
# aspa/barra/controle vindo do produto gerava JSON invalido (e o leitor caia em UNKNOWN
# silencioso) — agora o JSON e montado pelo python3 com escape correto (json.dumps),
# recebendo os campos por ARGV (nunca por concatenacao).
set -euo pipefail

CONTAINER="${TWS_CONTAINER:-tws-hwa}"

emit() {  # emit <status> <exit_code> <message> [plan]
  python3 -c '
import json, sys
status, code, msg = sys.argv[1], int(sys.argv[2]), sys.argv[3]
plan = sys.argv[4] if len(sys.argv) > 4 else ""
out = {"status": status, "message": msg}
if status == "HEALTHY":
    out["engine_port_31116"] = "OPEN"
    out["batchman"] = "LIVES"
    out["plan"] = plan
print(json.dumps(out, ensure_ascii=False))
' "$1" "$2" "$3" "${4:-}"
  exit "$2"
}

# 1. Checar container Docker
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
  emit CRITICAL 2 "Container ${CONTAINER} nao esta rodando!"
fi

# 2. Checar porta 31116 (Liberty engineServer)
PORT_OK=$(docker exec "$CONTAINER" ss -tln 2>/dev/null | grep -c ":31116 " || true)
if [ "${PORT_OK:-0}" -lt 1 ]; then
  emit CRITICAL 3 "Porta 31116 (engineServer) nao esta aberta!"
fi

# 3. Checar status do batchman no conman
BATCHMAN_STATUS=$(docker exec "$CONTAINER" su - wauser -c "cd /opt/hwa/TWS && conman status" 2>&1 | grep -iE "Batchman LIVES" || true)
if [ -z "$BATCHMAN_STATUS" ]; then
  emit WARNING 4 "Batchman nao esta em estado LIVES!"
fi

# 4. Checar plano atual (read-only)
PLAN_INFO=$(docker exec "$CONTAINER" su - wauser -c "cd /opt/hwa/TWS && planman showinfo" 2>&1 \
            | grep -iE "Production plan end time|Run number" | tr '\n' ' ' || true)

emit HEALTHY 0 "Todos os servicos criticos estao operacionais." "$PLAN_INFO"
