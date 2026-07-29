

# Slot: position 


_Motor position value at scan start_





URI: [analysis_api_schema:position](https://w3id.org/MONet/analysis-api-schema/position)
Alias: position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |
| [XASMotorPosition](XASMotorPosition.md) | Motor position recorded at the start of an XAS sweep |  no  |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:position |
| native | analysis_api_schema:position |




## LinkML Source

<details>
```yaml
name: position
description: Motor position value at scan start
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: position
domain_of:
- WellMetadata
- WellReading
- XASMotorPosition
range: float

```
</details>