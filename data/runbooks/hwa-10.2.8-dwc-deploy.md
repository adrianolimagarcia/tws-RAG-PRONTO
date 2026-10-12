# Dynamic Workload Console 10.2.8 — deploy no lab (procedimento oficial)

Data: 2026-10-12. Fase 2, itens 2.1 + 2.2 do PLANO_FECHAMENTO_LACUNAS.
Status: **LIMITACAO DOCUMENTADA** — deploy bloqueado por credencial comercial HCL (ver evidencia abaixo).

## O que e o DWC

O Dynamic Workload Console e a interface web do HCL Workload Automation:
monitoramento do plano, submissao ad-hoc, resposta a prompts, dashboards e metricas.
Roda sobre WebSphere Liberty dentro do container oficial.

## Imagem oficial

- Registro: `hclcr.io` (HCL Entitled Registry — acesso comercial)
- Imagem: `hclcr.io/wa/hcl-workload-automation-console`
- Tag do lab (10.2.8): `10.2.8.00.20260727`
- Fonte: repo oficial hcl-tech-software/hcl-workload-automation-docker-compose (readme_CONSOLE.md)

## Evidencia do bloqueio (2026-10-12, host cachyosdell)

```
$ docker pull hclcr.io/wa/hcl-workload-automation-console:10.2.8.00.20260727
Error response from daemon: pull access denied, repository does not exist
or may require authorization: authorization failed: no basic auth credentials
```

Nao ha imagem DWC local (`docker images` no host: so postgres, alpine, nginx
e as imagens customizadas tws-hwa/tws-bmdm/tws-agent). Nao ha midia de
instalacao HCL no host. O MDM (tws-hwa) nao expoe porta web (so 31111/31113/31114
TWS, 22 ssh, 5432 postgres, 41114 java) — sem DWC nao ha interface web.

## Pre-requisitos (quando houver credencial)

1. **Credencial do Entitled Registry**: solicitar ao representante comercial HCL,
   depois `docker login -u <usuario> -p <entitled_key> hclcr.io`
2. **Banco de dados dedicado ao DWC** (obrigatorio): DB2 (padrao), POSTGRES,
   ORACLE, MSSQL ou IDS. O lab tem imagem `postgres:18` local — candidata natural.
3. **Docker** 19.xx ou superior (lab: OK)
4. **Aceite da licenca**: `LICENSE=ACCEPT`

## Procedimento de deploy (docker run)

```bash
docker login -u <usuario> -p <entitled_key> hclcr.io

docker run -d --name tws-dwc --network hwa-mesh \
  -e LICENSE=ACCEPT \
  -e WA_PASSWORD='<senha-do-wauser>' \
  -e DB_TYPE=POSTGRES \
  -e DB_HOSTNAME=<host-ou-ip-do-postgres> \
  -e DB_PORT=5432 \
  -e DB_NAME=DWC \
  -e DB_USER=dwc_user \
  -e DB_PASSWORD='<senha>' \
  -e DB_ADMIN_USER=postgres \
  -e DB_ADMIN_PASSWORD='<senha-admin>' \
  -e ENGINE_HOSTNAME=tws-hwa \
  -e ENGINE_PORT=31116 \
  -e ENGINE_USER=wauser \
  -e LANG=pt_BR -e TZ=America/Sao_Paulo \
  -p 9443:9443 -p 9080:9080 \
  -v dwc-data:/home/wauser \
  hclcr.io/wa/hcl-workload-automation-console:10.2.8.00.20260727
```

Notas:
- `ENGINE_HOSTNAME/ENGINE_PORT/ENGINE_USER` preenchem automaticamente os campos
  de conexao ao engine na tela de login do DWC (MDM tws-hwa, porta 31116).
- Portas internas do Liberty sao fixas (9080 http / 9443 https); as externas
  podem ser remapeadas.
- O banco do DWC e separado do banco do TWS (que ja roda postgres na porta
  5432 dentro do tws-hwa) — usar instancia/schema dedicados.

## Verificacao pos-deploy

```bash
docker logs -f tws-dwc                      # acompanhar inicializacao do Liberty
curl -sk https://localhost:9443/ibm/console -o /dev/null -w '%{http_code}\n'  # esperado 200/302
```

No browser: `https://<host>:9443/ibm/console` -> login com wauser ->
adicionar conexao ao engine tws-hwa:31116.

## SSO (opcional)

Para SSO entre console e server, os tokens LTPA devem ser iguais nos dois
lados. Gerar uma vez com o utilitario da imagem:
`wa_create_ltpa_keys.sh -p <senha>` e distribuir `ltpa.keys`/`wa_ltpa.xml`
nos volumes de certificados/config do Liberty em ambos os componentes.

## Troubleshooting rapido

Ver runbook `hwa-10.2.8-dwc-troubleshooting.md`.

## Proximo passo quando houver credencial

1. Obter credencial HCL -> `docker login hclcr.io`
2. Subir postgres dedicado (ou schema dedicado) para o DWC
3. Executar o `docker run` acima na rede `hwa-mesh`
4. Validar login web e conexao ao engine tws-hwa:31116
5. Executar item 2.3 (validacao via browser)
