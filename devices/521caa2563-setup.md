# Preparação do computador — 23/10/2026

## Escopo e organização

Preparação exclusiva de Folk, Lake, Chain e Noon, conforme a orientação do usuário. `clustter-main`, `folk_app`, `lake_app`, `chain_app` e `noon_app` são pastas irmãs no workspace Clustter. Os demais repositórios já recuperados foram preservados e ficam fora da sincronização e do trabalho nesta máquina. A vitrine também está fora do escopo.

A seleção está em `.local/project-selection.json`, ignorada pelo Git. O inventário compartilhado não foi reduzido e a seleção de outro computador não foi alterada. A central continua sincronizada. Os repositórios dos aplicativos permaneceram na branch `main`.

## Ferramentas

| Componente | Resultado |
| --- | --- |
| Git para Windows | 2.55.0.windows.3, instalação existente reaproveitada |
| GitHub CLI | 2.97.0, autenticação existente válida e preservada |
| Python | 3.14.6 com Tkinter, instalação do usuário reaproveitada; instalador configurado com `-PythonPath` |
| Flutter / Dart | 3.44.1 / 3.12.1, tag oficial do Flutter `924134a44c189315be2148659913dda1671cbe99` |
| Java | Eclipse Temurin 21.0.12.1+1 |
| Visual Studio C++ | Build Tools 2022, instalação 17.14.37806.7 completa; ferramentas x64/x86, CMake e Windows SDK 10.0.26100 |
| Android SDK | Command-line tools 22.0, Platform Tools, API 36 e Build Tools 36.0.0 |
| NDK | 28.2.13676358 para os padrões deste Flutter; 29.0.13113456-beta1, base 29.0.13113456 exigida pelo Folk |
| Folk | Whisper Base Q5 e Silero presentes; FFmpeg/FFprobe recuperados, com SHA-256 conferido |
| Windows | Modo de Desenvolvedor ativado após autorização específica do usuário, permitindo os links dos plugins Flutter |

As entradas existentes de ambiente e a identidade Git foram preservadas. Os caminhos locais de ferramentas e logs ficam somente na configuração deste computador. As dependências dos projetos excluídos não foram preparadas.

## Validações executadas

- `install.ps1 -PythonPath ...`: código 0; recuperação dos repositórios e configuração local concluídas. Nova execução aplicou a seleção exclusiva dos quatro apps e o Python do usuário.
- `clustter.cmd doctor`: executado no início; identificou as ferramentas ausentes. Após o pedido do usuário para encerrar os testes, não foram repetidos diagnósticos nem iniciadas novas compilações. A conclusão dos instaladores foi conferida por seus resultados e metadados.
- Testes da central: 17 aprovados, incluindo exclusão de repositórios não selecionados e rejeição segura de configurações inválidas.
- Nos quatro apps: `flutter pub get --enforce-lockfile`, `flutter analyze --no-pub` e `flutter test --no-pub --reporter expanded`, todos com código 0. Nenhum problema nas análises; todos os lockfiles preservados.

| Aplicativo | Aprovados | Ignorados pelo projeto |
| --- | ---: | ---: |
| Folk | 12 | 1 |
| Lake | 40 | 1 |
| Chain | 10 | 0 |
| Noon | 28 | 0 |

`tool/prepare-windows.ps1` do Folk terminou com código 0. As versões de FFmpeg/FFprobe foram consultadas diretamente. Os pacotes Android foram conferidos na instalação e pelas revisões dos respectivos arquivos `source.properties`. A instalação C++ foi verificada pelo `vswhere` como completa.

## Sincronização automática

A configuração inicial incluía entrada no Windows e repetição de três minutos (`PT3M`). Foi observada uma execução real do próprio Agendador com resultado 0 e registros somente de Folk, Lake, Chain, Noon e central.

Posteriormente, em 23/10/2026, o usuário pediu a remoção da execução a cada três minutos. O gatilho periódico foi removido desta máquina, preservando somente o gatilho ao entrar no Windows, sem repetição. A sincronização manual continua disponível. A tarefa foi relida após a alteração e contém somente o gatilho de entrada; ações, usuário e configurações existentes foram preservados. O instalador compartilhado não foi alterado para os demais computadores.

Nenhum push forçado, exclusão de trabalho ou resolução automática de conflitos foi realizado. Folk e Lake continuam privados; Chain e Noon continuam públicos. Nenhuma visibilidade foi alterada. Nenhum aplicativo, download, release ou alteração da vitrine foi publicado.

## Falhas encontradas e corrigidas

- A verificação inicial restrita não acessava a autenticação do Windows; fora dessa restrição, a credencial existente estava válida. Nenhum token ou senha precisou ser fornecido.
- A recuperação inicial dos plugins Flutter falhou por falta de suporte a links simbólicos. O Modo de Desenvolvedor foi ativado com autorização específica e os quatro comandos de preparação passaram na repetição.
- A primeira instalação C++ falhou ao resolver os redirecionamentos de metadados. A repetição utilizou o manifesto oficial de canal baixado localmente.
- O download inicial do FFmpeg teve conexão abortada. Um download retomável, conferido pelo digest SHA-256 oficial, concluiu a recuperação.
- A primeira tentativa de SDK Android retornou código 0 sem instalar os pacotes por falta de aceite efetivo de licenças. A repetição respondeu às licenças do instalador e a conclusão foi conferida pelos pacotes presentes, sem depender somente do código de saída.

## Pendências e próximos passos

- Transferir por canal seguro as mesmas chaves de assinatura Android do computador anterior antes de atualizar aplicativos já instalados. A chave de desenvolvimento Android não estava presente nesta máquina; nenhuma chave substituta foi gerada.
- Validar os quatro aplicativos em Android físico. Os testes executados usam o ambiente de testes Flutter e não equivalem a essa validação.
- Por pedido do usuário, as validações foram encerradas após os resultados acima. Nenhuma compilação adicional foi iniciada. Builds de release, instalação dos aplicativos, transcrição/áudio nativos e testes de integração em hardware não foram executados nesta preparação. Não há publicação autorizada.
- Para continuar, sincronizar ao iniciar, trabalhar no app escolhido, atualizar seu handoff e sincronizar ao encerrar.

Os logs completos e os detalhes específicos do computador ficam em `.local/`, fora do versionamento. Este registro não contém caminhos pessoais, credenciais, dados de aplicativos, bancos, caches ou builds.
