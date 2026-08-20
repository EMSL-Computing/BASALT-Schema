

# Slot: light intensity (light_intensity) 


_Measurement of light intensity. Provide value and unit, any unit is valid._





URI: [basalt_schema:light_intensity](https://emsl-computing.github.io/BASALT-Schema/elements/light_intensity)
Alias: light_intensity

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
| self | basalt_schema:light_intensity |
| native | basalt_schema:light_intensity |




## LinkML Source

<details>
```yaml
name: light_intensity
description: Measurement of light intensity. Provide value and unit, any unit is valid.
title: light intensity
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: light_intensity
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>