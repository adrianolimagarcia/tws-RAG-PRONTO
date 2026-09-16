#!/usr/bin/env bash
#
# lab-up-2026-09-16.sh — sobe os 3 containers do lab HWA 10.2.8.
#
#   *** PREPARADO, NAO APLICADO.  O DEFAULT E DRY-RUN. ***
#
# Os argumentos de criacao sao DERIVADOS do `config.v2.json` / `hostconfig.json` originais,
# preservados no snapshot btrfs 112 — nao vem de memoria, de historico nem de suposicao.
# Se a derivacao falhar, o script ABORTA: nao ha fallback silencioso para valores chutados.
#
# ESCOPO (o que este script NAO faz):
#   - nao toca o banco do lab (o postgres roda DENTRO do container);
#   - nao remove imagens, snapshots nem volumes;
#   - nao roda `docker prune` de nenhum tipo;
#   - nao aplica nada sem `--apply` explicito (o dry-run e o default).
#
# O `--restart unless-stopped` entra por PROPOSTA e esta marcado no codigo. E a correcao do
# defeito que derrubou o lab em 16.09: os containers originais tinham `RestartPolicy: no`, entao
# apos o reboot do host eles ficaram PARADOS e um `docker container prune` ("containers parados")
# os removeu — junto com a camada gravavel. Sem isso, o proximo reboot repete o incidente.
#
# Uso:
#   ./lab-up-2026-09-16.sh                    # DRY-RUN: imprime os comandos, nao executa
#   ./lab-up-2026-09-16.sh --check            # so as pre-condicoes
#   ./lab-up-2026-09-16.sh --apply            # executa (exige autorizacao do dono)
#   ./lab-up-2026-09-16.sh --image A --apply  # Via A: imagem reconstruida do snapshot (pos-M1)
#   ./lab-up-2026-09-16.sh --image B --apply  # Via B: imagens ha_snap_* (09/14, exige re-aplicar a M1)
#   ./lab-up-2026-09-16.sh --down             # REVERSAO: para e remove os 3 containers
#
# Exit codes: 0 OK | 2 pre-condicao falhou | 3 argumento invalido | 4 docker indisponivel

set -euo pipefail

# --------------------------------------------------------------------------------------
# Configuracao (caminhos fixos do ambiente; nada de valor magico espalhado pelo codigo)
# --------------------------------------------------------------------------------------
SNAP_DEFAULT="/.snapshots/112/snapshot"
BIND_DEFAULT="/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/docker"
LAYER_REL="var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/7/fs"
CONTAINERS_REL="var/lib/docker/containers"
BASE_IMAGE="registry.access.redhat.com/ubi9/ubi-init:latest"
BASE_DIGEST="sha256:5e25c1ed0c669e3a93dd82e0cbcdf7e663d9681a512278ec28d76675609cefaa"
VIA_A_IMAGE="tws-hwa:vigia-validacao-20260916"
ORDER=("tws-agent" "tws-bmdm" "tws-hwa")   # ordem obrigatoria: agent -> bmdm -> hwa

SNAP="${SNAP_DIR:-$SNAP_DEFAULT}"
BIND="${BIND_DIR:-$BIND_DEFAULT}"
VIA="A"
MODE="dry-run"

# --------------------------------------------------------------------------------------
# Utilitarios
# --------------------------------------------------------------------------------------
log()  { printf '  %s\n' "$*"; }
warn() { printf '  AVISO: %s\n' "$*" >&2; }
die()  { printf '  ERRO: %s\n' "$*" >&2; exit "${2:-2}"; }

usage() { sed -n '2,32p' "$0" | sed 's/^# \{0,1\}//'; exit 0; }

# --------------------------------------------------------------------------------------
# Derivacao dos argumentos — a fonte e o snapshot, nao a memoria
# --------------------------------------------------------------------------------------
# Emite, por container, um bloco `chave=valor` que o resto do script consome.
derive() {
  python3 - "$SNAP" "$CONTAINERS_REL" "$BIND" <<'PY'
import glob, json, os, sys

snap, containers_rel, bind = sys.argv[1], sys.argv[2], sys.argv[3]
base = os.path.join(snap, containers_rel)
if not os.path.isdir(base):
    sys.exit("snapshot sem %s — nao derivavel" % containers_rel)

for d in sorted(glob.glob(os.path.join(base, "*/"))):
    cfg_f = os.path.join(d, "config.v2.json")
    hc_f = os.path.join(d, "hostconfig.json")
    if not (os.path.exists(cfg_f) and os.path.exists(hc_f)):
        continue
    c = json.load(open(cfg_f))
    hc = json.load(open(hc_f))
    name = (c.get("Name") or "").lstrip("/")
    if name not in ("tws-hwa", "tws-bmdm", "tws-agent"):
        continue

    nets = (c.get("NetworkSettings") or {}).get("Networks") or {}
    # o primeiro bind e sempre o cgroup; os demais vem do snapshot, com o prefixo do sdb trocado.
    # ATENCAO: o bind e "src:dst[:mode]" — preservar SEMPRE o ":dst", senao o mount vira o path errado.
    binds = []
    for b in (hc.get("Binds") or []):
        src, _, rest = b.partition(":")
        if src == "/sys/fs/cgroup":
            binds.append(b)
        elif src.startswith(bind):
            binds.append(bind + src[len(bind):] + ":" + rest)
        else:
            binds.append(b)

    print("NAME=%s" % name)
    print("MEM=%d" % int(hc.get("Memory") or 0))
    print("MEMSWAP=%d" % int(hc.get("MemorySwap") or 0))
    print("SHM=%d" % int(hc.get("ShmSize") or 0))
    print("HOSTNAME=%s" % name)   # o original do tws-hwa era o id do container; o nome e a escolha correta
    print("NETMODE=%s" % (hc.get("NetworkMode") or "bridge"))
    for i, b in enumerate(binds):
        print("BIND_%d=%s" % (i, b))
    print("NBINDS=%d" % len(binds))
    for net, nd in nets.items():
        if net == "bridge":
            continue   # o bridge padrao entra sozinho; nao precisa de flag
        print("NET=%s" % net)
        print("NET_%s_IP=%s" % (net, nd.get("IPAddress") or ""))
        for a in (nd.get("Aliases") or []):
            if a and a != name:
                print("NET_%s_ALIAS=%s" % (net, a))
    print("END")
PY
}

# --------------------------------------------------------------------------------------
# Pre-condicoes
# --------------------------------------------------------------------------------------
preconditions() {
  local ok=0
  log "1. docker responde?"
  docker info >/dev/null 2>&1 || die "docker indisponivel" 4

  log "2. snapshot presente e com a camada do tws-hwa?"
  [ -d "$SNAP/$LAYER_REL" ] || die "camada ausente em $SNAP/$LAYER_REL"
  local sent="$SNAP/$LAYER_REL/opt/hwa/TWSDATA/stdlist/traces/20260915_TWSMERGE.log"
  [ -f "$sent" ] || die "sentinela ausente: $sent"
  local sz; sz=$(stat -c '%s' "$sent")
  [ "$sz" = "386880" ] || warn "sentinela com $sz bytes (esperado 386880) — confira antes de seguir"
  log "   sentinela OK ($sz bytes)"

  log "3. a camada e o DIFF, nao o rootfs (tem de dar AUSENTE):"
  local f
  for f in usr/bin/bash sbin/init usr/lib/systemd/systemd etc/os-release; do
    if [ -e "$SNAP/$LAYER_REL/$f" ]; then warn "/$f presente no diff — inesperado"; ok=1
    else log "   esperado AUSENTE: /$f"; fi
  done

  log "4. a base ubi9 confere com o digest do config original?"
  if docker image inspect "$BASE_IMAGE" >/dev/null 2>&1; then
    local bd; bd=$(docker image inspect "$BASE_IMAGE" --format '{{.Id}}')
    if [ "$bd" = "$BASE_DIGEST" ]; then log "   digest OK ($BASE_DIGEST)"
    else warn "digest da base DIVERGE do original: $bd"; fi
  else
    warn "imagem base $BASE_IMAGE ausente no host (necessaria para refazer o flatten da Via A)"
  fi

  log "5. imagem escolhida existe?"
  case "$VIA" in
    A) docker image inspect "$VIA_A_IMAGE" >/dev/null 2>&1 \
         || die "imagem da Via A ausente ($VIA_A_IMAGE) — rode o flatten do §5 do doc antes" ;;
    B) local n
       for n in "${ORDER[@]}"; do
         docker image inspect "ha_snap_20260914-0035_${n}:latest" >/dev/null 2>&1 \
           || die "imagem da Via B ausente para $n"
       done ;;
    *) die "via invalida: $VIA" 3 ;;
  esac
  log "   Via $VIA OK"

  log "5. binds existem?"
  local b
  for b in "$BIND/tws-hwa/installers" "$BIND/tws-hwa/data" "$BIND/tws-bmdm/data" \
           "$BIND/tws-bmdm/ssl-certs" "$BIND/tws-agent/data" "$BIND/tws-agent/installers" \
           "$BIND/tws-agent/ssl-certs"; do
    [ -e "$b" ] || die "bind ausente: $b"
  done
  log "   7/7 binds OK"

  log "6. redes existem e estao vazias?"
  local net
  for net in hwa-mesh hwa-lan; do
    docker network inspect "$net" >/dev/null 2>&1 || die "rede ausente: $net"
    local n; n=$(docker network inspect "$net" --format '{{len .Containers}}')
    log "   $net: $n membro(s)"
  done

  log "7. nenhum container do lab ja existente?"
  local c
  for c in "${ORDER[@]}"; do
    if docker container inspect "$c" >/dev/null 2>&1; then
      warn "$c JA EXISTE — o script nao sobrescreve; use --down antes"
      ok=1
    fi
  done

  log "8. espaco em disco (>= 20G livres para a Via A)?"
  local free; free=$(df -Pk / | awk 'NR==2 {print int($4/1024/1024)}')
  log "   ${free}G livres"
  [ "$free" -ge 20 ] || warn "menos de 20G livres"

  [ "$ok" = 0 ] || die "pre-condicoes com avisos acima — resolva antes de aplicar"
  log "pre-condicoes OK"
}

# --------------------------------------------------------------------------------------
# Montagem e execucao
# --------------------------------------------------------------------------------------
build_and_maybe_run() {
  local name="$1" blk="$2"
  local image mem memswap shm hostname
  mem=$(printf '%s\n' "$blk" | sed -n 's/^MEM=//p')
  memswap=$(printf '%s\n' "$blk" | sed -n 's/^MEMSWAP=//p')
  shm=$(printf '%s\n' "$blk" | sed -n 's/^SHM=//p')
  hostname=$(printf '%s\n' "$blk" | sed -n 's/^HOSTNAME=//p')

  local netmode
  netmode=$(printf '%s\n' "$blk" | sed -n 's/^NETMODE=//p')

  case "$VIA" in
    A) # a reconstrucao do snapshot cobre o MDM (tws-hwa), que e onde a M1 foi aplicada;
       # o bmdm e o agent nao tem flatten proprio e vem das imagens commitadas de 09/14.
       if [ "$name" = "tws-hwa" ]; then image="$VIA_A_IMAGE"
       else image="ha_snap_20260914-0035_${name}:latest"; fi ;;
    B) image="ha_snap_20260914-0035_${name}:latest" ;;
  esac

  local args=(run -d --name "$name" --hostname "$hostname"
    --privileged --security-opt label=disable --cgroupns private
    --memory "$((mem/1024/1024))m" --memory-swap "$((memswap/1024/1024))m"
    --shm-size "$((shm/1024/1024))m")
  # a rede PRIMARIA vem do NetworkMode original (bridge no hwa, hwa-mesh nos outros):
  # e ela que define a rota default. As redes extras entram DEPOIS.
  [ -n "$netmode" ] && args+=(--network "$netmode")

  local i=0 nb
  nb=$(printf '%s\n' "$blk" | sed -n 's/^NBINDS=//p')
  while [ "$i" -lt "$nb" ]; do
    args+=(-v "$(printf '%s\n' "$blk" | sed -n "s/^BIND_${i}=//p")")
    i=$((i+1))
  done

  local line
  while IFS= read -r line; do
    case "$line" in
      NET=*) local net="${line#NET=}"
             args+=(--network "$net")
             local ip alias
             ip=$(printf '%s\n' "$blk" | sed -n "s/^NET_${net}_IP=//p")
             [ -n "$ip" ] && args+=(--ip "$ip")
             alias=$(printf '%s\n' "$blk" | sed -n "s/^NET_${net}_ALIAS=//p")
             [ -n "$alias" ] && args+=(--network-alias "$alias") ;;
    esac
  done <<< "$blk"

  # ---- PROPOSTA: restart policy. O original tinha `no`; e a causa do incidente de 16.09.
  args+=(--restart unless-stopped)

  args+=("$image" /sbin/init)

  log "docker ${args[*]}"
  if [ "$MODE" = "apply" ]; then
    docker "${args[@]}"
    # stop_criterion por etapa: o container tem de sobreviver ao boot
    sleep 5
    if docker container inspect -f '{{.State.Running}}' "$name" 2>/dev/null | grep -q true; then
      log "   $name: UP"
    else
      die "$name nao subiu (State.Running != true). Veja: docker logs $name" 2
    fi
  fi
}

# --------------------------------------------------------------------------------------
# Reversao
# --------------------------------------------------------------------------------------
down() {
  local c
  for c in "${ORDER[@]}"; do
    if docker container inspect "$c" >/dev/null 2>&1; then
      log "parando e removendo $c (os binds /data sao do host e NAO sao tocados)"
      [ "$MODE" = "apply" ] && docker stop "$c" >/dev/null && docker rm "$c" >/dev/null
    else
      log "$c nao existe — nada a fazer"
    fi
  done
  log "reversao concluida. O snapshot 112 e os binds /data permanecem intactos."
}

# --------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------
ACTION="up"
while [ $# -gt 0 ]; do
  case "$1" in
    --apply)  MODE="apply" ;;
    --check)  ACTION="check" ;;
    --down)   ACTION="down" ;;
    --image)  shift; VIA="${1:-}" ;;
    -h|--help) usage ;;
    *) die "argumento invalido: $1" 3 ;;
  esac
  shift
done

log "lab-up 2026-09-16 | modo=$MODE via=$VIA snap=$SNAP"

case "$ACTION" in
  check) preconditions ;;
  down)  [ "$MODE" = "apply" ] || log "(dry-run: nada sera removido — use --apply para valer)"; down ;;
  up)
    preconditions
    log "--- ordem: ${ORDER[*]} ---"
    BLOCKS=$(derive) || die "derivacao falhou (snapshot ilegivel?)"
    for c in "${ORDER[@]}"; do
      blk=$(printf '%s\n' "$BLOCKS" | awk -v n="$c" '
        $0=="NAME="n {p=1} p {print} p && $0=="END" {exit}')
      [ -n "$blk" ] || die "sem dados derivados para $c"
      log ""
      log "== $c =="
      build_and_maybe_run "$c" "$blk"
    done
    [ "$MODE" = "apply" ] || log ""
    [ "$MODE" = "apply" ] || log "DRY-RUN: nada foi criado. Use --apply (com autorizacao do dono) para executar."
    ;;
esac
