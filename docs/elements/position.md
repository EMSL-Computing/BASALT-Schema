

# Slot: position 



URI: [basalt_schema:position](https://emsl-computing.github.io/BASALT-Schema/elements/position)
Alias: position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |






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
| self | basalt_schema:position |
| native | basalt_schema:position |




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