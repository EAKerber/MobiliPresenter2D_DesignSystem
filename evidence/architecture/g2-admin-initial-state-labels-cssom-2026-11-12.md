# G2 Admin initial-state labels — local CSSOM recheck (2026-11-12)

**Disposition:** the light-mode finding reproduces on the pinned Product `main`; the dark-mode pair passes. A narrow candidate rule is on Product PR #271 and passes this local fixture. This subcase does not close #208 or G2.

## Pin and method

- Product source: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`.
- Browser: Chrome 156.0.8078.82, headless, DPR 1, viewport 1036×582 CSS px.
- A self-contained local fixture was assembled from the pinned `app/admin.html`, its actual CSS and classic scripts, and the actual `app/admin/admin.js` module. The V5 admin configuration was generated from repository defaults. The Identity boundary and the configuration fetch were stubbed locally; no credentials, remote services, database, or writes were used.
- The real hierarchy renderer created 18 `.initial-state-option` labels. CSSOM captured computed foreground, font size, and each ancestor background; the resulting background composition had no image, filter, opacity, blend, or backdrop-filter caveat.

## Source and cascade

The pinned source blobs were:

| Product path | Git blob |
|---|---|
| `app/admin.html` | `28e57028e235944dfd581820ed90078866af93bc` |
| `app/admin/admin.js` | `79925345e43096df77bef54fe257e483f922edd8` |
| `app/admin/admin.css` | `1b3b41e166d44dbf70c1096db36255398aff8493` |
| `app/ui-theme.css` | `3114bbfe0a67cbdc53757f5f50a0d035559767a6` |

`app/admin.html` loads `admin.css` before `ui-theme.css`. The renderer creates the label in `admin.js:234`; `admin.css:107` sets `color:var(--muted)` and `font-size:10px`. In light mode the later shared theme sheet resolves `--muted` to `#706C66` and gives `.hierarchy-item` a 3% dark overlay. That overlay sits on the opaque `#F0EDE8` hierarchy section, so the label's effective background is `#EAE7E2`; the earlier Admin light rule setting a white card is superseded by the later theme rule.

## Results

| State | Foreground | Effective background | Ratio | Issue #208 threshold |
|---|---|---|---:|---:|
| Product `main`, light | `#706C66` | `#EAE7E2` | **4.229:1** | 4.5:1 — fail |
| Product `main`, dark | `#C4BCB2` | `#232321` | **8.384:1** | 4.5:1 — pass |
| PR #271 candidate, light | `#403A34` | `#EAE7E2` | **9.092:1** | 4.5:1 — pass |

The candidate uses the existing `--control-text` token and scopes it to `html[data-theme="light"] .hierarchy-item .initial-state-option`. It preserves the card background and dark-mode style. Product PR #271 remains open at `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; all nine PR-triggered Actions runs and the Netlify Deploy Preview status succeeded for that head.

## Authenticated hosted review — Preview #271 Admin (2026-11-12, BRT)

The user authenticated in the exact Preview host. At viewport 634×652 CSS px / DPR 1.5, the real hierarchy showed 18 `.initial-state-option` labels. All 18 had visible layout boxes and enabled, already-checked checkboxes. No checkbox was changed and nothing was saved. The CSSOM resolved the candidate light label to `rgb(64,58,52)` (`#403A34`) over the unchanged composited background `rgb(234,231,226)` (`#EAE7E2`), **9.092:1**. Dark remained `rgb(196,188,178)` (`#C4BCB2`) over `rgb(35,35,33)` (`#232321`), **8.384:1**. The card surface, checkbox state, and dark result stayed unchanged. The theme was restored to dark after light/dark review. No page console warning/error was observed.

The active Admin stylesheet is Product PR #271 `app/admin/admin.css`, Git blob `81b115d4a15409d5c46ba5590a19ef587d785a0f`; the candidate selector is the one above. Source order remains `admin.css` then `ui-theme.css` in `app/admin.html`, with labels created by `app/admin/admin.js`. Session screenshot SHA-256 values: light `3b3966d1f2ccf900d1cb74a7401de302bedde8ff249ecb7195fcac2457b6b536`; dark `c5e9357d940110aebc264479aac001286efcfc76e9bf83e7beadc148f2c477fa`. The image bytes were reviewed in-session and are not stored in this repository.

This passes only the hosted Admin initial-state-label subgate. `/config/` still reports invalid published configuration; other labels, routes and states, focus/hover/disabled behavior, and remaining #208 criteria are outside this review. Product `main` remains at `221b54b`.

## Limits

The combined local and hosted evidence covers only the initial hierarchy state and this label family in light/dark. It does not cover focus/hover/disabled states, other routes, or the remaining #208 criteria. Keep #208 and G2 open until the broader structural, CSSOM, contrast, and hosted-fixture requirements are satisfied.
