

# Slot: particulate organic carbon (part_org_carb) 


_Concentration of particulate organic carbon. Provide value and unit, any unit is valid._





URI: [basalt_schema:part_org_carb](https://EMSL-Computing.github.io/basalt-schema/part_org_carb)
Alias: part_org_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:part_org_carb |
| native | basalt_schema:part_org_carb |




## LinkML Source

<details>
```yaml
name: part_org_carb
description: Concentration of particulate organic carbon. Provide value and unit,
  any unit is valid.
title: particulate organic carbon
from_schema: https://EMSL-Computing.github.io/basalt-schema
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