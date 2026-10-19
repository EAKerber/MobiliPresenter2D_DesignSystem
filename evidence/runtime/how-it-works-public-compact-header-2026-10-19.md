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
