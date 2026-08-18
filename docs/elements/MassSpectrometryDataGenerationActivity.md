

# Class: MassSpectrometryDataGenerationActivity 


_A record of the mass spectrometry run that generates a raw data product._





URI: [basalt_schema:MassSpectrometryDataGenerationActivity](https://emsl-computing.github.io/BASALT-Schema/elements/MassSpectrometryDataGenerationActivity)





```mermaid
 classDiagram
    class MassSpectrometryDataGenerationActivity
    click MassSpectrometryDataGenerationActivity href "../MassSpectrometryDataGenerationActivity/"
      DataGenerationActivity <|-- MassSpectrometryDataGenerationActivity
        click DataGenerationActivity href "../DataGenerationActivity/"
      
      MassSpectrometryDataGenerationActivity : acquisition_end_time
        
      MassSpectrometryDataGenerationActivity : acquisition_start_time
        
      MassSpectrometryDataGenerationActivity : analyte_category
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "0..1" AnalyteCategoryEnum : analyte_category
        click AnalyteCategoryEnum href "../AnalyteCategoryEnum/"
    

        
      MassSpectrometryDataGenerationActivity : analyte_id
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "0..1" ProcessedSample : analyte_id
        click ProcessedSample href "../ProcessedSample/"
    

        
      MassSpectrometryDataGenerationActivity : description
        
      MassSpectrometryDataGenerationActivity : id
        
      MassSpectrometryDataGenerationActivity : instrument_operator_id
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "0..1" PersonValue : instrument_operator_id
        click PersonValue href "../PersonValue/"
    

        
      MassSpectrometryDataGenerationActivity : instrument_used
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "0..1" Instrument : instrument_used
        click Instrument href "../Instrument/"
    

        
      MassSpectrometryDataGenerationActivity : name
        
      MassSpectrometryDataGenerationActivity : protocol_url
        
      MassSpectrometryDataGenerationActivity : protocol_version
        
      MassSpectrometryDataGenerationActivity : sequence_order
        
      MassSpectrometryDataGenerationActivity : uses_chromatography
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "0..1" ChromatographyConfiguration : uses_chromatography
        click ChromatographyConfiguration href "../ChromatographyConfiguration/"
    

        
      MassSpectrometryDataGenerationActivity : uses_ms_configuration
        
          
    
        
        
        MassSpectrometryDataGenerationActivity --> "1" MassSpectrometryConfiguration : uses_ms_configuration
        click MassSpectrometryConfiguration href "../MassSpectrometryConfiguration/"
    

        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * **MassSpectrometryDataGenerationActivity**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [uses_ms_configuration](uses_ms_configuration.md) | 1 <br/> [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Points to a record of the configuration used for the mass spectrometry run | direct |
| [uses_chromatography](uses_chromatography.md) | 0..1 <br/> [ChromatographyConfiguration](ChromatographyConfiguration.md) | Points to a record of the chromatography used to introduce samples for the ma... | direct |
| [analyte_category](analyte_category.md) | 0..1 <br/> [AnalyteCategoryEnum](AnalyteCategoryEnum.md) | omics type for easier search, optional | direct |
| [sequence_order](sequence_order.md) | 0..1 <br/> [Integer](Integer.md) | Integer ordering within a temporal series for the same analyte | [DataGenerationActivity](DataGenerationActivity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_url](protocol_url.md) | 0..1 <br/> [String](String.md) | URL pointing to the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [analyte_id](analyte_id.md) | 0..1 <br/> [ProcessedSample](ProcessedSample.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [acquisition_start_time](acquisition_start_time.md) | 1 <br/> [Datetime](Datetime.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [acquisition_end_time](acquisition_end_time.md) | 1 <br/> [Datetime](Datetime.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [instrument_used](instrument_used.md) | 0..1 <br/> [Instrument](Instrument.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [instrument_operator_id](instrument_operator_id.md) | 0..1 <br/> [PersonValue](PersonValue.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) | [produced_by_ms_run](produced_by_ms_run.md) | range | [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MassSpectrometryDataGenerationActivity |
| native | basalt_schema:MassSpectrometryDataGenerationActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MassSpectrometryDataGenerationActivity
description: A record of the mass spectrometry run that generates a raw data product.
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
slots:
- uses_ms_configuration
- uses_chromatography
- analyte_category

```
</details>

### Induced

<details>
```yaml
name: MassSpectrometryDataGenerationActivity
description: A record of the mass spectrometry run that generates a raw data product.
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
attributes:
  uses_ms_configuration:
    name: uses_ms_configuration
    description: Points to a record of the configuration used for the mass spectrometry
      run.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: uses_ms_configuration
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - MassSpectrometryDataGenerationActivity
    range: MassSpectrometryConfiguration
    required: true
  uses_chromatography:
    name: uses_chromatography
    description: Points to a record of the chromatography used to introduce samples
      for the mass spectrometry run.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: uses_chromatography
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - MassSpectrometryDataGenerationActivity
    range: ChromatographyConfiguration
  analyte_category:
    name: analyte_category
    description: omics type for easier search, optional
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: analyte_category
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - MassSpectrometryDataGenerationActivity
    range: AnalyteCategoryEnum
  sequence_order:
    name: sequence_order
    description: "Integer ordering within a temporal series for the same analyte.\n\
      Lower = earlier in series. Use when acquisition_time alone is insufficient.\n\
      \nDDL: ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order\
      \ INTEGER;"
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sequence_order
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: integer
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: MassSpectrometryDataGenerationActivity
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
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: description
    owner: MassSpectrometryDataGenerationActivity
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
  protocol_url:
    name: protocol_url
    description: URL pointing to the protocol used in the activity, if applicable.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_url
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  protocol_version:
    name: protocol_version
    description: Version of the protocol used in the activity, if applicable.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_version
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: MassSpectrometryDataGenerationActivity
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
  analyte_id:
    name: analyte_id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: analyte_id
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_start_time
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_end_time
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_used
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_operator_id
    owner: MassSpectrometryDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>