

# Slot: sealing_method 


_How the plate is sealed (e.g. "BreathEasy_membrane", "adhesive_film")_





URI: [basalt_schema:sealing_method](https://EMSL-Computing.github.io/basalt-schema/sealing_method)
Alias: sealing_method

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
| self | basalt_schema:sealing_method |
| native | basalt_schema:sealing_method |




## LinkML Source

<details>
```yaml
name: sealing_method
description: How the plate is sealed (e.g. "BreathEasy_membrane", "adhesive_film")
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: sealing_method
domain_of:
- PlateSetupActivity
range: string

```
</details>