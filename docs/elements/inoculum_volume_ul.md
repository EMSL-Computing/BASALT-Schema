

# Slot: inoculum_volume_ul 


_Volume of inoculum added (0 for blanks)_





URI: [basalt_schema:inoculum_volume_ul](https://EMSL-Computing.github.io/basalt-schema/inoculum_volume_ul)
Alias: inoculum_volume_ul

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [AMP2WellMetadata](AMP2WellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AMP2WellMetadata](AMP2WellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:inoculum_volume_ul |
| native | basalt_schema:inoculum_volume_ul |




## LinkML Source

<details>
```yaml
name: inoculum_volume_ul
description: Volume of inoculum added (0 for blanks)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: inoculum_volume_ul
owner: AMP2WellMetadata
domain_of:
- AMP2WellMetadata
range: float
required: true

```
</details>