

# Slot: agitation_speed_rpm 


_Agitation/shaking speed in RPM (0 for static)_





URI: [basalt_schema:agitation_speed_rpm](https://emsl-computing.github.io/BASALT-Schema/elements/agitation_speed_rpm)
Alias: agitation_speed_rpm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




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
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: agitation_speed_rpm
domain_of:
- HasIncubationConditions
range: integer

```
</details>