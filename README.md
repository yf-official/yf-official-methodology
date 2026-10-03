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

## Using and citing the collection

- **Read:** use the notes for orientation and the versioned PDF for equations, figures, and complete claims.
- **Cite:** use the individual manuscript's author, full title, year, and release URL. Copy the entries in [references.bib](references.bib); no DOI or publication venue is assigned here.
- **Reuse:** check rights per manuscript. DeckStage explicitly reserves all rights and requires permission for redistribution. IconLab and SHIYUN have no explicit manuscript reuse license in their releases. Public access alone does not grant a reuse license.
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
