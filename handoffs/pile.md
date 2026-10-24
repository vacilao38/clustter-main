# Pile — 24/10/2026

App em `pile_app/`, repositório próprio **privado** https://github.com/vacilao38/pile, branch `main`. Exceção privada solicitada explicitamente pelo usuário em 24/10/2026 por risco de LGPD, registrada em projects.json. O usuário também autorizou a publicação do aplicativo e dos downloads na Clustter na mesma data.

## Implementado e validado

Flutter 3.44.1 / Dart 3.12.1: Windows 10/11 x64 e Android 7+ (celular/tablet). Organização por categorias, nomes customizáveis, prévia/opção de um clique, diário e desfazer sem sobrescrita; coleções/etiquetas/capas/temas; EXIF por ano/coordenadas; regras sob demanda; duplicados por SHA-256 e semelhança visual separada. Cópias ficam em Revisar duplicados, fora da reorganização/análises posteriores, sem exclusão automática.

Windows usa MoveFileW; Android usa ponte Kotlin SAF com cópia verificada antes de remover origem. Índice local, sem telemetria/backend. IA opcional OpenRouter por lote autorizado: modelos :free de visão revalidados, chave em memória, miniaturas sem EXIF e sugestões revisadas antes de aplicar. Etiquetas residem no índice e não acompanham movimentos externos. Regras contam dias desde detecção e rodam sob demanda.

Análise estática sem problemas, 27 testes de domínio/IO/widgets e 1 integração Windows aprovados. Layouts 360/800/1440 px com texto 1,4. Builds Windows release e Android release por arquitetura gerados; Windows ZIP 13,4 MiB, APK ARM64 18,2 MiB. Runtime C++ acompanha ZIP; APKs têm assinatura de desenvolvimento. Sem aparelho ou AVD disponível: SAF em celular/tablet físico e LLM autenticada permanecem pendentes.

## Publicação autorizada

- Vitrine: https://vacilao38.github.io/clustter-cores-downloads/#pile
- Release pública: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/pile-v0.1.0
- Quatro pacotes e SHA256SUMS.txt publicados; tamanhos e hashes remotos comparados aos locais. Cinco links HTTP 200.
- Catálogo de cinco apps preserva Folk, Lake, Chain e Noon. Captura da interface contém somente arquivos sintéticos. Limites e riscos da IA aparecem na apresentação pública.
- Código-fonte, dados de uso, credenciais e índices não fazem parte da publicação. Fontes/validação em README.md e docs/ do app. Assets de distribuição em outputs/clustter-pile-publication (fora do repositório do app).

## Próximo passo

Validar SAF em celular e tablet reais (concessão/recusa, acesso persistente, cópia/desfazer, rotação/interrupção) e testar IA com chave e lote sintético autorizado. Medir desempenho em bibliotecas maiores e definir assinatura de distribuição para versões futuras. Build Android após testes deve regenerar configuração pelo comando normal flutter build apk --release --split-per-abi; evitar --no-pub e comandos Flutter concorrentes.

Sincronização global dispensada pelo usuário nesta sessão. Este chat não iniciou novo sync após a dispensa; foram observados checkpoints de outra execução da central, cujo agendamento não foi alterado. Pushes de publicação dos repositórios do Pile, catálogo e downloads pertencem ao pedido explícito de entrega/publicação.
