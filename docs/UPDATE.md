# Protocolo Update — padrão Clustter cores

Definido pelo usuário em 24/10/2026 para todos os apps novos e novas versões da família.

## Comportamento exigido

- Avisar **dentro do próprio aplicativo** quando existir versão publicada superior para a plataforma atual.
- Botão **Baixar no site** abre a página oficial do produto. Não baixar/executar instaladores automaticamente. Não há serviço de notificações com o app fechado.
- Consultar só o JSON público da Clustter; nenhuma biblioteca, projeto, arquivo, chave, conta, identificador de aparelho ou versão instalada é enviado no payload.
- Manter o aplicativo utilizável sem internet. Timeout, feed ausente, schema desconhecido e cache inválido não interrompem o trabalho. Verificar na abertura, a cada 30 minutos no app ativo e ao retornar ao app, com esse intervalo mínimo.
- Uma versão dispensada não volta a incomodar; a próxima versão superior volta a avisar. Comparar versão semântica numericamente, sem confundir códigos Android por ABI com versão comercial.

## Implementação reutilizável

Repositório `vacilao38/clustter-update`, checkout `clustter_update/`, pacote Flutter `clustter_update`. Dependência Git fixada no commit validado. Integrar `ClustterUpdate` em `MaterialApp.builder`; ler versão instalada pelo plugin package_info_plus, sem constante duplicada para comparação.

No Android, declarar `android.permission.INTERNET` no manifesto principal de Release. A permissão do manifesto de debug não vale para o APK distribuído. A preparação deve confirmar essa permissão no APK real, além de versão, ABI, assinatura e alinhamento.

O código dos apps fica em seus repositórios próprios, respeitando visibilidades e exceções de privacidade do inventário. O componente Update é genérico e não inclui dados ou implementação dos apps privados. Confira seu README e testes antes de alterar o protocolo.

Feed público: `https://vacilao38.github.io/clustter-cores-downloads/updates.json`, `protocol=clustter.update`, `schema=1`, releases por app e plataforma. Os destinos aceitos são páginas `https://vacilao38.github.io/clustter-cores-downloads/#<id>`. HTTPS normal, sem redirecionamentos, limite de 256 KiB e prazo de 8 segundos. O provedor da hospedagem recebe metadados HTTP normais, incluindo IP; não há telemetria própria.

## Windows

Todas as novas distribuições oferecem **Setup.exe**, gerado por `clustter_update/tool/build-installer.py` a partir do Release completo. Instalador por usuário, sem administrador, caminho e registro estáveis por id, atalho no menu Iniciar e desinstalador. Pedir para fechar a cópia instalada; nunca encerrar trabalho à força. Preservar projetos e preferências no diretório de suporte. Desinstalar somente arquivos conhecidos do pacote, sem apagar pastas recursivamente ou dados do usuário.

O compilador NSIS portátil vem do canal oficial e fica ignorado em `.tools/`. O pacote inclui DLLs/runtime C++ necessários. Não mudar CompanyName/ProductName/applicationId durante a migração ZIP → instalador: o diretório de suporte deve permanecer compatível. Usuários de ZIP instalam uma vez e passam a abrir pelo menu Iniciar. Um certificado digital Windows não é fornecido pelo protocolo.

## Publicação coordenada

1. Incrementar versão em pubspec.yaml e manter código de build superior ao anterior. Preservar a chave Android original.
2. Analisar e testar o app, compilar Windows Release/APKs aplicáveis e conferir versão real, assinatura, arquiteturas e dependências nativas. Gerar/testar instalador e hashes. Não publicar builds de teste.
3. Criar release de distribuição e enviar apenas pacotes, licenças e hashes autorizados. Nunca código de app privado, dados, credenciais ou cache. Conferir SHA-256 e disponibilidade dos assets antes de anunciar.
4. Atualizar `tools_pool_site/catalog.json`, fonte única de cards, versões e downloads. Rodar `node tool/build-catalog.mjs` para gerar `dist/catalog.json` e `dist/updates.json`; conferir só os produtos autorizados e pacotes existentes.
5. Publicar os arquivos estáticos no GitHub Pages do repositório de distribuição. Só então os clientes devem encontrar a versão nova no feed. Se uma plataforma ainda não estiver pronta, não anunciar uma versão inexistente para ela.
6. Conferir página, feed, links, hashes e layout mobile/desktop; registrar resultado no handoff e sincronizar código/documentação. Checkpoint no GitHub não é release.

Apps antigos que ainda não contêm Update precisam de uma primeira atualização manual. Não afirmar que eles receberão um aviso retroativo. Publicação de um aplicativo novo continua exigindo pedido explícito; o protocolo não inclui produtos automaticamente no catálogo.
