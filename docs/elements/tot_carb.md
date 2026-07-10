

# Slot: total carbon content (tot_carb) 


_Total carbon content. Provide value and unit, any unit is valid_





URI: [analysis_api_schema:tot_carb](https://w3id.org/MONet/analysis-api-schema/tot_carb)
Alias: tot_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
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
| self | analysis_api_schema:tot_carb |
| native | analysis_api_schema:tot_carb |




## LinkML Source

<details>
```yaml
name: tot_carb
description: Total carbon content. Provide value and unit, any unit is valid
title: total carbon content
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_carb
domain_of:
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>