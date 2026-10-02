# Contributing

English · [简体中文](CONTRIBUTING.zh-CN.md) · [Back to the collection](README.md)

Useful contributions include correcting a paper's metadata, improving a reading note, fixing a link, translating an explanation, or submitting a project methodology manuscript. New entries should explain the connection between a concrete project problem, its method, and its evidence.

## Add a paper

1. Prepare a manuscript with its actual author, full title, date, language, and rights statement. Label its publication status accurately. Do not add an unassigned DOI, an unconfirmed venue, or results that were not measured.
2. Attach the reviewed PDF to a versioned GitHub Release. Preserve existing release assets; publish substantive revisions under a new tag. Verify that the download link works without signing in.
3. Create `papers/<id>/README.md` and `README.zh-CN.md` using [the note template](templates/paper-notes.md). Label translated titles and distinguish Chinese notes from the language of the manuscript.
4. Add one entry to [catalog.json](catalog.json), following the existing fields. IDs and citation keys must be unique. Record exact page count and release asset name; include `project_url` only when a public source link has been verified.
5. Add the individual manuscript to [references.bib](references.bib), then update both root READMEs, their collection count, and any relevant reading paths. Keep factual details consistent across languages.
6. Run `python3 scripts/validate.py` from the repository root. For live release metadata, also run `python3 scripts/validate.py --remote` with network access. Submit the changes through a pull request.

## Write useful notes

State the problem and assumptions before the method. Provide a short section map, explain one transferable idea, and identify what a reported metric actually measures. Separate implementation observations, mathematical identities, synthetic experiments, proposed tests, and user studies. Link reproduction materials only when they are available, and say what is missing.

The [shared methodology guide](docs/methodology.md) is an editorial synthesis. Updating it does not create new evidence for a paper.

## Report a correction

Use the [issue form](https://github.com/yf-official/yf-official-methodology/issues/new/choose) and include the paper/version, page or section, the current statement, and the suggested correction with a source. If the PDF itself needs revision, explain that separately from a reading-note correction.

## Rights and maintenance

Check permissions separately for manuscripts, figures, artwork, code, and datasets. Preserve author attribution and the original rights statement. This repository does not apply a blanket open-source license to its contents.

The local validator uses the Python standard library and does not fetch remote links by default. CI checks metadata, citations, bilingual navigation, local files, and Markdown anchors. The optional remote check verifies release publication dates and PDF asset presence through the GitHub API; it does not test every external URL or verify a PDF's scientific claims.
