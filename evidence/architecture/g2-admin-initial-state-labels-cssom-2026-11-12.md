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

The candidate uses the existing `--control-text` token and scopes it to `html[data-theme="light"] .hierarchy-item .initial-state-option`. It preserves the card background and dark-mode style. Product PR #271 is open at `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; the new Actions checks and Deploy Preview rebuild were pending when this note was written. `main` remains at `221b54b`.

## Limits

This is local runtime evidence from a generated Admin fixture, not an authenticated hosted capture. It covers the initial hierarchy state and theme pair for this label family; it does not cover focus/hover/disabled states, other routes, or the remaining #208 criteria. Keep #208 and G2 open until their broader structural, CSSOM, contrast, and hosted fixture requirements are satisfied.
