# VIS-002C cascade winner trace — 2026-11-10

## Source pin and capture method

- Product source: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; local detached worktree was clean at capture.
- Browser: Chrome 156.0.0.0 through Chrome DevTools; viewport 766×608 CSS px, DPR 1.5.
- The original HTML routes were opened from local `file://` URLs. Their root-relative stylesheet URLs cannot resolve as they do over HTTP, so the exact source CSS files from the pinned `app/` tree were loaded directly in their page order. The v0.3 token stylesheet was included before the consuming page stylesheet, matching its production import position. The Landing page's `data.js` and `landing.js` were also loaded from the pinned files to populate the dynamic feature description.
- The HTML body and target DOM elements were retained. Chrome DevTools' matched-style panel reported the active declarations and overridden declarations. Computed foregrounds, nearest opaque section backgrounds, theme state, opacity, filter, and backdrop-filter were read from the live DOM. The `landing.css` absolute `@import` did not load under `file://`; its exact v0.3 stylesheet was therefore loaded directly.
- This is a local source trace. It is not an HTTP, Netlify, CDN, full production-route, or hosted-preview capture.

## Ten mapped v0.3 contexts

| Route / selector | Matched elements | Light winning rule | Previous/base light rule | Dark winning rule |
|---|---:|---|---|---|
| `/` · `.hero-description` | 1 | `landing.css:209` → v0.3 token `#292723` | `landing.css:53` → `#705C4B` (overridden) | `landing.css:52` → `var(--public-muted)` |
| `/` · `.story-section > p:not(.eyebrow)` | 1 | `landing.css:209` → v0.3 token `#292723` | `landing.css:130` → `var(--public-muted)` (overridden) | `landing.css:130` → `var(--public-muted)` |
| `/` · `.environment-feature .feature-copy > p:not(.eyebrow):not(.feature-availability)` | 1 | `landing.css:209` → v0.3 token `#292723` | `landing.css:109` → `var(--public-muted)` (overridden) | `landing.css:109` → `var(--public-muted)` |
| `/how-it-works/` · `.how-hero-note` | 1 | `how-it-works.css:312` → v0.3 token `#292723` | `how-it-works.css:296` → `#705C4B` (overridden) | `how-it-works.css:7` → `var(--public-muted)` |
| `/how-it-works/` · `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | 1 | `how-it-works.css:312` → v0.3 token `#292723` | `how-it-works.css:98` → `var(--public-muted)` (overridden) | `how-it-works.css:98` → `var(--public-muted)` |
| `/how-it-works/` · `.commercial-clarity > p:not(.eyebrow)` | 2 | `how-it-works.css:312` → v0.3 token `#292723` | `how-it-works.css:290` → `var(--public-muted)` (overridden) | `how-it-works.css:290` → `var(--public-muted)` |
| `/how-it-works/` · `.launch-card .launch-copy > p` | 1 | `how-it-works.css:312` → v0.3 token `#292723` | `how-it-works.css:50` → `var(--public-muted)` (overridden) | `how-it-works.css:50` → `var(--public-muted)` |
| `/about/` · `.about-scale p:not(.eyebrow)` | 3 | `about.css:54` → v0.3 token `#292723` | `about.css:50` → `#705C4B` (overridden) | `about.css:18` → `var(--public-muted)` |
| `/about/` · `.about-scale__stat > span` | 1 | `about.css:54` → v0.3 token `#292723` | `about.css:23` → `var(--public-muted)` (overridden) | `about.css:23` → `var(--public-muted)` |
| `/about/` · `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | 2 | `about.css:54` → v0.3 token `#292723` | `about.css:18` → `var(--public-muted)` (overridden) | `about.css:18` → `var(--public-muted)` |

The ten mapped selectors matched **14 elements** across the three routes. In light mode each resolved to `rgb(41, 39, 35)` / `#292723`, with the v0.3 token defined by `vis002c-long-copy-light-v0.3.0.css:6`. Dark mode retained `rgb(196, 188, 178)` / `#C4BCB2` through the existing `--public-muted` rules.

| Surface/context | Light background and contrast | Dark background and contrast |
|---|---|---|
| Landing hero, feature, How-it-works, About | `#F0EDE8`; **12.7658:1** | `#20211F`; **8.6109:1** |
| Landing story section | `#E8E3DC`; **11.6785:1** | `#20211F`; **8.6109:1** |

## Contextual exception

| Route / selector | Matched elements | Light winning rule | Dark winning rule |
|---|---:|---|---|
| `/how-it-works/` · `.study-band .eyebrow` | 1 | `how-it-works.css:297` → `#70522F` | `.eyebrow` in `landing.css:48` → `var(--public-accent)` = `#D8BC7C` |

The exception resolves against `#E8E3DC` at **5.6019:1** in light mode and `#20211F` at **8.7809:1** in dark mode. It is not one of the ten long-copy token contexts.

## Reading the result

The expanded trace closes the **local winner-attribution subgate** for the ten mapped v0.3 selectors and checks the separately approved study-band eyebrow exception. It confirms that v0.3 wins for all ten mapped contexts in light mode, legacy light declarations are overridden where present, and dark mode remains on the existing muted/accent colors.

The capture did not establish current CDN bytes, HTTP stylesheet ordering, whole-page visual acceptance, all breakpoints or interaction states, device behavior, or global accessibility. The contrast ratios are recalculated from computed CSS colors and the nearest opaque section background; they are not pixel sampling or a complete accessibility audit. Local file URLs and direct stylesheet loading remain material limitations. Issue #216 and G2 stay open pending its remaining acceptance criteria and the separate `/config/`, #208, and DS-05A work.
