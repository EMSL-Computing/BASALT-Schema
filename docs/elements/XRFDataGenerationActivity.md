

# Class: XRFDataGenerationActivity 


_X-ray Fluorescence (XRF) elemental analysis activity._

__

_XRF measures elemental composition by detecting characteristic X-ray emissions_

_from a sample bombarded with high-energy X-rays. Typical output: concentrations_

_of 10-30 elements per sample (Ni, Pb, As, Cr, Fe, Ca, K, etc.)._

__

_Data product: XRFElementalProduct (one row per element per sample)_

__

_Workflow pattern: Direct instrument output (no computational processing step)_

_  processedSample -> XRFDataGenerationActivity -> XRFElementalProduct (workflow_id = NULL)_

__

_Protocol information: Stored externally; link via protocol_url attribute._

_Example protocol parameters (stored in external SOP or DataProcessingActivity_

_if computational correction is needed):_

_  - Beam voltage (kV), beam current (mA)_

_  - Measurement duration (seconds)_

_  - Matrix correction method (fundamental parameters, empirical)_

_  - Calibration date_

_  - Operator ID_

__

_Required enum additions to enums.yaml:_

_  routemethod:_

_    xrf_analysis:  # Add to routemethod permissible_values_





URI: [analysis_api_schema:XRFDataGenerationActivity](https://w3id.org/MONet/analysis-api-schema/XRFDataGenerationActivity)






```mermaid
 classDiagram
    class XRFDataGenerationActivity
    click XRFDataGenerationActivity href "../XRFDataGenerationActivity"
      XRayDataGenerationActivity <|-- XRFDataGenerationActivity
        click XRayDataGenerationActivity href "../XRayDataGenerationActivity"
      
      XRFDataGenerationActivity : acquisition_end_time
        
      XRFDataGenerationActivity : acquisition_start_time
        
      XRFDataGenerationActivity : analyte_id
        
          
    
    
    
    
    XRFDataGenerationActivity --> "0..1" ProcessedSample : analyte_id
    click ProcessedSample href "../ProcessedSample"
    

        
      XRFDataGenerationActivity : description
        
      XRFDataGenerationActivity : id
        
          
    
    

        
      XRFDataGenerationActivity : instrument_operator_id
        
          
    
    
    
    
    XRFDataGenerationActivity --> "0..1" PersonValue : instrument_operator_id
    click PersonValue href "../PersonValue"
    

        
      XRFDataGenerationActivity : instrument_used
        
          
    
    
    
    
    XRFDataGenerationActivity --> "0..1" Instrument : instrument_used
    click Instrument href "../Instrument"
    

        
      XRFDataGenerationActivity : name
        
      XRFDataGenerationActivity : protocol_url
        
      XRFDataGenerationActivity : protocol_version
        
      XRFDataGenerationActivity : sequence_order
        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * [XRayDataGenerationActivity](XRayDataGenerationActivity.md)
        * **XRFDataGenerationActivity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sequence_order](sequence_order.md) | 0..1 <br/> [Integer](Integer.md) | Integer ordering within a temporal series for the same analyte | [DataGenerationActivity](DataGenerationActivity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_url](protocol_url.md) | 0..1 <br/> [String](String.md) | URL pointing to the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [id](id.md) | 1 <br/> uuid |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [analyte_id](analyte_id.md) | 0..1 <br/> [ProcessedSample](ProcessedSample.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [acquisition_start_time](acquisition_start_time.md) | 1 <br/> [Datetime](Datetime.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [acquisition_end_time](acquisition_end_time.md) | 1 <br/> [Datetime](Datetime.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [instrument_used](instrument_used.md) | 0..1 <br/> [Instrument](Instrument.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
| [instrument_operator_id](instrument_operator_id.md) | 0..1 <br/> [PersonValue](PersonValue.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:XRFDataGenerationActivity |
| native | analysis_api_schema:XRFDataGenerationActivity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XRFDataGenerationActivity
description: "X-ray Fluorescence (XRF) elemental analysis activity.\n\nXRF measures\
  \ elemental composition by detecting characteristic X-ray emissions\nfrom a sample\
  \ bombarded with high-energy X-rays. Typical output: concentrations\nof 10-30 elements\
  \ per sample (Ni, Pb, As, Cr, Fe, Ca, K, etc.).\n\nData product: XRFElementalProduct\
  \ (one row per element per sample)\n\nWorkflow pattern: Direct instrument output\
  \ (no computational processing step)\n  processedSample -> XRFDataGenerationActivity\
  \ -> XRFElementalProduct (workflow_id = NULL)\n\nProtocol information: Stored externally;\
  \ link via protocol_url attribute.\nExample protocol parameters (stored in external\
  \ SOP or DataProcessingActivity\nif computational correction is needed):\n  - Beam\
  \ voltage (kV), beam current (mA)\n  - Measurement duration (seconds)\n  - Matrix\
  \ correction method (fundamental parameters, empirical)\n  - Calibration date\n\
  \  - Operator ID\n\nRequired enum additions to enums.yaml:\n  routemethod:\n   \
  \ xrf_analysis:  # Add to routemethod permissible_values"
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: XRayDataGenerationActivity

```
</details>

### Induced

<details>
```yaml
name: XRFDataGenerationActivity
description: "X-ray Fluorescence (XRF) elemental analysis activity.\n\nXRF measures\
  \ elemental composition by detecting characteristic X-ray emissions\nfrom a sample\
  \ bombarded with high-energy X-rays. Typical output: concentrations\nof 10-30 elements\
  \ per sample (Ni, Pb, As, Cr, Fe, Ca, K, etc.).\n\nData product: XRFElementalProduct\
  \ (one row per element per sample)\n\nWorkflow pattern: Direct instrument output\
  \ (no computational processing step)\n  processedSample -> XRFDataGenerationActivity\
  \ -> XRFElementalProduct (workflow_id = NULL)\n\nProtocol information: Stored externally;\
  \ link via protocol_url attribute.\nExample protocol parameters (stored in external\
  \ SOP or DataProcessingActivity\nif computational correction is needed):\n  - Beam\
  \ voltage (kV), beam current (mA)\n  - Measurement duration (seconds)\n  - Matrix\
  \ correction method (fundamental parameters, empirical)\n  - Calibration date\n\
  \  - Operator ID\n\nRequired enum additions to enums.yaml:\n  routemethod:\n   \
  \ xrf_analysis:  # Add to routemethod permissible_values"
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: XRayDataGenerationActivity
attributes:
  sequence_order:
    name: sequence_order
    description: "Integer ordering within a temporal series for the same analyte.\n\
      Lower = earlier in series. Use when acquisition_time alone is insufficient.\n\
      \nDDL: ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order\
      \ INTEGER;"
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: sequence_order
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: integer
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: name
    owner: XRFDataGenerationActivity
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
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - biological_entity
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
    owner: XRFDataGenerationActivity
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
  protocol_url:
    name: protocol_url
    description: URL pointing to the protocol used in the activity, if applicable.
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: protocol_url
    owner: XRFDataGenerationActivity
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
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
    alias: id
    owner: XRFDataGenerationActivity
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
  analyte_id:
    name: analyte_id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: analyte_id
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: acquisition_start_time
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: acquisition_end_time
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: instrument_used
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: instrument_operator_id
    owner: XRFDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>