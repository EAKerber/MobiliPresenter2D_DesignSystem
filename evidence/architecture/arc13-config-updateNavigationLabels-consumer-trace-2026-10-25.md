# ARC-13 — rastreio de `updateNavigationLabels`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Escopo filho de `createDetailCarousel`, rota `/config/`.

## Consumers

- **Seta anterior:** nome acessível `Mostrar {previousPage.label}`; tooltip `Anterior: {previousPage.shortLabel}`.
- **Seta seguinte:** nome acessível `Mostrar {nextPage.label}`; tooltip `Próxima: {nextPage.shortLabel}`.

As setas visíveis são ícones ←/→. A página atual determina os rótulos adjacentes; o carrossel usa navegação circular pelas páginas disponíveis, incluindo “Vista interna” apenas quando o produto possui layout interno técnico. Labels e shortLabels vêm dos descriptors locais de página, não do nome do produto. Preservar sentido direcional e relação com a página adjacente, com as duas variantes de label.

## Limites

Rastreio manual de renderer, descriptors e ciclo do carrossel; sem runtime/AT. Nenhuma chave foi proposta; código do produto, catálogo, índice e `decisions.json` seguem inalterados.
