#!/usr/bin/env python3
"""Proxy TCP 127.0.0.1:5433 -> 127.0.0.1:5432 com kill switch determinístico.

Ao receber SIGUSR1, fecha ABRUPTAMENTE (SO_LINGER=0 -> RST) todas as conexoes ativas,
simulando firewall/LB matando conexoes em uso (gatilho deterministico para J2CA0056I).
"""
import socket, select, signal, sys, threading, time

LISTEN = ("127.0.0.1", 5433)
TARGET = ("127.0.0.1", 5432)
active = []
lock = threading.Lock()
kill_now = False


def handle(client):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(TARGET)
    except Exception:
        client.close()
        return
    with lock:
        active.append((client, server))
    try:
        while True:
            r, _, _ = select.select([client, server], [], [], 1.0)
            if kill_now:
                break
            if client in r:
                data = client.recv(65536)
                if not data:
                    break
                server.sendall(data)
            if server in r:
                data = server.recv(65536)
                if not data:
                    break
                client.sendall(data)
    except Exception:
        pass
    finally:
        with lock:
            if (client, server) in active:
                active.remove((client, server))
        try:
            client.close()
        except Exception:
            pass
        try:
            server.close()
        except Exception:
            pass


def killer(signum, frame):
    global kill_now
    print(f"[proxy] SIGUSR1: matando {len(active)} conexoes abruptamente (RST)", flush=True)
    with lock:
        conns = list(active)
        active.clear()
    for c, s in conns:
        for sock in (c, s):
            try:
                # SO_LINGER 0 => close envia RST em vez de FIN (reset abrupto)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                                b"\x01\x00\x00\x00\x00\x00\x00\x00")
            except Exception:
                pass
            try:
                sock.close()
            except Exception:
                pass


def main():
    signal.signal(signal.SIGUSR1, killer)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(LISTEN)
    srv.listen(128)
    print(f"[proxy] escutando em {LISTEN[0]}:{LISTEN[1]} -> {TARGET[0]}:{TARGET[1]} (pid {__import__('os').getpid()})", flush=True)
    while True:
        try:
            c, _ = srv.accept()
        except Exception:
            continue
        t = threading.Thread(target=handle, args=(c,), daemon=True)
        t.start()


if __name__ == "__main__":
    main()
