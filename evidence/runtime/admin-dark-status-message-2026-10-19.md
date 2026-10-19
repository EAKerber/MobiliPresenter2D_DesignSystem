# Runtime evidence: administrative status message

**Observed route:** `https://casaemmodulos.casa/admin.html`  
**Observed theme:** dark  
**Observation date:** 2026-10-19  
**Purpose:** inspect the rendered semantic-message state without changing product data or settings.

## Observation

The authenticated administration page was fully loaded. One visible `.message` element had `aria-live="polite"`, an empty `data-kind`, and no explicit semantic state. Its visible content confirmed that the configuration had loaded and could be published after validation.

- Foreground: `#C4BCB2` (computed `rgb(196, 188, 178)`)
- Effective background: `#111210` (computed `rgb(17, 18, 16)`)
- Font size: `13px`
- Calculated text contrast: `10.00:1`
- The element's own background is transparent.
- Two other `.message` elements were not visible in this state.

The measured contrast exceeds WCAG AA for ordinary text in this observed state. This does not establish the contrast or appearance of other message types, light theme, or other surfaces.

## Approved classification

The user confirmed that this message derives from the current state, rather than from an action just performed. It is therefore **process information**, not a success confirmation. The user selected option A in the VIS-002 review, approving these contextual text pairs:

- Light: `#245D87` on `#F0EDE8` — `6.01:1`.
- Dark: `#A7D1F0` on `#211F1C` — `10.19:1`.

The live dark Admin message still renders as `#C4BCB2` on `#111210` (`10.00:1`). Its contrast is sufficient in this observed state, but its color does not use the approved blue pair. Product implementation remains pending and was not performed in this audit. The approval does not establish global tokens or approve other surfaces, backgrounds, borders, or icons.

## Limits

This was a read-only DOM inspection of one live dark-theme state. No error or warning was triggered, the theme was not changed, and no account or catalog content was recorded. No screenshot was captured because this state did not present a visual alternative requiring aesthetic review.
