

# Slot: measure_type 


_Whether the measurement recorded is a single measurement, one of a set of  replicate measurements, or an average of several replicate measurements._





URI: [analysis_api_schema:measure_type](https://w3id.org/MONet/analysis-api-schema/measure_type)
Alias: measure_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) |  |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) |  |  no  |
| [TomographyProduct](TomographyProduct.md) |  |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [XRFElementalProduct](XRFElementalProduct.md) | X-ray Fluorescence (XRF) elemental concentration data |  no  |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) |  |  no  |
| [EnzymeProduct](EnzymeProduct.md) |  |  no  |
| [XRDPhaseProduct](XRDPhaseProduct.md) | X-ray Diffraction (XRD) mineral phase identification and quantification data |  no  |
| [MAOMProduct](MAOMProduct.md) |  |  no  |
| [WEOMProduct](WEOMProduct.md) |  |  no  |
| [PHProduct](PHProduct.md) |  |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [TextureProduct](TextureProduct.md) |  |  no  |
| [RespirationProduct](RespirationProduct.md) |  |  no  |
| [IonsAnalysisProduct](IonsAnalysisProduct.md) |  |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) |  |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) |  |  no  |






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