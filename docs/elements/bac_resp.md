

# Slot: bacterial respiration (bac_resp) 


_Measurement of bacterial respiration in the water column. Provide value and unit,any unit is valid._





URI: [basalt_schema:bac_resp](https://EMSL-Computing.github.io/BASALT-Schema/bac_resp)
Alias: bac_resp

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
| self | basalt_schema:bac_resp |
| native | basalt_schema:bac_resp |




## LinkML Source

<details>
```yaml
name: bac_resp
description: Measurement of bacterial respiration in the water column. Provide value
  and unit,any unit is valid.
title: bacterial respiration
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: bac_resp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>