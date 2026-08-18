

# Class: PlateDataGenerationActivity 


_Abstract base for plate measurement activities._

_Adds timepoint_label for repeated-measurement series _




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [basalt_schema:PlateDataGenerationActivity](https://emsl-computing.github.io/BASALT-Schema/elements/PlateDataGenerationActivity)





```mermaid
 classDiagram
    class PlateDataGenerationActivity
    click PlateDataGenerationActivity href "../PlateDataGenerationActivity/"
      DataGenerationActivity <|-- PlateDataGenerationActivity
        click DataGenerationActivity href "../DataGenerationActivity/"
      

      PlateDataGenerationActivity <|-- AMP2DataGenerationActivity
        click AMP2DataGenerationActivity href "../AMP2DataGenerationActivity/"
      PlateDataGenerationActivity <|-- EcoplateDataGenerationActivity
        click EcoplateDataGenerationActivity href "../EcoplateDataGenerationActivity/"
      

      PlateDataGenerationActivity : acquisition_end_time
        
      PlateDataGenerationActivity : acquisition_start_time
        
      PlateDataGenerationActivity : analyte_id
        
          
    
        
        
        PlateDataGenerationActivity --> "0..1" ProcessedSample : analyte_id
        click ProcessedSample href "../ProcessedSample/"
    

        
      PlateDataGenerationActivity : description
        
      PlateDataGenerationActivity : id
        
      PlateDataGenerationActivity : instrument_operator_id
        
          
    
        
        
        PlateDataGenerationActivity --> "0..1" PersonValue : instrument_operator_id
        click PersonValue href "../PersonValue/"
    

        
      PlateDataGenerationActivity : instrument_used
        
          
    
        
        
        PlateDataGenerationActivity --> "0..1" Instrument : instrument_used
        click Instrument href "../Instrument/"
    

        
      PlateDataGenerationActivity : name
        
      PlateDataGenerationActivity : protocol_url
        
      PlateDataGenerationActivity : protocol_version
        
      PlateDataGenerationActivity : sequence_order
        
      PlateDataGenerationActivity : timepoint_label
        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * **PlateDataGenerationActivity**
        * [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md)
        * [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [timepoint_label](timepoint_label.md) | 1 <br/> [String](String.md) | Human-readable timepoint label for repeated-measurement series | direct |
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













## TODOs

* measurement_time stamp



## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:PlateDataGenerationActivity |
| native | basalt_schema:PlateDataGenerationActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PlateDataGenerationActivity
description: 'Abstract base for plate measurement activities.

  Adds timepoint_label for repeated-measurement series '
todos:
- measurement_time stamp
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
abstract: true
slots:
- timepoint_label

```
</details>

### Induced

<details>
```yaml
name: PlateDataGenerationActivity
description: 'Abstract base for plate measurement activities.

  Adds timepoint_label for repeated-measurement series '
todos:
- measurement_time stamp
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
abstract: true
attributes:
  timepoint_label:
    name: timepoint_label
    description: 'Human-readable timepoint label for repeated-measurement series.

      Examples: "t=0", "t=24h", "t=48h".

      Lives on concrete analysis/product subclasses, NOT on base DataGenerationActivity'
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: timepoint_label
    owner: PlateDataGenerationActivity
    domain_of:
    - PlateDataGenerationActivity
    - PlateProduct
    range: string
    required: true
  sequence_order:
    name: sequence_order
    description: "Integer ordering within a temporal series for the same analyte.\n\
      Lower = earlier in series. Use when acquisition_time alone is insufficient.\n\
      \nDDL: ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order\
      \ INTEGER;"
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sequence_order
    owner: PlateDataGenerationActivity
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
    owner: PlateDataGenerationActivity
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
    owner: PlateDataGenerationActivity
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
    owner: PlateDataGenerationActivity
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
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: PlateDataGenerationActivity
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
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_start_time
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_end_time
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_used
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_operator_id
    owner: PlateDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>