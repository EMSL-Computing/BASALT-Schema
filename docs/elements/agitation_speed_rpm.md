

# Slot: agitation_speed_rpm 



URI: [analysis_api_schema:agitation_speed_rpm](https://w3id.org/MONet/analysis-api-schema/agitation_speed_rpm)
Alias: agitation_speed_rpm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:agitation_speed_rpm |
| native | analysis_api_schema:agitation_speed_rpm |




## LinkML Source

<details>
```yaml
name: agitation_speed_rpm
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: agitation_speed_rpm
domain_of:
- HasIncubationConditions
range: integer

```
</details>