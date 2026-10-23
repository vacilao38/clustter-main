# Validação da continuidade

Em 23/10/2026, os 14 testes automatizados de `tests/test_sync.py` passaram usando repositórios Git descartáveis, sem modificar remotes dos aplicativos.

```powershell
python -m unittest discover -s tests -v
```

Cobertura prática: arquivos novos e exclusões entre duas cópias; UTF-8; alterações simultâneas em arquivos diferentes; conflito com preservação das versões e envio de branch de resgate; checkpoint sem rede e envio posterior; bloqueio de credencial em commit ainda não enviado; exclusão de dados ignorados; ciclos sem alterações não geram commits; pastas preexistentes são preservadas; branch não é trocada automaticamente; espera de edições recentes; bloqueio de caminhos externos; trava contra execução concorrente; clone dos apps pelo inventário e estabilidade de ciclos da central; exceção restrita para URLs fictícias em testes.

A sintaxe de `install.ps1` e os módulos Python também foram verificados. Os apps não tiveram seus testes funcionais ou builds reexecutados por esta migração. A validação física do segundo computador depende de executar o instalador nele.

## Seleção local e preparação de outro computador — 23/10/2026

Executados novamente os testes do sincronizador com Python 3.14.6: **17 testes passaram**. A cobertura adicional verifica que um ciclo real ignora repositórios não selecionados, que uma seleção vazia inclui somente a central e que IDs desconhecidos ou formatos inválidos interrompem a execução antes de operar nos repositórios.

Nesta máquina foi configurada uma seleção local de Folk, Lake, Chain e Noon. A configuração fica em `.local/project-selection.json`, fora do versionamento, e não altera o inventário compartilhado. O agendamento com intervalo `PT3M` e gatilho de entrada no Windows foi conferido; uma execução pelo próprio Agendador terminou com resultado 0 e sincronizou somente esses quatro apps e a central.

Os quatro aplicativos tiveram `flutter pub get --enforce-lockfile`, `flutter analyze --no-pub` e `flutter test --no-pub --reporter expanded` executados com Flutter 3.44.1 e Dart 3.12.1. Todos os comandos terminaram com código 0, todas as análises ficaram sem problemas e os quatro lockfiles foram preservados:

| Aplicativo | Testes aprovados | Ignorados pelo próprio projeto |
| --- | ---: | ---: |
| Folk | 12 | 1 |
| Lake | 40 | 1 |
| Chain | 10 | 0 |
| Noon | 28 | 0 |

Esses resultados não representam build de release, teste de áudio/transcrição nativa nem validação em Android físico. A conclusão da instalação dos SDKs e as limitações da máquina constam no registro de preparação em `devices/` e nos respectivos handoffs.
