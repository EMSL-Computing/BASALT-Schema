

# Slot: pH regimen (ph_regm) 


_Information about treatment involving exposure of plants to varying levels of pH of the growth media, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimen_





URI: [basalt_schema:ph_regm](https://EMSL-Computing.github.io/basalt-schema/ph_regm)
Alias: ph_regm

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ph_regm |
| native | basalt_schema:ph_regm |




## LinkML Source

<details>
```yaml
name: ph_regm
description: Information about treatment involving exposure of plants to varying levels
  of pH of the growth media, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple regimen
title: pH regimen
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: ph_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>