#!/usr/bin/env python3
"""
Generate a simulated AMP2 dataset (YAML + CSVs) for the BASALT schema.

Scenario: 15 AMP2UserSample instances, mapped many-to-one onto 8 organism
records, each pushed through the full AMP2 lab workflow
(StrainPurity -> StockCulturePreparation -> PreCultureGrowth ->
ExperimentalCulture -> plate setup), then read for OD600 every 2 h for 24 h
on three plates (two 96-well, one 384-well).

Deterministic: seeded RNG, no wall-clock dependence.
"""

import csv
import os
import random
import zlib
from datetime import datetime, timedelta

RNG = random.Random(20260813)

OUT_DIR = os.environ.get(
    "AMP2_OUT",
    "/Users/maia.kapur/Library/CloudStorage/OneDrive-PNNL/Documents/CAM/"
    "analysis-db/analysis-api-schema/src/data/examples/valid",
)
BUNDLE = "amp2-full-workflow-002"
CSV_DIR = os.path.join(OUT_DIR, BUNDLE)
YAML_PATH = os.path.join(OUT_DIR, BUNDLE + ".yaml")

# ---------------------------------------------------------------------------
# People / instruments
# ---------------------------------------------------------------------------

PEOPLE = [
    {"id": "urn:amp2:person:kapu336", "first_name": "Maia", "last_name": "Kapur",
     "email": "maia.kapur@pnnl.gov", "orcid": "0000-0002-5605-2107"},
    {"id": "urn:amp2:person:elga519", "first_name": "Rosalind", "last_name": "Elgar",
     "email": "rosalind.elgar@pnnl.gov", "orcid": "0000-0001-8834-2261"},
    {"id": "urn:amp2:person:navi204", "first_name": "Devin", "last_name": "Navarro",
     "email": "devin.navarro@pnnl.gov", "orcid": "0000-0003-4471-9082"},
]

INSTRUMENTS = [
    {"id": "urn:amp2:instrument:plate-reader-001",
     "name": "BioTek Epoch2 microplate spectrophotometer",
     "serial_number": "EPOCH2-19F0142",
     "reader_model": "BioTek Epoch2"},
    {"id": "urn:amp2:instrument:plate-reader-002",
     "name": "Tecan Spark 10M multimode reader",
     "serial_number": "SPARK-2104773",
     "reader_model": "Tecan Spark 10M"},
    {"id": "urn:amp2:instrument:liquid-handler-001",
     "name": "Hamilton Microlab STAR liquid handler",
     "serial_number": "STAR-8817",
     "reader_model": None},
]

# ---------------------------------------------------------------------------
# Organisms  (8 records; fields follow organism.yaml / CRISPRi_Pp_11strains.csv)
# ---------------------------------------------------------------------------

ORGANISMS = [
    {
        "id": "urn:amp2:organism:AG5577-pJE2165",
        "name": "Pseudomonas putida AG5577-pJE2165",
        "description": "SAGE 3x landing pad parent strain carrying a "
                       "vanillate-inducible dCas12a cassette in the genome.",
        "strain_identifier": "AG5577-pJE2165",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "engineered from KT2440",
        "strain_type": "bacterial",
        "modification_method": "electroporation",
        "strain_description": "SAGE 3x landing pad parent strain with "
                              "CV-inducible dCas12a in the genome",
        "strain_mutation": "pJE2165",
        "phenotype": "apramycin resistance, gene knockdown dCas12a construct",
        "trait": "bacterial_resistance",
        "encoded_traits": "apramycin resistance (aac(3)IV); "
                          "vanillate-inducible dCas12a",
        "genotype_segment_category": "Gene(s) of Interest",
        "genotype_segment_name": "aprR_pJE-dCas12a",
        "component_name": "dCas12a",
        "construct_component": "Gene",
        "donor_organism": "Francisella novicida",
        "component_description": "d-Cpf1 nuclease-dead effector used to block "
                                 "gene expression",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        "id": "urn:amp2:organism:PP-0055",
        "name": "Pseudomonas putida PP_0055 CRISPRi knockdown",
        "description": "AG5577-pJE2165 background carrying a four-guide "
                       "CRISPRi array targeting PP_0055.",
        "strain_identifier": "PP_0055",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "engineered from KT2440",
        "strain_type": "bacterial",
        "modification_method": "electroporation",
        "strain_description": "AG5577-pJE2165 with CRISPRi guide array "
                              "targeting PP_0055",
        "strain_mutation": "pJE2165 + PP_0055 guide array",
        "phenotype": "knockdown guide array",
        "trait": "other",
        "encoded_traits": "apramycin resistance; PP_0055 transcriptional "
                          "knockdown on vanillate induction",
        "genotype_segment_category": "Gene Silencer",
        "genotype_segment_name": "PP_0055 guide array",
        "component_name": "4_sgRNAs",
        "construct_component": "Recognition Sequence",
        "donor_organism": "synthetic",
        "component_description": "recognition sequence for guide RNA "
                                 "processing",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        "id": "urn:amp2:organism:PP-1021",
        "name": "Pseudomonas putida PP_1021 CRISPRi knockdown",
        "description": "AG5577-pJE2165 background carrying a four-guide "
                       "CRISPRi array targeting PP_1021.",
        "strain_identifier": "PP_1021",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "engineered from KT2440",
        "strain_type": "bacterial",
        "modification_method": "electroporation",
        "strain_description": "AG5577-pJE2165 with CRISPRi guide array "
                              "targeting PP_1021",
        "strain_mutation": "pJE2165 + PP_1021 guide array",
        "phenotype": "knockdown guide array",
        "trait": "other",
        "encoded_traits": "apramycin resistance; PP_1021 transcriptional "
                          "knockdown on vanillate induction",
        "genotype_segment_category": "Gene Silencer",
        "genotype_segment_name": "PP_1021 guide array",
        "component_name": "4_sgRNAs",
        "construct_component": "Recognition Sequence",
        "donor_organism": "synthetic",
        "component_description": "recognition sequence for guide RNA "
                                 "processing",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        "id": "urn:amp2:organism:PP-3186",
        "name": "Pseudomonas putida PP_3186 CRISPRi knockdown",
        "description": "AG5577-pJE2165 background carrying a four-guide "
                       "CRISPRi array targeting PP_3186.",
        "strain_identifier": "PP_3186",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "engineered from KT2440",
        "strain_type": "bacterial",
        "modification_method": "electroporation",
        "strain_description": "AG5577-pJE2165 with CRISPRi guide array "
                              "targeting PP_3186",
        "strain_mutation": "pJE2165 + PP_3186 guide array",
        "phenotype": "knockdown guide array",
        "trait": "other",
        "encoded_traits": "apramycin resistance; PP_3186 transcriptional "
                          "knockdown on vanillate induction",
        "genotype_segment_category": "Gene Silencer",
        "genotype_segment_name": "PP_3186 guide array",
        "component_name": "4_sgRNAs",
        "construct_component": "Recognition Sequence",
        "donor_organism": "synthetic",
        "component_description": "recognition sequence for guide RNA "
                                 "processing",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        "id": "urn:amp2:organism:PP-5325",
        "name": "Pseudomonas putida PP_5325 CRISPRi knockdown",
        "description": "AG5577-pJE2165 background carrying a four-guide "
                       "CRISPRi array targeting PP_5325.",
        "strain_identifier": "PP_5325",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "engineered from KT2440",
        "strain_type": "bacterial",
        "modification_method": "electroporation",
        "strain_description": "AG5577-pJE2165 with CRISPRi guide array "
                              "targeting PP_5325",
        "strain_mutation": "pJE2165 + PP_5325 guide array",
        "phenotype": "knockdown guide array",
        "trait": "other",
        "encoded_traits": "apramycin resistance; PP_5325 transcriptional "
                          "knockdown on vanillate induction",
        "genotype_segment_category": "Gene Silencer",
        "genotype_segment_name": "PP_5325 guide array",
        "component_name": "4_sgRNAs",
        "construct_component": "Recognition Sequence",
        "donor_organism": "synthetic",
        "component_description": "recognition sequence for guide RNA "
                                 "processing",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        # Unmodified reference organism: exercises null genotype/trait slots.
        "id": "urn:amp2:organism:KT2440-WT",
        "name": "Pseudomonas putida KT2440 wild type",
        "description": "Unmodified KT2440 reference strain used as the "
                       "growth control across all three plates.",
        "strain_identifier": "KT2440_WT",
        "organism_name": "Pseudomonas putida",
        "taxonomy_id": "NCBITaxon:160488",
        "host_common_name": "Pseudomonas putida",
        "host_taxid": "NCBITaxon:160488",
        "strain_source": "ATCC 47054",
        "strain_type": "bacterial",
        "modification_method": None,
        "strain_description": "Wild type; no engineered modification.",
        "strain_mutation": None,
        "phenotype": None,
        "trait": None,
        "encoded_traits": None,
        "genotype_segment_category": "Wild Type",
        "genotype_segment_name": None,
        "component_name": None,
        "construct_component": "None",
        "donor_organism": None,
        "component_description": None,
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "asexual",
    },
    {
        "id": "urn:amp2:organism:RHA1-pTE314",
        "name": "Rhodococcus jostii RHA1 pTE314",
        "description": "Aromatic-degrading actinobacterium carrying a "
                       "conjugative vanillate catabolism reporter plasmid.",
        "strain_identifier": "RHA1_pTE314",
        "organism_name": "Rhodococcus jostii",
        "taxonomy_id": "NCBITaxon:101510",
        "host_common_name": "Rhodococcus jostii",
        "host_taxid": "NCBITaxon:101510",
        "strain_source": "PNNL; derived from RHA1 (Eltis lab)",
        "strain_type": "bacterial",
        "modification_method": "conjugation",
        "strain_description": "RHA1 with pTE314 carrying a vanillate-responsive "
                              "reporter and kanamycin marker",
        "strain_mutation": "pTE314",
        "phenotype": "kanamycin resistance, enhanced aromatic catabolism",
        "trait": "product_quality",
        "encoded_traits": "kanamycin resistance; xenobiotic (aromatic) "
                          "degradation",
        "genotype_segment_category": "Selectable Marker",
        "genotype_segment_name": "kanR_pTE314",
        "component_name": "nptII",
        "construct_component": "Gene",
        "donor_organism": "Escherichia coli (Tn5)",
        "component_description": "neomycin phosphotransferase II conferring "
                                 "kanamycin resistance",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "none reported",
        "host_spec_range": None,
        "propagation": "incompatibility group IncP",
    },
    {
        # Non-bacterial organism: exercises strain_type=fungal and a
        # different trophic/propagation vocabulary.
        "id": "urn:amp2:organism:IFO0880-LIP1",
        "name": "Rhodotorula toruloides IFO0880 LIP1-OE",
        "description": "Oleaginous yeast engineered for lipid accumulation "
                       "via LIP1 overexpression.",
        "strain_identifier": "IFO0880_LIP1-OE",
        "organism_name": "Rhodotorula toruloides",
        "taxonomy_id": "NCBITaxon:5286",
        "host_common_name": "Rhodotorula toruloides",
        "host_taxid": "NCBITaxon:5286",
        "strain_source": "engineered from IFO0880 (NBRC)",
        "strain_type": "fungal",
        "modification_method": "transformation",
        "strain_description": "IFO0880 with a constitutive LIP1 "
                              "overexpression cassette integrated at the "
                              "CAR2 locus",
        "strain_mutation": "PGPD1-LIP1 at CAR2",
        "phenotype": "elevated neutral lipid accumulation, nourseothricin "
                     "resistance",
        "trait": "product_quality",
        "encoded_traits": "nourseothricin resistance; increased "
                          "triacylglycerol yield",
        "genotype_segment_category": "Gene(s) of Interest",
        "genotype_segment_name": "PGPD1-LIP1",
        "component_name": "GPD1 promoter",
        "construct_component": "Promoter",
        "donor_organism": "Rhodotorula toruloides",
        "component_description": "constitutive glyceraldehyde-3-phosphate "
                                 "dehydrogenase promoter driving LIP1",
        "trophic_level": "chemoorganoheterotroph",
        "pathogenicity": "opportunistic in immunocompromised humans",
        "host_spec_range": "NCBITaxon:9606",
        "propagation": "asexual",
    },
]
ORG_BY_ID = {o["id"]: o for o in ORGANISMS}

# ---------------------------------------------------------------------------
# AMP2UserSample records
#
# Sample identity, spelled out because this is where the ingestion team got
# confused:
#   * `id`   -- the database primary key (urn:amp2:sample:AMP2-00NN).
#              This is the value every FK in this dataset points at,
#              including AMP2WellMetadata.sample_id.
#   * `name` -- the human-readable sample name the submitter wrote on the
#              tube, e.g. "PP_0055-R1". NOT unique across organisms by
#              construction, but unique here.
# The organism (strain identity) lives on the organism record and is reached
# through organism_ref; it is deliberately NOT the sample id.
# ---------------------------------------------------------------------------

# (sample_name, organism_id, biological replicate number)
SAMPLE_SPEC = [
    ("AG5577-pJE2165-R1", "urn:amp2:organism:AG5577-pJE2165", 1),
    ("AG5577-pJE2165-R2", "urn:amp2:organism:AG5577-pJE2165", 2),
    ("PP_0055-R1",        "urn:amp2:organism:PP-0055", 1),
    ("PP_0055-R2",        "urn:amp2:organism:PP-0055", 2),
    ("PP_0055-R3",        "urn:amp2:organism:PP-0055", 3),
    ("PP_1021-R1",        "urn:amp2:organism:PP-1021", 1),
    ("PP_3186-R1",        "urn:amp2:organism:PP-3186", 1),
    ("PP_3186-R2",        "urn:amp2:organism:PP-3186", 2),
    ("PP_5325-R1",        "urn:amp2:organism:PP-5325", 1),
    ("KT2440_WT-R1",      "urn:amp2:organism:KT2440-WT", 1),
    ("KT2440_WT-R2",      "urn:amp2:organism:KT2440-WT", 2),
    ("RHA1_pTE314-R1",    "urn:amp2:organism:RHA1-pTE314", 1),
    ("RHA1_pTE314-R2",    "urn:amp2:organism:RHA1-pTE314", 2),
    ("IFO0880_LIP1-R1",   "urn:amp2:organism:IFO0880-LIP1", 1),
    ("IFO0880_LIP1-R2",   "urn:amp2:organism:IFO0880-LIP1", 2),
]

SAMPLES = []
for i, (sname, org_id, rep) in enumerate(SAMPLE_SPEC, start=1):
    org = ORG_BY_ID[org_id]
    yeast = org["strain_type"] == "fungal"
    SAMPLES.append({
        "id": "urn:amp2:sample:AMP2-%04d" % i,
        "name": sname,
        "sample_number": i,
        "organism_ref": org_id,
        "description": "Biological replicate %d of %s submitted for the AMP2 "
                       "growth screen." % (rep, org["strain_identifier"]),
        "collection_date": "2026-04-15",
        "growth_facil": "lab_incubation",
        "isol_growth_condt": "DOI: 10.1126/sciadv.ade1285",
        "start_date_inc": "2026-04-16",
        "storage_condition": "frozen",
        "storage_temperature": "-80 C",
        "shipped_sample_size": "1.5 mL" if not yeast else "1.0 mL",
        "guid_source": "LIMS",
        "other_guid_source": None,
        "analysis_type": "analysis_activity",
        "cbi": False,
        "lims_barcode": "EMSL-AMP2-%06d" % (480100 + i),
        "emsl_activity": "AMP2 FY26 microbial growth screen",
        "replicate_number": rep,
    })
SAMPLE_BY_ID = {s["id"]: s for s in SAMPLES}

# ---------------------------------------------------------------------------
# Media preparations -> prepared_media ProcessedSamples
# ---------------------------------------------------------------------------

MEDIA = [
    {
        "key": "LB",
        "act_id": "urn:amp2:activity:media-prep-LB-001",
        "ps_id": "urn:amp2:processed-sample:media-LB-lennox-001",
        "name": "LB Lennox broth batch 001",
        "media_type": "rich_media",
        "volume_ml": 2000.0,
        "media_recipe": "LB Lennox broth (10 g/L tryptone, 5 g/L yeast "
                        "extract, 5 g/L NaCl)",
        "media_formulation": "commercial",
        "commercial_media_catalog": "Teknova L8000, lot 26D0417",
        "sterilization_method": "autoclave",
        "ph_adjustment": False,
        "ph_target": None,
        "exposure_sensitivity": None,
        "media_additions": [],
        "storage_temperature": "4 C",
        "creation_date": "2026-04-27",
    },
    {
        "key": "M9G",
        "act_id": "urn:amp2:activity:media-prep-M9-glucose-001",
        "ps_id": "urn:amp2:processed-sample:media-M9-glucose-001",
        "name": "M9 + 0.4% glucose batch 001",
        "media_type": "minimal_media",
        "volume_ml": 1500.0,
        "media_recipe": "M9 minimal salts with 0.4% (w/v) glucose, 2 mM MgSO4, "
                        "0.1 mM CaCl2",
        "media_formulation": "manual_mix",
        "commercial_media_catalog": None,
        "sterilization_method": "filter_0.22um",
        "ph_adjustment": True,
        "ph_target": 7.0,
        "exposure_sensitivity": None,
        "media_additions": ["0.4% glucose (w/v)", "2 mM MgSO4", "0.1 mM CaCl2"],
        "storage_temperature": "4 C",
        "creation_date": "2026-04-27",
    },
    {
        "key": "M9B",
        "act_id": "urn:amp2:activity:media-prep-M9-benzoate-001",
        "ps_id": "urn:amp2:processed-sample:media-M9-benzoate-001",
        "name": "M9 + 20 mM sodium benzoate batch 001",
        "media_type": "minimal_media",
        "volume_ml": 1000.0,
        "media_recipe": "M9 minimal salts with 20 mM sodium benzoate as sole "
                        "carbon source",
        "media_formulation": "manual_mix",
        "commercial_media_catalog": None,
        "sterilization_method": "filter_0.22um",
        "ph_adjustment": True,
        "ph_target": 7.2,
        "exposure_sensitivity": ["light-sensitive"],
        "media_additions": ["20 mM sodium benzoate", "2 mM MgSO4"],
        "storage_temperature": "4 C",
        "creation_date": "2026-04-28",
    },
    {
        "key": "YPD",
        "act_id": "urn:amp2:activity:media-prep-YPD-001",
        "ps_id": "urn:amp2:processed-sample:media-YPD-001",
        "name": "YPD broth batch 001",
        "media_type": "rich_media",
        "volume_ml": 800.0,
        "media_recipe": "YPD broth (10 g/L yeast extract, 20 g/L peptone, "
                        "20 g/L dextrose)",
        "media_formulation": "commercial",
        "commercial_media_catalog": "BD Difco 242820, lot 1264398",
        "sterilization_method": "autoclave",
        "ph_adjustment": False,
        "ph_target": None,
        "exposure_sensitivity": None,
        "media_additions": [],
        "storage_temperature": "room temperature",
        "creation_date": "2026-04-28",
    },
    {
        "key": "LBVAN",
        "act_id": "urn:amp2:activity:media-prep-LB-vanillate-001",
        "ps_id": "urn:amp2:processed-sample:media-LB-vanillate-001",
        "name": "LB + apramycin + vanillate induction medium batch 001",
        "media_type": "pre_culture",
        "volume_ml": 1200.0,
        "media_recipe": "LB Lennox broth with 50 ug/mL apramycin; vanillate "
                        "added per-well at plate setup",
        "media_formulation": "manual_mix",
        "commercial_media_catalog": None,
        "sterilization_method": "filter_0.22um",
        "ph_adjustment": False,
        "ph_target": None,
        "exposure_sensitivity": ["light-sensitive", "temperature-sensitive"],
        "media_additions": ["50 ug/mL apramycin", "vanillate added per well"],
        "storage_temperature": "4 C",
        "creation_date": "2026-04-29",
    },
    {
        "key": "LBAGAR",
        "act_id": "urn:amp2:activity:media-prep-LB-agar-001",
        "ps_id": "urn:amp2:processed-sample:media-LB-agar-001",
        "name": "LB agar purity plates batch 001",
        "media_type": "strain_purity",
        "volume_ml": 600.0,
        "media_recipe": "LB Lennox with 15 g/L agar, poured to 25 mL per plate",
        "media_formulation": "premixed",
        "commercial_media_catalog": None,
        "sterilization_method": "autoclave",
        "ph_adjustment": False,
        "ph_target": None,
        "exposure_sensitivity": None,
        "media_additions": ["15 g/L agar"],
        "storage_temperature": "4 C",
        "creation_date": "2026-04-20",
    },
    {
        "key": "GLYC",
        "act_id": "urn:amp2:activity:media-prep-glycerol-stock-001",
        "ps_id": "urn:amp2:processed-sample:media-glycerol-stock-001",
        "name": "LB + 25% glycerol cryostock medium batch 001",
        "media_type": "stock_culture",
        "volume_ml": 400.0,
        "media_recipe": "LB Lennox with 25% (v/v) glycerol for cryostorage",
        "media_formulation": "manual_mix",
        "commercial_media_catalog": None,
        "sterilization_method": "autoclave",
        "ph_adjustment": False,
        "ph_target": None,
        "exposure_sensitivity": None,
        "media_additions": ["25% glycerol (v/v)"],
        "storage_temperature": "-20 C",
        "creation_date": "2026-04-21",
    },
]
MEDIA_BY_KEY = {m["key"]: m for m in MEDIA}

# Which experimental-culture medium each organism is grown in upstream.
ORG_PRE_MEDIA = {
    "urn:amp2:organism:AG5577-pJE2165": "LBVAN",
    "urn:amp2:organism:PP-0055": "LBVAN",
    "urn:amp2:organism:PP-1021": "LBVAN",
    "urn:amp2:organism:PP-3186": "LBVAN",
    "urn:amp2:organism:PP-5325": "LBVAN",
    "urn:amp2:organism:KT2440-WT": "LB",
    "urn:amp2:organism:RHA1-pTE314": "M9B",
    "urn:amp2:organism:IFO0880-LIP1": "YPD",
}

# ---------------------------------------------------------------------------
# Culture growth chain
# ---------------------------------------------------------------------------

processed_samples = []      # dicts for the processed_samples: block
culture_activities = []
links = []                  # ProcessingSampleLink records
_link_n = [0]


def add_link(sample_id, processing_id, step_number, role):
    _link_n[0] += 1
    links.append({
        "id": "urn:amp2:link:psl-%05d" % _link_n[0],
        "sample_base_id": sample_id,
        "processing_id": processing_id,
        "step_number": step_number,
        "role": role,
    })


def add_processed_sample(ps_id, name, ps_type, sampled_during, description,
                         volume_uL=None, replicate=None, storage_location=None,
                         label_text=None):
    processed_samples.append({
        "id": ps_id,
        "name": name,
        "processed_sample_type": ps_type,
        "sampled_during": sampled_during,
        "description": description,
        "volume_uL": volume_uL,
        "replicate": replicate,
        "storage_location": storage_location,
        "label_text": label_text,
    })


# Media preparation activities each emit one prepared_media processed sample.
for m in MEDIA:
    add_processed_sample(
        m["ps_id"], m["name"], "prepared_media", m["act_id"],
        "Physical media batch produced by %s." % m["act_id"],
        volume_uL=m["volume_ml"] * 1000.0,
        storage_location="Cold room 2 / shelf B",
        label_text=m["name"],
    )
    add_link(m["ps_id"], m["act_id"], 1, "output_sample")

# Per-sample four-step chain.
# The one deliberate QC wrinkle: AMP2-0013 fails its first purity check,
# is re-streaked, and passes. It still completes the workflow.
CONTAMINATED_SAMPLE = "urn:amp2:sample:AMP2-0013"

TEMP_BY_ORG_TYPE = {"bacterial": 30.0, "fungal": 25.0}

for s in SAMPLES:
    org = ORG_BY_ID[s["organism_ref"]]
    n = s["sample_number"]
    sname = s["name"]
    temp = TEMP_BY_ORG_TYPE[org["strain_type"]]
    pre_media = ORG_PRE_MEDIA[s["organism_ref"]]
    fungal = org["strain_type"] == "fungal"

    # --- 1. StrainPurity (QC gate; emits no processed sample) -------------
    purity_id = "urn:amp2:activity:strain-purity-%04d" % n
    contaminated = s["id"] == CONTAMINATED_SAMPLE
    culture_activities.append({
        "id": purity_id,
        "activity_type": "StrainPurity",
        "name": "%s strain purity check" % sname,
        "description": ("First streak showed mixed colony morphology; sample "
                        "was re-streaked from the original vial and passed on "
                        "the second attempt."
                        if contaminated else
                        "Single-colony morphology confirmed; no contaminants "
                        "observed."),
        "organism_ref": s["organism_ref"],
        "media_ref": MEDIA_BY_KEY["LBAGAR"]["ps_id"],
        "growth_medium": "LB agar purity plate",
        "incubation_time_hours": 48.0 if fungal else 24.0,
        "temperature_celsius": temp,
        "agitation_speed_rpm": None,
        "oxygen_relationship": "aerobic",
        "container_type": "petri_dish",
        "inspection_method": "visual colony morphology + 16S colony PCR"
                             if not fungal else
                             "visual colony morphology + ITS colony PCR",
        "target_strain": org["strain_identifier"],
        "contaminant_strains": "Bacillus sp. (first streak only; cleared on "
                               "re-streak)" if contaminated else None,
        "preparation_date": None,
        "treatment_type": None,
        "growth_time": None,
        "processing_steps": "streak; incubate; inspect; colony PCR",
        "sample_name": sname,
    })
    add_link(s["id"], purity_id, 1, "input_sample")

    # --- 2. StockCulturePreparation --------------------------------------
    stock_id = "urn:amp2:activity:stock-culture-%04d" % n
    stock_ps = "urn:amp2:processed-sample:%s-stock" % sname
    culture_activities.append({
        "id": stock_id,
        "activity_type": "StockCulturePreparation",
        "name": "%s glycerol stock preparation" % sname,
        "description": "Overnight culture mixed 1:1 with cryostock medium and "
                       "banked at -80 C.",
        "organism_ref": s["organism_ref"],
        "media_ref": MEDIA_BY_KEY["GLYC"]["ps_id"],
        "growth_medium": "LB + 25% glycerol",
        "incubation_time_hours": 24.0 if fungal else 16.0,
        "temperature_celsius": temp,
        "agitation_speed_rpm": 200,
        "oxygen_relationship": "aerobic",
        "container_type": "culture_tube",
        "inspection_method": None,
        "target_strain": None,
        "contaminant_strains": None,
        "preparation_date": "2026-04-30",
        "treatment_type": None,
        "growth_time": None,
        "processing_steps": "inoculate; incubate; mix with glycerol; aliquot; "
                            "freeze",
        "sample_name": sname,
    })
    add_link(s["id"], stock_id, 1, "input_sample")
    add_link(stock_ps, stock_id, 2, "output_sample")
    add_processed_sample(
        stock_ps, "%s glycerol stock" % sname, "stock_culture", stock_id,
        "Cryobanked stock culture derived from user sample %s (%s)."
        % (sname, s["id"]),
        volume_uL=1000.0, replicate=1,
        storage_location="Freezer -80 C / rack A%02d" % ((n - 1) // 5 + 1),
        label_text="%s STOCK" % sname,
    )

    # --- 3. PreCultureGrowth ---------------------------------------------
    pre_id = "urn:amp2:activity:pre-culture-%04d" % n
    pre_ps = "urn:amp2:processed-sample:%s-preculture" % sname
    culture_activities.append({
        "id": pre_id,
        "activity_type": "PreCultureGrowth",
        "name": "%s pre-culture" % sname,
        "description": "Stock scraped into pre-culture medium to establish "
                       "viable inoculum.",
        "organism_ref": s["organism_ref"],
        "media_ref": MEDIA_BY_KEY[pre_media]["ps_id"],
        "growth_medium": MEDIA_BY_KEY[pre_media]["name"],
        "incubation_time_hours": 18.0 if fungal else 12.0,
        "temperature_celsius": temp,
        "agitation_speed_rpm": 200,
        "oxygen_relationship": "aerobic",
        "container_type": "baffled_flask",
        "inspection_method": None,
        "target_strain": None,
        "contaminant_strains": None,
        "preparation_date": None,
        "treatment_type": None,
        "growth_time": None,
        "processing_steps": "thaw; inoculate; incubate; check OD600",
        "sample_name": sname,
    })
    add_link(stock_ps, pre_id, 1, "input_sample")
    add_link(pre_ps, pre_id, 2, "output_sample")
    add_processed_sample(
        pre_ps, "%s pre-culture" % sname, "pre_culture", pre_id,
        "Pre-culture inoculum derived from user sample %s (%s)."
        % (sname, s["id"]),
        volume_uL=25000.0, replicate=1,
        storage_location="Incubator 3 / shaker deck",
        label_text="%s PRE" % sname,
    )

    # --- 4. ExperimentalCulture ------------------------------------------
    exp_id = "urn:amp2:activity:experimental-culture-%04d" % n
    exp_ps = "urn:amp2:processed-sample:%s-expculture" % sname
    treatment = ("vanillate induction (0.5 mM)"
                 if org["genotype_segment_category"] in
                 ("Gene Silencer", "Gene(s) of Interest")
                 and org["id"] != "urn:amp2:organism:IFO0880-LIP1"
                 else "none")
    culture_activities.append({
        "id": exp_id,
        "activity_type": "ExperimentalCulture",
        "name": "%s experimental culture" % sname,
        "description": "Terminal culture step; back-diluted to OD600 0.05 and "
                       "grown to mid-exponential before plating.",
        "organism_ref": s["organism_ref"],
        "media_ref": MEDIA_BY_KEY[pre_media]["ps_id"],
        "growth_medium": MEDIA_BY_KEY[pre_media]["name"],
        "incubation_time_hours": 6.0 if fungal else 4.0,
        "temperature_celsius": temp,
        "agitation_speed_rpm": 220,
        "oxygen_relationship": "aerobic",
        "container_type": "baffled_flask",
        "inspection_method": None,
        "target_strain": None,
        "contaminant_strains": None,
        "preparation_date": None,
        "treatment_type": treatment,
        "growth_time": "6 hours" if fungal else "4 hours",
        "processing_steps": "back-dilute; incubate; measure OD600; normalise "
                            "to OD600 0.10",
        "sample_name": sname,
    })
    add_link(pre_ps, exp_id, 1, "input_sample")
    add_link(exp_ps, exp_id, 2, "output_sample")
    add_processed_sample(
        exp_ps, "%s experimental culture" % sname, "experimental_culture",
        exp_id,
        "Normalised experimental culture loaded into plate wells. Traces back "
        "to user sample %s (%s)." % (sname, s["id"]),
        volume_uL=12000.0, replicate=1,
        storage_location="Incubator 3 / shaker deck",
        label_text="%s EXP" % sname,
    )
    s["stock_ps"] = stock_ps
    s["pre_ps"] = pre_ps
    s["exp_ps"] = exp_ps


# ---------------------------------------------------------------------------
# Plate layouts
# ---------------------------------------------------------------------------

def wells_96():
    return [(r, c) for r in "ABCDEFGH" for c in range(1, 13)]


def wells_384():
    return [(r, c) for r in "ABCDEFGHIJKLMNOP" for c in range(1, 25)]


def pos(r, c):
    return "%s%02d" % (r, c)


PLATES = []

# --- Plate 1: 96-well, per-well media split (LB rows A-D, M9G rows E-H) ----
p1_wells = []
p1_samples = SAMPLES[0:8]
for (r, c) in wells_96():
    row_i = "ABCDEFGH".index(r)
    top = row_i < 4
    media_key = "LB" if top else "M9G"
    # Plate-level default is LB, so only the M9G wells carry an override.
    media_ref = None if top else MEDIA_BY_KEY["M9G"]["ps_id"]
    rep = "rep_%d" % (row_i % 4 + 1)
    if c <= 8:
        smp = p1_samples[c - 1]
        p1_wells.append({
            "position": pos(r, c), "well_type": "sample",
            "replicate_group": rep, "media_ref": media_ref,
            "media_volume_ul": 180.0, "inoculum_volume_ul": 20.0,
            "sample_id": smp["id"], "sample_name": smp["name"],
            "treatments": None, "media_key": media_key,
        })
    elif c == 9:
        p1_wells.append({
            "position": pos(r, c), "well_type": "uninoculated_control",
            "replicate_group": rep, "media_ref": media_ref,
            "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
            "sample_id": None, "sample_name": None,
            "treatments": None, "media_key": media_key,
        })
    elif c == 10:
        p1_wells.append({
            "position": pos(r, c), "well_type": "blank",
            "replicate_group": rep, "media_ref": media_ref,
            "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
            "sample_id": None, "sample_name": None,
            "treatments": None, "media_key": media_key,
        })
    elif c == 11:
        ctrl = SAMPLE_BY_ID["urn:amp2:sample:AMP2-0010"]
        p1_wells.append({
            "position": pos(r, c), "well_type": "positive_control",
            "replicate_group": rep, "media_ref": media_ref,
            "media_volume_ul": 180.0, "inoculum_volume_ul": 20.0,
            "sample_id": ctrl["id"], "sample_name": ctrl["name"],
            "treatments": None, "media_key": media_key,
        })
    else:  # c == 12
        if top:
            p1_wells.append({
                "position": pos(r, c), "well_type": "standard",
                "replicate_group": rep, "media_ref": media_ref,
                "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
                "sample_id": None, "sample_name": None,
                "treatments": ["0.5 McFarland latex turbidity standard"],
                "media_key": media_key,
            })
        else:
            p1_wells.append({
                "position": pos(r, c), "well_type": "negative_control",
                "replicate_group": rep, "media_ref": media_ref,
                "media_volume_ul": 200.0, "inoculum_volume_ul": 0.0,
                "sample_id": None, "sample_name": None,
                "treatments": ["50 ug/mL apramycin sterility check"],
                "media_key": media_key,
            })

PLATES.append({
    "barcode": "AMP2-P001",
    "activity_id": "urn:amp2:activity:plate-setup-AMP2-P001",
    "plate_ps_id": "urn:amp2:processed-sample:plate-AMP2-P001",
    "plate_type": "Greiner_96well_flat_bottom_655161",
    "well_count": 96,
    "plate_format": "96-well (8 rows x 12 columns)",
    "setup_date": "2026-05-04T09:15:00",
    "operator": "urn:amp2:person:kapu336",
    "setup_instrument": "manual",
    "sealing_method": "BreathEasy_membrane",
    "default_media": "LB",
    "temperature_celsius": 30.0,
    "agitation_speed_rpm": 180,
    "oxygen_relationship": "aerobic",
    "instrument": "urn:amp2:instrument:plate-reader-001",
    "reader_model": "BioTek Epoch2",
    "read_operator": "urn:amp2:person:elga519",
    "t0": datetime(2026, 5, 4, 10, 0, 0),
    "wells": p1_wells,
    "description": "Carbon-source comparison plate. Rows A-D carry the "
                   "plate-level LB batch; rows E-H override to the M9 + 0.4% "
                   "glucose batch through AMP2WellMetadata.media_ref.",
})

# --- Plate 2: 96-well, uniform media, per-well vanillate treatments --------
p2_wells = []
p2_samples = SAMPLES[8:15]          # 7 samples
VAN_LEVELS = [("0 mM vanillate", 0.0), ("0.1 mM vanillate", 0.1),
              ("1.0 mM vanillate", 1.0)]
for (r, c) in wells_96():
    row_i = "ABCDEFGH".index(r)
    if row_i < 7:
        smp = p2_samples[row_i]
        level_i = (c - 1) // 4
        label, conc = VAN_LEVELS[level_i]
        p2_wells.append({
            "position": pos(r, c), "well_type": "sample",
            "replicate_group": "rep_%d" % ((c - 1) % 4 + 1),
            "media_ref": None,
            "media_volume_ul": 178.0, "inoculum_volume_ul": 20.0,
            "sample_id": smp["id"], "sample_name": smp["name"],
            "treatments": [label], "media_key": "LBVAN",
            "vanillate_mM": conc,
        })
    else:
        if c <= 3:
            wt, sid, sn, inoc, tr = "blank", None, None, 0.0, None
        elif c <= 6:
            wt, sid, sn, inoc, tr = ("uninoculated_control", None, None, 0.0,
                                     ["1.0 mM vanillate"])
        elif c <= 9:
            ctrl = SAMPLE_BY_ID["urn:amp2:sample:AMP2-0010"]
            wt, sid, sn, inoc, tr = ("positive_control", ctrl["id"],
                                     ctrl["name"], 20.0, ["0 mM vanillate"])
        else:
            wt, sid, sn, inoc, tr = ("standard", None, None, 0.0,
                                     ["0.5 McFarland latex turbidity standard"])
        p2_wells.append({
            "position": pos(r, c), "well_type": wt,
            "replicate_group": "rep_%d" % ((c - 1) % 3 + 1),
            "media_ref": None,
            "media_volume_ul": 198.0 if inoc == 0.0 else 178.0,
            "inoculum_volume_ul": inoc,
            "sample_id": sid, "sample_name": sn,
            "treatments": tr, "media_key": "LBVAN",
            "vanillate_mM": 0.0,
        })

PLATES.append({
    "barcode": "AMP2-P002",
    "activity_id": "urn:amp2:activity:plate-setup-AMP2-P002",
    "plate_ps_id": "urn:amp2:processed-sample:plate-AMP2-P002",
    "plate_type": "Corning_96well_flat_bottom_3596",
    "well_count": 96,
    "plate_format": "96-well (8 rows x 12 columns)",
    "setup_date": "2026-05-04T09:50:00",
    "operator": "urn:amp2:person:navi204",
    "setup_instrument": "Hamilton_Microlab_STAR",
    "sealing_method": "BreathEasy_membrane",
    "default_media": "LBVAN",
    "temperature_celsius": 30.0,
    "agitation_speed_rpm": 180,
    "oxygen_relationship": "aerobic",
    "instrument": "urn:amp2:instrument:plate-reader-001",
    "reader_model": "BioTek Epoch2",
    "read_operator": "urn:amp2:person:elga519",
    "t0": datetime(2026, 5, 4, 10, 30, 0),
    "wells": p2_wells,
    "description": "CRISPRi induction dose-response plate. One plate-level "
                   "medium for every well (no per-well media_ref overrides); "
                   "the experimental variable is the per-well vanillate "
                   "concentration carried in AMP2WellMetadata.treatments.",
})

# --- Plate 3: 384-well, four media quadrants, all 15 samples --------------
p3_wells = []
QUAD_MEDIA = {(0, 0): "LB", (0, 1): "M9G", (1, 0): "M9B", (1, 1): "YPD"}
quad_buckets = {k: [] for k in QUAD_MEDIA}
for (r, c) in wells_384():
    row_i = "ABCDEFGHIJKLMNOP".index(r)
    quad = (0 if row_i < 8 else 1, 0 if c <= 12 else 1)
    quad_buckets[quad].append((r, c))

for quad, cells in quad_buckets.items():
    media_key = QUAD_MEDIA[quad]
    media_ref = (None if media_key == "LB"
                 else MEDIA_BY_KEY[media_key]["ps_id"])
    # 96 cells per quadrant: 90 sample wells (15 samples x 6 reps) + 6 controls
    for i, (r, c) in enumerate(cells):
        if i < 90:
            smp = SAMPLES[i % 15]
            rep = i // 15 + 1
            p3_wells.append({
                "position": pos(r, c), "well_type": "sample",
                "replicate_group": "rep_%d" % rep, "media_ref": media_ref,
                "media_volume_ul": 45.0, "inoculum_volume_ul": 5.0,
                "sample_id": smp["id"], "sample_name": smp["name"],
                "treatments": None, "media_key": media_key,
            })
        else:
            j = i - 90
            if j < 2:
                wt, tr, inoc, sid, sn = "blank", None, 0.0, None, None
            elif j < 4:
                wt, tr, inoc, sid, sn = ("uninoculated_control", None, 0.0,
                                         None, None)
            elif j == 4:
                wt, tr, inoc, sid, sn = (
                    "standard",
                    ["0.5 McFarland latex turbidity standard"], 0.0, None, None)
            else:
                wt, tr, inoc, sid, sn = (
                    "negative_control", ["sterile medium sterility check"],
                    0.0, None, None)
            p3_wells.append({
                "position": pos(r, c), "well_type": wt,
                "replicate_group": "rep_1", "media_ref": media_ref,
                "media_volume_ul": 50.0, "inoculum_volume_ul": inoc,
                "sample_id": sid, "sample_name": sn,
                "treatments": tr, "media_key": media_key,
            })

p3_wells.sort(key=lambda w: ("ABCDEFGHIJKLMNOP".index(w["position"][0]),
                             int(w["position"][1:])))

PLATES.append({
    "barcode": "AMP2-P003",
    "activity_id": "urn:amp2:activity:plate-setup-AMP2-P003",
    "plate_ps_id": "urn:amp2:processed-sample:plate-AMP2-P003",
    "plate_type": "Greiner_384well_flat_bottom_781091",
    "well_count": 384,
    "plate_format": "384-well (16 rows A-P x 24 columns)",
    "setup_date": "2026-05-04T11:05:00",
    "operator": "urn:amp2:person:navi204",
    "setup_instrument": "Hamilton_Microlab_STAR",
    "sealing_method": "optically_clear_adhesive_film",
    "default_media": "LB",
    "temperature_celsius": 28.0,
    "agitation_speed_rpm": 150,
    "oxygen_relationship": "aerobic",
    "instrument": "urn:amp2:instrument:plate-reader-002",
    "reader_model": "Tecan Spark 10M",
    "read_operator": "urn:amp2:person:kapu336",
    "t0": datetime(2026, 5, 4, 12, 0, 0),
    "wells": p3_wells,
    "description": "Full-panel 384-well plate: all 15 user samples x 6 "
                   "technical replicates in each of four media quadrants "
                   "(A-H/01-12 LB, A-H/13-24 M9+glucose, I-P/01-12 "
                   "M9+benzoate, I-P/13-24 YPD). Demonstrates that the data "
                   "model is not limited to 96-well geometry.",
})

# ---------------------------------------------------------------------------
# Growth simulation
# ---------------------------------------------------------------------------

TIMEPOINTS = list(range(0, 25, 2))          # 0,2,...,24 -> 13 reads

# Carrying capacity (K) and growth rate (r) per organism x medium.
# None => organism does not grow in that medium (stays near blank).
GROWTH = {
    "urn:amp2:organism:AG5577-pJE2165": {
        "LB": (1.05, 0.62), "M9G": (0.72, 0.38), "M9B": (0.31, 0.20),
        "YPD": (0.88, 0.50), "LBVAN": (0.98, 0.58)},
    "urn:amp2:organism:PP-0055": {
        "LB": (0.95, 0.55), "M9G": (0.61, 0.33), "M9B": (0.25, 0.17),
        "YPD": (0.80, 0.44), "LBVAN": (0.90, 0.52)},
    "urn:amp2:organism:PP-1021": {
        "LB": (0.99, 0.58), "M9G": (0.66, 0.35), "M9B": (0.28, 0.18),
        "YPD": (0.83, 0.46), "LBVAN": (0.94, 0.55)},
    "urn:amp2:organism:PP-3186": {
        "LB": (0.90, 0.51), "M9G": (0.55, 0.29), "M9B": (0.22, 0.15),
        "YPD": (0.76, 0.42), "LBVAN": (0.86, 0.49)},
    "urn:amp2:organism:PP-5325": {
        "LB": (1.02, 0.60), "M9G": (0.69, 0.37), "M9B": (0.30, 0.19),
        "YPD": (0.85, 0.48), "LBVAN": (0.96, 0.57)},
    "urn:amp2:organism:KT2440-WT": {
        "LB": (1.18, 0.70), "M9G": (0.84, 0.45), "M9B": (0.38, 0.24),
        "YPD": (0.97, 0.55), "LBVAN": (1.12, 0.66)},
    "urn:amp2:organism:RHA1-pTE314": {
        "LB": (0.74, 0.36), "M9G": (0.40, 0.22), "M9B": (0.86, 0.41),
        "YPD": (0.66, 0.33), "LBVAN": (0.70, 0.34)},
    "urn:amp2:organism:IFO0880-LIP1": {
        "LB": (0.52, 0.24), "M9G": (0.63, 0.26), "M9B": (0.09, 0.08),
        "YPD": (1.34, 0.44), "LBVAN": (0.48, 0.22)},
}

# CRISPRi knockdown severity: fractional reduction in K at full induction.
KNOCKDOWN = {
    "urn:amp2:organism:PP-0055": 0.46,
    "urn:amp2:organism:PP-1021": 0.12,
    "urn:amp2:organism:PP-3186": 0.63,
    "urn:amp2:organism:PP-5325": 0.05,
    "urn:amp2:organism:AG5577-pJE2165": 0.02,
}

BLANK_OD = 0.038
LAG_H = {"bacterial": 1.5, "fungal": 3.5}


def well_seed(barcode, position):
    # zlib.crc32, not hash(): str hashing is salted per process and would
    # make the simulated values differ between runs.
    return zlib.crc32(("%s|%s" % (barcode, position)).encode("utf-8"))


def od_value(plate, well, t_hours):
    """Simulated OD600 for one well at one timepoint."""
    rng = random.Random(well_seed(plate["barcode"], well["position"]) + 7 * t_hours)
    wt = well["well_type"]
    baseline = BLANK_OD + rng.gauss(0.0, 0.0018)

    if wt in ("blank", "uninoculated_control", "negative_control"):
        # Sterile wells drift only from evaporation / condensation.
        return max(0.001, baseline + 0.0006 * t_hours)
    if wt == "standard":
        return max(0.001, 0.512 + rng.gauss(0.0, 0.004))

    smp = SAMPLE_BY_ID[well["sample_id"]]
    org = ORG_BY_ID[smp["organism_ref"]]
    media_key = well["media_key"]
    K, r = GROWTH[org["id"]][media_key]

    van = well.get("vanillate_mM", 0.0) or 0.0
    if van > 0 and org["id"] in KNOCKDOWN:
        # Saturating dose response on the knockdown effect.
        frac = KNOCKDOWN[org["id"]] * (van / (van + 0.15))
        K *= (1.0 - frac)
        r *= (1.0 - 0.5 * frac)

    # Well-to-well biological scatter, fixed per well across the series.
    wrng = random.Random(well_seed(plate["barcode"], well["position"]))
    K *= wrng.uniform(0.93, 1.07)
    r *= wrng.uniform(0.92, 1.08)

    lag = LAG_H[org["strain_type"]] * wrng.uniform(0.85, 1.15)
    od0 = 0.045 * wrng.uniform(0.9, 1.1)
    if t_hours <= lag:
        growth = od0
    else:
        te = t_hours - lag
        growth = (K * od0) / (od0 + (K - od0) * pow(2.718281828, -r * te))

    # Edge wells evaporate a little faster late in the run.
    row, col = well["position"][0], int(well["position"][1:])
    edge = (row in ("A", "H", "P") or col in (1, 12, 24))
    if edge and t_hours >= 18:
        growth *= 1.0 + 0.012 * (t_hours - 16)

    return max(0.001, baseline + growth + rng.gauss(0.0, 0.006))


# --- Injected read failures -----------------------------------------------
#  1. AMP2-P002 t=10h: whole read aborted -> activity recorded, no product.
#  2. AMP2-P003 t=14h: condensation over the YPD quadrant (rows I-P,
#     columns 13-24) -> 96 wells flagged "failed" with saturated values.
#  3. AMP2-P001 D07: contaminated from t=12h onward.
#  4. Scattered single-well optical artefacts flagged "outlier".
ABORTED_READS = {("AMP2-P002", 10)}
CONTAMINATED_WELLS = {("AMP2-P001", "D07"): 12}
SCATTERED_OUTLIERS = {
    ("AMP2-P001", "B03", 6), ("AMP2-P001", "G11", 16),
    ("AMP2-P002", "C09", 8), ("AMP2-P002", "F02", 22),
    ("AMP2-P003", "E17", 4), ("AMP2-P003", "K05", 12),
    ("AMP2-P003", "N21", 20), ("AMP2-P003", "B14", 24),
}


def p3_failed_quadrant(position):
    row, col = position[0], int(position[1:])
    return "ABCDEFGHIJKLMNOP".index(row) >= 8 and col >= 13


def reading_for(plate, well, t):
    """Return (value, flag) for one well at one timepoint."""
    bc, p = plate["barcode"], well["position"]
    rng = random.Random(well_seed(bc, p) + 991 * t)

    if bc == "AMP2-P003" and t == 14 and p3_failed_quadrant(p):
        return round(3.700 + rng.uniform(-0.08, 0.08), 4), "failed"

    onset = CONTAMINATED_WELLS.get((bc, p))
    if onset is not None and t >= onset:
        base = od_value(plate, well, t)
        return round(base * rng.uniform(1.9, 2.4) + 0.15, 4), "contaminated"

    if (bc, p, t) in SCATTERED_OUTLIERS:
        base = od_value(plate, well, t)
        return round(base * rng.uniform(2.2, 3.1) + 0.05, 4), "outlier"

    v = round(od_value(plate, well, t), 4)
    flag = "blank" if well["well_type"] == "blank" else "ok"
    return v, flag


# --- Build data generation activities + OD products -----------------------

dga = []
products = []
readings = []      # (product_id, plate, timepoint, position, value, flag)

for plate in PLATES:
    seq = 0
    for t in TIMEPOINTS:
        seq += 1
        tlabel = "t=%dh" % t
        start = plate["t0"] + timedelta(hours=t)
        # A 384-well plate takes longer to scan than a 96-well plate.
        dur_min = 4 if plate["well_count"] == 96 else 11
        aborted = (plate["barcode"], t) in ABORTED_READS
        act_id = "urn:amp2:activity:od-read-%s-t%02dh" % (plate["barcode"], t)
        prod_id = "urn:amp2:data:od-product-%s-t%02dh" % (plate["barcode"], t)

        dga.append({
            "id": act_id,
            "activity_type": "AMP2DataGenerationActivity",
            "name": "%s OD600 read %s" % (plate["barcode"], tlabel),
            "description": (
                "Read aborted: the reader reported a plate-carrier jam and no "
                "absorbance data were written. The plate was returned to the "
                "incubator and the series resumed at t=12h. No AMP2ODProduct "
                "exists for this activity."
                if aborted else
                "Endpoint OD600 absorbance read of all %d wells."
                % plate["well_count"]),
            "plate_barcode": plate["barcode"],
            "plate_setup_id": plate["activity_id"],
            "analyte_id": plate["plate_ps_id"],
            "timepoint_label": tlabel,
            "measurement_type": "optical_density",
            "wavelength_nm": 600,
            "sequence_order": seq,
            "acquisition_start_time": start.isoformat(),
            "acquisition_end_time": (start + timedelta(minutes=dur_min)).isoformat(),
            "instrument_used": plate["instrument"],
            "instrument_operator_id": plate["read_operator"],
            "protocol_url": "https://protocols.io/view/amp2-od600-kinetic-read-v2",
            "protocol_version": "2.1",
            "read_status": "aborted" if aborted else "complete",
            "product_id": None if aborted else prod_id,
        })

        if aborted:
            continue

        wr = []
        for w in plate["wells"]:
            v, flag = reading_for(plate, w, t)
            wr.append({"position": w["position"], "value": v, "flag": flag})
            readings.append((prod_id, plate["barcode"], tlabel, w["position"],
                             v, flag))

        by_pos = {x["position"]: x for x in wr}
        sample_vals = [by_pos[w["position"]]["value"] for w in plate["wells"]
                       if w["well_type"] in ("sample", "positive_control")
                       and by_pos[w["position"]]["flag"] == "ok"]
        blank_vals = [by_pos[w["position"]]["value"] for w in plate["wells"]
                      if w["well_type"] == "blank"]
        mean = sum(sample_vals) / len(sample_vals)
        var = sum((x - mean) ** 2 for x in sample_vals) / (len(sample_vals) - 1)
        sd = var ** 0.5
        n_flagged = sum(1 for x in wr if x["flag"] not in ("ok", "blank"))

        products.append({
            "id": prod_id,
            "product_type": "AMP2ODProduct",
            "name": "%s OD600 product %s" % (plate["barcode"], tlabel),
            "description": "Per-well OD600 summary for %s at %s."
                           % (plate["barcode"], tlabel),
            "was_generated_by": act_id,
            "plate_barcode": plate["barcode"],
            "analyte_id": plate["plate_ps_id"],
            "timepoint_label": tlabel,
            "wavelength_nm": 600,
            "plate_average": round(mean, 4),
            "blank_mean": round(sum(blank_vals) / len(blank_vals), 4),
            "cv_percent": round(100.0 * sd / mean, 2),
            "plate_reader_model": plate["reader_model"],
            "flagged_well_count": n_flagged,
            "well_readings": wr,
        })

# ---------------------------------------------------------------------------
# Plate setup activities + plate processed samples + links
# ---------------------------------------------------------------------------

plate_setups = []
for plate in PLATES:
    inoc_samples = sorted({w["sample_id"] for w in plate["wells"]
                           if w["sample_id"]})
    for step, sid in enumerate(inoc_samples, start=1):
        add_link(SAMPLE_BY_ID[sid]["exp_ps"], plate["activity_id"], step,
                 "input_sample")
    add_link(plate["plate_ps_id"], plate["activity_id"],
             len(inoc_samples) + 1, "output_sample")

    add_processed_sample(
        plate["plate_ps_id"],
        "%s inoculated %s" % (plate["barcode"], plate["plate_format"]),
        "amp2_%dwell_plate" % plate["well_count"],
        plate["activity_id"],
        "Inoculated plate produced by %s; the analyte every OD read points at."
        % plate["activity_id"],
        volume_uL=sum(w["media_volume_ul"] + w["inoculum_volume_ul"]
                      for w in plate["wells"]),
        storage_location="Incubator 5 / stack 2",
        label_text=plate["barcode"],
    )
    plate_setups.append(plate)

# ---------------------------------------------------------------------------
# Emit YAML
# ---------------------------------------------------------------------------


def q(v):
    """Scalar -> YAML."""
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def blk(lines, key, value, indent):
    pad = " " * indent
    if value is None:
        lines.append("%s%s: null" % (pad, key))
    elif isinstance(value, list):
        if not value:
            lines.append("%s%s: []" % (pad, key))
        else:
            lines.append("%s%s:" % (pad, key))
            for item in value:
                lines.append("%s  - %s" % (pad, q(item)))
    else:
        lines.append("%s%s: %s" % (pad, key, q(value)))


L = []
A = L.append

A("# " + "=" * 76)
A("# amp2-full-workflow-002.yaml")
A("#")
A("# Simulated AMP2 dataset for ingestion testing against the BASALT schema.")
A("# Generated from src/basalt_schema/schema/ (media_strain_culture_plate.yaml,")
A("# organism.yaml, sample_classes.yaml, slots.yaml, enums.yaml).")
A("#")
A("# Scope")
A("#   15 AMP2UserSample records mapped many-to-one onto 8 organism records,")
A("#   each carried through the full AMP2 lab workflow")
A("#     StrainPurity -> StockCulturePreparation -> PreCultureGrowth ->")
A("#     ExperimentalCulture -> AMP2PlateSetupActivity")
A("#   then read for OD600 every 2 hours for 24 hours (13 timepoints) on")
A("#   three plates: two 96-well and one 384-well.")
A("#")
A("# WHERE THE SAMPLE ID LIVES  (read this first)")
A("#   The submitter's sample is an `amp2_user_samples` record.")
A("#     .id   is the primary key, e.g. \"urn:amp2:sample:AMP2-0003\".")
A("#           Every FK in this file points at THIS value.")
A("#     .name is the human-readable name the submitter wrote on the tube,")
A("#           e.g. \"PP_0055-R1\". It is a label, never a foreign key.")
A("#   The strain/biological identity is a SEPARATE record in `organisms`,")
A("#   reached via amp2_user_samples[].organism_ref. Several samples may")
A("#   share one organism (PP_0055 has three), so an organism id can never")
A("#   stand in for a sample id.")
A("#   Downstream, AMP2WellMetadata.sample_id in `plate_setup_activities`")
A("#   holds the amp2_user_samples[].id of whatever went into that well,")
A("#   even though what was physically pipetted is the experimental_culture")
A("#   processed sample derived from it. Follow processing_sample_links to")
A("#   walk the physical chain; follow well.sample_id to answer \"whose")
A("#   sample is in this well\".")
A("#   00_sample_identity_crosswalk.csv in the sibling directory lays the")
A("#   whole chain out one row per sample.")
A("#")
A("# Structural notes")
A("#   * processing_sample_links is the SINGLE source of truth for which")
A("#     samples an activity consumed and produced (ProcessingSampleLink:")
A("#     sample_base_id, processing_id, step_number, role). Activities")
A("#     deliberately do NOT repeat input/output ids inline.")
A("#   * organism replaces the retired Strain class; ORGANISM records carry")
A("#     strain_identifier, genotype_segment_*, component_*, trait,")
A("#     phenotype, trophic_level, pathogenicity, propagation.")
A("#   * StrainPurity is a pass/fail QC gate and emits no processed sample,")
A("#     per media_strain_culture_plate.yaml.")
A("#   * oxygen_relationship is the canonical slot name (oxygen_status is an")
A("#     alias).")
A("#")
A("# Deliberate data conditions (all schema-valid; none are schema violations)")
A("#   * AMP2-0013 fails its first purity streak (contaminant_strains set),")
A("#     is re-streaked, and completes the workflow.")
A("#   * AMP2-P002 t=10h: the read was aborted mid-plate. The")
A("#     AMP2DataGenerationActivity exists with read_status \"aborted\" and")
A("#     NO AMP2ODProduct, so that plate has 12 products, not 13.")
A("#   * AMP2-P003 t=14h: condensation over the YPD quadrant (rows I-P,")
A("#     columns 13-24) -- 96 wells flagged \"failed\" at saturated values.")
A("#   * AMP2-P001 well D07 is flagged \"contaminated\" from t=12h onward.")
A("#   * Eight scattered wells are flagged \"outlier\" at single timepoints.")
A("#   * Wild-type KT2440 (urn:amp2:organism:KT2440-WT) leaves trait,")
A("#     phenotype, strain_mutation and modification_method null on purpose.")
A("# " + "=" * 76)
A("")
A("dataset:")
A('  id: "urn:amp2:dataset:amp2-full-workflow-002"')
A('  name: "AMP2 full-workflow growth screen 002"')
A('  description: "15 user samples, 8 organisms, 7 media batches, 3 plates '
  '(2 x 96-well, 1 x 384-well), OD600 every 2 h for 24 h."')
A('  emsl_activity: "AMP2 FY26 microbial growth screen"')
A('  schema_source: "src/basalt_schema/schema/media_strain_culture_plate.yaml"')
A("  counts:")
A("    organisms: %d" % len(ORGANISMS))
A("    amp2_user_samples: %d" % len(SAMPLES))
A("    media_preparations: %d" % len(MEDIA))
A("    culture_growth_activities: %d" % len(culture_activities))
A("    plate_setup_activities: %d" % len(PLATES))
A("    wells_total: %d" % sum(len(p["wells"]) for p in PLATES))
A("    data_generation_activities: %d" % len(dga))
A("    od_products: %d" % len(products))
A("    well_readings: %d" % len(readings))
A("    processing_sample_links: %d" % len(links))
A("")

# --- people / instruments -------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# PersonValue records referenced by setup_operator_id / instrument_operator_id")
A("# ---------------------------------------------------------------------------")
A("people:")
for p in PEOPLE:
    A("  - id: %s" % q(p["id"]))
    A("    first_name: %s" % q(p["first_name"]))
    A("    last_name: %s" % q(p["last_name"]))
    A("    email: %s" % q(p["email"]))
    A("    orcid: %s" % q(p["orcid"]))
A("")
A("# ---------------------------------------------------------------------------")
A("# Instrument records referenced by instrument_used")
A("# ---------------------------------------------------------------------------")
A("instruments:")
for it in INSTRUMENTS:
    A("  - id: %s" % q(it["id"]))
    A("    name: %s" % q(it["name"]))
    A("    serial_number: %s" % q(it["serial_number"]))
A("")

# --- organisms ------------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# organisms  (class: organism -- replaces the retired Strain class)")
A("#   Biological identity only. One organism : many amp2_user_samples.")
A("# ---------------------------------------------------------------------------")
A("organisms:")
ORG_FIELDS = ["id", "name", "description", "strain_identifier", "organism_name",
              "taxonomy_id", "host_common_name", "host_taxid", "strain_source",
              "strain_type", "modification_method", "strain_description",
              "strain_mutation", "phenotype", "trait", "encoded_traits",
              "genotype_segment_category", "genotype_segment_name",
              "component_name", "construct_component", "donor_organism",
              "component_description", "trophic_level", "pathogenicity",
              "host_spec_range", "propagation"]
for o in ORGANISMS:
    first = True
    for f in ORG_FIELDS:
        prefix = "  - " if first else "    "
        A("%s%s: %s" % (prefix, f, q(o[f])))
        first = False
    A("")

# --- samples --------------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# amp2_user_samples  (class: AMP2UserSample, is_a Sample)")
A("#   THE SAMPLE. `id` is the FK target used everywhere else in this file;")
A("#   `name` is the submitter's label. organism_ref reaches strain identity.")
A("# ---------------------------------------------------------------------------")
A("amp2_user_samples:")
SAMPLE_FIELDS = ["id", "name", "description", "organism_ref", "collection_date",
                 "growth_facil", "isol_growth_condt", "start_date_inc",
                 "storage_condition", "storage_temperature",
                 "shipped_sample_size", "guid_source", "other_guid_source",
                 "analysis_type", "cbi", "lims_barcode", "emsl_activity",
                 "replicate_number"]
for s in SAMPLES:
    first = True
    for f in SAMPLE_FIELDS:
        prefix = "  - " if first else "    "
        A("%s%s: %s" % (prefix, f, q(s[f])))
        first = False
    A("")

# --- media ----------------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# media_preparations  (class: MediaPreparation, is_a SampleProcessing)")
A("#   Each emits one processed_sample of type prepared_media; downstream")
A("#   media_ref slots point at that processed sample, never at this activity.")
A("# ---------------------------------------------------------------------------")
A("media_preparations:")
for m in MEDIA:
    A("  - id: %s" % q(m["act_id"]))
    A("    name: %s" % q(m["name"]))
    A("    media_type: %s" % q(m["media_type"]))
    A("    volume_ml: %s" % q(m["volume_ml"]))
    A("    media_recipe: %s" % q(m["media_recipe"]))
    A("    media_formulation: %s" % q(m["media_formulation"]))
    A("    commercial_media_catalog: %s" % q(m["commercial_media_catalog"]))
    A("    sterilization_method: %s" % q(m["sterilization_method"]))
    A("    ph_adjustment: %s" % q(m["ph_adjustment"]))
    A("    ph_target: %s" % q(m["ph_target"]))
    blk(L, "exposure_sensitivity", m["exposure_sensitivity"], 4)
    blk(L, "media_additions", m["media_additions"], 4)
    A("    storage_temperature: %s" % q(m["storage_temperature"]))
    A("    creation_date: %s" % q(m["creation_date"]))
    A("    processing_steps: %s" % q("weigh; dissolve; sterilise; QC; store"))
    A("    # output prepared_media processed sample: %s" % m["ps_id"])
    A("")

# --- culture activities ---------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# culture_growth_activities  (CultureGrowth subclasses, is_a SampleProcessing)")
A("#   Four per user sample. Inputs/outputs live in processing_sample_links.")
A("#   StrainPurity is a QC gate and produces no processed sample.")
A("# ---------------------------------------------------------------------------")
A("culture_growth_activities:")
CULT_FIELDS = ["id", "activity_type", "name", "description", "organism_ref",
               "media_ref", "growth_medium", "incubation_time_hours",
               "temperature_celsius", "agitation_speed_rpm",
               "oxygen_relationship", "container_type", "processing_steps",
               "inspection_method", "target_strain", "contaminant_strains",
               "preparation_date", "treatment_type", "growth_time"]
for a in culture_activities:
    A("  # user sample: %s" % a["sample_name"])
    first = True
    for f in CULT_FIELDS:
        prefix = "  - " if first else "    "
        A("%s%s: %s" % (prefix, f, q(a[f])))
        first = False
    A("")

# --- processed samples ----------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# processed_samples  (class: ProcessedSample, is_a Sample)")
A("#   sampled_during points at the SampleProcessing activity that made it.")
A("# ---------------------------------------------------------------------------")
A("processed_samples:")
for ps in processed_samples:
    A("  - id: %s" % q(ps["id"]))
    A("    name: %s" % q(ps["name"]))
    A("    processed_sample_type: %s" % q(ps["processed_sample_type"]))
    A("    sampled_during: %s" % q(ps["sampled_during"]))
    A("    description: %s" % q(ps["description"]))
    A("    volume_uL: %s" % q(ps["volume_uL"]))
    A("    replicate: %s" % q(ps["replicate"]))
    A("    storage_location: %s" % q(ps["storage_location"]))
    A("    label_text: %s" % q(ps["label_text"]))
A("")

# --- plate setups ---------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# plate_setup_activities  (class: AMP2PlateSetupActivity)")
A("#   media_ref is the plate-level default. A well whose media_ref is null")
A("#   inherits it; a non-null well media_ref overrides it for that well only.")
A("#   well_metadata entries are AMP2WellMetadata (embedded, not a table).")
A("# ---------------------------------------------------------------------------")
A("plate_setup_activities:")
for plate in plate_setups:
    A("  - id: %s" % q(plate["activity_id"]))
    A("    activity_type: \"AMP2PlateSetupActivity\"")
    A("    name: %s" % q("%s plate setup" % plate["barcode"]))
    A("    description: %s" % q(plate["description"]))
    A("    plate_type: %s" % q(plate["plate_type"]))
    A("    plate_barcode: %s" % q(plate["barcode"]))
    A("    plate_format: %s" % q(plate["plate_format"]))
    A("    well_count: %d" % plate["well_count"])
    A("    setup_date: %s" % q(plate["setup_date"]))
    A("    setup_operator_id: %s" % q(plate["operator"]))
    A("    setup_instrument: %s" % q(plate["setup_instrument"]))
    A("    sealing_method: %s" % q(plate["sealing_method"]))
    A("    temperature_celsius: %s" % q(plate["temperature_celsius"]))
    A("    agitation_speed_rpm: %s" % q(plate["agitation_speed_rpm"]))
    A("    oxygen_relationship: %s" % q(plate["oxygen_relationship"]))
    A("    processing_steps: %s"
      % q("dispense media; dispense inoculum; seal; load reader"))
    A("    media_ref: %s" % q(MEDIA_BY_KEY[plate["default_media"]]["ps_id"]))
    A("    # output plate processed sample: %s" % plate["plate_ps_id"])
    A("    well_metadata:")
    for w in plate["wells"]:
        parts = [
            "position: %s" % q(w["position"]),
            "well_type: %s" % q(w["well_type"]),
            "replicate_group: %s" % q(w["replicate_group"]),
            "media_ref: %s" % q(w["media_ref"]),
            "media_volume_ul: %s" % q(w["media_volume_ul"]),
            "inoculum_volume_ul: %s" % q(w["inoculum_volume_ul"]),
            "sample_id: %s" % q(w["sample_id"]),
        ]
        if w["treatments"]:
            parts.append("treatments: [%s]"
                         % ", ".join(q(t) for t in w["treatments"]))
        else:
            parts.append("treatments: null")
        A("      - {%s}" % ", ".join(parts))
    A("")

# --- data generation ------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# data_generation_activities  (class: AMP2DataGenerationActivity)")
A("#   analyte_id points at the plate processed sample. One activity per")
A("#   plate x timepoint. read_status \"aborted\" means no product was written.")
A("# ---------------------------------------------------------------------------")
A("data_generation_activities:")
DGA_FIELDS = ["id", "activity_type", "name", "description", "plate_barcode",
              "plate_setup_id", "analyte_id", "timepoint_label",
              "measurement_type", "wavelength_nm", "sequence_order",
              "acquisition_start_time", "acquisition_end_time",
              "instrument_used", "instrument_operator_id", "protocol_url",
              "protocol_version", "read_status", "product_id"]
for a in dga:
    first = True
    for f in DGA_FIELDS:
        prefix = "  - " if first else "    "
        A("%s%s: %s" % (prefix, f, q(a[f])))
        first = False
A("")

# --- products -------------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# od_products  (class: AMP2ODProduct, is_a PlateProduct)")
A("#   One per plate x completed timepoint. well_readings are embedded")
A("#   WellReading entries: position, value (OD600), flag.")
A("#   flag vocabulary: ok | blank | outlier | contaminated | failed")
A("# ---------------------------------------------------------------------------")
A("od_products:")
for pr in products:
    A("  - id: %s" % q(pr["id"]))
    A("    product_type: %s" % q(pr["product_type"]))
    A("    name: %s" % q(pr["name"]))
    A("    description: %s" % q(pr["description"]))
    A("    was_generated_by: %s" % q(pr["was_generated_by"]))
    A("    plate_barcode: %s" % q(pr["plate_barcode"]))
    A("    analyte_id: %s" % q(pr["analyte_id"]))
    A("    timepoint_label: %s" % q(pr["timepoint_label"]))
    A("    wavelength_nm: %s" % q(pr["wavelength_nm"]))
    A("    plate_average: %s" % q(pr["plate_average"]))
    A("    blank_mean: %s" % q(pr["blank_mean"]))
    A("    cv_percent: %s" % q(pr["cv_percent"]))
    A("    plate_reader_model: %s" % q(pr["plate_reader_model"]))
    A("    flagged_well_count: %d" % pr["flagged_well_count"])
    A("    well_readings:")
    for wr in pr["well_readings"]:
        A("      - {position: %s, value: %s, flag: %s}"
          % (q(wr["position"]), q(wr["value"]), q(wr["flag"])))
    A("")

# --- links ----------------------------------------------------------------
A("# ---------------------------------------------------------------------------")
A("# processing_sample_links  (class: ProcessingSampleLink)")
A("#   The authoritative sample <-> activity edges.")
A("#   sample_base_id may be an amp2_user_samples id OR a processed_samples id.")
A("#   role: input_sample | output_sample")
A("# ---------------------------------------------------------------------------")
A("processing_sample_links:")
for lk in links:
    A("  - {id: %s, sample_base_id: %s, processing_id: %s, step_number: %d, "
      "role: %s}" % (q(lk["id"]), q(lk["sample_base_id"]),
                     q(lk["processing_id"]), lk["step_number"], q(lk["role"])))
A("")

os.makedirs(CSV_DIR, exist_ok=True)
with open(YAML_PATH, "w") as fh:
    fh.write("\n".join(L))

# ---------------------------------------------------------------------------
# Emit CSVs
# ---------------------------------------------------------------------------


def write_csv(fname, header, rows):
    path = os.path.join(CSV_DIR, fname)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for r in rows:
            w.writerow(["" if v is None else v for v in r])
    return path


def joinlist(v):
    return "|".join(v) if v else None


# 00 crosswalk -------------------------------------------------------------
cw_rows = []
for s in SAMPLES:
    org = ORG_BY_ID[s["organism_ref"]]
    n = s["sample_number"]
    plates_used = []
    well_total = 0
    for plate in PLATES:
        hits = [w["position"] for w in plate["wells"]
                if w["sample_id"] == s["id"]]
        if hits:
            plates_used.append("%s(%d wells)" % (plate["barcode"], len(hits)))
            well_total += len(hits)
    cw_rows.append([
        s["id"], s["name"], s["lims_barcode"], s["organism_ref"],
        org["strain_identifier"], org["organism_name"], org["strain_type"],
        "urn:amp2:activity:strain-purity-%04d" % n,
        "urn:amp2:activity:stock-culture-%04d" % n, s["stock_ps"],
        "urn:amp2:activity:pre-culture-%04d" % n, s["pre_ps"],
        "urn:amp2:activity:experimental-culture-%04d" % n, s["exp_ps"],
        "|".join(plates_used), well_total,
    ])
write_csv("00_sample_identity_crosswalk.csv", [
    "user_sample_id", "user_sample_name", "lims_barcode", "organism_ref",
    "organism_strain_identifier", "organism_name", "strain_type",
    "strain_purity_activity_id", "stock_culture_activity_id",
    "stock_culture_processed_sample_id", "pre_culture_activity_id",
    "pre_culture_processed_sample_id", "experimental_culture_activity_id",
    "experimental_culture_processed_sample_id", "plates_and_well_counts",
    "total_wells"], cw_rows)

# 01 organisms -------------------------------------------------------------
write_csv("01_organisms.csv", ORG_FIELDS,
          [[o[f] for f in ORG_FIELDS] for o in ORGANISMS])

# 02 samples ---------------------------------------------------------------
write_csv("02_amp2_user_samples.csv", SAMPLE_FIELDS,
          [[s[f] for f in SAMPLE_FIELDS] for s in SAMPLES])

# 03 media -----------------------------------------------------------------
write_csv("03_media_preparations.csv", [
    "id", "name", "media_type", "volume_ml", "media_recipe",
    "media_formulation", "commercial_media_catalog", "sterilization_method",
    "ph_adjustment", "ph_target", "exposure_sensitivity", "media_additions",
    "storage_temperature", "creation_date", "output_processed_sample_id"],
    [[m["act_id"], m["name"], m["media_type"], m["volume_ml"],
      m["media_recipe"], m["media_formulation"],
      m["commercial_media_catalog"], m["sterilization_method"],
      m["ph_adjustment"], m["ph_target"], joinlist(m["exposure_sensitivity"]),
      joinlist(m["media_additions"]), m["storage_temperature"],
      m["creation_date"], m["ps_id"]] for m in MEDIA])

# 04 culture activities ----------------------------------------------------
write_csv("04_culture_growth_activities.csv",
          CULT_FIELDS + ["user_sample_name"],
          [[a[f] for f in CULT_FIELDS] + [a["sample_name"]]
           for a in culture_activities])

# 05 processed samples -----------------------------------------------------
write_csv("05_processed_samples.csv", [
    "id", "name", "processed_sample_type", "sampled_during", "description",
    "volume_uL", "replicate", "storage_location", "label_text"],
    [[p["id"], p["name"], p["processed_sample_type"], p["sampled_during"],
      p["description"], p["volume_uL"], p["replicate"],
      p["storage_location"], p["label_text"]] for p in processed_samples])

# 06 plate setup -----------------------------------------------------------
write_csv("06_plate_setup_activities.csv", [
    "id", "activity_type", "name", "plate_type", "plate_barcode",
    "plate_format", "well_count", "setup_date", "setup_operator_id",
    "setup_instrument", "sealing_method", "temperature_celsius",
    "agitation_speed_rpm", "oxygen_relationship", "media_ref",
    "output_plate_processed_sample_id", "description"],
    [[p["activity_id"], "AMP2PlateSetupActivity",
      "%s plate setup" % p["barcode"], p["plate_type"], p["barcode"],
      p["plate_format"], p["well_count"], p["setup_date"], p["operator"],
      p["setup_instrument"], p["sealing_method"], p["temperature_celsius"],
      p["agitation_speed_rpm"], p["oxygen_relationship"],
      MEDIA_BY_KEY[p["default_media"]]["ps_id"], p["plate_ps_id"],
      p["description"]] for p in plate_setups])

# 07 well metadata ---------------------------------------------------------
wm_rows = []
for plate in PLATES:
    default_media_ps = MEDIA_BY_KEY[plate["default_media"]]["ps_id"]
    for w in plate["wells"]:
        wm_rows.append([
            plate["barcode"], plate["activity_id"], w["position"],
            w["well_type"], w["replicate_group"], w["media_volume_ul"],
            w["inoculum_volume_ul"], w["sample_id"], w["sample_name"],
            w["media_ref"],
            w["media_ref"] if w["media_ref"] else default_media_ps,
            joinlist(w["treatments"]),
        ])
write_csv("07_well_metadata.csv", [
    "plate_barcode", "plate_setup_activity_id", "position", "well_type",
    "replicate_group", "media_volume_ul", "inoculum_volume_ul",
    "sample_id", "user_sample_name_denormalised", "media_ref_override",
    "effective_media_processed_sample_id", "treatments"], wm_rows)

# 08 data generation -------------------------------------------------------
write_csv("08_data_generation_activities.csv", DGA_FIELDS,
          [[a[f] for f in DGA_FIELDS] for a in dga])

# 09 products --------------------------------------------------------------
write_csv("09_od_products.csv", [
    "id", "product_type", "name", "was_generated_by", "plate_barcode",
    "analyte_id", "timepoint_label", "wavelength_nm", "plate_average",
    "blank_mean", "cv_percent", "plate_reader_model", "flagged_well_count"],
    [[p["id"], p["product_type"], p["name"], p["was_generated_by"],
      p["plate_barcode"], p["analyte_id"], p["timepoint_label"],
      p["wavelength_nm"], p["plate_average"], p["blank_mean"],
      p["cv_percent"], p["plate_reader_model"], p["flagged_well_count"]]
     for p in products])

# 10 well readings ---------------------------------------------------------
write_csv("10_well_readings.csv", [
    "product_id", "plate_barcode", "timepoint_label", "position", "value",
    "flag"], [list(r) for r in readings])

# 11 links -----------------------------------------------------------------
write_csv("11_processing_sample_links.csv", [
    "id", "sample_base_id", "processing_id", "step_number", "role"],
    [[lk["id"], lk["sample_base_id"], lk["processing_id"], lk["step_number"],
      lk["role"]] for lk in links])

# ---------------------------------------------------------------------------
# Bundle README
# ---------------------------------------------------------------------------

n_flag = {}
for _, _, _, _, _, flag in readings:
    n_flag[flag] = n_flag.get(flag, 0) + 1

readme = """# amp2-full-workflow-002

Simulated AMP2 dataset for ingestion testing against the BASALT schema.
Regenerate with `python3 generate.py` (deterministic — no wall-clock or
salted-hash inputs, so a re-run reproduces every value byte for byte).

The companion single-document view of the same data is
`../amp2-full-workflow-002.yaml`.

## What is in it

| | count |
|---|---|
| organisms (`organism`) | {n_org} |
| user samples (`AMP2UserSample`) | {n_samp} |
| media batches (`MediaPreparation`) | {n_media} |
| culture activities (`CultureGrowth` subclasses) | {n_cult} |
| plates (`AMP2PlateSetupActivity`) | {n_plate} |
| wells (`AMP2WellMetadata`) | {n_well} |
| OD reads (`AMP2DataGenerationActivity`) | {n_dga} |
| OD products (`AMP2ODProduct`) | {n_prod} |
| well readings (`WellReading`) | {n_read} |
| sample↔activity edges (`ProcessingSampleLink`) | {n_link} |

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

Flag tallies across all {n_read} readings: {flagtally}.

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
* `oxygen_relationship` is the canonical slot name; `oxygen_status` is an alias.
* Enum-ranged fields use permissible values from `enums.yaml`
  (`StrainTypeEnum`, `ModificationMethodEnum`, `IntendedTraitEnum`,
  `TrophicLevelEnum`, `GenotypeSegmentEnum`, `ConstructComponentEnum`,
  `MediaTypeEnum`, `FormulationEnum`, `StorageConditionEnum`,
  `GrowthFacilityEnum`, `OxygenStatusEnum`, `SampleRole`).
* Multivalued slots are pipe-delimited (`|`) in CSV and real YAML lists in the
  YAML document.
""".format(
    n_org=len(ORGANISMS), n_samp=len(SAMPLES), n_media=len(MEDIA),
    n_cult=len(culture_activities), n_plate=len(PLATES),
    n_well=sum(len(p["wells"]) for p in PLATES), n_dga=len(dga),
    n_prod=len(products), n_read=len(readings), n_link=len(links),
    flagtally=", ".join("`%s` %d" % (k, n_flag[k]) for k in
                        ("ok", "blank", "outlier", "contaminated", "failed")),
)

with open(os.path.join(CSV_DIR, "README.md"), "w") as fh:
    fh.write(readme)

# Ship the generator alongside the data so the bundle can be reproduced.
with open(__file__) as fh:
    _src = fh.read()
with open(os.path.join(CSV_DIR, "generate.py"), "w") as fh:
    fh.write(_src)

print("YAML   :", YAML_PATH, "%.1f KB" % (os.path.getsize(YAML_PATH) / 1024))
print("CSV dir:", CSV_DIR)
for f in sorted(os.listdir(CSV_DIR)):
    print("   %-42s %8.1f KB"
          % (f, os.path.getsize(os.path.join(CSV_DIR, f)) / 1024))
print()
print("samples=%d organisms=%d media=%d culture_acts=%d plates=%d wells=%d "
      "dga=%d products=%d readings=%d links=%d"
      % (len(SAMPLES), len(ORGANISMS), len(MEDIA), len(culture_activities),
         len(PLATES), sum(len(p['wells']) for p in PLATES), len(dga),
         len(products), len(readings), len(links)))
