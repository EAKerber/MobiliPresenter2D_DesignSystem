# Public access route — keyboard focus in the invalid-link state

**Date:** 2026-10-24  
**Production:** Netlify deploy 6adc221479c773577ed45e23, READY, main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf.  
**Route:** /access/, anonymous isolated browser context, CSS viewport 390 × 844, DPR 1.

## Observed state

The route showed “Confirmar acesso ao configurador” and the message that the link was not valid. No access token, email, or user session was supplied. The “Confirmar e continuar” control was hidden; no form was filled and no access action was submitted.

Visible keyboard targets were the brand link, theme toggle, menu toggle and “Voltar ao início”. The menu stayed closed. The route had no horizontal overflow (scrollWidth=clientWidth=390).

## Focus appearance

I traversed the visible controls by Tab in the light theme, then switched the isolated route through Claro and Escuro and checked each control in :focus-visible without activating it. All four controls showed a computed outline; the rounded width was 2.66667 px.

- **Light:** outline color rgb(110, 81, 46) (approximately #6E512E). The brand, menu and back link used 2.66667 px offset. The theme toggle used 2 px offset.
- **Dark:** outline color rgb(216, 188, 124) (#D8BC7C). The same 2.66667 px computed width and offsets persisted: 2.66667 px for brand/menu/back, 2 px for the theme toggle.
- No focus shadow was present. The Confirmar e continuar action was not visible and was not tested.

## Limits and cleanup

This covers only the anonymous invalid-link state at one mobile viewport and two themes. It does not evaluate a valid access link, any authenticated Configurator/Admin state, other dimensions, or broader conformance. A valid fixture or authorized session is still required for those states.

The theme was restored to Automático, the temporary isolated tab was closed, and the original browser tab was selected again. No input was submitted, no credentials or token were read, and no product code or user data changed.