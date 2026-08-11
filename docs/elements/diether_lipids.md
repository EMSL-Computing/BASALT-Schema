

# Slot: diether lipids (diether_lipids) 


_Concentration of diether lipids; can include multiple types of diether lipids (Unit: ng/L)_





URI: [basalt_schema:diether_lipids](https://EMSL-Computing.github.io/basalt-schema/diether_lipids)
Alias: diether_lipids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
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
| Regex Pattern | `^\d+(\.\d+)?\s*ng/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diether_lipids |
| native | basalt_schema:diether_lipids |




## LinkML Source

<details>
```yaml
name: diether_lipids
description: 'Concentration of diether lipids; can include multiple types of diether
  lipids (Unit: ng/L)'
title: diether lipids
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: diether_lipids
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ng/L$

```
</details>