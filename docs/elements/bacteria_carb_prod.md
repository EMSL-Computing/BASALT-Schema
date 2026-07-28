

# Slot: bacterial carbon production (bacteria_carb_prod) 


_Measurement of bacterial carbon production. Provide value and unit, any unit is valid_





URI: [analysis_api_schema:bacteria_carb_prod](https://w3id.org/MONet/analysis-api-schema/bacteria_carb_prod)
Alias: bacteria_carb_prod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:bacteria_carb_prod |
| native | analysis_api_schema:bacteria_carb_prod |




## LinkML Source

<details>
```yaml
name: bacteria_carb_prod
description: Measurement of bacterial carbon production. Provide value and unit, any
  unit is valid
title: bacterial carbon production
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: bacteria_carb_prod
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>