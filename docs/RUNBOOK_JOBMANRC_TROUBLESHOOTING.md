# RUNBOOK: Resolução de Falhas de Execução em FTA (jobmanrc, PATH e Permission Denied)

## 1. Contexto e Arquitetura de Execução

No **HCL Workload Automation (HWA) 10.2.8 Distributed**, a execução de jobs em agentes tolerantes a falhas (FTA) e no Master Domain Manager (MDM) segue um fluxo estrito gerenciado pelos processos `jobman` e `JobManager`:

1. **Agendamento e Despacho**: O `batchman` envia a ordem de execução do job ao `jobman` da estação de trabalho destino via Symphony/Sinfonia.
2. **Wrapper de Lançamento (`jobmanrc`)**: O processo `jobman` roda sob privilégios de sistema e chaveia (`su - <logon_user>`) para o usuário configurado na definição do job. Ele invoca o wrapper `/opt/hwa/TWS/jobmanrc` (apontando para `TWSDATA/jobmanrc`).
3. **Interceptação por `.jobmanrc` Local**: Se a opção `LOCAL_RC_OK="YES"` estiver ativa (padrão de fábrica) e o usuário de logon possuir um executável `$HOME/.jobmanrc`, o script global delega a execução para o script local do usuário, passando o comando/script como `$1` e `IS_COMMAND` (`YES`/`NO`) como `$2`.
4. **Captura de Stdlist**: Toda a saída padrão e erros gerados durante a execução são gravados no diretório `TWSDATA/stdlist/YYYY.MM.DD/O<jobnum>.<time>`.

---

## 2. Diagnóstico de Falhas Comuns de Execução

### Cenário A: Falha de PATH (`127 / command not found`)
* **Sintoma no Conman**: Job entra em estado `ABEND` com retorno de código `127`.
* **Evidência no stdlist**:
  ```text
  WA for UNIX/JOBMANRC 10.2.8.00-2026.07
  AWSBIS307I Starting /opt/hwa/TWS/TWS/jobmanrc my_custom_tool
  /opt/hwa/TWS/TWS/jobmanrc: line 342: my_custom_tool: command not found
  AWSBIS308I End of job
  Exit Status : 127
  ```
* **Causa Raiz**: O ambiente básico gerado pelo `jobmanrc` herda apenas o `PATH` padrão do sistema (`/bin:/usr/bin`). Se o binário residir em `/opt/custom/bin` ou no `$HOME/bin` do usuário sem caminho absoluto no JCL, a chamada falha.
* **Ações de Remediação**:
  1. *Opção 1 (Recomendada no JCL)*: Definir o caminho absoluto completo na diretiva `SCRIPTNAME` do job (ex: `/home/wauser/test_jobman/my_custom_tool`).
  2. *Opção 2 (Configuração via `.jobmanrc`)*: Implementar o script `$HOME/.jobmanrc` para exportar as variáveis de ambiente e diretórios no `PATH` antes da execução.

---

### Cenário B: Falha de Permissão de Execução (`126 / Permission denied`)
* **Sintoma no Conman**: Job entra em estado `ABEND` com retorno de código `126`.
* **Evidência no stdlist**:
  ```text
  WA for UNIX/JOBMANRC 10.2.8.00-2026.07
  AWSBIS307I Starting /opt/hwa/TWS/TWS/jobmanrc /home/wauser/test_jobman/run_permission_test.sh
  /opt/hwa/TWS/TWS/jobmanrc: line 342: /home/wauser/test_jobman/run_permission_test.sh: Permission denied
  AWSBIS308I End of job
  Exit Status : 126
  ```
* **Causa Raiz**: O script ou binário referenciado no JCL não possui permissão de leitura ou execução para o usuário (`chmod +x`), ou o sistema de arquivos destino foi montado com flag `noexec`.
* **Ações de Remediação**:
  1. Conceder permissão de execução: `chmod 755 /caminho/do/script.sh`.
  2. Assegurar que o proprietário e grupo do arquivo sejam compatíveis com o usuário de logon TWS (`chown <user>:<group>`).
  3. Verificar se o interpretador no shebang (`#!/bin/bash` ou `#!/bin/sh`) existe e é executável.

---

## 3. Casos de Uso Avançados do `jobmanrc` e `.jobmanrc`

### 1. Injeção de Perfis e Variáveis Globais de Ambiente
Em ambientes heterogêneos (Oracle, SAP, Java, Python), cada usuário pode exigir variáveis (`JAVA_HOME`, `ORACLE_SID`, `LD_LIBRARY_PATH`). O script `$HOME/.jobmanrc` centraliza o carregamento dos perfis corporativos:
```sh
#!/bin/sh
# Carrega perfil de producao se existir
[ -f /etc/profile ] && . /etc/profile
[ -f $HOME/.profile ] && . $HOME/.profile

if [ "$2" = "YES" ]; then
    eval "$1"
else
    exec "$1"
fi
```

### 2. Governança e Restrição por `localrc.allow` / `localrc.deny`
Por padrão, `LOCAL_RC_OK="YES"` permite que qualquer usuário com `.jobmanrc` execute lógica customizada. Para restringir essa funcionalidade:
* Crie o arquivo `/opt/hwa/TWSDATA/localrc.allow` contendo apenas os usuários autorizados (um por linha).
* Alternativamente, utilize `/opt/hwa/TWSDATA/localrc.deny` para barrar contas de serviço ou operadores específicos.

### 3. Fail-Closed com `UNISON_EXIT="YES"`
No `jobmanrc` padrão de fábrica, comandos encadeados continuam mesmo após falha intermediária (`UNISON_EXIT="NO"`). Para ambientes críticos onde qualquer erro em script deve interromper imediatamente a esteira, defina `UNISON_EXIT="YES"` no `/opt/hwa/TWSDATA/jobmanrc`.

### 4. Notificação Direta via `MAIL_ON_ABEND`
Configurando `MAIL_ON_ABEND="YES"` ou especificando um endereço (`MAIL_ON_ABEND="operacoes@empresa.com"`), o `jobmanrc` despacha automaticamente um alerta contendo o identificador do job e a localização do arquivo `stdlist` no caso de código de saída não-zero.
