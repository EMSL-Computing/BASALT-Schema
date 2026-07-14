

# Slot: chloride (chloride) 


_Concentration of chloride in the sample (Unit: mg/L or ppm)_





URI: [analysis_api_schema:chloride](https://w3id.org/MONet/analysis-api-schema/chloride)
Alias: chloride

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(mg/L|ppm)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:chloride |
| native | analysis_api_schema:chloride |




## LinkML Source

<details>
```yaml
name: chloride
description: 'Concentration of chloride in the sample (Unit: mg/L or ppm)'
title: chloride
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: chloride
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|ppm)$

```
</details>