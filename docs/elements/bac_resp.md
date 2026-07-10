

# Slot: bacterial respiration (bac_resp) 


_Measurement of bacterial respiration in the water column. Provide value and unit,any unit is valid._





URI: [analysis_api_schema:bac_resp](https://w3id.org/MONet/analysis-api-schema/bac_resp)
Alias: bac_resp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:bac_resp |
| native | analysis_api_schema:bac_resp |




## LinkML Source

<details>
```yaml
name: bac_resp
description: Measurement of bacterial respiration in the water column. Provide value
  and unit,any unit is valid.
title: bacterial respiration
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: bac_resp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>