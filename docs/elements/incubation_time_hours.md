

# Slot: incubation_time_hours 


_Incubation duration in hours_





URI: [basalt_schema:incubation_time_hours](https://w3id.org/MONet/basalt-schema/incubation_time_hours)
Alias: incubation_time_hours

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [CultureGrowth](CultureGrowth.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:incubation_time_hours |
| native | basalt_schema:incubation_time_hours |




## LinkML Source

<details>
```yaml
name: incubation_time_hours
description: Incubation duration in hours
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: incubation_time_hours
domain_of:
- CultureGrowth
range: float

```
</details>