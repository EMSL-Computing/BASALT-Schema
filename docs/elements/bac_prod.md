

# Slot: bacterial production (bac_prod) 


_Bacterial production in the water column measured by isotope uptake. Provide value and unit, any unit is valid._





URI: [basalt_schema:bac_prod](https://EMSL-Computing.github.io/basalt-schema/bac_prod)
Alias: bac_prod

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:bac_prod |
| native | basalt_schema:bac_prod |




## LinkML Source

<details>
```yaml
name: bac_prod
description: Bacterial production in the water column measured by isotope uptake.
  Provide value and unit, any unit is valid.
title: bacterial production
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: bac_prod
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>