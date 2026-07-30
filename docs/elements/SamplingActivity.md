

# Class: SamplingActivity 


_An activity that involves the collection of a sample. This class serves as an abstract class to relate subclasses of sampling activities. Samples reference their parent sampling activity via the 'sampled_during' slot._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [analysis_api_schema:SamplingActivity](https://w3id.org/MONet/analysis-api-schema/SamplingActivity)





```mermaid
 classDiagram
    class SamplingActivity
    click SamplingActivity href "../SamplingActivity/"
      SamplingActivity <|-- AerosolArmSamplingActivity
        click AerosolArmSamplingActivity href "../AerosolArmSamplingActivity/"
      SamplingActivity <|-- AerosolSamplingActivity
        click AerosolSamplingActivity href "../AerosolSamplingActivity/"
      SamplingActivity <|-- CommerciallyPurchasedSamplingActivity
        click CommerciallyPurchasedSamplingActivity href "../CommerciallyPurchasedSamplingActivity/"
      SamplingActivity <|-- CultureEnvironmentalSamplingActivity
        click CultureEnvironmentalSamplingActivity href "../CultureEnvironmentalSamplingActivity/"
      SamplingActivity <|-- EngineeredStrainSamplingActivity
        click EngineeredStrainSamplingActivity href "../EngineeredStrainSamplingActivity/"
      SamplingActivity <|-- FieldDeployedTerraformSamplingActivity
        click FieldDeployedTerraformSamplingActivity href "../FieldDeployedTerraformSamplingActivity/"
      SamplingActivity <|-- MixedCultureSamplingActivity
        click MixedCultureSamplingActivity href "../MixedCultureSamplingActivity/"
      SamplingActivity <|-- MonetSoilSamplingActivity
        click MonetSoilSamplingActivity href "../MonetSoilSamplingActivity/"
      SamplingActivity <|-- OtherUndescribedSamplingActivity
        click OtherUndescribedSamplingActivity href "../OtherUndescribedSamplingActivity/"
      SamplingActivity <|-- PlantSamplingActivity
        click PlantSamplingActivity href "../PlantSamplingActivity/"
      SamplingActivity <|-- PureCultureSamplingActivity
        click PureCultureSamplingActivity href "../PureCultureSamplingActivity/"
      SamplingActivity <|-- SedimentSamplingActivity
        click SedimentSamplingActivity href "../SedimentSamplingActivity/"
      SamplingActivity <|-- SoilSamplingActivity
        click SoilSamplingActivity href "../SoilSamplingActivity/"
      SamplingActivity <|-- SynthesizedMaterialSamplingActivity
        click SynthesizedMaterialSamplingActivity href "../SynthesizedMaterialSamplingActivity/"
      SamplingActivity <|-- TerraformSamplingActivity
        click TerraformSamplingActivity href "../TerraformSamplingActivity/"
      SamplingActivity <|-- WaterSamplingActivity
        click WaterSamplingActivity href "../WaterSamplingActivity/"
      
      SamplingActivity : collection_date
        
      SamplingActivity : description
        
      SamplingActivity : emsl_activity
        
      SamplingActivity : id
        
      SamplingActivity : name
        
      SamplingActivity : project
        
      SamplingActivity : sampled_at_site
        
          
    
        
        
        SamplingActivity --> "0..1" Site : sampled_at_site
        click Site href "../Site/"
    

        
      SamplingActivity : shipped_sample_size
        
      
```





## Inheritance
* **SamplingActivity**
    * [AerosolArmSamplingActivity](AerosolArmSamplingActivity.md)
    * [AerosolSamplingActivity](AerosolSamplingActivity.md)
    * [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md)
    * [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md)
    * [EngineeredStrainSamplingActivity](EngineeredStrainSamplingActivity.md)
    * [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md)
    * [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md)
    * [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md)
    * [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md)
    * [PlantSamplingActivity](PlantSamplingActivity.md)
    * [PureCultureSamplingActivity](PureCultureSamplingActivity.md)
    * [SedimentSamplingActivity](SedimentSamplingActivity.md)
    * [SoilSamplingActivity](SoilSamplingActivity.md)
    * [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md)
    * [TerraformSamplingActivity](TerraformSamplingActivity.md)
    * [WaterSamplingActivity](WaterSamplingActivity.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | direct |
| [project](project.md) | 0..1 <br/> [Integer](Integer.md) | Identifier for the user project associated with the entity or activity | direct |
| [emsl_activity](emsl_activity.md) | 0..1 <br/> [String](String.md) | Nullable string linking a Sample or SamplingActivity to a named EMSL activity... | direct |
| [collection_date](collection_date.md) | 0..1 <br/> [Date](Date.md) | 'The date of sampling as an instance | direct |
| [shipped_sample_size](shipped_sample_size.md) | 0..1 <br/> [String](String.md) | Total amount of sample sent to EMSL | direct |
| [sampled_at_site](sampled_at_site.md) | 0..1 <br/> [Site](Site.md) | Reference to the site where the sample was collected | direct |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SitePhoto](SitePhoto.md) | [photo_taken_during](photo_taken_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [AerosolArmSample](AerosolArmSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [AerosolSample](AerosolSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [MixedCultureSample](MixedCultureSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [MonetSoilSample](MonetSoilSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [OtherUndescribedSample](OtherUndescribedSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [PlantSample](PlantSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [PureCultureSample](PureCultureSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [SedimentSample](SedimentSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [SoilSample](SoilSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [TerraformSample](TerraformSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |
| [WaterSample](WaterSample.md) | [sampled_during](sampled_during.md) | range | [SamplingActivity](SamplingActivity.md) |










## TODOs

* is this for individual samples or can it be the activity of collecting multiple samples from one site? would need to change shipped_sample_size and storage_condt if so.
* does project number go here? how do we connect Sample/SamplingActivity to a project/Study?



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:SamplingActivity |
| native | analysis_api_schema:SamplingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SamplingActivity
description: An activity that involves the collection of a sample. This class serves
  as an abstract class to relate subclasses of sampling activities. Samples reference
  their parent sampling activity via the 'sampled_during' slot.
todos:
- is this for individual samples or can it be the activity of collecting multiple
  samples from one site? would need to change shipped_sample_size and storage_condt
  if so.
- does project number go here? how do we connect Sample/SamplingActivity to a project/Study?
from_schema: https://w3id.org/MONet/analysis-api-schema
abstract: true
slots:
- name
- description
- project
- emsl_activity
- collection_date
- shipped_sample_size
- sampled_at_site
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/sample-classes
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
name: SamplingActivity
description: An activity that involves the collection of a sample. This class serves
  as an abstract class to relate subclasses of sampling activities. Samples reference
  their parent sampling activity via the 'sampled_during' slot.
todos:
- is this for individual samples or can it be the activity of collecting multiple
  samples from one site? would need to change shipped_sample_size and storage_condt
  if so.
- does project number go here? how do we connect Sample/SamplingActivity to a project/Study?
from_schema: https://w3id.org/MONet/analysis-api-schema
abstract: true
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/sample-classes
    identifier: true
    alias: id
    owner: SamplingActivity
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: name
    owner: SamplingActivity
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: description
    owner: SamplingActivity
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
  project:
    name: project
    description: 'Identifier for the user project associated with the entity or activity. '
    title: Project
    todos:
    - should this be an ID? CURIE can use the one NMDC has https://bioregistry.io/reference/emsl.project:60141
      where emsl.project is the CURIE prefix
    from_schema: https://w3id.org/MONet/analysis-api-schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: SamplingActivity
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: emsl_activity
    owner: SamplingActivity
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
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: collection_date
    owner: SamplingActivity
    domain_of:
    - AMP2UserSample
    - SamplingActivity
    range: date
    pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$
  shipped_sample_size:
    name: shipped_sample_size
    description: Total amount of sample sent to EMSL. Must include units.
    title: shipped sample size
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: shipped_sample_size
    owner: SamplingActivity
    domain_of:
    - AMP2UserSample
    - SamplingActivity
    range: string
    pattern: ^\d+(\.\d+)?\s*[\w\s/]+$
  sampled_at_site:
    name: sampled_at_site
    description: Reference to the site where the sample was collected. This is a FK
      to the Site class, which contains detailed metadata about the sampling location.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: sampled_at_site
    owner: SamplingActivity
    domain_of:
    - SamplingActivity
    range: Site

```
</details>