

# Class: HydraulicPropertiesProduct 


_Soil hydraulic parameters derived from HYPROP evaporation-experiment data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID, sampling_set, and core_section are inherited from the parent processedData record._





URI: [basalt_schema:HydraulicPropertiesProduct](https://EMSL-Computing.github.io/basalt-schema/HydraulicPropertiesProduct)





```mermaid
 classDiagram
    class HydraulicPropertiesProduct
    click HydraulicPropertiesProduct href "../HydraulicPropertiesProduct/"
      ProcessedData <|-- HydraulicPropertiesProduct
        click ProcessedData href "../ProcessedData/"
      
      HydraulicPropertiesProduct : alpha
        
      HydraulicPropertiesProduct : core_section
        
          
    
        
        
        HydraulicPropertiesProduct --> "0..1" CoreSectionEnum : core_section
        click CoreSectionEnum href "../CoreSectionEnum/"
    

        
      HydraulicPropertiesProduct : description
        
      HydraulicPropertiesProduct : filesize
        
      HydraulicPropertiesProduct : flag
        
          
    
        
        
        HydraulicPropertiesProduct --> "0..1" ProcessedDataFlag : flag
        click ProcessedDataFlag href "../ProcessedDataFlag/"
    

        
      HydraulicPropertiesProduct : id
        
      HydraulicPropertiesProduct : lims_barcode
        
      HydraulicPropertiesProduct : md5checksum
        
      HydraulicPropertiesProduct : measure_type
        
          
    
        
        
        HydraulicPropertiesProduct --> "0..1" ProductMeasureType : measure_type
        click ProductMeasureType href "../ProductMeasureType/"
    

        
      HydraulicPropertiesProduct : n
        
      HydraulicPropertiesProduct : name
        
      HydraulicPropertiesProduct : project
        
      HydraulicPropertiesProduct : s3_base_url
        
      HydraulicPropertiesProduct : s3_bucket
        
      HydraulicPropertiesProduct : s3_key
        
      HydraulicPropertiesProduct : sample_id
        
          
    
        
        
        HydraulicPropertiesProduct --> "0..1" Sample : sample_id
        click Sample href "../Sample/"
    

        
      HydraulicPropertiesProduct : sample_name
        
      HydraulicPropertiesProduct : sampling_set
        
      HydraulicPropertiesProduct : summary_metrics
        
      HydraulicPropertiesProduct : theta_r
        
      HydraulicPropertiesProduct : theta_s
        
      
```





## Inheritance
* [DataProduct](DataProduct.md)
    * [ProcessedData](ProcessedData.md)
        * **HydraulicPropertiesProduct**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [measure_type](measure_type.md) | 0..1 <br/> [ProductMeasureType](ProductMeasureType.md) | Whether the measurement recorded is a single measurement, one of a set of  re... | direct |
| [alpha](alpha.md) | 0..1 <br/> [Double](Double.md) | Van Genuchten shape parameter alpha (1/cm) | direct |
| [n](n.md) | 0..1 <br/> [Double](Double.md) | Van Genuchten pore-size distribution index n (dimensionless, n > 1) | direct |
| [theta_r](theta_r.md) | 0..1 <br/> [Double](Double.md) | Residual volumetric water content theta_r (cm3 cm) | direct |
| [theta_s](theta_s.md) | 0..1 <br/> [Double](Double.md) | Saturated volumetric water content theta_s (cm3 cm e-3) | direct |
| [flag](flag.md) | 0..1 <br/> [ProcessedDataFlag](ProcessedDataFlag.md) | QC flag for the entire VGM fit (e | direct |
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
| self | basalt_schema:HydraulicPropertiesProduct |
| native | basalt_schema:HydraulicPropertiesProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HydraulicPropertiesProduct
description: Soil hydraulic parameters derived from HYPROP evaporation-experiment
  data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID,
  sampling_set, and core_section are inherited from the parent processedData record.
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: ProcessedData
slots:
- measure_type
attributes:
  alpha:
    name: alpha
    description: Van Genuchten shape parameter alpha (1/cm). Controls the inverse
      of the air-entry suction; typically fitted by HYPROP-FIT or similar software.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  n:
    name: n
    description: Van Genuchten pore-size distribution index n (dimensionless, n >
      1). Controls the slope of the water-retention curve.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  theta_r:
    name: theta_r
    description: Residual volumetric water content theta_r (cm3 cm). The water content
      at which liquid conductivity approaches zero.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  theta_s:
    name: theta_s
    description: Saturated volumetric water content theta_s (cm3 cm e-3). Approximates
      total porosity under saturated conditions.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  flag:
    name: flag
    description: QC flag for the entire VGM fit (e.g. missing sample, failed QC).
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    domain_of:
    - WellReading
    - BulkDensityProduct
    - EnzymeProduct
    - GWCMoistureProduct
    - HydraulicPropertiesProduct
    - PhosphorusAnalysisProduct
    - RespirationProduct
    - TextureProduct
    - pHProduct
    range: ProcessedDataFlag

```
</details>

### Induced

<details>
```yaml
name: HydraulicPropertiesProduct
description: Soil hydraulic parameters derived from HYPROP evaporation-experiment
  data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID,
  sampling_set, and core_section are inherited from the parent processedData record.
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: ProcessedData
attributes:
  alpha:
    name: alpha
    description: Van Genuchten shape parameter alpha (1/cm). Controls the inverse
      of the air-entry suction; typically fitted by HYPROP-FIT or similar software.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    alias: alpha
    owner: HydraulicPropertiesProduct
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  n:
    name: n
    description: Van Genuchten pore-size distribution index n (dimensionless, n >
      1). Controls the slope of the water-retention curve.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    alias: n
    owner: HydraulicPropertiesProduct
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  theta_r:
    name: theta_r
    description: Residual volumetric water content theta_r (cm3 cm). The water content
      at which liquid conductivity approaches zero.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    alias: theta_r
    owner: HydraulicPropertiesProduct
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  theta_s:
    name: theta_s
    description: Saturated volumetric water content theta_s (cm3 cm e-3). Approximates
      total porosity under saturated conditions.
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    rank: 1000
    alias: theta_s
    owner: HydraulicPropertiesProduct
    domain_of:
    - HydraulicPropertiesProduct
    range: double
  flag:
    name: flag
    description: QC flag for the entire VGM fit (e.g. missing sample, failed QC).
    from_schema: https://EMSL-Computing.github.io/basalt-schema/products
    alias: flag
    owner: HydraulicPropertiesProduct
    domain_of:
    - WellReading
    - BulkDensityProduct
    - EnzymeProduct
    - GWCMoistureProduct
    - HydraulicPropertiesProduct
    - PhosphorusAnalysisProduct
    - RespirationProduct
    - TextureProduct
    - pHProduct
    range: ProcessedDataFlag
  measure_type:
    name: measure_type
    description: Whether the measurement recorded is a single measurement, one of
      a set of  replicate measurements, or an average of several replicate measurements.
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: measure_type
    owner: HydraulicPropertiesProduct
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: summary_metrics
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
    domain_of:
    - DataProduct
    range: string
  s3_bucket:
    name: s3_bucket
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_bucket
    owner: HydraulicPropertiesProduct
    domain_of:
    - DataProduct
    range: string
  s3_key:
    name: s3_key
    description: MinIO/S3 object key; required for all data products
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: s3_key
    owner: HydraulicPropertiesProduct
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
    owner: HydraulicPropertiesProduct
    domain_of:
    - DataProduct
    range: integer
  md5checksum:
    name: md5checksum
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: md5checksum
    owner: HydraulicPropertiesProduct
    domain_of:
    - DataProduct
    range: string
  id:
    name: id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    identifier: true
    alias: id
    owner: HydraulicPropertiesProduct
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