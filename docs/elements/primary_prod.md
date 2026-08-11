

# Slot: primary production (primary_prod) 


_Measurement of primary production generally measured as isotope uptake. Provide value and unit, any unit is valid._





URI: [basalt_schema:primary_prod](https://EMSL-Computing.github.io/basalt-schema/primary_prod)
Alias: primary_prod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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
| self | basalt_schema:primary_prod |
| native | basalt_schema:primary_prod |




## LinkML Source

<details>
```yaml
name: primary_prod
description: Measurement of primary production generally measured as isotope uptake.
  Provide value and unit, any unit is valid.
title: primary production
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: primary_prod
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>