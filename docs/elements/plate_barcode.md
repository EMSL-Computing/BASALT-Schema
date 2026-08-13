

# Slot: plate_barcode 


_Physical barcode on plate (if different from UUID)_





URI: [basalt_schema:plate_barcode](https://EMSL-Computing.github.io/basalt-schema/plate_barcode)
Alias: plate_barcode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlateSetupActivity](PlateSetupActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plate_barcode |
| native | basalt_schema:plate_barcode |




## LinkML Source

<details>
```yaml
name: plate_barcode
description: Physical barcode on plate (if different from UUID)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: plate_barcode
domain_of:
- PlateSetupActivity
range: string

```
</details>