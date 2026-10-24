# Update — 24/10/2026

Componente genérico no repositório público https://github.com/vacilao38/clustter-update, checkout clustter_update. Integrado em Folk 1.0.1, Lake 1.2.1, Chain 1.1.1, Noon 0.1.1 e Pile 0.1.1; o código runtime usa commit fixo bc364d556bae449fc8dec3cf963b73b5a93abe6b. Ferramentas posteriores ficam no main, sem alterar esse runtime.

Protocolo clustter.update schema 1: consulta HTTPS ao feed da Clustter, versão semântica e plataforma, aviso em MaterialApp.builder e download pela página oficial. Verifica abertura/retorno e intervalo de 30 minutos com app ativo. Sem conta, telemetria própria, atualização automática ou aviso com app fechado. Dismissal persiste por versão; erro de rede/cache não bloqueia trabalho. Valida destino exato, não segue redirect, limita resposta 256 KiB e timeout de 8 segundos. Bibliotecas locais não são enviadas.

Instalador NSIS por usuário, sem administrador, atalho e desinstalador; registro/caminho estáveis e preservação de suporte/dados desconhecidos. Tool verifica versão real do exe e inclui CRT. APK tool confirma versão, ABI, assinatura original, INTERNET e zipalign. SDK/NSIS/chaves e pacotes ficam fora do Git.

Validação: flutter analyze sem problemas, sete testes compartilhados aprovados; integração nativa Windows no Chain passou. Smoke do instalador de teste isolado confirmou instalação, substituição e desinstalação preservando arquivo extra. Cinco builds Windows e quinze APKs preparados; cert/versão/ABI/permissão/alinhamento conferidos. Teste do cliente HTTPS real confirmou as dez entradas do feed público. Android físico permanece pendente.

Usuário autorizou explicitamente terminar e publicar após bloqueio inicial da revisão automática. Cinco releases foram publicados no repositório clustter-cores-downloads; vinte e cinco assets com hashes/tamanhos e HTTP 200 verificados. Catálogo anuncia só essas versões públicas. Padrão obrigatório de novos apps em AGENTS.md e docs/UPDATE.md.

Próximo passo: validar upgrade em Android físico. Para novo app, integrar componente, usar repositório próprio e instalador estável; inclusão na vitrine exige autorização explícita. Para próxima release, testar pacotes, publicar/verificar e só então mudar catálogo/feed. A primeira atualização de versões antigas é manual.
