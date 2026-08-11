

# Slot: lims_barcode 


_LIMS barcode identifier_





URI: [basalt_schema:lims_barcode](https://EMSL-Computing.github.io/basalt-schema/lims_barcode)
Alias: lims_barcode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |
| [MetaproteomicsProduct](MetaproteomicsProduct.md) | Abstract parent class for processed metaproteomics data |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) | Phosphorus analysis product, typically derived via colorimetric assay of soil... |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |
| [MolecularIdentificationProduct](MolecularIdentificationProduct.md) | a file containing molecular formula identifications that was output from a ma... |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) | Microbial biomass analysis product, typically derived via chloroform fumigati... |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [RespirationProduct](RespirationProduct.md) | Soil respiration analysis product |  no  |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) | Nitrogen analysis product, typically derived via colorimetric assay of soil e... |  no  |
| [PHProduct](PHProduct.md) | Soil pH analysis product, typically derived via pH meter or similar instrumen... |  no  |
| [MSImageProduct](MSImageProduct.md) | one or more image(s) output from a mass spec data processing workflow (eg |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) | Bulk density analysis product, typically derived via oven-drying and weighing... |  no  |
| [IonsAnalysisProduct](IonsAnalysisProduct.md) | Ions analysis product, typically derived via ICP-OES or similar instrument |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [TomographyProduct](TomographyProduct.md) | Soil tomography analysis product, typically derived via X-ray computed tomogr... |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [XRFElementalProduct](XRFElementalProduct.md) | X-ray Fluorescence (XRF) elemental concentration data |  no  |
| [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) | Abstract base for all mass spectrometry data products |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [XRDPhaseProduct](XRDPhaseProduct.md) | X-ray Diffraction (XRD) mineral phase identification and quantification data |  no  |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) | Elemental analysis product, typically derived via combustion or similar instr... |  no  |
| [EnzymeProduct](EnzymeProduct.md) | Enzyme activity analysis product, typically derived via colorimetric assay of... |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [Sample](Sample.md) | A physical sample collected from an environment |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) | Gravimetric water content (GWC) analysis product, typically derived via oven-... |  no  |
| [XRayDataProduct](XRayDataProduct.md) | Abstract base class for X-ray analytical data products |  no  |
| [ProcessedData](ProcessedData.md) | A data product generated by a workflow execution |  no  |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
| [TextureProduct](TextureProduct.md) | Soil texture analysis product, typically derived via hydrometer or similar in... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ProcessedData](ProcessedData.md), [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:lims_barcode |
| native | basalt_schema:lims_barcode |




## LinkML Source

<details>
```yaml
name: lims_barcode
description: LIMS barcode identifier
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: lims_barcode
domain_of:
- ProcessedData
- Sample
range: string
required: false

```
</details>