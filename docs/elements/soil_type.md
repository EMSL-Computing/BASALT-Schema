

# Slot: soil type (soil_type) 


_Soil series name or other lower-level classification_





URI: [analysis_api_schema:soil_type](https://w3id.org/MONet/analysis-api-schema/soil_type)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:soil_type |
| native | analysis_api_schema:soil_type |




## LinkML Source

<details>
```yaml
name: soil_type
description: Soil series name or other lower-level classification
title: soil type
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: soil_type
domain_of:
- MonetSoilSample
- SoilSample
range: SoilTypeEnum

```
</details>