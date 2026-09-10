import os, json
from collections import defaultdict

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
corpus_file = f"{base_dir}/data/export/tws_corpus_master_consolidated.jsonl"
llm_dir = f"{base_dir}/data/export/llm_knowledge_bases"
os.makedirs(llm_dir, exist_ok=True)

book_file = f"{llm_dir}/tws_hwa_10.2.8_knowledge_book_complete.md"

claims_by_category = defaultdict(list)
with open(corpus_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        claims_by_category[item.get("category", "Geral")].append(item)

category_slugs = {
    "Alta Disponibilidade & Failover": "01_alta_disponibilidade_failover.md",
    "Arquitetura & Topologia Mesh": "02_arquitetura_topologia_mesh.md",
    "Operacao CLI (conman/composer/planman)": "03_operacao_cli_conman_composer_planman.md",
    "Agendamento Avancado & Workflows": "04_agendamento_avancado_workflows.md",
    "API REST v2 & Integracao": "05_api_rest_v2_integracao.md",
    "Troubleshooting & Mensagens de Erro": "06_troubleshooting_mensagens_aws.md",
    "Instalacao & Manutencao": "07_instalacao_manutencao.md",
    "Outros": "08_procedimentos_e_referencias_adicionais.md"
}

all_content = []
header = """# MANUAL CANÔNICO DO ESPECIALISTA HCL WORKLOAD AUTOMATION 10.2.8 (DISTRIBUTED)
> **Base de Conhecimento Estruturada para Modelos de Linguagem (LLM, NotebookLM, Perplexity Spaces e Claude Projects)**
> Compilado a partir de 2.548 claims verificadas em laboratório físico/containerizado (RHEL 9 UBI9, FTA, Dynamic Agent, Broker e PostgreSQL).

---
"""
all_content.append(header)

print(f"Gerando bases Markdown temáticas em {llm_dir}...")

for cat, filename in category_slugs.items():
    items = claims_by_category.get(cat, [])
    if not items:
        continue
    
    cat_path = os.path.join(llm_dir, filename)
    lines = []
    lines.append(f"# {cat.upper()}\n")
    lines.append(f"> Total de tópicos canônicos cobertos nesta seção: {len(items)}\n\n---\n")
    
    for i, item in enumerate(items, start=1):
        cid = item["claim_id"]
        claim = item["claim"]
        prefix = item.get("context_prefix", "")
        questions = item.get("synthetic_questions", [])
        platform = item.get("platform", "HWA 10.2.8 Distributed")
        
        lines.append(f"### {i}. {cid}\n")
        if prefix:
            lines.append(f"**Escopo & Contexto:** `{prefix}`\n")
        lines.append(f"**Regra Canônica / Evidência:**\n{claim}\n")
        lines.append(f"**Plataforma / Validação:** {platform}\n")
        if questions:
            lines.append("**Perguntas e Cenários Relacionados:**\n")
            for q in questions:
                lines.append(f"- *{q}*")
            lines.append("")
        lines.append("---\n")
        
    doc_text = "\n".join(lines)
    with open(cat_path, "w", encoding="utf-8") as f:
        f.write(doc_text)
        
    all_content.append(doc_text)
    print(f"- Criado {filename} ({len(items)} tópicos)")

# Gravar livro consolidado único
with open(book_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_content))

book_size_mb = os.path.getsize(book_file) / (1024 * 1024)
print(f"\nLivro único consolidado gerado: {book_file} ({book_size_mb:.2f} MB)")
