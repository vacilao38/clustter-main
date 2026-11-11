# Análise pontual de proximidade — 10/11/2026

- Pedido: cruzar dois arquivos locais fornecidos no chat e localizar contas em até 10 km dos alvos, incluindo os responsáveis pelas contas vizinhas.
- Resultado: planilha local `Proximidade_contas_10km.xlsx`, na área de artefatos desta conversa. Os arquivos originais foram lidos sem alteração. Dados, nomes, coordenadas e arquivos de análise não foram incluídos em repositórios.
- Cobertura: 1.064 contas-alvo únicas, 14 com coordenadas, 10 com vizinhas no raio, 4 sem vizinhas no raio e 1.050 sem localização disponível. Há 16 leituristas identificados. Registros sem nome/código válido estão explicitamente separados.
- Conferências: varredura independente de todas as candidatas para os 14 alvos georreferenciados, reconciliação das 16.654 distâncias e das contagens, identificação de 18 divergências entre abas e uma linha duplicada. Identificação de alvos usa a BASE e o vínculo pela conta antiga, sem corrigir o arquivo original.
- Limites: distâncias em linha reta e responsabilidade cadastral; o resultado não acompanha a posição atual dos funcionários. Nova seleção é necessária se os arquivos ou o raio mudarem.
- Próximo passo: obter coordenadas das contas ainda não localizadas, caso o usuário deseje ampliar a cobertura.
- Continuidade: as tentativas de sincronização ao iniciar e ao encerrar retornaram erro Git 128, inclusive na central. Sincronização não concluída; nenhum push forçado executado. O resultado local permanece disponível.

## Correção de escopo solicitada no mesmo chat

- O usuário esclareceu que deseja somente a aba **Top Perdas**. O resultado vigente é `Top_Perdas_Proximidade_10km.xlsx`, na área local de artefatos da conversa.
- Preservados a ordem, as dez colunas e os 838 registros originais (837 contas únicas), inclusive a linha duplicada. Acrescentados os resultados de proximidade nas colunas K a T. Os 227 alvos exclusivos da BASE foram excluídos do resultado corrigido.
- Cobertura vigente: 14 contas únicas com coordenadas, dez com vizinhas até 10 km, quatro sem vizinhas no raio e 823 sem localização disponível. Os 16 leituristas identificados e os 16.654 pares de proximidade permanecem iguais, pois todos os alvos georreferenciados pertencem ao Top Perdas.
- Validação final: comparação das dez colunas originais nos 838 registros, preservação dos identificadores como texto, conferência de todas as distâncias e contagens, ausência de erros nas fórmulas e revisão visual da nova aba.
- O arquivo anterior permanece local como histórico. Nenhum dado das planilhas foi enviado aos repositórios.

## Mensagens para consulta de disponibilidade

- Por escolha explícita do usuário, preparados rascunhos individuais para os 16 leituristas identificados, consultando disponibilidade antes de distribuir visitas.
- Arquivo local: `Mensagens_leituristas_Top_Perdas.txt`, na área de artefatos da conversa. Contém as UCs do Top Perdas, apontamentos, referência das contas vinculadas ao leiturista, distâncias em linha reta e links de localização.
- Conferidos os 16 destinatários, 45 relações entre leiturista e conta-alvo e dez contas-alvo distintas. Uma conta pode aparecer em mais de uma consulta, conforme a escolha do usuário. Registros sem nome e com código zero foram excluídos.
- Nenhuma mensagem foi enviada. Próximo passo: o usuário copiar as consultas, reunir as disponibilidades e confirmar a distribuição, evitando visitas em duplicidade. Textos, nomes, UCs e coordenadas permanecem fora dos repositórios.
