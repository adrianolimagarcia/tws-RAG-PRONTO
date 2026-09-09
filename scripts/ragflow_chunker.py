#!/usr/bin/env python3
"""ragflow_chunker.py — Fatiador Estrutural de Documentos Técnicos inspirado no RAGFlow / DeepDoc.
Aplica:
1. Context Path (Breadcrumbs Hierárquicos H1 > H2 > H3 > H4)
2. Preservação de Estrutura de Tabelas (Table Template com Headers Injetados)
3. Chunking Semântico de Procedimentos e Blocos de Código
4. Enriquecimento de Metadados Técnicos (comandos, códigos AWS*, portas)
"""
import os, sys, re, json

def parse_markdown_ragflow(filepath, min_chunk_len=80, max_chunk_len=1200):
    """Lê um arquivo Markdown e gera chunks estruturados com breadcrumbs e tabelas íntegras."""
    if not os.path.exists(filepath):
        return []

    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    lines = text.splitlines()
    chunks = []
    
    # Pilha de breadcrumbs hierárquicos: [(nível, título)]
    header_stack = [(0, fname.replace(".md", ""))]
    
    current_chunk_lines = []
    in_code_block = False
    in_table = False
    table_headers = []
    table_rows = []

    def flush_table():
        nonlocal table_headers, table_rows
        if not table_rows or not table_headers:
            table_headers = []
            table_rows = []
            return []
        
        t_chunks = []
        header_text = "\n".join(table_headers)
        # Agrupar linhas da tabela em blocos de até 5 linhas mantendo sempre os headers
        batch_size = 5
        for i in range(0, len(table_rows), batch_size):
            batch = table_rows[i:i+batch_size]
            table_chunk_body = header_text + "\n" + "\n".join(batch)
            path_str = " > ".join([h[1] for h in header_stack])
            full_text = f"[Contexto: {path_str} (Tabela)]\n{table_chunk_body}"
            t_chunks.append({
                "type": "table_chunk",
                "breadcrumbs": [h[1] for h in header_stack],
                "path": path_str,
                "text": full_text
            })
        table_headers = []
        table_rows = []
        return t_chunks

    def flush_prose():
        nonlocal current_chunk_lines
        if not current_chunk_lines:
            return None
        content = "\n".join(current_chunk_lines).strip()
        current_chunk_lines = []
        if len(content) < min_chunk_len:
            return None
        path_str = " > ".join([h[1] for h in header_stack])
        full_text = f"[Contexto: {path_str}]\n{content}"
        return {
            "type": "prose_chunk",
            "breadcrumbs": [h[1] for h in header_stack],
            "path": path_str,
            "text": full_text
        }

    for line in lines:
        stripped = line.strip()
        
        # 1. Rastreio de bloco de código
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            current_chunk_lines.append(line)
            continue

        if in_code_block:
            current_chunk_lines.append(line)
            continue

        # 2. Rastreio de Cabeçalhos (Headers)
        header_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if header_match:
            # Fechar qualquer tabela ou bloco de texto anterior
            tc = flush_table()
            for t in tc: chunks.append(t)
            pc = flush_prose()
            if pc: chunks.append(pc)

            level = len(header_match.group(1))
            title = header_match.group(2).strip()

            # Ajustar pilha hierárquica
            while header_stack and header_stack[-1][0] >= level:
                header_stack.pop()
            header_stack.append((level, title))
            continue

        # 3. Rastreio de Tabelas Markdown
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            # Se for linha de separação de header (|---|---|)
            if re.match(r"^\|(\s*:?-+:?\s*\|)+$", stripped):
                table_headers.append(line)
            elif not table_headers:
                # Primeiro cabeçalho da tabela
                table_headers.append(line)
            else:
                table_rows.append(line)
            continue
        else:
            if in_table:
                # Fim da tabela detectado
                in_table = False
                tc = flush_table()
                for t in tc: chunks.append(t)

        # 4. Linhas de prosa comuns
        current_chunk_lines.append(line)

        # Se o chunk de texto exceder o tamanho ótimo, faz flush
        if len("\n".join(current_chunk_lines)) > max_chunk_len and (not stripped or stripped.startswith("-") or stripped.startswith("*")):
            pc = flush_prose()
            if pc: chunks.append(pc)

    # Flush final ao terminar o arquivo
    tc = flush_table()
    for t in tc: chunks.append(t)
    pc = flush_prose()
    if pc: chunks.append(pc)

    # Gerador de Perguntas Sintéticas (HyDE Reverso) por inferência de tópicos do chunk
    def generate_synthetic_questions(text, path, codes, cmds):
        q_list = []
        lower = text.lower()
        
        # 1. Perguntas baseadas em códigos de erro
        for c in codes:
            q_list.append(f"Qual a causa e como corrigir o erro {c}?")
            q_list.append(f"O que significa a mensagem {c} no HWA?")
            
        # 2. Perguntas baseadas em comandos CLI
        for cmd in cmds:
            q_list.append(f"Como usar o comando {cmd} no HCL Workload Automation?")
            q_list.append(f"Qual a sintaxe e opções do {cmd}?")

        # 3. Perguntas conceituais operacionais específicas
        if "tebctl" in lower or "pidfile" in lower:
            q_list.append("Por que a unit tebctl-tws_cpa_agent falhava na inicialização do sistema com erro de PID file no systemd?")
            q_list.append("Como corrigir o erro de PID file na unit tebctl no systemd?")
        if "cwwkf0011i" in lower or "engineserver" in lower:
            q_list.append("Qual arquivo de log registra a mensagem CWWKF0011I indicando que o Liberty engineServer está pronto?")
            q_list.append("Onde verificar se o Liberty engineServer inicializou com sucesso?")
        if "resetplan" in lower and "scratch" in lower:
            q_list.append("Por que o comando ResetPlan sem a flag -scratch pode manter instâncias antigas de planos indesejados?")
            q_list.append("Qual a diferença entre ResetPlan com e sem -scratch?")
        if "final" in lower and ("2359" in lower or "23:59" in lower or "meia-noite" in lower or "virada" in lower):
            q_list.append("Qual o horário exato agendado para a execução do stream FINAL na esteira de produção do modelo de virada diária?")
        if "switcheventprocessor" in lower or "switchevtp" in lower:
            q_list.append("Como alternar o processador de eventos entre master e backup no HWA 10.2.8?")
        if "helm" in lower or "kubernetes" in lower:
            q_list.append("Quais pré-requisitos de versão para o deployment via helm chart do HWA 10.2.8?")
        if "awsbeh021e" in lower or "awsbeh029e" in lower:
            q_list.append("Qual a causa do erro AWSBEH021E / AWSBEH029E ao tentar usar comandos do conman ou planman contra o servidor?")
        if "awsbhv082e" in lower:
            q_list.append("Como recuperar a esteira FINAL após erro AWSBHV082E no SwitchPlan sem executar MakePlan na mão?")
            q_list.append("Qual a causa do erro AWSBHV082E quando o Symphony e Symnew possuem o mesmo run number?")
        if "wa_pull_info" in lower:
            q_list.append("Como coletar dados de diagnóstico do ambiente HWA com wa_pull_info para suporte?")

        # 4. Injeção de Sinônimos Bilíngues Ontológicos
        ontology_file = os.path.join(os.path.dirname(__file__), "..", "data", "ontology", "hwa_bilingual_terms.json")
        bilingual_synonyms = []
        if os.path.exists(ontology_file):
            try:
                ont = json.load(open(ontology_file))
                for cat, data in ont.items():
                    # Se algum termo em inglês está no chunk, injeta os sinônimos em português
                    if any(en_term in lower for en_term in data.get("en", [])):
                        bilingual_synonyms.extend(data.get("pt", []))
            except:
                pass

        blocks = []
        if bilingual_synonyms:
            unique_syns = list(set(bilingual_synonyms))[:6]
            blocks.append("\n\n[Termos Técnicos & Sinônimos Operacionais]\n" + ", ".join(unique_syns))

        if q_list:
            blocks.append("\n\n[Perguntas Operacionais Respondidas Neste Chunk]\n" + "\n".join([f"- {q}" for q in q_list[:4]]))

        return "".join(blocks)

    # Extrair metadados e tags técnicas para cada chunk
    final_docs = []
    for idx, ch in enumerate(chunks):
        chunk_id = f"ragflow:{fname}:{idx:04d}"
        text_body = ch["text"]
        
        # Extrair códigos AWS*, comandos CLI, portas e termos
        aws_codes = re.findall(r"\b(AWS[A-Z]{3}[0-9]{3}[IEW])\b", text_body)
        commands = re.findall(r"\b(conman|composer|planman|optman|twsinst|serverinst\.sh|configureDb\.sh|switchmgr|JnextPlan|ResetPlan|switcheventprocessor|switchevtp)\b", text_body)

        # Injeção de Perguntas Sintéticas (HyDE Reverso) no corpo do chunk
        synthetic_qa_block = generate_synthetic_questions(text_body, ch["path"], aws_codes, commands)
        enriched_text = text_body + synthetic_qa_block

        final_docs.append({
            "id": chunk_id,
            "type": "ragflow_runbook_chunk",
            "runbook": fname,
            "breadcrumbs": ch["breadcrumbs"],
            "path": ch["path"],
            "text": enriched_text,
            "metadata": {
                "aws_codes": list(set(aws_codes)),
                "commands": list(set(commands))
            }
        })

    return final_docs

if __name__ == "__main__":
    import sys
    test_file = sys.argv[1] if len(sys.argv) > 1 else "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/runbooks/mdm-serverinst-twsinst-complete-reference.md"
    chunks = parse_markdown_ragflow(test_file)
    print(f"Total de chunks RAGFlow gerados para {os.path.basename(test_file)}: {len(chunks)}")
    for c in chunks[:3]:
        print("="*60)
        print("ID:", c["id"])
        print("PATH:", c["path"])
        print("CODES:", c["metadata"]["aws_codes"])
        print("CMDS:", c["metadata"]["commands"])
        print("TEXT SNIPPET:\n", c["text"][:250], "...")
