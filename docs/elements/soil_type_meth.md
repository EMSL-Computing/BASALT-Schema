

# Slot: soil type method (soil_type_meth) 


_Reference or method used in determining soil series name or other lower-level classification_





URI: [analysis_api_schema:soil_type_meth](https://w3id.org/MONet/analysis-api-schema/soil_type_meth)
Alias: soil_type_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:soil_type_meth |
| native | analysis_api_schema:soil_type_meth |




## LinkML Source

<details>
```yaml
name: soil_type_meth
description: Reference or method used in determining soil series name or other lower-level
  classification
title: soil type method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: soil_type_meth
domain_of:
- MonetSoilSample
- SoilSample
range: string

```
</details>