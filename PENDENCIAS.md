# Pendências compartilhadas

Atualizar este arquivo quando surgir algo necessário para continuar em outro computador. Não registrar senhas, tokens, endereços de clientes ou dados pessoais.

- [ ] Executar `install.ps1` no segundo computador e autenticar o GitHub para acesso aos repositórios privados.
- [x] Visibilidade definida pelo usuário: abrir somente membros da Clustter. Chain e Noon públicos; Folk e Lake mantêm exceção privada. Os outros projetos legados ficam privados.
- [ ] Executar `clustter.cmd doctor` no segundo computador e instalar os SDKs dos projetos que serão usados. Os requisitos e comandos estão em `projects.json`.
- [ ] Para atualizar APKs já instalados, transferir com segurança as mesmas chaves de assinatura. Os READMEs atuais descrevem assinatura de desenvolvimento; gerar uma nova chave em outro PC pode impedir atualização sobre a instalação existente. Nunca versionar essas chaves.
- [ ] Para compilar Folk, recuperar os modelos e bibliotecas nativas conforme o README do próprio repositório; a central não transporta os arquivos grandes.
- [ ] Validar uso no Android físico onde os READMEs registram essa validação pendente.

## Ao encerrar uma sessão

Atualize `handoffs/<id>.md`: resultado, validação realizada, limitações e próximo passo. Execute `clustter.cmd sync` e confira o resultado. Se houver conflito ou indisponibilidade, registre a pendência e preserve o checkpoint.
