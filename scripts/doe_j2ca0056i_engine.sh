#!/bin/bash
# DoE no ENGINE: isola validationTimeout x purgePolicy usando o gatilho confiavel
# (operacao de plano = trabalho real no DB + terminacao das conexoes durante ela)
EDS=/opt/hwa/TWSDATA/usr/servers/engineServer/configDropins/overrides/datasource.xml
LOG=/opt/hwa/TWSDATA/stdlist/appserver/engineServer/logs/messages.log
ROUNDS=3

set_config() {
  local VT="$1" PP="$2"
  # normaliza: remove validationTimeout do connectionManager e ajusta purgePolicy
  sed -i 's| validationTimeout="[0-9]*s"||' "$EDS"
  if [ "$VT" != "none" ]; then
    sed -i "s|reapTime=\"90s\" purgePolicy=\"[A-Za-z]*\" maxIdleTime=\"10m\" enableSharingForDirectLookups|reapTime=\"90s\" purgePolicy=\"$PP\" maxIdleTime=\"10m\" validationTimeout=\"$VT\" enableSharingForDirectLookups|" "$EDS"
  else
    sed -i "s|reapTime=\"90s\" purgePolicy=\"[A-Za-z]*\" maxIdleTime=\"10m\" enableSharingForDirectLookups|reapTime=\"90s\" purgePolicy=\"$PP\" maxIdleTime=\"10m\" enableSharingForDirectLookups|" "$EDS"
  fi
  sleep 15
}

run_rounds() {
  local novos=0
  for r in $(seq 1 $ROUNDS); do
    local B; B=$(grep -c "J2CA0056I" "$LOG" 2>/dev/null); B=${B:-0}
    su - wauser -c "planman unlock" >/dev/null 2>&1
    ( su - wauser -c "planman ext -days 1" >/dev/null 2>&1 ) &
    ( su - wauser -c "planman showinfo" >/dev/null 2>&1 ) &
    ( su - wauser -c "conman 'sc @'" >/dev/null 2>&1 ) &
    sleep 0.4
    su - postgres -c "psql -tAc \"SELECT count(pg_terminate_backend(pid)) FROM pg_stat_activity WHERE datname='TWS' AND pid <> pg_backend_pid()\"" >/dev/null 2>&1
    wait
    sleep 2
    local A; A=$(grep -c "J2CA0056I" "$LOG" 2>/dev/null); A=${A:-0}
    novos=$((novos + A - B))
  done
  echo "$novos"
}

echo "combo|validationTimeout|purgePolicy|novos_J2CA0056I"
for combo in "A:none:EntirePool" "B:none:ValidateAllConnections" "C:10s:EntirePool" "D:10s:ValidateAllConnections"; do
  N="${combo%%:*}"; rest="${combo#*:}"; VT="${rest%%:*}"; PP="${rest##*:}"
  set_config "$VT" "$PP"
  echo "# $N aplicado: $(grep -o 'purgePolicy=\"[A-Za-z]*\"' "$EDS" | head -1) $(grep -c 'validationTimeout' "$EDS")x_vt" >&2
  N1=$(run_rounds)
  echo "$N|$VT|$PP|$N1"
done
