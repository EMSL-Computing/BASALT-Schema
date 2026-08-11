

# Slot: strain source (strain_source) 


_Indicate the source of the strain provided (e.g. "PNNL", "ATCC"). If purchased provide the_

_vendor and lot number if from another registered or known strain provide a reference._





URI: [basalt_schema:strain_source](https://EMSL-Computing.github.io/basalt-schema/strain_source)
Alias: strain_source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  yes  |






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


* source_institution
* strain_origin




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:strain_source |
| native | basalt_schema:strain_source |




## LinkML Source

<details>
```yaml
name: strain_source
description: 'Indicate the source of the strain provided (e.g. "PNNL", "ATCC"). If
  purchased provide the

  vendor and lot number if from another registered or known strain provide a reference.'
title: strain source
from_schema: https://EMSL-Computing.github.io/basalt-schema
aliases:
- source_institution
- strain_origin
rank: 1000
alias: strain_source
domain_of:
- organism
range: string

```
</details>