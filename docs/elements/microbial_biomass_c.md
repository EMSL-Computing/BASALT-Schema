

# Slot: microbial biomass carbon (microbial_biomass_c) 


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer. If you keep this, you would need to have correction factors used for conversion to the final units. Provide value and unit, any unit is valid_





URI: [basalt_schema:microbial_biomass_c](https://emsl-computing.github.io/BASALT-Schema/elements/microbial_biomass_c)
Alias: microbial_biomass_c

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md) |

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
| self | basalt_schema:microbial_biomass_c |
| native | basalt_schema:microbial_biomass_c |




## LinkML Source

<details>
```yaml
name: microbial_biomass_c
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer. If you keep this, you would need to have correction
  factors used for conversion to the final units. Provide value and unit, any unit
  is valid
title: microbial biomass carbon
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: microbial_biomass_c
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>