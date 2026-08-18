

# Class: NucleotideSequencing 


_A lab activity in which DNA or RNA that was extracted from a sample is sequenced._





URI: [basalt_schema:NucleotideSequencing](https://emsl-computing.github.io/BASALT-Schema/elements/NucleotideSequencing)





```mermaid
 classDiagram
    class NucleotideSequencing
    click NucleotideSequencing href "../NucleotideSequencing/"
      DataGenerationActivity <|-- NucleotideSequencing
        click DataGenerationActivity href "../DataGenerationActivity/"
      
      NucleotideSequencing : acquisition_end_time
        
      NucleotideSequencing : acquisition_start_time
        
      NucleotideSequencing : analyte_id
        
          
    
        
        
        NucleotideSequencing --> "0..1" ProcessedSample : analyte_id
        click ProcessedSample href "../ProcessedSample/"
    

        
      NucleotideSequencing : description
        
      NucleotideSequencing : external_identifiers
        
      NucleotideSequencing : id
        
      NucleotideSequencing : instrument_operator_id
        
          
    
        
        
        NucleotideSequencing --> "0..1" PersonValue : instrument_operator_id
        click PersonValue href "../PersonValue/"
    

        
      NucleotideSequencing : instrument_used
        
          
    
        
        
        NucleotideSequencing --> "0..1" Instrument : instrument_used
        click Instrument href "../Instrument/"
    

        
      NucleotideSequencing : name
        
      NucleotideSequencing : nucleotide_sequencing_category
        
          
    
        
        
        NucleotideSequencing --> "0..1" NucleotideSequencingEnum : nucleotide_sequencing_category
        click NucleotideSequencingEnum href "../NucleotideSequencingEnum/"
    

        
      NucleotideSequencing : protocol_url
        
      NucleotideSequencing : protocol_version
        
      NucleotideSequencing : sequence_order
        
      
```





## Inheritance
* [DataGenerationActivity](DataGenerationActivity.md)
    * **NucleotideSequencing**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [nucleotide_sequencing_category](nucleotide_sequencing_category.md) | 0..1 <br/> [NucleotideSequencingEnum](NucleotideSequencingEnum.md) | The category of nucleotide sequencing performed (e | direct |
| [external_identifiers](external_identifiers.md) | * <br/> [Uriorcurie](Uriorcurie.md) | List of external identifiers (e | direct |
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





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NucleotideSequencingInstrumentData](NucleotideSequencingInstrumentData.md) | [produced_by_sequencing_activity](produced_by_sequencing_activity.md) | range | [NucleotideSequencing](NucleotideSequencing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:NucleotideSequencing |
| native | basalt_schema:NucleotideSequencing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NucleotideSequencing
description: A lab activity in which DNA or RNA that was extracted from a sample is
  sequenced.
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
slots:
- nucleotide_sequencing_category
- external_identifiers
slot_usage:
  external_identifiers:
    name: external_identifiers
    description: List of external identifiers (e.g., GOLD sequencing project, NCBI
      BioProject) associated with this sequencing activity.

```
</details>

### Induced

<details>
```yaml
name: NucleotideSequencing
description: A lab activity in which DNA or RNA that was extracted from a sample is
  sequenced.
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataGenerationActivity
slot_usage:
  external_identifiers:
    name: external_identifiers
    description: List of external identifiers (e.g., GOLD sequencing project, NCBI
      BioProject) associated with this sequencing activity.
attributes:
  nucleotide_sequencing_category:
    name: nucleotide_sequencing_category
    description: The category of nucleotide sequencing performed (e.g., amplicon,
      shotgun).
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: nucleotide_sequencing_category
    owner: NucleotideSequencing
    domain_of:
    - NucleotideSequencing
    range: NucleotideSequencingEnum
  external_identifiers:
    name: external_identifiers
    description: List of external identifiers (e.g., GOLD sequencing project, NCBI
      BioProject) associated with this sequencing activity.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: external_identifiers
    owner: NucleotideSequencing
    domain_of:
    - NucleotideSequencing
    - AerosolArmSample
    - AerosolSample
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
    - Study
    range: uriorcurie
    multivalued: true
  sequence_order:
    name: sequence_order
    description: "Integer ordering within a temporal series for the same analyte.\n\
      Lower = earlier in series. Use when acquisition_time alone is insufficient.\n\
      \nDDL: ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order\
      \ INTEGER;"
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: sequence_order
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: integer
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: name
    owner: NucleotideSequencing
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
    owner: NucleotideSequencing
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
  protocol_url:
    name: protocol_url
    description: URL pointing to the protocol used in the activity, if applicable.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_url
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  protocol_version:
    name: protocol_version
    description: Version of the protocol used in the activity, if applicable.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: protocol_version
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    - SampleProcessing
    range: string
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: NucleotideSequencing
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
  analyte_id:
    name: analyte_id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: analyte_id
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: ProcessedSample
  acquisition_start_time:
    name: acquisition_start_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_start_time
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  acquisition_end_time:
    name: acquisition_end_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: acquisition_end_time
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: datetime
    required: true
  instrument_used:
    name: instrument_used
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_used
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: Instrument
  instrument_operator_id:
    name: instrument_operator_id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: instrument_operator_id
    owner: NucleotideSequencing
    domain_of:
    - DataGenerationActivity
    range: PersonValue

```
</details>