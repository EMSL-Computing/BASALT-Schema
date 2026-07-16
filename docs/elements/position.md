

# Slot: position 



URI: [analysis_api_schema:position](https://w3id.org/MONet/analysis-api-schema/position)
Alias: position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WellMetadata](WellMetadata.md), [WellReading](WellReading.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:position |
| native | analysis_api_schema:position |




## LinkML Source

<details>
```yaml
name: position
alias: position
domain_of:
- WellMetadata
- WellReading
range: string

```
</details>