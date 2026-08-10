

# Slot: donor organism (donor_organism) 


_Provide the scientific name (genus and species) of the organism from which the construct component was first described or obtained. _

_You may enter 'synthetic' if relevant._





URI: [basalt_schema:donor_organism](https://w3id.org/MONet/basalt-schema/donor_organism)
Alias: donor_organism

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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:donor_organism |
| native | basalt_schema:donor_organism |




## LinkML Source

<details>
```yaml
name: donor_organism
description: "Provide the scientific name (genus and species) of the organism from\
  \ which the construct component was first described or obtained. \nYou may enter\
  \ 'synthetic' if relevant."
title: donor organism
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: donor_organism
domain_of:
- organism
range: string

```
</details>