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

```bash
# ---- A0. Verificações (READ-ONLY, sem criar nada) ----
SNAP=/.snapshots/112/snapshot
LAYER=$SNAP/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/7/fs
test -f "$LAYER/opt/hwa/TWSDATA/stdlist/traces/20260915_TWSMERGE.log" && echo "camada OK"
du -sh "$LAYER"      # esperado ~5,2G
df -h /              # exigir >= 12G livres
# (rodar antes o §4.1 para ter $IP_HWA_MESH / $IP_HWA_LAN)

# ---- A1. Materializar a camada como imagem (CRIA imagem; não cria container) ----
tar -C "$LAYER" -cf /var/tmp/tws-hwa-layer-20260916.tar .
docker import /var/tmp/tws-hwa-layer-20260916.tar tws-hwa:reconstruido-20260916
docker image inspect tws-hwa:reconstruido-20260916 --format '{{.Size}}'

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
