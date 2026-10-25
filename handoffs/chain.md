# Chain

## Estado — 24/10/2026

Desenvolvimento 1.1.0+2 em `chain_app`, repositório próprio **privado** `vacilao38/chain`, branch `main`. Em 24/10/2026 o usuário pediu explicitamente essa alteração por preocupação com privacidade e proteção de dados; API do GitHub confirmou `visibility=private` e `private=true`. Exceção registrada no inventário. Não reabrir sem novo pedido explícito. Downloads 1.0 da Clustter não foram atualizados nesta sessão e continuam no repositório público de distribuição.

- Botão de copiar endereço visível em cada link, incluindo favoritos e busca. Itens estreitos usam texto + ícone abaixo do conteúdo; itens largos usam ícone lateral. Falhas da área de transferência passam pelo tratamento de erro.
- WebRTC nativo via flutter_webrtc 1.6.2+hotfix.4, com sinalização PeerServer Cloud e prioridade ao caminho direto. TCP local, protocolo AES-256-GCM, push/pull por revisão e confiança armazenada preservados. Convites novos incluem ID de internet; antigos continuam locais.
- Configuração TURN por aparelho em **Conexões → Configurar conexão entre redes**. Aceita JSON ICE ou snippet `const iceServers`, confere os destinos, exige credencial TURN e guarda via flutter_secure_storage. Não executa código nem aceita API/Secret Key administrativa. Não inclui a configuração em exportações, convites ou sincronização.
- Revisão do próprio agente corrigiu fechamento do transporte quando o primeiro envio de autenticação falha, retry após erro inicial de sinalização, tratamento de aparelho offline e escolha da rota exibida por stats WebRTC.

O usuário autorizou auxílio mínimo com P2P prioritário, PeerServer Cloud (`0.peerjs.com`: IDs/SDP/ICE/IPs) e Open Relay (`staticauth.openrelay.metered.ca`: pacotes criptografados). O endpoint público não respondeu aos testes desta rede. O usuário criou/ativou uma conta Metered e forneceu uma credencial TURN dos hosts `stun.relay.metered.ca` e `global.relay.metered.ca` para teste. **Nunca registrar a credencial em código, documentos, commits, APK ou logs.** O teste leu arquivo temporário ignorado e o removeu imediatamente; os resultados contêm somente estados e rota.

## Validação

- `flutter analyze --no-pub`: nenhum problema encontrado após implementação da configuração.
- `flutter test --no-pub --reporter expanded`: 13 testes passaram. Incluem TCP real, criptografia, cópia nos cinco tamanhos (360/390/800/844/1366), compatibilidade de convites, rejeição de configuração insegura sem ecoar segredos e fluxo de salvar a configuração em celular.
- `flutter test integration_test/internet_test.dart -d windows --no-pub --reporter expanded`, com credencial Metered autorizada: 2 cenários passaram. Automático selecionou **P2P direto · WebRTC**; relay forçado selecionou **Retransmissão TURN · criptografada**. Ambos confirmaram pareamento, push de coleção/link/capa, pull de edição e reconexão com confiança lembrada.
- O primeiro ensaio com Open Relay público falhou por timeout; TCP/TLS e UDP nos endpoints verificados não responderam nesta rede. Não usar sucesso P2P como evidência de funcionamento desse endpoint público.
- A repetição nativa final usou leitura e gravação reais via flutter_secure_storage em uma entrada temporária isolada, removida no final. Os dois cenários passaram novamente; a credencial não foi deixada na configuração de produção.
- `flutter build windows --release --no-pub`: aprovado; executável local `chain_app/build/windows/x64/runner/Release/chain.exe`, ProductVersion **1.1.0+2**. Não é publicação de download; manter DLLs e pasta data junto dele.
- Android físico e duas máquinas físicas em redes distintas ainda não validados. A preparação Android posterior desta sessão está registrada abaixo. Não houve aceite automático de novas licenças nem geração de chave substituta.

Fontes, operação e comandos detalhados em `chain_app/docs/NETWORK.md`. Capturas e resultados locais em `chain_app/artifacts/`, ignorados pelo sincronizador.

## Android preparado — 24/10/2026

O usuário pediu concluir a preparação Android. A chave local existente foi comparada ao APK 1.0 publicado: os certificados coincidem (SHA-256 público `ffe345ae284d16df6e57a7fa3646210f4cad3a52282a215aaed67c86aece1d76`). Não foi necessária outra chave. O Gradle agora valida esse certificado antes da release e recusa chave ausente/diferente. Configuração opcional `android/key.properties` é ignorada pelo Git. O teste com caminho de chave ausente falhou como esperado; após remover a configuração temporária, a chave original passou.

- Manifesto: adicionados `ACCESS_NETWORK_STATE` e `CHANGE_NETWORK_STATE` para WebRTC. Removidas permissões transitivas de Bluetooth legado/áudio. `MainActivity` desativa o gerenciamento de áudio do plugin antes de registrá-lo, pois Chain usa apenas DataChannel.
- `flutter build apk --release --split-per-abi`: aprovado. `com.clustter.chain`, minSdk 24, target/compileSdk 36, 1.1.0, códigos 1002 ARM32 / 2002 ARM64 / 4002 x64; superiores aos respectivos códigos 1.0. NDK 28.2.13676358, JDK 21 configurado pelo Flutter.
- Build com `--no-pub` falhou inicialmente pelo registrador Android obsoleto incluindo `integration_test`. Regeneração por build normal resolveu; lockfile preservado. Não editar o registrador nem executar pub get concorrente ao build. Fonte/diagnóstico em `chain_app/docs/ANDROID.md`.
- R8 ativo. APKs finais verificados por `tool/package-android.ps1`: pacote, versões por ABI, arquitetura, assinatura/certificado original, ausência de depuração/permissões de mídia e zipalign de 16 KiB. `tool/verify-apk-native.py` confirmou LOAD e RELRO de 64 bits, incluindo Flutter, JNI e WebRTC. RELRO em segmento próprio é válido mesmo sem terminar no limite de 16 KiB; regra completa da documentação Android aplicada.
- Pacotes locais e SHA-256 em `chain_app/dist/android-1.1.0+2/`; ARM64 30,5 MB, ARM32 22,8 MB, x64 35,5 MB conforme Flutter. Não incluídos no Git nem publicados no catálogo. Preferir ARM64 em celulares atuais.
- Análise final sem problemas; 13 testes Flutter passaram novamente. Sem dispositivo/emulador no ADB: instalação sobre 1.0, seletores SAF e P2P/TURN no Android físico continuam pendentes.
- Avisos de migração futura para Kotlin embutido permanecem no toolchain fixado, sem falha no build atual. Não desativar R8 nem atualizar Flutter/AGP sem rever os plugins.

O sync inicial enviou Chain/central, mas falhou no Pile ainda sem commit inicial, pertencente a outro trabalho. Ao final da preparação, Pile já apresentava branch acompanhando origin/main; executar e conferir o sync final, sem alterar código desse projeto.

## Próximo passo

Instalar o APK adequado sobre a versão 1.0, sem desinstalar/limpar dados, e validar a biblioteca e confiança preservadas em Android físico. Usar a configuração TURN pessoal em cada aparelho atualizado e testar celular/PC nas duas redes reais. Esta máquina já possui a chave original compatível; em outro PC, transferi-la por canal seguro e configurar key.properties, sem gerar substituta. A configuração TURN é pessoal por dispositivo. Downloads públicos continuam 1.0; distribuição atualizada e mudança na vitrine exigem escopo de publicação autorizado.

Executar `clustter.cmd sync` ao iniciar e terminar. Checkpoint do código não é release.

## Update e instalador Windows — 24/10/2026

Distribuição **1.1.1** publicada por pedido explícito final do usuário para concluir e subir aos repositórios e à Clustter. Release: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/chain-v1.1.1. Instalador Windows x64 `.exe`, APKs ARM64/ARM32/x64 e SHA256SUMS.txt públicos. Os cinco assets tiveram tamanho/digest SHA-256 comparado com os arquivos locais e cinco URLs HTTP 200. Versão e downloads oficiais no catálogo/feed. Fontes preservam a visibilidade registrada na central.

Update compartilhado integrado em MaterialApp.builder, dependência Git fixada em bc364d556bae449fc8dec3cf963b73b5a93abe6b. Consulta HTTPS somente de metadados; aviso dentro do app e botão abre a página oficial. Primeiro upgrade é manual para versões antigas sem o componente. Instalador por usuário, caminho/registro estáveis e preservação dos dados de suporte; sem instalação automática.

Validação: análise estática aprovada; testes 13 aprovados, além da integração nativa Windows do Update. Builds Windows Release e três APKs concluídos. Versão real Windows, versão/códigos Android por ABI, certificado original, permissão INTERNET, zipalign de 16 KiB e alinhamento nativo conferidos. Instalador compartilhado testado em instalação/substituição/desinstalação isolada, preservando arquivo extra. O teste nativo do Chain confirmou versão instalada, aviso Update e destino correto. O cliente HTTPS real leu o feed público dos cinco apps.

Pacotes locais em `chain_app/dist/1.1.1/`, ignorados pelo Git. Não sincronizar APKs/executáveis/credenciais. Próximo passo: testar atualização e uso em Android físico; não há aparelho ou emulador disponível nesta validação. Para release futura, seguir docs/UPDATE.md, preservar assinatura e anunciar só pacotes públicos verificados.

## Chain 1.2.0 e Companion — 24/10/2026

Pedido do usuário: regras de cópia com prefixo/sufixo padrão ou por hashtag, extensão para enviar link ao Chain e captura pelo Compartilhar do Android, sem navegar pela biblioteca. Implementado e publicado em https://github.com/vacilao38/clustter-cores-downloads/releases/tag/chain-v1.2.0 . Fonte Chain permanece privada. Companion tem repositório próprio público vacilao38/chain-companion e release chain-extension-v1.0.0.

Regras em menu Biblioteca → Regras de cópia: 30 regras no máximo, uma por etiqueta e um padrão, texto literal antes/depois com espaços preservados. Etiqueta ativa tem prioridade; ordem ajustável. Botão Copiar usa regra, menu Copiar apenas endereço ignora. Preferências locais, não sincronizadas/exportadas. Trilha é campo opcional compatível com arquivo v1; versões antigas podem descartá-la ao editar, atualizar os dois lados.

Android CaptureActivity ACTION_SEND/text/plain em janela própria, sem sobreposição/clipboard monitor/serviço. Reutiliza formulário/repositório Flutter. Windows: --capture abre janela compacta; chain_browser_host.exe aceita origem exata da extensão e JSON com limite, valida URL e apenas abre a revisão. O usuário confirma salvar. Host é registrado por usuário para Chrome/Edge pelo Setup; build de teste não toca esses registros. tool/prepare-browser.ps1 é obrigatório após build Windows e antes do empacotamento.

Trava por caminho/processo, lock OS entre processos, leitura sob trava, escrita atômica e commit de delta preservam inclusões externas. Editor de coleção desatualizada é rejeitado. Ao retomar, biblioteca recarrega. Corrigida a primeira chamada ShowWindow que podia herdar SW_HIDE do host nativo; abertura visível confirmada pela UI, exemplo cancelado sem salvar na biblioteca do usuário.

Validação: analyze sem problemas; 19 testes Flutter passaram; duas integrações Windows passaram (captura com biblioteca temporária e Update/versionamento). Ponte Release real rejeitou origem diferente, schema/URL inválidos e frame grande, e abriu popup visível com dados sintéticos. NSIS isolado: instalar, substituir e desinstalar, preservando arquivo extra e registros reais de navegador. APKs finais: versões, certificados originais, ABIs, INTERNET, share target, ausência de SYSTEM_ALERT_WINDOW e alinhamento 16 KiB conferidos. Quatro pacotes + checksums públicos, SHA-256/tamanhos remotos iguais aos locais e cinco URLs HTTP 200.

Limites: Android físico e fluxo completo com Companion carregado em Chrome/Edge não foram executados. Não afirmar homologação de lojas; extensão distribuída manualmente. Captura segura de UI sintética em outputs/chain-1.2-publication/captura-rapida-windows.png e tools_pool_site/dist/assets/chain-capture-1.2.png. Uma captura nativa que pegou outra janela foi descartada e não publicada. Docs: chain_app/docs/CAPTURE.md e RELEASE-1.2.md.

Próximo passo: testar Compartilhar real (YouTube/navegador, frio/quente, salvar/cancelar, teclado/rotação) no Android e carregar o ZIP no Chrome/Edge com Chain instalado. Confirmar captura completa, persistência e retorno à biblioteca. Preservar assinatura e exceção privada.
