# Runtime evidence: services and disabled lighting in the configurator

**Observed route:** `https://casaemmodulos.casa/config/`  
**Observed date:** 2026-10-19  
**Theme / viewport:** dark / 1280 × 720  
**Scope:** read-only visual and accessibility-tree observation.

## Captured state

After moving from Módulos to Serviços, the visible summary showed “8 de 8 itens incluídos” and an estimated value of `R$ 0,00`. The accessibility tree showed all seven module checkboxes with `Value=0`. The lighting checkbox was disabled and unchecked; its helper text says that the refrigerator side and sink upper module are required.

The initial accessibility snapshot, before opening Serviços, had shown the seven module checkboxes with `Value=1`. Their values changed alongside the stage navigation. This confirms a contradictory state during the visit, but it does not establish whether the initial snapshot was stale, the stage transition reset the selection, or another cause. Persistence after reload was not checked.

## Disabled-control styling

The lighting label was `.service-check.is-blocked` with computed opacity `0.6`. The checkbox reported `disabled=true` and `checked=false`. The current dark muted token was `rgba(255, 255, 255, 0.48)`; the row border was `rgba(255, 255, 255, 0.1)`.

The current opacity is the measured implementation. Alternative values and the secondary-text treatment in [FIND-010-disabled-control-candidates.svg](../../visualEvidence/experiments/FIND-010-disabled-control-candidates.svg) are visual experiments only. Their contrast ratios are calculated over the solid reference surfaces displayed on the board, not measured from the page's composed DOM.

## Evidence limits

The browser screenshot was inspected during the session, but no raster capture is stored in this repository. The linked SVG is an experimental comparison, not a screenshot. No module selection was intentionally changed or saved, no account data was modified, and no product code was changed.
