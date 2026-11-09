# Steam Saves Sync — 09/11/2026

## Pedido e entrega

Usuário pediu script bilateral Windows/Linux para copiar/sobrescrever saves Steam e confirmou diretório compartilhado entre os sistemas. Implementação em repositório próprio `https://github.com/vacilao38/steam-save-sync`, pasta `steam_save_sync/`, branch `main`.

Script Python 3.10+ sem pacotes externos; menu e iniciadores Windows/Linux. Cadastro explícito de pasta por jogo/sistema, pasta compartilhada com identificação, envio/recebimento e sync por hashes e estado local independente. Backup completo do destino antes de sobrescrever, simulação sem escrita, conflito por conjunto do jogo, trava, preparação e verificação de integridade. Não replica exclusões. Saves, backups, configuração, identidade de memória e memória local não publicados no repositório do código.

## Validação

21 testes locais aprovados no Windows com Python 3.12.14 e dados sintéticos. Sintaxe Python 3.10 e interface de comandos verificadas. Fluxo remoto preparado para Windows/Ubuntu com Python 3.10/3.12; conferir resultado final no repositório. Não ensaiado em dual boot real ou com saves reais. WSL indisponível e Git Bash restrito no ambiente local.

Substituição atômica por arquivo; em interrupção no meio do conjunto pode ser necessária restauração manual do backup. Formatos Windows/Linux precisam ser compatíveis no próprio jogo; não há conversão nem descoberta automática dos caminhos.

## Continuidade

- Informar o caminho do diretório compartilhado em cada sistema e cadastrar os jogos e caminhos reais. Nenhum save real foi lido ou alterado.
- Antes de jogar no outro sistema, sincronizar; após jogar, sincronizar novamente, com jogo e Steam fechados. Coordenar Steam Cloud do jogo para evitar restauração externa de versão anterior.
- Código público por padrão autorizado pelo projeto; nenhuma publicação do script/downloads na vitrine Clustter foi solicitada ou feita. Ferramenta de script, sem instalador/app ou integração Update nesta entrega.
- ai-memory não disponível entre as ferramentas desta sessão; manter BMDS local validado, sem declarar consulta/indexação da wiki.
- Sync inicial da central falhou por rede (`getaddrinfo() thread failed to start`); resultado da tentativa final deve ser registrado antes de encerrar.
