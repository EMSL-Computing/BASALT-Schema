

# Slot: plant age (plant_age) 


_Age of plant at the time of sampling. Must provide unit_





URI: [basalt_schema:plant_age](https://w3id.org/MONet/basalt-schema/plant_age)
Alias: plant_age

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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*\w+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_age |
| native | basalt_schema:plant_age |




## LinkML Source

<details>
```yaml
name: plant_age
description: Age of plant at the time of sampling. Must provide unit
title: plant age
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: plant_age
domain_of:
- PlantSample
range: string
pattern: ^\d+(\.\d+)?\s*\w+$

```
</details>