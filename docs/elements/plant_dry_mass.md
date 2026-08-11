

# Slot: plant dry mass (plant_dry_mass) 


_Measurement of dry mass. (Unit: kg or g)_





URI: [basalt_schema:plant_dry_mass](https://EMSL-Computing.github.io/basalt-schema/plant_dry_mass)
Alias: plant_dry_mass

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_dry_mass |
| native | basalt_schema:plant_dry_mass |




## LinkML Source

<details>
```yaml
name: plant_dry_mass
description: 'Measurement of dry mass. (Unit: kg or g)'
title: plant dry mass
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: plant_dry_mass
domain_of:
- PlantSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>