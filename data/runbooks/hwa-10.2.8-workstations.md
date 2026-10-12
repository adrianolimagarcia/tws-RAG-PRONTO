# Workstations — tipos existentes no lab (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.5 do PLANO_FECHAMENTO_LACUNAS.

## Inventário (`conman "showcpus"`)

| CPUID | Tipo | Node | Estado | Papel no lab |
|-------|------|------|--------|--------------|
| MDM | UNIX MASTER | tws-hwa | IJ | Master Domain Manager |
| MDM_BK | UNIX FTA | tws-bmdm | LTI | Backup FTA (failover) |
| MDMDA | UNIX AGENT | — | LBI | Dynamic agent local |
| TWS-AGENT_1 | UNIX AGENT | tws-agent | LBI | Dynamic agent remoto |
| MDMXA | OTHR X-AGENT | — | LXI | Extended agent |
| MDM_DWB | OTHR BROKER | — | LTI | Broker (mailman dinâmico) |
| LABPOOL | OTHR POOL | — | LBI | Pool: MDMDA + TWS-AGENT_1 |
| MASTERAGENTS | OTHR POOL | — | LBI | Pool de agentes |

## Dynamic agent (ex: TWS-AGENT_1)

```
CPUNAME TWS-AGENT_1
  DESCRIPTION "This workstation was automatically created."
  OS UNIX
  NODE tws-agent SECUREADDR 31114
  FOR MAESTRO HOST MDM_DWB
    AGENTID "87B46946102139B2A0D5602502ABFA41"
    TYPE AGENT
    PROTOCOL HTTPS
END
```

- Criado automaticamente quando o dynamic agent se registra.
- Comunica via HTTPS (porta 31114) através do broker MDM_DWB.
- Roda jobs via JobManager local; ideal para workloads elásticos.

## FTA — Fault Tolerant Agent (ex: MDM_BK)

```
CPUNAME MDM_BK
  DESCRIPTION "FTA CPU"
  OS UNIX
  NODE tws-bmdm.lab TCPADDR 31111
  SECUREADDR 31113
  DOMAIN MASTERDM
  FOR MAESTRO
    TYPE FTA
    AUTOLINK ON
    BEHINDFIREWALL OFF
    SECURITYLEVEL FORCE_ENABLED
    FULLSTATUS ON
END
```

- Recebe cópia do plano (Symphony) e executa local mesmo sem o master.
- `AUTOLINK ON`: religa sozinho após queda de rede.
- Porta clássica: TCP 31111.

## Pool (ex: LABPOOL)

```
CPUNAME LABPOOL
  DESCRIPTION "Dynamic pool com agentes MDMDA e TWS-AGENT_1"
  OS OTHER
  FOR MAESTRO HOST MDM_DWB
    TYPE POOL
  MEMBERS
    MDMDA
    TWS-AGENT_1
END
```

- Jobs submetidos ao pool rodam no primeiro membro livre.
- Ver membros: definição acima ou `composer "display ws=LABPOOL"`.

## Comandos úteis

```bash
conman "showcpus"                    # lista todas as workstations e estados
conman "showcpus;offline"            # só as offline
composer "display ws=NOME"            # definição completa
conman "link MDM_BK" / "unlink MDM_BK"  # (des)conectar FTA manualmente
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Agent LBI mas job não inicia | JobManager parado no agent | checar container/serviço do agent |
| FTA não aparece no showcpus | Definição existe mas nunca linkou | `conman "link NOME"` |
| Pool não distribui | Nenhum membro livre/linkado | `showcpus` nos membros |
