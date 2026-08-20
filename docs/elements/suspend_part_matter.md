

# Slot: suspended particulate matter (suspend_part_matter) 


_Concentration of suspended particulate matter. (Unit: mg/L)_





URI: [basalt_schema:suspend_part_matter](https://emsl-computing.github.io/BASALT-Schema/elements/suspend_part_matter)
Alias: suspend_part_matter

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
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:suspend_part_matter |
| native | basalt_schema:suspend_part_matter |




## LinkML Source

<details>
```yaml
name: suspend_part_matter
description: 'Concentration of suspended particulate matter. (Unit: mg/L)'
title: suspended particulate matter
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: suspend_part_matter
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L)$

```
</details>