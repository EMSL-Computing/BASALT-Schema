

# Class: Soil Sampling Activity (SoilSamplingActivity) 


_Collection of soil samples from the environment._





URI: [basalt_schema:SoilSamplingActivity](https://emsl-computing.github.io/BASALT-Schema/elements/SoilSamplingActivity)





```mermaid
 classDiagram
    class SoilSamplingActivity
    click SoilSamplingActivity href "../SoilSamplingActivity/"
      SamplingActivity <|-- SoilSamplingActivity
        click SamplingActivity href "../SamplingActivity/"
      
      SoilSamplingActivity : collection_date
        
      SoilSamplingActivity : collection_time
        
      SoilSamplingActivity : description
        
      SoilSamplingActivity : emsl_activity
        
      SoilSamplingActivity : id
        
      SoilSamplingActivity : infiltration_1
        
      SoilSamplingActivity : infiltration_2
        
      SoilSamplingActivity : infiltration_notes
        
      SoilSamplingActivity : name
        
      SoilSamplingActivity : project
        
      SoilSamplingActivity : sample_collected
        
      SoilSamplingActivity : sample_collection_dev
        
      SoilSamplingActivity : sample_collection_method
        
      SoilSamplingActivity : sampled_at_site
        
          
    
        
        
        SoilSamplingActivity --> "0..1" Site : sampled_at_site
        click Site href "../Site/"
    

        
      SoilSamplingActivity : shipped_sample_size
        
      SoilSamplingActivity : weather
        
      SoilSamplingActivity : wind_direction
        
          
    
        
        
        SoilSamplingActivity --> "0..1" CardinalDirectionEnum : wind_direction
        click CardinalDirectionEnum href "../CardinalDirectionEnum/"
    

        
      
```





## Inheritance
* [SamplingActivity](SamplingActivity.md)
    * **SoilSamplingActivity**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | direct |
| [collection_time](collection_time.md) | 0..1 <br/> [String](String.md) | The time of sampling as an instance (single point) | direct |
| [infiltration_1](infiltration_1.md) | 0..1 <br/> [String](String.md) | Amount of time it takes to accomplish the first infiltration activity | direct |
| [infiltration_2](infiltration_2.md) | 0..1 <br/> [String](String.md) | Amount of time it takes to accomplish the second infiltration activity | direct |
| [infiltration_notes](infiltration_notes.md) | 0..1 <br/> [String](String.md) | Provide any details, issues, or context needed to understand the infiltration... | direct |
| [sample_collected](sample_collected.md) | 0..1 <br/> [String](String.md) | This refers to the TOTAL amount of sample collected from the experiment | direct |
| [sample_collection_dev](sample_collection_dev.md) | 0..1 <br/> [String](String.md) | The device used to collect an environmental sample | direct |
| [sample_collection_method](sample_collection_method.md) | 0..1 <br/> [String](String.md) | The method used to collect an environmental sample | direct |
| [wind_direction](wind_direction.md) | 0..1 <br/> [CardinalDirectionEnum](CardinalDirectionEnum.md) | Direction of the wind on the day of sampling | direct |
| [weather](weather.md) | 0..1 <br/> [String](String.md) | The state of the atmosphere at a given time and place with respect to variabl... | direct |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [project](project.md) | 0..1 <br/> [Integer](Integer.md) | Identifier for the user project associated with the entity or activity | [SamplingActivity](SamplingActivity.md) |
| [emsl_activity](emsl_activity.md) | 0..1 <br/> [String](String.md) | Nullable string linking a Sample or SamplingActivity to a named EMSL activity... | [SamplingActivity](SamplingActivity.md) |
| [collection_date](collection_date.md) | 0..1 <br/> [Date](Date.md) | 'The date of sampling as an instance | [SamplingActivity](SamplingActivity.md) |
| [shipped_sample_size](shipped_sample_size.md) | 0..1 <br/> [String](String.md) | Total amount of sample sent to EMSL | [SamplingActivity](SamplingActivity.md) |
| [sampled_at_site](sampled_at_site.md) | 0..1 <br/> [Site](Site.md) | Reference to the site where the sample was collected | [SamplingActivity](SamplingActivity.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:SoilSamplingActivity |
| native | basalt_schema:SoilSamplingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SoilSamplingActivity
description: Collection of soil samples from the environment.
title: Soil Sampling Activity
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: SamplingActivity
slots:
- name
- description
- collection_time
- infiltration_1
- infiltration_2
- infiltration_notes
- sample_collected
- sample_collection_dev
- sample_collection_method
- wind_direction
- weather
attributes:
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema/sample-classes
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
name: SoilSamplingActivity
description: Collection of soil samples from the environment.
title: Soil Sampling Activity
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: SamplingActivity
attributes:
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema/sample-classes
    identifier: true
    alias: id
    owner: SoilSamplingActivity
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
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: SoilSamplingActivity
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
    owner: SoilSamplingActivity
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
  collection_time:
    name: collection_time
    description: 'The time of sampling as an instance (single point). Required format:
      HH:MM:SS in 24-hour time format. Don''t forget the second! (Unit: hh:mm:ss or
      HH:MM:SS)'
    title: collection time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: collection_time
    owner: SoilSamplingActivity
    domain_of:
    - AerosolSamplingActivity
    - CultureEnvironmentalSamplingActivity
    - FieldDeployedTerraformSamplingActivity
    - MixedCultureSamplingActivity
    - MonetSoilSamplingActivity
    - OtherUndescribedSamplingActivity
    - PlantSamplingActivity
    - PureCultureSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    - TerraformSamplingActivity
    - WaterSamplingActivity
    range: string
    pattern: ^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$
  infiltration_1:
    name: infiltration_1
    description: 'Amount of time it takes to accomplish the first infiltration activity.
      If infiltration time was started and unsuccessful enter ''failed'' if infiltration
      time was not attempted enter ''did not collect''. Units and format of mm:ss
      required. (Example: 15:20 mm:ss)'
    title: first infiltration time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: infiltration_1
    owner: SoilSamplingActivity
    domain_of:
    - MonetSoilSamplingActivity
    - SoilSamplingActivity
    range: string
    pattern: ^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)$
  infiltration_2:
    name: infiltration_2
    description: 'Amount of time it takes to accomplish the second infiltration activity.
      If infiltration time was started and unsuccessful enter ''failed'' if infiltration
      time was not attempted enter ''did not collect''. Units and format of mm:ss
      required. (Example: 15:20 mm:ss)'
    title: second infiltration time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: infiltration_2
    owner: SoilSamplingActivity
    domain_of:
    - MonetSoilSamplingActivity
    - SoilSamplingActivity
    range: string
    pattern: ^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)
  infiltration_notes:
    name: infiltration_notes
    description: Provide any details, issues, or context needed to understand the
      infiltration activity
    title: infiltration notes
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: infiltration_notes
    owner: SoilSamplingActivity
    domain_of:
    - MonetSoilSamplingActivity
    - SoilSamplingActivity
    range: string
  sample_collected:
    name: sample_collected
    description: This refers to the TOTAL amount of sample collected from the experiment.
      NOT the amount sent to EMSL or collected for a specific analysis. Provide value
      and unit, any unit is valid
    title: sample collected
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sample_collected
    owner: SoilSamplingActivity
    domain_of:
    - AerosolSamplingActivity
    - CommerciallyPurchasedSamplingActivity
    - CultureEnvironmentalSamplingActivity
    - FieldDeployedTerraformSamplingActivity
    - MixedCultureSamplingActivity
    - OtherUndescribedSamplingActivity
    - PlantSamplingActivity
    - PureCultureSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    - SynthesizedMaterialSamplingActivity
    - TerraformSamplingActivity
    - WaterSamplingActivity
    range: string
    pattern: ^\d+(\.\d+)?\s*[\w\s/]+$
  sample_collection_dev:
    name: sample_collection_dev
    description: The device used to collect an environmental sample. Include dimensions
      of device if applicable
    title: sample collection device
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sample_collection_dev
    owner: SoilSamplingActivity
    domain_of:
    - AerosolSamplingActivity
    - CommerciallyPurchasedSamplingActivity
    - CultureEnvironmentalSamplingActivity
    - MixedCultureSamplingActivity
    - MonetSoilSamplingActivity
    - OtherUndescribedSamplingActivity
    - PlantSamplingActivity
    - PureCultureSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    - SynthesizedMaterialSamplingActivity
    - WaterSamplingActivity
    range: string
  sample_collection_method:
    name: sample_collection_method
    description: The method used to collect an environmental sample. This can be a
      citation or description.
    title: sample collection method
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sample_collection_method
    owner: SoilSamplingActivity
    domain_of:
    - CultureEnvironmentalSamplingActivity
    - FieldDeployedTerraformSamplingActivity
    - MixedCultureSamplingActivity
    - OtherUndescribedSamplingActivity
    - PlantSamplingActivity
    - PureCultureSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    - TerraformSamplingActivity
    - WaterSamplingActivity
    range: string
  wind_direction:
    name: wind_direction
    description: Direction of the wind on the day of sampling. Collected via anemometer.
      Provide cardinal direction.
    title: wind direction
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: wind_direction
    owner: SoilSamplingActivity
    domain_of:
    - AerosolSamplingActivity
    - OtherUndescribedSamplingActivity
    - SoilSamplingActivity
    range: CardinalDirectionEnum
    required: false
  weather:
    name: weather
    description: The state of the atmosphere at a given time and place with respect
      to variables such as temperature, moisture, wind velocity, and barometric pressure.
    title: weather
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: weather
    owner: SoilSamplingActivity
    domain_of:
    - MonetSoilSamplingActivity
    - PlantSamplingActivity
    - SedimentSamplingActivity
    - SoilSamplingActivity
    range: string
  project:
    name: project
    description: 'Identifier for the user project associated with the entity or activity. '
    title: Project
    todos:
    - should this be an ID? CURIE can use the one NMDC has https://bioregistry.io/reference/emsl.project:60141
      where emsl.project is the CURIE prefix
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: SoilSamplingActivity
    domain_of:
    - DataProduct
    - AerosolArmSample
    - AerosolSample
    - CommerciallyPurchasedSample
    - CultureEnvironmentalSample
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
    - SamplingActivity
    range: integer
  emsl_activity:
    name: emsl_activity
    description: 'Nullable string linking a Sample or SamplingActivity to a named
      EMSL activity or

      campaign (e.g., ''AMP2'', ''MONet_FY26''). Optional for historical records

      predating activity tracking.'
    todos:
    - Is sampling activity where we want to capture this?
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: emsl_activity
    owner: SoilSamplingActivity
    domain_of:
    - Sample
    - SamplingActivity
    range: string
    required: false
  collection_date:
    name: collection_date
    description: '''The date of sampling as an instance. Format: YYYY-MM-DD. Also
      valid if entire collection date is unknown is just year (YYYY) or just year
      and month

      (YYYY-MM)'''
    title: collection date
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: collection_date
    owner: SoilSamplingActivity
    domain_of:
    - AMP2UserSample
    - SamplingActivity
    range: date
    pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$
  shipped_sample_size:
    name: shipped_sample_size
    description: Total amount of sample sent to EMSL. Must include units.
    title: shipped sample size
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: shipped_sample_size
    owner: SoilSamplingActivity
    domain_of:
    - AMP2UserSample
    - SamplingActivity
    range: string
    pattern: ^\d+(\.\d+)?\s*[\w\s/]+$
  sampled_at_site:
    name: sampled_at_site
    description: Reference to the site where the sample was collected. This is a FK
      to the Site class, which contains detailed metadata about the sampling location.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sampled_at_site
    owner: SoilSamplingActivity
    domain_of:
    - SamplingActivity
    range: Site

```
</details>