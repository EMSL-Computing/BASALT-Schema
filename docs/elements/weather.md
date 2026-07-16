

# Slot: weather (weather) 


_The state of the atmosphere at a given time and place with respect to variables such as temperature, moisture, wind velocity, and barometric pressure._





URI: [analysis_api_schema:weather](https://w3id.org/MONet/analysis-api-schema/weather)
Alias: weather

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [PlantSamplingActivity](PlantSamplingActivity.md), [SedimentSamplingActivity](SedimentSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:weather |
| native | analysis_api_schema:weather |




## LinkML Source

<details>
```yaml
name: weather
description: The state of the atmosphere at a given time and place with respect to
  variables such as temperature, moisture, wind velocity, and barometric pressure.
title: weather
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: weather
domain_of:
- MonetSoilSamplingActivity
- PlantSamplingActivity
- SedimentSamplingActivity
- SoilSamplingActivity
range: string

```
</details>