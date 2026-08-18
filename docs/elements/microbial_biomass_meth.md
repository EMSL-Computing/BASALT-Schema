

# Slot: microbial biomass method (microbial_biomass_meth) 


_Reference or method used in determining microbial biomass_





URI: [basalt_schema:microbial_biomass_meth](https://emsl-computing.github.io/BASALT-Schema/elements/microbial_biomass_meth)
Alias: microbial_biomass_meth

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:microbial_biomass_meth |
| native | basalt_schema:microbial_biomass_meth |




## LinkML Source

<details>
```yaml
name: microbial_biomass_meth
description: Reference or method used in determining microbial biomass
title: microbial biomass method
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: microbial_biomass_meth
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string

```
</details>