# Shared methodology

English · [简体中文](methodology.zh-CN.md) · [Back to the collection](../README.md)

This guide is an editorial synthesis of [DeckStage](../papers/deckstage/README.md) and [IconLab](../papers/iconlab/README.md). It connects their engineering choices; it is not an additional experimental result.

## From a problem to a checkable output

```text
Original resources + explicit constraints
                    ↓
          Canonical state and geometry
                    ↓
       Interaction and destination rendering
                    ↓
          Output + independent checks
```

Both papers ask what must remain invariant when the representation changes. DeckStage connects artwork, physical card dimensions, scene projection, and final pixels. IconLab connects design coordinates, display gestures, undo history, and output sizes.

## Five recurring decisions

| Decision | DeckStage | IconLab |
| --- | --- | --- |
| Preserve original resources | Immutable source images and one packaging atlas | Artwork resource separated from editable parameters |
| Declare coordinate meaning | Artwork, physical card, scene, output, and world coordinates | Canonical normalized coordinates, display reflection, destination pixels |
| Share geometry | Plane homography, card-local masks, box camera | Continuous plate and canonical affine parameters |
| Separate editing from output | Assignment and poses stored in scene state; source-based export | Immediate preview, deferred history commit, frozen export snapshot |
| Match evidence to claims | Exact trim checks, reference diagnostics, synthetic fit study | Source inspection, algebraic identity, synthetic coverage and coordinate tests |

## A concrete example: moving an image

Dragging an image changes a position parameter. It should not overwrite the source, silently alter the crop, or make export depend on the current display zoom.

In DeckStage, inverse mapping determines which visible card receives an artwork assignment. The camera and local card geometry then determine its rendered position. In IconLab, display displacement is converted back to canonical units from the gesture-start state. A meaningful edit becomes one undo transaction, and export uses the saved design rather than a screenshot.

The same user action therefore needs several explicit contracts: coordinate conversion, state ownership, hit testing, transaction boundaries, and the export snapshot.

## Four questions for reading a result

1. **Which object is being tested?** An equation, a synthetic fixture, an application renderer, and a human judgment require different evidence.
2. **Which units and conditions apply?** Pixel error depends on reference size; supersampling depends on phase, shape, reference density, and kernel.
3. **What is shared?** Common state can imply common geometric intent without implying identical output pixels across backends.
4. **What remains unmeasured?** Proposed acceptance thresholds, latency goals, and aesthetic benefits must remain distinguishable from observed results.

## Applying the pattern to another project

Start by writing down the source resources, canonical parameters, coordinate units, and invariants. Then describe how interaction mutates the state and how export consumes it. Choose checks that can fail independently: asymmetric markers for orientation, known bleed bands for cropping, interrupted gestures for undo, and frozen-state outputs for package consistency.

Keep the evidence chain visible in the notes using the [paper template](../templates/paper-notes.md). When a manuscript is revised, preserve the old release and state which assumptions, implementation details, or measurements changed.
