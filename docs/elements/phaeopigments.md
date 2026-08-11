

# Slot: phaeopigments (phaeopigments) 


_Concentration of phaeopigments; can include multiple phaeopigments separated by a `;` (Unit: mg/cm3)_





URI: [basalt_schema:phaeopigments](https://EMSL-Computing.github.io/basalt-schema/phaeopigments)
Alias: phaeopigments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*mg/cm3(;\s*\d+(\.\d+)?\s*mg/cm3)*$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:phaeopigments |
| native | basalt_schema:phaeopigments |




## LinkML Source

<details>
```yaml
name: phaeopigments
description: 'Concentration of phaeopigments; can include multiple phaeopigments separated
  by a `;` (Unit: mg/cm3)'
title: phaeopigments
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: phaeopigments
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mg/cm3(;\s*\d+(\.\d+)?\s*mg/cm3)*$

```
</details>