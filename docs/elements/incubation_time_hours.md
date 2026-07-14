

# Slot: incubation_time_hours 


_Incubation duration in hours_





URI: [analysis_api_schema:incubation_time_hours](https://w3id.org/MONet/analysis-api-schema/incubation_time_hours)
Alias: incubation_time_hours

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:incubation_time_hours |
| native | analysis_api_schema:incubation_time_hours |




## LinkML Source

<details>
```yaml
name: incubation_time_hours
description: Incubation duration in hours
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: incubation_time_hours
domain_of:
- CultureGrowth
range: float

```
</details>