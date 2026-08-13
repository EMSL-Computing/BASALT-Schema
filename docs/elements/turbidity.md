

# Slot: turbidity (turbidity) 


_Measure of the amount of cloudiness or haziness in water caused by individual particles. Provide value and unit any unit is valid._





URI: [basalt_schema:turbidity](https://EMSL-Computing.github.io/BASALT-Schema/turbidity)
Alias: turbidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
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










## TODOs

* decide how to represent in backend (normalized child table with FK to PlateSetupActivity, array column, or other)



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:turbidity |
| native | basalt_schema:turbidity |




## LinkML Source

<details>
```yaml
name: turbidity
description: Measure of the amount of cloudiness or haziness in water caused by individual
  particles. Provide value and unit any unit is valid.
title: turbidity
todos:
- decide how to represent in backend (normalized child table with FK to PlateSetupActivity,
  array column, or other)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: turbidity
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>