

# Slot: water current (water_current) 


_Measurement of magnitude and direction of flow within a fluid. Provide value and unit, any unit is valid._





URI: [basalt_schema:water_current](https://emsl-computing.github.io/BASALT-Schema/elements/water_current)
Alias: water_current

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:water_current |
| native | basalt_schema:water_current |




## LinkML Source

<details>
```yaml
name: water_current
description: Measurement of magnitude and direction of flow within a fluid. Provide
  value and unit, any unit is valid.
title: water current
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: water_current
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>