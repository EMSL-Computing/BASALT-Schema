# About
# NAME PLACEHOLDER Schema

**NAME PLACEHOLDER schema** is a comprehensive schema for representing multimodal environmental and microbiological analysis data, including soil characterization and high-throughput microbial culture workflows. It supports diverse experimental techniques including mass spectrometry, metagenomics sequencing, X-ray fluorescence/diffraction, and 96-well plate-based growth assays. It is a production model in ongoing development to support the open, user-driven science the [Environmental Molecular Sciences Laboratory](https://www.emsl.pnnl.gov/) (EMSL).

**NOTE:** This schema is under active development and integrates metadata standards from multiple collaborating institutions (EMSL, GLBRC, NMDC, and more). Some areas are marked with TODOs for future refinement.

## Schema Organization

The schema follows a **relational design** with flat entity collections, explicit association tables for many-to-many relationships, and a pre-computed linkage cache for efficient provenance traversal. This supports flexible data reuse across studies and proposals.

The top-level entity is a **Study** (or Proposal), which serves as a container for related research. A study might represent all data from a specific EMSL proposal, user project, or collaborative investigation.

## Entity Tables

All entities are stored in flat collections linked to studies:

### Biological Materials

- **Samples**: Physical specimens submitted for analysis (soil, aerosol, user-submitted microbial cultures). Each sample includes collection metadata, storage conditions, and analysis type specifications.

- **Organisms**: Reference data representing biological identities (strains, isolates, engineered constructs) that can be instantiated by multiple physical samples. This separates the "what" (strain identity) from the "this tube" (physical sample).

- **Processed Samples**: Samples that have undergone laboratory processing—subsampling, extraction, digestion, or culture growth. These form chains linking back to original samples.

### Laboratory Resources

- **Media**: Growth media preparations with detailed recipes, pH adjustments, sterilization methods, and storage conditions. Supports strain purity, stock culture, pre-culture, and experimental culture media types.

- **Instruments**: Physical instrument metadata including manufacturer, model, and serial number. Activities reference instruments via association tables.

- **Purchased Materials**: Commercial reagents, standards, and supplies with catalog information and lot tracking.

### AMP2-Specific Culture-to-Phenotyping Workflows 

**Culture Growth Activities**: Laboratory activities for microbial culture workflows on the [Anaerobic Microbial Phenotyping Platform (AMP2)](https://www.emsl.pnnl.gov/science/instruments-resources/anaerobic-microbial-phenotyping-platform-amp2) including:

 - *Strain Purity*: Initial purity verification of user samples

 - *Stock Culture Preparation*: Creating glycerol stocks for long-term storage

 - *Pre-Culture Growth*: Starter cultures before experimental conditions

 - *Experimental Culture*: Growth under defined treatment conditions 

**Plate Setup Activities**: Configuration of 96-well plates for optical density measurements or Ecoplate metabolic profiling, with well-level sample/media assignments.
**Coming Soon**: HPLC and Flow Cytometry

### Data Generation

**Data Generation Activities**: Instrument runs that produce raw data, specialized by technique:

 - *Mass Spectrometry*: LC-MS, GC-MS, direct infusion FT-ICR with ionization and chromatography configurations 

 - *Nucleotide Sequencing*: Metagenomics and metatranscriptomics sequencing runs

 - *X-ray Analysis*: XRF elemental analysis and XRD mineralogical diffraction 

 - *Plate Reading*: Optical density and fluorescence measurements from plate readers

### Data Processing

**Data Processing Activities**: Computational workflows applied to raw data, including:
 - Mass spectrometry molecular identification (CoreMS)
 - Metagenomics assembly, annotation, and binning
 - XRD Rietveld refinement [10]

**Workflow Chaining**: Parent-child relationships between processing activities enable multi-step pipeline tracking via `parent_workflow_id`.

### Data Products

**Processed Data**: Abstract base for all analytical results, with concrete subclasses by technique:

 - *Mass Spectrometry Products*: Molecular identification tables, MS images, metaproteomics results

 - *Metagenomics Products*: Annotation, binning, and gene phylogeny outputs 

 - *Soil Characterization Products*: pH, texture, bulk density, hydraulic properties, elemental analysis, microbial biomass

 - *Plate Products*: Well-level readings with timepoints, blanks, and quality metrics

 - *X-ray Products*: XRF elemental concentrations and XRD mineral phase percentages

### Supporting Classes

- **Sites**: Location metadata for field sampling including coordinates, land use, vegetation, and climate information.

- **Methods**: Analytical method specifications with instrument parameters, calibration details, and detection limits.

- **Value Tables**: Structured representations for quantities (with units), controlled terms, timestamps, and person records.

## Association Tables

Many-to-many relationships are represented via explicit association tables:

- **ProcessingSampleLink**: Links samples to processing activities with step number and role (input/output) 

- **Instrument Associations**: Links instruments to activities with custodian tracking

- **Workflow Associations**: Links functional annotations and other outputs to workflow executions


## Contacts
- Yuri Corilo (corilo@pnnl.gov)
- Maia Kapur (maia.kapur@pnnl.gov)
- Bea Meluch (beata.meluch@pnnl.gov)
- Montana Smith (montana.smith@pnnl.gov)

