![Methodology paper collection](assets/methodology.svg)

# Methodology

English · [简体中文](README.zh-CN.md)

Project methodology papers, technical manuscripts, and research notes from yf-official. Each entry presents its own research question, methods, publication information, and reading materials, with a link to the corresponding project when available.

[Paper library](#paper-library) · [BibTeX](references.bib) · [Contributing](CONTRIBUTING.md)

## Paper library

| Paper | Central question | Topics | Read |
| --- | --- | --- | --- |
| **[DeckStage](#deckstage)** | How can a card mockup follow reference geometry while preserving the supplied artwork? | Projective geometry · non-destructive rendering · folded packaging | [Notes](papers/deckstage/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/paper-2026-10-01/DeckStage_Methodology.pdf) |
| **[IconLab](#iconlab)** | How can interactive composition and exports at different sizes share one geometric meaning? | Affine transforms · undo transactions · supersampling | [Notes](papers/iconlab/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/iconlab-paper-2026-10-01/IconLab-methodology.pdf) |
| **[SHIYUN](#shiyun)** | How can a long-running literary interface coordinate presentation, personal libraries, and bounded resources? | State contracts · local persistence · retrieval · memory and energy | [Notes](papers/shiyun/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/shiyun-paper-2026-10-03/ShiYun-methodology.pdf) |
| **[VidAudio](#vidaudio)** | How can a native media tool make duration, finalization, permissions, and job outcomes independently reviewable? | Design contracts · temporal integrity · VBR metadata · scoped access | [Notes](papers/vidaudio/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/vidaudio-paper-2026-10-03/VidAudio-methodology.pdf) |
| **[SlideSafe](#slidesafe)** | How can presentation text become font-independent without changing its viewport or damaging surrounding objects? | OOXML style resolution · fixed-viewport rendering · geometry invariance · fail-safe replacement | [Notes](papers/slidesafe/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/slidesafe-paper-2026-10-03/SlideSafe-methodology.pdf) |
| **[Codex Usage Bar](#codex-usage-bar)** | How can a desktop quota monitor preserve meaning and freshness across changing runtimes and lifecycle events? | Quota semantics · runtime discovery · lifecycle scheduling · information age | [Notes](papers/codexusagebar/README.md) · [PDF](https://github.com/yf-official/yf-official-methodology/releases/download/codexusagebar-paper-2026-10-03/CodexUsageBar-methodology.pdf) |

### DeckStage

**Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation**<br>
Fox Studio · 22 pages · English · Technical manuscript for design review

A card scene couples physical dimensions, reference perspective, overlapping objects, and original artwork. The paper connects line-family reconstruction to a shared plane homography, render-time trimming, local rounded masks, oblique fans, and a box camera. A fold graph extends the model to packaging from one immutable artwork atlas.

**What to take away:** model the scene before styling it; preserve source artwork; make projection, visibility, hit testing, and export follow the same geometry.

**Evidence:** exact dimension checks and a controlled synthetic projective-versus-affine experiment. Reference registration, application performance, and the proposed renderer acceptance criteria still require independent validation.

[Explore the paper →](papers/deckstage/README.md) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/paper-2026-10-01)

### IconLab

**A Geometry-Consistent Method for Interactive Icon Composition and Multiresolution Export**<br>
yf-official · 8 pages · English · Technical paper

An icon editor has to connect continuous gestures to discrete raster outputs. The paper separates canonical design state, display preferences, immediate preview updates, undo transactions, and snapshot export. It formalizes coordinate reflection, affine transforms, gradients, and sampling while identifying gaps in the native baseline.

**What to take away:** share geometric semantics across preview and export; keep feedback immediate; commit meaningful undo groups; render each destination from one frozen design.

**Evidence:** synthetic coverage measurements and 30,000 coordinate checks. Native pixel parity, interaction latency, and aesthetic benefit were not measured.

[Explore the paper →](papers/iconlab/README.md) · [Project source](https://github.com/yf-official/IconLab) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/iconlab-paper-2026-10-01)

### SHIYUN

**Resource-Aware Development of Ambient Literary Interfaces: A Contract-Based Methodology**<br>
yf-official · 11 pages · English · Development-stage technical methodology manuscript

A native literary application must connect interruptible presentation, meaningful keyboard focus, personal collections, local authorship, and visual customization without accumulating unnecessary work. The paper maps requirements to owners, formal contracts, counterexamples, and acceptance observations. It covers generation-guarded transitions, bounded selection history, ingestion equivalence, prepared retrieval, shared typography, and long-running memory governance.

**What to take away:** distinguish content-dependent memory from duration-dependent retention; give tasks and caches explicit ownership and budgets; verify resource claims with controlled workloads rather than interface appearance.

**Evidence:** four synthetic selection regimes with 50,000 draws each, a 2,000-record ingestion workload, and a 16-context command-gate check. Native power measurements, memory-soak results, and user-study outcomes are not reported. Figures are original abstract schematics, not product screenshots.

[Explore the paper →](papers/shiyun/README.md) · [Project source](https://github.com/yf-official/SHIYUN) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/shiyun-paper-2026-10-03)

### VidAudio

**A Contract-Guided Development Methodology for Private Native Media-Extraction Tools**<br>
yf-official · 7 pages · English · Development-stage technical methodology manuscript

A native media tool must coordinate decoding, encoding, file access, visible state, and distributable artifacts. The paper translates those boundaries into six development contracts and a staged verification process. It distinguishes container extent, decoded sample count, coded frames, and player-reported duration, then connects VBR metadata finalization, sequential jobs, buffer demand, and scoped permissions to explicit acceptance observations.

**What to take away:** declare the timeline policy before comparing durations; distinguish finalized output from safe publication and terminal progress from successful extraction; verify complete outcomes rather than relying on one component's success.

**Evidence:** source inspection and the assertion scopes of seven existing regression tests, with analytical duration and resource examples. Independent-decoder coverage, gap reconstruction, atomic publication, relaunch permissions, and native performance remain acceptance work, not reported benchmark results. Figures are original abstract schematics and analytical plots, not product screenshots.

[Explore the paper →](papers/vidaudio/README.md) · [Project source](https://github.com/yf-official/VidAudio) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/vidaudio-paper-2026-10-03)

### SlideSafe

**Geometry-Invariant Vector-Backed Image Replacement for Portable Presentation Typography**<br>
yf-official · 5 pages · English · Development-stage technical methodology manuscript

Presentation typography can change with fonts and rendering environments even when the document remains valid. The paper combines hierarchical OOXML style resolution, exact-font eligibility, fixed-viewport glyph rendering, explicit highlights and text decorations, and object-aware replacement for text boxes, shapes, groups, and tables. The result is a vector-backed image with a raster fallback, not editable outline text.

**What to take away:** keep object geometry separate from glyph ink bounds; retain transparent margins and paragraph structure; render and validate a complete substitute before clearing source text.

**Evidence:** a four-object baseline and a 32-object synthetic typography corpus. All 30 eligible stress objects were converted, both deliberately unsupported objects were preserved, and XML comparison found zero transform mismatches in the 30 replacements. Cross-engine pixel fidelity, large-scale coverage, and performance remain unmeasured. Figures are original abstract schematics, not product screenshots.

[Explore the paper →](papers/slidesafe/README.md) · [Project source](https://github.com/yf-official/SlideSafe) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/slidesafe-paper-2026-10-03)

### Codex Usage Bar

**Codex Usage Bar: A Methodology for Lifecycle-Aware Desktop Quota Observability**<br>
yf-official · 7 pages · English · Development-stage technical methodology manuscript

A desktop quota monitor must distinguish absent windows, unknown percentages, stale observations, and unavailable hosts. The paper separates a read-only runtime adapter, typed quota semantics, lifecycle-aware acquisition, shared presentation, and window-specific alert identity. It formalizes remaining-percentage conversion, reset handling, capped backoff, receipt age, and glyph-bound centering.

**What to take away:** preserve unknown and absent states; separate executable identity from desktop-host identity and receipt age from source age; connect compact presentation and independent alerts to one observation model.

**Evidence:** 18 automated core/transport tests passed, with explicitly idealized freshness/load calculations. Long-duration memory, CPU/energy, on-device placement, and participant usability remain unmeasured. Figures are original abstract diagrams and an analytical plot, not product screenshots or account observations.

[Explore the paper →](papers/codexusagebar/README.md) · [Project source](https://github.com/yf-official/Codex-Usage-Bar) · [Versioned release](https://github.com/yf-official/yf-official-methodology/releases/tag/codexusagebar-paper-2026-10-03)

## Using and citing the collection

- **Read:** use the notes for orientation and the versioned PDF for equations, figures, and complete claims.
- **Cite:** use the individual manuscript's author, full title, year, and release URL. Copy the entries in [references.bib](references.bib); no DOI or publication venue is assigned here.
- **Reuse:** check rights per manuscript. DeckStage explicitly reserves all rights and requires permission for redistribution. IconLab, SHIYUN, VidAudio, SlideSafe, and Codex Usage Bar have no explicit manuscript reuse license in their releases. Public access alone does not grant a reuse license.
- **Extend:** follow the [contribution guide](CONTRIBUTING.md) and [paper-note template](templates/paper-notes.md). Metadata is recorded in [catalog.json](catalog.json).

## Collection structure

```text
papers/          Bilingual reading notes, section maps, and evidence boundaries
assets/          Repository artwork
templates/       Template for the next paper's notes
catalog.json     Structured publication metadata
references.bib   Citation entries for individual manuscripts
scripts/         Catalog and local-link validation
```

PDFs remain attached to their versioned GitHub Releases. Reading notes are maintained separately and do not replace or revise the published manuscripts.

## Development priorities

- Expand the collection when another project has a manuscript ready for review, using the same bilingual notes and metadata structure.
- Link reproducibility scripts and datasets when their authors publish them; the present repository distributes manuscripts and notes.
- Record revised editions as new releases and describe which claims or experiments changed.

To report a broken link, factual error, or missing explanation, [open an issue](https://github.com/yf-official/yf-official-methodology/issues/new/choose) with the paper, section, and expected correction.
