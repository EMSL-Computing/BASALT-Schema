

# Class: MassSpectrometryStandardRun 


_A record of a mass spectrometry standard run with a batch of samples, which is used for calibration and quality control._





URI: [basalt_schema:MassSpectrometryStandardRun](https://EMSL-Computing.github.io/BASALT-Schema/MassSpectrometryStandardRun)





```mermaid
 classDiagram
    class MassSpectrometryStandardRun
    click MassSpectrometryStandardRun href "../MassSpectrometryStandardRun/"
      MassSpectrometryStandardRun : calibration_data
        
          
    
        
        
        MassSpectrometryStandardRun --> "0..1" MassSpectrometryInstrumentData : calibration_data
        click MassSpectrometryInstrumentData href "../MassSpectrometryInstrumentData/"
    

        
      MassSpectrometryStandardRun : calibration_standard
        
          
    
        
        
        MassSpectrometryStandardRun --> "0..1" PurchasedMaterial : calibration_standard
        click PurchasedMaterial href "../PurchasedMaterial/"
    

        
      MassSpectrometryStandardRun : calibration_target
        
          
    
        
        
        MassSpectrometryStandardRun --> "0..1" CalibrationTargetEnum : calibration_target
        click CalibrationTargetEnum href "../CalibrationTargetEnum/"
    

        
      MassSpectrometryStandardRun : description
        
      MassSpectrometryStandardRun : id
        
      MassSpectrometryStandardRun : internal_calibration
        
      MassSpectrometryStandardRun : name
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | direct |
| [internal_calibration](internal_calibration.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether internal calibration was used | direct |
| [calibration_target](calibration_target.md) | 0..1 <br/> [CalibrationTargetEnum](CalibrationTargetEnum.md) | The measurement being calibrated | direct |
| [calibration_standard](calibration_standard.md) | 0..1 <br/> [PurchasedMaterial](PurchasedMaterial.md) | The reference standard used for calibration | direct |
| [calibration_data](calibration_data.md) | 0..1 <br/> [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) | Reference to the raw instrument data file used for calibration | direct |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | [uses_calibration](uses_calibration.md) | range | [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MassSpectrometryStandardRun |
| native | basalt_schema:MassSpectrometryStandardRun |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MassSpectrometryStandardRun
description: A record of a mass spectrometry standard run with a batch of samples,
  which is used for calibration and quality control.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
slots:
- name
- description
- internal_calibration
- calibration_target
- calibration_standard
- calibration_data
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema/mass-spec
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

```
</details>

### Induced

<details>
```yaml
name: MassSpectrometryStandardRun
description: A record of a mass spectrometry standard run with a batch of samples,
  which is used for calibration and quality control.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema/mass-spec
    identifier: true
    alias: id
    owner: MassSpectrometryStandardRun
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
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: MassSpectrometryStandardRun
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
    owner: MassSpectrometryStandardRun
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
  internal_calibration:
    name: internal_calibration
    description: Whether internal calibration was used
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: internal_calibration
    owner: MassSpectrometryStandardRun
    domain_of:
    - MassSpectrometryStandardRun
    range: boolean
  calibration_target:
    name: calibration_target
    description: The measurement being calibrated
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: calibration_target
    owner: MassSpectrometryStandardRun
    domain_of:
    - MassSpectrometryStandardRun
    range: CalibrationTargetEnum
  calibration_standard:
    name: calibration_standard
    description: The reference standard used for calibration
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: calibration_standard
    owner: MassSpectrometryStandardRun
    domain_of:
    - MassSpectrometryStandardRun
    range: PurchasedMaterial
  calibration_data:
    name: calibration_data
    description: Reference to the raw instrument data file used for calibration
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: calibration_data
    owner: MassSpectrometryStandardRun
    domain_of:
    - MassSpectrometryStandardRun
    range: MassSpectrometryInstrumentData

```
</details>