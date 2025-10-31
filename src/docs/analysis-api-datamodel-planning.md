# MONet Analysis API Extension Summary
## Project Context
We are extending the existing MONet analysis-api data model to accommodate the incoming AMP2 system and several FY26 Campaigns,  while maintaining the current hierarchy and using LinkML for schema development. The goal is to avoid excessive null columns and work within the existing Flask/SQLAlchemy/PostgreSQL structure.

## Campaign Data Integration
### Overview
Four one-year campaigns with shared analytical protocols. Campaigns use a dimensional table approach (not enums) for flexibility and manual data control (Conrad's suggestion).

#### Key Thoughts

- Campaign as Dimension Table: Use a proper fact/dimension table (Campaign) that gets populated manually, avoiding enum constraints
- Protocol-Based Organization: Organize data types by analytical protocol (not campaign year) since protocols are shared across campaigns
- Existing Schema Extension: Leverage existing processed_data table with JSON flexibility and data_type field for protocol distinction
- Ensure that sample preparation is documented for each protocol. Ideally, this information should be added to the SampleProcessing table, as it has been overlooked for some time. *Montana* & all to consider how this can integrate with campaign-specific

#### Identified Protocols, *not* in order of prority

1. XRF & XRD - mineral oxide concentrations (all campaigns); simple measurements of concentrations from external vendor. **Crucially**, these are not campaign specific and are to be added to the baseline set of MONet data types moving forward.
2. CMMs - univariate metal concentrations (subset of campaigns) via a sequential extraction. One sample to be passed thru the ICP 3+ times with various fractionating chemicals and the same set of target CMMs measured at each extraction; output similar to WEOM/MAOM.
3. LCMS metabolomics - metabolite profiles (subset of campaigns); this is a unique protocol and will separately include LESA methods for Terraforms (Rosey Chu and Aivett Bilbao will be generating the LESA-MS).
4. Ecoplates - time series data from 96-well plates with 3 reps each of 32 unique media in each well.  Soils PacWest will use these as-is. CMM-Rhizo will run each soil-depth combo against three plates with zero, low, or high nickel concentration, so we need to represent the distinct ecoplate media setup for these campaigns. The treatment/consideration of the time series nature of the raw data is TBD.
5. Terraforms - CMM-Rhizo (subtap, field micromodels) and lab microdels (CMM-Unconventional). Treatment/handling of time series nature TBDs.
6. Nickel Solubilization Assay (CMM-Rhizo only). Petri dish with nickel-spiked media; measure diameter of consumption. Will only happen for samples determined as nickel-resistant from ecoplate step (#4), meaning not all sample-depth combinations will have results from this protocol.


#### Database Changes
- New Campaign dimension table with fields (can modify): campaign_id, campaign_name, campaign_year, display_name, description, start_date, end_date, protocols_used, status
- Foreign key campaign_id added to Sample and ProcessedData tables
- Protocol-specific data types stored in existing processed_data.data JSON column
- Heavy raw data (like ecoplate time series) stored as URLs pointing to MinIO
    
#### LinkML Schema Files Needed
1. `campaigns/campaign_dimension.yaml` - Campaign dimension table, see overview of campaign names and leads [here](../docs/files/Campaign_Leads_Cheatsheet.pdf) -[X] addressed via [MR!7](https://gitlab.pnnl.gov/MoNET/analysis-api-schema/-/merge_requests/7)
2. `protocols/xrf_xrd_protocol.yaml` - XRF & XRD data structures and metadata **CONTACTS**: Kaizad's team has provided some [templated materials](../docs/files/XRF_XRD_template.xlsx) but more processing TBD. Consider subclassing XRAY approaches for these.
3. `protocols/cmms_protocol.yaml` - CMMS data structures and metadata **CONTACTS**: Odeta Qafoku & Amir Ahkami POST CMM workshops scheduled for early Nov.
4. `protocols/lcms_protocol.yaml` - LCMS data structures and metadata. **CONTACTS**: Che Clendinen; Conrad has some examples; ideally look for alignment with JGI.
5. `protocols/ecoplate_protocol.yaml` - Ecoplate data structures and metadata **CONTACTS**: Emily Graham and Amir Ahkami will be using these
6. `Updated processed_data.yaml` - Import all protocol schemas

    
## AMP2 System Integration
### Overview
Automated lab system with workflow chaining capabilities. Samples can be transformed through multiple processing steps, creating complex lineage chains. Focus is on workflow execution tracking and sample/data provenance.
#### Key Thoughts
- Workflow as anchor: Track individual workflow executions with chaining via self-referential foreign keys
- Sample vs Data Distinction: Physical samples (extracts, cultures) go in `samples` table; analytical results go in `processed_data` table
- Provenance Tracking: Enable bidirectional traversal from any sample/data product back to origins or forward to derivatives ("traverse the graph")
- Flexible Metadata: Use JSON columns with LinkML-defined schemas that vary by **workflow** type (not just instrument type)
- Non-Instrument Workflows: Optionally support workflows like cultivation, incubation, or sample preparation that don't use instruments

#### Core Concepts
- WorkflowDefinition: Template for any processing method that **may or may not** involve an instrument (e.g., "XRF_Analysis_v2.1", "Cultivation_Protocol_v1.0", "Sample_Prep_Standard")
- WorkflowExecution: Individual run of a workflow with specific metadata and sample inputs/outputs
- Chaining: `parent_execution_id` creates workflow chains (cultivation → extraction → analysis → summary)
- Sample Lineage: `source_workflow_execution_id` on `samples` tracks which workflow created them

#### Database Changes
- New workflow_definition table: workflow templates with workflow types (instrument-based **OR** process-based) and metadata schemas; consider [PROV-O Ontology](https://www.w3.org/TR/prov-o/)
- New workflow_execution table: individual runs with self-referential chaining and JSON metadata
- source_workflow_execution_id foreign key added to Sample table for lineage tracking
- source_workflow_execution_id foreign key added to ProcessedData table for data provenance

#### Metadata Schema Strategy
- Workflow-specific schemas: Each workflow type (e.g. HPLC, OD, EXTRACTION, FLOWCYTOMETER, STRAINCULTIVATION) has its own metadata structure
- Schema validation: `WorkflowDefinition.metadata_schema_class` field specifies which LinkML schema to validate against
- Nested structures: Metadata can be deeply nested for both instrument and non-instrument workflows

#### LinkML Schema Files Needed
1. `amp2/amp2_base.yaml` - Core workflow classes and relationships
2. `amp2/workflow_metadata.yaml` - Metadata schemas for each workflow type (instrument and non-instrument)
3. `amp2/sample_extensions.yaml` - AMP2-specific sample attributes and transformations
4. `amp2/processing_data.yaml `- AMP2-specific processed data types with workflow links
5. `amp2/enums.yaml` - Workflow types (both instrument and process), execution statuses, sample states
6. `amp2.yaml `- Master schema importing all AMP2 compon


