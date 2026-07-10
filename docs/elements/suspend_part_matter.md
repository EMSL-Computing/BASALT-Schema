

# Slot: suspended particulate matter (suspend_part_matter) 


_Concentration of suspended particulate matter. (Unit: mg/L)_





URI: [analysis_api_schema:suspend_part_matter](https://w3id.org/MONet/analysis-api-schema/suspend_part_matter)
Alias: suspend_part_matter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(mg/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:suspend_part_matter |
| native | analysis_api_schema:suspend_part_matter |




## LinkML Source

<details>
```yaml
name: suspend_part_matter
description: 'Concentration of suspended particulate matter. (Unit: mg/L)'
title: suspended particulate matter
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: suspend_part_matter
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L)$

```
</details>