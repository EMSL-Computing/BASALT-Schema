

# Slot: chlorophyll (chlorophyll) 


_Concentration of chlorophyll (Unit: mg/m3 or ug/L)_





URI: [analysis_api_schema:chlorophyll](https://w3id.org/MONet/analysis-api-schema/chlorophyll)
Alias: chlorophyll

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(mg/m3|ug/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:chlorophyll |
| native | analysis_api_schema:chlorophyll |




## LinkML Source

<details>
```yaml
name: chlorophyll
description: 'Concentration of chlorophyll (Unit: mg/m3 or ug/L)'
title: chlorophyll
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: chlorophyll
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/m3|ug/L)$

```
</details>