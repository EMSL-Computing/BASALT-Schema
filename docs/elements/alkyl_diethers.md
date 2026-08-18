

# Slot: alkyl diethers (alkyl_diethers) 


_Concentration of alkyl diethers. Provide value and unit, any unit is valid_





URI: [basalt_schema:alkyl_diethers](https://emsl-computing.github.io/BASALT-Schema/elements/alkyl_diethers)
Alias: alkyl_diethers

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












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:alkyl_diethers |
| native | basalt_schema:alkyl_diethers |




## LinkML Source

<details>
```yaml
name: alkyl_diethers
description: Concentration of alkyl diethers. Provide value and unit, any unit is
  valid
title: alkyl diethers
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: alkyl_diethers
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>