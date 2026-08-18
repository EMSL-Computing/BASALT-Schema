

# Slot: well_type 


_Role of this well   "sample", "blank", "uninoculated_control", "standard"_





URI: [basalt_schema:well_type](https://emsl-computing.github.io/BASALT-Schema/elements/well_type)
Alias: well_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WellMetadata](WellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WellMetadata](WellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:well_type |
| native | basalt_schema:well_type |




## LinkML Source

<details>
```yaml
name: well_type
description: Role of this well   "sample", "blank", "uninoculated_control", "standard"
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: well_type
owner: WellMetadata
domain_of:
- WellMetadata
range: string

```
</details>