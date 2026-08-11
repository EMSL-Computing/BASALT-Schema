

# Class: LabDevice 


_A lab device is a physical instrument or equipment used in a laboratory setting for conducting experiments, measurements, or analyses. It can include various types of instruments such as microscopes, spectrometers, centrifuges, and other specialized equipment. Lab devices are essential for performing scientific research and obtaining accurate data._





URI: [basalt_schema:LabDevice](https://EMSL-Computing.github.io/basalt-schema/LabDevice)





```mermaid
 classDiagram
    class LabDevice
    click LabDevice href "../LabDevice/"
      LabDevice : activity_speed_id
        
          
    
        
        
        LabDevice --> "0..1" QuantityValue : activity_speed_id
        click QuantityValue href "../QuantityValue/"
    

        
      LabDevice : activity_time_id
        
          
    
        
        
        LabDevice --> "0..1" QuantityValue : activity_time_id
        click QuantityValue href "../QuantityValue/"
    

        
      LabDevice : description
        
      LabDevice : device_type
        
          
    
        
        
        LabDevice --> "0..1" DeviceTypeEnum : device_type
        click DeviceTypeEnum href "../DeviceTypeEnum/"
    

        
      LabDevice : id
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [device_type](device_type.md) | 0..1 <br/> [DeviceTypeEnum](DeviceTypeEnum.md) |  | direct |
| [activity_time_id](activity_time_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [activity_speed_id](activity_speed_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:LabDevice |
| native | basalt_schema:LabDevice |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabDevice
description: A lab device is a physical instrument or equipment used in a laboratory
  setting for conducting experiments, measurements, or analyses. It can include various
  types of instruments such as microscopes, spectrometers, centrifuges, and other
  specialized equipment. Lab devices are essential for performing scientific research
  and obtaining accurate data.
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
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
  description:
    name: description
    from_schema: https://EMSL-Computing.github.io/basalt-schema
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
  device_type:
    name: device_type
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - LabDevice
    range: DeviceTypeEnum
  activity_time_id:
    name: activity_time_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - LabDevice
    range: QuantityValue
  activity_speed_id:
    name: activity_speed_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - LabDevice
    range: QuantityValue

```
</details>

### Induced

<details>
```yaml
name: LabDevice
description: A lab device is a physical instrument or equipment used in a laboratory
  setting for conducting experiments, measurements, or analyses. It can include various
  types of instruments such as microscopes, spectrometers, centrifuges, and other
  specialized equipment. Lab devices are essential for performing scientific research
  and obtaining accurate data.
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: LabDevice
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
  description:
    name: description
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    alias: description
    owner: LabDevice
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
  device_type:
    name: device_type
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: device_type
    owner: LabDevice
    domain_of:
    - LabDevice
    range: DeviceTypeEnum
  activity_time_id:
    name: activity_time_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: activity_time_id
    owner: LabDevice
    domain_of:
    - LabDevice
    range: QuantityValue
  activity_speed_id:
    name: activity_speed_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: activity_speed_id
    owner: LabDevice
    domain_of:
    - LabDevice
    range: QuantityValue

```
</details>