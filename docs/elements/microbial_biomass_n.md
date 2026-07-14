

# Slot: microbial biomass nitrogen (microbial_biomass_n) 


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer. If you keep this, you would need to have correction factors used for conversion to the final units. Provide value and unit, any unit is valid_





URI: [analysis_api_schema:microbial_biomass_n](https://w3id.org/MONet/analysis-api-schema/microbial_biomass_n)
Alias: microbial_biomass_n

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:microbial_biomass_n |
| native | analysis_api_schema:microbial_biomass_n |




## LinkML Source

<details>
```yaml
name: microbial_biomass_n
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer. If you keep this, you would need to have correction
  factors used for conversion to the final units. Provide value and unit, any unit
  is valid
title: microbial biomass nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: microbial_biomass_n
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>