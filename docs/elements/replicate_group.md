

# Slot: replicate_group 


_Identifier linking technical replicates (e.g. "rep1", "rep2")_





URI: [basalt_schema:replicate_group](https://EMSL-Computing.github.io/basalt-schema/replicate_group)
Alias: replicate_group

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:replicate_group |
| native | basalt_schema:replicate_group |




## LinkML Source

<details>
```yaml
name: replicate_group
description: Identifier linking technical replicates (e.g. "rep1", "rep2")
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: replicate_group
owner: WellMetadata
domain_of:
- WellMetadata
range: string

```
</details>