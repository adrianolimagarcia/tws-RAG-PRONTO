# Fix — Plugin opencode-antigravity-auth (interrupções de sessão) — 2026-08-29

## Resultado

**Config hardening + pin de versão aplicados** no plugin
`opencode-antigravity-auth@1.6.0` (instalado em `~/.config/opencode/node_modules/`).
A causa raiz das interrupções frequentes de sessão é **múltipla** — não é um
único bug, mas 5 fatores somados que foram mitigados por configuração (o pacote
compilado não foi alterado). Backups completos criados antes de qualquer edição.

## Sintoma

Sessões do opencode eram interrompidas com frequência ao usar o plugin de auth
Antigravity (modelos `antigravity-*` e `gemini-*`).

## Diagnóstico

### Evidência primária (log de debug 2026-08-24)

`%APPDATA%\opencode\antigravity-logs\antigravity-debug-2026-08-24T23-21-38-244Z.log`

- `403 PERMISSION_DENIED` / `SUBSCRIPTION_REQUIRED` (#3501) em
  `cloudaicompanion.googleapis.com` — a conta `adrianolimagarcia@gmail.com`
  **não possui licença** do produto (Code Assist/Antigravity).
- `Response 200 OK` no fallback Gemini CLI
  (`generativelanguage.googleapis.com` / `daily-cloudcode-pa.sandbox.googleapis.com`)
  — o fallback funciona, mas **toda request paga um 403 antes** (+latência,
  +tokens, +superfície de falha).
- `[QuotaFetch] START` a cada 15min (refresh de quota em background).

### Análise de código (dist v1.6.0)

| # | Causa | Onde | Efeito |
|---|-------|------|--------|
| 1 | Conta sem licença Antigravity → 403 determinístico no caminho `antigravity` | log; `plugin.js:1801-1829` (403 → próximo endpoint) | quando todos os endpoints falham, o erro cru chega ao opencode → `session.error` |
| 2 | **`auto_resume: true` no `DEFAULT_CONFIG`** (schema zod diz `default(false)` — discrepância real) | `schema.js:391` vs `schema.js:128`; `plugin.js:1075` | o session-recovery fazia `client.session.abort()` + injeta `tool_result` sintéticos + **auto-envia "continue"** → loop de auto-continuação |
| 3 | **Conflito entre plugins no evento `session.error`**: antigravity (abort+inject+resume) e `oh-my-openagent@4.19.4` (todo-continuation + atlas, ambos também injetam continuations) | `recovery.js:268-373`; `oh-my-openagent/dist/index.js:89328, 95766, 115925` | dois plugins reagindo ao mesmo erro → duplo abort/injeção → interrupções visíveis |
| 4 | `auto_update: true` + `invalidatePackage()` — **apaga o pacote do cache em runtime** (config usava `@latest`) | `cache.js:33-42`; `hooks/auto-update-checker/index.js:76-78` | risco de reload/quebra do plugin durante a sessão |
| 5 | Retries agressivos: `empty_response_max_attempts: 4` (2s cada), espera de rate-limit até **300s**, `proactive_token_refresh` a cada 5min, `quota_refresh_interval_minutes` 15min | `schema.js` defaults | hangs longos que parecem interrupção |

## Fix aplicado

### 1. Config hardening — `~/.config/opencode/antigravity.json` (novo)

```json
{
  "$schema": "https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/assets/antigravity.schema.json",
  "auto_resume": false,
  "auto_update": false,
  "empty_response_max_attempts": 2,
  "empty_response_retry_delay_ms": 2000,
  "default_retry_after_seconds": 30,
  "max_backoff_seconds": 30,
  "max_rate_limit_wait_seconds": 30,
  "proactive_token_refresh": false,
  "quota_refresh_interval_minutes": 0,
  "request_jitter_max_ms": 0
}
```

Decisões de configuração:

- `auto_resume: false` — elimina o auto-"continue" pós-recovery (causa #2).
- `session_recovery` **mantido `true`** — com `auto_resume: false` o recovery
  apenas repara (toast + correção) sem sequestrar a sessão (causa #3 mitigada).
- `auto_update: false` + pin de versão — desativa o `invalidatePackage()` em
  runtime (causa #4).
- `max_rate_limit_wait_seconds: 30` (era 300) — fail-fast em vez de hang de 5min.
- `empty_response_max_attempts: 2` (era 4) — menos retries de resposta vazia.
- `proactive_token_refresh: false` e `quota_refresh_interval_minutes: 0` —
  menos churn de rede em background (token renova on-demand no request path).

### 2. Pin de versão — `opencode.jsonc`

```
"opencode-antigravity-auth@latest" → "opencode-antigravity-auth@1.6.0"
```

Com `auto_update: false`, o auto-update checker vira no-op (no fetch npm, no
`invalidatePackage`). Versão instalada = versão latest (1.6.0), sem perda.

### 3. Backups (criados antes de qualquer edição)

| Backup | Conteúdo |
|--------|----------|
| `~/.config/opencode/backups/opencode-antigravity-auth-20260829-114943/` | pacote completo (283 arquivos, 1.58MB) |
| `~/.config/opencode/opencode.jsonc.bak-antigravity-20260829-115522` | config opencode pré-edição |
| `~/.config/opencode/antigravity.json.bak-20260829-115522` | config antigravity pré-edição |

## Verificação (harness)

| Gate | Método | Resultado |
|------|--------|-----------|
| GATE1 | `AntigravityConfigSchema.partial().safeParse()` (zod do próprio plugin) | ✅ `VALID: true` |
| GATE2 | merge `DEFAULT_CONFIG` + override, valores efetivos conferidos | ✅ `auto_resume=false`, `auto_update=false`, etc. |
| GATE3 | parse JSONC do `opencode.jsonc` (stripJsonComments) | ✅ plugins: `["oh-my-openagent@latest", "opencode-antigravity-auth@1.6.0"]` |
| GATE4 | import standalone do `dist/index.js` | N/A — directory-import exige loader do opencode (não é falha) |
| Pesquisa externa | Perplexity (6 fontes: GitHub NoeFabris, troubleshooting oficial, issues oh-my-openagent) | corrobora: auth stale + conflito de plugins + rate limits como causas conhecidas |

## Como monitorar após restart

1. **Reiniciar o opencode** — a config é lida no boot.
2. Opcional: `OPENCODE_ANTIGRAVITY_DEBUG=1` (ou `debug: true` na config) para
   log em `%APPDATA%\opencode\antigravity-logs\`.
3. Sinais de sucesso: ausência dos toasts "Tool Crash Recovery"/"Session
   Recovered", sem auto-"continue" não solicitado, sem fetch npm no startup,
   requests respondendo direto no caminho Gemini CLI.
4. Se persistir instabilidade, candidatos seguintes:
   - `session_recovery: false` (desliga o recovery do antigravity por completo,
     deixando só o do oh-my-openagent).
   - Remover o prefixo `antigravity-` dos modelos Gemini no `opencode.jsonc`
     (rota Gemini CLI direta, eliminando o 403 inicial por request) — requer
     que a conta tenha quota Gemini API (evidência: fallback retornava 200).

## Patch no dist (2026-08-29 — após restart, evidência de bypass)

> ⚠️ **Local correto dos patches — DOIS locais**: o opencode **CLI** carrega do
> cache `~/.cache/opencode/packages/opencode-antigravity-auth@1.6.0/node_modules/...`
> e o opencode **Desktop 1.18.25** carrega de
> `~/.config/opencode/node_modules/opencode-antigravity-auth` — cópias
> SEPARADAS. Todos os 3 patches foram aplicados nos DOIS locais.

### Validação OAuth confirmada (2026-08-29 16:13)

Teste real via CLI (`opencode run --model google/antigravity-gemini-3-flash`):

```
POST https://daily-cloudcode-pa.sandbox.googleapis.com/v1internal:streamGenerateContent  (Code Assist sandbox)
  Original URL: generativelanguage.googleapis.com/v1beta/models/antigravity-gemini-3-flash
  Headers: { "authorization": "[redacted]", "x-goog-api-key": "", 
             "user-agent": "antigravity/2.0.6 win32/arm64",
             "x-session-affinity": "ses_...", "x-session-id": "ses_..." }
  Body: {"project":"gen-lang-client-0256516260", ...}   ← projeto da conta Google
  → Response 200 OK (2356ms)
```

**Prova do OAuth**: `authorization` Bearer presente + `x-goog-api-key` VAZIO
(não é API key) + endpoint Code Assist sandbox (mesmo do IDE) + projeto da
conta + 200 OK. O request sai autenticado como a conta Google via OAuth, não
via API key.

Após o restart, o log do opencode revelou o erro real (Desktop v1.18.25):

```
15:44:57 ERROR process ... error="Google Generative AI API key is missing..."
   stack: AI_LoadAPIKeyError at loadApiKey8 ... at GoogleGenerativeAILanguageModel.doStream
          at getHeaders (app.asar/out/main/chunks/node-BBwF64dM.js)
```

### Causa raiz (v1.18.25)

O **@ai-sdk/google embutido no Desktop 1.18.25** passou a **validar o apiKey no
`getHeaders()`** (`loadApiKey` → `!apiKey` → `AI_LoadAPIKeyError`). O plugin
fornecia `apiKey: ""` (vazia) no auth loader — que funcionava nas versões
anteriores do Desktop (1.18.18–1.18.23) mas agora lança o erro **antes** de
qualquer fetch custom. O stack confirma: `GoogleGenerativeAILanguageModel.doStream
→ getHeaders → loadApiKey` — o provider é instanciado sem apiKey válida.

### Patches aplicados no cache (v1.6.0 instalado)

**Patch 1 — `dist/src/plugin/request.js` (`isGenerativeLanguageRequest`):**
aceita `Request` object além de string URL (robustez de interceptação):

```js
export function isGenerativeLanguageRequest(input) {
    if (typeof input === "string") {
        return input.includes("generativelanguage.googleapis.com");
    }
    if (input instanceof Request) {
        try {
            return input.url.includes("generativelanguage.googleapis.com");
        }
        catch {
            return false;
        }
    }
    return false;
}
```

**Patch 2 — `dist/src/plugin.js` (bypass não-OAuth):** erro claro em vez de
`return fetch(input, init)` que sempre falhava com `apiKey: ""`.

**Patch 3 — `dist/src/plugin.js` (apiKey placeholder) — o fix do v1.18.25:**
`apiKey: ""` → `apiKey: "antigravity-oauth-placeholder"` no retorno do auth
loader. O `loadApiKey` do SDK aceita (não-falsy) e o fetch custom do plugin
reescreve os headers com o OAuth real (`Authorization: Bearer` + `x-goog-api-key: ""`),
então a key fake **nunca chega ao Google**. Se algum request não for interceptado,
o Google retorna 401 claro (melhor que "API key missing" confuso).

### Validação

- `node --check`: OK nos 2 arquivos.
- Teste funcional `isGenerativeLanguageRequest` (7 casos): string → intercepta;
  **Request object → intercepta (novo)**; não-google/null → não intercepta. ✅
- Backup pré-patch do cache:
  `~/.cache/opencode/packages/opencode-antigravity-auth@1.6.0.bak-20260829-125032/`.

> ⚠️ Nota de durabilidade: patches em `dist/` são **sobrescritos na próxima
> reinstalação** do pacote (ex.: se o opencode reinstalar o plugin). Reaplique
> os 3 patches se o erro "API key is missing" voltar.

## Limitações

- **Não resolvível por config/patch**: a falta de licença Antigravity/Code Assist
  na conta Google. O sandbox diário cobre (mesmo endpoint do IDE, capacidade via
  conta logada), mas o endpoint de produção (`cloudcode-pa.googleapis.com`)
  permanece 403 enquanto a conta não tiver licença.

## Confirmação de conta (2026-08-29)

Verificado via CDP (porta 9223) no Antigravity IDE v1.107.0 (Electron 39/Chrome 142):

- `state.vscdb` do IDE contém OAuth state do Google (`oauthToken` → protobuf
  `authStateWithContacts`) — **o IDE está logado** com uma conta Google, mas o
  email fica encriptado (safeStorage/DPAPI), não legível por fora.
- O fork **não expõe avatar** de conta na activity/status bar (diferente do VS
  Code padrão); o painel de conta fica em Settings → Antigravity.
- **Usuário confirmou visualmente**: a conta do IDE é a **mesma** do plugin
  (`adrianolimagarcia@gmail.com`).

**Conclusão**: não há conta com licença disponível em lugar nenhum. IDE e plugin
usam a mesma conta sem licença → ambos operam no sandbox diário com capacidade
limitada (cooldown ~20s no log). O 403 do prod é o teto real da conta; nenhum
ajuste de plugin ou config muda isso — a única via é uma licença Code Assist
(admin/Workspace) ou billing no projeto Google Cloud.

## Cópia portátil do plugin (2026-08-29)

Pasta **`antigravity-plugin/`** na raiz do projeto contém:

- `opencode-antigravity-auth/` — pacote v1.6.0 **com os 3 patches aplicados**
  (instalável via `file://` em outra IDE/máquina)
- `patches/` — diffs unificados dos patches (01 e 02)
- `config/antigravity.json` — config endurecida de referência
- `apply_patches.ps1` — script de reaplicação (testado; auto-detecta o cache,
  faz backup, aplica e valida)
- `README.md` — instruções de instalação/reuso em outra IDE

Ver `antigravity-plugin/README.md` para o passo a passo completo.

## Registro

- Memória: salvo em mem0 (`user_id=default`, tags `opencode/antigravity/plugin`).
- Anytype indisponível (timeouts MCP) no momento da edição — pendente re-sync.
- Data: 2026-08-29. Autor: sessão Sisyphus.
