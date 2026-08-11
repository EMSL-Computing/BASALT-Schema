

# Slot: strain description (strain_description) 


_A brief description of the modifications that comprise this strain_





URI: [basalt_schema:strain_description](https://EMSL-Computing.github.io/basalt-schema/strain_description)
Alias: strain_description

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







## Aliases


* strain_desc
* strain_notes




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:strain_description |
| native | basalt_schema:strain_description |




## LinkML Source

<details>
```yaml
name: strain_description
description: A brief description of the modifications that comprise this strain
title: strain description
from_schema: https://EMSL-Computing.github.io/basalt-schema
aliases:
- strain_desc
- strain_notes
rank: 1000
alias: strain_description
domain_of:
- organism
range: string

```
</details>