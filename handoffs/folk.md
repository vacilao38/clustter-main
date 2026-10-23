# folk

## Estado — 23/10/2026

Repositório próprio recuperado na branch `main`. Preparação neste computador limitada a Folk, Lake, Chain e Noon; a seleção em `.local/project-selection.json` da central ignora os demais projetos e a vitrine. O inventário compartilhado e as visibilidades existentes foram preservados.

Flutter 3.44.1 e Dart 3.12.1 preparados. Consultar `../devices/521caa2563-setup.md` para as versões finais dos SDKs, os resultados da instalação e as limitações do ambiente.

## Validação

- `flutter pub get --enforce-lockfile`: código 0; `pubspec.lock` preservado.
- `flutter analyze --no-pub`: código 0; nenhum problema encontrado.
- `flutter test --no-pub --reporter expanded`: código 0; 12 testes aprovados e 1 ignorados pelo próprio projeto.
- Sincronização pela tarefa do Windows: ciclo com resultado 0, somente os quatro apps e a central. Gatilhos ao entrar no Windows e a cada três minutos conferidos.

Os resultados acima não representam build de release, validação de integrações nativas ou uso em Android físico. A migração anterior não havia reexecutado estes testes; os resultados desta seção foram executados nesta preparação.

## Próximo passo

Continuar o desenvolvimento na branch cadastrada, executando a sincronização ao iniciar e encerrar. Para atualizar APKs já instalados, transferir com segurança a chave de assinatura original; não gerar substituta. Validar o aplicativo em Android físico antes de declarar essa plataforma testada. Publicação de aplicativo, download ou alteração na vitrine depende de pedido explícito.

Modelos Whisper Base Q5 e Silero presentes. `tool/prepare-windows.ps1` concluiu com código 0 após recuperar FFmpeg/FFprobe. O SHA-256 do pacote foi conferido com o digest oficial. O teste de transcrição nativa permanece separado dos testes acima.
