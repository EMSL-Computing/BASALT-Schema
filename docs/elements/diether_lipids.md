

# Slot: diether lipids (diether_lipids) 


_Concentration of diether lipids; can include multiple types of diether lipids (Unit: ng/L)_





URI: [analysis_api_schema:diether_lipids](https://w3id.org/MONet/analysis-api-schema/diether_lipids)
Alias: diether_lipids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*ng/L$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:diether_lipids |
| native | analysis_api_schema:diether_lipids |




## LinkML Source

<details>
```yaml
name: diether_lipids
description: 'Concentration of diether lipids; can include multiple types of diether
  lipids (Unit: ng/L)'
title: diether lipids
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: diether_lipids
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ng/L$

```
</details>