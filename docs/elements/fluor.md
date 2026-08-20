

# Slot: fluorescence (fluor) 


_Raw or converted fluorescence of water. Provide value and unit, any unit is valid._





URI: [basalt_schema:fluor](https://emsl-computing.github.io/BASALT-Schema/elements/fluor)
Alias: fluor

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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:fluor |
| native | basalt_schema:fluor |




## LinkML Source

<details>
```yaml
name: fluor
description: Raw or converted fluorescence of water. Provide value and unit, any unit
  is valid.
title: fluorescence
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: fluor
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>