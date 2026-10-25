# VIS-002C — cores próximas para texto corrido (candidata v0.3)

**Data:** 2026-10-24. **Estado:** proposta versionada em branch para preview; decisão canônica e produção permanecem inalteradas.

## Direção e escopo

Para texto corrido e longo, usar cores próximas de preto no tema claro e próximas de branco no tema escuro, conforme a superfície. Esta versão cobre somente os dez contextos medidos e autorizados nas rotas públicas Landing, Quem somos e Como funciona. No claro, reutiliza o papel existente `VIS-002.approvedPalette.colors.textPrimary.light` (`#292723`). No escuro, mantém `#C4BCB2` sobre `#20211F`.

Os três contextos da distribuição v0.2 — `.hero-description`, `.how-hero-note` e `.about-scale p:not(.eyebrow)` — já faziam parte dos pares runtime aprovados e são medidos sobre `#F0EDE8`. A preferência posterior por quase preto para texto longo substitui o tom `#705C4B` nesses três contextos dentro da v0.3. A distribuição v0.2 permanece como histórico fixado; não é carregada ao lado da v0.3. Eyebrows, assinaturas, tokens globais e tema escuro ficam fora da alteração.

## Contextos medidos e contraste

**Evidência:** [DOM/CSSOM no preview da PR #241](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/current-handover-20261024/evidence/runtime/pr241-vis002-measured-copy-contrast-preview-2026-10-24.md) e [revisão manual v0.3](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/current-handover-20261024/evidence/runtime/pr241-vis002-v03-preview-manual-review-2026-10-25.md). Os três fundos legados foram revistos no preview; o fundo verificado foi `#F0EDE8`.

| Rota | Seletor | Fundo | Texto v0.3 | Contraste |
| --- | --- | --- | --- | ---: |
| / | `.hero-description` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.how-hero-note` | `#F0EDE8` | `#292723` | 12,77:1 |
| /about/ | `.about-scale p:not(.eyebrow)` | `#F0EDE8` | `#292723` | 12,77:1 |
| / | `.story-section > p:not(.eyebrow)` | `#E8E3DC` | `#292723` | 11,68:1 |
| / | `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /about/ | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /about/ | `.about-scale__stat > span` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.commercial-clarity > p:not(.eyebrow)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.launch-card .launch-copy > p` | `#F0EDE8` | `#292723` | 12,77:1 |

## Artefatos e limites

- `docs/VIS002C_CONTEXTUAL_MAPPING_V0_3_0.json` registra os dez contextos, superfícies, papel e autorização medida.
- `dist/vis002c-long-copy-light-v0.3.0.css` atribui a custom property somente nesses dez seletores exatos sob o tema claro.
- O manifesto fixa fonte, papel, valor, superfícies e contraste de cada contexto.
- `decisions.json` permanece byte-idêntico à fonte canônica; não há atribuição global em `:root`.
- Eyebrows, assinaturas, Viewer, outras superfícies e tema escuro não são alterados.
- O produto consome os arquivos fixados por hash em PR #241. O preview atualizado e os gates precisam passar antes de qualquer integração.
