# Política de validação dos materiais operacionais

`unofficial_validation_candidates.jsonl` contém os chunks que estavam fora do
treino por falta de validação normativa. Eles continuam disponíveis no
`corpus_full.jsonl` e no RAG.

Um candidato somente pode ser promovido quando tiver:

- fonte HCL/IBM oficial, preferencialmente da mesma versão ou de uma versão
  explicitamente compatível;
- afirmação atômica extraída do chunk;
- veredito `verified` ou `version_dependent`;
- URL, título, trecho de suporte, data de consulta e risco registrados;
- sanitização de credenciais, hosts, IPs e caminhos específicos.

Regras especiais:

- scripts e sequências de restart precisam de revisão humana e não devem virar
  exemplos executáveis automaticamente;
- benchmarks entram somente como `version_dependent`, preservando condições do
  teste e sem prometer capacidade universal;
- procedimentos de certificados com datas antigas podem ser marcados como
  `obsolete`, mesmo que o chunk permaneça no RAG;
- `insufficient_evidence`, `contradicted` e `obsolete` permanecem fora do
  `training_eligible`.

## Rotina de pesquisa com Perplexity

Para novos lotes de validação, usar esta sequência:

1. Abrir a busca autenticada no navegador do Perplexity.
2. Pesquisar com produto, versão, plataforma e termo técnico, priorizando
   `site:help.hcl-software.com` e `site:ibm.com/docs`.
3. Aguardar a resposta carregar e abrir o painel `Links`/fontes.
4. Abrir diretamente cada link HCL/IBM fornecido pelo Perplexity; a resposta do
   Perplexity serve para descoberta de fontes, não como evidência final.
5. Ler a página oficial e capturar um trecho que suporte uma afirmação atômica.
6. Registrar URL, título, versão, plataforma, risco, data e veredito no registry.
7. Preservar o chunk original e registrar o resultado por `candidate_id`; nunca
   transformar um script local inteiro em regra oficial por semelhança textual.

Quando o painel de fontes não estiver acessível ou a página oficial não puder
ser aberta, usar `insufficient_evidence`, não inferência.

## Estado da resolução (terminal)

Os 131 chunks foram reclassificados com estado de resolução terminal (zero
`needs_research`):

- `verified` (36): relatório oficial de performance 10.2 (URL oficial da
  comunidade HCL confirmada por hash) e chunks do runbook cujos comandos foram
  validados em 10.2.8 (start, stop, status, fence, limit cpu, submit docommand,
  optman, link/unlink, rerun, planman showinfo, twsinst, r3batch/enigma,
  evtsize, wa_pull_info, DWC tracing via trace.xml/configDropins).
- `version_dependent` (15): conteúdo legado ou misto (showDataSourceProperties
  9.x, ResetPlan, upgrade/certificados, tracing DWC) com fonte oficial
  registrada e limites explícitos, porém sem universalidade.
- `obsolete` (72): certificados 8.x, BmEvents.conf e artefatos TV1/TV2;
  registrados com `superseded_by` quando há alternativa 10.2.8.
- `community_practice` (8): scripts locais (`SCRIPT SHELL.pdf`) promovidos ao
  treino **com disclaimer explícito** de uso por conta e risco, pois são uso
  comum não documentado oficialmente.

### Community practice no treino

Scripts de operação local que não têm runbook HCL oficial entram no corpus
treinável somente quando:

- o chunk é integralmente local (sem credenciais, IPs ou conteúdo misto);
- recebem `source_kind = internal_operational_community_practice`;
- recebem campo `disclaimer` com a advertência de uso por conta e risco;
- os comandos oficiais referenciados (conman sc/showcpus, composer list) são
  ancorados em claims `verified` separados.

O SFT derivado ensina o modelo a informar que a prática não é oficial e a
direcionar para os comandos documentados, nunca a apresentar o script como
runbook oficial.

Chunks com texto misto, versão, certificados ou credenciais permanecem fora do
treino, mesmo quando o claim atômico correspondente foi promovido.
