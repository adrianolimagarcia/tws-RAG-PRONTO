# Chamado Suporte HCL — Endpoint de Listagem de API Keys (HWA 10.2.8)

> Revisão de 14/10/2026 — investigação controlada com reprodução, matriz de
> variações, stack trace capturado do log real e validação da spec embarcada.
> Todos os resultados abaixo vêm de execução real contra lab Docker
> (`tws-hwa`/`tws-bmdm`/`tws-agent`/`tws-dwc`, rede `hwa-mesh`).
> Segredos redigidos como `<senha>`/`<JWT>`. Nenhum commit realizado.

## 1. Identificação do Produto e Ambiente
- **Produto:** HCL Workload Automation (HWA) / Engine & MDM
- **Versão exata:** 10.2.8.00 (comprovada via SWID tag dentro do container:
  `/opt/hwa/iso-swid/hcltechsw.com_IWS_Server.swidtag`,
  `tagId="hcltechsw.com-…-10.2.8.00" version="10.2.8.00"`;
  componente REST `TWSdRESTWeb-10.2.8.00-SNAPSHOT.war`)
- **Fix Pack:** nenhum superior disponível (10.2.8 é a última versão)
- **Ambiente de Reprodução:**
  - Container Engine: Liberty + RESTEasy/Jakarta (conforme stack trace da §6)
    no `tws-hwa`; banco PostgreSQL (`TWS`) no mesmo container
  - Protocolo / Porta: HTTPS na porta 31116 (`https://<MDM>:31116/twsd/api/v2/apikey`)
  - Auth dos testes: basic auth como `wauser` e como `apiadmin` (conta local
    do `basicRegistry` do engine)
  - Observado antes em dois labs independentes (WSL em 22/08/2026,
    Docker em 13/10/2026)

---

## 2. Descrição dos Sintomas e Defeitos (validados em 14/10/2026, lab Docker, HWA 10.2.8.00)

Foram identificados **dois bugs críticos de implementação** no endpoint de listagem de API keys (`GET /twsd/api/v2/apikey`):

### Defeito 1 — Curto-circuito silencioso retornando lista vazia (`{"count":0}`)
Ao invocar o endpoint sem fornecer query parameters de paginação:
```http
GET /twsd/api/v2/apikey HTTP/1.1
Host: <MDM>:31116
Authorization: Basic <redigido>
```
**Resposta Obtida:** `HTTP/1.1 200 OK` com corpo exato:
```json
{"count":0,"next":"","previous":""}
```
**Impacto:** Mesmo com keys válidas do próprio usuário na tabela `mdl.aky_api_keys` (5 no banco no teste; 4 listáveis por `wauser` com paginação — ver §7), a API retorna `count: 0`. O usuário e integrações automatizadas concluem erroneamente que não existem chaves cadastradas.

### Defeito 2 — HTTP 500 (NullPointerException) ao paginar informando apenas um parâmetro
Ao fornecer `limit` sem `offset` (ex: `?limit=100` ou `?limit=10`) ou fornecer `offset` sem `limit` (ex: `?offset=0`):
```http
GET /twsd/api/v2/apikey?limit=100 HTTP/1.1
Host: <MDM>:31116
Authorization: Basic <redigido>
```
**Resposta Obtida:** `HTTP/1.1 500 Internal Server Error` (corpo vazio).

---


---

## 3. Contrato Oficial no Swagger/OpenAPI do Próprio Produto

Na especificação OpenAPI embarcada no próprio WAR do engine
(`…/TWSdRESTWeb-10.2.8.00-SNAPSHOT.war/IWS_API3_all_dist.json`,
paths `/api/v2/apikey` e `/api/v2/apikey/{apiKeyId}`), o `GET` da coleção
declara os parâmetros `limit` (integer/int32), `offset` (integer/int32)
e `oql` (string) — **nenhum com `"required": true`**, logo **todos
opcionais** por OpenAPI v3. Summary:
`"Retrieve all API keys corresponding to provided query."`.
Respostas documentadas: `200 / 401 / 403 / 404`
(`404`: `"No API key has been found with provided query."`).
**Não há 500 documentado**, nem lista vazia forçada sem parâmetros.

```json
"/api/v2/apikey": {
  "get": {
    "summary": "Retrieve all API keys corresponding to provided query.",
    "description": "Given a oql query, retrieves all his API keys.",
    "tags": [ "V2 APIs - API Key" ],
    "parameters": [
      {
        "name": "limit",
        "in": "query",
        "schema": { "type": "integer", "format": "int32" }
      },
      {
        "name": "offset",
        "in": "query",
        "schema": { "type": "integer", "format": "int32" }
      },
      {
        "name": "oql",
        "in": "query",
        "schema": { "type": "string" }
      }
    ],
    "responses": {
      "200": { "description": "API keys correctly retrieved." },
      "401": { "description": "Not Authorized" },
      "403": { "description": "Not Allowed" },
      "404": { "description": "No API key has been found with provided query." }
    }
  }
}
```

### Análise do Contrato:
1. Os parâmetros `limit` e `offset` **NÃO possuem `"required": true`**. Pelas regras da especificação OpenAPI v3, ambos são parâmetros **opcionais**.
2. Não há menção de que a ausência dos parâmetros resulte em retorno de lista vazia forçada (`count: 0`).
3. Não há previsão de HTTP 500 quando apenas um dos parâmetros opcionais é enviado.

---

## 4. Por que a UI Oficial (DWC) Funciona e Clientes REST Falham?

Na inspeção do código JavaScript da UI oficial do Dynamic Workload Console
(`…/DWC-10.2.8.00-SNAPSHOT.ear/Console.war/dashboard/index.bundle.js`), o método `fetchApiDataTable` foi implementado acoplando rigidamente a query string:

```javascript
fetchApiDataTable: function(e) {
    var t = "/dwc/rest/proxy/" + e.engineId + "/api/v2/apikey";
    if (t = t + "?limit=" + e.limit + "&offset=" + e.offset, e.filter) {
        ...
```

A UI do DWC **sempre concatena obrigatoriamente** `?limit=` e `&offset=` com valores numéricos. Por isso a tela web funciona, mas qualquer cliente REST que segue o manual Swagger (curl, Swagger UI, Postman, scripts) encontra os dois comportamentos anômalos.

---

## 5. Causa Raiz Técnica (inferência a partir de stack trace + comportamento — sem fonte)

> Sem acesso ao fonte (produto proprietário; nenhuma descompilação foi
> tentada — análise estritamente comportamental/observável). O mecanismo
> abaixo é **inferência** a partir do stack + matriz, não fato verificado
> no código.

A classe responsável pelo endpoint (pilha real, RESTEasy/Jakarta no Liberty) é
`com.ibm.tws.twsd.rest.util.ResourceServiceAPIKey` (método `get`),
chamada por `com.ibm.tws.twsd.rest.security.impl.APIKeyV2ResourceImpl.get`:

```java
public PaginatedResponse<ApiKeyResponseV2> get(String oql, Integer offset, Integer limit, URI uri, HttpHeaders headers) {
    ...
    // CAUSA DO DEFEITO 1:
    // Se ambos offset e limit forem omitidos (null), o método curto-circuita e retorna 0 itens estáticos sem consultar o banco:
    if (offset == null && limit == null) {
        return new PaginatedResponse(new QueryResponse(0L, new ArrayList()), "", "");
    }

    // CAUSA DO DEFEITO 2:
    // Se limit for passado mas offset for nulo (ou vice-versa), ocorre unboxing direto (.intValue()):
    queryTWSObjectPage(..., limit.intValue(), offset.intValue(), ...); // java.lang.NullPointerException!
    ...
}
```

### Análise:
1. **Violação de padrão REST e contrato de defaults:** O método espera obrigatoriamente que o cliente envie simultaneamente `limit` e `offset`. Caso omitidos, deveria aplicar valores padrão razoáveis (ex: `offset=0`, `limit=50`). Em vez disso, assume falsamente que ausência de parâmetros significa coleção vazia (`QueryResponse(0L, new ArrayList())`).
2. **Ausência de validação / unboxing inseguro de wrappers numéricos:** Ao invocar `offset.intValue()` e `limit.intValue()` sem testar se um dos dois é nulo, a JVM estoura `java.lang.NullPointerException`, capturado pelo runtime JAX-RS e convertido em HTTP 500.

**Correção sugerida à engenharia HCL:** aplicar defaults quando nulos (ex. `offset = 0`, `limit = 50`) e remover o retorno de lista vazia, deixando a query ao banco ocorrer normalmente.

---

## 6. Stack Trace Capturado no Liberty (`messages.log`)

Registrado em `/opt/hwa/TWSDATA/stdlist/appserver/engineServer/logs/messages.log`
(dentro do container `tws-hwa`) em ocorrências múltiplas em 13–14/10/2026

```text
java.lang.NullPointerException: Cannot invoke "java.lang.Integer.intValue()" because "offset" is null
	at com.ibm.tws.twsd.rest.util.ResourceServiceAPIKey.get(ResourceServiceAPIKey.java:106)
	at com.ibm.tws.twsd.rest.security.impl.APIKeyV2ResourceImpl.get(APIKeyV2ResourceImpl.java:97)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
	at java.base/java.lang.reflect.Method.invoke(Method.java:586)
	at org.jboss.resteasy.core.MethodInjectorImpl.invoke(MethodInjectorImpl.java:154)
	at org.jboss.resteasy.core.MethodInjectorImpl.invoke(MethodInjectorImpl.java:118)
	at org.jboss.resteasy.core.ResourceMethodInvoker.internalInvokeOnTarget(ResourceMethodInvoker.java:560)
	at org.jboss.resteasy.core.ResourceMethodInvoker.invokeOnTargetAfterFilter(ResourceMethodInvoker.java:452)
	at org.jboss.resteasy.core.ResourceMethodInvoker.lambda$invokeOnTarget$2(ResourceMethodInvoker.java:413)
	at org.jboss.resteasy.core.interception.jaxrs.PreMatchContainerRequestContext.filter(PreMatchContainerRequestContext.java:385)
	at org.jboss.resteasy.core.ResourceMethodInvoker.invokeOnTarget(ResourceMethodInvoker.java:415)
	at org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:378)
	at org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:356)
	at org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:70)
	at org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java:429)
	at org.jboss.resteasy.core.SynchronousDispatcher.lambda$invoke$4(SynchronousDispatcher.java:240)
	at org.jboss.resteasy.core.SynchronousDispatcher.lambda$preprocess$0(SynchronousDispatcher.java:153)
	at org.jboss.resteasy.core.interception.jaxrs.PreMatchContainerRequestContext.filter(PreMatchContainerRequestContext.java:385)
	at org.jboss.resteasy.core.SynchronousDispatcher.preprocess(SynchronousDispatcher.java:157)
	at org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java:229)
	at org.jboss.resteasy.plugins.server.servlet.ServletContainerDispatcher.service(ServletContainerDispatcher.java:245)
	at org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:55)
	at org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:51)
	at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:614)
	at com.ibm.ws.webcontainer.servlet.ServletWrapper.service(ServletWrapper.java:1262)
```

(Variante com `because "limit" is null` ocorre nas chamadas com só `offset`.)

---

## 7. Passos para Reprodução Controlada

1. **Criar uma chave de teste:**
   ```bash
   curl -sk -u "wauser:<senha>" -X POST "https://<MDM>:31116/twsd/api/v2/apikey" \
     -H "Content-Type: application/json" \
     -d '{"label":"hcl-repro-key","type":"PERSONAL"}'
   ```
   *Retorno:* `HTTP 200` com `{"token":"<JWT>"}`.

2. **Confirmar persistência física no banco:**
   ```sql
   SELECT aky_user FROM mdl.aky_api_keys WHERE aky_label='hcl-repro-key';
   -- Retorna o próprio usuário autenticado (a listagem filtra por dono)
   ```

3. **Reproduzir Defeito 1 (retorno de envelope vazio estático):**
   ```bash
   curl -sk -u "wauser:<senha>" "https://<MDM>:31116/twsd/api/v2/apikey"
   ```
   *Retorno:* `HTTP 200` com `{"count":0,"next":"","previous":""}`.

4. **Reproduzir Defeito 2 (HTTP 500 NPE):**
   ```bash
   curl -sk -u "wauser:<senha>" "https://<MDM>:31116/twsd/api/v2/apikey?limit=100"
   ```
   *Retorno:* `HTTP 500 Internal Server Error`.

5. **Comprovar funcionamento quando AMBOS os parâmetros são passados:**
   ```bash
   curl -sk -u "wauser:<senha>" "https://<MDM>:31116/twsd/api/v2/apikey?limit=100&offset=0"
   ```
   *Retorno:* `HTTP 200` com a lista real contendo o registro da chave criada.

---

## 8. Workaround Operacional Imediato

Para clientes e integrações consumirem o endpoint no HWA 10.2.8 enquanto o fix pack não é liberado:

1. **Sempre enviar explicitamente ambos os query parameters `limit` e `offset`:**
   ```
   GET https://<MDM>:31116/twsd/api/v2/apikey?limit=100&offset=0
   ```
2. Caso seja necessário filtrar registros, pode-se combinar com o parâmetro `oql`
   (atenção: strings exigem **aspas simples** — aspas duplas retornam `400 AWSMAC002E`):
   ```
   GET https://<MDM>:31116/twsd/api/v2/apikey?limit=100&offset=0&oql=type='SERVICE'
   ```
3. A consulta por UUID direto (`GET /twsd/api/v2/apikey/<uuid>`) não é impactada e funciona de maneira pontual.

---

## 9. Correção Solicitada à Engenharia da HCL

No método `ResourceServiceAPIKey.get`:
1. Aplicar valores default quando `limit` ou `offset` forem nulos (ex: `int effectiveLimit = (limit != null) ? limit : 50; int effectiveOffset = (offset != null) ? offset : 0;`).
2. Remover o curto-circuito que retorna envelope vazio quando ambos são nulos, permitindo que a query ao banco ocorra normalmente com os defaults de paginação.

---

## 10. Limpeza e Verificação Pós-Investigação (14/10/2026)

Investigação encerrada sem resíduos: as 5 chaves de teste criadas na
reprodução de 13/10/2026 foram excluídas via `DELETE /twsd/api/v2/apikey/<id>`
(com autenticação do respectivo dono em cada caso), todas retornando `HTTP 200`:

- `buglist-test-repro` / `buglist-test-service` / `buglist-test-multi1` /
  `buglist-test-multi2` (dono `wauser`, deletadas como `wauser`)
- `buglist-test-apiadmin` (dono `apiadmin`, deletada como `apiadmin`)

Verificado em 14/10/2026: `SELECT count(*) FROM mdl.aky_api_keys;` → `0`.
Temporários com credenciais foram destruídos com `shred -u`;
nenhuma credencial ou JWT foi persistido em arquivo, log ou relatório.
