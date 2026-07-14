

# Slot: microbial biomass (microbial_biomass) 


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer. If you keep this, you would need to have correction factors used for conversion to the final units_





URI: [analysis_api_schema:microbial_biomass](https://w3id.org/MONet/analysis-api-schema/microbial_biomass)
Alias: microbial_biomass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:microbial_biomass |
| native | analysis_api_schema:microbial_biomass |




## LinkML Source

<details>
```yaml
name: microbial_biomass
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer. If you keep this, you would need to have correction
  factors used for conversion to the final units
title: microbial biomass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: microbial_biomass
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string

```
</details>