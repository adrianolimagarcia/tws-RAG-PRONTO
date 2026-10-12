# Job UNIX script (TASKTYPE UNIXSCRIPT) — criar, executar e ver saída (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.3 do PLANO_FECHAMENTO_LACUNAS.

## Criar o script no workstation

```bash
cat > /tmp/lab_script.sh <<'EOF'
#!/bin/bash
echo "=== script de teste fase 1.3 ==="
echo "args recebidos: $1 $2"
date
exit 0
EOF
chmod +x /tmp/lab_script.sh
```

## Criar a job definition

Arquivo com cabeçalho `$JOBS` (obrigatório para `composer add`):

```
$JOBS

MDM#LAB_UNIX_SCRIPT
 SCRIPTNAME "/tmp/lab_script.sh alpha beta"
 STREAMLOGON wauser
 DESCRIPTION "Job UNIX script de teste - fase 1 item 1.3"
 TASKTYPE UNIXSCRIPT
 RECOVERY STOP
```

```bash
composer add /tmp/lab_job13.txt
```

**Nota:** argumentos vão na mesma linha do SCRIPTNAME, após o caminho.
Não existe keyword `SCRIPTARGS` — causa erro `unexpected token "SCRIPTARGS"`.

## Job stream, submit e resultado

```
SCHEDULE MDM#LAB_JS_SCRIPT
DESCRIPTION "Job stream de teste - fase 1 item 1.3"
ON RUNCYCLE RC1 "FREQ=DAILY;"
:
MDM#LAB_UNIX_SCRIPT
END
```

```bash
composer add /tmp/lab_js13.txt
conman "sbs LAB_JS_SCRIPT"
```

Saída observada (`conman "sj LAB_JS_SCRIPT;stdlist"`):
```
AWSBIS307I Starting /opt/hwa/TWS/jobmanrc /tmp/lab_script.sh alpha beta
=== script de teste fase 1.3 ===
args recebidos: alpha beta
Mon Oct 12 11:04:13 -03 2026
= Exit Status           : 0
= Elapsed Time (hh:mm:ss) : 0:00:01
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| `unexpected token "SCRIPTARGS"` | Keyword não existe | Colocar args na linha do SCRIPTNAME |
| Job ABEND com "permission denied" | Script sem +x | `chmod +x` no script |
| `Starting jobmanrc` mas sem saída | Script não encontrado no path | Usar caminho absoluto em SCRIPTNAME |
