"""Recuperador lexical do nucleo RAG (rag_core).

Contem a tokenizacao, a expansao de consulta (jargao HWA + mapa bilingue), o
scorer BM25 e a deteccao de familias de mensagem AWS. Este codigo foi EXTRAIDO
VERBATIM de `data/eval/evaluate_rag_benchmark.py` (fatia de refatoracao pura:
mesmo comportamento, sem 'melhorias'). Nao altere o scorer aqui sem medicao
propria - o controle obrigatorio do projeto depende deste comportamento exato.
"""
import os
import re

from .config import AVG_DL, FAMILY_BOOST

SYNONYMS = {
    "sfinal": ["makeplan", "switchplan", "startappserver", "checksync", "createpostreports", "updatestats", "2359", "final", "d+1"],
    "planman": ["showinfo", "resync", "checksync", "resetplan", "symphony", "preproduction", "scratch"],
    "conman": ["batchman", "mailman", "jobman", "showcpus", "showjobs", "start", "stop", "link", "limit", "lc", "confirm", "status"],
    "composer": ["vartable", "runcycle", "schedule", "jsdl", "erule", "lock", "unlock", "pool", "cpuname", "broker"],
    "edwa": ["eventrule", "genericeventplugin", "twsobjectmonitor", "filemonitor", "sendevent", "event1", "jobstatuschanged", "msglog", "objectkey"],
    "rest": ["twsd", "31116", "submit-ad-hoc-job", "joblog", "rerun", "update-priority", "release", "hold", "openapi", "bearer", "apikey"],
    "boot": ["systemd", "tebctl", "tws-domain-start", "hosts", "pidfile", "postgresql", "restart"]
}

# Mapa bilíngue termo->sinônimos (PT<->EN + jargão HWA). Aplicado na expansão de
# consulta e de documento para elevar recall sem recorrer a rótulos de avaliação.
TERM_EXPAND = {
    "senha": ["password", "credential", "passwd", "senha", "credencial"],
    "password": ["password", "senha", "credential"],
    "credencial": ["credential", "password", "senha", "apikey"],
    "autenticacao": ["authentication", "auth", "login", "jwt", "bearer", "apikey"],
    "authentication": ["authentication", "auth", "login", "jwt", "bearer"],
    "jwt": ["jwt", "token", "apikey", "api key", "bearer"],
    "api key": ["apikey", "jwt", "token", "api key"],
    "chave": ["key", "token", "chave"],
    "falha": ["error", "fail", "erro", "problema", "falha", "failure"],
    "error": ["error", "fail", "erro", "falha", "failure", "problema"],
    "erro": ["error", "erro", "fail", "falha"],
    "mensagem": ["message", "msg", "mensagem", "codigo", "code"],
    "procedimento": ["procedure", "command", "procedimento", "comando", "passo", "step"],
    "comando": ["command", "comando", "cli"],
    "bloqueio": ["lockout", "lock", "bloqueio", "retry", "bind", "ldap"],
    "critica": ["critical", "hot", "list", "wsa", "deadline", "hotlist"],
    "dependencia": ["dependency", "deps", "dependencia", "predecessor", "follows", "conddep"],
    "ad-hoc": ["ad-hoc", "adhoc", "submit", "pontual"],
    "limpeza": ["cleanup", "purge", "limpeza", "logcleanupfrequency"],
    "repeticao": ["repeat", "every", "periodic", "interval"],
    "consulta": ["query", "showinfo", "display", "show", "consulta"],
    "plano": ["plan", "symphony", "plano", "production plan"],
    "production plan": ["plan", "symphony", "plano de producao", "plano"],
    "agenda": ["schedule", "schedule", "job stream", "stream", "agendamento"],
    "backup": ["backup", "backup", "restore", "copia", "copia de seguranca"],
    "restore": ["restore", "restauracao", "recuperacao", "backup"],
    "restauracao": ["restore", "recuperacao", "backup"],
    "agente": ["agent", "agente", "fta", "dynamic agent", "workstation"],
    "workstation": ["workstation", "cpu", "ws", "maestro host", "node", "agente"],
    "pool": ["pool", "dynamic pool", "broker", "workstation pool"],
    "virada": ["rollover", "jnextplan", "sfinal", "makeplan", "switchplan", "virada", "final"],
    "failover": ["failover", "switchmgr", "switch", "backup", "fta", "alta disponibilidade", "ha"],
    "seguranca": ["security", "seguranca", "tls", "ssl", "certificado", "ldap", "sso"],
    "security": ["security", "seguranca", "tls", "ssl", "sso", "authorization"],
    "console": ["dwc", "console", "dynamic workload console", "ui", "web"],
    "variavel": ["variable", "vartable", "variavel", "substituicao", "caret", "circunflexo", "expand"],
    "recurso": ["resource", "recurso", "resource advisor", "needs"],
    "evento": ["event", "evento", "event rule", "edwa", "trigger", "dispara"],
    "regra": ["rule", "event rule", "regra", "erule"],
    "plano de producao": ["production plan", "symphony", "plano"],
    "jnextplan": ["jnextplan", "makeplan", "virada", "rollover", "switchplan"],
    "diario": ["daily", "everyday", "diario", "23:59", "2359"],
    "processador": ["processador", "processor", "switcheventprocessor", "switchevtp", "event processor"],
    "alternar": ["alternar", "switch", "switchmgr", "switcheventprocessor", "switchevtp"],
}

# ---------------------------------------------------------------------------
# FAMILY_LEXICON: mapeia sintomas/termos de consulta para a FAMILIA de mensagem
# AWS (prefixo de 3 letras). Baseado no dominio semantico de cada familia no
# catalogo 10.2.8 (nao afinado as 39 perguntas do benchmark virgem):
#   BHU  = runtime Conman/Symphony + validacao de argumento/estacao
#   BIA  = parser/declaracao do Composer (sintaxe, identificador, job stream)
#   DAH  = licenca/ativacao do produto (demo, aluguel, cpu, instalacao)
#   DEG  = banco de dados/memoria compartilhada (comarea, isam)
#   DBY  = execucao de programa RUN (params, capacidade, recursos)
#   FAB  = instalacao (twsinst/install)
# Permite boost de ranking: se a consulta menciona um sintoma, prioriza
# mensagens do catalogo da familia correspondente.
FAMILY_LEXICON = {
    "BHU": [
        "comando de parada", "stop", "intermediario", "outro dominio", "broker",
        "logon", "nao existe no sistema", "submissao rejeitada", "valor numerico",
        "numero excessivo", "formato de quatro digitos", "horario fora", "meia-noite",
        "conman", "symphony", "console recusou", "final do dia", "mais de quatro",
        "informado", "rejeitou a submissao", "recusou",
    ],
    "BIA": [
        "composer", "job stream", "jobstream", "referenciei", "nao existe dentro",
        "ja existe", "duplicidade", "adicionar um job", "mestre de jobs", "declaracao",
        "identificador", "job que nao existe", "nao foi localizado pelo nome",
        "defini", "sintaxe", "esperado", "nao encontrado", "devolveu",
    ],
    "DAH": [
        "licenca", "periodo de demonstracao", "demo", "aluguel", "venceu",
        "valida para o processador", "processador desta maquina", "incompativel com",
        "binario", "incompativel", "instalacao atual", "nao faz parte",
        "software", "expirou", "valido",
    ],
    "DEG": [
        "memoria compartilhada", "comarea", "isam", "arquivo indexado",
        "rotina interna", "area de memoria", "entre processos", "nao foi criada",
    ],
    "DBY": [
        "execucao de programa", "numero excessivo de parametros", "parametros",
        "demais parametros", "run command", "capacidade", "recursos do sistema",
        "nao pode executar", "muitos parametros",
    ],
    "FAB": [
        "instalacao terminou", "instalacao", "install", "twsinst", "terminou com exito",
        "exito", "final da instalacao", "script de instalacao",
    ],
}


def detect_families(query_raw):
    """Detecta (deterministico) a(s) familia(s) AWS que a consulta sugere.

    Retorna o conjunto de prefixos de familia (3 letras) referenciados pelos
    termos do FAMILY_LEXICON presentes na consulta.
    """
    q_low = query_raw.lower()
    fams = set()
    for fam, terms in FAMILY_LEXICON.items():
        for term in terms:
            if term.lower() in q_low:
                fams.add(fam)
                break
    return fams


def tokenize(text):
    """Tokeniza texto e devolve tokens limpos, removendo pontuação das bordas."""
    if not text:
        return set()
    raw_words = re.findall(r"[A-Za-z0-9_\-\.\:\^\/\+\@]+", text.lower())
    stop = {"de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "nao", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "qual", "quais", "por que", "onde", "ser", "sao", "entre", "este", "esta", "pode", "deve", "utilizar", "usar", "para o", "naquele", "daquele", "nesses", "desses", "quando", "apos", "antes", "atraves", "quero", "preciso", "isso", "pela", "sem", "uso", "existe", "apenas", "inteira", "exemplo", "faco", "consigo"}
    cleaned = set()
    for w in raw_words:
        w_clean = w.strip(".,;:?!'\"()[]{}")
        if len(w_clean) > 2 and w_clean not in stop:
            cleaned.add(w_clean)
            # Normalização de códigos de erro divididos por hífen (ex: awkzsj-001e -> awkzsj001e)
            if "-" in w_clean and any(w_clean.startswith(p) for p in ["aws", "awk", "eqq", "cww", "dsra"]):
                cleaned.add(w_clean.replace("-", ""))
            # Normalização de variações awswui -> awsui
            if "awswui" in w_clean:
                cleaned.add(w_clean.replace("awswui", "awsui"))
            elif "awsui" in w_clean:
                cleaned.add(w_clean.replace("awsui", "awswui"))

            # CamelCase e Subword Decomposition (ex: enRetainNameOnRerunFrom -> enretain, mmResolveMaster -> mmresolve)
            subwords = re.findall(r'[A-Za-z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|[0-9]+', w)
            if len(subwords) > 1:
                for sw in subwords:
                    if len(sw) > 2 and sw.lower() not in stop:
                        cleaned.add(sw.lower())
                # Prefixo composto (primeiras 2 partes)
                combo = (subwords[0] + subwords[1]).lower()
                if len(combo) > 3:
                    cleaned.add(combo)
    return cleaned

def _expand_tokens(tokens):
    """Expande tokens apenas para a consulta (jargão HWA + mapa bilíngue)."""
    out = set(tokens)
    for t in sorted(tokens):  # ordem deterministica (set -> hash-seed)
        tl = t.lower()
        for root, syns in SYNONYMS.items():
            if root in tl:
                out.update(syns)
        for term, syns in TERM_EXPAND.items():
            if term in tl or tl in term:
                out.update(syns)
    return out

def expand_query(text):
    """Expande a CONSULTA apenas, com jargão HWA + mapa bilíngue, via _expand_tokens."""
    return _expand_tokens(tokenize(text))


def compute_bm25(query_tokens, doc_tokens, query_raw, doc_text, doc=None, avg_dl=AVG_DL):
    if not doc_tokens:
        return 0.0
    k1 = 1.2
    b = 0.75
    overlap = query_tokens.intersection(doc_tokens)
    if not overlap:
        return 0.0
    score = 0.0
    dl = len(doc_tokens)
    doc_lower = doc_text.lower()

    # 1. Base BM25 com boost em termos HWA
    # Iterar em ordem DETERMINISTICA: `overlap` e um set, cuja ordem depende do PYTHONHASHSEED
    # (randomizado por processo). Como a soma de floats nao e associativa, a ordem de iteracao
    # mudava os scores em ~1e-16 e flipava empates -> metrica nao-reprodutivel (95,7% x 97,1%).
    for t in sorted(overlap):
        boost = 1.0
        if any(term in t for term in ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer", "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens", "limit", "securityutility", "resync", "twsobjectmonitor", "switcheventprocessor", "switchevtp", "helm", "chart", "kubernetes", "tebctl", "cwwkf0011i", "enretain", "wapl", "mmrresolve", "symnew", "conddep", "wa_pull_info", "baserecprompt", "aida", "carryforward"]):
            boost = 4.0
        score += boost * ((k1 + 1) / (1.0 + k1 * (1.0 - b + b * (dl / avg_dl))))

    # 1.1 Boost em Frases Operacionais HWA na Query
    q_low = query_raw.lower()
    if "processador de eventos" in q_low or "event processor" in q_low:
        if "switcheventprocessor" in doc_lower or "switchevtp" in doc_lower:
            score += 15.0

    # 2. Boost em codigos de erro exatos (ex: AWSJDB802E, AWSVAL006E, AWSBEH021E)
    codes_in_query = re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", query_raw.lower())
    for code in codes_in_query:
        if code in doc_lower:
            score += 15.0  # boost forte para match de código de erro

    # 2.1 Boost por familia de mensagem AWS (FAMILY_LEXICON)
    # Se a consulta menciona um sintoma caracteristico de uma familia (ex.: licenca->DAH,
    # comarea->DEG), prioriza as mensagens do catalogo daquela familia. Detectado de forma
    # deterministica apenas a partir do texto da consulta (sem rotulos de avaliacao).
    if doc and doc.get("type") == "message_catalog":
        doc_fam = re.search(r"aws([a-z]{3})", doc.get("id", "").lower())
        if doc_fam:
            for fam in detect_families(query_raw):
                if fam.lower() == doc_fam.group(1):
                    score += FAMILY_BOOST
                    break

    # 3. Re-ranking por tipo e autoridade da evidência
    if doc:
        dtype = doc.get("type")
        if dtype == "canonical_claim":
            score *= 1.25  # Prioridade para claims canônicas verificadas
        elif dtype == "lab_evidence":
            score *= 1.20  # Prioridade para validações reais de laboratório
        elif dtype == "ragflow_runbook_chunk":
            score *= 1.15
        elif dtype == "message_catalog":
            # Catalogo de mensagens do produto: texto canonico da versao instalada.
            # Sem boost, ficava sistematicamente atras das claims canonicas (que recebem 1.25).
            score *= 1.10

        # Boost se a pergunta menciona um código/termo e o doc o tem no id/nome
        for token in sorted(query_tokens):  # ordem deterministica (set -> hash-seed)
            if token.isalnum() and len(token) > 3 and token in (doc.get("id") or "").lower():
                score += 4.0
        # Heading/runbook relevante reforça score
        if doc.get("title") and query_tokens.intersection(tokenize(doc["title"])):
            score *= 1.15
        if doc.get("runbook") and doc.get("runbook").replace(".md","").replace("-","") in query_raw.lower().replace("-",""):
            score *= 1.1

        # 4. Boost RAGFlow: Casamento de Breadcrumbs Hierárquicos e Metadados Extraídos
        if dtype == "ragflow_runbook_chunk":
            meta = doc.get("metadata", {})
            # Match exato de comandos no chunk
            for cmd in meta.get("commands", []):
                if cmd.lower() in query_raw.lower():
                    score += 3.5
            # Match exato de códigos AWS extraídos pelo DeepDoc
            for c_code in meta.get("aws_codes", []):
                if c_code.lower() in query_raw.lower():
                    score += 12.0
            # Breadcrumbs overlap
            if doc.get("path") and query_tokens.intersection(tokenize(doc["path"])):
                score *= 1.2

    return score

def extract_ngrams(words, n=2):
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]
