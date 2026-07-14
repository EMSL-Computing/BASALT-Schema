

# Slot: non microbial biomass method (non_microb_biomass_method) 


_Reference or method used in determining biomass_





URI: [analysis_api_schema:non_microb_biomass_method](https://w3id.org/MONet/analysis-api-schema/non_microb_biomass_method)
Alias: non_microb_biomass_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:non_microb_biomass_method |
| native | analysis_api_schema:non_microb_biomass_method |




## LinkML Source

<details>
```yaml
name: non_microb_biomass_method
description: Reference or method used in determining biomass
title: non microbial biomass method
from_schema: https://w3id.org/MONet/analysis-api-schema
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