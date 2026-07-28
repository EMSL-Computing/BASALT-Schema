

# Slot: well_metadata 


_Structured per-well metadata array. Format varies by activity subclass:_

_  AMP2:     AMP2WellMetadata instances (position, volumes, replicate_group)_

_  Ecoplate: EcoplateWellMetadata instances (position, carbon_source, treatment, volumes)_





URI: [analysis_api_schema:well_metadata](https://w3id.org/MONet/analysis-api-schema/well_metadata)
Alias: well_metadata

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WellMetadata](WellMetadata.md) |
| Domain Of | [PlateSetupActivity](PlateSetupActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## TODOs

* decide how to represent in backend (normalized child table with FK to PlateSetupActivity, array column, or other)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:well_metadata |
| native | analysis_api_schema:well_metadata |




## LinkML Source

<details>
```yaml
name: well_metadata
description: "Structured per-well metadata array. Format varies by activity subclass:\n\
  \  AMP2:     AMP2WellMetadata instances (position, volumes, replicate_group)\n \
  \ Ecoplate: EcoplateWellMetadata instances (position, carbon_source, treatment,\
  \ volumes)"
todos:
- decide how to represent in backend (normalized child table with FK to PlateSetupActivity,
  array column, or other)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: well_metadata
domain_of:
- PlateSetupActivity
range: WellMetadata
multivalued: true
inlined: true
inlined_as_list: true

```
</details>