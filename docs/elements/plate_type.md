

# Slot: plate_type 


_Vendor and model of plate (e.g. "Greiner_96well_flat_bottom", "Biolog_EcoPlate")_





URI: [basalt_schema:plate_type](https://emsl-computing.github.io/BASALT-Schema/elements/plate_type)
Alias: plate_type

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
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plate_type |
| native | basalt_schema:plate_type |




## LinkML Source

<details>
```yaml
name: plate_type
description: Vendor and model of plate (e.g. "Greiner_96well_flat_bottom", "Biolog_EcoPlate")
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: plate_type
domain_of:
- PlateSetupActivity
range: string
required: true

```
</details>