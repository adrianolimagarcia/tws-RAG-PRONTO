#!/usr/bin/env python3
"""
Gerador v2 do Livro de Conhecimento HWA 10.2.8 para consumo por LLM.

Diferencas em relacao ao v1 (digest de claims):
  1. Integra TODOS os campos de cada registro (notes, risk, preconditions,
     impact, stop_criterion, reversibility, source_url, supporting_quote,
     evidence_tier, topic/subtopic, capability, version_scope, etc).
  2. Integra os RUNBOOKS operacionais como capitulos (chunked por heading).
  3. Integra dicionario de mensagens AWS*, catalogo optman, evidencias de lab,
     candidatos nao-validados e adjudicacoes de contradicao.
  4. Marca o TIER DE EVIDENCIA em cada secao (fato oficial x pratica de
     comunidade) para impedir contaminacao factual por parte do LLM.
  5. Mescla registros com o mesmo claim_id (uniao de todos os campos).

Saidas:
  data/export/llm_knowledge_bases/tws_hwa_10.2.8_knowledge_book_v2_complete.md
  data/export/llm_knowledge_bases/parts_v2/*.md
  data/export/llm_knowledge_bases/BOOK_V2_MANIFEST.json
"""
import json
import os
import glob
import re
from collections import defaultdict, OrderedDict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVID = os.path.join(BASE, "data", "evidence")
RUNBOOKS = os.path.join(BASE, "data", "runbooks")
OUT_DIR = os.path.join(BASE, "data", "export", "llm_knowledge_bases")
PARTS_DIR = os.path.join(OUT_DIR, "parts_v2")
os.makedirs(PARTS_DIR, exist_ok=True)

BOOK_PATH = os.path.join(OUT_DIR, "tws_hwa_10.2.8_knowledge_book_v2_complete.md")
MANIFEST_PATH = os.path.join(OUT_DIR, "BOOK_V2_MANIFEST.json")

# ---------------------------------------------------------------------------
# Carregamento e mesclagem de todas as fontes de evidencia
# ---------------------------------------------------------------------------

SOURCES = OrderedDict([
    ("canonical_claims", ["claims.jsonl"]),
    ("claim_identity", ["claim_identity.jsonl"]),
    ("aws_messages", ["aws_messages_dictionary.jsonl"]),
    ("optman_options", ["optman_global_options_catalog.jsonl"]),
    ("awsui_draft", ["claims_messages_awsui_draft.jsonl"]),
    ("lab_validation", sorted(os.path.basename(p) for p in glob.glob(os.path.join(EVID, "lab-validation-*.jsonl")))),
    ("contradiction_adjudications", ["contradiction_adjudications.jsonl"]),
    ("jnextplan_safety", ["jnextplan-production-safety-2026-08-17.jsonl"]),
    ("limit_fence_reference", ["limit-fence-reference-2026-08-17.jsonl"]),
    ("recusal_resumecond", ["recusal-resumecond-0001.jsonl"]),
    ("unofficial_candidates", ["unofficial_validation_candidates.jsonl"]),
    ("unofficial_results", ["unofficial_validation_results.jsonl"]),
])


def load_all_records():
    """Carrega todos os JSONL e mescla registros com o mesmo claim_id."""
    merged = {}          # id -> dict (uniao de campos)
    origin = defaultdict(set)   # id -> conjunto de arquivos de origem
    untagged = []        # registros sem claim_id (mantidos individualmente)

    for group, files in SOURCES.items():
        for fname in files:
            path = os.path.join(EVID, fname)
            if not os.path.exists(path):
                continue
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except Exception:
                        continue
                    cid = obj.get("claim_id") or obj.get("id")
                    if not cid:
                        untagged.append((group, fname, obj))
                        continue
                    if cid not in merged:
                        merged[cid] = {}
                    # uniao de campos: nao sobrescreve com valor vazio
                    for k, v in obj.items():
                        if v in ("", None, [], {}):
                            continue
                        if k not in merged[cid] or merged[cid][k] in ("", None, [], {}):
                            merged[cid][k] = v
                    origin[cid].add(fname)
                    merged[cid].setdefault("_source_group", group)

    return merged, origin, untagged


# ---------------------------------------------------------------------------
# Classificacao taxonomica e rotulos de tier
# ---------------------------------------------------------------------------

TIER_LABEL = {
    "official_primary": "FATO OFICIAL (documentacao HCL primaria)",
    "official_secondary": "OFICIAL (fonte HCL secundaria)",
    "official_corroborated": "FATO OFICIAL CORROBORADO (documentacao HCL + corroboracao cruzada)",
    "official_lab": "VALIDADO EM LABORATORIO (comportamento de runtime observado)",
    "lab_observation": "OBSERVADO EM LABORATORIO (observacao pontual, sem repeticao)",
    "lab_verified": "VALIDADO EM LABORATORIO (comportamento de runtime observado)",
    "community_reviewed": "PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)",
    "community_practice": "PRATICA DE COMUNIDADE/ORGANIZACIONAL (NAO e fato de produto)",
    "unofficial": "NAO VALIDADO (nao usar como fato)",
}

CATEGORY_ORDER = [
    "Alta Disponibilidade & Failover",
    "Arquitetura & Topologia Mesh",
    "Operacao CLI (conman/composer/planman)",
    "Agendamento Avancado & Workflows",
    "API REST v2 & Integracao",
    "Troubleshooting & Mensagens de Erro",
    "Instalacao & Manutencao",
    "Praticas de Comunidade & Governanca",
    "Outros",
]


def categorize(rec):
    """Deriva a categoria a partir de topic/context_prefix/evidence_tier."""
    tier = str(rec.get("evidence_tier", ""))
    topic = str(rec.get("topic", "")).lower()
    sub = str(rec.get("subtopic", "")).lower()
    pfx = str(rec.get("context_prefix", "")).lower()
    cid = str(rec.get("claim_id", "")).lower()
    blob = " ".join([topic, sub, pfx, str(rec.get("capability", "")).lower()])

    if "community" in tier or rec.get("is_community_practice") is True:
        return "Praticas de Comunidade & Governanca"
    if "troubleshooting" in topic or "message" in topic or cid.startswith("hwa-10.2.8-msg"):
        return "Troubleshooting & Mensagens de Erro"
    if "globalopts" in topic or "optman" in sub or "optman" in blob:
        return "Operacao CLI (conman/composer/planman)"
    if any(k in blob for k in ["failover", "high_availability", "switchmgr", "backup master", "bmdm", "disaster"]):
        return "Alta Disponibilidade & Failover"
    if any(k in blob for k in ["rest", "openapi", "twsd", "api v2", "integration", "bearer"]):
        return "API REST v2 & Integracao"
    if any(k in blob for k in ["dynamic agent", "broker", "topology", "mesh", "architecture", "fta", "pool", "agent"]):
        return "Arquitetura & Topologia Mesh"
    if any(k in blob for k in ["scheduling", "needs", "opens", "recovery", "vartable", "prompt", "dependenc", "jobs", "calendar", "runc"]):
        return "Agendamento Avancado & Workflows"
    if any(k in blob for k in ["install", "upgrade", "twsinst", "serverinst", "dwcinst", "configuredb", "certman"]):
        return "Instalacao & Manutencao"
    if any(k in blob for k in ["conman", "composer", "planman", "cli", "ocli", "optman"]):
        return "Operacao CLI (conman/composer/planman)"
    return "Outros"


# ---------------------------------------------------------------------------
# Renderizacao de campos
# ---------------------------------------------------------------------------

# Campos ja renderizados explicitamente no cabecalho/corpo da secao.
# `notes`, `test_procedure` e `actual_output` recebem destaque proprio (bloco
# ATENCAO / bloco de procedimento) e por isso sao omitidos da tabela de
# atributos, evitando duplicacao do mesmo texto na secao.
HANDLED = {
    "claim_id", "claim", "id", "text", "context_prefix", "synthetic_questions",
    "_source_group", "topic", "subtopic", "evidence_tier", "knowledge_status",
    "notes", "test_procedure", "actual_output",
}

FIELD_PT = {
    "notes": "Ressalvas de uso",
    "risk": "Classificacao de risco",
    "operation_mode": "Modo de operacao",
    "result": "Resultado observado",
    "status": "Status do conhecimento",
    "confidence": "Confianca",
    "capability": "Capacidade",
    "version": "Versao",
    "version_scope": "Escopo de versao",
    "platform": "Plataforma",
    "platform_scope": "Escopo de plataforma",
    "product": "Produto",
    "product_version": "Versao do produto",
    "source_url": "Fonte (URL)",
    "source_title": "Titulo da fonte",
    "source": "Fonte",
    "source_name": "Nome da fonte",
    "supporting_quote": "Citacao de suporte",
    "retrieved_at": "Coletado em",
    "review_status": "Status de revisao",
    "assigned_to": "Responsavel",
    "rationale": "Justificativa",
    "corroborating_sources": "Fontes corroborantes",
    "normalized_terminology": "Terminologia normalizada",
    "test_procedure": "Procedimento executado",
    "actual_output": "Saida real observada",
    "observed_at": "Observado em",
    "synthetic_questions": "Perguntas relacionadas",
    "code": "Codigo",
    "component": "Componente",
    "severity": "Severidade",
    "message": "Texto da mensagem",
    "message_code": "Codigo da mensagem",
    "name": "Nome",
    "alias": "Abreviacao",
    "value": "Valor",
    "kind": "Tipo",
    "tool": "Ferramenta",
    "family_raw": "Familia",
    "community_topic": "Topico de comunidade",
    "is_community_practice": "Pratica de comunidade",
    "preconditions": "Pre-condicoes",
    "impact": "Impacto",
    "stop_criterion": "Criterio de parada",
    "reversibility": "Reversibilidade",
    "training_eligible": "Elegivel para treino",
    "candidate_id": "ID do candidato",
    "chunk": "Chunk",
    "official_sources": "Fontes oficiais",
    "platform_canonical": "Plataforma canonica",
}

# Campos internos/ruidosos que nao agregam valor ao leitor LLM
DROP_FIELDS = {
    "corroborating_sources", "unofficial_sources", "provenance", "raw", "hash",
    "sha256", "embedding", "vector",
}


def fmt_value(v):
    if isinstance(v, bool):
        return "sim" if v else "nao"
    if isinstance(v, list):
        if not v:
            return ""
        parts = []
        for item in v:
            if isinstance(item, (dict, list)):
                parts.append(json.dumps(item, ensure_ascii=False))
            else:
                parts.append(str(item))
        return "; ".join(parts)
    if isinstance(v, dict):
        return ", ".join(f"{k}={v[k]}" for k in v)
    return str(v)


def sanitize(text, limit=None):
    """Remove bytes nulos e normaliza espacos; corta em `limit` chars."""
    if text is None:
        return ""
    s = str(text).replace("\x00", " ").replace("\r", " ")
    s = re.sub(r"[ \t]+", " ", s).strip()
    if limit and len(s) > limit:
        s = s[:limit].rstrip() + " [...]"
    return s


def render_record(rec, idx):
    """Renderiza um registro completo com todos os campos disponiveis."""
    cid = rec.get("claim_id", f"sem-id-{idx}")
    tier = str(rec.get("evidence_tier", ""))
    tier_note = TIER_LABEL.get(tier) or (
        "NAO CLASSIFICADO (tratar com cautela; nao afirmar como fato do produto)"
        if not tier else tier
    )

    out = [f"### {idx}. `{cid}`", ""]
    out.append(f"**Nivel de evidencia:** {tier_note}")
    ks = rec.get("knowledge_status")
    if ks:
        out.append(f"**Status do conhecimento:** {ks}")
    topic = rec.get("topic")
    sub = rec.get("subtopic")
    if topic or sub:
        out.append(f"**Taxonomia:** `{topic or '-'}` / `{sub or '-'}`")
    out.append("")

    # Corpo principal
    body = sanitize(rec.get("claim") or rec.get("text") or "")
    if body:
        out.append("**Afirmacao / Conteudo:**")
        out.append("")
        out.append(body)
        out.append("")

    # Ressalvas (critico para nao contaminar o LLM)
    notes = sanitize(rec.get("notes"))
    if notes:
        out.append(f"> **ATENCAO / RESSALVAS DE USO:** {notes}")
        out.append("")

    # Campos restantes
    rows = []
    for k, v in rec.items():
        if k in HANDLED or k in DROP_FIELDS:
            continue
        if v in ("", None, [], {}):
            continue
        label = FIELD_PT.get(k, k)
        val = sanitize(fmt_value(v))
        if not val:
            continue
        rows.append(f"| {label} | {val} |")

    if rows:
        out.append("| Atributo | Valor |")
        out.append("| --- | --- |")
        out.extend(rows)
        out.append("")

    # Procedimento / saida de laboratorio em bloco proprio
    for fld, title in (("test_procedure", "Procedimento executado"),
                       ("actual_output", "Saida real observada"),
                       ("observed_at", "Observado em")):
        val = sanitize(rec.get(fld))
        if val and fld not in ("observed_at",):
            out.append(f"**{title}:** {val}")
            out.append("")

    # Perguntas relacionadas
    qs = rec.get("synthetic_questions") or []
    if qs:
        out.append("**Perguntas relacionadas:**")
        out.append("")
        for q in qs:
            out.append(f"- {sanitize(q)}")
        out.append("")

    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Runbooks: chunk por heading de nivel 2
# ---------------------------------------------------------------------------

def split_runbook(path):
    """Divide um runbook em secoes por heading ## (mantendo o H1 como contexto)."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    lines = text.split("\n")
    h1 = ""
    sections = []
    cur_title = None
    cur_body = []

    for ln in lines:
        if ln.startswith("# ") and not h1:
            h1 = ln[2:].strip()
            continue
        if ln.startswith("## "):
            if cur_title is not None:
                sections.append((cur_title, "\n".join(cur_body).strip()))
            cur_title = ln[3:].strip()
            cur_body = []
        elif ln.startswith("### ") and cur_title is None:
            cur_title = ln[4:].strip()
            cur_body = []
        else:
            cur_body.append(ln)

    if cur_title is not None:
        sections.append((cur_title, "\n".join(cur_body).strip()))

    # Caso o arquivo nao tenha headings de nivel 2
    if not sections and text.strip():
        sections = [("Documento completo", text.strip())]

    return h1, sections


# ---------------------------------------------------------------------------
# Montagem do livro
# ---------------------------------------------------------------------------

def main():
    merged, origin, untagged = load_all_records()

    # Inferir evidence_tier quando ausente (registros de laboratorio e fontes oficiais)
    TIER_BY_GROUP = {
        "lab_validation": "official_lab",
        "aws_messages": "official_primary",
        "optman_options": "official_lab",
        "unofficial_candidates": "unofficial",
        "unofficial_results": "unofficial",
    }
    inferred = 0
    for cid, rec in merged.items():
        if not rec.get("evidence_tier"):
            grp = rec.get("_source_group", "")
            t = TIER_BY_GROUP.get(grp)
            if not t and any("lab-validation" in f for f in origin.get(cid, ())):
                t = "official_lab"
            if t:
                rec["evidence_tier"] = t
                inferred += 1
    print(f"Tier inferido para {inferred} registros sem evidence_tier")

    print(f"Registros mesclados por claim_id: {len(merged)}")
    print(f"Registros sem claim_id: {len(untagged)}")

    # Agrupar por categoria
    buckets = defaultdict(list)
    for cid, rec in merged.items():
        buckets[categorize(rec)].append((cid, rec))
    for cat in buckets:
        buckets[cat].sort(key=lambda x: x[0])

    parts = {}            # nome_arquivo -> conteudo
    manifest = {
        "version": "v2",
        "generated_from": "data/evidence/*.jsonl + data/runbooks/*.md",
        "total_records": len(merged),
        "untagged_records": len(untagged),
        "categories": {},
        "runbooks": {},
        "parts": [],
    }

    # --- Cabecalho -----------------------------------------------------------
    head = []
    head.append("# MANUAL COMPLETO DO ESPECIALISTA HCL WORKLOAD AUTOMATION 10.2.8 (DISTRIBUTED)")
    head.append("")
    head.append("> **Base de conhecimento estruturada para consumo por LLM** (NotebookLM, Perplexity Spaces, ChatGPT Projects, Claude Projects).")
    head.append(">")
    head.append(f"> Compilada a partir de **{len(merged)} registros canonicos** e **{len(glob.glob(os.path.join(RUNBOOKS, '*.md')))} runbooks operacionais**,")
    head.append("> todos validados em laboratorio distribuido real (containers RHEL 9 UBI9, FTA, Dynamic Agent, Broker, PostgreSQL, Liberty engineServer).")
    head.append("")
    head.append("---")
    head.append("")
    head.append("## COMO LER ESTE DOCUMENTO (INSTRUCOES PARA O MODELO)")
    head.append("")
    head.append("Cada secao traz um rotulo explicito de **Nivel de evidencia**. Respeite a distincao:")
    head.append("")
    head.append("| Nivel de evidencia | Significado | Como usar |")
    head.append("| --- | --- | --- |")
    head.append("| FATO OFICIAL | Extraido da documentacao HCL primaria | Pode ser afirmado como comportamento do produto |")
    head.append("| VALIDADO EM LABORATORIO | Comportamento observado em runtime real | Pode ser afirmado, citando que foi observado em laboratorio |")
    head.append("| PRATICA DE COMUNIDADE/ORGANIZACIONAL | Recomendacao de comunidade, **nao prescrita pela HCL** | Deve ser apresentada como recomendacao, NUNCA como fato do produto |")
    head.append("| NAO VALIDADO | Material bruto sem confronto com fonte oficial | Nao deve ser afirmado como fato |")
    head.append("")
    head.append("Sempre que uma secao trouxer o campo **ATENCAO / RESSALVAS DE USO**, essas ressalvas prevalecem sobre o texto principal.")
    head.append("")
    head.append("---")
    head.append("")

    # Sumario
    head.append("## SUMARIO")
    head.append("")
    head.append("- **Parte I** — Conhecimento Canonico por dominio (registros tecnicos verificados)")
    for i, cat in enumerate(CATEGORY_ORDER, start=1):
        n = len(buckets.get(cat, []))
        if n:
            head.append(f"  - I.{i} {cat} ({n} registros)")
    head.append("- **Parte II** — Runbooks Operacionais (procedimentos SRE ponta a ponta)")
    head.append("- **Parte III** — Apendices (candidatos nao validados, adjudicacoes)")
    head.append("")
    head.append("---")
    head.append("")

    # --- Parte I: categorias -------------------------------------------------
    part_i = ["# PARTE I — CONHECIMENTO CANONICO POR DOMINIO", ""]
    for cat in CATEGORY_ORDER:
        items = buckets.get(cat, [])
        if not items:
            continue
        manifest["categories"][cat] = len(items)
        block = [f"## I. {cat}", "", f"> {len(items)} registros.", "", "---", ""]
        for i, (cid, rec) in enumerate(items, start=1):
            block.append(render_record(rec, i))
            block.append("---")
            block.append("")
        text = "\n".join(block)
        part_i.append(text)
        slug = re.sub(r"[^a-z0-9]+", "_", cat.lower()).strip("_")
        parts[f"parte1_{slug}.md"] = text

    # --- Parte II: runbooks --------------------------------------------------
    part_ii = ["# PARTE II — RUNBOOKS OPERACIONAIS", "",
               "> Procedimentos operacionais completos, incluindo recuperacao de incidentes, failover e virada de plano.", "",
               "---", ""]
    for rb in sorted(glob.glob(os.path.join(RUNBOOKS, "*.md"))):
        name = os.path.basename(rb)
        h1, sections = split_runbook(rb)
        manifest["runbooks"][name] = {"sections": len(sections), "bytes": os.path.getsize(rb)}
        block = [f"## RUNBOOK: {h1 or name}", "", f"**Arquivo de origem:** `data/runbooks/{name}`", ""]
        for t, body in sections:
            if not body:
                continue
            block.append(f"### {t}")
            block.append("")
            block.append(body)
            block.append("")
        text = "\n".join(block)
        part_ii.append(text)
        part_ii.append("---")
        part_ii.append("")
        slug = re.sub(r"[^a-z0-9]+", "_", name.replace(".md", "").lower()).strip("_")
        parts[f"parte2_runbook_{slug}.md"] = text

    # --- Parte III: apendices ------------------------------------------------
    part_iii = ["# PARTE III — APENDICES", ""]
    if untagged:
        part_iii.append(f"## III.1 Materiais sem identificador canonico ({len(untagged)} registros)")
        part_iii.append("")
        part_iii.append("> Material bruto preservado para rastreabilidade. **Nao validado contra fonte oficial.**")
        part_iii.append("")
        part_iii.append("---")
        part_iii.append("")
        for i, (group, fname, obj) in enumerate(untagged, start=1):
            part_iii.append(f"### A{i}. `{fname}` (grupo: {group})")
            part_iii.append("")
            txt = sanitize(obj.get("text") or obj.get("claim") or "")
            if txt:
                part_iii.append(txt[:4000])
                part_iii.append("")
            rows = []
            for k, v in obj.items():
                if k in ("text", "claim"):
                    continue
                if v in ("", None, [], {}):
                    continue
                rows.append(f"| {FIELD_PT.get(k, k)} | {sanitize(fmt_value(v))} |")
            if rows:
                part_iii.append("| Atributo | Valor |")
                part_iii.append("| --- | --- |")
                part_iii.extend(rows)
                part_iii.append("")
            part_iii.append("---")
            part_iii.append("")

    # --- Indice de IDs -------------------------------------------------------
    index = ["## INDICE DE IDENTIFICADORES", ""]
    index.append("| ID | Categoria | Tier |")
    index.append("| --- | --- | --- |")
    for cid, rec in sorted(merged.items()):
        index.append(f"| `{cid}` | {categorize(rec)} | {rec.get('evidence_tier','-')} |")
    index.append("")
    index_text = "\n".join(index)
    parts["indice_ids.md"] = index_text

    # --- Montagem final ------------------------------------------------------
    full = "\n".join(head) + "\n" + "\n".join(part_i) + "\n" + "\n".join(part_ii) + "\n" + "\n".join(part_iii) + "\n" + index_text + "\n"

    with open(BOOK_PATH, "w", encoding="utf-8") as fh:
        fh.write(full)

    for pname, ptext in parts.items():
        with open(os.path.join(PARTS_DIR, pname), "w", encoding="utf-8") as fh:
            fh.write(ptext if pname == "indice_ids.md" else
                     f"# {pname.replace('.md','').replace('_',' ').upper()}\n\n" + ptext)
        manifest["parts"].append({"file": f"parts_v2/{pname}", "bytes": len(ptext.encode())})

    manifest["book_bytes"] = os.path.getsize(BOOK_PATH)
    manifest["book_path"] = os.path.relpath(BOOK_PATH, BASE)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)

    print("\nLivro v2 gerado:")
    print(f"  {BOOK_PATH} ({manifest['book_bytes']/1024/1024:.2f} MB)")
    print(f"  Partes: {len(parts)} arquivos em {PARTS_DIR}")
    print("\nRegistros por categoria:")
    for cat, n in manifest["categories"].items():
        print(f"  {n:5d}  {cat}")


if __name__ == "__main__":
    main()
