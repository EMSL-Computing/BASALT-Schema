

# Class: ControlledTermValue 



URI: [analysis_api_schema:ControlledTermValue](https://w3id.org/MONet/analysis-api-schema/ControlledTermValue)





```mermaid
 classDiagram
    class ControlledTermValue
    click ControlledTermValue href "../ControlledTermValue/"
      ControlledTermValue : controlled_term_provider
        
      ControlledTermValue : description
        
      ControlledTermValue : has_raw_value
        
      ControlledTermValue : id
        
      ControlledTermValue : term
        
      ControlledTermValue : term_id
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | direct |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [has_raw_value](has_raw_value.md) | 0..1 <br/> [String](String.md) |  | direct |
| [term](term.md) | 0..1 <br/> [String](String.md) |  | direct |
| [term_id](term_id.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | pointer to an ontology class | direct |
| [controlled_term_provider](controlled_term_provider.md) | 0..1 <br/> [String](String.md) | name of ontology or other controlled term provider | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetagenomicsProduct](MetagenomicsProduct.md) | [provider_name](provider_name.md) | range | [ControlledTermValue](ControlledTermValue.md) |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | [provider_name](provider_name.md) | range | [ControlledTermValue](ControlledTermValue.md) |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | [provider_name](provider_name.md) | range | [ControlledTermValue](ControlledTermValue.md) |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | [provider_name](provider_name.md) | range | [ControlledTermValue](ControlledTermValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ControlledTermValue |
| native | analysis_api_schema:ControlledTermValue |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ControlledTermValue
from_schema: https://w3id.org/MONet/analysis-api-schema
slots:
- description
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
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
    range: string
    required: true
  has_raw_value:
    name: has_raw_value
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    domain_of:
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - QuantityValue
    - ConditioningValue
    range: string
  term:
    name: term
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    domain_of:
    - ControlledTermValue
    range: string
  term_id:
    name: term_id
    description: pointer to an ontology class
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    domain_of:
    - ControlledTermValue
    range: uriorcurie
  controlled_term_provider:
    name: controlled_term_provider
    description: name of ontology or other controlled term provider
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    domain_of:
    - ControlledTermValue
    range: string

```
</details>

### Induced

<details>
```yaml
name: ControlledTermValue
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    identifier: true
    alias: id
    owner: ControlledTermValue
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
    range: string
    required: true
  has_raw_value:
    name: has_raw_value
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    alias: has_raw_value
    owner: ControlledTermValue
    domain_of:
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - QuantityValue
    - ConditioningValue
    range: string
  term:
    name: term
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    alias: term
    owner: ControlledTermValue
    domain_of:
    - ControlledTermValue
    range: string
  term_id:
    name: term_id
    description: pointer to an ontology class
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    alias: term_id
    owner: ControlledTermValue
    domain_of:
    - ControlledTermValue
    range: uriorcurie
  controlled_term_provider:
    name: controlled_term_provider
    description: name of ontology or other controlled term provider
    from_schema: https://w3id.org/MONet/analysis-api-schema/value-tables
    rank: 1000
    alias: controlled_term_provider
    owner: ControlledTermValue
    domain_of:
    - ControlledTermValue
    range: string
  description:
    name: description
    description: Human-readable description for the entity or activity
    title: description
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: description
    owner: ControlledTermValue
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
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - biological_entity
    - Study
    - TimestampValue
    - TextValue
    - SoftwareControlledTermValue
    - ControlledTermValue
    - QuantityValue
    range: string

```
</details>