

# Slot: container_type 


_Physical container used for the culture (flask, tube, plate, etc.)_





URI: [basalt_schema:container_type](https://EMSL-Computing.github.io/basalt-schema/container_type)
Alias: container_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ContainerType](ContainerType.md) |  |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:container_type |
| native | basalt_schema:container_type |




## LinkML Source

<details>
```yaml
name: container_type
description: Physical container used for the culture (flask, tube, plate, etc.)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: container_type
domain_of:
- ContainerType
- CultureGrowth
range: string

```
</details>