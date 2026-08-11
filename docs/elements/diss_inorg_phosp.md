

# Slot: dissolved inorganic phosphate (diss_inorg_phosp) 


_Concentration of dissolved inorganic phosphorus in the sample. Provide value and unit, any unit is valid._





URI: [basalt_schema:diss_inorg_phosp](https://EMSL-Computing.github.io/basalt-schema/diss_inorg_phosp)
Alias: diss_inorg_phosp

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
| self | basalt_schema:diss_inorg_phosp |
| native | basalt_schema:diss_inorg_phosp |




## LinkML Source

<details>
```yaml
name: diss_inorg_phosp
description: Concentration of dissolved inorganic phosphorus in the sample. Provide
  value and unit, any unit is valid.
title: dissolved inorganic phosphate
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: diss_inorg_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>