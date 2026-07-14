

# Slot: measure_type 


_Whether the measurement recorded is a single measurement, one of a set of  replicate measurements, or an average of several replicate measurements._





URI: [analysis_api_schema:measure_type](https://w3id.org/MONet/analysis-api-schema/measure_type)
Alias: measure_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IonsAnalysisProduct](IonsAnalysisProduct.md) |  |  no  |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) |  |  no  |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) |  |  no  |
| [PHProduct](PHProduct.md) |  |  no  |
| [TextureProduct](TextureProduct.md) |  |  no  |
| [XRFElementalProduct](XRFElementalProduct.md) | X-ray Fluorescence (XRF) elemental concentration data |  no  |
| [WEOMProduct](WEOMProduct.md) |  |  no  |
| [XRDPhaseProduct](XRDPhaseProduct.md) | X-ray Diffraction (XRD) mineral phase identification and quantification data |  no  |
| [MAOMProduct](MAOMProduct.md) |  |  no  |
| [RespirationProduct](RespirationProduct.md) |  |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) |  |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) |  |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) |  |  no  |
| [TomographyProduct](TomographyProduct.md) |  |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [EnzymeProduct](EnzymeProduct.md) |  |  no  |







## Properties

* Range: [ProductMeasureType](ProductMeasureType.md)





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