

# Slot: treatment 


_Experimental treatment (e.g. "control", "nickel_1pct")_





URI: [basalt_schema:treatment](https://EMSL-Computing.github.io/basalt-schema/treatment)
Alias: treatment

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
| self | basalt_schema:treatment |
| native | basalt_schema:treatment |




## LinkML Source

<details>
```yaml
name: treatment
description: Experimental treatment (e.g. "control", "nickel_1pct")
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: treatment
owner: EcoplateWellMetadata
domain_of:
- EcoplateWellMetadata
range: string

```
</details>