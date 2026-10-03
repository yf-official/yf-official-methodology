# SlideSafe

English · [简体中文](README.zh-CN.md) · [Back to the collection](../../README.md)

## Publication

**Geometry-Invariant Vector-Backed Image Replacement for Portable Presentation Typography**

| Field | Value |
| --- | --- |
| Author | yf-official |
| Released | October 3, 2026 |
| Format | English development-stage technical methodology manuscript, 5 pages |
| Release | `slidesafe-paper-2026-10-03` |
| Contents | 18 numbered equations, 4 original schematic figures, 1 table, 12 references |
| Topics | OOXML style resolution, font eligibility, fixed-viewport typography, SVG composition, object-aware rewriting, fail-safe processing |
| Edition | Author-marked PDF with a `yf-official` watermark |

[Read PDF](https://github.com/yf-official/yf-official-methodology/releases/download/slidesafe-paper-2026-10-03/SlideSafe-methodology.pdf) · [Project source](https://github.com/yf-official/SlideSafe) · [Release details](https://github.com/yf-official/yf-official-methodology/releases/tag/slidesafe-paper-2026-10-03) · [BibTeX](../../references.bib)

These notes describe the released manuscript, not an audit of later application versions. IEEE-style typesetting does not make this an IEEE publication, a peer-reviewed article, or an assigned-DOI contribution. The release date records public availability, not a claimed historical development date. Figures are original abstract diagrams, not finished-product screenshots or private presentation content.

## The problem

A presentation can remain structurally readable while its typography changes under another font environment. Font substitution affects glyph shape and line breaking; trimming a replacement to visible ink can change its size and placement; replacing a text-bearing shape indiscriminately can remove its fill or border.

The paper asks how to freeze eligible typography while preserving the surrounding presentation package and the original object's geometry. The output is a **vector-backed image with a raster compatibility fallback**, not editable PowerPoint outline text.

## Method in five steps

1. **Resolve the style cascade.** Combine theme, master, layout, shape, list, paragraph, and run properties. Resolve exact fonts, including known naming aliases; an unrelated fallback does not satisfy eligibility.
2. **Keep the original viewport.** Copy offsets, extents, rotation, and flip state exactly. OOXML positions use EMU; 12,700 EMU equals one typographic point. Retain transparent margins, empty paragraphs, and paragraph metrics rather than trimming to glyph bounds.
3. **Render complete run appearance.** Compose highlights behind glyph paths, then explicit underline, double-underline, and strikeout paths. Retain color and opacity; supported gradients, outlines, vertical modes, and warps use declared rendering policies. Auto-fit is reflow-aware and changes internal layout, not the object transform.
4. **Respect object semantics.** Replace a plain text box in its stacking position. For a text-bearing shape, retain its nontext carrier and add a text-only overlay. Preserve group structure. Treat a table as one conversion unit: a table-sized text SVG and a cleared native table share a group, keeping borders and cell geometry.
5. **Validate before mutation.** Render vector and fallback resources, validate geometry, create package relationships, and insert the substitute before clearing source text. Missing fonts and unsupported features remain editable review items. The final package is written to a new output path.

## Section map

| Sections | Read for |
| --- | --- |
| I | Portability problem, transformation scope, and contributions |
| II | Object model, exact geometry invariant, and proposed visual metric |
| III-A–B | Package pipeline, hierarchical style resolution, and font eligibility |
| III-C–D | Fixed-viewport layout, reflow-aware auto-fit, glyphs, highlights, decorations, and warps |
| III-E–IV | Object-specific rewrite rules and fail-safe mutation protocol |
| V | Acceptance criteria, synthetic regression results, and recommended visual evaluation |
| VI–VIII | Trade-offs, limitations, development gates, and conclusion |

## A transferable distinction: viewport geometry is not glyph ink

The hard invariant is equality of the original and replacement geometry tuples: x, y, cx, cy, rotation, and both flip flags. Transparent regions inside a text box are part of its layout, even when no glyph occupies them. Internal glyph placement can change without changing the enclosing picture transform; trimming to an ink bounding box confuses these two coordinate systems.

This separation is also an evidence boundary: zero XML transform differences do **not** prove identical line breaks, glyph positions, or rendered pixels. The proposed SSIM, CIEDE2000, and edge-displacement metric evaluates visual fidelity separately and cannot compensate for a changed transform.

## What the evidence establishes

Table I reports development-stage regression on two synthetic corpora:

| Corpus | Text objects | Eligible | Converted | Preserved |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 4 | 3 | 3 | 1 |
| Typography stress | 32 | 30 | 30 | 2 |

The stress corpus deliberately includes an unresolved font and an unsupported shape-level effect. Both were preserved. XML-level comparison of the **30 eligible replacements** found **zero mismatches** in offsets, extents, rotation, and flip state. Generated SVGs were checked for expected paint colors, a gradient definition, and a stroked outline; package decompression and relationship checks completed without structural errors.

These are small synthetic conformance checks, not a large-scale visual benchmark, user study, timing measurement, or exhaustive proof of rollback safety. The broader appearance criteria and mutation protocol describe the method and its acceptance targets; the reported counts do not independently establish every feature across all presentation engines.

## Remaining acceptance work

Cross-engine render comparisons, script-specific layout review, decorative-warps coverage, malformed-package tests, and failure injection require broader verification. The manuscript recommends median and 95th-percentile SSIM, color differences, line-break agreement, and edge displacement; those cross-engine measurements are **not reported results**.

Converted image text loses text editing, selection, search, and accessibility semantics. Preserved hyperlink styling does not by itself preserve the click action. Missing fonts, unsupported warps and effects, per-character animations, equations, SmartArt, and charts remain outside the supported conversion scope. Color management, antialiasing, SVG support, and fallback selection can still differ between consumers.

This release distributes the selected watermarked PDF only. No test decks, private paths, application bundle, product screenshots, or separate reproduction dataset are attached. The application repository is linked separately; the manuscript's exact synthetic reproduction materials are not bundled with this release.

## Citation and integrity

yf-official. *Geometry-Invariant Vector-Backed Image Replacement for Portable Presentation Typography*. Development-stage technical methodology manuscript, 2026. Release `slidesafe-paper-2026-10-03`. BibTeX key: `yfofficial2026slidesafe`.

SHA-256 of the released PDF:

```text
6ccfda4e20bbeee7e67bcba317602e5cff7dbceca420b5f2a2c0fa0b95c7cf4c
```

## Rights

No explicit manuscript reuse license is specified. Public reading access and an author watermark do not establish a reuse license; consult the author before redistribution or adaptation. Application-source rights are separate.
