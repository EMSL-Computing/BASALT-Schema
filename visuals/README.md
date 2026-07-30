# Visuals

Standalone, self-contained visual explainers for the MONet Analysis API schema.
Each file is a single HTML page with all CSS/JS inlined — no build step, no server,
no external dependencies. Open directly in any browser (`file://` works).

## `schema-explorer.html`

An interactive, hierarchical map of the **entire active schema** — a box-and-arrow
diagram for communication and for spotting modeling inconsistencies. The model is
extracted directly from the LinkML schema with `SchemaView` (see
[`build.py`](build.py)), so the 148 classes, their inheritance, and every slot
(range, pattern, required, description) are the real thing, not hand-transcribed.

Layout is a left-to-right process flow — **Sampling → Samples → Sample processing →
Data generation → Data processing → Data products** — with `organism` shown
as a satellite linked in by `organism_ref`/`strain_ref`, and supporting lanes
(Methods, Value tables, Reference/embedded) below. Colour encodes the inheritance
family / process stage. Within each column, classes nest by `is_a` (dashed border =
abstract base, solid = concrete).

Interactions:

- **Click any box or sidebar entry** to select a class — its inheritance ancestors
  light up in place, the sidebar syncs, and the right panel shows the inheritance
  breadcrumb, badges (stage / module / abstract / mixins), description, outgoing
  class references, and the full slot list.
- **Hover a slot** for a tooltip with its range, `required`/`identifier` flags,
  regex `pattern`, enum values, and description.
- **Follow references** — class-typed slots and the breadcrumb are clickable jumps.
- **Sidebar grouping** toggles between *process stage* and *workflow set* (source
  module: `mass-spec`, `metagenomics`, `media-strain-culture-plate`, …).
- **Highlight workflow set** chips glow every class a set touches across the flow and
  dim the rest — **AMP2 / plate** (= `media_strain_culture_plate.yaml`), **Mass spec**,
  **Metagenomics**. This is the mid-level "FTICR lives in the mass-spec workflow set" view.
- **Search** filters the class list; **↺** resets; light/dark aware.

**Deep-link:** `#c=ClassName` opens with that class selected, e.g.
`schema-explorer.html#c=MetaproteomicsProduct`.

### Updating after a schema change

The class/slot data is embedded in the HTML (a standalone file can't `fetch()` a
sibling JSON under `file://`). Refresh it in place with one command, then reload the
page in the browser:

```bash
uv run python visuals/build.py      # or: .venv/bin/python visuals/build.py
```

`build.py` re-reads the schema with `SchemaView`, rewrites the `<script id="model">`
block, and prints which classes were added/removed since the last build. Nothing else
to touch. (LinkML's own `just gen-project` JSON Schema is *not* usable here — it
flattens `is_a` inheritance and drops the `from_schema`/module tags this map relies on.)

Optional `just` target — add to the justfile if you want `just gen-viz`:

```make
gen-viz:
    uv run python visuals/build.py
```

## `amp2-data-journey.html`

An animated walkthrough of how one **AMP2 96-well plate submission** travels through
the API, from the web uploader to stored, queryable records. Built around the classes
in [`media_strain_culture_plate.yaml`](../src/analysis_api_schema/schema/media_strain_culture_plate.yaml)
and grounded in the worked example under
[`src/data/examples`](../src/data/examples) (two strains, two media batches, 96 wells,
five OD₆₀₀ timepoints).

A right-hand rail lists eight stages; the left stage animates each one. It auto-plays
and loops, with transport controls (play/pause, step, restart, loop, speed) and a
scrubber. Light/dark theme aware.

**The eight stages**

1. **Upload** — the seven linked CSVs enter the web uploader as one submission.
2. **Parse** — each file/column maps onto a LinkML class and slot.
3. **Validate** — `linkml-validate` enforces enums, required fields, foreign keys,
   patterns and unique keys (the example carries six seeded violations).
4. **Identity** — strain rows become `organism` records.
5. **Lab lifecycle** — the `SampleProcessing` chain (MediaPreparation → cultures),
   each activity emitting a `ProcessedSample`.
6. **Plate setup** — `AMP2PlateSetupActivity` / `AMP2WellMetadata` lay out the 96 wells.
7. **Measure** — `AMP2DataGenerationActivity` reads OD₆₀₀ over five timepoints.
8. **Store** — readings roll up into `AMP2ODProduct`; metadata to PostgreSQL, raw files to S3/MinIO.

**Deep-link parameters** (handy for slides or embedding)

- `#s=N` — open directly on stage N (1–8), e.g. `amp2-data-journey.html#s=6`
- `#still` — open paused instead of auto-playing, e.g. `#s=3&still`

**Keyboard** — `←`/`→` step, `space` play/pause, `R` restart.
