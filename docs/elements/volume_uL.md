

# Slot: volume_uL 


_Volume of the entity in microliters_





URI: [basalt_schema:volume_uL](https://EMSL-Computing.github.io/basalt-schema/volume_uL)
Alias: volume_uL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:volume_uL |
| native | basalt_schema:volume_uL |




## LinkML Source

<details>
```yaml
name: volume_uL
description: Volume of the entity in microliters
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: volume_uL
domain_of:
- ProcessedSample
range: float

```
</details>