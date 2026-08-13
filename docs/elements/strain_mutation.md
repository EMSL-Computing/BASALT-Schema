

# Slot: strain_mutation 


_Primary genetic modification or plasmid carried (e.g., "pTE314")._

_For complex constructs, use genotype_segment_* and component_* slots._





URI: [basalt_schema:strain_mutation](https://EMSL-Computing.github.io/BASALT-Schema/strain_mutation)
Alias: strain_mutation

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:strain_mutation |
| native | basalt_schema:strain_mutation |




## LinkML Source

<details>
```yaml
name: strain_mutation
description: 'Primary genetic modification or plasmid carried (e.g., "pTE314").

  For complex constructs, use genotype_segment_* and component_* slots.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: strain_mutation
domain_of:
- organism
range: string

```
</details>