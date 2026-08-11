

# Slot: strain_type 


_Type of strain/organism (bacterial, fungal, archaeal, etc.)_





URI: [basalt_schema:strain_type](https://EMSL-Computing.github.io/basalt-schema/strain_type)
Alias: strain_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StrainTypeEnum](StrainTypeEnum.md) |
| Domain Of | [Organism](Organism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* organism_type




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:strain_type |
| native | basalt_schema:strain_type |




## LinkML Source

<details>
```yaml
name: strain_type
description: Type of strain/organism (bacterial, fungal, archaeal, etc.)
from_schema: https://EMSL-Computing.github.io/basalt-schema
aliases:
- organism_type
rank: 1000
alias: strain_type
domain_of:
- organism
range: StrainTypeEnum

```
</details>