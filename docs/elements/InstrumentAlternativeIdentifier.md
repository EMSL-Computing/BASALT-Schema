

# Class: InstrumentAlternativeIdentifier 



URI: [basalt_schema:InstrumentAlternativeIdentifier](https://EMSL-Computing.github.io/basalt-schema/InstrumentAlternativeIdentifier)





```mermaid
 classDiagram
    class InstrumentAlternativeIdentifier
    click InstrumentAlternativeIdentifier href "../InstrumentAlternativeIdentifier/"
      InstrumentAlternativeIdentifier : alt_id
        
          
    
        
        
        InstrumentAlternativeIdentifier --> "0..1" AlternativeIdentifier : alt_id
        click AlternativeIdentifier href "../AlternativeIdentifier/"
    

        
      InstrumentAlternativeIdentifier : id
        
      InstrumentAlternativeIdentifier : instrument_alt_id_provider
        
          
    
        
        
        InstrumentAlternativeIdentifier --> "0..1" InstrumentAltIdProviderEnum : instrument_alt_id_provider
        click InstrumentAltIdProviderEnum href "../InstrumentAltIdProviderEnum/"
    

        
      InstrumentAlternativeIdentifier : instrument_id
        
          
    
        
        
        InstrumentAlternativeIdentifier --> "1" Instrument : instrument_id
        click Instrument href "../Instrument/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [alt_id](alt_id.md) | 0..1 <br/> [AlternativeIdentifier](AlternativeIdentifier.md) |  | direct |
| [instrument_alt_id_provider](instrument_alt_id_provider.md) | 0..1 <br/> [InstrumentAltIdProviderEnum](InstrumentAltIdProviderEnum.md) |  | direct |
| [instrument_id](instrument_id.md) | 1 <br/> [Instrument](Instrument.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:InstrumentAlternativeIdentifier |
| native | basalt_schema:InstrumentAlternativeIdentifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstrumentAlternativeIdentifier
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
  alt_id:
    name: alt_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - InstrumentAlternativeIdentifier
    range: AlternativeIdentifier
  instrument_alt_id_provider:
    name: instrument_alt_id_provider
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - InstrumentAlternativeIdentifier
    range: InstrumentAltIdProviderEnum
  instrument_id:
    name: instrument_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - InstrumentAlternativeIdentifier
    - InstrumentCustodian
    range: Instrument
    required: true

```
</details>

### Induced

<details>
```yaml
name: InstrumentAlternativeIdentifier
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: InstrumentAlternativeIdentifier
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
  alt_id:
    name: alt_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: alt_id
    owner: InstrumentAlternativeIdentifier
    domain_of:
    - InstrumentAlternativeIdentifier
    range: AlternativeIdentifier
  instrument_alt_id_provider:
    name: instrument_alt_id_provider
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: instrument_alt_id_provider
    owner: InstrumentAlternativeIdentifier
    domain_of:
    - InstrumentAlternativeIdentifier
    range: InstrumentAltIdProviderEnum
  instrument_id:
    name: instrument_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: instrument_id
    owner: InstrumentAlternativeIdentifier
    domain_of:
    - InstrumentAlternativeIdentifier
    - InstrumentCustodian
    range: Instrument
    required: true

```
</details>