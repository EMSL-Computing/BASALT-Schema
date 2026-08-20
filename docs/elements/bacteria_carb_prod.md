

# Slot: bacterial carbon production (bacteria_carb_prod) 


_Measurement of bacterial carbon production. Provide value and unit, any unit is valid_





URI: [basalt_schema:bacteria_carb_prod](https://emsl-computing.github.io/BASALT-Schema/elements/bacteria_carb_prod)
Alias: bacteria_carb_prod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:bacteria_carb_prod |
| native | basalt_schema:bacteria_carb_prod |




## LinkML Source

<details>
```yaml
name: bacteria_carb_prod
description: Measurement of bacterial carbon production. Provide value and unit, any
  unit is valid
title: bacterial carbon production
from_schema: https://emsl-computing.github.io/BASALT-Schema
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