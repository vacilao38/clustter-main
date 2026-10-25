# Pile

## Desktop 0.2.0 — 25/10/2026

Novo pedido executado: gerenciador visual Windows com navegação por endereço/unidades/pasta acima, leitura de cada pasta visitada e catálogo local por unidade, sem varredura global automática. Migração única dos índices antigos preserva etiquetas/coleções/capas, preferências, regras com escopo e último diário. Corrigido o bug de renomear na raiz (`./nome.ext` recusado); renomeação em lote (numeração/substituição/prefixo), busca sem acentos e por nomes anteriores, atalhos de etiquetas, menu de botão direito, abrir/revelar direto na prévia, copiar/recortar/colar, renomear pastas e Lixeira nativa. Bytes das imagens preservados; operações com plano/diário/desfazer. Recuperação ambígua de cópia exige conferência manual, sem assumir autoria de arquivo preexistente.

Usuário confirmou **skill/ponte para o Codex**, sem banco SQL. Preparar 1–200 prévias sem EXIF/GPS e nomes pessoais, skill por lote em `.agents/skills/pile-image-curator/SKILL.md`, pedido copiado e resposta JSON importada/revisada. Mapa privado/hashes ficam no suporte do app. IDs/schema/hash validados, propostas inicialmente desmarcadas, edição individual e plano antes de aplicar. Não existe upload/login ou abertura automática de sessão do Codex. O contrato pode servir a outro assistente com visão; transporte/interface no celular fica para etapa futura.

Validação: análise final sem problemas, **43 testes aprovados**, integração Windows nativa aprovada (botão direito/renomear, cópia+SHA-256, IFileOperation ao desfazer cópia, pasta renomeada/desfeita, lote com resposta sintética e prévia). Skill validada pelo validador oficial. Windows release **0.2.0+3** compilado. Capturas inspecionadas em `pile_app/.local/desktop-2026-10-25/`. Fontes, decisões assumidas/confirmadas, revisão crítica e limites em `pile_app/docs/DESKTOP-2026-10-25.md` e `docs/VALIDACAO.md`.

Nenhum arquivo pessoal processado e nenhuma IA autenticada chamada: a resposta JSON usada nos testes é fixture. Sem novo APK/teste Android/WhatsApp, sem alteração de outros apps, sincronização global ou nova publicação do catálogo/release. Público permanece 0.1.1, fonte privada. Próximo ensaio concreto: preparar uma seleção escolhida pelo usuário, abrir o lote no Codex, obter resposta de visão real e revisar/importar; testar restauração manual da Lixeira e unidades removíveis/rede antes de ampliar garantias. Recorte entre unidades, cópia de pastas e arrastar/soltar não implementados.

Instalador local final: `pile_app/dist/0.2.0/Pile-0.2.0-Windows-x64-Setup.exe`, 12.357.410 bytes, SHA-256 `eee2276a119ecdab6747c5e8d016e2001d53d02bc955fcebf9b12af39e94ca70`. Variante Test aprovada em instalação/desinstalação isoladas, executável idêntico ao Release e arquivo extra preservado. Provas sintéticas copiadas para `outputs/pile-desktop-2026-10-25/`. Branch de revisão do app: `codex/pile-desktop-curadoria`; a principal publicada foi preservada.

Fonte enviada ao repositório privado na branch acima: commit `b9675ba` (`feat: expande gerenciador Windows e adiciona curadoria por skill Codex`). Privacidade confirmada pela API (`isPrivate=true`). A central recebe estes registros em commit local, sem push/sincronização global nesta etapa.

Revisão automática recusou remover a proteção de abertura de executáveis/tipos desconhecidos por ampliar execução além do pedido explícito; salvaguarda mantida, sem contorno. Imagens e tipos suportados abrem diretamente. Não há aprovação pendente para os fluxos implementados.

## Publicação Pile 0.1.1 — 24/10/2026

Nova autorização explícita do usuário: “suba no clustter e no repositório”. A evolução visual está publicada em https://vacilao38.github.io/clustter-cores-downloads/#pile ; release https://github.com/vacilao38/clustter-cores-downloads/releases/tag/pile-v0.1.1 . Windows Setup (11,7 MiB), APKs ARM64 (20,6 MiB), ARM32 (18,4 MiB), x64 (22,0 MiB) e SHA256SUMS.txt públicos, tamanhos/digests SHA-256 locais e remotos iguais e cinco links HTTP 200. Certificado Android igual ao 0.1.0. Instalador testado em pasta/registro isolados, preservando um arquivo sintético extra na desinstalação. Não foi instalada uma cópia de produção neste usuário.

Pages confirmou built em `99cff4766a63996c11c35eddd434b4852c09571a`. Feed anuncia Pile 0.1.1 em Windows/Android. Página real conferida no navegador: versão, galeria sintética atual, instalador/APKs e limites da integração WhatsApp. Prova em `outputs/pile-evolution-2026-10-24/pile-0.1.1-publicado.png`. O código do Pile permanece privado; não foi executado sync global. Android físico/SAF e adição real ao WhatsApp/Business continuam pendentes e divulgados publicamente.

Houve publicação concorrente de versões de outros apps por outra execução. Seus pacotes públicos foram preservados; esta execução preparou e enviou somente pacotes do Pile. O catálogo público e a fonte foram conferidos iguais ao final. Uma release de rascunho homônima de Pile criada por outra execução não foi publicada nem excluída por esta etapa; a release pública e os cinco links corretos foram verificados.


## Evolução retomada após o reset — 24/10/2026

Código salvo e enviado ao repositório privado: `88ae918284a8f686635ae5c4fc989ee06d8919c5`; HEAD remoto conferido igual ao local, árvore do Pile limpa. Capturas e medições também copiadas para `outputs/pile-evolution-2026-10-24/`. Builds locais finais Windows/Android aprovados. A central recebeu somente commits locais destes registros, sem sincronização global.

Pedido executado após 16h47 São Paulo. Galeria/lista com seleção e filtros, busca por nomes/caminhos/etiquetas (Cute validado após reiniciar), índice em memória, navegação por pastas inclusive vazias, criar pasta no contexto, mover/renomear com prévia e desfazer, prévia com zoom e vídeo local. Ações compactas, ícones Lucide leves, marca de pasta/pilha. IA secundária e opcional preservada. Código privado confirmado pela API. Nada desta evolução foi publicado no catálogo/release, e não houve sync global.

Figurinhas: revisão de 3–30 imagens estáticas, WebP/capa convertidos no Android, até dez pacotes privados, ContentProvider/intent oficiais para WhatsApp/Business. Só a ação Adicionar autoriza expor o pacote. Sem leitura de conversas/credenciais/bancos privados. Confirmação real ainda pendente por ausência de Android conectado/AVD. Windows só revisa, sem alegar importação. Vídeos/animações e edição/remoção de pacotes não implementados.

Validação: análise sem problemas, 32 testes; integrações Windows de organizar/desfazer e galeria/mídia/criar pasta/mover preservando tags passaram separadamente. O runner falhou ao iniciar o segundo teste em execução conjunta; execução separada corrigiu o bloqueio de inicialização. Builds locais Windows e APKs por ABI. Capturas 360/800/1440 e prévias em `pile_app/.local/design/`. Busca 10 mil entradas: 2.51 ms/consulta média em debug, índice 125.56 ms; não é benchmark Android ou 10 mil imagens físicas. Miniatura fria 391.40 ms, cache 0.159 ms. Ver `pile_app/docs/EVOLUCAO-VISUAL.md` e `docs/VALIDACAO.md` para fontes e limites.

Integração Update e metadados 0.1.1+2 já estavam no workspace antes da retomada: preservados e validados juntos. Outras alterações da central não pertencem a esta etapa e devem permanecer fora do seu commit. Automação única `retomar-evolu-o-do-pile-ap-s-o-reset` encerrada; não duplicar/reativar. Próximo passo necessário: conectar Android com WhatsApp/Business e validar SAF, recusa/adição do pacote, vídeo/EXIF e tablet. Futuro gerenciador: copiar, lixeira e gestão de pastas/pacotes ainda não cobertos. Não anunciar substituição integral do Explorer.

App em `pile_app/`, repositório próprio **privado** https://github.com/vacilao38/pile, branch `main`. Exceção privada solicitada explicitamente pelo usuário em 24/10/2026 por risco de LGPD, registrada em projects.json. O usuário também autorizou a publicação do aplicativo e dos downloads na Clustter na mesma data.

## Implementado e validado

Flutter 3.44.1 / Dart 3.12.1: Windows 10/11 x64 e Android 7+ (celular/tablet). Organização por categorias, nomes customizáveis, prévia/opção de um clique, diário e desfazer sem sobrescrita; coleções/etiquetas/capas/temas; EXIF por ano/coordenadas; regras sob demanda; duplicados por SHA-256 e semelhança visual separada. Cópias ficam em Revisar duplicados, fora da reorganização/análises posteriores, sem exclusão automática.

Windows usa MoveFileW; Android usa ponte Kotlin SAF com cópia verificada antes de remover origem. Índice local, sem telemetria/backend. IA opcional OpenRouter por lote autorizado: modelos :free de visão revalidados, chave em memória, miniaturas sem EXIF e sugestões revisadas antes de aplicar. Etiquetas residem no índice e não acompanham movimentos externos. Regras contam dias desde detecção e rodam sob demanda.

Análise estática sem problemas, 27 testes de domínio/IO/widgets e 1 integração Windows aprovados. Layouts 360/800/1440 px com texto 1,4. Builds Windows release e Android release por arquitetura gerados; Windows ZIP 13,4 MiB, APK ARM64 18,2 MiB. Runtime C++ acompanha ZIP; APKs têm assinatura de desenvolvimento. Sem aparelho ou AVD disponível: SAF em celular/tablet físico e LLM autenticada permanecem pendentes.

## Publicação autorizada

- Vitrine: https://vacilao38.github.io/clustter-cores-downloads/#pile
- Release pública: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/pile-v0.1.0
- Quatro pacotes e SHA256SUMS.txt publicados; tamanhos e hashes remotos comparados aos locais. Cinco links HTTP 200.
- Catálogo de cinco apps preserva Folk, Lake, Chain e Noon. Captura da interface contém somente arquivos sintéticos. Limites e riscos da IA aparecem na apresentação pública.
- Código-fonte, dados de uso, credenciais e índices não fazem parte da publicação. Fontes/validação em README.md e docs/ do app. Assets de distribuição em outputs/clustter-pile-publication (fora do repositório do app).

## Próximo passo

Validar SAF em celular e tablet reais (concessão/recusa, acesso persistente, cópia/desfazer, rotação/interrupção) e testar IA com chave e lote sintético autorizado. Medir desempenho em bibliotecas maiores e definir assinatura de distribuição para versões futuras. Build Android após testes deve regenerar configuração pelo comando normal flutter build apk --release --split-per-abi; evitar --no-pub e comandos Flutter concorrentes.

Sincronização global dispensada pelo usuário nesta sessão. Este chat não iniciou novo sync após a dispensa; foram observados checkpoints de outra execução da central, cujo agendamento não foi alterado. Pushes de publicação dos repositórios do Pile, catálogo e downloads pertencem ao pedido explícito de entrega/publicação.

## Update e instalador Windows — 24/10/2026

Distribuição **0.1.1** publicada por pedido explícito final do usuário para concluir e subir aos repositórios e à Clustter. Release: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/pile-v0.1.1. Instalador Windows x64 `.exe`, APKs ARM64/ARM32/x64 e SHA256SUMS.txt públicos. Os cinco assets tiveram tamanho/digest SHA-256 comparado com os arquivos locais e cinco URLs HTTP 200. Versão e downloads oficiais no catálogo/feed. Fontes preservam a visibilidade registrada na central.

Update compartilhado integrado em MaterialApp.builder, dependência Git fixada em bc364d556bae449fc8dec3cf963b73b5a93abe6b. Consulta HTTPS somente de metadados; aviso dentro do app e botão abre a página oficial. Primeiro upgrade é manual para versões antigas sem o componente. Instalador por usuário, caminho/registro estáveis e preservação dos dados de suporte; sem instalação automática.

Validação: análise estática aprovada; testes 27 testes nesta integração; a evolução visual posterior registra 32 testes e duas integrações em docs/VALIDACAO.md. Builds Windows Release e três APKs concluídos. Versão real Windows, versão/códigos Android por ABI, certificado original, permissão INTERNET, zipalign de 16 KiB e alinhamento nativo conferidos. Instalador compartilhado testado em instalação/substituição/desinstalação isolada, preservando arquivo extra. O teste nativo do Chain confirmou versão instalada, aviso Update e destino correto. O cliente HTTPS real leu o feed público dos cinco apps.

Pacotes locais em `pile_app/dist/0.1.1/`, ignorados pelo Git. Não sincronizar APKs/executáveis/credenciais. Próximo passo: testar atualização e uso em Android físico; não há aparelho ou emulador disponível nesta validação. Para release futura, seguir docs/UPDATE.md, preservar assinatura e anunciar só pacotes públicos verificados.

## Update — correção de tooltip preparada no código

Dependência e lockfile migrados para clustter_update 1.0.1, ref 4f518a8e884bf0bbc2e83acb0d95c4e3ad2bcce7. Corrige falta de Overlay no aviso em MaterialApp.builder; regressão compartilhada reproduziu erro antes e passou depois (hover no X, fechar, rota/rascunho preservados). Nenhum binário novo deste app foi publicado neste ajuste: versão pública e feed permanecem anteriores. Incrementar versão/build e recompilar antes de distribuir a correção neste app.

Resolução de dependências e flutter analyze --no-pub passaram após alinhar o Update; apenas o pacote compartilhado mudou no lockfile. Binário público anterior preservado.
