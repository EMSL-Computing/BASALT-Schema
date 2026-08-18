

# Slot: temperature_celsius 


_Temperature at which the method/process/activity was performed_





URI: [basalt_schema:temperature_celsius](https://emsl-computing.github.io/BASALT-Schema/elements/temperature_celsius)
Alias: temperature_celsius

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md), [HasIncubationConditions](HasIncubationConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:temperature_celsius |
| native | basalt_schema:temperature_celsius |




## LinkML Source

<details>
```yaml
name: temperature_celsius
description: Temperature at which the method/process/activity was performed
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: temperature_celsius
domain_of:
- ChromatographyConfiguration
- HasIncubationConditions
range: float

```
</details>