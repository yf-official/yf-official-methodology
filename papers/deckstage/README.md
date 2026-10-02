# DeckStage

English · [简体中文](README.zh-CN.md) · [Back to the collection](../../README.md)

## Publication

**Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation**

| Field | Value |
| --- | --- |
| Author | Fox Studio |
| Published | October 1, 2026 |
| Format | English technical manuscript for design review, 22 pages |
| Release | `paper-2026-10-01` |
| Topics | Projective geometry, immutable artwork, card fans, occlusion, camera priors, folded packaging |

[Read PDF](https://github.com/yf-official/yf-official-methodology/releases/download/paper-2026-10-01/DeckStage_Methodology.pdf) · [Release details](https://github.com/yf-official/yf-official-methodology/releases/tag/paper-2026-10-01) · [BibTeX](../../references.bib)

These notes summarize the released manuscript. They are not a separate paper or a claim that its proposed system has been completed.

## The problem

A plausible mockup must satisfy two constraints together: the scene follows the reference composition, and the original design survives unchanged. Independently rotating rectangles can approximate the arrangement while losing shared perspective. Repainting artwork can preserve the scene's appearance while changing text, suits, or other design details.

The paper treats the mockup as a geometric scene with immutable image inputs. Sampling, physical trimming, masking, projection, illumination, and composition are explicit operations on those inputs.

## Method in five steps

1. **Recover the supporting plane.** Fit two construction-line families, establish line pairing, recover intersections, and estimate one homography for the repeated lattice. Diagnose full-field residuals rather than judging one central cell.
2. **Separate artwork from manufactured size.** A 67 × 90 mm artwork canvas becomes a 63 × 88 mm card through normalized render-time trimming. The crop removes 2 mm from each side and 1 mm from top and bottom; it does not stretch the artwork or overwrite the source.
3. **Construct masks and poses locally.** Rounded boundaries follow the card's local geometry through projection. Fan reconstruction distinguishes observed trim edges, printed edges, assembly silhouettes, and inferred hidden boundaries. An oblique camera, finite layers, and visibility determine the exposed result.
4. **Connect the box to the same camera.** A six-face cuboid uses declared dimensional and intrinsic priors. A packaging extension partitions one immutable atlas into panel domains and connects them with rigid carried hinges, with explicit assumptions for the notch and inserted tongue.
5. **Use the model for interaction and export.** Direct-drop assignment uses inverse mapping and visible-object ownership. Export re-renders from source artwork at the requested dimensions, with declared alpha, color, and shadow policies.

## Section map

| Sections | Read for |
| --- | --- |
| I–III | Scope, coordinate systems, and the scene contract |
| IV–V | Line extraction, shared plane estimation, residual control |
| VI–VII | Physical trimming, rounded masks, fan reconstruction and occlusion |
| VIII–IX | A shared box camera and fold-aware packaging from one atlas |
| X–XII | Rendering, direct artwork assignment, template state, and export |
| XIII–XIV | Reproducible evaluation, validation targets, limitations |
| XV | The resulting construction and implementation decisions |

## What the evidence establishes

The physical crop is an exact consequence of the declared dimensions. For example, 670 × 900 artwork has a 630 × 880 retained region with 20-pixel side bleed and 10-pixel top/bottom bleed. This arithmetic does not by itself validate a renderer's crop orientation or its source preservation.

The synthetic geometry study uses a fixed seed, **200 trials per noise level**, four perturbed fitting corners, and **100 interior holdout points**. At **1 px corner noise**, Table VII reports mean holdout RMSE of **1.041 px** for the projective fit and **10.243 px** for the affine approximation in the 1600-pixel reference coordinate system.

Those values demonstrate model mismatch for the specified synthetic geometry. They are not measured accuracy on an independently annotated reference image, and they are not application performance results. Table VIII's renderer and interaction pass conditions are proposed validation targets.

## Open questions to carry into implementation

- Verify peripheral line pairing and gap dimensions using independent annotations.
- Declare camera priors and thickness assumptions before interpreting a recovered 3D pose.
- Test asymmetric face textures, source-byte preservation, crop orientation, alpha edges, and depth-owned drag targets.
- Review tongue exposure, insertion clearance, and rigid-fold assumptions against real packaging.
- Measure export time and peak memory on stated hardware after implementation.

The manuscript describes associated numerical materials, but the current release attaches only the PDF. No runnable reproduction bundle is supplied by this collection.

## Citation and rights

Fox Studio. *Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation*. Technical manuscript for design review, 2026. Release `paper-2026-10-01`. BibTeX key: `foxstudio2026deckstage`.

The manuscript states: © 2026 Fox Studio. All rights reserved. Redistribution requires permission. Use the official release link when sharing the paper.
