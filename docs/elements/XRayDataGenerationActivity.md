

# Class: XRayDataGenerationActivity 


_Abstract base class for X-ray analytical methods including XRF (elemental)_

_and XRD (mineralogical) analysis. Inherits acquisition_time, instrument_id,_

_protocol_url, analyte_id, and other core metadata from DataGenerationActivity._

__

_Concrete subclasses define method-specific measurement parameters._

_Future X-ray methods (e.g., XCT) can extend this class._

__

_Shared patterns:_

_  - Direct instrument output (no computational workflow) is typical for XRF_

_  - XRD may optionally link to DataProcessingActivity for Rietveld refinement_

_  - protocol_url should link to vendor SOP or EMSL internal protocol documentation_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [analysis_api_schema:XRayDataGenerationActivity](https://w3id.org/MONet/analysis-api-schema/XRayDataGenerationActivity)





```mermaid
 classDiagram
    class XRayDataGenerationActivity
    click XRayDataGenerationActivity href "../XRayDataGenerationActivity/"
      DataGenerationActivity <|-- XRayDataGenerationActivity
        click DataGenerationActivity href "../DataGenerationActivity/"
      

      XRayDataGenerationActivity <|-- XRFDataGenerationActivity
        click XRFDataGenerationActivity href "../XRFDataGenerationActivity/"
      XRayDataGenerationActivity <|-- XRDDataGenerationActivity
        click XRDDataGenerationActivity href "../XRDDataGenerationActivity/"
      

      XRayDataGenerationActivity : acquisition_end_time
        
      XRayDataGenerationActivity : acquisition_start_time
        
      XRayDataGenerationActivity : analyte_id
        
          
    
        
        
        XRayDataGenerationActivity --> "0..1" ProcessedSample : analyte_id
        click ProcessedSample href "../ProcessedSample/"
    

        
      XRayDataGenerationActivity : description
        
      XRayDataGenerationActivity : id
        
      XRayDataGenerationActivity : instrument_operator_id
        
          
    
        
        
        XRayDataGenerationActivity --> "0..1" PersonValue : instrument_operator_id
        click PersonValue href "../PersonValue/"
    

        
      XRayDataGenerationActivity : instrument_used
        
          
    
        
        
        XRayDataGenerationActivity --> "0..1" Instrument : instrument_used
        click Instrument href "../Instrument/"
    

        
      XRayDataGenerationActivity : name
        
      XRayDataGenerationActivity : protocol_url
        
      XRayDataGenerationActivity : protocol_version
        
      XRayDataGenerationActivity : sequence_order
        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * **XRayDataGenerationActivity**
        * [XRFDataGenerationActivity](XRFDataGenerationActivity.md)
        * [XRDDataGenerationActivity](XRDDataGenerationActivity.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sequence_order](sequence_order.md) | 0..1 <br/> [Integer](Integer.md) | Integer ordering within a temporal series for the same analyte | [DataGenerationActivity](DataGenerationActivity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_url](protocol_url.md) | 0..1 <br/> [String](String.md) | URL pointing to the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [protocol_version](protocol_version.md) | 0..1 <br/> [String](String.md) | Version of the protocol used in the activity, if applicable | [DataGenerationActivity](DataGenerationActivity.md) |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | [DataGenerationActivity](DataGenerationActivity.md) |
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
| self | analysis_api_schema:XRayDataGenerationActivity |
| native | analysis_api_schema:XRayDataGenerationActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XRayDataGenerationActivity
description: "Abstract base class for X-ray analytical methods including XRF (elemental)\n\
  and XRD (mineralogical) analysis. Inherits acquisition_time, instrument_id,\nprotocol_url,\
  \ analyte_id, and other core metadata from DataGenerationActivity.\n\nConcrete subclasses\
  \ define method-specific measurement parameters.\nFuture X-ray methods (e.g., XCT)\
  \ can extend this class.\n\nShared patterns:\n  - Direct instrument output (no computational\
  \ workflow) is typical for XRF\n  - XRD may optionally link to DataProcessingActivity\
  \ for Rietveld refinement\n  - protocol_url should link to vendor SOP or EMSL internal\
  \ protocol documentation"
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: DataGenerationActivity
abstract: true

```
</details>

### Induced

<details>
```yaml
name: XRayDataGenerationActivity
description: "Abstract base class for X-ray analytical methods including XRF (elemental)\n\
  and XRD (mineralogical) analysis. Inherits acquisition_time, instrument_id,\nprotocol_url,\
  \ analyte_id, and other core metadata from DataGenerationActivity.\n\nConcrete subclasses\
  \ define method-specific measurement parameters.\nFuture X-ray methods (e.g., XCT)\
  \ can extend this class.\n\nShared patterns:\n  - Direct instrument output (no computational\
  \ workflow) is typical for XRF\n  - XRD may optionally link to DataProcessingActivity\
  \ for Rietveld refinement\n  - protocol_url should link to vendor SOP or EMSL internal\
  \ protocol documentation"
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: DataGenerationActivity
abstract: true
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
    owner: XRayDataGenerationActivity
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
    owner: XRayDataGenerationActivity
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
    owner: XRayDataGenerationActivity
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
    owner: XRayDataGenerationActivity
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
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    identifier: true
    alias: id
    owner: XRayDataGenerationActivity
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
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: acquisition_start_time
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: acquisition_end_time
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: instrument_used
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: instrument_operator_id
    owner: XRayDataGenerationActivity
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>