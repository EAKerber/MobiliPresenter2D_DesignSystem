# Runtime follow-up: public compact header and settled light-theme logo

**Route:** [https://casaemmodulos.casa/how-it-works/](https://casaemmodulos.casa/how-it-works/)  
**Observed:** 2026-10-19 · **Theme:** light for visual review  
**Browser viewport:** 486 × 590 CSS px; `window.innerWidth=486`, `documentElement.clientWidth=471`  
**Scope:** read-only DOM, computed style, accessibility tree and visual observation. The currently deployed product commit was not independently identified during this visit.

## NAV-005 compact header

At 486 CSS px, the header box measured 470.67 × 77.93 px. The brand image remained at 160 × 57.26 px from x=14. The right controls were:

- WhatsApp CTA: 38 × 38 px at x=316.67, outside the menu.
- Theme control: 44 × 44 px at x=362.67, icon-only, with an accessible name that stated the current and next theme.
- Hamburger: 42 × 42 px at x=414.67.

The hamburger opened on the first click. Its navigation contained **Ambientes**, **Como funciona**, and **Quem somos**. No contact or WhatsApp entry appeared in the expanded navigation; the WhatsApp CTA remained outside it.

Same-origin stylesheet rules explain the current arrangement:

- `landing.css` hides the public nav at `max-width: 900px`, and shows it when the menu opens.
- `ui-theme.css` applies icon-only to `.site-header .ui-theme-toggle--header` through `max-width: 1150px`, hiding the short label. At 486 px the logo had not been reduced.
- `landing.css` converts `.header-cta` to icon-only at `max-width: 520px`.

This conflicts with the approved compact NAV-005 behavior: keep public contact access inside the hamburger menu, and retain the theme label while reducing the logo by no more than 30%, switching to icon-only only when that reduction is insufficient. The product correction is tracked at [MobiliPresenter2D issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218).

## FIND-011 settled logo review

After the light-theme transition settled at 486 × 590, the logo was visibly dark and legible against the light header. The image source was `/branding/logo-light-380.png`; computed opacity was 1 and filter was `none`. The washed-out appearance was seen only in an earlier transition frame and did not recur in the settled state. No stable logo contrast defect was confirmed. A numeric text-color ratio is not applicable to the raster image; its specific non-text contrast was not measured.

## Evidence limits

No raster screenshot was persisted in this repository for this follow-up; the observation is recorded from the live screenshot and read-only DOM. The current deployment commit was not identified, and behavior at other compact widths was not tested in this follow-up. The earlier dark-theme browser preference was restored and the menu was left closed. No account data, product settings, or product code were changed.


## Follow-up narrow-width sweep (2026-10-19, dark theme)

The same public route was checked at 360, 340, 321, 320, 291 and 290 CSS px. The theme remained icon-only at every sample. The logo measured 129.6 px at 360, 122.4 px at 340, and the 120 px minimum from 321 downwards. Thus the icon-only rule activates while the logo remains at or above 75% of its 160 px reference size; at 321 px, NAV-005 says the theme label should still remain visible.

At 291 and 290 px, `html` and `body` had `min-width: 320px`; `.how-page` had `overflow-x: clip`. The page stayed in a 320 px, one-row header instead of wrapping. At 290 px, the document client width was 275 px and scroll width 320 px; the menu target starts at x=264 and extends to x=306, leaving only 11 px visible inside the document client area. The screenshot also showed clipped heading text. The hamburger remains in the DOM and has an accessible name, but most of its visual hit target is outside the clipped area.

These measurements add a second compact-header defect to [product issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218): current public layout clips content below the 320 px minimum and does not switch to the approved two-row fallback below approximately 291 px. Exact behavior between sampled widths remains unmeasured. No raster screenshot was saved for this sweep.
