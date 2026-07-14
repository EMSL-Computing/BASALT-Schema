

# Class: MassSpectrometryInstrumentData 


_Raw data files output from a mass spectrometry instrument._





URI: [analysis_api_schema:MassSpectrometryInstrumentData](https://w3id.org/MONet/analysis-api-schema/MassSpectrometryInstrumentData)






```mermaid
 classDiagram
    class MassSpectrometryInstrumentData
    click MassSpectrometryInstrumentData href "../MassSpectrometryInstrumentData"
      InstrumentData <|-- MassSpectrometryInstrumentData
        click InstrumentData href "../InstrumentData"
      
      MassSpectrometryInstrumentData : alternative_identifiers
        
      MassSpectrometryInstrumentData : collection_mode
        
          
    
    
    
    
    MassSpectrometryInstrumentData --> "0..1" MassSpectrumCollectionModeEnum : collection_mode
    click MassSpectrumCollectionModeEnum href "../MassSpectrumCollectionModeEnum"
    

        
      MassSpectrometryInstrumentData : compression_type
        
      MassSpectrometryInstrumentData : core_section
        
          
    
    
    
    
    MassSpectrometryInstrumentData --> "0..1" CoreSectionEnum : core_section
    click CoreSectionEnum href "../CoreSectionEnum"
    

        
      MassSpectrometryInstrumentData : description
        
      MassSpectrometryInstrumentData : file_curie
        
      MassSpectrometryInstrumentData : file_type
        
          
    
    
    
    
    MassSpectrometryInstrumentData --> "0..1" FileTypeEnum : file_type
    click FileTypeEnum href "../FileTypeEnum"
    

        
      MassSpectrometryInstrumentData : filesize
        
      MassSpectrometryInstrumentData : id
        
          
    
    

        
      MassSpectrometryInstrumentData : md5checksum
        
      MassSpectrometryInstrumentData : ms_raw_file_type
        
          
    
    
    
    
    MassSpectrometryInstrumentData --> "0..1" MassSpecRawFileTypeEnum : ms_raw_file_type
    click MassSpecRawFileTypeEnum href "../MassSpecRawFileTypeEnum"
    

        
      MassSpectrometryInstrumentData : name
        
      MassSpectrometryInstrumentData : produced_by_ms_run
        
          
    
    
    
    
    MassSpectrometryInstrumentData --> "0..1" MassSpectrometryDataGenerationActivity : produced_by_ms_run
    click MassSpectrometryDataGenerationActivity href "../MassSpectrometryDataGenerationActivity"
    

        
      MassSpectrometryInstrumentData : project
        
      MassSpectrometryInstrumentData : s3_base_url
        
      MassSpectrometryInstrumentData : s3_bucket
        
      MassSpectrometryInstrumentData : s3_key
        
      MassSpectrometryInstrumentData : sample_name
        
      MassSpectrometryInstrumentData : sampling_set
        
      MassSpectrometryInstrumentData : software_version
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [InstrumentData](InstrumentData.md)
        * **MassSpectrometryInstrumentData**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [produced_by_ms_run](produced_by_ms_run.md) | 0..1 <br/> [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | a reference to the data generation activity that produced instrument data | direct |
| [ms_raw_file_type](ms_raw_file_type.md) | 0..1 <br/> [MassSpecRawFileTypeEnum](MassSpecRawFileTypeEnum.md) | the filetype of the mass spectrometry instrument data | direct |
| [collection_mode](collection_mode.md) | 0..1 <br/> [MassSpectrumCollectionModeEnum](MassSpectrumCollectionModeEnum.md) | The collection mode for the mass spectrometry data (e | direct |
| [file_curie](file_curie.md) | 0..1 <br/> [String](String.md) | an identifier for a file that resolves to the file's accessible location | [InstrumentData](InstrumentData.md) |
| [alternative_identifiers](alternative_identifiers.md) | 0..1 <br/> [String](String.md) |  | [InstrumentData](InstrumentData.md) |
| [compression_type](compression_type.md) | 0..1 <br/> [String](String.md) |  | [InstrumentData](InstrumentData.md) |
| [file_type](file_type.md) | 0..1 <br/> [FileTypeEnum](FileTypeEnum.md) |  | [InstrumentData](InstrumentData.md) |
| [software_version](software_version.md) | 0..1 <br/> [String](String.md) |  | [InstrumentData](InstrumentData.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataProduct](DataProduct.md) |
| [description](description.md) | 1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataProduct](DataProduct.md) |
| [project](project.md) | 0..1 <br/> [Integer](Integer.md) | Identifier for the user project associated with the entity or activity | [DataProduct](DataProduct.md) |
| [sampling_set](sampling_set.md) | 0..1 <br/> [Integer](Integer.md) | Sampling set number for grouping related samples collected together | [DataProduct](DataProduct.md) |
| [core_section](core_section.md) | 0..1 <br/> [CoreSectionEnum](CoreSectionEnum.md) | The section of the core | [DataProduct](DataProduct.md) |
| [sample_name](sample_name.md) | 0..1 <br/> [String](String.md) | The name or label that is present on the shipped sample | [DataProduct](DataProduct.md) |
| [s3_base_url](s3_base_url.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_bucket](s3_bucket.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_key](s3_key.md) | 1 <br/> [String](String.md) | MinIO/S3 object key; required for all data products | [DataProduct](DataProduct.md) |
| [filesize](filesize.md) | 0..1 <br/> [Integer](Integer.md) | Size of the file in bytes | [DataProduct](DataProduct.md) |
| [md5checksum](md5checksum.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [id](id.md) | 1 <br/> uuid |  | [DataProduct](DataProduct.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | [uses_raw_ms_data](uses_raw_ms_data.md) | range | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |
| [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) | [calibration_data](calibration_data.md) | range | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:MassSpectrometryInstrumentData |
| native | analysis_api_schema:MassSpectrometryInstrumentData |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MassSpectrometryInstrumentData
description: Raw data files output from a mass spectrometry instrument.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: InstrumentData
slots:
- produced_by_ms_run
- ms_raw_file_type
- collection_mode

```
</details>

### Induced

<details>
```yaml
name: MassSpectrometryInstrumentData
description: Raw data files output from a mass spectrometry instrument.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: InstrumentData
attributes:
  produced_by_ms_run:
    name: produced_by_ms_run
    description: a reference to the data generation activity that produced instrument
      data
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: produced_by_ms_run
    owner: MassSpectrometryInstrumentData
    domain_of:
    - MassSpectrometryInstrumentData
    range: MassSpectrometryDataGenerationActivity
  ms_raw_file_type:
    name: ms_raw_file_type
    description: the filetype of the mass spectrometry instrument data
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: ms_raw_file_type
    owner: MassSpectrometryInstrumentData
    domain_of:
    - MassSpectrometryInstrumentData
    range: MassSpecRawFileTypeEnum
  collection_mode:
    name: collection_mode
    description: The collection mode for the mass spectrometry data (e.g., profile,
      centroid)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: collection_mode
    owner: MassSpectrometryInstrumentData
    domain_of:
    - MassSpectrometryInstrumentData
    range: MassSpectrumCollectionModeEnum
  file_curie:
    name: file_curie
    description: an identifier for a file that resolves to the file's accessible location
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: file_curie
    owner: MassSpectrometryInstrumentData
    domain_of:
    - InstrumentData
    range: string
  alternative_identifiers:
    name: alternative_identifiers
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: alternative_identifiers
    owner: MassSpectrometryInstrumentData
    domain_of:
    - InstrumentData
    - OntologyClass
    range: string
  compression_type:
    name: compression_type
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: compression_type
    owner: MassSpectrometryInstrumentData
    domain_of:
    - InstrumentData
    range: string
  file_type:
    name: file_type
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: file_type
    owner: MassSpectrometryInstrumentData
    domain_of:
    - InstrumentData
    range: FileTypeEnum
  software_version:
    name: software_version
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: software_version
    owner: MassSpectrometryInstrumentData
    domain_of:
    - InstrumentData
    - DataProcessingActivity
    range: string
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: name
    owner: MassSpectrometryInstrumentData
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
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - biological_entity
    - Study
    - SoftwareControlledTermValue
    range: string
    required: true
  description:
    name: description
    description: Human-readable description for the entity or activity
    title: description
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: description
    owner: MassSpectrometryInstrumentData
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
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - biological_entity
    - Study
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - QuantityValue
    range: string
    required: true
  project:
    name: project
    description: 'Identifier for the user project associated with the entity or activity. '
    title: Project
    todos:
    - should this be an ID? CURIE can use the one NMDC has https://bioregistry.io/reference/emsl.project:60141
      where emsl.project is the CURIE prefix
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: '[''study'', ''study_id'', ''project_id'', ''proposal'', ''proposal_id'']'
    owner: MassSpectrometryInstrumentData
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: sampling_set
    owner: MassSpectrometryInstrumentData
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: core_section
    owner: MassSpectrometryInstrumentData
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    aliases:
    - samp_name
    rank: 1000
    alias: sample_name
    owner: MassSpectrometryInstrumentData
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: s3_base_url
    owner: MassSpectrometryInstrumentData
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: s3_bucket
    owner: MassSpectrometryInstrumentData
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: s3_key
    owner: MassSpectrometryInstrumentData
    domain_of:
    - DataProduct
    range: string
    required: true
  filesize:
    name: filesize
    description: Size of the file in bytes
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: filesize
    owner: MassSpectrometryInstrumentData
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: md5checksum
    owner: MassSpectrometryInstrumentData
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
    alias: id
    owner: MassSpectrometryInstrumentData
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
    - biological_entity
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