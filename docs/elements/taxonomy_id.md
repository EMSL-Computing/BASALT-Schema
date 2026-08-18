

# Slot: taxonomy_id 


_NCBI taxon ID for the organism._





URI: [basalt_schema:taxonomy_id](https://emsl-computing.github.io/BASALT-Schema/elements/taxonomy_id)
Alias: taxonomy_id

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


* ncbi_taxon_id
* taxon_id




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:taxonomy_id |
| native | basalt_schema:taxonomy_id |




## LinkML Source

<details>
```yaml
name: taxonomy_id
description: NCBI taxon ID for the organism.
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- ncbi_taxon_id
- taxon_id
rank: 1000
alias: taxonomy_id
domain_of:
- organism
range: string

```
</details>