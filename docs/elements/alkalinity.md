

# Slot: alkalinity (alkalinity) 


_The ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate (Unit: mg/L or meq/L)_





URI: [basalt_schema:alkalinity](https://emsl-computing.github.io/BASALT-Schema/elements/alkalinity)
Alias: alkalinity

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
| Regex Pattern | `^\d+(\.\d+)?\s*(mg|meq)/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:alkalinity |
| native | basalt_schema:alkalinity |




## LinkML Source

<details>
```yaml
name: alkalinity
description: 'The ability of a solution to neutralize acids to the equivalence point
  of carbonate or bicarbonate (Unit: mg/L or meq/L)'
title: alkalinity
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: alkalinity
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg|meq)/L$

```
</details>