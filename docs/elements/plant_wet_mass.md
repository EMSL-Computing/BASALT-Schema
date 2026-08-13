

# Slot: plant wet mass (plant_wet_mass) 


_Measurement of wet mass. (Unit: kg or g)_





URI: [basalt_schema:plant_wet_mass](https://EMSL-Computing.github.io/BASALT-Schema/plant_wet_mass)
Alias: plant_wet_mass

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
| Regex Pattern | `^\d+(\.\d+)?\s*(kg|g)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_wet_mass |
| native | basalt_schema:plant_wet_mass |




## LinkML Source

<details>
```yaml
name: plant_wet_mass
description: 'Measurement of wet mass. (Unit: kg or g)'
title: plant wet mass
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: plant_wet_mass
domain_of:
- PlantSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>