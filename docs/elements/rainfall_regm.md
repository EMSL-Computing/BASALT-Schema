

# Slot: rainfall regimen (rainfall_regm) 


_Information about treatment involving an exposure to a given amount of rainfall, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_





URI: [basalt_schema:rainfall_regm](https://emsl-computing.github.io/BASALT-Schema/elements/rainfall_regm)
Alias: rainfall_regm

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:rainfall_regm |
| native | basalt_schema:rainfall_regm |




## LinkML Source

<details>
```yaml
name: rainfall_regm
description: Information about treatment involving an exposure to a given amount of
  rainfall, treatment regimen including how many times the treatment was repeated,
  how long each treatment lasted, and the start and end time of the entire treatment;
  can include multiple regimens
title: rainfall regimen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: rainfall_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>