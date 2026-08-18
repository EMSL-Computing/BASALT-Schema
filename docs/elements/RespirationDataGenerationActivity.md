

# Class: RespirationDataGenerationActivity 


_Data generation activity for soil respiration analysis._

_Captures CO2-C efflux measured per gram of soil._





URI: [basalt_schema:RespirationDataGenerationActivity](https://EMSL-Computing.github.io/BASALT-Schema/RespirationDataGenerationActivity)





```mermaid
 classDiagram
    class RespirationDataGenerationActivity
    click RespirationDataGenerationActivity href "../RespirationDataGenerationActivity/"
      DataGenerationActivity <|-- RespirationDataGenerationActivity
        click DataGenerationActivity href "../DataGenerationActivity/"
      
      RespirationDataGenerationActivity : acquisition_end_time
        
      RespirationDataGenerationActivity : acquisition_start_time
        
      RespirationDataGenerationActivity : analyte_id
        
          
    
        
        
        RespirationDataGenerationActivity --> "0..1" ProcessedSample : analyte_id
        click ProcessedSample href "../ProcessedSample/"
    

        
      RespirationDataGenerationActivity : description
        
      RespirationDataGenerationActivity : id
        
      RespirationDataGenerationActivity : instrument_operator_id
        
          
    
        
        
        RespirationDataGenerationActivity --> "0..1" PersonValue : instrument_operator_id
        click PersonValue href "../PersonValue/"
    

        
      RespirationDataGenerationActivity : instrument_used
        
          
    
        
        
        RespirationDataGenerationActivity --> "0..1" Instrument : instrument_used
        click Instrument href "../Instrument/"
    

        
      RespirationDataGenerationActivity : method_id
        
          
    
        
        
        RespirationDataGenerationActivity --> "0..1" RespirationMethod : method_id
        click RespirationMethod href "../RespirationMethod/"
    

        
      RespirationDataGenerationActivity : name
        
      RespirationDataGenerationActivity : protocol_url
        
      RespirationDataGenerationActivity : protocol_version
        
      RespirationDataGenerationActivity : sequence_order
        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * **RespirationDataGenerationActivity**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [method_id](method_id.md) | 0..1 <br/> [RespirationMethod](RespirationMethod.md) | Reference to the RespirationMethod used for this run | direct |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:RespirationDataGenerationActivity |
| native | basalt_schema:RespirationDataGenerationActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RespirationDataGenerationActivity
description: 'Data generation activity for soil respiration analysis.

  Captures CO2-C efflux measured per gram of soil.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
attributes:
  method_id:
    name: method_id
    description: Reference to the RespirationMethod used for this run
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    domain_of:
    - RespirationDataGenerationActivity
    range: RespirationMethod

```
</details>

### Induced

<details>
```yaml
name: RespirationDataGenerationActivity
description: 'Data generation activity for soil respiration analysis.

  Captures CO2-C efflux measured per gram of soil.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
attributes:
  method_id:
    name: method_id
    description: Reference to the RespirationMethod used for this run
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: method_id
    owner: RespirationDataGenerationActivity
    domain_of:
    - RespirationDataGenerationActivity
    range: RespirationMethod
  sequence_order:
    name: sequence_order
    description: "Integer ordering within a temporal series for the same analyte.\n\
      Lower = earlier in series. Use when acquisition_time alone is insufficient.\n\
      \nDDL: ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order\
      \ INTEGER;"
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: sequence_order
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: integer
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: RespirationDataGenerationActivity
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
    owner: RespirationDataGenerationActivity
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
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_url
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  protocol_version:
    name: protocol_version
    description: Version of the protocol used in the activity, if applicable.
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_version
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: RespirationDataGenerationActivity
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
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: analyte_id
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_start_time
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_end_time
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_used
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_operator_id
    owner: RespirationDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>