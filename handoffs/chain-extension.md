# Chain Companion 1.0.0 — 24/10/2026

Extensão solicitada pelo usuário para publicação também na Clustter. Repositório próprio público https://github.com/vacilao38/chain-companion ; checkout chain_extension. Fonte publicada em main (commit inicial 86f65bd). Distribuição: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/chain-extension-v1.0.0 . ZIP e SHA256SUMS públicos com digest/tamanho e HTTP 200 conferidos.

Manifest V3, Chrome/Edge Windows, activeTab temporária + contextMenus + nativeMessaging. Sem content scripts, cookies/histórico, captura contínua ou envio de links à rede. Ícone revisa URL/título; ação e menu contextual abrem a revisão nativa do Chain. Requer Chain 1.2.0+ instalado pelo Setup. Extensão manual: extrair ZIP em pasta permanente, modo de desenvolvedor e Carregar sem compactação. Não foi enviada a lojas. Android usa o compartilhamento do app; Firefox, mobile e outros sistemas não foram incluídos.

identity.json contém somente chave pública estável; ID emedfcknbodikopedciihmfmbdabhefe. Ponte privada do Chain aceita chrome-extension://emedfcknbodikopedciihmfmbdabhefe/ sem wildcard. JSON schema 1, framing Native Messaging até 32 KiB, URL HTTP/HTTPS sem credenciais. Resposta ok significa janela acionada; o link só é salvo após confirmação nela.

Update próprio consulta o mesmo feed público clustter.update/schema 1, entrada chain-extension/browser; avisa e abre apenas a página oficial. Não instala automaticamente. Sem rede, continua captura local. O catálogo/gerador da Clustter agora suporta plataforma browser, filtro Navegador e downloadName distinto da apresentação.

Validação: dois testes Node aprovados, validação de identidade/manifesto/ZIP e hashes. Ponte nativa real e popup Release visível confirmados no Windows; captura salva corretamente na integração do Chain com biblioteca sintética isolada. Não foi carregada a extensão no perfil real do navegador: integração completa Chrome/Edge permanece pendente. Não declarar compatibilidade validada em hardware Android ou homologação de loja.

Próximo passo: teste manual Chrome/Edge com ZIP e Setup instalados; confirmar menu, popup, coleta temporária de título/URL, cancelamento e link salvo. Para futura loja, coordenar novo ID e allowed_origins da ponte sem ampliar acesso genérico. A ponte pertence ao instalador do Chain; o ZIP da extensão não é um app Windows separado.
