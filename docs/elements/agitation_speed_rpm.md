

# Slot: agitation_speed_rpm 


_Agitation/shaking speed in RPM (0 for static)_





URI: [basalt_schema:agitation_speed_rpm](https://w3id.org/MONet/basalt-schema/agitation_speed_rpm)
Alias: agitation_speed_rpm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [HasIncubationConditions](HasIncubationConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:agitation_speed_rpm |
| native | basalt_schema:agitation_speed_rpm |




## LinkML Source

<details>
```yaml
name: agitation_speed_rpm
description: Agitation/shaking speed in RPM (0 for static)
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: agitation_speed_rpm
domain_of:
- HasIncubationConditions
range: integer

```
</details>