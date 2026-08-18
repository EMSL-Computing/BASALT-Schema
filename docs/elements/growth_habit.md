

# Slot: growth habit (growth_habit) 


_Characteristic shape appearance or growth form of a plant species_





URI: [basalt_schema:growth_habit](https://EMSL-Computing.github.io/BASALT-Schema/growth_habit)
Alias: growth_habit

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
| Range | [GrowthHabitEnum](GrowthHabitEnum.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:growth_habit |
| native | basalt_schema:growth_habit |




## LinkML Source

<details>
```yaml
name: growth_habit
description: Characteristic shape appearance or growth form of a plant species
title: growth habit
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: growth_habit
domain_of:
- OtherUndescribedSample
- PlantSample
range: GrowthHabitEnum

```
</details>