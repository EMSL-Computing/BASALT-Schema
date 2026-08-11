

# Slot: genotype segment name (genotype_segment_name) 


_Provide a name that describes the genotype modification engineered_

_relative to the reference unmodified genome. The name should describe the spatially_

_grouped components or specific function of the modification._





URI: [basalt_schema:genotype_segment_name](https://EMSL-Computing.github.io/basalt-schema/genotype_segment_name)
Alias: genotype_segment_name

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:genotype_segment_name |
| native | basalt_schema:genotype_segment_name |




## LinkML Source

<details>
```yaml
name: genotype_segment_name
description: 'Provide a name that describes the genotype modification engineered

  relative to the reference unmodified genome. The name should describe the spatially

  grouped components or specific function of the modification.'
title: genotype segment name
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: genotype_segment_name
domain_of:
- organism
range: string

```
</details>