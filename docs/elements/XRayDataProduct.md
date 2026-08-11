

# Class: XRayDataProduct 


_Abstract base class for X-ray analytical data products._

_Inherits S3 storage metadata and sample linkage from dataProduct via ProcessedData._

__

_Concrete subclasses:_

_  - XRFElementalProduct: elemental concentrations (one row per sample)_

_  - XRDPhaseProduct: mineral phases (one row per sample)_

__

_Common patterns:_

_  - s3_key points to raw spectrum/diffractogram file in MinIO_

_  - summary_metrics provides lightweight queryable summaries:_

_      XRF: {"Ni_mg_kg":45.3, "Pb_mg_kg":8.2, "As_mg_kg":12.1}_

_      XRD: {"quartz_percent":42, "albite_percent":18, "kaolinite_percent":31}_

_  - workflow_id is NULL for direct instrument output (XRF typical)_

_  - workflow_id links to DataProcessingActivity for computational processing (XRD Rietveld) _




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [basalt_schema:XRayDataProduct](https://EMSL-Computing.github.io/basalt-schema/XRayDataProduct)





```mermaid
 classDiagram
    class XRayDataProduct
    click XRayDataProduct href "../XRayDataProduct/"
      ProcessedData <|-- XRayDataProduct
        click ProcessedData href "../ProcessedData/"
      

      XRayDataProduct <|-- XRFElementalProduct
        click XRFElementalProduct href "../XRFElementalProduct/"
      XRayDataProduct <|-- XRDPhaseProduct
        click XRDPhaseProduct href "../XRDPhaseProduct/"
      

      XRayDataProduct : core_section
        
          
    
        
        
        XRayDataProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      XRayDataProduct : description
        
      XRayDataProduct : filesize
        
      XRayDataProduct : id
        
      XRayDataProduct : lims_barcode
        
      XRayDataProduct : md5checksum
        
      XRayDataProduct : name
        
      XRayDataProduct : project
        
      XRayDataProduct : s3_base_url
        
      XRayDataProduct : s3_bucket
        
      XRayDataProduct : s3_key
        
      XRayDataProduct : sample_id
        
          
    
        
        
        XRayDataProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      XRayDataProduct : sample_name
        
      XRayDataProduct : sampling_set
        
      XRayDataProduct : summary_metrics
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * **XRayDataProduct**
            * [XRFElementalProduct](XRFElementalProduct.md)
            * [XRDPhaseProduct](XRDPhaseProduct.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [summary_metrics](summary_metrics.md) | 0..1 <br/> [String](String.md) | Lightweight per-product summary for common queries that avoid full file downl... | [ProcessedData](ProcessedData.md) |
| [lims_barcode](lims_barcode.md) | 0..1 <br/> [String](String.md) | LIMS barcode identifier | [ProcessedData](ProcessedData.md) |
| [sample_id](sample_id.md) | 0..1 <br/> [Sample](Sample.md) | Link back to the originating sample | [ProcessedData](ProcessedData.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Human-readable name for the entity or activity | [DataProduct](DataProduct.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Human-readable description for the entity or activity | [DataProduct](DataProduct.md) |
| [project](project.md) | 0..1 <br/> [Integer](Integer.md) | Identifier for the user project associated with the entity or activity | [DataProduct](DataProduct.md) |
| [sampling_set](sampling_set.md) | 0..1 <br/> [Integer](Integer.md) | Sampling set number for grouping related samples collected together | [DataProduct](DataProduct.md) |
| [core_section](core_section.md) | 0..1 <br/> [CoreSectionEnum](CoreSectionEnum.md) | The section of the core | [DataProduct](DataProduct.md) |
| [sample_name](sample_name.md) | 0..1 <br/> [String](String.md) | The name or label that is present on the shipped sample | [DataProduct](DataProduct.md) |
| [s3_base_url](s3_base_url.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_bucket](s3_bucket.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [s3_key](s3_key.md) | 1 <br/> [String](String.md) | MinIO/S3 object key; required for all data products | [DataProduct](DataProduct.md) |
| [filesize](filesize.md) | 0..1 <br/> [Integer](Integer.md) | Size of the file in bytes | [DataProduct](DataProduct.md) |
| [md5checksum](md5checksum.md) | 0..1 <br/> [String](String.md) |  | [DataProduct](DataProduct.md) |
| [id](id.md) | 1 <br/> [Uuid](Uuid.md) |  | [DataProduct](DataProduct.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:XRayDataProduct |
| native | basalt_schema:XRayDataProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XRayDataProduct
description: "Abstract base class for X-ray analytical data products.\nInherits S3\
  \ storage metadata and sample linkage from dataProduct via ProcessedData.\n\nConcrete\
  \ subclasses:\n  - XRFElementalProduct: elemental concentrations (one row per sample)\n\
  \  - XRDPhaseProduct: mineral phases (one row per sample)\n\nCommon patterns:\n\
  \  - s3_key points to raw spectrum/diffractogram file in MinIO\n  - summary_metrics\
  \ provides lightweight queryable summaries:\n      XRF: {\"Ni_mg_kg\":45.3, \"Pb_mg_kg\"\
  :8.2, \"As_mg_kg\":12.1}\n      XRD: {\"quartz_percent\":42, \"albite_percent\"\
  :18, \"kaolinite_percent\":31}\n  - workflow_id is NULL for direct instrument output\
  \ (XRF typical)\n  - workflow_id links to DataProcessingActivity for computational\
  \ processing (XRD Rietveld) "
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: ProcessedData
abstract: true

```
</details>

### Induced

<details>
```yaml
name: XRayDataProduct
description: "Abstract base class for X-ray analytical data products.\nInherits S3\
  \ storage metadata and sample linkage from dataProduct via ProcessedData.\n\nConcrete\
  \ subclasses:\n  - XRFElementalProduct: elemental concentrations (one row per sample)\n\
  \  - XRDPhaseProduct: mineral phases (one row per sample)\n\nCommon patterns:\n\
  \  - s3_key points to raw spectrum/diffractogram file in MinIO\n  - summary_metrics\
  \ provides lightweight queryable summaries:\n      XRF: {\"Ni_mg_kg\":45.3, \"Pb_mg_kg\"\
  :8.2, \"As_mg_kg\":12.1}\n      XRD: {\"quartz_percent\":42, \"albite_percent\"\
  :18, \"kaolinite_percent\":31}\n  - workflow_id is NULL for direct instrument output\
  \ (XRF typical)\n  - workflow_id links to DataProcessingActivity for computational\
  \ processing (XRD Rietveld) "
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: ProcessedData
abstract: true
attributes:
  summary_metrics:
    name: summary_metrics
    description: "Lightweight per-product summary for common queries that avoid full\
      \ file download.\nDirection: structured key-value pairs; per-type schemas TBD:\n\
      \  ecoplate:  well-level absorbance summaries (position, timepoint, absorbance)\n\
      \  xrf:       per-element concentration results + QC flag\n  lcms:      feature\
      \ count, identification count, MSI-2 fraction\nInterim DB storage: JSONB column\
      \ retained until formal typed class exists."
    todos:
    - make this inined/multivalued?
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: summary_metrics
    owner: XRayDataProduct
    domain_of:
    - ProcessedData
    range: string
    required: false
  lims_barcode:
    name: lims_barcode
    description: LIMS barcode identifier
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: lims_barcode
    owner: XRayDataProduct
    domain_of:
    - ProcessedData
    - Sample
    range: string
    required: false
  sample_id:
    name: sample_id
    description: Link back to the originating sample
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sample_id
    owner: XRayDataProduct
    domain_of:
    - ProcessedData
    - AMP2WellMetadata
    - MetagenomicsProduct
    range: Sample
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: name
    owner: XRayDataProduct
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
    owner: XRayDataProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: XRayDataProduct
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
  sampling_set:
    name: sampling_set
    description: 'Sampling set number for grouping related samples collected together.

      This is a user-defined sequential integer that can be used to link samples collected

      in the same sampling event or campaign.'
    title: sampling set
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: sampling_set
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    - MonetSoilSample
    range: integer
  core_section:
    name: core_section
    description: The section of the core.
    title: core section
    examples:
    - value: TOP
    - value: MID
    - value: BTM
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: core_section
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    - CoreSection
    range: CoreSectionEnum
  sample_name:
    name: sample_name
    description: 'The name or label that is present on the shipped sample. This should

      be a human readable name.'
    title: sample name
    notes:
    - This is typically an alias for the inherited 'name' slot on Sample classes.
      Defined separately for compatibility with source data files using 'sample_name'
      column headers.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    aliases:
    - samp_name
    rank: 1000
    alias: sample_name
    owner: XRayDataProduct
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
    range: string
  s3_base_url:
    name: s3_base_url
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_base_url
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_bucket
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_key
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    range: string
    required: true
  filesize:
    name: filesize
    description: Size of the file in bytes
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: filesize
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: md5checksum
    owner: XRayDataProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: XRayDataProduct
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