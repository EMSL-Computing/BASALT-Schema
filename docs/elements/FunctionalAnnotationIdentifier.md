

# Class: FunctionalAnnotationIdentifier 



URI: [basalt_schema:FunctionalAnnotationIdentifier](https://EMSL-Computing.github.io/basalt-schema/FunctionalAnnotationIdentifier)





```mermaid
 classDiagram
    class FunctionalAnnotationIdentifier
    click FunctionalAnnotationIdentifier href "../FunctionalAnnotationIdentifier/"
      FunctionalAnnotationIdentifier : database
        
          
    
        
        
        FunctionalAnnotationIdentifier --> "1" AnnotationDatabaseEnum : database
        click AnnotationDatabaseEnum href "../AnnotationDatabaseEnum/"
    

        
      FunctionalAnnotationIdentifier : functional_identifier
        
      FunctionalAnnotationIdentifier : id
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [functional_identifier](functional_identifier.md) | 1 <br/> [String](String.md) |  | direct |
| [database](database.md) | 1 <br/> [AnnotationDatabaseEnum](AnnotationDatabaseEnum.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowExecutionFunctionalAnnotation](WorkflowExecutionFunctionalAnnotation.md) | [functional_annotation_id](functional_annotation_id.md) | range | [FunctionalAnnotationIdentifier](FunctionalAnnotationIdentifier.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:FunctionalAnnotationIdentifier |
| native | basalt_schema:FunctionalAnnotationIdentifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FunctionalAnnotationIdentifier
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
  functional_identifier:
    name: functional_identifier
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - FunctionalAnnotationIdentifier
    range: string
    required: true
  database:
    name: database
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - FunctionalAnnotationIdentifier
    range: AnnotationDatabaseEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: FunctionalAnnotationIdentifier
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: FunctionalAnnotationIdentifier
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
  functional_identifier:
    name: functional_identifier
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: functional_identifier
    owner: FunctionalAnnotationIdentifier
    domain_of:
    - FunctionalAnnotationIdentifier
    range: string
    required: true
  database:
    name: database
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: database
    owner: FunctionalAnnotationIdentifier
    domain_of:
    - FunctionalAnnotationIdentifier
    range: AnnotationDatabaseEnum
    required: true

```
</details>