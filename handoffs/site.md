# site

## Estado

Código existente cadastrado para continuidade entre computadores em 23/10/2026. Repositório próprio: https://github.com/vacilao38/clustter-cores-site.

## Validação

A migração não reexecutou testes funcionais nem builds deste app. Consultar README e documentação de validação do projeto para o histórico anterior.

## Próximo passo

No outro computador, preparar as dependências de `projects.json`, executar os comandos de validação e registrar o resultado aqui antes de alterar funcionalidades.

## Pile publicado — 24/10/2026

Usuário autorizou Pile no catálogo e seus downloads, mantendo código privado por risco de LGPD. Publicação concluída: https://vacilao38.github.io/clustter-cores-downloads/#pile . Release https://github.com/vacilao38/clustter-cores-downloads/releases/tag/pile-v0.1.0 com quatro pacotes e checksums; hashes/tamanhos conferidos, cinco URLs HTTP 200. Pages built no commit 9a8120898b95f6d309aff6d5c9c6b2d2669395b4. Catálogo preserva Folk, Lake, Chain e Noon. Interface pública conferida em desktop e 390 px, sem overflow; modal/downloads funcionais e screenshot sintético carregado. Registro completo em tools_pool_site/VALIDATION.md e handoffs/pile.md. Nenhum código-fonte do Pile publicado no repositório da vitrine ou downloads.

Sincronização global dispensada pelo usuário; foram usados pushes específicos para a publicação solicitada. Próximo passo: validar Pile em Android físico/IA real antes de anunciar essas integrações como testadas. Não mudar visibilidade privada nem publicar versões novas sem autorização aplicável.

## Catálogo único e Update — 24/10/2026

Topo exibe cinco apps em cards com identidade e versão completa; até seis destaques, com lista principal extensível por catálogo. Fonte única tools_pool_site/catalog.json, gerador tool/build-catalog.mjs e runtime dist/catalog-app.js. Cada card/apresentação mostra a versão. O script antigo permanece para cache de HTML anterior.

Publicados Folk 1.0.1, Lake 1.2.1, Chain 1.1.1, Noon 0.1.1 e Pile 0.1.1, todos com instalador Windows e três APKs + hashes. Os vinte e cinco assets públicos passaram na conferência de tamanho/SHA-256 e HTTP 200. Feed updates.json clustter.update schema 1 aponta às páginas oficiais por app/plataforma. Não anunciar versão sem pacotes.

Vitrine/feeds no commit 99cff4766a63996c11c35eddd434b4852c09571a; guias atualizados em 1fa13bb05d36372b87180811543d669e86b086ea. A evolução Pile foi preservada no catálogo e no screenshot próprio. Site/JSON/JS públicos retornaram HTTP 200 e o cliente Dart real leu todas as versões finais. Layout desktop e celular conferidos sem overflow horizontal; modal mostra versão e quatro downloads. Código dos apps privados não faz parte desta distribuição.

Próximo passo: manter catálogo e feed coordenados; apps antigos precisam da primeira atualização manual. Compilar/enviar código não autoriza novo produto público.
