

# Slot: water temperature regimen (water_temp_regm) 


_Information about treatment involving an exposure to water with varying degree of temperature, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_





URI: [analysis_api_schema:water_temp_regm](https://w3id.org/MONet/analysis-api-schema/water_temp_regm)
Alias: water_temp_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:water_temp_regm |
| native | analysis_api_schema:water_temp_regm |




## LinkML Source

<details>
```yaml
name: water_temp_regm
description: Information about treatment involving an exposure to water with varying
  degree of temperature, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple regimens
title: water temperature regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: water_temp_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>