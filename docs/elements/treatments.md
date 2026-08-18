

# Slot: treatments 


_Per-well treatments if applicable (e.g. different mineral concentrations)._

_NULL for uniform-treatment plates._





URI: [basalt_schema:treatments](https://emsl-computing.github.io/BASALT-Schema/elements/treatments)
Alias: treatments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2WellMetadata](AMP2WellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AMP2WellMetadata](AMP2WellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:treatments |
| native | basalt_schema:treatments |




## LinkML Source

<details>
```yaml
name: treatments
description: 'Per-well treatments if applicable (e.g. different mineral concentrations).

  NULL for uniform-treatment plates.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: treatments
owner: AMP2WellMetadata
domain_of:
- AMP2WellMetadata
range: string
multivalued: true

```
</details>