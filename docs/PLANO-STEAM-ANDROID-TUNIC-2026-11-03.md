# Steam e TUNIC no Galaxy Tab S10 Lite — avaliação e plano

Data: 03/11/2026. Escopo: pesquisa e proposta, sem implementação ou publicação autorizada nesta etapa. O usuário confirmou 6 GB de RAM e declarou possuir licenças reais dos jogos. Execução local é a premissa de planejamento; a aceitação de streaming ainda não foi confirmada.

## Parecer

É tecnicamente possível criar um aplicativo Android que coordene camadas existentes de compatibilidade para executar determinados jogos de PC e, se o cliente oficial funcionar nesse ambiente, instalar e baixar jogos pela Steam. A existência de Winlator e GameNative demonstra a categoria de solução, mas não comprova desempenho do TUNIC no aparelho do usuário.

Para o Tab S10 Lite de 6 GB, o projeto é experimental. Não há benchmark próprio nem teste reproduzível deste conjunto exato localizado nesta pesquisa. Não prometer 30 ou 60 FPS. A proposta é testar 30 FPS sustentados em 960×540 e depois 1280×720, com qualidade baixa quando disponível. A resolução nativa e 60 FPS não são critérios iniciais.

Se o objetivo imediato for apenas jogar com boa qualidade, Steam Link é a alternativa oficial com maior previsibilidade, desde que o PC execute bem o jogo e a rede tenha baixa latência. Ele executa o jogo no PC; não atende à independência do tablet.

## Evidências e limites

- A Samsung identifica Exynos 1380, tela de 2112×1320 e variantes de 6/8 GB no [Tab S10 Lite](https://news.samsung.com/br/galaxy-tab-s10-lite-um-tablet-com-recursos-valiosos-de-inteligencia-artificial-para-as-necessidades-do-dia-a-dia). A [ficha do Exynos](https://semiconductor.samsung.com/processor/mobile-processor/exynos-1380/) informa GPU Mali-G68 com cinco núcleos. O usuário confirmou a versão de 6 GB.
- [TUNIC na Steam](https://store.steampowered.com/app/553420/TUNIC/) informa mínimos de Windows 10, i5 de quatro núcleos/2,7 GHz, 8 GB de RAM, GTX 660/RX 460 e 2 GB de armazenamento. Os 8 GB são requisito declarado para PC, não medição de consumo: não provam sozinhos que o tablet falhará. Entretanto, Android, tradução, cliente e jogo disputam os 6 GB, e a GPU usa memória compartilhada.
- [Winlator](https://github.com/brunodev85/winlator) combina Wine com Box86/Box64. [GameNative](https://gamenative.app/) anuncia autenticação, download e execução local de jogos comprados. Sua existência reduz a justificativa para escrever um emulador do zero; não certifica compatibilidade nem autorização da Valve.
- [Turnip](https://docs.mesa3d.org/drivers/freedreno.html) pertence à família Adreno. Não é driver para a Mali deste tablet. [Vortek](https://github.com/brunodev85/vortek) oferece uma camada sobre o driver Vulkan do sistema e é candidato a avaliar.
- [DXVK](https://github.com/doitsujin/dxvk) traduz Direct3D para Vulkan. Sua [documentação atual de drivers](https://github.com/doitsujin/dxvk/wiki/Driver-support) impõe capacidades específicas e declara não oferecer suporte primário a drivers Android/mobile. Escolher versão/variante compatível com as extensões efetivamente expostas; não instalar simplesmente a mais recente nem falsear capacidades Vulkan.

## Licenciamento e conformidade

Ter a licença real é uma premissa adequada, mas não autoriza qualquer meio de acesso ou redistribuição. O [Steam Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/), especialmente §§1.B, 2.A e 2.G, prevê uso pessoal, termos adicionais por jogo e restrições a modificações e emulação de protocolos de rede. A aplicação da lei e dos termos não foi objeto de parecer jurídico individual.

O desenho proposto mantém conta, Steam Guard, verificações de propriedade e arquivos originais. O instalador oficial deve vir da Valve; o usuário entra no próprio cliente, que administra downloads e atualizações. O app não recebe senhas em tela própria nem reimplementa autenticação/download Steam no MVP. Não incluir jogos, arquivos proprietários da Steam, cracks, emuladores de licença, executáveis corrigidos para remover DRM ou mecanismos para contornar anticheat. Copiar uma instalação própria para teste só quando permitido pela licença e sem neutralizar verificações exigidas pelo jogo.

Isso reduz riscos contratuais; não constitui selo de aprovação da Valve para execução local no Android. Antes de anunciar um produto como plenamente conforme, revisar os termos aplicáveis do TUNIC e os componentes exatos. [Steam Link/Remote Play](https://store.steampowered.com/remoteplay) é o caminho expressamente oferecido pela Valve para jogar no tablet.

GameNative é referência de produto, não uma base automaticamente redistribuível em sua totalidade: seu [THIRD_PARTY_NOTICES](https://github.com/utkarshdalal/GameNative/blob/master/THIRD_PARTY_NOTICES) descreve componentes proprietários e integrações internas com o cliente Steam. Auditar modo de execução e licenças antes de aproveitar código ou binários. O rótulo GPL da aplicação não licencia todos os componentes agregados. O uso de bibliotecas gráficas de compatibilidade não deve ser confundido com remover verificações de propriedade.

## Arquitetura proposta

Interface Android em Kotlin/Jetpack Compose para biblioteca local, configuração, controles, diagnóstico e sessão. Integração nativa por JNI/NDK quando necessária. Em um fork, preservar inicialmente a stack existente para reduzir alterações sem benefício medido. Flutter/React Native não resolvem o gargalo do runtime; não são a primeira escolha para um projeto novo com esse foco.

O aplicativo coordena um ambiente Wine compatível com Android; Wine implementa APIs Windows, e Box64 ou FEX traduz instruções x86/x64 para ARM64. A renderização segue Direct3D → DXVK compatível → Vortek/driver Vulkan Mali → tela Android. Box64 e FEX são alternativas a comparar, não camadas a empilhar. A versão e o caminho de 32 bits/WoW64 devem acompanhar as necessidades reais do cliente e do jogo.

No primeiro protótipo, usar um ambiente conhecido para Steam e TUNIC, evitando incompatibilidade de comunicação entre cliente e jogo. Perfis por título guardam resolução, runtime e configurações; separar prefixos só depois de validar o modelo de inicialização. Um prefixo Wine organiza arquivos e configuração, mas não é uma barreira completa de segurança. Aplicar o sandbox Android e mapear apenas pastas necessárias.

Distribuir apenas componentes com direito de redistribuição verificado. Fixar versões e hashes dos componentes aprovados, manter avisos/fontes exigidos e permitir retorno à última versão funcional. Atualização do runtime deve preservar saves e o prefixo antigo até validar a migração. Não congelar um cliente Steam antigo e inseguro para contornar incompatibilidade.

## Execução por etapas e critérios de decisão

| Etapa | Trabalho e entrega | Condição para avançar |
| --- | --- | --- |
| 1. Inventário | Registrar modelo, Android/One UI, ABI, driver e extensões Vulkan, RAM disponível, espaço livre e controle. Preparar backup dos saves. | Aparelho físico acessível, dependências e licenças conhecidas. |
| 2. Prova gráfica | Ambiente existente auditado, programa simples e depois TUNIC original. Registrar versão de cada camada; começar em 960×540/baixo. | Jogo entra em partida, desenha corretamente, recebe controle e reproduz áudio. Falha de driver é investigada antes de construir interface. |
| 3. Steam oficial | Instalar cliente original, entrar com Steam Guard, baixar TUNIC no tablet e iniciar por ele. Validar reinício e atualização. | Fluxo completo funciona sem cliente substituto, remoção de DRM ou alteração de autenticação. Se falhar, a promessa de baixar e jogar pela Steam permanece não demonstrada. |
| 4. Desempenho | Ensaios em 960×540 e 1280×720; limitar a 30 FPS quando suportado. Cenas repetíveis de exploração e combate, controle físico, cache frio/quente. | Cumprir critérios abaixo sem superar limites térmicos nem depender de frame generation. |
| 5. MVP próprio | Biblioteca local, abrir Steam, instalar componentes aprovados, perfil TUNIC, iniciar/encerrar sessão, controles, métricas e diagnóstico exportável. | Resultado de desempenho preservado e ciclo de vida Android confiável. |
| 6. Robustez | Falta de espaço/rede, login expirado, download interrompido, memória baixa, desligamento de controle, retorno após bloqueio da tela, saves e migração de runtime. | Não perder saves; erros recuperáveis; build reproduzível e componentes licenciados. |

As etapas 2 e 3 são necessárias: abrir diretamente um jogo não prova que o cliente Steam consegue autenticar e baixar conteúdo. Se o build do jogo exige Steam, a etapa 2 depende da etapa 3; não remover essa exigência.

Reserva inicial sugerida: alguns dias de ensaio técnico antes de aprovar desenvolvimento de semanas. Não há cronograma fechado sem acesso ao aparelho. Se cliente, renderização ou memória inviabilizarem o caso, encerrar a aposta no MVP para este tablet ou redefinir o objetivo com o usuário. Uma interface nova não aumenta a capacidade física da GPU.

## Protocolo de desempenho

Executar ao menos três sessões de 30 minutos, registrando também a condição térmica, brilho, alimentação e aplicativos de fundo. Comparar mesmas cenas e versões. Coletar FPS real, distribuição de frametimes/1% low, pausas, PSS/RSS dos processos quando acessíveis, encerramentos por memória, comportamento térmico e bateria. Instrumentação disponível no aparelho define quais métricas são confiáveis; dados de emulador Android não substituem o tablet.

Critério proposto de jogabilidade: média de pelo menos 29 FPS com limite de 30, 1% low de pelo menos 24 FPS nas cenas repetidas, nenhuma falha gráfica grave, nenhum crash/encerramento por memória, áudio e controles corretos e salvar/carregar após reiniciar o aplicativo. Verificar que o trecho final aquecido mantém o critério. Metas são decisões de produto propostas, não números observados. Pausas persistentes perceptíveis também reprovam, mesmo se a média passar.

Otimizar por evidência: resolução/qualidade para gargalo gráfico; custo do cliente e runtime para CPU/memória; shaders para pausas de compilação; driver para artefatos. Não usar RAM virtual como substituto de RAM física nem frame generation para declarar 30 FPS reais. Não fazer root, overclock ou desativar proteção térmica. Saves offline e Steam Cloud dependem do jogo e da sessão oficial; validar conflito de saves antes de automatizar sincronização.

## Situação ao encerrar a pesquisa

Foram consultadas fontes primárias de Samsung, Valve e mantenedores. Não foi instalado APK, autenticada conta, baixado jogo, criado app, medido FPS ou publicado produto. O usuário confirmou 6 GB; modelo exato, versão do Android e preferência sobre streaming permanecem a coletar.

Próximo passo recomendado: acesso ao Tab S10 Lite para o ensaio das etapas 1–4. Somente depois decidir se existe benefício em criar aplicativo próprio. Se houver criação futura, usar repositório próprio e cadastrar requisitos/comandos em projects.json; não adicionar código de app à central. Nenhuma autorização de publicação na Clustter decorre desta proposta.
