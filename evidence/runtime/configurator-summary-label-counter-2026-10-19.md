# Runtime evidence: configurator summary label and included-item counter

**Route:** [https://casaemmodulos.casa/config/](https://casaemmodulos.casa/config/)  
**Observed:** 2026-10-19 · **Viewport:** 1280 × 720 CSS px  
**Themes:** dark and light, read-only  
**Scope:** DOM/accessibility-tree state and computed contrast. The deployed product commit was not independently identified during this visit.

## Counter and summary state — FIND-006

On initial load at the Módulos stage, the seven list inclusion controls #toggle-module-01 through #toggle-module-07 each reported Value=1 and their list rows said “Incluído”. The viewer counter displayed **8 de 8 itens incluídos**, and the estimated composition value was **R$ 8.740,00**.

Without clicking any inclusion checkbox, I selected the **Resumo** stage. The summary then said **“Nenhum módulo incluído.”**, showed **0 incluído(s)** and **R$ 0,00**. The viewer counter still displayed **8 de 8**.

The contradiction was reproduced during the transition. The state change coincided with stage navigation, so this observation does not isolate whether a selection reset, separate state source, stale count, or another cause produced it. No selection was intentionally changed and nothing was saved.

## Light-theme contrast — FIND-010 / DS04-07

The label **Módulos** in the summary resolves to .price-state__breakdown dt. The loaded stylesheet styles.css?v=runtime-v40 applies the same declaration in both themes:

    .price-state__breakdown dt {
      color: rgba(255, 255, 255, 0.68);
      font-size: 11px;
      font-weight: 750;
    }

In light mode, #summaryPanel had rgb(255, 255, 255); its child .price-state had rgba(203, 188, 170, 0.13). Compositing those values gives an approximate background of rgb(248.24, 246.29, 243.95). The translucent white text composites to rgb(252.84, 252.21, 251.46), for a calculated contrast of **1.05:1**. The 11 px label appears nearly white on the light card and fails the 4.5:1 threshold for normal text.

In dark mode the same selector and foreground were rgba(255, 255, 255, 0.68) over panel rgb(27, 28, 26) with the same rgba(203, 188, 170, 0.13) overlay. The composed pair measured **6.95:1**. This is a confirmed light-theme contrast defect, separate from the disabled lighting treatment already reviewed under FIND-010.

## Backlog and limits

The functional mismatch is tracked in [MobiliPresenter2D issue #209](https://github.com/EAKerber/MobiliPresenter2D/issues/209); the light summary-label contrast is tracked in [issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208). Both issues received this runtime follow-up.

The screenshot was inspected but no raster image from this visit was persisted. The measurements are read-only computed DOM values; the ratio is an exploratory WCAG calculation, not an independent certification. The live deploy commit was not identified. No product code, account data, or module inclusion was edited or saved; the temporary theme change was restored to dark.