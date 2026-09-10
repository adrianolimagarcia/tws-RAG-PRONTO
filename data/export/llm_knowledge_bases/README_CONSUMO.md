# Guia de Consumo da Base de Conhecimento HWA 10.2.8

Este diretório contém a base de conhecimento do HCL Workload Automation 10.2.8
em **três formatos**, cada um otimizado para um tipo de consumo. Escolha o
artefato conforme a ferramenta de destino.

---

## 1. Qual artefato usar em cada ferramenta

| Ferramenta | Artefato recomendado | Motivo |
| --- | --- | --- |
| **Google NotebookLM** | `parts_v2/*.md` (24 arquivos) | O livro completo tem ~809k palavras e excede o limite de 500k palavras por fonte do NotebookLM. Suba as partes como fontes separadas (limite de 50 fontes). |
| **ChatGPT Projects / Custom GPT** | `tws_hwa_10.2.8_knowledge_book_v2_complete.md` | Aceita arquivo único grande; o livro completo preserva o contexto integral. |
| **Claude Projects** | `tws_hwa_10.2.8_knowledge_book_v2_complete.md` | Idem acima. |
| **Perplexity Spaces** | `parts_v2/parte1_*.md` + `parts_v2/parte2_*.md` | Espaços funcionam melhor com arquivos temáticos e menores. |
| **Agentes com MCP** | `mcp_server/tws_expert_mcp.py` | Consulta sob demanda, sem carregar o corpus no contexto. Preferível para agentes. |
| **RAG / busca programática** | `data/export/tws_corpus_master_consolidated.jsonl` | Formato estruturado com todos os campos. |

---

## 2. Livro completo (v2)

**Arquivo:** `tws_hwa_10.2.8_knowledge_book_v2_complete.md`
**Tamanho:** ~5,3 MB · ~809 mil palavras · ~110 mil linhas

### Estrutura

```
Cabeçalho + Instruções de leitura para o modelo
  ↓ tabela de Níveis de Evidência
PARTE I  — Conhecimento canônico por domínio (2.548 registros)
           I.1  Alta Disponibilidade & Failover
           I.2  Arquitetura & Topologia Mesh
           I.3  Operação CLI (conman/composer/planman)
           I.4  Agendamento Avançado & Workflows
           I.5  API REST v2 & Integração
           I.6  Troubleshooting & Mensagens de Erro
           I.7  Instalação & Manutenção
           I.8  Práticas de Comunidade & Governança
           I.9  Outros
PARTE II — Runbooks operacionais (14 documentos, íntegra)
PARTE III— Apêndices (material bruto não validado)
ÍNDICE   — 2.548 identificadores com categoria e tier
```

### O que cada registro traz

- **Nível de evidência** (obrigatório de respeitar)
- **Status do conhecimento** e **taxonomia** (topic/subtopic)
- **Afirmação / conteúdo**
- **ATENÇÃO / RESSALVAS DE USO** — quando existir, prevalece sobre o texto
- **Tabela de atributos**: risco, modo de operação, versão, plataforma, fonte (URL),
  título da fonte, citação de suporte, data de coleta, confiança, status de revisão,
  pré-condições, impacto, critério de parada, reversibilidade, terminologia normalizada
- **Procedimento executado** e **saída real observada** (nas evidências de laboratório)
- **Perguntas relacionadas**

---

## 3. Partes temáticas (`parts_v2/`)

24 arquivos, todos abaixo do limite de 500k palavras por fonte.

### Parte I — Conhecimento canônico

| Arquivo | Palavras |
| --- | --- |
| `parte1_troubleshooting_mensagens_de_erro.md` | ~251k |
| `parte1_operacao_cli_conman_composer_planman.md` | ~165k |
| `parte1_outros.md` | ~128k |
| `parte1_arquitetura_topologia_mesh.md` | ~85k |
| `parte1_api_rest_v2_integracao.md` | ~45k |
| `parte1_instalacao_manutencao.md` | ~30k |
| `parte1_agendamento_avancado_workflows.md` | ~25k |
| `parte1_alta_disponibilidade_failover.md` | ~13k |
| `parte1_praticas_de_comunidade_governanca.md` | ~5k |
| `indice_ids.md` | ~25k |

### Parte II — Runbooks (`parte2_runbook_*.md`)

14 arquivos: instalação MDM/agente em container, lab WSL, referência de flags
`serverinst`/`twsinst`, failover MDM/FTA, recuperação de JnextPlan/SwitchPlan,
recuperação da esteira FINAL (Sfinal) e upgrades.

---

## 4. Regra crítica de uso (anti-contaminação)

O corpus mistura **fatos oficiais** e **práticas de comunidade**. Um modelo que
ignore o rótulo pode afirmar como comportamento do produto algo que a HCL nunca
documentou. Por isso:

| Rótulo | Como o modelo deve tratar |
| --- | --- |
| FATO OFICIAL | Afirmar como comportamento do produto |
| FATO OFICIAL CORROBORADO | Afirmar, podendo citar corroboração cruzada |
| VALIDADO EM LABORATÓRIO | Afirmar, indicando que foi observado em runtime de laboratório |
| OBSERVADO EM LABORATÓRIO | Afirmar com ressalva de observação pontual |
| PRÁTICA DE COMUNIDADE | Apresentar como *recomendação organizacional*, nunca como fato do produto |
| NÃO VALIDADO | Não afirmar como fato |

Se houver bloco **ATENÇÃO / RESSALVAS DE USO**, ele prevalece sobre a afirmação principal.

---

## 5. Regeneração

```bash
python3 scripts/generate_llm_knowledge_book_v2.py
```

Lê `data/evidence/*.jsonl` + `data/runbooks/*.md`, mescla registros com o mesmo
`claim_id` (união de campos) e regrava o livro, as partes e o manifesto
`BOOK_V2_MANIFEST.json`. Para adicionar conhecimento novo basta incluir o arquivo
em `data/evidence/` e rodar o script.
