

# Slot: non microbial biomass (non_microb_biomass) 


_Amount of biomass; should include the name for the part of biomass measured, e.g.insect, plant, total. Can include multiple measurements separated by ;_





URI: [basalt_schema:non_microb_biomass](https://emsl-computing.github.io/BASALT-Schema/elements/non_microb_biomass)
Alias: non_microb_biomass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:non_microb_biomass |
| native | basalt_schema:non_microb_biomass |




## LinkML Source

<details>
```yaml
name: non_microb_biomass
description: Amount of biomass; should include the name for the part of biomass measured,
  e.g.insect, plant, total. Can include multiple measurements separated by ;
title: non microbial biomass
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: non_microb_biomass
domain_of:
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>