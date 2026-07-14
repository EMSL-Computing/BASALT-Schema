

# Slot: nitrate (nitrate) 


_Concentration of nitrate in the sample (Unit: umol/L or mg/L or ppm)_





URI: [analysis_api_schema:nitrate](https://w3id.org/MONet/analysis-api-schema/nitrate)
Alias: nitrate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:nitrate |
| native | analysis_api_schema:nitrate |




## LinkML Source

<details>
```yaml
name: nitrate
description: 'Concentration of nitrate in the sample (Unit: umol/L or mg/L or ppm)'
title: nitrate
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: nitrate
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>