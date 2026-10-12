# localopts e globalopts do MDM — referência do lab (10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM). Fase 3, item 3.1 do PLANO_FECHAMENTO_LACUNAS.
Arquivos reais: `/opt/hwa/TWSDATA/localopts` e `/opt/hwa/TWSDATA/config/globalopts`.
Somente leitura — nenhuma alteração foi feita.

## globalopts (atributos do domínio)

| Parâmetro | Valor no lab | Significado |
|-----------|--------------|-------------|
| company | LAB | Nome da empresa/dominio |
| master | MDM | Workstation master do domínio |
| start | 0000 | Hora de início do dia de produção (meia-noite) |

## localopts — parâmetros relevantes em uso

### Identidade
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| thiscpu | MDM | Nome desta workstation |

### batchman (execução do plano)
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| bm check file | 120 | Intervalo (s) de verificação de arquivos |
| bm check status | 300 | Intervalo (s) de checagem de status |
| bm look | 5 | Janela de antecipação (min) para jobs |
| bm check until | 300 | Tempo máx (s) esperando condição |

### jobman (execução de jobs)
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| jm job table size | 1024 | Tamanho da tabela de jobs |
| jm nice | 0 | Prioridade UNIX dos jobs |
| jm no root | yes | Jobs NÃO rodam como root (segurança) |

### mailman (comunicação)
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| mm response | 600 | Timeout (s) de resposta |
| mm retrylink | 600 | Intervalo (s) de retentativa de link |
| mm unlink | 960 | Tempo (s) antes de declarar link caído |

### netman (rede)
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| nm port | 31111 | Porta TCP do netman |
| nm SSL full port | 31113 | Porta SSL do netman |
| nm retry | 800 | Tentativas de reconexão |

### SSL (ver item 3.4 para detalhes)
| Parâmetro | Valor |
|-----------|-------|
| SSL auth mode | caonly |
| SSL auth string | tws |
| SSL version | atleast.TLSv1.2 |
| SSL certificate | /opt/hwa/TWSDATA/ssl/certs/TWSClientKeyStore.p12 |

### Diversos
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| CAN BE EVENT PROCESSOR | yes | MDM pode processar eventos |
| Appserver auto restart | yes | Reinicia o appserver se cair |
| DEFAULTWS | MDM | Workstation padrão no conman |

## Quando mexer
- `bm look` / `bm check status`: ajuste fino de performance do plano
- `mm unlink`: links instáveis entre MDM e agentes
- `jm no root`: nunca mude para `no` sem motivo forte (segurança)

## Troubleshooting
| Sintoma | Verificar |
|---------|-----------|
| Jobs demoram a iniciar | `bm check status`, `bm look` |
| Agent aparece como UNLINK | `mm unlink`, `mm retrylink`, rede/porta 31111 |
| CLI não conecta | `HOST`, `PORT`, `PROTOCOL` no fim do localopts |
