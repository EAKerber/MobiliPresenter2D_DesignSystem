# Public routes — reduced motion and transition audit

**Date:** 2026-10-24  
**Production:** Netlify deploy `6adc221479c773577ed45e23`, READY, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` (rechecked through Netlify immediately before this audit).  
**Scope:** anonymous isolated browser context, CSS viewport 390 × 844, DPR 1, light theme. No account data or persistent site data was used.

## Method

For each route, I compared `prefers-reduced-motion: no-preference` with `reduce` after navigation. I read `matchMedia`, computed transition/animation durations on visible elements, and `document.getAnimations()`. I also opened and closed the Landing menu with keyboard input and selected a Viewer hotspot with Enter, without retaining the selection.

## Results

### Landing — `/`

- `reduce` was true in the reduced-motion pass and false in the baseline.
- Baseline computed transitions included 0.18–0.24 s for visible buttons, environment controls, feature cards and content. The public reveal animation was 0.65 s; intro animations included 0.32 s, 0.35 s, 0.40 s and 0.58 s. The finished-animation list recorded those durations.
- With reduction active, the 15 visible elements that declared transitions reported `1e-05s` (0.00001 s); the intro/reveal animation effects also reported `1e-05s`.
- With reduction active, opening the menu set `aria-expanded=true`; its computed transition was `1e-05s`, with zero running animations after 50 ms. Escape closed it and returned focus to the menu button. The selected environment remained COZINHA; no page data was changed.

### About — `/about/`

- `reduce` was true in the reduced-motion pass and false in the baseline.
- Baseline visible transitions included 0.18 s on the copper CTA and 0.20 s on the menu icon spans. With reduction active, each of the four visible transition-bearing elements reported `1e-05s`.
- `document.getAnimations()` was empty in both settled snapshots; no active animation was observed. This is a runtime sample after load, not an audit of every frame or interaction on the page.

### Viewer — `/viewer/`

- `reduce` was true in the reduced-motion pass and false in the baseline.
- Baseline layer-group opacity transitions were 0.18 s and hotspot-tag opacity transitions were 0.16 s. Under reduction, the visible layer groups and tags reported `1e-05s`.
- Under reduction, Enter selected module 02 while `:focus-visible` remained true. After 50 ms, no animation was running and layer/tag transition durations remained `1e-05s`. I restored module 01 before closing the isolated page.

### Landing — ambiente e carrossel com teclado

- Com `reduce` ativo, usei Enter para mudar o ambiente de Cozinha para Sala; após 50 ms, o cartão de apresentação tinha `transition-duration: 1e-05s` e `getAnimations()` não tinha animações em execução. Em seguida, Enter no controle de próximo grupo ativou o grupo 2 e também terminou sem animações em execução. O viewport continuou sem overflow (390 px de scroll/client width).
- Antes de fechar a aba, restaurei Cozinha e grupo 1. Redução ativa, ambiente e carrossel em seu estado inicial e zero animações em execução foram confirmados. Nenhum estado foi persistido.

## Limits

This confirms the reduced-motion media query and sampled computed durations on the three routes in one browser, viewport and theme. It does not cover other browsers, themes, widths, every interactive state, embedded content, or screen-reader behavior. It does not constitute a full accessibility conformance assessment.

The emulation was reset and the temporary isolated tab closed; the user's original browser tab remained selected. No product CSS, tokens, decisions, deployment, or persistent site state changed.
