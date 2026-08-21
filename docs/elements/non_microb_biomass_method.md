

# Slot: non microbial biomass method (non_microb_biomass_method) 


_Reference or method used in determining biomass_





URI: [basalt_schema:non_microb_biomass_method](https://emsl-computing.github.io/BASALT-Schema/elements/non_microb_biomass_method)
Alias: non_microb_biomass_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:non_microb_biomass_method |
| native | basalt_schema:non_microb_biomass_method |




## LinkML Source

<details>
```yaml
name: non_microb_biomass_method
description: Reference or method used in determining biomass
title: non microbial biomass method
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: non_microb_biomass_method
domain_of:
- CultureEnvironmentalSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>