

# Class: MetagenomicsProduct 


_Abstract base for all metagenomics data products._

_Inherits S3/file slots from dataProduct (via processedData is_a chain)._

_Concrete sub-types (Annotation, Binning, GenePhylogeny) use is_a to inherit_

_and add only their type-specific slots._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [basalt_schema:MetagenomicsProduct](https://EMSL-Computing.github.io/BASALT-Schema/MetagenomicsProduct)





```mermaid
 classDiagram
    class MetagenomicsProduct
    click MetagenomicsProduct href "../MetagenomicsProduct/"
      ProcessedData <|-- MetagenomicsProduct
        click ProcessedData href "../ProcessedData/"
      

      MetagenomicsProduct <|-- MetagenomicsAnnotationProduct
        click MetagenomicsAnnotationProduct href "../MetagenomicsAnnotationProduct/"
      MetagenomicsProduct <|-- MetagenomicsBinningProduct
        click MetagenomicsBinningProduct href "../MetagenomicsBinningProduct/"
      MetagenomicsProduct <|-- MetagenomicsGenePhylogenyProduct
        click MetagenomicsGenePhylogenyProduct href "../MetagenomicsGenePhylogenyProduct/"
      

      MetagenomicsProduct : additional_information
        
      MetagenomicsProduct : core_section
        
          
    
        
        
        MetagenomicsProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      MetagenomicsProduct : description
        
      MetagenomicsProduct : filesize
        
      MetagenomicsProduct : id
        
      MetagenomicsProduct : lims_barcode
        
      MetagenomicsProduct : md5checksum
        
      MetagenomicsProduct : mg_workflow_step
        
          
    
        
        
        MetagenomicsProduct --> "0..1" MetagenomicsSteps : mg_workflow_step
        click MetagenomicsSteps href "../MetagenomicsSteps/"
    

        
      MetagenomicsProduct : name
        
      MetagenomicsProduct : project
        
      MetagenomicsProduct : provider_name
        
          
    
        
        
        MetagenomicsProduct --> "0..1" ControlledTermValue : provider_name
        click ControlledTermValue href "../ControlledTermValue/"
    

        
      MetagenomicsProduct : raw_fasta_url
        
      MetagenomicsProduct : s3_base_url
        
      MetagenomicsProduct : s3_bucket
        
      MetagenomicsProduct : s3_key
        
      MetagenomicsProduct : sample_id
        
          
    
        
        
        MetagenomicsProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      MetagenomicsProduct : sample_name
        
      MetagenomicsProduct : sampling_set
        
      MetagenomicsProduct : summary_metrics
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * **MetagenomicsProduct**
            * [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md)
            * [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md)
            * [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [mg_workflow_step](mg_workflow_step.md) | 0..1 <br/> [MetagenomicsSteps](MetagenomicsSteps.md) | Metagenomics workflow step that produced this product (e | direct |
| [sample_id](sample_id.md) | 0..1 <br/> [Sample](Sample.md) | Link back to the originating sample | direct |
| [provider_name](provider_name.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Provider class (e | direct |
| [raw_fasta_url](raw_fasta_url.md) | 0..1 <br/> [String](String.md) | URL of raw FASTA file, if available from provider | direct |
| [additional_information](additional_information.md) | 0..1 <br/> [String](String.md) | Additional information pertaining to these data, including SP Project ID and ... | direct |
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
| self | basalt_schema:MetagenomicsProduct |
| native | basalt_schema:MetagenomicsProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetagenomicsProduct
description: 'Abstract base for all metagenomics data products.

  Inherits S3/file slots from dataProduct (via processedData is_a chain).

  Concrete sub-types (Annotation, Binning, GenePhylogeny) use is_a to inherit

  and add only their type-specific slots.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: ProcessedData
abstract: true
slots:
- mg_workflow_step
- sample_id
- provider_name
- raw_fasta_url
- additional_information

```
</details>

### Induced

<details>
```yaml
name: MetagenomicsProduct
description: 'Abstract base for all metagenomics data products.

  Inherits S3/file slots from dataProduct (via processedData is_a chain).

  Concrete sub-types (Annotation, Binning, GenePhylogeny) use is_a to inherit

  and add only their type-specific slots.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: ProcessedData
abstract: true
attributes:
  mg_workflow_step:
    name: mg_workflow_step
    description: Metagenomics workflow step that produced this product (e.g., MagsAnalysis)
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: mg_workflow_step
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
    domain_of:
    - MetagenomicsProduct
    range: ControlledTermValue
  raw_fasta_url:
    name: raw_fasta_url
    description: URL of raw FASTA file, if available from provider
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: raw_fasta_url
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: s3_bucket
    owner: MetagenomicsProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: s3_key
    owner: MetagenomicsProduct
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
    owner: MetagenomicsProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: md5checksum
    owner: MetagenomicsProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: MetagenomicsProduct
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