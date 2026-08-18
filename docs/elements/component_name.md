

# Slot: construct component name (component_name) 


_Provide a one-to-three word name based on the component. If using an_

_acronym provide the full component name in the component description._





URI: [basalt_schema:component_name](https://emsl-computing.github.io/BASALT-Schema/elements/component_name)
Alias: component_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | basalt_schema:component_name |
| native | basalt_schema:component_name |




## LinkML Source

<details>
```yaml
name: component_name
description: 'Provide a one-to-three word name based on the component. If using an

  acronym provide the full component name in the component description.'
title: construct component name
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: component_name
domain_of:
- organism
range: string

```
</details>