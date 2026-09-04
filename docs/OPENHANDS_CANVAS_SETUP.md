# OpenHands Agent Canvas — Control Center Multi-Agente (Ubuntu/WSL2 + Windows)

Guia completo de instalação e operação do OpenHands Agent Canvas como hub que
controla Hermes (Ubuntu/WSL2), OpenCode (Windows) e CowAgent (Ubuntu/WSL2).

Estado: **FUNCIONAL e verificado E2E** (PONG) para Hermes e OpenCode.
Criado em: 2026-08-24.

---

## 1. Arquitetura

```
UBUNTU (WSL2)                                         WINDOWS
┌────────────────────────────────────────────┐         ┌──────────────────────────────────┐
│ OpenHands Agent Canvas (systemd, :8000)    │         │ Agent Server (:8100)             │
│  └─ Agent Server local (:8000)             │         │  (venv Python, openhands-agent-  │
│      └─ ACP subprocess: hermes acp         │         │   server 1.43.1)                 │
│                                            │         │  └─ ACP subprocess: opencode acp │
│ Hermes Agent v0.20.5 (/root/.local/bin)    │         │     --pure + XDG_CONFIG_HOME     │
│                                            │         │                                 │
│ CowAgent v2.1.7 (rodando, sem ACP)         │         │ OpenCode v1.18.18 (npm)          │
│  → via CLI/terminal, não ACP               │         │                                 │
└────────────────────────────────────────────┘         └──────────────────────────────────┘
        ▲                                                       ▲
        └── HTTP/WS (172.27.96.1:8100) ────────────────────────┘
            (WSL → host Windows via gateway vEthernet)
```

- **Canvas** = frontend (localhost:8000) + Agent Server local. Fala com agentes
  ACP por subprocesso (stdio JSON-RPC) na mesma máquina, ou com Agent Servers
  remotos via HTTP/WebSocket.
- **Hermes e OpenCode** falam ACP → controlados diretamente.
- **CowAgent** não implementa ACP → uso via CLI/terminal ou canais próprios.

---

## 2. Pré-requisitos / Estado do ambiente

| Item | Local | Estado |
|---|---|---|
| WSL2 Ubuntu 22.04 | Windows | rodando (root) |
| Docker Engine 29.7.2 | WSL | instalado (só p/ futuro; Canvas usa npm nativo) |
| uv 0.12.5 | WSL `/root/.local/bin/uv` | instalado |
| Node 26 (WSL) / 24 (Windows) | ambos | instalado |
| Python 3.13 (Windows venv) | `Temp\opencode\ohsrv` | instalado |
| OpenHands Agent Canvas 1.15.0 | WSL (npm global) | serviço systemd **active** |
| Hermes 0.20.5 | WSL `/root/.local/bin/hermes` | configurado (~/.hermes/.env) |
| OpenCode 1.18.18 | Windows (npm) | ACP validado |
| CowAgent 2.1.7 | `/mnt/g/projetos/1/CowAgent` | rodando (PID próprio) |

> ⚠️ Quirk WSL: o `$HOME` vaza do Windows (`C:\Users\User`). SEMPRE exporte
> `HOME=/root` em scripts WSL. Use scripts em arquivo (não `bash -c '...'` com
> aspas duplas) — o `wsl.exe` re-parseia aspas e quebra pipes/greps.

---

## 3. Instalação — WSL Ubuntu

### 3.1 Docker Engine (opcional, para sandbox futuro)

```bash
curl -fsSL https://get.docker.com | sh
systemctl enable --now docker
docker run --rm hello-world   # valida
```

### 3.2 uv

```bash
export HOME=/root
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH=/root/.local/bin:$PATH
uv --version   # 0.12.5
```

### 3.3 OpenHands Agent Canvas (instalação nativa, sem sandbox)

> Escolha nativa (não Docker) porque o Canvas precisa lançar os agentes ACP
> (`hermes acp`, `opencode acp`) como **subprocessos na mesma máquina**.

```bash
npm install -g @openhands/agent-canvas   # 1.15.0
agent-canvas --help
```

### 3.4 Serviço systemd

`/etc/systemd/system/agent-canvas.service`:

```ini
[Unit]
Description=OpenHands Agent Canvas
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
Environment=HOME=/root
Environment=PATH=/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
WorkingDirectory=/root
ExecStart=/usr/local/bin/agent-canvas
Restart=on-failure
RestartSec=5
TimeoutStartSec=300

[Install]
WantedBy=multi-user.target
```

```bash
cp agent-canvas.service /etc/systemd/system/
systemctl daemon-reload && systemctl enable agent-canvas && systemctl start agent-canvas
systemctl is-active agent-canvas   # active
journalctl -u agent-canvas -f      # logs (1º boot baixa o agent-server Python via uv)
```

UI: **http://localhost:8000** (npm launcher usa a raiz, não /canvas).

### 3.5 Configuração via API (chave em `/root/.openhands/agent-canvas/api-key.txt`)

```bash
KEY=$(cat /root/.openhands/agent-canvas/api-key.txt)
AUTH="X-Session-API-Key: $KEY"
BASE=http://localhost:8000
OR_KEY="sk-or-v1-..."   # chave OpenRouter reutilizada

# 1. Perfil LLM (OpenRouter) — para o agente OpenHands + títulos
curl -X POST -H "$AUTH" -H "Content-Type: application/json" \
  -d "{\"llm\":{\"model\":\"openrouter/anthropic/claude-sonnet-4.5\",\"api_key\":\"$OR_KEY\",\"auth_type\":\"api_key\"},\"include_secrets\":true}" \
  "$BASE/api/profiles/openrouter"
curl -X POST -H "$AUTH" "$BASE/api/profiles/openrouter/activate"

# 2. Agente ACP → Hermes
curl -X PATCH -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"agent_settings_diff":{"agent_kind":"acp","acp_server":"custom","acp_command":["/root/.local/bin/hermes","acp"]}}' \
  "$BASE/api/settings"
```

Teste E2E local (Hermes):

```bash
curl -X POST -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"workspace":{"working_dir":"/root","kind":"LocalWorkspace"},
       "agent_settings":{"agent_kind":"acp","acp_server":"custom",
         "acp_command":["/root/.local/bin/hermes","acp"]},
       "initial_message":{"content":[{"text":"Responda apenas com a palavra PONG"}],"role":"user"}}' \
  "$BASE/api/conversations"
# poll: GET /api/conversations/{id}/agent_final_response  → {"response":"PONG"}
```

---

## 4. Instalação — Windows (OpenCode via Agent Server remoto)

### 4.1 Venv + pacotes

```powershell
py -3.13 -m venv C:\Users\User\AppData\Local\Temp\opencode\ohsrv
& "C:\Users\User\AppData\Local\Temp\opencode\ohsrv\Scripts\python.exe" -m pip install -U `
  openhands-sdk openhands-tools openhands-workspace openhands-agent-server
```

### 4.2 Chaves persistentes

`C:\Users\User\AppData\Local\Temp\opencode\ohsrv-keys.txt`:
```
OH_SESSION_API_KEYS_0=<hex 64>
OH_SECRET_KEY=<hex 64>
```

### 4.3 Subir o Agent Server (porta 8100)

```powershell
$env:OH_SESSION_API_KEYS_0 = (Get-Content ohsrv-keys.txt | ? {$_ -match 'OH_SESSION_API_KEYS_0='}) -replace '.*=',''
$env:OH_SECRET_KEY = (Get-Content ohsrv-keys.txt | ? {$_ -match 'OH_SECRET_KEY='}) -replace '.*=',''
$env:OH_ALLOW_CORS_ORIGINS_0 = "http://localhost:8000"
Start-Process -FilePath "C:\Users\User\AppData\Local\Temp\opencode\ohsrv\Scripts\python.exe" `
  -ArgumentList "-m","openhands.agent_server","--host","0.0.0.0","--port","8100" `
  -RedirectStandardOutput ohsrv.out.log -RedirectStandardError ohsrv.err.log -WindowStyle Hidden
# valida: Invoke-RestMethod http://127.0.0.1:8100/health → {"status":"ok"}
```

> Segurança: porta 8100 exposta na rede — limite a hosts de confiança/firewall.

### 4.4 Configurar o backend Windows (via WSL → 172.27.96.1)

```bash
KEY=$(grep OH_SESSION_API_KEYS_0 /mnt/c/Users/User/AppData/Local/Temp/opencode/ohsrv-keys.txt | cut -d= -f2)
BASE=http://172.27.96.1:8100
OPENCODE_EXE='C:\Users\User\AppData\Roaming\npm\node_modules\.opencode-ai-fgTcxTup\node_modules\opencode-windows-x64\bin\opencode.exe'

# LLM do agent-server (títulos etc.)
curl -X PATCH -H "X-Session-API-Key: $KEY" -H "Content-Type: application/json" \
  -d "{\"agent_settings_diff\":{\"llm\":{\"model\":\"openrouter/anthropic/claude-sonnet-4.5\",\"api_key\":\"$OR_KEY\",\"auth_type\":\"api_key\"}}}" \
  "$BASE/api/settings"

# Comando ACP com --pure (CRÍTICO — ver seção 6)
curl -X PATCH -H "X-Session-API-Key: $KEY" -H "Content-Type: application/json" \
  -d "{\"agent_settings_diff\":{\"acp_command\":[\"$OPENCODE_EXE\",\"acp\",\"--pure\"]}}" \
  "$BASE/api/settings"

# Secret XDG_CONFIG_HOME (env exportado para o subprocesso opencode)
curl -X PUT -H "X-Session-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"name":"XDG_CONFIG_HOME","value":"C:/Users/User/AppData/Local/Temp/opencode/xdg-acp"}' \
  "$BASE/api/settings/secrets"
```

### 4.5 Config limpa do opencode (sem skills/plugins que penduram)

`C:\Users\User\AppData\Local\Temp\opencode\xdg-acp\opencode\opencode.json`:
modelo + providers (a6, cheap2, nvidia1, qubax) + `"mcp":{}` + `"plugin":[]`.
Sem skills, sem plugins → ACP não trava.

### 4.6 Teste E2E (do WSL)

Igual ao 3.5, mas `BASE=http://172.27.96.1:8100`, workspace
`C:\Users\User\AppData\Local\Temp\opencode\proj`, e o opencode responde **PONG**.
(`status: finished` + ActionEvent/ObservationEvent nos eventos.)

---

## 5. Conectar no Canvas (UI) e usar

O registro de backends fica no **localStorage do navegador** (não é API).
Para ver o backend "opencode-win" na UI:

1. Abra http://localhost:8000 (npm launcher) — pule o onboarding se aparecer.
2. Seletor de backend (combobox com "Local") → **Manage Backends** → **Add Backend**:
   - Nome: `opencode-win`
   - Host: `http://172.27.96.1:8100`
   - API key: `$OH_SESSION_API_KEYS_0`
3. Salvar e selecionar. Conversas novas rodam no backend selecionado
   (settings/LLM/MCP são por backend).

APIs úteis (com `X-Session-API-Key`):
- `GET/PATCH /api/settings` — config do agente (agent_kind, acp_command, llm)
- `GET/PUT/DELETE /api/settings/secrets[/{name}]` — secrets → env do subprocesso
- `POST /api/conversations` — criar (workspace + agent_settings + initial_message)
- `GET /api/conversations/{id}/agent_final_response` — resposta final
- `GET /api/conversations/{id}/events/search?limit=50` — eventos
- `POST /api/profiles/{name}` + `/activate` — perfis LLM

---

## 6. Troubleshooting

### opencode ACP trava em `new_session` ("init count=11")
**Causa**: skills/plugins do `~/.config/opencode` do usuário penduram o bootstrap
da sessão ACP (reproduzido isoladamente; com `XDG_CONFIG_HOME` limpo funciona).
**Fix**: `opencode acp --pure` + env `XDG_CONFIG_HOME` → config limpa com os
providers do usuário (sem skills/plugins). A secret com o mesmo nome do env var
é exportada para o subprocesso pelo agent-server.

### "Error from provider (Console): Endpoint is unavailable"
opencode sem modelo definido na sessão ACP → fallback "Console". Definir
`"model"` na config limpa (ex: `a6/deepseek-v4-flash`).

### litellm "LLM Provider NOT provided" com acp_model
Não usar `acp_model` com ids de providers custom do opencode (a6/...) — o
agent-server tenta usar como modelo litellm. Deixar `acp_model` nulo; o modelo
do opencode vem da config limpa.

### "Missing credentials" no agent-server
Configurar `llm` (model + api_key) no PATCH /api/settings DO backend em uso
(por backend). Conversas que passam `agent_settings` próprio precisam incluir
o `llm`.

### auth 401 na API
Header `X-Session-API-Key`, não Bearer. Chave em
`/root/.openhands/agent-canvas/api-key.txt` (local) ou `ohsrv-keys.txt` (Windows).

### $HOME errado no WSL / quoting quebrado
`export HOME=/root`; use scripts `.sh` em arquivo, nunca `bash -c '...'` com
aspas duplas (wsl.exe re-parseia e quebra `|`, `"`, `&`).

---

## 7. Comandos úteis

| Ação | Comando |
|---|---|
| Status Canvas | `wsl -d Ubuntu -- systemctl is-active agent-canvas` |
| Logs Canvas | `wsl -d Ubuntu -- journalctl -u agent-canvas -f` |
| Restart Canvas | `wsl -d Ubuntu -- systemctl restart agent-canvas` |
| Status Agent Server Win | `Get-NetTCPConnection -LocalPort 8100` |
| Logs Agent Server Win | `Get-Content Temp\opencode\ohsrv.err.log -Tail 50` |
| Hermes CLI | `wsl -d Ubuntu -- bash -c 'export HOME=/root; hermes'` |
| CowAgent | `wsl -d Ubuntu -- bash -c 'export HOME=/root; cow status'` (já ativo) |
