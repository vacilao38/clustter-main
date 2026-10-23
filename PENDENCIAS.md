# Pendências compartilhadas

Atualizar este arquivo quando surgir algo necessário para continuar em outro computador. Não registrar senhas, tokens, endereços de clientes ou dados pessoais.

- [x] Executado `install.ps1` no segundo computador com autenticação GitHub existente. Por pedido do usuário, esta máquina trabalha e sincroniza exclusivamente Folk, Lake, Chain e Noon; a central é mantida e os demais projetos e a vitrine são ignorados por seleção local.
- [x] Visibilidade definida pelo usuário: abrir somente membros da Clustter. Chain e Noon públicos; Folk e Lake mantêm exceção privada. Os outros projetos legados ficam privados.
- [x] Executado `clustter.cmd doctor` no início e instalados os SDKs de Folk, Lake, Chain e Noon. Preparação, análises e testes Flutter passaram nos quatro apps. O usuário encerrou testes adicionais; versões, falhas corrigidas e limites em `devices/521caa2563-setup.md`.
- [ ] Para atualizar APKs já instalados, transferir com segurança as mesmas chaves de assinatura. Os READMEs atuais descrevem assinatura de desenvolvimento; gerar uma nova chave em outro PC pode impedir atualização sobre a instalação existente. Nunca versionar essas chaves.
- [x] Modelos do Folk presentes no repositório, dependências Flutter recuperadas com lockfile preservado e FFmpeg/FFprobe preparados com SHA-256 conferido.
- [ ] Compilação e validação de integrações nativas continuam pendentes. O usuário encerrou os testes após análise e testes Flutter aprovados nos quatro apps; nenhuma compilação adicional foi iniciada.
- [ ] Validar uso no Android físico onde os READMEs registram essa validação pendente.

## Ao encerrar uma sessão

Por pedido do usuário, a execução periódica de três minutos foi removida. Manter somente sincronização ao entrar no Windows e ao iniciar/encerrar o trabalho. Instalações antigas aplicam a migração local ao receber a atualização da central.

Atualize `handoffs/<id>.md`: resultado, validação realizada, limitações e próximo passo. Execute `clustter.cmd sync` e confira o resultado. Se houver conflito ou indisponibilidade, registre a pendência e preserve o checkpoint.
