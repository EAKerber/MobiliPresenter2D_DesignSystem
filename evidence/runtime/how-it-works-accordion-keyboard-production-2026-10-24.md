# Como funciona — controles expansíveis por teclado em Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/
- Deploy observado: Production, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`.
- Viewport: 1280×720 CSS px; tema escuro; `prefers-reduced-motion: reduce` retornou `false`.
- Data: 24/10/2026, sessão anônima, sem autenticação.

## Disclosures de fundações e estudo

Os seis disclosures nativos foram ativados por teclado; alternaram entre Enter e Espaço:

| Seção | Controle | Tecla | Resultado |
|---|---|---|---|
| Fundações | Evoluir a forma de produzir | Enter | expandido |
| Fundações | Eficiência com liberdade | Espaço | expandido |
| Fundações | Transparência faz parte do produto | Enter | expandido |
| Estudo | Plantas e dimensões | Espaço | expandido |
| Estudo | Circulação e ergonomia | Enter | expandido |
| Estudo | Necessidades de armazenamento | Espaço | expandido |

O DOM confirmou controles `summary` dentro de `details`; o estado `open` mudou e os textos de conteúdo apareceram no DOM e na árvore de acessibilidade. O snapshot final manteve foco no último controle ativado.

## Cartões da seção de economia

Os seis botões expansíveis da seção “Por que custa menos?” também responderam às teclas Enter e Espaço alternadamente: Compra em escala, Compras coletivas, Produção planejada, Aproveitamento de material, Engenharia já estudada e Menos retrabalho. Em cada ativação, `aria-expanded` mudou para `true` e o texto do controle ficou disponível. O snapshot de acessibilidade confirmou o painel de “Menos retrabalho” expandido e com seu conteúdo.

## Limites

A passagem cobre uma rota, um navegador, tema escuro e viewport 1280×720. Não cobre leitores de tela, outros navegadores, temas/larguras, aparência/contraste do foco, movimento reduzido ativo ou todos os estados de recolhimento. É uma observação runtime; nenhum código do produto foi alterado e nenhum achado foi encerrado.
