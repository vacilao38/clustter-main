# Bridge · 27/10/2026

Bridge **0.1.0+1** criado para Windows e Android. Repositório próprio `https://github.com/vacilao38/bridge`, branch `main`, **privado confirmado na API** por pedido explícito do usuário. O mesmo pedido autorizou publicação do aplicativo e dos downloads na Clustter. Inventário cadastrado com requisitos e comandos.

## Entrega

- Flutter com runners C++/Kotlin; teclado e mouse Windows → Android por TCP direto na mesma rede IPv4/Wi-Fi/hotspot. Sem backend, conta ou novo runtime.
- Convite descartável de 256 bits por 10 minutos, HKDF-SHA256, AES-256-GCM, chave por direção/sessão, contadores e heartbeat. Não gravar convites ou teclas.
- Windows captura por clique; Ctrl+Alt+Esc, foco, watchdog ou desconexão liberam. Android usa acessibilidade sem leitura de conteúdo, IME selecionado manualmente e serviço com notificação para encerrar. Arraste reproduzido ao soltar, até dois segundos. Internet, USB, Bluetooth, espelhamento e controle reverso não incluídos.
- Temas claro/escuro, redução de movimento, interface responsiva, licenças e Update. Preferências são da sessão nesta primeira versão.
- Setup por usuário e APKs em `bridge_app/dist/0.1.0/`, ignorados no Git. Certificado Android original fixado; chave transferida por canal seguro para outro PC. Não versionar chave, dados, builds ou caches.

## Validação

Análise sem problemas; **10 testes** aprovados (TCP real/Unicode, ordenação, chave incorreta, replay/adulteração, limites, cancelamento e Android 390 px/texto 200%). Integração Windows final aprovada: ação pela UI, tecla sintética SendInput recebida, Ctrl+Alt+Esc e watchdog com rede mantida por heartbeat. Teste aguarda foco da própria janela, pois Windows pode impedir ativação automática; não retirar essa proteção do produto. Comandos Debug confirmados ausentes do Release.

Windows Release e três APKs Release compilados. Setup isolado/desinstalador passaram preservando arquivo extra. APKs: versão, ABI, não depurável, INTERNET, certificado e alinhamento 16 KiB conferidos. Hashes/tamanhos em `bridge_app/docs/VALIDATION.md`.

Build Android **sem `--no-pub`**: Flutter #169336 deixa o registrador de integration_test no Release quando essa flag é usada. Build final regenerou corretamente; não editar o SDK nem Java gerado e não executar comandos Flutter concorrentes no checkout. README/inventário registram o procedimento.

## Publicação

Página: https://vacilao38.github.io/clustter-cores-downloads/#bridge
Release: https://github.com/vacilao38/clustter-cores-downloads/releases/tag/bridge-v0.1.0

Cinco assets públicos com SHA-256/tamanhos conferidos e HTTP 200. Setup final: 10.333.975 bytes, SHA-256 `9c608f222b50222f93a7d1b27b579f955603c24ab6703502daf486d1f22d862b`. Pages **built** no commit `6b25ffeb0733354272c88e7d2b4302bd5f7b4826`; catálogo público igual à fonte e feed Bridge Windows/Android 0.1.0. Sete produtos; seis anteriores preservados integralmente. Imagem real do app sem dados pessoais. Apresentação/links/limites conferidos em navegador estreito; prova `outputs/bridge-publication/bridge-publicado.png` (local, não sincronizada). Publicador compartilhado Update registra somente a nova autorização Bridge.

## Memória e continuidade

BMDS canônico: `bridge_app/memory.bmds.md`, arquitetura `bmds://bridge_app-1aa781cc0f/cell/memoria-2701500835@1`, entrega `bmds://bridge_app-1aa781cc0f/cell/memoria-478a22741c@1`, pilha desenvolvimento rev 2, validada; sem orgânicas afetadas. ai-memory workspace `default`, project `bridge_app-1aa781cc0f`: localhost:49374 indisponível mesmo fora do isolamento. Nenhuma consulta/indexação wiki concluída.

Sincronização inicial de todos os projetos/central aprovada após acesso de rede. A sincronização final deve ser conferida em `.local/status.json` antes de declarar concluída; não usar push forçado.

## Próximo passo

**Validar em Android físico e redes reais**: gestos/cliques/arraste, digitação e atalhos em outros apps, rotação, tela bloqueada, bateria, notificação e segundo plano. Nenhum aparelho ou AVD disponível nesta etapa; não confundir APK compilado com controle físico validado. Testar outro Windows sem SDK, DPI/múltiplos monitores e layouts de teclado. Não instalar automaticamente em aparelhos do usuário.
