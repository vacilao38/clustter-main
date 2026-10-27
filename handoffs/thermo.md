# Thermo · 27/10/2026

Aplicativo novo solicitado para Windows: termômetro de reserva e consumo do Codex, com neomorfismo moderno. Fonte em `../codex_thermometer`, repositório próprio público `https://github.com/vacilao38/thermo`, branch `main`, versão `0.1.0+1`. Inventário cadastrado com dependências/comandos. Sem autorização de publicação de instaladores, downloads, catálogo ou feed.

## Entrega

- Flutter Windows com limites reais via app-server do Codex instalado: preferir rateLimitsByLimitId, janelas de duração real, percentuais restantes e contagem regressiva para renovação. Termômetro usa a janela válida com menor saldo do grupo escolhido.
- Histórico de tokens da conta hoje/sete datas e gráfico; leitura incremental de token_count neste PC, entrada/cache/saída e taxa por minuto de até 60 segundos. Fontes identificadas; ausência não vira zero. Tokens restantes da assinatura são “Não informado”, pois o contrato não oferece franquia fixa em tokens.
- Compacto, always-on-top, bandeja Win32 com retorno/menu Sair, temas claro/escuro, pausa e atualização manual/automática. Preferências locais e processo de consulta encerrado com o app. Update integrado sem incluir produto no catálogo.
- Executável e instalador local em `codex_thermometer/dist/0.1.0/Thermo-0.1.0-Windows-x64-Setup.exe`. Build e binários não são versionados. Instalação normal por usuário; teste usou pasta e registro isolados.

## Verificação

Analyze sem problemas; 13 testes unitários/widget aprovados; integração Windows com conta real aprovada, incluindo dados locais, taxa por minuto, pin/compacto/tray/show e capturas clara/escura/compacta. Release x64 compilado. Instalador/desinstalador isolados passaram, preservando arquivo extra do usuário. Contrato/fontes em docs/DESIGN.md; evidências/limites e hash em docs/VALIDATION.md. Não rodar build e integração simultaneamente no diretório CMake.

## Memória e continuidade

BMDS canônico: `codex_thermometer/memory.bmds.md`, `bmds://codex_thermometer-f2b83602a8/cell/thermo-windows-0.1.0-7dbd5ae695@1`, pilha desenvolvimento rev 1, validado. Nenhuma orgânica existente ficou obsoleta. Workspace ai-memory `default`, projeto `codex_thermometer-f2b83602a8`; serviço recusou conexão em localhost:49374, sem consulta/indexação de wiki concluída.

Sincronização inicial retornou código 128 nos repositórios sob ambiente restrito. Resultado da tentativa final deve ser conferido em `.local/status.json`; nunca usar push forçado ou declarar todos os projetos sincronizados quando houver pendência.

## Próximo passo

Usar o app durante uma sessão longa; testar em outro Windows sem SDK, Codex com outro caminho de instalação, múltiplos monitores/DPI e Narrador. Publicar distribuições ou incluir na Clustter somente após pedido explícito. Dados da conta, conversas, capturas, autenticação e contadores reais não fazem parte do repositório ou sincronizador.
