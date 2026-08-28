

# Slot: position 


_Motor position value at scan start_





URI: [basalt_schema:position](https://emsl-computing.github.io/BASALT-Schema/elements/position)
Alias: position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |
| [XASMotorPosition](XASMotorPosition.md) | Motor position recorded at the start of an XAS sweep |  no  |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [WellMetadata](WellMetadata.md), [WellReading](WellReading.md), [XASMotorPosition](XASMotorPosition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:position |
| native | basalt_schema:position |




## LinkML Source

<details>
```yaml
name: position
description: Motor position value at scan start
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: position
domain_of:
- WellMetadata
- WellReading
- XASMotorPosition
range: float

```
</details>