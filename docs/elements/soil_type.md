

# Slot: soil type (soil_type) 


_Soil series name or other lower-level classification_





URI: [basalt_schema:soil_type](https://emsl-computing.github.io/BASALT-Schema/elements/soil_type)
Alias: soil_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SoilTypeEnum](SoilTypeEnum.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soil_type |
| native | basalt_schema:soil_type |




## LinkML Source

<details>
```yaml
name: soil_type
description: Soil series name or other lower-level classification
title: soil type
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: soil_type
domain_of:
- MonetSoilSample
- SoilSample
range: SoilTypeEnum

```
</details>