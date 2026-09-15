#!/usr/bin/env bash
# scripts/publish.sh — publica o repo APENAS se a varredura de segredo passar.
#
# POR QUE EXISTE
#   O guardrail manda publicar por aqui; sem script, o trabalho verificado ficava
#   so na maquina e `origin` atrasava em silencio.
#
# GARANTIAS (contrato)
#   1. ABORTA (rc 1) se a varredura achar segredo no range a publicar.
#   2. NUNCA imprime o VALOR do hit: reporta apenas TIPO, REV, ARQUIVO e LINHA.
#      (`git grep -n | cut -d: -f1-3` corta o conteudo — nunca use `git grep` cru aqui.)
#   3. NAO configura credencial, NAO grava token em arquivo, NAO ecoa nada sensivel.
#      Usa a autenticacao que o host JA tem: se o `gh` estiver autenticado, passa o
#      helper dele SO para este comando (`-c`), sem tocar em gitconfig.
#   4. NAO faz force-push, NAO reescreve historia, NAO toca em claims.jsonl.
#
# USO
#   scripts/publish.sh --scan-only            # so a varredura; nao publica
#   scripts/publish.sh                        # varredura -> commit -> push
#   scripts/publish.sh --range A..B           # range explicito
#   PUBLISH_BRANCH=master scripts/publish.sh  # branch explicito
#
# SAIDA: a varredura SEMPRE aparece antes de qualquer push.

set -uo pipefail
cd "$(dirname "$0")/.." || { echo "publish: nao consegui entrar no repo" >&2; exit 2; }

BRANCH="${PUBLISH_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
RANGE="${PUBLISH_RANGE:-origin/${BRANCH}..HEAD}"
MSG="${PUBLISH_MSG:-}"
SCAN_ONLY=0
RANGE_EXPLICITO=0

while [ $# -gt 0 ]; do
  case "$1" in
    --scan-only) SCAN_ONLY=1; shift ;;
    --range)     RANGE="${2:?--range exige A..B}"; RANGE_EXPLICITO=1; shift 2 ;;
    --message)   MSG="${2:?--message exige texto}"; shift 2 ;;
    -h|--help)   sed -n '2,25p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)           echo "publish: opcao desconhecida: $1" >&2; exit 2 ;;
  esac
done

# Este proprio arquivo contem os padroes da varredura: fica fora do escopo,
# senao ele se auto-acusa.
SELF=':(exclude)scripts/publish.sh'

# --- padroes -----------------------------------------------------------------
# Os literais sao MONTADOS EM PARTES de proposito: assim o proprio fonte nunca
# contem a forma exata que procura (nem dispara redatores/varreduras de terceiros).
# publish-patterns:start — unica regiao do repo isenta da varredura (as proprias
# definicoes dos padroes; um regex de credencial casa consigo mesmo). O RESTO do
# arquivo e varrido normalmente: excluir o script INTEIRO esconderia um segredo
# real dentro dele.
P_PEM="${P_PEM1:-$(printf '%s' '-----BE' 'GIN ')}"
P_PEME="${P_PEM2:-$(printf '%s' 'PRIVA' 'TE KEY-----')}"
P_GH="${P_GH:-$(printf '%s' 'gh' '[pousr]' '_')}"
P_PAT="${P_PAT:-$(printf '%s' 'gith' 'ub_pat' '_')}"
P_AWS="${P_AWS:-$(printf '%s' 'AK' 'IA')}"

PATTERNS=(
  "chave_privada:${P_PEM}[A-Z ]*${P_PEME}"
  "token_github:${P_GH}[A-Za-z0-9]{20,}"
  "token_github_pat:${P_PAT}[A-Za-z0-9_]{20,}"
  "chave_aws:${P_AWS}[0-9A-Z]{16}"
  'ipv4:\b([0-9]{1,3}[.]){3}[0-9]{1,3}\b'
  'credencial_em_url://[^/@[:space:]]+:[^/@[:space:]]+@'
  'header_auth:(Bearer|Basic)[[:space:]]+[A-Za-z0-9+/=_-]{16,}'
)
# publish-patterns:end

# --- auto-teste --------------------------------------------------------------
# Um padrao que nao casa e um padrao QUEBRADO: a varredura passaria por engano.
# As amostras sao montadas em runtime (nada de segredo real, nada persistido).
selftest() {
  local ok=1 rep
  rep=$(printf 'A%.0s' 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24)
  local s_pem="${P_PEM}${P_PEME}"
  # amostra LITERAL: o regex tem classe ([pousr]), a amostra nao pode ter colchete
  local s_gh="$(printf '%s' 'gh' 'p' '_')${rep}"
  local s_pat="${P_PAT}${rep}"
  local s_aws="${P_AWS}${rep}"
  # Fixtures montadas em PARTES (mesma tecnica do s_gh): literais sinteticos no
  # fonte fazem o proprio scanner abortar no seu conteudo (defeito 6, medido —
  # as fixtures ficavam FORA da janela de isencao). A janela NAO foi ampliada:
  # ampliar isencao e pior que montar o literal em partes.
  local s_ip="$(printf '%s' '10.' '99.0.7')"
  local s_url="$(printf '%s' 'https://' 'u:s' '@' 'exemplo.invalido/x')"
  local s_auth="Authorization: $(printf '%s' 'Bea' 'rer') ${rep}"
  # Os regexes vem da PROPRIA tabela de producao — nunca literais aqui. Assim o
  # auto-teste nao pode divergir do que a varredura executa (defeito 3).
  rx_of() {
    local e
    for e in "${PATTERNS[@]}"; do [ "${e%%:*}" = "$1" ] && { printf '%s' "${e#*:}"; return; }; done
  }
  check() { printf '%s\n' "$2" | grep -qE -e "$1" || { echo "  selftest FALHOU: $3" >&2; ok=0; }; }
  check "$(rx_of chave_privada)"     "$s_pem" chave_privada
  check "$(rx_of token_github)"      "$s_gh"  token_github
  check "$(rx_of token_github_pat)"  "$s_pat" token_github_pat
  check "$(rx_of chave_aws)"         "$s_aws" chave_aws
  check "$(rx_of ipv4)"              "$s_ip"  ipv4
  check "$(rx_of credencial_em_url)" "$s_url" credencial_em_url
  check "$(rx_of header_auth)"       "$s_auth" header_auth
  [ "$ok" -eq 1 ] && echo "publish: auto-teste dos padroes: OK (7/7 casam)"
  return $((1 - ok))
}
selftest || exit 3

echo "publish: branch=${BRANCH}"
# PUBLISH_RANGE no ambiente tambem conta como range explicito (nao commitar).
[ -n "${PUBLISH_RANGE:-}" ] && RANGE_EXPLICITO=1

# --- commit ANTES do scan ----------------------------------------------------
# O scan tem de cobrir EXATAMENTE o que sera empurrado. Na ordem ingenua
# (scan -> commit -> push) uma alteracao PENDENTE nao esta no range: ela seria
# commitada e publicada SEM varredura — buraco real. Por isso commitamos primeiro.
# Guardas: nunca em --scan-only, e nunca com --range explicito (um teste nao pode
# ter efeito colateral de commitar o worktree).
if [ "$SCAN_ONLY" -eq 0 ] && [ "$RANGE_EXPLICITO" -eq 0 ] \
   && [ -n "$(git status --porcelain -- . ':(exclude)**/__pycache__/**')" ]; then
  echo "publish: ha alteracoes nao commitadas; commitando ANTES do scan (pycache excluido)"
  git add -A -- . ':(exclude)**/__pycache__/**' || exit 1
  git commit -q -m "${MSG:-publish: publica o estado verificado}" || exit 1
  echo "publish: commit $(git rev-parse --short HEAD)"
fi

echo "publish: range=${RANGE}"
# `rev-parse --verify` NAO aceita intervalo (A..B); quem valida range e o rev-list.
if ! NCOMMITS=$(git rev-list --count "$RANGE" 2>/dev/null); then
  echo "publish: range invalido: ${RANGE}" >&2
  exit 2
fi
echo "publish: commits no range: ${NCOMMITS}"
if [ "$NCOMMITS" -eq 0 ]; then
  echo "publish: nada a publicar (range vazio)."
  exit 0
fi

#  5. Excluir o script INTEIRO da varredura escondia segredo real dentro dele — e o
#     conteudo dele E publicado. A isencao agora e so o bloco publish-patterns:*.
#  6. As FIXTURES do auto-teste ficavam FORA da janela de isencao e o proprio
#     scanner abortava no seu conteudo (falso POSITIVO). Corrigido nas duas pontas:
#     fixtures montadas em partes (como o s_gh) E isencao estreita das linhas de
#     atribuicao de fixture, para que re-auditar o historico ja publicado passe.
# ATENCAO (seis defeitos reais ja corrigidos aqui):
#  1. `git grep <padrao> A..B` NAO funciona — git grep quer TREE/commit, nao
#     intervalo; com range ele devolve vazio e a varredura PARECE limpa.
#  2. `git grep <padrao> <rev>` varre a ARVORE INTEIRA daquele commit, inclusive
#     arquivos herdados e JA PUBLICOS — o contrato e varrer o DIFF DO RANGE.
#  3. O casamento NAO pode ser feito em awk: `\b` nao existe em awk (o padrao de
#     IP nunca casaria) e o auto-teste usa grep -E. Teste e producao TEM de usar a
#     MESMA engine, senao o teste valida o que a producao nao executa.
# Estrutura: `git show` por commit (pega segredo adicionado E removido no range),
# awk so para EXTRAIR rev:arquivo:linha:conteudo das linhas ADICIONADAS, e o
# casamento em grep -E. O `cut` descarta o conteudo: o valor nunca e impresso.
REVS=$(git rev-list "$RANGE")

# Extrai rev:arquivo:linha:conteudo das linhas ADICIONADAS de um commit.
# Unica isencao: o bloco delimitado por publish-patterns:start/end (as proprias
# definicoes dos padroes). Excluir o arquivo INTEIRO esconderia segredo real nele.
extract_added() {  # $1 = rev
  git show --format= --no-color --unified=0 "$1" 2>/dev/null | awk -v rev="$1" '
    /^\+\+\+ b\// { f = substr($0, 7); next }
    /^@@/ { if (match($0, /\+[0-9]+/)) n = substr($0, RSTART + 1, RLENGTH - 1) + 0; next }
    /^\+/ {
      if ($0 ~ /^\+# publish-patterns:start$/) { inpat = 1; n++; next }
      if ($0 ~ /^\+# publish-patterns:end$/)   { inpat = 0; n++; next }
      # Fixture do auto-teste: sintetica POR CONSTRUCAO. Isencao ESTREITA — so a
      # linha de atribuicao de fixture (local s_*), nunca o resto do arquivo.
      # Existe para que re-auditar o historico ja publicado nao acuse as fixtures
      # dos commits anteriores ao fix (defeito 6).
      if ($0 ~ /^\+[[:space:]]*local s_(pem|gh|pat|aws|ip|url|auth)=/) { n++; next }
      if (!inpat) print rev ":" f ":" n ":" $0
      n++; next
    }
  '
}

scan_range() {  # $1 = regex ; imprime rev:arquivo:linha (NUNCA o conteudo)
  local rev
  for rev in $REVS; do extract_added "$rev"; done | grep -E -e "$1" | cut -d: -f1-3 | sort -u
}

HITS=0
echo "publish: varredura de segredo (mostra TIPO rev:arquivo:linha, nunca o valor)"
# Controle POSITIVO do MECANISMO: a extracao das linhas adicionadas tem de
# produzir saida. Sem isto, "0 hits" pode significar "extracao quebrada".
# NAO ancore o controle em CONTEUDO (ex.: uma palavra que "deve" existir): da
# falso negativo quando o range so mexe em arquivos excluidos, como o proprio
# script (medido: um commit que so alterava o publish.sh abortou o controle).
if [ -z "$(for rev in $REVS; do extract_added "$rev"; done | head -1)" ]; then
  echo "publish: ABORTADO — controle positivo falhou: a extracao nao produz linhas adicionadas." >&2
  exit 3
fi
echo "publish: controle positivo OK (a extracao le as linhas adicionadas do range)."
for entry in "${PATTERNS[@]}"; do
  name="${entry%%:*}"; rx="${entry#*:}"
  found=$(scan_range "$rx")
  if [ -n "$found" ]; then
    HITS=$((HITS + 1))
    echo "  HIT [${name}]:"
    echo "$found" | sed 's/^/    /'
  fi
done
if [ "$HITS" -gt 0 ]; then
  echo "publish: ABORTADO — ${HITS} tipo(s) de segredo no range. Nada foi enviado." >&2
  echo "publish: revise os hits acima (o valor NAO foi impresso de proposito)." >&2
  exit 1
fi
echo "publish: varredura limpa (0 hits em ${#PATTERNS[@]} padroes)."

[ "$SCAN_ONLY" -eq 1 ] && { echo "publish: --scan-only, parando aqui."; exit 0; }

# --- push (auth que o host JA tem; nada persistido) -------------------------
# O commit ja aconteceu ANTES do scan (ver acima): o que se empurra aqui e
# exatamente o que foi varrido.
PUSH_ARGS=()
if ! git config --get credential.helper >/dev/null 2>&1 \
   && command -v gh >/dev/null 2>&1 \
   && gh auth status >/dev/null 2>&1; then
  # helper do gh SO nesta invocacao: nao escreve em gitconfig, nao grava token
  PUSH_ARGS=(-c credential.helper='!gh auth git-credential')
  echo "publish: usando a autenticacao existente do gh (apenas neste comando)"
fi

echo "publish: enviando para origin/${BRANCH}..."
if ! git "${PUSH_ARGS[@]}" push origin "$BRANCH"; then
  echo "publish: FALHOU o push. Entregavel = este erro + este script. Nao vou contornar a autenticacao." >&2
  exit 1
fi

# --- verificacao ------------------------------------------------------------
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git ls-remote origin "refs/heads/${BRANCH}" | cut -f1)
echo "publish: HEAD local      = ${LOCAL}"
echo "publish: origin/${BRANCH} = ${REMOTE}"
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "publish: OK — remoto == local (${NCOMMITS} commits no range)."
else
  echo "publish: DIVERGENCIA — remoto != local" >&2
  exit 1
fi
