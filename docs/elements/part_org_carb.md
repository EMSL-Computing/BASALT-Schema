

# Slot: particulate organic carbon (part_org_carb) 


_Concentration of particulate organic carbon. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:part_org_carb](https://w3id.org/MONet/analysis-api-schema/part_org_carb)
Alias: part_org_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
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
| self | analysis_api_schema:part_org_carb |
| native | analysis_api_schema:part_org_carb |




## LinkML Source

<details>
```yaml
name: part_org_carb
description: Concentration of particulate organic carbon. Provide value and unit,
  any unit is valid.
title: particulate organic carbon
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: part_org_carb
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>