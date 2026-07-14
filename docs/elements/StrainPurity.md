

# Class: StrainPurity 


_Purity check of a strain culture.  Verifies that a sample contains the_

_expected strain without contamination._

__

_Input:  sample(s) via processingSampleLink (role: input_sample)_

_Output: typically no new processedSample   pass/fail QC gate._

_Refs:   Media (growth medium), Strain (target organism)_





URI: [analysis_api_schema:StrainPurity](https://w3id.org/MONet/analysis-api-schema/StrainPurity)






```mermaid
 classDiagram
    class StrainPurity
    click StrainPurity href "../StrainPurity"
      CultureGrowth <|-- StrainPurity
        click CultureGrowth href "../CultureGrowth"
      
      StrainPurity : agitation_speed_rpm
        
      StrainPurity : analysis_type
        
          
    
    
    
    
    StrainPurity --> "0..1" RouteMethodEnum : analysis_type
    click RouteMethodEnum href "../RouteMethodEnum"
    

        
      StrainPurity : biological_entity_ref
        
          
    
    
    
    
    StrainPurity --> "0..1" BiologicalEntity : biological_entity_ref
    click BiologicalEntity href "../BiologicalEntity"
    

        
      StrainPurity : container_type
        
      StrainPurity : contaminant_strains
        
      StrainPurity : growth_medium
        
      StrainPurity : id
        
          
    
    

        
      StrainPurity : incubation_time_hours
        
      StrainPurity : inspection_method
        
      StrainPurity : method_name
        
          
    
    
    
    
    StrainPurity --> "0..1" MethodNameEnum : method_name
    click MethodNameEnum href "../MethodNameEnum"
    

        
      StrainPurity : oxygen_relationship
        
          
    
    
    
    
    StrainPurity --> "0..1" OxygenStatusEnum : oxygen_relationship
    click OxygenStatusEnum href "../OxygenStatusEnum"
    

        
      StrainPurity : processing_steps
        
      StrainPurity : protocol_url
        
      StrainPurity : protocol_version
        
      StrainPurity : target_strain
        
      StrainPurity : temperature_celsius
        
      StrainPurity : uses_sample
        
          
    
    
    
    
    StrainPurity --> "0..1" Sample : uses_sample
    click Sample href "../Sample"
    

        
      
```





## Inheritance
* [SampleProcessing](SampleProcessing.md)
    * [CultureGrowth](CultureGrowth.md) [ [HasIncubationConditions](HasIncubationConditions.md)]
        * **StrainPurity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [inspection_method](inspection_method.md) | 0..1 <br/> [String](String.md) | Method used to inspect or verify purity (visual, sequencing, etc | direct |
| [target_strain](target_strain.md) | 0..1 <br/> [String](String.md) | Target strain identifier for purity checks | direct |
| [contaminant_strains](contaminant_strains.md) | 0..1 <br/> [String](String.md) | Known or detected contaminant strains (if any) | direct |
| [biological_entity_ref](biological_entity_ref.md) | 0..1 <br/> [BiologicalEntity](BiologicalEntity.md) | FK reference to a biological_entity representing the biological identity | [CultureGrowth](CultureGrowth.md) |
| [growth_medium](growth_medium.md) | 0..1 <br/> [String](String.md) | Method of growth and medium/materials used | [CultureGrowth](CultureGrowth.md) |
| [incubation_time_hours](incubation_time_hours.md) | 0..1 <br/> [Float](Float.md) | Incubation duration in hours | [CultureGrowth](CultureGrowth.md) |
| [container_type](container_type.md) | 0..1 <br/> [String](String.md) | Physical container used for the culture (flask, tube, plate, etc | [CultureGrowth](CultureGrowth.md) |
| [temperature_celsius](temperature_celsius.md) | 0..1 <br/> [Float](Float.md) | Temperature at which the method/process/activity was performed | [HasIncubationConditions](HasIncubationConditions.md) |
| [agitation_speed_rpm](agitation_speed_rpm.md) | 0..1 <br/> [Integer](Integer.md) | Agitation/shaking speed in RPM (0 for static) | [HasIncubationConditions](HasIncubationConditions.md) |
| [oxygen_relationship](oxygen_relationship.md) | 0..1 <br/> [OxygenStatusEnum](OxygenStatusEnum.md) | The relationship of the sample to oxygen, such as aerobic or anaerobic | [HasIncubationConditions](HasIncubationConditions.md) |
| [protocol_url](protocol_url.md) | 0..1 <br/> [String](String.md) | URL pointing to the protocol used in the activity, if applicable | [SampleProcessing](SampleProcessing.md) |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the protocol used in the activity, if applicable | [SampleProcessing](SampleProcessing.md) |
| [id](id.md) | 1 <br/> uuid |  | [SampleProcessing](SampleProcessing.md) |
| [analysis_type](analysis_type.md) | 0..1 <br/> [RouteMethodEnum](RouteMethodEnum.md) |  | [SampleProcessing](SampleProcessing.md) |
| [method_name](method_name.md) | 0..1 <br/> [MethodNameEnum](MethodNameEnum.md) |  | [SampleProcessing](SampleProcessing.md) |
| [processing_steps](processing_steps.md) | 1 <br/> [String](String.md) |  | [SampleProcessing](SampleProcessing.md) |
| [uses_sample](uses_sample.md) | 0..1 <br/> [Sample](Sample.md) |  | [SampleProcessing](SampleProcessing.md) |









## TODOs

* purity percentage

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:StrainPurity |
| native | analysis_api_schema:StrainPurity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StrainPurity
description: 'Purity check of a strain culture.  Verifies that a sample contains the

  expected strain without contamination.


  Input:  sample(s) via processingSampleLink (role: input_sample)

  Output: typically no new processedSample   pass/fail QC gate.

  Refs:   Media (growth medium), Strain (target organism)'
todos:
- purity percentage
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: CultureGrowth
slots:
- inspection_method
- target_strain
- contaminant_strains

```
</details>

### Induced

<details>
```yaml
name: StrainPurity
description: 'Purity check of a strain culture.  Verifies that a sample contains the

  expected strain without contamination.


  Input:  sample(s) via processingSampleLink (role: input_sample)

  Output: typically no new processedSample   pass/fail QC gate.

  Refs:   Media (growth medium), Strain (target organism)'
todos:
- purity percentage
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: CultureGrowth
attributes:
  inspection_method:
    name: inspection_method
    description: Method used to inspect or verify purity (visual, sequencing, etc.)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: inspection_method
    owner: StrainPurity
    domain_of:
    - StrainPurity
    range: string
  target_strain:
    name: target_strain
    description: Target strain identifier for purity checks
    todos:
    - should this point to the Strain class?
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: target_strain
    owner: StrainPurity
    domain_of:
    - StrainPurity
    range: string
  contaminant_strains:
    name: contaminant_strains
    description: Known or detected contaminant strains (if any)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: contaminant_strains
    owner: StrainPurity
    domain_of:
    - StrainPurity
    range: string
  biological_entity_ref:
    name: biological_entity_ref
    description: 'FK reference to a biological_entity representing the biological
      identity

      strain, isolate, engineered construct) that this sample or activity

      is associated with.'
    from_schema: https://w3id.org/MONet/analysis-api-schema
    aliases:
    - strain_ref
    - strain_id
    rank: 1000
    alias: biological_entity_ref
    owner: StrainPurity
    domain_of:
    - CultureGrowth
    - AMP2UserSample
    - EngineeredStrainSample
    range: biological_entity
    required: false
  growth_medium:
    name: growth_medium
    description: Method of growth and medium/materials used. Indicate broth, gel,
      3-D structure, bioreactor, etc. followed by the formula, recipe, or components
      used to create the growth medium.
    title: growth medium
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: growth_medium
    owner: StrainPurity
    domain_of:
    - CultureGrowth
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - OtherUndescribedSample
    - PureCultureSample
    - TerraformSample
    range: string
  incubation_time_hours:
    name: incubation_time_hours
    description: Incubation duration in hours
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: incubation_time_hours
    owner: StrainPurity
    domain_of:
    - CultureGrowth
    range: float
  container_type:
    name: container_type
    description: Physical container used for the culture (flask, tube, plate, etc.)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: container_type
    owner: StrainPurity
    domain_of:
    - ContainerType
    - CultureGrowth
    range: string
  temperature_celsius:
    name: temperature_celsius
    description: Temperature at which the method/process/activity was performed
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: temperature_celsius
    owner: StrainPurity
    domain_of:
    - ChromatographyConfiguration
    - HasIncubationConditions
    range: float
  agitation_speed_rpm:
    name: agitation_speed_rpm
    description: Agitation/shaking speed in RPM (0 for static)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: agitation_speed_rpm
    owner: StrainPurity
    domain_of:
    - HasIncubationConditions
    range: integer
  oxygen_relationship:
    name: oxygen_relationship
    description: The relationship of the sample to oxygen, such as aerobic or anaerobic.
    title: oxygen relationship
    from_schema: https://w3id.org/MONet/analysis-api-schema
    exact_mappings:
    - MIXS:0000015
    rank: 1000
    alias: oxygen_status
    owner: StrainPurity
    domain_of:
    - HasIncubationConditions
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
    - FieldDeployedTerraformSample
    - MixedCultureSample
    - OtherUndescribedSample
    - PureCultureSample
    - SedimentSample
    - SoilSample
    - SynthesizedMaterialSample
    - TerraformSample
    - WaterSample
    range: OxygenStatusEnum
  protocol_url:
    name: protocol_url
    description: URL pointing to the protocol used in the activity, if applicable.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: protocol_url
    owner: StrainPurity
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
    owner: StrainPurity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
    alias: id
    owner: StrainPurity
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
  analysis_type:
    name: analysis_type
    from_schema: https://w3id.org/MONet/analysis-api-schema
    alias: analysis_type
    owner: StrainPurity
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
    owner: StrainPurity
    domain_of:
    - SampleProcessing
    range: MethodNameEnum
  processing_steps:
    name: processing_steps
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: processing_steps
    owner: StrainPurity
    domain_of:
    - SampleProcessing
    range: string
    required: true
  uses_sample:
    name: uses_sample
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: uses_sample
    owner: StrainPurity
    domain_of:
    - SampleProcessing
    range: Sample

```
</details>