

# Slot: trait 


_Trait category for the organism._

_Example: "Bacterial Resistance", "Other"_





URI: [basalt_schema:trait](https://EMSL-Computing.github.io/BASALT-Schema/trait)
Alias: trait

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IntendedTraitEnum](IntendedTraitEnum.md) |
| Domain Of | [Organism](Organism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:trait |
| native | basalt_schema:trait |




## LinkML Source

<details>
```yaml
name: trait
description: 'Trait category for the organism.

  Example: "Bacterial Resistance", "Other"'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: trait
domain_of:
- organism
range: IntendedTraitEnum

```
</details>