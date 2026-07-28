-- =============================================================================
-- amp2_plate_validation.sql
-- AMP2 plate-workflow SQL test harness
--
-- Assumes PostgreSQL with JSONB for well_metadata and well_readings columns.
-- Table names mirror the YAML top-level keys; adjust to your actual DDL.
--
-- Assumed tables (simplified):
--   strain(id, entity_type, name, strain_identifier, strain_source, strain_mutation)
--   processed_sample(id, name, sample_base_type, processed_sample_type)
--   media_preparation(id, name, media_type, sterilization_method, ph_adjustment,
--                     ph_target, creation_date, output_sample_id)
--   culture_growth_activity(id, activity_type, name, strain_ref, media_ref,
--                            incubation_time_hours, temperature_celsius,
--                            treatment_type, input_sample_id, output_sample_id)
--   plate_setup_activity(id, activity_type, plate_barcode, plate_type, setup_date,
--                        media_ref, input_sample_id, output_sample_id,
--                        well_metadata jsonb)
--   data_generation_activity(id, activity_type, plate_setup_id, plate_barcode,
--                             timepoint_label, wavelength_nm, sequence_order,
--                             acquisition_time)
--   plate_product(id, product_type, activity_id, plate_barcode, timepoint_label,
--                 wavelength_nm, plate_average, blank_mean, cv_percent,
--                 plate_reader_model, well_readings jsonb)
-- =============================================================================


-- ---------------------------------------------------------------------------
-- Q1: All well readings for a plate at a specific timepoint
--     Basic retrieval — confirms data round-trip after ingest.
-- ---------------------------------------------------------------------------
SELECT
    wr->>'position'          AS position,
    (wr->>'value')::numeric  AS od_value,
    wr->>'flag'              AS flag
FROM plate_product pp,
     jsonb_array_elements(pp.well_readings) AS wr
WHERE pp.plate_barcode  = 'EPix1'
  AND pp.timepoint_label = 't=0'
ORDER BY wr->>'position';


-- ---------------------------------------------------------------------------
-- Q2: Full OD time-series per well (all timepoints, ordered by sequence)
--     Validates multi-timepoint chaining and sequence_order correctness.
-- ---------------------------------------------------------------------------
SELECT
    wr->>'position'           AS position,
    pp.timepoint_label,
    dga.sequence_order,
    (wr->>'value')::numeric   AS od_value,
    wr->>'flag'               AS flag
FROM plate_product pp
JOIN data_generation_activity dga ON dga.id = pp.activity_id
JOIN plate_setup_activity     psa ON psa.id = dga.plate_setup_id,
     jsonb_array_elements(pp.well_readings) AS wr
WHERE psa.plate_barcode = 'EPix1'
ORDER BY wr->>'position', dga.sequence_order NULLS LAST;


-- ---------------------------------------------------------------------------
-- Q3: Per-well effective media
--     Returns each well's media_ref — per-well override if present, else
--     falls back to plate-level media_ref.  Key test for the complex dataset.
-- ---------------------------------------------------------------------------
SELECT
    psa.plate_barcode,
    wm->>'position'   AS position,
    wm->>'well_type'  AS well_type,
    COALESCE(
        NULLIF(wm->>'media_ref', ''),
        psa.media_ref
    )                 AS effective_media_ref,
    CASE
        WHEN wm->>'media_ref' IS NOT NULL AND wm->>'media_ref' != ''
            THEN 'per_well_override'
        ELSE 'plate_level_fallback'
    END               AS media_source
FROM plate_setup_activity psa,
     jsonb_array_elements(psa.well_metadata) AS wm
WHERE psa.plate_barcode = 'EPix1-complex'
ORDER BY wm->>'position';


-- ---------------------------------------------------------------------------
-- Q4: Full provenance trace — well reading → plate → culture chain → strain
--     Given plate_barcode + position, walk 5 hops back to the source strain.
--     Run once per dataset; both vanilla and complex should resolve to a strain.
-- ---------------------------------------------------------------------------
WITH well_values AS (
    SELECT
        pp.id                             AS product_id,
        pp.activity_id,
        dga.plate_setup_id,
        dga.timepoint_label,
        dga.sequence_order,
        wr->>'position'                   AS position,
        (wr->>'value')::numeric           AS od_value,
        wr->>'flag'                       AS flag
    FROM plate_product pp
    JOIN data_generation_activity dga ON dga.id = pp.activity_id,
         jsonb_array_elements(pp.well_readings) AS wr
    WHERE pp.plate_barcode = 'EPix1'
      AND wr->>'position'  = 'G1'         -- high-OD well in vanilla dataset
)
SELECT
    wv.position,
    wv.timepoint_label,
    wv.od_value,
    psa.plate_barcode,
    psa.setup_date,
    ec.name               AS experimental_culture,
    ec.treatment_type,
    pc.name               AS pre_culture,
    sc.name               AS stock_culture,
    sp.name               AS strain_purity,
    s.strain_identifier,
    s.strain_source,
    s.strain_mutation
FROM well_values wv
JOIN plate_setup_activity      psa ON psa.id = wv.plate_setup_id
-- experimental culture → plate
JOIN culture_growth_activity   ec  ON ec.output_sample_id  = psa.input_sample_id
                                   AND ec.activity_type     = 'ExperimentalCulture'
-- pre-culture → experimental culture
LEFT JOIN culture_growth_activity pc  ON pc.output_sample_id = ec.input_sample_id
                                      AND pc.activity_type    = 'PreCultureGrowth'
-- stock culture → pre-culture
LEFT JOIN culture_growth_activity sc  ON sc.output_sample_id = pc.input_sample_id
                                      AND sc.activity_type    = 'StockCulturePreparation'
-- strain purity → stock culture
LEFT JOIN culture_growth_activity sp  ON sp.output_sample_id = sc.input_sample_id
                                      AND sp.activity_type    = 'StrainPurity'
-- strain entity
JOIN strain                    s   ON s.id = ec.strain_ref
ORDER BY wv.sequence_order;


-- ---------------------------------------------------------------------------
-- Q5: Workflow completeness check
--     For every plate, flag which CultureGrowth steps are present/missing.
--     Expected: vanilla = all 4 present; complex may show gaps for BL21 arm.
-- ---------------------------------------------------------------------------
SELECT
    psa.plate_barcode,
    psa.id                                             AS plate_setup_id,
    CASE WHEN sp.id IS NULL  THEN 'MISSING' ELSE 'ok' END AS strain_purity_step,
    CASE WHEN sc.id IS NULL  THEN 'MISSING' ELSE 'ok' END AS stock_culture_step,
    CASE WHEN pc.id IS NULL  THEN 'MISSING' ELSE 'ok' END AS pre_culture_step,
    CASE WHEN ec.id IS NULL  THEN 'MISSING' ELSE 'ok' END AS experimental_culture_step
FROM plate_setup_activity psa
LEFT JOIN culture_growth_activity ec
       ON ec.output_sample_id = psa.input_sample_id
      AND ec.activity_type    = 'ExperimentalCulture'
LEFT JOIN culture_growth_activity pc
       ON pc.output_sample_id = ec.input_sample_id
      AND pc.activity_type    = 'PreCultureGrowth'
LEFT JOIN culture_growth_activity sc
       ON sc.output_sample_id = pc.input_sample_id
      AND sc.activity_type    = 'StockCulturePreparation'
LEFT JOIN culture_growth_activity sp
       ON sp.output_sample_id = sc.input_sample_id
      AND sp.activity_type    = 'StrainPurity'
ORDER BY psa.plate_barcode;


-- ---------------------------------------------------------------------------
-- Q6: Blank-corrected OD values per well per timepoint
--     Subtracts blank_mean (computed from flag='blank' wells) from each
--     sample well; flags negative-corrected values for review.
-- ---------------------------------------------------------------------------
WITH blank_means AS (
    SELECT
        pp.id             AS product_id,
        pp.timepoint_label,
        AVG((wr->>'value')::numeric) AS computed_blank_mean
    FROM plate_product pp,
         jsonb_array_elements(pp.well_readings) AS wr
    WHERE wr->>'flag' = 'blank'
    GROUP BY pp.id, pp.timepoint_label
)
SELECT
    pp.timepoint_label,
    dga.sequence_order,
    wr->>'position'                                        AS position,
    (wr->>'value')::numeric                                AS raw_od,
    bm.computed_blank_mean                                 AS blank_mean,
    ROUND((wr->>'value')::numeric - bm.computed_blank_mean, 4) AS corrected_od,
    CASE
        WHEN (wr->>'value')::numeric - bm.computed_blank_mean < 0
        THEN 'negative_after_correction'
        ELSE 'ok'
    END                                                    AS qc_flag
FROM plate_product pp
JOIN data_generation_activity dga ON dga.id = pp.activity_id
JOIN plate_setup_activity     psa ON psa.id = dga.plate_setup_id
JOIN blank_means              bm  ON bm.product_id = pp.id,
     jsonb_array_elements(pp.well_readings) AS wr
WHERE psa.plate_barcode = 'EPix1'
  AND wr->>'flag'        != 'blank'
ORDER BY wr->>'position', dga.sequence_order;


-- ---------------------------------------------------------------------------
-- Q7: Duplicate timepoint_label detection within a plate
--     Should return 1 row for EPix1-complex (the t=8h duplicate — violation C6).
-- ---------------------------------------------------------------------------
SELECT
    dga.plate_barcode,
    dga.timepoint_label,
    COUNT(*)     AS dga_count,
    STRING_AGG(dga.id, ', ') AS conflicting_ids
FROM data_generation_activity dga
GROUP BY dga.plate_barcode, dga.timepoint_label
HAVING COUNT(*) > 1
ORDER BY dga.plate_barcode, dga.timepoint_label;


-- ---------------------------------------------------------------------------
-- Q8: Orphan plate_product records (no matching data_generation_activity)
--     Catches FK integrity failures on ingestion.
-- ---------------------------------------------------------------------------
SELECT
    pp.id,
    pp.plate_barcode,
    pp.timepoint_label,
    pp.activity_id
FROM plate_product pp
WHERE pp.activity_id IS NULL
   OR NOT EXISTS (
       SELECT 1
       FROM data_generation_activity dga
       WHERE dga.id = pp.activity_id
   );
