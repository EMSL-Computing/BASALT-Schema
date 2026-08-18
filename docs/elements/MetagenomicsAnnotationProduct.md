

# Class: MetagenomicsAnnotationProduct 


_Top-level archive for functional annotation outputs (zip/tar stored in MinIO)._

_Inherits all MetagenomicsProduct and dataProduct slots._





URI: [basalt_schema:MetagenomicsAnnotationProduct](https://EMSL-Computing.github.io/BASALT-Schema/MetagenomicsAnnotationProduct)





```mermaid
 classDiagram
    class MetagenomicsAnnotationProduct
    click MetagenomicsAnnotationProduct href "../MetagenomicsAnnotationProduct/"
      MetagenomicsProduct <|-- MetagenomicsAnnotationProduct
        click MetagenomicsProduct href "../MetagenomicsProduct/"
      
      MetagenomicsAnnotationProduct : additional_information
        
      MetagenomicsAnnotationProduct : annotation_database
        
          
    
        
        
        MetagenomicsAnnotationProduct --> "0..1" AnnotationDatabaseEnum : annotation_database
        click AnnotationDatabaseEnum href "../AnnotationDatabaseEnum/"
    

        
      MetagenomicsAnnotationProduct : core_section
        
          
    
        
        
        MetagenomicsAnnotationProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      MetagenomicsAnnotationProduct : description
        
      MetagenomicsAnnotationProduct : filesize
        
      MetagenomicsAnnotationProduct : id
        
      MetagenomicsAnnotationProduct : lims_barcode
        
      MetagenomicsAnnotationProduct : md5checksum
        
      MetagenomicsAnnotationProduct : mg_workflow_step
        
          
    
        
        
        MetagenomicsAnnotationProduct --> "0..1" MetagenomicsSteps : mg_workflow_step
        click MetagenomicsSteps href "../MetagenomicsSteps/"
    

        
      MetagenomicsAnnotationProduct : name
        
      MetagenomicsAnnotationProduct : project
        
      MetagenomicsAnnotationProduct : provider_name
        
          
    
        
        
        MetagenomicsAnnotationProduct --> "0..1" ControlledTermValue : provider_name
        click ControlledTermValue href "../ControlledTermValue/"
    

        
      MetagenomicsAnnotationProduct : raw_fasta_url
        
      MetagenomicsAnnotationProduct : s3_base_url
        
      MetagenomicsAnnotationProduct : s3_bucket
        
      MetagenomicsAnnotationProduct : s3_key
        
      MetagenomicsAnnotationProduct : sample_id
        
          
    
        
        
        MetagenomicsAnnotationProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      MetagenomicsAnnotationProduct : sample_name
        
      MetagenomicsAnnotationProduct : sampling_set
        
      MetagenomicsAnnotationProduct : summary_metrics
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * [MetagenomicsProduct](MetagenomicsProduct.md)
            * **MetagenomicsAnnotationProduct**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [annotation_database](annotation_database.md) | 0..1 <br/> [AnnotationDatabaseEnum](AnnotationDatabaseEnum.md) | Primary annotation database used (e | direct |
| [mg_workflow_step](mg_workflow_step.md) | 0..1 <br/> [MetagenomicsSteps](MetagenomicsSteps.md) | Metagenomics workflow step that produced this product (e | [MetagenomicsProduct](MetagenomicsProduct.md) |
| [sample_id](sample_id.md) | 0..1 <br/> [Sample](Sample.md) | Link back to the originating sample | [ProcessedData](ProcessedData.md), [MetagenomicsProduct](MetagenomicsProduct.md) |
| [provider_name](provider_name.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Provider class (e | [MetagenomicsProduct](MetagenomicsProduct.md) |
| [raw_fasta_url](raw_fasta_url.md) | 0..1 <br/> [String](String.md) | URL of raw FASTA file, if available from provider | [MetagenomicsProduct](MetagenomicsProduct.md) |
| [additional_information](additional_information.md) | 0..1 <br/> [String](String.md) | Additional information pertaining to these data, including SP Project ID and ... | [MetagenomicsProduct](MetagenomicsProduct.md) |
| [summary_metrics](summary_metrics.md) | 0..1 <br/> [String](String.md) | Lightweight per-product summary for common queries that avoid full file downl... | [ProcessedData](ProcessedData.md) |
| [lims_barcode](lims_barcode.md) | 0..1 <br/> [String](String.md) | LIMS barcode identifier | [ProcessedData](ProcessedData.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataProduct](DataProduct.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataProduct](DataProduct.md) |
| [project](project.md) | 0..1 <br/> [Integer](Integer.md) | Identifier for the user project associated with the entity or activity | [DataProduct](DataProduct.md) |
| [sampling_set](sampling_set.md) | 0..1 <br/> [Integer](Integer.md) | Sampling set number for grouping related samples collected together | [DataProduct](DataProduct.md) |
| [core_section](core_section.md) | 0..1 <br/> [CoreSectionEnum](CoreSectionEnum.md) | The section of the core | [DataProduct](DataProduct.md) |
| [sample_name](sample_name.md) | 0..1 <br/> [String](String.md) | The name or label that is present on the shipped sample | [DataProduct](DataProduct.md) |
| [s3_base_url](s3_base_url.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_bucket](s3_bucket.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_key](s3_key.md) | 1 <br/> [String](String.md) | MinIO/S3 object key; required for all data products | [DataProduct](DataProduct.md) |
| [filesize](filesize.md) | 0..1 <br/> [Integer](Integer.md) | Size of the file in bytes | [DataProduct](DataProduct.md) |
| [md5checksum](md5checksum.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | [DataProduct](DataProduct.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MetagenomicsAnnotationProduct |
| native | basalt_schema:MetagenomicsAnnotationProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Metagenomics_AnnotationProduct
description: 'Top-level archive for functional annotation outputs (zip/tar stored
  in MinIO).

  Inherits all MetagenomicsProduct and dataProduct slots.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: MetagenomicsProduct
slots:
- annotation_database

```
</details>

### Induced

<details>
```yaml
name: Metagenomics_AnnotationProduct
description: 'Top-level archive for functional annotation outputs (zip/tar stored
  in MinIO).

  Inherits all MetagenomicsProduct and dataProduct slots.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: MetagenomicsProduct
attributes:
  annotation_database:
    name: annotation_database
    description: Primary annotation database used (e.g., IMG, KEGG)
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: annotation_database
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - Metagenomics_AnnotationProduct
    range: AnnotationDatabaseEnum
    required: false
  mg_workflow_step:
    name: mg_workflow_step
    description: Metagenomics workflow step that produced this product (e.g., MagsAnalysis)
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: mg_workflow_step
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - MetagenomicsProduct
    range: MetagenomicsSteps
    required: false
  sample_id:
    name: sample_id
    description: Link back to the originating sample
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: sample_id
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - ProcessedData
    - AMP2WellMetadata
    - MetagenomicsProduct
    range: Sample
    required: false
  provider_name:
    name: provider_name
    description: Provider class (e.g., JGI, SeqCenter) using ontology terms where
      possible
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: provider_name
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - MetagenomicsProduct
    range: ControlledTermValue
  raw_fasta_url:
    name: raw_fasta_url
    description: URL of raw FASTA file, if available from provider
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: raw_fasta_url
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - MetagenomicsProduct
    range: string
  additional_information:
    name: additional_information
    description: Additional information pertaining to these data, including SP Project
      ID and Taxon OID
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: additional_information
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - MetagenomicsProduct
    range: string
  summary_metrics:
    name: summary_metrics
    description: "Lightweight per-product summary for common queries that avoid full\
      \ file download.\nDirection: structured key-value pairs; per-type schemas TBD:\n\
      \  ecoplate:  well-level absorbance summaries (position, timepoint, absorbance)\n\
      \  xrf:       per-element concentration results + QC flag\n  lcms:      feature\
      \ count, identification count, MSI-2 fraction\nInterim DB storage: JSONB column\
      \ retained until formal typed class exists."
    todos:
    - make this inined/multivalued?
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: summary_metrics
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - ProcessedData
    range: string
    required: false
  lims_barcode:
    name: lims_barcode
    description: LIMS barcode identifier
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: lims_barcode
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - ProcessedData
    - Sample
    range: string
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - Activity
    - Entity
    - DataProduct
    - DataGenerationActivity
    - Instrument
    - OntologyClass
    - ContainerAxis
    - Configuration
    - MobilePhaseSegment
    - MassSpectrometryStandardRun
    - PurchasedMaterial
    - LabProcessingActivity
    - organism
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - Study
    - SoftwareControlledTermValue
    range: string
    required: true
  description:
    name: description
    description: Human-readable description for the entity or activity
    title: description
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: description
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - Activity
    - Entity
    - DataProduct
    - DataGenerationActivity
    - DataProcessingActivity
    - OntologyClass
    - ContainerType
    - LabDevice
    - Configuration
    - MassSpectrometryStandardRun
    - PurchasedMaterial
    - LabProcessingActivity
    - organism
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - Study
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - QuantityValue
    range: string
  project:
    name: project
    description: 'Identifier for the user project associated with the entity or activity. '
    title: Project
    todos:
    - should this be an ID? CURIE can use the one NMDC has https://bioregistry.io/reference/emsl.project:60141
      where emsl.project is the CURIE prefix
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    - AerosolArmSample
    - AerosolSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - MonetSoilSample
    - OtherUndescribedSample
    - PlantSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    - SamplingActivity
    range: integer
  sampling_set:
    name: sampling_set
    description: 'Sampling set number for grouping related samples collected together.

      This is a user-defined sequential integer that can be used to link samples collected

      in the same sampling event or campaign.'
    title: sampling set
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: sampling_set
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    - MonetSoilSample
    range: integer
  core_section:
    name: core_section
    description: The section of the core.
    title: core section
    examples:
    - value: TOP
    - value: MID
    - value: BTM
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: core_section
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    - CoreSection
    range: CoreSectionEnum
  sample_name:
    name: sample_name
    description: 'The name or label that is present on the shipped sample. This should

      be a human readable name.'
    title: sample name
    notes:
    - This is typically an alias for the inherited 'name' slot on Sample classes.
      Defined separately for compatibility with source data files using 'sample_name'
      column headers.
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    aliases:
    - samp_name
    rank: 1000
    alias: sample_name
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    - AerosolArmSample
    - AerosolSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - MonetSoilSample
    - OtherUndescribedSample
    - PlantSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    range: string
  s3_base_url:
    name: s3_base_url
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: s3_base_url
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: s3_bucket
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: s3_key
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    range: string
    required: true
  filesize:
    name: filesize
    description: Size of the file in bytes
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: filesize
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: md5checksum
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: Metagenomics_AnnotationProduct
    domain_of:
    - Activity
    - Entity
    - DataProduct
    - DataGenerationActivity
    - DataProcessingActivity
    - AlternativeIdentifier
    - FunctionalAnnotationIdentifier
    - Instrument
    - OntologyClass
    - ContainerType
    - Custodian
    - InstrumentAlternativeIdentifier
    - LabDevice
    - SampleProcessing
    - ProcessingSampleLink
    - Configuration
    - MobilePhaseSegment
    - MassSpectrometryStandardRun
    - PurchasedMaterial
    - LabProcessingActivity
    - organism
    - MAOMProduct
    - WEOMProduct
    - Site
    - Sample
    - AerosolArmSample
    - AerosolSample
    - AMP2UserSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - EngineeredStrainSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - MonetSoilSample
    - OtherUndescribedSample
    - PlantSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    - ProcessedSample
    - CoreSection
    - SamplingActivity
    - AerosolArmSamplingActivity
    - AerosolSamplingActivity
    - CommerciallyPurchasedSamplingActivity
    - CultureEnvironmentalSamplingActivity
    - EngineeredStrainSamplingActivity
    - FieldDeployedTerraformSamplingActivity
    - MixedCultureSamplingActivity
    - MonetSoilSamplingActivity
    - OtherUndescribedSamplingActivity
    - PlantSamplingActivity
    - PureCultureSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    - SynthesizedMaterialSamplingActivity
    - TerraformSamplingActivity
    - WaterSamplingActivity
    - Study
    - ProjectParticipant
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - PersonValue
    - QuantityValue
    - ConditioningValue
    - zipDownload
    range: uuid
    required: true

```
</details>