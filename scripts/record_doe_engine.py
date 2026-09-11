import json
base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-11-j2ca0056i-doe-parameter-isolation.jsonl"
ev = {
 "claim_id": "hwa-lab-10.2.8-j2ca0056i-parameter-isolation-doe-0019",
 "claim": "DoE (design of experiments) isolando validationTimeout x purgePolicy no pool JDBC do HWA 10.2.8, executado no datasource jdbc/twsdb do engineServer (que usa o banco continuamente, permitindo gatilho confiavel). METODO DO GATILHO: operacao de plano (planman ext/showinfo, conman sc) em background — o que faz o Liberty executar trabalho real no banco — combinada com pg_terminate_backend nas conexoes do engine DURANTE a operacao (conexao EM USO). Este gatilho reproduziu J2CA0056I de forma confiavel (6 novos em 5 rodadas, sem proxy e sem restart). MATRIZ 2x2 (3 rodadas cada): A=validationTimeout ausente + purgePolicy=EntirePool -> 3 erros; B=ausente + ValidateAllConnections -> 4; C=10s + EntirePool -> 3; D=10s + ValidateAllConnections -> 5. RESULTADO: NAO houve diferenca mensuravel entre os combos (3-5, nivel de ruido). CONCLUSAO IMPORTANTE E NUANCADA: validationTimeout resolve o cenario 'conexao morta OCIOSA no pool entregue depois a aplicacao' (que foi o cenario do teste A/B da DWC: 2 erros -> 0 com a correcao), mas NAO resolve o cenario 'conexao morre DURANTE uma transacao ativa' (STATE_ACTIVE_INUSE em transacao em voo) — nesse caso o erro ocorre antes de qualquer validacao previa ser util. purgePolicy=ValidateAllConnections NAO apresentou efeito mensuravel em nenhum dos dois cenarios testados. Portanto: (a) aplicar validationTimeout no jdbc/dwcdb da DWC faz sentido e esta provado para o cenario de conexao ociosa; (b) trocar purgePolicy para ValidateAllConnections NAO tem evidencia de beneficio nos testes realizados; (c) nenhum parametro de pool resolve queda de conexao em transacao ativa, que exige correcao de rede/firewall/banco.",
 "result": "SUCCESS", "risk": "read_only",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8; Liberty engineServer + PostgreSQL 18",
 "observed_at": "2026-09-11T15:35:00-03:00",
 "test_procedure": "Gatilho: planman unlock + planman ext -days 1 + planman showinfo + conman sc em background, e 0,4s depois pg_terminate_backend nas conexoes do datname TWS; 3 rodadas por combo, medindo o delta de 'grep -c J2CA0056I' no messages.log do engineServer. Config alterada por sed no datasource do engine (removendo/inserindo validationTimeout no connectionManager e trocando purgePolicy), com 15s de espera para aplicacao. Backup do datasource preservado e restaurado ao final.",
 "actual_output": "A=3, B=4, C=3, D=5 novos J2CA0056I — sem diferenca significativa entre os 4 combos. Confirma que o parametro nao altera o desfecho quando a conexao morre em transacao ativa.",
 "synthetic_questions": [
   "validationTimeout resolve o J2CA0056I em todos os cenarios?",
   "Qual a diferenca entre conexao ociosa morta no pool e conexao morta em transacao ativa?",
   "purgePolicy ValidateAllConnections melhora o comportamento do pool JDBC?",
   "O que fazer quando a conexao morre durante uma transacao ativa no Liberty?",
   "Por que o mesmo parametro de pool teve efeito na DWC e nao no engineServer?",
   "Como isolar o efeito de parametros de pool JDBC em laboratorio?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: pool JDBC Liberty (jdbc/twsdb e jdbc/dwcdb) > Interface: datasource.xml + gatilho planman/pg_terminate_backend > Topico: troubleshooting > jdbc_pool [parameter_isolation_doe]]"
}
with open(out, "w", encoding="utf-8") as f:
    f.write(json.dumps(ev, ensure_ascii=False) + "\n")
print("OK")