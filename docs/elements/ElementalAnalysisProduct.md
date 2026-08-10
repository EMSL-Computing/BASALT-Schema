

# Class: ElementalAnalysisProduct 


_Elemental analysis product, typically derived via combustion or similar instrument._

_One row per sample with columns for total carbon, total nitrogen, total Kjeldahl nitrogen, and total sulfur._

_Individual QC flags for each measurement using ProcessedDataFlag enum._





URI: [basalt_schema:ElementalAnalysisProduct](https://w3id.org/MONet/basalt-schema/ElementalAnalysisProduct)





```mermaid
 classDiagram
    class ElementalAnalysisProduct
    click ElementalAnalysisProduct href "../ElementalAnalysisProduct/"
      ProcessedData <|-- ElementalAnalysisProduct
        click ProcessedData href "../ProcessedData/"
      
      ElementalAnalysisProduct : core_section
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      ElementalAnalysisProduct : description
        
      ElementalAnalysisProduct : filesize
        
      ElementalAnalysisProduct : flag_tkn
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" ProcessedDataFlag : flag_tkn
        click ProcessedDataFlag href "../ProcessedDataFlag/"
    

        
      ElementalAnalysisProduct : flag_total_carbon
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" ProcessedDataFlag : flag_total_carbon
        click ProcessedDataFlag href "../ProcessedDataFlag/"
    

        
      ElementalAnalysisProduct : flag_total_nitrogen
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" ProcessedDataFlag : flag_total_nitrogen
        click ProcessedDataFlag href "../ProcessedDataFlag/"
    

        
      ElementalAnalysisProduct : flag_total_sulfur
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" ProcessedDataFlag : flag_total_sulfur
        click ProcessedDataFlag href "../ProcessedDataFlag/"
    

        
      ElementalAnalysisProduct : id
        
      ElementalAnalysisProduct : lims_barcode
        
      ElementalAnalysisProduct : md5checksum
        
      ElementalAnalysisProduct : measure_type
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" ProductMeasureType : measure_type
        click ProductMeasureType href "../ProductMeasureType/"
    

        
      ElementalAnalysisProduct : name
        
      ElementalAnalysisProduct : project
        
      ElementalAnalysisProduct : s3_base_url
        
      ElementalAnalysisProduct : s3_bucket
        
      ElementalAnalysisProduct : s3_key
        
      ElementalAnalysisProduct : sample_id
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      ElementalAnalysisProduct : sample_name
        
      ElementalAnalysisProduct : sampling_set
        
      ElementalAnalysisProduct : summary_metrics
        
      ElementalAnalysisProduct : total_carbon_id
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" QuantityValue : total_carbon_id
        click QuantityValue href "../QuantityValue/"
    

        
      ElementalAnalysisProduct : total_kjeldahl_nitrogen_id
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" QuantityValue : total_kjeldahl_nitrogen_id
        click QuantityValue href "../QuantityValue/"
    

        
      ElementalAnalysisProduct : total_nitrogen_id
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" QuantityValue : total_nitrogen_id
        click QuantityValue href "../QuantityValue/"
    

        
      ElementalAnalysisProduct : total_sulfur_id
        
          
    
        
        
        ElementalAnalysisProduct --> "0..1" QuantityValue : total_sulfur_id
        click QuantityValue href "../QuantityValue/"
    

        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * **ElementalAnalysisProduct**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [measure_type](measure_type.md) | 0..1 <br/> [ProductMeasureType](ProductMeasureType.md) | Whether the measurement recorded is a single measurement, one of a set of  re... | direct |
| [total_carbon_id](total_carbon_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [total_nitrogen_id](total_nitrogen_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [total_kjeldahl_nitrogen_id](total_kjeldahl_nitrogen_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [total_sulfur_id](total_sulfur_id.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [flag_total_carbon](flag_total_carbon.md) | 0..1 <br/> [ProcessedDataFlag](ProcessedDataFlag.md) |  | direct |
| [flag_total_nitrogen](flag_total_nitrogen.md) | 0..1 <br/> [ProcessedDataFlag](ProcessedDataFlag.md) |  | direct |
| [flag_tkn](flag_tkn.md) | 0..1 <br/> [ProcessedDataFlag](ProcessedDataFlag.md) |  | direct |
| [flag_total_sulfur](flag_total_sulfur.md) | 0..1 <br/> [ProcessedDataFlag](ProcessedDataFlag.md) |  | direct |
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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ElementalAnalysisProduct |
| native | basalt_schema:ElementalAnalysisProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ElementalAnalysisProduct
description: 'Elemental analysis product, typically derived via combustion or similar
  instrument.

  One row per sample with columns for total carbon, total nitrogen, total Kjeldahl
  nitrogen, and total sulfur.

  Individual QC flags for each measurement using ProcessedDataFlag enum.'
from_schema: https://w3id.org/MONet/basalt-schema
is_a: ProcessedData
slots:
- measure_type
attributes:
  total_carbon_id:
    name: total_carbon_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  total_nitrogen_id:
    name: total_nitrogen_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    - MAOMProduct
    - WEOMProduct
    range: QuantityValue
  total_kjeldahl_nitrogen_id:
    name: total_kjeldahl_nitrogen_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  total_sulfur_id:
    name: total_sulfur_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  flag_total_carbon:
    name: flag_total_carbon
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_total_nitrogen:
    name: flag_total_nitrogen
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_tkn:
    name: flag_tkn
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_total_sulfur:
    name: flag_total_sulfur
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag

```
</details>

### Induced

<details>
```yaml
name: ElementalAnalysisProduct
description: 'Elemental analysis product, typically derived via combustion or similar
  instrument.

  One row per sample with columns for total carbon, total nitrogen, total Kjeldahl
  nitrogen, and total sulfur.

  Individual QC flags for each measurement using ProcessedDataFlag enum.'
from_schema: https://w3id.org/MONet/basalt-schema
is_a: ProcessedData
attributes:
  total_carbon_id:
    name: total_carbon_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: total_carbon_id
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  total_nitrogen_id:
    name: total_nitrogen_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: total_nitrogen_id
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    - MAOMProduct
    - WEOMProduct
    range: QuantityValue
  total_kjeldahl_nitrogen_id:
    name: total_kjeldahl_nitrogen_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: total_kjeldahl_nitrogen_id
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  total_sulfur_id:
    name: total_sulfur_id
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: total_sulfur_id
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: QuantityValue
  flag_total_carbon:
    name: flag_total_carbon
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: flag_total_carbon
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_total_nitrogen:
    name: flag_total_nitrogen
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: flag_total_nitrogen
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_tkn:
    name: flag_tkn
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: flag_tkn
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  flag_total_sulfur:
    name: flag_total_sulfur
    from_schema: https://w3id.org/MONet/basalt-schema/products
    rank: 1000
    alias: flag_total_sulfur
    owner: ElementalAnalysisProduct
    domain_of:
    - ElementalAnalysisProduct
    range: ProcessedDataFlag
  measure_type:
    name: measure_type
    description: Whether the measurement recorded is a single measurement, one of
      a set of  replicate measurements, or an average of several replicate measurements.
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: measure_type
    owner: ElementalAnalysisProduct
    domain_of:
    - BulkDensityProduct
    - ElementalAnalysisProduct
    - EnzymeProduct
    - GWCMoistureProduct
    - HydraulicPropertiesProduct
    - IonsAnalysisProduct
    - MAOMProduct
    - MicrobialBiomassProduct
    - NitrogenAnalysisProduct
    - PhosphorusAnalysisProduct
    - RespirationProduct
    - TextureProduct
    - TomographyProduct
    - WEOMProduct
    - pHProduct
    - XRFElementalProduct
    - XRDPhaseProduct
    range: ProductMeasureType
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
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: summary_metrics
    owner: ElementalAnalysisProduct
    domain_of:
    - ProcessedData
    range: string
    required: false
  lims_barcode:
    name: lims_barcode
    description: LIMS barcode identifier
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: lims_barcode
    owner: ElementalAnalysisProduct
    domain_of:
    - ProcessedData
    - Sample
    range: string
    required: false
  sample_id:
    name: sample_id
    description: Link back to the originating sample
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: sample_id
    owner: ElementalAnalysisProduct
    domain_of:
    - ProcessedData
    - AMP2WellMetadata
    - MetagenomicsProduct
    range: Sample
    required: false
  name:
    name: name
    description: Human-readable name for the entity or activity.
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: name
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: description
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    aliases:
    - study
    - study_id
    - project_id
    - proposal
    - proposal_id
    rank: 1000
    alias: project
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: sampling_set
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: core_section
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    aliases:
    - samp_name
    rank: 1000
    alias: sample_name
    owner: ElementalAnalysisProduct
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
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: s3_base_url
    owner: ElementalAnalysisProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: s3_bucket
    owner: ElementalAnalysisProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: s3_key
    owner: ElementalAnalysisProduct
    domain_of:
    - DataProduct
    range: string
    required: true
  filesize:
    name: filesize
    description: Size of the file in bytes
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: filesize
    owner: ElementalAnalysisProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: md5checksum
    owner: ElementalAnalysisProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://w3id.org/MONet/basalt-schema
    identifier: true
    alias: id
    owner: ElementalAnalysisProduct
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