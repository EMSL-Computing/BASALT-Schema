

# Slot: non microbial biomass (non_microb_biomass) 


_Amount of biomass; should include the name for the part of biomass measured, e.g.insect, plant, total. Can include multiple measurements separated by ;_





URI: [analysis_api_schema:non_microb_biomass](https://w3id.org/MONet/analysis-api-schema/non_microb_biomass)
Alias: non_microb_biomass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:non_microb_biomass |
| native | analysis_api_schema:non_microb_biomass |




## LinkML Source

<details>
```yaml
name: non_microb_biomass
description: Amount of biomass; should include the name for the part of biomass measured,
  e.g.insect, plant, total. Can include multiple measurements separated by ;
title: non microbial biomass
from_schema: https://w3id.org/MONet/analysis-api-schema
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