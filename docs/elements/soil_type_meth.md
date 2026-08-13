

# Slot: soil type method (soil_type_meth) 


_Reference or method used in determining soil series name or other lower-level classification_





URI: [basalt_schema:soil_type_meth](https://EMSL-Computing.github.io/BASALT-Schema/soil_type_meth)
Alias: soil_type_meth

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
| Range | [String](String.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soil_type_meth |
| native | basalt_schema:soil_type_meth |




## LinkML Source

<details>
```yaml
name: soil_type_meth
description: Reference or method used in determining soil series name or other lower-level
  classification
title: soil type method
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: soil_type_meth
domain_of:
- MonetSoilSample
- SoilSample
range: string

```
</details>