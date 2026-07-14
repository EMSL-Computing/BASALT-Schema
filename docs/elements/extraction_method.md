

# Slot: extraction method (extraction_method) 


_If you (the user) performed an extraction preparation or processing before sending the sample to EMSL, what was it? This is only applicable when sending an 'analytical sample'. See README for more details on types of samples._





URI: [analysis_api_schema:extraction_method](https://w3id.org/MONet/analysis-api-schema/extraction_method)
Alias: extraction_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:extraction_method |
| native | analysis_api_schema:extraction_method |




## LinkML Source

<details>
```yaml
name: extraction_method
description: If you (the user) performed an extraction preparation or processing before
  sending the sample to EMSL, what was it? This is only applicable when sending an
  'analytical sample'. See README for more details on types of samples.
title: extraction method
from_schema: https://w3id.org/MONet/analysis-api-schema
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