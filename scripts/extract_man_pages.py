#!/usr/bin/env python3
"""Extrai as man pages do produto HWA 10.2.8 (composer/conman) do container do lab e
gera um DERIVADO em PT-BR no padrao do dataset do RAG.

LICENCA — LEIA ANTES DE MEXER
-----------------------------
O texto das man pages e material do produto (HCL). Este script NAO grava texto
verbatim no repositorio. O que vai ao git:
  (i)  este script (versionado);
  (ii) um jsonl DERIVADO por registro contendo: parafrase PT-BR escrita por nos,
       a sintaxe essencial (gramatica — fato), uma citacao CURTA (<= 160 chars) e o
       caminho da man page de origem (source_title/source_url).
O texto cru nunca e escrito no repo: a leitura acontece direto do container e o que
nao vira parafrase/citacao curta e descartado em memoria.

Uso:  python3 scripts/extract_man_pages.py [--check]
      --check  nao escreve; so reporta quantos registros seriam gerados
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

CONTAINER = os.environ.get("MANPAGES_CONTAINER", "tws-hwa")
MAN_DIRS = ["/opt/hwa/TWS/man/composer/cat1", "/opt/hwa/TWS/man/conman/cat1"]
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(REPO, "data", "knowledge", "man-pages-derived.jsonl")

# ---------------------------------------------------------------------------
# Parafrases PT-BR escritas por nos (nao sao traducao literal das man pages).
# Chave: (tool, comando).
# ---------------------------------------------------------------------------
DESC: dict[tuple[str, str], str] = {
    # ---------------- composer ----------------
    ("composer", "add"): "Adiciona ou atualiza objetos de agendamento a partir de um arquivo texto. Se o objeto ja existe, o produto pergunta se deve substitui-lo: sem responder 'y' nada muda. E o verbo de escrita de definicoes — 'replace' nao serve para isso.",
    ("composer", "authenticate"): "Troca as credenciais do usuario em uso durante a sessao do composer.",
    ("composer", "chfolder"): "Navega entre pastas do banco; muda o diretorio de trabalho do composer.",
    ("composer", "commands"): "Indice dos comandos do composer, com nomes curtos e a regra de abreviacao: nomes e keywords aceitam maiuscula/minuscula e podem ser abreviados ate o ponto de unicidade.",
    ("composer", "continue"): "Instrui o composer a ignorar o proximo erro de comando em vez de abortar.",
    ("composer", "create"): "Sinonimo de extract: extrai a definicao de um objeto do banco para um arquivo texto.",
    ("composer", "delete"): "Remove definicoes de objetos do banco.",
    ("composer", "display"): "Mostra os detalhes de uma ou mais definicoes do mesmo tipo. Para jobstream e job o nome exige o qualificador <workstation>#<nome>, senao o produto devolve 'Total objects: 0' mesmo quando o objeto existe.",
    ("composer", "edit"): "Abre um arquivo para edicao.",
    ("composer", "exit"): "Encerra o programa composer.",
    ("composer", "extract"): "Cria um arquivo texto com a definicao de objetos extraida do banco. A ordem e 'extract <arquivo> from <objeto>': o ARQUIVO vem primeiro (a ordem invertida devolve AWSBIA002E).",
    ("composer", "help"): "Mostra a ajuda on-line de um comando ou a lista de comandos.",
    ("composer", "list"): "Lista, em resumo, os objetos definidos no banco — inclusive a coluna 'Locked By', que revela objetos travados.",
    ("composer", "listfolder"): "Lista as pastas definidas no banco.",
    ("composer", "lock"): "Trava o acesso a definicoes de objetos no banco, impedindo alteracao por outros usuarios ou sessoes.",
    ("composer", "mkfolder"): "Cria uma nova pasta no banco.",
    ("composer", "modify"): "Modifica (ou adiciona) objetos de agendamento; extrai apenas os objetos que o usuario corrente consegue travar. Sem fonte de definicao abre EDITOR e fica preso esperando entrada.",
    ("composer", "new"): "Adiciona uma nova definicao de objeto usando um arquivo texto onde a definicao e inserida.",
    ("composer", "print"): "Sinonimo de display quando usado com a opcao ;offline.",
    ("composer", "redo"): "Edita e executa novamente o comando anterior.",
    ("composer", "rename"): "Renomeia um objeto ja existente no banco.",
    ("composer", "renamefolder"): "Renomeia uma pasta definida no banco.",
    ("composer", "replace"): "Substitui definicoes de objetos no banco. Cuidado: a gramatica dele exige o keyword UNLOCK no ponto em que se esperaria o nome do objeto, por isso nao serve como verbo de escrita generico.",
    ("composer", "rmfolder"): "Remove pastas definidas no banco.",
    ("composer", "runcomposer"): "Como executar comandos do composer a partir da linha de comando (modo nao interativo: o comando inteiro vai como UM argumento).",
    ("composer", "setupcompose"): "Configuracao do programa composer, inclusive o editor usado por edit/modify.",
    ("composer", "specialchar"): "Descreve curingas, delimitadores e caracteres especiais aceitos nas definicoes.",
    ("composer", "system"): "Executa um comando do sistema operacional de dentro do composer.",
    ("composer", "unlock"): "Libera travas de acesso a objetos do banco. Por padrao so libera o que a MESMA sessao travou; com ';forced' libera tambem o que o mesmo usuario travou em OUTRA sessao (AWSBIA308I).",
    ("composer", "update"): "Modifica atributos de tipos especificos de objeto. Nao aceita arquivo de definicao de job diretamente.",
    ("composer", "validate"): "Valida as definicoes de objetos contidas em um arquivo fornecido pelo usuario.",
    ("composer", "version"): "Mostra o banner e a versao do programa composer.",
    # ---------------- conman ----------------
    ("conman", "adddep"): "Adiciona dependencias a um job no plano.",
    ("conman", "altjob"): "Modifica um job no plano antes de ele rodar.",
    ("conman", "altpass"): "Troca a senha de um objeto de usuario no plano de producao corrente (nao tem relacao com 'pass' de plano).",
    ("conman", "altpri"): "Altera a prioridade de um job ou job stream.",
    ("conman", "cancel"): "Cancela um job.",
    ("conman", "checkhealths"): "Invoca o servico chkhltst para verificar a conectividade entre o dominio e os servidores.",
    ("conman", "chfolder"): "Navega entre pastas do plano.",
    ("conman", "commands"): "Indice dos comandos do conman e de onde ele pode ser executado (master e demais workstations).",
    ("conman", "confirm"): "Confirma a conclusao de um job agendado com dependencia do tipo 'confirmed'.",
    ("conman", "console"): "Atribui o console do HWA e define o nivel de mensagem.",
    ("conman", "continue"): "Ignora o proximo erro de comando.",
    ("conman", "deldep"): "Remove dependencias de um job.",
    ("conman", "deployconf"): "Baixa a configuracao de monitoramento mais recente para o motor de eventos.",
    ("conman", "display"): "Mostra um job file ou a definicao de um job stream.",
    ("conman", "exit"): "Encerra o programa conman.",
    ("conman", "fence"): "Altera o 'job fence' de uma workstation: com fence ativo os jobs nao sao lancados nela.",
    ("conman", "help"): "Mostra ajuda sobre os comandos (nao disponivel no Windows).",
    ("conman", "jobselect"): "Como selecionar jobs nos comandos: [jobstream_<ws>#]<stream>(<hhmm>[data]).<job>, ou <ws>#<numero do job>. Vale para rerun, release e afins.",
    ("conman", "jobstates"): "Lista os estados possiveis de um job.",
    ("conman", "jsselect"): "Como selecionar job streams nos comandos.",
    ("conman", "jsstates"): "Lista os estados possiveis de um job stream.",
    ("conman", "kill"): "Para um job que esta em execucao.",
    ("conman", "limit"): "Altera o limite de jobs que podem rodar simultaneamente numa workstation.",
    ("conman", "link"): "Abre os links de comunicacao entre workstations.",
    ("conman", "listfolder"): "Lista as pastas do plano.",
    ("conman", "listsucc"): "Lista os sucessores de um job.",
    ("conman", "listsym"): "Lista os planos de producao (arquivos Symphony) ja processados.",
    ("conman", "recall"): "Mostra os prompts que estao aguardando resposta.",
    ("conman", "redo"): "Edita e re-executa o comando anterior.",
    ("conman", "release"): "Libera jobs de dependencias normais e de TEMPO. Sao dois comandos distintos: RELEASE JOB (rj) libera o JOB (com ;at libera so a dependencia de tempo dele) e RELEASE SCHED (rs) libera o JOB STREAM (com ;at libera a dependencia de tempo do stream). Sem argumento de dependencia libera TODAS, inclusive os follows internos.",
    ("conman", "reply"): "Responde a um prompt de job ou job stream.",
    ("conman", "rerun"): "Re-executa um job (nao o stream inteiro). Sintaxe: rr <ws>#<stream>.<job>, opcionalmente com (hhmm data) para escolher a instancia.",
    ("conman", "rerunsucc"): "Re-executa um job e os sucessores dele.",
    ("conman", "resetfta"): "Gera um Sinfonia atualizado e o envia para um agente tolerante a falhas.",
    ("conman", "resource"): "Altera o numero total de unidades de um recurso.",
    ("conman", "runconman"): "Como executar o conman a partir da linha de comando.",
    ("conman", "setsym"): "Seleciona um arquivo de plano de producao arquivado; os comandos de display seguintes passam a mostrar esse plano.",
    ("conman", "setupconman"): "Configuracao do programa conman.",
    ("conman", "showcpus"): "Mostra informacoes sobre workstations e links.",
    ("conman", "showdomain"): "Mostra informacoes do dominio.",
    ("conman", "showfiles"): "Mostra informacoes sobre dependencias de arquivo.",
    ("conman", "showjobs"): "Mostra informacoes sobre jobs.",
    ("conman", "showprompts"): "Mostra informacoes sobre prompts.",
    ("conman", "showresource"): "Mostra informacoes sobre recursos.",
    ("conman", "showschedule"): "Mostra informacoes sobre job streams.",
    ("conman", "shutdown"): "Para incondicionalmente todos os processos de producao do HWA.",
    ("conman", "specialchar"): "Curingas, delimitadores e caracteres especiais aceitos nos comandos.",
    ("conman", "start"): "Inicia os processos de producao (exceto o motor de eventos e o Liberty). Com ';mgr' inicia a workstation local COMO DOMAIN MANAGER. Nao pode ser emitido enquanto JnextPlan ou stageman estiver rodando.",
    ("conman", "startappserv"): "Inicia o WebSphere Application Server Liberty na workstation.",
    ("conman", "starteventpr"): "Inicia o servidor de processamento de eventos no master ou no backup.",
    ("conman", "startmon"): "Inicia o processo monman, ligando o motor de monitoramento de eventos.",
    ("conman", "status"): "Mostra o banner do conman e o estado da producao — inclusive a data em que o plano esta agendado, o run number e o estado do batchman.",
    ("conman", "stop"): "Para os processos de producao do HWA.",
    ("conman", "stopappserve"): "Para o WebSphere Application Server Liberty na workstation.",
    ("conman", "stopeventpro"): "Para o servidor de processamento de eventos.",
    ("conman", "stopmon"): "Para o motor de monitoramento de eventos.",
    ("conman", "submit"): "Submete um comando para ser lancado como job. Variantes: SUBMIT DOCOMMAND, SUBMIT FILE, SUBMIT JOB e SUBMIT SCHED (sbs), que submete um JOB STREAM e aceita ';at=<HHMM>' — interpretado em UTC, enquanto o plano exibe o schedtime em hora local.",
    ("conman", "switcheventp"): "Alterna o servidor de processamento de eventos entre master e backup.",
    ("conman", "switchmgr"): "Alterna a gerencia do dominio entre os tipos de workstation (promove e despromove master/backup). Atua sobre o PLANO: pode divergir do MODELO no banco.",
    ("conman", "system"): "Executa um comando do sistema operacional de dentro do conman.",
    ("conman", "tellop"): "Envia uma mensagem ao console do HWA.",
    ("conman", "unlink"): "Fecha os links de comunicacao entre workstations.",
    ("conman", "version"): "Mostra o banner e a versao do conman.",
}

# Comandos que este laboratorio exercitou de fato (status observed_in_lab).
VALIDADO = {
    ("composer", "add"), ("composer", "extract"), ("composer", "display"),
    ("composer", "list"), ("composer", "modify"), ("composer", "unlock"),
    ("composer", "delete"), ("composer", "replace"),
    ("conman", "rerun"), ("conman", "release"), ("conman", "submit"),
    ("conman", "start"), ("conman", "status"), ("conman", "switchmgr"),
    ("conman", "altjob"), ("conman", "limit"), ("conman", "fence"),
}


def read_man_pages() -> dict[tuple[str, str], str]:
    """Le as man pages direto do container (nada e gravado no repo)."""
    script = "for d in " + " ".join(MAN_DIRS) + "; do for f in $d/*.1; do echo \"@@FILE@@ $f\"; cat \"$f\"; done; done"
    proc = subprocess.run(
        ["docker", "exec", CONTAINER, "bash", "-lc", script],
        capture_output=True, text=True, timeout=300,
    )
    if proc.returncode != 0:
        sys.exit(f"erro ao ler as man pages do container: {proc.stderr[:300]}")
    pages: dict[tuple[str, str], str] = {}
    cur = None
    buf: list[str] = []
    for line in proc.stdout.splitlines():
        if line.startswith("@@FILE@@ "):
            if cur:
                pages[cur] = "\n".join(buf)
            path = line[len("@@FILE@@ "):].strip()
            tool = "composer" if "/composer/" in path else "conman"
            cur = (tool, os.path.basename(path)[:-2])
            buf = []
        else:
            buf.append(line)
    if cur:
        pages[cur] = "\n".join(buf)
    return pages


def first_quote(text: str, limit: int = 160) -> str:
    """Citacao CURTA: a primeira frase substantiva depois do TITULO da man page.

    Duas armadilhas medidas: (i) a linha semantica costuma ser CURTA ('Reruns a job.',
    13 chars) e um filtro de tamanho alto a descarta; (ii) varias paginas NAO tem secao
    'Authorization' — as linhas de permissao vem soltas e precisam ser puladas por padrao.
    """
    PERM = re.compile(r"(must have|must be|access to the|you must|requires|authorization)", re.I)
    lines = text.splitlines()
    start = 0
    for i, line in enumerate(lines[:10]):
        s = line.strip()
        if s and s.isupper() and len(s) > 2:
            start = i + 1
            break
    for line in lines[start:]:
        s = line.strip()
        if not s or s.isupper() or len(s) < 10 or PERM.search(s):
            continue
        m = re.split(r"(?<=[.;])\s", s)
        return m[0][:limit].strip()
    return ""


def syntax_of(text: str, limit: int = 420) -> str:
    """Sintaxe essencial: as linhas de TODOS os blocos Syntax (paginas com varias
    variantes, como submit.1, tem um bloco por variante — pegar so o primeiro engana)."""
    lines = text.splitlines()
    out: list[str] = []
    inside = False
    for line in lines:
        s = line.rstrip()
        if re.match(r"^\s*Syntax\s*$", s):
            inside = True
            continue
        if inside:
            if re.match(r"^\s*(Arguments|Comments|Examples|See also|Related|Notes|Return codes|Exit status)\s*$", s):
                inside = False
                continue
            if s.strip():
                out.append(s.strip())
    joined = " ".join(out)
    joined = re.sub(r"\s+", " ", joined).strip()
    return joined[:limit]


def build() -> list[dict]:
    pages = read_man_pages()
    records: list[dict] = []
    faltando: list[str] = []
    for (tool, cmd), raw in sorted(pages.items()):
        desc = DESC.get((tool, cmd))
        if not desc:
            faltando.append(f"{tool}/{cmd}")
            desc = f"Comando {cmd} do {tool} (documentado no produto; descricao PT-BR pendente)."
        records.append({
            "claim_id": f"hwa-10.2.8-man-{tool}-{cmd}-0001",
            "kind": "man_page_syntax",
            "tool": tool,
            "command": cmd,
            "claim": f"{tool.upper()} {cmd}: {desc}",
            "syntax": syntax_of(raw),
            "supporting_quote": first_quote(raw),
            "source_title": f"man page {tool} {cmd} (HWA 10.2.8)",
            "source_url": f"/opt/hwa/TWS/man/{tool}/cat1/{cmd}.1",
            "status": "observed_in_lab" if (tool, cmd) in VALIDADO else "version_dependent",
            "result": "SUCCESS",
        })
    if faltando:
        print(f"AVISO: {len(faltando)} comandos sem parafrase propria: {', '.join(faltando)}", file=sys.stderr)
    return records


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nao escreve; so reporta")
    args = ap.parse_args()
    recs = build()
    if args.check:
        print(f"seriam gerados {len(recs)} registros")
        print(f"  observed_in_lab: {sum(1 for r in recs if r['status'] == 'observed_in_lab')}")
        print(f"  version_dependent: {sum(1 for r in recs if r['status'] == 'version_dependent')}")
        print(f"  com sintaxe: {sum(1 for r in recs if r['syntax'])}")
        print(f"  com quote curta: {sum(1 for r in recs if r['supporting_quote'])}")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"gravado {OUT} com {len(recs)} registros")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
