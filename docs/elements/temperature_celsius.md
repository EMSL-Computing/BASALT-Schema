

# Slot: temperature_celsius 


_Temperature at which the method/process/activity was performed_





URI: [analysis_api_schema:temperature_celsius](https://w3id.org/MONet/analysis-api-schema/temperature_celsius)
Alias: temperature_celsius

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:temperature_celsius |
| native | analysis_api_schema:temperature_celsius |




## LinkML Source

<details>
```yaml
name: temperature_celsius
description: Temperature at which the method/process/activity was performed
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: temperature_celsius
domain_of:
- ChromatographyConfiguration
- HasIncubationConditions
range: float

```
</details>