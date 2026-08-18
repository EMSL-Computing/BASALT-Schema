

# Class: MassSpectrometryDataProcessingActivity 


_Concrete mass spectrometry workflow run. Inherits all DataProcessingActivity_

_slots including used_software and version._





URI: [basalt_schema:MassSpectrometryDataProcessingActivity](https://emsl-computing.github.io/BASALT-Schema/elements/MassSpectrometryDataProcessingActivity)





```mermaid
 classDiagram
    class MassSpectrometryDataProcessingActivity
    click MassSpectrometryDataProcessingActivity href "../MassSpectrometryDataProcessingActivity/"
      DataProcessingActivity <|-- MassSpectrometryDataProcessingActivity
        click DataProcessingActivity href "../DataProcessingActivity/"
      
      MassSpectrometryDataProcessingActivity : description
        
      MassSpectrometryDataProcessingActivity : ended_at_time
        
      MassSpectrometryDataProcessingActivity : execution_resource
        
          
    
        
        
        MassSpectrometryDataProcessingActivity --> "0..1" ExecutionResourceEnum : execution_resource
        click ExecutionResourceEnum href "../ExecutionResourceEnum/"
    

        
      MassSpectrometryDataProcessingActivity : id
        
      MassSpectrometryDataProcessingActivity : lims_task_instance_id
        
      MassSpectrometryDataProcessingActivity : metaproteomics_analysis_category
        
          
    
        
        
        MassSpectrometryDataProcessingActivity --> "0..1" MetaproteomicsAnalysisCategoryEnum : metaproteomics_analysis_category
        click MetaproteomicsAnalysisCategoryEnum href "../MetaproteomicsAnalysisCategoryEnum/"
    

        
      MassSpectrometryDataProcessingActivity : parent_workflow_id
        
          
    
        
        
        MassSpectrometryDataProcessingActivity --> "0..1" DataProcessingActivity : parent_workflow_id
        click DataProcessingActivity href "../DataProcessingActivity/"
    

        
      MassSpectrometryDataProcessingActivity : software_poc
        
      MassSpectrometryDataProcessingActivity : software_url
        
      MassSpectrometryDataProcessingActivity : software_version
        
      MassSpectrometryDataProcessingActivity : started_at_time
        
      MassSpectrometryDataProcessingActivity : uses_calibration
        
          
    
        
        
        MassSpectrometryDataProcessingActivity --> "0..1" MassSpectrometryStandardRun : uses_calibration
        click MassSpectrometryStandardRun href "../MassSpectrometryStandardRun/"
    

        
      MassSpectrometryDataProcessingActivity : uses_raw_ms_data
        
          
    
        
        
        MassSpectrometryDataProcessingActivity --> "0..1" MassSpectrometryInstrumentData : uses_raw_ms_data
        click MassSpectrometryInstrumentData href "../MassSpectrometryInstrumentData/"
    

        
      MassSpectrometryDataProcessingActivity : workflow_steps
        
      
```





## Inheritance
* [DataProcessingActivity](DataProcessingActivity.md)
    * **MassSpectrometryDataProcessingActivity**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [uses_calibration](uses_calibration.md) | 0..1 <br/> [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) | Reference to the raw data file from the standard which was run with a batch o... | direct |
| [uses_raw_ms_data](uses_raw_ms_data.md) | 0..1 <br/> [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) | The raw data file, output by a mass spectrometer, that was analyzed in  this ... | direct |
| [lims_task_instance_id](lims_task_instance_id.md) | 0..1 <br/> [Integer](Integer.md) | L7 task_instance_id for the activity, if known | direct |
| [metaproteomics_analysis_category](metaproteomics_analysis_category.md) | 0..1 <br/> [MetaproteomicsAnalysisCategoryEnum](MetaproteomicsAnalysisCategoryEnum.md) | The category of metaproteomics analysis being performed, if applicable | direct |
| [parent_workflow_id](parent_workflow_id.md) | 0..1 <br/> [DataProcessingActivity](DataProcessingActivity.md) | Self-referential FK to the preceding DataProcessingActivity in a chain | [DataProcessingActivity](DataProcessingActivity.md) |
| [workflow_steps](workflow_steps.md) | 0..1 <br/> [String](String.md) | Per-run workflow parameters | [DataProcessingActivity](DataProcessingActivity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description of the data analysis workflow | [DataProcessingActivity](DataProcessingActivity.md) |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [started_at_time](started_at_time.md) | 1 <br/> [Datetime](Datetime.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [ended_at_time](ended_at_time.md) | 0..1 <br/> [Datetime](Datetime.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [software_url](software_url.md) | 0..1 <br/> [String](String.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [software_version](software_version.md) | 0..1 <br/> [String](String.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [software_poc](software_poc.md) | 0..1 <br/> [String](String.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |
| [execution_resource](execution_resource.md) | 0..1 <br/> [ExecutionResourceEnum](ExecutionResourceEnum.md) |  | [DataProcessingActivity](DataProcessingActivity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) | [results_from_ms_processing](results_from_ms_processing.md) | range | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |
| [MSImageProduct](MSImageProduct.md) | [results_from_ms_processing](results_from_ms_processing.md) | range | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |
| [MolecularIdentificationProduct](MolecularIdentificationProduct.md) | [results_from_ms_processing](results_from_ms_processing.md) | range | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |
| [MetaproteomicsProduct](MetaproteomicsProduct.md) | [results_from_ms_processing](results_from_ms_processing.md) | range | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MassSpectrometryDataProcessingActivity |
| native | basalt_schema:MassSpectrometryDataProcessingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MassSpectrometryDataProcessingActivity
description: 'Concrete mass spectrometry workflow run. Inherits all DataProcessingActivity

  slots including used_software and version.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataProcessingActivity
slots:
- uses_calibration
- uses_raw_ms_data
- lims_task_instance_id
- metaproteomics_analysis_category

```
</details>

### Induced

<details>
```yaml
name: MassSpectrometryDataProcessingActivity
description: 'Concrete mass spectrometry workflow run. Inherits all DataProcessingActivity

  slots including used_software and version.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: DataProcessingActivity
attributes:
  uses_calibration:
    name: uses_calibration
    description: Reference to the raw data file from the standard which was run with
      a batch of samples that was used as calibration for this data processing workflow
      run.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: uses_calibration
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - MassSpectrometryDataProcessingActivity
    range: MassSpectrometryStandardRun
  uses_raw_ms_data:
    name: uses_raw_ms_data
    description: The raw data file, output by a mass spectrometer, that was analyzed
      in  this data processing workflow run.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: uses_raw_ms_data
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - MassSpectrometryDataProcessingActivity
    range: MassSpectrometryInstrumentData
  lims_task_instance_id:
    name: lims_task_instance_id
    description: L7 task_instance_id for the activity, if known.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: lims_task_instance_id
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - MassSpectrometryDataProcessingActivity
    range: integer
  metaproteomics_analysis_category:
    name: metaproteomics_analysis_category
    description: The category of metaproteomics analysis being performed, if applicable.
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: metaproteomics_analysis_category
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - MassSpectrometryDataProcessingActivity
    range: MetaproteomicsAnalysisCategoryEnum
  parent_workflow_id:
    name: parent_workflow_id
    description: "Self-referential FK to the preceding DataProcessingActivity in a\
      \ chain.\nNULL -> first (or standalone) step.\nNon-null -> this execution directly\
      \ follows parent_workflow_id.\nEnables single-hop chaining queries; full traversal\
      \ via linkage_cache.\n\nDDL: ALTER TABLE \"DataProcessingActivity\"\n      \
      \ ADD COLUMN parent_workflow_id UUID\n       REFERENCES \"DataProcessingActivity\"\
      (id);"
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: parent_workflow_id
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - DataProcessingActivity
    range: DataProcessingActivity
    required: false
  workflow_steps:
    name: workflow_steps
    description: 'Per-run workflow parameters. Previously annotated TODO JSONB in
      schema.

      Direction: structured key-value pairs keyed by workflow type.

      Schema for allowed keys TBD per workflow type before full implementation.'
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: workflow_steps
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - DataProcessingActivity
    range: string
    required: false
  description:
    name: description
    description: A human-readable description of the data analysis workflow. May  include
      details such as the purpose, output, and/or main steps of  the workflow.
    title: description
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: description
    owner: MassSpectrometryDataProcessingActivity
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
  id:
    name: id
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    identifier: true
    alias: id
    owner: MassSpectrometryDataProcessingActivity
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
  started_at_time:
    name: started_at_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    alias: started_at_time
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - Activity
    - DataProcessingActivity
    range: datetime
    required: true
  ended_at_time:
    name: ended_at_time
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    alias: ended_at_time
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - Activity
    - DataProcessingActivity
    range: datetime
  software_url:
    name: software_url
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: software_url
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - DataProcessingActivity
    range: string
  software_version:
    name: software_version
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    alias: software_version
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - InstrumentData
    - DataProcessingActivity
    range: string
  software_poc:
    name: software_poc
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: software_poc
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - DataProcessingActivity
    range: string
  execution_resource:
    name: execution_resource
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: execution_resource
    owner: MassSpectrometryDataProcessingActivity
    domain_of:
    - DataProcessingActivity
    range: ExecutionResourceEnum

```
</details>