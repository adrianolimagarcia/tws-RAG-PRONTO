# Design de Automacao Segura — Allowlist de Acoes por Risk (Contrato R4)

Data: 2026-08-30 | Projeto: HWA/TWS RAG (`G:\projetos\1`)

## 1. Objetivo

Definir como o consumidor Python do RAG executa acoes com seguranca, respeitando
o contrato evidence-first (docs/RAG_EVIDENCE_CONTRACT.md, regra R4): acoes de
risco alto (mutating/destructive/credential_sensitive) NUNCA sao executadas sem
validacao explicita — o modelo apenas *sugere*; a integracao Python valida contra
uma allowlist finita e mapeia para funcoes previamente permitidas.

## 2. Estado atual (base existente)

O release r28-sota ja carrega `data/automation-action-registry.json`
(copiado para o snapshot como `automation-action-registry.json`):

| Aspecto | Valor |
|---|---|
| schema_version | 1.0 |
| execution_model | `structured_action_only` (nao executa texto livre) |
| actions | 39 (read_only=19, mutating=8, destructive=10, credential_sensitive=2) |
| habilitadas | 16 (todas read_only) |
| refusal_schema | JSON estruturado com `refusal`/`confirmation_required`/`executable_action` |
| blocked_patterns | 11 padroes proibidos (arbitrary_shell, curl -k, ;noask, altpass, resetFTA c/ X-Agent, ocli force, etc.) |
| parameter_schemas | schema por acao (required/optional/additional_properties=false) |

Principio ja estabelecido: **nenhuma acao mutating/destructive/credential_sensitive
esta habilitada por default** (enabled=false + confirmation_required=true). O RAG
(inferencia rag_hwa.py) nunca executa comandos — devolve evidencias + risco.

## 3. Arquitetura da camada de execucao

```
[LLM resposta JSON (RAG)]              rag_hwa.py
        |
        v
[Schema Validator]                     valida contra automation-action-registry.json
   - action_name existe? risk? enabled? allowed_origins?
   - parametros casam parameter_schemas? additional_properties=false
        |
        v
[Risk Gate]                            risco + politica
   read_only           -> executa direto
   mutating            -> confirmation_required=true -> NUNCA auto
   destructive         -> BLOQUEADO (blocked) salvo aprovacao manual explicita
   credential_sensitive-> BLOQUEADO (nunca logado/exposto)
        |
        v
[Action Dispatcher]    mapeia action_name -> funcao Python pre-registrada
   (dicionario estatico, sem eval/exec de string)
        |
        v
[Origin/Version Gate]  allowed_origins (mdm/fta/composer) + version_scope
```

### Fluxo de decisao (pseudo)

```
def execute_safely(action_name, params, origin, version, approval=None):
    action = registry.actions[action_name]            # ausente -> refusal
    if not action.enabled:                            # disabled -> refusal
        return refusal("mutating_action_disabled")
    if origin not in action.allowed_origins:          # origem -> refusal
        return refusal("origin_not_allowed")
    validate_params(action.parameter_schemas, params) # schema -> refusal
    if action.risk == "read_only":
        return dispatch(action_name, params)
    if action.risk == "mutating" and action.confirmation_required:
        if approval is None:
            return refusal("confirmation_required")
        # aprovacao explicita do humano (token de aprovacao fora do LLM)
    if action.risk in ("destructive", "credential_sensitive"):
        return refusal("destructive_action_blocked")  # so manual, fora do RAG
    return dispatch(action_name, params)
```

## 4. Regra de derivacao: risk do chunk -> politica de execucao

O chunk RAG carrega o campo `risk` (de data/rag/chunks.jsonl). A regra:

| risk do chunk | Acao permitida | Confirmacao | Log |
|---|---|---|---|
| read_only | sim | nao | info |
| mutating | sim (se enabled) | **sim, humana obrigatoria** | warn + quem aprovou |
| destructive | **nao** (bloqueado) | so manual fora do pipeline | error + bloqueio |
| credential_sensitive | **nao** (nunca exposto) | nao aplicavel | error + redacao |

Validacao: `data/rag/index_meta.json statistics.by_risk` confirma a distribuicao
no indice atual (read_only=1070, mutating=249, destructive=61, credential_sensitive=64).

## 5. Consequencia para o pipeline RAG (rag_hwa.py)

- O RAG continua *sugerindo* (nunca executando): saida JSON com `evidence_ids`,
  `sources`, `sufficiency` e o `risk` do chunk viajando junto (contrato R4).
- Para queries de risco alto, o prompt ja instrui recusa (validado no corpus de
  respostas: D1 recusa adversarial 100% correto em 630 casos de alto risco).
- A camada `execute_safely` e um modulo NOVO em `scripts/automation_gate.py`
  (nao existe hoje — o registry e dados estaticos sem executor).
- O dispatcher mapeia somente as 16 acoes habilitadas; qualquer outra acao
  retorna refusal estruturado (nunca executa string de comando).

## 6. Entregaveis

1. `scripts/automation_gate.py` — validador + risk gate + dispatcher (novo).
2. `scripts/automation_actions/` — funcoes Python por action_name (read_only
   habilitadas; mutating stubs que exigem approval token).
3. Testes (`scripts/test_automation_gate.py`):
   - action inexistente -> refusal `mutating_action_disabled`
   - read_only valido -> executa
   - mutating sem approval -> refusal `confirmation_required`
   - destructive -> refusal `destructive_action_blocked` (mesmo com approval)
   - parametro extra (additional_properties) -> refusal `invalid_parameter`
   - blocked_pattern (ex. `;noask`, `curl -k`) rejeitado mesmo se action valida
4. Doc de politica de aprovacao (quem pode aprovar mutating, fora do escopo LLM).

## 7. Fora de escopo (nao fazer nesta iteracao)

- NAO habilitar mutating/destructive por default.
- NAO aceitar aprovacao vinda do proprio LLM (aprovacao e humana, canal separado).
- NAO executar comandos a partir de texto livre (structured_action_only).
- NAO logar credential_sensitive (redacao obrigatoria).

## 8. Referencias

- Contrato: docs/RAG_EVIDENCE_CONTRACT.md (R1-R5)
- Registry: data/automation-action-registry.json (39 acoes, schema v1.0)
- Inferencia: scripts/rag_hwa.py (evidence-first, sem execucao)
- Validacao de risco no corpus: data/rag/index_meta.json statistics.by_risk
