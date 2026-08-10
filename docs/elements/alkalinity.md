

# Slot: alkalinity (alkalinity) 


_The ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate (Unit: mg/L or meq/L)_





URI: [basalt_schema:alkalinity](https://w3id.org/MONet/basalt-schema/alkalinity)
Alias: alkalinity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




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
from_schema: https://w3id.org/MONet/basalt-schema
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