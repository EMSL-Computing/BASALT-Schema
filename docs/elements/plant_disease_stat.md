

# Slot: plant disease status (plant_disease_stat) 


_List of diseases with which the plant has been diagnosed; can include multiple diagnoses._





URI: [basalt_schema:plant_disease_stat](https://EMSL-Computing.github.io/BASALT-Schema/plant_disease_stat)
Alias: plant_disease_stat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_disease_stat |
| native | basalt_schema:plant_disease_stat |




## LinkML Source

<details>
```yaml
name: plant_disease_stat
description: List of diseases with which the plant has been diagnosed; can include
  multiple diagnoses.
title: plant disease status
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: plant_disease_stat
domain_of:
- PlantSample
range: string

```
</details>