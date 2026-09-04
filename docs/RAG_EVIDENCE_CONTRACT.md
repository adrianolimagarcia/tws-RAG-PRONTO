# Contrato RAG — Evidence-First (P2)

## Propósito

Reduzir alucinação no **sistema final** (RAG + modelo), não apenas no dataset.
Todo componente que responde perguntas factuais sobre HWA/TWS deve seguir este
contrato. O validador `scripts/validate_rag_contract.py` aplica as regras a um
corpus de respostas.

## Regras

### R1 — Resposta factual carrega evidência
Toda resposta factual (não-recusa) DEVE conter uma lista de evidências:
- `evidence_ids`: lista de `claim_id` (ex.: `hwa-10.2.8-composer-priority-in-jobs-0124`).
- Alternativa: marcador inline `[evidence: <claim_id|source_url>]`.

O campo é obrigatório na estrutura de resposta estruturada e o marcador é
obrigatório na resposta textual.

### R2 — Insuficiência de suporte
Se a recuperação não atingir o limiar de **versão**, **plataforma** e
**evidência** exigidos pela pergunta, a resposta DEVE ser de insuficiência:

```
"não há suporte suficiente no corpus disponível"
```

e DEVE pedir o dado ausente (versão, plataforma, comando) ou encaminhar para
a fonte oficial (HCL Help Center). Uma resposta factual fabricada sem
evidência é **violação R2**.

### R3 — Sinalização de status da fonte
Quando a evidência usada for:
- `version_dependent` → rotular `[versão-dependente]`.
- `observed_in_lab` → rotular `[observado em laboratório]`.
- `community` → rotular `[prática de comunidade, não oficial]`.

### R4 — Risco alto exige citação completa
Respostas sobre ações `mutating`, `destructive` ou `credential_sensitive`
DEVEM incluir URL/título/versão da evidência, além do `evidence_id`.

### R5 — Conflito de fontes
Se a recuperação retornar fontes conflitantes (ver
`contradiction_backlog.jsonl`), a resposta DEVE declarar o conflito, apresentar
ambas as evidências e pedir adjudicação humana — nunca afirmar uma única
resposta sem resolver o conflito.

## Estrutura de resposta recomendada (JSON)

```json
{
  "answer": "texto da resposta",
  "evidence_ids": ["hwa-..."],
  "source": {"url": "https://...", "title": "...", "version": "10.2.8"},
  "source_status": "official|lab|community|version_dependent",
  "sufficiency": "sufficient|insufficient",
  "risk": "read_only|mutating|destructive|credential_sensitive"
}
```

## Recuperação e reranking

A recuperação deve priorizar por produto + versão + plataforma + tópico +
risco, não por similaridade textual apenas. Ordem de reranking sugerida:
1. Exatidão de versão (match exato da versão da pergunta).
2. Plataforma (Distributed vs z/OS).
3. Tópico/subject.
4. Tier de evidência (official > lab > community).
5. Similaridade textual (desempate).

## Validação

```powershell
python scripts/validate_rag_contract.py --responses data/eval/rag_responses.jsonl
```

O validador reporta violações por regra (R1–R5). Saída com contagem de
violações e exemplos; exit 0 se sem violações, exit 1 caso contrário.
