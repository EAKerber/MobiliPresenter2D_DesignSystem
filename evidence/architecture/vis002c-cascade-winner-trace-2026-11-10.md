# VIS-002C cascade winner trace — 2026-11-10

## Pin and method

- Product source: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; detached worktree was clean at capture.
- Browser: Chrome 156.0.0.0 through Chrome DevTools; viewport 766×608 CSS px, DPR 1.5.
- The original route HTML was opened from local `file://` URLs. Because its root-relative stylesheet URLs resolve to the drive root under `file://`, the three source pages used the exact CSS files from the pinned `app/` directory, linked in their production order. The v0.3 token stylesheet was loaded separately immediately before Landing CSS to reproduce its `@import` position. The HTML body and target elements were not rewritten.
- `get_css_styles` identified the active declaration and listed overridden declarations. In light mode the token value was also read from `getComputedStyle`; in dark mode the light-only token was absent. The same page DOMs were inspected in explicit `data-theme=light/dark` states.
- This is a local source-cascade trace. It is not an HTTP/Netlify/CDN capture; the browser’s file-scheme path workaround and the failed absolute `@import` request mean it must not be described as a full production-route runtime test.

## Results

| Route / selector | Matches | Light winning foreground rule | Previous light declaration | Dark winning foreground rule |
|---|---:|---|---|---|
| `/` · `.hero-description` | 1 | `landing.css:209` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `landing.css:53` — `#705C4B` (overridden) | `landing.css:52` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |
| `/how-it-works/` · `.how-hero-note` | 1 | `how-it-works.css:312` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `how-it-works.css:296` — `#705C4B` (overridden) | `how-it-works.css:7` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |
| `/about/` · `.about-scale p:not(.eyebrow)` | 3 | `about.css:54` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `about.css:50` — `#705C4B` (overridden) | `about.css:18` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |

All three contexts produced identical computed colors per theme:

| Theme | Computed foreground | Computed background | CSSOM-derived contrast |
|---|---|---|---:|
| Light | `rgb(41, 39, 35)` / `#292723` | `rgb(240, 237, 232)` / `#F0EDE8` | **12.7658:1** |
| Dark | `rgb(196, 188, 178)` / `#C4BCB2` | `rgb(32, 33, 31)` / `#20211F` | **8.6109:1** |

The About selector matched three paragraphs; all three retained the same color, token, background and ratio. The ancestor background inspection found no image, filter, opacity, blend or backdrop-filter caveats for these targets.

## Scope and limits

This resolves the missing **winner-attribution subgate** for the three originally captured #216 consumers in the pinned source, across light and dark. It confirms that the v0.3 token wins in the three light contexts, the former `#705C4B` declarations lose there, and dark text still resolves through the original `--public-muted` rule.

It does **not** close issue #216 or G2. The issue’s `.study-band .eyebrow` and the later five additional contexts are not part of this trace; `/config/` remains a separate 98-pair UNCERTAIN analysis; the trace does not prove current CDN bytes, a whole-page visual review, device behavior, or global accessibility. Existing six screenshots and the earlier CSSOM receipt remain the evidence for their stated limits.
