# Clustter main

Central de continuidade entre computadores. Os aplicativos ficam em repositórios próprios; aqui ficam os requisitos, pendências, handoffs e o sincronizador. Sem serviço pago ou biblioteca Python adicional. O inventário distingue membros da Clustter e projetos legados privados; cadastrar um legado para continuidade não o inclui na família nem na vitrine.

## Preparar o outro computador (uma vez)

Instale **Git para Windows** e **Python 3.10 ou superior** (com Python no PATH ou o lançador `py`). Autentique o GitHub pelo Git Credential Manager e configure a identidade Git:

```powershell
git config --global user.name "Seu nome"
git config --global user.email "Seu e-mail Git"
mkdir C:\Projetos\Clustter
cd C:\Projetos\Clustter
git clone https://github.com/vacilao38/clustter-main.git
powershell -NoProfile -ExecutionPolicy Bypass -File .\clustter-main\install.ps1
```

A pasta pode ser outra. O instalador registra apenas este computador, executa a primeira sincronização e agenda uma execução ao entrar no Windows. Não há verificação periódica. É necessário entrar no usuário do Windows e ter internet; desligado ou sem rede não envia nem recebe. Não é preciso que os dois PCs estejam ligados juntos. Se a entrada no Windows ocorrer sem rede, execute `clustter.cmd sync` quando a conexão voltar.

Abra a pasta **Clustter** como projeto no Codex. O instalador cria um `AGENTS.md` na raiz apenas se ainda não existir. As instruções são baseadas em arquivos, portanto funcionam também em uma conversa nova. Instale em ambos os computadores: a configuração de inicialização é local.

## Uso

```powershell
.\clustter-main\clustter.cmd sync       # salvar, buscar, integrar e enviar
.\clustter-main\clustter.cmd doctor     # verificar ferramentas e pendências
```

O Codex deve executar `sync` ao começar e terminar, e atualizar `handoffs/<projeto>.md` com o próximo passo. Não existe execução recorrente entre sessões. `projects.json` descreve as ferramentas necessárias para cada app, com comandos de preparação e validação. `doctor` verifica executáveis e mostra versões; não instala SDKs automaticamente.

Instalações antigas removem a repetição automaticamente quando o sincronizador recebe esta atualização. Para aplicar imediatamente em outra máquina que já atualizou a central, execute `powershell -NoProfile -ExecutionPolicy Bypass -File .\clustter-main\update-schedule.ps1`.

## Comportamento da sincronização

### Selecionar projetos neste computador

Para trabalhar apenas com alguns aplicativos, crie `.local/project-selection.json` na central:

```json
{"include": ["folk", "lake", "chain", "noon"]}
```

`sync` e `doctor` consideram apenas os IDs selecionados. A central continua sendo sincronizada; os demais repositórios existentes são preservados e ignorados. A seleção fica somente neste computador, não modifica `projects.json` nem a seleção de outro PC. Uma lista vazia sincroniza apenas a central. Configurações inválidas interrompem a execução sem ampliar o escopo.

### Ciclo

1. Atualiza a central e relê o inventário.
2. Clona repositórios ausentes em pastas irmãs da central.
3. Salva alterações elegíveis em commits de checkpoint, busca a branch cadastrada, integra alterações e faz push sem força.
4. Registra o estado local em `.local/status.json` e um resumo sem caminhos pessoais em `devices/`.

Execuções em segundo plano aguardam arquivos sem edições por pelo menos 30 segundos. Cada ciclo possui trava local. Operações Git em andamento, branch diferente, alterações durante a execução e conflitos suspendem apenas o projeto afetado. O comando retorna erro se houver pendência.

Se duas máquinas alterarem o mesmo trecho, o checkpoint é preservado, o merge é abortado e o sincronizador tenta enviar uma branch `codex/sync-rescue-*`. O Codex deve integrar essa branch manualmente e executar `sync` de novo. Nenhuma versão é escolhida automaticamente. Alterações não conflitantes podem gerar commits de merge.

**Checkpoints não são releases e podem não compilar.** O arquivo de handoff deve distinguir testes executados de testes pendentes. Um PC desligado antes do último envio só disponibilizará alterações quando voltar a se conectar.

## Limites e privacidade

- Novos projetos Clustter têm repositório próprio público por padrão; exceções precisam de justificativa no inventário. Noon permanece público. Em 24/10/2026, após a abertura anterior, o usuário pediu tornar Chain privado por preocupação com privacidade e proteção de dados; a alteração foi confirmada no GitHub e registrada no inventário. Folk e Lake preservam a exceção privada. Projetos legados fora da família Clustter ficam privados.
- A central não contém senhas nem arquivos principais dos apps. `.gitignore` e a verificação do sincronizador bloqueiam caminhos de dados, chaves, credenciais reconhecíveis e arquivos maiores que 90 MiB. Isso não substitui revisar o que é colocado em um repositório público.
- Credenciais GitHub são próprias de cada PC. Chaves de assinatura Android, modelos grandes, bases pessoais e bibliotecas locais precisam de transferência separada quando necessárias. Consulte `PENDENCIAS.md`.
- Não sincroniza o histórico de conversas/configuração pessoal do Codex nem os dados de uso dos aplicativos.
- Não altera a vitrine pública nem faz deploy. A regra de publicação permanece independente da visibilidade do código.
- O antigo repositório `memeger`, na raiz deste computador, é legado e não participa da automação. Cofre e Memoteca passam a ter repositórios individuais; o histórico antigo permanece no legado.

## Adicionar projeto

Todos os novos apps e novas distribuições seguem o [protocolo Update](docs/UPDATE.md), incluindo aviso no app, catálogo versionado e instalador `.exe` por usuário no Windows. A implementação compartilhada fica no repositório próprio `clustter-update`.

Crie o repositório próprio, prepare um `.gitignore` que exclua dados e builds, envie o código revisado e acrescente uma entrada em `projects.json`. Cadastre a branch usada para continuar o trabalho, dependências, comandos e o handoff. A próxima sincronização recupera o projeto no outro PC.

## Remover o agendamento

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\clustter-main\install.ps1 -Uninstall
```

Isso remove só o agendamento desta central. Arquivos e repositórios são preservados.
