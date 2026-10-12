# Segurança: SSL/TLS e autenticação de usuários — referência do lab (10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM). Fase 3, item 3.4 do PLANO_FECHAMENTO_LACUNAS.
Somente leitura — nenhum segredo exposto (senhas/hashes mascarados).

## SSL/TLS entre componentes

### Modo e versão (localopts)
| Parâmetro | Valor | Significado |
|-----------|-------|-------------|
| SSL auth mode | caonly | Autenticação mútua via CA (certificado obrigatório) |
| SSL auth string | tws | String de autenticação esperada |
| SSL version | atleast.TLSv1.2 | Mínimo TLS 1.2 |
| SSL FIPS compliance | no | FIPS desabilitado no lab |

### Certificados (em /opt/hwa/TWSDATA/ssl/certs/)
| Arquivo | Função |
|---------|--------|
| TWSClientKeyStore.p12 | Keystore do cliente (certificado + chave) |
| TWSClientTrustStore.pem | Truststore (CAs confiáveis) |
| tls.sth | Stash da senha do keystore (<redacted>) |
| tls.rnd | Seed aleatória para SSL |
| /opt/hwa/TWSDATA/ssl/aes/key.p12 | Keystore AES para criptografia interna |

### Portas SSL
| Porta | Serviço |
|-------|---------|
| 31113 | netman SSL (comunicação entre workstations) |
| 31116 | appserver HTTPS (REST API, DWC) |
| 31131 | EIF SSL (eventos) |

## Autenticação de usuários (Security.conf)

Arquivo: `/opt/hwa/TWS/Security.conf`. Modelo do lab (aberto, ambiente de teste):

```
user maestro
    cpu = @ + logon = wauser, root, wauser
```

- Usuário `maestro` tem acesso total (`@`) a todos os objetos em todas as CPUs
- Logons permitidos para execução de jobs: `wauser`, `root`

## Verificar

```bash
# certificado do netman SSL:
openssl s_client -connect tws-hwa:31113 </dev/null 2>/dev/null | openssl x509 -noout -subject -dates

# REST API com autenticação:
curl -sk -u <redacted> https://tws-hwa:31116/twsd/
```

## Troubleshooting
| Sintoma | Verificar |
|---------|-----------|
| Erro de handshake SSL | `SSL version`, certificados expirados? `tls.sth` íntegro? |
| CLI rejeitada | `SSL auth string` confere? truststore tem a CA? |
| Acesso negado a objeto | Regras em `Security.conf` para o usuário |
