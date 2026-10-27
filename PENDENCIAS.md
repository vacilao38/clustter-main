# Pendências compartilhadas

## Chain — WebSocket, 27/10/2026

- [x] Investigação Windows/Android: serviço respondeu em probe sintético; corrigidos no código timeouts/resultado tardio/reconexão e fallback TCP autenticado para convites com internetId. Análise limpa, suíte 44 testes e sete regressões de sinalização aprovadas. Ver handoff/NETWORK.md.
- [ ] Coletar mensagem completa e versões do incidente; validar em Android físico e redes reais. Não atribuir o erro a TURN sem separar a etapa de sinalização. Nenhuma nova distribuição realizada; downloads 1.3.1 mantidos.
- [ ] ai-memory indisponível nesta sessão: BMDS local do Chain gravada e validada, wiki ainda não consultada/indexada.

Atualizar este arquivo quando surgir algo necessário para continuar em outro computador. Não registrar senhas, tokens, endereços de clientes ou dados pessoais.

- [x] Executado `install.ps1` no segundo computador com autenticação GitHub existente. Por pedido do usuário, esta máquina trabalha e sincroniza exclusivamente Folk, Lake, Chain e Noon; a central é mantida e os demais projetos e a vitrine são ignorados por seleção local.
- [x] Visibilidade definida pelo usuário: Noon público; Folk e Lake mantêm exceção privada. Em 24/10/2026, o usuário pediu tornar Chain privado por preocupação com privacidade e proteção de dados. Alteração confirmada pela API do GitHub (`private=true`) e exceção registrada em `projects.json`. Os outros projetos legados ficam privados.
- [x] Executado `clustter.cmd doctor` no início e instalados os SDKs de Folk, Lake, Chain e Noon. Preparação, análises e testes Flutter passaram nos quatro apps. O usuário encerrou testes adicionais; versões, falhas corrigidas e limites em `devices/521caa2563-setup.md`.
- [ ] Para atualizar APKs já instalados, transferir com segurança as mesmas chaves de assinatura. Os READMEs atuais descrevem assinatura de desenvolvimento; gerar uma nova chave em outro PC pode impedir atualização sobre a instalação existente. Nunca versionar essas chaves.
- [x] Chain Android 1.1 preparado em 24/10: chave local confirmada compatível com o APK 1.0; três APKs de release compilados e verificados (assinatura, versões, ABI, manifesto e alinhamento nativo). Pacotes locais não publicados. Ver `handoffs/chain.md`; permanece necessário testar atualização e sincronização no Android físico. Transferência segura da chave continua necessária em outro computador.
- [x] Modelos do Folk presentes no repositório, dependências Flutter recuperadas com lockfile preservado e FFmpeg/FFprobe preparados com SHA-256 conferido.
- [ ] Compilação e validação de integrações nativas continuam pendentes nos demais apps conforme a preparação anterior. Em 24/10 o usuário retomou o desenvolvimento do Chain: integração Windows WebRTC direto e TURN forçado passou com credencial Metered pessoal. Ver `handoffs/chain.md`; ainda falta Android físico e ensaio celular/PC nas redes reais.
- [ ] Validar uso no Android físico onde os READMEs registram essa validação pendente.

## Refinamento Pile e Chain · 25/10/2026

- [x] Pile 0.3.0: etiquetas roláveis, coleções gerais preservando detalhes, movimento, regras/limpeza e gestão Android SAF. 58 testes/análise/integração Windows aprovados. Fonte privada main `75854f8`.
- [x] Chain 1.3.1: indicador/menu/rolagem refinados, 37 testes/análise/três integrações Windows aprovados. Fonte privada main `fe829b9`.
- [x] Usuário pediu publicar atualizações: duas releases com Setup/APKs/checksums, dez HTTP200/digests/tamanhos conferidos. Catálogo e feed enviados, distribuição `6219e9a` e fonte `ac04268`; Pages built e páginas/feed confirmados.
- [ ] Testar Android físico: novos fluxos SAF e Lixeira Pile, atualização preservando dados, figurinhas/WhatsApp e avaliações Chain já descritas. Sem aparelho conectado.
- [ ] Medir FPS e grandes bibliotecas em release. Outras interfaces adotarão docs/MOTION.md quando forem trabalhadas; só Pile/Chain mudaram nesta etapa.
- Sincronização global dispensada pelo usuário; handoffs mantidos localmente nesta etapa.

## Ao encerrar uma sessão

### Pile desktop — 25/10/2026

- [x] Gerenciador Windows 0.2.0 desenvolvido e compilado localmente: navegação por unidades/endereço, correção de renomeação, lote, etiquetas/busca sem acentos, ações diretas/botão direito, cópia/recorte/colar, pastas e Lixeira. 43 testes e integração Windows aprovados, análise sem problemas. Fonte privada, catálogo público anterior preservado; sem sincronização global.
- [x] Usuário confirmou skill/ponte Codex. Preparação local de prévias e skill, resposta JSON com revisão e hash, sem upload automático. Decisões/fontes/limites em `pile_app/docs/DESKTOP-2026-10-25.md`; continuidade em `handoffs/pile.md`.
- [ ] Ensaiar a primeira curadoria com lote escolhido pelo usuário e resposta real do Codex/ChatGPT; os testes usam conteúdo e respostas sintéticos. Verificar restauração pela Lixeira e unidades removíveis/rede. Futuro: transporte pelo celular, recorte entre unidades e cópia de pastas.

### Pile — 24/10/2026

- [x] Após novo pedido explícito, Pile 0.1.1 publicado com instalador Windows, APKs e checksums. Pages built, links HTTP 200 e feed conferidos; fonte do app privada. Detalhes no handoff.

- [x] Retomada após reset executada: gerenciador visual com galeria/lista, busca Cute, prévias, navegação/criação de pastas, mover/desfazer e nova marca. Fluxo oficial Android de figurinhas estáticas implementado e compilado; confirmação em WhatsApp real ainda pendente. Fontes, métricas e testes em `pile_app/docs/EVOLUCAO-VISUAL.md` e `docs/VALIDACAO.md`. Sem nova publicação ou sync global; agendamento único encerrado.
- [ ] Conectar Android com WhatsApp/Business e validar o pacote preparado, confirmação/recusa, permissões SAF, vídeo/EXIF e layout em tablet. Só então declarar a importação de figurinhas validada no dispositivo.

- [x] Novo app cadastrado em `projects.json`, com repositório próprio, dependências, comandos e `handoffs/pile.md`. Repositório privado por pedido de 24/10/2026 (risco de LGPD). Pile e downloads publicados na Clustter por autorização explícita posterior na mesma sessão.
- [x] Sincronização entre computadores dispensada expressamente pelo usuário nesta sessão. A tentativa inicial falhou por restrição de rede; a nova tentativa foi interrompida após essa instrução. Não declarar sincronizado.
- [ ] Validar Pile em Android físico (celular/tablet), principalmente permissões e operações SAF. IA real depende de chave e consentimento por lote; testes desta sessão foram locais e sintéticos.

Por pedido do usuário, a execução periódica de três minutos foi removida. Manter somente sincronização ao entrar no Windows e ao iniciar/encerrar o trabalho. Instalações antigas aplicam a migração local ao receber a atualização da central.

Atualize `handoffs/<id>.md`: resultado, validação realizada, limitações e próximo passo. Execute `clustter.cmd sync` e confira o resultado. Se houver conflito ou indisponibilidade, registre a pendência e preserve o checkpoint.

## Update e instaladores — 24/10/2026

- [x] Padrão Update documentado e integrado em Folk, Lake, Chain, Noon e Pile; pacote genérico em repositório próprio e inventário.
- [x] Análise/testes e builds Windows/Android concluídos. Os cinco instaladores `.exe` e quinze APKs foram publicados após autorização explícita final; assinaturas anteriores preservadas, hashes/tamanhos e URLs verificados. Os registros de compilação pendente anteriores são históricos e foram superados para estas versões.
- [x] Catálogo com cinco destaques/versões e feed público atualizado para Folk 1.0.1, Lake 1.2.1, Chain 1.1.1, Noon 0.1.1 e Pile 0.1.1.
- [ ] Testar upgrade sobre instalação existente e uso no Android físico. Credencial TURN entre redes continua por aparelho, fora dos pacotes e do sincronizador.
- [ ] Primeiro upgrade das versões anteriores ao Update é manual. Para futuras versões, publicar/verificar pacotes antes de mudar o feed.

## Chain 1.2 e Companion — 24/10/2026

- [x] Regras de cópia, campo de trilha, captura Android e ponte/extensão Chrome/Edge Windows implementados. Analyze, 19 testes Flutter, dois testes Node e duas integrações Windows aprovados; builds e pacotes verificados.
- [x] Chain 1.2.0 e Companion 1.0.0 publicados na Clustter por escopo solicitado; sete assets com SHA-256/tamanhos e HTTP 200 conferidos. Extensão em repositório próprio público, Chain mantém exceção privada.
- [ ] Testar Compartilhar no Android físico e fluxo completo com extensão carregada no Chrome/Edge. Distribuição manual, sem publicação em lojas.
- [ ] Para compilar Windows Chain: executar tool/prepare-browser.ps1 após o Release e antes do instalador, preservando ID público/origem exata. SDKs/chaves/builds não vão pelo sync.

## Aviso Update — correção do X

- [x] Falha reproduzida: tooltip em MaterialApp.builder sem Overlay ancestral; causava erro visual/área branca. Componente 1.0.1 corrige e oito testes passaram, incluindo hover, fechar e preservar rota/rascunho.
- [x] Chain 1.2.1+5: análise, 19 testes e integração Windows de hover/fechamento passaram. Windows/APKs compilados e verificados; cinco assets publicados e acessíveis, catálogo/feed atualizado.
- [x] Código dos outros quatro apps alinhado ao componente corrigido; resolução e análises passaram, somente clustter_update mudou nos lockfiles.
- [ ] Na próxima distribuição de Folk/Lake/Noon/Pile, incrementar versão/build e recompilar para levar a correção aos binários. Seus downloads antigos não foram republicados neste ajuste.

## Chain 1.3 — aparelhos, conflitos, movimento e sons

- [x] 1.3.0+6 implementado e publicado: apelidos locais persistentes, quatro resoluções de conflito, transições com redução de movimento e paleta sonora original opcional. Pesquisa detalhada com fontes e riscos de LLM em chain_app/docs/EXPERIENCE-RESEARCH.md.
- [x] Analyze, 35 testes Flutter e três integrações Windows passaram; Setup isolado validado, APKs/assinatura/alinhamento/permissões/sons conferidos. Cinco downloads públicos HTTP 200; Pages e feed Windows/Android 1.3.0 confirmados. Código Chain permanece privado.
- [ ] Validar em Android físico: conflitos offline nas duas redes reais, apelidos/reconexão, áudio com música, silencioso/Não Perturbe, segundo plano e redução de movimento. Agradabilidade com participantes e FPS em profile/release ainda não medidos.
- [ ] Futuro Flutter: acompanhar migração do KGP em flutter_webrtc, cujo build atual emitiu aviso; não trocar versão sem repetir integração direta/TURN e testes Android.

## Thermo — 27/10/2026

- [x] Novo aplicativo Windows de reserva/atividade do Codex; repositório próprio público `vacilao38/thermo`, inventário e handoff/thermo.md. Interface neomórfica clara/escura, compacto, sempre visível, bandeja e dados reais.
- [x] 13 testes, análise sem problemas, integração Windows/conta real, Release e instalador local. Instalação/desinstalação isoladas preservaram arquivo extra. Ajuste final MSVC UTF-8 verificado em execução; detalhes e hash em docs/VALIDATION.md do app.
- [ ] Ensaiar outro Windows sem SDK, layout diferente de instalação do Codex, DPI/múltiplos monitores e Narrador. Serviço ai-memory local indisponível; BMDS validado, sem indexação de wiki declarada.
- O aplicativo e seus downloads não foram publicados na vitrine/feed. Publicação continua dependendo de pedido explícito.
