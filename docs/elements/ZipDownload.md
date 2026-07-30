

# Class: ZipDownload 


_A zip download record, capturing the details of a zip file download event._





URI: [analysis_api_schema:ZipDownload](https://w3id.org/MONet/analysis-api-schema/ZipDownload)





```mermaid
 classDiagram
    class ZipDownload
    click ZipDownload href "../ZipDownload/"
      ZipDownload : files
        
      ZipDownload : id
        
      ZipDownload : packages
        
      ZipDownload : time
        
      ZipDownload : user
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [time](time.md) | 1 <br/> [Datetime](Datetime.md) |  | direct |
| [user](user.md) | 1 <br/> [String](String.md) |  | direct |
| [files](files.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [packages](packages.md) | 0..1 <br/> [String](String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ZipDownload |
| native | analysis_api_schema:ZipDownload |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: zipDownload
description: A zip download record, capturing the details of a zip file download event.
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
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
  time:
    name: time
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    domain_of:
    - zipDownload
    range: datetime
    required: true
  user:
    name: user
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    domain_of:
    - zipDownload
    range: string
    required: true
  files:
    name: files
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    domain_of:
    - zipDownload
    range: integer
    required: true
  packages:
    name: packages
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    domain_of:
    - zipDownload
    range: string

```
</details>

### Induced

<details>
```yaml
name: zipDownload
description: A zip download record, capturing the details of a zip file download event.
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    identifier: true
    alias: id
    owner: zipDownload
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
  time:
    name: time
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    alias: time
    owner: zipDownload
    domain_of:
    - zipDownload
    range: datetime
    required: true
  user:
    name: user
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    alias: user
    owner: zipDownload
    domain_of:
    - zipDownload
    range: string
    required: true
  files:
    name: files
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    alias: files
    owner: zipDownload
    domain_of:
    - zipDownload
    range: integer
    required: true
  packages:
    name: packages
    from_schema: https://w3id.org/MONet/analysis-api-schema/zip_download
    rank: 1000
    alias: packages
    owner: zipDownload
    domain_of:
    - zipDownload
    range: string

```
</details>