

# Slot: modification method (modification_method) 


_Select the method used to insert your construct into the genome of_

_your modified organism. Examples: "Electroporation", "Conjugation", "CRISPR", "Transduction"_





URI: [basalt_schema:modification_method](https://emsl-computing.github.io/BASALT-Schema/elements/modification_method)
Alias: modification_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ModificationMethodEnum](ModificationMethodEnum.md) |
| Domain Of | [Organism](Organism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* genetic_modification_method
* transformation_method




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:modification_method |
| native | basalt_schema:modification_method |




## LinkML Source

<details>
```yaml
name: modification_method
description: 'Select the method used to insert your construct into the genome of

  your modified organism. Examples: "Electroporation", "Conjugation", "CRISPR", "Transduction"'
title: modification method
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- genetic_modification_method
- transformation_method
rank: 1000
alias: modification_method
domain_of:
- organism
range: ModificationMethodEnum

```
</details>