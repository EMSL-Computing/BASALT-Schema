

# Slot: plant dry mass (plant_dry_mass) 


_Measurement of dry mass. (Unit: kg or g)_





URI: [analysis_api_schema:plant_dry_mass](https://w3id.org/MONet/analysis-api-schema/plant_dry_mass)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plant_dry_mass |
| native | analysis_api_schema:plant_dry_mass |




## LinkML Source

<details>
```yaml
name: plant_dry_mass
description: 'Measurement of dry mass. (Unit: kg or g)'
title: plant dry mass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plant_dry_mass
domain_of:
- PlantSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>