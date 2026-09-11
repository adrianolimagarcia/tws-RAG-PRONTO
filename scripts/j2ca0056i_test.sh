#!/bin/bash
# Ataque agressivo: alta concorrencia + kills em rajada durante a carga
LOG=/opt/hwa/DWC/DWC_DATA/stdlist/appserver/dwcServer/logs/messages.log
DS=/opt/hwa/DWC/DWC_DATA/usr/servers/dwcServer/configDropins/overrides/datasource.xml

echo "config: $(grep -o 'purgePolicy="[A-Za-z]*"' $DS | head -1) | validationTimeout5s=$(grep -c 'validationTimeout="5s"' $DS)"

B=$(grep -c "J2CA0056I" $LOG 2>/dev/null)
echo "baseline: $B"

# 3 rodadas de 8s de carga intensa, com kills a cada ~300ms
for r in 1 2 3; do
  END=$((SECONDS+8))
  while [ $SECONDS -lt $END ]; do
    for i in $(seq 1 30); do
      curl -sk -o /dev/null https://localhost:9443/dwc --max-time 4 &
    done
    pkill -USR1 -f pg_proxy.py
    sleep 0.3
  done
  wait
done
sleep 12

A=$(grep -c "J2CA0056I" $LOG 2>/dev/null)
echo "depois: $A"
echo "NOVOS_J2CA0056I: $((A-B))"
grep -m 1 "J2CA0056I" $LOG 2>/dev/null | cut -c1-200
