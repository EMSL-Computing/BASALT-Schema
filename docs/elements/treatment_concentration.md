

# Slot: treatment_concentration 


_Treatment concentration with unit (e.g. "1.0 pct", "10 mM")_





URI: [basalt_schema:treatment_concentration](https://EMSL-Computing.github.io/basalt-schema/treatment_concentration)
Alias: treatment_concentration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EcoplateWellMetadata](EcoplateWellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EcoplateWellMetadata](EcoplateWellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:treatment_concentration |
| native | basalt_schema:treatment_concentration |




## LinkML Source

<details>
```yaml
name: treatment_concentration
description: Treatment concentration with unit (e.g. "1.0 pct", "10 mM")
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: treatment_concentration
owner: EcoplateWellMetadata
domain_of:
- EcoplateWellMetadata
range: string

```
</details>