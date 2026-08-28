

# Slot: carbon_source 


_Carbon source in this well (e.g. "L-malic acid", "glucose")_





URI: [basalt_schema:carbon_source](https://emsl-computing.github.io/BASALT-Schema/elements/carbon_source)
Alias: carbon_source

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
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EcoplateWellMetadata](EcoplateWellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:carbon_source |
| native | basalt_schema:carbon_source |




## LinkML Source

<details>
```yaml
name: carbon_source
description: Carbon source in this well (e.g. "L-malic acid", "glucose")
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: carbon_source
owner: EcoplateWellMetadata
domain_of:
- EcoplateWellMetadata
range: string
required: true

```
</details>