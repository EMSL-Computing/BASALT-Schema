

# Slot: plant wet mass (plant_wet_mass) 


_Measurement of wet mass. (Unit: kg or g)_





URI: [analysis_api_schema:plant_wet_mass](https://w3id.org/MONet/analysis-api-schema/plant_wet_mass)
Alias: plant_wet_mass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(kg|g)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plant_wet_mass |
| native | analysis_api_schema:plant_wet_mass |




## LinkML Source

<details>
```yaml
name: plant_wet_mass
description: 'Measurement of wet mass. (Unit: kg or g)'
title: plant wet mass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plant_wet_mass
domain_of:
- PlantSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>