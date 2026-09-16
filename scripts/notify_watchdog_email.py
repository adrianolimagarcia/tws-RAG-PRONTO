#!/usr/bin/env python3
"""notify_watchdog_email.py — Executa o watchdog do HWA 10.2.8 e reporta por e-mail/journal.

Exit codes — ORTOGONAIS ao transporte do alerta (o e-mail ligado/desligado NAO altera o
codigo de saida; o transporte so decide se alem do journal sai e-mail):

    0 HEALTHY            1 WARNING            2 CRITICAL
    3 UNKNOWN (status nao declarado / JSON invalido)
    4 TELEMETRY_FAILURE (watchdog ausente, nao executavel ou timeout)

CORRECAO 2026-09-15 (medida no codigo): a versao anterior dava `return` no ramo do
e-mail desativado, entao o processo terminava com **exit 0** mesmo com o container DOWN
(`Result=success` no systemd = falso verde). E `UNKNOWN` (JSON invalido com rc=0) caia no
ramo `Sistema saudavel (UNKNOWN)`. Agora o status vem do watchdog e o exit code segue a
tabela acima — UNKNOWN nunca e saudavel, e falha de telemetria e um estado proprio.
"""
import email.message
import json
import os
import smtplib
import ssl
import subprocess
import sys
import time
from pathlib import Path

EXIT_HEALTHY, EXIT_WARNING, EXIT_CRITICAL, EXIT_UNKNOWN, EXIT_TELEMETRY = 0, 1, 2, 3, 4
EXIT_BY_STATUS = {
    "HEALTHY": EXIT_HEALTHY,
    "WARNING": EXIT_WARNING,
    "CRITICAL": EXIT_CRITICAL,
    "UNKNOWN": EXIT_UNKNOWN,
}

WATCHDOG_SCRIPT = Path(os.environ.get(
    "TWS_WATCHDOG_SCRIPT", str(Path(__file__).resolve().parent / "watchdog_tws_container.sh")))
# Timeout do watchdog: sem isso um `docker exec`/`conman` pendurado congela o oneshot
# indefinidamente (o systemd espera, e a janela de 30 min perde o tick seguinte).
WATCHDOG_TIMEOUT_S = int(os.environ.get("TWS_WATCHDOG_TIMEOUT", "180"))

SMTP_HOST = os.environ.get("TWS_SMTP_HOST", "mail.haos.fyi")
SMTP_PORT = int(os.environ.get("TWS_SMTP_PORT", "465"))
SMTP_USER = os.environ.get("TWS_SMTP_USER", "")
# SEGREDO: nunca no repositorio. Env ou arquivo 600 fora de base indexada.
SMTP_PASS = os.environ.get("TWS_SMTP_PASS") or (
    Path("/root/.haos/secrets/tws_smtp_pass").read_text().strip()
    if Path("/root/.haos/secrets/tws_smtp_pass").is_file() else "")
DESTINATARIO = os.environ.get("TWS_WATCHDOG_DEST", "adrianolimagarcia@gmail.com")

# Alerta por e-mail DESATIVADO por padrao (dono, 2026-09-10). O watchdog continua rodando
# e o RESULTADO sai no journal + no exit code; so o envio de e-mail esta suprimido.
# REATIVAR: drop-in no unit com Environment=TWS_WATCHDOG_EMAIL=1 + systemctl daemon-reload
EMAIL_ENABLED = os.environ.get("TWS_WATCHDOG_EMAIL", "0").strip().lower() in {"1", "true", "yes", "on"}


def run_watchdog():
    """Roda o watchdog. Devolve (rc, data, exec_ok).

    exec_ok=False => falha de TELEMETRIA (nao executou / timeout), distinta de
    "executou e reportou UNKNOWN".
    """
    try:
        r = subprocess.run([str(WATCHDOG_SCRIPT)], capture_output=True, text=True,
                           timeout=WATCHDOG_TIMEOUT_S)
    except (subprocess.TimeoutExpired, OSError) as exc:
        return None, {"status": "TELEMETRY_FAILURE", "error": f"{type(exc).__name__}: {exc}"}, False
    try:
        data = json.loads(r.stdout)
        if not isinstance(data, dict):
            raise ValueError("JSON nao e objeto")
    except Exception as exc:
        # SEM status utilizavel: NAO inventar "UNKNOWN" aqui — o rc do watchdog ainda e
        # contrato (2/3 = critico, 4 = warning) e quem decide e o classify().
        return r.returncode, {"raw": r.stdout, "error": f"{type(exc).__name__}: {exc}"}, True
    return r.returncode, data, True


def classify(rc, data, exec_ok):
    """(status, exit_code) — o status declarado manda; sem ele, o rc decide."""
    if not exec_ok:
        return "TELEMETRY_FAILURE", EXIT_TELEMETRY
    status = str(data.get("status") or "").upper()
    if status in EXIT_BY_STATUS:
        code = EXIT_BY_STATUS[status]
        # contradicao: watchdog declarou saudavel mas saiu != 0 -> nao acreditar em verde
        if status == "HEALTHY" and rc not in (0, None):
            return "UNKNOWN", EXIT_UNKNOWN
        return status, code
    # sem status utilizavel: o rc do watchdog decide (2/3 = critico, 4 = warning, 0 = unknown)
    if rc == 0:
        return "UNKNOWN", EXIT_UNKNOWN
    if rc == 4:
        return "WARNING", EXIT_WARNING
    return "CRITICAL", EXIT_CRITICAL


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
    rc, data, exec_ok = run_watchdog()
    status, code = classify(rc, data, exec_ok)
    ts = time.strftime("%Y-%m-%d %H:%M:%S %Z")

    alertar = code != EXIT_HEALTHY or force_send
    if not alertar:
        print(f"Sistema saudavel ({status}). Nenhum alerta necessario.")
        return EXIT_HEALTHY

    subject = f"[HAOS HWA Monitor] {status} do container tws-hwa ({ts})"
    if force_send and code == EXIT_HEALTHY:
        subject = f"[HAOS HWA Monitor] Relatorio de Integridade e Operacao: {status} ({ts})"

    body = f"""Olá Adriano,

Este é o relatório de monitoramento automatizado do nó HWA 10.2.8 (tws-hwa.lab):

============================================================
STATUS GERAL:       {status} (exit code: {code}; rc do watchdog: {rc})
DATA E HORA:        {ts}
CONTAINER:          tws-hwa
DESTINATÁRIO:       {DESTINATARIO}
============================================================

DETALHES DO SISTEMA:
- Porta 31116 (Liberty engineServer): {data.get('engine_port_31116', 'N/A')}
- Processo Batchman:                 {data.get('batchman', 'N/A')}
- Estado do Plano de Produção:       {data.get('plan', 'N/A')}

Mensagem adicional: {data.get('message') or data.get('error') or 'sem mensagem do watchdog'}

Atenciosamente,
Hermes Agent — Control Plane HAOS
"""
    if not EMAIL_ENABLED:
        # Alerta suprimido no TRANSPORTE: o resultado segue no journal e no exit code.
        print(f"[email-desativado] alerta NAO enviado — STATUS={status} exit={code} rc={rc} ts={ts}")
        print(body)
        return code

    try:
        print(f"Enviando e-mail para {DESTINATARIO} via {SMTP_HOST}:{SMTP_PORT}...")
        send_email(subject, body)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        # Falha de TRANSPORTE nao apaga o diagnostico: devolve o pior entre o status
        # real e a falha de entrega (nunca 0).
        print(f"Erro ao enviar e-mail: {e}", file=sys.stderr)
        return max(code, EXIT_WARNING) if code != EXIT_HEALTHY else EXIT_TELEMETRY
    return code


if __name__ == "__main__":
    sys.exit(main())
