

# Slot: extraction method (extraction_method) 


_If you (the user) performed an extraction preparation or processing before sending the sample to EMSL, what was it? This is only applicable when sending an 'analytical sample'. See README for more details on types of samples._





URI: [basalt_schema:extraction_method](https://EMSL-Computing.github.io/BASALT-Schema/extraction_method)
Alias: extraction_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) | Phosphorus analysis product, typically derived via colorimetric assay of soil... |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md), [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:extraction_method |
| native | basalt_schema:extraction_method |




## LinkML Source

<details>
```yaml
name: extraction_method
description: If you (the user) performed an extraction preparation or processing before
  sending the sample to EMSL, what was it? This is only applicable when sending an
  'analytical sample'. See README for more details on types of samples.
title: extraction method
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: extraction_method
domain_of:
- PhosphorusAnalysisProduct
- AerosolArmSample
- AerosolSample
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>