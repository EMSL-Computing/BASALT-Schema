

# Slot: measure_type 


_Whether the measurement recorded is a single measurement, one of a set of  replicate measurements, or an average of several replicate measurements._





URI: [analysis_api_schema:measure_type](https://w3id.org/MONet/analysis-api-schema/measure_type)
Alias: measure_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) | Nitrogen analysis product, typically derived via colorimetric assay of soil e... |  no  |
| [XRFElementalProduct](XRFElementalProduct.md) | X-ray Fluorescence (XRF) elemental concentration data |  no  |
| [MAOMProduct](MAOMProduct.md) | Mineral-Associated Organic Matter (MAOM) analysis product, typically derived ... |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) | Bulk density analysis product, typically derived via oven-drying and weighing... |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [TomographyProduct](TomographyProduct.md) | Soil tomography analysis product, typically derived via X-ray computed tomogr... |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) | Gravimetric water content (GWC) analysis product, typically derived via oven-... |  no  |
| [WEOMProduct](WEOMProduct.md) | Water Extractable Organic Matter (WEOM) analysis product, typically derived v... |  no  |
| [EnzymeProduct](EnzymeProduct.md) | Enzyme activity analysis product, typically derived via colorimetric assay of... |  no  |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) | Elemental analysis product, typically derived via combustion or similar instr... |  no  |
| [IonsAnalysisProduct](IonsAnalysisProduct.md) | Ions analysis product, typically derived via ICP-OES or similar instrument |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) | Phosphorus analysis product, typically derived via colorimetric assay of soil... |  no  |
| [RespirationProduct](RespirationProduct.md) | Soil respiration analysis product |  no  |
| [TextureProduct](TextureProduct.md) | Soil texture analysis product, typically derived via hydrometer or similar in... |  no  |
| [PHProduct](PHProduct.md) | Soil pH analysis product, typically derived via pH meter or similar instrumen... |  no  |
| [XRDPhaseProduct](XRDPhaseProduct.md) | X-ray Diffraction (XRD) mineral phase identification and quantification data |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) | Microbial biomass analysis product, typically derived via chloroform fumigati... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProductMeasureType](ProductMeasureType.md) |
| Domain Of | [BulkDensityProduct](BulkDensityProduct.md), [ElementalAnalysisProduct](ElementalAnalysisProduct.md), [EnzymeProduct](EnzymeProduct.md), [GWCMoistureProduct](GWCMoistureProduct.md), [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md), [IonsAnalysisProduct](IonsAnalysisProduct.md), [MAOMProduct](MAOMProduct.md), [MicrobialBiomassProduct](MicrobialBiomassProduct.md), [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md), [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md), [RespirationProduct](RespirationProduct.md), [TextureProduct](TextureProduct.md), [TomographyProduct](TomographyProduct.md), [WEOMProduct](WEOMProduct.md), [PHProduct](PHProduct.md), [XRFElementalProduct](XRFElementalProduct.md), [XRDPhaseProduct](XRDPhaseProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:measure_type |
| native | analysis_api_schema:measure_type |




## LinkML Source

<details>
```yaml
name: measure_type
description: Whether the measurement recorded is a single measurement, one of a set
  of  replicate measurements, or an average of several replicate measurements.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: measure_type
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

```
</details>