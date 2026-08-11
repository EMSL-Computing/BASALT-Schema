

# Slot: total particulate carbon (tot_part_carb) 


_Total particulate carbon content. (Unit: ug/L or umol/L)_





URI: [basalt_schema:tot_part_carb](https://w3id.org/MONet/basalt-schema/tot_part_carb)
Alias: tot_part_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L|umol/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_part_carb |
| native | basalt_schema:tot_part_carb |




## LinkML Source

<details>
```yaml
name: tot_part_carb
description: 'Total particulate carbon content. (Unit: ug/L or umol/L)'
title: total particulate carbon
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: tot_part_carb
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|umol/L)$

```
</details>