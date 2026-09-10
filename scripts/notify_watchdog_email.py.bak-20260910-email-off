#!/usr/bin/env python3
"""notify_watchdog_email.py — Executa o watchdog do HWA 10.2.8 e envia alerta/relatório por e-mail.
Destinatário: adrianolimagarcia@gmail.com
Remetente: twstest@haos.fyi (SMTP SSL mail.haos.fyi:465)
"""
import email.message, json, smtplib, ssl, subprocess, sys, time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WATCHDOG_SCRIPT = REPO / "scripts" / "watchdog_tws_container.sh"

SMTP_HOST = "mail.haos.fyi"
SMTP_PORT = 465
SMTP_USER = "twstest@haos.fyi"
SMTP_PASS = "S$OoCip7X5JqrvC!"
DESTINATARIO = "adrianolimagarcia@gmail.com"

def run_watchdog():
    r = subprocess.run([str(WATCHDOG_SCRIPT)], capture_output=True, text=True)
    try:
        data = json.loads(r.stdout)
    except Exception:
        data = {"status": "UNKNOWN", "raw": r.stdout, "error": r.stderr}
    return r.returncode, data

def send_email(subject, body):
    msg = email.message.EmailMessage()
    msg["Subject"] = subject
    msg["From"] = f"HAOS TWS Watchdog <{SMTP_USER}>"
    msg["To"] = DESTINATARIO
    msg.set_content(body)

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx, timeout=20) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)

def main():
    force_send = "--test" in sys.argv or "--force" in sys.argv
    rc, data = run_watchdog()

    status = data.get("status", "UNKNOWN")
    ts = time.strftime("%Y-%m-%d %H:%M:%S %Z")

    # Envia email se houver falha (rc != 0) ou se for execucao de teste forçada
    if rc != 0 or force_send:
        subject = f"[HAOS HWA Monitor] Alerta de Saúde do Container: {status} ({ts})"
        if force_send and rc == 0:
            subject = f"[HAOS HWA Monitor] Relatório de Integridade e Operação: {status} ({ts})"

        body = f"""Olá Adriano,

Este é o relatório de monitoramento automatizado do nó HWA 10.2.8 (tws-hwa.lab):

============================================================
STATUS GERAL:       {status} (Código de Retorno: {rc})
DATA E HORA:        {ts}
CONTAINER:          tws-hwa
DESTINATÁRIO:       {DESTINATARIO}
============================================================

DETALHES DO SISTEMA:
- Porta 31116 (Liberty engineServer): {data.get('engine_port_31116', 'N/A')}
- Processo Batchman:                 {data.get('batchman', 'N/A')}
- Estado do Plano de Produção:       {data.get('plan', 'N/A')}

Mensagem adicional: {data.get('message', 'Todos os serviços críticos estão operacionais.')}

Atenciosamente,
Hermes Agent — Control Plane HAOS
"""
        try:
            print(f"Enviando e-mail para {DESTINATARIO} via {SMTP_HOST}:{SMTP_PORT}...")
            send_email(subject, body)
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Sistema saudável ({status}). Nenhum alerta necessário.")

if __name__ == "__main__":
    main()
