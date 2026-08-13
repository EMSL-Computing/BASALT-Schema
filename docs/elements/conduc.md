

# Slot: conductivity (conduc) 


_Electrical conductivity of water. Provide value and unit, any unit is valid._





URI: [basalt_schema:conduc](https://EMSL-Computing.github.io/BASALT-Schema/conduc)
Alias: conduc

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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:conduc |
| native | basalt_schema:conduc |




## LinkML Source

<details>
```yaml
name: conduc
description: Electrical conductivity of water. Provide value and unit, any unit is
  valid.
title: conductivity
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: conduc
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>