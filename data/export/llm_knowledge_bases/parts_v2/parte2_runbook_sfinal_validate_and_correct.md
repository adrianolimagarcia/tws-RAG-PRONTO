# PARTE2 RUNBOOK SFINAL VALIDATE AND CORRECT

## RUNBOOK: Runbook: Validar e corrigir FINAL/Sfinal no HWA 10.2.8

**Arquivo de origem:** `data/runbooks/sfinal-validate-and-correct.md`

### Objetivo

Confirmar se os streams `FINAL` e `FINALPOSTREPORTS` do banco correspondem ao
arquivo `Sfinal`/`Sfinal2` instalado, verificar a cadeia de dependências e
identificar se o ciclo noturno gera `Symnew`, executa `SwitchPlan` e sincroniza
o plano. Este runbook não presume que `planman ext` seja falha: no produto, o
FINAL automatiza o ciclo de produção; a escolha entre extensão e criação deve
ser confirmada pelo script `MakePlan` e pelos parâmetros do plano.

### Evidência do laboratório (somente leitura)

Executar como `wauser` com o ambiente carregado:

```bash
date '+%F %T %z %Z'
optman ls | grep -iE 'startOfDay|enTimeZone|LegacyStartOfDay'
conman 'showcpu;info'
planman showinfo
conman 'sj MDMXA#@'
composer 'display sched MDMXA#FINAL'
composer 'display sched MDMXA#FINALPOSTREPORTS'
```

Preservar também:

```bash
cp -p "$UNISONHOME/Sfinal" /tmp/Sfinal.lab
cp -p "$UNISONHOME/Sfinal2" /tmp/Sfinal2.lab
composer 'display sched MDMXA#FINAL' > /tmp/final-db.txt
composer 'display sched MDMXA#FINALPOSTREPORTS' > /tmp/finalpost-db.txt
```

Não coletar senhas, tokens, certificados ou conteúdo de `Security`.

### Diagnóstico

### 1. Comparar a fonte e o banco

```bash
diff -u "$UNISONHOME/Sfinal" "$UNISONHOME/config/Sfinal"
diff -u "$UNISONHOME/Sfinal" "$UNISONHOME/Sfinal2"
composer 'display sched MDMXA#FINAL'
composer 'display sched MDMXA#FINALPOSTREPORTS'
```

No laboratório validado, `config/Sfinal` e `Sfinal` eram iguais. O banco
continha a variante `Sfinal`, com `FINAL` dependente de
`FINAL.SWITCHPLAN PREVIOUS`; `Sfinal2` acrescentava a dependência temporal do
`FINALPOSTREPORTS.UPDATESTATS` anterior. Isso é uma diferença de ordenação e
carry-forward, não prova por si só que `Sfinal2` force `planman crt`.

### 2. Verificar a cadeia executada

O ciclo esperado é:

```text
STARTAPPSERVER -> MAKEPLAN -> SWITCHPLAN
SWITCHPLAN -> CHECKSYNC -> CREATEPOSTREPORTS -> UPDATESTATS
```

Verificar o último ciclo:

```bash
grep -aH -E 'Running planman (crt|ext)|AWSJCL062I|AWSJCL065I|Ending SwitchPlan|Exit Status|AWSJPL206W' \
  "$UNISONHOME"/../TWSDATA/stdlist/YYYY.MM.DD/*
```

Critérios:

- `MAKEPLAN` termina com código aceito pelo `RCCONDSUCC`.
- `SWITCHPLAN` termina com `Exit Status: 0`.
- há `AWSJCL065I Run number has been successfully updated`.
- `CHECKSYNC` e `UPDATESTATS` terminam sem erro.

### 3. Verificar datas e timezone

`startOfDay`, o timezone do sistema, `conman showcpu;info` e o timezone
explicitamente definido no MDM devem ser coerentes. O alerta `AWSJPL206W`
deve ser tratado, mesmo quando o sistema herda `America/Sao_Paulo`.

### Mudança controlada (não executar sem aprovação)

Se a análise confirmar que o banco precisa da variante fornecida pelo produto:

1. Exportar as definições atuais e registrar checksum dos arquivos.
2. Comparar customizações; não sobrescrever uma definição customizada sem
   mesclar as mudanças.
3. Aplicar a fonte aprovada com `composer replace` ou o procedimento de
   upgrade indicado pela versão.
4. Cancelar instâncias FINAL antigas somente com uma janela aprovada.
5. Submeter as novas instâncias conforme a documentação.
6. Executar `JnextPlan` em janela controlada.
7. Validar `planman showinfo`, `conman sj`, `CHECKSYNC`, `SWITCHPLAN` e o run
   number.

Não executar automaticamente:

```bash
rm Symphony
ResetPlan
composer replace Sfinal2
```

O último comando altera objetos do banco e deve ser aprovado antes da execução.

### Critérios de aceitação

- [ ] `Sfinal`/`Sfinal2` e as definições do banco foram comparados.
- [ ] A cadeia FINAL foi validada sem instâncias concorrentes.
- [ ] O timezone do sistema e das workstations foi registrado.
- [ ] `startOfDay` foi comparado com o horário de início do plano.
- [ ] O último ciclo teve `MAKEPLAN`, `SWITCHPLAN`, `CHECKSYNC` e
      `UPDATESTATS` bem-sucedidos.
- [ ] Nenhuma alteração foi aplicada sem aprovação.
- [ ] Após eventual mudança, um novo ciclo foi validado por logs e comandos.

### Fontes oficiais

- HCL 10.2.8 — Automating production plan processing:
  https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgautomateprodplan.html
- HCL 10.2.8 — JnextPlan:
  https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html
- HCL 10.2.8 — Customizing and submitting optional FINAL:
  https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiparallelupgradefrom95FINALjs.html
- HCL 10.2.8 — SwitchPlan same run number:
  https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrswitchplan3.html
- HCL 10.2.8 — Time/date inconsistency:
  https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrtimezone.html
