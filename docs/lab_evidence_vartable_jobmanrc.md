# Relatório Técnico: Resolução de VARTABLE vs PATH no .jobmanrc (TWS/HWA 10.2.8)

## 1. Contexto e Objetivo
Investigação empírica realizada no laboratório HWA 10.2.8 (`tws-hwa` MDM / `tws-bmdm` FTA) para caracterizar o comportamento de resolução de variáveis de tabela (`VARTABLE`), herança de variáveis de ambiente (`PATH`), e a arquitetura de interceptação defensiva via `$HOME/.jobmanrc`.

---

## 2. Fatos e Comportamentos Descobertos

### 2.1 Resolução de VARTABLE pelo TWS/HWA
1. **Resolução em Nível de Linha de Comando (Substituição Estática Pré-Jobmanrc)**:
   - Variáveis delimitadas por circunflexo (`^VAR_NAME^`) referenciadas na tabela de variáveis do Job Stream (`VARTABLE FTA_TEST_TBL`) são substituídas pelo compilador/gerenciador do TWS **antes** do JCL ser entregue ao executor local (`jobmanrc`).
   - Se o JCL define:
     ```text
     DOCOMMAND "export PATH=^FTA_VALID_DIR^:$PATH && meu_worker.sh"
     ```
     O `jobmanrc` recebe:
     ```bash
     export PATH=/tmp/fta_bin:$PATH && meu_worker.sh
     ```
2. **Não Injeção em Variáveis de Ambiente de Processo**:
   - As variáveis definidas na `VARTABLE` **NÃO** são automaticamente exportadas para o ambiente do processo (`ENV`) do usuário (`$FTA_VAR_FOO` chega vazio a menos que explicitamente atribuída no JCL ou exportada via script).
   - Teste comprovado:
     `echo ENV_VAR_FOO is [$FTA_VAR_FOO] && echo JCL expanded is [^FTA_VAR_FOO^]`
     Resultado no log:
     `ENV_VAR_FOO is []`
     `JCL expanded is [VALOR_INJETADO_FOO]`
3. **Falha Silenciosa de Variáveis Inexistentes na Tabela**:
   - Se uma variável não existe na `VARTABLE` (ex: `^VAR_NAO_EXISTE_DIR^` ou `^FTA_CUSTOM_BIN^`), o TWS **não aborta a submissão nem a compilação do job stream**.
   - O TWS envia o texto **literal com os circunflexos** (`^VAR_NAO_EXISTE_DIR^`) diretamente para o executor.
   - Isso resulta em falhas tardias em tempo de execução:
     - Erro de comando: `/opt/hwa/TWS/TWS/jobmanrc: line 342: ^VAR_NAO_EXISTE_DIR^/worker.sh: No such file or directory` (Exit Code 127).
     - Erro de PATH corrupto: `which: no meu_worker.sh in (^FTA_CUSTOM_BIN^:/usr/local/bin:...)` (Exit Code 1).

---

### 2.2 Arquitetura do `.jobmanrc` na FTA e Mecânica de Execução
1. **Hierarquia de Chamada**:
   - O binário `/opt/hwa/TWS/TWS/bin/jobman` invoca o wrapper mestre `/opt/hwa/TWS/TWS/jobmanrc`.
   - Se o arquivo `$HOME/.jobmanrc` existir no diretório home do usuário de execução (`STREAMLOGON`), o wrapper mestre chama `$HOME/.jobmanrc`.
2. **Comportamento das Variáveis de Ambiente no `.jobmanrc`**:
   - Ao executar `$HOME/.jobmanrc`, o ambiente é populado com metadados do TWS:
     - `UNISON_JCL`: O comando completo ou path do script a ser executado.
     - `UNISON_JOB`, `UNISON_CPU`, `UNISON_SCHED`, `UNISON_JOBNUM`, `UNISON_STDLIST`.
   - Importante: Na chamada do `$HOME/.jobmanrc`, os argumentos `$1` e `$2` podem vir vazios dependendo da flag `USE_SHELL` configurada no ambiente do agente; no entanto, **`UNISON_JCL` está invariavelmente populado e preservado**.
3. **Execução Segura**:
   - Para permitir comandos com pipes, exports múltiplos e cadeias lógicas (`&&`), o `$HOME/.jobmanrc` deve invocar:
     ```bash
     eval "$UNISON_JCL"
     ```
     Evitando `exec "$UNISON_JCL"` que falha com exit code 127 ao tentar tratar strings compostas como um único executável.

---

### 2.3 Padrão Defensivo de Proteção (Guard Hook no `.jobmanrc`)
Para evitar que variáveis não resolvidas causem danos a arquivos ou executem em caminhos imprevisíveis, foi desenhado e homologado no lab o seguinte hook em `/home/wauser/.jobmanrc`:

```bash
#!/bin/bash
# Hook defensivo padrao HCL/TWS no .jobmanrc da FTA

echo "[JOBMANRC_GUARD] Avaliando UNISON_JCL: $UNISON_JCL" >&2

# 1. Defesa preventiva contra variaveis de VARTABLE nao resolvidas
if echo "$UNISON_JCL" | grep -E '\^[A-Za-z0-9_]+\^' >/dev/null; then
    echo "[GUARD_ABORT] ERRO FATAL: Variavel de VARTABLE nao resolvida no JCL: $UNISON_JCL" >&2
    exit 99
fi

# 2. Execucao via eval
eval "$UNISON_JCL"
```

#### Evidência de Validação no Lab:
- **Cenário Variável Inexistente**: Job `JOB_GUARD_FAIL` submetido com `^VAR_INEXISTENTE_ERR^`.
  - Resultado: Interceptado imediatamente pelo guard hook.
  - Status: `ABEND` (Exit Code 99).
  - Log: `[GUARD_ABORT] ERRO FATAL: Variavel de VARTABLE nao resolvida no JCL: ... ^VAR_INEXISTENTE_ERR^`.
- **Cenário Variável Resolvida**: Job executando com `^FTA_VALID_DIR^`.
  - Resultado: Passou pelo guard hook, expandiu para `/tmp/fta_bin`, executou `meu_worker.sh` com sucesso.
  - Status: `SUCC` (Exit Code 0).
