# Formato de Sessão de Laboratório (P3)

Cada sessão de laboratório reproduzível gera evidência estruturada para o
dataset. Este formato é obrigatório para novas sessões, especialmente para
operações mutantes/destrutivas, incidentes e troubleshooting.

## Arquivo de evidência

Formato: `data/evidence/lab-validation-<YYYY-MM-DD>-<slug>.jsonl`
Um registro por claim validado, com o schema abaixo.

## Schema do registro

```json
{
  "claim_id": "hwa-lab-10.2.8-<slug>-<nnnn>",
  "command": "comando exato executado",
  "preconditions": [
    "versão do produto (ex.: 10.2.8.00)",
    "SO/plataforma (ex.: RHEL 8 no WSL2)",
    "workstation/broker (ex.: MDMDA)",
    "usuário/autorização (ex.: wauser, enListSecChk=no)",
    "estado inicial do objeto (ex.: job READY, plano run 12)"
  ],
  "sanitized_output": "saída pós-anonimização (remover credenciais, IPs, hosts, usuários reais)",
  "result": "SUCCESS | FAIL | REJECTED | PARTIAL",
  "product_version": "10.2.8",
  "platform": "Distributed (Linux/WSL2)",
  "risk": "read_only | mutating | destructive | credential_sensitive",
  "reversibility": "procedimento de reversão aplicável ou NA",
  "stop_criterion": "condição para interromper a execução",
  "evidence_url": "URL oficial relacionada, quando aplicável",
  "performed_at": "ISO-8601",
  "performed_by": "operador do laboratório",
  "observations": "fatos observados, incluindo divergências documentação x implementação"
}
```

## Regras

1. **Nunca** incluir credenciais, IPs reais, hosts internos ou usuários reais
   no arquivo — anonimizar antes de gravar.
2. Registrar comando **exato** (reproduzível) e pré-condições completas.
3. Para operações destrutivas: registrar estado anterior (backup/snapshot),
   resultado e reversibilidade; interromper se `stop_criterion` for atingido.
4. Divergências doc x implementação viram **claim nova** ou atualização da
   claim existente (com status adequado: `verified`, `version_dependent`).
5. Toda claim sensível nova exige **duas evidências independentes** OU uma
   fonte oficial + uma execução de laboratório
   (`validate_evidence.py --require-corroboration`).

## Prioridade de execução

1. Operações mutantes/destrutivas (composer add/delete, jnextplan, resetFTA,
   conman manipulação de jobs) com confirmação e reversão.
2. Incidentes e troubleshooting (mensagens AWS*, EQQ*, EEL*).
3. DWC/REST API v2, OCLI, bancos, HA, upgrades.

## Referência

- Validador: `scripts/validate_evidence.py` (inclui `observed_in_lab`).
- Claims de lab: prefixo `hwa-lab-*` (ver `data/evidence/lab-claims.jsonl`).
- Runbook de sessões passadas: `data/runbooks/hwa-10.2.8-wsl-lab.md`.
