

# Slot: strain_identifier 


_External human-readable strain identifier (e.g. "KT2440_pTE314")._

_NOT the database UUID   that is the Strain.id attribute._





URI: [basalt_schema:strain_identifier](https://emsl-computing.github.io/BASALT-Schema/elements/strain_identifier)
Alias: strain_identifier

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
| Required | Yes |







## Aliases


* strain_id
* strain_name




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:strain_identifier |
| native | basalt_schema:strain_identifier |




## LinkML Source

<details>
```yaml
name: strain_identifier
description: 'External human-readable strain identifier (e.g. "KT2440_pTE314").

  NOT the database UUID   that is the Strain.id attribute.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- strain_id
- strain_name
rank: 1000
alias: strain_identifier
domain_of:
- organism
range: string
required: true

```
</details>