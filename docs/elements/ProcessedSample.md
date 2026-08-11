

# Class: Processed Sample (ProcessedSample) 


_A sample that has undergone processing or analysis. Processed Sample entities are derived from Activities. The upstream SampleProcessing that produced this ProcessedSample is referenced via sampled_during._





URI: [basalt_schema:ProcessedSample](https://EMSL-Computing.github.io/basalt-schema/ProcessedSample)





```mermaid
 classDiagram
    class ProcessedSample
    click ProcessedSample href "../ProcessedSample/"
      Sample <|-- ProcessedSample
        click Sample href "../Sample/"
      

      ProcessedSample <|-- CoreSection
        click CoreSection href "../CoreSection/"
      

      ProcessedSample : concentration_ug_per_uL
        
      ProcessedSample : description
        
      ProcessedSample : emsl_activity
        
      ProcessedSample : id
        
      ProcessedSample : label_text
        
      ProcessedSample : lims_barcode
        
      ProcessedSample : name
        
      ProcessedSample : replicate
        
      ProcessedSample : sampled_during
        
          
    
        
        
        ProcessedSample --> "0..1" SampleProcessing : sampled_during
        click SampleProcessing href "../SampleProcessing/"
    

        
      ProcessedSample : sampled_portion
        
          
    
        
        
        ProcessedSample --> "0..1" SamplePortionEnum : sampled_portion
        click SamplePortionEnum href "../SamplePortionEnum/"
    

        
      ProcessedSample : storage_location
        
      ProcessedSample : total_amount_ug
        
      ProcessedSample : volume_uL
        
      
```





## Inheritance
* [Sample](Sample.md)
    * **ProcessedSample**
        * [CoreSection](CoreSection.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [storage_location](storage_location.md) | 0..1 <br/> [String](String.md) | The physical or digital location where the processed sample is stored (e | direct |
| [label_text](label_text.md) | 0..1 <br/> [String](String.md) | The label on the stored processed sample, if applicable (e | direct |
| [concentration_ug_per_uL](concentration_ug_per_uL.md) | 0..1 <br/> [Float](Float.md) | Concentration of the substance in micrograms per microliter | direct |
| [total_amount_ug](total_amount_ug.md) | 0..1 <br/> [Float](Float.md) | Total amount of analyte in micrograms | direct |
| [volume_uL](volume_uL.md) | 0..1 <br/> [Float](Float.md) | Volume of the entity in microliters | direct |
| [sampled_portion](sampled_portion.md) | 0..1 <br/> [SamplePortionEnum](SamplePortionEnum.md) | The portion of the original sample used in creating this processed sample (e | direct |
| [sampled_during](sampled_during.md) | 0..1 <br/> [SampleProcessing](SampleProcessing.md) | A reference to the sample processing activity (generally lab work) that gener... | direct |
| [replicate](replicate.md) | 0..1 <br/> [Integer](Integer.md) | The TECHNICAL replicate number of the processed sample, if applicable | direct |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [Sample](Sample.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [Sample](Sample.md) |
| [emsl_activity](emsl_activity.md) | 0..1 <br/> [String](String.md) | Nullable string linking a Sample or SamplingActivity to a named EMSL activity... | [Sample](Sample.md) |
| [lims_barcode](lims_barcode.md) | 0..1 <br/> [String](String.md) | LIMS barcode identifier | [Sample](Sample.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataGenerationActivity](DataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | [media_ref](media_ref.md) | range | [ProcessedSample](ProcessedSample.md) |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |
| [AMP2WellMetadata](AMP2WellMetadata.md) | [media_ref](media_ref.md) | range | [ProcessedSample](ProcessedSample.md) |
| [NucleotideSequencing](NucleotideSequencing.md) | [analyte_id](analyte_id.md) | range | [ProcessedSample](ProcessedSample.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ProcessedSample |
| native | basalt_schema:ProcessedSample |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessedSample
description: A sample that has undergone processing or analysis. Processed Sample
  entities are derived from Activities. The upstream SampleProcessing that produced
  this ProcessedSample is referenced via sampled_during.
title: Processed Sample
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Sample
slots:
- storage_location
- label_text
- concentration_ug_per_uL
- total_amount_ug
- volume_uL
- sampled_portion
- sampled_during
- replicate
slot_usage:
  replicate:
    name: replicate
    description: The TECHNICAL replicate number of the processed sample, if applicable.
  sampled_during:
    name: sampled_during
    description: A reference to the sample processing activity (generally lab work)
      that generated this processed_sample.
    range: SampleProcessing
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema/sample-classes
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
name: ProcessedSample
description: A sample that has undergone processing or analysis. Processed Sample
  entities are derived from Activities. The upstream SampleProcessing that produced
  this ProcessedSample is referenced via sampled_during.
title: Processed Sample
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Sample
slot_usage:
  replicate:
    name: replicate
    description: The TECHNICAL replicate number of the processed sample, if applicable.
  sampled_during:
    name: sampled_during
    description: A reference to the sample processing activity (generally lab work)
      that generated this processed_sample.
    range: SampleProcessing
attributes:
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema/sample-classes
    identifier: true
    alias: id
    owner: ProcessedSample
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
  storage_location:
    name: storage_location
    description: The physical or digital location where the processed sample is stored
      (e.g., freezer location, database ID).
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: storage_location
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: string
  label_text:
    name: label_text
    description: The label on the stored processed sample, if applicable (e.g., "f01").
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: label_text
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: string
  concentration_ug_per_uL:
    name: concentration_ug_per_uL
    description: Concentration of the substance in micrograms per microliter.
    title: concentration (ug/uL)
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: concentration_ug_per_uL
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: float
  total_amount_ug:
    name: total_amount_ug
    description: Total amount of analyte in micrograms
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: total_amount_ug
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: float
  volume_uL:
    name: volume_uL
    description: Volume of the entity in microliters
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: volume_uL
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: float
  sampled_portion:
    name: sampled_portion
    description: The portion of the original sample used in creating this processed
      sample (e.g., "interlayer", "supernatant", "pellet").
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sampled_portion
    owner: ProcessedSample
    domain_of:
    - ProcessedSample
    range: SamplePortionEnum
  sampled_during:
    name: sampled_during
    description: A reference to the sample processing activity (generally lab work)
      that generated this processed_sample.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sampled_during
    owner: ProcessedSample
    domain_of:
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
    - ProcessedSample
    range: SampleProcessing
  replicate:
    name: replicate
    description: The TECHNICAL replicate number of the processed sample, if applicable.
    todos:
    - reconcile replicate modelling
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: replicate
    owner: ProcessedSample
    domain_of:
    - MAOMProduct
    - MicrobialBiomassProduct
    - NitrogenAnalysisProduct
    - PhosphorusAnalysisProduct
    - WEOMProduct
    - ProcessedSample
    range: integer
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: name
    owner: ProcessedSample
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: description
    owner: ProcessedSample
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
  emsl_activity:
    name: emsl_activity
    description: 'Nullable string linking a Sample or SamplingActivity to a named
      EMSL activity or

      campaign (e.g., ''AMP2'', ''MONet_FY26''). Optional for historical records

      predating activity tracking.'
    todos:
    - Is sampling activity where we want to capture this?
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: emsl_activity
    owner: ProcessedSample
    domain_of:
    - Sample
    - SamplingActivity
    range: string
    required: false
  lims_barcode:
    name: lims_barcode
    description: LIMS barcode identifier
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: lims_barcode
    owner: ProcessedSample
    domain_of:
    - ProcessedData
    - Sample
    range: string
    required: false

```
</details>