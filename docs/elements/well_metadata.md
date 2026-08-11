

# Slot: well_metadata 


_Structured per-well metadata array. Format varies by activity subclass:_

_  AMP2:     AMP2WellMetadata instances (position, volumes, replicate_group)_

_  Ecoplate: EcoplateWellMetadata instances (position, carbon_source, treatment, volumes)_





URI: [basalt_schema:well_metadata](https://EMSL-Computing.github.io/basalt-schema/well_metadata)
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:well_metadata |
| native | basalt_schema:well_metadata |




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
from_schema: https://EMSL-Computing.github.io/basalt-schema
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