# Chain

## Estado — 24/10/2026

Desenvolvimento 1.1.0+2 em `chain_app`, repositório próprio público `vacilao38/chain`, branch `main`. Downloads 1.0 da Clustter não foram atualizados nesta sessão.

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
- Android físico, duas máquinas físicas em redes distintas e atualização de APK com a assinatura original ainda não validados. SDK Android desta máquina tem licenças pendentes; não houve aceite automático nem geração de chave de assinatura substituta.

Fontes, operação e comandos detalhados em `chain_app/docs/NETWORK.md`. Capturas e resultados locais em `chain_app/artifacts/`, ignorados pelo sincronizador.

## Próximo passo

Usar a configuração TURN pessoal em cada aparelho atualizado e testar celular/PC nas duas redes reais. Para atualizar APK existente, transferir com segurança a chave de assinatura original; não gerar substituta. Validar Android físico antes de declarar a plataforma testada. A configuração atual é pessoal por dispositivo. Distribuição atualizada e mudança na vitrine exigem escopo de publicação autorizado.

Executar `clustter.cmd sync` ao iniciar e terminar. Checkpoint do código não é release.
