

# Class: SampleProcessing 


_Abstract base for any sample processing activity (physical to physical). Input data should _

_be specified on workflow subclasses._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [analysis_api_schema:SampleProcessing](https://w3id.org/MONet/analysis-api-schema/SampleProcessing)





```mermaid
 classDiagram
    class SampleProcessing
    click SampleProcessing href "../SampleProcessing/"
      SampleProcessing <|-- MediaPreparation
        click MediaPreparation href "../MediaPreparation/"
      SampleProcessing <|-- CultureGrowth
        click CultureGrowth href "../CultureGrowth/"
      SampleProcessing <|-- PlateSetupActivity
        click PlateSetupActivity href "../PlateSetupActivity/"
      
      SampleProcessing : analysis_type
        
          
    
        
        
        SampleProcessing --> "0..1" RouteMethodEnum : analysis_type
        click RouteMethodEnum href "../RouteMethodEnum/"
    

        
      SampleProcessing : id
        
      SampleProcessing : method_name
        
          
    
        
        
        SampleProcessing --> "0..1" MethodNameEnum : method_name
        click MethodNameEnum href "../MethodNameEnum/"
    

        
      SampleProcessing : processing_steps
        
      SampleProcessing : protocol_url
        
      SampleProcessing : protocol_version
        
      SampleProcessing : uses_sample
        
          
    
        
        
        SampleProcessing --> "0..1" Sample : uses_sample
        click Sample href "../Sample/"
    

        
      
```





## Inheritance
* **SampleProcessing**
    * [MediaPreparation](MediaPreparation.md)
    * [CultureGrowth](CultureGrowth.md) [ [HasIncubationConditions](HasIncubationConditions.md)]
    * [PlateSetupActivity](PlateSetupActivity.md) [ [HasIncubationConditions](HasIncubationConditions.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [protocol_url](protocol_url.md) | 0..1 <br/> [String](String.md) | URL pointing to the protocol used in the activity, if applicable | direct |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the protocol used in the activity, if applicable | direct |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [analysis_type](analysis_type.md) | 0..1 <br/> [RouteMethodEnum](RouteMethodEnum.md) |  | direct |
| [method_name](method_name.md) | 0..1 <br/> [MethodNameEnum](MethodNameEnum.md) |  | direct |
| [processing_steps](processing_steps.md) | 1 <br/> [String](String.md) |  | direct |
| [uses_sample](uses_sample.md) | 0..1 <br/> [Sample](Sample.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | [processing_id](processing_id.md) | range | [SampleProcessing](SampleProcessing.md) |
| [ProcessedSample](ProcessedSample.md) | [sampled_during](sampled_during.md) | range | [SampleProcessing](SampleProcessing.md) |
| [CoreSection](CoreSection.md) | [sampled_during](sampled_during.md) | range | [SampleProcessing](SampleProcessing.md) |










## TODOs

* why does this have both analysis type and method name, as enums, just set the range to the class



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:SampleProcessing |
| native | analysis_api_schema:SampleProcessing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SampleProcessing
description: "Abstract base for any sample processing activity (physical to physical).\
  \ Input data should \nbe specified on workflow subclasses."
todos:
- why does this have both analysis type and method name, as enums, just set the range
  to the class
from_schema: https://w3id.org/MONet/analysis-api-schema
abstract: true
slots:
- protocol_url
- protocol_version
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
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
  analysis_type:
    name: analysis_type
    from_schema: https://w3id.org/MONet/analysis-api-schema
    domain_of:
    - SampleProcessing
    - AerosolArmSample
    - AerosolSample
    - AMP2UserSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - OtherUndescribedSample
    - PlantSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    range: RouteMethodEnum
  method_name:
    name: method_name
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    domain_of:
    - SampleProcessing
    range: MethodNameEnum
  processing_steps:
    name: processing_steps
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    domain_of:
    - SampleProcessing
    range: string
    required: true
  uses_sample:
    name: uses_sample
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    domain_of:
    - SampleProcessing
    range: Sample

```
</details>

### Induced

<details>
```yaml
name: SampleProcessing
description: "Abstract base for any sample processing activity (physical to physical).\
  \ Input data should \nbe specified on workflow subclasses."
todos:
- why does this have both analysis type and method name, as enums, just set the range
  to the class
from_schema: https://w3id.org/MONet/analysis-api-schema
abstract: true
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
    alias: id
    owner: SampleProcessing
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
  analysis_type:
    name: analysis_type
    from_schema: https://w3id.org/MONet/analysis-api-schema
    alias: analysis_type
    owner: SampleProcessing
    domain_of:
    - SampleProcessing
    - AerosolArmSample
    - AerosolSample
    - AMP2UserSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - OtherUndescribedSample
    - PlantSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    range: RouteMethodEnum
  method_name:
    name: method_name
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: method_name
    owner: SampleProcessing
    domain_of:
    - SampleProcessing
    range: MethodNameEnum
  processing_steps:
    name: processing_steps
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: processing_steps
    owner: SampleProcessing
    domain_of:
    - SampleProcessing
    range: string
    required: true
  uses_sample:
    name: uses_sample
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: uses_sample
    owner: SampleProcessing
    domain_of:
    - SampleProcessing
    range: Sample
  protocol_url:
    name: protocol_url
    description: URL pointing to the protocol used in the activity, if applicable.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: protocol_url
    owner: SampleProcessing
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  protocol_version:
    name: protocol_version
    description: Version of the protocol used in the activity, if applicable.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: protocol_version
    owner: SampleProcessing
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string

```
</details>