# VIS-002C — separação contextual para textos longos (candidata v0.3)

**Data:** 2026-10-24. **Estado:** proposta versionada em branch; autorização do usuário limitada aos contextos medidos. Não integrada à main, ao produto ou à decisão canônica.

## Direção

Para texto corrido e longo, usar cores próximas de preto no tema claro e próximas de branco no tema escuro, conforme a superfície. Esta versão trata somente os sete contextos medidos abaixo no tema claro. A implementação escura permanece intocada.

A proposta reutiliza o papel existente `VIS-002.approvedPalette.colors.textPrimary.light` (`#292723`) em vez de criar uma nova cor ou mudar a paleta. Não altera os três contextos anteriores da v0.2, que continuam com `textSecondary.light` (`#705C4B`).

## Contextos medidos e contraste

| Rota | Seletor | Fundo | Texto | Contraste |
| --- | --- | --- | --- | ---: |
| / | `.story-section > p:not(.eyebrow)` | `#E8E3DC` | `#292723` | 11,68:1 |
| / | `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /about/ | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /about/ | `.about-scale__stat > span` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.commercial-clarity > p:not(.eyebrow)` | `#F0EDE8` | `#292723` | 12,77:1 |
| /how-it-works/ | `.launch-card .launch-copy > p` | `#F0EDE8` | `#292723` | 12,77:1 |

## Artefatos e limites

- `docs/VIS002C_CONTEXTUAL_MAPPING_V0_3_0.json` registra papel, seletores e superfícies.
- `dist/vis002c-long-copy-light-v0.3.0.css` atribui somente uma custom property nos cinco seletores exatos.
- O manifesto fixa fonte, papel, valor e pares medidos.
- `decisions.json`, v0.2, outros seletores, cores de eyebrow, superfícies, Viewer e tema escuro não são alterados.
- A autorização para corrigir os contextos medidos não equivale a autorização global. Integração no produto permanece separada.
- O artefato ainda requer verificação automatizada e revisão do preview antes de qualquer integração.
