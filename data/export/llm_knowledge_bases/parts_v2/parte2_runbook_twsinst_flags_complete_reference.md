# PARTE2 RUNBOOK TWSINST FLAGS COMPLETE REFERENCE

## RUNBOOK: Catálogo Canônico e Referência Completa de Flags do Instalador `twsinst` (HWA 10.2.8)

**Arquivo de origem:** `data/runbooks/twsinst-flags-complete-reference.md`

### 1. Modos de Operação (Tipos de Ação)

O `twsinst` exige a declaração de exatamente um dos 5 modos de operação mutuamente exclusivos:

| Flag de Modo | Descrição | Parâmetros Obrigatórios Mínimos | Escopo |
|---|---|---|---|
| `-new` | Instalação limpa de novo agente | `-acceptlicense yes`, `-uname <user>` | Dynamic, FTA, Both, zCentric |
| `-update` | Atualização/upgrade de versão de um agente existente | `-acceptlicense yes`, `-uname <user>` | Preserva ou migra instâncias existentes |
| `-modify` | Modificação de agente existente (adiciona Java Runtime / JRE) | `-acceptlicense yes`, `-uname <user>`, `-addjruntime true` | Habilita tipos de jobs com opções avançadas |
| `-uninst` | Desinstalação completa do agente da máquina | `-uname <user>` | Finaliza processos e remove arquivos/registros |
| `-restore` | Restauração para a versão da imagem de backup anterior | `-acceptlicense yes`, `-uname <user>` | Procedimento de rollback pós-falha de update |
| `-u` / `-v` | Exibe tela de ajuda (usage) ou versão do instalador | N/A | Informativo |

---

### 2. Flags Globais e Comuns de Instalação

| Flag | Tipo de Dado | Default | Modos Válidos | Descrição e Regras de Validação |
|---|---|---|---|---|
| `-acceptlicense` | `yes \| no` | N/A (obrigatório) | `-new`, `-update`, `-modify`, `-restore` | Aceite dos termos de licença. Se diferente de `yes`, a execução aborta imediatamente (`AWSFAB009E`). |
| `-uname` | `string` | N/A (obrigatório) | Todos | Usuário do SO que será dono da instalação do agente. Não pode ser `root` (`AWSFAB404E`). O script checa existência no `/etc/passwd`. |
| `-inst_dir` | `caminho` | `/opt/HCL/TWA_<user>` | `-new`, `-update`, `-modify`, `-restore` | Diretório de instalação dos binários. No `-new`, exige que o diretório não contenha instalação anterior (`AWSFAB022E`). |
| `-data_dir` | `caminho` | `${INST_DIR}/TWSDATA` | `-new` | Diretório dedicado de dados do produto se o operador optar por separar binários de dados. |
| `-work_dir` | `caminho` | `$HOME/tmp/wa10.2.8.00` | `-new`, `-update`, `-restore` | Diretório temporário para descompactação e pacotes de instalação. |
| `-lang` | `código ISO` | `$LANG` (fallback `C`) | Todos | Idioma das mensagens de saída do `twsinst` (ex: `en`, `pt`, `es`, `fr`, `it`, `ja`, `zh`). |
| `-agent` | `dynamic \| fta \| both \| zcentric` | `dynamic` | `-new` | Define a arquitetura do agente: `dynamic` (orientado a broker REST), `fta` (tolerante a falhas com Symphony), `both` (ambos na mesma máquina), `zcentric` (controlado por z/OS). |
| `-addjruntime` | `true \| false` | `true` (dynamic/both), `false` (fta) | `-new`, `-update`, `-modify`, `-restore` | Inclui o runtime Java para execução de plugins e job types com opções avançadas (Cloud, REST, File Transfer, SAP). Obrigatório `true` no `-modify`. |
| `-enablefips` | `true \| false` | `false` | `-new`, `-update`, `-restore` | Na versão 10.2.8, **apenas `false` é suportado**. Fornecer `true` gera erro de incompatibilidade. |
| `-skip_usercheck` | `switch` | Desativado | Todos | Ignora a validação prévia de existência do usuário no SO (útil em ambientes com NIS/LDAP remoto ainda não conectado). |
| `-skipcheckprereq` | `switch` | Desativado | `-new`, `-update`, `-modify`, `-restore` | Ignora a verificação automatizada de pré-requisitos do sistema operacional (memória, espaço, bibliotecas). |
| `-reset_perm` | `switch` | Desativado | `-new`, `-update`, `-restore` | Reseta as permissões das bibliotecas compartilhadas sob `/usr/HCL`. |
| `-create_link` | `switch` | Desativado | `-new`, `-update`, `-restore` | Cria symlinks dos executáveis do cliente no diretório padrão `/usr/bin` do sistema. |
| `-wait` | `inteiro` | `60` (minutos) | `-uninst` | Tempo limite de espera para finalização de jobs em execução antes de forçar a desinstalação. `-1` aguarda indefinidamente. |
| `-skipbackup` | `switch` | Desativado | `-update`, `-restore` | Desativa o backup prévio da instância antes da atualização. |
| `-patch` | `switch` | Desativado | `-update` | Sinaliza que a atualização em curso é uma aplicação de correção pontual (patch/e-fix). |
| `-recovInstReg` | `true \| false` | `false` | `-update`, `-modify`, `-restore` | Reconstrói registros corrompidos de instalação e informações de Software Distribution em clusters. |

---

### 3. Flags do Agente Dinâmico (`-agent dynamic` ou `both`)

| Flag | Tipo de Dado | Default | Regras de Sintaxe e Comportamento |
|---|---|---|---|
| `-displayname` | `string (1-16 chars)` | Hostname do computador | **Nome lógico da workstation no banco de dados e conman**. Não pode começar com dígito (`0-9`). Proibidos caracteres especiais: `@ \ " , + \` * ) ( ' & $ # ! / [ . ? > = < ; : \ } { \| ~ ^`. Se omitido, assume o hostname da máquina (`AWSFAB010E`). |
| `-hostname` | `FQDN / IP` | Hostname do computador | Endereço pelo qual o Dynamic Workload Broker/Server contacta o agente JobManager. |
| `-jmport` | `1 a 65535` | `31114` | Porta TCP local onde o daemon JobManager escuta requisições. |
| `-jmportssl` | `true \| false` | `true` | Habilita criptografia HTTPS na comunicação da porta do JobManager (`31114`). |
| `-tdwbhostname` | `FQDN / IP` | `localhost` | **Hostname do Master / Dynamic Workload Broker** onde o agente se registra. Obrigatório se autenticar por `-wauser` ou `-apikey`. |
| `-tdwbport` | `1 a 65535` | `0` (não config) | **Porta HTTPS do Broker no Master** (padrão oficial: `31116`). Obrigatório junto com `-tdwbhostname`. |
| `-agentid` | `string` | Gerado automaticamente | Identificador interno persistente do agente no Broker. Mutuamente exclusivo com `-jwt true`. |
| `-gateway` | `local \| remote \| none` | `none` | Topologia de gateway para redes protegidas/NAT: `local` (gateway no próprio agente), `remote` (gateway em nó intermediário), `none` (conexão direta). |
| `-gwid` | `string` | Hostname do computador | Identificador do Gateway (válido apenas se `-gateway local`). |
| `-gweifport` | `1 a 65535` | `31132` | Porta EIF através da qual o gateway despacha eventos. |

---

### 4. Flags de Autenticação e Certificados (Matriz de Exclusão Mútua)

A partir da versão 10.2.x, o HWA exige securitização com certificados ou tokens. O instalador possui 3 caminhos de autenticação bem definidos:

### Matriz de Combinações:
| Parâmetro | Cenário A: Custom PEM | Cenário B: Download via REST | Cenário C: API Key (DWC) |
|---|---|---|---|
| `-jwt` | `false` ou omitido | `true` | `true` ou omitido |
| `-sslkeysfolder` | **Obrigatório** (pasta com ca.crt, tls.key, tls.crt) | **Proibido** (ignorado/erro 498) | **Proibido** (ignorado/erro 510) |
| `-sslpassword` | **Obrigatório** (senha p/ gerar keystore) | **Proibido** | **Proibido** |
| `-wauser` | **Proibido** (erro 486 com sslkeysfolder) | **Obrigatório** | **Proibido** (ignorado/erro 509) |
| `-wapassword` | **Proibido** (erro 486 com sslkeysfolder) | **Obrigatório** | **Proibido** |
| `-apikey` | **Proibido** | **Proibido** | **Obrigatório** (JWT gerado no DWC) |
| `-tdwbhostname` | Recomendado / Obrigatório se dinâmico | **Obrigatório** | **Obrigatório** |
| `-tdwbport` | Recomendado / Obrigatório se dinâmico | **Obrigatório** (`31116`) | **Obrigatório** (`31116`) |

* **Regra de Omissão Total (Erro `AWSFAB502E`)**: Se o operador não fornecer nenhum dos três grupos (`-sslkeysfolder`, `-wauser/-wapassword` ou `-apikey`), a instalação é abortada: `"Specify either the sslkeysfolder and sslpassword parameters, or the wauser and wapassword parameters, or apikey parameter."`.
* **Regra de Auto-Ativação do JWT**: Se `-jwt` for omitido, mas `-wauser` + `-wapassword` ou `-apikey` forem passados, o instalador infere automaticamente `-jwt true`.

---

### 5. Flags do Fault-Tolerant Agent (`-agent fta` ou `both`)

| Flag | Tipo de Dado | Default | Regras de Sintaxe e Comportamento |
|---|---|---|---|
| `-thiscpu` | `string (1-16 chars)` | Hostname do computador | **Nome da workstation FTA no Symphony/plano**. Não pode começar com dígito (`0-9`). Proibidos caracteres especiais. **Se instalado via `serverinst` ou `-agent both`, `-thiscpu` e `-displayname` DEVEM SER DIFERENTES**, caso contrário falha com `AWSFAB164E`. |
| `-master` | `string` | `MASTER` | Nome da workstation do Master Domain Manager na rede HWA. Não pode ser igual ao `-thiscpu` (`AWSFAB098E`). |
| `-company` | `string` | `COMPANY` | Nome da organização gravado no cabeçalho do arquivo Symphony e licenças. |
| `-port` | `1 a 65535` | `31111` | Porta TCP do Netman para comunicação sem SSL. |
| `-netmansslport`| `1 a 65535` | `31113` | Porta TCP do Netman para comunicação segura em SSL/TLS. |
| `-useencryption`| `true \| false` | `true` | Habilita criptografia AES-256 em repouso para os arquivos locais do plano (Symphony) e filas de mensagens. |
| `-encryptionpassword` | `string` | `default` | Senha da keystore que armazena a chave AES-256 local. |

---

### 6. Flags para Agentes z/OS (`-agent zcentric`)

| Flag | Tipo de Dado | Descrição |
|---|---|---|
| `-zhostname` | `FQDN / IP` | Hostname ou IP da partição z/OS onde reside o controlador Z-centric. |
| `-zport` | `1 a 65535` | Porta TCP/IP de comunicação com o gateway z/OS. |

---

### 7. Flags Ocultas e Internas (Engenharia HWA)

Identificadas no código-fonte do script `twsinst`:
* `-caller <MDM|DDM|customer>`: Informa a origem da chamada. Usado internamente pelo `serverinst.sh` para ignorar ou relaxar certas validações de certificados padrão.
* `-skip_check_ssl_parms`: Desativa checagens estritas de consistência de parâmetros SSL/TLS.
* `-skipconfig`: Realiza apenas a extração e deploy dos binários sem executar as etapas de pós-configuração (`configAction`).
* `-allObjAuth`: Flag restrita exclusivamente ao sistema operacional IBM i (OS/400); se usada no Linux, dispara `AWSFAB288E`.
* `-recovInstReg true`: Reconstrói os descritores do registro do produto em `/etc/TWS` ou `/var/ibm/InstallationManager` em caso de corrupção.
