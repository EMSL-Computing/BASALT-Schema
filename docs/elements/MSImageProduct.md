

# Class: MSImageProduct 


_one or more image(s) output from a mass spec data processing workflow (eg. LESA, CoreMS QC plots). Should be a zip file containing all similar image outputs from one data processing workflow._





URI: [basalt_schema:MSImageProduct](https://EMSL-Computing.github.io/basalt-schema/MSImageProduct)





```mermaid
 classDiagram
    class MSImageProduct
    click MSImageProduct href "../MSImageProduct/"
      MassSpectrometryDataProduct <|-- MSImageProduct
        click MassSpectrometryDataProduct href "../MassSpectrometryDataProduct/"
      
      MSImageProduct : core_section
        
          
    
        
        
        MSImageProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      MSImageProduct : description
        
      MSImageProduct : filesize
        
      MSImageProduct : id
        
      MSImageProduct : lims_barcode
        
      MSImageProduct : md5checksum
        
      MSImageProduct : name
        
      MSImageProduct : project
        
      MSImageProduct : results_from_ms_processing
        
          
    
        
        
        MSImageProduct --> "0..1" MassSpectrometryDataProcessingActivity : results_from_ms_processing
        click MassSpectrometryDataProcessingActivity href "../MassSpectrometryDataProcessingActivity/"
    

        
      MSImageProduct : s3_base_url
        
      MSImageProduct : s3_bucket
        
      MSImageProduct : s3_key
        
      MSImageProduct : sample_id
        
          
    
        
        
        MSImageProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      MSImageProduct : sample_name
        
      MSImageProduct : sampling_set
        
      MSImageProduct : summary_metrics
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md)
            * **MSImageProduct**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [results_from_ms_processing](results_from_ms_processing.md) | 0..1 <br/> [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | a reference to the mass spec data processing activity that produced this data... | [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) |
| [summary_metrics](summary_metrics.md) | 0..1 <br/> [String](String.md) | Lightweight per-product summary for common queries that avoid full file downl... | [ProcessedData](ProcessedData.md) |
| [lims_barcode](lims_barcode.md) | 0..1 <br/> [String](String.md) | LIMS barcode identifier | [ProcessedData](ProcessedData.md) |
| [sample_id](sample_id.md) | 0..1 <br/> [Sample](Sample.md) | Link back to the originating sample | [ProcessedData](ProcessedData.md) |
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MSImageProduct |
| native | basalt_schema:MSImageProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MSImageProduct
description: one or more image(s) output from a mass spec data processing workflow
  (eg. LESA, CoreMS QC plots). Should be a zip file containing all similar image outputs
  from one data processing workflow.
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: MassSpectrometryDataProduct

```
</details>

### Induced

<details>
```yaml
name: MSImageProduct
description: one or more image(s) output from a mass spec data processing workflow
  (eg. LESA, CoreMS QC plots). Should be a zip file containing all similar image outputs
  from one data processing workflow.
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: MassSpectrometryDataProduct
attributes:
  results_from_ms_processing:
    name: results_from_ms_processing
    description: a reference to the mass spec data processing activity that produced
      this data product
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: results_from_ms_processing
    owner: MSImageProduct
    domain_of:
    - MassSpectrometryDataProduct
    range: MassSpectrometryDataProcessingActivity
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: summary_metrics
    owner: MSImageProduct
    domain_of:
    - ProcessedData
    range: string
    required: false
  lims_barcode:
    name: lims_barcode
    description: LIMS barcode identifier
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: lims_barcode
    owner: MSImageProduct
    domain_of:
    - ProcessedData
    - Sample
    range: string
    required: false
  sample_id:
    name: sample_id
    description: Link back to the originating sample
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sample_id
    owner: MSImageProduct
    domain_of:
    - ProcessedData
    - AMP2WellMetadata
    - MetagenomicsProduct
    range: Sample
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: name
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: description
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sampling_set
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: core_section
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    aliases:
    - samp_name
    rank: 1000
    alias: sample_name
    owner: MSImageProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_base_url
    owner: MSImageProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_bucket
    owner: MSImageProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_key
    owner: MSImageProduct
    domain_of:
    - DataProduct
    range: string
    required: true
  filesize:
    name: filesize
    description: Size of the file in bytes
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: filesize
    owner: MSImageProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: md5checksum
    owner: MSImageProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: MSImageProduct
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