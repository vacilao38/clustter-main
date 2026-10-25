# noon

## Estado — 23/10/2026

Repositório próprio recuperado na branch `main`. Preparação neste computador limitada a Folk, Lake, Chain e Noon; a seleção em `.local/project-selection.json` da central ignora os demais projetos e a vitrine. O inventário compartilhado e as visibilidades existentes foram preservados.

Flutter 3.44.1 e Dart 3.12.1 preparados. Consultar o [registro de preparação](../devices/521caa2563-setup.md) para as versões finais dos SDKs, os resultados da instalação e as limitações do ambiente.

## Validação

- `flutter pub get --enforce-lockfile`: código 0; `pubspec.lock` preservado.
- `flutter analyze --no-pub`: código 0; nenhum problema encontrado.
- `flutter test --no-pub --reporter expanded`: código 0; 28 testes aprovados e 0 ignorados pelo próprio projeto.
- Sincronização pela tarefa do Windows: ciclo com resultado 0, somente os quatro apps e a central. Depois, a repetição de três minutos foi removida desta máquina por pedido do usuário; permanece somente a execução ao entrar no Windows, além da sincronização manual.

Os resultados acima não representam build de release, validação de integrações nativas ou uso em Android físico. A migração anterior não havia reexecutado estes testes; os resultados desta seção foram executados nesta preparação. Após estes resultados, o usuário pediu para encerrar os testes; nenhuma compilação adicional foi iniciada.

## Próximo passo

Continuar o desenvolvimento na branch cadastrada, executando a sincronização ao iniciar e encerrar. Para atualizar APKs já instalados, transferir com segurança a chave de assinatura original; não gerar substituta. Validar o aplicativo em Android físico antes de declarar essa plataforma testada. Publicação de aplicativo, download ou alteração na vitrine depende de pedido explícito.

## Update e instalador Windows — 24/10/2026

Distribuição **0.1.1** publicada por pedido explícito final do usuário para concluir e subir aos repositórios e à Clustter. Release: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/noon-v0.1.1. Instalador Windows x64 `.exe`, APKs ARM64/ARM32/x64 e SHA256SUMS.txt públicos. Os cinco assets tiveram tamanho/digest SHA-256 comparado com os arquivos locais e cinco URLs HTTP 200. Versão e downloads oficiais no catálogo/feed. Fontes preservam a visibilidade registrada na central.

Update compartilhado integrado em MaterialApp.builder, dependência Git fixada em bc364d556bae449fc8dec3cf963b73b5a93abe6b. Consulta HTTPS somente de metadados; aviso dentro do app e botão abre a página oficial. Primeiro upgrade é manual para versões antigas sem o componente. Instalador por usuário, caminho/registro estáveis e preservação dos dados de suporte; sem instalação automática.

Validação: análise estática aprovada; testes 28 aprovados. Builds Windows Release e três APKs concluídos. Versão real Windows, versão/códigos Android por ABI, certificado original, permissão INTERNET, zipalign de 16 KiB e alinhamento nativo conferidos. Instalador compartilhado testado em instalação/substituição/desinstalação isolada, preservando arquivo extra. O teste nativo do Chain confirmou versão instalada, aviso Update e destino correto. O cliente HTTPS real leu o feed público dos cinco apps.

Pacotes locais em `noon_app/dist/0.1.1/`, ignorados pelo Git. Não sincronizar APKs/executáveis/credenciais. Próximo passo: testar atualização e uso em Android físico; não há aparelho ou emulador disponível nesta validação. Para release futura, seguir docs/UPDATE.md, preservar assinatura e anunciar só pacotes públicos verificados.

## Update — correção de tooltip preparada no código

Dependência e lockfile migrados para clustter_update 1.0.1, ref 4f518a8e884bf0bbc2e83acb0d95c4e3ad2bcce7. Corrige falta de Overlay no aviso em MaterialApp.builder; regressão compartilhada reproduziu erro antes e passou depois (hover no X, fechar, rota/rascunho preservados). Nenhum binário novo deste app foi publicado neste ajuste: versão pública e feed permanecem anteriores. Incrementar versão/build e recompilar antes de distribuir a correção neste app.

Resolução de dependências e flutter analyze --no-pub passaram após alinhar o Update; apenas o pacote compartilhado mudou no lockfile. Binário público anterior preservado.
