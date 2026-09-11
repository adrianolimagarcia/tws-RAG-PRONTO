# Plano de Enriquecimento do Dataset — HWA 10.2.8

> Registrado em 2026-09-11. Base: medicao real do corpus vs catalogo do produto.
> Corpus no momento do registro: 2.564 claims + 15 runbooks + 3.254 perguntas sinteticas.

## Diagnostico medido (numeros duros)

### 1. Cobertura de mensagens de erro: 22,3% (MAIOR LACUNA)
Comparacao do nosso `data/export/tws_error_catalog.json` contra o catalogo real do produto
(`/opt/hwa/TWS/catalog/C/*.cat`, extraido do container):

| Metrica | Valor |
|---|---|
| Codigos existentes no produto | **4.338** |
| Documentados por nos | 966 |
| Faltam | **3.372** |
| Cobertura | **22,3%** |

Piores familias:
| Familia | Cobertura | Componente |
|---|---|---|
| AWSDEM | 1,0% (1/98) | deploy |
| AWSBIJ | 3,8% (3/78) | — |
| AWSBHU | 8,5% (27/318) | conman |
| AWSDEO | 8,0% (6/75) | — |
| AWSBIB | 9,7% (14/144) | — |
| AWSBHT | 11,0% (12/109) | batchman |
| AWSBCV | 11,0% (14/127) | — |
| AWSBIA | 18,0% (52/289) | composer |

### 2. Taxonomia: 63% em "Outros"
1.609 de 2.564 claims nao classificadas — quebra o metadata filtering.

### 3. Matriz de versao: quase so 10.2.8
10.2.8=2435 | 9.5=51 | 10.1=30 | 10.2.0=32 | 10.2.3=16 | 10.2.4=9 | 10.2.7=8

### 4. Alta Disponibilidade & Failover: apenas 13 claims
Desproporcional; ha muito material de lab nao convertido.

## Acoes priorizadas

| # | Acao | Fonte | Esforco | Valor |
|---|---|---|---|---|
| P1 | Completar catalogo de erros (22% -> 80%+) | referencia oficial HCL de mensagens (crawlavel; v95 confirmado com 131 codigos AWSJPL; path 10.2.8 a descobrir) | script + crawl | ★★★★★ |
| P2 | Corrigir classificador de taxonomia (Outros 63% -> <20%) | proprio corpus | baixo | ★★★★★ |
| P3 | Matriz de versao (9.5/10.1/10.2.x) | docs HCL por versao | medio | ★★★★★ |
| P4 | Camada de incidentes do lab (HA/failover/recovery) | evidencias ja existentes | baixo | ★★★★☆ |
| P5 | Camada de configuracao (arquivos/parametros/paths) | lab + docs | medio | ★★★★☆ |

## Notas de execucao
- P1: primeiro descobrir o path exato da referencia de mensagens 10.2.8; se nao existir,
  usar v95 com marcacao explicita de versao (as mensagens sao largamente compartilhadas).
- P2: melhorar a heuristica em `scripts/consolidate_corpus.py` (funcao de classificacao).
- Toda claim nova entra como `lab-validation-*` (lab) ou com `source_url` (oficial), nunca
  editando `claims.jsonl` diretamente.
