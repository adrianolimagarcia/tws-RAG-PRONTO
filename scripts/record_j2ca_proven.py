import json
base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-11-j2ca0056i-fix-proven.jsonl"
ev = {
 "claim_id": "hwa-lab-10.2.8-j2ca0056i-fix-proven-ab-0018",
 "claim": "PROVA EXPERIMENTAL (A/B reproduzivel) de que a correcao de pool JDBC elimina a mensagem J2CA0056I no datasource jdbc/dwcdb da DWC (HWA 10.2.8). Metodo: foi introduzido um proxy TCP proprio (127.0.0.1:5433 -> 127.0.0.1:5432) no caminho da DWC, com kill switch por SIGUSR1 que fecha as conexoes ativas com SO_LINGER=0, forcando RST abrupto — simulando firewall/LB matando conexoes EM USO de forma deterministica (o gatilho que pg_terminate_backend/SIGKILL nao produziam, por serem encerramentos limpos ou nao coincidirem com o uso). Carga agressiva: 30 requisicoes concorrentes a https://localhost:9443/dwc por ~8s, com kill em rajada a cada ~300ms, 3 rodadas. RESULTADO: com a configuracao ORIGINAL (purgePolicy=\"EntirePool\", SEM validationTimeout) foram reproduzidas 3 novas ocorrencias de J2CA0056I em 3 rodadas (1 por rodada, consistente). Com a configuracao CORRIGIDA (validationTimeout=\"5s\" no dataSource + purgePolicy=\"ValidateAllConnections\" no connectionManager, com restart do dwcServer) foram 0 novas ocorrencias em 4 rodadas. Conclusao: a correcao resolve o problema. Explicacao do mecanismo: validationTimeout faz o Liberty validar a conexao antes de entrega-la a aplicacao, descartando conexoes mortas; purgePolicy=ValidateAllConnections remove apenas as conexoes invalidas em vez de descartar o pool inteiro (EntirePool), evitando o efeito em cascata.",
 "result": "SUCCESS", "risk": "guided_action",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8; Liberty dwcServer + PostgreSQL 18; proxy TCP Python",
 "observed_at": "2026-09-11T12:35:00-03:00",
 "test_procedure": "1) Proxy TCP 5433->5432 com SIGUSR1 => RST abrupto (SO_LINGER=0). 2) datasource db.portNumber apontado para 5433; restart do dwcServer. 3) Teste agressivo: 30 curls concorrentes por ~8s + pkill -USR1 no proxy a cada 300ms, 3 rodadas, medindo o delta de 'grep -c J2CA0056I' no messages.log. 4) Config ORIGINAL -> 3/3 rodadas com 1 novo erro cada. 5) Config CORRIGIDA (validationTimeout=5s + ValidateAllConnections) + restart -> 0 em 4 rodadas. 6) Lab restaurado (porta 5432, proxy parado, datasource original do vendor).",
 "actual_output": "A/B conclusivo: ORIGINAL=3 novos J2CA0056I em 3 rodadas; CORRIGIDA=0 em 4 rodadas. Correcao validada experimentalmente e de forma reproduzivel.",
 "synthetic_questions": [
   "A correcao de validationTimeout e ValidateAllConnections resolve o J2CA0056I?",
   "Como reproduzir de forma deterministica o J2CA0056I em laboratorio?",
   "Por que pg_terminate_backend nao reproduz o J2CA0056I e um proxy com RST reproduz?",
   "O que muda no comportamento do pool entre purgePolicy EntirePool e ValidateAllConnections?",
   "Por que validationTimeout evita entregar conexoes mortas a aplicacao?",
   "Quantas ocorrencias de J2CA0056I a config original produziu no teste A/B?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: DWC / pool JDBC jdbc/dwcdb > Interface: datasource.xml + proxy TCP de teste > Topico: troubleshooting > jdbc_pool [j2ca0056i_fix_proven]]"
}
with open(out, "w", encoding="utf-8") as f:
    f.write(json.dumps(ev, ensure_ascii=False) + "\n")
print("OK")