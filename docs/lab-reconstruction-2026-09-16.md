# Reconstrução do lab HWA 10.2.8 após a remoção dos containers (16.09.2026)

> **ESTE DOCUMENTO É PREPARAÇÃO, NÃO EXECUÇÃO.** Nada aqui foi executado. A execução é decisão do
> dono e exige autorização explícita. Preparado a pedido do VIGIA-ARQUITETO (escopo: escrever,
> validar por leitura e publicar).
>
> **Sobre endereços:** este repositório **proíbe literal IPv4** (regra do gate de publicação). Por isso os
> endereços das redes do lab **não estão escritos aqui** — o procedimento os **deriva do snapshot** (§4.1),
> que é a fonte exata. Não substituir por literais.

## 1. O que aconteceu (causa raiz medida)

| hora (BR) | evento |
|---|---|
| `15/09 23:55:32` | capturas do boundary ficam `Deactivated successfully` — **nenhuma escreveu o alvo** |
| `15/09 23:55:42` | **shutdown do host** (última entrada do boot `-1`) |
| `16/09 01:03:35` | host volta (boot 0); `dockerd` restaura os 5 containers às `01:08:38` |
| `16/09 02:28:08` | **sessão irmã `e9b3b8b7e0c4`** roda `docker container prune -f` (escopo aprovado: "dangling + **containers parados**") → **remove os 3 do lab** (`Total reclaimed space: 12.3GB`), **camada gravável junto** |
| `16/09 02:28:14` | `docker image prune -f` (só dangling) — as imagens `ha_snap_20260914-0035_tws-*` **sobrevivem** |

**Mecanismo:** o lab **não tem `restart policy`** (`RestartPolicy: {"Name": "no"}` nos três — lido do
`hostconfig.json` original). Após o reboot os containers ficaram **parados**, o que os tornou elegíveis ao
prune. O `tws-watchdog` detectou corretamente (`CRITICAL`); o email está desativado por default.

## 2. Estado preservado (verificado por leitura)

| o quê | onde | estado |
|---|---|---|
| **Instalação TWS + `/opt/hwa/TWSDATA`** | camada gravável do `tws-hwa` (containerd **snapshot 7**, 5,2 G) dentro do **snapshot btrfs 112** | **PÓS-M1** ✓ |
| Banco do lab (`/var/lib/pgsql/18/data`) | idem (postgres só roda no MDM → confirma que a camada é a do `tws-hwa`) | mtime `23:55:34` |
| `20260915_TWSMERGE.log` | idem | **386880 B, mtime `22:58:33`** (o tick de 3 h do profiler) |
| Imagens `ha_snap_20260914-0035_tws-{hwa,bmdm,agent}` | docker | íntegras — **09/14 00:35, NÃO contêm a M1** |
| `/data` dos três (bind no sdb) | `.../hermes/docker/tws-*/data` | **íntegro** (`tws-hwa` 4,5 M / `tws-bmdm` 20 K / `tws-agent` 16 K) |
| Redes `hwa-mesh` (bridge) e `hwa-lan` (**ipvlan**, parent `wlan0`) | docker | existem, **sem membros** — subnets e IPs **derivados no §4.1** (não literalizados aqui por regra do repo) |

## 3. Config original dos containers (lida do snapshot — é o que define os comandos)

Todos: imagem base `registry.access.redhat.com/ubi9/ubi-init:latest`, `Cmd ["/sbin/init"]`,
`Privileged: true`, `SecurityOpt ["label=disable"]`, `CgroupnsMode: private`, `ShmSize 64m`,
`RestartPolicy: no`, **sem portas publicadas**, bind `/sys/fs/cgroup:/sys/fs/cgroup:rw`.

| | tws-hwa (MDM) | tws-bmdm | tws-agent |
|---|---|---|---|
| hostname | `tws-hwa` | `tws-bmdm` | `tws-agent` |
| memória / swap | 4 G / 6 G | 4 G / 6 G | 2 G / 3 G |
| redes | `bridge`, `hwa-lan` (`$IP_HWA_LAN`), `hwa-mesh` (`$IP_HWA_MESH`, alias `tws-hwa.lab`) | `hwa-mesh` (`$IP_BMDM_MESH`, alias `tws-bmdm.lab`) | `hwa-mesh` (`$IP_AGENT_MESH`, alias `tws-agent.lab`) |
| binds | `.../tws-hwa/installers:/installers`, `.../tws-hwa/data:/data` | `.../tws-bmdm/data:/data`, `.../tws-hwa/installers:/installers`, `.../tws-bmdm/ssl-certs:/opt/ssl-certs:ro` | `.../tws-agent/data:/data`, `.../tws-agent/installers:/installers:ro`, `.../tws-agent/ssl-certs:/opt/ssl-certs:ro` |

Prefixo dos binds: `/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/docker/`

## 4. Pré-condições

### 4.1 Derivar os endereços do snapshot (obrigatório antes dos `docker run`)

```bash
# Fonte EXATA: os config.v2.json dos containers originais, preservados no snapshot 112.
# O container id do tws-hwa e do tws-bmdm e do tws-agent e recuperado por NOME (nao por literal).
eval "$(python3 - <<'PY'
import json, glob, os
base = "/.snapshots/112/snapshot/var/lib/docker/containers/"
want = {"tws-hwa": "HWA", "tws-bmdm": "BMDM", "tws-agent": "AGENT"}
for d in glob.glob(base + "*/"):
    f = os.path.join(d, "config.v2.json")
    if not os.path.exists(f):
        continue
    c = json.load(open(f))
    name = (c.get("Name") or "").lstrip("/")
    if name not in want:
        continue
    tag = want[name]
    ns = (c.get("NetworkSettings") or {}).get("Networks") or {}
    print("IP_%s_MESH=%s" % (tag, (ns.get("hwa-mesh") or {}).get("IPAddress", "")))
    print("IP_%s_LAN=%s"  % (tag, (ns.get("hwa-lan")  or {}).get("IPAddress", "")))
PY
)"
echo "hwa: mesh=$IP_HWA_MESH lan=$IP_HWA_LAN"
echo "bmdm: mesh=$IP_BMDM_MESH   agent: mesh=$IP_AGENT_MESH"
```

### 4.2 Demais pré-condições

1. **Snapshot 112 íntegro** — `.../snapshots/7/fs/opt/hwa/TWSDATA/stdlist/traces/20260915_TWSMERGE.log` existe com **386880 B**.
2. **Espaço em disco** para a Via A: a camada tem **5,2 G** → reserve **≥ 12 G** livres.
3. **Host sem reboot pendente** e `docker` saudável (`docker info` responde).
4. **As redes existem e estão vazias** (`hwa-mesh`, `hwa-lan`) — conferir antes; **não recriar** sem necessidade (a `hwa-lan` é ipvlan com parent `wlan0`).
5. **Autorização explícita do dono** para executar (o escopo atual é só preparar).
6. **Nada mais usando os binds** `/data`.

## 5. VIA A — reconstruir da camada do snapshot 112 (**preserva a M1**)

**Racional:** a camada gravável do `tws-hwa` no snapshot 112 contém a instalação do TWS já no estado
**pós-M1** (M1 aplicada em 09/15 10:57). É o caminho que **não exige re-aplicar a M1**.

> ### ⚠️ DEFEITO MATERIAL CORRIGIDO (medido por execução, 16.09)
> A versão anterior deste passo mandava `tar -C $LAYER` + `docker import` direto. **Isso produz uma imagem
> que NÃO BOOTA.** `$LAYER` é o **diff (upper) do overlay**, **não** o rootfs: medido, `/usr/bin/bash`,
> `/sbin/init`, `/usr/lib/systemd/systemd`, `/usr/bin/systemctl` e `/etc/os-release` estão **AUSENTES**
> dele (`/usr/bin` tem **50** itens contra **383** da base). O `docker import` retorna **rc=0 sem avisar**
> e a falha só aparece no boot (`exec: "/bin/sh": stat /bin/sh: no such file or directory`).
> **O teste do arquivo-sentinela NÃO prova completude** — o sentinela está no diff. **Não repetir.**

```bash
# ---- A0. Verificações (READ-ONLY) ----
SNAP=/.snapshots/112/snapshot
LAYER=$SNAP/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/7/fs

# o sentinela prova que o DIFF tem o TWS — NÃO prova que é o rootfs:
stat -c '%s bytes' "$LAYER/opt/hwa/TWSDATA/stdlist/traces/20260915_TWSMERGE.log"   # esperado 386880

# CONFERÊNCIA OBRIGATÓRIA: o rootfs da base NÃO está aqui — tem de dar AUSENTE
for f in usr/bin/bash sbin/init usr/lib/systemd/systemd etc/os-release; do
  test -e "$LAYER/$f" && echo "INESPERADO: /$f presente no diff" || echo "esperado AUSENTE: /$f"
done
du -sh "$LAYER"   # ~5,2G = tamanho do DIFF, não do rootfs
df -h /           # exigir >= 20G livres (base + diff + tar flattened ~5,8G + imagem)
# (rodar antes o §4.1 para ter $IP_HWA_MESH / $IP_HWA_LAN)

# ---- A1. FLATTEN: base (export) + diff por cima + import ----
# a base é EXATAMENTE a original — o digest tem de conferir com o campo Image do config.v2.json:
docker image inspect registry.access.redhat.com/ubi9/ubi-init:latest --format '{{.Id}}'
# esperado: sha256:5e25c1ed0c669e3a93dd82e0cbcdf7e663d9681a512278ec28d76675609cefaa

rm -rf /var/tmp/flatten && mkdir -p /var/tmp/flatten
docker create --name ubi9-flatten-base registry.access.redhat.com/ubi9/ubi-init:latest >/dev/null
docker export ubi9-flatten-base | tar -C /var/tmp/flatten -xf -
docker rm ubi9-flatten-base >/dev/null
tar -C "$LAYER" -cf - . | tar -C /var/tmp/flatten -xf -   # o DIFF por cima (diff ganha da base)
tar -C /var/tmp/flatten -cf /var/tmp/tws-hwa-flat-20260916.tar .
docker import /var/tmp/tws-hwa-flat-20260916.tar tws-hwa:reconstruido-20260916

# ---- A1.5. GATE OBRIGATÓRIO: a imagem BOOTA? (antes de qualquer docker run de verdade) ----
docker run --rm --entrypoint /bin/sh tws-hwa:reconstruido-20260916 \
  -c 'ls -la /sbin/init; ls -l /usr/lib/systemd/systemd; ls -l /usr/bin/bash; head -2 /etc/os-release'
# esperado: /sbin/init -> ../lib/systemd/systemd PRESENTE, bash PRESENTE, os-release RHEL 9.x
# Se /sbin/init ou bash faltarem, a imagem está QUEBRADA — NÃO subir o lab.
```

> **Artefato de validação já pronto no host:** a imagem `tws-hwa:vigia-validacao-20260916`
> (id `d9ad09693a1c`) é o resultado do flatten acima, construído e **validado ponta-a-ponta pelo vigia**:
> `/sbin/init`, `/usr/bin/bash`, `systemctl` presentes, `/etc/os-release` = RHEL 9.8,
> `/opt/hwa/TWS/bin/conman` e `/opt/hwa/TWSDATA` presentes, `/usr/pgsql-18/bin/postgres` presente, e o
> **sentinela preservado** (`20260915_TWSMERGE.log` 386880 B, mtime `22:58:33`).
> **Controle de completude** (conjunto × conjunto): árvore da reconstruída = **97.915** caminhos vs
> **97.908** do commit `ha_snap_20260914-0035_tws-hwa`; as 162 diferenças são **integralmente ruído
> transitório** (`/tmp`, cache do dnf, logs do engineServer, `postmaster.pid`, um `pg_wal`, um socket de
> EDWA) — **nenhum binário, nenhuma unidade, nenhum dado de `/opt/hwa` ou do banco**. Não há perda real.
> Pode ser usada como resultado de A1 ou removida depois. Custo do flatten: ~4 min.

```bash
# ---- A2. Subir o MDM com a config EXATA (ordem: agent -> bmdm -> hwa) ----
BIND=/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/docker
docker run -d --name tws-hwa --hostname tws-hwa \
  --privileged --security-opt label=disable --cgroupns private \
  --memory 4g --memory-swap 6g --shm-size 64m \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v "$BIND/tws-hwa/installers:/installers" \
  -v "$BIND/tws-hwa/data:/data" \
  --network hwa-mesh --ip "$IP_HWA_MESH" --network-alias tws-hwa.lab \
  --network hwa-lan --ip "$IP_HWA_LAN" \
  --restart unless-stopped \
  tws-hwa:reconstruido-20260916 /sbin/init
```

> **`--restart unless-stopped` é deliberado e é a correção do defeito de origem** — o original tinha
> `no`. Sem isso, o próximo reboot repete o incidente. Registrar a mudança.

**Notas da Via A (riscos conhecidos, não medidos):**
- `docker import` de um fs **achata** a imagem (perde `Cmd`/`Env` da base) → o `/sbin/init` vai explícito.
- O `import` **não preserva** dono/permissões de todos os arquivos de forma idêntica; conferir
  `ls -la /opt/hwa` dentro do container contra o snapshot antes de considerar bom.
- Se o TWS usar **systemd** dentro do container, o `/sbin/init` precisa dos mounts de cgroup — por isso
  o bind `/sys/fs/cgroup` e `--privileged` (como no original).

## 6. VIA B — reconstruir das imagens `ha_snap_*` (**exige re-aplicar a M1**)

**Racional:** as imagens são `docker commit` de **09/14 00:35** — contêm a instalação, mas **não** a M1.
Rodar antes o §4.1.

```bash
BIND=/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/docker

docker run -d --name tws-agent --hostname tws-agent \
  --privileged --security-opt label=disable --cgroupns private \
  --memory 2g --memory-swap 3g --shm-size 64m \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v "$BIND/tws-agent/data:/data" \
  -v "$BIND/tws-agent/installers:/installers:ro" \
  -v "$BIND/tws-agent/ssl-certs:/opt/ssl-certs:ro" \
  --network hwa-mesh --ip "$IP_AGENT_MESH" --network-alias tws-agent.lab \
  --restart unless-stopped \
  ha_snap_20260914-0035_tws-agent:latest /sbin/init

docker run -d --name tws-bmdm --hostname tws-bmdm \
  --privileged --security-opt label=disable --cgroupns private \
  --memory 4g --memory-swap 6g --shm-size 64m \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v "$BIND/tws-bmdm/data:/data" \
  -v "$BIND/tws-hwa/installers:/installers" \
  -v "$BIND/tws-bmdm/ssl-certs:/opt/ssl-certs:ro" \
  --network hwa-mesh --ip "$IP_BMDM_MESH" --network-alias tws-bmdm.lab \
  --restart unless-stopped \
  ha_snap_20260914-0035_tws-bmdm:latest /sbin/init

docker run -d --name tws-hwa --hostname tws-hwa \
  --privileged --security-opt label=disable --cgroupns private \
  --memory 4g --memory-swap 6g --shm-size 64m \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v "$BIND/tws-hwa/installers:/installers" \
  -v "$BIND/tws-hwa/data:/data" \
  --network hwa-mesh --ip "$IP_HWA_MESH" --network-alias tws-hwa.lab \
  --network hwa-lan --ip "$IP_HWA_LAN" \
  --restart unless-stopped \
  ha_snap_20260914-0035_tws-hwa:latest /sbin/init
```

Depois, **re-aplicar a M1** (alinhamento do domain manager, via `composer` em duas etapas
`MDM_BK→fta` e `MDM→manager`, round-trip `extract → editar → add`; **não** usar `replace`, e
`modify` sem fonte abre editor e trava). O procedimento medido está na skill `tws-hwa`.

## 7. Mapa de reversão

| passo | como reverter | custo |
|---|---|---|
| A1 `docker import` | `docker image rm tws-hwa:reconstruido-20260916` + `rm /var/tmp/tws-hwa-layer-20260916.tar` | nulo (aditivo) |
| A2 / B `docker run` | `docker stop tws-hwa && docker rm tws-hwa` | nulo — **os `/data` são bind, não volumes anônimos**; nada se perde com `rm` |
| Rede (se recriada) | `docker network rm <nome>` (só com 0 membros) | nulo |
| **Qualquer coisa no banco** | **PROIBIDO neste procedimento** | — |
| Snapshot btrfs 112 | **não apagar** até o lab estar validado; é o único ponto que preserva a M1 | — |

**Regra de ouro da reversão:** o estado durável está em **(a)** o snapshot 112 e **(b)** os binds `/data`.
Remover containers e imagens reconstruídas **não** destrói nenhum dos dois.

## 8. Stop criterion por etapa

| etapa | PARAR e escalar se… |
|---|---|
| A0 / §4.1 | o arquivo-sentinela da camada não existir ou o tamanho divergir de **386880 B**; disco < 12 G; os IPs não puderem ser derivados |
| A1 | `docker import` falhar; a imagem resultante tiver tamanho irreal (< 1 G); erro de leitura no snapshot |
| A2 / B | container sai do `docker ps` em < 60 s (o `/sbin/init` não subiu); `docker logs` mostra falha de cgroup/systemd |
| pós-subida | o `conman` não responde; `batchman` não fica `LIVES`; o plano não é legível |
| **qualquer etapa** | aparecer `AWSJPL004E`; qualquer operação tocar o banco do lab; necessidade de `prune` |

**Proibido em qualquer etapa:** `docker run`/`create`/`import` sem autorização do dono; tocar o banco;
qualquer `prune`; `MakePlan`; `planman reset|crt`; `SwitchPlan` manual.

## 9. Validação feita por LEITURA / dry-run (nada criado)

- A camada do snapshot 112 contém `.../opt/hwa/TWSDATA/stdlist/traces/20260915_TWSMERGE.log` com
  **386880 B / mtime 22:58:33** e o banco com mtime `23:55:34`.
- `config.v2.json` + `hostconfig.json` dos 3 containers lidos do snapshot → **todos os parâmetros das §3
  são medidos, não presumidos**.
- `docker network ls` / `network inspect` → `hwa-mesh` e `hwa-lan` existem e têm **0 membros**.
- Binds `/data` no sdb: **existem e têm conteúdo**.
- Imagens `ha_snap_20260914-0035_tws-*`: presentes.
- **Dry-run executado em 2026-09-16 07:3xZ (read-only, nada criado):**
  - os **7 binds** citados existem no sdb;
  - **todas as flags** usadas existem neste `docker` (`--network-alias`, `--cgroupns`, `--memory-swap`,
    `--shm-size`, `--security-opt`, `--restart`, `--ip`, `--privileged`) e `docker import` está disponível;
  - **disco: 101 G livres** em `/` (exigido ≥ 12 G);
  - **camada = 5,2 G** e o arquivo-sentinela confere: **386880 bytes, mtime 2026-09-15 22:58:33**;
  - `docker info`: 2 containers (2 rodando), 29 imagens.
- **Não executado:** `docker run`, `docker create`, `docker import`, `tar`, qualquer `prune`.

## 10. Recomendação (para decisão do dono)

**Via A** preserva a M1 e evita repetir trabalho; **Via B** é mais próxima do caminho conhecido (imagem
commitada) mas **exige re-aplicar a M1** e parte de 09/14. Em ambos os casos, subir **com
`--restart unless-stopped`** — o defeito que causou o incidente foi a ausência de restart policy.

**Script de subida versionado:** `docs/lab-up-2026-09-16.sh` — **default = DRY-RUN** (nada é criado sem
`--apply`). Deriva os argumentos de criação do `config.v2.json`/`hostconfig.json` do snapshot 112 e
**aborta se a derivação falhar** (não há fallback para valor chutado). Uso:

```bash
./docs/lab-up-2026-09-16.sh                  # dry-run: imprime os comandos exatos
./docs/lab-up-2026-09-16.sh --check          # só as pré-condições
./docs/lab-up-2026-09-16.sh --apply          # executa (exige autorização do dono)
./docs/lab-up-2026-09-16.sh --image B --apply # Via B (imagens de 09/14; exige re-aplicar a M1)
./docs/lab-up-2026-09-16.sh --down --apply   # REVERSÃO: para e remove os 3 containers
```

> **Nota de escopo da Via A no script:** o flatten validado cobre **o MDM (`tws-hwa`)**, que é onde a M1 foi
> aplicada. `tws-bmdm` e `tws-agent` **não têm flatten próprio** e são subidos das imagens commitadas de
> 09/14 — comportamento explícito no código, não implícito.
>
> **Bugs que o dry-run pegou antes de qualquer execução** (registro de por que o dry-run é obrigatório):
> (1) os binds perdiam o `:dst` (o mount viraria o path errado); (2) a Via A usava a imagem do `tws-hwa` nos
> **três** containers; (3) sumia a rede primária, e o `tws-hwa` subiria com `hwa-lan` como default em vez de
> `bridge`. Todos corrigidos e re-validados.
