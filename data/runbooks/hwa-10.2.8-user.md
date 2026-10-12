# User — objeto de credencial para logon de jobs (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, item 1.11 do PLANO_FECHAMENTO_LACUNAS.

## Para que serve

O objeto `user` armazena credenciais que o TWS usa para executar jobs com
um logon específico (relacionado ao `STREAMLOGON` da job definition).
Sem o objeto correspondente, jobs com STREAMLOGON de outro usuário falham.

## Criar

```
USERNAME LABUSR_DOC
  PASSWORD "senha_teste_123"
END
```

```bash
composer add /tmp/lab_usr.txt
```

## Consultar (senha mascarada)

```bash
composer "display user=LABUSR_DOC"
```

```
USERNAME LABUSR_DOC
  PASSWORD "**********"
END
```

A senha nunca é exibida — aparece mascarada mesmo para o dono.

## Relação com STREAMLOGON

Na job definition:
```
MDM#MEU_JOB
 DOCOMMAND "..."
 STREAMLOGON wauser     # <-- precisa de objeto user correspondente
 ...
```

Se o job falha com erro de logon, verificar:
1. Objeto `user` existe: `composer "display user=NOME"`
2. Usuário existe no SO do workstation alvo
3. Senha está atualizada no objeto

## Limpeza

```bash
echo y | composer "delete user=LABUSR_DOC"
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Job ABEND com erro de logon | Objeto user inexistente ou senha errada | Recriar/atualizar o objeto user |
| `display user` mostra `**********` | Comportamento normal (segurança) | Não há como recuperar; redefinir |
