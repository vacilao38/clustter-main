# Validação da continuidade

Em 23/10/2026, os 14 testes automatizados de `tests/test_sync.py` passaram usando repositórios Git descartáveis, sem modificar remotes dos aplicativos.

```powershell
python -m unittest discover -s tests -v
```

Cobertura prática: arquivos novos e exclusões entre duas cópias; UTF-8; alterações simultâneas em arquivos diferentes; conflito com preservação das versões e envio de branch de resgate; checkpoint sem rede e envio posterior; bloqueio de credencial em commit ainda não enviado; exclusão de dados ignorados; ciclos sem alterações não geram commits; pastas preexistentes são preservadas; branch não é trocada automaticamente; espera de edições recentes; bloqueio de caminhos externos; trava contra execução concorrente; clone dos apps pelo inventário e estabilidade de ciclos da central; exceção restrita para URLs fictícias em testes.

A sintaxe de `install.ps1` e os módulos Python também foram verificados. Os apps não tiveram seus testes funcionais ou builds reexecutados por esta migração. A validação física do segundo computador depende de executar o instalador nele.
