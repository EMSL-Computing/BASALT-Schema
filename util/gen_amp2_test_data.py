#!/usr/bin/env python3
"""
gen_amp2_test_data.py

Generate AMP2 validation test data (YAML + CSV) from real EPix1 plate readings.
Run from the analysis-api-schema repo root:

    python util/gen_amp2_test_data.py

Outputs
-------
src/data/examples/invalid/amp2-vanilla-001.yaml
src/data/examples/invalid/amp2-vanilla-001/
    01_strains.csv
    02_media_preparations.csv
    03_culture_activities.csv
    04_plate_setup.csv
    05_well_metadata.csv
    06_data_generation_activities.csv
    07_well_readings.csv

src/data/examples/invalid/amp2-complex-001.yaml
src/data/examples/invalid/amp2-complex-001/   (same CSV set)

tests/amp2_plate_validation.sql
"""

import argparse
import csv
import math
from pathlib import Path

# ---------------------------------------------------------------------------
# Well-position constants
# ---------------------------------------------------------------------------
ROWS = list("ABCDEFGH")
COLS = list(range(1, 13))
ALL_WELLS: list[str] = [f"{r}{c}" for r in ROWS for c in COLS]
BLANK_WELLS_VANILLA: set[str] = {f"H{c}" for c in COLS}   # row H  = blanks (vanilla)
BLANK_WELLS_COMPLEX: set[str] = {f"H{c}" for c in COLS}   # same for complex

# ---------------------------------------------------------------------------
# t=0 values — EPix1__20260324_1619_Absorbance_600nm.csv (2026-03-24 16:19)
# ---------------------------------------------------------------------------
T0: dict[str, float] = {
    "A1":  0.0684, "A2":  0.0789, "A3":  0.0681, "A4":  0.0676,
    "A5":  0.0672, "A6":  0.0729, "A7":  0.0833, "A8":  0.0672,
    "A9":  0.0668, "A10": 0.0676, "A11": 0.0697, "A12": 0.0665,
    "B1":  0.0679, "B2":  0.0712, "B3":  0.2862, "B4":  0.0685,
    "B5":  0.0693, "B6":  0.0693, "B7":  0.2143, "B8":  0.0682,
    "B9":  0.0686, "B10": 0.0910, "B11": 0.0690, "B12": 0.0671,
    "C1":  0.0689, "C2":  0.0695, "C3":  0.0693, "C4":  0.0684,
    "C5":  0.0675, "C6":  0.0677, "C7":  0.0672, "C8":  0.0685,
    "C9":  0.0676, "C10": 0.0679, "C11": 0.0677, "C12": 0.0680,
    "D1":  0.0741, "D2":  0.1551, "D3":  0.0683, "D4":  0.1079,
    "D5":  0.3321, "D6":  0.0677, "D7":  0.0686, "D8":  0.0697,
    "D9":  0.0680, "D10": 0.0700, "D11": 0.0687, "D12": 0.0677,
    "E1":  0.1407, "E2":  0.0673, "E3":  0.0694, "E4":  0.0684,
    "E5":  0.0853, "E6":  0.1326, "E7":  0.0705, "E8":  0.3191,
    "E9":  0.0671, "E10": 0.0741, "E11": 0.0723, "E12": 0.1230,
    "F1":  0.0709, "F2":  0.0678, "F3":  0.1221, "F4":  0.0782,
    "F5":  0.3594, "F6":  0.1341, "F7":  0.0793, "F8":  0.0734,
    "F9":  0.1124, "F10": 0.0774, "F11": 0.0762, "F12": 0.0959,
    "G1":  1.2251, "G2":  0.0682, "G3":  0.0733, "G4":  0.0680,
    "G5":  0.1302, "G6":  0.0739, "G7":  0.0685, "G8":  0.1044,
    "G9":  0.0742, "G10": 0.0756, "G11": 0.0733, "G12": 0.0696,
    "H1":  0.0679, "H2":  0.0702, "H3":  0.0691, "H4":  0.0685,
    "H5":  0.0697, "H6":  0.0696, "H7":  0.0689, "H8":  0.0668,
    "H9":  0.0674, "H10": 0.0698, "H11": 0.0693, "H12": 0.0684,
}


def scale_tp(t0: dict[str, float], sample_scale: float, blank_scale: float = 1.02,
             blank_wells: set[str] = BLANK_WELLS_VANILLA) -> dict[str, float]:
    """Multiply sample wells by sample_scale, blank wells by blank_scale."""
    return {
        w: round(v * (blank_scale if w in blank_wells else sample_scale), 4)
        for w, v in t0.items()
    }


def stats(values: dict[str, float], blank_wells: set[str]) -> tuple[float, float, float]:
    """Return (plate_average_of_samples, blank_mean, cv_pct_of_samples)."""
    sv = [v for w, v in values.items() if w not in blank_wells]
    bv = [v for w, v in values.items() if w in blank_wells]
    avg = round(sum(sv) / len(sv), 4)
    bm  = round(sum(bv) / len(bv), 4) if bv else 0.0
    std = round(math.sqrt(sum((v - avg) ** 2 for v in sv) / len(sv)), 4)
    cv  = round((std / avg) * 100, 2) if avg else 0.0
    return avg, bm, cv


# ---------------------------------------------------------------------------
# Vanilla timepoints
# ---------------------------------------------------------------------------
V_T0   = T0
V_T8H  = scale_tp(T0, 1.30)
V_T24H = scale_tp(T0, 2.00)

# ---------------------------------------------------------------------------
# Complex timepoints (same base readings, same plate — 5 timepoints)
# ---------------------------------------------------------------------------
C_T0   = T0
C_T4H  = scale_tp(T0, 1.15)
C_T8H  = scale_tp(T0, 1.30)
C_T16H = scale_tp(T0, 1.65)
C_T24H = scale_tp(T0, 2.00)


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------

def _flag(well: str, val: float, blank_wells: set[str]) -> str:
    if well in blank_wells:
        return "blank"
    if val > 1.5:
        return "outlier"
    return "ok"


def readings_block(values: dict[str, float], blank_wells: set[str],
                   bad_pos: str | None = None, pad: int = 6) -> str:
    """Compact inline YAML list for well_readings."""
    sp = " " * pad
    lines: list[str] = []
    for well in ALL_WELLS:
        val  = values[well]
        flag = _flag(well, val, blank_wells)
        pos  = bad_pos if (bad_pos and well == "A1") else well
        lines.append(f'{sp}- {{position: "{pos}", value: {val:.4f}, flag: "{flag}"}}')
    return "\n".join(lines)


def vanilla_well_metadata(pad: int = 6) -> str:
    """96-well metadata — all same media (plate-level), row H = blanks."""
    sp = " " * pad
    lines: list[str] = []
    for r in ROWS:
        for c in COLS:
            pos = f"{r}{c}"
            if r == "H":
                lines.append(
                    f'{sp}- {{position: "{pos}", well_type: "blank",'
                    f' media_volume_ul: 200.0, inoculum_volume_ul: 0.0}}'
                )
            else:
                lines.append(
                    f'{sp}- {{position: "{pos}", well_type: "sample",'
                    f' replicate_group: "rep_{c}", media_volume_ul: 180.0,'
                    f' inoculum_volume_ul: 20.0, sample_id: "KT2440-{pos}"}}'
                )
    return "\n".join(lines)


def complex_well_metadata(pad: int = 6) -> str:
    """Per-well media overrides: cols 1–6 → M9, cols 7–12 → LB; row H = blanks.
    Violations: A3, B7, D11 have inoculum_volume_ul omitted (required field).
    """
    sp    = " " * pad
    m9_id = "urn:amp2:ps:M9-glucose-batch-002"
    lb_id = "urn:amp2:ps:LB-media-batch-001"
    missing_inoculum = {"A3", "B7", "D11"}   # [C5] intentional missing required field
    lines: list[str] = []
    for r in ROWS:
        for c in COLS:
            pos = f"{r}{c}"
            if r == "H":
                lines.append(
                    f'{sp}- {{position: "{pos}", well_type: "blank",'
                    f' media_volume_ul: 200.0, inoculum_volume_ul: 0.0}}'
                )
                continue
            media_ref = m9_id if c <= 6 else lb_id
            rep_group = f"rep_{c}"
            strain_arm = "KT2440" if c <= 6 else "BL21"
            if pos in missing_inoculum:
                # [C5] inoculum_volume_ul missing
                lines.append(
                    f'{sp}- {{position: "{pos}", well_type: "sample",'
                    f' media_ref: "{media_ref}", replicate_group: "{rep_group}",'
                    f' media_volume_ul: 180.0, sample_id: "{strain_arm}-{pos}"}}'
                )
            else:
                lines.append(
                    f'{sp}- {{position: "{pos}", well_type: "sample",'
                    f' media_ref: "{media_ref}", replicate_group: "{rep_group}",'
                    f' media_volume_ul: 180.0, inoculum_volume_ul: 20.0,'
                    f' sample_id: "{strain_arm}-{pos}"}}'
                )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Vanilla YAML
# ---------------------------------------------------------------------------

def build_vanilla_yaml() -> str:
    bw     = BLANK_WELLS_VANILLA
    a0, bm0, cv0    = stats(V_T0,   bw)
    a8, bm8, cv8    = stats(V_T8H,  bw)
    a24, bm24, cv24 = stats(V_T24H, bw)

    wm   = vanilla_well_metadata(pad=6)
    wr0  = readings_block(V_T0,   bw, pad=8)
    wr8  = readings_block(V_T8H,  bw, pad=8)
    wr24 = readings_block(V_T24H, bw, pad=8)

    return f"""\
# =============================================================================
# amp2-vanilla-001.yaml
#
# Scenario: Single strain (P. putida KT2440 pTE314), single M9+glucose media
#   batch, 4-step CultureGrowth chain, 1 plate (EPix1), 3 OD timepoints.
#
# Intentional violations (for schema / DB validation testing):
#   [V1] wavelength_nm on dga-EPix1-t8h is a string ("600nm") — must be integer
#   [V2] setup_date missing from plate_setup_activity (required field)
#   [V3] timepoint_label absent from plate_product amp2-prod-t24h (required field)
# =============================================================================

strains:
  - id: "urn:amp2:strain:KT2440-pTE314"
    entity_type: "strain"
    name: "Pseudomonas putida KT2440 pTE314"
    strain_identifier: "KT2440_pTE314"
    strain_type: "bacterial"
    strain_source: "PNNL"
    strain_mutation: "pTE314"

processed_samples:
  - id: "urn:amp2:ps:M9-glucose-batch-001"
    name: "M9 + 1% glucose batch 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "prepared_media"
    description: "M9 minimal salts + 1% glucose (w/v), autoclave sterilized, pH 7.0"

  - id: "urn:amp2:ps:KT2440-purity-output-001"
    name: "KT2440 pTE314 strain purity culture"
    sample_base_type: "processed_sample"
    processed_sample_type: "strain_purity_culture"

  - id: "urn:amp2:ps:KT2440-stock-output-001"
    name: "KT2440 pTE314 stock culture 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "stock_culture"

  - id: "urn:amp2:ps:KT2440-preculture-output-001"
    name: "KT2440 pTE314 pre-culture 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "pre_culture"

  - id: "urn:amp2:ps:KT2440-experimental-output-001"
    name: "KT2440 pTE314 experimental culture 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "experimental_culture"

  - id: "urn:amp2:ps:EPix1-plate-001"
    name: "EPix1 AMP2 96-well plate 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "amp2_96well_plate"

media_preparations:
  - id: "urn:amp2:act:media-prep-M9-001"
    name: "M9 + 1% glucose preparation"
    media_type: "pre_culture"
    volume_ml: 500.0
    media_recipe: "M9 minimal salts with 1% glucose (w/v)"
    media_formulation: "manual_mix"
    sterilization_method: "autoclave"
    ph_adjustment: true
    ph_target: 7.0
    creation_date: "2026-03-20"
    storage_temperature: "4 C"
    media_additions:
      - "1% glucose (w/v)"
    output_sample_id: "urn:amp2:ps:M9-glucose-batch-001"

culture_growth_activities:
  - id: "urn:amp2:act:strain-purity-001"
    activity_type: "StrainPurity"
    name: "KT2440 pTE314 strain purity check"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-001"
    incubation_time_hours: 24.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "tube"
    inspection_method: "visual"
    target_strain: "KT2440_pTE314"
    input_sample_id: null
    output_sample_id: "urn:amp2:ps:KT2440-purity-output-001"

  - id: "urn:amp2:act:stock-culture-001"
    activity_type: "StockCulturePreparation"
    name: "KT2440 pTE314 stock culture preparation"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-001"
    incubation_time_hours: 16.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "flask"
    preparation_date: "2026-03-21"
    input_sample_id: "urn:amp2:ps:KT2440-purity-output-001"
    output_sample_id: "urn:amp2:ps:KT2440-stock-output-001"

  - id: "urn:amp2:act:preculture-001"
    activity_type: "PreCultureGrowth"
    name: "KT2440 pTE314 pre-culture"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-001"
    incubation_time_hours: 12.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "flask"
    input_sample_id: "urn:amp2:ps:KT2440-stock-output-001"
    output_sample_id: "urn:amp2:ps:KT2440-preculture-output-001"

  - id: "urn:amp2:act:experimental-culture-001"
    activity_type: "ExperimentalCulture"
    name: "KT2440 pTE314 experimental culture — no treatment"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-001"
    incubation_time_hours: 4.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "flask"
    treatment_type: "none"
    growth_time: "4 hours"
    input_sample_id: "urn:amp2:ps:KT2440-preculture-output-001"
    output_sample_id: "urn:amp2:ps:KT2440-experimental-output-001"

plate_setup_activities:
  - id: "urn:amp2:act:plate-setup-EPix1-001"
    activity_type: "AMP2PlateSetupActivity"
    name: "EPix1 AMP2 plate setup"
    plate_type: "Greiner_96well_flat_bottom"
    plate_barcode: "EPix1"
    # [V2] setup_date intentionally omitted — required field missing
    setup_operator_id: "kapu336"
    setup_instrument: "manual"
    sealing_method: "BreathEasy_membrane"
    media_ref: "urn:amp2:ps:M9-glucose-batch-001"
    input_sample_id: "urn:amp2:ps:KT2440-experimental-output-001"
    output_sample_id: "urn:amp2:ps:EPix1-plate-001"
    well_metadata:
{wm}

data_generation_activities:
  - id: "urn:amp2:act:dga-EPix1-t0"
    activity_type: "AMP2dataGenerationActivity"
    name: "EPix1 OD read t=0"
    plate_setup_id: "urn:amp2:act:plate-setup-EPix1-001"
    plate_id: "urn:amp2:ps:EPix1-plate-001"
    timepoint_label: "t=0"
    wavelength_nm: 600
    measurement_type: "optical_density"
    sequence_order: 1
    acquisition_time: "2026-03-24T16:19:00"

  - id: "urn:amp2:act:dga-EPix1-t8h"
    activity_type: "AMP2dataGenerationActivity"
    name: "EPix1 OD read t=8h"
    plate_setup_id: "urn:amp2:act:plate-setup-EPix1-001"
    plate_id: "urn:amp2:ps:EPix1-plate-001"
    timepoint_label: "t=8h"
    wavelength_nm: "600nm"   # [V1] should be integer 600, not string "600nm"
    measurement_type: "optical_density"
    sequence_order: 2
    acquisition_time: "2026-03-25T00:19:00"

  - id: "urn:amp2:act:dga-EPix1-t24h"
    activity_type: "AMP2dataGenerationActivity"
    name: "EPix1 OD read t=24h"
    plate_setup_id: "urn:amp2:act:plate-setup-EPix1-001"
    plate_id: "urn:amp2:ps:EPix1-plate-001"
    timepoint_label: "t=24h"
    wavelength_nm: 600
    measurement_type: "optical_density"
    sequence_order: 3
    acquisition_time: "2026-03-25T16:19:00"

plate_products:
  - id: "urn:amp2:prod:EPix1-t0"
    product_type: "AMP2ODProduct"
    activity_id: "urn:amp2:act:dga-EPix1-t0"
    plate_barcode: "EPix1"
    timepoint_label: "t=0"
    wavelength_nm: 600
    plate_average: {a0}
    blank_mean: {bm0}
    cv_percent: {cv0}
    plate_reader_model: "Tecan Spark"
    well_readings:
{wr0}

  - id: "urn:amp2:prod:EPix1-t8h"
    product_type: "AMP2ODProduct"
    activity_id: "urn:amp2:act:dga-EPix1-t8h"
    plate_barcode: "EPix1"
    timepoint_label: "t=8h"
    wavelength_nm: 600
    plate_average: {a8}
    blank_mean: {bm8}
    cv_percent: {cv8}
    plate_reader_model: "Tecan Spark"
    well_readings:
{wr8}

  - id: "urn:amp2:prod:EPix1-t24h"
    product_type: "AMP2ODProduct"
    activity_id: "urn:amp2:act:dga-EPix1-t24h"
    plate_barcode: "EPix1"
    # [V3] timepoint_label intentionally omitted — required field missing
    wavelength_nm: 600
    plate_average: {a24}
    blank_mean: {bm24}
    cv_percent: {cv24}
    plate_reader_model: "Tecan Spark"
    well_readings:
{wr24}
"""


# ---------------------------------------------------------------------------
# Complex YAML
# ---------------------------------------------------------------------------

def build_complex_yaml() -> str:
    bw = BLANK_WELLS_COMPLEX

    tp_defs = [
        ("t=0",   "C_T0",  C_T0,   1, "2026-03-24T16:19:00"),
        ("t=4h",  "C_T4H", C_T4H,  2, "2026-03-24T20:19:00"),
        ("t=8h",  "C_T8H", C_T8H,  3, "2026-03-25T00:19:00"),
        ("t=16h", "C_T16H",C_T16H, 4, "2026-03-25T08:19:00"),
        ("t=24h", "C_T24H",C_T24H, 5, "2026-03-25T16:19:00"),
    ]

    wm = complex_well_metadata(pad=6)

    # Build DGA block — inject duplicate timepoint_label at t=8h [C6]
    dga_entries: list[str] = []
    for label, _, _, seq, acq in tp_defs:
        bad_wavelength = (label == "t=8h")   # the real t=8h entry is fine; we add a dup
        dga_entries.append(f"""\
  - id: "urn:amp2:act:dga-complex-{label.replace('=', '')}"
    activity_type: "AMP2dataGenerationActivity"
    name: "EPix1-complex OD read {label}"
    plate_setup_id: "urn:amp2:act:plate-setup-complex-001"
    plate_id: "urn:amp2:ps:EPix1-complex-plate-001"
    timepoint_label: "{label}"
    wavelength_nm: 600
    measurement_type: "optical_density"
    sequence_order: {seq}
    acquisition_time: "{acq}\"""")

    # [C6] Extra DGA that duplicates "t=8h" label
    dga_entries.append("""\
  - id: "urn:amp2:act:dga-complex-t8h-dup"
    # [C6] Duplicate timepoint_label — two DGAs both claim "t=8h" for same plate
    activity_type: "AMP2dataGenerationActivity"
    name: "EPix1-complex OD read t=8h (DUPLICATE — violation C6)"
    plate_setup_id: "urn:amp2:act:plate-setup-complex-001"
    plate_id: "urn:amp2:ps:EPix1-complex-plate-001"
    timepoint_label: "t=8h"
    wavelength_nm: 600
    measurement_type: "optical_density"
    sequence_order: 3
    acquisition_time: "2026-03-25T00:45:00\"""")

    dga_block = "\n\n".join(dga_entries)

    # Build product blocks
    prod_entries: list[str] = []
    for i, (label, _, values, seq, _) in enumerate(tp_defs):
        a, bm, cv = stats(values, bw)
        # [C4] inject bad position in t=4h product (well A1 → "A-1")
        bad_pos = "A-1" if label == "t=4h" else None
        wr = readings_block(values, bw, bad_pos=bad_pos, pad=8)
        prod_entries.append(f"""\
  - id: "urn:amp2:prod:complex-{label.replace('=', '')}"
    product_type: "AMP2ODProduct"
    activity_id: "urn:amp2:act:dga-complex-{label.replace('=', '')}"
    plate_barcode: "EPix1-complex"
    timepoint_label: "{label}"
    wavelength_nm: 600
    plate_average: {a}
    blank_mean: {bm}
    cv_percent: {cv}
    plate_reader_model: "Tecan Spark"{"" if label != "t=4h" else chr(10) + "    # [C4] well A1 position formatted as 'A-1' (invalid) in well_readings below"}
    well_readings:
{wr}""")

    prod_block = "\n\n".join(prod_entries)

    return f"""\
# =============================================================================
# amp2-complex-001.yaml
#
# Scenario: Two strains (KT2440 pTE314 + E. coli BL21-DE3), two media batches
#   (M9+glucose, LB), per-well media overrides, 5 OD timepoints at 600nm.
#   Cols 1–6 → KT2440 / M9 arm; cols 7–12 → BL21 / LB arm; row H = blanks.
#
# Intentional violations (for schema / DB validation testing):
#   [C1] media_type: "experimental_batch" on lb-media-prep — not in MediaTypeEnum
#   [C2] media_ref on bL21 experimental culture points to nonexistent UUID
#   [C3] ph_target: 7.5 on lb-media-prep without ph_adjustment: true
#   [C4] well position "A-1" (should be "A1") in t=4h plate_product well_readings
#   [C5] inoculum_volume_ul missing (required) on wells A3, B7, D11
#   [C6] duplicate timepoint_label "t=8h" on two data_generation_activities
# =============================================================================

strains:
  - id: "urn:amp2:strain:KT2440-pTE314"
    entity_type: "strain"
    name: "Pseudomonas putida KT2440 pTE314"
    strain_identifier: "KT2440_pTE314"
    strain_type: "bacterial"
    strain_source: "PNNL"
    strain_mutation: "pTE314"

  - id: "urn:amp2:strain:BL21-DE3"
    entity_type: "strain"
    name: "Escherichia coli BL21-DE3"
    strain_identifier: "BL21-DE3"
    strain_type: "bacterial"
    strain_source: "ATCC"
    strain_mutation: null

processed_samples:
  - id: "urn:amp2:ps:M9-glucose-batch-002"
    name: "M9 + 1% glucose batch 002"
    sample_base_type: "processed_sample"
    processed_sample_type: "prepared_media"

  - id: "urn:amp2:ps:LB-media-batch-001"
    name: "LB broth batch 001"
    sample_base_type: "processed_sample"
    processed_sample_type: "prepared_media"

  - id: "urn:amp2:ps:KT2440-exp-output-complex"
    name: "KT2440 experimental culture for complex plate"
    sample_base_type: "processed_sample"
    processed_sample_type: "experimental_culture"

  - id: "urn:amp2:ps:BL21-exp-output-complex"
    name: "BL21-DE3 experimental culture for complex plate"
    sample_base_type: "processed_sample"
    processed_sample_type: "experimental_culture"

  - id: "urn:amp2:ps:EPix1-complex-plate-001"
    name: "EPix1-complex AMP2 96-well plate"
    sample_base_type: "processed_sample"
    processed_sample_type: "amp2_96well_plate"

media_preparations:
  - id: "urn:amp2:act:media-prep-M9-002"
    name: "M9 + 1% glucose preparation (complex)"
    media_type: "pre_culture"
    volume_ml: 500.0
    media_recipe: "M9 minimal salts with 1% glucose (w/v)"
    media_formulation: "manual_mix"
    sterilization_method: "autoclave"
    ph_adjustment: true
    ph_target: 7.0
    creation_date: "2026-03-20"
    output_sample_id: "urn:amp2:ps:M9-glucose-batch-002"

  - id: "urn:amp2:act:media-prep-LB-001"
    name: "LB broth preparation"
    media_type: "experimental_batch"   # [C1] "experimental_batch" not in MediaTypeEnum
    volume_ml: 300.0
    media_recipe: "Lysogeny broth: 10g/L tryptone, 5g/L yeast extract, 10g/L NaCl"
    media_formulation: "manual_mix"
    sterilization_method: "autoclave"
    ph_adjustment: false
    ph_target: 7.5   # [C3] ph_target set but ph_adjustment is false
    creation_date: "2026-03-21"
    output_sample_id: "urn:amp2:ps:LB-media-batch-001"

culture_growth_activities:
  - id: "urn:amp2:act:complex-kt2440-preculture"
    activity_type: "PreCultureGrowth"
    name: "KT2440 pre-culture (complex)"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-002"
    incubation_time_hours: 12.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "flask"
    input_sample_id: null
    output_sample_id: "urn:amp2:ps:KT2440-exp-output-complex"

  - id: "urn:amp2:act:complex-kt2440-experimental"
    activity_type: "ExperimentalCulture"
    name: "KT2440 experimental culture — nickel stress 0.5 mM"
    strain_ref: "urn:amp2:strain:KT2440-pTE314"
    media_ref: "urn:amp2:ps:M9-glucose-batch-002"
    incubation_time_hours: 4.0
    temperature_celsius: 30.0
    agitation_speed_rpm: 200
    oxygen_status: "aerobic"
    container_type: "flask"
    treatment_type: "nickel_stress"
    growth_time: "4 hours"
    input_sample_id: "urn:amp2:ps:KT2440-exp-output-complex"
    output_sample_id: "urn:amp2:ps:KT2440-exp-output-complex"

  - id: "urn:amp2:act:complex-bl21-experimental"
    activity_type: "ExperimentalCulture"
    name: "BL21-DE3 experimental culture — nickel stress 0.5 mM"
    strain_ref: "urn:amp2:strain:BL21-DE3"
    media_ref: "urn:amp2:ps:NONEXISTENT-MEDIA-999"   # [C2] broken FK — ID does not exist
    incubation_time_hours: 4.0
    temperature_celsius: 37.0
    agitation_speed_rpm: 220
    oxygen_status: "aerobic"
    container_type: "flask"
    treatment_type: "nickel_stress"
    growth_time: "4 hours"
    input_sample_id: null
    output_sample_id: "urn:amp2:ps:BL21-exp-output-complex"

plate_setup_activities:
  - id: "urn:amp2:act:plate-setup-complex-001"
    activity_type: "AMP2PlateSetupActivity"
    name: "EPix1-complex plate setup — dual-strain, per-well media"
    plate_type: "Greiner_96well_flat_bottom"
    plate_barcode: "EPix1-complex"
    setup_date: "2026-03-24T15:30:00"
    setup_operator_id: "kapu336"
    setup_instrument: "manual"
    sealing_method: "BreathEasy_membrane"
    # No plate-level media_ref — per-well overrides used instead
    input_sample_id: "urn:amp2:ps:KT2440-exp-output-complex"
    output_sample_id: "urn:amp2:ps:EPix1-complex-plate-001"
    well_metadata:
{wm}

data_generation_activities:
{dga_block}

plate_products:
{prod_block}
"""


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path}")


def write_vanilla_csvs(out_dir: Path) -> None:
    bw = BLANK_WELLS_VANILLA

    # 01 strains
    write_csv(out_dir / "01_strains.csv",
              ["id", "entity_type", "name", "strain_identifier", "strain_type",
               "strain_source", "strain_mutation"],
              [{"id": "urn:amp2:strain:KT2440-pTE314",
                "entity_type": "strain",
                "name": "Pseudomonas putida KT2440 pTE314",
                "strain_identifier": "KT2440_pTE314",
                "strain_type": "bacterial",
                "strain_source": "PNNL",
                "strain_mutation": "pTE314"}])

    # 02 media_preparations
    write_csv(out_dir / "02_media_preparations.csv",
              ["id", "name", "media_type", "volume_ml", "media_recipe",
               "media_formulation", "sterilization_method", "ph_adjustment",
               "ph_target", "creation_date", "storage_temperature",
               "media_additions", "output_sample_id"],
              [{"id": "urn:amp2:act:media-prep-M9-001",
                "name": "M9 + 1% glucose preparation",
                "media_type": "pre_culture",
                "volume_ml": 500.0,
                "media_recipe": "M9 minimal salts with 1% glucose (w/v)",
                "media_formulation": "manual_mix",
                "sterilization_method": "autoclave",
                "ph_adjustment": True,
                "ph_target": 7.0,
                "creation_date": "2026-03-20",
                "storage_temperature": "4 C",
                "media_additions": "1% glucose (w/v)",
                "output_sample_id": "urn:amp2:ps:M9-glucose-batch-001"}])

    # 03 culture_activities
    write_csv(out_dir / "03_culture_activities.csv",
              ["id", "activity_type", "name", "strain_ref", "media_ref",
               "incubation_time_hours", "temperature_celsius", "agitation_speed_rpm",
               "oxygen_status", "container_type", "treatment_type", "growth_time",
               "preparation_date", "inspection_method", "target_strain",
               "input_sample_id", "output_sample_id"],
              [
                  {"id": "urn:amp2:act:strain-purity-001",
                   "activity_type": "StrainPurity",
                   "name": "KT2440 pTE314 strain purity check",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-001",
                   "incubation_time_hours": 24.0,
                   "temperature_celsius": 30.0,
                   "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic",
                   "container_type": "tube",
                   "inspection_method": "visual",
                   "target_strain": "KT2440_pTE314",
                   "input_sample_id": "",
                   "output_sample_id": "urn:amp2:ps:KT2440-purity-output-001"},
                  {"id": "urn:amp2:act:stock-culture-001",
                   "activity_type": "StockCulturePreparation",
                   "name": "KT2440 pTE314 stock culture preparation",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-001",
                   "incubation_time_hours": 16.0,
                   "temperature_celsius": 30.0,
                   "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic",
                   "container_type": "flask",
                   "preparation_date": "2026-03-21",
                   "input_sample_id": "urn:amp2:ps:KT2440-purity-output-001",
                   "output_sample_id": "urn:amp2:ps:KT2440-stock-output-001"},
                  {"id": "urn:amp2:act:preculture-001",
                   "activity_type": "PreCultureGrowth",
                   "name": "KT2440 pTE314 pre-culture",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-001",
                   "incubation_time_hours": 12.0,
                   "temperature_celsius": 30.0,
                   "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic",
                   "container_type": "flask",
                   "input_sample_id": "urn:amp2:ps:KT2440-stock-output-001",
                   "output_sample_id": "urn:amp2:ps:KT2440-preculture-output-001"},
                  {"id": "urn:amp2:act:experimental-culture-001",
                   "activity_type": "ExperimentalCulture",
                   "name": "KT2440 pTE314 experimental culture — no treatment",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-001",
                   "incubation_time_hours": 4.0,
                   "temperature_celsius": 30.0,
                   "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic",
                   "container_type": "flask",
                   "treatment_type": "none",
                   "growth_time": "4 hours",
                   "input_sample_id": "urn:amp2:ps:KT2440-preculture-output-001",
                   "output_sample_id": "urn:amp2:ps:KT2440-experimental-output-001"},
              ])

    # 04 plate_setup
    write_csv(out_dir / "04_plate_setup.csv",
              ["id", "activity_type", "plate_type", "plate_barcode", "setup_date",
               "setup_operator_id", "setup_instrument", "sealing_method",
               "media_ref", "input_sample_id", "output_sample_id",
               "violation_note"],
              [{"id": "urn:amp2:act:plate-setup-EPix1-001",
                "activity_type": "AMP2PlateSetupActivity",
                "plate_type": "Greiner_96well_flat_bottom",
                "plate_barcode": "EPix1",
                "setup_date": "",           # [V2] intentionally blank
                "setup_operator_id": "kapu336",
                "setup_instrument": "manual",
                "sealing_method": "BreathEasy_membrane",
                "media_ref": "urn:amp2:ps:M9-glucose-batch-001",
                "input_sample_id": "urn:amp2:ps:KT2440-experimental-output-001",
                "output_sample_id": "urn:amp2:ps:EPix1-plate-001",
                "violation_note": "[V2] setup_date missing (required field)"}])

    # 05 well_metadata
    wm_rows: list[dict] = []
    for r in ROWS:
        for c in COLS:
            pos = f"{r}{c}"
            if r == "H":
                wm_rows.append({"plate_barcode": "EPix1", "position": pos,
                                 "well_type": "blank", "replicate_group": "",
                                 "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
                                 "sample_id": "", "media_ref_override": ""})
            else:
                wm_rows.append({"plate_barcode": "EPix1", "position": pos,
                                 "well_type": "sample", "replicate_group": f"rep_{c}",
                                 "media_volume_ul": 180.0, "inoculum_volume_ul": 20.0,
                                 "sample_id": f"KT2440-{pos}", "media_ref_override": ""})
    write_csv(out_dir / "05_well_metadata.csv",
              ["plate_barcode", "position", "well_type", "replicate_group",
               "media_volume_ul", "inoculum_volume_ul", "sample_id",
               "media_ref_override"],
              wm_rows)

    # 06 data_generation_activities
    dga_rows = [
        {"id": "urn:amp2:act:dga-EPix1-t0",
         "activity_type": "AMP2dataGenerationActivity",
         "plate_barcode": "EPix1",
         "timepoint_label": "t=0",
         "wavelength_nm": 600,
         "measurement_type": "optical_density",
         "sequence_order": 1,
         "acquisition_time": "2026-03-24T16:19:00",
         "violation_note": ""},
        {"id": "urn:amp2:act:dga-EPix1-t8h",
         "activity_type": "AMP2dataGenerationActivity",
         "plate_barcode": "EPix1",
         "timepoint_label": "t=8h",
         "wavelength_nm": "600nm",      # [V1]
         "measurement_type": "optical_density",
         "sequence_order": 2,
         "acquisition_time": "2026-03-25T00:19:00",
         "violation_note": "[V1] wavelength_nm is string '600nm' not integer 600"},
        {"id": "urn:amp2:act:dga-EPix1-t24h",
         "activity_type": "AMP2dataGenerationActivity",
         "plate_barcode": "EPix1",
         "timepoint_label": "t=24h",
         "wavelength_nm": 600,
         "measurement_type": "optical_density",
         "sequence_order": 3,
         "acquisition_time": "2026-03-25T16:19:00",
         "violation_note": ""},
    ]
    write_csv(out_dir / "06_data_generation_activities.csv",
              ["id", "activity_type", "plate_barcode", "timepoint_label",
               "wavelength_nm", "measurement_type", "sequence_order",
               "acquisition_time", "violation_note"],
              dga_rows)

    # 07 well_readings (one row per well per timepoint)
    timepoints = [
        ("t=0",  "urn:amp2:prod:EPix1-t0",   V_T0),
        ("t=8h", "urn:amp2:prod:EPix1-t8h",  V_T8H),
        ("t=24h","urn:amp2:prod:EPix1-t24h", V_T24H),
    ]
    wr_rows: list[dict] = []
    for label, prod_id, values in timepoints:
        for well in ALL_WELLS:
            val = values[well]
            flag = _flag(well, val, bw)
            violation = ""
            if label == "t=24h" and well == "A1":
                violation = "[V3] parent product missing timepoint_label"
            wr_rows.append({
                "product_id": prod_id,
                "plate_barcode": "EPix1",
                "timepoint_label": label if label != "t=24h" else "",  # [V3] propagated
                "position": well,
                "value": f"{val:.4f}",
                "flag": flag,
                "violation_note": violation,
            })
    write_csv(out_dir / "07_well_readings.csv",
              ["product_id", "plate_barcode", "timepoint_label", "position",
               "value", "flag", "violation_note"],
              wr_rows)


def write_complex_csvs(out_dir: Path) -> None:
    bw = BLANK_WELLS_COMPLEX

    # 01 strains
    write_csv(out_dir / "01_strains.csv",
              ["id", "entity_type", "name", "strain_identifier", "strain_type",
               "strain_source", "strain_mutation"],
              [
                  {"id": "urn:amp2:strain:KT2440-pTE314",
                   "entity_type": "strain",
                   "name": "Pseudomonas putida KT2440 pTE314",
                   "strain_identifier": "KT2440_pTE314",
                   "strain_type": "bacterial",
                   "strain_source": "PNNL",
                   "strain_mutation": "pTE314"},
                  {"id": "urn:amp2:strain:BL21-DE3",
                   "entity_type": "strain",
                   "name": "Escherichia coli BL21-DE3",
                   "strain_identifier": "BL21-DE3",
                   "strain_type": "bacterial",
                   "strain_source": "ATCC",
                   "strain_mutation": ""},
              ])

    # 02 media_preparations
    write_csv(out_dir / "02_media_preparations.csv",
              ["id", "name", "media_type", "volume_ml", "media_recipe",
               "media_formulation", "sterilization_method", "ph_adjustment",
               "ph_target", "creation_date", "output_sample_id", "violation_note"],
              [
                  {"id": "urn:amp2:act:media-prep-M9-002",
                   "name": "M9 + 1% glucose preparation (complex)",
                   "media_type": "pre_culture",
                   "volume_ml": 500.0,
                   "media_recipe": "M9 minimal salts with 1% glucose (w/v)",
                   "media_formulation": "manual_mix",
                   "sterilization_method": "autoclave",
                   "ph_adjustment": True,
                   "ph_target": 7.0,
                   "creation_date": "2026-03-20",
                   "output_sample_id": "urn:amp2:ps:M9-glucose-batch-002",
                   "violation_note": ""},
                  {"id": "urn:amp2:act:media-prep-LB-001",
                   "name": "LB broth preparation",
                   "media_type": "experimental_batch",  # [C1]
                   "volume_ml": 300.0,
                   "media_recipe": "Lysogeny broth: 10g/L tryptone, 5g/L yeast, 10g/L NaCl",
                   "media_formulation": "manual_mix",
                   "sterilization_method": "autoclave",
                   "ph_adjustment": False,
                   "ph_target": 7.5,  # [C3]
                   "creation_date": "2026-03-21",
                   "output_sample_id": "urn:amp2:ps:LB-media-batch-001",
                   "violation_note": "[C1] invalid media_type enum; [C3] ph_target set without ph_adjustment"},
              ])

    # 03 culture_activities
    write_csv(out_dir / "03_culture_activities.csv",
              ["id", "activity_type", "name", "strain_ref", "media_ref",
               "incubation_time_hours", "temperature_celsius", "agitation_speed_rpm",
               "oxygen_status", "container_type", "treatment_type",
               "input_sample_id", "output_sample_id", "violation_note"],
              [
                  {"id": "urn:amp2:act:complex-kt2440-preculture",
                   "activity_type": "PreCultureGrowth",
                   "name": "KT2440 pre-culture (complex)",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-002",
                   "incubation_time_hours": 12.0,
                   "temperature_celsius": 30.0, "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic", "container_type": "flask",
                   "input_sample_id": "", "output_sample_id": "urn:amp2:ps:KT2440-exp-output-complex",
                   "violation_note": ""},
                  {"id": "urn:amp2:act:complex-kt2440-experimental",
                   "activity_type": "ExperimentalCulture",
                   "name": "KT2440 experimental — nickel stress 0.5 mM",
                   "strain_ref": "urn:amp2:strain:KT2440-pTE314",
                   "media_ref": "urn:amp2:ps:M9-glucose-batch-002",
                   "incubation_time_hours": 4.0,
                   "temperature_celsius": 30.0, "agitation_speed_rpm": 200,
                   "oxygen_status": "aerobic", "container_type": "flask",
                   "treatment_type": "nickel_stress",
                   "input_sample_id": "urn:amp2:ps:KT2440-exp-output-complex",
                   "output_sample_id": "urn:amp2:ps:KT2440-exp-output-complex",
                   "violation_note": ""},
                  {"id": "urn:amp2:act:complex-bl21-experimental",
                   "activity_type": "ExperimentalCulture",
                   "name": "BL21-DE3 experimental — nickel stress 0.5 mM",
                   "strain_ref": "urn:amp2:strain:BL21-DE3",
                   "media_ref": "urn:amp2:ps:NONEXISTENT-MEDIA-999",  # [C2]
                   "incubation_time_hours": 4.0,
                   "temperature_celsius": 37.0, "agitation_speed_rpm": 220,
                   "oxygen_status": "aerobic", "container_type": "flask",
                   "treatment_type": "nickel_stress",
                   "input_sample_id": "", "output_sample_id": "urn:amp2:ps:BL21-exp-output-complex",
                   "violation_note": "[C2] media_ref points to nonexistent processed_sample ID"},
              ])

    # 04 plate_setup
    write_csv(out_dir / "04_plate_setup.csv",
              ["id", "activity_type", "plate_type", "plate_barcode", "setup_date",
               "setup_operator_id", "setup_instrument", "sealing_method",
               "media_ref", "input_sample_id", "output_sample_id", "violation_note"],
              [{"id": "urn:amp2:act:plate-setup-complex-001",
                "activity_type": "AMP2PlateSetupActivity",
                "plate_type": "Greiner_96well_flat_bottom",
                "plate_barcode": "EPix1-complex",
                "setup_date": "2026-03-24T15:30:00",
                "setup_operator_id": "kapu336",
                "setup_instrument": "manual",
                "sealing_method": "BreathEasy_membrane",
                "media_ref": "",   # no plate-level media; per-well overrides used
                "input_sample_id": "urn:amp2:ps:KT2440-exp-output-complex",
                "output_sample_id": "urn:amp2:ps:EPix1-complex-plate-001",
                "violation_note": "No plate-level media_ref (per-well overrides used)"}])

    # 05 well_metadata
    m9_id = "urn:amp2:ps:M9-glucose-batch-002"
    lb_id = "urn:amp2:ps:LB-media-batch-001"
    missing_inoculum = {"A3", "B7", "D11"}
    wm_rows: list[dict] = []
    for r in ROWS:
        for c in COLS:
            pos = f"{r}{c}"
            if r == "H":
                wm_rows.append({"plate_barcode": "EPix1-complex", "position": pos,
                                 "well_type": "blank", "replicate_group": "",
                                 "media_ref_override": "",
                                 "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
                                 "sample_id": "", "strain_arm": "",
                                 "violation_note": ""})
            else:
                media_ref = m9_id if c <= 6 else lb_id
                strain_arm = "KT2440" if c <= 6 else "BL21"
                vol = "" if pos in missing_inoculum else 20.0  # [C5]
                note = "[C5] inoculum_volume_ul missing (required)" if pos in missing_inoculum else ""
                wm_rows.append({"plate_barcode": "EPix1-complex", "position": pos,
                                 "well_type": "sample", "replicate_group": f"rep_{c}",
                                 "media_ref_override": media_ref,
                                 "media_volume_ul": 180.0, "inoculum_volume_ul": vol,
                                 "sample_id": f"{strain_arm}-{pos}",
                                 "strain_arm": strain_arm,
                                 "violation_note": note})
    write_csv(out_dir / "05_well_metadata.csv",
              ["plate_barcode", "position", "well_type", "replicate_group",
               "media_ref_override", "media_volume_ul", "inoculum_volume_ul",
               "sample_id", "strain_arm", "violation_note"],
              wm_rows)

    # 06 data_generation_activities (includes duplicate t=8h [C6])
    tp_defs = [
        ("t=0",  1, "2026-03-24T16:19:00"),
        ("t=4h", 2, "2026-03-24T20:19:00"),
        ("t=8h", 3, "2026-03-25T00:19:00"),
        ("t=16h",4, "2026-03-25T08:19:00"),
        ("t=24h",5, "2026-03-25T16:19:00"),
    ]
    dga_rows = [
        {"id": f"urn:amp2:act:dga-complex-{label.replace('=','')}",
         "activity_type": "AMP2dataGenerationActivity",
         "plate_barcode": "EPix1-complex",
         "timepoint_label": label,
         "wavelength_nm": 600,
         "sequence_order": seq,
         "acquisition_time": acq,
         "violation_note": ""}
        for label, seq, acq in tp_defs
    ]
    dga_rows.append({
        "id": "urn:amp2:act:dga-complex-t8h-dup",
        "activity_type": "AMP2dataGenerationActivity",
        "plate_barcode": "EPix1-complex",
        "timepoint_label": "t=8h",           # [C6] duplicate
        "wavelength_nm": 600,
        "sequence_order": 3,
        "acquisition_time": "2026-03-25T00:45:00",
        "violation_note": "[C6] duplicate timepoint_label 't=8h' for same plate",
    })
    write_csv(out_dir / "06_data_generation_activities.csv",
              ["id", "activity_type", "plate_barcode", "timepoint_label",
               "wavelength_nm", "sequence_order", "acquisition_time", "violation_note"],
              dga_rows)

    # 07 well_readings
    tp_values = [
        ("t=0",   "urn:amp2:prod:complex-t0",   C_T0),
        ("t=4h",  "urn:amp2:prod:complex-t4h",  C_T4H),
        ("t=8h",  "urn:amp2:prod:complex-t8h",  C_T8H),
        ("t=16h", "urn:amp2:prod:complex-t16h", C_T16H),
        ("t=24h", "urn:amp2:prod:complex-t24h", C_T24H),
    ]
    wr_rows: list[dict] = []
    for label, prod_id, values in tp_values:
        for well in ALL_WELLS:
            val = values[well]
            flag = _flag(well, val, bw)
            pos = well
            note = ""
            if label == "t=4h" and well == "A1":
                pos = "A-1"   # [C4]
                note = "[C4] position 'A-1' should be 'A1'"
            wr_rows.append({
                "product_id": prod_id,
                "plate_barcode": "EPix1-complex",
                "timepoint_label": label,
                "position": pos,
                "value": f"{val:.4f}",
                "flag": flag,
                "violation_note": note,
            })
    write_csv(out_dir / "07_well_readings.csv",
              ["product_id", "plate_barcode", "timepoint_label", "position",
               "value", "flag", "violation_note"],
              wr_rows)


# ---------------------------------------------------------------------------
# SQL harness
# ---------------------------------------------------------------------------

SQL_HARNESS = """\
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
"""


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AMP2 validation test data.")
    parser.add_argument(
        "--root",
        default=".",
        help="Repo root (default: current directory)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    invalid_dir = root / "src" / "data" / "examples" / "invalid"
    tests_dir   = root / "tests"

    # YAML files
    vanilla_yaml = invalid_dir / "amp2-vanilla-001.yaml"
    complex_yaml = invalid_dir / "amp2-complex-001.yaml"

    invalid_dir.mkdir(parents=True, exist_ok=True)
    vanilla_yaml.write_text(build_vanilla_yaml(), encoding="utf-8")
    print(f"wrote {vanilla_yaml}")

    complex_yaml.write_text(build_complex_yaml(), encoding="utf-8")
    print(f"wrote {complex_yaml}")

    # CSV companions
    vanilla_csv_dir = invalid_dir / "amp2-vanilla-001"
    complex_csv_dir = invalid_dir / "amp2-complex-001"

    print("\nVanilla CSVs:")
    write_vanilla_csvs(vanilla_csv_dir)
    print("\nComplex CSVs:")
    write_complex_csvs(complex_csv_dir)

    # SQL harness
    tests_dir.mkdir(parents=True, exist_ok=True)
    sql_path = tests_dir / "amp2_plate_validation.sql"
    sql_path.write_text(SQL_HARNESS, encoding="utf-8")
    print(f"\nwrote {sql_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
