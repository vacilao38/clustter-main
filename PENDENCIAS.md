# Pendências compartilhadas

Atualizar este arquivo quando surgir algo necessário para continuar em outro computador. Não registrar senhas, tokens, endereços de clientes ou dados pessoais.

- [x] Executado `install.ps1` no segundo computador com autenticação GitHub existente. Por pedido do usuário, esta máquina trabalha e sincroniza exclusivamente Folk, Lake, Chain e Noon; a central é mantida e os demais projetos e a vitrine são ignorados por seleção local.
- [x] Visibilidade definida pelo usuário: Noon público; Folk e Lake mantêm exceção privada. Em 24/10/2026, o usuário pediu tornar Chain privado por preocupação com privacidade e proteção de dados. Alteração confirmada pela API do GitHub (`private=true`) e exceção registrada em `projects.json`. Os outros projetos legados ficam privados.
- [x] Executado `clustter.cmd doctor` no início e instalados os SDKs de Folk, Lake, Chain e Noon. Preparação, análises e testes Flutter passaram nos quatro apps. O usuário encerrou testes adicionais; versões, falhas corrigidas e limites em `devices/521caa2563-setup.md`.
- [ ] Para atualizar APKs já instalados, transferir com segurança as mesmas chaves de assinatura. Os READMEs atuais descrevem assinatura de desenvolvimento; gerar uma nova chave em outro PC pode impedir atualização sobre a instalação existente. Nunca versionar essas chaves.
- [x] Chain Android 1.1 preparado em 24/10: chave local confirmada compatível com o APK 1.0; três APKs de release compilados e verificados (assinatura, versões, ABI, manifesto e alinhamento nativo). Pacotes locais não publicados. Ver `handoffs/chain.md`; permanece necessário testar atualização e sincronização no Android físico. Transferência segura da chave continua necessária em outro computador.
- [x] Modelos do Folk presentes no repositório, dependências Flutter recuperadas com lockfile preservado e FFmpeg/FFprobe preparados com SHA-256 conferido.
- [ ] Compilação e validação de integrações nativas continuam pendentes nos demais apps conforme a preparação anterior. Em 24/10 o usuário retomou o desenvolvimento do Chain: integração Windows WebRTC direto e TURN forçado passou com credencial Metered pessoal. Ver `handoffs/chain.md`; ainda falta Android físico e ensaio celular/PC nas redes reais.
- [ ] Validar uso no Android físico onde os READMEs registram essa validação pendente.

## Ao encerrar uma sessão

### Pile — 24/10/2026

- [x] Retomada após reset executada: gerenciador visual com galeria/lista, busca Cute, prévias, navegação/criação de pastas, mover/desfazer e nova marca. Fluxo oficial Android de figurinhas estáticas implementado e compilado; confirmação em WhatsApp real ainda pendente. Fontes, métricas e testes em `pile_app/docs/EVOLUCAO-VISUAL.md` e `docs/VALIDACAO.md`. Sem nova publicação ou sync global; agendamento único encerrado.
- [ ] Conectar Android com WhatsApp/Business e validar o pacote preparado, confirmação/recusa, permissões SAF, vídeo/EXIF e layout em tablet. Só então declarar a importação de figurinhas validada no dispositivo.

- [x] Novo app cadastrado em `projects.json`, com repositório próprio, dependências, comandos e `handoffs/pile.md`. Repositório privado por pedido de 24/10/2026 (risco de LGPD). Pile e downloads publicados na Clustter por autorização explícita posterior na mesma sessão.
- [x] Sincronização entre computadores dispensada expressamente pelo usuário nesta sessão. A tentativa inicial falhou por restrição de rede; a nova tentativa foi interrompida após essa instrução. Não declarar sincronizado.
- [ ] Validar Pile em Android físico (celular/tablet), principalmente permissões e operações SAF. IA real depende de chave e consentimento por lote; testes desta sessão foram locais e sintéticos.

Por pedido do usuário, a execução periódica de três minutos foi removida. Manter somente sincronização ao entrar no Windows e ao iniciar/encerrar o trabalho. Instalações antigas aplicam a migração local ao receber a atualização da central.

Atualize `handoffs/<id>.md`: resultado, validação realizada, limitações e próximo passo. Execute `clustter.cmd sync` e confira o resultado. Se houver conflito ou indisponibilidade, registre a pendência e preserve o checkpoint.
