

# Class: ProjectParticipant 


_A record of a person and their role on an EMSL project._





URI: [analysis_api_schema:ProjectParticipant](https://w3id.org/MONet/analysis-api-schema/ProjectParticipant)





```mermaid
 classDiagram
    class ProjectParticipant
    click ProjectParticipant href "../ProjectParticipant/"
      ProjectParticipant : id
        
      ProjectParticipant : person
        
          
    
        
        
        ProjectParticipant --> "1" PersonValue : person
        click PersonValue href "../PersonValue/"
    

        
      ProjectParticipant : role
        
          
    
        
        
        ProjectParticipant --> "1" NexusRoleEnum : role
        click NexusRoleEnum href "../NexusRoleEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [role](role.md) | 1 <br/> [NexusRoleEnum](NexusRoleEnum.md) | The role of the contributor in the study (e | direct |
| [person](person.md) | 1 <br/> [PersonValue](PersonValue.md) | The person who contributed to the study | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [has_participants](has_participants.md) | range | [ProjectParticipant](ProjectParticipant.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ProjectParticipant |
| native | analysis_api_schema:ProjectParticipant |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProjectParticipant
description: A record of a person and their role on an EMSL project.
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
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
  role:
    name: role
    description: The role of the contributor in the study (e.g., data analysis, writing).
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
    domain_of:
    - ProcessingSampleLink
    - ProjectParticipant
    range: NexusRoleEnum
    required: true
  person:
    name: person
    description: The person who contributed to the study.
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
    rank: 1000
    domain_of:
    - ProjectParticipant
    range: PersonValue
    required: true

```
</details>

### Induced

<details>
```yaml
name: ProjectParticipant
description: A record of a person and their role on an EMSL project.
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
    identifier: true
    alias: id
    owner: ProjectParticipant
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
  role:
    name: role
    description: The role of the contributor in the study (e.g., data analysis, writing).
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
    alias: role
    owner: ProjectParticipant
    domain_of:
    - ProcessingSampleLink
    - ProjectParticipant
    range: NexusRoleEnum
    required: true
  person:
    name: person
    description: The person who contributed to the study.
    from_schema: https://w3id.org/MONet/analysis-api-schema/study
    rank: 1000
    alias: person
    owner: ProjectParticipant
    domain_of:
    - ProjectParticipant
    range: PersonValue
    required: true

```
</details>