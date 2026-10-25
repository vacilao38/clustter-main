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

## Chain 1.2.1 — aviso de atualização

Correção solicitada pelo usuário: ao passar mouse no X, o aviso causava erro visual/área branca. Causa confirmada por reprodução: tooltip do banner inserido em MaterialApp.builder sem Overlay ancestral, acima do Navigator. Update 1.0.1 usa Overlay.wrap estável, preservando o Navigator e a tela atual. Ref 4f518a8e884bf0bbc2e83acb0d95c4e3ad2bcce7, versão app 1.2.1+5, About alinhado.

Validação: reprodução falhou antes e passou depois; oito testes do componente e 19 do Chain aprovados, analyze sem problemas. Integração Windows confirmou PackageInfo 1.2.1, tooltip ao hover, abertura da página, fechamento e trabalho local preservado, usando MaterialApp.builder igual à produção. Pacotes/continuidade da publicação registrados abaixo ao concluir.

Distribuição concluída: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/chain-v1.2.1 . Instalador x64 e três APKs + SHA256SUMS públicos; digests/tamanhos de upload comparados aos locais, cinco URLs HTTP 200. AOT de cada ABI diferente de 1.2.0 confirmado; certificado original, versões/códigos, zipalign e alinhamento nativo aprovados. Companion 1.0.0 mantido. Catálogo/feed atualizados no commit 95355eb. Uso em Android físico continua pendente.

## Chain 1.3.0 — aparelhos, conflitos e experiência

Pedido do usuário: nomear aparelhos já conectados, resolver divergências de envio/puxar, melhorar movimento com referência Apple e pesquisar sons “cream”, fóruns e falhas de implementações por LLM. Implementado em 1.3.0+6, fonte enviada no commit 0b41116. Privacidade do repositório vacilao38/chain confirmada pela API; nenhuma alteração de visibilidade. Pesquisa detalhada em chain_app/docs/EXPERIENCE-RESEARCH.md, fontes primárias Apple/Google/Microsoft/NNG/Flutter/Android, relatos qualitativos de fóruns e estudo USENIX sobre pacotes inventados. Não extrapolar o estudo para taxas de erros Flutter/animação.

Apelidos são locais, persistem na reconexão e não mudam a chave/identidade. Conexões permite renomear o conectado e os demais na lista. Metadados de conflito opcionais mantêm compatibilidade com arquivo v1. Central de revisão oferece manter ambas (padrão), usar daqui, usar outra ou combinar com escolhas por conteúdo e aparência. Transação verifica as duas revisões e recarrega dados ao detectar formulário antigo. Nova revisão reconhece as duas pontas; trocas repetidas não multiplicam cópias próprias nem ressuscitam cópias intactas reconhecidas. Cópias editadas depois são preservadas. Exclusões não se propagam; combinação é união, não merge de três vias; histórico limitado a 64 revisões. Resolver não envia automaticamente.

Movimento: troca de conteúdo 180/120 ms, curva discreta, conteúdo de saída sem cliques/foco/semântica. Sistema de redução de movimento tem prioridade; tipos estáveis preservam rascunhos ao mudar preferência. Sons originais curtos (85–220 ms) gerados por tool/generate-ui-sounds.py, sem assets Apple. Mestre desligado por padrão, navegação/cópia adicionais, volume/prévias, sem hover/fila de sons. Preferências em chain-experience-v1.json, locais. Windows usa audioplayers 6.8.1; Android SoundPool via UiSoundBridge nas duas Activities, sem foco/roteamento global ou MODIFY_AUDIO_SETTINGS. Erros de áudio não desfazem operações. Não afirmar agradabilidade universal, teste de participantes ou FPS medido.

Validação: analyze sem problemas, 35 testes Flutter e três integrações Windows aprovados. Testes incluem TCP autenticado com apelido e reconexão, quatro resoluções, repetição de trocas, colisões, revisão antiga e cópia editada, persistência real, áudio cancelado/desligado e formulários em 360 px com texto 1,4. Windows nativo usou biblioteca temporária e plugin de áudio real; fotos sintéticas em artifacts/experience-*.png. Runner falhou ao reiniciar alvos separados; usar comando único flutter test integration_test/native_regression_test.dart -d windows, registrado no inventário.

Windows Release e ponte Companion compilados. Setup por usuário gerado; variante isolada instalada/substituída/desinstalada com hashes de executável/plugin/ponte/WAV conferidos e arquivo sintético extra preservado; não publicada. Três APKs com versões/códigos, certificado original, INTERNET, share target e alinhamento ZIP/ELF 16 KiB conferidos. Sem microfone, câmera, overlay, Bluetooth ou MODIFY_AUDIO_SETTINGS. WAVs sem compressão no APK; AOTs diferentes de 1.2.1 por ABI. Nenhum dispositivo adb disponível. Aviso de futura migração KGP do flutter_webrtc registrado; build atual passou, não atualizar dependência sem nova validação de rede.

Publicação: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/chain-v1.3.0 . Setup x64, APKs ARM64/ARM32/x64 e SHA256SUMS: upload com digest/tamanho comparados, cinco URLs HTTP 200 e checksums baixados iguais aos locais. Fonte do catálogo 45e9ed7; Pages built no commit e0eeafe0e318a7c1dd99a428cd1d5ba9d10149a1. Página real no navegador mostra 1.3.0, novos recursos e quatro downloads; feed Windows/Android 1.3.0 confirmado. Folk/Lake/Noon/Pile/Companion preservados. Provas e auditorias locais em outputs/chain-1.3-publication e dist/1.3.0, ignorados pelo Git.

Próximo passo: testar update sobre Android físico e fluxo completo celular/PC em redes diferentes. Exercitar renomear/reconectar, duas edições offline, quatro escolhas e envio/puxar após resolver; verificar fones/alto-falante, música, silencioso/Não Perturbe, segundo plano, toque rápido, teclado, escala de fonte e redução de movimento. Avaliar sensação sonora com pessoas e medir frames em profile/release antes de prometer desempenho. Preservar assinatura, dados e exceção privada. Sincronização final registrada ao concluir.
