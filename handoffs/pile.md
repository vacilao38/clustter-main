# Pile — 24/10/2026

Novo app Clustter em `pile_app/`, repositório público próprio [vacilao38/pile](https://github.com/vacilao38/pile), branch `main`. Inventário cadastrado. O usuário dispensou a sincronização entre computadores nesta sessão; não executar sync ao encerrar. Sem autorização de catálogo ou download público.

## Implementado

Flutter 3.44.1 / Dart 3.12.1: Windows 10/11 x64 e Android 7+ (celular/tablet). Organização por categorias com nomes customizáveis, prévia/opção de um clique, sem sobrescrita, diário/desfazer, coleções/etiquetas/capas/temas, EXIF por ano/coordenadas, regras sob demanda, duplicados por SHA-256 e semelhança visual separada. Cópias são separadas para revisão, sem exclusão automática.

Windows: MoveFileW. Android: ponte Kotlin SAF e cópia verificada antes de remover origem. Índice/metadados locais, sem telemetria/backend. IA OpenRouter opt-in por lote: modelos :free de visão com preço revalidado, chave em memória, miniaturas sem EXIF, nomes/caminhos locais não enviados e sugestões revisadas antes de aplicar. Sem chamada real de LLM nesta sessão.

Documentação/fontes em README.md, docs/DECISOES.md e docs/VALIDACAO.md do app. Código UTF-8. Builds, chaves e dados excluídos do Git. Etiquetas residem no índice e não acompanham movimentos externos. Dias nas regras contam desde a primeira detecção, não modificação. Regras rodam mediante ação do usuário com o app aberto.

## Validação

27 testes de domínio/IO/widgets aprovados: arquivos sintéticos reais Windows, colisões, desfazer, recuperação, duplicados, regras, snapshots danificados, EXIF e layouts 360/800/1440 px com texto 1,4. Builds Windows release, Android debug e Android release universal e por arquitetura gerados (ARM64: 18,2 MB). Um teste de integração Windows também passou pelo fluxo organizar/desfazer real na interface. Para Android release, usar flutter build apk --release com regeneração normal dos plugins, evitando --no-pub depois de testes. Tela Windows renderizada inspecionada. Consultar docs/VALIDACAO.md do app para a passagem final e testes posteriores.

## Próximo passo

Validar SAF em celular/tablet: concessão/recusa, acesso persistente, cópia/desfazer, rotação e interrupções. Não há dispositivo ou AVD disponível. Testar LLM com lote sintético, chave e consentimento, incluindo cota/disponibilidade do modelo. Medir desempenho em bibliotecas maiores e preparar assinatura de distribuição antes de publicar, somente por pedido explícito. Sem sincronização nesta sessão por decisão do usuário.

Observação: outra execução da central gerou checkpoints durante esta tarefa. Este chat não iniciou nova sincronização após a dispensa; não alterou o agendamento nem interrompeu trabalhos de outros chats.
