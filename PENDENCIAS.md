# Pendências compartilhadas

Atualizar este arquivo quando surgir algo necessário para continuar em outro computador. Não registrar senhas, tokens, endereços de clientes ou dados pessoais.

- [x] Executado `install.ps1` no segundo computador com autenticação GitHub existente. Por pedido do usuário, esta máquina trabalha e sincroniza exclusivamente Folk, Lake, Chain e Noon; a central é mantida e os demais projetos e a vitrine são ignorados por seleção local.
- [x] Visibilidade definida pelo usuário: abrir somente membros da Clustter. Chain e Noon públicos; Folk e Lake mantêm exceção privada. Os outros projetos legados ficam privados.
- [ ] Executar `clustter.cmd doctor` no segundo computador e instalar os SDKs dos projetos que serão usados. Os requisitos e comandos estão em `projects.json`.
- [ ] Para atualizar APKs já instalados, transferir com segurança as mesmas chaves de assinatura. Os READMEs atuais descrevem assinatura de desenvolvimento; gerar uma nova chave em outro PC pode impedir atualização sobre a instalação existente. Nunca versionar essas chaves.
- [x] Modelos do Folk presentes no repositório, dependências Flutter recuperadas com lockfile preservado e FFmpeg/FFprobe preparados com SHA-256 conferido.
- [ ] Compilação e validação de integrações nativas continuam pendentes. O usuário encerrou os testes após análise e testes Flutter aprovados nos quatro apps; nenhuma compilação adicional foi iniciada.
- [ ] Validar uso no Android físico onde os READMEs registram essa validação pendente.

## Ao encerrar uma sessão

Atualize `handoffs/<id>.md`: resultado, validação realizada, limitações e próximo passo. Execute `clustter.cmd sync` e confira o resultado. Se houver conflito ou indisponibilidade, registre a pendência e preserve o checkpoint.
