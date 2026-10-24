# Anel de foco em componentes públicos — amostra Production (24/10/2026)

## Alvo e método

- Production: deploy READY `6adc221479c773577ed45e23`, produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Rota `/`, contexto anônimo isolado, viewport móvel de 390 × 844 CSS px.
- `prefers-reduced-motion: reduce`; sequência real de dez teclas Tab em claro e repetida em escuro. Foi lido o estilo computado do elemento ativo em cada parada.

## Resultado

Os dez focos foram: link da marca, CTA WhatsApp do header, controle de tema, botão do menu, CTA “Conheça nossos ambientes” e cinco botões de ambiente (Cozinha, Sala, Quarto, Escritório e Lavanderia).

- Claro: contorno sólido de 2.67 px em `#6E512E`; offset 2.67 px em nove focos, e 2 px no controle de tema.
- Escuro: contorno sólido de 2.67 px em `#D8BC7C`; offsets iguais aos observados no tema claro.
- VIS-002 registra a referência aprovada de 4 px e offset de 3 px, com claro `#8B6A40` e escuro `#D8BC7C`.

A divergência de largura aparece em todos os dez focos amostrados; a cor clara diverge em todos, e o offset varia no controle de tema. Isto amplia a evidência do link de About e da marca, mas não prova que todos os controles ou rotas compartilham a mesma regra.

## Limites

Amostra de uma rota, uma largura e dez paradas sequenciais. Não mede contraste do anel, leitores de tela, outros navegadores, estados sobrepostos ou todos os focos da página. Não cria token, mapeamento canônico ou autorização de implementação. Nenhum código, configuração ou deploy foi alterado.
