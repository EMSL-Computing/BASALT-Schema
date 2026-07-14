

# Slot: density (density) 


_Density of the sample, which is its mass per unit volume (aka volumetric mass density) (Unit: g/m3 or g/cm3)_





URI: [analysis_api_schema:density](https://w3id.org/MONet/analysis-api-schema/density)
Alias: density

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(g/m3|g/cm3)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:density |
| native | analysis_api_schema:density |




## LinkML Source

<details>
```yaml
name: density
description: 'Density of the sample, which is its mass per unit volume (aka volumetric
  mass density) (Unit: g/m3 or g/cm3)'
title: density
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: density
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(g/m3|g/cm3)$

```
</details>