# Como funciona — teclado nos disclosures em Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/
- Deploy observado: Production, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`.
- Viewport: 1280×720 CSS px; tema escuro; `prefers-reduced-motion: reduce` retornou `false`.
- Data: 24/10/2026, sessão anônima, sem autenticação.

## Interação

- O snapshot de acessibilidade expôs os três itens de “As fundações da Casa em Módulos” e os três itens de “Aspectos analisados no estudo” como disclosures com estado recolhido.
- No primeiro item (“Evoluir a forma de produzir”), pressionei Enter. O disclosure passou a expandido, o conteúdo explicativo apareceu no snapshot e o foco permaneceu no controle.
- No segundo item (“Eficiência com liberdade”), pressionei Espaço. O disclosure passou a expandido, o conteúdo explicativo apareceu no snapshot e o foco permaneceu no controle.
- A inspeção DOM confirmou que esses controles são elementos nativos `summary` dentro de `details`; o atributo `open` apareceu após cada ativação.

## Limites

A amostra verifica Enter e Espaço em dois dos seis disclosures nativos dessa página. Não cobre os outros quatro disclosures, o grupo separado de cartões da economia, leitores de tela, outros navegadores, temas ou larguras. Não avalia aparência do foco, contraste nem mudança no produto. É uma observação pontual e não encerra achados de acessibilidade.
