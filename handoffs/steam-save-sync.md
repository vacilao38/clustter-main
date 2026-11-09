# Steam Saves Sync — 09/11/2026

## Atualização 1.1.0 — qualquer jogo e caminhos por item

Novo pedido do usuário: selecionar saves de outros jogos/plataformas, incluindo jogos sem plataforma, e escolher o caminho de cada item. Implementado em `ca2c0f4`, enviado à `main` pública.

- Itens com nome livre, plataforma/launcher como rótulo opcional, tipo pasta inteira ou arquivo individual e caminho próprio Windows/Linux.
- Menu para listar/editar itens, selecionar vários por número e procurar arquivos/pastas pelo seletor Tkinter opcional (`?`); alternativa de caminho digitado. Comandos `listar`, `editar`, `adicionar --nome --plataforma --tipo --windows --linux` e múltiplos IDs nos comandos de cópia/simulação.
- Arquivos individuais podem ter nomes locais diferentes e não copiam seus vizinhos. Backup integral, conflitos por item, hashes, ausência de propagação de exclusões e recusa de tipo divergente preservados.
- Cadastro versão 1 lido sem alterações; gravação de edição/configuração migra para versão 2 sem mover saves, IDs ou backups. Atualizar scripts nos dois sistemas antes de editar o cadastro. Simulação/listagem não migram.
- 44 testes locais passaram no Windows com Python 3.12.14; sintaxe Python 3.10 e ajuda da CLI verificadas. A suíte de 44 testes e ajuda CLI foram aprovadas nos quatro ambientes remotos Windows/Ubuntu com Python 3.10/3.12: https://github.com/vacilao38/steam-save-sync/actions/runs/42668843840.
- Diálogo gráfico real, dual boot e saves reais não ensaiados. Dados usados nos testes são sintéticos; arquivos pessoais permanecem intocados. Registro na vitrine não solicitado.

Próximo passo: atualizar a cópia do script nos dois sistemas; cadastrar/editar itens e seus caminhos. Usar opções 2 (cadastrar), 8 (editar), 7 (listar), 3/4 (selecionar itens e simular/sincronizar).

Pacote local: `outputs/steam-save-sync/SavesSync-1.1.0.zip`, sem configuração, memória ou saves pessoais. BMDS local: `steam_save_sync/memory.bmds.md`, `bmds://steam_save_sync-1307c24e60/cell/memoria-1712909b9e@1`, validação aprovada. ai-memory indisponível entre as ferramentas; wiki não consultada/indexada. Sync inicial desta etapa falhou por restrição de rede; executar a tentativa final com rede após estes registros.

## Pedido e entrega

Usuário pediu script bilateral Windows/Linux para copiar/sobrescrever saves Steam e confirmou diretório compartilhado entre os sistemas. Implementação em repositório próprio `https://github.com/vacilao38/steam-save-sync`, pasta `steam_save_sync/`, branch `main`.

Script Python 3.10+ sem pacotes externos; menu e iniciadores Windows/Linux. Cadastro explícito de pasta por jogo/sistema, pasta compartilhada com identificação, envio/recebimento e sync por hashes e estado local independente. Backup completo do destino antes de sobrescrever, simulação sem escrita, conflito por conjunto do jogo, trava, preparação e verificação de integridade. Não replica exclusões. Saves, backups, configuração, identidade de memória e memória local não publicados no repositório do código.

## Validação

21 testes locais aprovados no Windows com Python 3.12.14 e dados sintéticos. Sintaxe Python 3.10 e interface de comandos verificadas. Os quatro ambientes remotos Windows/Ubuntu com Python 3.10/3.12 concluíram com sucesso, suíte de 21 testes e `--help`: https://github.com/vacilao38/steam-save-sync/actions/runs/42645728269. Não ensaiado em dual boot real ou com saves reais. WSL indisponível e Git Bash restrito no ambiente local.

Substituição atômica por arquivo; em interrupção no meio do conjunto pode ser necessária restauração manual do backup. Formatos Windows/Linux precisam ser compatíveis no próprio jogo; não há conversão nem descoberta automática dos caminhos.

## Continuidade

- Informar o caminho do diretório compartilhado em cada sistema e cadastrar os jogos e caminhos reais. Nenhum save real foi lido ou alterado.
- Antes de jogar no outro sistema, sincronizar; após jogar, sincronizar novamente, com jogo e Steam fechados. Coordenar Steam Cloud do jogo para evitar restauração externa de versão anterior.
- Código público por padrão autorizado pelo projeto; nenhuma publicação do script/downloads na vitrine Clustter foi solicitada ou feita. Ferramenta de script, sem instalador/app ou integração Update nesta entrega.
- ai-memory não disponível entre as ferramentas desta sessão; manter BMDS local validado, sem declarar consulta/indexação da wiki.
- Registro local: `steam_save_sync/memory.bmds.md`, `bmds://steam_save_sync-1307c24e60/cell/memoria-26df3aff76@1`; válido, com resultado remoto parcial no instante da gravação, superado pelo resultado completo acima.
- Sync inicial da central falhou por rede (`getaddrinfo() thread failed to start`); repetição com acesso à rede concluiu com todos os projetos e a central sincronizados. Reexecutar após os últimos registros desta entrega.
