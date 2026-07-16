

# Slot: plate_type 


_Vendor and model of plate (e.g. "Greiner_96well_flat_bottom", "Biolog_EcoPlate")_





URI: [analysis_api_schema:plate_type](https://w3id.org/MONet/analysis-api-schema/plate_type)
Alias: plate_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plate_type |
| native | analysis_api_schema:plate_type |




## LinkML Source

<details>
```yaml
name: plate_type
description: Vendor and model of plate (e.g. "Greiner_96well_flat_bottom", "Biolog_EcoPlate")
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plate_type
domain_of:
- PlateSetupActivity
range: string
required: true

```
</details>