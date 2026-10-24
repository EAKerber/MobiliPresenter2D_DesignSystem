# Anel de foco em componentes públicos — amostra Production (24/10/2026)

## Alvo e método

- Production: deploy READY `6adc221479c773577ed45e23`, produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Rota `/`, contexto anônimo isolado, viewport móvel de 390 × 844 CSS px.
- `prefers-reduced-motion: reduce`; sequência real de dez teclas Tab em claro e repetida em escuro. Foi lido o estilo computado do elemento ativo em cada parada.

## Resultado

Os dez focos foram: link da marca, CTA WhatsApp do header, controle de tema, botão do menu, CTA “Conheça nossos ambientes” e cinco botões de ambiente (Cozinha, Sala, Quarto, Escritório e Lavanderia).

- Claro: a CSSOM retornou contorno de 2.67 px em `#6E512E`; offset computado 2.67 px em nove focos e 2 px no controle de tema. A fonte declara 3 px/offset 3 px na regra global e 3 px/offset 2 px no tema.
- Escuro: a CSSOM retornou contorno de 2.67 px em `#D8BC7C`; offsets computados iguais aos do tema claro. A fonte declara 3 px/offset 3 px globalmente e 3 px/offset 2 px no controle de tema.
- VIS-002 registra 4 px/offset 3 px, claro `#8B6A40` e escuro `#D8BC7C`. Comparando declarações CSS, a regra global tem 3 px/offset 3 px e a exceção do controle de tema 3 px/offset 2 px. A CSSOM também retornou 2.67 px para um elemento de teste com `outline:3px`; causa não identificada.

Nas declarações CSS, a largura global é 3 px em todos os dez focos, abaixo dos 4 px aprovados; a cor clara também diverge. Nove focos herdam offset 3 px, e o controle de tema declara 2 px. A CSSOM retornou 2.67 px inclusive para um elemento de teste com `outline:3px`; a causa dessa diferença não foi identificada. A amostra não prova que todos os controles ou rotas compartilham a regra.

## Limites

Amostra de uma rota, uma largura e dez paradas sequenciais. Não mede contraste do anel, leitores de tela, outros navegadores, estados sobrepostos ou todos os focos da página. Não cria token, mapeamento canônico ou autorização de implementação. Nenhum código, configuração ou deploy foi alterado.
