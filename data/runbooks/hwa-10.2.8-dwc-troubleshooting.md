# DWC 10.2.8 — troubleshooting

Data: 2026-10-12. Fase 2, item 2.4 do PLANO_FECHAMENTO_LACUNAS.
Cenario de referencia: DWC em container `tws-dwc` na rede `hwa-mesh`,
conectando ao MDM `tws-hwa:31116` (ver `hwa-10.2.8-dwc-deploy.md`).

## 1. Container nao sobe / Liberty nao inicializa

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| Container sai logo apos `docker run` | `LICENSE` nao aceito | Verificar `-e LICENSE=ACCEPT` (obrigatorio) |
| Log trava em "waiting for database" | DB_HOSTNAME/DB_PORT errados ou DB fora do ar | `docker exec tws-dwc ping <db>`; conferir credenciais DB_* |
| `create_database.sql` nao rodou | Schema do DWC nao criado | Extrair da imagem: `docker run --rm <img> cat /opt/dwc/tools/create_database.sql` e aplicar no DB antes de subir |

## 2. Conexao recusada ao engine (MDM)

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| DWC mostra engine "Disconnected" / connection refused | Porta 31116 fechada ou hostname errado | No MDM: `ss -tlnp | grep 31116`; do DWC: `nc -zv tws-hwa 31116` (ambos na mesma rede docker) |
| Timeout intermitente | Firewall entre redes | Manter DWC e MDM na mesma rede (`hwa-mesh`) |
| "Engine hostname" vazio no login | `ENGINE_HOSTNAME` nao passado | Recriar container com `-e ENGINE_HOSTNAME=tws-hwa -e ENGINE_PORT=31116 -e ENGINE_USER=wauser` |

## 3. Certificados SSL

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| Browser acusa certificado invalido em `https://<host>:9443` | Cert self-signed padrao do Liberty | Esperado em lab; aceitar excecao ou instalar cert proprio |
| DWC nao confia no engine (SSL handshake failure) | CA do MDM nao importada no truststore do DWC | Montar volume `<dir-certs>:/opt/wautils/certs` com `ca.crt`, `tls.crt`, `tls.key` e informar `SSL_PASSWORD` |
| Erro apos trocar certificado | Keystore desatualizado | Reiniciar container; Liberty recarrega do volume |

## 4. Usuario sem permissao

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| Login OK mas sem ver o plano / acoes bloqueadas | `WA_PASSWORD` diverge da senha do wauser no MDM | Alinhar a senha nos dois lados e recriar o container |
| "Not authorized" ao submeter job | Usuario DWC sem papel de operador no engine | No MDM, verificar `composer "display user=<nome>"` e papeis; usar wauser (admin do lab) para validar |

## 5. SSO (LTPA) quebrado

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| SSO funcionava e parou apos recriar um lado | `ltpa.keys` diferentes entre console e server | Regenerar uma vez com `wa_create_ltpa_keys.sh -p <senha>` e redistribuir `ltpa.keys` + `wa_ltpa.xml` nos dois lados |

## 6. Banco de dados do DWC

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| DWC lento / erros de escrita | Disco do volume do DB cheio | `docker system df`; limpar volumes orfaos |
| Tabelas DWC corrompidas apos queda | Shutdown abrupto do postgres | Restaurar backup do schema DWC; em lab, recriar schema e re-subir |

## Comandos uteis

```bash
docker logs -f tws-dwc                                   # log do Liberty
docker exec tws-dwc ss -tlnp | grep -E '9080|9443'        # portas do console
curl -sk https://localhost:9443/ibm/console -o /dev/null -w '%{http_code}\n'
docker exec tws-dwc nc -zv tws-hwa 31116                  # alcance ao MDM
```
