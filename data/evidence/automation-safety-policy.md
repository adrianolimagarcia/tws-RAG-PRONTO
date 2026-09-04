# HWA/TWS Automation Safety Policy

This dataset supports instruction following and future automation. The model must
not receive unrestricted shell access or execute arbitrary conman, composer, curl,
or REST commands.

## Execution Boundary

- The model proposes a structured action from a finite allowlist.
- Deterministic application code validates version, platform, target, permissions,
  parameters, and policy before execution.
- Credentials remain in a secret manager or environment variables and are never
  supplied in prompts, SFT records, logs, or model output.
- The executor records an audit event before and after every attempted action.
- The model receives the structured result and must not infer success.

## Action Classes

| Class | Examples | Policy |
|---|---|---|
| `read_only` | `showjobs`, `showscheds`, Composer `display`, Composer `list`, syntax validation | Allow only with a registered action, validated scope, and version-compatible evidence. |
| `mutating` | `rerun`, `submit sched`, `release job`, centralized agent update | Require an exact target, impact preview where available, authorization check, and an explicit confirmation bound to the proposed action. |
| `destructive` | `cancel job`, `cancel sched`, Composer `delete` | Deny by default. Permit only through a separately enabled workflow with a fully specified target, authorization check, human approval, and immutable audit record. Never use `;noask`. |
| `credential_sensitive` | REST authentication, certificate or TLS changes | Do not expose credentials or disable certificate verification. Use managed secrets and a trusted TLS configuration. |

## Required Action Contract

```json
{
  "action": "show_jobs",
  "version": "10.2.0",
  "platform": "distributed",
  "parameters": {
    "selector": "@#@.@"
  },
  "confirmation_required": false
}
```

For mutating or destructive actions, the contract must additionally include an
immutable confirmation token generated after target and impact validation. A user
statement such as "do it" is not sufficient for an unspecified target.

## Evidence Gate

- Only `verified` records in `data/evidence/claims.jsonl` can support an action.
- Version-specific claims must match the requested product version and platform.
- `contradicted`, `insufficient_evidence`, and human-approved configuration claims
  without product-version evidence cannot authorize an execution path.
- The REST `/twsd` port 31116 record is configuration information only; it does
  not authorize a REST call or certificate-bypass option.

## Current Explicit Blocks

- Arbitrary shell strings and arbitrary REST paths.
- `curl -k` or any certificate-verification bypass.
- `conman` batch examples using single quotes as HCL syntax.
- `rj <job>;dep`, because `dep` is not a documented dependency argument.
- Composer `job=` selector until independently verified for the target version.
- Any action with missing, wildcard, ambiguous, or cross-version target scope.
- `resetFTA` when the target FTA hosts any Extended Agent, including SAP X-Agents.

## resetFTA Emergency Rule

`resetFTA` is disabled for automatic execution. It may be proposed only for a
physical FTA without hosted Extended Agents after all of these preconditions are
independently confirmed: Symphony corruption is diagnosed, documented link
recovery attempts did not restore the workstation, a human change approval exists,
and a post-action reconciliation is planned.

The mandatory X-Agent preflight may use Composer definitions or two correlated
Conman reads: `sc @!@` identifies the `X-AGENT` type and `sc @!@;link` identifies
its `HOST`. Block reset when an X-Agent row maps to the target FTA workstation.
Do not use the operating-system hostname (`node`) as the association key. Both
preflight actions remain disabled until their parser is independently tested
against the target version.

An FTA hosting an SAP X-Agent is always refused. `resetFTA` replaces Symphony and
can lose queue or status data; a job whose state was in those queues can rerun.
This creates an unacceptable duplicate-processing risk for SAP workload unless a
separate, human-operated recovery procedure is approved.
