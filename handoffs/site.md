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

## Chain 1.2 + Companion — 24/10/2026

Catálogo autorizado com seis ferramentas, preservando as cinco anteriores. Chain 1.2.0: regras de cópia e captura rápida. Novo Chain Companion 1.0.0 para Chrome/Edge Windows com instalação manual, download ZIP e dependência explícita do Setup Chain 1.2+. Dois releases publicados/verificados antes do feed. Sete assets: hashes/tamanhos iguais aos locais, HTTP 200.

Site adiciona plataforma/filtro Navegador, sexto destaque e manifesto Update em apps.chain-extension.browser. Gerador aceita downloadName separado de name para nomes seguros dos assets. A imagem da extensão é a janela real de destino do Chain, identificada como tal; usa dados sintéticos do teste nativo, sem captura da conversa ou biblioteca real. Limites de validação Android e browser explícitos no catálogo/releases.

Pages built confirmado no commit 0fef21846992bf70cd9c4b72098a107b7c2f3afa. Interface pública conferida: seis destaques, filtro Navegador retorna um produto, modal Companion 1.0.0 com ZIP e SHA-256 corretos, imagem carregada. Largura efetiva 498 px sem overflow no documento ou modal (454/454). Catálogo público igual à fonte; clientes Dart/JS confirmaram Chain 1.2 e Companion 1.0 no feed. Captura pública em outputs/chain-1.2-publication/companion-publicado.png. Próximo passo: validar fluxo completo com a extensão carregada e Android físico; atualizar somente os produtos autorizados.

## Chain 1.2.1 — tooltip do aviso

Catálogo e feed anunciam Chain 1.2.1 no lugar de 1.2.0, preservando os outros cinco itens e Companion 1.0.0. Pacotes públicos verificados antes do anúncio: Setup, três APKs e hashes. Deploy enviado em 95355eb. Correção preserva rota/rascunho após hover/fechamento do X; testes do componente e Windows nativo confirmaram.

Pages built confirmado em 95355eb3e4a254f0fdd98636c8a44c572603bf80. Catálogo público igual à fonte e feed Windows/Android do Chain em 1.2.1.

## Pile 0.3.0 e Chain 1.3.1 · 25/10/2026

Usuário solicitou publicar as atualizações. Duas releases de cinco assets cada, pacotes verificados e HTTP200/checksums iguais. Catálogo/Update apenas destes produtos, capturas atuais com fixtures sintéticas, notas e limites atualizados. Fonte `ac04268`, distribuição `6219e9a`. Fonte apps continua privada; outros produtos/Companion preservados. Pages built no commit `6219e9a`; apresentações no navegador, feed e imagens conferidos. Sem sincronização global.

## Bridge 0.1.0 · 27/10/2026

Novo produto explicitamente autorizado: teclado/mouse Windows → Android local. Cinco assets públicos verificados, fonte privada. Fonte/catalog.json e JSONs gerados atualizados; somente Bridge acrescentado, seis produtos anteriores preservados integralmente. Pages built em 6b25ffeb0733354272c88e7d2b4302bd5f7b4826; catálogo público igual à fonte, Update Windows/Android em 0.1.0 e imagem HTTP 200. Modal e quatro downloads conferidos no navegador estreito. Limitações de Android físico explícitas. Prova local outputs/bridge-publication/bridge-publicado.png.
