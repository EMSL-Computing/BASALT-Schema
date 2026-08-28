

# Slot: microbial biomass nitrogen method (micro_biomass_n_meth) 


_Reference or method used in determining microbial biomass nitrogen_





URI: [basalt_schema:micro_biomass_n_meth](https://emsl-computing.github.io/BASALT-Schema/elements/micro_biomass_n_meth)
Alias: micro_biomass_n_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






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
| self | basalt_schema:micro_biomass_n_meth |
| native | basalt_schema:micro_biomass_n_meth |




## LinkML Source

<details>
```yaml
name: micro_biomass_n_meth
description: Reference or method used in determining microbial biomass nitrogen
title: microbial biomass nitrogen method
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: micro_biomass_n_meth
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string

```
</details>