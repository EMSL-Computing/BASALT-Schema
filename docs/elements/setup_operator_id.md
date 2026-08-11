

# Slot: setup_operator_id 


_Person who set up the plate_





URI: [basalt_schema:setup_operator_id](https://EMSL-Computing.github.io/basalt-schema/setup_operator_id)
Alias: setup_operator_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonValue](PersonValue.md) |
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
| self | basalt_schema:setup_operator_id |
| native | basalt_schema:setup_operator_id |




## LinkML Source

<details>
```yaml
name: setup_operator_id
description: Person who set up the plate
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: setup_operator_id
domain_of:
- PlateSetupActivity
range: PersonValue

```
</details>