

# Slot: construct component (construct_component) 


_Select the construct component type._





URI: [basalt_schema:construct_component](https://emsl-computing.github.io/BASALT-Schema/elements/construct_component)
Alias: construct_component

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConstructComponentEnum](ConstructComponentEnum.md) |
| Domain Of | [Organism](Organism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:construct_component |
| native | basalt_schema:construct_component |




## LinkML Source

<details>
```yaml
name: construct_component
description: Select the construct component type.
title: construct component
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: construct_component
domain_of:
- organism
range: ConstructComponentEnum

```
</details>