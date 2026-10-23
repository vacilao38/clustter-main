# Clustter: trabalho entre computadores

- Usar UTF-8 em código e documentação.
- Esta central contém inventário, instruções, pendências e o sincronizador; código de aplicativos fica nos respectivos repositórios.
- Antes de trabalhar: executar `clustter.cmd sync`, ler `PENDENCIAS.md` e o handoff do projeto. Conferir `.local/status.json` se algum repositório falhar.
- Depois de trabalhar: atualizar `handoffs/<id>.md` com resultado, testes e próximo passo; executar `clustter.cmd sync`. Não declarar sincronizado se o comando falhar.
- Novos apps/ferramentas da Clustter: repositório próprio público por padrão, salvo motivo de privacidade explicitamente registrado em `projects.json`. Projetos fora da família não têm abertura pública autorizada. Não mudar automaticamente a visibilidade de repositórios existentes.
- Cadastrar todo projeto em `projects.json` com URL, pasta relativa, branch de continuidade, requisitos e comandos. A pasta é relativa ao workspace, nunca a um usuário do Windows.
- Durante o uso simples nos dois PCs, trabalhar na branch de continuidade cadastrada. Outras branches não são trocadas automaticamente; publicar a branch e atualizar o inventário se a continuidade passar a ocorrer nela.
- Checkpoints automáticos podem conter trabalho incompleto; não equivalem a teste, release ou aprovação. Registrar validação no handoff.
- Nunca usar `push --force`, apagar alterações, escolher um lado de conflito automaticamente ou sincronizar diretórios de dados/segredos. Conflitos mantêm o checkpoint local e tentam salvar uma branch remota de resgate.
- Não incluir novos produtos na vitrine nem publicar instaladores sem pedido explícito. Repositório público de código e publicação no catálogo são decisões distintas.
- O sincronizador ignora o repositório legado que contém a pasta inteira. Não adicionar apps como cópias de código à central.
- Banco local, biblioteca dos apps e chats do Codex não são transportados por este mecanismo. Chaves de assinatura existentes devem ser transferidas por canal seguro para manter atualizações Android compatíveis.
