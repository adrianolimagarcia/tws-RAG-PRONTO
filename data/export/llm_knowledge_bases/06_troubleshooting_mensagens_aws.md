# TROUBLESHOOTING & MENSAGENS DE ERRO

> Total de tópicos canônicos cobertos nesta seção: 225

---

### 1. hwa-10.2.8-AWSWUI-0100E-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; Dynamic Workload Console) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWSUI0100E indica que a lista de job streams não pôde ser carregada devido a um erro do engine IBM Workload Scheduler; a causa documentada é um erro ocorrido no engine, cujo ID é informado no texto da mensagem, e a recuperação é resolver o erro indicado e tentar novamente a operação.

**Plataforma / Validação:** distributed; Dynamic Workload Console

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0100E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0100E no HWA?*
- *Qual é o significado da mensagem de erro AWSWUI0100E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSWUI0100E no HWA?*
- *Qual é o significado da mensagem de erro AWSWUI0100E no HWA e qual ação é recomendada?*
- *Qual é o significado da mensagem de erro AWSUI0100E no HWA e qual ação é recomendada?*

---

### 2. hwa-10.2.8-AWSZAP-002E-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; action plug-in for z/OS) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWSZAP002E indica que a submissão de um job stream no subsistema z/OS não foi bem-sucedida; a causa é fornecida no texto da própria mensagem (campo reason), e a recuperação documentada é usar a mensagem de reason para determinar a causa, corrigir o problema se possível e tentar novamente, ou pesquisar a base de suporte IBM.

**Plataforma / Validação:** distributed; action plug-in for z/OS

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSZAP002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSZAP002E no HWA?*
- *Qual é o significado da mensagem de erro AWSZAP002E no HWA e qual ação é recomendada?*

---

### 3. hwa-10.2.8-AWSZAP-003E-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; action plug-in for z/OS) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
Em HCL Workload Automation 10.2.8, a mensagem AWSZAP003E indica que o valor de um parâmetro não está no formato correto key=value; a causa é remetida ao texto da mensagem, e a recuperação documentada é escrever o parâmetro indicado no formato correto e tentar novamente.

**Plataforma / Validação:** distributed; action plug-in for z/OS

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSZAP003E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSZAP003E no HWA?*
- *Qual é o significado da mensagem de erro AWSZAP003E no HWA e qual ação é recomendada?*

---

### 4. hwa-10.2.8-aida-es-oom-0003

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: AI Data Advisor (AIDA) > Interface: Geral > Tópico: aida > troubleshooting [aida_troubleshoot]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o container OpenSearch (aida-es) do AI Data Advisor pode falhar com ExitCode 137 / OOMKilled quando os limits de memoria default do docker-compose.yml (8G) e o heap default da JVM (metade do limite do cgroup) excedem a RAM disponivel no host; em maquinas com pouca RAM (ex.: 11.5GiB no lab), a correcao pratica e definir ES_JAVA_OPTS e OPENSEARCH_JAVA_OPTS=-Xms768m -Xmx768m, elevar o limit do es para 3G (reservation 1.5G) e reduzir limits de outros servicos (keycloak 768M, predictor 768M, ui 512M). O OpenSearch tambem exige vm.max_map_count >= 262144 no HOST (sysctl), nao dentro do container; o Dockerfile-es ja adiciona esta config ao /etc/sysctl.conf da imagem.

**Plataforma / Validação:** Distributed; Linux x86_64

---

### 5. hwa-10.2.8-eqq199e-distributed-0001

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed (fora de escopo para claims de motor distributed)) > Componente: Workload Automation for Z (z/OS Engine) > Interface: Geral > Tópico: incidents > error [error]]`

**Regra Canônica / Evidência:**
EQQ199E is an error code from HCL Workload Automation for Z (z/OS), not from the Distributed platform. The EQQ message prefix belongs to the z/OS engine; generalizing EQQ error codes to distributed environments is incorrect.

**Plataforma / Validação:** distributed (fora de escopo para claims de motor distributed)

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro EQQ199E no HWA?*
- *Como solucionar ou diagnosticar o erro EQQ199E no HWA?*
- *Qual é o significado da mensagem de erro EQQ199E no HWA e qual ação é recomendada?*

---

### 6. hwa-10.2.8-messages-awsui0002e-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0002E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a user name that contains only supported characters. Wizard installation Re-enter the user name ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0002E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0002E no HWA e qual ação é recomendada?*

---

### 7. hwa-10.2.8-messages-awsui0004e-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0004E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a password that contains only supported characters. Wizard installation Re-enter the password ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0004E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0004E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0004E no HWA e qual ação é recomendada?*

---

### 8. hwa-10.2.8-messages-awsui0005e-0009

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0005E indica um problema no Dynamic Workload Console: The confirm password must be the same as the password. O sistema The graphical wizard installation, stops with an error message. A acao documentada e: Re-enter the password and confirm password ensuring they are the same, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0005E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0005E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0005E no HWA e qual ação é recomendada?*

---

### 9. hwa-10.2.8-messages-awsui0007e-0010

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0007E indica um problema no Dynamic Workload Console: A value must be entered in the password field. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid password, and launch a new installation. Wizard installation Enter a valid password, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0007E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0007E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0007E no HWA e qual ação é recomendada?*

---

### 10. hwa-10.2.8-messages-awsui0009e-0011

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0009E indica um problema no Dynamic Workload Console: The entered value contains characters that are not supported. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying an installation path that contains only supported characters. Wizard installation Re-enter the installation path ensuring that it does not contain any unsupported characters, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0009E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0009E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0009E no HWA e qual ação é recomendada?*

---

### 11. hwa-10.2.8-messages-awsui0011e-0012

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0011E indica um problema no Dynamic Workload Console: The specified INSTALL_METHOD is not valid. O sistema The installation exits with an error. A acao documentada e: Edit the response file specifying a supported installation method..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0011E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0011E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0011E no HWA e qual ação é recomendada?*

---

### 12. hwa-10.2.8-messages-awsui0014e-0013

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0014E indica um problema no Dynamic Workload Console: The value entered as TCP/IP port is not valid. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid TCP/IP port number, and launch a new installation. Wizard installation Re-enter a valid TCP/IP port number, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0014E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0014E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0014E no HWA e qual ação é recomendada?*

---

### 13. hwa-10.2.8-messages-awsui0016e-0014

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0016E indica um problema no Dynamic Workload Console: The value entered for TCP/IP port has already been assigned to the other ports indicated in the message text. O sistema The installation stops with an error message. A acao documentada e: Re-enter a new TCP/IP port number, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0016E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0016E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0016E no HWA e qual ação é recomendada?*

---

### 14. hwa-10.2.8-messages-awsui0020e-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0020E indica um problema no Dynamic Workload Console: A value must be entered in the service ID field. O sistema The installation stops with an error message. A acao documentada e: Enter a valid service ID, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0020E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0020E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0020E no HWA e qual ação é recomendada?*

---

### 15. hwa-10.2.8-messages-awsui0023e-0016

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0023E indica um problema no Dynamic Workload Console: The values entered as credentials for IBM Integrated Portal are incorrect. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying valid credentials, and start a new installation. Wizard installation Enter the credentials again, ensuring that they are valid, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0023E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0023E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0023E no HWA e qual ação é recomendada?*

---

### 16. hwa-10.2.8-messages-awsui0025e-0017

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0025E indica um problema no Dynamic Workload Console: This installation mode is not supported. O sistema Installation does not start. A acao documentada e: Launch a new installation using one of the supported methods: either the graphical wizard or the silent installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0025E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0025E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0025E no HWA e qual ação é recomendada?*

---

### 17. hwa-10.2.8-messages-awsui0026e-0018

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0026E indica um problema no Dynamic Workload Console: The uninstallation completed but not all the files have been removed. You can find the error messages in the log file, before current error. O sistema The system uninstalls the application but leaves some files to be removed manually. A acao documentada e: Check the errors that caused the uninstallation failure in the log file. Optionally, remove the unnecessary files that have not been uninstalled properly..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0026E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0026E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0026E no HWA e qual ação é recomendada?*

---

### 18. hwa-10.2.8-messages-awsui0028e-0019

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0028E indica um problema no Dynamic Workload Console: The installation of the product requires security to be enabled on the selected instance of IBM Integrated Portal. O sistema The installation exits with an error message. A acao documentada e: Enable security on the selected instance of IBM Integrated Portal or select a different instance of IBM Integrated Portal that has security enabled..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0028E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0028E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0028E no HWA e qual ação é recomendada?*

---

### 19. hwa-10.2.8-messages-awsui0030w-0020

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0030W indica um problema no Dynamic Workload Console: The availability of the specified TCP/IP port could not be verified. O sistema Installation continues without checking port availability. A acao documentada e: Proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0030W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0030W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0030W no HWA e qual ação é recomendada?*

---

### 20. hwa-10.2.8-messages-awsui0031e-0021

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0031E indica um problema no Dynamic Workload Console: A location must be specified for the WebSphere Update Installer. O sistema The installation stops with an error message. A acao documentada e: Enter a valid location, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0031E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0031E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0031E no HWA e qual ação é recomendada?*

---

### 21. hwa-10.2.8-messages-awsui0033w-0022

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0033W indica um problema no Dynamic Workload Console: It was not possible to verify if IBM Integrated Portal is correctly installed. O sistema Installation continues. A acao documentada e: Check that IBM Integrated Portal is installed correctly, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0033W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0033W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0033W no HWA e qual ação é recomendada?*

---

### 22. hwa-10.2.8-messages-awsui0034e-0023

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0034E indica um problema no Dynamic Workload Console: The IBM Integrated Portal profile that does not exist. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a directory where the IBM Integrated Portal was installed, and start the installation again. Wizard installation Specify a directory where the IBM Integrated Portal was installed and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0034E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0034E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0034E no HWA e qual ação é recomendada?*

---

### 23. hwa-10.2.8-messages-awsui0036e-0024

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0036E indica um problema no Dynamic Workload Console: The IBM Integrated Portal cell does not exist. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a different directory, and start the installation again. Wizard installation Specify a directory that contains an instance of IBM Integrated Portal, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0036E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0036E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0036E no HWA e qual ação é recomendada?*

---

### 24. hwa-10.2.8-messages-awsui0038e-0025

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0038E indica um problema no Dynamic Workload Console: The specified directory does not contain any WebSphere Update Installer. O sistema If you are running the graphical wizard installation, the installation stops with an error message. If you are running the silent installation, the installation exits with an error. A acao documentada e: If you are running: Silent installation Edit the response file specifying a valid directory, and launch a new installation. Wizard installation Specify a valid directory, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0038E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0038E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0038E no HWA e qual ação é recomendada?*

---

### 25. hwa-10.2.8-messages-awsui0043e-0026

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0043E indica um problema no Dynamic Workload Console: It is not possible to install more than one instance of Dynamic Workload Console on the same system. O sistema Installation fails. A acao documentada e: Uninstall the existing Dynamic Workload Console or install the new Dynamic Workload Console on a different system..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0043E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0043E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0043E no HWA e qual ação é recomendada?*

---

### 26. hwa-10.2.8-messages-awsui0045e-0027

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0045E indica um problema no Dynamic Workload Console: It is not possible to install the Dynamic Workload Console Fix Pack 2 more than once on the same system. O sistema The installation fails. A acao documentada e: Uninstall the existing Dynamic Workload Console or install the Dynamic Workload Console Fix Pack 2 on a different system..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0045E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0045E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0045E no HWA e qual ação é recomendada?*

---

### 27. hwa-10.2.8-messages-awsui0046e-0028

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0046E indica um problema no Dynamic Workload Console: A Windows Service ID was specified that already exists in the registry. O sistema The graphical wizard installation stops with an error message. A acao documentada e: Specify a valid Windows Service ID, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0046E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0046E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0046E no HWA e qual ação é recomendada?*

---

### 28. hwa-10.2.8-messages-awsui0048e-0029

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0048E indica um problema no Dynamic Workload Console: The Windows Service ID specified for the WAS_SERVICE_NAME variable in the response file already exists in the registry. O sistema The silent installation fails with an error. A acao documentada e: Specify a valid Windows Service ID in the response file, and launch a new installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0048E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0048E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0048E no HWA e qual ação é recomendada?*

---

### 29. hwa-10.2.8-messages-awsui0070w-0030

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0070W indica um problema no Dynamic Workload Console: You have selected to upgrade Dynamic Workload Console, but the instance of Dynamic Workload Console found on the system cannot be upgraded. O sistema If you are running the interactive wizard, the wizard stops. If you are running the silent installation, the installation fails. A acao documentada e: Proceed as follows:.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0070W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0070W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0070W no HWA e qual ação é recomendada?*

---

### 30. hwa-10.2.8-messages-awsui0079e-0031

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0079E indica um problema no Dynamic Workload Console: A more recent version of the Dynamic Workload Console fix pack is installed on the workstation. It is no longer possible to perform the rollbackoperation with the Fix Pack 2. O sistema Installation stops. A acao documentada e: Click Cancel to exit from the installation wizard. Proceed with the installation of a more recent fix pack.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0079E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0079E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0079E no HWA e qual ação é recomendada?*

---

### 31. hwa-10.2.8-messages-awsui0083e-0032

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0083E indica um problema no Dynamic Workload Console: The specified directory does not contain any instance of IBM Integrated Portal. O sistema If you are running a graphical wizard installation, the installation stops and displayes an error message. If you are running a silent installation, the installation exits with an error message. A acao documentada e: If you are running: Silent installation Edit the response file specifying a different directory, and start the installation again. Wizard installation Specify a directory that contains an instance of IBM Integrated Portal, and proceed with the installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0083E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0083E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0083E no HWA e qual ação é recomendada?*

---

### 32. hwa-10.2.8-messages-awsui0101e-0033

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0101E indica um problema no Dynamic Workload Console: The plan view could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0101E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0101E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0101E no HWA e qual ação é recomendada?*

---

### 33. hwa-10.2.8-messages-awsui0102e-0034

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0102E indica um problema no Dynamic Workload Console: The resource list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0102E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0102E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0102E no HWA e qual ação é recomendada?*

---

### 34. hwa-10.2.8-messages-awsui0104e-0035

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0104E indica um problema no Dynamic Workload Console: The workstation list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0104E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0104E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0104E no HWA e qual ação é recomendada?*

---

### 35. hwa-10.2.8-messages-awsui0106e-0036

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0106E indica um problema no Dynamic Workload Console: The job stream could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0106E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0106E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0106E no HWA e qual ação é recomendada?*

---

### 36. hwa-10.2.8-messages-awsui0107e-0037

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0107E indica um problema no Dynamic Workload Console: The Job Stream Editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0107E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0107E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0107E no HWA e qual ação é recomendada?*

---

### 37. hwa-10.2.8-messages-awsui0109e-0038

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0109E indica um problema no Dynamic Workload Console: The Resource Editor could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0109E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0109E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0109E no HWA e qual ação é recomendada?*

---

### 38. hwa-10.2.8-messages-awsui0111e-0039

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0111E indica um problema no Dynamic Workload Console: The job stream could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0111E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0111E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0111E no HWA e qual ação é recomendada?*

---

### 39. hwa-10.2.8-messages-awsui0112e-0040

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0112E indica um problema no Dynamic Workload Console: The resource availability definition could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0112E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0112E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0112E no HWA e qual ação é recomendada?*

---

### 40. hwa-10.2.8-messages-awsui0114e-0041

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0114E indica um problema no Dynamic Workload Console: The job stream could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0114E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0114E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0114E no HWA e qual ação é recomendada?*

---

### 41. hwa-10.2.8-messages-awsui0116e-0042

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0116E indica um problema no Dynamic Workload Console: The resource could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0116E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0116E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0116E no HWA e qual ação é recomendada?*

---

### 42. hwa-10.2.8-messages-awsui0121e-0043

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0121E indica um problema no Dynamic Workload Console: In job A you have defined a dependency on job B, but job B is dependent, directly or indirectly, on job A. O sistema The requested action was not completed successfully. A acao documentada e: Define a valid dependency that does not create a circular dependency. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0121E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0121E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0121E no HWA e qual ação é recomendada?*

---

### 43. hwa-10.2.8-messages-awsui0125e-0044

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0125E indica um problema no Dynamic Workload Console: The workstation could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0125E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0125E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0125E no HWA e qual ação é recomendada?*

---

### 44. hwa-10.2.8-messages-awsui0127e-0045

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0127E indica um problema no Dynamic Workload Console: There was a class cast exception due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0127E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0127E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0127E no HWA e qual ação é recomendada?*

---

### 45. hwa-10.2.8-messages-awsui0128e-0046

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0128E indica um problema no Dynamic Workload Console: There is a problem with the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0128E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0128E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0128E no HWA e qual ação é recomendada?*

---

### 46. hwa-10.2.8-messages-awsui0130e-0047

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0130E indica um problema no Dynamic Workload Console: The job dependency could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0130E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0130E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0130E no HWA e qual ação é recomendada?*

---

### 47. hwa-10.2.8-messages-awsui0132e-0048

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0132E indica um problema no Dynamic Workload Console: The job could not be changed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0132E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0132E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0132E no HWA e qual ação é recomendada?*

---

### 48. hwa-10.2.8-messages-awsui0133e-0049

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0133E indica um problema no Dynamic Workload Console: The job could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0133E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0133E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0133E no HWA e qual ação é recomendada?*

---

### 49. hwa-10.2.8-messages-awsui0135e-0050

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0135E indica um problema no Dynamic Workload Console: The instance could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0135E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0135E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0135E no HWA e qual ação é recomendada?*

---

### 50. hwa-10.2.8-messages-awsui0137e-0051

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0137E indica um problema no Dynamic Workload Console: The instance could not be released due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0137E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0137E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0137E no HWA e qual ação é recomendada?*

---

### 51. hwa-10.2.8-messages-awsui0138e-0052

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0138E indica um problema no Dynamic Workload Console: The object could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0138E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0138E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0138E no HWA e qual ação é recomendada?*

---

### 52. hwa-10.2.8-messages-awsui0140e-0053

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0140E indica um problema no Dynamic Workload Console: The status in the database could not be modified due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0140E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0140E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0140E no HWA e qual ação é recomendada?*

---

### 53. hwa-10.2.8-messages-awsui0142e-0054

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0142E indica um problema no Dynamic Workload Console: The job dependency could not be removed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0142E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0142E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0142E no HWA e qual ação é recomendada?*

---

### 54. hwa-10.2.8-messages-awsui0143e-0055

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0143E indica um problema no Dynamic Workload Console: The dependency could not be removed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0143E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0143E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0143E no HWA e qual ação é recomendada?*

---

### 55. hwa-10.2.8-messages-awsui0145e-0056

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0145E indica um problema no Dynamic Workload Console: The action could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0145E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0145E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0145E no HWA e qual ação é recomendada?*

---

### 56. hwa-10.2.8-messages-awsui0150e-0057

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0150E indica um problema no Dynamic Workload Console: The action could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0150E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0150E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0150E no HWA e qual ação é recomendada?*

---

### 57. hwa-10.2.8-messages-awsui0155e-0058

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0155E indica um problema no Dynamic Workload Console: The workstation editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0155E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0155E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0155E no HWA e qual ação é recomendada?*

---

### 58. hwa-10.2.8-messages-awsui0157e-0059

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0157E indica um problema no Dynamic Workload Console: The workstation could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0157E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0157E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0157E no HWA e qual ação é recomendada?*

---

### 59. hwa-10.2.8-messages-awsui0158e-0060

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0158E indica um problema no Dynamic Workload Console: The selected workstations could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0158E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0158E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0158E no HWA e qual ação é recomendada?*

---

### 60. hwa-10.2.8-messages-awsui0160e-0061

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0160E indica um problema no Dynamic Workload Console: Another run cycle could not be created due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0160E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0160E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0160E no HWA e qual ação é recomendada?*

---

### 61. hwa-10.2.8-messages-awsui0162e-0062

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0162E indica um problema no Dynamic Workload Console: The operation could not be interrupted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0162E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0162E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0162E no HWA e qual ação é recomendada?*

---

### 62. hwa-10.2.8-messages-awsui0163e-0063

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0163E indica um problema no Dynamic Workload Console: The resource could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0163E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0163E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0163E no HWA e qual ação é recomendada?*

---

### 63. hwa-10.2.8-messages-awsui0165e-0064

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0165E indica um problema no Dynamic Workload Console: The resource header could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0165E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0165E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0165E no HWA e qual ação é recomendada?*

---

### 64. hwa-10.2.8-messages-awsui0167e-0065

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0167E indica um problema no Dynamic Workload Console: The resource dependency could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0167E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0167E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0167E no HWA e qual ação é recomendada?*

---

### 65. hwa-10.2.8-messages-awsui0168e-0066

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0168E indica um problema no Dynamic Workload Console: The scheduling specifications could not be added due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0168E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0168E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0168E no HWA e qual ação é recomendada?*

---

### 66. hwa-10.2.8-messages-awsui0177e-0067

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0177E indica um problema no Dynamic Workload Console: An attempt was made to add a dependency from a different job scheduling engine. A job stream cannot have external dependencies from other job scheduling engines. O sistema The requested action was not completed successfully. A acao documentada e: Add the dependency into a job stream on the same engine. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0177E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0177E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0177E no HWA e qual ação é recomendada?*

---

### 67. hwa-10.2.8-messages-awsui0180e-0068

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0180E indica um problema no Dynamic Workload Console: The selected engine is not available due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0180E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0180E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0180E no HWA e qual ação é recomendada?*

---

### 68. hwa-10.2.8-messages-awsui0183e-0069

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0183E indica um problema no Dynamic Workload Console: The job output could not be loaded because it uses an unsupported encoding. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0183E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0183E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0183E no HWA e qual ação é recomendada?*

---

### 69. hwa-10.2.8-messages-awsui0185e-0070

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0185E indica um problema no Dynamic Workload Console: The plan view could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0185E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0185E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0185E no HWA e qual ação é recomendada?*

---

### 70. hwa-10.2.8-messages-awsui0188e-0071

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0188E indica um problema no Dynamic Workload Console: The job could not be updated due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0188E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0188E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0188E no HWA e qual ação é recomendada?*

---

### 71. hwa-10.2.8-messages-awsui0193e-0072

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0193E indica um problema no Dynamic Workload Console: Two lists cannot be created with the same name in the same path. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new list name. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0193E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0193E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0193E no HWA e qual ação é recomendada?*

---

### 72. hwa-10.2.8-messages-awsui0196e-0073

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0196E indica um problema no Dynamic Workload Console: Two lists cannot be created with the same name in the same path. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new list name..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0196E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0196E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0196E no HWA e qual ação é recomendada?*

---

### 73. hwa-10.2.8-messages-awsui0197w-0074

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0197W indica um problema no Dynamic Workload Console: The number format is not correct. The value remains unchanged. O sistema The requested action was not completed successfully. A acao documentada e: Supply a new number in the correct format. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0197W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0197W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0197W no HWA e qual ação é recomendada?*

---

### 74. hwa-10.2.8-messages-awsui0199e-0075

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0199E indica um problema no Dynamic Workload Console: The workstation definition could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0199E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0199E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0199E no HWA e qual ação é recomendada?*

---

### 75. hwa-10.2.8-messages-awsui0201e-0076

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0201E indica um problema no Dynamic Workload Console: The job stream list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0201E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0201E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0201E no HWA e qual ação é recomendada?*

---

### 76. hwa-10.2.8-messages-awsui0206e-0077

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0206E indica um problema no Dynamic Workload Console: The resource could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0206E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0206E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0206E no HWA e qual ação é recomendada?*

---

### 77. hwa-10.2.8-messages-awsui0208e-0078

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0208E indica um problema no Dynamic Workload Console: The resource instance could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0208E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0208E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0208E no HWA e qual ação é recomendada?*

---

### 78. hwa-10.2.8-messages-awsui0243e-0079

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0243E indica um problema no Dynamic Workload Console: The Job Stream Editor could not be opened due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0243E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0243E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0243E no HWA e qual ação é recomendada?*

---

### 79. hwa-10.2.8-messages-awsui0246e-0080

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0246E indica um problema no Dynamic Workload Console: The resources necessary to show the localized version were not found. O sistema Processing continues but the dialogs are shown without messages. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0246E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0246E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0246E no HWA e qual ação é recomendada?*

---

### 80. hwa-10.2.8-messages-awsui0254e-0081

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0254E indica um problema no Dynamic Workload Console: The resource name is a mandatory field. O sistema The requested action was not completed successfully. A acao documentada e: Supply a name for the resource. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0254E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0254E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0254E no HWA e qual ação é recomendada?*

---

### 81. hwa-10.2.8-messages-awsui0264e-0082

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0264E indica um problema no Dynamic Workload Console: The Workstation name is a mandatory field. O sistema The requested action was not completed successfully. A acao documentada e: Supply a Workstation name. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0264E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0264E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0264E no HWA e qual ação é recomendada?*

---

### 82. hwa-10.2.8-messages-awsui0266e-0083

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0266E indica um problema no Dynamic Workload Console: The blank character is not a valid character. O sistema The requested action was not completed successfully. A acao documentada e: Supply the string again without using the blank character. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0266E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0266E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0266E no HWA e qual ação é recomendada?*

---

### 83. hwa-10.2.8-messages-awsui0283e-0084

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0283E indica um problema no Dynamic Workload Console: The object could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0283E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0283E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0283E no HWA e qual ação é recomendada?*

---

### 84. hwa-10.2.8-messages-awsui0286e-0085

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0286E indica um problema no Dynamic Workload Console: Two run cycles with the same name cannot exist for the same job stream. O sistema The requested action was not completed successfully. A acao documentada e: Supply a different name for the new run cycle. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0286E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0286E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0286E no HWA e qual ação é recomendada?*

---

### 85. hwa-10.2.8-messages-awsui0291e-0086

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0291E indica um problema no Dynamic Workload Console: The job stream could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0291E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0291E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0291E no HWA e qual ação é recomendada?*

---

### 86. hwa-10.2.8-messages-awsui0292e-0087

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0292E indica um problema no Dynamic Workload Console: System action: O sistema Operator response: A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0292E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0292E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0292E no HWA e qual ação é recomendada?*

---

### 87. hwa-10.2.8-messages-awsui0295e-0088

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0295E indica um problema no Dynamic Workload Console: You have defined a dependency so that job A depends on job B, but jobs A and B are the same. O sistema The requested action was not completed successfully. A acao documentada e: Change the dependency to a job other than itself. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0295E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0295E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0295E no HWA e qual ação é recomendada?*

---

### 88. hwa-10.2.8-messages-awsui0303e-0089

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0303E indica um problema no Dynamic Workload Console: A dependency between job streams must be unique. O sistema The requested action was not completed successfully. A acao documentada e: Modify one or both dependencies to make them unique. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0303E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0303E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0303E no HWA e qual ação é recomendada?*

---

### 89. hwa-10.2.8-messages-awsui0304e-0090

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0304E indica um problema no Dynamic Workload Console: Run cycle names in job streams must be unique. O sistema The requested action was not completed successfully. A acao documentada e: Modify one or both run cycles to make their names unique. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0304E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0304E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0304E no HWA e qual ação é recomendada?*

---

### 90. hwa-10.2.8-messages-awsui0305e-0091

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0305E indica um problema no Dynamic Workload Console: The remote server is not reachable. O sistema The requested action was not completed successfully. A acao documentada e: Check the validity of the user name and password. Check if the connection with the remote server is available. Check if the remote server is started. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0305E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0305E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0305E no HWA e qual ação é recomendada?*

---

### 91. hwa-10.2.8-messages-awsui0311e-0092

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0311E indica um problema no Dynamic Workload Console: The job output could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested action was not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0311E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0311E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0311E no HWA e qual ação é recomendada?*

---

### 92. hwa-10.2.8-messages-awsui0313e-0093

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0313E indica um problema no Dynamic Workload Console: To rerun a job you have to specify either both the job definition and workstation, or neither of them (in this case, the original job definition and workstation will be used). O sistema The requested action was not completed successfully. A acao documentada e: Specify the workstation or clear the job definition field. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0313E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0313E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0313E no HWA e qual ação é recomendada?*

---

### 93. hwa-10.2.8-messages-awsui0314e-0094

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0314E indica um problema no Dynamic Workload Console: To rerun a job you have to specify either both the job definition and workstation, or neither of them (in this case, the original job definition and workstation will be used). O sistema The requested action was not completed successfully. A acao documentada e: Specify the job definition or clear the workstation field. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0314E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0314E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0314E no HWA e qual ação é recomendada?*

---

### 94. hwa-10.2.8-messages-awsui0327e-0095

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0327E indica um problema no Dynamic Workload Console: A string containing less than the indicated minimum characters has been entered. O sistema The requested action was not completed successfully. A acao documentada e: Enter a valid value of more than the indicated minimum characters. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0327E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0327E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0327E no HWA e qual ação é recomendada?*

---

### 95. hwa-10.2.8-messages-awsui0333e-0096

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0333E indica um problema no Dynamic Workload Console: For the requested operation at least one Status value must be supplied. O sistema The requested action was not completed successfully. A acao documentada e: Supply at least one Status value. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0333E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0333E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0333E no HWA e qual ação é recomendada?*

---

### 96. hwa-10.2.8-messages-awsui0336e-0097

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0336E indica um problema no Dynamic Workload Console: The connection to the database could not be established because the database is not active or the connection parameters set in the engine connection are not correct. O sistema The requested action was not completed successfully. A acao documentada e: Verify that the database is up and running and the connection parameters set in the engine connection are correct. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0336E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0336E no HWA?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual é o significado da mensagem de erro AWSUI0336E no HWA e qual ação é recomendada?*

---

### 97. hwa-10.2.8-messages-awsui0337e-0098

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0337E indica um problema no Dynamic Workload Console: The query does not return any results because the From time is later than the To time. O sistema The requested action was not completed successfully. A acao documentada e: Supply an earlier From time, or a later To time. Retry the query..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0337E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0337E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0337E no HWA e qual ação é recomendada?*

---

### 98. hwa-10.2.8-messages-awsui0340e-0099

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0340E indica um problema no Dynamic Workload Console: The query does not return any results because the Specific Dates list is empty. O sistema The requested action was not completed successfully. A acao documentada e: Add at least one date to the Specific Dates list. Retry the query..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0340E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0340E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0340E no HWA e qual ação é recomendada?*

---

### 99. hwa-10.2.8-messages-awsui0346e-0100

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0346E indica um problema no Dynamic Workload Console: The database might not be available or the parameters specified for the database configuration are not correct. O sistema The requested action was not completed successfully. A acao documentada e: Check the database credentials, if the problem persists, contact the IBM Workload Scheduler administrator..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0346E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0346E no HWA?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual é o significado da mensagem de erro AWSUI0346E no HWA e qual ação é recomendada?*

---

### 100. hwa-10.2.8-messages-awsui0359w-0101

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0359W indica um problema no Dynamic Workload Console: The list of available actions and event types in the event rule task that you are editing depends on the engine specified. The engine has been modified and the new engine supports a different set of actions and event types. O sistema The engine has been changed as requested and the list of selected actions and event types has been reset. A acao documentada e: Edit your event rule definition specifying a new list of actions and event types. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0359W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0359W no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual é o significado da mensagem de erro AWSUI0359W no HWA e qual ação é recomendada?*

---

### 101. hwa-10.2.8-messages-awsui0407e-0102

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0407E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you have sufficient permission and that the object was not deleted..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0407E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0407E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0407E no HWA e qual ação é recomendada?*

---

### 102. hwa-10.2.8-messages-awsui0530e-0103

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0530E indica um problema no Dynamic Workload Console: It is not possible to establish a connection with the R/3 system. O sistema The requested operation is not completed successfully. A acao documentada e: Wait for the R/3 system to become available and try again..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0530E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0530E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0530E no HWA e qual ação é recomendada?*

---

### 103. hwa-10.2.8-messages-awsui0532e-0104

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0532E indica um problema no Dynamic Workload Console: The job definition could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0532E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0532E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0532E no HWA e qual ação é recomendada?*

---

### 104. hwa-10.2.8-messages-awsui0533e-0105

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0533E indica um problema no Dynamic Workload Console: The job definition list could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0533E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0533E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0533E no HWA e qual ação é recomendada?*

---

### 105. hwa-10.2.8-messages-awsui0536e-0106

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0536E indica um problema no Dynamic Workload Console: The job definitions could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0536E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0536E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0536E no HWA e qual ação é recomendada?*

---

### 106. hwa-10.2.8-messages-awsui0538w-0107

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0538W indica um problema no Dynamic Workload Console: The workstation class could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0538W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0538W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0538W no HWA e qual ação é recomendada?*

---

### 107. hwa-10.2.8-messages-awsui0540e-0108

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0540E indica um problema no Dynamic Workload Console: The workstation class could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0540E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0540E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0540E no HWA e qual ação é recomendada?*

---

### 108. hwa-10.2.8-messages-awsui0541e-0109

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0541E indica um problema no Dynamic Workload Console: The workstation class could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0541E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0541E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0541E no HWA e qual ação é recomendada?*

---

### 109. hwa-10.2.8-messages-awsui0543e-0110

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0543E indica um problema no Dynamic Workload Console: The user could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0543E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0543E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0543E no HWA e qual ação é recomendada?*

---

### 110. hwa-10.2.8-messages-awsui0544e-0111

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0544E indica um problema no Dynamic Workload Console: The selected user list could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0544E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0544E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0544E no HWA e qual ação é recomendada?*

---

### 111. hwa-10.2.8-messages-awsui0546e-0112

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0546E indica um problema no Dynamic Workload Console: The user could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0546E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0546E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0546E no HWA e qual ação é recomendada?*

---

### 112. hwa-10.2.8-messages-awsui0548e-0113

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0548E indica um problema no Dynamic Workload Console: The parameters could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0548E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0548E no HWA?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual é o significado da mensagem de erro AWSUI0548E no HWA e qual ação é recomendada?*

---

### 113. hwa-10.2.8-messages-awsui0549w-0114

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0549W indica um problema no Dynamic Workload Console: The parameter could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0549W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0549W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0549W no HWA e qual ação é recomendada?*

---

### 114. hwa-10.2.8-messages-awsui0551e-0115

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0551E indica um problema no Dynamic Workload Console: The parameter could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0551E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0551E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0551E no HWA e qual ação é recomendada?*

---

### 115. hwa-10.2.8-messages-awsui0553e-0116

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0553E indica um problema no Dynamic Workload Console: The prompts could not be loaded due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0553E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0553E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0553E no HWA e qual ação é recomendada?*

---

### 116. hwa-10.2.8-messages-awsui0554w-0117

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0554W indica um problema no Dynamic Workload Console: The prompt could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0554W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0554W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0554W no HWA e qual ação é recomendada?*

---

### 117. hwa-10.2.8-messages-awsui0556e-0118

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0556E indica um problema no Dynamic Workload Console: The prompt could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0556E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0556E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0556E no HWA e qual ação é recomendada?*

---

### 118. hwa-10.2.8-messages-awsui0557e-0119

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0557E indica um problema no Dynamic Workload Console: The prompt could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0557E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0557E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0557E no HWA e qual ação é recomendada?*

---

### 119. hwa-10.2.8-messages-awsui0559w-0120

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0559W indica um problema no Dynamic Workload Console: The calendar could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0559W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0559W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0559W no HWA e qual ação é recomendada?*

---

### 120. hwa-10.2.8-messages-awsui0561e-0121

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0561E indica um problema no Dynamic Workload Console: The calendar could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0561E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0561E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0561E no HWA e qual ação é recomendada?*

---

### 121. hwa-10.2.8-messages-awsui0562e-0122

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0562E indica um problema no Dynamic Workload Console: The calendar could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0562E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0562E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0562E no HWA e qual ação é recomendada?*

---

### 122. hwa-10.2.8-messages-awsui0564w-0123

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0564W indica um problema no Dynamic Workload Console: The domain could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0564W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0564W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0564W no HWA e qual ação é recomendada?*

---

### 123. hwa-10.2.8-messages-awsui0565e-0124

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0565E indica um problema no Dynamic Workload Console: The multiple domains could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0565E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0565E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0565E no HWA e qual ação é recomendada?*

---

### 124. hwa-10.2.8-messages-awsui0567e-0125

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0567E indica um problema no Dynamic Workload Console: The domain could not be deleted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0567E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0567E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0567E no HWA e qual ação é recomendada?*

---

### 125. hwa-10.2.8-messages-awsui0569e-0126

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0569E indica um problema no Dynamic Workload Console: The selected multiple prompts could not be replied to due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0569E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0569E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0569E no HWA e qual ação é recomendada?*

---

### 126. hwa-10.2.8-messages-awsui0570e-0127

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0570E indica um problema no Dynamic Workload Console: The link action for selected domain could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0570E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0570E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0570E no HWA e qual ação é recomendada?*

---

### 127. hwa-10.2.8-messages-awsui0572e-0128

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0572E indica um problema no Dynamic Workload Console: The unlink action for the selected domain could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0572E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0572E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0572E no HWA e qual ação é recomendada?*

---

### 128. hwa-10.2.8-messages-awsui0574e-0129

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0574E indica um problema no Dynamic Workload Console: Some of the start actions were not completed for the domain due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0574E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0574E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0574E no HWA e qual ação é recomendada?*

---

### 129. hwa-10.2.8-messages-awsui0575e-0130

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0575E indica um problema no Dynamic Workload Console: The start action for the selected domains cannot be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0575E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0575E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0575E no HWA e qual ação é recomendada?*

---

### 130. hwa-10.2.8-messages-awsui0577e-0131

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0577E indica um problema no Dynamic Workload Console: The stop action for the selected domains could not be performed due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0577E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0577E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0577E no HWA e qual ação é recomendada?*

---

### 131. hwa-10.2.8-messages-awsui0589e-0132

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0589E indica um problema no Dynamic Workload Console: A workstation class might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new name. O sistema If OK is clicked the workstation class is renamed. Otherwise the rename action is ignored. A acao documentada e: Click OK to rename the workstation class or click Cancel to cancel the rename action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0589E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0589E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0589E no HWA e qual ação é recomendada?*

---

### 132. hwa-10.2.8-messages-awsui0592e-0133

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0592E indica um problema no Dynamic Workload Console: The prompt might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new name. O sistema If OK is clicked the prompt is renamed. Otherwise the rename action is ignored. A acao documentada e: Click OK to rename the prompt or click Cancel to cancel the rename action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0592E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0592E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0592E no HWA e qual ação é recomendada?*

---

### 133. hwa-10.2.8-messages-awsui0598w-0134

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0598W indica um problema no Dynamic Workload Console: An error has occurred. See the error.log file for details. O sistema Processing continues. A acao documentada e: See the error.log file for details. If you can resolve the problem, do so. Retry the operation. If you cannot resolve the problem, or the problem persists, contact Software Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0598W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0598W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0598W no HWA e qual ação é recomendada?*

---

### 134. hwa-10.2.8-messages-awsui0605e-0135

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0605E indica um problema no Dynamic Workload Console: This job might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new workstation data. O sistema If OK is clicked the workstation is modified. Otherwise the request is ignored. A acao documentada e: Click OK to modify the workstation, or click Cancel to cancel the modify request and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0605E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0605E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0605E no HWA e qual ação é recomendada?*

---

### 135. hwa-10.2.8-messages-awsui0606w-0136

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0606W indica um problema no Dynamic Workload Console: This resource might be a dependency for a job scheduling object. If so, the dependency is also updated with the new workstation data. O sistema If OK is clicked the workstation is modified. Otherwise the request is ignored. A acao documentada e: Click OK to modify the workstation, or click Cancel to cancel the modify request and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0606W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0606W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0606W no HWA e qual ação é recomendada?*

---

### 136. hwa-10.2.8-messages-awsui0608e-0137

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0608E indica um problema no Dynamic Workload Console: This job might be part of a dependency for a job scheduling object in the database. If so, the dependency is also updated with the new job name. O sistema If OK is clicked the job is renamed. Otherwise the rename request is ignored. A acao documentada e: Click OK to rename the job, or click Cancel to cancel the rename request and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0608E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0608E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0608E no HWA e qual ação é recomendada?*

---

### 137. hwa-10.2.8-messages-awsui0620e-0138

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0620E indica um problema no Dynamic Workload Console: The dependency field can be enclosed in quote characters, but there can only be two - at the beginning and the end. At least one more has been found. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that if the dependency field begins with a quote character it also ends with one, with no other quote characters in the field, and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0620E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0620E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0620E no HWA e qual ação é recomendada?*

---

### 138. hwa-10.2.8-messages-awsui0624e-0139

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0624E indica um problema no Dynamic Workload Console: The successor for the job stream could not be retrieved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0624E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0624E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0624E no HWA e qual ação é recomendada?*

---

### 139. hwa-10.2.8-messages-awsui0626e-0140

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0626E indica um problema no Dynamic Workload Console: The job or job stream could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0626E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0626E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0626E no HWA e qual ação é recomendada?*

---

### 140. hwa-10.2.8-messages-awsui0631e-0141

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0631E indica um problema no Dynamic Workload Console: The SAP job definition could not be saved due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0631E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0631E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0631E no HWA e qual ação é recomendada?*

---

### 141. hwa-10.2.8-messages-awsui0633e-0142

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0633E indica um problema no Dynamic Workload Console: The SAP job definition could not be renamed. O sistema The requested action is not completed successfully. A acao documentada e: Click Save and Close to rename the job. Otherwise, enter the original job name and click Modify and Close to modify the job and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0633E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0633E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0633E no HWA e qual ação é recomendada?*

---

### 142. hwa-10.2.8-messages-awsui0720e-0143

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0720E indica um problema no Dynamic Workload Console: A dependency was specified on a resource that does not exist, or the rights of the specifying user are not sufficient to use the resource. The resource might have been removed from the database after the dependency was added. O sistema The requested operation is not completed successfully. A acao documentada e: Remove the resource dependency. Create the resource and recreate the dependency and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0720E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0720E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0720E no HWA e qual ação é recomendada?*

---

### 143. hwa-10.2.8-messages-awsui0722e-0144

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0722E indica um problema no Dynamic Workload Console: A negative or null number of units for the resource was specified. O sistema The requested operation is not completed successfully. A acao documentada e: Modify the number of units for the specified resource to a positive value less than or equal to the number of units available and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0722E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0722E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0722E no HWA e qual ação é recomendada?*

---

### 144. hwa-10.2.8-messages-awsui0726e-0145

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0726E indica um problema no Dynamic Workload Console: The query does not return any results because the date filter is not set correctly. O sistema The requested operation is not completed successfully. A acao documentada e: Set values for both Date and Time fields, or do not set values for either Date or Time fields and retry the query..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0726E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0726E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0726E no HWA e qual ação é recomendada?*

---

### 145. hwa-10.2.8-messages-awsui0727e-0146

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0727E indica um problema no Dynamic Workload Console: The query does not return any results because the date filter is not set correctly. O sistema The requested operation is not completed successfully. A acao documentada e: Set values both for Time and Date fields, or do not set values for either Date or Time fields and retry the query..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0727E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0727E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0727E no HWA e qual ação é recomendada?*

---

### 146. hwa-10.2.8-messages-awsui0729e-0147

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0729E indica um problema no Dynamic Workload Console: It is not possible to unlock the object. Some problem has been encountered during this operation. O sistema The requested operation is not completed successfully. A acao documentada e: Refer to the reason indicated in the message to resolve the issue and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0729E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0729E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0729E no HWA e qual ação é recomendada?*

---

### 147. hwa-10.2.8-messages-awsui0735e-0148

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0735E indica um problema no Dynamic Workload Console: If a job stream is defined in a workstation class, then all of its jobs must be defined either on a workstation, or in the same workstation class. O sistema The requested operation is not completed successfully. A acao documentada e: Set the workstation of this job stream to the original value and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0735E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0735E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0735E no HWA e qual ação é recomendada?*

---

### 148. hwa-10.2.8-messages-awsui0744e-0149

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0744E indica um problema no Dynamic Workload Console: The job could not be submitted due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0744E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0744E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0744E no HWA e qual ação é recomendada?*

---

### 149. hwa-10.2.8-messages-awsui0747e-0150

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0747E indica um problema no Dynamic Workload Console: There is a problem with Table criteria due to an error in the IBM Workload Scheduler for Applications. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text represents an error code reported by IBM Workload Scheduler for Applications. Resolve the error and retry the operation. IBM Workload Scheduler for Applications User's Guide for information about the error message..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0747E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0747E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0747E no HWA e qual ação é recomendada?*

---

### 150. hwa-10.2.8-messages-awsui0753w-0151

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0753W indica um problema no Dynamic Workload Console: The selected job definition is used by one or more job streams. Verify that these job streams are defined on the same workstation class O sistema If OK is clicked, the job definition is saved. If cancel is clicked the save action is ignored. A acao documentada e: Click OK to submit or click Cancel to cancel the submit action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0753W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0753W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0753W no HWA e qual ação é recomendada?*

---

### 151. hwa-10.2.8-messages-awsui0782e-0152

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0782E indica um problema no Dynamic Workload Console: The selected engine has been shared by another user. O sistema The engine was not modified. A acao documentada e: Create another engine and share it..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0782E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0782E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0782E no HWA e qual ação é recomendada?*

---

### 152. hwa-10.2.8-messages-awsui0786e-0153

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0786E indica um problema no Dynamic Workload Console: You tried to perform an action on multiple items, but some or all of the selected items do not support the specified action. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that all the selected items are compatible with the specified action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0786E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0786E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0786E no HWA e qual ação é recomendada?*

---

### 153. hwa-10.2.8-messages-awsui0788e-0154

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0788E indica um problema no Dynamic Workload Console: You tried to perform an action on multiple items, but some of them do not support that action. O sistema The requested operation is not completed successfully. A acao documentada e: Deselect the items not compatible with the action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0788E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0788E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0788E no HWA e qual ação é recomendada?*

---

### 154. hwa-10.2.8-messages-awsui0801e-0155

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0801E indica um problema no Dynamic Workload Console: You attempted to test the database connection or to run a report task to an engine that does not support the reporting. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports reporting..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0801E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0801E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0801E no HWA e qual ação é recomendada?*

---

### 155. hwa-10.2.8-messages-awsui0803w-0156

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0803W indica um problema no Dynamic Workload Console: You have tested the connection to the indicated engine. The engine connection is working correctly but the database could not be accessed. O sistema The requested operation is not completed successfully. A acao documentada e: Ask the IBM Workload Scheduler administrator to resolve the problem with the access to the database for the indicated engine. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0803W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0803W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0803W no HWA e qual ação é recomendada?*

---

### 156. hwa-10.2.8-messages-awsui0810e-0157

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0810E indica um problema no Dynamic Workload Console: The selected item has been shared by another user. O sistema The requested operation is not completed successfully. A acao documentada e: Choose an object you own to delete..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0810E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0810E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0810E no HWA e qual ação é recomendada?*

---

### 157. hwa-10.2.8-messages-awsui0818e-0158

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0818E indica um problema no Dynamic Workload Console: You have tried to change a workstation to become the master domain manager. As there can only be one master domain manager at any given time, the program must first change the definition of the existing master domain manager to remove the manager attribute. However it could not find the existing master domain manager definition. Perhaps someone else has performed the same action at the same time. O sistema The requested operation is not completed successfully. A acao documentada e: Check the workstation definitions for the master domain and determine which workstation is the manager. Determine why the problem occurred and whether you still need to change the workstation to become the master domain manager. If so, retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0818E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0818E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0818E no HWA e qual ação é recomendada?*

---

### 158. hwa-10.2.8-messages-awsui0843e-0159

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0843E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler without specifying any action in the URL. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying an action..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0843E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0843E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0843E no HWA e qual ação é recomendada?*

---

### 159. hwa-10.2.8-messages-awsui0844e-0160

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0844E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with invalid parameters. O sistema The IBM Workload Scheduler has not been not launched. A acao documentada e: Check the documentation to ensure that you have correctly typed the parameters..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0844E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0844E no HWA?*
- *O que causa erro na resolução de local parameters em jobs e como solucionar?*
- *Qual é o significado da mensagem de erro AWSUI0844E no HWA e qual ação é recomendada?*

---

### 160. hwa-10.2.8-messages-awsui0846e-0161

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0846E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with an invalid status value. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying a valid status..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0846E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0846E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0846E no HWA e qual ação é recomendada?*

---

### 161. hwa-10.2.8-messages-awsui0847e-0162

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0847E indica um problema no Dynamic Workload Console: You have tried to launch a IBM Workload Scheduler with an invalid column parameter. O sistema The IBM Workload Scheduler has not been launched. A acao documentada e: Launch the IBM Workload Scheduler specifying a valid value for the column parameter, valid values are “”min“” or “”all“”..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0847E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0847E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0847E no HWA e qual ação é recomendada?*

---

### 162. hwa-10.2.8-messages-awsui0875e-0163

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0875E indica um problema no Dynamic Workload Console: You have tried to launch an operation not applicable on the selected tasks. O sistema The operation has not been launched. A acao documentada e: Launch the operation on a valid task..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0875E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0875E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0875E no HWA e qual ação é recomendada?*

---

### 163. hwa-10.2.8-messages-awsui0877e-0164

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0877E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the Workload Service Assurance feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports Workload Service Assurance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0877E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0877E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0877E no HWA e qual ação é recomendada?*

---

### 164. hwa-10.2.8-messages-awsui0888w-0165

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0888W indica um problema no Dynamic Workload Console: Variable Tables are supported from version 8.5. If you selected an engine of an older version, the specified variable table value is ignored. O sistema Processing continues, ignoring the “”variable table“” field. A acao documentada e: No action is required. To avoid this warning message in the future, do not specify a value in the “”variable table“” field for engine versions prior to version 8.5..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0888W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0888W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0888W no HWA e qual ação é recomendada?*

---

### 165. hwa-10.2.8-messages-awsui0893e-0166

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0893E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Contact Software Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0893E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0893E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0893E no HWA e qual ação é recomendada?*

---

### 166. hwa-10.2.8-messages-awsui0894e-0167

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0894E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Contact Software Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0894E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0894E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0894E no HWA e qual ação é recomendada?*

---

### 167. hwa-10.2.8-messages-awsui0903w-0168

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0903W indica um problema no Dynamic Workload Console: See text. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure that status of the selected workstation is compatible with the specified action and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0903W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0903W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0903W no HWA e qual ação é recomendada?*

---

### 168. hwa-10.2.8-messages-awsui0904w-0169

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0904W indica um problema no Dynamic Workload Console: The workstation type “”Workload Broker“” is supported startingfrom version 8.5. If you selected an engine with a previous version, the operation is interrupted. O sistema Processing is interrupted. A acao documentada e: Specify a different workstation type if the selected engine version is prior to version 8.5..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0904W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0904W no HWA?*
- *Como configurar ou solucionar problemas no dynamic agent ou broker para awsui?*
- *Qual é o significado da mensagem de erro AWSUI0904W no HWA e qual ação é recomendada?*

---

### 169. hwa-10.2.8-messages-awsui0906w-0170

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0906W indica um problema no Dynamic Workload Console: For security and auditability reasons, when an engine connection is shared to other users, the associated engine credentials are not shared. This message is presented when the default settings are overridden, for you to confirm the choice. O sistema If operator answers “”Yes“” the engine credentials will be shared along with the other engine properties. A acao documentada e: Answer “”Yes“” to allow sharing of engine credentials, or “”No“” to go back. This choice can be changed at any time by editing the engine properties..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0906W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0906W no HWA?*

---

### 170. hwa-10.2.8-messages-awsui0907e-0171

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0907E indica um problema no Dynamic Workload Console: You attempted to run an operation using an old version of the connector for z/OS that does not support the Conditional logic feature. O sistema The requested operation is not completed successfully. A acao documentada e: You should upgrade your connector for z/OS to have all the new features available..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0907E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0907E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0907E no HWA e qual ação é recomendada?*

---

### 171. hwa-10.2.8-messages-awsui0913w-0172

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0913W indica um problema no Dynamic Workload Console: User name and password are required to perform this operation. O sistema The requested operation is not completed successfully. A acao documentada e: Specify valid user and password values..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0913W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0913W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0913W no HWA e qual ação é recomendada?*

---

### 172. hwa-10.2.8-messages-awsui0914e-0173

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0914E indica um problema no Dynamic Workload Console: You attempted run a plan view on an engine that does not support it. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports plan view..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0914E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0914E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0914E no HWA e qual ação é recomendada?*

---

### 173. hwa-10.2.8-messages-awsui0916e-0174

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0916E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the Virtual workstation creation feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports Virtual workstation creation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0916E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0916E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0916E no HWA e qual ação é recomendada?*

---

### 174. hwa-10.2.8-messages-awsui0917e-0175

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0917E indica um problema no Dynamic Workload Console: You attempted to run an operation using an old version of the connector for z/OS that does not support the Virtual workstation creation feature. O sistema The requested operation is not completed successfully. A acao documentada e: You should upgrade your connector for z/OS to have all the new features available..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0917E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0917E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0917E no HWA e qual ação é recomendada?*

---

### 175. hwa-10.2.8-messages-awsui0918e-0176

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0918E indica um problema no Dynamic Workload Console: The task you tried to run does not exit or has been deleted. O sistema The requested operation is not completed successfully. A acao documentada e: Replace this bookmark with a valid one that links an existing task..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0918E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0918E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0918E no HWA e qual ação é recomendada?*

---

### 176. hwa-10.2.8-messages-awsui0920e-0177

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0920E indica um problema no Dynamic Workload Console: The specified object documentation url is invalid. O sistema The requested operation is not completed successfully. A acao documentada e: Change the documentation url and specify a valid url in the TdwcGlobalSettings.xml file..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0920E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0920E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0920E no HWA e qual ação é recomendada?*

---

### 177. hwa-10.2.8-messages-awsui0921e-0178

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0921E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you have sufficient permission and that the object was not deleted..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0921E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0921E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0921E no HWA e qual ação é recomendada?*

---

### 178. hwa-10.2.8-messages-awsui0922e-0179

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0922E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: Make sure you selected only one “”Monitor task on Multiple Engines“” task before runniong View as Report action..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0922E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0922E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0922E no HWA e qual ação é recomendada?*

---

### 179. hwa-10.2.8-messages-awsui0923e-0180

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0923E indica um problema no Dynamic Workload Console: System action: The requested operation is not completed successfully. O sistema The requested operation is not completed successfully. A acao documentada e: The file you are trying to upload it is not valid. Check file type and file size..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0923E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0923E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0923E no HWA e qual ação é recomendada?*

---

### 180. hwa-10.2.8-messages-awsui0943e-0181

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0943E indica um problema no Dynamic Workload Console: You attempted to test the engine connection with or to run an operation on an engine that does not support the User Fields feature. O sistema The requested operation is not completed successfully. A acao documentada e: Change to an engine that supports User Fields..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0943E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0943E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0943E no HWA e qual ação é recomendada?*

---

### 181. hwa-10.2.8-messages-awsui0958e-0182

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0958E indica um problema no Dynamic Workload Console: The selected prompt could not be replied to due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0958E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0958E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0958E no HWA e qual ação é recomendada?*

---

### 182. hwa-10.2.8-messages-awsui0959w-0183

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0959W indica um problema no Dynamic Workload Console: One or more filters are not supported with the current IBM Workload Scheduler engine version. The unsupported filters has been ignored. O sistema The query has been completed, but a specified filter has been ignored. A acao documentada e: Remove the indicated filter from the task..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0959W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0959W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0959W no HWA e qual ação é recomendada?*

---

### 183. hwa-10.2.8-messages-awsui0975e-0184

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI0975E indica um problema no Dynamic Workload Console: System action: O sistema Operator response: A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI0975E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI0975E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI0975E no HWA e qual ação é recomendada?*

---

### 184. hwa-10.2.8-messages-awsui2000e-0185

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2000E indica um problema no Dynamic Workload Console: There is a connection problem with the database. Possible errors are: • The database is down • The database password provided when the engine was created is wrong or has been changed. O sistema The requested operation is not completed successfully. A acao documentada e: Check the error log and trace files for the possible cause of the problem. Check that the database is up and that the connection credentials are correct. Correct the problem and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI2000E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI2000E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI2000E no HWA e qual ação é recomendada?*

---

### 185. hwa-10.2.8-messages-awsui2007e-0186

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI2007E indica um problema no Dynamic Workload Console: The report could not be produced due to an error that occurred in the IBM Workload Scheduler engine. The error code is specified in the message text. O sistema The requested operation is not completed successfully. A acao documentada e: The reason displayed in the message text is the ID of an error reported by the IBM Workload Scheduler engine. Resolve the error and retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI2007E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI2007E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI2007E no HWA e qual ação é recomendada?*

---

### 186. hwa-10.2.8-messages-awsui3055e-0187

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3055E indica um problema no Dynamic Workload Console: The objectType cannot be created or update or delete or read in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3055E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3055E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3055E no HWA e qual ação é recomendada?*

---

### 187. hwa-10.2.8-messages-awsui3057e-0188

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3057E indica um problema no Dynamic Workload Console: An Access Method and a Host must be specified for the Extended Agent. O sistema The workstation is not created. A acao documentada e: Specify an Access Method and an Host workstation name for the Extended Agent..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3057E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3057E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3057E no HWA e qual ação é recomendada?*

---

### 188. hwa-10.2.8-messages-awsui3058e-0189

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3058E indica um problema no Dynamic Workload Console: A Domain must be specified for the workstation. O sistema The workstation is not created. A acao documentada e: Specify a Domain for the workstation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3058E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3058E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3058E no HWA e qual ação é recomendada?*

---

### 189. hwa-10.2.8-messages-awsui3069e-0190

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3069E indica um problema no Dynamic Workload Console: The workstation has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3069E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3069E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3069E no HWA e qual ação é recomendada?*

---

### 190. hwa-10.2.8-messages-awsui3070e-0191

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3070E indica um problema no Dynamic Workload Console: The domain has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3070E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3070E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3070E no HWA e qual ação é recomendada?*

---

### 191. hwa-10.2.8-messages-awsui3071e-0192

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3071E indica um problema no Dynamic Workload Console: The workstation has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3071E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3071E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3071E no HWA e qual ação é recomendada?*

---

### 192. hwa-10.2.8-messages-awsui3074e-0193

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3074E indica um problema no Dynamic Workload Console: The workstation cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3074E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3074E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3074E no HWA e qual ação é recomendada?*

---

### 193. hwa-10.2.8-messages-awsui3075e-0194

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3075E indica um problema no Dynamic Workload Console: The domain cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3075E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3075E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3075E no HWA e qual ação é recomendada?*

---

### 194. hwa-10.2.8-messages-awsui3086e-0195

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3086E indica um problema no Dynamic Workload Console: The job stream has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3086E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3086E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3086E no HWA e qual ação é recomendada?*

---

### 195. hwa-10.2.8-messages-awsui3088e-0196

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3088E indica um problema no Dynamic Workload Console: The job stream cannot be created or update or delete or read or unlock in the DB. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3088E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3088E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3088E no HWA e qual ação é recomendada?*

---

### 196. hwa-10.2.8-messages-awsui3089e-0197

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3089E indica um problema no Dynamic Workload Console: The job definition has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3089E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3089E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3089E no HWA e qual ação é recomendada?*

---

### 197. hwa-10.2.8-messages-awsui3090e-0198

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3090E indica um problema no Dynamic Workload Console: The job definition has been deleted from the DataBase. O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3090E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3090E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3090E no HWA e qual ação é recomendada?*

---

### 198. hwa-10.2.8-messages-awsui3092e-0199

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3092E indica um problema no Dynamic Workload Console: The master domain cannot be retrieved. O sistema The requested action was not completed successfully. A acao documentada e: Verify that the engine connection is working and that the operator is authorized to retrieve this information. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3092E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3092E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3092E no HWA e qual ação é recomendada?*

---

### 199. hwa-10.2.8-messages-awsui3098e-0200

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3098E indica um problema no Dynamic Workload Console: You are saving a condition without defining any condition dependencies O sistema The requested action was not completed successfully. A acao documentada e: Add a condition dependency or press Cancel.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3098E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3098E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3098E no HWA e qual ação é recomendada?*

---

### 200. hwa-10.2.8-messages-awsui3100e-0201

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3100E indica um problema no Dynamic Workload Console: The first value in the range must be lower than the second value. O sistema The requested action was not completed successfully. A acao documentada e: Specify a correct range or press Cancel..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3100E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3100E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3100E no HWA e qual ação é recomendada?*

---

### 201. hwa-10.2.8-messages-awsui3101e-0202

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3101E indica um problema no Dynamic Workload Console: You cannot specify the “”Not equal to“” operator with an intermediate status, such as “”Started“”. O sistema The requested action was not completed successfully. A acao documentada e: Change either the operator or status values to form a valid combination..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3101E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3101E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3101E no HWA e qual ação é recomendada?*

---

### 202. hwa-10.2.8-messages-awsui3110e-0203

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3110E indica um problema no Dynamic Workload Console: Kill and Job Log actions are not permitted on a Shadow Job O sistema The requested action was not completed successfully. A acao documentada e: Contact Customer Support for assistance..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3110E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3110E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3110E no HWA e qual ação é recomendada?*

---

### 203. hwa-10.2.8-messages-awsui3117e-0204

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3117E indica um problema no Dynamic Workload Console: The engine connection version does not support this object type. O sistema The requested action was not completed successfully. A acao documentada e: Use a later version engine connection that supports the object type.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3117E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3117E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3117E no HWA e qual ação é recomendada?*

---

### 204. hwa-10.2.8-messages-awsui3126w-0205

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3126W indica um problema no Dynamic Workload Console: Multiple engine tasks can be run against Current plan only O sistema None A acao documentada e: Chapter 3. AWSWUI - Dynamic Workload Console messages.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3126W no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3126W no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3126W no HWA e qual ação é recomendada?*

---

### 205. hwa-10.2.8-messages-awsui3130e-0206

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI3130E indica um problema no Dynamic Workload Console: The update can be performed on a predefined number of workstations at a time. O sistema The operation is not performed. A acao documentada e: To update more workstations, browse to the TdwcGlobalSettings.xml file and specify the number of workstations in the updateWorkstationMaxNumber property..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI3130E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI3130E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI3130E no HWA e qual ação é recomendada?*

---

### 206. hwa-10.2.8-messages-awsui5002e-0207

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5002E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a valid value..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5002E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5002E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5002E no HWA e qual ação é recomendada?*

---

### 207. hwa-10.2.8-messages-awsui5003e-0208

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5003E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter all the required values..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5003E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5003E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5003E no HWA e qual ação é recomendada?*

---

### 208. hwa-10.2.8-messages-awsui5004e-0209

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5004E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a longer value..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5004E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5004E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5004E no HWA e qual ação é recomendada?*

---

### 209. hwa-10.2.8-messages-awsui5006e-0210

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5006E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Enter a value between 0 and 100..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5006E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5006E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5006E no HWA e qual ação é recomendada?*

---

### 210. hwa-10.2.8-messages-awsui5009e-0211

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5009E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema none A acao documentada e: Provide a new value, ensuring it is supported..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5009E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5009E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5009E no HWA e qual ação é recomendada?*

---

### 211. hwa-10.2.8-messages-awsui5014e-0212

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5014E indica um problema no Dynamic Workload Console: Unable to execute an Heart Beat to keep the session up. O sistema The session is not kept up A acao documentada e: Close current session and start a new one.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5014E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5014E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5014E no HWA e qual ação é recomendada?*

---

### 212. hwa-10.2.8-messages-awsui5015e-0213

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5015E indica um problema no Dynamic Workload Console: The Rule Editor cannot be opened. O sistema none A acao documentada e: Ensure that the connection to the server is working properly..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5015E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5015E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5015E no HWA e qual ação é recomendada?*

---

### 213. hwa-10.2.8-messages-awsui5016e-0214

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5016E indica um problema no Dynamic Workload Console: The Rule Editor cannot be closed. O sistema none A acao documentada e: Ensure that the connection to the server is working properly..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5016E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5016E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5016E no HWA e qual ação é recomendada?*

---

### 214. hwa-10.2.8-messages-awsui5018e-0215

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5018E indica um problema no Dynamic Workload Console: This message is displayed when a not specific internal error occurs. O sistema No change happens in the event rule. A acao documentada e: Close Rule Editor panel, reopen it and try to process the rule again..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5018E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5018E no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual é o significado da mensagem de erro AWSUI5018E no HWA e qual ação é recomendada?*

---

### 215. hwa-10.2.8-messages-awsui5023e-0216

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5023E indica um problema no Dynamic Workload Console: This message is displayed when an error occurs while ordering an event in sequence with others. O sistema The event has not been moved. A acao documentada e: Specify a different event sequence..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5023E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5023E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5023E no HWA e qual ação é recomendada?*

---

### 216. hwa-10.2.8-messages-awsui5029e-0217

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5029E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema The event rule cannot be saved. A acao documentada e: Provide date and time values..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5029E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5029E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5029E no HWA e qual ação é recomendada?*

---

### 217. hwa-10.2.8-messages-awsui5030e-0218

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5030E indica um problema no Dynamic Workload Console: The data input is not valid. O sistema The event rule cannot be saved. A acao documentada e: Provide a valid date value..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5030E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5030E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI5030E no HWA e qual ação é recomendada?*

---

### 218. hwa-10.2.8-messages-awsui5038e-0219

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI5038E indica um problema no Dynamic Workload Console: There is an error in some field of the Rule Editor. The event rule cannot be saved. O sistema The event rule cannot be saved and the button SAVE is disabled. A acao documentada e: Fix the errors and proceed..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI5038E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI5038E no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*
- *Qual é o significado da mensagem de erro AWSUI5038E no HWA e qual ação é recomendada?*

---

### 219. hwa-10.2.8-messages-awsui6030e-0220

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Instalação / Utilitários de Setup > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6030E indica um problema no Dynamic Workload Console: It was not possible to find the plugin with specified identifier. It may has been uninstalled from the engine. O sistema The requested operation is not completed. A acao documentada e: Check the plugin installation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI6030E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI6030E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI6030E no HWA e qual ação é recomendada?*

---

### 220. hwa-10.2.8-messages-awsui6114e-0221

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awsui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8 Distributed, a mensagem AWSUI6114E indica um problema no Dynamic Workload Console: The total number of characters in one or more of the specified fields exceeds the maximum supported limit. O sistema The requested operation is not performed. A acao documentada e: Reduce the number of characters in the specified fields. Retry the operation..

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSUI6114E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSUI6114E no HWA?*
- *Qual é o significado da mensagem de erro AWSUI6114E no HWA e qual ação é recomendada?*

---

### 221. hwa-10.2.8-messages-awswui-0005

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed; Linux x86_64) > Componente: Dynamic Workload Console (DWC) > Interface: Geral > Tópico: messages > awswui [messages_dwc]]`

**Regra Canônica / Evidência:**
No HCL Workload Automation 10.2.8, o conjunto de mensagens AWSWUI cobre erros e avisos do Dynamic Workload Console (DWC). Essas mensagens sao emitidas pela interface web do DWC e podem indicar problemas de conexao com o engine, erros de autenticacao, ou falhas na interface. O Message Help em https://help.hcl-software.com/workloadautomation/v1028/common/src_ms/awsmsmsghelp.html fornece Explanation, System action e Operator response para cada codigo AWSWUI.

**Plataforma / Validação:** Distributed; Linux x86_64

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSWUI0005 no HWA?*
- *Como solucionar ou diagnosticar o erro AWSWUI0005 no HWA?*
- *Qual a ação recomendada para a mensagem AWSUI0005 no DWC?*

---

### 222. hwa-10.2.8-trouble-awsmsp104e-0007

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (distributed; event rules) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
TROUBLESHOOTING: no HCL Workload Automation 10.2.8, a acao de envio automatico de e-mail de uma event rule falha com AWSMSP104E 'The mail <mailID> has not been successfully delivered to <recipient>', com a causa documentada: o dominio do servidor SMTP nao esta definido na opcao global de remetente de e-mail mailSenderName (ms); a recuperacao e definir o dominio do SMTP na opcao global mailSenderName (ms).

**Plataforma / Validação:** distributed; event rules

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSMSP104E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSMSP104E no HWA?*
- *Como a automação orientada a eventos (event rules) funciona no HWA 10.2.8?*

---

### 223. hwa-10.2.8-vm-9f-0008

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
A palavra-chave onoverlap (parallel|enqueue|donotstart) é suportada na definição de job stream do HCL Workload Automation Distributed 10.2.0 e 10.2.8, com os três valores idênticos. PORÉM, o limite de 39 dependências manuais com enqueue e a mensagem AWSJOM138E são documentados apenas na 10.2.8 (introduzidos na 10.2.7, fix KB0128221); a página 10.2.0 não menciona esse limite.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM138E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM138E no HWA?*

---

### 224. hwa-10.2.8-vm-9f-0008-contrast-0015

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.0; 10.2.7; 10.2.8 (Distributed) > Componente: Master Domain Manager (MDM) > Interface: Geral > Tópico: incidents > aws [aws]]`

**Regra Canônica / Evidência:**
PAR CONTRASTIVO de hwa-10.2.8-vm-9f-0008 (onoverlap + limite 39 deps): a keyword onoverlap (parallel|enqueue|donotstart) e suportada em 10.2.0 e 10.2.8, mas o limite de 39 dependencias manuais com enqueue e a mensagem AWSJOM138E sao documentados apenas a partir da 10.2.7 (fix KB0128221); na 10.2.0 a pagina nao menciona o limite; portanto, o limite nao deve ser generalizado para 10.2.0.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJOM138E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJOM138E no HWA?*

---

### 225. hwa-official-message-10.2.8-0002

**Escopo & Contexto:** `[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Relational Database (PostgreSQL / DB2 / Oracle) > Interface: Geral > Tópico: incidents > error [error]]`

**Regra Canônica / Evidência:**
Em HWA Distributed 10.2.8, AWSJPL006E indica que um objeto do banco não pôde ser carregado e a página aponta conexão quebrada com o banco. Context: This error means that a connection with the database is broken.

**Plataforma / Validação:** Distributed

**Perguntas e Cenários Relacionados:**

- *Qual é o significado da mensagem de erro AWSJPL006E no HWA?*
- *Como solucionar ou diagnosticar o erro AWSJPL006E no HWA?*
- *Qual é o significado da mensagem de erro AWSJPL006E no HWA e qual ação é recomendada?*

---
