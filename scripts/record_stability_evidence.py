import json
base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-10-container-oom-restart-stability.jsonl"
ev = {
 "claim_id": "hwa-lab-10.2.8-container-sigkill-restart-recovery-0013",
 "claim": "No laboratorio HWA 10.2.8 containerizado (tws-hwa + tws-bmdm + tws-agent), os tres containers podem ser terminados simultaneamente com exit code 137 (SIGKILL) por pressao de memoria do host. O host observado tem 30 GiB de RAM e swap zram de 31 GiB com vm.swappiness=100; os limites dos containers sao tws-hwa 4 GiB RAM + 6 GiB swap, tws-bmdm 4 GiB RAM + 6 GiB swap e tws-agent 2 GiB RAM + 3 GiB swap (potencial combinado de ~25 GiB). Nao havia registro de OOM-killer no dmesg/journalctl no momento da analise, portanto o SIGKILL pode ter origem em cgroup/`docker stop`/restart do daemon e nao apenas no OOM-killer do kernel. IMPORTANTE: apos o SIGKILL, o dominio volta SAUDAVEL sozinho no restart (`docker start`), pois as units de boot (postgresql-18, tebctl/agente, engine Liberty, tws-domain-start) estao habilitadas — verificado: postgres active, engine em LISTEN na 31116, `conman status` = 'Batchman LIVES'. A queda abrupta durante a janela de virada de plano e a causa upstream do incidente de plano preso (AWSJPL017E), pois interrompe a operacao do planner deixando lock orfao. Mitigacao recomendada: executar `planman unlock` apos qualquer restart nao planejado antes de operacoes de plano, e considerar aumento de memoria do host ou reducao dos limites dos containers.",
 "result": "SUCCESS", "risk": "read_only",
 "platform": "Distributed; Linux x86_64; containers RHEL 9 UBI9 na rede hwa-mesh; HWA 10.2.8",
 "observed_at": "2026-09-10T17:40:00-03:00",
 "test_procedure": "Observado 'docker ps -a' com os tres containers em 'Exited (137)'; inspecionados limites via 'docker inspect' (Memory/MemorySwap); verificado 'free -h' (30 GiB RAM, 6.4 GiB livre, swap zram 8.4 GiB usada) e swappiness. Apos 'docker start' dos tres containers, verificado o estado do dominio: systemctl is-active postgresql-18, porta 31116 e conman status.",
 "actual_output": "Containers reiniciados com sucesso; dominio voltou operacional sem intervencao manual (Batchman LIVES, engine LISTEN, postgres active); confirmado que a queda nao deixou corrupcao permanente.",
 "synthetic_questions": [
   "O que significa o exit code 137 em um container Docker do HWA?",
   "Os containers do laboratorio HWA voltam sozinhos apos um SIGKILL?",
   "Qual a relacao entre a queda abrupta dos containers e o plano de producao preso (AWSJPL017E)?",
   "Quais sao os limites de memoria configurados nos containers tws-hwa, tws-bmdm e tws-agent?",
   "O que fazer apos um restart nao planejado dos containers HWA antes de operar o plano?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: laboratorio containerizado / estabilidade > Interface: docker + systemd interno > Topico: operations > lab_stability [sigkill_restart]]"
}
with open(out, "w", encoding="utf-8") as f:
    f.write(json.dumps(ev, ensure_ascii=False) + "\n")
print("OK")