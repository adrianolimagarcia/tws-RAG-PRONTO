# TWS RAG — Base de Conhecimento HCL Workload Automation 10.2.8

> **Status:** `v1.0.0-gold` — validado em lab físico/containerizado e auditado por CI gates.

Base de conhecimento empírica sobre **HCL Workload Automation (TWS/HWA) 10.2.8**,
construída com rigor de engenharia: cada afirmação técnica foi validada contra o
comportamento real de um cluster distribuído de 3 containers Docker:

| Container | Papel |
|---|---|
| `tws-hwa` | Master Domain Manager (MDM), broker dinâmico, Liberty, DWC |
| `tws-bmdm` | Backup Master (BMDM) com replicação de Symphony |
| `tws-agent` | Agente híbrido (FTA `AGT1` + Dynamic Agent `TWS-AGENT_1`) |

**Benchmark:** 1.952 perguntas únicas — Hit@1 **93,5%**, Hit@5 **96,5%**, MRR **0,948**.

## Mapa do projeto

```
tws-RAG-PRONTO/
├── README.md            ← você está aqui
├── AGENTS.md            ← instruções para agentes de IA
├── data/
│   ├── knowledge/       ← BASE DE CONHECIMENTO (jsonl: lab, man-pages, rest-api)
│   ├── runbooks/        ← runbooks operacionais
│   ├── indexes/         ← índices densos (BM25 + embeddings)
│   ├── eval/            ← perguntas e resultados de benchmark
│   ├── evidence/        ← evidências de lab que sustentam as claims
│   ├── ontology/        ← taxonomia do domínio
│   ├── export/          ← corpus consolidado + exports multiformato
│   ├── lab/             ← dados brutos das sessões de lab
│   └── sft/             ← dataset para fine-tuning
├── docs/
│   ├── INDICE.md        ← índice da documentação
│   ├── guias/           ← como fazer (treinamento, troubleshooting, enriquecimento)
│   ├── specs/           ← especificações técnicas (SPECs, PRDs, contratos)
│   ├── releases/        ← histórico de releases
│   ├── sessoes/         ← registros de sessões de trabalho
│   └── lab-protocols/   ← protocolos dos experimentos
├── rag_core/            ← pipeline de retrieval (BM25 + reranker)
├── mcp_server/          ← servidor MCP: `tws_expert_mcp.py`
└── scripts/             ← 120 scripts de build, eval e enriquecimento
```

## Uso rápido

```bash
# Consultar via MCP (para agentes: Hermes, Claude Code, OpenCode)
python3 mcp_server/tws_expert_mcp.py
# ferramenta: tws_expert_search(query, category, top_k)

# Rodar benchmark completo
python3 scripts/calibrated_full_benchmark.py
```

## Enriquecer a base (o fluxo principal)

Quer adicionar manuais, interações documentadas ou novas evidências de lab?
O passo a passo está em **[docs/guias/ENRIQUECIMENTO.md](docs/guias/ENRIQUECIMENTO.md)**.

Resumo: documente em `data/knowledge/` (ou `data/runbooks/`) →
valide com `scripts/apply_enrichment_safe.py` →
reindexe com `scripts/build_dense_index_mcp.py` →
rode o benchmark para medir o ganho.

## Documentação

Comece por **[docs/INDICE.md](docs/INDICE.md)**. Destaques:

- `docs/guias/TRAINING_GUIDE.md` — como treinar com o material
- `docs/guias/PLANO_ENRIQUECIMENTO_DATASET.md` — lacunas medidas e ações priorizadas
- `docs/specs/RAG_EVIDENCE_CONTRACT.md` — contrato de evidência das claims
