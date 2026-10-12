# Guia de Treino e Inferência HWA — Qwen3-0.6B-Instruct + QLoRA

> Documento consolidado (2026-08-24). Contém: pipeline, fixes permanentes aplicados,
> descobertas da pesquisa Perplexity OPUS, e como reproduzir.

## 1. Arquitetura

```
Qwen/Qwen3-0.6B  (chat/instruction-tuned, 4-bit NF4)   ← base correto
   + LoRA rank=16/alpha=32  → output/qlora-causal/final  (domain adaptation, Step 1)
   + LoRA rank=16/alpha=32  → output/sft-hwa/final       (SFT chat, Step 2)
```

- **Modelo Instruct**: `Qwen/Qwen3-0.6B` (sem sufixo) é o post-trained/instruction-
  following. **`Qwen/Qwen3-0.6B-Instruct` NÃO existe oficialmente** no HF (verificado
  via API + Perplexity OPUS). `Qwen/Qwen3-0.6B-Base` é o raw base sem alignment.
- **Adapters separados** (CPT e SFT) — recomendado pela pesquisa de domain adaptation
  (Nature s41524-025-01564): permite controle independente por estágio.

## 2. Pipeline de Treino

```bash
# Step 1 — QLoRA domain adaptation (corpus causal data/train.jsonl)
python scripts/train_qlora.py            # ~1h07min no RTX 4060

# Step 2 — SFT com chat template nativa (data/sft/approved.jsonl)
python scripts/train_sft.py --qlora output/qlora-causal/final   # ~1h51min
```

Hiperparâmetros (config/qlora_config.yaml):

| Param | Step 1 (causal) | Step 2 (SFT) | Fonte |
|---|---|---|---|
| learning_rate | 2e-5 | 1e-4 | ICLR 2025 (arxiv 2412.13337) |
| LoRA rank/alpha | 16/32 | 16/32 | ICLR 2025 + lightning.ai |
| max_grad_norm | 0.3 | 0.3 | QLoRA NeurIPS |
| epochs | 1 | 3 | — |
| optim | adamw_torch | adamw_torch | evita GradScaler (ver fix 3) |
| dtype | bf16 | bf16 | RTX 4060 nativo |
| fp16 | false | false | — |
| packing | false | false | sem flash-attn (ver fix 5) |

## 3. Fixes Permanentes Aplicados

### Fix 1 — EOS token (Qwen3 issue #1064) ⚠️ CRÍTICO
**Problema**: tokenizer usa `<|endoftext|>` (id 151643) como eos, mas a chat template
gera `<|im_end|>` (id 151645). A geração NÃO para no fim da resposta → produz lixo
(fetisch, tailandês, repetições). Confirmado por diagnóstico + pesquisa Perplexity.

**Fix (scripts/infer_hwa.py, eval_final.py)**:
```python
model.generate(..., eos_token_id=151645, pad_token_id=151643)
```

### Fix 2 — Limpeza de prefixo não-latino
Modelos 0.6B tendem a emitir tokens de alta-entropia (ex.: tailandês) no início da
resposta. `clean_prefix()` corta até a 1ª letra ASCII. Perda média: ~11 chars em 621.

### Fix 3 — is_trainable=True ao continuar LoRA
**Problema**: `PeftModel.from_pretrained` sem `is_trainable=True` carrega o adapter com
`requires_grad=False` (adapter_config tem `inference_mode: true`) → treino roda com 0
params treináveis (loss estático, grad_norm=0). Confirmado por diagnóstico + peft issue #1340.

**Fix (train_sft.py)**: `PeftModel.from_pretrained(model, path, is_trainable=True)`
+ sanity check: `raise` se trainable_params == 0.

### Fix 4 — enable_thinking=False
Qwen3 gera `<think></think>` no SFT se habilitado, desperdiçando tokens de treino.
Usado em `apply_chat_template(..., chat_template_kwargs={"enable_thinking": False})`.
Fonte: QwenLM/Qwen3 discussion #1429.

### Fix 5 — packing=false (sem flash-attn)
O paper 2407.09105 recomenda packing + flash_attention_2. Sem flash-attn instalado,
packing causa cross-contamination entre amostras (aviso do transformers). Mantido
`packing: false` até instalar flash-attn.

### Fix 6 — adamw_torch em vez de paged_adamw_8bit
`paged_adamw_8bit` + GradScaler causava `AssertionError: No inf checks were recorded`.
`adamw_torch` resolve. O paper RTX 4060 (2509.12229) mostra paged+fp16 é mais rápido,
mas requer fp16+float16 alinhados — adiado como otimização futura.

## 4. Inferência

```bash
python scripts/infer_hwa.py --query "No HWA 10.2, para que serve conman showjobs?"
python scripts/infer_hwa.py --adapter output/sft-hwa/final --interactive
```

O script `infer_hwa.py` embute: chat template nativa + EOS fix + limpeza de prefixo
+ sampling (t=0.5, top_p=0.9, rep_penalty=1.15).

## 5. Avaliação

```bash
# G-Eval (LLM-as-judge) — reavaliação justa
python scripts/eval_geval.py            # gera respostas + julga via API
python scripts/eval_final.py            # matching (legado, tende a ser otimista)
```

- **G-Eval** usa rubrica 1-5 com CoT: factual_correctness, factual_precision,
  version_scope, risk_signaling, relevance (fonte: G-Eval, DeepEval).
- **Atenção**: factual_correctness ~0.006 no 0.6B — o modelo gera texto coerente mas
  não alinhado à evidência (limitação de capacidade para fatos novos de nicho;
  arxiv 2406.14785). Caminhos: distillation de teacher, modelo maior, ou RAG.

## 6. Resultados (RTX 4060 Laptop 8GB)

| Etapa | Tempo | eval_loss | nota |
|---|---|---|---|
| Step 1 (base, lr 2e-4) | 1h18m | 6.74 | DIVERGIU |
| Step 1 (base, lr 2e-5) | 1h07m | 2.40 | convergiu |
| Step 2 (base, bug congelado) | 1h49m | 7.56 | inútil |
| Step 2 (base, is_trainable) | 1h51m | 1.649 | funcional |
| **Step 1+2 (Instruct)** | pendente | — | objetivo |

## 7. Estado Atual (2026-08-24)

- Config: base `Qwen/Qwen3-0.6B-Instruct` + fixes documentados
- `scripts/infer_hwa.py`: inferência canônica com todos os fixes
- `scripts/train_qlora.py` / `train_sft.py`: fixes 3, 4, 6 embutidos
- `scripts/eval_final.py`: EOS fix + Instruct
- Re-treino com Instruct em andamento
