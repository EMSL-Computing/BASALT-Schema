# amp2-full-workflow-002

Simulated AMP2 dataset for ingestion testing against the BASALT schema.
Regenerate with `python3 generate.py` (deterministic — no wall-clock or
salted-hash inputs, so a re-run reproduces every value byte for byte).

The companion single-document view of the same data is
`../amp2-full-workflow-002.yaml`.

## What is in it

| | count |
|---|---|
| organisms (`organism`) | 8 |
| user samples (`AMP2UserSample`) | 15 |
| media batches (`MediaPreparation`) | 7 |
| culture activities (`CultureGrowth` subclasses) | 60 |
| plates (`AMP2PlateSetupActivity`) | 3 |
| wells (`AMP2WellMetadata`) | 576 |
| OD reads (`AMP2DataGenerationActivity`) | 39 |
| OD products (`AMP2ODProduct`) | 38 |
| well readings (`WellReading`) | 7392 |
| sample↔activity edges (`ProcessingSampleLink`) | 146 |

Fifteen user samples, each carried through the complete workflow

```
AMP2UserSample
  → StrainPurity              (QC gate; emits no processed sample)
  → StockCulturePreparation   → ProcessedSample(stock_culture)
  → PreCultureGrowth          → ProcessedSample(pre_culture)
  → ExperimentalCulture       → ProcessedSample(experimental_culture)
  → AMP2PlateSetupActivity    → ProcessedSample(amp2_*well_plate)
  → AMP2DataGenerationActivity × 13   (OD600 every 2 h for 24 h)
  → AMP2ODProduct             → WellReading per well
```

## Where the sample ID lives

This is the part that caused confusion previously, so it is spelled out.

There are **three different identifiers** in play and they are not
interchangeable:

| what you mean | where it lives | example |
|---|---|---|
| the tube the submitter sent | `02_amp2_user_samples.csv` → `id` | `urn:amp2:sample:AMP2-0003` |
| what the submitter called it | `02_amp2_user_samples.csv` → `name` | `PP_0055-R1` |
| the strain / biological identity | `01_organisms.csv` → `id`, reached via `organism_ref` | `urn:amp2:organism:PP-0055` |

**The sample id is `AMP2UserSample.id`.** Every foreign key in this dataset
points at that value, including `AMP2WellMetadata.sample_id`. The organism id
can never substitute for it: organisms are shared, e.g. `PP_0055` has three
samples (`AMP2-0003`, `AMP2-0004`, `AMP2-0005`) and `KT2440_WT` has two.

Physically, what gets pipetted into a well is the `experimental_culture`
ProcessedSample descended from that user sample, not the tube itself. So there
are two ways to ask a question about a well and they answer different things:

* *"Whose sample is in well D07?"* → `AMP2WellMetadata.sample_id`, which holds
  the `AMP2UserSample.id` directly.
* *"What physical material is in well D07 and how was it made?"* → walk
  `11_processing_sample_links.csv` backwards from the plate setup activity.

`00_sample_identity_crosswalk.csv` flattens the whole chain into one row per
sample so you can check either path at a glance.

## Files

| file | contents |
|---|---|
| `00_sample_identity_crosswalk.csv` | one row per user sample: id, name, organism, and every downstream activity/processed-sample id |
| `01_organisms.csv` | `organism` records (replaces the retired `Strain` class) |
| `02_amp2_user_samples.csv` | `AMP2UserSample` records |
| `03_media_preparations.csv` | `MediaPreparation` activities + the `prepared_media` sample each emits |
| `04_culture_growth_activities.csv` | the four `CultureGrowth` steps per sample |
| `05_processed_samples.csv` | every `ProcessedSample` (media, stock, pre, experimental, plate) |
| `06_plate_setup_activities.csv` | `AMP2PlateSetupActivity`, one row per plate |
| `07_well_metadata.csv` | `AMP2WellMetadata`, one row per well |
| `08_data_generation_activities.csv` | `AMP2DataGenerationActivity`, one row per plate × timepoint |
| `09_od_products.csv` | `AMP2ODProduct` plate-level summaries |
| `10_well_readings.csv` | `WellReading`, one row per well × timepoint |
| `11_processing_sample_links.csv` | `ProcessingSampleLink` — the authoritative input/output edges |

`07_well_metadata.csv` carries two convenience columns that are **not** schema
slots, marked as such by their names:
`user_sample_name_denormalised` (the sample's human-readable name, so you can
eyeball a layout without a join) and `effective_media_processed_sample_id`
(the per-well `media_ref` override if present, otherwise the plate-level
`media_ref` — i.e. the medium actually in that well).

## Plates

| barcode | format | media | design |
|---|---|---|---|
| `AMP2-P001` | 96-well, Greiner flat bottom | plate-level LB; rows E–H **override** to M9 + 0.4% glucose | carbon-source comparison, samples `AMP2-0001`–`AMP2-0008` |
| `AMP2-P002` | 96-well, Corning flat bottom | one medium for every well, no overrides | CRISPRi vanillate dose-response (0 / 0.1 / 1.0 mM) via per-well `treatments`, samples `AMP2-0009`–`AMP2-0015` |
| `AMP2-P003` | **384-well**, Greiner flat bottom | four media, one per quadrant, via per-well overrides | all 15 samples × 6 replicates in each of LB, M9+glucose, M9+benzoate, YPD |

`AMP2-P003` is included specifically to show the model is not hard-wired to
96-well geometry: `plate_type` names the vendor format, positions run `A01`–`P24`,
and nothing in `AMP2WellMetadata` or `WellReading` assumes a well count.

Well types used: `sample`, `blank`, `uninoculated_control`, `positive_control`,
`negative_control`, `standard`. `WellMetadata.well_type` is a free-text slot;
the first four in that list are the values named in the schema docstring, and
`positive_control` / `negative_control` extend it. `blank` is a media-only well
read for absorbance zeroing; `uninoculated_control` is a full media well
incubated alongside the samples to catch contamination — they are deliberately
kept distinct.

## Simulated growth

OD600 follows a logistic curve per well with organism-specific and
medium-specific carrying capacity and rate, a lag phase (longer for the yeast),
per-well biological scatter, per-read instrument noise, and a mild late-run
edge-evaporation effect. The biology is meant to be plausible rather than
merely non-constant — for example `RHA1_pTE314` reaches its highest density on
M9 + benzoate while `IFO0880_LIP1` barely grows there and peaks on YPD.

## Deliberate data conditions

Everything here is schema-**valid**. These are realistic messy-data
conditions, not schema violations, so the whole bundle should ingest cleanly
and then exercise your QC paths.

* **Aborted read.** `AMP2-P002` at `t=10h`: the `AMP2DataGenerationActivity`
  exists with `read_status: aborted` and **no** `AMP2ODProduct`. That plate has
  13 read activities but only 12 products — code that assumes
  one-product-per-activity will notice here.
* **Failed quadrant.** `AMP2-P003` at `t=14h`: condensation over the YPD
  quadrant (rows I–P, columns 13–24) flags 96 wells `failed` at saturated
  values near 3.7.
* **Contaminated well.** `AMP2-P001` well `D07` is flagged `contaminated` from
  `t=12h` onward, with OD roughly double its neighbours.
* **Scattered outliers.** Eight wells flagged `outlier` at a single timepoint.
* **Failed purity check.** `AMP2-0013` fails its first streak
  (`contaminant_strains` populated on its `StrainPurity` activity), is
  re-streaked, and completes the workflow.
* **Sparse organism.** Wild-type `KT2440_WT` leaves `trait`, `phenotype`,
  `strain_mutation` and `modification_method` null on purpose, so nullability
  on the organism table gets exercised.

Flag tallies across all 7392 readings: `ok` 7039, `blank` 242, `outlier` 8, `contaminated` 7, `failed` 96.

## Modelling notes

* `ProcessingSampleLink` is the single source of truth for what an activity
  consumed and produced. Activities deliberately do **not** repeat
  `input_sample_id` / `output_sample_id` inline the way the older
  `amp2-vanilla-001` / `amp2-complex-001` examples did.
* `StrainPurity` is a pass/fail QC gate and emits no `ProcessedSample`, per
  `media_strain_culture_plate.yaml`. Its only link is `input_sample`.
* `media_ref` points at a `ProcessedSample` of type `prepared_media` — the
  physical media batch — never at the `MediaPreparation` activity itself.
* `organism` replaces the retired `Strain` class. Organism records carry
  `strain_identifier`, `organism_name`, `taxonomy_id`, the
  `genotype_segment_*` / `component_*` construct detail slots, `trait`,
  `phenotype`, `trophic_level`, `pathogenicity` and `propagation`. Values for
  the CRISPRi strains follow `CRISPRi_Pp_11strains.csv` from the AMP2 Data
  Model Campaign folder.
* `oxygen_saturation_pct` is a float (percent O2 saturation in the incubation
  atmosphere, e.g. 20.9 for ambient air).
* Enum-ranged fields use permissible values from `enums.yaml`
  (`StrainTypeEnum`, `ModificationMethodEnum`, `IntendedTraitEnum`,
  `TrophicLevelEnum`, `GenotypeSegmentEnum`, `ConstructComponentEnum`,
  `MediaTypeEnum`, `FormulationEnum`, `StorageConditionEnum`,
  `GrowthFacilityEnum`, `SampleRole`).
* Multivalued slots are pipe-delimited (`|`) in CSV and real YAML lists in the
  YAML document.
