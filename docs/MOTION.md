# Movimento Clustter · 25/10/2026

Diretriz solicitada pelo usuário a partir da revisão do Pile e Chain. Implementada nesses dois apps nesta etapa; adoção nos demais apps deve ocorrer quando forem trabalhados.

- Menus: fade da superfície inteira, 120 ms, sem crescimento em escada por item; fechamento equivalente.
- Navegação: indicador compartilhado desliza/estica entre destinos, 240 ms easeInOutCubic; foco e alvos estáveis.
- Páginas: fade 260 ms entrada / 160 ms saída. Diálogos Chain: 200/140 ms. Evitar movimento supérfluo.
- Roda Windows: desaceleração curta de 190 ms, acumular destino, inverter imediatamente o sentido, respeitar extremos. Não alterar física nativa de toque/trackpad.
- Ocultar scrollbar persistente, manter roda, teclado e gestos; faixas horizontais precisam setas e descoberta das extremidades.
- Respeitar redução de movimento do sistema e preferência do app. Sem animação quando desativada.
- Ícones funcionais 18–20 px e alvos de toque de pelo menos 48 px. Não reduzir acessibilidade ao compactar.
- Lista grande virtualizada; não adicionar dependência pesada para animação. Verificar texto ampliado e celular/tablet/desktop.

Referências: [Fluent motion](https://fluent2.microsoft.design/motion), [Windows timing/easing](https://learn.microsoft.com/en-us/windows/apps/design/motion/timing-and-easing).
