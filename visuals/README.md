# Visuals

Standalone, self-contained visual explainers for the MONet Analysis API schema.
Each file is a single HTML page with all CSS/JS inlined — no build step, no server,
no external dependencies. Open directly in any browser (`file://` works).

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
4. **Identity** — strain rows become `biological_entity` records.
5. **Lab lifecycle** — the `SampleProcessing` chain (MediaPreparation → cultures),
   each activity emitting a `ProcessedSample`.
6. **Plate setup** — `AMP2PlateSetupActivity` / `AMP2WellMetadata` lay out the 96 wells.
7. **Measure** — `AMP2DataGenerationActivity` reads OD₆₀₀ over five timepoints.
8. **Store** — readings roll up into `AMP2ODProduct`; metadata to PostgreSQL, raw files to S3/MinIO.

**Deep-link parameters** (handy for slides or embedding)

- `#s=N` — open directly on stage N (1–8), e.g. `amp2-data-journey.html#s=6`
- `#still` — open paused instead of auto-playing, e.g. `#s=3&still`

**Keyboard** — `←`/`→` step, `space` play/pause, `R` restart.
