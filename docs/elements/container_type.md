

# Slot: container_type 


_Physical container used for the culture (flask, tube, plate, etc.)_





URI: [analysis_api_schema:container_type](https://w3id.org/MONet/analysis-api-schema/container_type)
Alias: container_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [ContainerType](ContainerType.md) |  |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContainerType](ContainerType.md), [CultureGrowth](CultureGrowth.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:container_type |
| native | analysis_api_schema:container_type |




## LinkML Source

<details>
```yaml
name: container_type
description: Physical container used for the culture (flask, tube, plate, etc.)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: container_type
domain_of:
- ContainerType
- CultureGrowth
range: string

```
</details>